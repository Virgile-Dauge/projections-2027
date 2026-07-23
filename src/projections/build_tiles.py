"""Génération du PMTiles France entière : jointure des scores carte aux contours d'affichage.

Entrée : le panel ingéré (`projections.ingest.ingest`) et deux géométries
d'affichage — « Proposition de contours des bureaux de vote » (REU, Voronoï
sept. 2022, data.gouv) pour la couche `bureaux`, contours communaux Etalab pour
la couche `communes`. Rappel du glossaire (CONTEXT.md) : les contours n'ont
aucune existence officielle, la donnée est jointe par identifiants
(`codeBureauVote` / `code`), jamais par géométrie.

Le fichier de contours bureaux fait ~615 Mo : on ne le charge jamais entier en
mémoire (`_iter_features_geojson`, un parseur JSON incrémental en stdlib qui
décode une Feature à la fois). Le fichier communes (~32 Mo décompressé) est
assez petit pour être chargé entier.

Sortie : un unique fichier PMTiles à deux couches (`bureaux` haute zoom,
`communes` basse zoom pour le dézoom), chaque feature portant résultats 2024
ET données mobilisation, produit par tippecanoe (binaire externe,
non vendored — voir `--tippecanoe-bin` / variable d'environnement
`TIPPECANOE_BIN`, README du projet).
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import subprocess
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

import polars as pl

from projections.carte import BLOC_SLUG, scores_bureau, scores_commune
from projections.mobilisation import construire_donnees_mobilisation

_TAILLE_MORCEAU = 1 << 20  # 1 Mio : taille des lectures successives du flux GeoJSON.

# Couche bureaux : zooms hauts (l'échelle du quartier). Couche communes : zooms
# bas (dézoom, vue département/région). Pas de recouvrement -> un seul niveau de
# détail visible à chaque zoom, transition nette à z9. Choix documenté dans le
# README (compromis taille de fichier / lisibilité).
BUREAUX_MINZOOM = 9
BUREAUX_MAXZOOM = 14
COMMUNES_MINZOOM = 0
COMMUNES_MAXZOOM = 8


def _iter_features_geojson(chemin: Path) -> Iterator[dict]:
    """Itère les Feature d'un GeoJSON FeatureCollection sans jamais le charger entier.

    Parseur minimal en stdlib : avance dans le fichier par blocs, localise le
    tableau `"features"`, puis décode un objet Feature à la fois avec
    `json.JSONDecoder.raw_decode` sur un tampon glissant. Suffisant pour un
    FeatureCollection plat (pas de Feature imbriqué dans un autre) — la forme
    des deux sources d'affichage de ce projet.
    """
    decodeur = json.JSONDecoder()
    with chemin.open("r", encoding="utf-8") as source:
        tampon = ""
        while '"features"' not in tampon:
            morceau = source.read(_TAILLE_MORCEAU)
            if not morceau:
                raise ValueError(f"GeoJSON sans champ 'features' : {chemin}")
            tampon += morceau
        debut = tampon.index("[", tampon.index('"features"')) + 1
        tampon = tampon[debut:]

        while True:
            # Élimine espaces et virgule de séparation ; relit tant que le tampon
            # ne permet pas de trancher (vide après un feature qui finissait pile
            # au bord du bloc lu -> il faut lire plus avant de conclure à la fin).
            while True:
                tampon = tampon.lstrip()
                if tampon.startswith(","):
                    tampon = tampon[1:].lstrip()
                if tampon.startswith("]"):
                    return
                if tampon:
                    break
                morceau = source.read(_TAILLE_MORCEAU)
                if not morceau:
                    raise ValueError(f"GeoJSON tronqué (fin de fichier avant ']') : {chemin}")
                tampon += morceau
            while True:
                try:
                    objet, fin = decodeur.raw_decode(tampon)
                    break
                except json.JSONDecodeError:
                    morceau = source.read(_TAILLE_MORCEAU)
                    if not morceau:
                        raise
                    tampon += morceau
            yield objet
            tampon = tampon[fin:]


def _proprietes_score(score: dict) -> dict:
    """Sous-ensemble des colonnes de score à embarquer dans les propriétés GeoJSON."""
    return {
        "bloc_tete": score["bloc_tete"],
        **{f"pct_{slug}": round(score[f"pct_{slug}"], 1) for slug in BLOC_SLUG.values()},
        "participation": round(score["participation"], 1),
    }


@dataclass(frozen=True)
class RapportJointure:
    """Taux de jointure identifiants-résultats <-> identifiants-contours pour une couche."""

    nom_couche: str
    total_scores: int
    scores_joints: int
    total_contours: int
    contours_sans_score: int
    # Fusion mobilisation (issue #26) : None quand la couche est construite sans
    # données mobilisation (tracer bullet seul), sinon la couverture de la fusion.
    mobilisation_total: int | None = None
    mobilisation_jointes: int | None = None

    @property
    def taux_scores_joints(self) -> float:
        return self.scores_joints / self.total_scores * 100 if self.total_scores else 0.0

    def __str__(self) -> str:
        texte = (
            f"{self.nom_couche} : {self.scores_joints}/{self.total_scores} résultats joints à un "
            f"contour ({self.taux_scores_joints:.1f} %) ; {self.contours_sans_score}/{self.total_contours} "
            f"contours sans résultat correspondant."
        )
        if self.mobilisation_total is not None:
            texte += f" Mobilisation : {self.mobilisation_jointes}/{self.mobilisation_total} lignes fusionnées."
        return texte


def joindre_bureaux(
    chemin_contours: Path,
    scores: pl.DataFrame,
    sortie: Path,
    donnees_mobilisation: pl.DataFrame | None = None,
) -> RapportJointure:
    """Joint les contours REU (couche `bureaux`) aux scores par `codeBureauVote` == `id_bv`.

    Écrit un NDJSON en streaming (une ligne par Feature jointe). Les contours de
    l'étranger n'existent pas dans la source REU : les bureaux `id_bv` en `ZZ...`
    du panel sont donc naturellement absents de la carte, sans filtre explicite.

    `donnees_mobilisation` (issue #26, sortie de
    `projections.mobilisation.assembler_donnees_bureau`, jointe par `unite_id`
    == `codeBureauVote`) : ses colonnes (statut/maille, réserve, rapport de
    force) sont FUSIONNÉES dans les propriétés de la MÊME couche `bureaux` —
    jamais une seconde couche : dupliquer la géométrie double le poids des
    tuiles et pousse tippecanoe à sacrifier la couche dupliquée
    (`--drop-densest-as-needed`, constaté sur données réelles : 1 feature
    survivante par tuile z5). Un contour n'ayant QUE des données mobilisation
    (sans score descriptif) est conservé, et réciproquement.
    """
    scores_par_id = {ligne["id_bv"]: ligne for ligne in scores.iter_rows(named=True) if not ligne["id_bv"].startswith("ZZ")}
    mobilisation_par_id: dict = {}
    if donnees_mobilisation is not None:
        mobilisation_par_id = {
            ligne["unite_id"]: ligne
            for ligne in donnees_mobilisation.iter_rows(named=True)
            if not ligne["unite_id"].startswith("ZZ")
        }
    ids_scores_joints: set[str] = set()
    ids_mobilisation_joints: set[str] = set()
    total_contours = 0
    contours_sans_score = 0

    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("w", encoding="utf-8") as f:
        for feature in _iter_features_geojson(chemin_contours):
            total_contours += 1
            id_bv = feature.get("properties", {}).get("codeBureauVote")
            score = scores_par_id.get(id_bv) if id_bv else None
            ligne_mob = mobilisation_par_id.get(id_bv) if id_bv else None
            if score is None and ligne_mob is None:
                contours_sans_score += 1
                continue
            proprietes = feature.get("properties", {})
            proprietes_feature = {
                "id_bv": id_bv,
                "commune": proprietes.get("nomCommune"),
                "bureau": proprietes.get("numeroBureauVote"),
            }
            if score is not None:
                ids_scores_joints.add(id_bv)
                proprietes_feature.update(_proprietes_score(score))
            if ligne_mob is not None:
                ids_mobilisation_joints.add(id_bv)
                proprietes_feature.update(
                    {
                        "statut": ligne_mob["statut"],
                        "maille": ligne_mob["maille"],
                        **_proprietes_reserve(ligne_mob),
                        **_proprietes_rapport_force(ligne_mob),
                    }
                )
            sortie_feature = {
                "type": "Feature",
                "tippecanoe": {"layer": "bureaux", "minzoom": BUREAUX_MINZOOM, "maxzoom": BUREAUX_MAXZOOM},
                "properties": proprietes_feature,
                "geometry": feature["geometry"],
            }
            f.write(json.dumps(sortie_feature, ensure_ascii=False))
            f.write("\n")

    return RapportJointure(
        nom_couche="bureaux",
        total_scores=len(scores_par_id),
        scores_joints=len(ids_scores_joints),
        total_contours=total_contours,
        contours_sans_score=contours_sans_score,
        mobilisation_total=len(mobilisation_par_id) if donnees_mobilisation is not None else None,
        mobilisation_jointes=len(ids_mobilisation_joints) if donnees_mobilisation is not None else None,
    )


def joindre_communes(
    chemin_communes_gz: Path,
    scores: pl.DataFrame,
    sortie: Path,
    donnees_mobilisation: pl.DataFrame | None = None,
) -> RapportJointure:
    """Joint les contours communaux Etalab (couche `communes`) aux scores par `code` == `code_commune`.

    Fichier assez petit (~32 Mo décompressé) pour être chargé entier — pas de
    contrainte de streaming ici contrairement à `joindre_bureaux`.

    `donnees_mobilisation` (issue #26, sortie de
    `projections.mobilisation.assembler_donnees_commune`, jointe par
    `code_commune` == `code`) : colonnes fusionnées dans la MÊME couche
    `communes` (jamais une seconde couche — même raison que `joindre_bureaux`).
    Zoom variable PAR FEATURE selon `degrade` (ADR 0002 « Repli », dégradation
    jamais silencieuse) : une commune en repli (`degrade=True`) n'a pas de
    contour bureau fiable — son polygone commune reste visible JUSQU'AU ZOOM
    BUREAU (`BUREAUX_MAXZOOM`), là où la couche `bureaux` est vide pour elle.
    Une commune stable (`degrade=False`) s'arrête au zoom de bascule
    (`COMMUNES_MAXZOOM`), remplacée par `bureaux` au-delà. Un contour n'ayant
    QUE des données mobilisation (sans score descriptif) est conservé, et
    réciproquement.
    """
    scores_par_code = {ligne["code_commune"]: ligne for ligne in scores.iter_rows(named=True)}
    mobilisation_par_code: dict = {}
    if donnees_mobilisation is not None:
        mobilisation_par_code = {ligne["code_commune"]: ligne for ligne in donnees_mobilisation.iter_rows(named=True)}
    with gzip.open(chemin_communes_gz, "rt", encoding="utf-8") as f:
        geojson = json.load(f)
    features = geojson["features"]

    ids_scores_joints: set[str] = set()
    ids_mobilisation_joints: set[str] = set()
    contours_sans_score = 0
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("w", encoding="utf-8") as f:
        for feature in features:
            proprietes = feature.get("properties", {})
            code = proprietes.get("code")
            score = scores_par_code.get(code) if code else None
            ligne_mob = mobilisation_par_code.get(code) if code else None
            if score is None and ligne_mob is None:
                contours_sans_score += 1
                continue
            proprietes_feature = {
                "code_commune": code,
                "commune": proprietes.get("nom"),
            }
            maxzoom = COMMUNES_MAXZOOM
            if score is not None:
                ids_scores_joints.add(code)
                proprietes_feature.update(_proprietes_score(score))
            if ligne_mob is not None:
                ids_mobilisation_joints.add(code)
                degrade = bool(ligne_mob["degrade"])
                if degrade:
                    maxzoom = BUREAUX_MAXZOOM
                proprietes_feature.update(
                    {
                        "statut": ligne_mob["statut"],
                        "degrade": degrade,
                        **_proprietes_reserve(ligne_mob),
                        **_proprietes_rapport_force(ligne_mob),
                    }
                )
            sortie_feature = {
                "type": "Feature",
                "tippecanoe": {"layer": "communes", "minzoom": COMMUNES_MINZOOM, "maxzoom": maxzoom},
                "properties": proprietes_feature,
                "geometry": feature["geometry"],
            }
            f.write(json.dumps(sortie_feature, ensure_ascii=False))
            f.write("\n")

    return RapportJointure(
        nom_couche="communes",
        total_scores=len(scores_par_code),
        scores_joints=len(ids_scores_joints),
        total_contours=len(features),
        contours_sans_score=contours_sans_score,
        mobilisation_total=len(mobilisation_par_code) if donnees_mobilisation is not None else None,
        mobilisation_jointes=len(ids_mobilisation_joints) if donnees_mobilisation is not None else None,
    )


# --- Propriétés mobilisation (issue #26, ADR 0002/0003 — réserve #25 + rapport --
# --- de force projeté #5, fusionnées par IDENTIFIANTS dans les couches ci-dessus) --


# Décision mainteneur (2026-07-22, PR #33) : seule la réserve du bloc Gauche
# est diffusée sur la carte — les autres blocs restent publiés dans
# `reserve-2027.md` (la transparence méthode ne bouge pas), mais la carte
# n'outille pas la mobilisation des autres camps. Bonus : ~8 propriétés de
# moins par feature dans les tuiles.
BLOCS_RESERVE_CARTE: tuple[str, ...] = ("gauche",)


def _proprietes_reserve(ligne: dict) -> dict:
    """Colonnes réserve (`reserve_<slug>`/`quantile_reserve_<slug>`/
    `quantile_reserve_<slug>_dep`) fusionnées aux couches `bureaux`/`communes`,
    restreintes à `BLOCS_RESERVE_CARTE` (mêmes noms de colonnes en sortie de
    `projections.mobilisation.assembler_donnees_bureau`/`assembler_donnees_commune`).
    Valeur absente (unité structurellement sans estimation, cf.
    `projections.mobilisation._completer_colonnes_blocs`) -> null, jamais un
    zéro fabriqué -- une réserve n'est pas un pourcentage.

    Tranche départementale (issue #37, ADR 0005) : `quantile_reserve_<slug>_dep`
    embarquée À CÔTÉ du quantile national `quantile_reserve_<slug>`, jamais à
    sa place -- le national reste dans les tuiles (réversibilité côté client
    seul), seul le site (`site/main.js`) cesse de l'afficher.
    """
    proprietes: dict = {}
    for slug in BLOCS_RESERVE_CARTE:
        valeur = ligne.get(f"reserve_{slug}")
        proprietes[f"reserve_{slug}"] = round(valeur, 1) if valeur is not None else None
        proprietes[f"quantile_reserve_{slug}"] = ligne.get(f"quantile_reserve_{slug}")
        proprietes[f"quantile_reserve_{slug}_dep"] = ligne.get(f"quantile_reserve_{slug}_dep")
    return proprietes


def _proprietes_rapport_force(ligne: dict) -> dict:
    """Bloc en tête projeté + quantile large (cf.
    `projections.mobilisation.preparer_carte_rapport_force`). Préfixé
    `rapport_force_`/`quantile_rapport_force` pour ne pas se confondre, côté
    site, avec `bloc_tete` (résultats 2024 réels, couche descriptive)."""
    return {
        "rapport_force_bloc_tete": ligne.get("bloc_tete_projete"),
        "quantile_rapport_force": ligne.get("quantile_rapport_force"),
    }


def construire_pmtiles(
    ndjson_fichiers: list[Path], sortie: Path, tippecanoe_bin: str, tmpdir: Path | None = None
) -> None:
    """Invoque tippecanoe pour fusionner N NDJSON (un par couche) en un unique PMTiles.

    Chaque Feature porte sa propre extension `tippecanoe.layer/minzoom/maxzoom`
    (voir `joindre_bureaux`/`joindre_communes`) : un seul appel suffit, pas
    besoin de `-L` par fichier. Les données mobilisation (issue #26) sont
    FUSIONNÉES dans les couches `bureaux`/`communes` en amont — jamais des
    couches séparées, qui dupliqueraient la géométrie et se feraient sacrifier
    par `--drop-densest-as-needed` (constaté sur données réelles).
    `--drop-densest-as-needed` est un filet de sécurité pour rester sous la
    limite de taille par tuile (surtout aux zooms bas de la couche communes, où
    de nombreux petits polygones peuvent se superposer dans une même tuile)
    sans faire échouer le build.

    `--simplification=10` (défaut tippecanoe : 1) : compromis taille/fidélité
    documenté au README — mesuré sur les vraies données, ce facteur fait passer
    le PMTiles de ~320 Mo à ~240 Mo à géométrie visuellement équivalente aux
    zooms où chaque couche est affichée (la choroplèthe reste lisible, la perte
    de détail ne se voit qu'en zoomant bien au-delà de la résolution utile).

    `tmpdir` : tippecanoe écrit ses fichiers de travail dans `/tmp` par défaut
    (`--temporary-directory`) ; à surcharger si `/tmp` n'est pas inscriptible
    (environnement sandboxé, ex. `$TMPDIR`).
    """
    sortie.parent.mkdir(parents=True, exist_ok=True)
    commande = [
        tippecanoe_bin,
        "-o",
        str(sortie),
        "--force",
        "-Z0",
        "-z14",
        "--simplification=10",
        "--drop-densest-as-needed",
        "--extend-zooms-if-still-dropping",
        *[str(fichier) for fichier in ndjson_fichiers],
    ]
    if tmpdir is not None:
        tmpdir.mkdir(parents=True, exist_ok=True)
        commande.append(f"--temporary-directory={tmpdir}")
    try:
        subprocess.run(commande, check=True)
    except FileNotFoundError as erreur:
        raise RuntimeError(
            f"Binaire tippecanoe introuvable ({tippecanoe_bin!r}). Compile-le (voir README) et passe "
            "son chemin via --tippecanoe-bin ou la variable d'environnement TIPPECANOE_BIN."
        ) from erreur


RAW_DIR = Path("data/raw")
INTERIM_DIR = Path("data/interim")
TILES_DIR = Path("data/tiles")


def main() -> None:
    """Point d'entrée `uv run build-tiles`.

    Construit le PMTiles France entière : couches `bureaux`/`communes` portant
    À LA FOIS les résultats 2024 réels (tracer bullet) et les données
    mobilisation (issue #26 — réserve #25 + rapport de force projeté #5),
    fusionnées par identifiants dans les mêmes features. Le gate mécanique
    (`projections.mobilisation.construire_donnees_mobilisation`, réutilise
    `projections.backtest.verdict_carte_mobilisation` tel quel) s'exécute
    AVANT toute jointure aux contours : si le verdict est FAIL, la commande
    lève et n'écrit AUCUN fichier -- la tranche s'arrête à la préparation, pas
    de mise en ligne (cf. `docs/adr/0002-*.md`/`0003-*.md`).
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, default=INTERIM_DIR / "panel_bureau_scrutin_bloc.parquet")
    parser.add_argument(
        "--panel-avec-statut",
        type=Path,
        default=INTERIM_DIR / "panel_avec_statut.parquet",
        help="Panel réconcilié (projections.churn), pour les couches mobilisation.",
    )
    parser.add_argument("--baseline", type=Path, default=INTERIM_DIR / "baseline_unite_bloc.parquet")
    parser.add_argument(
        "--contours-bureaux", type=Path, default=RAW_DIR / "contours" / "contours-france-entiere-latest-v2.geojson"
    )
    parser.add_argument(
        "--contours-communes", type=Path, default=RAW_DIR / "communes" / "communes-100m-2026.geojson.gz"
    )
    parser.add_argument("--id-election", default="2024_legi_t1")
    parser.add_argument("--out", type=Path, default=TILES_DIR / "france.pmtiles")
    parser.add_argument("--workdir", type=Path, default=TILES_DIR)
    parser.add_argument("--tippecanoe-bin", default=os.environ.get("TIPPECANOE_BIN", "tippecanoe"))
    parser.add_argument(
        "--tippecanoe-tmpdir",
        type=Path,
        default=None,
        help="Répertoire de travail de tippecanoe si /tmp n'est pas inscriptible (sinon défaut tippecanoe).",
    )
    args = parser.parse_args()

    # Gate mécanique en premier : refuse avant même de lire les contours (~615 Mo)
    # si le verdict de publication est rouge.
    panel_avec_statut = pl.read_parquet(args.panel_avec_statut)
    baseline = pl.read_parquet(args.baseline)
    donnees_mobilisation = construire_donnees_mobilisation(panel_avec_statut, baseline)

    panel = pl.read_parquet(args.panel)
    scores_b = scores_bureau(panel, id_election=args.id_election)
    scores_c = scores_commune(panel, id_election=args.id_election)

    ndjson_bureaux = args.workdir / "bureaux.ndjson"
    ndjson_communes = args.workdir / "communes.ndjson"
    rapport_b = joindre_bureaux(
        args.contours_bureaux, scores_b, ndjson_bureaux, donnees_mobilisation=donnees_mobilisation["donnees_bureau"]
    )
    rapport_c = joindre_communes(
        args.contours_communes, scores_c, ndjson_communes, donnees_mobilisation=donnees_mobilisation["donnees_commune"]
    )
    print(rapport_b)
    print(rapport_c)

    construire_pmtiles(
        [ndjson_bureaux, ndjson_communes],
        args.out,
        args.tippecanoe_bin,
        tmpdir=args.tippecanoe_tmpdir,
    )
    taille_mo = args.out.stat().st_size / 1_048_576
    print(f"PMTiles écrit : {args.out} ({taille_mo:.1f} Mo)")


if __name__ == "__main__":
    main()

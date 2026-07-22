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
`communes` basse zoom pour le dézoom), produit par tippecanoe (binaire externe,
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

    @property
    def taux_scores_joints(self) -> float:
        return self.scores_joints / self.total_scores * 100 if self.total_scores else 0.0

    def __str__(self) -> str:
        return (
            f"{self.nom_couche} : {self.scores_joints}/{self.total_scores} résultats joints à un "
            f"contour ({self.taux_scores_joints:.1f} %) ; {self.contours_sans_score}/{self.total_contours} "
            f"contours sans résultat correspondant."
        )


def joindre_bureaux(chemin_contours: Path, scores: pl.DataFrame, sortie: Path) -> RapportJointure:
    """Joint les contours REU (couche `bureaux`) aux scores par `codeBureauVote` == `id_bv`.

    Écrit un NDJSON en streaming (une ligne par Feature jointe). Les contours de
    l'étranger n'existent pas dans la source REU : les bureaux `id_bv` en `ZZ...`
    du panel sont donc naturellement absents de la carte, sans filtre explicite.
    """
    scores_par_id = {ligne["id_bv"]: ligne for ligne in scores.iter_rows(named=True) if not ligne["id_bv"].startswith("ZZ")}
    ids_scores_joints: set[str] = set()
    total_contours = 0
    contours_sans_score = 0

    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("w", encoding="utf-8") as f:
        for feature in _iter_features_geojson(chemin_contours):
            total_contours += 1
            id_bv = feature.get("properties", {}).get("codeBureauVote")
            score = scores_par_id.get(id_bv) if id_bv else None
            if score is None:
                contours_sans_score += 1
                continue
            ids_scores_joints.add(id_bv)
            proprietes = feature.get("properties", {})
            sortie_feature = {
                "type": "Feature",
                "tippecanoe": {"layer": "bureaux", "minzoom": BUREAUX_MINZOOM, "maxzoom": BUREAUX_MAXZOOM},
                "properties": {
                    "id_bv": id_bv,
                    "commune": proprietes.get("nomCommune"),
                    "bureau": proprietes.get("numeroBureauVote"),
                    **_proprietes_score(score),
                },
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
    )


def joindre_communes(chemin_communes_gz: Path, scores: pl.DataFrame, sortie: Path) -> RapportJointure:
    """Joint les contours communaux Etalab (couche `communes`) aux scores par `code` == `code_commune`.

    Fichier assez petit (~32 Mo décompressé) pour être chargé entier — pas de
    contrainte de streaming ici contrairement à `joindre_bureaux`.
    """
    scores_par_code = {ligne["code_commune"]: ligne for ligne in scores.iter_rows(named=True)}
    with gzip.open(chemin_communes_gz, "rt", encoding="utf-8") as f:
        geojson = json.load(f)
    features = geojson["features"]

    ids_scores_joints: set[str] = set()
    contours_sans_score = 0
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("w", encoding="utf-8") as f:
        for feature in features:
            proprietes = feature.get("properties", {})
            code = proprietes.get("code")
            score = scores_par_code.get(code) if code else None
            if score is None:
                contours_sans_score += 1
                continue
            ids_scores_joints.add(code)
            sortie_feature = {
                "type": "Feature",
                "tippecanoe": {"layer": "communes", "minzoom": COMMUNES_MINZOOM, "maxzoom": COMMUNES_MAXZOOM},
                "properties": {
                    "code_commune": code,
                    "commune": proprietes.get("nom"),
                    **_proprietes_score(score),
                },
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
    )


def construire_pmtiles(
    ndjson_bureaux: Path, ndjson_communes: Path, sortie: Path, tippecanoe_bin: str, tmpdir: Path | None = None
) -> None:
    """Invoque tippecanoe pour fusionner les deux NDJSON en un unique PMTiles.

    Chaque Feature porte sa propre extension `tippecanoe.layer/minzoom/maxzoom`
    (voir `joindre_bureaux`/`joindre_communes`) : un seul appel suffit, pas besoin
    de `-L` par fichier. `--drop-densest-as-needed` est un filet de sécurité pour
    rester sous la limite de taille par tuile (surtout aux zooms bas de la
    couche communes, où de nombreux petits polygones peuvent se superposer dans
    une même tuile) sans faire échouer le build.

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
        str(ndjson_bureaux),
        str(ndjson_communes),
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
    """Point d'entrée `uv run build-tiles`."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, default=INTERIM_DIR / "panel_bureau_scrutin_bloc.parquet")
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

    panel = pl.read_parquet(args.panel)
    scores_b = scores_bureau(panel, id_election=args.id_election)
    scores_c = scores_commune(panel, id_election=args.id_election)

    ndjson_bureaux = args.workdir / "bureaux.ndjson"
    ndjson_communes = args.workdir / "communes.ndjson"
    rapport_b = joindre_bureaux(args.contours_bureaux, scores_b, ndjson_bureaux)
    rapport_c = joindre_communes(args.contours_communes, scores_c, ndjson_communes)
    print(rapport_b)
    print(rapport_c)

    construire_pmtiles(ndjson_bureaux, ndjson_communes, args.out, args.tippecanoe_bin, tmpdir=args.tippecanoe_tmpdir)
    taille_mo = args.out.stat().st_size / 1_048_576
    print(f"PMTiles écrit : {args.out} ({taille_mo:.1f} Mo)")


if __name__ == "__main__":
    main()

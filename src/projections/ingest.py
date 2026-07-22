"""Ingestion des 4 scrutins sources vers une table longue bureau × scrutin × bloc.

Source : `data/raw/elections/general_results.parquet` et `candidats_results.parquet`
(jeu agrégé data.gouv.fr, format modifié en janvier 2026 — voir le manifeste dans
`projections.datasets`). Ce Parquet est déjà en format long et typé (pas de
colonnes wide par candidat, pas de nombres à la française du type `"12,5%"`) :
les pièges classiques de l'héritage 2024 (`docs/heritage-2024.md`) concernent les
CSV bruts du ministère, pas cette source-ci. Les garde-fous qui s'appliquent
malgré tout : agrégation toujours par les voix (jamais de moyenne de ratio), clé
`id_bv`, aucun bureau perdu silencieusement.

Faits vérifiés sur les vrais fichiers (juillet 2026, cf. `pl.scan_parquet` en
exploration) et documentés ici faute d'autre endroit où les figer :

- `code_commune` fait toujours 5 caractères : communes de métropole/Corse à
  5 chiffres, DOM en `971xx`..`976xx` (bien que leur `code_departement` soit
  lettré, `ZA` pour la Guadeloupe par ex.), bureaux de l'étranger en `ZZnnn`.
- `code_bv` fait toujours 4 chiffres avec zéros de tête (`"0001"`, `"0117"`...).
  `id_bv` = `code_commune + "_" + code_bv` est donc une simple concaténation,
  sans complètement à faire.
- La colonne `nuance` de `candidats_results` est **entièrement vide** pour
  `2022_pres_t1`/`2022_pres_t2` : les candidats à la présidentielle ne reçoivent
  pas de nuance préfectorale (contrairement aux législatives/européennes). Le
  mapping se fait alors par nom de candidat, cf. `CANDIDAT_PRESIDENTIELLE_VERS_NUANCE`.
- Les législatives 2022 utilisent des codes de nuance différents de ceux
  documentés dans `docs/classification_en_blocs.md` (qui documente la
  nomenclature 2024) : `NUP` (Nouvelle Union Populaire / NUPES) là où 2024 a
  `UG`, `DXG`/`DXD` (divers extrême gauche/droite) là où 2024 a `EXG`/`EXD`.
- Les européennes utilisent des nuances de liste préfixées `L` (`LRN`, `LFI`...)
  qui recouvrent exactement les mêmes 14 familles politiques.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable
from pathlib import Path

import polars as pl

# Les 7 identifiants de scrutin couvrant les 4 scrutins sources : présidentielle
# 2022 (T1/T2), législatives 2022 (T1/T2), législatives 2024 (T1/T2), européennes
# 2024. `id_election` suit le format `<année>_<type>_t<tour>`.
SCRUTINS_SOURCES: tuple[str, ...] = (
    "2022_pres_t1",
    "2022_pres_t2",
    "2022_legi_t1",
    "2022_legi_t2",
    "2024_euro_t1",
    "2024_legi_t1",
    "2024_legi_t2",
)

COLONNES_GENERAL_REQUISES: tuple[str, ...] = (
    "id_election",
    "code_departement",
    "code_commune",
    "code_bv",
    "inscrits",
    "abstentions",
    "votants",
    "blancs",
    "nuls",
    "exprimes",
)

COLONNES_CANDIDATS_REQUISES: tuple[str, ...] = (
    "id_election",
    "code_commune",
    "code_bv",
    "voix",
    "nuance",
    "nom",
)

# Mapping nuance -> bloc, selon docs/classification_en_blocs.md. NE JAMAIS utiliser
# la colonne `bloc` de data/raw/elections/nuances-2026.csv : elle classe FI en EXG
# (extrême gauche) alors que notre classification met FI en Gauche.
NUANCE_VERS_BLOC: dict[str, str] = {
    # Gauche
    "EXG": "Gauche",
    "COM": "Gauche",
    "FI": "Gauche",
    "SOC": "Gauche",
    "RDG": "Gauche",
    "VEC": "Gauche",
    "DVG": "Gauche",
    "UG": "Gauche",
    "ECO": "Gauche",
    "REG": "Gauche",
    # Centre
    "ENS": "Centre",
    "HOR": "Centre",
    "UDI": "Centre",
    "DVC": "Centre",
    # Droite
    "LR": "Droite",
    "DVD": "Droite",
    "DSV": "Droite",
    # Extrême droite
    "RN": "Extrême droite",
    "REC": "Extrême droite",
    "UXD": "Extrême droite",
    "EXD": "Extrême droite",
    # Divers (nuance inclassable, ne fait partie d'aucun bloc de clivage officiel)
    "DIV": "Divers",
    # Codes hérités des législatives 2022 (vérifiés sur le Parquet réel), absents
    # de la nomenclature 2024 documentée dans classification_en_blocs.md :
    "NUP": "Gauche",  # Nouvelle Union Populaire (NUPES 2022) -> équivalent de UG
    "DXG": "Gauche",  # Divers extrême gauche (2022) -> équivalent de EXG
    "DXD": "Extrême droite",  # Divers extrême droite (2022) -> équivalent de EXD
}

# Nuances de liste des européennes : mêmes 14 familles, préfixées "L" (vérifié
# sur le Parquet réel : 2024_euro_t1 n'emploie que ces codes-là).
NUANCE_VERS_BLOC.update(
    {
        f"L{code}": bloc
        for code, bloc in {
            "COM": "Gauche",
            "DIV": "Divers",
            "DVD": "Droite",
            "DVG": "Gauche",
            "ECO": "Gauche",
            "ENS": "Centre",
            "EXD": "Extrême droite",
            "EXG": "Gauche",
            "FI": "Gauche",
            "LR": "Droite",
            "REC": "Extrême droite",
            "RN": "Extrême droite",
            "UG": "Gauche",
            "VEC": "Gauche",
        }.items()
    }
)

# Présidentielle 2022 : nuance reconstituée depuis le nom du candidat, faute de
# nuance préfectorale dans la source (colonne `nuance` vide sur tout le Parquet
# réel pour 2022_pres_t1/t2). Correspond à la classification usuelle du ministère
# de l'Intérieur pour la présidentielle 2022 (mêmes codes que les législatives).
CANDIDAT_PRESIDENTIELLE_VERS_NUANCE: dict[str, str] = {
    "ARTHAUD": "EXG",
    "POUTOU": "EXG",
    "ROUSSEL": "COM",
    "MÉLENCHON": "FI",
    "HIDALGO": "SOC",
    "JADOT": "VEC",
    "LASSALLE": "DVC",
    "MACRON": "ENS",
    "PÉCRESSE": "LR",
    "DUPONT-AIGNAN": "DSV",
    "LE PEN": "RN",
    "ZEMMOUR": "REC",
}


def _verifier_colonnes(df: pl.DataFrame, colonnes_requises: Iterable[str], nom_table: str) -> None:
    """Garde-fou anti-dérive de schéma : échoue clairement si une colonne attendue manque."""
    manquantes = [colonne for colonne in colonnes_requises if colonne not in df.columns]
    if manquantes:
        raise ValueError(
            f"Colonnes manquantes dans {nom_table} : {manquantes}. "
            "Schéma source modifié ? (une rupture de schéma data.gouv est déjà "
            "survenue en janvier 2026, voir docs/heritage-2024.md)."
        )


def filtrer_scrutins_sources(df: pl.DataFrame) -> pl.DataFrame:
    """Ne garde que les lignes des 7 identifiants de scrutin des 4 scrutins sources."""
    return df.filter(pl.col("id_election").is_in(SCRUTINS_SOURCES))


def construire_id_bv(df: pl.DataFrame) -> pl.DataFrame:
    """Ajoute `id_bv` = code_commune (5 caractères) + "_" + code_bv.

    Lève une erreur explicite si `code_commune` n'est pas partout sur 5 caractères
    (le format observé sur le Parquet réel — voir docstring du module) : mieux
    vaut échouer que produire un id_bv non conforme au glossaire silencieusement.
    """
    non_conformes = df.filter(pl.col("code_commune").str.len_chars() != 5)
    if non_conformes.height:
        valeurs = non_conformes.get_column("code_commune").unique().to_list()
        raise ValueError(f"code_commune non conforme (attendu 5 caractères) : {sorted(valeurs)[:10]}")
    return df.with_columns((pl.col("code_commune") + "_" + pl.col("code_bv")).alias("id_bv"))


def resoudre_nuance_presidentielle(df: pl.DataFrame) -> pl.DataFrame:
    """Complète `nuance` depuis le nom du candidat quand elle est absente.

    Ne concerne en pratique que la présidentielle (seule source où `nuance` est
    vide). Un nom absent de CANDIDAT_PRESIDENTIELLE_VERS_NUANCE reste tel quel :
    `nuance_vers_bloc` le signalera alors comme nuance inconnue, avec le nom du
    candidat dans le message d'erreur.
    """
    return df.with_columns(
        pl.when(pl.col("nuance").is_null())
        .then(pl.col("nom").replace(CANDIDAT_PRESIDENTIELLE_VERS_NUANCE))
        .otherwise(pl.col("nuance"))
        .alias("nuance")
    )


def nuance_vers_bloc(df: pl.DataFrame) -> pl.DataFrame:
    """Ajoute `bloc` depuis `nuance`, selon docs/classification_en_blocs.md.

    Toute nuance absente du mapping (y compris une nuance restée manquante après
    `resoudre_nuance_presidentielle`) fait échouer l'ingestion avec la liste des
    codes en cause — jamais de repli silencieux vers Divers.
    """
    connues = set(NUANCE_VERS_BLOC)
    presentes = set(df.get_column("nuance").unique().to_list())
    inconnues = sorted(str(nuance) for nuance in presentes - connues)
    if inconnues:
        raise ValueError(
            f"Nuance(s) inconnue(s), à ajouter à NUANCE_VERS_BLOC (ou à "
            f"CANDIDAT_PRESIDENTIELLE_VERS_NUANCE si ce sont des noms de "
            f"candidats à la présidentielle) : {inconnues}"
        )
    return df.with_columns(
        pl.col("nuance").replace_strict(NUANCE_VERS_BLOC, return_dtype=pl.String).alias("bloc")
    )


def agreger_par_bloc(df: pl.DataFrame) -> pl.DataFrame:
    """Agrège les voix des candidats par bureau × scrutin × bloc.

    Toujours par les voix, jamais par une moyenne de ratio (docs/heritage-2024.md) :
    la somme des voix par bloc reconstruit l'exprimé du bureau.
    """
    return (
        df.group_by(["id_election", "code_departement", "code_commune", "code_bv", "id_bv", "bloc"])
        .agg(pl.col("voix").sum())
        .sort(["id_election", "id_bv", "bloc"])
    )


def joindre_participation(candidats_bloc: pl.DataFrame, general: pl.DataFrame) -> pl.DataFrame:
    """Joint les voix par bloc aux colonnes de participation du bureau (scrutin × bureau).

    Jointure `full` sur (id_election, id_bv) : un bureau présent d'un seul côté
    n'est jamais perdu silencieusement. Sur les Parquet réels vérifiés, les deux
    tables couvrent exactement les mêmes bureaux par scrutin (aucune ligne
    orpheline), mais la jointure `full` reste le choix sûr si ça change.
    """
    participation = general.select(
        "id_election",
        "id_bv",
        "inscrits",
        "abstentions",
        "votants",
        "blancs",
        "nuls",
        "exprimes",
    )
    return candidats_bloc.join(participation, on=["id_election", "id_bv"], how="full", coalesce=True)


def ingest(general_results: pl.DataFrame, candidats_results: pl.DataFrame) -> pl.DataFrame:
    """Construit la table longue bureau × scrutin × bloc, en voix, pour les 4 scrutins sources.

    DROM et bureaux de l'étranger sont ingérés, pas filtrés : c'est à la carte de
    décider de leur affichage, pas au pipeline.

    ⚠️ Schéma long : les colonnes de participation (inscrits, abstentions, votants,
    blancs, nuls, exprimes) sont RÉPÉTÉES sur chaque ligne de bloc d'un même
    bureau × scrutin. Pour agréger la participation vers une maille supérieure,
    dédupliquer d'abord par (id_election, id_bv) — les sommer telles quelles
    compterait chaque bureau autant de fois qu'il a de blocs.
    """
    _verifier_colonnes(general_results, COLONNES_GENERAL_REQUISES, "general_results")
    _verifier_colonnes(candidats_results, COLONNES_CANDIDATS_REQUISES, "candidats_results")

    general = construire_id_bv(filtrer_scrutins_sources(general_results))

    candidats = filtrer_scrutins_sources(candidats_results)
    candidats = construire_id_bv(candidats)
    candidats = resoudre_nuance_presidentielle(candidats)
    candidats = nuance_vers_bloc(candidats)
    candidats_bloc = agreger_par_bloc(candidats)

    return joindre_participation(candidats_bloc, general)


RAW_DIR = Path("data/raw/elections")
INTERIM_DIR = Path("data/interim")


def main() -> None:
    """Point d'entrée `uv run ingest`."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--general-results", type=Path, default=RAW_DIR / "general_results.parquet"
    )
    parser.add_argument(
        "--candidats-results", type=Path, default=RAW_DIR / "candidats_results.parquet"
    )
    parser.add_argument(
        "--out", type=Path, default=INTERIM_DIR / "panel_bureau_scrutin_bloc.parquet"
    )
    args = parser.parse_args()

    general_results = pl.read_parquet(args.general_results)
    candidats_results = pl.read_parquet(args.candidats_results)
    panel = ingest(general_results, candidats_results)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    panel.write_parquet(args.out)
    print(f"panel écrit : {args.out} ({panel.height} lignes)")


if __name__ == "__main__":
    main()

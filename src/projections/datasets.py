"""Manifeste des jeux de données sources (data.gouv.fr) et téléchargement en local.

Les fichiers sont volumineux et exclus du dépôt git (voir `data/` dans .gitignore).
Cette commande les récupère dans `data/raw/`, avec reprise : un fichier déjà présent
n'est pas retéléchargé, ce qui permet de relancer la commande sans tout recommencer.
"""

from __future__ import annotations

import urllib.request
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

RAW_DIR = Path("data/raw")


@dataclass(frozen=True)
class Source:
    """Un fichier source : chemin de destination relatif sous `data/raw/`, et URL."""

    dest: str
    url: str


# Résolu et vérifié contre l'API data.gouv le 2026-07-22.
# Couvre les 4 scrutins sources (présidentielle 2022 T1/T2, législatives 2022,
# législatives 2024, européennes 2024) via le jeu agrégé « Données des élections
# agrégées », plus la table de réconciliation bureaux/adresses (REU) et les
# référentiels géographiques (IRIS, contours, communes).
MANIFEST: tuple[Source, ...] = (
    Source(
        "elections/general_results.parquet",
        "https://data-pipeline-open.s3.sbg.io.cloud.ovh.net/elections/general_results.parquet",
    ),
    Source(
        "elections/candidats_results.parquet",
        "https://data-pipeline-open.s3.sbg.io.cloud.ovh.net/elections/candidats_results.parquet",
    ),
    Source(
        "elections/nuances-2026.csv",
        "https://static.data.gouv.fr/resources/donnees-des-elections-agregees/20260324-132009/nuances.csv",
    ),
    Source(
        "elections/schema-general-results.json",
        "https://static.data.gouv.fr/resources/donnees-des-elections-agregees/20260204-102727/schema-general-results.json",
    ),
    Source(
        "elections/schema-candidats-results.json",
        "https://static.data.gouv.fr/resources/donnees-des-elections-agregees/20260204-102742/schema-candidats-results.json",
    ),
    Source(
        "reu/table-bv-reu.parquet",
        "https://static.data.gouv.fr/resources/bureaux-de-vote-et-adresses-de-leurs-electeurs/20230626-135809/table-bv-reu.parquet",
    ),
    Source(
        "reu/dictionnaire-donnees-bv.pdf",
        "https://static.data.gouv.fr/resources/bureaux-de-vote-et-adresses-de-leurs-electeurs/20230627-150505/dictionnaire-donnees-bv.pdf",
    ),
    Source(
        "reu/methodologie.pdf",
        "https://static.data.gouv.fr/resources/bureaux-de-vote-et-adresses-de-leurs-electeurs/20230627-150505/methodologie.pdf",
    ),
    Source(
        "iris/liaison-iris-bureaux-de-vote.csv",
        "https://static.data.gouv.fr/resources/liaison-iris-bureaux-de-vote-de-2024/20260329-123247/liaison-iris-bureaux-de-vote.csv",
    ),
    Source(
        "iris/rattacheuririsbureaux.txt",
        "https://static.data.gouv.fr/resources/liaison-iris-bureaux-de-vote-de-2024/20260402-200739/rattacheuririsbureaux.txt",
    ),
    Source(
        "contours/contours-france-entiere-latest-v2.geojson",
        "https://object.files.data.gouv.fr/data-pipeline-open/reu/contours-france-entiere-latest-v2.geojson",
    ),
    Source(
        "contours/reu-france-entiere-2022-06-01-v2.pmtiles",
        "https://object.files.data.gouv.fr/data-pipeline-open/reu/reu-france-entiere-2022-06-01-v2.pmtiles",
    ),
    Source(
        "communes/communes-100m-2026.geojson.gz",
        "https://etalab-datasets.geo.data.gouv.fr/contours-administratifs/2026/geojson/communes-100m.geojson.gz",
    ),
)


def download(
    sources: Iterable[Source] = MANIFEST, dest_root: Path = RAW_DIR
) -> list[Path]:
    """Télécharge chaque source manquante sous `dest_root`.

    Un fichier déjà présent est sauté (ni retéléchargé, ni vérifié) : relancer la
    commande après une interruption ne refait que le travail restant.
    Retourne les chemins effectivement téléchargés.
    """
    downloaded: list[Path] = []
    for source in sources:
        target = dest_root / source.dest
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(source.url, target)
        downloaded.append(target)
    return downloaded


def main() -> None:
    """Point d'entrée `uv run download-data`."""
    downloaded = download()
    for path in downloaded:
        print(f"téléchargé : {path}")
    deja_presents = len(MANIFEST) - len(downloaded)
    print(f"{len(downloaded)} fichier(s) téléchargé(s), {deja_presents} déjà présent(s).")


if __name__ == "__main__":
    main()

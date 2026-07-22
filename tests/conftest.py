"""Fixtures partagées : extrait réel gelé des 4 scrutins sources (tests/fixtures/*.parquet).

Utilisées par test_ingest.py et test_carte.py — un seul panel réel construit une
fois par session, pour éviter de reconstruire le pipeline d'ingestion à chaque
fichier de test.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.ingest import ingest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def general_results_reel() -> pl.DataFrame:
    return pl.read_parquet(FIXTURES / "general_results.parquet")


@pytest.fixture(scope="session")
def candidats_results_reel() -> pl.DataFrame:
    return pl.read_parquet(FIXTURES / "candidats_results.parquet")


@pytest.fixture(scope="session")
def panel_reel(general_results_reel, candidats_results_reel) -> pl.DataFrame:
    return ingest(general_results_reel, candidats_results_reel)

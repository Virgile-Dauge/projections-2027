"""Tests des fonctions pures de préparation des données carte (bureau + commune).

Deux familles, comme test_ingest.py : DataFrame synthétiques par fonction, puis
intégration sur le panel réel gelé (tests/fixtures/*.parquet, via la fixture
`panel_reel` de conftest.py) pour un scrutin réellement présent dans l'extrait.

Rappel garde-fou (docs/heritage-2024.md, ADR 0001) : les % par bloc ici sont des
résultats 2024 RÉELS et OBSERVÉS (descriptif), pas une projection à intervalle de
confiance — l'ADR 0001 interdit la seconde catégorie, pas la première.
"""

import polars as pl
import pytest

from projections.carte import BLOC_SLUG, scores_bureau, scores_commune

# --- Fixtures synthétiques ----------------------------------------------------


def _panel_synthetique() -> pl.DataFrame:
    """Deux bureaux d'une même commune, un bureau d'une autre commune, 2 scrutins."""
    lignes = []
    # Commune 69123, bureau 0001 : petit bureau, RN en tête.
    for bloc, voix in [("Extrême droite", 60), ("Gauche", 30), ("Divers", 10)]:
        lignes.append(
            {
                "id_election": "2024_legi_t1",
                "code_departement": "69",
                "code_commune": "69123",
                "code_bv": "0001",
                "id_bv": "69123_0001",
                "bloc": bloc,
                "voix": voix,
                "inscrits": 200,
                "abstentions": 50,
                "votants": 100,
                "blancs": 5,
                "nuls": 5,
                "exprimes": 100,
            }
        )
    # Commune 69123, bureau 0002 : gros bureau, Gauche en tête (pour tester que
    # l'agrégat commune suit les voix, pas la moyenne des deux bureaux).
    for bloc, voix in [("Extrême droite", 100), ("Gauche", 700), ("Divers", 100)]:
        lignes.append(
            {
                "id_election": "2024_legi_t1",
                "code_departement": "69",
                "code_commune": "69123",
                "code_bv": "0002",
                "id_bv": "69123_0002",
                "bloc": bloc,
                "voix": voix,
                "inscrits": 1200,
                "abstentions": 100,
                "votants": 1000,
                "blancs": 50,
                "nuls": 50,
                "exprimes": 900,
            }
        )
    # Autre commune, autre scrutin : ne doit apparaître dans aucun résultat filtré
    # sur 2024_legi_t1.
    lignes.append(
        {
            "id_election": "2022_pres_t1",
            "code_departement": "01",
            "code_commune": "01001",
            "code_bv": "0001",
            "id_bv": "01001_0001",
            "bloc": "Droite",
            "voix": 50,
            "inscrits": 100,
            "abstentions": 20,
            "votants": 80,
            "blancs": 0,
            "nuls": 0,
            "exprimes": 50,
        }
    )
    return pl.DataFrame(lignes)


@pytest.fixture
def panel_synthetique() -> pl.DataFrame:
    return _panel_synthetique()


# --- scores_bureau --------------------------------------------------------------


def test_scores_bureau_filtre_par_scrutin(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    assert set(resultat.get_column("id_bv").to_list()) == {"69123_0001", "69123_0002"}


def test_scores_bureau_pct_des_exprimes_par_bloc(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    bureau_1 = resultat.filter(pl.col("id_bv") == "69123_0001").row(0, named=True)
    assert bureau_1["pct_extreme_droite"] == pytest.approx(60.0)
    assert bureau_1["pct_gauche"] == pytest.approx(30.0)
    assert bureau_1["pct_divers"] == pytest.approx(10.0)
    # Bloc absent du bureau (aucun candidat Centre/Droite) -> 0 %, jamais nul.
    assert bureau_1["pct_centre"] == pytest.approx(0.0)
    assert bureau_1["pct_droite"] == pytest.approx(0.0)


def test_scores_bureau_bloc_en_tete(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    par_bureau = {row["id_bv"]: row["bloc_tete"] for row in resultat.iter_rows(named=True)}
    assert par_bureau["69123_0001"] == "Extrême droite"
    assert par_bureau["69123_0002"] == "Gauche"


def test_scores_bureau_participation_votants_sur_inscrits(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    bureau_1 = resultat.filter(pl.col("id_bv") == "69123_0001").row(0, named=True)
    assert bureau_1["participation"] == pytest.approx(100 / 200 * 100)


def test_scores_bureau_conserve_code_commune_et_departement(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    bureau_1 = resultat.filter(pl.col("id_bv") == "69123_0001").row(0, named=True)
    assert bureau_1["code_commune"] == "69123"
    assert bureau_1["code_departement"] == "69"


def test_scores_bureau_gere_un_bureau_sans_exprimes_sans_division_par_zero():
    panel = pl.DataFrame(
        [
            {
                "id_election": "2024_legi_t1",
                "code_departement": "69",
                "code_commune": "69123",
                "code_bv": "0003",
                "id_bv": "69123_0003",
                "bloc": "Gauche",
                "voix": 0,
                "inscrits": 10,
                "abstentions": 10,
                "votants": 0,
                "blancs": 0,
                "nuls": 0,
                "exprimes": 0,
            }
        ]
    )
    resultat = scores_bureau(panel, id_election="2024_legi_t1")
    assert resultat.get_column("pct_gauche").to_list() == [0.0]


def test_scores_bureau_toutes_les_colonnes_de_pct_couvrent_les_5_blocs(panel_synthetique):
    resultat = scores_bureau(panel_synthetique, id_election="2024_legi_t1")
    for slug in BLOC_SLUG.values():
        assert f"pct_{slug}" in resultat.columns


# --- scores_commune : agrégation PAR LES VOIX, jamais moyenne de % -------------


def test_scores_commune_agrege_par_les_voix_pas_par_moyenne_des_pourcentages(panel_synthetique):
    resultat = scores_commune(panel_synthetique, id_election="2024_legi_t1")
    commune = resultat.filter(pl.col("code_commune") == "69123").row(0, named=True)
    # Bureau 1 (100 exprimés) : 60 % EXD / 30 % Gauche. Bureau 2 (900 exprimés) :
    # ~11,1 % EXD / ~77,8 % Gauche. Une moyenne naïve des % donnerait ~35,6 %
    # EXD ; la bonne réponse (voix : 160 EXD / 1000 exprimés) est 16 %.
    total_exprimes = 100 + 900
    assert commune["pct_extreme_droite"] == pytest.approx((60 + 100) / total_exprimes * 100)
    assert commune["pct_gauche"] == pytest.approx((30 + 700) / total_exprimes * 100)
    # La moyenne naïve des deux % de bureau aurait donné un résultat différent :
    naive = (60.0 + 100 / 900 * 100) / 2
    assert commune["pct_extreme_droite"] != pytest.approx(naive)


def test_scores_commune_bloc_en_tete_suit_le_total_des_voix(panel_synthetique):
    resultat = scores_commune(panel_synthetique, id_election="2024_legi_t1")
    commune = resultat.filter(pl.col("code_commune") == "69123").row(0, named=True)
    # Gauche : 30+700=730 voix ; Extrême droite : 60+100=160 voix -> Gauche en tête.
    assert commune["bloc_tete"] == "Gauche"


def test_scores_commune_participation_somme_les_effectifs_sans_double_compte(panel_synthetique):
    resultat = scores_commune(panel_synthetique, id_election="2024_legi_t1")
    commune = resultat.filter(pl.col("code_commune") == "69123").row(0, named=True)
    # inscrits = 200 (bureau 1) + 1200 (bureau 2) = 1400, PAS 1400 x 3 blocs.
    assert commune["inscrits"] == 1400
    assert commune["exprimes"] == 1000


def test_scores_commune_une_ligne_par_commune(panel_synthetique):
    resultat = scores_commune(panel_synthetique, id_election="2024_legi_t1")
    assert resultat.filter(pl.col("code_commune") == "69123").height == 1


# --- Intégration sur le panel réel gelé -----------------------------------------


def test_scores_bureau_reel_pct_somme_a_100_pour_cent(panel_reel):
    resultat = scores_bureau(panel_reel, id_election="2024_legi_t1")
    assert resultat.height > 0
    total = resultat.select(sum(pl.col(f"pct_{slug}") for slug in BLOC_SLUG.values()).alias("total"))
    # Un bureau sans aucun exprimé (rarissime) donnerait 0, pas 100 : on tolère.
    for valeur in total.get_column("total").to_list():
        assert valeur == pytest.approx(100.0) or valeur == pytest.approx(0.0)


def test_scores_commune_reel_couvre_moins_de_communes_que_de_bureaux(panel_reel):
    bureaux = scores_bureau(panel_reel, id_election="2024_legi_t1")
    communes = scores_commune(panel_reel, id_election="2024_legi_t1")
    assert 0 < communes.height <= bureaux.height


def test_scores_reel_bloc_tete_toujours_un_bloc_connu(panel_reel):
    resultat = scores_bureau(panel_reel, id_election="2024_legi_t1")
    inconnus = set(resultat.get_column("bloc_tete").drop_nulls().unique().to_list()) - set(BLOC_SLUG)
    assert inconnus == set()

"""Tests du churn et du crosswalk à deux étages (issue #4, CONTEXT.md).

Vocabulaire du glossaire (CONTEXT.md) : une commune est stable si le nombre de
bureaux est identique sur les 4 scrutins sources -> jointure directe par
id_bv. Instable -> repli (agrégation à la maille communale). Chaque bureau du
panel final porte l'un de ces deux statuts, jamais un troisième état
silencieux.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.churn import (
    ELECTIONS_SOURCES,
    STATUT_INSTABLE,
    STATUT_JOINT_VALIDE,
    STATUT_REPLI,
    STATUT_STABLE,
    classifier_communes,
    compter_bureaux_par_commune,
    construire_panel_avec_statut,
    distribution_par_departement,
    generer_rapport_churn,
    main,
    part_inscrits_zone_stable,
    taux_churn_national,
)
from projections.ingest import ingest

FIXTURES = Path(__file__).parent / "fixtures"


# --- Fixtures pytest ---------------------------------------------------------


@pytest.fixture(scope="session")
def panel_reel() -> pl.DataFrame:
    general = pl.read_parquet(FIXTURES / "general_results.parquet")
    candidats = pl.read_parquet(FIXTURES / "candidats_results.parquet")
    return ingest(general, candidats)


def _ligne_bureau(id_election, code_commune, code_bv, bloc="Gauche", voix=10, code_departement="69"):
    id_bv = f"{code_commune}_{code_bv}"
    return {
        "id_election": id_election,
        "code_departement": code_departement,
        "code_commune": code_commune,
        "code_bv": code_bv,
        "id_bv": id_bv,
        "bloc": bloc,
        "voix": voix,
        "inscrits": 500,
        "abstentions": 100,
        "votants": 400,
        "blancs": 10,
        "nuls": 5,
        "exprimes": 385,
    }


def _panel_synthetique(lignes: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(lignes)


# --- ELECTIONS_SOURCES ---------------------------------------------------------


def test_elections_sources_couvre_les_4_scrutins_sans_les_tours():
    assert set(ELECTIONS_SOURCES) == {"2022_pres", "2022_legi", "2024_legi", "2024_euro"}
    assert len(ELECTIONS_SOURCES) == 4


# --- compter_bureaux_par_commune -----------------------------------------------


def test_compter_bureaux_par_commune_fusionne_les_deux_tours_d_un_meme_scrutin():
    # Un second tour de législatives ne couvre pas toutes les circonscriptions
    # (pas de ballotage partout) : son absence seule ne doit jamais compter
    # comme un changement du nombre de bureaux.
    panel = _panel_synthetique(
        [
            _ligne_bureau("2022_legi_t1", "69123", "0001"),
            _ligne_bureau("2022_legi_t1", "69123", "0002"),
            _ligne_bureau("2022_legi_t2", "69123", "0001"),  # pas de bureau 0002 au T2
        ]
    )
    resultat = compter_bureaux_par_commune(panel)
    ligne = resultat.filter(pl.col("code_commune") == "69123")
    assert ligne.get_column("nb_bureaux").to_list() == [2]
    assert ligne.get_column("election").to_list() == ["2022_legi"]


def test_compter_bureaux_par_commune_compte_par_commune_et_scrutin():
    panel = _panel_synthetique(
        [
            _ligne_bureau("2022_pres_t1", "69123", "0001"),
            _ligne_bureau("2022_pres_t1", "69123", "0002"),
            _ligne_bureau("2024_euro_t1", "69123", "0001"),
        ]
    )
    resultat = compter_bureaux_par_commune(panel).sort("election")
    assert resultat.get_column("election").to_list() == ["2022_pres", "2024_euro"]
    assert resultat.get_column("nb_bureaux").to_list() == [2, 1]


# --- classifier_communes : stable / instable -----------------------------------


def test_classifier_communes_commune_stable_meme_nombre_de_bureaux_sur_les_4_scrutins():
    lignes = []
    for election in ("2022_pres_t1", "2022_legi_t1", "2024_legi_t1", "2024_euro_t1"):
        lignes.append(_ligne_bureau(election, "69123", "0001"))
        lignes.append(_ligne_bureau(election, "69123", "0002"))
    resultat = classifier_communes(_panel_synthetique(lignes))
    assert resultat.filter(pl.col("code_commune") == "69123").get_column("statut").to_list() == [STATUT_STABLE]


def test_classifier_communes_commune_instable_le_compte_change_entre_deux_scrutins():
    lignes = [
        _ligne_bureau("2022_pres_t1", "69123", "0001"),
        _ligne_bureau("2022_legi_t1", "69123", "0001"),
        _ligne_bureau("2024_legi_t1", "69123", "0001"),
        _ligne_bureau("2024_legi_t1", "69123", "0002"),  # redécoupage : un bureau de plus
        _ligne_bureau("2024_euro_t1", "69123", "0001"),
        _ligne_bureau("2024_euro_t1", "69123", "0002"),
    ]
    resultat = classifier_communes(_panel_synthetique(lignes))
    assert resultat.filter(pl.col("code_commune") == "69123").get_column("statut").to_list() == [STATUT_INSTABLE]


def test_classifier_communes_une_seule_ligne_par_commune_meme_si_code_departement_incoherent():
    # Bug réel observé sur les données complètes : certaines communes DOM/COM
    # ont un code_departement lettré sur un scrutin ("ZC") et numérique sur un
    # autre ("973") pour la même commune. Sans dédup, la table
    # commune -> département a 2 lignes pour cette commune et fait fan-out
    # toute jointure ultérieure (duplication silencieuse de voix).
    lignes = []
    for election, departement in (
        ("2022_pres_t1", "973"),
        ("2022_legi_t1", "973"),
        ("2024_legi_t1", "ZC"),  # même commune, code département différent
        ("2024_euro_t1", "ZC"),
    ):
        lignes.append(_ligne_bureau(election, "97303", "0001", code_departement=departement))
    resultat = classifier_communes(_panel_synthetique(lignes))
    assert resultat.filter(pl.col("code_commune") == "97303").height == 1


def test_classifier_communes_commune_absente_d_un_scrutin_source_est_instable():
    # Prudence : impossible de valider la stabilité d'une commune qui n'a pas
    # de données sur l'un des 4 scrutins sources -> jamais de jointure directe
    # silencieuse.
    lignes = [
        _ligne_bureau("2022_pres_t1", "69123", "0001"),
        _ligne_bureau("2022_legi_t1", "69123", "0001"),
        _ligne_bureau("2024_legi_t1", "69123", "0001"),
        # pas de ligne 2024_euro_t1 pour cette commune
    ]
    resultat = classifier_communes(_panel_synthetique(lignes))
    assert resultat.filter(pl.col("code_commune") == "69123").get_column("statut").to_list() == [STATUT_INSTABLE]


# --- construire_panel_avec_statut : jamais de jointure silencieuse ------------


def test_construire_panel_avec_statut_commune_stable_jointure_directe():
    lignes = []
    for election in ("2022_pres_t1", "2022_legi_t1", "2024_legi_t1", "2024_euro_t1"):
        lignes.append(_ligne_bureau(election, "69123", "0001", voix=10))
    panel = _panel_synthetique(lignes)
    classification = classifier_communes(panel)
    resultat = construire_panel_avec_statut(panel, classification)

    assert resultat.get_column("statut").unique().to_list() == [STATUT_JOINT_VALIDE]
    # Jointure directe : les lignes passent telles quelles, un bureau par ligne.
    assert set(resultat.get_column("id_bv").to_list()) == {"69123_0001"}
    assert resultat.get_column("voix").to_list() == [10, 10, 10, 10]


def test_construire_panel_avec_statut_commune_instable_repli_maille_communale():
    lignes = [
        _ligne_bureau("2022_pres_t1", "69123", "0001", voix=10),
        _ligne_bureau("2022_legi_t1", "69123", "0001", voix=10),
        _ligne_bureau("2024_legi_t1", "69123", "0001", voix=6),
        _ligne_bureau("2024_legi_t1", "69123", "0002", voix=4),  # redécoupage
        _ligne_bureau("2024_euro_t1", "69123", "0001", voix=6),
        _ligne_bureau("2024_euro_t1", "69123", "0002", voix=4),
    ]
    panel = _panel_synthetique(lignes)
    classification = classifier_communes(panel)
    resultat = construire_panel_avec_statut(panel, classification)

    assert resultat.get_column("statut").unique().to_list() == [STATUT_REPLI]
    # Repli à la maille communale : plus de granularité bureau (id_bv/code_bv à
    # null), une ligne par scrutin × bloc pour la commune entière.
    assert resultat.get_column("id_bv").null_count() == resultat.height
    ligne_2024_legi = resultat.filter(pl.col("id_election") == "2024_legi_t1")
    assert ligne_2024_legi.get_column("voix").to_list() == [10]  # 6 + 4 sommés
    # Participation dédupliquée avant somme (pas doublée par bureau).
    assert ligne_2024_legi.get_column("inscrits").to_list() == [1000]  # 500 + 500


def test_construire_panel_avec_statut_leve_une_erreur_si_commune_absente_de_la_classification():
    panel = _panel_synthetique([_ligne_bureau("2022_pres_t1", "69123", "0001")])
    classification_incomplete = pl.DataFrame(
        {"code_commune": ["01001"], "code_departement": ["01"], "statut": [STATUT_STABLE]}
    )
    with pytest.raises(ValueError, match="69123"):
        construire_panel_avec_statut(panel, classification_incomplete)


# --- Statistiques du rapport ----------------------------------------------------


def test_taux_churn_national_proportion_de_communes_instables():
    classification = pl.DataFrame(
        {
            "code_commune": ["A", "B", "C", "D"],
            "code_departement": ["69", "69", "01", "01"],
            "statut": [STATUT_STABLE, STATUT_INSTABLE, STATUT_STABLE, STATUT_STABLE],
        }
    )
    assert taux_churn_national(classification) == pytest.approx(0.25)


def test_distribution_par_departement_taux_instable_par_departement():
    classification = pl.DataFrame(
        {
            "code_commune": ["A", "B", "C", "D"],
            "code_departement": ["69", "69", "01", "01"],
            "statut": [STATUT_STABLE, STATUT_INSTABLE, STATUT_STABLE, STATUT_STABLE],
        }
    )
    resultat = distribution_par_departement(classification).sort("code_departement")
    # Trié par code_departement croissant : "01" (0 instable) puis "69" (1 instable).
    assert resultat.get_column("nb_communes").to_list() == [2, 2]
    assert resultat.get_column("nb_communes_instables").to_list() == [0, 1]
    assert resultat.get_column("taux_instable").to_list() == [0.0, 0.5]


def test_distribution_par_departement_ordre_deterministe_a_egalite_de_taux():
    # Reproductibilité du rapport (critère d'acceptation #4) : à taux
    # d'instabilité égal (ex. 0 %, le cas le plus fréquent), l'ordre des
    # départements doit être déterministe d'un run à l'autre.
    classification = pl.DataFrame(
        {
            "code_commune": ["A", "B", "C"],
            "code_departement": ["93", "01", "69"],
            "statut": [STATUT_STABLE, STATUT_STABLE, STATUT_STABLE],
        }
    )
    resultat = distribution_par_departement(classification)
    assert resultat.get_column("code_departement").to_list() == ["01", "69", "93"]


def test_part_inscrits_zone_stable_pondere_par_les_inscrits_pas_par_la_surface():
    panel = _panel_synthetique(
        [
            _ligne_bureau("2024_legi_t1", "69123", "0001", code_departement="69"),  # 500 inscrits
            _ligne_bureau("2024_legi_t1", "01001", "0001", code_departement="01"),  # 500 inscrits
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69123", "01001"],
            "code_departement": ["69", "01"],
            "statut": [STATUT_STABLE, STATUT_INSTABLE],
        }
    )
    resultat = part_inscrits_zone_stable(panel, classification, "2024_legi_t1")
    assert resultat == pytest.approx(0.5)


# --- generer_rapport_churn : contenu attendu par le rapport --------------------


def test_generer_rapport_churn_contient_les_trois_chiffres_requis(panel_reel):
    rapport = generer_rapport_churn(panel_reel, scrutin_reference="2024_legi_t1")
    assert "Taux de churn national" in rapport
    assert "Distribution par département" in rapport
    assert "inscrits en zone stable" in rapport


# --- Intégration sur l'extrait réel gelé ---------------------------------------


def test_panel_avec_statut_reel_ne_laisse_aucun_statut_null(panel_reel):
    classification = classifier_communes(panel_reel)
    resultat = construire_panel_avec_statut(panel_reel, classification)
    assert resultat.get_column("statut").null_count() == 0
    assert set(resultat.get_column("statut").unique().to_list()) <= {STATUT_JOINT_VALIDE, STATUT_REPLI}


# --- Entrée console `uv run rapport-churn` -------------------------------------


def test_main_ecrit_le_rapport_et_le_panel_avec_statut(tmp_path, monkeypatch):
    rapport_out = tmp_path / "rapport-churn.md"
    panel_out = tmp_path / "panel_avec_statut.parquet"
    monkeypatch.setattr(
        "sys.argv",
        [
            "rapport-churn",
            "--general-results",
            str(FIXTURES / "general_results.parquet"),
            "--candidats-results",
            str(FIXTURES / "candidats_results.parquet"),
            "--out",
            str(rapport_out),
            "--panel-out",
            str(panel_out),
        ],
    )
    main()
    assert rapport_out.exists()
    assert panel_out.exists()
    assert "Taux de churn national" in rapport_out.read_text(encoding="utf-8")

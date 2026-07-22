"""Tests du churn et du crosswalk à deux étages (issue #4, CONTEXT.md).

Vocabulaire du glossaire (CONTEXT.md) : une commune est stable si le nombre de
bureaux est identique sur les 4 scrutins sources -> jointure directe par
id_bv. Instable -> repli (agrégation à la maille communale, ou réconciliation
bureau par réallocation dasymétrique pondérée par les inscrits pour Paris —
issue #14). Chaque bureau du panel final porte un statut explicite, jamais un
troisième état silencieux.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.churn import (
    COMMUNES_RECONCILIATION_BUREAU,
    ELECTIONS_SOURCES,
    STATUT_INSTABLE,
    STATUT_IRRESOLUBLE,
    STATUT_JOINT_VALIDE,
    STATUT_RECONCILIE,
    STATUT_REALLOUE,
    STATUT_REPLI,
    STATUT_STABLE,
    classifier_communes,
    compter_bureaux_par_commune,
    construire_panel_avec_statut,
    distribution_par_departement,
    generer_rapport_churn,
    inscrits_par_departement,
    main,
    part_inscrits_zone_instable,
    part_inscrits_zone_instable_apres_reconciliation,
    part_inscrits_zone_stable,
    reconcilier_bureaux_par_reallocation,
    table_departements,
    taux_churn_national,
    top_communes_instables_par_inscrits,
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


# --- reconcilier_bureaux_par_reallocation : second étage du repli (issue #14) --


def test_reconcilier_bureaux_par_reallocation_bureau_apparie_reste_reconcilie():
    # Même id_bv des deux côtés : jointure directe, pas de réallocation, mais
    # statut distinct de joint-validé (CONTEXT.md : la commune reste instable).
    lignes = [
        _ligne_bureau("2024_legi_t1", "75056", "0001", voix=20, code_departement="75"),
        _ligne_bureau("2022_pres_t1", "75056", "0001", voix=15, code_departement="75"),
    ]
    commune = _panel_synthetique(lignes)
    resultat = reconcilier_bureaux_par_reallocation(commune, scrutin_reference="2024_legi_t1")
    assert resultat.get_column("statut").unique().to_list() == [STATUT_RECONCILIE]
    assert sorted(resultat.get_column("voix").to_list()) == [15, 20]


def test_reconcilier_bureaux_par_reallocation_reliquat_realloue_au_prorata_des_inscrits():
    # Grille cible (scrutin_reference) : 2 bureaux orphelins, poids d'inscrits
    # très inégaux (300 vs 700). Scrutin source : 1 bureau orphelin (numéroté
    # différemment, ex. renumérotation), avec des voix connues par bloc.
    cible = [
        {**_ligne_bureau("2024_legi_t1", "75056", "0211", bloc="Gauche", voix=999, code_departement="75"), "inscrits": 300},
        {**_ligne_bureau("2024_legi_t1", "75056", "0212", bloc="Gauche", voix=999, code_departement="75"), "inscrits": 700},
    ]
    source = [
        {**_ligne_bureau("2022_pres_t1", "75056", "0201", bloc="Gauche", voix=100, code_departement="75"), "inscrits": 950},
        {**_ligne_bureau("2022_pres_t1", "75056", "0201", bloc="Droite", voix=50, code_departement="75"), "inscrits": 950},
    ]
    commune = _panel_synthetique(cible + source)
    resultat = reconcilier_bureaux_par_reallocation(commune, scrutin_reference="2024_legi_t1")

    realloue = resultat.filter(pl.col("id_election") == "2022_pres_t1")
    assert set(realloue.get_column("statut").unique().to_list()) == {STATUT_REALLOUE}

    b211 = realloue.filter((pl.col("id_bv") == "75056_0211") & (pl.col("bloc") == "Gauche")).get_column("voix").item()
    b212 = realloue.filter((pl.col("id_bv") == "75056_0212") & (pl.col("bloc") == "Gauche")).get_column("voix").item()
    assert b211 == pytest.approx(30.0)  # 100 * 300/1000
    assert b212 == pytest.approx(70.0)  # 100 * 700/1000

    # Conservation des totaux par commune x scrutin x bloc (critère d'acceptation) :
    # la somme réallouée reconstitue exactement le pool source, jamais plus jamais moins.
    assert realloue.filter(pl.col("bloc") == "Gauche").get_column("voix").sum() == pytest.approx(100.0)
    assert realloue.filter(pl.col("bloc") == "Droite").get_column("voix").sum() == pytest.approx(50.0)

    # Participation réallouée au même prorata d'inscrits (jamais par la surface).
    inscrits_211 = realloue.filter(pl.col("id_bv") == "75056_0211").get_column("inscrits").to_list()[0]
    assert inscrits_211 == pytest.approx(950 * 0.3)


def test_reconcilier_bureaux_par_reallocation_bureau_non_resoluble_sans_donnee_source():
    # 75056_0299 n'a aucune ligne (sous aucun id_bv) sur 2022_pres_t1 : aucun
    # reliquat à réallouer -> statut explicite, jamais un zéro fabriqué.
    cible = [
        {**_ligne_bureau("2024_legi_t1", "75056", "0211", bloc="Gauche", voix=10, code_departement="75"), "inscrits": 300},
        {**_ligne_bureau("2024_legi_t1", "75056", "0299", bloc="Gauche", voix=10, code_departement="75"), "inscrits": 200},
    ]
    source = [
        {**_ligne_bureau("2022_pres_t1", "75056", "0211", bloc="Gauche", voix=8, code_departement="75"), "inscrits": 300},
    ]
    commune = _panel_synthetique(cible + source)
    resultat = reconcilier_bureaux_par_reallocation(commune, scrutin_reference="2024_legi_t1")

    irresoluble = resultat.filter((pl.col("id_election") == "2022_pres_t1") & (pl.col("id_bv") == "75056_0299"))
    assert irresoluble.get_column("statut").to_list() == [STATUT_IRRESOLUBLE]
    assert irresoluble.get_column("voix").item() is None


def test_reconcilier_bureaux_par_reallocation_second_tour_legi_partiel_non_realloue():
    # Ballottage : seul le bureau 0211 a un second tour de législatives, 0212
    # n'en a pas -- absence normale (pas de circonscription disputée partout),
    # jamais une réallocation ou une irrésolution fabriquée pour 0212.
    cible = [
        {**_ligne_bureau("2024_legi_t1", "75056", "0211", bloc="Gauche", voix=10, code_departement="75"), "inscrits": 300},
        {**_ligne_bureau("2024_legi_t1", "75056", "0212", bloc="Gauche", voix=10, code_departement="75"), "inscrits": 200},
    ]
    source_t2 = [
        {**_ligne_bureau("2024_legi_t2", "75056", "0211", bloc="Gauche", voix=9, code_departement="75"), "inscrits": 300},
    ]
    commune = _panel_synthetique(cible + source_t2)
    resultat = reconcilier_bureaux_par_reallocation(commune, scrutin_reference="2024_legi_t1")

    t2 = resultat.filter(pl.col("id_election") == "2024_legi_t2")
    assert t2.get_column("id_bv").to_list() == ["75056_0211"]
    assert t2.get_column("statut").to_list() == [STATUT_RECONCILIE]


# --- construire_panel_avec_statut : routage Paris (issue #14) ------------------


def test_construire_panel_avec_statut_paris_maille_bureau_statut_distinct_joint_valide():
    # Reproduit la structure réelle de Paris en miniature : un bureau apparié
    # (0001) + un bureau renuméroté entre 2022 et 2024 (0201 -> 0211).
    lignes = [
        _ligne_bureau("2024_legi_t1", "75056", "0001", code_departement="75"),
        _ligne_bureau("2024_legi_t1", "75056", "0211", code_departement="75"),
        _ligne_bureau("2022_pres_t1", "75056", "0001", code_departement="75"),
        _ligne_bureau("2022_pres_t1", "75056", "0201", code_departement="75"),
    ]
    panel = _panel_synthetique(lignes)
    classification = pl.DataFrame(
        {"code_commune": ["75056"], "code_departement": ["75"], "statut": [STATUT_INSTABLE]}
    )
    resultat = construire_panel_avec_statut(panel, classification, scrutin_reference="2024_legi_t1")
    paris = resultat.filter(pl.col("code_commune") == "75056")

    # Critère d'acceptation #1 : maille bureau conservée, statut distinct de
    # joint-validé (la commune reste instable dans son ensemble).
    assert paris.get_column("id_bv").null_count() == 0
    statuts = set(paris.get_column("statut").unique().to_list())
    assert statuts <= {STATUT_RECONCILIE, STATUT_REALLOUE, STATUT_IRRESOLUBLE}
    assert STATUT_JOINT_VALIDE not in statuts
    assert STATUT_REPLI not in statuts


def test_construire_panel_avec_statut_commune_hors_paris_inchangee():
    # Critère d'acceptation : une commune instable hors Paris continue le
    # repli communal classique, même structure de mismatch que Paris.
    assert "69123" not in COMMUNES_RECONCILIATION_BUREAU
    lignes = [
        _ligne_bureau("2024_legi_t1", "69123", "0001", voix=6),
        _ligne_bureau("2024_legi_t1", "69123", "0002", voix=4),
        _ligne_bureau("2022_pres_t1", "69123", "0001", voix=10),
    ]
    panel = _panel_synthetique(lignes)
    classification = pl.DataFrame(
        {"code_commune": ["69123"], "code_departement": ["69"], "statut": [STATUT_INSTABLE]}
    )
    resultat = construire_panel_avec_statut(panel, classification)
    assert resultat.get_column("statut").unique().to_list() == [STATUT_REPLI]
    assert resultat.get_column("id_bv").null_count() == resultat.height


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


def test_inscrits_par_departement_ratio_depuis_les_sommes_jamais_une_moyenne_de_taux():
    # 2 communes dans le même département, poids d'inscrits très inégaux
    # (100 vs 900) : si le code moyennait les taux communaux (0 et 1), le
    # résultat serait 0.5. Le bon calcul (somme des inscrits instables /
    # somme des inscrits du département) donne 0.9.
    panel = _panel_synthetique(
        [
            {**_ligne_bureau("2024_legi_t1", "69001", "0001", code_departement="69"), "inscrits": 100},
            {**_ligne_bureau("2024_legi_t1", "69002", "0001", code_departement="69"), "inscrits": 900},
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69001", "69002"],
            "code_departement": ["69", "69"],
            "statut": [STATUT_STABLE, STATUT_INSTABLE],
        }
    )
    resultat = inscrits_par_departement(panel, classification, "2024_legi_t1")
    ligne = resultat.filter(pl.col("code_departement") == "69")
    assert ligne.get_column("inscrits_departement").to_list() == [1000]
    assert ligne.get_column("inscrits_instables").to_list() == [900]
    assert ligne.get_column("part_inscrits_instables").to_list() == pytest.approx([0.9])


def test_table_departements_triee_par_inscrits_instables_absolu_decroissant():
    # Département "69" : taux communal élevé (1 commune instable sur 1 =
    # 100 %) mais peu d'inscrits (100). Département "75" : taux communal
    # plus faible (1 sur 2 = 50 %) mais beaucoup plus d'inscrits instables
    # (900). La table doit prioriser l'absolu (75 en tête), pas le taux.
    panel = _panel_synthetique(
        [
            {**_ligne_bureau("2024_legi_t1", "69001", "0001", code_departement="69"), "inscrits": 100},
            {**_ligne_bureau("2024_legi_t1", "75001", "0001", code_departement="75"), "inscrits": 900},
            {**_ligne_bureau("2024_legi_t1", "75002", "0001", code_departement="75"), "inscrits": 50},
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69001", "75001", "75002"],
            "code_departement": ["69", "75", "75"],
            "statut": [STATUT_INSTABLE, STATUT_INSTABLE, STATUT_STABLE],
        }
    )
    resultat = table_departements(panel, classification, "2024_legi_t1")
    assert resultat.get_column("code_departement").to_list() == ["75", "69"]
    assert resultat.get_column("inscrits_instables").to_list() == [900, 100]
    # Colonnes communales existantes toujours présentes (ajout, pas remplacement).
    assert "nb_communes" in resultat.columns
    assert "taux_instable" in resultat.columns


def test_table_departements_ordre_deterministe_a_egalite_d_inscrits_instables():
    panel = _panel_synthetique(
        [
            {**_ligne_bureau("2024_legi_t1", "93001", "0001", code_departement="93"), "inscrits": 100},
            {**_ligne_bureau("2024_legi_t1", "01001", "0001", code_departement="01"), "inscrits": 100},
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["93001", "01001"],
            "code_departement": ["93", "01"],
            "statut": [STATUT_INSTABLE, STATUT_INSTABLE],
        }
    )
    resultat = table_departements(panel, classification, "2024_legi_t1")
    assert resultat.get_column("code_departement").to_list() == ["01", "93"]


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


def test_part_inscrits_zone_instable_pondere_par_les_inscrits_jamais_par_la_surface():
    # Mesure canonique du churn (CONTEXT.md « Churn ») : la grandeur à
    # minimiser, jamais un compte de communes. Poids délibérément inégaux
    # (200 vs 800) pour distinguer d'une simple moyenne 50/50 des statuts.
    panel = _panel_synthetique(
        [
            {**_ligne_bureau("2024_legi_t1", "69123", "0001", code_departement="69"), "inscrits": 200},
            {**_ligne_bureau("2024_legi_t1", "01001", "0001", code_departement="01"), "inscrits": 800},
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69123", "01001"],
            "code_departement": ["69", "01"],
            "statut": [STATUT_STABLE, STATUT_INSTABLE],
        }
    )
    resultat = part_inscrits_zone_instable(panel, classification, "2024_legi_t1")
    assert resultat == pytest.approx(0.8)  # 800 / (200 + 800), pas une moyenne de statuts (0.5)


# --- part_inscrits_zone_instable_apres_reconciliation : gain Paris (issue #14) -


def test_part_inscrits_zone_instable_apres_reconciliation_baisse_grace_a_paris():
    # 01001 (joint-validé) et 75056 (réconciliée) comptent résolus ; seul
    # 69123 (repli communal classique, id_bv devenu null) reste instable.
    panel_avec_statut = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1", "2024_legi_t1", "2024_legi_t1"],
            "code_commune": ["01001", "75056", "69123"],
            "id_bv": ["01001_0001", "75056_0001", None],
            "inscrits": [500, 1000, 2000],
            "statut": [STATUT_JOINT_VALIDE, STATUT_RECONCILIE, STATUT_REPLI],
        }
    )
    resultat = part_inscrits_zone_instable_apres_reconciliation(panel_avec_statut, "2024_legi_t1")
    assert resultat == pytest.approx(2000 / 3500)


def test_part_inscrits_zone_instable_apres_reconciliation_bureau_irresoluble_compte_encore_instable():
    # Le bureau est `reconcilie` à la référence, mais `irresoluble` sur un
    # autre scrutin : il reste compté comme instable (jamais un blanc-seing
    # donné par le seul statut du scrutin de référence).
    panel_avec_statut = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1", "2022_pres_t1"],
            "code_commune": ["75056", "75056"],
            "id_bv": ["75056_0001", "75056_0001"],
            "inscrits": [1000, 1000],
            "statut": [STATUT_RECONCILIE, STATUT_IRRESOLUBLE],
        }
    )
    resultat = part_inscrits_zone_instable_apres_reconciliation(panel_avec_statut, "2024_legi_t1")
    assert resultat == pytest.approx(1.0)


def test_top_communes_instables_par_inscrits_tri_et_limite():
    # 3 communes instables + 1 stable (exclue) ; on ne garde que le top 2 par
    # inscrits, avec leur nombre de bureaux sur le scrutin de référence.
    panel = _panel_synthetique(
        [
            _ligne_bureau("2024_legi_t1", "69001", "0001", code_departement="69"),  # 500 inscrits, instable
            _ligne_bureau("2024_legi_t1", "69002", "0001", code_departement="69"),
            _ligne_bureau("2024_legi_t1", "69002", "0002", code_departement="69"),  # 2 bureaux -> 1000 inscrits
            _ligne_bureau("2024_legi_t1", "69003", "0001", code_departement="69"),  # 500 inscrits, instable
            _ligne_bureau("2024_legi_t1", "69004", "0001", code_departement="69"),  # stable, exclue
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69001", "69002", "69003", "69004"],
            "code_departement": ["69", "69", "69", "69"],
            "statut": [STATUT_INSTABLE, STATUT_INSTABLE, STATUT_INSTABLE, STATUT_STABLE],
        }
    )
    resultat = top_communes_instables_par_inscrits(panel, classification, "2024_legi_t1", n=2)
    assert resultat.height == 2
    assert resultat.get_column("code_commune").to_list() == ["69002", "69001"]
    assert resultat.get_column("inscrits").to_list() == [1000, 500]
    assert resultat.get_column("nb_bureaux").to_list() == [2, 1]


def test_top_communes_instables_par_inscrits_ordre_deterministe_a_egalite():
    panel = _panel_synthetique(
        [
            _ligne_bureau("2024_legi_t1", "69003", "0001", code_departement="69"),
            _ligne_bureau("2024_legi_t1", "69001", "0001", code_departement="69"),
        ]
    )
    classification = pl.DataFrame(
        {
            "code_commune": ["69003", "69001"],
            "code_departement": ["69", "69"],
            "statut": [STATUT_INSTABLE, STATUT_INSTABLE],
        }
    )
    resultat = top_communes_instables_par_inscrits(panel, classification, "2024_legi_t1")
    assert resultat.get_column("code_commune").to_list() == ["69001", "69003"]


# --- generer_rapport_churn : contenu attendu par le rapport --------------------


def test_generer_rapport_churn_contient_les_trois_chiffres_requis(panel_reel):
    # Chiffre de tête = part des inscrits en zone instable (issue #13) ; le
    # compte de communes descend en contexte dans le même paragraphe.
    rapport = generer_rapport_churn(panel_reel, scrutin_reference="2024_legi_t1")
    assert "Churn national" in rapport
    assert "part des inscrits" in rapport
    assert "Distribution par département" in rapport
    assert "Top 20 communes instables par inscrits" in rapport


def test_generer_rapport_churn_contient_le_gain_avant_apres_reconciliation(panel_reel):
    # Issue #14 : le rapport documente la méthode et chiffre le gain
    # avant/après réconciliation de Paris (le fixture réel de test ne contient
    # pas Paris, donc le gain y est nul, mais la section doit être présente
    # et ne jamais lever d'exception, y compris sans Paris dans les données).
    rapport = generer_rapport_churn(panel_reel, scrutin_reference="2024_legi_t1")
    assert "Réconciliation de Paris" in rapport
    assert "Avant réconciliation" in rapport
    assert "Après réconciliation" in rapport
    assert "Gain chiffré" in rapport


def test_generer_rapport_churn_table_departements_triee_par_absolu_pas_par_taux(panel_reel):
    # Reproductibilité + priorisation (issue #13) : la table des départements
    # doit être ordonnée par inscrits en zone instable décroissant, jamais
    # par le taux communal. On vérifie que l'ordre des lignes suit bien la
    # colonne "Inscrits en zone instable" et pas la colonne "Taux instable".
    rapport = generer_rapport_churn(panel_reel, scrutin_reference="2024_legi_t1")
    debut = rapport.index("## Distribution par département")
    fin = rapport.index("## Top 20 communes instables par inscrits")
    bloc = rapport[debut:fin]
    lignes = [ligne for ligne in bloc.splitlines() if ligne.startswith("| ") and "---" not in ligne][1:]
    valeurs_inscrits = [int(ligne.split("|")[2].strip()) for ligne in lignes]
    assert valeurs_inscrits == sorted(valeurs_inscrits, reverse=True)


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
    assert "Churn national" in rapport_out.read_text(encoding="utf-8")

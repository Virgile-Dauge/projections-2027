"""Tests des backtests 2022->2024 et du verdict du gate (issue #6, ADR 0001).

Trois familles de tests :
- propriétés mathématiques sur données synthétiques (Spearman correcte sur cas
  connus, tercile bien défini, gate évalué correctement sur seuils synthétiques) ;
- garde-fou anti-fuite : le prédicteur 2022 ne doit pas bouger si les données
  2024 changent (CLAUDE.md « RÈGLE ANTI-FUITE ») ;
- intégration sur l'extrait réel gelé (tests/fixtures/*.parquet), qui traverse
  tout `executer_backtests`.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.backtest import (
    BLOCS_MAJEURS,
    CIBLES,
    CIBLES_PARTICIPATION,
    COLONNE_ABSTENTION_PREDICTEUR,
    POIDS_COMPOSITE_2022_PAR_DEFAUT,
    SCRUTIN_LEGISLATIVES_2022,
    SCRUTIN_LEGISLATIVES_2022_CORRIGE,
    SEUIL_RHO_PARTICIPATION,
    calculer_ecart_national_departement,
    calculer_taux_abstention,
    calculer_taux_abstention_departement,
    calibrer_poids,
    construire_predicteur_2022,
    construire_predicteur_departemental_2022,
    construire_table_backtest,
    construire_table_participation,
    correlation_euro_pres_rn,
    correlation_spearman,
    distribution_swing,
    evaluer_gate,
    evaluer_gate_participation,
    executer_backtest_participation,
    executer_backtests,
    garde_anti_hasard_participation,
    garde_anti_hasard_structure,
    generer_rapport_backtest,
    generer_rapport_complet,
    isoler_scrutins_2022,
    main,
    rho_par_bloc,
    tercile_competitif,
    verdict_anti_hasard,
    verdict_carte_mobilisation,
    verifier_regularite_seuil,
    verdict_global,
)
from projections.baseline import SCRUTIN_PRESIDENTIELLE, construire_baseline
from projections.churn import classifier_communes, construire_panel_avec_statut
from projections.ingest import ingest

FIXTURES = Path(__file__).parent / "fixtures"


# --- Fixtures pytest ---------------------------------------------------------


@pytest.fixture(scope="session")
def panel_avec_statut_reel() -> pl.DataFrame:
    general = pl.read_parquet(FIXTURES / "general_results.parquet")
    candidats = pl.read_parquet(FIXTURES / "candidats_results.parquet")
    panel = ingest(general, candidats)
    classification = classifier_communes(panel)
    return construire_panel_avec_statut(panel, classification)


@pytest.fixture(scope="session")
def baseline_reel(panel_avec_statut_reel: pl.DataFrame) -> pl.DataFrame:
    return construire_baseline(panel_avec_statut_reel)


def _ligne(id_election, code_commune, code_bv, bloc, voix, exprimes, code_departement="69", abstentions=10, inscrits=None):
    id_bv = f"{code_commune}_{code_bv}"
    return {
        "id_election": id_election,
        "code_departement": code_departement,
        "code_commune": code_commune,
        "code_bv": code_bv,
        "id_bv": id_bv,
        "bloc": bloc,
        "voix": voix,
        "inscrits": inscrits if inscrits is not None else exprimes + 50,
        "abstentions": abstentions,
        "votants": exprimes + 20,
        "blancs": 10,
        "nuls": 10,
        "exprimes": exprimes,
    }


def _panel(lignes: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(lignes)


def _panel_complet_deux_unites(voix_2024_a=(10, 90), voix_2024_b=(90, 10)) -> pl.DataFrame:
    """Panel synthétique couvrant 2022 (pres+legi) et 2024 (euro+legi), 2 unités.

    Utilisé par les tests anti-fuite : les paramètres `voix_2024_*` ne
    contrôlent QUE les lignes 2024 (européennes), pour vérifier que le
    prédicteur 2022 ne varie pas quand elles changent.
    """
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 60, 100),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 40, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 30, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 70, 100),
        _ligne("2022_legi_t1", "69123", "0001", "Gauche", 55, 100),
        _ligne("2022_legi_t1", "69123", "0001", "Droite", 45, 100),
        _ligne("2022_legi_t1", "01001", "0001", "Gauche", 35, 100),
        _ligne("2022_legi_t1", "01001", "0001", "Droite", 65, 100),
        _ligne("2024_euro_t1", "69123", "0001", "Gauche", voix_2024_a[0], 100),
        _ligne("2024_euro_t1", "69123", "0001", "Droite", voix_2024_a[1], 100),
        _ligne("2024_euro_t1", "01001", "0001", "Gauche", voix_2024_b[0], 100),
        _ligne("2024_euro_t1", "01001", "0001", "Droite", voix_2024_b[1], 100),
    ]
    return _panel(lignes)


# --- correlation_spearman : cas connus ---------------------------------------


def test_correlation_spearman_permutation_parfaite_vaut_un():
    table = pl.DataFrame({"x": [1.0, 2.0, 3.0, 4.0, 5.0], "y": [10.0, 20.0, 30.0, 40.0, 50.0]})
    assert correlation_spearman(table, "x", "y") == pytest.approx(1.0)


def test_correlation_spearman_inversion_parfaite_vaut_moins_un():
    table = pl.DataFrame({"x": [1.0, 2.0, 3.0, 4.0, 5.0], "y": [5.0, 4.0, 3.0, 2.0, 1.0]})
    assert correlation_spearman(table, "x", "y") == pytest.approx(-1.0)


def test_correlation_spearman_ignore_les_nulls():
    table = pl.DataFrame({"x": [1.0, 2.0, 3.0, None], "y": [1.0, 2.0, 3.0, 99.0]})
    assert correlation_spearman(table, "x", "y") == pytest.approx(1.0)


def test_correlation_spearman_gere_les_ex_aequo():
    # x a un ex-aequo (2.0 répété) : le rang moyen doit tout de même produire
    # une corrélation calculable, pas d'erreur.
    table = pl.DataFrame({"x": [1.0, 2.0, 2.0, 3.0], "y": [1.0, 2.0, 3.0, 4.0]})
    rho = correlation_spearman(table, "x", "y")
    assert rho == pytest.approx(0.9486832980505138)  # valeur de référence scipy.stats.spearmanr


def test_correlation_spearman_moins_de_deux_points_vaut_nan():
    table = pl.DataFrame({"x": [1.0], "y": [1.0]})
    rho = correlation_spearman(table, "x", "y")
    assert rho != rho  # NaN


def test_correlation_spearman_colonne_constante_vaut_nan():
    table = pl.DataFrame({"x": [1.0, 1.0, 1.0], "y": [1.0, 2.0, 3.0]})
    rho = correlation_spearman(table, "x", "y")
    assert rho != rho  # NaN, pas une division par zéro


# --- rho_par_bloc --------------------------------------------------------------


def test_rho_par_bloc_calcule_un_rho_par_bloc_distinct():
    table = pl.DataFrame(
        {
            "bloc": ["A", "A", "A", "B", "B", "B"],
            "x": [1.0, 2.0, 3.0, 1.0, 2.0, 3.0],
            "y": [1.0, 2.0, 3.0, 3.0, 2.0, 1.0],
        }
    )
    resultat = rho_par_bloc(table, "x", "y")
    rho_a = resultat.filter(pl.col("bloc") == "A").get_column("rho")[0]
    rho_b = resultat.filter(pl.col("bloc") == "B").get_column("rho")[0]
    assert rho_a == pytest.approx(1.0)
    assert rho_b == pytest.approx(-1.0)
    assert resultat.get_column("n").to_list() == [3, 3]


# --- Anti-fuite : le prédicteur 2022 est aveugle à 2024 -----------------------


def test_construire_predicteur_2022_invariant_si_2024_change():
    panel_a = _panel_complet_deux_unites(voix_2024_a=(10, 90), voix_2024_b=(90, 10))
    panel_b = _panel_complet_deux_unites(voix_2024_a=(99, 1), voix_2024_b=(1, 99))  # 2024 très différent
    predicteur_a = construire_predicteur_2022(panel_a)
    predicteur_b = construire_predicteur_2022(panel_b)
    assert predicteur_a.sort(["unite_id", "bloc"]).equals(predicteur_b.sort(["unite_id", "bloc"]))


def test_isoler_scrutins_2022_ne_garde_que_2022():
    panel = _panel_complet_deux_unites()
    isole = isoler_scrutins_2022(panel)
    assert set(isole.get_column("id_election").unique().to_list()) <= {"2022_pres_t1", SCRUTIN_LEGISLATIVES_2022}


def test_construire_predicteur_2022_ignore_une_colonne_2024_meme_si_panel_complet():
    # Même en passant un panel complet (avec 2024), le résultat ne doit
    # dépendre que des lignes 2022 -- vérifié en comparant à un panel où les
    # lignes 2024 ont été purement supprimées.
    panel_complet = _panel_complet_deux_unites()
    panel_sans_2024 = isoler_scrutins_2022(panel_complet)
    predicteur_complet = construire_predicteur_2022(panel_complet)
    predicteur_sans_2024 = construire_predicteur_2022(panel_sans_2024)
    assert predicteur_complet.sort(["unite_id", "bloc"]).equals(predicteur_sans_2024.sort(["unite_id", "bloc"]))


def test_construire_predicteur_2022_impute_depuis_la_presidentielle_pas_les_europeennes():
    # 69123 : offre complète aux législatives 2022 (Gauche + Droite présents).
    # 01001 : Droite absente des législatives 2022 -- doit être imputée depuis
    # la PRÉSIDENTIELLE 2022, jamais depuis les européennes 2024 (même très
    # différentes, cf. voix_2024_b).
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 60, 100),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 40, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 30, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 70, 100),
        _ligne("2022_legi_t1", "69123", "0001", "Gauche", 55, 100),
        _ligne("2022_legi_t1", "69123", "0001", "Droite", 45, 100),
        _ligne("2022_legi_t1", "01001", "0001", "Gauche", 100, 100),  # pas de candidat Droite
        _ligne("2024_euro_t1", "01001", "0001", "Droite", 1, 100),  # très différent, ne doit pas être vu
        _ligne("2024_euro_t1", "01001", "0001", "Gauche", 99, 100),
    ]
    panel = _panel(lignes)
    predicteur = construire_predicteur_2022(panel)
    ligne_manquante = predicteur.filter((pl.col("unite_id") == "01001_0001") & (pl.col("bloc") == "Droite"))
    valeur_imputee = ligne_manquante.get_column(f"ecart_{SCRUTIN_LEGISLATIVES_2022_CORRIGE}")[0]
    # La valeur imputée doit provenir de la structure présidentielle 2022 de
    # cette unité (70% Droite -> écart positif fort), pas de la structure
    # européenne 2024 (1% Droite -> écart très négatif).
    assert valeur_imputee > 0


# --- Tercile compétitif ---------------------------------------------------------


def test_tercile_competitif_tiers_central_bien_defini():
    # 9 valeurs distinctes 1..9 pour un bloc : le tiers central attendu est
    # exactement {4, 5, 6} (cf. docstring du module, calcul du percentile).
    table = pl.DataFrame({"bloc": ["A"] * 9, "unite_id": [f"u{i}" for i in range(1, 10)], "composite_2022": list(range(1, 10))})
    resultat = tercile_competitif(table)
    dans_le_tercile = set(
        resultat.filter(pl.col("tercile_competitif")).get_column("composite_2022").to_list()
    )
    assert dans_le_tercile == {4, 5, 6}


def test_tercile_competitif_est_calcule_par_bloc():
    # Bloc B a une distribution décalée : son tercile ne doit pas dépendre de A.
    table = pl.DataFrame(
        {
            "bloc": ["A"] * 9 + ["B"] * 9,
            "unite_id": [f"a{i}" for i in range(9)] + [f"b{i}" for i in range(9)],
            "composite_2022": list(range(1, 10)) + list(range(101, 110)),
        }
    )
    resultat = tercile_competitif(table)
    tercile_b = set(resultat.filter((pl.col("bloc") == "B") & pl.col("tercile_competitif")).get_column("composite_2022"))
    assert tercile_b == {104, 105, 106}


def test_tercile_competitif_valeur_nulle_jamais_dans_le_tercile():
    table = pl.DataFrame({"bloc": ["A"] * 4, "unite_id": ["u1", "u2", "u3", "u4"], "composite_2022": [1.0, None, 3.0, 4.0]})
    resultat = tercile_competitif(table)
    assert resultat.filter(pl.col("unite_id") == "u2").get_column("tercile_competitif")[0] is False


# --- Gate ADR 0001 : seuils synthétiques ----------------------------------------


def _resultats_synthetiques(rho_ens_composite, rho_ter_composite, rho_ens_mono, bloc="Extrême droite", cible="euro") -> pl.DataFrame:
    lignes = [
        {"predicteur": "composite", "cible": cible, "scope": "ensemble", "bloc": bloc, "rho": rho_ens_composite, "n": 100},
        {"predicteur": "composite", "cible": cible, "scope": "tercile", "bloc": bloc, "rho": rho_ter_composite, "n": 33},
        {"predicteur": "mono", "cible": cible, "scope": "ensemble", "bloc": bloc, "rho": rho_ens_mono, "n": 100},
        {"predicteur": "mono", "cible": cible, "scope": "tercile", "bloc": bloc, "rho": rho_ens_mono, "n": 33},
    ]
    return pl.DataFrame(lignes)


def test_evaluer_gate_pass_quand_les_3_clauses_sont_verifiees():
    resultats = _resultats_synthetiques(rho_ens_composite=0.8, rho_ter_composite=0.6, rho_ens_mono=0.7)
    verdict = evaluer_gate(resultats, blocs=("Extrême droite",))
    ligne = verdict.filter(pl.col("bloc") == "Extrême droite")
    assert ligne.get_column("pass_ensemble")[0] is True
    assert ligne.get_column("pass_tercile")[0] is True
    assert ligne.get_column("pass_composite_vs_mono")[0] is True
    assert ligne.get_column("pass_global")[0] is True
    assert verdict_global(verdict) is True


def test_evaluer_gate_fail_si_rho_ensemble_sous_le_seuil():
    resultats = _resultats_synthetiques(rho_ens_composite=0.65, rho_ter_composite=0.6, rho_ens_mono=0.5)
    verdict = evaluer_gate(resultats, blocs=("Extrême droite",))
    ligne = verdict.filter(pl.col("bloc") == "Extrême droite")
    assert ligne.get_column("pass_ensemble")[0] is False
    assert ligne.get_column("pass_global")[0] is False
    assert verdict_global(verdict) is False


def test_evaluer_gate_fail_si_rho_tercile_sous_le_seuil():
    resultats = _resultats_synthetiques(rho_ens_composite=0.8, rho_ter_composite=0.4, rho_ens_mono=0.5)
    verdict = evaluer_gate(resultats, blocs=("Extrême droite",))
    ligne = verdict.filter(pl.col("bloc") == "Extrême droite")
    assert ligne.get_column("pass_tercile")[0] is False
    assert ligne.get_column("pass_global")[0] is False


def test_evaluer_gate_fail_si_composite_moins_bon_que_mono():
    resultats = _resultats_synthetiques(rho_ens_composite=0.75, rho_ter_composite=0.6, rho_ens_mono=0.9)
    verdict = evaluer_gate(resultats, blocs=("Extrême droite",))
    ligne = verdict.filter(pl.col("bloc") == "Extrême droite")
    assert ligne.get_column("pass_composite_vs_mono")[0] is False
    assert ligne.get_column("pass_global")[0] is False


def test_evaluer_gate_seuils_a_la_limite_sont_pass():
    # >= strict, pas >, cf. ADR 0001 ("ρ ≥ 0,7").
    resultats = _resultats_synthetiques(rho_ens_composite=0.7, rho_ter_composite=0.5, rho_ens_mono=0.7)
    verdict = evaluer_gate(resultats, blocs=("Extrême droite",))
    ligne = verdict.filter(pl.col("bloc") == "Extrême droite")
    assert ligne.get_column("pass_global")[0] is True


def test_evaluer_gate_couvre_toutes_les_cibles_presentes():
    resultats = pl.concat(
        [
            _resultats_synthetiques(0.8, 0.6, 0.5, bloc="Gauche", cible="euro"),
            _resultats_synthetiques(0.4, 0.6, 0.5, bloc="Gauche", cible="legi"),
        ]
    )
    verdict = evaluer_gate(resultats, blocs=("Gauche",))
    assert set(verdict.get_column("cible").to_list()) == {"euro", "legi"}
    pass_par_cible = {row["cible"]: row["pass_global"] for row in verdict.iter_rows(named=True)}
    assert pass_par_cible["euro"] is True
    assert pass_par_cible["legi"] is False


# --- Distribution du swing + régularité -----------------------------------------


def test_distribution_swing_calcule_les_quantiles_attendus():
    table = pl.DataFrame({"bloc": ["Extrême droite"] * 5, "derive": [1.0, 2.0, 3.0, 4.0, 5.0]})
    resultat = distribution_swing(table)
    assert resultat["median"] == pytest.approx(3.0)
    assert resultat["min"] == pytest.approx(1.0)
    assert resultat["max"] == pytest.approx(5.0)
    assert resultat["n"] == 5


def test_verifier_regularite_seuil_pas_d_anomalie_sur_distribution_uniforme():
    table = pl.DataFrame({"bloc": ["Extrême droite"] * 100, "derive": [float(i) for i in range(100)]})
    resultat = verifier_regularite_seuil(table, n_bins=10)
    assert resultat["anomalie"] is False


def test_verifier_regularite_seuil_detecte_un_pic_au_seuil():
    # 90 valeurs concentrées exactement à la médiane (0.0), quelques valeurs
    # étalées autour pour donner un min/max non nul -- pic massif détecté.
    table = pl.DataFrame({"bloc": ["Extrême droite"] * 94, "derive": [0.0] * 90 + [-10.0, -5.0, 5.0, 10.0]})
    resultat = verifier_regularite_seuil(table, n_bins=10)
    assert resultat["anomalie"] is True


# --- correlation_euro_pres_rn : identique à la ligne mono/euro du backtest 1 --


def test_correlation_euro_pres_rn_egale_la_ligne_mono_euro_ensemble():
    table = pl.DataFrame(
        {
            "bloc": ["Extrême droite"] * 4,
            f"ecart_{SCRUTIN_PRESIDENTIELLE}": [1.0, 2.0, 3.0, 4.0],
            "ecart_2024_euro_t1": [10.0, 20.0, 30.0, 40.0],
        }
    )
    assert correlation_euro_pres_rn(table) == pytest.approx(1.0)
    rho_bloc = rho_par_bloc(table, f"ecart_{SCRUTIN_PRESIDENTIELLE}", "ecart_2024_euro_t1")
    assert correlation_euro_pres_rn(table) == pytest.approx(rho_bloc.get_column("rho")[0])


# --- Intégration sur l'extrait réel gelé ----------------------------------------


def test_construire_predicteur_2022_colonnes_attendues(panel_avec_statut_reel):
    predicteur = construire_predicteur_2022(panel_avec_statut_reel)
    assert {"unite_id", "bloc", f"ecart_{SCRUTIN_PRESIDENTIELLE}", "composite_2022"} <= set(predicteur.columns)
    assert predicteur.height > 0


def test_construire_table_backtest_colonnes_attendues(panel_avec_statut_reel, baseline_reel):
    table = construire_table_backtest(panel_avec_statut_reel, baseline_reel)
    colonnes_attendues = {
        "unite_id",
        "bloc",
        "composite_2022",
        "ecart_2024_euro_t1",
        "ecart_2024_legi_t1_corrige",
        "derive",
        "statut",
        "maille",
    }
    assert colonnes_attendues <= set(table.columns)


def test_executer_backtests_produit_toutes_les_combinaisons(panel_avec_statut_reel, baseline_reel):
    resultat = executer_backtests(panel_avec_statut_reel, baseline_reel)
    resultats = resultat["resultats"]
    assert set(resultats.get_column("predicteur").unique().to_list()) == {"mono", "composite"}
    assert set(resultats.get_column("cible").unique().to_list()) == {"euro", "legi"}
    assert set(resultats.get_column("scope").unique().to_list()) == {"ensemble", "tercile"}
    assert resultat["verdict"].height == len(BLOCS_MAJEURS) * 2  # 2 blocs majeurs x 2 cibles
    assert isinstance(resultat["correlation_euro_pres"], float)


def test_calibrer_poids_retourne_au_moins_3_jeux_de_poids(panel_avec_statut_reel, baseline_reel):
    calibration = calibrer_poids(panel_avec_statut_reel, baseline_reel)
    assert calibration.get_column("jeu_de_poids").n_unique() >= 3


def _resultats_participation_reels(panel_avec_statut_reel, baseline_reel):
    resultat = executer_backtests(panel_avec_statut_reel, baseline_reel)
    resultats_participation = executer_backtest_participation(panel_avec_statut_reel, baseline_reel)
    anti_hasard_structure = garde_anti_hasard_structure(resultat, panel_avec_statut_reel)
    anti_hasard_participation = garde_anti_hasard_participation(resultats_participation, panel_avec_statut_reel)
    return resultat, resultats_participation, anti_hasard_structure, anti_hasard_participation


def test_generer_rapport_backtest_contient_les_sections_attendues(panel_avec_statut_reel, baseline_reel):
    resultat, resultats_participation, anti_hasard_structure, anti_hasard_participation = (
        _resultats_participation_reels(panel_avec_statut_reel, baseline_reel)
    )
    calibration = calibrer_poids(panel_avec_statut_reel, baseline_reel)
    rapport = generer_rapport_backtest(
        resultat,
        calibration,
        poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT,
        methode_correction="imputation",
        n_total=100,
        n_perimetre=90,
        resultats_participation=resultats_participation,
        anti_hasard_structure=anti_hasard_structure,
        anti_hasard_participation=anti_hasard_participation,
    )
    for section in (
        "Note d'étanchéité",
        "Périmètre",
        "Tercile compétitif",
        "Corrélation de rang 2022→2024",
        "Verdict du gate",
        "Corrélation géographique RN",
        "Distribution du swing",
        "Condition de régularité",
        "Calibration des poids",
        "Backtest participation",
        "Garde anti-hasard",
        "carte mobilisation",
    ):
        assert section in rapport


def test_generer_rapport_backtest_est_deterministe(panel_avec_statut_reel, baseline_reel):
    # Déterminisme (acceptance criteria #24) : mêmes entrées -> texte identique,
    # condition nécessaire à la régénération byte-identique CLI / notebook.
    resultat, resultats_participation, anti_hasard_structure, anti_hasard_participation = (
        _resultats_participation_reels(panel_avec_statut_reel, baseline_reel)
    )
    calibration = calibrer_poids(panel_avec_statut_reel, baseline_reel)
    args = dict(
        poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT,
        methode_correction="imputation",
        n_total=100,
        n_perimetre=90,
        resultats_participation=resultats_participation,
        anti_hasard_structure=anti_hasard_structure,
        anti_hasard_participation=anti_hasard_participation,
    )
    rapport_1 = generer_rapport_backtest(resultat, calibration, **args)
    rapport_2 = generer_rapport_backtest(resultat, calibration, **args)
    assert rapport_1 == rapport_2


def test_generer_rapport_complet_identique_a_l_assemblage_manuel(panel_avec_statut_reel, baseline_reel):
    # Verrou CLI <-> notebook (revue PR #27) : le chemin partagé produit
    # exactement ce que l'assemblage manuel produisait.
    resultat, resultats_participation, anti_hasard_structure, anti_hasard_participation = (
        _resultats_participation_reels(panel_avec_statut_reel, baseline_reel)
    )
    calibration = calibrer_poids(panel_avec_statut_reel, baseline_reel)
    table_brute = construire_table_backtest(panel_avec_statut_reel, baseline_reel)
    attendu = generer_rapport_backtest(
        resultat,
        calibration,
        poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT,
        methode_correction="imputation",
        n_total=table_brute.height,
        n_perimetre=resultat["table"].height,
        resultats_participation=resultats_participation,
        anti_hasard_structure=anti_hasard_structure,
        anti_hasard_participation=anti_hasard_participation,
    )
    sortie = generer_rapport_complet(panel_avec_statut_reel, baseline_reel)
    assert sortie["rapport"] == attendu
    assert isinstance(sortie["pass_gate_adr_0001"], bool)
    assert isinstance(sortie["pass_carte_mobilisation"], bool)


def test_notebook_regenere_par_le_meme_chemin_que_le_cli():
    # Le notebook ne réassemble pas le rapport à la main : il doit passer par
    # generer_rapport_complet, l'unique chemin partagé avec `uv run backtest`.
    source = (Path(__file__).parent.parent / "notebooks" / "backtest_2022_2024.py").read_text(encoding="utf-8")
    assert "generer_rapport_complet(" in source
    assert "generer_rapport_backtest(" not in source


# --- Backtest participation (ADR 0002) ------------------------------------------


def test_calculer_taux_abstention_deduplique_par_bloc_et_calcule_le_taux():
    # 2 lignes de bloc pour le même bureau x scrutin (abstentions/inscrits
    # répétés) : le taux ne doit apparaître qu'une fois, calculé depuis les
    # comptes (20/200 = 0.1), jamais une moyenne de taux déjà calculés.
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 60, 100, abstentions=20, inscrits=200),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 40, 100, abstentions=20, inscrits=200),
    ]
    resultat = calculer_taux_abstention(_panel(lignes), scrutins=("2022_pres_t1",))
    assert resultat.height == 1
    assert resultat.get_column("taux_abstention")[0] == pytest.approx(0.1)


def test_calculer_taux_abstention_exprimes_nul_donne_null_jamais_nan():
    lignes = [_ligne("2022_pres_t1", "69123", "0001", "Gauche", 0, 0, abstentions=10, inscrits=0)]
    resultat = calculer_taux_abstention(_panel(lignes), scrutins=("2022_pres_t1",))
    assert resultat.get_column("taux_abstention").null_count() == 1
    assert not resultat.get_column("taux_abstention").is_nan().any()


def test_construire_table_participation_colonnes_attendues(panel_avec_statut_reel, baseline_reel):
    table = construire_table_participation(panel_avec_statut_reel, baseline_reel)
    colonnes_attendues = {
        "unite_id",
        COLONNE_ABSTENTION_PREDICTEUR,
        *CIBLES_PARTICIPATION.values(),
        "code_departement",
        "statut",
        "maille",
    }
    assert colonnes_attendues <= set(table.columns)


def test_executer_backtest_participation_calcule_un_rho_par_cible(panel_avec_statut_reel, baseline_reel):
    resultat = executer_backtest_participation(panel_avec_statut_reel, baseline_reel)
    resultats = resultat["resultats"]
    assert set(resultats.get_column("cible").unique().to_list()) == set(CIBLES_PARTICIPATION)
    assert isinstance(resultat["rho_inter_cibles"], float)
    assert resultat["n_inter_cibles"] > 0
    assert "pass_global" in resultats.columns


def test_evaluer_gate_participation_seuil_a_la_limite_est_pass():
    # >= strict, pas > (même convention que le gate ADR 0001) : ρ = 0,8 pile PASS.
    resultats = pl.DataFrame({"cible": ["euro"], "rho": [0.8], "n": [100]})
    verdict = evaluer_gate_participation(resultats)
    assert verdict.get_column("pass_global")[0] is True
    assert verdict_global(verdict) is True


def test_evaluer_gate_participation_juste_sous_le_seuil_est_fail():
    resultats = pl.DataFrame({"cible": ["euro"], "rho": [0.7999], "n": [100]})
    verdict = evaluer_gate_participation(resultats)
    assert verdict.get_column("pass_global")[0] is False
    assert verdict_global(verdict) is False


def test_evaluer_gate_participation_seuil_gele_a_0_8():
    # Clause pré-enregistrée ADR 0002 : le seuil ne doit pas dériver silencieusement.
    assert SEUIL_RHO_PARTICIPATION == 0.8


# --- Garde anti-hasard : prédicteur département (structure) -------------------


def test_calculer_ecart_national_departement_recalcule_par_sommes_jamais_moyenne():
    # Département 69 : 2 bureaux à 50/50 (moyenne des écarts bureau = 0 par
    # construction, quel que soit leur poids). Département 01 : 1 gros bureau
    # à 90% Gauche. Recalculé par sommes de voix/exprimés (jamais par moyenne
    # des écarts de bureau), le département 69 doit rester à un écart nul.
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 50, 100, code_departement="69"),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 50, 100, code_departement="69"),
        _ligne("2022_pres_t1", "69456", "0001", "Gauche", 50, 100, code_departement="69"),
        _ligne("2022_pres_t1", "69456", "0001", "Droite", 50, 100, code_departement="69"),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 9000, 10000, code_departement="01"),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 1000, 10000, code_departement="01"),
    ]
    resultat = calculer_ecart_national_departement(_panel(lignes))
    ecart_69 = resultat.filter((pl.col("unite_id") == "69") & (pl.col("bloc") == "Gauche")).get_column(
        "ecart_national"
    )[0]
    national_gauche = (50 + 50 + 9000) / (100 + 100 + 10000)
    assert ecart_69 == pytest.approx((0.5 - national_gauche) * 100)


def test_construire_predicteur_departemental_2022_invariant_si_2024_change():
    panel_a = _panel_complet_deux_unites(voix_2024_a=(10, 90), voix_2024_b=(90, 10))
    panel_b = _panel_complet_deux_unites(voix_2024_a=(99, 1), voix_2024_b=(1, 99))
    predicteur_a = construire_predicteur_departemental_2022(panel_a)
    predicteur_b = construire_predicteur_departemental_2022(panel_b)
    assert predicteur_a.sort(["code_departement", "bloc"]).equals(predicteur_b.sort(["code_departement", "bloc"]))


def test_construire_predicteur_departemental_2022_colonnes_attendues(panel_avec_statut_reel):
    predicteur = construire_predicteur_departemental_2022(panel_avec_statut_reel)
    assert {"code_departement", "bloc", "composite_2022"} <= set(predicteur.columns)
    assert predicteur.height > 0


# --- Garde anti-hasard : prédicteur département (participation) ---------------


def test_calculer_taux_abstention_departement_calcule_par_sommes_jamais_moyenne_des_taux():
    # 2 bureaux du même département à taux d'abstention très différents et à
    # poids d'inscrits très différents : le taux départemental doit être la
    # somme des abstentions sur la somme des inscrits, PAS la moyenne (0.5)
    # des 2 taux de bureau (0.1 et 0.9).
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 10, 100, abstentions=10, inscrits=100),
        _ligne("2022_pres_t1", "69456", "0001", "Gauche", 10, 100, abstentions=900, inscrits=1000),
    ]
    resultat = calculer_taux_abstention_departement(_panel(lignes), scrutin="2022_pres_t1")
    taux = resultat.get_column("abstention_departement_2022")[0]
    moyenne_naive = (0.1 + 0.9) / 2
    taux_par_sommes = (10 + 900) / (100 + 1000)
    assert taux == pytest.approx(taux_par_sommes)
    assert taux != pytest.approx(moyenne_naive)


def test_calculer_taux_abstention_departement_ignore_les_donnees_2024():
    lignes_a = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 10, 100, abstentions=10, inscrits=100),
        _ligne("2024_euro_t1", "69123", "0001", "Gauche", 10, 100, abstentions=10, inscrits=100),
    ]
    lignes_b = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 10, 100, abstentions=10, inscrits=100),
        _ligne("2024_euro_t1", "69123", "0001", "Gauche", 90, 100, abstentions=90, inscrits=100),
    ]
    resultat_a = calculer_taux_abstention_departement(_panel(lignes_a), scrutin="2022_pres_t1")
    resultat_b = calculer_taux_abstention_departement(_panel(lignes_b), scrutin="2022_pres_t1")
    assert resultat_a.equals(resultat_b)


# --- Garde anti-hasard : verdict bureau vs département + hasard ---------------


def test_verdict_anti_hasard_pass_quand_bureau_bat_departement():
    verdict = verdict_anti_hasard(rho_bureau=0.9, rho_departement=0.5)
    assert verdict["rho_hasard"] == 0.0
    assert verdict["lift_vs_hasard"] == pytest.approx(0.9)
    assert verdict["lift_vs_departement"] == pytest.approx(0.4)
    assert verdict["pass_global"] is True


def test_verdict_anti_hasard_a_egalite_ne_bat_pas_donc_fail():
    # Frontière de la clause : "battre" (ADR 0002) exige un >, pas un >= --
    # à égalité, le bureau ne bat pas le département.
    verdict = verdict_anti_hasard(rho_bureau=0.7, rho_departement=0.7)
    assert verdict["pass_global"] is False


def test_verdict_anti_hasard_fail_si_rho_departement_indefini():
    verdict = verdict_anti_hasard(rho_bureau=0.9, rho_departement=float("nan"))
    assert verdict["pass_global"] is False


def test_garde_anti_hasard_structure_produit_toutes_les_combinaisons(panel_avec_statut_reel, baseline_reel):
    resultat = executer_backtests(panel_avec_statut_reel, baseline_reel)
    anti_hasard = garde_anti_hasard_structure(resultat, panel_avec_statut_reel)
    assert set(anti_hasard.get_column("bloc").unique().to_list()) == set(BLOCS_MAJEURS)
    assert anti_hasard.height == len(BLOCS_MAJEURS) * len(CIBLES)
    assert "pass_global" in anti_hasard.columns


def test_garde_anti_hasard_participation_produit_toutes_les_cibles(panel_avec_statut_reel, baseline_reel):
    resultats_participation = executer_backtest_participation(panel_avec_statut_reel, baseline_reel)
    anti_hasard = garde_anti_hasard_participation(resultats_participation, panel_avec_statut_reel)
    assert set(anti_hasard.get_column("cible").unique().to_list()) == set(CIBLES_PARTICIPATION)
    assert "pass_global" in anti_hasard.columns


# --- Verdict global carte mobilisation (ADR 0002, point 5) ---------------------


def _verdict_pass(cible="euro"):
    return pl.DataFrame({"cible": [cible], "pass_global": [True]})


def _verdict_fail(cible="euro"):
    return pl.DataFrame({"cible": [cible], "pass_global": [False]})


def test_verdict_carte_mobilisation_pass_quand_tout_est_vert():
    assert verdict_carte_mobilisation(_verdict_pass(), _verdict_pass(), _verdict_pass()) is True


def test_verdict_carte_mobilisation_fail_si_participation_fail():
    assert verdict_carte_mobilisation(_verdict_fail(), _verdict_pass(), _verdict_pass()) is False


def test_verdict_carte_mobilisation_fail_si_anti_hasard_structure_fail():
    assert verdict_carte_mobilisation(_verdict_pass(), _verdict_fail(), _verdict_pass()) is False


def test_verdict_carte_mobilisation_fail_si_anti_hasard_participation_fail():
    assert verdict_carte_mobilisation(_verdict_pass(), _verdict_pass(), _verdict_fail()) is False


# --- Entrée console `uv run backtest` -------------------------------------------


def test_main_ecrit_le_rapport_et_les_donnees(tmp_path, monkeypatch, panel_avec_statut_reel, baseline_reel):
    panel_in = tmp_path / "panel_avec_statut.parquet"
    baseline_in = tmp_path / "baseline_unite_bloc.parquet"
    sortie = tmp_path / "backtest-2022-2024.md"
    panel_avec_statut_reel.write_parquet(panel_in)
    baseline_reel.write_parquet(baseline_in)
    monkeypatch.setattr(
        "sys.argv",
        ["backtest", "--panel", str(panel_in), "--baseline", str(baseline_in), "--out", str(sortie)],
    )
    main()
    assert sortie.exists()
    assert "Backtest 2022" in sortie.read_text(encoding="utf-8")

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
    POIDS_COMPOSITE_2022_PAR_DEFAUT,
    SCRUTIN_LEGISLATIVES_2022,
    SCRUTIN_LEGISLATIVES_2022_CORRIGE,
    calibrer_poids,
    construire_predicteur_2022,
    construire_table_backtest,
    correlation_euro_pres_rn,
    correlation_spearman,
    distribution_swing,
    evaluer_gate,
    executer_backtests,
    generer_rapport_backtest,
    isoler_scrutins_2022,
    main,
    rho_par_bloc,
    tercile_competitif,
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


def _ligne(id_election, code_commune, code_bv, bloc, voix, exprimes, code_departement="69"):
    id_bv = f"{code_commune}_{code_bv}"
    return {
        "id_election": id_election,
        "code_departement": code_departement,
        "code_commune": code_commune,
        "code_bv": code_bv,
        "id_bv": id_bv,
        "bloc": bloc,
        "voix": voix,
        "inscrits": exprimes + 50,
        "abstentions": 10,
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


def test_generer_rapport_backtest_contient_les_sections_attendues(panel_avec_statut_reel, baseline_reel):
    resultat = executer_backtests(panel_avec_statut_reel, baseline_reel)
    calibration = calibrer_poids(panel_avec_statut_reel, baseline_reel)
    rapport = generer_rapport_backtest(
        resultat,
        calibration,
        poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT,
        methode_correction="imputation",
        n_total=100,
        n_perimetre=90,
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
    ):
        assert section in rapport


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

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl

    from projections.backtest import (
        INTERIM_DIR,
        POIDS_COMPOSITE_2022_PAR_DEFAUT,
        calibrer_poids,
        construire_table_backtest,
        evaluer_gate_participation_relatif,
        executer_backtest_participation,
        executer_backtests,
        garde_anti_hasard_participation,
        garde_anti_hasard_structure,
        generer_rapport_complet,
        verdict_carte_mobilisation,
        verdict_global,
    )

    return (
        INTERIM_DIR,
        POIDS_COMPOSITE_2022_PAR_DEFAUT,
        calibrer_poids,
        construire_table_backtest,
        evaluer_gate_participation_relatif,
        executer_backtest_participation,
        executer_backtests,
        garde_anti_hasard_participation,
        garde_anti_hasard_structure,
        generer_rapport_complet,
        mo,
        pl,
        verdict_carte_mobilisation,
        verdict_global,
    )


@app.cell
def _(mo):
    mo.md("""
    # Backtest 2022→2024 et verdict du gate (ADR 0001 + ADR 0002)

    Shell fin : toute la logique (prédicteur 2022 anti-fuite, Spearman en Polars
    pur, tercile compétitif, gate ADR 0001, calibration des poids, backtest
    participation + garde anti-hasard ADR 0002 issue #24) vit dans
    `projections.backtest`, unit-testée dans `tests/test_backtest.py`. Ce notebook
    charge les 2 artefacts intermédiaires déjà reproductibles par leurs propres
    entrées console (`uv run rapport-churn` -> `panel_avec_statut.parquet`,
    `uv run baseline` -> `baseline_unite_bloc.parquet`), appelle les fonctions de
    `projections.backtest`, et publie `backtest-2022-2024.md` à la racine du
    dépôt — destiné à être **publié avec les cartes**.
    """)
    return


@app.cell
def _(mo):
    mo.md("""## 1. Chargement du panel avec statut (étape 0) et de la baseline (étape 1, issue #5)""")
    return


@app.cell
def _(INTERIM_DIR, pl):
    panel_avec_statut = pl.read_parquet(INTERIM_DIR / "panel_avec_statut.parquet")
    panel_avec_statut.get_column("statut").value_counts()
    return (panel_avec_statut,)


@app.cell
def _(INTERIM_DIR, pl):
    baseline = pl.read_parquet(INTERIM_DIR / "baseline_unite_bloc.parquet")
    baseline.height
    return (baseline,)


@app.cell
def _(mo):
    mo.md("""
    ## 2. Backtest (étape 2, issue #6)

    Prédicteur 2022 anti-fuite (`construire_predicteur_2022` : présidentielle
    2022 seule, ou composite présidentielle + législatives 2022 corrigées en
    imputant depuis la présidentielle 2022 — jamais depuis les européennes
    2024), corrélé (Spearman, Polars pur) aux cibles 2024 observées
    (européennes, législatives corrigées), sur les unités joint-validées
    uniquement, ensemble et tercile compétitif.
    """)
    return


@app.cell
def _(POIDS_COMPOSITE_2022_PAR_DEFAUT, baseline, executer_backtests, panel_avec_statut):
    resultats_backtest = executer_backtests(
        panel_avec_statut, baseline, poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT
    )
    resultats_backtest["resultats"]
    return (resultats_backtest,)


@app.cell
def _(resultats_backtest):
    resultats_backtest["verdict"]
    return


@app.cell
def _(resultats_backtest, verdict_global):
    f"gate ADR 0001 : {'PASS' if verdict_global(resultats_backtest['verdict']) else 'FAIL'}"
    return


@app.cell
def _(mo):
    mo.md("""## 3. Calibration des poids du composite 2022 (promesse de l'issue #5)""")
    return


@app.cell
def _(baseline, calibrer_poids, panel_avec_statut):
    calibration = calibrer_poids(panel_avec_statut, baseline)
    calibration
    return (calibration,)


@app.cell
def _(mo):
    mo.md("""## 4. Périmètre (unités jointes prédicteur × cible, avant filtre joint_valide)""")
    return


@app.cell
def _(baseline, construire_table_backtest, panel_avec_statut):
    table_brute = construire_table_backtest(panel_avec_statut, baseline)
    table_brute.height
    return (table_brute,)


@app.cell
def _(mo):
    mo.md("""
    ## 5. Backtest participation + garde anti-hasard (ADR 0002, issue #24)

    Deux clauses pré-enregistrées qui conditionnent la publication de la carte
    mobilisation (postérieures aux seuils, commit docs de la branche) : le
    backtest participation (persistance de l'abstention 2022→2024, ρ ≥ 0,8 par
    cible, ABSOLU) et la garde anti-hasard (la granularité bureau doit battre la
    granularité département sur la métrique principale de chaque backtest). Le
    seuil absolu est sorti rouge sur la cible européennes (0,769 < 0,8) : la
    clause qui gouverne effectivement la publication est désormais la clause
    révisée ADR 0003 (relative au plafond inter-cibles, section 5bis ci-dessous).
    """)
    return


@app.cell
def _(baseline, executer_backtest_participation, panel_avec_statut):
    resultats_participation = executer_backtest_participation(panel_avec_statut, baseline)
    resultats_participation["resultats"]
    return (resultats_participation,)


@app.cell
def _(garde_anti_hasard_structure, panel_avec_statut, resultats_backtest):
    anti_hasard_structure = garde_anti_hasard_structure(resultats_backtest, panel_avec_statut)
    anti_hasard_structure
    return (anti_hasard_structure,)


@app.cell
def _(garde_anti_hasard_participation, panel_avec_statut, resultats_participation):
    anti_hasard_participation = garde_anti_hasard_participation(resultats_participation, panel_avec_statut)
    anti_hasard_participation
    return (anti_hasard_participation,)


@app.cell
def _(mo):
    mo.md("""
    ### 5bis. Clause participation révisée (ADR 0003, issue #28/#30)

    Le seuil absolu ci-dessus est rendu à sa grandeur (test de même enjeu
    2017→2022, calcul différé) : la clause qui gouverne la publication devient
    relative au plafond inter-cibles mesuré sur le même périmètre.
    """)
    return


@app.cell
def _(evaluer_gate_participation_relatif, resultats_participation):
    verdict_participation_relatif = evaluer_gate_participation_relatif(resultats_participation)
    verdict_participation_relatif
    return (verdict_participation_relatif,)


@app.cell
def _(
    anti_hasard_participation,
    anti_hasard_structure,
    verdict_carte_mobilisation,
    verdict_participation_relatif,
):
    f"carte mobilisation PASS (ADR 0002/0003) : {verdict_carte_mobilisation(verdict_participation_relatif, anti_hasard_structure, anti_hasard_participation)}"
    return


@app.cell
def _(mo):
    mo.md("""## 6. Rapport publié : `backtest-2022-2024.md`""")
    return


@app.cell
def _(baseline, generer_rapport_complet, mo, panel_avec_statut):
    # Même chemin que `uv run backtest` : la byte-identité CLI/notebook est
    # structurelle (les cellules ci-dessus ne servent qu'à l'exploration).
    rapport = generer_rapport_complet(panel_avec_statut, baseline)["rapport"]
    mo.md(rapport)
    return (rapport,)


@app.cell
def _(rapport):
    from pathlib import Path

    sortie = Path("backtest-2022-2024.md")
    sortie.write_text(rapport, encoding="utf-8")
    f"rapport écrit : {sortie.resolve()}"
    return


if __name__ == "__main__":
    app.run()

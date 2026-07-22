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
        executer_backtests,
        generer_rapport_backtest,
        verdict_global,
    )

    return (
        INTERIM_DIR,
        POIDS_COMPOSITE_2022_PAR_DEFAUT,
        calibrer_poids,
        construire_table_backtest,
        executer_backtests,
        generer_rapport_backtest,
        mo,
        pl,
        verdict_global,
    )


@app.cell
def _(mo):
    mo.md("""
    # Backtest 2022→2024 et verdict du gate (ADR 0001)

    Shell fin : toute la logique (prédicteur 2022 anti-fuite, Spearman en Polars
    pur, tercile compétitif, gate ADR 0001, calibration des poids) vit dans
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
    mo.md("""## 5. Rapport publié : `backtest-2022-2024.md`""")
    return


@app.cell
def _(
    POIDS_COMPOSITE_2022_PAR_DEFAUT,
    calibration,
    generer_rapport_backtest,
    mo,
    resultats_backtest,
    table_brute,
):
    rapport = generer_rapport_backtest(
        resultats_backtest,
        calibration,
        poids_composite_2022=POIDS_COMPOSITE_2022_PAR_DEFAUT,
        methode_correction="imputation",
        n_total=table_brute.height,
        n_perimetre=resultats_backtest["table"].height,
    )
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

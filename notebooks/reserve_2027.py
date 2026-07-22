import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl

    from projections.reserve import (
        INTERIM_DIR,
        METHODE_PART_DEFAUT,
        calculer_donnees_reserve,
        generer_rapport_complet,
        sensibilite_h1,
        top_gisements_bureau,
        top_gisements_departement,
    )

    return (
        INTERIM_DIR,
        METHODE_PART_DEFAUT,
        calculer_donnees_reserve,
        generer_rapport_complet,
        mo,
        pl,
        sensibilite_h1,
        top_gisements_bureau,
        top_gisements_departement,
    )


@app.cell
def _(mo):
    mo.md("""
    # Réserve de voix par bureau × bloc — estimateur v1 (issue #25, ADR 0002)

    Shell fin : toute la logique (formule v1, méthodes H1, sensibilité, top
    gisements, lift bureau/département — réutilisation #24) vit dans
    `projections.reserve`, unit-testée dans `tests/test_reserve.py`. Ce notebook
    charge les 2 artefacts intermédiaires déjà reproductibles par leurs propres
    entrées console (`uv run rapport-churn` -> `panel_avec_statut.parquet`,
    `uv run baseline` -> `baseline_unite_bloc.parquet`), appelle les fonctions de
    `projections.reserve`, et publie `reserve-2027.md` à la racine du dépôt.

    Couche *estimation* du pivot mobilisation (`docs/adr/0002-pivot-mobilisation-reserve.md`),
    non backtestable par construction : voir le rapport pour le verdict de
    publication en carte (hérité du gate ADR 0002, clause participation révisée
    par l'ADR 0003 -- `docs/adr/0003-clause-participation-plafond-relatif.md`).
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
    mo.md("""## 2. Table réserve (méthode H1 par défaut) + sensibilité + tops (issue #25)""")
    return


@app.cell
def _(baseline, calculer_donnees_reserve, panel_avec_statut):
    donnees = calculer_donnees_reserve(panel_avec_statut, baseline)
    donnees["table_reserve"]
    return (donnees,)


@app.cell
def _(donnees):
    donnees["sensibilite_h1"]
    return


@app.cell
def _(donnees):
    donnees["top_gisements_bureau"]
    return


@app.cell
def _(donnees):
    donnees["top_gisements_departement"]
    return


@app.cell
def _(donnees):
    donnees["lift_bureau_vs_departement"]
    return


@app.cell
def _(donnees):
    f"publication en carte autorisée (ADR 0002/0003) : {donnees['pass_carte_mobilisation']}"
    return


@app.cell
def _(mo):
    mo.md("""## 3. Rapport publié : `reserve-2027.md`""")
    return


@app.cell
def _(baseline, generer_rapport_complet, mo, panel_avec_statut):
    # Même chemin que `uv run reserve` : la byte-identité CLI/notebook est
    # structurelle (les cellules ci-dessus ne servent qu'à l'exploration).
    sortie = generer_rapport_complet(panel_avec_statut, baseline)
    rapport = sortie["rapport"]
    mo.md(rapport)
    return (rapport, sortie)


@app.cell
def _(rapport, sortie):
    from pathlib import Path

    chemin_rapport = Path("reserve-2027.md")
    chemin_rapport.write_text(rapport, encoding="utf-8")
    chemin_table = Path("data/interim/reserve_bureau_bloc.parquet")
    sortie["table_reserve"].write_parquet(chemin_table)
    f"rapport écrit : {chemin_rapport.resolve()} / table : {chemin_table.resolve()}"
    return


if __name__ == "__main__":
    app.run()

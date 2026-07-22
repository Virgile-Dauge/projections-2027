import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl

    from projections.churn import (
        SCRUTIN_REFERENCE_INSCRITS,
        classifier_communes,
        construire_panel_avec_statut,
        generer_rapport_churn,
    )
    from projections.ingest import RAW_DIR, ingest

    return (
        RAW_DIR,
        SCRUTIN_REFERENCE_INSCRITS,
        classifier_communes,
        construire_panel_avec_statut,
        generer_rapport_churn,
        ingest,
        mo,
        pl,
    )


@app.cell
def _(mo):
    mo.md("""
    # Rapport de churn — étape 0

    Shell fin : toute la logique (classification stable/instable, repli à
    la maille communale, statistiques) vit dans `projections.churn` et
    `projections.ingest`, unit-testée dans `tests/test_churn.py`. Ce
    notebook charge les données réelles, appelle ces fonctions, et publie
    `rapport-churn.md` à la racine du dépôt.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 1. Ingestion des 4 scrutins sources
    """)
    return


@app.cell
def _(RAW_DIR, ingest, pl):
    general_results = pl.read_parquet(RAW_DIR / "general_results.parquet")
    candidats_results = pl.read_parquet(RAW_DIR / "candidats_results.parquet")
    panel = ingest(general_results, candidats_results)
    panel.height
    return (panel,)


@app.cell
def _(mo):
    mo.md("""
    ## 2. Classification stable / instable par commune
    """)
    return


@app.cell
def _(classifier_communes, panel):
    classification = classifier_communes(panel)
    classification
    return (classification,)


@app.cell
def _(mo):
    mo.md("""
    ## 3. Panel final : jointure directe ou repli, jamais de troisième état
    """)
    return


@app.cell
def _(classification, construire_panel_avec_statut, panel):
    panel_avec_statut = construire_panel_avec_statut(panel, classification)
    panel_avec_statut.get_column("statut").value_counts()
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4. Rapport publié : `rapport-churn.md`
    """)
    return


@app.cell
def _(SCRUTIN_REFERENCE_INSCRITS, generer_rapport_churn, mo, panel):
    rapport = generer_rapport_churn(panel, scrutin_reference=SCRUTIN_REFERENCE_INSCRITS)
    mo.md(rapport)
    return (rapport,)


@app.cell
def _(rapport):
    from pathlib import Path

    sortie = Path("rapport-churn.md")
    sortie.write_text(rapport, encoding="utf-8")
    f"rapport écrit : {sortie.resolve()}"
    return


if __name__ == "__main__":
    app.run()

"""Préparation des données carte : scores descriptifs par bureau et par commune.

Depuis le panel bureau × scrutin × bloc (`projections.ingest.ingest`), pour UN
scrutin paramétrable (défaut : `2024_legi_t1`), calcule par maille (bureau ou
commune) : le bloc en tête, le % des exprimés par bloc, et la participation.

Ce sont des résultats **réels et observés** d'un scrutin passé — descriptif, pas
une projection. L'ADR 0001 (`docs/adr/0001-sortie-ordinale-gate-backtest.md`)
interdit d'afficher un pourcentage PROJETÉ à intervalle de confiance par bureau ;
elle ne concerne pas des résultats officiels déjà connus.

Garde-fou repris de `projections.ingest.ingest` : les colonnes de participation
(inscrits, abstentions, votants, exprimes) sont répétées sur chaque ligne de bloc
d'un même bureau × scrutin. Toute agrégation (vers la commune, ou simplement pour
lire la participation d'un bureau) déduplique d'abord par (id_election, id_bv) —
sans quoi la participation serait comptée une fois par bloc présent.

L'agrégat commune (`scores_commune`, pour le dézoom carte) suit la règle
`docs/heritage-2024.md` : jamais de moyenne de pourcentages, toujours une somme
de voix recalculée en pourcentage.
"""

from __future__ import annotations

import polars as pl

# Les 5 blocs (docs/classification_en_blocs.md) -> slug pour les noms de colonne
# / propriétés GeoJSON (pas d'accent, pas d'espace).
BLOC_SLUG: dict[str, str] = {
    "Gauche": "gauche",
    "Centre": "centre",
    "Droite": "droite",
    "Extrême droite": "extreme_droite",
    "Divers": "divers",
}

COLONNES_PARTICIPATION: tuple[str, ...] = ("inscrits", "abstentions", "votants", "exprimes")


def _dedupliquer_participation(panel_scrutin: pl.DataFrame, cle: str) -> pl.DataFrame:
    """Une ligne par bureau : neutralise la répétition des colonnes de participation par bloc."""
    return panel_scrutin.unique(subset=["id_bv"]).select(
        cle, "code_commune", "code_departement", *COLONNES_PARTICIPATION
    )


def _bloc_tete_et_pct(voix_par_bloc: pl.DataFrame, cle: str, exprimes: pl.DataFrame) -> pl.DataFrame:
    """Depuis les voix par bloc et l'exprimé de chaque maille : bloc en tête + % par bloc.

    `voix_par_bloc` : colonnes (cle, bloc, voix). `exprimes` : colonnes (cle, exprimes).
    """
    bloc_tete = (
        voix_par_bloc.sort("voix", descending=True)
        .group_by(cle, maintain_order=True)
        .agg(pl.col("bloc").first().alias("bloc_tete"))
    )
    pct = voix_par_bloc.join(exprimes, on=cle).with_columns(
        pl.when(pl.col("exprimes") > 0)
        .then(pl.col("voix") / pl.col("exprimes") * 100)
        .otherwise(0.0)
        .alias("pct")
    )
    pct_large = pct.pivot(on="bloc", index=cle, values="pct").fill_null(0.0)
    # Un bloc absent de toute la maille (aucune ligne) n'a pas de colonne après pivot :
    # on la crée à 0 pour garantir les 5 colonnes pct_<bloc> en sortie.
    manquantes = {
        f"pct_{slug}": pl.lit(0.0) for bloc, slug in BLOC_SLUG.items() if bloc not in pct_large.columns
    }
    if manquantes:
        pct_large = pct_large.with_columns(**manquantes)
    renommage = {bloc: f"pct_{slug}" for bloc, slug in BLOC_SLUG.items() if bloc in pct_large.columns}
    pct_large = pct_large.rename(renommage)
    return bloc_tete.join(pct_large, on=cle)


def _colonnes_sortie(cle: str) -> list[str]:
    """Colonnes de sortie, dédupliquées : `cle` vaut `code_commune` pour scores_commune."""
    colonnes = [
        cle,
        "code_commune",
        "code_departement",
        "bloc_tete",
        *[f"pct_{slug}" for slug in BLOC_SLUG.values()],
        "participation",
        "inscrits",
        "exprimes",
    ]
    vues: list[str] = []
    for colonne in colonnes:
        if colonne not in vues:
            vues.append(colonne)
    return vues


def scores_bureau(panel: pl.DataFrame, id_election: str = "2024_legi_t1") -> pl.DataFrame:
    """Par bureau (`id_bv`) : bloc en tête, % des exprimés par bloc, participation.

    Résultats réels du scrutin `id_election` (descriptif, voir docstring module).
    """
    panel_scrutin = panel.filter(pl.col("id_election") == id_election)
    participation = _dedupliquer_participation(panel_scrutin, "id_bv")
    voix_par_bloc = panel_scrutin.group_by("id_bv", "bloc").agg(pl.col("voix").sum())
    scores = _bloc_tete_et_pct(voix_par_bloc, "id_bv", participation.select("id_bv", "exprimes"))
    resultat = participation.join(scores, on="id_bv").with_columns(
        pl.when(pl.col("inscrits") > 0)
        .then(pl.col("votants") / pl.col("inscrits") * 100)
        .otherwise(0.0)
        .alias("participation")
    )
    return resultat.select(_colonnes_sortie("id_bv"))


def scores_commune(panel: pl.DataFrame, id_election: str = "2024_legi_t1") -> pl.DataFrame:
    """Par commune (`code_commune`) : agrégat des bureaux calculé PAR LES VOIX.

    Jamais de moyenne des % de bureau (docs/heritage-2024.md) : les voix de
    chaque bloc et les effectifs de participation sont sommés sur les bureaux de
    la commune, puis le % est recalculé sur ces sommes. Sert au dézoom carte.
    """
    panel_scrutin = panel.filter(pl.col("id_election") == id_election)
    participation_bureau = _dedupliquer_participation(panel_scrutin, "id_bv")
    participation_commune = participation_bureau.group_by("code_commune").agg(
        pl.col("code_departement").first(),
        *[pl.col(colonne).sum() for colonne in COLONNES_PARTICIPATION],
    )
    voix_par_bloc = panel_scrutin.group_by("code_commune", "bloc").agg(pl.col("voix").sum())
    scores = _bloc_tete_et_pct(
        voix_par_bloc, "code_commune", participation_commune.select("code_commune", "exprimes")
    )
    resultat = participation_commune.join(scores, on="code_commune").with_columns(
        pl.when(pl.col("inscrits") > 0)
        .then(pl.col("votants") / pl.col("inscrits") * 100)
        .otherwise(0.0)
        .alias("participation")
    )
    return resultat.select(_colonnes_sortie("code_commune"))

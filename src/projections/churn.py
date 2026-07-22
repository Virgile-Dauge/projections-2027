"""Churn et crosswalk à deux étages : classification stable/instable des communes,
repli du panel bureau × scrutin × bloc, et `rapport-churn.md`.

Condition suspensive du reste du pipeline (HANDOFF.md, étape 0) : la jointure
bureau-à-bureau entre scrutins n'est pas sûre par défaut (numérotation
communale sans norme, découpages qui changent). Le churn — instabilité du
découpage en bureaux entre deux scrutins (CONTEXT.md) — est détecté en
comparant le nombre de bureaux par commune sur les 4 scrutins sources, sans
REU (LE nombre que personne n'a jamais publié), et mesuré canoniquement en
**part des inscrits** en zone instable, jamais en compte de communes ou de
bureaux — unités trop inégales pour être comparées (issue #13).

Stratégie à deux étages (CONTEXT.md « Commune stable / instable », « Repli ») :
- commune stable (même nombre de bureaux sur les 4 scrutins sources) ->
  jointure directe par id_bv, statut `joint_valide` ;
- commune instable (le compte change, ou la commune n'apparaît pas dans l'un
  des 4 scrutins sources) -> repli à la maille communale, statut `repli`.
Jamais de troisième état silencieux : chaque ligne du panel final porte
l'un de ces deux statuts.

⚠️ Repli implémenté : agrégation à la maille communale (voix sommées,
participation dédupliquée puis sommée). La réallocation dasymétrique
pondérée par électeurs inscrits (CONTEXT.md, alternative au repli communal)
n'est pas implémentée ici : elle suppose un crosswalk adresses -> bureaux
(REU/IRIS) hors scope de cette étape. À ajouter si le repli communal s'avère
trop grossier pour la baseline (étape 1).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import polars as pl

from projections.ingest import RAW_DIR, SCRUTINS_SOURCES, ingest

# Les 4 scrutins sources (CONTEXT.md), dérivés de SCRUTINS_SOURCES en retirant
# le tour (`_t1`/`_t2`) : un second tour de législatives ne couvre pas toutes
# les circonscriptions (pas de ballotage partout), son absence seule ne doit
# jamais se lire comme un changement du nombre de bureaux.
ELECTIONS_SOURCES: tuple[str, ...] = tuple(
    dict.fromkeys(re.sub(r"_t\d+$", "", scrutin) for scrutin in SCRUTINS_SOURCES)
)

STATUT_STABLE = "stable"
STATUT_INSTABLE = "instable"
STATUT_JOINT_VALIDE = "joint_valide"
STATUT_REPLI = "repli"

# Scrutin de référence pour tout calcul en inscrits (churn national, tables par
# département, top communes) : un seul scrutin explicite et documenté, jamais
# une moyenne entre scrutins (CONTEXT.md).
SCRUTIN_REFERENCE_INSCRITS = "2024_legi_t1"

PARTICIPATION: tuple[str, ...] = ("inscrits", "abstentions", "votants", "blancs", "nuls", "exprimes")

COLONNES_PANEL: tuple[str, ...] = (
    "id_election",
    "code_departement",
    "code_commune",
    "code_bv",
    "id_bv",
    "bloc",
    "voix",
    *PARTICIPATION,
)


def compter_bureaux_par_commune(panel: pl.DataFrame) -> pl.DataFrame:
    """Nombre de bureaux distincts (id_bv) par commune × scrutin source, sans REU.

    Base du diagnostic stable/instable : LE nombre que personne n'a jamais
    publié (HANDOFF.md, étape 0). Les deux tours d'un même scrutin sont
    fusionnés (union des id_bv) avant de compter, cf. docstring du module.
    """
    return (
        panel.with_columns(pl.col("id_election").str.replace(r"_t\d+$", "").alias("election"))
        .select("code_commune", "election", "id_bv")
        .unique()
        .group_by(["code_commune", "election"])
        .agg(pl.col("id_bv").n_unique().alias("nb_bureaux"))
        .sort(["code_commune", "election"])
    )


def classifier_communes(panel: pl.DataFrame) -> pl.DataFrame:
    """Classe chaque commune stable/instable (CONTEXT.md).

    Stable : le nombre de bureaux est identique sur les 4 scrutins sources
    (`ELECTIONS_SOURCES`). Instable : soit ce nombre change, soit la commune
    n'apparaît pas dans l'un des 4 -> on ne peut alors pas valider sa
    stabilité, donc jamais de jointure directe silencieuse.
    """
    comptes = compter_bureaux_par_commune(panel)
    # Une commune -> un département, déterministe : certaines communes DOM/COM
    # ont un code_departement lettré sur un scrutin ("ZC") et numérique sur un
    # autre ("973") pour la même commune (vérifié sur le Parquet réel). Sans
    # dédup au niveau commune, cette table ferait du fan-out sur la jointure
    # ci-dessous (duplication silencieuse des lignes du panel).
    departements = (
        panel.select("code_commune", "code_departement")
        .unique()
        .sort(["code_commune", "code_departement"])
        .unique(subset="code_commune", keep="first")
    )

    resume = comptes.group_by("code_commune").agg(
        pl.col("nb_bureaux").n_unique().alias("_nb_valeurs_distinctes"),
        pl.col("election").n_unique().alias("_nb_scrutins_presents"),
        pl.col("nb_bureaux").first().alias("nb_bureaux_reference"),
    )
    return (
        resume.join(departements, on="code_commune", how="left")
        .with_columns(
            pl.when(
                (pl.col("_nb_valeurs_distinctes") == 1)
                & (pl.col("_nb_scrutins_presents") == len(ELECTIONS_SOURCES))
            )
            .then(pl.lit(STATUT_STABLE))
            .otherwise(pl.lit(STATUT_INSTABLE))
            .alias("statut")
        )
        .select("code_commune", "code_departement", "statut", "nb_bureaux_reference")
        .sort("code_commune")
    )


def _replier_a_la_maille_communale(instable: pl.DataFrame) -> pl.DataFrame:
    """Agrège les lignes des communes instables à la maille communale (repli).

    Voix sommées par bloc ; participation dédupliquée par bureau puis sommée
    (elle est répétée sur chaque ligne de bloc d'un même bureau × scrutin,
    cf. projections.ingest) — jamais additionnée telle quelle, sous peine de
    compter chaque bureau autant de fois qu'il a de blocs.
    """
    participation = (
        instable.select("id_election", "code_commune", "id_bv", *PARTICIPATION)
        .unique()
        .group_by(["id_election", "code_commune"])
        .agg([pl.col(colonne).sum() for colonne in PARTICIPATION])
    )
    voix = instable.group_by(["id_election", "code_departement", "code_commune", "bloc"]).agg(
        pl.col("voix").sum()
    )
    return voix.join(participation, on=["id_election", "code_commune"]).with_columns(
        pl.lit(None, dtype=pl.String).alias("code_bv"),
        pl.lit(None, dtype=pl.String).alias("id_bv"),
    )


def construire_panel_avec_statut(panel: pl.DataFrame, classification: pl.DataFrame) -> pl.DataFrame:
    """Panel final bureau × scrutin × bloc : chaque ligne porte son statut de crosswalk.

    Communes stables : lignes du panel passées telles quelles (jointure
    directe par id_bv déjà faite dans `projections.ingest`), statut
    `joint_valide`. Communes instables : lignes agrégées à la maille
    communale (repli), statut `repli`. Aucune ligne sans statut explicite —
    lève une erreur si une commune du panel manque à la classification plutôt
    que de la joindre silencieusement.
    """
    avec_statut = panel.join(classification.select("code_commune", "statut"), on="code_commune", how="left")
    manquantes = avec_statut.filter(pl.col("statut").is_null())
    if manquantes.height:
        codes = sorted(manquantes.get_column("code_commune").unique().to_list())
        raise ValueError(f"commune(s) du panel absente(s) de la classification : {codes}")

    stable = (
        avec_statut.filter(pl.col("statut") == STATUT_STABLE)
        .select(*COLONNES_PANEL)
        .with_columns(pl.lit(STATUT_JOINT_VALIDE).alias("statut"))
    )
    instable = avec_statut.filter(pl.col("statut") == STATUT_INSTABLE)
    if instable.height == 0:
        return stable

    repli = (
        _replier_a_la_maille_communale(instable)
        .select(*COLONNES_PANEL)
        .with_columns(pl.lit(STATUT_REPLI).alias("statut"))
    )
    return pl.concat([stable, repli])


def taux_churn_national(classification: pl.DataFrame) -> float:
    """Proportion de communes instables parmi l'ensemble des communes du panel.

    Chiffre de contexte uniquement (issue #13) : la mesure canonique du churn
    est `part_inscrits_zone_instable`, pas ce compte de communes — des unités
    de tailles trop inégales pour être comparées (CONTEXT.md « Churn »).
    """
    total = classification.height
    if total == 0:
        return 0.0
    instables = classification.filter(pl.col("statut") == STATUT_INSTABLE).height
    return instables / total


def distribution_par_departement(classification: pl.DataFrame) -> pl.DataFrame:
    """Taux d'instabilité par département, du plus touché au moins touché.

    Tri secondaire par code_departement : sans lui, l'ordre des départements
    à égalité de taux (nombreux à 0 %) n'est pas garanti stable d'un run à
    l'autre (group_by ne préserve pas d'ordre), ce qui casserait la
    reproductibilité du rapport.
    """
    return (
        classification.group_by("code_departement")
        .agg(
            pl.len().alias("nb_communes"),
            (pl.col("statut") == STATUT_INSTABLE).sum().alias("nb_communes_instables"),
        )
        .with_columns((pl.col("nb_communes_instables") / pl.col("nb_communes")).alias("taux_instable"))
        .sort(["taux_instable", "code_departement"], descending=[True, False])
    )


def inscrits_par_departement(
    panel: pl.DataFrame, classification: pl.DataFrame, scrutin_reference: str
) -> pl.DataFrame:
    """Inscrits en zone instable par département (absolu et part), depuis les sommes.

    Jamais de moyenne des taux communaux (CONTEXT.md, « Churn ») : chaque
    département recalcule sa part depuis la somme de ses inscrits (`statut`
    lu sur `classification`, jamais sur le `code_departement` du panel qui
    peut être incohérent pour une même commune DOM/COM d'un scrutin à
    l'autre, cf. `classifier_communes`), dédupliqués par bureau.
    """
    inscrits = (
        panel.filter(pl.col("id_election") == scrutin_reference)
        .select("code_commune", "id_bv", "inscrits")
        .unique()
        .join(classification.select("code_commune", "code_departement", "statut"), on="code_commune", how="left")
    )
    return inscrits.group_by("code_departement").agg(
        pl.col("inscrits").sum().alias("inscrits_departement"),
        pl.col("inscrits").filter(pl.col("statut") == STATUT_INSTABLE).sum().alias("inscrits_instables"),
    ).with_columns(
        (pl.col("inscrits_instables") / pl.col("inscrits_departement")).alias("part_inscrits_instables")
    )


def table_departements(panel: pl.DataFrame, classification: pl.DataFrame, scrutin_reference: str) -> pl.DataFrame:
    """Table de priorisation par département : inscrits en zone instable + colonnes communales.

    Ajoute `inscrits_instables` (absolu) et `part_inscrits_instables` aux
    colonnes de `distribution_par_departement` (nb_communes,
    nb_communes_instables, taux_instable). Triée par inscrits en zone
    instable décroissant — l'ordre de la charge de travail — puis
    code_departement croissant (déterminisme à égalité) ; le taux communal
    reste en colonne (intensité) mais ne pilote plus le tri (CONTEXT.md).
    """
    return (
        inscrits_par_departement(panel, classification, scrutin_reference)
        .join(distribution_par_departement(classification), on="code_departement", how="left")
        .sort(["inscrits_instables", "code_departement"], descending=[True, False])
    )


def _part_inscrits(panel: pl.DataFrame, classification: pl.DataFrame, scrutin_reference: str, statut: str) -> float:
    """% des inscrits (sur `scrutin_reference`) situés dans une commune du `statut` donné.

    Pondéré par les électeurs inscrits, jamais par la surface (CONTEXT.md).
    Les inscrits sont dédupliqués par bureau avant sommation : ils sont
    répétés sur chaque ligne de bloc d'un même bureau × scrutin.
    """
    inscrits = (
        panel.filter(pl.col("id_election") == scrutin_reference)
        .select("code_commune", "id_bv", "inscrits")
        .unique()
        .join(classification.select("code_commune", "statut"), on="code_commune", how="left")
    )
    total = inscrits.get_column("inscrits").sum()
    if not total:
        return 0.0
    part = inscrits.filter(pl.col("statut") == statut).get_column("inscrits").sum()
    return part / total


def part_inscrits_zone_stable(panel: pl.DataFrame, classification: pl.DataFrame, scrutin_reference: str) -> float:
    """% des inscrits (sur `scrutin_reference`) situés dans une commune stable."""
    return _part_inscrits(panel, classification, scrutin_reference, STATUT_STABLE)


def top_communes_instables_par_inscrits(
    panel: pl.DataFrame,
    classification: pl.DataFrame,
    scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS,
    n: int = 20,
) -> pl.DataFrame:
    """Top `n` communes instables par inscrits, avec leur nombre de bureaux.

    Cible concrète de la future réallocation dasymétrique (CONTEXT.md,
    « Repli ») : dit où chaque effort récupère le plus d'électorat, à la
    granularité fine. Tri par inscrits décroissant, code_commune croissant
    en secondaire (déterminisme à égalité).
    """
    election_reference = re.sub(r"_t\d+$", "", scrutin_reference)
    nb_bureaux = (
        compter_bureaux_par_commune(panel)
        .filter(pl.col("election") == election_reference)
        .select("code_commune", "nb_bureaux")
    )
    inscrits = (
        panel.filter(pl.col("id_election") == scrutin_reference)
        .select("code_commune", "id_bv", "inscrits")
        .unique()
        .group_by("code_commune")
        .agg(pl.col("inscrits").sum())
    )
    return (
        classification.filter(pl.col("statut") == STATUT_INSTABLE)
        .select("code_commune", "code_departement")
        .join(inscrits, on="code_commune", how="left")
        .join(nb_bureaux, on="code_commune", how="left")
        .with_columns(pl.col("inscrits").fill_null(0), pl.col("nb_bureaux").fill_null(0))
        .sort(["inscrits", "code_commune"], descending=[True, False])
        .head(n)
    )


def part_inscrits_zone_instable(panel: pl.DataFrame, classification: pl.DataFrame, scrutin_reference: str) -> float:
    """% des inscrits (sur `scrutin_reference`) situés dans une commune instable.

    Mesure canonique du churn (CONTEXT.md « Churn ») : la grandeur à
    minimiser est l'électorat mal identifié localement, jamais un compte de
    communes ou de bureaux — unités trop inégales pour être comparées.
    C'est le chiffre de tête de `rapport-churn.md`.
    """
    return _part_inscrits(panel, classification, scrutin_reference, STATUT_INSTABLE)


def generer_rapport_churn(panel: pl.DataFrame, scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS) -> str:
    """Construit le texte de `rapport-churn.md` (issue #13, CONTEXT.md).

    Chiffre de tête : part des inscrits en zone instable — la grandeur à
    minimiser (CONTEXT.md « Churn »), jamais un compte de communes ou de
    bureaux. Le compte de communes descend en simple contexte. Publie
    ensuite la table de priorisation par département (triée par inscrits en
    zone instable décroissant, ratios recalculés depuis les sommes) puis le
    top 20 des communes instables par inscrits — la liste de cibles concrète
    de la future réallocation dasymétrique.
    """
    classification = classifier_communes(panel)
    part_instable = part_inscrits_zone_instable(panel, classification, scrutin_reference)
    taux_national = taux_churn_national(classification)  # contexte uniquement, cf. docstring
    departements = table_departements(panel, classification, scrutin_reference)
    top_communes = top_communes_instables_par_inscrits(panel, classification, scrutin_reference)

    lignes_departements = "\n".join(
        f"| {ligne['code_departement']} | {ligne['inscrits_instables']} | "
        f"{ligne['part_inscrits_instables']:.1%} | {ligne['nb_communes']} | "
        f"{ligne['nb_communes_instables']} | {ligne['taux_instable']:.1%} |"
        for ligne in departements.iter_rows(named=True)
    )

    lignes_communes = "\n".join(
        f"| {ligne['code_commune']} | {ligne['code_departement']} | "
        f"{ligne['nb_bureaux']} | {ligne['inscrits']} |"
        for ligne in top_communes.iter_rows(named=True)
    )

    return f"""# Rapport de churn — étape 0

Mesure du churn (CONTEXT.md) : la grandeur à minimiser est la **part des
inscrits** en zone instable, jamais un compte de communes ou de bureaux —
des unités de tailles trop inégales pour être comparées. L'instabilité est
détectée par commune : le nombre de bureaux change entre les
{len(ELECTIONS_SOURCES)} scrutins sources (présidentielle 2022, législatives
2022, législatives 2024, européennes 2024), sans crosswalk REU — comparaison
brute `id_election` × `code_commune` (HANDOFF.md, étape 0).

## Churn national

**{part_instable:.1%}** des inscrits (référence : {scrutin_reference}) sont
situés dans une commune instable et passent en repli à la maille communale
plutôt qu'en jointure directe par bureau — la part des inscrits en zone
instable (CONTEXT.md « Churn »). Pour contexte : cela représente
**{taux_national:.1%}** des {classification.height} communes du panel, un
compte à part (les communes ont des tailles trop inégales pour être
comparées directement).

## Distribution par département

Triée par inscrits en zone instable décroissant (l'ordre de la charge de
travail) ; le taux instable communal reste en colonne (intensité) mais ne
pilote plus le tri. Ratios recalculés depuis les sommes d'inscrits, jamais
en moyennant des taux communaux.

| Département | Inscrits en zone instable | % des inscrits du département | Communes | dont instables | Taux instable (communes) |
| --- | --- | --- | --- | --- | --- |
{lignes_departements}

## Top 20 communes instables par inscrits

Cible concrète de la future réallocation dasymétrique (CONTEXT.md
« Repli ») : où chaque effort récupère le plus d'électorat, à la granularité
fine.

| Commune | Département | Bureaux | Inscrits |
| --- | --- | --- | --- |
{lignes_communes}
"""


INTERIM_DIR = Path("data/interim")


def main() -> None:
    """Point d'entrée `uv run rapport-churn`.

    Ingère les 2 Parquet sources, classe les communes, construit le panel
    avec statut et écrit `rapport-churn.md` + le panel avec statut en Parquet.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--general-results", type=Path, default=RAW_DIR / "general_results.parquet")
    parser.add_argument("--candidats-results", type=Path, default=RAW_DIR / "candidats_results.parquet")
    parser.add_argument("--out", type=Path, default=Path("rapport-churn.md"))
    parser.add_argument("--panel-out", type=Path, default=INTERIM_DIR / "panel_avec_statut.parquet")
    args = parser.parse_args()

    general_results = pl.read_parquet(args.general_results)
    candidats_results = pl.read_parquet(args.candidats_results)
    panel = ingest(general_results, candidats_results)

    classification = classifier_communes(panel)
    panel_avec_statut = construire_panel_avec_statut(panel, classification)

    args.panel_out.parent.mkdir(parents=True, exist_ok=True)
    panel_avec_statut.write_parquet(args.panel_out)

    rapport = generer_rapport_churn(panel, scrutin_reference=SCRUTIN_REFERENCE_INSCRITS)
    args.out.write_text(rapport, encoding="utf-8")

    print(f"rapport écrit : {args.out}")
    print(f"panel avec statut écrit : {args.panel_out} ({panel_avec_statut.height} lignes)")


if __name__ == "__main__":
    main()

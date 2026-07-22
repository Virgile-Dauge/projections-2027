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
  des 4 scrutins sources) -> repli, deux traitements possibles :
  - repli communal classique (agrégation à la maille communale, voix
    sommées, participation dédupliquée puis sommée), statut `repli` ;
  - réconciliation bureau à bureau par réallocation dasymétrique pondérée
    par les électeurs inscrits, jamais par la surface (CONTEXT.md « Repli »,
    issue #14) — réservée aux communes de `COMMUNES_RECONCILIATION_BUREAU`
    (Paris pour l'instant, cf. `reconcilier_bureaux_par_reallocation`),
    statuts `reconcilie` / `realloue` / `irresoluble`.
Jamais de troisième état silencieux : chaque ligne du panel final porte
l'un de ces statuts explicites.
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

# Second étage du repli (issue #14, CONTEXT.md « Repli ») : réconciliation
# bureau à bureau d'une commune instable par réallocation dasymétrique
# pondérée par les inscrits, plutôt que l'agrégation à la maille communale.
# `reconcilie` : bureau apparié directement par id_bv (même identifiant dans
# la grille cible et le scrutin source) — distinct de `joint_valide` car la
# commune reste instable dans son ensemble (CONTEXT.md « Commune stable /
# instable »). `realloue` : bureau cible sans id_bv correspondant dans le
# scrutin source, dont les voix et la participation sont reconstruites au
# prorata des inscrits des bureaux cible orphelins. `irresoluble` : bureau
# cible sans aucune donnée exploitable pour ce scrutin (aucun reliquat à
# réallouer) — jamais un zéro fabriqué.
STATUT_RECONCILIE = "reconcilie"
STATUT_REALLOUE = "realloue"
STATUT_IRRESOLUBLE = "irresoluble"

# Communes traitées par le second étage (réconciliation bureau) plutôt que le
# repli communal classique. Paris (75056) seul : c'est la cible de l'issue
# #14 (le plus gros gisement d'inscrits en zone instable, cf.
# rapport-churn.md). Le mécanisme ci-dessous est générique (n'importe quelle
# commune instable pourrait y être ajoutée), mais l'étendre à d'autres
# grandes villes à arrondissements (Lyon, Marseille — également instables,
# cf. top 20 du rapport) est un choix délibérément laissé de côté : chacune
# mériterait sa propre vérification de crosswalk avant d'être ajoutée ici.
COMMUNES_RECONCILIATION_BUREAU: tuple[str, ...] = ("75056",)

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


def reconcilier_bureaux_par_reallocation(
    commune: pl.DataFrame, scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS
) -> pl.DataFrame:
    """Réconciliation bureau à bureau d'UNE commune instable (issue #14, CONTEXT.md « Repli »).

    `commune` : lignes du panel brut pour une seule commune (toutes colonnes
    de `COLONNES_PANEL` sauf `statut`), tous scrutins confondus.

    La grille cible (id_bv + inscrits par bureau) est celle de
    `scrutin_reference` — le scrutin le plus récent, seule grandeur stable
    disponible pour un bureau qui n'existe pas sous cet identifiant dans un
    scrutin plus ancien (même convention que le reste du module :
    `SCRUTIN_REFERENCE_INSCRITS`, jamais une moyenne entre scrutins).

    Pour chaque scrutin, les bureaux dont l'id_bv figure tel quel dans la
    grille cible passent inchangés (statut `reconcilie`). Le reliquat — voix
    et participation des bureaux orphelins côté source, dans ce scrutin —
    est réalloué en comptes au prorata des inscrits (grille cible, jamais la
    surface) des bureaux orphelins côté cible (statut `realloue`). Quand
    aucun reliquat n'existe pour absorber un bureau cible orphelin (aucune
    donnée source disponible, poids d'inscrits nul), ce bureau reste
    `irresoluble` pour ce scrutin : voix et participation à `null`, jamais un
    zéro fabriqué.

    Second tour des législatives (`*_legi_t2`) exclu de la réallocation : son
    absence pour une partie des bureaux est structurelle (pas de ballottage
    dans toutes les circonscriptions, cf. `ELECTIONS_SOURCES`) et ne doit
    jamais se lire comme un reliquat à réallouer — les bureaux non appariés y
    sont silencieusement absents, comme pour une commune stable.
    """
    grille_cible = (
        commune.filter(pl.col("id_election") == scrutin_reference)
        .select("id_bv", "code_bv", "code_departement", "inscrits")
        .unique()
    )
    if grille_cible.height == 0:
        raise ValueError(
            f"grille cible introuvable : commune absente de {scrutin_reference!r} "
            "(réconciliation bureau impossible sans grille de référence)"
        )
    code_commune = commune.get_column("code_commune").unique().to_list()[0]
    cible_ids = set(grille_cible.get_column("id_bv").to_list())
    blocs_commune = commune.select("bloc").unique()

    morceaux: list[pl.DataFrame] = []
    for id_election in sorted(commune.get_column("id_election").unique().to_list()):
        source = commune.filter(pl.col("id_election") == id_election)
        source_ids = set(source.get_column("id_bv").unique().to_list())
        apparies = cible_ids & source_ids

        if apparies:
            morceaux.append(
                source.filter(pl.col("id_bv").is_in(apparies))
                .select(*COLONNES_PANEL)
                .with_columns(pl.lit(STATUT_RECONCILIE).alias("statut"))
            )

        if id_election.endswith("_legi_t2"):
            # Ballottage partiel : cf. docstring, jamais de réallocation ici.
            continue

        orphelins_cible = cible_ids - source_ids
        if not orphelins_cible:
            continue

        orphelins_source = source_ids - cible_ids
        cible_orphelins = grille_cible.filter(pl.col("id_bv").is_in(orphelins_cible))
        poids_total = cible_orphelins.get_column("inscrits").sum()

        if not orphelins_source or not poids_total:
            morceaux.append(
                cible_orphelins.select("id_bv", "code_bv", "code_departement")
                .join(blocs_commune, how="cross")
                .with_columns(
                    pl.lit(id_election).alias("id_election"),
                    pl.lit(code_commune).alias("code_commune"),
                    pl.lit(None, dtype=pl.Float64).alias("voix"),
                    *(pl.lit(None, dtype=pl.Float64).alias(colonne) for colonne in PARTICIPATION),
                )
                .select(*COLONNES_PANEL)
                .with_columns(pl.lit(STATUT_IRRESOLUBLE).alias("statut"))
            )
            continue

        source_orphelins = source.filter(pl.col("id_bv").is_in(orphelins_source))
        pool_participation = (
            source_orphelins.select("id_bv", *PARTICIPATION)
            .unique()
            .select([pl.col(colonne).sum().alias(f"{colonne}_pool") for colonne in PARTICIPATION])
        )
        pool_voix = source_orphelins.group_by("bloc").agg(pl.col("voix").sum().alias("voix_pool"))

        realloue = (
            cible_orphelins.select("id_bv", "code_bv", "code_departement", "inscrits")
            .rename({"inscrits": "inscrits_cible"})
            .with_columns((pl.col("inscrits_cible") / poids_total).alias("part"))
            .join(pool_voix, how="cross")
            .join(pool_participation, how="cross")
            .with_columns(
                (pl.col("part") * pl.col("voix_pool")).alias("voix"),
                *(
                    (pl.col("part") * pl.col(f"{colonne}_pool")).alias(colonne)
                    for colonne in PARTICIPATION
                ),
                pl.lit(id_election).alias("id_election"),
                pl.lit(code_commune).alias("code_commune"),
            )
            .select(*COLONNES_PANEL)
            .with_columns(pl.lit(STATUT_REALLOUE).alias("statut"))
        )
        morceaux.append(realloue)

    return pl.concat(morceaux, how="vertical_relaxed")


def voix_perdues_t2(commune: pl.DataFrame, scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS) -> pl.DataFrame:
    """Voix perdues par exclusion du second tour des législatives de la réallocation (issues #14, #18).

    `reconcilier_bureaux_par_reallocation` exclut délibérément `*_legi_t2` de
    la réallocation (fabriquer un reliquat sur ces bureaux fabriquerait des
    ballottages qui n'ont pas eu lieu, cf. sa docstring) : les bureaux du T2
    dont l'`id_bv` n'existe pas dans la grille cible (`scrutin_reference`) —
    typiquement des bureaux renumérotés — ne sont ni réconciliés ni réalloués,
    donc absents du panel final pour ce scrutin. Cette fonction recompte leurs
    voix depuis les données (jamais une constante) pour que le chiffre publié
    reste vrai si les données ou le périmètre changent (issue #18 : à
    réexaminer avec une matrice de transfert).

    `commune` : lignes du panel brut pour une seule commune, tous scrutins
    confondus (même contrat que `reconcilier_bureaux_par_reallocation`).
    Retourne une ligne par `*_legi_t2` présent dans `commune`
    (`id_election`, `voix_perdues` sommées tous blocs confondus) ; un
    DataFrame vide (mais avec le bon schéma) si aucun T2 n'est présent.
    """
    schema = {"id_election": pl.String, "voix_perdues": pl.Float64}
    cible_ids = set(
        commune.filter(pl.col("id_election") == scrutin_reference).get_column("id_bv").unique().to_list()
    )
    scrutins_t2 = sorted(e for e in commune.get_column("id_election").unique().to_list() if e.endswith("_legi_t2"))
    if not scrutins_t2:
        return pl.DataFrame(schema=schema)

    return (
        commune.filter(pl.col("id_election").is_in(scrutins_t2) & ~pl.col("id_bv").is_in(cible_ids))
        .group_by("id_election")
        .agg(pl.col("voix").sum().alias("voix_perdues"))
        .join(pl.DataFrame({"id_election": scrutins_t2}), on="id_election", how="right")
        .with_columns(pl.col("voix_perdues").fill_null(0.0))
        .sort("id_election")
        .select("id_election", "voix_perdues")
        .cast(schema)
    )


def construire_panel_avec_statut(
    panel: pl.DataFrame,
    classification: pl.DataFrame,
    scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS,
) -> pl.DataFrame:
    """Panel final bureau × scrutin × bloc : chaque ligne porte son statut de crosswalk.

    Communes stables : lignes du panel passées telles quelles (jointure
    directe par id_bv déjà faite dans `projections.ingest`), statut
    `joint_valide`. Communes instables : deux traitements possibles (second
    étage du repli, issue #14, CONTEXT.md « Repli ») —
    `COMMUNES_RECONCILIATION_BUREAU` (Paris) passe par la réconciliation
    bureau à bureau (`reconcilier_bureaux_par_reallocation`, statuts
    `reconcilie` / `realloue` / `irresoluble`) ; toutes les autres communes
    instables gardent le repli communal classique (statut `repli`). Aucune
    ligne sans statut explicite — lève une erreur si une commune du panel
    manque à la classification plutôt que de la joindre silencieusement.
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

    morceaux = [stable]

    instable_reconciliee = instable.filter(pl.col("code_commune").is_in(COMMUNES_RECONCILIATION_BUREAU))
    instable_repli = instable.filter(~pl.col("code_commune").is_in(COMMUNES_RECONCILIATION_BUREAU))

    if instable_repli.height:
        morceaux.append(
            _replier_a_la_maille_communale(instable_repli)
            .select(*COLONNES_PANEL)
            .with_columns(pl.lit(STATUT_REPLI).alias("statut"))
        )

    for code_commune in sorted(instable_reconciliee.get_column("code_commune").unique().to_list()):
        morceaux.append(
            reconcilier_bureaux_par_reallocation(
                instable_reconciliee.filter(pl.col("code_commune") == code_commune),
                scrutin_reference,
            )
        )

    return pl.concat(morceaux, how="vertical_relaxed")


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

    Liste de cibles pour la réconciliation bureau par réallocation
    dasymétrique (CONTEXT.md « Repli ») : dit où chaque effort récupère le
    plus d'électorat, à la granularité fine. Paris (#1) y est déjà traitée
    (issue #14) ; le reste de la liste reste en repli communal classique.
    Tri par inscrits décroissant, code_commune croissant en secondaire
    (déterminisme à égalité).
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


def part_inscrits_zone_instable_apres_reconciliation(
    panel_avec_statut: pl.DataFrame, scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS
) -> float:
    """% des inscrits encore en zone instable après le second étage du repli (issue #14).

    Comparable au chiffre de tête `part_inscrits_zone_instable` (même
    dénominateur, inscrits lus sur `scrutin_reference`) : mesure le gain de
    la réconciliation bureau. Un bureau (ou une commune restée en repli
    classique) compte encore comme instable s'il porte, sur au moins un des
    scrutins sources, le statut `irresoluble` — ou s'il n'a jamais quitté le
    repli communal classique (`id_bv` devenu null par agrégation, cf.
    `_replier_a_la_maille_communale`). Les bureaux `joint_valide`,
    `reconcilie` et `realloue` comptent comme résolus.
    """
    jamais_resolu = (
        panel_avec_statut.filter(pl.col("id_bv").is_not_null())
        .group_by("id_bv")
        .agg((pl.col("statut") == STATUT_IRRESOLUBLE).any().alias("jamais_resolu"))
    )
    reference = panel_avec_statut.filter(pl.col("id_election") == scrutin_reference)

    bureau = (
        reference.filter(pl.col("id_bv").is_not_null())
        .select("id_bv", "inscrits")
        .unique()
        .join(jamais_resolu, on="id_bv", how="left")
    )
    commune_repli = reference.filter(pl.col("id_bv").is_null()).select("code_commune", "inscrits").unique()

    total = bureau.get_column("inscrits").sum() + commune_repli.get_column("inscrits").sum()
    if not total:
        return 0.0
    instable_bureau = bureau.filter(pl.col("jamais_resolu")).get_column("inscrits").sum()
    instable_commune = commune_repli.get_column("inscrits").sum()
    return (instable_bureau + instable_commune) / total


def generer_rapport_churn(panel: pl.DataFrame, scrutin_reference: str = SCRUTIN_REFERENCE_INSCRITS) -> str:
    """Construit le texte de `rapport-churn.md` (issues #13 et #14, CONTEXT.md).

    Chiffre de tête : part des inscrits en zone instable — la grandeur à
    minimiser (CONTEXT.md « Churn »), jamais un compte de communes ou de
    bureaux. Le compte de communes descend en simple contexte. Publie
    ensuite le gain de la réconciliation bureau de Paris (issue #14, avant/
    après chiffré) et le coût chiffré de l'exclusion du second tour des
    législatives de la réallocation (`voix_perdues_t2`, jamais une constante
    — issue #18), la table de priorisation par département (triée par
    inscrits en zone instable décroissant, ratios recalculés depuis les
    sommes) puis le top 20 des communes instables par inscrits.
    """
    classification = classifier_communes(panel)
    part_instable = part_inscrits_zone_instable(panel, classification, scrutin_reference)
    taux_national = taux_churn_national(classification)  # contexte uniquement, cf. docstring
    departements = table_departements(panel, classification, scrutin_reference)
    top_communes = top_communes_instables_par_inscrits(panel, classification, scrutin_reference)

    panel_avec_statut = construire_panel_avec_statut(panel, classification, scrutin_reference)
    part_apres = part_inscrits_zone_instable_apres_reconciliation(panel_avec_statut, scrutin_reference)
    gain_points = (part_instable - part_apres) * 100

    perdues_t2 = (
        pl.concat(
            [
                voix_perdues_t2(panel.filter(pl.col("code_commune") == code_commune), scrutin_reference)
                for code_commune in COMMUNES_RECONCILIATION_BUREAU
            ],
            how="vertical_relaxed",
        )
        .group_by("id_election")
        .agg(pl.col("voix_perdues").sum())
        .sort("id_election")
    )
    total_voix_perdues_t2 = perdues_t2.get_column("voix_perdues").sum() if perdues_t2.height else 0.0
    lignes_perdues_t2 = "\n".join(
        f"- {ligne['id_election']} : **{ligne['voix_perdues']:.0f} voix**"
        for ligne in perdues_t2.iter_rows(named=True)
    ) or "- aucun scrutin T2 dans ce panel"

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

## Réconciliation de Paris (second étage du repli)

Paris (75056, département 75) sort du repli communal (issue #14) : c'est la
commune la plus lourde en zone instable (voir top 20 ci-dessous), pour un
outil dont le cœur de cible est le ciblage fin en zone urbaine dense. Ses
bureaux sont réconciliés un à un entre les {len(ELECTIONS_SOURCES)} scrutins
sources plutôt qu'agrégés en un seul bloc départemental.

**Méthode.** La grille cible (bureaux + inscrits) est celle du scrutin le
plus récent ({scrutin_reference}). Pour chaque scrutin source, les bureaux
dont l'`id_bv` figure tel quel dans cette grille passent inchangés (statut
`reconcilie`). Le reliquat — voix et participation des bureaux orphelins côté
source — est réalloué **en comptes de voix**, au prorata des inscrits
(jamais de la surface, CONTEXT.md « Repli ») des bureaux orphelins côté
cible (statut `realloue`) ; les ratios se recalculent ensuite depuis ces
comptes, jamais l'inverse. Un bureau cible sans aucun reliquat exploitable
reste `irresoluble` (statut explicite, voix à `null`, jamais un zéro
fabriqué) — distinct à la fois de `joint_valide` (commune stable) et de
`repli` (commune instable non réconciliée).

**Hypothèses et cas non résolus.** Sur les données réelles, l'essentiel du
désaccord entre scrutins parisiens est une pure renumérotation administrative
d'une quarantaine de bureaux contigus (ex. `0201`→`0211` entre 2022 et 2024),
à inscrits quasi identiques : le crosswalk parisien est mécaniquement
trivial, pas un vrai découpage ou une fusion de zones. La réallocation ne
cherche pas à retrouver cette bijection cachée (aucun crosswalk adresses/IRIS
disponible) : elle répartit le reliquat au prorata des inscrits sur
l'ensemble des bureaux orphelins du même scrutin — une approximation très
proche de la vérité dans ce cas précis, qui le serait moins sur une commune
au redécoupage plus disruptif.

**Second tour des législatives : exclu de la réallocation, coût chiffré.**
`*_legi_t2` est délibérément exclu du calcul du reliquat : une partie des
circonscriptions n'a pas de second tour (pas de ballottage), et réallouer un
reliquat sur ces bureaux fabriquerait des ballottages qui n'ont pas eu lieu.
Cette exclusion a un coût mesurable, jamais silencieux — les bureaux
renumérotés du second tour n'ont, par construction, aucune correspondance
dans la grille cible, et n'y sont ni réconciliés ni réalloués : leurs voix
sortent purement et simplement du panel pour ce scrutin.

{lignes_perdues_t2}
- **Total : {total_voix_perdues_t2:.0f} voix**

À réexaminer avec la matrice de transfert — voir issue #18.

Le mécanisme (`COMMUNES_RECONCILIATION_BUREAU`) est générique mais
volontairement limité à Paris ici : l'étendre à d'autres grandes villes à
arrondissements (Lyon, Marseille, également instables) est laissé à une
itération suivante.

**Gain chiffré.** Avant réconciliation (Paris à 100 % en repli communal,
comme toute commune instable) : **{part_instable:.1%}** des inscrits en zone
instable. Après réconciliation bureau de Paris : **{part_apres:.1%}** — gain
de **{gain_points:.1f} point(s)**.

## Distribution par département

Triée par inscrits en zone instable décroissant (l'ordre de la charge de
travail) ; le taux instable communal reste en colonne (intensité) mais ne
pilote plus le tri. Ratios recalculés depuis les sommes d'inscrits, jamais
en moyennant des taux communaux.

| Département | Inscrits en zone instable | % des inscrits du département | Communes | dont instables | Taux instable (communes) |
| --- | --- | --- | --- | --- | --- |
{lignes_departements}

## Top 20 communes instables par inscrits

Cible concrète de la réconciliation bureau par réallocation dasymétrique
(CONTEXT.md « Repli ») : où chaque effort récupère le plus d'électorat, à la
granularité fine. Paris (#1) y est déjà traitée (issue #14, cf. section
ci-dessus) ; le reste de la liste reste en repli communal classique.

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

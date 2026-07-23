"""Préparation des données carte mobilisation (issue #26, PRD #23, ADR 0002/0003).

Jalon public : la réserve de voix par bloc (#25) et le rapport de force projeté
(#5) deviennent des couches de tuiles, jointes par IDENTIFIANTS (jamais par
géométrie, cf. CONTEXT.md « Crosswalk ») dans `projections.build_tiles`. Ce
module ne fait QUE la préparation des tables (format large par unité, quantiles,
dézoom, gate) — la jointure aux contours GeoJSON reste dans `build_tiles.py`.

## Sortie ordinale partout (ADR 0001, inchangé)

Aucun pourcentage à intervalle de confiance : `quantiles_larges` produit un
bucket ORDINAL (1..n, n petit — la carte affiche des tranches, pas un rang
fin). Deux échelles distinctes et documentées : réserve en 5 tranches (gisement
très faible -> très élevé, un choix de granularité produit, pas gravé par un
ADR), rapport de force en 4 tranches -- délibérément DIFFÉRENT du découpage en
tercile de `projections.backtest.tercile_competitif` (ADR 0002 : ce
tercile-là a été démis comme objectif produit ; réutiliser son découpage ici
pour la couche de contexte laisserait croire, à tort, qu'il s'agit du même
concept réhabilité).

## Réserve : dézoom par sommes, repli visible (ADR 0002 point 1, CONTEXT.md « Repli »)

`preparer_carte_reserve` (maille bureau, zoom haut) et `agreger_reserve_commune`
(maille commune, zoom bas ET communes en repli à tout zoom -- pas de contour
bureau fiable pour elles) ne moyennent jamais une réserve : le dézoom
recalcule une SOMME de voix mobilisables (CLAUDE.md « Never average
percentages », qui s'applique de la même façon à un compte de voix agrégé).
Le statut de réconciliation (`statut`/`maille`, `projections.churn`) est
propagé jusqu'aux propriétés de sortie -- jamais une dégradation silencieuse.

## Rapport de force : couche de contexte (ADR 0002 point 2)

`preparer_carte_rapport_force` lit `baseline_unite_bloc.parquet` (#5) tel
quel : bloc en tête (composite maximal, départage déterministe) + quantile
large DU BLOC EN TÊTE dans SA PROPRE distribution (jamais toutes valeurs de
tous les blocs mélangées -- un bloc structurellement plus fort au national,
ex. Droite/Extrême droite selon le scrutin, ne doit pas écraser l'échelle des
autres). Aucune agrégation commune n'est recalculée pour les communes stables
dézoomées (ponytail : nécessiterait un recalcul de composite depuis les voix
communales, un chantier de données à part entière, hors périmètre de cette
itération -- documenté dans la page méthode). Les communes en repli ont déjà
un composite valide à la maille communale (calculé depuis des voix, pas
fabriqué) : elles n'ont pas besoin de cette agrégation.

## Gate mécanique (issue #26 : refuser la construction si le verdict est rouge)

`verifier_publication_autorisee` ne recalcule RIEN : elle prend le booléen
déjà produit par `projections.backtest.verdict_carte_mobilisation` (lui-même
réutilisé tel quel par `projections.reserve.calculer_donnees_reserve`) et lève
si `False`. Appelée en tête de la construction des tuiles mobilisation
(`projections.build_tiles`) : si le gate est rouge, aucune tuile mobilisation
n'est produite, jamais un export silencieusement obsolète.
"""

from __future__ import annotations

import polars as pl

from projections.carte import BLOC_SLUG
from projections.reserve import METHODE_PART_DEFAUT, generer_rapport_complet

# --- Sortie ordinale générique --------------------------------------------------


def quantiles_larges(
    table: pl.DataFrame, colonne: str, groupe: str | list[str] = "bloc", n: int = 5, suffixe: str = ""
) -> pl.DataFrame:
    """Ajoute `quantile_{colonne}{suffixe}` (Int64, 1..n) : quantile ORDINAL de
    `colonne`, calculé séparément PAR `groupe` (cf. docstring du module).

    `groupe` accepte une seule colonne (`"bloc"`, national) ou une LISTE de
    colonnes (`["bloc", "code_departement"]`, tranche départementale -- issue
    #37, CONTEXT.md « Tranche départementale ») : `.over()` Polars partitionne
    alors sur la combinaison des colonnes, jamais sur une colonne à la fois --
    chaque sous-groupe (ex. Gauche x Rhône) a sa propre échelle, indépendante
    des autres. `suffixe` distingue la colonne de sortie quand plusieurs appels
    coexistent (ex. `quantile_reserve` national + `quantile_reserve_dep`
    départemental, tous deux embarqués dans les tuiles -- ADR 0005) : par
    défaut vide, comportement inchangé.

    Rang moyen (ex-aequo -> même bucket le plus souvent, comme
    `projections.backtest.correlation_spearman`/`tercile_competitif`) ramené en
    fraction `rang / effectif` (effectif = nombre de valeurs NON NULLES du
    groupe, jamais le nombre total de lignes) puis multiplié par `n` et
    arrondi au-dessus (`ceil`), borné à `[1, n]` -- garantit qu'aucune valeur
    non nulle ne tombe hors bornes par arrondi, même pour un groupe plus petit
    que `n` (ex. 975, 4 bureaux : la tranche 1 reste simplement vide, jamais
    une erreur). Déterministe (tri stable, aucun aléa). `colonne` nulle ->
    quantile null, jamais un bucket fabriqué.
    """
    valeur = pl.col(colonne)
    rang = valeur.rank(method="average").over(groupe)
    effectif = valeur.count().over(groupe)  # .count() Polars exclut déjà les null.
    fraction = rang / effectif
    bucket = (fraction * n).ceil().clip(1, n).cast(pl.Int64)
    return table.with_columns(
        pl.when(valeur.is_not_null()).then(bucket).otherwise(None).alias(f"quantile_{colonne}{suffixe}")
    )


# --- Gate mécanique --------------------------------------------------------------


def _completer_colonnes_blocs(large: pl.DataFrame, prefixe: str, dtype: pl.DataType, suffixe: str = "") -> pl.DataFrame:
    """Garantit une colonne `{prefixe}_{slug}{suffixe}` par bloc (docs/classification_en_blocs.md),
    même si un bloc n'a aucune ligne dans toute la maille après pivot (ex. Divers,
    structurellement absent des candidatures présidentielle -- CONTEXT.md « Nuance »).
    Valeur null, jamais fabriquée : contrairement à `carte.py._bloc_tete_et_pct`
    (qui remplit un pourcentage absent à 0.0, une valeur réelle), une réserve ou
    un rapport de force absent n'a simplement pas d'estimation. `suffixe` (issue
    #37) distingue la variante départementale (`quantile_reserve_<slug>_dep`) de
    la nationale, mêmes garanties de complétude pour les deux.
    """
    manquantes = {
        f"{prefixe}_{slug}{suffixe}": pl.lit(None, dtype=dtype)
        for slug in BLOC_SLUG.values()
        if f"{prefixe}_{slug}{suffixe}" not in large.columns
    }
    return large.with_columns(**manquantes) if manquantes else large


def _reserve_large(table_longue: pl.DataFrame, cle: str, n_quantiles: int) -> pl.DataFrame:
    """Table réserve longue (`cle` x bloc x reserve x contexte) -> large (une ligne
    par `cle`, colonnes `reserve_<slug>`/`quantile_reserve_<slug>`/
    `quantile_reserve_<slug>_dep` par bloc).

    Reprend le pattern pivot + renommage de `carte.py._bloc_tete_et_pct` (pas un
    second calcul indépendant) : trois pivots séparés (valeur, quantile
    national, quantile départemental) plutôt qu'un pivot multi-valeurs, pour un
    renommage explicite et symétrique.

    Tranche départementale (issue #37, CONTEXT.md « Tranche départementale »,
    ADR 0005) : quantile RECALCULÉ par sous-groupe (bloc x `code_departement`),
    colonne ADDITIONNELLE `_dep` -- le quantile national `quantile_reserve_<slug>`
    reste présent tel quel (réversibilité côté client seul, site n'affiche
    plus que la variante départementale). Appelé séparément par
    `preparer_carte_reserve` (population bureau) et `agreger_reserve_commune`
    (population commune) : chaque maille calcule sa PROPRE échelle
    départementale sur sa propre population, jamais mélangées -- même
    discipline que le quantile national existant.
    """
    avec_quantile = quantiles_larges(table_longue, "reserve", groupe="bloc", n=n_quantiles)
    avec_quantile = quantiles_larges(
        avec_quantile, "reserve", groupe=["bloc", "code_departement"], n=n_quantiles, suffixe="_dep"
    )
    colonnes_contexte = [c for c in ("code_departement", "statut", "maille", "degrade") if c in avec_quantile.columns]
    contexte = avec_quantile.select(cle, *colonnes_contexte).unique(subset=cle, keep="first").sort(cle)

    reserve_large = avec_quantile.pivot(on="bloc", index=cle, values="reserve")
    reserve_large = reserve_large.rename(
        {bloc: f"reserve_{slug}" for bloc, slug in BLOC_SLUG.items() if bloc in reserve_large.columns}
    )
    reserve_large = _completer_colonnes_blocs(reserve_large, "reserve", pl.Float64)

    quantile_large = avec_quantile.pivot(on="bloc", index=cle, values="quantile_reserve")
    quantile_large = quantile_large.rename(
        {bloc: f"quantile_reserve_{slug}" for bloc, slug in BLOC_SLUG.items() if bloc in quantile_large.columns}
    )
    quantile_large = _completer_colonnes_blocs(quantile_large, "quantile_reserve", pl.Int64)

    quantile_dep_large = avec_quantile.pivot(on="bloc", index=cle, values="quantile_reserve_dep")
    quantile_dep_large = quantile_dep_large.rename(
        {bloc: f"quantile_reserve_{slug}_dep" for bloc, slug in BLOC_SLUG.items() if bloc in quantile_dep_large.columns}
    )
    quantile_dep_large = _completer_colonnes_blocs(quantile_dep_large, "quantile_reserve", pl.Int64, suffixe="_dep")

    return (
        contexte.join(reserve_large, on=cle)
        .join(quantile_large, on=cle)
        .join(quantile_dep_large, on=cle)
        .sort(cle)
    )


# --- Réserve : bureau (zoom haut) et commune (dézoom + repli, ADR 0002 point 1) --


def preparer_carte_reserve(table_reserve: pl.DataFrame, n_quantiles: int = 5) -> pl.DataFrame:
    """Table réserve large, maille BUREAU uniquement (`maille == "bureau"`) :
    une ligne par `unite_id`, `reserve_<slug>`/`quantile_reserve_<slug>` par
    bloc (cf. docstring du module). Les communes en repli (`maille ==
    "commune"`) ne sont PAS dans cette table -- elles n'ont pas de réserve
    fiable par bureau ; voir `agreger_reserve_commune`.

    Quantile calculé sur la SEULE population bureau : mélanger des unités
    bureau et des unités commune (des ordres de grandeur très différents,
    une commune agrégeant plusieurs bureaux) fausserait l'échelle -- c'est
    pour cette raison que `agreger_reserve_commune` recalcule sa PROPRE
    échelle de quantile sur sa propre population.
    """
    bureau = table_reserve.filter(pl.col("maille") == "bureau")
    return _reserve_large(bureau, cle="unite_id", n_quantiles=n_quantiles)


def agreger_reserve_commune(table_reserve: pl.DataFrame, n_quantiles: int = 5) -> pl.DataFrame:
    """Table réserve large, maille COMMUNE, POUR TOUTE LA FRANCE (dézoom carte
    + communes en repli, ADR 0002 point 1 / CONTEXT.md « Repli »).

    Une ligne par `code_commune`, de deux origines mélangées dans UNE seule
    population (pour un quantile cohérent, cf. `preparer_carte_reserve`) :

    - communes en repli (`maille == "commune"` dans `table_reserve`) : valeur
      déjà à cette maille, reprise TELLE QUELLE (`degrade=True`) -- jamais de
      contour bureau fiable pour elles (CONTEXT.md « Repli »), la dégradation
      reste visible plutôt que masquée ;
    - communes stables (`maille == "bureau"`) : SOMME des réserves de leurs
      bureaux (jamais une moyenne, CLAUDE.md « Never average percentages » --
      s'applique de la même façon à un compte de voix agrégé), `degrade=False`
      -- un agrégat de dézoom, pas une dégradation.

    `code_commune` dérivé de `unite_id` : les 5 premiers caractères pour une
    unité bureau (`unite_id` = `id_bv` = code_commune + "_" + code_bureau,
    CONTEXT.md « id_bv »), `unite_id` lui-même pour une unité déjà à la
    maille commune.
    """
    repli = table_reserve.filter(pl.col("maille") == "commune").with_columns(
        pl.col("unite_id").alias("code_commune"), pl.lit(True).alias("degrade")
    )
    bureau = table_reserve.filter(pl.col("maille") == "bureau").with_columns(
        pl.col("unite_id").str.slice(0, 5).alias("code_commune")
    )
    agrege_bureau = (
        bureau.sort(["code_commune", "bloc", "unite_id"])
        .group_by(["code_commune", "bloc"], maintain_order=True)
        .agg(
            pl.col("reserve").sum(),
            pl.col("inscrits").sum(),
            pl.col("code_departement").first(),
            pl.col("statut").first(),
        )
        .with_columns(pl.lit(False).alias("degrade"))
    )
    colonnes = ["code_commune", "bloc", "reserve", "inscrits", "code_departement", "statut", "degrade"]
    longue = pl.concat([repli.select(colonnes), agrege_bureau.select(colonnes)], how="vertical_relaxed")
    return _reserve_large(longue, cle="code_commune", n_quantiles=n_quantiles)


# --- Rapport de force projeté (couche de contexte, ADR 0002 point 2) ------------


def preparer_carte_rapport_force(baseline: pl.DataFrame, n_quantiles: int = 4) -> pl.DataFrame:
    """Table rapport de force large : une ligne par `unite_id` (bureau OU
    commune en repli, mêmes deux mailles que la baseline #5) --
    `bloc_tete_projete` (bloc au composite maximal) + `quantile_rapport_force`
    (quantile large DU BLOC EN TÊTE, dans SA PROPRE distribution -- cf.
    docstring du module).

    Départage déterministe des égalités de composite : tri (composite
    décroissant, bloc croissant) avant de prendre la première ligne par
    unité -- jamais un ordre d'arrivée non spécifié. Une unité sans aucun
    composite non nul (cas dégénéré, pas rencontré en pratique) n'a pas de
    ligne de sortie plutôt qu'un bloc en tête fabriqué.

    Aucune agrégation commune n'est recalculée ici pour les communes stables
    dézoomées (cf. docstring du module, limitation documentée) : les communes
    en repli ont déjà un composite valide à la maille communale, calculé
    depuis des voix par `projections.baseline`, jamais fabriqué.
    """
    avec_quantile = quantiles_larges(baseline, "composite", groupe="bloc", n=n_quantiles)
    return (
        avec_quantile.filter(pl.col("composite").is_not_null())
        .sort(["unite_id", "composite", "bloc"], descending=[False, True, False])
        .group_by("unite_id", maintain_order=True)
        .agg(
            pl.col("bloc").first().alias("bloc_tete_projete"),
            pl.col("quantile_composite").first().alias("quantile_rapport_force"),
            pl.col("code_departement").first(),
            pl.col("statut").first(),
            pl.col("maille").first(),
        )
        .sort("unite_id")
    )


# --- Assemblage réserve + rapport de force, par maille (pour build_tiles.py) ----


def assembler_donnees_bureau(
    table_reserve: pl.DataFrame,
    baseline: pl.DataFrame,
    n_quantiles_reserve: int = 5,
    n_quantiles_force: int = 4,
) -> pl.DataFrame:
    """Réserve + rapport de force pour la couche tuiles `mobilisation_bureaux`
    (maille bureau uniquement) : une ligne par `unite_id`.

    Jointure PLEINE (`how="full"`) sur `unite_id`, jamais interne : une unité
    présente d'un seul côté (réserve calculable mais composite non défini, ou
    l'inverse -- cas dégénérés, non rencontrés en pratique) garde ses colonnes
    de l'autre côté à null plutôt que de disparaître silencieusement.
    """
    reserve = preparer_carte_reserve(table_reserve, n_quantiles=n_quantiles_reserve)
    force = preparer_carte_rapport_force(baseline, n_quantiles=n_quantiles_force).filter(pl.col("maille") == "bureau")
    colonnes_partagees = [c for c in ("code_departement", "statut", "maille") if c in force.columns]
    force_sans_doublon = force.drop(colonnes_partagees)
    return reserve.join(force_sans_doublon, on="unite_id", how="full", coalesce=True).sort("unite_id")


def assembler_donnees_commune(
    table_reserve: pl.DataFrame,
    baseline: pl.DataFrame,
    n_quantiles_reserve: int = 5,
    n_quantiles_force: int = 4,
) -> pl.DataFrame:
    """Réserve (dézoom + repli) + rapport de force (REPLI SEULEMENT, cf.
    limitation documentée dans `preparer_carte_rapport_force`) pour la couche
    tuiles `mobilisation_communes` : une ligne par `code_commune`, pour toute
    la France.

    Jointure `left` (jamais `inner`) : les communes stables dézoomées restent
    dans la sortie même sans rapport de force agrégé (colonnes null, jamais
    une ligne perdue).
    """
    reserve_commune = agreger_reserve_commune(table_reserve, n_quantiles=n_quantiles_reserve)
    force_repli = (
        preparer_carte_rapport_force(baseline, n_quantiles=n_quantiles_force)
        .filter(pl.col("maille") == "commune")
        .rename({"unite_id": "code_commune"})
        .select("code_commune", "bloc_tete_projete", "quantile_rapport_force")
    )
    return reserve_commune.join(force_repli, on="code_commune", how="left").sort("code_commune")


# --- Orchestration : gate + assemblage, un seul passage (issue #26) -------------


def construire_donnees_mobilisation(
    panel_avec_statut: pl.DataFrame,
    baseline: pl.DataFrame,
    methode_part: str = METHODE_PART_DEFAUT,
    n_quantiles_reserve: int = 5,
    n_quantiles_force: int = 4,
) -> dict:
    """Pipeline complet panel + baseline -> données mobilisation prêtes pour les
    tuiles (issue #26). Point d'entrée unique appelé par `projections.build_tiles`.

    Réutilise `projections.reserve.generer_rapport_complet` TEL QUEL pour le
    verdict de publication ET la table réserve (jamais recalculés séparément
    -- la carte et `reserve-2027.md` doivent porter exactement la même donnée,
    même discipline que le verrou CLI/notebook des issues #24/#25).
    `verifier_publication_autorisee` lève AVANT tout assemblage bureau/commune
    si le verdict est FAIL : refus mécanique, pas de tuiles mobilisation
    préparées pour un verdict rouge.
    """
    sortie_reserve = generer_rapport_complet(panel_avec_statut, baseline, methode_part=methode_part)
    verifier_publication_autorisee(sortie_reserve["pass_carte_mobilisation"])
    table_reserve = sortie_reserve["table_reserve"]
    return {
        "donnees_bureau": assembler_donnees_bureau(table_reserve, baseline, n_quantiles_reserve, n_quantiles_force),
        "donnees_commune": assembler_donnees_commune(table_reserve, baseline, n_quantiles_reserve, n_quantiles_force),
        "pass_carte_mobilisation": sortie_reserve["pass_carte_mobilisation"],
    }


def verifier_publication_autorisee(pass_carte_mobilisation: bool) -> None:
    """Lève si le verdict de publication de la carte mobilisation est rouge.

    `pass_carte_mobilisation` : booléen déjà calculé par
    `projections.backtest.verdict_carte_mobilisation` (jamais recalculé ici --
    cf. docstring du module). Appelée en tête de la construction des tuiles
    mobilisation : un gate qui ne peut pas bloquer ne vaut rien (même
    philosophie que `docs/adr/0001-sortie-ordinale-gate-backtest.md`).
    """
    if not pass_carte_mobilisation:
        raise RuntimeError(
            "Verdict de publication de la carte mobilisation : FAIL (clause participation ADR 0003 "
            "et/ou garde anti-hasard, cf. `projections.backtest.verdict_carte_mobilisation`). "
            "Construction des tuiles mobilisation refusée -- la tranche s'arrête à la préparation, "
            "pas de mise en ligne (issue #26)."
        )

"""Backtests 2022->2024 et verdict du gate de publication (issue #6, HANDOFF.md
étape 2, ADR 0001).

## Règle anti-fuite (cardinale)

Le backtest simule quelqu'un en 2022 qui prédit 2024. Le prédicteur "2022" ne
doit incorporer AUCUNE donnée 2024 :

- `isoler_scrutins_2022` filtre le panel aux seuls `id_election` 2022
  (présidentielle T1 + législatives T1) AVANT tout calcul -- garde-fou
  physique, pas seulement documentaire : une ligne 2024 ne peut pas entrer
  dans `construire_predicteur_2022` même si le panel complet lui est passé.
- Baseline mono-scrutin 2022 = `ecart_2022_pres_t1` seul (écart relatif au
  national, `projections.baseline.calculer_ecart_national`).
- Baseline composite 2022 = présidentielle 2022 brute + législatives 2022
  corrigées de l'offre -- la correction s'impute depuis la présidentielle
  2022 (`scrutin_reference=SCRUTIN_PRESIDENTIELLE`), JAMAIS depuis les
  européennes 2024 (contrairement à la baseline #5, qui corrige les
  législatives 2024 depuis les européennes 2024 -- ce repli-là n'existe pas
  ici par construction, cf. `construire_predicteur_2022`).
- Les cibles (structure 2024 observée : européennes puis législatives
  corrigées) sont lues directement dans `baseline_unite_bloc.parquet`
  (sortie de `projections.baseline`, issue #5) : côté cible, c'est de la
  donnée observée, pas de fuite -- ces colonnes ne participent JAMAIS à la
  construction du prédicteur 2022 ci-dessus.

## Périmètre

Tous les calculs de ce module portent sur les unités **joint-validées**
du panel (statut `joint_valide`, maille bureau, cf. `projections.churn`) --
les unités en repli (maille commune) sont exclues : mélanger une validation
de rang à la maille bureau avec des agrégats communaux comparerait des
granularités différentes. `construire_table_backtest` conserve la colonne
`statut` ; c'est aux appelants (`executer_backtests`, le notebook) de
filtrer avant de corréler.

## Tercile compétitif

Pour chaque bloc, le tiers central du classement de `composite_2022` (le
prédicteur composite 2022, la meilleure estimation disponible à l'époque) --
là où les bureaux sont ni bastions ni déserts pour ce bloc, l'endroit où la
carte prétend servir (persuasion). Défini par percentile de rang au sein du
bloc (bornes 1/3 et 2/3), cf. `tercile_competitif`.

## Spearman en Polars pur

`correlation_spearman` = corrélation de Pearson calculée sur les rangs
(méthode "average", gère les ex-aequo comme scipy.stats.spearmanr) -- aucune
nouvelle dépendance.

## Gate (ADR 0001, seuils gravés, appliqués ici, jamais réinterprétés)

- ρ ≥ 0,7 par bloc majeur (Extrême droite, Gauche) sur l'ensemble des
  unités joint-validées ;
- ρ ≥ 0,5 sur le tercile compétitif ;
- le composite doit faire au moins aussi bien que la meilleure baseline
  mono-scrutin (ici, l'unique candidat mono-scrutin : présidentielle 2022
  seule).

`evaluer_gate` calcule un verdict PASS/FAIL explicite par bloc majeur x
cible (européennes, législatives corrigées) -- un backtest qui ne peut pas
échouer ne valide rien : si un seuil échoue, le code et le rapport le disent
franchement. Le gate ne bloque QUE la publication de la carte structurelle
(décision humaine), jamais le merge du code.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import polars as pl

from projections.baseline import (
    SCRUTIN_EUROPEENNES,
    SCRUTIN_LEGISLATIVES,
    SCRUTIN_PRESIDENTIELLE,
    calculer_ecart_national,
    composite_pondere,
    construire_table_composantes,
    corriger_offre_legislatives,
)
from projections.churn import STATUT_JOINT_VALIDE

INTERIM_DIR = Path("data/interim")

# --- Constantes -----------------------------------------------------------

SCRUTIN_LEGISLATIVES_2022 = "2022_legi_t1"
SCRUTIN_LEGISLATIVES_2022_CORRIGE = f"{SCRUTIN_LEGISLATIVES_2022}_corrige"

# Anti-fuite : le prédicteur "2022" ne peut être construit qu'à partir de ces
# 2 identifiants de scrutin (cf. docstring du module).
SCRUTINS_PREDICTEUR_2022: tuple[str, ...] = (SCRUTIN_PRESIDENTIELLE, SCRUTIN_LEGISLATIVES_2022)

CIBLE_EUROPEENNES = "ecart_2024_euro_t1"
CIBLE_LEGISLATIVES = "ecart_2024_legi_t1_corrige"
CIBLES: dict[str, str] = {"euro": CIBLE_EUROPEENNES, "legi": CIBLE_LEGISLATIVES}

COLONNE_MONO = f"ecart_{SCRUTIN_PRESIDENTIELLE}"
COLONNE_COMPOSITE = "composite_2022"
PREDICTEURS: dict[str, str] = {"mono": COLONNE_MONO, "composite": COLONNE_COMPOSITE}

# Point de départ documenté (pas une constante figée, cf. calibrer_poids) :
# légèrement plus de poids à la présidentielle (participation plus homogène
# sur tout le territoire que des législatives où l'offre varie).
POIDS_COMPOSITE_2022_PAR_DEFAUT: dict[str, float] = {
    SCRUTIN_PRESIDENTIELLE: 0.6,
    SCRUTIN_LEGISLATIVES_2022_CORRIGE: 0.4,
}

# Gate ADR 0001 -- seuils gravés à la session de cadrage du 2026-07-22, ne
# jamais les recalibrer après avoir vu les résultats (docs/adr/0001).
BLOCS_MAJEURS: tuple[str, ...] = ("Extrême droite", "Gauche")
SEUIL_RHO_ENSEMBLE = 0.7
SEUIL_RHO_TERCILE = 0.5

# Backtest participation + garde anti-hasard (ADR 0002, issue #24) -- seuil
# gravé à la session de cadrage, ne jamais le recalibrer après avoir vu les
# résultats (même règle que le gate ADR 0001 ci-dessus).
SCRUTINS_PARTICIPATION: tuple[str, ...] = (SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES, SCRUTIN_LEGISLATIVES)
COLONNE_ABSTENTION_PREDICTEUR = f"abstention_{SCRUTIN_PRESIDENTIELLE}"
CIBLES_PARTICIPATION: dict[str, str] = {
    "euro": f"abstention_{SCRUTIN_EUROPEENNES}",
    "legi": f"abstention_{SCRUTIN_LEGISLATIVES}",
}
SEUIL_RHO_PARTICIPATION = 0.8


# --- Prédicteur 2022 (anti-fuite) ------------------------------------------


def isoler_scrutins_2022(panel: pl.DataFrame) -> pl.DataFrame:
    """Garde-fou anti-fuite : ne garde que les lignes des scrutins 2022 du panel.

    Appelé en tête de `construire_predicteur_2022` : le reste du pipeline ne
    peut physiquement pas voir une ligne 2024, même si on lui passe le panel
    complet par erreur.
    """
    return panel.filter(pl.col("id_election").is_in(SCRUTINS_PREDICTEUR_2022))


def construire_predicteur_2022(
    panel: pl.DataFrame,
    poids: dict[str, float] | None = None,
    methode_correction: str = "imputation",
) -> pl.DataFrame:
    """Prédicteur 2022 (mono-scrutin + composite), construit sans aucune donnée 2024.

    `panel` : panel complet ou déjà restreint à 2022 -- `isoler_scrutins_2022`
    est appelé en premier dans tous les cas (cf. docstring du module). Les
    législatives 2022 sont corrigées de l'offre en imputant depuis la
    présidentielle 2022 (`scrutin_reference=SCRUTIN_PRESIDENTIELLE`), jamais
    depuis un scrutin 2024.

    Retourne une table unité x bloc avec les colonnes `ecart_2022_pres_t1`
    (mono-scrutin), `ecart_2022_legi_t1_corrige` et `composite_2022`.
    """
    panel_2022 = isoler_scrutins_2022(panel)
    ecart = calculer_ecart_national(panel_2022, scrutins=SCRUTINS_PREDICTEUR_2022)
    legi_corrige = corriger_offre_legislatives(
        ecart,
        scrutin_a_corriger=SCRUTIN_LEGISLATIVES_2022,
        scrutin_reference=SCRUTIN_PRESIDENTIELLE,
        methode=methode_correction,
    )
    table = construire_table_composantes(ecart, legi_corrige, scrutins_bruts=[SCRUTIN_PRESIDENTIELLE])
    return composite_pondere(table, poids=poids or POIDS_COMPOSITE_2022_PAR_DEFAUT, nom_colonne=COLONNE_COMPOSITE)


def construire_table_backtest(
    panel: pl.DataFrame,
    baseline: pl.DataFrame,
    poids_composite_2022: dict[str, float] | None = None,
    methode_correction: str = "imputation",
) -> pl.DataFrame:
    """Table de travail du backtest : prédicteur 2022 joint aux cibles 2024 observées.

    `baseline` : sortie de `projections.baseline.construire_baseline` (issue
    #5) -- fournit les cibles (`ecart_2024_euro_t1`, `ecart_2024_legi_t1_corrige`,
    déjà des données observées, jamais utilisées côté prédicteur) ainsi que
    `statut`/`maille`/`derive`/`code_departement`. Jointure interne sur
    (unite_id, bloc) : une unité absente de la baseline (ou du prédicteur)
    n'a pas de ligne cible (resp. prédicteur) comparable, donc pas de ligne
    de sortie -- c'est la définition même des "unités jointes" du périmètre.
    """
    predicteur = construire_predicteur_2022(panel, poids=poids_composite_2022, methode_correction=methode_correction)
    cibles = baseline.select(
        "unite_id",
        "bloc",
        CIBLE_EUROPEENNES,
        CIBLE_LEGISLATIVES,
        "derive",
        "statut",
        "maille",
        "code_departement",
    )
    return predicteur.join(cibles, on=["unite_id", "bloc"], how="inner")


# --- Spearman en Polars pur --------------------------------------------------


def correlation_spearman(table: pl.DataFrame, colonne_x: str, colonne_y: str) -> float:
    """Corrélation de rang de Spearman = Pearson calculée sur les rangs.

    Rangs "average" (ex-aequo -> moyenne de leurs rangs, comme
    `scipy.stats.spearmanr`) ; lignes avec une valeur nulle dans l'une des 2
    colonnes exclues avant le calcul. Moins de 2 points valides -> `nan`
    (rho non défini), jamais une erreur de division par zéro silencieuse.
    """
    valide = table.select(colonne_x, colonne_y).drop_nulls()
    if valide.height < 2:
        return float("nan")
    rangs = valide.select(
        pl.col(colonne_x).rank(method="average").alias("_rang_x"),
        pl.col(colonne_y).rank(method="average").alias("_rang_y"),
    )
    if rangs.get_column("_rang_x").n_unique() < 2 or rangs.get_column("_rang_y").n_unique() < 2:
        return float("nan")  # colonne constante -> corrélation non définie
    return rangs.select(pl.corr("_rang_x", "_rang_y")).item()


def rho_par_bloc(table: pl.DataFrame, colonne_predicteur: str, colonne_cible: str) -> pl.DataFrame:
    """Spearman(colonne_predicteur, colonne_cible), par bloc, avec la taille d'échantillon."""
    lignes = []
    for bloc in sorted(table.get_column("bloc").unique().to_list()):
        sous_table = table.filter(pl.col("bloc") == bloc)
        n = sous_table.select(colonne_predicteur, colonne_cible).drop_nulls().height
        rho = correlation_spearman(sous_table, colonne_predicteur, colonne_cible)
        lignes.append({"bloc": bloc, "rho": rho, "n": n})
    return pl.DataFrame(lignes, schema={"bloc": pl.String, "rho": pl.Float64, "n": pl.Int64})


# --- Tercile compétitif ------------------------------------------------------


def tercile_competitif(table: pl.DataFrame, colonne: str = COLONNE_COMPOSITE, bloc_col: str = "bloc") -> pl.DataFrame:
    """Ajoute `tercile_competitif` (bool) : tiers central du classement de `colonne`, par bloc.

    Définition opérationnelle (documentée AVANT le calcul, cf. docstring du
    module) : pour chaque bloc, le percentile de rang (rang moyen ex-aequo,
    normalisé en [0, 1] par bloc) est calculé sur `colonne` ; le tercile
    compétitif est le sous-ensemble [1/3, 2/3] -- ni bastion (extrémité
    haute), ni désert (extrémité basse). Une valeur nulle de `colonne` ne
    peut pas être classée -> `tercile_competitif` false.
    """
    rang = pl.col(colonne).rank(method="average").over(bloc_col)
    effectif = pl.col(colonne).is_not_null().sum().over(bloc_col)
    percentile = (rang - 1) / (effectif - 1)
    dans_le_tercile = (
        pl.col(colonne).is_not_null() & (effectif > 1) & (percentile >= 1 / 3) & (percentile <= 2 / 3)
    )
    return table.with_columns(dans_le_tercile.fill_null(False).alias("tercile_competitif"))


# --- Corrélation géographique RN européennes <-> présidentielle -------------


def correlation_euro_pres_rn(table: pl.DataFrame, bloc: str = "Extrême droite") -> float:
    """Spearman(ecart_2022_pres_t1, ecart_2024_euro_t1) pour `bloc` (défaut Extrême droite).

    Le chiffre absent de la littérature (HANDOFF.md étape 2) : équivalent du
    0,89 CEVIPOF mesuré pour la gauche. Identique par construction à la ligne
    (predicteur=mono, cible=euro, scope=ensemble, bloc=`bloc`) du backtest 1
    -- fonction dédiée pour la lisibilité du rapport et la testabilité
    isolée, pas un second calcul indépendant.
    """
    return correlation_spearman(table.filter(pl.col("bloc") == bloc), COLONNE_MONO, CIBLE_EUROPEENNES)


# --- Distribution du swing ---------------------------------------------------


def distribution_swing(table: pl.DataFrame, bloc: str = "Extrême droite", colonne: str = "derive") -> dict:
    """Statistiques de forme (quantiles, asymétrie) de `colonne` pour `bloc`."""
    serie = table.filter(pl.col("bloc") == bloc).get_column(colonne).drop_nulls()
    if serie.len() == 0:
        return {"n": 0}
    quantiles = {f"p{int(q * 100)}": serie.quantile(q) for q in (0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)}
    return {
        "n": serie.len(),
        "min": serie.min(),
        "max": serie.max(),
        "mean": serie.mean(),
        "median": serie.median(),
        "skew": serie.skew(),
        **quantiles,
    }


def verifier_regularite_seuil(
    table: pl.DataFrame,
    bloc: str = "Extrême droite",
    colonne: str = "derive",
    n_bins: int = 20,
    seuil_alerte: float = 1.5,
) -> dict:
    """Condition de régularité : pas de DISCONTINUITÉ anormale au seuil de décision.

    Seuil pris comme la MÉDIANE de `colonne` -- choix défendable et
    documenté (cf. docstring du module) : le point qui sépare, dans le
    classement produit, les unités où le bloc progresse de celles où il
    recule. Découpe `colonne` en `n_bins` classes de largeur égale entre ses
    percentiles 1 et 99 (PAS son min/max : le swing par bureau a des queues
    extrêmes -- quelques bureaux à très faibles exprimés -- qui dilateraient
    artificiellement la largeur de classe). Compare la densité de la classe
    contenant le seuil à la densité MOYENNE DE SES 2 CLASSES VOISINES
    (immédiatement inférieure et supérieure) -- pas à la densité moyenne sur
    l'ensemble des classes, qui confondrait la forme globale de la
    distribution (une variable de swing est naturellement piquée en son
    centre, cf. `distribution_swing`) avec une vraie discontinuité locale au
    seuil. `anomalie` si le ratio dépasse `seuil_alerte` (1,5x la densité
    des voisins par défaut) -- un test dans l'esprit d'un test de
    manipulation (densité locale, à la McCrary), pas une estimation de
    densité à noyau complète (ponytail : bins équidistants + voisins
    immédiats, à raffiner si ce diagnostic devient un critère du gate).
    """
    serie = table.filter(pl.col("bloc") == bloc).get_column(colonne).drop_nulls()
    if serie.len() < 2:
        return {"n": serie.len(), "anomalie": False}
    seuil = serie.median()
    borne_basse, borne_haute = serie.quantile(0.01), serie.quantile(0.99)
    largeur = (borne_haute - borne_basse) / n_bins
    if largeur == 0:
        return {"n": serie.len(), "seuil": seuil, "anomalie": False}

    classes = ((serie - borne_basse) / largeur).floor().clip(0, n_bins - 1).cast(pl.Int64)
    comptes_observes = pl.DataFrame({"classe": classes}).group_by("classe").agg(pl.len().alias("n"))
    # Classes complètes 0..n_bins-1, y compris celles sans aucune observation
    # (n=0) : sans ce complétage, une classe vide fausserait silencieusement
    # la moyenne des voisins (elle disparaîtrait de la comparaison au lieu de
    # compter comme une densité nulle).
    comptes = (
        pl.DataFrame({"classe": list(range(n_bins))})
        .join(comptes_observes, on="classe", how="left")
        .with_columns(pl.col("n").fill_null(0))
    )

    indice_seuil = min(max(int((seuil - borne_basse) / largeur), 0), n_bins - 1)
    densite_seuil = comptes.filter(pl.col("classe") == indice_seuil).get_column("n")[0]
    voisins = [i for i in (indice_seuil - 1, indice_seuil + 1) if 0 <= i < n_bins]
    densites_voisines = comptes.filter(pl.col("classe").is_in(voisins)).get_column("n")

    if densites_voisines.len() == 0:
        # Pas de classe voisine calculable (n_bins trop petit) : diagnostic
        # non disponible, jamais une fausse "absence d'anomalie".
        return {"n": serie.len(), "seuil": seuil, "n_bins": n_bins, "anomalie": False}

    densite_voisine_moyenne = densites_voisines.mean()
    if densite_voisine_moyenne == 0:
        # Voisins vides : un seuil non nul y est un pic isolé (ratio infini),
        # pas une absence de signal -- l'inverse de `bool(0) == False` aurait
        # silencieusement classé ce cas-là comme "pas d'anomalie".
        ratio = float("inf") if densite_seuil > 0 else 0.0
    else:
        ratio = densite_seuil / densite_voisine_moyenne
    return {
        "n": serie.len(),
        "seuil": seuil,
        "n_bins": n_bins,
        "densite_classe_seuil": densite_seuil,
        "densite_voisine_moyenne": densite_voisine_moyenne,
        "ratio": ratio,
        "anomalie": ratio > seuil_alerte,
    }


# --- Gate ADR 0001 ------------------------------------------------------------


def evaluer_gate(
    resultats: pl.DataFrame,
    blocs: tuple[str, ...] = BLOCS_MAJEURS,
    seuil_ensemble: float = SEUIL_RHO_ENSEMBLE,
    seuil_tercile: float = SEUIL_RHO_TERCILE,
) -> pl.DataFrame:
    """Verdict PASS/FAIL du gate ADR 0001, par bloc majeur x cible.

    `resultats` : table longue (colonnes `predicteur` in {mono, composite},
    `cible` in {euro, legi}, `scope` in {ensemble, tercile}, `bloc`, `rho`) --
    sortie de `executer_backtests`. Applique, pour chaque (bloc, cible) où
    bloc est un bloc majeur : ρ_ensemble(composite) ≥ `seuil_ensemble`,
    ρ_tercile(composite) ≥ `seuil_tercile`, ρ_ensemble(composite) ≥
    ρ_ensemble(mono) -- les 3 clauses du gate (docs/adr/0001), jamais
    réinterprétées ici.
    """

    def _rho(bloc: str, cible: str, predicteur: str, scope: str) -> float:
        ligne = resultats.filter(
            (pl.col("bloc") == bloc)
            & (pl.col("cible") == cible)
            & (pl.col("predicteur") == predicteur)
            & (pl.col("scope") == scope)
        )
        if ligne.height == 0:
            return float("nan")
        return ligne.get_column("rho")[0]

    lignes = []
    for bloc in blocs:
        for cible in sorted(resultats.get_column("cible").unique().to_list()):
            rho_ens_composite = _rho(bloc, cible, "composite", "ensemble")
            rho_ter_composite = _rho(bloc, cible, "composite", "tercile")
            rho_ens_mono = _rho(bloc, cible, "mono", "ensemble")

            pass_ensemble = rho_ens_composite >= seuil_ensemble
            pass_tercile = rho_ter_composite >= seuil_tercile
            pass_vs_mono = rho_ens_composite >= rho_ens_mono

            lignes.append(
                {
                    "bloc": bloc,
                    "cible": cible,
                    "rho_ensemble_composite": rho_ens_composite,
                    "seuil_ensemble": seuil_ensemble,
                    "pass_ensemble": pass_ensemble,
                    "rho_tercile_composite": rho_ter_composite,
                    "seuil_tercile": seuil_tercile,
                    "pass_tercile": pass_tercile,
                    "rho_ensemble_mono": rho_ens_mono,
                    "pass_composite_vs_mono": pass_vs_mono,
                    "pass_global": pass_ensemble and pass_tercile and pass_vs_mono,
                }
            )
    return pl.DataFrame(lignes)


def verdict_global(verdict: pl.DataFrame) -> bool:
    """PASS uniquement si toutes les lignes (bloc x cible) du gate sont PASS.

    Générique : ne lit que la colonne `pass_global`, réutilisée telle quelle
    par `evaluer_gate_participation` et par les tables de la garde anti-hasard
    (ADR 0002, issue #24) -- même contrat, pas une réimplémentation par gate.
    """
    return bool(verdict.height) and bool(verdict.get_column("pass_global").all())


# --- Backtest participation (ADR 0002, issue #24) ------------------------------
#
# Corrélation de rang du taux d'abstention par bureau, présidentielle 2022 T1
# -> européennes 2024 ET législatives 2024 T1, sur l'ensemble des bureaux
# joints (statut joint_valide, même périmètre que le backtest structure).
# Anti-fuite par construction : le prédicteur est `abstention_2022_pres_t1`,
# un seul scrutin 2022, structurellement aveugle à 2024 -- aucune fonction ici
# n'a besoin d'un garde-fou `isoler_scrutins_2022` séparé, il n'y a qu'un seul
# scrutin côté prédicteur. Clause pré-enregistrée (ADR 0002) : ρ ≥ 0,8 par
# cible. `abstentions`/`inscrits` sont des colonnes de participation répétées
# sur chaque ligne de bloc du panel long -- dédupliquées avant tout calcul,
# jamais moyennées (CLAUDE.md « Never average percentages »).


def calculer_taux_abstention(panel: pl.DataFrame, scrutins: tuple[str, ...] = SCRUTINS_PARTICIPATION) -> pl.DataFrame:
    """Taux d'abstention (abstentions / inscrits) par unité x scrutin.

    `panel` : table longue bureau/commune x scrutin x bloc -- `abstentions` et
    `inscrits` y sont répétés sur chaque ligne de bloc, dédupliqués ici avant
    de diviser (jamais une moyenne de taux déjà calculés). `inscrits` nul (cas
    réel rarissime) -> taux null, jamais une division par zéro silencieuse.
    """
    df = panel.with_columns(pl.coalesce(["id_bv", "code_commune"]).alias("unite_id")).filter(
        pl.col("id_election").is_in(list(scrutins))
    )
    participation = df.select("id_election", "unite_id", "abstentions", "inscrits").unique()
    return participation.with_columns(
        pl.when(pl.col("inscrits") > 0)
        .then(pl.col("abstentions") / pl.col("inscrits"))
        .otherwise(None)
        .alias("taux_abstention")
    )


def construire_table_participation(panel: pl.DataFrame, baseline: pl.DataFrame) -> pl.DataFrame:
    """Table de travail du backtest participation : abstention 2022 (prédicteur)
    x abstention 2024 (cibles), par unité, colonnes larges.

    `baseline` : sortie de `projections.baseline.construire_baseline` (issue
    #5) -- fournit `code_departement`/`statut`/`maille` par unité, mêmes
    colonnes et même provenance que `construire_table_backtest` (pas
    recalculées ici). Jointure interne : une unité sans les 3 scrutins de
    `SCRUTINS_PARTICIPATION` a des colonnes nulles côté manquant, gérées par
    `correlation_spearman` (drop_nulls), jamais une ligne perdue en amont.
    """
    taux = calculer_taux_abstention(panel)
    large = taux.pivot(on="id_election", index="unite_id", values="taux_abstention")
    renommage = {scrutin: f"abstention_{scrutin}" for scrutin in SCRUTINS_PARTICIPATION if scrutin in large.columns}
    large = large.rename(renommage)
    contexte = baseline.select("unite_id", "code_departement", "statut", "maille").unique(
        subset="unite_id", keep="first"
    )
    return large.join(contexte, on="unite_id", how="inner")


def evaluer_gate_participation(resultats: pl.DataFrame, seuil: float = SEUIL_RHO_PARTICIPATION) -> pl.DataFrame:
    """Verdict PASS/FAIL du backtest participation (ADR 0002) : ρ ≥ 0,8 par cible.

    `resultats` : table `cible` x `rho` x `n` (sortie de
    `executer_backtest_participation`). Ajoute `seuil` et `pass_global`
    (`>=` strict, même convention que le gate ADR 0001) -- colonne réutilisée
    telle quelle par `verdict_global`.
    """
    return resultats.with_columns(
        pl.lit(seuil).alias("seuil"),
        (pl.col("rho") >= seuil).alias("pass_global"),
    )


def executer_backtest_participation(panel: pl.DataFrame, baseline: pl.DataFrame) -> dict:
    """Calcule le backtest participation (ADR 0002) sur le périmètre joint-validé.

    Retourne un dict : `table` (table de travail, jointe-validée, maille
    bureau), `resultats` (cible x rho x n x seuil x pass_global), et l'accord
    inter-cibles publié en contexte (`rho_inter_cibles`, `n_inter_cibles` --
    abstention 2024 européennes vs abstention 2024 législatives, même
    transparence que les plafonds inter-cibles du tercile, cf. ADR 0002).
    """
    table_brute = construire_table_participation(panel, baseline)
    table = table_brute.filter(pl.col("statut") == STATUT_JOINT_VALIDE)

    lignes = [
        {
            "cible": nom_cible,
            "rho": correlation_spearman(table, COLONNE_ABSTENTION_PREDICTEUR, colonne_cible),
            "n": table.select(COLONNE_ABSTENTION_PREDICTEUR, colonne_cible).drop_nulls().height,
        }
        for nom_cible, colonne_cible in CIBLES_PARTICIPATION.items()
    ]
    resultats = evaluer_gate_participation(
        pl.DataFrame(lignes, schema={"cible": pl.String, "rho": pl.Float64, "n": pl.Int64})
    )

    colonne_euro, colonne_legi = CIBLES_PARTICIPATION["euro"], CIBLES_PARTICIPATION["legi"]
    return {
        "table": table,
        "resultats": resultats,
        "rho_inter_cibles": correlation_spearman(table, colonne_euro, colonne_legi),
        "n_inter_cibles": table.select(colonne_euro, colonne_legi).drop_nulls().height,
    }


# --- Garde anti-hasard (ADR 0002, issue #24) -----------------------------------
#
# Pour la métrique principale de chaque backtest publié (composite ensemble,
# blocs majeurs x cibles pour la structure ; rho par cible pour la
# participation), lift contre 2 nulls : le hasard (rho = 0, l'espérance
# théorique d'un classement indépendant -- contexte, jamais recalculé par
# permutation) et le prédicteur à maille département (chaque bureau prédit
# par la valeur de son département, RECALCULÉE PAR SOMMES de voix/exprimés ou
# d'abstentions/inscrits -- jamais une moyenne des écarts ou des taux de
# bureau, CLAUDE.md « Never average percentages »). Clause : la granularité
# bureau doit BATTRE (>, pas >=) la granularité département.


def calculer_ecart_national_departement(panel: pl.DataFrame, scrutins: tuple[str, ...] | None = None) -> pl.DataFrame:
    """Écart relatif au national à la maille département (garde anti-hasard).

    Même convention que `projections.baseline.calculer_ecart_national` (écart
    en points des exprimés vs national), mais volontairement une fonction
    séparée plutôt qu'un paramètre de granularité sur celle-ci : recalculer à
    une maille plus grossière qu'un bureau/commune est une agrégation
    plusieurs-vers-un (plusieurs bureaux par département), pas un simple
    changement d'étiquette -- voix et exprimés sont dédupliqués par
    bureau/commune PUIS RESOMMÉS par département avant de recalculer la part,
    jamais une moyenne des écarts de bureau.
    """
    df = panel.with_columns(pl.coalesce(["id_bv", "code_commune"]).alias("unite_id"))
    if scrutins is not None:
        df = df.filter(pl.col("id_election").is_in(list(scrutins)))

    exprimes_bureau = df.select("id_election", "unite_id", "code_departement", "exprimes").unique()
    exprimes_departement = exprimes_bureau.group_by(["id_election", "code_departement"]).agg(
        pl.col("exprimes").sum().alias("exprimes_departement")
    )
    exprimes_national = exprimes_bureau.group_by("id_election").agg(
        pl.col("exprimes").sum().alias("exprimes_national")
    )
    voix_departement = df.group_by(["id_election", "code_departement", "bloc"]).agg(
        pl.col("voix").sum().alias("voix_departement")
    )
    voix_national = df.group_by(["id_election", "bloc"]).agg(pl.col("voix").sum().alias("voix_national"))
    national = voix_national.join(exprimes_national, on="id_election").with_columns(
        (pl.col("voix_national") / pl.col("exprimes_national")).alias("pct_national")
    )

    return (
        voix_departement.join(exprimes_departement, on=["id_election", "code_departement"])
        .with_columns(
            pl.when(pl.col("exprimes_departement") > 0)
            .then(pl.col("voix_departement") / pl.col("exprimes_departement"))
            .otherwise(None)
            .alias("pct_unite")
        )
        .join(national.select("id_election", "bloc", "pct_national"), on=["id_election", "bloc"])
        .with_columns(((pl.col("pct_unite") - pl.col("pct_national")) * 100).alias("ecart_national"))
        .rename({"code_departement": "unite_id"})
        .sort(["id_election", "unite_id", "bloc"])
    )


def construire_predicteur_departemental_2022(
    panel: pl.DataFrame,
    poids: dict[str, float] | None = None,
    methode_correction: str = "imputation",
) -> pl.DataFrame:
    """Prédicteur 2022 à la maille département (garde anti-hasard, ADR 0002).

    Même construction anti-fuite que `construire_predicteur_2022`
    (`isoler_scrutins_2022` en tête -- aucune donnée 2024 ne peut y entrer),
    mais recalculé depuis les sommes de voix/exprimés par département
    (`calculer_ecart_national_departement`), jamais depuis une moyenne des
    écarts de bureau. Retourne une table `code_departement` x `bloc` x
    `composite_2022` (mêmes noms de colonnes que le prédicteur bureau, sauf
    la clé d'unité).
    """
    panel_2022 = isoler_scrutins_2022(panel)
    ecart = calculer_ecart_national_departement(panel_2022, scrutins=SCRUTINS_PREDICTEUR_2022)
    legi_corrige = corriger_offre_legislatives(
        ecart,
        scrutin_a_corriger=SCRUTIN_LEGISLATIVES_2022,
        scrutin_reference=SCRUTIN_PRESIDENTIELLE,
        methode=methode_correction,
    )
    table = construire_table_composantes(ecart, legi_corrige, scrutins_bruts=[SCRUTIN_PRESIDENTIELLE])
    table = composite_pondere(table, poids=poids or POIDS_COMPOSITE_2022_PAR_DEFAUT, nom_colonne=COLONNE_COMPOSITE)
    return table.rename({"unite_id": "code_departement"})


def calculer_taux_abstention_departement(panel: pl.DataFrame, scrutin: str = SCRUTIN_PRESIDENTIELLE) -> pl.DataFrame:
    """Taux d'abstention 2022 à la maille département (garde anti-hasard, ADR 0002).

    Anti-fuite par construction : filtre sur un unique `scrutin` (2022 par
    défaut), structurellement incapable de lire une ligne 2024. Sommes
    d'abstentions/inscrits par département (dédupliquées par bureau d'abord,
    répétées sur chaque ligne de bloc) -- jamais une moyenne des taux de
    bureau.
    """
    df = panel.with_columns(pl.coalesce(["id_bv", "code_commune"]).alias("unite_id")).filter(
        pl.col("id_election") == scrutin
    )
    bureau = df.select("unite_id", "code_departement", "abstentions", "inscrits").unique()
    departement = bureau.group_by("code_departement").agg(
        pl.col("abstentions").sum().alias("abstentions_departement"),
        pl.col("inscrits").sum().alias("inscrits_departement"),
    )
    return departement.with_columns(
        pl.when(pl.col("inscrits_departement") > 0)
        .then(pl.col("abstentions_departement") / pl.col("inscrits_departement"))
        .otherwise(None)
        .alias("abstention_departement_2022")
    ).select("code_departement", "abstention_departement_2022")


def verdict_anti_hasard(rho_bureau: float, rho_departement: float) -> dict:
    """Lift bureau vs 2 nulls + verdict de la clause (ADR 0002).

    `rho_hasard` = 0 (espérance théorique de Spearman pour un classement
    indépendant -- contexte, jamais simulé par permutation : c'est un résultat
    de théorie, pas une mesure). `pass_global` : le bureau doit BATTRE (`>`,
    pas `>=`) le département -- clause plus stricte que le "au moins aussi
    bien" du gate ADR 0001 (composite vs mono), cf. formulation ADR 0002. Un
    rho non défini (NaN, échantillon trop petit ou colonne constante) ne bat
    jamais rien : verdict FAIL explicite, jamais une comparaison silencieuse.
    """
    comparable = rho_bureau == rho_bureau and rho_departement == rho_departement  # ni l'un ni l'autre n'est NaN
    return {
        "rho_bureau": rho_bureau,
        "rho_hasard": 0.0,
        "lift_vs_hasard": rho_bureau if rho_bureau == rho_bureau else float("nan"),
        "rho_departement": rho_departement,
        "lift_vs_departement": (rho_bureau - rho_departement) if comparable else float("nan"),
        "pass_global": bool(comparable and rho_bureau > rho_departement),
    }


def garde_anti_hasard_structure(
    resultats_backtest: dict,
    panel: pl.DataFrame,
    poids_composite_2022: dict[str, float] | None = None,
    methode_correction: str = "imputation",
    blocs: tuple[str, ...] = BLOCS_MAJEURS,
) -> pl.DataFrame:
    """Garde anti-hasard pour la métrique principale du backtest structure
    (ρ_ensemble du composite, blocs majeurs x cibles, ADR 0001/0002).

    `resultats_backtest` : sortie de `executer_backtests` (fournit `table`,
    déjà restreinte au périmètre joint-validé). Retourne `bloc` x `cible` x
    les colonnes de `verdict_anti_hasard`.
    """
    table = resultats_backtest["table"]
    predicteur_dept = construire_predicteur_departemental_2022(
        panel, poids=poids_composite_2022, methode_correction=methode_correction
    )

    lignes = []
    for bloc in blocs:
        predicteur_bloc = predicteur_dept.filter(pl.col("bloc") == bloc).select(
            "code_departement", pl.col(COLONNE_COMPOSITE).alias("composite_departement_2022")
        )
        sous_table = table.filter(pl.col("bloc") == bloc).join(predicteur_bloc, on="code_departement", how="left")
        for nom_cible, colonne_cible in CIBLES.items():
            rho_bureau = correlation_spearman(sous_table, COLONNE_COMPOSITE, colonne_cible)
            rho_departement = correlation_spearman(sous_table, "composite_departement_2022", colonne_cible)
            lignes.append({"bloc": bloc, "cible": nom_cible, **verdict_anti_hasard(rho_bureau, rho_departement)})
    return pl.DataFrame(lignes)


def garde_anti_hasard_participation(resultats_participation: dict, panel: pl.DataFrame) -> pl.DataFrame:
    """Garde anti-hasard pour la métrique principale du backtest participation
    (ρ abstention 2022 -> cible 2024, par cible, ADR 0002).

    `resultats_participation` : sortie de `executer_backtest_participation`.
    """
    table = resultats_participation["table"]
    departement = calculer_taux_abstention_departement(panel)
    avec_dept = table.join(departement, on="code_departement", how="left")

    lignes = [
        {
            "cible": nom_cible,
            **verdict_anti_hasard(
                correlation_spearman(avec_dept, COLONNE_ABSTENTION_PREDICTEUR, colonne_cible),
                correlation_spearman(avec_dept, "abstention_departement_2022", colonne_cible),
            ),
        }
        for nom_cible, colonne_cible in CIBLES_PARTICIPATION.items()
    ]
    return pl.DataFrame(lignes)


def verdict_carte_mobilisation(
    verdict_participation: pl.DataFrame,
    verdict_anti_hasard_structure: pl.DataFrame,
    verdict_anti_hasard_participation: pl.DataFrame,
) -> bool:
    """PASS uniquement si TOUTES les clauses de la carte mobilisation le sont
    (ADR 0002, point 5) : backtest participation (ρ ≥ 0,8 par cible) ET garde
    anti-hasard (structure + participation, bureau bat département). La
    clause tercile de l'ADR 0001 ne gouverne plus ce produit -- elle reste
    publiée (FAIL inclus) mais ne conditionne plus cette publication-ci.
    """
    return (
        verdict_global(verdict_participation)
        and verdict_global(verdict_anti_hasard_structure)
        and verdict_global(verdict_anti_hasard_participation)
    )


# --- Orchestration ------------------------------------------------------------


def executer_backtests(
    panel: pl.DataFrame,
    baseline: pl.DataFrame,
    poids_composite_2022: dict[str, float] | None = None,
    methode_correction: str = "imputation",
) -> dict:
    """Calcule les 3 backtests + le verdict du gate, sur le périmètre joint-validé.

    Retourne un dict : `table` (table de travail restreinte au périmètre),
    `resultats` (table longue predicteur x cible x scope x bloc x rho x n,
    tous les blocs), `verdict` (gate ADR 0001, blocs majeurs uniquement),
    `correlation_euro_pres` (float), `swing` et `regularite` (dict, bloc
    Extrême droite).
    """
    table_brute = construire_table_backtest(
        panel, baseline, poids_composite_2022=poids_composite_2022, methode_correction=methode_correction
    )
    table = table_brute.filter(pl.col("statut") == STATUT_JOINT_VALIDE)
    table = tercile_competitif(table)

    lignes = []
    for nom_predicteur, colonne_predicteur in PREDICTEURS.items():
        for nom_cible, colonne_cible in CIBLES.items():
            for nom_scope, sous_table in (
                ("ensemble", table),
                ("tercile", table.filter(pl.col("tercile_competitif"))),
            ):
                resultat = rho_par_bloc(sous_table, colonne_predicteur, colonne_cible).with_columns(
                    pl.lit(nom_predicteur).alias("predicteur"),
                    pl.lit(nom_cible).alias("cible"),
                    pl.lit(nom_scope).alias("scope"),
                )
                lignes.append(resultat)
    resultats = pl.concat(lignes).select("predicteur", "cible", "scope", "bloc", "rho", "n")

    return {
        "table": table,
        "resultats": resultats,
        "verdict": evaluer_gate(resultats),
        "correlation_euro_pres": correlation_euro_pres_rn(table),
        "swing": distribution_swing(table),
        "regularite": verifier_regularite_seuil(table),
    }


# --- Calibration des poids (issue #5 : promesse tenue par le backtest #6) ---


JEUX_DE_POIDS_CALIBRATION: dict[str, dict[str, float]] = {
    "mono (100% présidentielle)": {SCRUTIN_PRESIDENTIELLE: 1.0, SCRUTIN_LEGISLATIVES_2022_CORRIGE: 0.0},
    "50-50": {SCRUTIN_PRESIDENTIELLE: 0.5, SCRUTIN_LEGISLATIVES_2022_CORRIGE: 0.5},
    "défaut (60% présidentielle / 40% législatives)": POIDS_COMPOSITE_2022_PAR_DEFAUT,
}


def calibrer_poids(
    panel: pl.DataFrame,
    baseline: pl.DataFrame,
    jeux_de_poids: dict[str, dict[str, float]] | None = None,
    methode_correction: str = "imputation",
) -> pl.DataFrame:
    """Compare plusieurs jeux de poids du composite 2022, sur l'ensemble joint-validé.

    Pour chaque jeu de poids nommé (`jeux_de_poids`, défaut
    `JEUX_DE_POIDS_CALIBRATION` : mono / 50-50 / défaut -- la calibration
    promise par l'issue #5), reconstruit le prédicteur composite 2022 et
    mesure son Spearman aux 2 cibles 2024, pour les blocs majeurs. Triée par
    rho décroissant : la première ligne d'une (bloc, cible) donnée est le
    jeu de poids qui maximise la corrélation de rang.
    """
    jeux_de_poids = jeux_de_poids or JEUX_DE_POIDS_CALIBRATION
    lignes = []
    for nom, poids in jeux_de_poids.items():
        table_brute = construire_table_backtest(
            panel, baseline, poids_composite_2022=poids, methode_correction=methode_correction
        )
        table = table_brute.filter(pl.col("statut") == STATUT_JOINT_VALIDE)
        for nom_cible, colonne_cible in CIBLES.items():
            for bloc in BLOCS_MAJEURS:
                rho = correlation_spearman(table.filter(pl.col("bloc") == bloc), COLONNE_COMPOSITE, colonne_cible)
                lignes.append({"jeu_de_poids": nom, "cible": nom_cible, "bloc": bloc, "rho": rho})
    return pl.DataFrame(lignes).sort("rho", descending=True)


# --- Rapport ------------------------------------------------------------------


def _formater_poids(poids: dict[str, float]) -> str:
    return " / ".join(f"{valeur:.0%} {scrutin}" for scrutin, valeur in poids.items())


def _ligne_resultats(ligne: dict) -> str:
    rho = ligne["rho"]
    rho_txt = f"{rho:.3f}" if rho == rho else "n/d"  # NaN != NaN
    return f"| {ligne['predicteur']} | {ligne['cible']} | {ligne['scope']} | {ligne['bloc']} | {rho_txt} | {ligne['n']} |"


def _ligne_verdict(ligne: dict) -> str:
    def _b(v: bool) -> str:
        return "PASS" if v else "FAIL"

    return (
        f"| {ligne['bloc']} | {ligne['cible']} "
        f"| {ligne['rho_ensemble_composite']:.3f} ≥ {ligne['seuil_ensemble']:.1f} ({_b(ligne['pass_ensemble'])}) "
        f"| {ligne['rho_tercile_composite']:.3f} ≥ {ligne['seuil_tercile']:.1f} ({_b(ligne['pass_tercile'])}) "
        f"| composite {ligne['rho_ensemble_composite']:.3f} vs mono {ligne['rho_ensemble_mono']:.3f} "
        f"({_b(ligne['pass_composite_vs_mono'])}) | **{_b(ligne['pass_global'])}** |"
    )


def _ligne_calibration(ligne: dict) -> str:
    rho = ligne["rho"]
    rho_txt = f"{rho:.3f}" if rho == rho else "n/d"
    return f"| {ligne['jeu_de_poids']} | {ligne['cible']} | {ligne['bloc']} | {rho_txt} |"


def _fmt_rho(x: float) -> str:
    return f"{x:.3f}" if x == x else "n/d"  # NaN != NaN


def _ligne_resultats_participation(ligne: dict) -> str:
    verdict_txt = "PASS" if ligne["pass_global"] else "FAIL"
    return f"| {ligne['cible']} | {_fmt_rho(ligne['rho'])} ≥ {ligne['seuil']:.1f} ({verdict_txt}) | {ligne['n']} |"


def _ligne_anti_hasard(prefixe: str, ligne: dict) -> str:
    verdict_txt = "PASS" if ligne["pass_global"] else "FAIL"
    return (
        f"| {prefixe} | {_fmt_rho(ligne['rho_bureau'])} "
        f"| {ligne['rho_hasard']:.1f} (lift {_fmt_rho(ligne['lift_vs_hasard'])}) "
        f"| {_fmt_rho(ligne['rho_departement'])} (lift {_fmt_rho(ligne['lift_vs_departement'])}) "
        f"| **{verdict_txt}** |"
    )


def _ligne_anti_hasard_structure(ligne: dict) -> str:
    return _ligne_anti_hasard(f"{ligne['bloc']} | {ligne['cible']}", ligne)


def _ligne_anti_hasard_participation(ligne: dict) -> str:
    return _ligne_anti_hasard(ligne["cible"], ligne)


def generer_rapport_backtest(
    resultats_backtest: dict,
    calibration: pl.DataFrame,
    poids_composite_2022: dict[str, float],
    methode_correction: str,
    n_total: int,
    n_perimetre: int,
    resultats_participation: dict,
    anti_hasard_structure: pl.DataFrame,
    anti_hasard_participation: pl.DataFrame,
) -> str:
    """Construit le texte de `backtest-2022-2024.md` (issue #6, enrichi ADR 0002/issue #24).

    `resultats_participation` : sortie de `executer_backtest_participation`.
    `anti_hasard_structure` / `anti_hasard_participation` : sorties de
    `garde_anti_hasard_structure` / `garde_anti_hasard_participation`. Les
    sections existantes (issue #6) ne sont pas réécrites -- seules des
    sections nouvelles s'ajoutent à la suite (ADR 0002, point 5 : le rapport
    s'enrichit sans réécrire l'existant, l'échec du tercile reste publié tel quel).
    """
    resultats = resultats_backtest["resultats"]
    verdict = resultats_backtest["verdict"]
    correlation_euro_pres = resultats_backtest["correlation_euro_pres"]
    swing = resultats_backtest["swing"]
    regularite = resultats_backtest["regularite"]

    part_perimetre = n_perimetre / n_total if n_total else 0.0

    lignes_resultats = "\n".join(
        _ligne_resultats(ligne) for ligne in resultats.sort(["cible", "predicteur", "scope", "bloc"]).iter_rows(named=True)
    )
    lignes_verdict = "\n".join(_ligne_verdict(ligne) for ligne in verdict.sort(["bloc", "cible"]).iter_rows(named=True))
    lignes_calibration = "\n".join(
        _ligne_calibration(ligne) for ligne in calibration.sort(["cible", "bloc", "rho"], descending=[False, False, True]).iter_rows(named=True)
    )

    pass_global = verdict_global(verdict)
    verdict_txt = (
        "**PASS** — le composite passe les 3 clauses du gate pour les 2 blocs majeurs et les 2 cibles."
        if pass_global
        else (
            "**FAIL** — au moins une clause du gate échoue (détail dans le tableau ci-dessus). "
            "Un backtest qui ne peut pas échouer ne valide rien : ceci bloque la publication de la "
            "**carte structurelle** (ADR 0001), pas ce commit ni ce merge. Décision de révision "
            "d'architecture à l'humain — recommandation : ouvrir une issue de révision d'architecture "
            "avant toute publication."
        )
    )

    recommandation_euro = (
        "≥ 0,5 : pas de rétrogradation recommandée du poids des européennes dans le composite #5."
        if correlation_euro_pres == correlation_euro_pres and correlation_euro_pres >= 0.5
        else (
            "< 0,5 : recommandation — rétrograder le poids des européennes 2024 dans le composite #5 "
            "(HANDOFF.md étape 2). Recommandation écrite ici, aucun changement automatique des poids."
        )
    )

    meilleur_par_cible = (
        calibration.sort("rho", descending=True).group_by("cible", maintain_order=True).first()
    )
    lignes_meilleur = "\n".join(
        f"- **{ligne['cible']}** : « {ligne['jeu_de_poids']} » (ρ = {ligne['rho']:.3f}, bloc {ligne['bloc']})"
        for ligne in meilleur_par_cible.iter_rows(named=True)
    )

    # --- ADR 0002 / issue #24 : sections ajoutées, aucune des lignes ci-dessus
    # n'est modifiée (rapport enrichi, jamais réécrit).
    resultats_part = resultats_participation["resultats"]
    lignes_participation = "\n".join(
        _ligne_resultats_participation(ligne) for ligne in resultats_part.sort("cible").iter_rows(named=True)
    )
    lignes_anti_hasard_structure = "\n".join(
        _ligne_anti_hasard_structure(ligne)
        for ligne in anti_hasard_structure.sort(["bloc", "cible"]).iter_rows(named=True)
    )
    lignes_anti_hasard_participation = "\n".join(
        _ligne_anti_hasard_participation(ligne) for ligne in anti_hasard_participation.sort("cible").iter_rows(named=True)
    )

    pass_participation = verdict_global(resultats_part)
    verdict_participation_txt = (
        "**PASS** — ρ ≥ 0,8 atteint sur chaque cible (ADR 0002)."
        if pass_participation
        else (
            "**FAIL** — au moins une cible est sous le seuil ρ ≥ 0,8 (ADR 0002), détail dans le tableau "
            "ci-dessus. Clause pré-enregistrée, jamais réinterprétée ici."
        )
    )

    pass_anti_hasard = verdict_global(anti_hasard_structure) and verdict_global(anti_hasard_participation)
    verdict_anti_hasard_txt = (
        "**PASS** — la granularité bureau bat la granularité département sur toutes les métriques "
        "principales publiées ci-dessus (structure et participation)."
        if pass_anti_hasard
        else (
            "**FAIL** — au moins une métrique principale ne bat pas son prédicteur département "
            "(détail dans les tableaux ci-dessus)."
        )
    )

    pass_carte = verdict_carte_mobilisation(resultats_part, anti_hasard_structure, anti_hasard_participation)
    verdict_carte_mobilisation_txt = (
        "**PASS** — les clauses pré-enregistrées de l'ADR 0002 (backtest participation + garde "
        "anti-hasard) sont toutes au vert : publication de la carte mobilisation autorisée."
        if pass_carte
        else (
            "**FAIL** — au moins une clause pré-enregistrée de l'ADR 0002 échoue (détail dans les "
            "sections 4 et 5 ci-dessus) : pas de publication de la carte mobilisation. Décision de "
            "révision d'architecture à l'humain (nouvelle issue de révision, ADR 0002) — les seuils "
            "ne bougent pas."
        )
    )

    rho_inter_cibles = resultats_participation["rho_inter_cibles"]
    n_inter_cibles = resultats_participation["n_inter_cibles"]

    sections_existantes = f"""# Backtest 2022→2024 et verdict du gate (ADR 0001)

Validation auto-produite (HANDOFF.md étape 2, CONTEXT.md « Backtest ») : personne
n'a jamais publié de projection à la maille bureau de vote en France, donc aucune
validation externe n'existe. Ce document sera **publié avec les cartes**.

## Note d'étanchéité (règle anti-fuite)

Le backtest simule quelqu'un en 2022 qui prédit 2024. Le prédicteur "2022"
(`projections.backtest.construire_predicteur_2022`) n'incorpore **aucune**
donnée 2024 : `isoler_scrutins_2022` filtre le panel aux seuls `id_election`
2022 (présidentielle T1, législatives T1) avant tout calcul — garde-fou
physique, pas seulement documentaire. La baseline mono-scrutin 2022 est
l'écart relatif au national de la présidentielle 2022 T1 seule ; la baseline
composite 2022 combine présidentielle 2022 + législatives 2022 (offre
corrigée en imputant depuis la **présidentielle 2022**, jamais depuis les
européennes 2024 — contrairement à la correction d'offre des législatives
**2024** faite dans la baseline #5). Les cibles (structure 2024 observée :
européennes puis législatives 2024 corrigées de l'offre) sont lues telles
quelles dans `baseline_unite_bloc.parquet` : côté cible, c'est de la donnée
observée, pas de fuite.

## Périmètre

**{n_perimetre} lignes unité×bloc** (statut `joint_valide`, maille bureau)
sur {n_total} lignes jointes prédicteur×cible au total, soit **{part_perimetre:.1%}**
du périmètre. Les unités en repli (maille commune, cf. `projections.churn`)
sont exclues : elles agrègent plusieurs bureaux physiques, une granularité
différente qui fausserait une validation de rang à la maille bureau.
Correction de l'offre des législatives : méthode `{methode_correction}`.
Poids du composite 2022 utilisés pour le backtest principal : {_formater_poids(poids_composite_2022)}.

## Tercile compétitif — définition

Pour chaque bloc, le tiers central du classement de `composite_2022` (percentile
de rang dans [1/3, 2/3], calculé par bloc) — ni bastion, ni désert : l'endroit où
la carte prétend servir (persuasion, cf. CONTEXT.md « Rapport de force »).

## 1. Corrélation de rang 2022→2024

Spearman (Polars pur : rang moyen ex-aequo + corrélation de Pearson sur les rangs),
par bloc, prédicteur (mono = présidentielle 2022 seule, composite = présidentielle +
législatives 2022), cible (européennes 2024, législatives 2024 corrigées) et
périmètre (ensemble des unités joint-validées, tercile compétitif).

| Prédicteur | Cible | Périmètre | Bloc | ρ | n |
| --- | --- | --- | --- | --- | --- |
{lignes_resultats}

### Verdict du gate (ADR 0001, blocs majeurs)

| Bloc | Cible | ρ ensemble (seuil 0,7) | ρ tercile (seuil 0,5) | Composite vs mono | Verdict |
| --- | --- | --- | --- | --- | --- |
{lignes_verdict}

{verdict_txt}

## 2. Corrélation géographique RN européennes ↔ présidentielle

**ρ = {correlation_euro_pres:.3f}** (Spearman, écart relatif Extrême droite,
2024_euro_t1 vs 2022_pres_t1, unités joint-validées) — l'équivalent du 0,89
CEVIPOF mesuré pour la gauche, absent de la littérature avant ce calcul.
Identique par construction à la ligne (mono, euro, ensemble, Extrême droite)
du tableau ci-dessus. Règle décisionnelle (HANDOFF.md étape 2) : {recommandation_euro}

## 3. Distribution du swing Extrême droite par unité (2022_pres_t1 → 2024)

`derive` = moyenne(écart européennes 2024, écart législatives 2024 corrigées) −
écart présidentielle 2022 (`projections.baseline.calculer_derive`), bloc Extrême
droite, unités joint-validées. n = {swing.get("n", 0)}.

| min | p5 | p25 | médiane | p75 | p95 | max | moyenne | asymétrie (skew) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {swing.get("min", float("nan")):.2f} | {swing.get("p5", float("nan")):.2f} | {swing.get("p25", float("nan")):.2f} | {swing.get("median", float("nan")):.2f} | {swing.get("p75", float("nan")):.2f} | {swing.get("p95", float("nan")):.2f} | {swing.get("max", float("nan")):.2f} | {swing.get("mean", float("nan")):.2f} | {swing.get("skew", float("nan")):.2f} |

### Condition de régularité

Seuil de décision pris comme la **médiane** de `derive` (choix défendable et
documenté, cf. docstring de `verifier_regularite_seuil`) : {regularite.get("seuil", float("nan")):.2f}.
Densité de la classe contenant le seuil : {regularite.get("densite_classe_seuil", "n/d")}
(densité moyenne des 2 classes voisines, sur {regularite.get("n_bins", "n/d")} classes au total :
{regularite.get("densite_voisine_moyenne", float("nan")):.1f}, ratio
{regularite.get("ratio", float("nan")):.2f}). {"**Discontinuité détectée**" if regularite.get("anomalie") else "Pas de discontinuité anormale détectée"}
autour du seuil, par rapport à ses classes immédiatement voisines (seuil d'alerte : ratio > 1,5).

## Calibration des poids du composite 2022 (promesse de l'issue #5)

Comparaison de {calibration.get_column("jeu_de_poids").n_unique()} jeux de poids
(mono / 50-50 / défaut) sur les blocs majeurs, ensemble des unités joint-validées :

| Jeu de poids | Cible | Bloc | ρ |
| --- | --- | --- | --- |
{lignes_calibration}

Meilleur jeu de poids par cible (maximise Spearman) :
{lignes_meilleur}

Recommandation écrite ici uniquement — `POIDS_COMPOSITE_2022_PAR_DEFAUT` et
`projections.baseline.POIDS_PAR_DEFAUT` restent des points de départ documentés,
pas des constantes changées automatiquement par ce backtest.
"""

    sections_ajoutees = f"""
## 4. Backtest participation (ADR 0002)

Corrélation de rang (Spearman) du taux d'abstention par bureau, présidentielle
2022 T1 → cible 2024, sur l'ensemble des bureaux joints (statut `joint_valide`,
maille bureau) — proxy de H2 (persistance de la géographie de l'abstention
d'une présidentielle à l'autre, cf. ADR 0002 et CONTEXT.md « Réserve
d'abstention »). Prédicteur (`abstention_2022_pres_t1`) structurellement
aveugle à 2024 : un seul scrutin 2022 côté prédicteur.

| Cible | ρ (seuil 0,8) | n |
| --- | --- | --- |
{lignes_participation}

Accords inter-cibles publiés en contexte (même transparence que les plafonds
du tercile, section 1 ci-dessus) : les 2 cibles 2024 (abstention européennes,
abstention législatives) s'accordent entre elles à **ρ = {rho_inter_cibles:.3f}**
(n = {n_inter_cibles}).

{verdict_participation_txt}

## 5. Garde anti-hasard (ADR 0002)

Pour la métrique principale de chaque backtest publié ci-dessus (ρ ensemble du
composite, blocs majeurs, pour la structure ; ρ par cible, pour la
participation), lift contre 2 nulls : le **hasard** (ρ = 0, espérance
théorique d'un classement indépendant — contexte, pas simulé) et le
**prédicteur à maille département** (chaque bureau prédit par la valeur
agrégée de son département, recalculée par sommes de voix/exprimés ou
d'abstentions/inscrits — jamais une moyenne des écarts ou des taux de bureau).
Clause : la granularité bureau doit **battre** (>, pas ≥) la granularité
département, sinon pas de publication à cette maille.

### Structure (composite, blocs majeurs)

| Bloc | Cible | ρ bureau | ρ hasard (lift) | ρ département (lift) | Verdict |
| --- | --- | --- | --- | --- | --- |
{lignes_anti_hasard_structure}

### Participation (abstention 2022)

| Cible | ρ bureau | ρ hasard (lift) | ρ département (lift) | Verdict |
| --- | --- | --- | --- | --- |
{lignes_anti_hasard_participation}

{verdict_anti_hasard_txt}

## Verdict global — publication de la carte mobilisation (ADR 0002)

{verdict_carte_mobilisation_txt}

La clause tercile de l'ADR 0001 (section 1 ci-dessus) reste publiée telle
quelle — son échec ne conditionne plus cette publication : elle gouvernait le
rapport de force / persuasion, un produit déclassé au profit de la réserve de
voix par bloc (ADR 0002, point 5). Les seuils de l'ADR 0001 comme ceux de
l'ADR 0002 ne bougent pas après avoir vu les résultats.
"""

    return sections_existantes + sections_ajoutees


# --- Entrée console -----------------------------------------------------------


def main() -> None:
    """Point d'entrée `uv run backtest`."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, default=INTERIM_DIR / "panel_avec_statut.parquet")
    parser.add_argument("--baseline", type=Path, default=INTERIM_DIR / "baseline_unite_bloc.parquet")
    parser.add_argument("--out", type=Path, default=Path("backtest-2022-2024.md"))
    parser.add_argument(
        "--poids-presidentielle-2022", type=float, default=POIDS_COMPOSITE_2022_PAR_DEFAUT[SCRUTIN_PRESIDENTIELLE]
    )
    parser.add_argument(
        "--poids-legislatives-2022",
        type=float,
        default=POIDS_COMPOSITE_2022_PAR_DEFAUT[SCRUTIN_LEGISLATIVES_2022_CORRIGE],
    )
    parser.add_argument("--methode-correction", choices=("imputation", "exclusion"), default="imputation")
    args = parser.parse_args()

    poids = {
        SCRUTIN_PRESIDENTIELLE: args.poids_presidentielle_2022,
        SCRUTIN_LEGISLATIVES_2022_CORRIGE: args.poids_legislatives_2022,
    }

    panel = pl.read_parquet(args.panel)
    baseline = pl.read_parquet(args.baseline)

    resultats_backtest = executer_backtests(panel, baseline, poids_composite_2022=poids, methode_correction=args.methode_correction)
    calibration = calibrer_poids(panel, baseline, methode_correction=args.methode_correction)

    resultats_participation = executer_backtest_participation(panel, baseline)
    anti_hasard_structure = garde_anti_hasard_structure(
        resultats_backtest, panel, poids_composite_2022=poids, methode_correction=args.methode_correction
    )
    anti_hasard_participation = garde_anti_hasard_participation(resultats_participation, panel)

    table_brute = construire_table_backtest(
        panel, baseline, poids_composite_2022=poids, methode_correction=args.methode_correction
    )
    rapport = generer_rapport_backtest(
        resultats_backtest,
        calibration,
        poids_composite_2022=poids,
        methode_correction=args.methode_correction,
        n_total=table_brute.height,
        n_perimetre=resultats_backtest["table"].height,
        resultats_participation=resultats_participation,
        anti_hasard_structure=anti_hasard_structure,
        anti_hasard_participation=anti_hasard_participation,
    )

    args.out.write_text(rapport, encoding="utf-8")
    print(f"rapport écrit : {args.out}")
    print(f"gate ADR 0001 PASS: {verdict_global(resultats_backtest['verdict'])}")
    print(
        "carte mobilisation PASS (ADR 0002): "
        f"{verdict_carte_mobilisation(resultats_participation['resultats'], anti_hasard_structure, anti_hasard_participation)}"
    )


if __name__ == "__main__":
    main()

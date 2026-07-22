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
    """Condition de régularité : pas de masse anormale concentrée au seuil de décision.

    Seuil pris comme la MÉDIANE de `colonne` -- choix défendable et
    documenté (cf. docstring du module) : le point qui sépare, dans le
    classement produit, les unités où le bloc progresse de celles où il
    recule. Découpe `colonne` en `n_bins` classes de largeur égale entre son
    min et son max, compare la densité de la classe contenant le seuil à la
    densité moyenne des classes -- `anomalie` si le ratio dépasse
    `seuil_alerte` (1,5x la densité moyenne par défaut).
    """
    serie = table.filter(pl.col("bloc") == bloc).get_column(colonne).drop_nulls()
    if serie.len() < 2:
        return {"n": serie.len(), "anomalie": False}
    seuil = serie.median()
    minimum, maximum = serie.min(), serie.max()
    largeur = (maximum - minimum) / n_bins
    if largeur == 0:
        return {"n": serie.len(), "seuil": seuil, "anomalie": False}

    classes = ((serie - minimum) / largeur).floor().clip(0, n_bins - 1)
    comptes = pl.DataFrame({"classe": classes}).group_by("classe").agg(pl.len().alias("n")).sort("classe")
    densite_moyenne = comptes.get_column("n").mean()

    indice_seuil = min(max(int((seuil - minimum) / largeur), 0), n_bins - 1)
    ligne_seuil = comptes.filter(pl.col("classe") == indice_seuil).get_column("n")
    densite_seuil = ligne_seuil[0] if ligne_seuil.len() else 0

    ratio = densite_seuil / densite_moyenne if densite_moyenne else float("nan")
    return {
        "n": serie.len(),
        "seuil": seuil,
        "n_bins": n_bins,
        "densite_classe_seuil": densite_seuil,
        "densite_moyenne_classe": densite_moyenne,
        "ratio": ratio,
        "anomalie": bool(densite_moyenne) and ratio > seuil_alerte,
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
    """PASS uniquement si toutes les lignes (bloc x cible) du gate sont PASS."""
    return bool(verdict.height) and bool(verdict.get_column("pass_global").all())


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


def generer_rapport_backtest(
    resultats_backtest: dict,
    calibration: pl.DataFrame,
    poids_composite_2022: dict[str, float],
    methode_correction: str,
    n_total: int,
    n_perimetre: int,
) -> str:
    """Construit le texte de `backtest-2022-2024.md` (issue #6)."""
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

    return f"""# Backtest 2022→2024 et verdict du gate (ADR 0001)

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
Poids du composite 2022 utilisés pour le backtest principal : {poids_composite_2022}.

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
(densité moyenne sur {regularite.get("n_bins", "n/d")} classes :
{regularite.get("densite_moyenne_classe", float("nan")):.1f}, ratio
{regularite.get("ratio", float("nan")):.2f}). {"**Anomalie détectée**" if regularite.get("anomalie") else "Pas de masse anormale détectée"}
autour du seuil (seuil d'alerte : ratio > 1,5).

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
    )

    args.out.write_text(rapport, encoding="utf-8")
    print(f"rapport écrit : {args.out}")
    print(f"gate PASS: {verdict_global(resultats_backtest['verdict'])}")


if __name__ == "__main__":
    main()

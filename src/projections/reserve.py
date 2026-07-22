"""Estimateur v1 de la réserve de voix par bureau × bloc (issue #25, ADR 0002 point 1,
CONTEXT.md « Réserve d'abstention »).

## Formule (glossaire, gravée avant tout calcul)

    réserve(unité, bloc) = inscrits × abstention au scrutin de même enjeu
                            (présidentielle 2022 T1, cible 2027) × part estimée du bloc

`unité` = bureau (`id_bv`) si la commune est stable (statut `joint_valide`,
`projections.churn`), commune (`code_commune`) sinon -- jamais déguisé : le
statut de réconciliation du panel est propagé jusqu'à la sortie (colonnes
`statut`/`maille`, réutilisées telles quelles depuis `baseline_unite_bloc.parquet`,
issue #5). Intermittents (votants présidentielle absents des scrutins
intermédiaires) exclus par construction : `abstention` et `inscrits` ne
proviennent que du scrutin de référence (présidentielle 2022 T1), jamais d'un
scrutin intermédiaire -- aucun garde-fou anti-fuite séparé n'est nécessaire, il
n'y a qu'un seul scrutin côté volume (même remarque que le backtest
participation, `projections.backtest`).

## Part estimée du bloc (H1) -- décision d'implémentation documentée

CONTEXT.md énonce H1 : « répartition politique des abstentionnistes ≈ celle
des **votants du bureau** ». Deux lectures étaient possibles pour « part
estimée du bloc » : (a) la part réelle du bloc parmi les exprimés du bureau au
scrutin de référence (`part_proportionnelle_aux_votants`, littéralement « celle
des votants du bureau »), ou (b) l'écart composite de la baseline (#5)
reconverti en part. (b) a été écartée : `composite` est un écart en points
relatif à 3 national différents (présidentielle 2022, européennes 2024,
législatives 2024 corrigées) -- le reconvertir en part exigerait une ancre
nationale inventée, absente du glossaire. **Décision retenue : (a)**, qui
correspond aussi mot pour mot à la variante « proportionnelle aux votants »
citée par l'issue #25 comme opérationnalisation de H1 -- `baseline_unite_bloc.parquet`
reste utilisée « telle quelle », mais uniquement comme source des colonnes de
contexte (`code_departement`/`statut`/`maille`), au même titre que
`projections.backtest.construire_table_participation`. La variante « uniforme
entre blocs » (`part_uniforme_entre_blocs`) est l'AUTRE opérationnalisation
citée par l'issue, utilisée pour la sensibilité H1 ci-dessous -- jamais pour le
calcul par défaut.

## Non backtestable (ADR 0002 point 3)

La couche estimation n'a pas de vérité terrain : validée par définition ex
ante (ci-dessus), analyse de sensibilité (`sensibilite_h1`, variantes H1) et
appel public à contradiction -- jamais par un gate PASS/FAIL comme les
backtests structure/participation (`projections.backtest`, issue #24). Le
« lift bureau vs département » demandé par l'issue #25 porte sur la SEULE
composante backtestable de la formule (l'abstention 2022→2024, déjà validée
par #24) : `lift_reserve_bureau_vs_departement` réutilise telle quelle
`garde_anti_hasard_participation`, jamais un nouveau calcul de lift sur la part
(non backtestable par construction).

## Publication : héritée du verdict carte mobilisation (ADR 0002 point 5)

Le backtest participation est sorti **rouge** (ρ euro = 0,769 < 0,8, voir
`backtest-2022-2024.md` §4) : la révision d'architecture (#28) est ouverte et
tranche. `generer_rapport_complet` calcule et affiche ce verdict sans jamais le
recalculer différemment -- si FAIL, le rapport marque explicitement la réserve
comme préparatoire, non publiable en carte tant que #28 n'a pas tranché
(les chiffres restent publiés, jamais cachés : même philosophie que le gate
ADR 0001/0002 dans `projections.backtest`).
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path

import polars as pl

from projections.backtest import (
    correlation_spearman,
    distribution_swing,
    executer_backtest_participation,
    executer_backtests,
    garde_anti_hasard_participation,
    garde_anti_hasard_structure,
    calculer_taux_abstention,
    verdict_carte_mobilisation,
)
from projections.baseline import SCRUTIN_PRESIDENTIELLE, calculer_ecart_national

INTERIM_DIR = Path("data/interim")

# Scrutin de référence ("même enjeu", CONTEXT.md « Réserve d'abstention ») :
# présidentielle 2022 T1 pour la cible 2027 -- présidentielle elle aussi.
SCRUTIN_REFERENCE = SCRUTIN_PRESIDENTIELLE

BLOCS: tuple[str, ...] = ("Gauche", "Centre", "Droite", "Extrême droite", "Divers")


# --- Part estimée du bloc (H1, 2 opérationnalisations documentées) ------------


def part_proportionnelle_aux_votants(panel: pl.DataFrame, scrutin: str = SCRUTIN_REFERENCE) -> pl.DataFrame:
    """H1 par défaut (CONTEXT.md, littéralement « celle des votants du bureau ») :
    part réelle du bloc parmi les exprimés de l'unité, au scrutin de référence.

    Réutilise `calculer_ecart_national` (`projections.baseline`) tel quel : sa
    colonne intermédiaire `pct_unite` (voix du bloc / exprimés de l'unité, déjà
    calculée pour la baseline #5) est exactement cette part -- aucun nouveau
    calcul de part/exprimés n'est réintroduit ici.
    """
    ecart = calculer_ecart_national(panel, scrutins=[scrutin])
    return ecart.select("unite_id", "bloc", pl.col("pct_unite").alias("part_estimee_bloc"))


def part_uniforme_entre_blocs(panel: pl.DataFrame, scrutin: str = SCRUTIN_REFERENCE) -> pl.DataFrame:
    """Variante de sensibilité H1 : abstentionnistes répartis également entre les
    blocs PRÉSENTS dans l'unité au scrutin de référence (1/n, jamais 1/5 fixe --
    un bloc structurellement absent de l'offre, ex. Divers à la présidentielle,
    cf. `projections.baseline`, ne doit pas diluer artificiellement les autres).
    """
    presents = (
        panel.filter(pl.col("id_election") == scrutin)
        .with_columns(pl.coalesce(["id_bv", "code_commune"]).alias("unite_id"))
        .select("unite_id", "bloc")
        .unique()
    )
    n_blocs = presents.group_by("unite_id").agg(pl.col("bloc").n_unique().alias("_n_blocs"))
    return (
        presents.join(n_blocs, on="unite_id")
        .with_columns((1.0 / pl.col("_n_blocs")).alias("part_estimee_bloc"))
        .select("unite_id", "bloc", "part_estimee_bloc")
    )


METHODES_PART_H1: dict[str, Callable[..., pl.DataFrame]] = {
    "proportionnelle_aux_votants": part_proportionnelle_aux_votants,
    "uniforme_entre_blocs": part_uniforme_entre_blocs,
}
METHODE_PART_DEFAUT = "proportionnelle_aux_votants"


# --- Table réserve --------------------------------------------------------------


def construire_table_reserve(
    panel: pl.DataFrame,
    baseline: pl.DataFrame,
    methode_part: str = METHODE_PART_DEFAUT,
    scrutin_reference: str = SCRUTIN_REFERENCE,
) -> pl.DataFrame:
    """Table réserve unité × bloc (formule v1, cf. docstring du module).

    `panel` : panel avec statut (`projections.churn.construire_panel_avec_statut`).
    `baseline` : sortie de `projections.baseline.construire_baseline` (issue #5)
    -- fournit `code_departement`/`statut`/`maille` par unité, réutilisés tels
    quels (même convention que `projections.backtest.construire_table_participation`),
    jamais recalculés ici. `inscrits`/`abstentions` proviennent de
    `projections.backtest.calculer_taux_abstention` restreint au SEUL scrutin de
    référence -- dédupliqués par unité avant tout produit (répétés sur chaque
    ligne de bloc dans le panel long, CLAUDE.md « Never average percentages »).
    Aucune ligne sans statut explicite : lève une erreur plutôt que de publier
    une réserve à l'état de réconciliation silencieusement absent.
    """
    if methode_part not in METHODES_PART_H1:
        raise ValueError(f"méthode de part inconnue : {methode_part!r} (attendu un de {sorted(METHODES_PART_H1)})")

    abstention = calculer_taux_abstention(panel, scrutins=(scrutin_reference,)).select(
        "unite_id", "inscrits", "abstentions", "taux_abstention"
    )
    part = METHODES_PART_H1[methode_part](panel, scrutin=scrutin_reference)
    contexte = baseline.select("unite_id", "code_departement", "statut", "maille").unique(
        subset="unite_id", keep="first"
    )

    table = (
        part.join(abstention, on="unite_id", how="inner")
        .join(contexte, on="unite_id", how="inner")
        .with_columns((pl.col("inscrits") * pl.col("taux_abstention") * pl.col("part_estimee_bloc")).alias("reserve"))
        .sort(["unite_id", "bloc"])
    )

    manquants = table.filter(pl.col("statut").is_null())
    if manquants.height:
        raise ValueError(
            "statut de réconciliation manquant pour au moins une unité -- "
            "aucun état silencieux autorisé (CONTEXT.md « Panel »)"
        )

    return table.select(
        "unite_id",
        "bloc",
        "code_departement",
        "statut",
        "maille",
        "inscrits",
        "abstentions",
        "taux_abstention",
        "part_estimee_bloc",
        "reserve",
    )


# --- Sensibilité H1 (ADR 0002 point 3 : validation par sensibilité, pas backtest)


def sensibilite_h1(
    panel: pl.DataFrame,
    baseline: pl.DataFrame,
    methode_reference: str = METHODE_PART_DEFAUT,
    n_top: int = 20,
) -> pl.DataFrame:
    """Sensibilité de la réserve aux variantes de H1 : pour chaque bloc, compare
    le classement des gisements entre `methode_reference` (défaut du produit) et
    chacune des autres variantes de `METHODES_PART_H1`.

    Deux mesures, par bloc x variante : le Spearman des VALEURS de réserve
    entre les 2 méthodes (`rho` proche de 1 = classement quasi inchangé, la
    réserve est robuste à H1) et le recouvrement des top `n_top` gisements
    (part commune aux 2 ensembles, 0 = aucun gisement en commun, 1 = classement
    identique). Triée bloc puis variante (déterminisme).
    """
    table_reference = construire_table_reserve(panel, baseline, methode_part=methode_reference)
    lignes = []
    for nom_variante in sorted(m for m in METHODES_PART_H1 if m != methode_reference):
        table_variante = construire_table_reserve(panel, baseline, methode_part=nom_variante)
        jointe = table_reference.select("unite_id", "bloc", pl.col("reserve").alias("reserve_reference")).join(
            table_variante.select("unite_id", "bloc", pl.col("reserve").alias("reserve_variante")),
            on=["unite_id", "bloc"],
            how="inner",
        )
        for bloc in sorted(jointe.get_column("bloc").unique().to_list()):
            sous_jointe = jointe.filter(pl.col("bloc") == bloc)
            rho = correlation_spearman(sous_jointe, "reserve_reference", "reserve_variante")

            top_reference = set(
                table_reference.filter(pl.col("bloc") == bloc)
                .sort(["reserve", "unite_id"], descending=[True, False])
                .head(n_top)
                .get_column("unite_id")
                .to_list()
            )
            top_variante = set(
                table_variante.filter(pl.col("bloc") == bloc)
                .sort(["reserve", "unite_id"], descending=[True, False])
                .head(n_top)
                .get_column("unite_id")
                .to_list()
            )
            recouvrement = len(top_reference & top_variante) / n_top if n_top else float("nan")
            lignes.append(
                {
                    "bloc": bloc,
                    "methode_reference": methode_reference,
                    "methode_variante": nom_variante,
                    "rho": rho,
                    "recouvrement_top_n": recouvrement,
                    "n_top": n_top,
                }
            )
    return pl.DataFrame(lignes).sort(["bloc", "methode_variante"])


# --- Top gisements et agrégation département -----------------------------------


def top_gisements_bureau(table_reserve: pl.DataFrame, n: int = 20) -> pl.DataFrame:
    """Top `n` gisements (réserve décroissante) par bloc, à la maille de `table_reserve`.

    Tri déterministe : réserve décroissante, `unite_id` croissant en secondaire
    (ex-aequo). Les lignes à réserve nulle (statut `irresoluble`, jamais un
    zéro fabriqué -- `projections.churn`) sont exclues, pas classées à zéro.
    """
    return (
        table_reserve.filter(pl.col("reserve").is_not_null())
        .sort(["bloc", "reserve", "unite_id"], descending=[False, True, False])
        .group_by("bloc", maintain_order=True)
        .head(n)
    )


def agreger_reserve_par_departement(table_reserve: pl.DataFrame) -> pl.DataFrame:
    """Réserve agrégée par département × bloc -- SOMME des réserves d'unité,
    jamais une moyenne (CLAUDE.md « Never average percentages » : la réserve
    est un compte de voix, s'agrège comme tel). Triée bloc puis réserve
    décroissante, département croissant en secondaire (déterminisme).
    """
    return (
        table_reserve.filter(pl.col("reserve").is_not_null())
        .group_by(["code_departement", "bloc"])
        .agg(pl.col("reserve").sum())
        .sort(["bloc", "reserve", "code_departement"], descending=[False, True, False])
    )


def top_gisements_departement(table_reserve: pl.DataFrame, n: int = 20) -> pl.DataFrame:
    """Top `n` départements (réserve agrégée décroissante) par bloc."""
    return agreger_reserve_par_departement(table_reserve).group_by("bloc", maintain_order=True).head(n)


# --- Lift bureau vs département (réutilise la garde anti-hasard #24) -----------


def lift_reserve_bureau_vs_departement(panel: pl.DataFrame, baseline: pl.DataFrame) -> pl.DataFrame:
    """Lift bureau vs département de la composante volume de la réserve (abstention
    présidentielle 2022, persistance déjà backtestée -- issue #24, ADR 0002).

    Réutilise TELLES QUELLES les primitives de la garde anti-hasard #24
    (`executer_backtest_participation` + `garde_anti_hasard_participation`) :
    seule la composante volume de la réserve est backtestable (une cible 2024
    existe) -- la composante « part estimée du bloc » ne l'est pas (ADR 0002
    point 3), sa robustesse est mesurée par `sensibilite_h1`, jamais par un
    lift. Retourne `cible` x `rho_bureau` x `rho_hasard` (lift) x
    `rho_departement` (lift) x `pass_global` (contexte, pas un gate de la
    réserve elle-même).
    """
    resultats_participation = executer_backtest_participation(panel, baseline)
    return garde_anti_hasard_participation(resultats_participation, panel)


# --- Orchestration : calcul + verdict de publication (ADR 0002 point 5) --------


def calculer_donnees_reserve(
    panel: pl.DataFrame, baseline: pl.DataFrame, methode_part: str = METHODE_PART_DEFAUT
) -> dict:
    """Calcule tout ce dont le rapport a besoin (table, sensibilité, tops, lift,
    verdict de publication) -- un seul passage sur les données, partagé par
    `generer_rapport_complet` (CLI et notebook).
    """
    table_reserve = construire_table_reserve(panel, baseline, methode_part=methode_part)
    sensibilite = sensibilite_h1(panel, baseline, methode_reference=methode_part)
    top_bureau = top_gisements_bureau(table_reserve)
    top_departement = top_gisements_departement(table_reserve)
    lift_participation = lift_reserve_bureau_vs_departement(panel, baseline)

    resultats_backtest = executer_backtests(panel, baseline)
    resultats_participation = executer_backtest_participation(panel, baseline)
    anti_hasard_structure = garde_anti_hasard_structure(resultats_backtest, panel)
    pass_carte_mobilisation = verdict_carte_mobilisation(
        resultats_participation["resultats"], anti_hasard_structure, lift_participation
    )

    distribution = {
        bloc: distribution_swing(table_reserve, bloc=bloc, colonne="reserve")
        for bloc in sorted(table_reserve.get_column("bloc").unique().to_list())
    }
    compte_statuts = (
        table_reserve.select("unite_id", "statut")
        .unique()
        .group_by("statut")
        .agg(pl.len().alias("n_unites"))
        .sort("statut")
    )

    return {
        "table_reserve": table_reserve,
        "sensibilite_h1": sensibilite,
        "top_gisements_bureau": top_bureau,
        "top_gisements_departement": top_departement,
        "lift_bureau_vs_departement": lift_participation,
        "distribution": distribution,
        "compte_statuts": compte_statuts,
        "methode_part": methode_part,
        "pass_carte_mobilisation": pass_carte_mobilisation,
    }


# --- Rapport ---------------------------------------------------------------------


def _ligne_top_bureau(ligne: dict) -> str:
    return (
        f"| {ligne['bloc']} | {ligne['unite_id']} | {ligne['code_departement']} | {ligne['statut']} "
        f"| {ligne['maille']} | {ligne['reserve']:.0f} |"
    )


def _ligne_top_departement(ligne: dict) -> str:
    return f"| {ligne['bloc']} | {ligne['code_departement']} | {ligne['reserve']:.0f} |"


def _ligne_sensibilite(ligne: dict) -> str:
    rho = ligne["rho"]
    rho_txt = f"{rho:.3f}" if rho == rho else "n/d"
    return (
        f"| {ligne['bloc']} | {ligne['methode_variante']} | {rho_txt} "
        f"| {ligne['recouvrement_top_n']:.1%} (top {ligne['n_top']}) |"
    )


def _ligne_statut(ligne: dict) -> str:
    return f"| {ligne['statut']} | {ligne['n_unites']} |"


def _ligne_lift(ligne: dict) -> str:
    verdict_txt = "PASS" if ligne["pass_global"] else "FAIL"

    def _fmt(x: float) -> str:
        return f"{x:.3f}" if x == x else "n/d"

    return (
        f"| {ligne['cible']} | {_fmt(ligne['rho_bureau'])} "
        f"| {ligne['rho_hasard']:.1f} (lift {_fmt(ligne['lift_vs_hasard'])}) "
        f"| {_fmt(ligne['rho_departement'])} (lift {_fmt(ligne['lift_vs_departement'])}) | {verdict_txt} |"
    )


def _ligne_distribution(bloc: str, stats: dict) -> str:
    def _f(cle: str) -> str:
        v = stats.get(cle, float("nan"))
        return f"{v:.1f}" if v == v else "n/d"

    return (
        f"| {bloc} | {stats.get('n', 0)} | {_f('min')} | {_f('p25')} | {_f('median')} "
        f"| {_f('p75')} | {_f('max')} | {_f('mean')} |"
    )


def generer_rapport_reserve(donnees: dict) -> str:
    """Construit le texte de `reserve-2027.md` (issue #25, ADR 0002).

    `donnees` : sortie de `calculer_donnees_reserve`. Chaque section publie ses
    chiffres tels quels, y compris quand le verdict de publication est FAIL
    (transparence, même philosophie que `projections.backtest`).
    """
    table_reserve = donnees["table_reserve"]
    methode_part = donnees["methode_part"]
    pass_carte = donnees["pass_carte_mobilisation"]

    lignes_statuts = "\n".join(_ligne_statut(ligne) for ligne in donnees["compte_statuts"].iter_rows(named=True))
    lignes_top_bureau = "\n".join(
        _ligne_top_bureau(ligne)
        for ligne in donnees["top_gisements_bureau"]
        .sort(["bloc", "reserve", "unite_id"], descending=[False, True, False])
        .iter_rows(named=True)
    )
    lignes_top_departement = "\n".join(
        _ligne_top_departement(ligne)
        for ligne in donnees["top_gisements_departement"]
        .sort(["bloc", "reserve", "code_departement"], descending=[False, True, False])
        .iter_rows(named=True)
    )
    lignes_sensibilite = "\n".join(
        _ligne_sensibilite(ligne)
        for ligne in donnees["sensibilite_h1"].sort(["bloc", "methode_variante"]).iter_rows(named=True)
    )
    lignes_lift = "\n".join(
        _ligne_lift(ligne) for ligne in donnees["lift_bureau_vs_departement"].sort("cible").iter_rows(named=True)
    )
    lignes_distribution = "\n".join(
        _ligne_distribution(bloc, donnees["distribution"][bloc]) for bloc in sorted(donnees["distribution"])
    )

    avertissement = (
        "**Publication en carte : AUTORISÉE** — les clauses pré-enregistrées de l'ADR 0002 "
        "(backtest participation + garde anti-hasard, cf. `backtest-2022-2024.md`) sont au vert."
        if pass_carte
        else (
            "**⚠ PRÉPARATION SEULEMENT — non publiable en carte tant que la révision (issue #28) "
            "n'a pas tranché.** Le gate de publication de la carte mobilisation (ADR 0002 point 5, "
            "réutilisation de `projections.backtest.verdict_carte_mobilisation`) est **FAIL** : le "
            "backtest participation est sorti rouge (ρ europ. 0,769 < 0,8, voir `backtest-2022-2024.md` "
            "§4). Cette table et ce rapport sont publiés tels quels, en préparation de la carte — "
            "aucun chiffre n'est caché — mais aucune publication cartographique n'est autorisée avant "
            "que la révision d'architecture (#28) ne tranche. Les seuils ne bougent pas."
        )
    )

    return f"""# Réserve de voix par bureau × bloc — estimateur v1 (issue #25, ADR 0002)

Couche *estimation* du pivot mobilisation (`docs/adr/0002-pivot-mobilisation-reserve.md`) :
le gisement de voix mobilisables d'un bloc dans une unité (bureau ou commune),
défini par la formule v1 du glossaire (CONTEXT.md « Réserve d'abstention »).
Non backtestable par construction (pas de vérité terrain) — validée par
définition ex ante, analyse de sensibilité (section 3) et appel public à
contradiction, jamais par un gate PASS/FAIL comme les backtests structure/
participation de `projections.backtest` (issue #24).

{avertissement}

## Formule

    réserve(unité, bloc) = inscrits × abstention à la présidentielle 2022 T1
                            (scrutin de même enjeu que la cible 2027)
                            × part estimée du bloc (méthode : « {methode_part} »)

Participation dédupliquée par unité avant tout produit (`projections.backtest.calculer_taux_abstention`,
réutilisée telle quelle). Intermittents (votants présidentielle absents des
scrutins intermédiaires) exclus par construction : seul le scrutin de
référence alimente le volume.

## 1. Statut de réconciliation propagé (aucun état silencieux)

Chaque unité de la table réserve porte le statut hérité du panel
(`projections.churn`) : `joint_valide`/`reconcilie`/`realloue` -> maille
bureau ; `repli` -> maille communale (jamais déguisée en bureau). **{table_reserve.height}**
lignes unité × bloc au total.

| Statut | Unités |
| --- | --- |
{lignes_statuts}

## 2. Top gisements

### Par bloc, à la maille de l'unité (bureau ou commune)

| Bloc | Unité | Département | Statut | Maille | Réserve (voix) |
| --- | --- | --- | --- | --- | --- |
{lignes_top_bureau}

### Par bloc et par département (réserve agrégée par SOMME, jamais une moyenne)

| Bloc | Département | Réserve (voix) |
| --- | --- | --- |
{lignes_top_departement}

## 3. Distribution de la réserve par bloc

| Bloc | n | min | p25 | médiane | p75 | max | moyenne |
| --- | --- | --- | --- | --- | --- | --- | --- |
{lignes_distribution}

## 4. Sensibilité H1 (analyse ex ante, ADR 0002 point 3)

H1 (CONTEXT.md) : la répartition politique des abstentionnistes ≈ celle des
votants du bureau (méthode par défaut, `{methode_part}`). Variante testée pour
la sensibilité : `uniforme_entre_blocs` (répartition égale entre les blocs
présents). `rho` : Spearman des valeurs de réserve entre les 2 méthodes (1 =
classement inchangé) ; `recouvrement_top_n` : part commune aux 2 top 20 de
gisements (1 = ensembles identiques).

| Bloc | Variante | ρ (valeurs de réserve) | Recouvrement top N |
| --- | --- | --- | --- |
{lignes_sensibilite}

## 5. Lift bureau vs département (réutilisation de la garde anti-hasard #24)

Seule la composante volume de la réserve (abstention présidentielle 2022,
persistance 2022→2024) est backtestable : ce tableau réutilise tel quel le
résultat de `projections.backtest.garde_anti_hasard_participation` (issue #24,
ADR 0002) — la granularité bureau doit battre (>, pas ≥) la granularité
département sur la persistance de l'abstention. La composante « part estimée
du bloc » n'a pas de lift (non backtestable, cf. section 4 ci-dessus).

| Cible | ρ bureau | ρ hasard (lift) | ρ département (lift) | Verdict |
| --- | --- | --- | --- | --- |
{lignes_lift}

## Verdict de publication en carte (ADR 0002 point 5)

{avertissement}
"""


def generer_rapport_complet(panel: pl.DataFrame, baseline: pl.DataFrame, methode_part: str = METHODE_PART_DEFAUT) -> dict:
    """Pipeline complet panel + baseline → rapport et verdict (issue #25).

    Unique chemin de génération de `reserve-2027.md` : le CLI (`main`) et le
    notebook marimo appellent tous deux cette fonction -- la byte-identité
    CLI/notebook est structurelle (même discipline que `projections.backtest`,
    revue PR #27).
    """
    donnees = calculer_donnees_reserve(panel, baseline, methode_part=methode_part)
    rapport = generer_rapport_reserve(donnees)
    return {
        "rapport": rapport,
        "table_reserve": donnees["table_reserve"],
        "pass_carte_mobilisation": donnees["pass_carte_mobilisation"],
    }


# --- Entrée console -----------------------------------------------------------


def main() -> None:
    """Point d'entrée `uv run reserve`."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, default=INTERIM_DIR / "panel_avec_statut.parquet")
    parser.add_argument("--baseline", type=Path, default=INTERIM_DIR / "baseline_unite_bloc.parquet")
    parser.add_argument("--out", type=Path, default=Path("reserve-2027.md"))
    parser.add_argument("--table-out", type=Path, default=INTERIM_DIR / "reserve_bureau_bloc.parquet")
    parser.add_argument("--methode-part", choices=tuple(METHODES_PART_H1), default=METHODE_PART_DEFAUT)
    args = parser.parse_args()

    panel = pl.read_parquet(args.panel)
    baseline = pl.read_parquet(args.baseline)

    sortie = generer_rapport_complet(panel, baseline, methode_part=args.methode_part)

    args.out.write_text(sortie["rapport"], encoding="utf-8")
    args.table_out.parent.mkdir(parents=True, exist_ok=True)
    sortie["table_reserve"].write_parquet(args.table_out)

    print(f"rapport écrit : {args.out}")
    print(f"table réserve écrite : {args.table_out} ({sortie['table_reserve'].height} lignes)")
    print(f"publication en carte autorisée (ADR 0002) : {sortie['pass_carte_mobilisation']}")


if __name__ == "__main__":
    main()

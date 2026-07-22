"""Baseline composite + terme de dérive 2022->2024, par unité x bloc (issue #5,
HANDOFF.md étape 1).

Aucun scrutin seul ne convient (législatives biaisées par l'offre, européennes
biaisées en niveau par l'effet second-ordre, présidentielle 2022 datée par la
recomposition) : on combine les 3 en un indice composite type Cook PVI / 538
partisan lean, le premier construit pour la France à la maille bureau de vote.

## Écart relatif au national (calculer_ecart_national)

Par scrutin x unité x bloc, la structure spatiale est mesurée en **écart en
points des exprimés vs national** (convention Cook PVI, la plus lisible pour
un public militant et la plus directe à calculer depuis des voix) :

    pct_unite    = voix_bloc_unite / exprimes_unite
    pct_national = somme(voix_bloc) / somme(exprimes, dédupliqué par unité)
    ecart        = (pct_unite - pct_national) * 100

Jamais de moyenne de pourcentages (docs/heritage-2024.md) : tout part des
colonnes de comptage (voix, exprimes), sommées puis reconverties en part.

Propriété garantie par cette forme, mais SEULEMENT à offre complète (chaque
bloc a un candidat dans chaque unité) : la somme des écarts sur les blocs
d'une même unité est nulle, et la somme des écarts sur les unités pour un
bloc donné, pondérée par les exprimés de chaque unité, est nulle aussi (le
national est justement la moyenne pondérée des unités). Cette propriété est
vraie par construction pour la présidentielle et quasi vraie pour les
européennes (listes nationales), mais PAS pour les législatives T1 : une
circonscription sans candidat d'un bloc n'a tout simplement pas de ligne pour
ce bloc, ce qui casse la propriété -- raison d'être de la correction d'offre
ci-dessous.

## Correction d'offre des législatives T1 (corriger_offre_legislatives)

Dans le panel, l'absence d'une ligne (id_election=2024_legi_t1, unité, bloc)
signifie « aucun candidat de ce bloc sur le bulletin de cette unité » (les
candidats à 0 voix existent quand même comme ligne dans candidats_results :
seule l'absence totale de candidat produit une ligne manquante après
`agreger_par_bloc`, cf. projections.ingest). Sans correction, ce score
manquant-structurel serait confondu avec un score de 0 -- faux, puisque
personne ne pouvait voter pour ce bloc.

Méthode retenue (par défaut, `methode="imputation"`) : imputer l'écart
relatif du bloc depuis sa structure européennes 2024 dans la même unité.
Justification : les européennes se votent sur listes nationales, donc
l'offre y est quasi complète partout (contrairement aux législatives, où
chaque bloc n'aligne pas forcément un candidat dans les 577
circonscriptions) -- c'est la meilleure structure de repli disponible dans
le panel actuel.

Analyse de sensibilité (`methode="exclusion"`) : au lieu d'imputer une
valeur, on exclut purement le bloc de l'unité pour ce scrutin (aucune ligne
ajoutée). En aval, `composite_pondere` (à venir) renormalise ses poids sur
les composantes réellement présentes -- la composante manquante ne compte ni
pour 0 ni pour la valeur européenne, elle est simplement absente du calcul.
Les deux variantes sont documentées et disponibles ; le choix par défaut
(imputation) suppose que la dynamique européenne est un meilleur proxy que
l'absence pure d'information, hypothèse à confronter au backtest (#6).

Remarque sur `code_circonscription` : la source (`general_results`) porte
cette colonne, mais elle est **entièrement vide pour 2024_legi_t1 et
2024_euro_t1** dans les données réelles (vérifié sur le Parquet complet,
juillet 2026) -- seule la présidentielle 2022 la renseigne. Étendre
`projections.ingest` pour la conserver n'aurait donc rien apporté ici. La
détection se fait à la place directement au niveau unité : l'absence d'une
ligne (unité, bloc) pour 2024_legi_t1 équivaut à « aucun candidat de ce bloc
sur ce bulletin », puisque tous les bureaux d'une même circonscription
partagent le même bulletin -- une détection à la maille unité est donc au
moins aussi précise qu'une détection à la maille circonscription, sans
dépendre d'une colonne vide.

## Composite pondéré (composite_pondere) et variante moyenne tronquée
(composite_moyenne_tronquee)

Combinaison pondérée des 3 composantes conservées (présidentielle 2022 brute,
européennes 2024 brutes, législatives 2024 corrigées) : poids par défaut 50 %
/ 25 % / 25 % (`POIDS_PAR_DEFAUT`), PARAMÉTRABLES -- ce sont des constantes de
départ, pas des constantes enfouies : c'est le backtest (#6) qui les calibre.

Variante « moyenne tronquée » à la Inside Elections : avec exactement 3
composantes, une troncature à 1 de chaque extrémité ne laisse qu'une seule
valeur -- la médiane. C'est une dégénérescence VOULUE, pas un raccourci
malheureux : à 3 notations, moyenne tronquée et médiane coïncident
exactement. `composite_moyenne_tronquee` calcule directement la médiane des
composantes présentes (généralise proprement au cas où une composante est
absente via la variante d'exclusion : médiane de 2 valeurs = leur moyenne,
médiane de 1 valeur = cette valeur).

## Dérive 2022->2024 (calculer_derive)

    derive = moyenne(ecart_2024_euro_t1, ecart_2024_legi_t1_corrige) - ecart_2022_pres_t1

Évolution de l'écart relatif entre la présidentielle 2022 et la structure
2024 (moyenne des deux scrutins 2024, législatives déjà corrigées de
l'offre). Positif : le bloc gagne du terrain relatif dans l'unité entre 2022
et 2024 -- capte la diffusion RN hors bastions (HANDOFF.md étape 1).
Extrapolable pour un scénario 2027, jamais figé.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable
from pathlib import Path

import polars as pl

INTERIM_DIR = Path("data/interim")

SCRUTIN_PRESIDENTIELLE = "2022_pres_t1"
SCRUTIN_EUROPEENNES = "2024_euro_t1"
SCRUTIN_LEGISLATIVES = "2024_legi_t1"
SCRUTIN_LEGISLATIVES_CORRIGE = f"{SCRUTIN_LEGISLATIVES}_corrige"

# Les 3 scrutins de structure spatiale (HANDOFF.md étape 1) : présidentielle 2022,
# européennes 2024, législatives 2024 (avant correction d'offre -- la version
# corrigée est calculée par corriger_offre_legislatives, à venir).
SCRUTINS_STRUCTURE: tuple[str, ...] = (SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES, SCRUTIN_LEGISLATIVES)

# Point de départ, pas une constante figée : le backtest (#6) calibre ces poids.
POIDS_PAR_DEFAUT: dict[str, float] = {
    SCRUTIN_PRESIDENTIELLE: 0.50,
    SCRUTIN_EUROPEENNES: 0.25,
    SCRUTIN_LEGISLATIVES_CORRIGE: 0.25,
}


def _colonne_composante(scrutin: str) -> str:
    return f"ecart_{scrutin}"


def _ajouter_unite(panel: pl.DataFrame) -> pl.DataFrame:
    """unite_id = id_bv (jointure directe, statut joint_valide) ou code_commune (repli).

    Coalesce : les lignes en repli (CONTEXT.md, churn.py) ont id_bv/code_bv à
    null, seul code_commune identifie alors l'unité.
    """
    return panel.with_columns(pl.coalesce(["id_bv", "code_commune"]).alias("unite_id"))


def calculer_ecart_national(panel: pl.DataFrame, scrutins: Iterable[str] | None = None) -> pl.DataFrame:
    """Écart relatif au national, par scrutin x unité x bloc (cf. docstring du module).

    `panel` : table longue bureau/commune x scrutin x bloc (schéma `projections.ingest`
    / `projections.churn`, colonnes `voix` et `exprimes` au minimum). `scrutins` limite
    le calcul à ces `id_election` (le national de chaque scrutin ne dépend que des
    lignes de ce même scrutin, filtrer ne change donc pas le résultat des scrutins
    conservés -- ça évite juste de calculer ce qui ne sera pas utilisé).
    """
    df = _ajouter_unite(panel)
    if scrutins is not None:
        df = df.filter(pl.col("id_election").is_in(list(scrutins)))

    # Participation dédupliquée par unité x scrutin : répétée sur chaque ligne de
    # bloc dans le panel long (cf. projections.ingest), la sommer telle quelle
    # compterait chaque unité autant de fois qu'elle a de blocs.
    exprimes_unite = (
        df.select("id_election", "unite_id", "exprimes").unique().rename({"exprimes": "exprimes_unite"})
    )
    exprimes_national = exprimes_unite.group_by("id_election").agg(
        pl.col("exprimes_unite").sum().alias("exprimes_national")
    )
    voix_national = df.group_by(["id_election", "bloc"]).agg(pl.col("voix").sum().alias("voix_national"))
    national = voix_national.join(exprimes_national, on="id_election").with_columns(
        (pl.col("voix_national") / pl.col("exprimes_national")).alias("pct_national")
    )

    return (
        df.select("id_election", "unite_id", "bloc", "voix")
        .join(exprimes_unite, on=["id_election", "unite_id"])
        # Garde-fou division par zéro : quelques dizaines de bureaux réels ont
        # exprimes=0 (bulletins tous nuls/blancs) -- pct_unite doit être null
        # (donnée absente), jamais NaN (0/0), sous peine de contaminer tout
        # calcul en aval (composite, dérive) qui ignore les null mais pas les NaN.
        .with_columns(
            pl.when(pl.col("exprimes_unite") > 0)
            .then(pl.col("voix") / pl.col("exprimes_unite"))
            .otherwise(None)
            .alias("pct_unite")
        )
        .join(national.select("id_election", "bloc", "pct_national"), on=["id_election", "bloc"])
        .with_columns(((pl.col("pct_unite") - pl.col("pct_national")) * 100).alias("ecart_national"))
        .sort(["id_election", "unite_id", "bloc"])
    )


def corriger_offre_legislatives(
    ecart: pl.DataFrame,
    scrutin_a_corriger: str = SCRUTIN_LEGISLATIVES,
    scrutin_reference: str = SCRUTIN_EUROPEENNES,
    methode: str = "imputation",
) -> pl.DataFrame:
    """Corrige l'offre des législatives T1 (cf. docstring du module).

    `ecart` : sortie de `calculer_ecart_national`, doit couvrir au moins
    `scrutin_a_corriger` et `scrutin_reference`. Retourne une table
    (id_election=<scrutin_a_corriger>_corrige, unite_id, bloc, ecart_national, impute)
    -- `impute` distingue les valeurs d'origine (False) des valeurs reprises du
    scrutin de référence (True, méthode "imputation" seulement).
    """
    if methode not in ("imputation", "exclusion"):
        raise ValueError(f"méthode inconnue : {methode!r} (attendu 'imputation' ou 'exclusion')")

    id_election_corrige = f"{scrutin_a_corriger}_corrige"
    observe = ecart.filter(pl.col("id_election") == scrutin_a_corriger).select(
        "unite_id", "bloc", "ecart_national"
    )
    observe_marque = observe.with_columns(
        pl.lit(False).alias("impute"), pl.lit(id_election_corrige).alias("id_election")
    ).select("id_election", "unite_id", "bloc", "ecart_national", "impute")

    if methode == "exclusion":
        return observe_marque

    univers = (
        ecart.filter(pl.col("id_election").is_in([scrutin_a_corriger, scrutin_reference]))
        .select("unite_id", "bloc")
        .unique()
    )
    manquants = univers.join(observe.select("unite_id", "bloc"), on=["unite_id", "bloc"], how="anti")
    reference = ecart.filter(pl.col("id_election") == scrutin_reference).select(
        "unite_id", "bloc", "ecart_national"
    )
    impute = (
        manquants.join(reference, on=["unite_id", "bloc"], how="left")
        .with_columns(pl.lit(True).alias("impute"), pl.lit(id_election_corrige).alias("id_election"))
        .select("id_election", "unite_id", "bloc", "ecart_national", "impute")
    )
    return pl.concat([observe_marque, impute]).sort(["unite_id", "bloc"])


def construire_table_composantes(ecart: pl.DataFrame, legi_corrige: pl.DataFrame) -> pl.DataFrame:
    """Table large unité x bloc : une colonne par composante mono-scrutin conservée.

    Combine l'écart présidentielle 2022 et européennes 2024 (bruts, `ecart` =
    sortie de `calculer_ecart_national`) avec les législatives 2024 corrigées
    (`legi_corrige` = sortie de `corriger_offre_legislatives`) -- les 3
    composantes que le backtest (#6) doit pouvoir comparer individuellement au
    composite.
    """
    composantes_long = pl.concat(
        [
            ecart.filter(pl.col("id_election").is_in([SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES])).select(
                "id_election", "unite_id", "bloc", "ecart_national"
            ),
            legi_corrige.select("id_election", "unite_id", "bloc", "ecart_national"),
        ]
    )
    large = composantes_long.pivot(on="id_election", index=["unite_id", "bloc"], values="ecart_national")
    renommage = {
        scrutin: _colonne_composante(scrutin) for scrutin in large.columns if scrutin not in ("unite_id", "bloc")
    }
    return large.rename(renommage)


def composite_pondere(
    table: pl.DataFrame, poids: dict[str, float] | None = None, nom_colonne: str = "composite"
) -> pl.DataFrame:
    """Moyenne pondérée des composantes présentes (cf. docstring du module).

    `poids` : mapping id_election (SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES,
    SCRUTIN_LEGISLATIVES_CORRIGE par défaut) -> poids. PARAMÉTRABLE : jamais de
    poids figé en dur ailleurs que dans `POIDS_PAR_DEFAUT`, qui n'est qu'un point
    de départ. Une composante nulle pour une unité x bloc (variante "exclusion"
    de la correction d'offre) est exclue du calcul et son poids renormalisé sur
    les composantes restantes -- jamais traitée comme un 0.
    """
    poids = poids or POIDS_PAR_DEFAUT
    colonnes = {scrutin: _colonne_composante(scrutin) for scrutin in poids}
    manquantes = [col for col in colonnes.values() if col not in table.columns]
    if manquantes:
        raise ValueError(f"composante(s) manquante(s) dans la table : {manquantes}")

    poids_disponible = pl.sum_horizontal(
        [
            pl.when(pl.col(col).is_not_null()).then(pl.lit(w)).otherwise(0.0)
            for w, col in zip(poids.values(), colonnes.values(), strict=True)
        ]
    )
    somme_ponderee = pl.sum_horizontal(
        [pl.col(col).fill_null(0.0) * w for w, col in zip(poids.values(), colonnes.values(), strict=True)]
    )
    # Aucune composante disponible (ex. bloc structurellement absent d'un scrutin,
    # comme "Divers" à la présidentielle) : composite null, jamais une division
    # par zéro qui produirait NaN.
    return table.with_columns(
        pl.when(poids_disponible > 0).then(somme_ponderee / poids_disponible).otherwise(None).alias(nom_colonne)
    )


def composite_moyenne_tronquee(
    table: pl.DataFrame, colonnes: Iterable[str] | None = None, nom_colonne: str = "composite_tronque"
) -> pl.DataFrame:
    """Variante « moyenne tronquée » à la Inside Elections (cf. docstring du module).

    Médiane des composantes présentes : à 3 composantes (le cas par défaut),
    c'est très exactement une moyenne tronquée à 1 de chaque extrémité --
    dégénérescence voulue, pas un raccourci.
    """
    colonnes = (
        list(colonnes)
        if colonnes is not None
        else [_colonne_composante(s) for s in (SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES, SCRUTIN_LEGISLATIVES_CORRIGE)]
    )
    manquantes = [c for c in colonnes if c not in table.columns]
    if manquantes:
        raise ValueError(f"composante(s) manquante(s) dans la table : {manquantes}")
    mediane = pl.concat_list(colonnes).list.drop_nulls().list.median()
    return table.with_columns(mediane.alias(nom_colonne))


def calculer_derive(table: pl.DataFrame, nom_colonne: str = "derive") -> pl.DataFrame:
    """Terme de dérive 2022->2024 par unité x bloc (cf. docstring du module).

    derive = moyenne(ecart_2024_euro_t1, ecart_2024_legi_t1_corrige) - ecart_2022_pres_t1
    """
    col_pres = _colonne_composante(SCRUTIN_PRESIDENTIELLE)
    col_euro = _colonne_composante(SCRUTIN_EUROPEENNES)
    col_legi = _colonne_composante(SCRUTIN_LEGISLATIVES_CORRIGE)
    manquantes = [c for c in (col_pres, col_euro, col_legi) if c not in table.columns]
    if manquantes:
        raise ValueError(f"composante(s) manquante(s) dans la table : {manquantes}")
    moyenne_2024 = pl.concat_list([col_euro, col_legi]).list.drop_nulls().list.mean()
    return table.with_columns((moyenne_2024 - pl.col(col_pres)).alias(nom_colonne))


def construire_baseline(
    panel: pl.DataFrame,
    poids: dict[str, float] | None = None,
    methode_correction: str = "imputation",
) -> pl.DataFrame:
    """Table baseline unité x bloc complète (issue #5) : composantes mono-scrutin
    conservées + composite + variante moyenne tronquée + dérive + statut/maille
    hérités du panel (churn.py).

    `panel` : panel avec statut (`projections.churn.construire_panel_avec_statut`),
    colonne `statut` requise pour hériter la maille (joint_valide -> bureau,
    repli -> commune).
    """
    ecart = calculer_ecart_national(panel, scrutins=SCRUTINS_STRUCTURE)
    legi_corrige = corriger_offre_legislatives(ecart, methode=methode_correction)
    table = construire_table_composantes(ecart, legi_corrige)
    table = composite_pondere(table, poids=poids)
    table = composite_moyenne_tronquee(table)
    table = calculer_derive(table)

    statut_maille = (
        _ajouter_unite(panel)
        .select("unite_id", "code_departement", "statut")
        .sort(["unite_id", "code_departement"])
        .unique(subset="unite_id", keep="first")
        .with_columns(
            pl.when(pl.col("statut") == "joint_valide")
            .then(pl.lit("bureau"))
            .otherwise(pl.lit("commune"))
            .alias("maille")
        )
    )
    return table.join(statut_maille, on="unite_id", how="left").sort(["unite_id", "bloc"])


def main() -> None:
    """Point d'entrée `uv run baseline`."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panel", type=Path, default=INTERIM_DIR / "panel_avec_statut.parquet")
    parser.add_argument("--out", type=Path, default=INTERIM_DIR / "baseline_unite_bloc.parquet")
    parser.add_argument(
        "--poids-presidentielle", type=float, default=POIDS_PAR_DEFAUT[SCRUTIN_PRESIDENTIELLE]
    )
    parser.add_argument("--poids-europeennes", type=float, default=POIDS_PAR_DEFAUT[SCRUTIN_EUROPEENNES])
    parser.add_argument(
        "--poids-legislatives", type=float, default=POIDS_PAR_DEFAUT[SCRUTIN_LEGISLATIVES_CORRIGE]
    )
    parser.add_argument("--methode-correction", choices=("imputation", "exclusion"), default="imputation")
    args = parser.parse_args()

    poids = {
        SCRUTIN_PRESIDENTIELLE: args.poids_presidentielle,
        SCRUTIN_EUROPEENNES: args.poids_europeennes,
        SCRUTIN_LEGISLATIVES_CORRIGE: args.poids_legislatives,
    }

    panel = pl.read_parquet(args.panel)
    baseline = construire_baseline(panel, poids=poids, methode_correction=args.methode_correction)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    baseline.write_parquet(args.out)
    print(f"baseline écrite : {args.out} ({baseline.height} lignes)")


if __name__ == "__main__":
    main()

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
à venir (issue #5, prochain morceau de ce module).
"""

from __future__ import annotations

from collections.abc import Iterable

import polars as pl

SCRUTIN_PRESIDENTIELLE = "2022_pres_t1"
SCRUTIN_EUROPEENNES = "2024_euro_t1"
SCRUTIN_LEGISLATIVES = "2024_legi_t1"

# Les 3 scrutins de structure spatiale (HANDOFF.md étape 1) : présidentielle 2022,
# européennes 2024, législatives 2024 (avant correction d'offre -- la version
# corrigée est calculée par corriger_offre_legislatives, à venir).
SCRUTINS_STRUCTURE: tuple[str, ...] = (SCRUTIN_PRESIDENTIELLE, SCRUTIN_EUROPEENNES, SCRUTIN_LEGISLATIVES)


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

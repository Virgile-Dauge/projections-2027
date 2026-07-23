"""Tests de la préparation des données carte mobilisation (issue #26, ADR 0002/0003).

Quatre familles :
- `quantiles_larges` : bucket ordinal générique, calculé par groupe, déterministe ;
- `preparer_carte_reserve` / `agreger_reserve_commune` : format large bureau x
  commune de la réserve (#25), dézoom par SOMMES jamais moyennes, repli visible ;
- `preparer_carte_rapport_force` : bloc en tête projeté + quantile large (#5,
  ADR 0002 — l'ordre fin est déclassé, jamais recalculé ici) ;
- `verifier_publication_autorisee` : gate mécanique, réutilise
  `projections.backtest.verdict_carte_mobilisation` tel quel, jamais recalculé.
"""

from __future__ import annotations

import polars as pl
import pytest

from projections.baseline import construire_baseline
from projections.churn import classifier_communes, construire_panel_avec_statut
from projections.mobilisation import (
    agreger_reserve_commune,
    assembler_donnees_bureau,
    assembler_donnees_commune,
    construire_donnees_mobilisation,
    preparer_carte_rapport_force,
    preparer_carte_reserve,
    quantiles_larges,
    verifier_publication_autorisee,
)
from projections.reserve import construire_table_reserve

# --- quantiles_larges ----------------------------------------------------------


def test_quantiles_larges_repartit_en_n_buckets_egaux():
    # 10 valeurs, 1 seul groupe, n=5 -> 2 valeurs par bucket, buckets 1..5 dans
    # l'ordre croissant de la valeur.
    table = pl.DataFrame({"bloc": ["Gauche"] * 10, "reserve": list(range(10))})
    resultat = quantiles_larges(table, "reserve", groupe="bloc", n=5)
    buckets = resultat.sort("reserve").get_column("quantile_reserve").to_list()
    assert buckets == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


def test_quantiles_larges_calcule_separement_par_groupe():
    # 2 blocs, échelles de valeurs très différentes : le bucket d'une unité ne
    # doit dépendre que de la distribution DE SON PROPRE bloc.
    table = pl.DataFrame(
        {
            "bloc": ["Gauche", "Gauche", "Droite", "Droite"],
            "v": [1.0, 1000.0, 5.0, 6.0],
        }
    )
    resultat = quantiles_larges(table, "v", groupe="bloc", n=2)
    gauche = resultat.filter(pl.col("bloc") == "Gauche").sort("v").get_column("quantile_v").to_list()
    droite = resultat.filter(pl.col("bloc") == "Droite").sort("v").get_column("quantile_v").to_list()
    assert gauche == [1, 2]
    assert droite == [1, 2]


def test_quantiles_larges_valeur_nulle_reste_nulle_jamais_un_bucket_fabrique():
    table = pl.DataFrame({"bloc": ["Gauche", "Gauche", "Gauche"], "v": [1.0, None, 3.0]})
    resultat = quantiles_larges(table, "v", groupe="bloc", n=2)
    ligne_nulle = resultat.filter(pl.col("v").is_null())
    assert ligne_nulle.get_column("quantile_v")[0] is None


def test_quantiles_larges_est_deterministe():
    table = pl.DataFrame({"bloc": ["Gauche"] * 6, "v": [3.0, 1.0, 4.0, 1.0, 5.0, 9.0]})
    a = quantiles_larges(table, "v", groupe="bloc", n=3)
    b = quantiles_larges(table, "v", groupe="bloc", n=3)
    assert a.equals(b)


def test_quantiles_larges_groupe_multiple_calcule_par_sous_groupe():
    # `groupe` accepte une liste de colonnes (issue #37, CONTEXT.md « Tranche
    # départementale ») : le bucket d'une unité ne dépend que de la
    # distribution de SON sous-groupe (bloc x département), jamais des deux
    # départements mélangés.
    table = pl.DataFrame(
        {
            "bloc": ["Gauche"] * 4,
            "code_departement": ["69", "69", "75", "75"],
            "v": [1.0, 1000.0, 5.0, 6.0],
        }
    )
    resultat = quantiles_larges(table, "v", groupe=["bloc", "code_departement"], n=2)
    d69 = resultat.filter(pl.col("code_departement") == "69").sort("v").get_column("quantile_v").to_list()
    d75 = resultat.filter(pl.col("code_departement") == "75").sort("v").get_column("quantile_v").to_list()
    assert d69 == [1, 2]
    assert d75 == [1, 2]


def test_quantiles_larges_suffixe_nomme_la_colonne_differemment():
    # `suffixe` (issue #37) : le quantile départemental s'ajoute en colonne
    # SUPPLÉMENTAIRE (`quantile_<colonne>_dep`), jamais en remplacement.
    table = pl.DataFrame({"bloc": ["Gauche"] * 4, "v": [1.0, 2.0, 3.0, 4.0]})
    resultat = quantiles_larges(table, "v", groupe="bloc", n=2, suffixe="_dep")
    assert "quantile_v_dep" in resultat.columns
    assert "quantile_v" not in resultat.columns


def test_quantiles_larges_petit_groupe_reste_borne_dans_1_n():
    # Cas 975 (Saint-Pierre-et-Miquelon, 4 bureaux, n=5) : un groupe plus petit
    # que n ne peut jamais produire un bucket hors [1, n] -- la tranche 1 peut
    # simplement rester vide (jamais une erreur, cf. docs/adr/0005-*.md).
    table = pl.DataFrame({"bloc": ["Gauche"] * 4, "v": [1.0, 2.0, 3.0, 4.0]})
    resultat = quantiles_larges(table, "v", groupe="bloc", n=5)
    buckets = resultat.sort("v").get_column("quantile_v").to_list()
    assert buckets == [2, 3, 4, 5]
    assert all(1 <= b <= 5 for b in buckets)


# --- verifier_publication_autorisee ---------------------------------------------


def test_verifier_publication_autorisee_ne_leve_rien_si_pass():
    verifier_publication_autorisee(True)  # ne doit pas lever


def test_verifier_publication_autorisee_leve_si_fail():
    with pytest.raises(RuntimeError, match="[Vv]erdict"):
        verifier_publication_autorisee(False)


# --- preparer_carte_reserve / agreger_reserve_commune : pipeline réel ----------


def _ligne(id_election, code_commune, code_bv, bloc, voix, exprimes, code_departement="69", abstentions=10, inscrits=None):
    id_bv = f"{code_commune}_{code_bv}"
    return {
        "id_election": id_election,
        "code_departement": code_departement,
        "code_commune": code_commune,
        "code_bv": code_bv,
        "id_bv": id_bv,
        "bloc": bloc,
        "voix": voix,
        "inscrits": inscrits if inscrits is not None else exprimes + 50,
        "abstentions": abstentions,
        "votants": exprimes + 20,
        "blancs": 10,
        "nuls": 10,
        "exprimes": exprimes,
    }


def _panel_bureau_commune_repli() -> list[dict]:
    lignes = []
    # 69123 : 1 bureau stable, 2 blocs.
    for id_election in ("2022_pres_t1", "2022_legi_t1", "2024_euro_t1", "2024_legi_t1"):
        lignes.append(_ligne(id_election, "69123", "0001", "Gauche", 30, 100, abstentions=60, inscrits=200))
        lignes.append(_ligne(id_election, "69123", "0001", "Droite", 70, 100, abstentions=60, inscrits=200))
    # 69777 : 2 bureaux stables (mêmes 2 blocs) -- pour tester la SOMME du dézoom.
    for id_election in ("2022_pres_t1", "2022_legi_t1", "2024_euro_t1", "2024_legi_t1"):
        lignes.append(_ligne(id_election, "69777", "0001", "Gauche", 20, 100, abstentions=40, inscrits=150))
        lignes.append(_ligne(id_election, "69777", "0001", "Droite", 80, 100, abstentions=40, inscrits=150))
        lignes.append(_ligne(id_election, "69777", "0002", "Gauche", 10, 50, abstentions=25, inscrits=100))
        lignes.append(_ligne(id_election, "69777", "0002", "Droite", 40, 50, abstentions=25, inscrits=100))
    # 69456 : commune en repli (2 bureaux au pres/legi2022/euro2024, 1 seul aux legi2024).
    lignes += [
        _ligne("2022_pres_t1", "69456", "0001", "Gauche", 10, 50, abstentions=20, inscrits=100),
        _ligne("2022_pres_t1", "69456", "0001", "Droite", 40, 50, abstentions=20, inscrits=100),
        _ligne("2022_pres_t1", "69456", "0002", "Gauche", 5, 40, abstentions=15, inscrits=80),
        _ligne("2022_pres_t1", "69456", "0002", "Droite", 35, 40, abstentions=15, inscrits=80),
        _ligne("2022_legi_t1", "69456", "0001", "Gauche", 10, 50, abstentions=20, inscrits=100),
        _ligne("2022_legi_t1", "69456", "0001", "Droite", 40, 50, abstentions=20, inscrits=100),
        _ligne("2022_legi_t1", "69456", "0002", "Gauche", 5, 40, abstentions=15, inscrits=80),
        _ligne("2022_legi_t1", "69456", "0002", "Droite", 35, 40, abstentions=15, inscrits=80),
        _ligne("2024_euro_t1", "69456", "0001", "Gauche", 10, 50, abstentions=20, inscrits=100),
        _ligne("2024_euro_t1", "69456", "0001", "Droite", 40, 50, abstentions=20, inscrits=100),
        _ligne("2024_euro_t1", "69456", "0002", "Gauche", 5, 40, abstentions=15, inscrits=80),
        _ligne("2024_euro_t1", "69456", "0002", "Droite", 35, 40, abstentions=15, inscrits=80),
        _ligne("2024_legi_t1", "69456", "0003", "Gauche", 15, 90, abstentions=35, inscrits=180),
        _ligne("2024_legi_t1", "69456", "0003", "Droite", 75, 90, abstentions=35, inscrits=180),
    ]
    return lignes


@pytest.fixture(scope="module")
def panel_et_baseline_synthetiques() -> tuple[pl.DataFrame, pl.DataFrame]:
    panel_brut = pl.DataFrame(_panel_bureau_commune_repli())
    classification = classifier_communes(panel_brut)
    panel = construire_panel_avec_statut(panel_brut, classification)
    baseline = construire_baseline(panel)
    return panel, baseline


@pytest.fixture(scope="module")
def table_reserve_synthetique(panel_et_baseline_synthetiques) -> pl.DataFrame:
    panel, baseline = panel_et_baseline_synthetiques
    return construire_table_reserve(panel, baseline)


def test_preparer_carte_reserve_une_ligne_par_unite_bureau_avec_colonnes_par_bloc(table_reserve_synthetique):
    large = preparer_carte_reserve(table_reserve_synthetique, n_quantiles=5)
    ligne = large.filter(pl.col("unite_id") == "69123_0001")
    assert ligne.height == 1
    # inscrits=200, taux_abstention=0.3, part Gauche=0.3 -> réserve = 18.0 ; Droite 0.7 -> 42.0.
    assert ligne.get_column("reserve_gauche")[0] == pytest.approx(18.0)
    assert ligne.get_column("reserve_droite")[0] == pytest.approx(42.0)
    assert ligne.get_column("statut")[0] == "joint_valide"
    assert ligne.get_column("maille")[0] == "bureau"


def test_preparer_carte_reserve_exclut_les_communes_en_repli(table_reserve_synthetique):
    large = preparer_carte_reserve(table_reserve_synthetique, n_quantiles=5)
    assert large.filter(pl.col("unite_id") == "69456").height == 0
    assert (large.get_column("maille") == "bureau").all()


# --- Tranche départementale (issue #37, CONTEXT.md « Tranche départementale »,
# --- docs/adr/0005-*.md) : quantile_reserve_<slug>_dep, recalculé PAR département --


def _table_reserve_deux_departements() -> pl.DataFrame:
    # 69 : bastion (20 bureaux, réserve Gauche élevée partout) ; 75 : réserve
    # Gauche faible partout (5 bureaux) -- au national, même le MEILLEUR
    # bureau de 75 tombe en tranche basse (écrasé par le volume du bastion) ;
    # à l'échelle départementale, chaque département affiche sa PROPRE gamme
    # complète de tranches (l'objectif produit de l'issue).
    lignes = []
    for i in range(20):
        lignes.append(
            {
                "unite_id": f"69_{i}",
                "bloc": "Gauche",
                "reserve": 100.0 + i * 10,
                "code_departement": "69",
                "statut": "joint_valide",
                "maille": "bureau",
            }
        )
    for i, valeur in enumerate([1.0, 2.0, 3.0, 4.0, 5.0]):
        lignes.append(
            {
                "unite_id": f"75_{i}",
                "bloc": "Gauche",
                "reserve": valeur,
                "code_departement": "75",
                "statut": "joint_valide",
                "maille": "bureau",
            }
        )
    return pl.DataFrame(lignes)


def test_preparer_carte_reserve_quantile_departemental_desaplatit_le_departement_faible():
    large = preparer_carte_reserve(_table_reserve_deux_departements(), n_quantiles=5)
    ligne = large.filter(pl.col("unite_id") == "75_4")  # valeur=5.0, max de SON département.
    # National : écrasé par le volume du bastion 69 (20 bureaux à 100+) -> tranche la plus basse.
    assert ligne.get_column("quantile_reserve_gauche")[0] == 1
    # Départemental : au sommet de SA PROPRE distribution -> tranche max.
    assert ligne.get_column("quantile_reserve_gauche_dep")[0] == 5


def test_preparer_carte_reserve_quantile_national_reste_present_inchange():
    # Le quantile national n'est pas retiré des tuiles (réversibilité côté
    # client seul) -- seul le site cesse de l'afficher (site/main.js).
    large = preparer_carte_reserve(_table_reserve_deux_departements(), n_quantiles=5)
    assert "quantile_reserve_gauche" in large.columns
    assert "quantile_reserve_gauche_dep" in large.columns


def test_agreger_reserve_commune_quantile_departemental_calcule_sur_sa_propre_population(table_reserve_synthetique):
    # La maille commune recalcule sa PROPRE échelle départementale (jamais
    # mélangée avec la population bureau, même discipline que le quantile
    # national -- cf. docstring de `agreger_reserve_commune`).
    large = agreger_reserve_commune(table_reserve_synthetique, n_quantiles=3)
    assert "quantile_reserve_gauche_dep" in large.columns


def test_agreger_reserve_commune_repli_participe_au_quantile_departemental(table_reserve_synthetique):
    # CONTEXT.md « Repli » : la dégradation reste visible, mais la commune en
    # repli participe bien au calcul du quantile communal de son département
    # (jamais exclue silencieusement).
    large = agreger_reserve_commune(table_reserve_synthetique, n_quantiles=3)
    ligne_repli = large.filter(pl.col("code_commune") == "69456")
    assert ligne_repli.get_column("quantile_reserve_gauche_dep")[0] is not None


def test_agreger_reserve_commune_somme_les_bureaux_stables(table_reserve_synthetique):
    large = agreger_reserve_commune(table_reserve_synthetique, n_quantiles=3)
    ligne = large.filter(pl.col("code_commune") == "69777")
    assert ligne.height == 1
    # Gauche : bureau1 (150*0.4/150*20/100=0.2)=150*0.2667*0.2 ... calcul direct via somme des réserves des 2 bureaux.
    b1 = table_reserve_synthetique.filter((pl.col("unite_id") == "69777_0001") & (pl.col("bloc") == "Gauche")).get_column("reserve")[0]
    b2 = table_reserve_synthetique.filter((pl.col("unite_id") == "69777_0002") & (pl.col("bloc") == "Gauche")).get_column("reserve")[0]
    assert ligne.get_column("reserve_gauche")[0] == pytest.approx(b1 + b2)
    # bureau1 : inscrits=150, abstention=40/150, part Gauche=20/100=0.2 -> 8.0 ;
    # bureau2 : inscrits=100, abstention=25/100, part Gauche=10/50=0.2 -> 5.0.
    assert ligne.get_column("reserve_gauche")[0] == pytest.approx(13.0)
    assert ligne.get_column("degrade")[0] is False


def test_agreger_reserve_commune_repli_reste_visible_et_degrade(table_reserve_synthetique):
    large = agreger_reserve_commune(table_reserve_synthetique, n_quantiles=3)
    ligne = large.filter(pl.col("code_commune") == "69456")
    assert ligne.height == 1
    assert ligne.get_column("degrade")[0] is True
    assert ligne.get_column("statut")[0] == "repli"


def test_agreger_reserve_commune_couvre_toute_la_france_bureau_et_repli(table_reserve_synthetique):
    large = agreger_reserve_commune(table_reserve_synthetique, n_quantiles=3)
    communes = set(large.get_column("code_commune").to_list())
    assert communes == {"69123", "69777", "69456"}


# --- preparer_carte_rapport_force -----------------------------------------------


def _baseline_synthetique() -> pl.DataFrame:
    return pl.DataFrame(
        [
            {"unite_id": "a", "bloc": "Gauche", "composite": 10.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "a", "bloc": "Droite", "composite": 5.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "b", "bloc": "Gauche", "composite": -8.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "b", "bloc": "Droite", "composite": 12.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "c", "bloc": "Gauche", "composite": 20.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "c", "bloc": "Droite", "composite": -20.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            # égalité exacte entre Droite et Gauche -> départage par bloc croissant ("Droite" < "Gauche").
            {"unite_id": "d", "bloc": "Gauche", "composite": 3.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            {"unite_id": "d", "bloc": "Droite", "composite": 3.0, "code_departement": "69", "statut": "joint_valide", "maille": "bureau"},
            # commune en repli : composite déjà à cette maille, jamais recalculé ici.
            {"unite_id": "69456", "bloc": "Gauche", "composite": 1.0, "code_departement": "69", "statut": "repli", "maille": "commune"},
            {"unite_id": "69456", "bloc": "Droite", "composite": -1.0, "code_departement": "69", "statut": "repli", "maille": "commune"},
        ]
    )


def test_preparer_carte_rapport_force_choisit_le_bloc_au_composite_maximal():
    resultat = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    tete = dict(zip(resultat.get_column("unite_id").to_list(), resultat.get_column("bloc_tete_projete").to_list()))
    assert tete["a"] == "Gauche"
    assert tete["b"] == "Droite"
    assert tete["c"] == "Gauche"


def test_preparer_carte_rapport_force_departage_les_egalites_par_bloc_croissant():
    resultat = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    ligne = resultat.filter(pl.col("unite_id") == "d")
    assert ligne.get_column("bloc_tete_projete")[0] == "Droite"


def test_preparer_carte_rapport_force_quantile_calcule_sur_le_bloc_gagnant_uniquement():
    resultat = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    # "c" gagne avec Gauche=20.0, le plus fort de la distribution Gauche (10, -8, 20, 3) -> quantile max (4).
    ligne_c = resultat.filter(pl.col("unite_id") == "c")
    assert ligne_c.get_column("quantile_rapport_force")[0] == 4


def test_preparer_carte_rapport_force_conserve_le_statut_et_la_maille_du_repli():
    resultat = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    ligne = resultat.filter(pl.col("unite_id") == "69456")
    assert ligne.get_column("bloc_tete_projete")[0] == "Gauche"
    assert ligne.get_column("statut")[0] == "repli"
    assert ligne.get_column("maille")[0] == "commune"


def test_preparer_carte_rapport_force_est_deterministe():
    a = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    b = preparer_carte_rapport_force(_baseline_synthetique(), n_quantiles=4)
    assert a.equals(b)


# --- assembler_donnees_bureau / assembler_donnees_commune -----------------------


def test_assembler_donnees_bureau_joint_reserve_et_rapport_de_force(panel_et_baseline_synthetiques, table_reserve_synthetique):
    _, baseline = panel_et_baseline_synthetiques
    donnees = assembler_donnees_bureau(table_reserve_synthetique, baseline)
    ligne = donnees.filter(pl.col("unite_id") == "69123_0001")
    assert ligne.height == 1
    assert ligne.get_column("reserve_gauche")[0] is not None
    # Le composite est un écart au NATIONAL (pas la part brute) : seule
    # l'appartenance à un bloc connu est vérifiée ici, pas la direction --
    # `preparer_carte_rapport_force` (testé séparément) couvre le calcul exact.
    assert ligne.get_column("bloc_tete_projete")[0] in ("Gauche", "Droite")
    assert ligne.get_column("quantile_rapport_force")[0] is not None


def test_assembler_donnees_bureau_exclut_les_communes_en_repli(panel_et_baseline_synthetiques, table_reserve_synthetique):
    _, baseline = panel_et_baseline_synthetiques
    donnees = assembler_donnees_bureau(table_reserve_synthetique, baseline)
    assert donnees.filter(pl.col("unite_id") == "69456").height == 0


def test_assembler_donnees_commune_attache_le_rapport_de_force_du_repli_seulement(
    panel_et_baseline_synthetiques, table_reserve_synthetique
):
    _, baseline = panel_et_baseline_synthetiques
    donnees = assembler_donnees_commune(table_reserve_synthetique, baseline)
    ligne_repli = donnees.filter(pl.col("code_commune") == "69456")
    assert ligne_repli.get_column("bloc_tete_projete")[0] is not None

    ligne_dezoom = donnees.filter(pl.col("code_commune") == "69777")
    # Pas de rapport de force agrégé pour une commune stable dézoomée (limitation documentée).
    assert ligne_dezoom.get_column("bloc_tete_projete")[0] is None


# --- construire_donnees_mobilisation : gate mécanique ---------------------------


def test_construire_donnees_mobilisation_leve_si_verdict_rouge(panel_et_baseline_synthetiques):
    # Le panel synthétique minuscule échoue nécessairement la garde anti-hasard
    # (trop peu d'unités pour battre un prédicteur département) -- même
    # situation que l'extrait gelé réel (cf. tests/test_reserve.py).
    panel, baseline = panel_et_baseline_synthetiques
    with pytest.raises(RuntimeError, match="[Vv]erdict"):
        construire_donnees_mobilisation(panel, baseline)


def test_construire_donnees_mobilisation_assemble_si_verdict_force_vert(monkeypatch, panel_et_baseline_synthetiques):
    import projections.mobilisation as mobilisation

    panel, baseline = panel_et_baseline_synthetiques

    appel_original = mobilisation.generer_rapport_complet

    def _force_pass(*args, **kwargs):
        sortie = appel_original(*args, **kwargs)
        return {**sortie, "pass_carte_mobilisation": True}

    monkeypatch.setattr(mobilisation, "generer_rapport_complet", _force_pass)

    resultat = construire_donnees_mobilisation(panel, baseline)
    assert resultat["pass_carte_mobilisation"] is True
    assert resultat["donnees_bureau"].height > 0
    assert resultat["donnees_commune"].height > 0

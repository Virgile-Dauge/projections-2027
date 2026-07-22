"""Tests de la baseline composite + dérive (issue #5, HANDOFF.md étape 1).

Vocabulaire du glossaire (CONTEXT.md) : la baseline est un indice partisan par
unité x bloc (Cook PVI français) -- structure spatiale relative (écart au national),
jamais le niveau brut. « Unité » = bureau (id_bv) si la commune est stable
(statut `joint_valide`, churn.py), commune (`code_commune`) si elle est en repli.

Deux familles de tests :
- des tests unitaires sur de petits DataFrame synthétiques, un par fonction pure,
  vérifiant les propriétés mathématiques garanties (somme à zéro, jamais de
  moyenne de %, imputation vs valeur intacte, dégénérescence médiane à 3) ;
- un test d'intégration sur l'extrait réel gelé (tests/fixtures/*.parquet) qui
  traverse tout `construire_baseline`.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.baseline import (
    POIDS_PAR_DEFAUT,
    SCRUTIN_EUROPEENNES,
    SCRUTIN_LEGISLATIVES,
    SCRUTIN_LEGISLATIVES_CORRIGE,
    SCRUTIN_PRESIDENTIELLE,
    calculer_derive,
    calculer_ecart_national,
    composite_moyenne_tronquee,
    composite_pondere,
    construire_baseline,
    corriger_offre_legislatives,
    main,
)
from projections.churn import classifier_communes, construire_panel_avec_statut
from projections.ingest import ingest

FIXTURES = Path(__file__).parent / "fixtures"


# --- Fixtures pytest ---------------------------------------------------------


@pytest.fixture(scope="session")
def panel_avec_statut_reel() -> pl.DataFrame:
    general = pl.read_parquet(FIXTURES / "general_results.parquet")
    candidats = pl.read_parquet(FIXTURES / "candidats_results.parquet")
    panel = ingest(general, candidats)
    classification = classifier_communes(panel)
    return construire_panel_avec_statut(panel, classification)


def _ligne(id_election, code_commune, code_bv, bloc, voix, exprimes, code_departement="69"):
    id_bv = f"{code_commune}_{code_bv}"
    return {
        "id_election": id_election,
        "code_departement": code_departement,
        "code_commune": code_commune,
        "code_bv": code_bv,
        "id_bv": id_bv,
        "bloc": bloc,
        "voix": voix,
        "inscrits": exprimes + 50,
        "abstentions": 10,
        "votants": exprimes + 20,
        "blancs": 10,
        "nuls": 10,
        "exprimes": exprimes,
        "statut": "joint_valide",
    }


def _panel(lignes: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(lignes)


# --- calculer_ecart_national : calcul depuis les voix, jamais une moyenne de % ---


def test_calculer_ecart_national_nul_quand_l_unite_reproduit_le_national():
    # Deux unités aux proportions identiques : le national est cette même
    # proportion, donc l'écart relatif est nul partout.
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 60, 100),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 40, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 6, 10),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 4, 10),
    ]
    resultat = calculer_ecart_national(_panel(lignes))
    assert resultat.get_column("ecart_national").to_list() == pytest.approx([0.0, 0.0, 0.0, 0.0])


def test_calculer_ecart_national_calcule_depuis_les_voix_pas_une_moyenne_de_pourcentages():
    # Deux unités de poids très différent (100 exprimés vs 10 000) : si le calcul
    # moyennait naïvement les % par unité, le national serait biaisé vers la
    # petite unité. Le national doit être pondéré par les voix (docs/heritage-2024.md).
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 50, 100),  # 50%, petite unité
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 50, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 9000, 10000),  # 90%, grosse unité
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 1000, 10000),
    ]
    resultat = calculer_ecart_national(_panel(lignes))
    # national Gauche = (50 + 9000) / (100 + 10000) = 0.895049...  (pas (0.5+0.9)/2 = 0.70)
    national_gauche = (50 + 9000) / (100 + 10000)
    ecart_petite_unite = resultat.filter(
        (pl.col("unite_id") == "69123_0001") & (pl.col("bloc") == "Gauche")
    ).get_column("ecart_national")[0]
    assert ecart_petite_unite == pytest.approx((0.5 - national_gauche) * 100)


def test_calculer_ecart_national_somme_a_zero_par_unite_si_offre_complete():
    # Propriété garantie par cette forme (écart en points des exprimés, Cook PVI) :
    # à offre complète (tous les blocs présents dans l'unité), la somme des écarts
    # sur les blocs d'une même unité est nulle -- les pct se partitionnent à 1 des
    # deux côtés de la soustraction. C'est précisément la propriété qui casse aux
    # législatives T1 en cas d'offre incomplète (raison d'être de la correction).
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 30, 100),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 70, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 500, 1000),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 500, 1000),
    ]
    resultat = calculer_ecart_national(_panel(lignes))
    par_unite = resultat.group_by("unite_id").agg(pl.col("ecart_national").sum().alias("somme"))
    assert par_unite.get_column("somme").to_list() == pytest.approx([0.0, 0.0])


def test_calculer_ecart_national_somme_ponderee_a_zero_sur_les_unites():
    # Pendant du test précédent côté national : la somme des écarts sur les
    # unités, pondérée par les exprimés de chaque unité, est nulle pour un bloc
    # donné -- le national est justement leur moyenne pondérée par construction.
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 30, 100),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 70, 100),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 700, 1000),
        _ligne("2022_pres_t1", "01001", "0001", "Droite", 300, 1000),
    ]
    resultat = calculer_ecart_national(_panel(lignes))
    gauche = resultat.filter(pl.col("bloc") == "Gauche")
    somme_ponderee = (gauche.get_column("ecart_national") * gauche.get_column("exprimes_unite")).sum()
    assert somme_ponderee == pytest.approx(0.0, abs=1e-6)


def test_calculer_ecart_national_exprimes_nul_donne_null_jamais_nan():
    # Cas réel observé sur les données complètes : une poignée de bureaux ont
    # exprimes=0 (bulletins tous nuls/blancs). voix/0 doit produire un écart
    # null (donnée absente), jamais NaN -- un NaN contaminerait silencieusement
    # le composite et la dérive en aval (ils savent ignorer les null, pas les NaN).
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 0, 0),
        _ligne("2022_pres_t1", "01001", "0001", "Gauche", 40, 100),
    ]
    resultat = calculer_ecart_national(_panel(lignes))
    ligne_nulle = resultat.filter(pl.col("unite_id") == "69123_0001")
    assert ligne_nulle.get_column("ecart_national").null_count() == 1
    assert not ligne_nulle.get_column("ecart_national").is_nan().any()


def test_calculer_ecart_national_filtre_sur_les_scrutins_demandes():
    lignes = [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 30, 100),
        _ligne("2024_euro_t1", "69123", "0001", "Gauche", 40, 100),
    ]
    resultat = calculer_ecart_national(_panel(lignes), scrutins=["2022_pres_t1"])
    assert resultat.get_column("id_election").unique().to_list() == ["2022_pres_t1"]


# --- corriger_offre_legislatives : imputation vs bloc intact -------------------


def _table_ecart_offre() -> pl.DataFrame:
    # 69123_0001 : offre complète aux législatives (Gauche + Extrême droite présents).
    # 01001_0001 : Extrême droite absente des législatives (pas de candidat) -- doit
    # être imputée depuis les européennes, jamais mise à zéro.
    return pl.DataFrame(
        {
            "id_election": [
                "2024_legi_t1", "2024_legi_t1",
                "2024_legi_t1",
                "2024_euro_t1", "2024_euro_t1",
                "2024_euro_t1", "2024_euro_t1",
            ],
            "unite_id": [
                "69123_0001", "69123_0001",
                "01001_0001",
                "69123_0001", "69123_0001",
                "01001_0001", "01001_0001",
            ],
            "bloc": [
                "Gauche", "Extrême droite",
                "Gauche",
                "Gauche", "Extrême droite",
                "Gauche", "Extrême droite",
            ],
            "ecart_national": [5.0, -3.0, 12.0, 7.0, -1.0, 9.0, 22.0],
        }
    )


def test_corriger_offre_legislatives_bloc_absent_impute_depuis_les_europeennes():
    corrige = corriger_offre_legislatives(_table_ecart_offre())
    ligne = corrige.filter((pl.col("unite_id") == "01001_0001") & (pl.col("bloc") == "Extrême droite"))
    assert ligne.height == 1
    assert ligne.get_column("ecart_national").to_list() == [22.0]  # valeur européenne, pas 0
    assert ligne.get_column("impute").to_list() == [True]


def test_corriger_offre_legislatives_bloc_present_reste_intact():
    corrige = corriger_offre_legislatives(_table_ecart_offre())
    ligne = corrige.filter((pl.col("unite_id") == "69123_0001") & (pl.col("bloc") == "Extrême droite"))
    assert ligne.get_column("ecart_national").to_list() == [-3.0]  # valeur législative d'origine
    assert ligne.get_column("impute").to_list() == [False]


def test_corriger_offre_legislatives_variante_exclusion_n_ajoute_aucune_ligne():
    # Analyse de sensibilité : au lieu d'imputer, on exclut le bloc de l'unité --
    # le composite (renormalisation des poids) s'en charge en aval.
    corrige = corriger_offre_legislatives(_table_ecart_offre(), methode="exclusion")
    manquant = corrige.filter((pl.col("unite_id") == "01001_0001") & (pl.col("bloc") == "Extrême droite"))
    assert manquant.height == 0
    assert corrige.get_column("impute").unique().to_list() == [False]


def test_corriger_offre_legislatives_methode_inconnue_leve_une_erreur():
    with pytest.raises(ValueError, match="méthode inconnue"):
        corriger_offre_legislatives(_table_ecart_offre(), methode="n_importe_quoi")


# --- composite_pondere : pondérations paramétrables -----------------------------


def _table_composantes() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "unite_id": ["u1"],
            "bloc": ["Extrême droite"],
            f"ecart_{SCRUTIN_PRESIDENTIELLE}": [10.0],
            f"ecart_{SCRUTIN_EUROPEENNES}": [30.0],
            f"ecart_{SCRUTIN_LEGISLATIVES}_corrige": [50.0],
        }
    )


def test_composite_pondere_poids_par_defaut():
    resultat = composite_pondere(_table_composantes())
    attendu = 10.0 * 0.5 + 30.0 * 0.25 + 50.0 * 0.25
    assert resultat.get_column("composite").to_list() == pytest.approx([attendu])


def test_composite_pondere_poids_parametrables_changent_le_resultat():
    # Poids 100% sur une seule composante : le composite doit reproduire
    # exactement cette composante -- preuve que les poids sont effectifs, pas
    # des constantes enfouies.
    poids_tout_sur_pres = {
        SCRUTIN_PRESIDENTIELLE: 1.0,
        SCRUTIN_EUROPEENNES: 0.0,
        f"{SCRUTIN_LEGISLATIVES}_corrige": 0.0,
    }
    resultat = composite_pondere(_table_composantes(), poids=poids_tout_sur_pres)
    assert resultat.get_column("composite").to_list() == pytest.approx([10.0])


def test_composite_pondere_par_defaut_somme_a_un():
    assert sum(POIDS_PAR_DEFAUT.values()) == pytest.approx(1.0)


def test_composite_pondere_renormalise_sur_les_composantes_presentes():
    # Variante 'exclusion' : une composante peut être absente (null) pour une
    # unité x bloc donnée -- le composite renormalise les poids sur ce qui reste,
    # au lieu de traiter le null comme un zéro.
    table = pl.DataFrame(
        {
            "unite_id": ["u1"],
            "bloc": ["Extrême droite"],
            f"ecart_{SCRUTIN_PRESIDENTIELLE}": [10.0],
            f"ecart_{SCRUTIN_EUROPEENNES}": [30.0],
            f"ecart_{SCRUTIN_LEGISLATIVES}_corrige": [None],
        }
    )
    resultat = composite_pondere(table)
    attendu = (10.0 * 0.5 + 30.0 * 0.25) / (0.5 + 0.25)
    assert resultat.get_column("composite").to_list() == pytest.approx([attendu])


# --- composite_moyenne_tronquee : dégénérescence en médiane à 3 composantes ----


def test_composite_moyenne_tronquee_egale_la_mediane_a_3_composantes():
    resultat = composite_moyenne_tronquee(_table_composantes())
    # valeurs 10 / 30 / 50 triées -> médiane 30.
    assert resultat.get_column("composite_tronque").to_list() == pytest.approx([30.0])


def test_composite_moyenne_tronquee_ignore_les_composantes_absentes():
    table = pl.DataFrame(
        {
            "unite_id": ["u1"],
            "bloc": ["Extrême droite"],
            f"ecart_{SCRUTIN_PRESIDENTIELLE}": [10.0],
            f"ecart_{SCRUTIN_EUROPEENNES}": [30.0],
            f"ecart_{SCRUTIN_LEGISLATIVES}_corrige": [None],
        }
    )
    resultat = composite_moyenne_tronquee(table)
    # 2 valeurs restantes (10, 30) -> médiane = leur moyenne = 20.
    assert resultat.get_column("composite_tronque").to_list() == pytest.approx([20.0])


# --- calculer_derive : cas synthétique connu ------------------------------------


def test_calculer_derive_cas_synthetique_connu():
    resultat = calculer_derive(_table_composantes())
    # derive = moyenne(30, 50) - 10 = 40 - 10 = 30 : le bloc progresse de 30 points
    # entre 2022 et la structure 2024 dans cette unité.
    assert resultat.get_column("derive").to_list() == pytest.approx([30.0])


def test_calculer_derive_nulle_si_structure_2024_egale_a_2022():
    table = pl.DataFrame(
        {
            "unite_id": ["u1"],
            "bloc": ["Gauche"],
            f"ecart_{SCRUTIN_PRESIDENTIELLE}": [15.0],
            f"ecart_{SCRUTIN_EUROPEENNES}": [15.0],
            f"ecart_{SCRUTIN_LEGISLATIVES}_corrige": [15.0],
        }
    )
    resultat = calculer_derive(table)
    assert resultat.get_column("derive").to_list() == pytest.approx([0.0])


# --- construire_baseline : intégration sur l'extrait réel gelé -----------------


def test_construire_baseline_colonnes_attendues(panel_avec_statut_reel):
    baseline = construire_baseline(panel_avec_statut_reel)
    colonnes_attendues = {
        "unite_id",
        "bloc",
        f"ecart_{SCRUTIN_PRESIDENTIELLE}",
        f"ecart_{SCRUTIN_EUROPEENNES}",
        f"ecart_{SCRUTIN_LEGISLATIVES}_corrige",
        "composite",
        "composite_tronque",
        "derive",
        "statut",
        "maille",
        "code_departement",
    }
    assert colonnes_attendues <= set(baseline.columns)
    assert baseline.height > 0


def test_construire_baseline_jamais_de_nan(panel_avec_statut_reel):
    # Régression : voix/0 (bureaux à exprimes=0) et division par un poids
    # disponible nul doivent produire des null, jamais des NaN qui passeraient
    # silencieusement à travers les null_count() de contrôle.
    baseline = construire_baseline(panel_avec_statut_reel)
    for colonne in ("composite", "composite_tronque", "derive"):
        assert baseline.get_column(colonne).is_nan().sum() == 0


def test_construire_baseline_maille_coherente_avec_le_statut(panel_avec_statut_reel):
    baseline = construire_baseline(panel_avec_statut_reel)
    incoherent = baseline.filter(
        ((pl.col("statut") == "joint_valide") & (pl.col("maille") != "bureau"))
        | ((pl.col("statut") == "repli") & (pl.col("maille") != "commune"))
    )
    assert incoherent.height == 0


def test_construire_baseline_poids_parametrables_de_bout_en_bout(panel_avec_statut_reel):
    poids_tout_sur_pres = {
        SCRUTIN_PRESIDENTIELLE: 1.0,
        SCRUTIN_EUROPEENNES: 0.0,
        SCRUTIN_LEGISLATIVES_CORRIGE: 0.0,
    }
    baseline = construire_baseline(panel_avec_statut_reel, poids=poids_tout_sur_pres)
    # Là où ecart_2022_pres_t1 est renseigné, le composite (100% sur cette
    # composante) doit lui être rigoureusement égal.
    comparable = baseline.filter(pl.col(f"ecart_{SCRUTIN_PRESIDENTIELLE}").is_not_null())
    assert comparable.get_column("composite").to_list() == pytest.approx(
        comparable.get_column(f"ecart_{SCRUTIN_PRESIDENTIELLE}").to_list()
    )


# --- Entrée console `uv run baseline` -------------------------------------------


def test_main_ecrit_la_baseline_en_parquet(tmp_path, monkeypatch, panel_avec_statut_reel):
    # panel_avec_statut n'est pas committé sous cette forme dans tests/fixtures/
    # (seuls les Parquet ingest bruts le sont) : on l'écrit dans tmp_path plutôt
    # que dans le dépôt.
    panel_in = tmp_path / "panel_avec_statut.parquet"
    sortie = tmp_path / "baseline.parquet"
    panel_avec_statut_reel.write_parquet(panel_in)
    monkeypatch.setattr(
        "sys.argv",
        ["baseline", "--panel", str(panel_in), "--out", str(sortie)],
    )
    main()
    assert sortie.exists()
    baseline = pl.read_parquet(sortie)
    assert baseline.height > 0

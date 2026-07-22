"""Tests de l'estimateur v1 de la réserve de voix par bureau × bloc (issue #25, ADR 0002).

Trois familles de tests :
- formule sur cas synthétiques (ordres de grandeur, bornes, dédup participation
  avant produit, invariance à 2024 -- même esprit anti-fuite que #6/#24) ;
- statut de réconciliation propagé jusqu'à la sortie (commune en repli -> réserve
  à la maille communale, jamais déguisée en maille bureau) ;
- intégration sur l'extrait réel gelé (tests/fixtures/*.parquet), qui traverse
  tout `generer_rapport_complet` (verrou CLI <-> notebook, comme #24/PR #27).
"""

from pathlib import Path

import polars as pl
import pytest

from projections.reserve import (
    METHODE_PART_DEFAUT,
    METHODES_PART_H1,
    SCRUTIN_REFERENCE,
    agreger_reserve_par_departement,
    calculer_donnees_reserve,
    construire_table_reserve,
    generer_rapport_complet,
    generer_rapport_reserve,
    lift_reserve_bureau_vs_departement,
    main,
    part_proportionnelle_aux_votants,
    part_uniforme_entre_blocs,
    sensibilite_h1,
    top_gisements_bureau,
    top_gisements_departement,
)
from projections.baseline import construire_baseline
from projections.churn import STATUT_JOINT_VALIDE, STATUT_REPLI, classifier_communes, construire_panel_avec_statut
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


@pytest.fixture(scope="session")
def baseline_reel(panel_avec_statut_reel: pl.DataFrame) -> pl.DataFrame:
    return construire_baseline(panel_avec_statut_reel)


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


def _panel(lignes: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(lignes)


def _panel_avec_baseline(lignes: list[dict]) -> tuple[pl.DataFrame, pl.DataFrame]:
    panel_brut = _panel(lignes)
    classification = classifier_communes(panel_brut)
    panel = construire_panel_avec_statut(panel_brut, classification)
    baseline = construire_baseline(panel)
    return panel, baseline


def _panel_synthetique_simple() -> list[dict]:
    # Une seule commune stable (bureau 0001), 2 blocs au 2022_pres_t1 : Gauche
    # 30/100 exprimés (30%), Droite 70/100 (70%) -- inscrits=200, abstentions=60
    # (taux 30%). Les 2024 sont présents (offre complète) pour ne pas casser
    # `classifier_communes` (4 scrutins sources requis pour être "stable").
    return [
        _ligne("2022_pres_t1", "69123", "0001", "Gauche", 30, 100, abstentions=60, inscrits=200),
        _ligne("2022_pres_t1", "69123", "0001", "Droite", 70, 100, abstentions=60, inscrits=200),
        _ligne("2022_legi_t1", "69123", "0001", "Gauche", 30, 100, abstentions=60, inscrits=200),
        _ligne("2022_legi_t1", "69123", "0001", "Droite", 70, 100, abstentions=60, inscrits=200),
        _ligne("2024_euro_t1", "69123", "0001", "Gauche", 30, 100, abstentions=60, inscrits=200),
        _ligne("2024_euro_t1", "69123", "0001", "Droite", 70, 100, abstentions=60, inscrits=200),
        _ligne("2024_legi_t1", "69123", "0001", "Gauche", 30, 100, abstentions=60, inscrits=200),
        _ligne("2024_legi_t1", "69123", "0001", "Droite", 70, 100, abstentions=60, inscrits=200),
    ]


# --- Formule v1 : cas synthétique ---------------------------------------------


def test_construire_table_reserve_formule_exacte_proportionnelle():
    panel, baseline = _panel_avec_baseline(_panel_synthetique_simple())
    table = construire_table_reserve(panel, baseline, methode_part="proportionnelle_aux_votants")

    ligne_gauche = table.filter((pl.col("unite_id") == "69123_0001") & (pl.col("bloc") == "Gauche"))
    # inscrits=200, taux_abstention=60/200=0.3, part_estimee (Gauche)=30/100=0.3
    # -> réserve = 200 * 0.3 * 0.3 = 18.0
    assert ligne_gauche.get_column("inscrits")[0] == 200
    assert ligne_gauche.get_column("taux_abstention")[0] == pytest.approx(0.3)
    assert ligne_gauche.get_column("part_estimee_bloc")[0] == pytest.approx(0.3)
    assert ligne_gauche.get_column("reserve")[0] == pytest.approx(18.0)

    ligne_droite = table.filter((pl.col("unite_id") == "69123_0001") & (pl.col("bloc") == "Droite"))
    # part_estimee (Droite) = 70/100 = 0.7 -> réserve = 200 * 0.3 * 0.7 = 42.0
    assert ligne_droite.get_column("reserve")[0] == pytest.approx(42.0)


def test_construire_table_reserve_bornes_jamais_negative_jamais_superieure_aux_inscrits():
    panel, baseline = _panel_avec_baseline(_panel_synthetique_simple())
    table = construire_table_reserve(panel, baseline)
    reserve = table.get_column("reserve")
    inscrits = table.get_column("inscrits")
    assert (reserve >= 0).all()
    assert (reserve <= inscrits).all()


def test_construire_table_reserve_deduplique_la_participation_avant_le_produit():
    # 2 lignes de bloc pour le même bureau x scrutin (abstentions/inscrits
    # répétés à l'identique sur chaque ligne, cf. projections.ingest) : la
    # réserve totale (somme des 2 blocs) ne doit pas dépasser les abstentions
    # réelles du bureau -- une participation additionnée par erreur (pas
    # dédupliquée) doublerait ce total.
    panel, baseline = _panel_avec_baseline(_panel_synthetique_simple())
    table = construire_table_reserve(panel, baseline)
    total_reserve = table.filter(pl.col("unite_id") == "69123_0001").get_column("reserve").sum()
    abstentions_reelles = 60.0
    assert total_reserve == pytest.approx(abstentions_reelles)  # 18 + 42 = 60, jamais 120


def test_construire_table_reserve_invariant_si_2024_change():
    # Anti-fuite (même esprit que #6/#24) : la réserve ne dépend que du scrutin
    # de référence (présidentielle 2022 T1) -- changer les scrutins 2024 (même
    # très différemment) ne doit rien changer à la table réserve.
    lignes_a = _panel_synthetique_simple()
    lignes_b = [dict(ligne) for ligne in lignes_a]
    for ligne in lignes_b:
        if ligne["id_election"] == "2024_euro_t1" and ligne["bloc"] == "Gauche":
            ligne["voix"] = 99
        if ligne["id_election"] == "2024_euro_t1" and ligne["bloc"] == "Droite":
            ligne["voix"] = 1
    panel_a, baseline_a = _panel_avec_baseline(lignes_a)
    panel_b, baseline_b = _panel_avec_baseline(lignes_b)
    table_a = construire_table_reserve(panel_a, baseline_a)
    table_b = construire_table_reserve(panel_b, baseline_b)
    assert table_a.sort(["unite_id", "bloc"]).equals(table_b.sort(["unite_id", "bloc"]))


def test_part_uniforme_entre_blocs_repartit_egalement():
    panel, _ = _panel_avec_baseline(_panel_synthetique_simple())
    part = part_uniforme_entre_blocs(panel)
    # 2 blocs présents au 2022_pres_t1 pour cette unité -> 1/2 chacun.
    valeurs = part.filter(pl.col("unite_id") == "69123_0001").get_column("part_estimee_bloc").to_list()
    assert valeurs == pytest.approx([0.5, 0.5])


def test_part_proportionnelle_aux_votants_egale_le_pct_reel():
    panel, _ = _panel_avec_baseline(_panel_synthetique_simple())
    part = part_proportionnelle_aux_votants(panel)
    gauche = part.filter((pl.col("unite_id") == "69123_0001") & (pl.col("bloc") == "Gauche"))
    assert gauche.get_column("part_estimee_bloc")[0] == pytest.approx(0.3)


# --- Statut de réconciliation propagé : commune en repli -> maille communale --


def _panel_avec_une_commune_en_repli() -> list[dict]:
    # 69123 : 1 bureau sur les 4 scrutins sources -> stable, joint_valide.
    # 69456 : 2 bureaux à la présidentielle, 1 seul aux législatives 2024 ->
    # instable -> repli communal classique (pas dans COMMUNES_RECONCILIATION_BUREAU).
    lignes = list(_panel_synthetique_simple())
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
        # Un seul bureau aux législatives 2024 -> nb_bureaux change -> instable.
        _ligne("2024_legi_t1", "69456", "0003", "Gauche", 15, 90, abstentions=35, inscrits=180),
        _ligne("2024_legi_t1", "69456", "0003", "Droite", 75, 90, abstentions=35, inscrits=180),
    ]
    return lignes


def test_construire_table_reserve_commune_en_repli_donne_une_reserve_a_la_maille_communale():
    panel, baseline = _panel_avec_baseline(_panel_avec_une_commune_en_repli())
    table = construire_table_reserve(panel, baseline)

    ligne_repli = table.filter(pl.col("unite_id") == "69456")
    assert ligne_repli.height > 0
    assert (ligne_repli.get_column("statut") == STATUT_REPLI).all()
    assert (ligne_repli.get_column("maille") == "commune").all()

    ligne_stable = table.filter(pl.col("unite_id") == "69123_0001")
    assert (ligne_stable.get_column("statut") == STATUT_JOINT_VALIDE).all()
    assert (ligne_stable.get_column("maille") == "bureau").all()

    # Jamais d'état silencieux : chaque ligne porte un statut explicite.
    assert table.get_column("statut").null_count() == 0


def test_construire_table_reserve_repli_agrege_les_2_bureaux_par_sommes():
    # 69456 en repli : inscrits présidentielle 2022 = 100 + 80 = 180, abstentions
    # = 20 + 15 = 35 -- sommés, jamais moyennés (CLAUDE.md « Never average »).
    panel, baseline = _panel_avec_baseline(_panel_avec_une_commune_en_repli())
    table = construire_table_reserve(panel, baseline)
    ligne = table.filter(pl.col("unite_id") == "69456").unique(subset=["unite_id"])
    assert ligne.get_column("inscrits")[0] == pytest.approx(180)
    assert ligne.get_column("abstentions")[0] == pytest.approx(35)


# --- Sensibilité H1 : les variantes changent le classement quand H1 varie fort


def _panel_sensibilite_h1() -> list[dict]:
    # 3 bureaux d'une même commune stable, structure très hétérogène en
    # présidentielle 2022 : proportionnelle et uniforme (2 blocs -> 50/50)
    # doivent donner un TOP 1 différent pour "Droite" (uniforme ignore la
    # structure : les 3 bureaux sont à égalité à 50%, donc le gisement le
    # plus gros est piloté par l'abstention seule -- b3 a la plus grosse
    # abstention -- alors que la proportionnelle privilégie b1, très favorable
    # à Droite en part relative malgré une abstention plus faible).
    lignes = []
    donnees = [
        ("0001", 95, 5, 40, 100, 20),  # b1 : Droite 95% des exprimés, faible abstention
        ("0002", 50, 50, 40, 100, 20),  # b2 : 50/50, abstention moyenne
        ("0003", 5, 95, 40, 100, 90),  # b3 : Droite 5%, abstention énorme
    ]
    for code_bv, droite, gauche, exprimes_ignore, inscrits, abstentions in donnees:
        for id_election in ("2022_pres_t1", "2022_legi_t1", "2024_euro_t1", "2024_legi_t1"):
            lignes.append(
                _ligne(id_election, "69999", code_bv, "Droite", droite, droite + gauche, abstentions=abstentions, inscrits=inscrits)
            )
            lignes.append(
                _ligne(id_election, "69999", code_bv, "Gauche", gauche, droite + gauche, abstentions=abstentions, inscrits=inscrits)
            )
    return lignes


def test_sensibilite_h1_change_le_classement_quand_h1_varie_fortement():
    panel, baseline = _panel_avec_baseline(_panel_sensibilite_h1())
    table_proportionnelle = construire_table_reserve(panel, baseline, methode_part="proportionnelle_aux_votants")
    table_uniforme = construire_table_reserve(panel, baseline, methode_part="uniforme_entre_blocs")

    top_proportionnelle = (
        table_proportionnelle.filter(pl.col("bloc") == "Droite").sort("reserve", descending=True).get_column("unite_id")[0]
    )
    top_uniforme = (
        table_uniforme.filter(pl.col("bloc") == "Droite").sort("reserve", descending=True).get_column("unite_id")[0]
    )
    assert top_proportionnelle == "69999_0001"
    assert top_uniforme == "69999_0003"
    assert top_proportionnelle != top_uniforme


def test_sensibilite_h1_rapporte_un_rho_et_un_recouvrement_par_bloc(panel_avec_statut_reel, baseline_reel):
    resultat = sensibilite_h1(panel_avec_statut_reel, baseline_reel, n_top=20)
    assert set(resultat.columns) >= {"bloc", "methode_reference", "methode_variante", "rho", "recouvrement_top_n", "n_top"}
    assert resultat.height > 0
    assert (resultat.get_column("recouvrement_top_n") >= 0).all()
    assert (resultat.get_column("recouvrement_top_n") <= 1).all()


# --- Méthodes H1 déclarées -----------------------------------------------------


def test_methodes_part_h1_contient_les_2_variantes_documentees():
    assert set(METHODES_PART_H1) == {"proportionnelle_aux_votants", "uniforme_entre_blocs"}
    assert METHODE_PART_DEFAUT == "proportionnelle_aux_votants"


def test_scrutin_reference_est_la_presidentielle_2022():
    assert SCRUTIN_REFERENCE == "2022_pres_t1"


# --- Intégration réelle --------------------------------------------------------


def test_construire_table_reserve_colonnes_attendues(panel_avec_statut_reel, baseline_reel):
    table = construire_table_reserve(panel_avec_statut_reel, baseline_reel)
    colonnes_attendues = {
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
    }
    assert colonnes_attendues <= set(table.columns)
    assert table.height > 0
    assert table.get_column("statut").null_count() == 0


def test_top_gisements_bureau_est_trie_par_reserve_decroissante_par_bloc(panel_avec_statut_reel, baseline_reel):
    table = construire_table_reserve(panel_avec_statut_reel, baseline_reel)
    top = top_gisements_bureau(table, n=10)
    for bloc in top.get_column("bloc").unique().to_list():
        valeurs = top.filter(pl.col("bloc") == bloc).get_column("reserve").to_list()
        assert valeurs == sorted(valeurs, reverse=True)
        assert len(valeurs) <= 10


def test_agreger_reserve_par_departement_est_une_somme_jamais_une_moyenne(panel_avec_statut_reel, baseline_reel):
    table = construire_table_reserve(panel_avec_statut_reel, baseline_reel)
    agrege = agreger_reserve_par_departement(table)
    bloc = agrege.get_column("bloc")[0]
    departement = agrege.filter(pl.col("bloc") == bloc).get_column("code_departement")[0]
    attendu = table.filter((pl.col("bloc") == bloc) & (pl.col("code_departement") == departement)).get_column("reserve").sum()
    obtenu = agrege.filter((pl.col("bloc") == bloc) & (pl.col("code_departement") == departement)).get_column("reserve")[0]
    assert obtenu == pytest.approx(attendu)


def test_top_gisements_departement_par_bloc(panel_avec_statut_reel, baseline_reel):
    table = construire_table_reserve(panel_avec_statut_reel, baseline_reel)
    top = top_gisements_departement(table, n=5)
    for bloc in top.get_column("bloc").unique().to_list():
        assert top.filter(pl.col("bloc") == bloc).height <= 5


def test_lift_reserve_bureau_vs_departement_reutilise_la_garde_anti_hasard_24(panel_avec_statut_reel, baseline_reel):
    lift = lift_reserve_bureau_vs_departement(panel_avec_statut_reel, baseline_reel)
    assert "pass_global" in lift.columns
    assert "lift_vs_departement" in lift.columns
    assert "rho_hasard" in lift.columns


def test_generer_rapport_reserve_contient_les_sections_attendues(panel_avec_statut_reel, baseline_reel):
    donnees = calculer_donnees_reserve(panel_avec_statut_reel, baseline_reel)
    rapport = generer_rapport_reserve(donnees)
    for section in (
        "Réserve",
        "Statut de réconciliation",
        "Top gisements",
        "département",
        "Sensibilité",
        "Lift bureau",
        "non publiable",
    ):
        assert section in rapport


def test_generer_rapport_reserve_est_deterministe(panel_avec_statut_reel, baseline_reel):
    donnees = calculer_donnees_reserve(panel_avec_statut_reel, baseline_reel)
    rapport_1 = generer_rapport_reserve(donnees)
    rapport_2 = generer_rapport_reserve(donnees)
    assert rapport_1 == rapport_2


def test_generer_rapport_complet_identique_a_l_assemblage_manuel(panel_avec_statut_reel, baseline_reel):
    # Verrou CLI <-> notebook (même discipline que #24/PR #27).
    donnees = calculer_donnees_reserve(panel_avec_statut_reel, baseline_reel)
    attendu = generer_rapport_reserve(donnees)
    sortie = generer_rapport_complet(panel_avec_statut_reel, baseline_reel)
    assert sortie["rapport"] == attendu
    assert isinstance(sortie["pass_carte_mobilisation"], bool)
    assert sortie["table_reserve"].equals(donnees["table_reserve"])


def test_notebook_regenere_par_le_meme_chemin_que_le_cli():
    source = (Path(__file__).parent.parent / "notebooks" / "reserve_2027.py").read_text(encoding="utf-8")
    assert "generer_rapport_complet(" in source
    assert "generer_rapport_reserve(" not in source


def test_main_ecrit_le_rapport_et_la_table(tmp_path, monkeypatch, panel_avec_statut_reel, baseline_reel):
    panel_in = tmp_path / "panel_avec_statut.parquet"
    baseline_in = tmp_path / "baseline_unite_bloc.parquet"
    sortie = tmp_path / "reserve-2027.md"
    table_out = tmp_path / "reserve_bureau_bloc.parquet"
    panel_avec_statut_reel.write_parquet(panel_in)
    baseline_reel.write_parquet(baseline_in)
    monkeypatch.setattr(
        "sys.argv",
        [
            "reserve",
            "--panel",
            str(panel_in),
            "--baseline",
            str(baseline_in),
            "--out",
            str(sortie),
            "--table-out",
            str(table_out),
        ],
    )
    main()
    assert sortie.exists()
    assert table_out.exists()
    assert "Réserve" in sortie.read_text(encoding="utf-8")
    assert pl.read_parquet(table_out).height > 0

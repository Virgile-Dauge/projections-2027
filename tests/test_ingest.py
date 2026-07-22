"""Tests de l'ingestion des 4 scrutins sources vers la table longue bureau × scrutin × bloc.

Deux familles de tests :
- des tests unitaires sur de petits DataFrame synthétiques, un par fonction pure ;
- des tests d'intégration sur un extrait réel gelé (tests/fixtures/*.parquet,
  quelques communes des vrais Parquet source) qui traversent tout le pipeline
  `ingest()` et cassent si le schéma source change.

Note d'écart avec l'énoncé de l'issue : la source (`data/raw/elections/*.parquet`)
est déjà en format long et typée (voir docstring de `projections.ingest`) — pas de
`"12,5%"` à parser, pas de wide->long. Les tests ci-dessous couvrent donc
l'intention des critères d'acceptation (garde-fous d'agrégation, id_bv, nuances)
sur la forme réelle des données plutôt que sur un format ministère qui n'existe
plus dans cette source.
"""

from pathlib import Path

import polars as pl
import pytest

from projections.ingest import (
    NUANCE_VERS_BLOC,
    SCRUTINS_SOURCES,
    agreger_par_bloc,
    construire_id_bv,
    filtrer_scrutins_sources,
    ingest,
    joindre_participation,
    main,
    nuance_vers_bloc,
    resoudre_nuance_presidentielle,
)

FIXTURES = Path(__file__).parent / "fixtures"


# --- Fixtures pytest ---------------------------------------------------------


@pytest.fixture(scope="session")
def general_results_reel() -> pl.DataFrame:
    return pl.read_parquet(FIXTURES / "general_results.parquet")


@pytest.fixture(scope="session")
def candidats_results_reel() -> pl.DataFrame:
    return pl.read_parquet(FIXTURES / "candidats_results.parquet")


@pytest.fixture(scope="session")
def panel_reel(general_results_reel, candidats_results_reel) -> pl.DataFrame:
    return ingest(general_results_reel, candidats_results_reel)


# --- filtrer_scrutins_sources -------------------------------------------------


def test_filtrer_scrutins_sources_ne_garde_que_les_7_scrutins():
    df = pl.DataFrame({"id_election": ["2022_pres_t1", "2017_pres_t1", "2024_legi_t1"]})
    resultat = filtrer_scrutins_sources(df)
    assert resultat.get_column("id_election").to_list() == ["2022_pres_t1", "2024_legi_t1"]


def test_scrutins_sources_couvre_les_4_scrutins_en_7_identifiants():
    assert len(SCRUTINS_SOURCES) == 7
    assert len(set(SCRUTINS_SOURCES)) == 7


# --- construire_id_bv ---------------------------------------------------------


def test_construire_id_bv_concatene_commune_et_bureau():
    df = pl.DataFrame({"code_commune": ["69123", "97133", "ZZ001"], "code_bv": ["0101", "0002", "0001"]})
    resultat = construire_id_bv(df)
    assert resultat.get_column("id_bv").to_list() == ["69123_0101", "97133_0002", "ZZ001_0001"]


def test_construire_id_bv_leve_une_erreur_si_code_commune_non_conforme():
    df = pl.DataFrame({"code_commune": ["691"], "code_bv": ["0001"]})
    with pytest.raises(ValueError, match="code_commune non conforme"):
        construire_id_bv(df)


# --- nuance_vers_bloc ----------------------------------------------------------


def test_nuance_vers_bloc_mappe_les_nuances_connues():
    df = pl.DataFrame({"nuance": ["RN", "FI", "LR", "ENS", "DIV"]})
    resultat = nuance_vers_bloc(df)
    assert resultat.get_column("bloc").to_list() == [
        "Extrême droite",
        "Gauche",
        "Droite",
        "Centre",
        "Divers",
    ]


def test_nuance_vers_bloc_fi_est_en_gauche_pas_en_extreme_gauche():
    # Garde-fou explicite : la colonne `bloc` de nuances-2026.csv classe FI en
    # EXG (extrême gauche). Notre classification (classification_en_blocs.md)
    # met FI en Gauche — ne jamais régresser dessus.
    df = pl.DataFrame({"nuance": ["FI"]})
    assert nuance_vers_bloc(df).get_column("bloc").to_list() == ["Gauche"]


def test_nuance_vers_bloc_leve_une_erreur_explicite_sur_nuance_inconnue():
    df = pl.DataFrame({"nuance": ["RN", "PIRATE"]})
    with pytest.raises(ValueError, match="PIRATE"):
        nuance_vers_bloc(df)


def test_nuance_vers_bloc_couvre_les_codes_herites_des_legislatives_2022():
    # Vérifiés sur le vrai Parquet : 2022_legi_t1/t2 emploient NUP/DXG/DXD là où
    # 2024 emploie UG/EXG/EXD.
    df = pl.DataFrame({"nuance": ["NUP", "DXG", "DXD"]})
    assert nuance_vers_bloc(df).get_column("bloc").to_list() == ["Gauche", "Gauche", "Extrême droite"]


def test_nuance_vers_bloc_couvre_les_nuances_de_liste_europeennes():
    df = pl.DataFrame({"nuance": ["LRN", "LFI", "LUG"]})
    assert nuance_vers_bloc(df).get_column("bloc").to_list() == ["Extrême droite", "Gauche", "Gauche"]


# --- resoudre_nuance_presidentielle --------------------------------------------


def test_resoudre_nuance_presidentielle_mappe_par_nom_de_candidat():
    df = pl.DataFrame({"nom": ["MACRON", "LE PEN"], "nuance": [None, None]})
    resultat = resoudre_nuance_presidentielle(df)
    assert resultat.get_column("nuance").to_list() == ["ENS", "RN"]


def test_resoudre_nuance_presidentielle_ne_touche_pas_une_nuance_deja_presente():
    df = pl.DataFrame({"nom": ["DUPONT"], "nuance": ["RN"]})
    resultat = resoudre_nuance_presidentielle(df)
    assert resultat.get_column("nuance").to_list() == ["RN"]


def test_candidat_presidentiel_inconnu_echoue_a_l_etape_nuance_vers_bloc():
    df = pl.DataFrame({"nom": ["INCONNU DU MAPPING"], "nuance": [None]})
    resolu = resoudre_nuance_presidentielle(df)
    with pytest.raises(ValueError, match="INCONNU DU MAPPING"):
        nuance_vers_bloc(resolu)


# --- agreger_par_bloc : agrégation par les voix, jamais par une moyenne -------


def test_agreger_par_bloc_somme_les_voix_du_meme_bloc():
    df = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1"] * 3,
            "code_departement": ["69"] * 3,
            "code_commune": ["69123"] * 3,
            "code_bv": ["0001"] * 3,
            "id_bv": ["69123_0001"] * 3,
            "bloc": ["Gauche", "Gauche", "Extrême droite"],
            "voix": [100, 50, 200],
        }
    )
    resultat = agreger_par_bloc(df).sort("bloc")
    assert resultat.get_column("voix").to_list() == [200, 150]
    assert resultat.get_column("bloc").to_list() == ["Extrême droite", "Gauche"]


# --- joindre_participation : aucun bureau perdu --------------------------------


def test_joindre_participation_ajoute_les_colonnes_de_participation():
    candidats_bloc = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1"],
            "code_departement": ["69"],
            "code_commune": ["69123"],
            "code_bv": ["0001"],
            "id_bv": ["69123_0001"],
            "bloc": ["Gauche"],
            "voix": [150],
        }
    )
    general = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1"],
            "id_bv": ["69123_0001"],
            "inscrits": [500],
            "abstentions": [100],
            "votants": [400],
            "blancs": [10],
            "nuls": [5],
            "exprimes": [385],
        }
    )
    resultat = joindre_participation(candidats_bloc, general)
    assert resultat.get_column("inscrits").to_list() == [500]
    assert resultat.get_column("exprimes").to_list() == [385]


def test_joindre_participation_ne_perd_aucun_bureau_meme_orphelin_d_un_cote():
    candidats_bloc = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1", "2024_legi_t1"],
            "code_departement": ["69", "01"],
            "code_commune": ["69123", "01001"],
            "code_bv": ["0001", "0001"],
            "id_bv": ["69123_0001", "01001_0001"],
            "bloc": ["Gauche", "Droite"],
            "voix": [150, 80],
        }
    )
    # général ne connaît que le bureau lyonnais : le bureau 01001_0001 (présent
    # côté candidats) ne doit pas disparaître de la sortie.
    general = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1"],
            "id_bv": ["69123_0001"],
            "inscrits": [500],
            "abstentions": [100],
            "votants": [400],
            "blancs": [10],
            "nuls": [5],
            "exprimes": [385],
        }
    )
    resultat = joindre_participation(candidats_bloc, general)
    assert set(resultat.get_column("id_bv").to_list()) == {"69123_0001", "01001_0001"}


# --- ingest() : colonnes requises ----------------------------------------------


def test_ingest_leve_une_erreur_claire_si_colonne_requise_absente():
    general = pl.DataFrame({"id_election": ["2024_legi_t1"]})  # colonnes manquantes
    candidats = pl.DataFrame(
        {
            "id_election": ["2024_legi_t1"],
            "code_commune": ["69123"],
            "code_bv": ["0001"],
            "voix": [100],
            "nuance": ["RN"],
            "nom": ["X"],
        }
    )
    with pytest.raises(ValueError, match="Colonnes manquantes"):
        ingest(general, candidats)


# --- Tests d'intégration sur l'extrait réel gelé --------------------------------


def test_panel_reel_a_les_7_scrutins_sources(panel_reel):
    assert set(panel_reel.get_column("id_election").unique().to_list()) == set(SCRUTINS_SOURCES)


def test_panel_reel_id_bv_conforme_au_glossaire(panel_reel):
    # id_bv = code INSEE commune 5 caractères + "_" + code bureau (CONTEXT.md).
    id_bv = panel_reel.get_column("id_bv")
    assert id_bv.str.contains(r"^[A-Z0-9]{5}_\d{4}$").all()


def test_panel_reel_aucune_nuance_inconnue(panel_reel):
    # Le pipeline complet a tourné sans lever d'erreur : implicite, mais on
    # vérifie explicitement qu'aucun bloc n'est resté nul.
    assert panel_reel.get_column("bloc").null_count() == 0
    assert set(panel_reel.get_column("bloc").drop_nulls().unique().to_list()) <= {
        "Gauche",
        "Centre",
        "Droite",
        "Extrême droite",
        "Divers",
    }


def test_panel_reel_agregation_par_bloc_egale_la_somme_des_voix_candidats(
    panel_reel, candidats_results_reel
):
    # Garde-fou anti-régression : jamais de moyenne de pourcentages, toujours une
    # somme de voix. On la vérifie en reconstruisant l'exprimé depuis panel_reel
    # et en le comparant à la somme des voix candidats du même bureau × scrutin.
    total_panel = (
        panel_reel.group_by(["id_election", "id_bv"])
        .agg(pl.col("voix").sum().alias("total_voix_blocs"))
        .sort(["id_election", "id_bv"])
    )
    total_candidats = (
        candidats_results_reel.filter(pl.col("id_election").is_in(SCRUTINS_SOURCES))
        .with_columns((pl.col("code_commune") + "_" + pl.col("code_bv")).alias("id_bv"))
        .group_by(["id_election", "id_bv"])
        .agg(pl.col("voix").sum().alias("total_voix_candidats"))
        .sort(["id_election", "id_bv"])
    )
    compare = total_panel.join(total_candidats, on=["id_election", "id_bv"])
    assert compare.height == total_candidats.height
    assert compare.get_column("total_voix_blocs").to_list() == compare.get_column(
        "total_voix_candidats"
    ).to_list()


def test_panel_reel_aucun_bureau_perdu_entre_candidats_et_sortie(panel_reel, candidats_results_reel):
    bureaux_candidats = (
        candidats_results_reel.filter(pl.col("id_election").is_in(SCRUTINS_SOURCES))
        .with_columns((pl.col("code_commune") + "_" + pl.col("code_bv")).alias("id_bv"))
        .select("id_election", "id_bv")
        .unique()
    )
    bureaux_panel = panel_reel.select("id_election", "id_bv").unique()
    manquants = bureaux_candidats.join(bureaux_panel, on=["id_election", "id_bv"], how="anti")
    assert manquants.height == 0


def test_panel_reel_contient_drom_et_etranger(panel_reel):
    ids_drom_etranger = panel_reel.filter(
        pl.col("code_commune").str.starts_with("97") | pl.col("code_commune").str.starts_with("ZZ")
    )
    communes = set(ids_drom_etranger.get_column("code_commune").unique().to_list())
    assert any(c.startswith("97") for c in communes), "aucune commune DOM dans le panel"
    assert any(c.startswith("ZZ") for c in communes), "aucun bureau de l'étranger dans le panel"


def test_panel_reel_participation_coherente(panel_reel):
    lignes = panel_reel.select("inscrits", "votants", "exprimes").unique()
    assert (lignes.get_column("inscrits") >= lignes.get_column("votants")).all()
    assert (lignes.get_column("votants") >= lignes.get_column("exprimes")).all()


# --- Entrée console `uv run ingest` --------------------------------------------


def test_main_ecrit_le_panel_en_parquet_a_partir_des_chemins_donnes(tmp_path, monkeypatch):
    sortie = tmp_path / "panel.parquet"
    monkeypatch.setattr(
        "sys.argv",
        [
            "ingest",
            "--general-results",
            str(FIXTURES / "general_results.parquet"),
            "--candidats-results",
            str(FIXTURES / "candidats_results.parquet"),
            "--out",
            str(sortie),
        ],
    )
    main()
    assert sortie.exists()
    panel = pl.read_parquet(sortie)
    assert set(panel.get_column("id_election").unique().to_list()) == set(SCRUTINS_SOURCES)


def test_toutes_les_nuances_reelles_de_la_fixture_sont_dans_le_mapping(candidats_results_reel):
    # Sécurité supplémentaire, indépendante du pipeline : toute nuance présente
    # dans l'extrait réel (hors présidentielle, résolue par nom) doit être connue.
    nuances_legi_euro = (
        candidats_results_reel.filter(
            pl.col("id_election").is_in(SCRUTINS_SOURCES) & pl.col("nuance").is_not_null()
        )
        .get_column("nuance")
        .unique()
        .to_list()
    )
    inconnues = sorted(set(nuances_legi_euro) - set(NUANCE_VERS_BLOC))
    assert inconnues == []

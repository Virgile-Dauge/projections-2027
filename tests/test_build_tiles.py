"""Tests du parseur GeoJSON en streaming et de la jointure contours <-> scores.

Fichiers minuscules (tests/fixtures ou tmp_path) : on ne teste jamais ici sur les
vraies données 615 Mo (voir docstring de `projections.build_tiles`), seulement la
logique du parseur et de la jointure par identifiant.
"""

import gzip
import json
from pathlib import Path

import polars as pl
import pytest

from projections.build_tiles import (
    BUREAUX_MAXZOOM,
    BUREAUX_MINZOOM,
    COMMUNES_MAXZOOM,
    RapportJointure,
    _iter_features_geojson,
    construire_pmtiles,
    joindre_bureaux,
    joindre_communes,
    joindre_mobilisation_bureaux,
    joindre_mobilisation_communes,
)

# --- _iter_features_geojson : parseur streaming --------------------------------


def _ecrire_geojson(chemin: Path, features: list[dict], avec_crs: bool = False) -> None:
    contenu: dict = {"type": "FeatureCollection"}
    if avec_crs:
        contenu["crs"] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}}
    contenu["features"] = features
    chemin.write_text(json.dumps(contenu), encoding="utf-8")


def test_iter_features_geojson_extrait_toutes_les_features(tmp_path):
    features = [
        {"type": "Feature", "properties": {"id": i}, "geometry": {"type": "Point", "coordinates": [0, 0]}}
        for i in range(5)
    ]
    chemin = tmp_path / "test.geojson"
    _ecrire_geojson(chemin, features)
    resultat = list(_iter_features_geojson(chemin))
    assert [f["properties"]["id"] for f in resultat] == [0, 1, 2, 3, 4]


def test_iter_features_geojson_gere_un_champ_crs_avant_features(tmp_path):
    features = [{"type": "Feature", "properties": {"id": "x"}, "geometry": {"type": "Point", "coordinates": [1, 2]}}]
    chemin = tmp_path / "test.geojson"
    _ecrire_geojson(chemin, features, avec_crs=True)
    resultat = list(_iter_features_geojson(chemin))
    assert len(resultat) == 1
    assert resultat[0]["properties"]["id"] == "x"


def test_iter_features_geojson_collection_vide(tmp_path):
    chemin = tmp_path / "vide.geojson"
    _ecrire_geojson(chemin, [])
    assert list(_iter_features_geojson(chemin)) == []


def test_iter_features_geojson_lit_par_petits_blocs_sans_couper_une_feature(tmp_path, monkeypatch):
    # Force des lectures de 16 octets pour vérifier que le tampon glissant
    # recolle correctement des objets Feature qui dépassent la taille du bloc.
    import projections.build_tiles as bt

    monkeypatch.setattr(bt, "_TAILLE_MORCEAU", 16)
    features = [
        {"type": "Feature", "properties": {"nom": "une feature assez longue pour dépasser 16 octets"}, "geometry": None}
        for _ in range(3)
    ]
    chemin = tmp_path / "test.geojson"
    _ecrire_geojson(chemin, features)
    resultat = list(_iter_features_geojson(chemin))
    assert len(resultat) == 3
    assert all(f["properties"]["nom"].startswith("une feature") for f in resultat)


# --- joindre_bureaux -------------------------------------------------------------


def _scores_bureau_synthetiques() -> pl.DataFrame:
    return pl.DataFrame(
        [
            {
                "id_bv": "69123_0001",
                "code_commune": "69123",
                "code_departement": "69",
                "bloc_tete": "Gauche",
                "pct_gauche": 55.0,
                "pct_centre": 10.0,
                "pct_droite": 15.0,
                "pct_extreme_droite": 15.0,
                "pct_divers": 5.0,
                "participation": 62.3,
                "inscrits": 1000,
                "exprimes": 700,
            },
            {
                "id_bv": "ZZ001_0001",  # bureau de l'étranger : jamais dans les contours REU.
                "code_commune": "ZZ001",
                "code_departement": "ZZ",
                "bloc_tete": "Centre",
                "pct_gauche": 20.0,
                "pct_centre": 50.0,
                "pct_droite": 20.0,
                "pct_extreme_droite": 5.0,
                "pct_divers": 5.0,
                "participation": 40.0,
                "inscrits": 500,
                "exprimes": 300,
            },
            {
                # bureau du panel absent des contours REU (churn/renumérotation) :
                # doit rester non joint, sans faire échouer la jointure.
                "id_bv": "69123_9999",
                "code_commune": "69123",
                "code_departement": "69",
                "bloc_tete": "Droite",
                "pct_gauche": 10.0,
                "pct_centre": 10.0,
                "pct_droite": 60.0,
                "pct_extreme_droite": 10.0,
                "pct_divers": 10.0,
                "participation": 50.0,
                "inscrits": 200,
                "exprimes": 100,
            },
        ]
    )


def _contours_bureaux_geojson() -> list[dict]:
    return [
        {
            "type": "Feature",
            "properties": {
                "codeDepartement": "69",
                "codeCommune": "69123",
                "nomCommune": "Lyon",
                "numeroBureauVote": "0001",
                "codeBureauVote": "69123_0001",
                "id_bv": "69123_1",  # champ REU natif, PAS le même format -> jamais utilisé pour joindre.
            },
            "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
        },
        {
            # contour orphelin : aucun score correspondant (ancien découpage).
            "type": "Feature",
            "properties": {
                "codeDepartement": "69",
                "codeCommune": "69123",
                "nomCommune": "Lyon",
                "numeroBureauVote": "0002",
                "codeBureauVote": "69123_0002",
            },
            "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
        },
    ]


def test_joindre_bureaux_joint_par_codeBureauVote_pas_par_le_champ_id_bv_reu(tmp_path):
    chemin_contours = tmp_path / "contours.geojson"
    _ecrire_geojson(chemin_contours, _contours_bureaux_geojson())
    sortie = tmp_path / "bureaux.ndjson"

    joindre_bureaux(chemin_contours, _scores_bureau_synthetiques(), sortie)

    lignes = sortie.read_text(encoding="utf-8").strip().splitlines()
    assert len(lignes) == 1
    feature = json.loads(lignes[0])
    assert feature["properties"]["id_bv"] == "69123_0001"
    assert feature["properties"]["bloc_tete"] == "Gauche"
    assert feature["properties"]["pct_gauche"] == 55.0
    assert feature["properties"]["commune"] == "Lyon"
    assert feature["tippecanoe"]["layer"] == "bureaux"


def test_joindre_bureaux_exclut_naturellement_l_etranger(tmp_path):
    # Le bureau ZZ001_0001 est dans les scores mais jamais dans les contours REU :
    # il ne doit pas compter comme "score joint".
    chemin_contours = tmp_path / "contours.geojson"
    _ecrire_geojson(chemin_contours, _contours_bureaux_geojson())
    sortie = tmp_path / "bureaux.ndjson"

    rapport = joindre_bureaux(chemin_contours, _scores_bureau_synthetiques(), sortie)

    # total_scores exclut déjà les ZZ (jamais candidats à un contour) :
    assert rapport.total_scores == 2  # 69123_0001 et 69123_9999
    assert rapport.scores_joints == 1  # seul 69123_0001 a trouvé un contour
    assert rapport.total_contours == 2
    assert rapport.contours_sans_score == 1  # 69123_0002 est orphelin


def test_rapport_jointure_taux_et_str():
    rapport = RapportJointure(
        nom_couche="bureaux", total_scores=2, scores_joints=1, total_contours=2, contours_sans_score=1
    )
    assert rapport.taux_scores_joints == pytest.approx(50.0)
    assert "bureaux" in str(rapport)
    assert "50.0" in str(rapport)


# --- joindre_communes -------------------------------------------------------------


def test_joindre_communes_joint_par_code_insee(tmp_path):
    communes_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"code": "69123", "nom": "Lyon", "departement": "69"},
                "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
            },
            {
                "type": "Feature",
                "properties": {"code": "01001", "nom": "Sans résultat", "departement": "01"},
                "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
            },
        ],
    }
    chemin = tmp_path / "communes.geojson.gz"
    with gzip.open(chemin, "wt", encoding="utf-8") as f:
        json.dump(communes_geojson, f)

    scores = pl.DataFrame(
        [
            {
                "code_commune": "69123",
                "code_departement": "69",
                "bloc_tete": "Gauche",
                "pct_gauche": 45.0,
                "pct_centre": 20.0,
                "pct_droite": 15.0,
                "pct_extreme_droite": 15.0,
                "pct_divers": 5.0,
                "participation": 60.0,
                "inscrits": 5000,
                "exprimes": 3500,
            }
        ]
    )
    sortie = tmp_path / "communes.ndjson"
    rapport = joindre_communes(chemin, scores, sortie)

    lignes = sortie.read_text(encoding="utf-8").strip().splitlines()
    assert len(lignes) == 1
    feature = json.loads(lignes[0])
    assert feature["properties"]["code_commune"] == "69123"
    assert feature["properties"]["commune"] == "Lyon"
    assert feature["tippecanoe"]["layer"] == "communes"
    assert rapport.total_contours == 2
    assert rapport.contours_sans_score == 1


# --- joindre_mobilisation_bureaux (issue #26) -----------------------------------


def _donnees_bureau_synthetiques() -> pl.DataFrame:
    def _ligne(unite_id, statut, bloc_tete, quantile_force, reserve_gauche=12.0, quantile_reserve_gauche=3):
        return {
            "unite_id": unite_id,
            "code_departement": "69",
            "statut": statut,
            "maille": "bureau",
            "reserve_gauche": reserve_gauche,
            "reserve_centre": None,
            "reserve_droite": 8.0,
            "reserve_extreme_droite": 5.0,
            "reserve_divers": None,
            "quantile_reserve_gauche": quantile_reserve_gauche,
            "quantile_reserve_centre": None,
            "quantile_reserve_droite": 2,
            "quantile_reserve_extreme_droite": 1,
            "quantile_reserve_divers": None,
            "bloc_tete_projete": bloc_tete,
            "quantile_rapport_force": quantile_force,
        }

    return pl.DataFrame(
        [
            _ligne("69123_0001", "joint_valide", "Gauche", 3),
            _ligne("ZZ001_0001", "joint_valide", "Centre", 2),  # étranger : jamais dans les contours REU.
            _ligne("69123_9999", "joint_valide", "Droite", 4),  # absent des contours REU (churn).
        ]
    )


def test_joindre_mobilisation_bureaux_joint_par_unite_id(tmp_path):
    chemin_contours = tmp_path / "contours.geojson"
    _ecrire_geojson(chemin_contours, _contours_bureaux_geojson())
    sortie = tmp_path / "mobilisation_bureaux.ndjson"

    rapport = joindre_mobilisation_bureaux(chemin_contours, _donnees_bureau_synthetiques(), sortie)

    lignes = sortie.read_text(encoding="utf-8").strip().splitlines()
    assert len(lignes) == 1
    feature = json.loads(lignes[0])
    assert feature["properties"]["unite_id"] == "69123_0001"
    assert feature["properties"]["statut"] == "joint_valide"
    assert feature["properties"]["maille"] == "bureau"
    assert feature["properties"]["reserve_gauche"] == 12.0
    assert feature["properties"]["reserve_centre"] is None
    assert feature["properties"]["quantile_reserve_gauche"] == 3
    assert feature["properties"]["rapport_force_bloc_tete"] == "Gauche"
    assert feature["properties"]["quantile_rapport_force"] == 3
    assert feature["tippecanoe"]["layer"] == "mobilisation_bureaux"
    assert feature["tippecanoe"]["minzoom"] == BUREAUX_MINZOOM
    assert feature["tippecanoe"]["maxzoom"] == BUREAUX_MAXZOOM
    assert rapport.nom_couche == "mobilisation_bureaux"
    assert rapport.scores_joints == 1


def test_joindre_mobilisation_bureaux_exclut_naturellement_l_etranger(tmp_path):
    chemin_contours = tmp_path / "contours.geojson"
    _ecrire_geojson(chemin_contours, _contours_bureaux_geojson())
    sortie = tmp_path / "mobilisation_bureaux.ndjson"

    rapport = joindre_mobilisation_bureaux(chemin_contours, _donnees_bureau_synthetiques(), sortie)

    assert rapport.total_scores == 2  # ZZ001_0001 exclu.
    assert rapport.scores_joints == 1
    assert rapport.contours_sans_score == 1  # 69123_0002, orphelin.


# --- joindre_mobilisation_communes (issue #26) ----------------------------------


def _donnees_commune_synthetiques() -> pl.DataFrame:
    def _ligne(code_commune, statut, degrade, bloc_tete, quantile_force):
        return {
            "code_commune": code_commune,
            "code_departement": "69",
            "statut": statut,
            "degrade": degrade,
            "reserve_gauche": 40.0,
            "reserve_centre": None,
            "reserve_droite": 30.0,
            "reserve_extreme_droite": 20.0,
            "reserve_divers": None,
            "quantile_reserve_gauche": 2,
            "quantile_reserve_centre": None,
            "quantile_reserve_droite": 1,
            "quantile_reserve_extreme_droite": 1,
            "quantile_reserve_divers": None,
            "bloc_tete_projete": bloc_tete,
            "quantile_rapport_force": quantile_force,
        }

    return pl.DataFrame(
        [
            _ligne("69123", "joint_valide", False, "Gauche", 2),  # dézoom d'une commune stable.
            _ligne("69456", "repli", True, "Droite", 3),  # commune en repli, visible à tout zoom.
        ]
    )


def _contours_communes_geojson() -> dict:
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"code": "69123", "nom": "Lyon", "departement": "69"},
                "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
            },
            {
                "type": "Feature",
                "properties": {"code": "69456", "nom": "Commune en repli", "departement": "69"},
                "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
            },
            {
                "type": "Feature",
                "properties": {"code": "01001", "nom": "Sans donnée mobilisation", "departement": "01"},
                "geometry": {"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]},
            },
        ],
    }


def test_joindre_mobilisation_communes_joint_par_code_commune(tmp_path):
    chemin = tmp_path / "communes.geojson.gz"
    with gzip.open(chemin, "wt", encoding="utf-8") as f:
        json.dump(_contours_communes_geojson(), f)
    sortie = tmp_path / "mobilisation_communes.ndjson"

    rapport = joindre_mobilisation_communes(chemin, _donnees_commune_synthetiques(), sortie)

    lignes = {json.loads(ligne)["properties"]["code_commune"]: json.loads(ligne) for ligne in sortie.read_text(encoding="utf-8").strip().splitlines()}
    assert set(lignes) == {"69123", "69456"}
    assert rapport.total_contours == 3
    assert rapport.contours_sans_score == 1


def test_joindre_mobilisation_communes_repli_visible_a_tout_zoom_stable_seulement_au_dezoom(tmp_path):
    chemin = tmp_path / "communes.geojson.gz"
    with gzip.open(chemin, "wt", encoding="utf-8") as f:
        json.dump(_contours_communes_geojson(), f)
    sortie = tmp_path / "mobilisation_communes.ndjson"

    joindre_mobilisation_communes(chemin, _donnees_commune_synthetiques(), sortie)
    lignes = {json.loads(ligne)["properties"]["code_commune"]: json.loads(ligne) for ligne in sortie.read_text(encoding="utf-8").strip().splitlines()}

    assert lignes["69456"]["properties"]["degrade"] is True
    assert lignes["69456"]["tippecanoe"]["maxzoom"] == BUREAUX_MAXZOOM  # visible même au zoom bureau.
    assert lignes["69123"]["properties"]["degrade"] is False
    assert lignes["69123"]["tippecanoe"]["maxzoom"] == COMMUNES_MAXZOOM  # remplacée par mobilisation_bureaux au-delà.
    assert lignes["69123"]["tippecanoe"]["layer"] == "mobilisation_communes"


# --- construire_pmtiles : erreur explicite si le binaire est introuvable -------


def test_construire_pmtiles_leve_une_erreur_explicite_si_tippecanoe_absent(tmp_path):
    with pytest.raises(RuntimeError, match="tippecanoe"):
        construire_pmtiles(
            [tmp_path / "bureaux.ndjson", tmp_path / "communes.ndjson"],
            tmp_path / "out.pmtiles",
            tippecanoe_bin=str(tmp_path / "binaire-inexistant"),
        )

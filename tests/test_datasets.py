"""Tests du manifeste des sources data.gouv.fr et de la logique de téléchargement."""

from pathlib import Path
from urllib.parse import urlparse

from projections.datasets import MANIFEST, Source, download


def test_manifest_destinations_are_relatives_et_surs():
    for source in MANIFEST:
        chemin = Path(source.dest)
        assert not chemin.is_absolute()
        assert ".." not in chemin.parts


def test_manifest_urls_sont_https():
    for source in MANIFEST:
        assert urlparse(source.url).scheme == "https"


def test_manifest_sans_destination_dupliquee():
    destinations = [source.dest for source in MANIFEST]
    assert len(destinations) == len(set(destinations))


def test_download_saute_un_fichier_deja_present(tmp_path, monkeypatch):
    source = Source(dest="elections/deja-la.csv", url="https://example.org/deja-la.csv")
    cible = tmp_path / source.dest
    cible.parent.mkdir(parents=True)
    cible.write_text("contenu existant")

    def urlretrieve_interdit(url, filename):
        raise AssertionError("urlretrieve ne doit pas être appelé pour un fichier déjà présent")

    monkeypatch.setattr(
        "projections.datasets.urllib.request.urlretrieve", urlretrieve_interdit
    )

    telecharges = download(sources=[source], dest_root=tmp_path)

    assert telecharges == []
    assert cible.read_text() == "contenu existant"


def test_download_recupere_un_fichier_manquant(tmp_path, monkeypatch):
    source = Source(dest="elections/nouveau.csv", url="https://example.org/nouveau.csv")
    appels = []

    def urlretrieve_simule(url, filename):
        appels.append((url, Path(filename)))
        Path(filename).write_text("contenu")

    monkeypatch.setattr(
        "projections.datasets.urllib.request.urlretrieve", urlretrieve_simule
    )

    telecharges = download(sources=[source], dest_root=tmp_path)

    cible = tmp_path / source.dest
    assert telecharges == [cible]
    assert cible.read_text() == "contenu"
    assert appels == [(source.url, cible)]

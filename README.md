# Projections 2027

Cartes électorales libres et gratuites, construites à partir des données officielles du ministère de l'Intérieur, à destination des militant·es de terrain. Objectif : projeter les résultats des élections passées sur la dynamique politique actuelle, au niveau du bureau de vote, pour aider à prioriser l'action face à l'extrême droite d'ici la présidentielle de 2027.

Ce projet succède à [carto_legislatives_2024](https://github.com/Virgile-Dauge/carto_legislatives_2024), fait dans l'urgence de la dissolution de juin 2024. Voir [docs/heritage-2024.md](docs/heritage-2024.md) pour ce qu'on en garde.

## État

🚧 Démarrage (juillet 2026). Deux chantiers en cours :

1. **Recherche** — état de l'art des méthodes de projection électorale (swing, inférence écologique, MRP…) et du choix des élections sources. Cadrage dans [docs/recherche/prompt-hyperresearch.md](docs/recherche/prompt-hyperresearch.md).
2. **Stack** — pipeline de données en marimo + Polars produisant un fichier PMTiles France entière, servi par un site statique MapLibre GL JS (chargement par tuiles, zéro serveur).

## Installation

```bash
uv sync
```

## Télécharger les données

Les fichiers sources (data.gouv.fr) sont volumineux et exclus du dépôt. Ils sont
téléchargés dans `data/raw/`, hors git :

```bash
uv run download-data
```

## Construire le panel bureau × scrutin × bloc

Ingère les 4 scrutins sources (présidentielle 2022, législatives 2022 et 2024,
européennes 2024) vers une table longue bureau × scrutin × bloc, en voix, écrite
dans `data/interim/` (hors git) :

> ⚠️ Format long : la participation (inscrits, votants, exprimés…) est répétée
> sur chaque ligne de bloc d'un même bureau × scrutin — dédupliquer par
> (`id_election`, `id_bv`) avant toute somme de participation.

```bash
uv run ingest
```

## Générer les tuiles

Joint le panel aux contours d'affichage (« Proposition de contours des bureaux
de vote » REU pour la couche `bureaux`, contours communaux Etalab pour la
couche `communes`, dézoom) et produit un unique fichier PMTiles France entière
(métropole + DROM ; les bureaux de l'étranger n'ont pas de contours REU, ils
restent hors carte) dans `data/tiles/` (hors git) :

```bash
uv run build-tiles
```

Prérequis : [tippecanoe](https://github.com/felt/tippecanoe) (binaire non
vendored — le compiler localement) :

```bash
git clone https://github.com/felt/tippecanoe.git .tippecanoe-src
cd .tippecanoe-src && make -j$(nproc)
```

Le binaire se passe via `--tippecanoe-bin` ou la variable d'environnement
`TIPPECANOE_BIN` (défaut : `tippecanoe` du PATH). La commande affiche le taux
de jointure identifiants-résultats ↔ identifiants-contours (les contours REU,
figés à septembre 2022, ne couvrent pas tous les bureaux 2024). Si le fichier
produit dépasse 100 Mo, il n'est pas commité mais publié en asset de Release
GitHub (`gh release upload`), et `site/config.js` pointé vers cette URL.

## Site carto

Site statique dans `site/` : MapLibre GL JS 5 + PMTiles 4 (chargés en CDN,
aucune dépendance à installer), choroplèthe par bloc en tête, dézoom vers la
couche communes. Carte **descriptive** (résultats 2024 réels), pas une
projection — mention affichée en permanence sur la carte.

Test local : copier ou symlinker le PMTiles généré sous `site/tiles/`, puis
servir le dossier avec un serveur HTTP statique quelconque, par exemple :

```bash
mkdir -p site/tiles && ln -sf ../../data/tiles/france.pmtiles site/tiles/france.pmtiles
python -m http.server --directory site
```

`site/config.js` définit l'URL du PMTiles (`./tiles/france.pmtiles` par
défaut) — à remplacer par l'URL de la Release GitHub une fois le fichier
hébergé en production. Déploiement automatique sur GitHub Pages via
`.github/workflows/deploy.yml` à chaque push sur `main` touchant `site/**`.

## Tests

```bash
uv run pytest
uv run ruff check .
```

## Licence

AGPL-3.0 — voir [LICENSE](LICENSE).

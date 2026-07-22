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

```bash
uv run ingest
```

## Tests

```bash
uv run pytest
uv run ruff check .
```

## Licence

AGPL-3.0 — voir [LICENSE](LICENSE).

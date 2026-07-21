# Héritage de carto_legislatives_2024

Ce document résume ce qui a été fait — et appris — dans [carto_legislatives_2024](https://github.com/Virgile-Dauge/carto_legislatives_2024), le prédécesseur de ce projet, construit en ~2 semaines dans l'urgence de la dissolution de juin 2024. Il était assumé « à l'arrache » : stack improvisée, notebooks à moitié cassés, pas de tests. Le repo est archivé mais reste consultable.

## Ce que faisait le projet 2024

- **Pipeline européennes → législatives** (`src/carto_legislatives_2024/`) : projection des votes des européennes 2024 sur les circonscriptions législatives, avec un score d'« engagement » pondéré (abstention, vote extrême droite, modèle « coude-à-coude » de compétitivité `(1-(x-y)²·(x·(1-y)+y·(1-x)))^500`) et des cartes Folium par département (choroplèthes Jenks + camemberts par circonscription).
- **Pipeline législatives 2024** (notebooks marimo `analyse_legislatives.py` / `generer_cartes.py`) : résultats définitifs par bureau de vote, agrégés en 5 blocs politiques, une carte Folium par département.
- D'abord fait pour la Loire-Atlantique (44), étendu à toute la France sur demande. Le découpage par département servait à limiter les temps de calcul et la taille des HTML.

## Ce qu'on garde (les leçons chèrement acquises)

### Données ministère de l'Intérieur

- **Format « wide »** : un jeu de colonnes par candidat (`Nuance candidat {i}`, `% Voix/exprimés {i}`), à faire fondre en long puis pivoter par nuance.
- **Nombres à la française** : les pourcentages arrivent en chaînes `"12,5%"` (virgule décimale, suffixe `%`).
- **24 nuances officielles** attribuées par les préfets (circulaire IOMA2415630C) : voir [classification_en_blocs.md](classification_en_blocs.md), qui documente chaque nuance et le regroupement en blocs (Gauche / Centre / Droite / Extrême droite / Divers).

### Réconciliation des bureaux de vote — LE point dur

Les identifiants de bureaux dans les géométries ne correspondent pas totalement à ceux des fichiers de résultats. Clé de jointure construite en 2024 : `id_bv` = code commune INSEE complété à 5 chiffres + `_` + code bureau. Une partie de la réconciliation a été faite à la main pour les européennes. **Les découpages de bureaux changent entre élections** : toute comparaison multi-scrutins au niveau bureau (2022 ↔ 2024) exigera une table de correspondance. C'est un sujet de la recherche en cours, pas un détail d'implémentation.

### Agrégation : toujours pondérer par les effectifs

Pour agréger des pourcentages de bureaux vers une maille supérieure (circonscription…), reconvertir en nombres de voix (`% × Exprimés / 100`), sommer, puis recalculer les pourcentages. La moyenne simple des pourcentages est fausse (bug corrigé en 2024, commit `f6c2c3a`).

### Convention de couleurs des blocs

Gauche `#e60000` · Centre `#ffcc00` · Droite `#542788` · Extrême droite `#996633` · Divers/Abstention `#bababa`

### Ce qui n'a PAS marché (et motive la nouvelle stack)

- **Une carte HTML statique par département** : lourd à générer, pénible à distribuer, et la vue France entière (Lonboard, 260 Mo) était inutilisable en pratique. → Remplacé par un unique fichier PMTiles + site statique MapLibre.
- **Folium multi-couches** : tooltips masqués par les changements de couches (problème de z-index des panes Leaflet, documenté dans `z-index.md` de l'ancien repo), légendes à supprimer à la main.
- **Notebooks Jupyter non reproductibles** (`split.ipynb`, `sandbox.ipynb` de 32 Mo dans git) : la moitié ne tournait plus quelques mois après. → marimo (reproductible par construction) + données volumineuses hors git.

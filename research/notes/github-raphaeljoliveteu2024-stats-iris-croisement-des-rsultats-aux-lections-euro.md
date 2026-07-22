---
title: 'GitHub - raphaeljolivet/eu2024-stats-iris: Croisement des résultats aux élections
  européennes 2024 avec les données démographique INSEE au niveau IRIS · GitHub'
id: github-raphaeljoliveteu2024-stats-iris-croisement-des-rsultats-aux-lections-euro
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- crosswalk-iris
created: '2026-07-21T20:03:07.731051Z'
updated: '2026-07-21T21:14:01.549416Z'
source: https://github.com/raphaeljolivet/eu2024-stats-iris
source_domain: github.com
fetched_at: '2026-07-21T20:03:07.691869Z'
fetch_provider: crawl4ai
status: review
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: GitHub repo (raphaeljolivet/eu2024-stats-iris) joining 2024 European election
  results with 2020 INSEE IRIS-level demographic data for metropolitan France, released
  as a geopackage. The join is geographic, relying on a separate project's automatic
  reconstruction of bureau-de-vote geometry from INSEE REU + OpenStreetMap (rather
  than an official bureau shapefile) as the intermediate layer between IRIS and election
  results. Demonstrates a working, reproducible IRIS-bureau-election crosswalk pipeline
  usable as a template for a 2027 CSP/diploma-to-bureau join, though it depends on
  a third-party geometry-reconstruction project rather than the official Etalab bureau
  contours.
---

[Skip to content](https://github.com/raphaeljolivet/eu2024-stats-iris#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/raphaeljolivet/eu2024-stats-iris) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/raphaeljolivet/eu2024-stats-iris) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/raphaeljolivet/eu2024-stats-iris) to refresh your session. Dismiss alert
/ **[eu2024-stats-iris](https://github.com/raphaeljolivet/eu2024-stats-iris) ** Public
  * [ Notifications ](https://github.com/login?return_to=%2Fraphaeljolivet%2Feu2024-stats-iris) You must be signed in to change notification settings
  * [ Fork 0 ](https://github.com/login?return_to=%2Fraphaeljolivet%2Feu2024-stats-iris)
  * [ Star  9 ](https://github.com/login?return_to=%2Fraphaeljolivet%2Feu2024-stats-iris)


[**1** Branch](https://github.com/raphaeljolivet/eu2024-stats-iris/branches)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
Jun 16, 2024 [44f3a21](https://github.com/raphaeljolivet/eu2024-stats-iris/commit/44f3a2139675564b442d7cb07c88d6fa0c3a24f0) · Jun 16, 2024
## History
[4 Commits](https://github.com/raphaeljolivet/eu2024-stats-iris/commits/main/)Open commit details 4 Commits  |  
| [res/img](https://github.com/raphaeljolivet/eu2024-stats-iris/tree/main/res/img "This path skips through empty directories")  | [res/img](https://github.com/raphaeljolivet/eu2024-stats-iris/tree/main/res/img "This path skips through empty directories")  |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
|   |   |   | Jun 16, 2024  |  
| View all files |  
## Repository files navigation
# Croisement des résultats des élections européennes 2024, avec les donnnées démographique INSEE de 2020, au niveau IRIS
Ce projet croise les [résultats des élections européennes de 2024](https://www.data.gouv.fr/fr/datasets/resultats-des-elections-europeennes-du-9-juin-2024/) avec les données démographiques [INSEE au niveau IRIS (2020)](https://www.insee.fr/fr/statistiques/7704076), pour l'ensemble de la France métropolitaine.
Cette jointure est faite de manière géographique, gràce à la reconcustruction de la géométrie des bureaux de vote produite par [cet autre projet](https://www.data.gouv.fr/fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/)
L'objectif est de permettre des statistiques démographiques fines sur les tendances politiques récentes.
# Données de sortie
La sortie de cette jointure est disponible :
  * au [format geopackage](https://github.com/raphaeljolivet/eu2024-stats-iris/releases/download/1.0/iris-stats.gpkg)


# Utilisation
Pour générer vous même les fichiers de sorties :
  1. Créez un nouvel environeme,nt Python 3.10, avec **conda** ou *_virtualenv_
  2. Importez lees dépendances : `pip install -r requirements.txt```
  3. Exécutez le point d'entrée principal : `python main.py`


Les données d'entrée sont téléchargées dans le dossier `data/in` et les sorties sont générées dans `data/out`
# Source de données
## Shapefile bureaux
  * <https://www.data.gouv.fr/fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/>
  * <https://www.data.gouv.fr/fr/datasets/r/d2392385-c12f-4b1b-8940-37da09be6333>


## Contours IRIS
<https://data.geopf.fr/telechargement/download/CONTOURS-IRIS/CONTOURS-IRIS_3-0__SHP__FRA_2023-01-01/CONTOURS-IRIS_3-0__SHP__FRA_2023-01-01.7z>
## Résultats des elections
<https://www.data.gouv.fr/fr/datasets/r/1996b2bc-e95a-4481-904f-28d16987fe61>
## Démographie 2020 Insee
<https://www.insee.fr/fr/statistiques/7704076> <https://www.insee.fr/fr/statistiques/fichier/7704076/base-ic-evol-struct-pop-2020_csv.zip>
# LICENSE
La code source et les données de sorties sont fournies selon les termes de la license [Creative Common NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.fr)
## About
Croisement des résultats aux élections européennes 2024 avec les données démographique INSEE au niveau IRIS 
### Resources
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/raphaeljolivet/eu2024-stats-iris).
[ Activity](https://github.com/raphaeljolivet/eu2024-stats-iris/activity)
### Stars
**9** stars 
### Watchers
**3** watching 
### Forks
[ **0** forks](https://github.com/raphaeljolivet/eu2024-stats-iris/forks)
##  [Releases 1](https://github.com/raphaeljolivet/eu2024-stats-iris/releases)
[ v1.0 Latest  Jun 16, 2024 ](https://github.com/raphaeljolivet/eu2024-stats-iris/releases/tag/1.0)
##  [Packages 0](https://github.com/users/raphaeljolivet/packages?repo_name=eu2024-stats-iris)
No packages published 
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/raphaeljolivet/eu2024-stats-iris).
##  [Contributors 1](https://github.com/raphaeljolivet/eu2024-stats-iris/graphs/contributors)
  * [ **raphaeljolivet** Raphael Jolivet ](https://github.com/raphaeljolivet)


## Languages
  * [ Jupyter Notebook 96.3% ](https://github.com/raphaeljolivet/eu2024-stats-iris/search?l=jupyter-notebook)
  * [ Python 3.7% ](https://github.com/raphaeljolivet/eu2024-stats-iris/search?l=python)


You can’t perform that action at this time. 

---
title: 'GitHub - datagouv/bureau-vote: Preparatory work for the publication of polling
  place shapes as open data. · GitHub'
id: github-datagouvbureau-vote-preparatory-work-for-the-publication-of-polling-place
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- contours-geographiques
- code-source
created: '2026-07-21T18:30:01.199963Z'
updated: '2026-07-21T18:39:17.668103Z'
source: https://github.com/datagouv/bureau-vote
source_domain: github.com
fetched_at: '2026-07-21T18:30:01.159274Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'Dépôt technique Etalab/data.gouv.fr (28 stars, archivé fonctionnellement
  mi-2023) documentant la génération des contours par diagrammes de Voronoï à partir
  des adresses REU. Contient le notebook Creation_de_contours_a_partir_du_REU.ipynb
  reproduisant exactement les contours publiés sur data.gouv.fr, et du code préparatoire
  de nettoyage/géocodage testé sur le département pilote de l''Ariège avant généralisation
  nationale. Confirme explicitement la non-unicité des tracés : ''D''autres méthodes
  sont possibles... il n''y a pas unicité des contours.'' Dépend du fichier de contours
  communaux (communes-20220101.shp, source data.gouv.fr découpage administratif OSM).'
---

[Skip to content](https://github.com/datagouv/bureau-vote#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/datagouv/bureau-vote) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/datagouv/bureau-vote) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/datagouv/bureau-vote) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/datagouv/bureau-vote).
/ Public
  * [ Notifications ](https://github.com/login?return_to=%2Fdatagouv%2Fbureau-vote) You must be signed in to change notification settings
  * [ Fork 4 ](https://github.com/login?return_to=%2Fdatagouv%2Fbureau-vote)
  * [ Star  28 ](https://github.com/login?return_to=%2Fdatagouv%2Fbureau-vote)


[**10** Branches](https://github.com/datagouv/bureau-vote/branches)[](https://github.com/datagouv/bureau-vote/tags)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
[Update with contours creation](https://github.com/datagouv/bureau-vote/commit/7e11dd8b87e349d7dc7229a91db7de6d7d9d5b46) Open commit details Jul 3, 2023 [7e11dd8](https://github.com/datagouv/bureau-vote/commit/7e11dd8b87e349d7dc7229a91db7de6d7d9d5b46) · Jul 3, 2023
## History
[43 Commits](https://github.com/datagouv/bureau-vote/commits/main/)Open commit details 43 Commits  |  
|   |   |   | Sep 21, 2022  |  
| [Creation_de_contours_a_partir_du_REU.ipynb](https://github.com/datagouv/bureau-vote/blob/main/Creation_de_contours_a_partir_du_REU.ipynb "Creation_de_contours_a_partir_du_REU.ipynb")  | [Creation_de_contours_a_partir_du_REU.ipynb](https://github.com/datagouv/bureau-vote/blob/main/Creation_de_contours_a_partir_du_REU.ipynb "Creation_de_contours_a_partir_du_REU.ipynb")  |   | Jul 3, 2023  |  
|   |   |   | Jul 3, 2023  |  
|   |   | [feat: update carto for REU addresses file](https://github.com/datagouv/bureau-vote/commit/3b6ddf50ed8612b008f0f234f75e4f236508accd "feat: update carto for REU addresses file")  | Dec 12, 2022  |  
|   |   | [Documentation of functions](https://github.com/datagouv/bureau-vote/commit/b0d6bca5b3d5ddc8be87a9ee8f0c8c30cc819bc3 "Documentation of functions")  | Aug 30, 2022  |  
|   |   | [feat: update carto for REU addresses file](https://github.com/datagouv/bureau-vote/commit/3b6ddf50ed8612b008f0f234f75e4f236508accd "feat: update carto for REU addresses file")  | Dec 12, 2022  |  
|   |   |   | Jul 3, 2023  |  
|   |   |   | Dec 13, 2022  |  
|   |   | [One file to generate contours from departemental parquet file](https://github.com/datagouv/bureau-vote/commit/4a45e303e86459b9b34a5db20ca5325246fc051d "One file to generate contours from departemental parquet file")  | Mar 13, 2023  |  
| [generate_areas_geojson.py](https://github.com/datagouv/bureau-vote/blob/main/generate_areas_geojson.py "generate_areas_geojson.py")  | [generate_areas_geojson.py](https://github.com/datagouv/bureau-vote/blob/main/generate_areas_geojson.py "generate_areas_geojson.py")  |   | Jul 3, 2023  |  
|   |   | [feat: enable geojson export](https://github.com/datagouv/bureau-vote/commit/750fd8c9afa3edf304d82f694eda3f6d4b7aa377 "feat: enable geojson export")  | Mar 27, 2023  |  
|   |   |   | Sep 26, 2022  |  
|   |   |   | Sep 22, 2022  |  
|   |   | [feat: update carto for REU addresses file](https://github.com/datagouv/bureau-vote/commit/3b6ddf50ed8612b008f0f234f75e4f236508accd "feat: update carto for REU addresses file")  | Dec 12, 2022  |  
|   |   |   | Aug 26, 2022  |  
|   |   | [Add numpy in requirements](https://github.com/datagouv/bureau-vote/commit/e98a6ac1397559db298ae869e668075750c703be "Add numpy in requirements")  | Dec 13, 2022  |  
|   |   |   | Dec 11, 2022  |  
| View all files |  
## Repository files navigation
# bureau-vote
Ce dépôt contient les travaux conjoints des équipes Etalab et data.gouv.fr, en étroite colaboration avec l'INSEE, au sujet du répertoire électoral unique (REU). Le but de ces travaux était de partir des [données du REU](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/) (adresses de France et leur bureau de vote attribué) pour déterminer des contours des bureaux de vote de France. Une telle donnée permettra à l'avenir - ainsi que pour toutes les élections dont les données sont déjà publiques - d'afficher les résultats des élections à la maille la plus fine qui soit : celle des bureaux de vote.
La méthode choisie est celle des [aires de Voronoï](https://fr.wikipedia.org/wiki/Diagramme_de_Vorono%C3%AF), qui permet de séparer un plan contenant des points d'intérêt (dit germes) en autant de zones autour de ces germes, de sorte que chaque zone enferme un seul germe, et forme l'ensemble des points de plus proches de ce germe que d'aucun autre. D'autres méthodes sont possibles, ainsi que d'autres choix au sein même de cette méthode : il n'y a pas unicité des contours.
## Création des contours
Le notebook python `Creation_de_contours_a_partir_du_REU.ipynb` contient toutes les informations permettant de regénérer les contours tels que nous les avons publiés. Les prérequis sont :
  * `python` et `jupyter notebook` installés
  * tous les packages listés dans le fichier `requirements.txt`


Il suffit ensuite de dérouler le notebook pour obtenir les contours de la même façon que nous les avons générés. Toutes les fonctions utilisées sont dans ce repo et sont perfectibles : n'hésitez pas à contribuer !
## Travaux préalables
Ce dépôt comprend aussi du code en langage Python permettant de nettoyer et géocoder un extrait (le département de l'Ariège) du format brut des adresses du Répertoire Electoral Unique, ainsi que du code permettant d'afficher sur un fond de carte le standard de publication retenu par l'INSEE [le lien de la documentation sera indiqué ici ultérieurement].
Il s'agit d'un des dépôts de travail en vue de la publication en open data des adresses du Répertoire Electoral Unique, qui n'a pas vocation à être maintenu à l'issue de la diffusion du fichier.
### Visualisation sur un fond de carte du fichier des adresses déjà géocodés, pour n'importe quel département
Déposer les fichiers sources de données à la racine du dépôt, modifier si utile le code en indiquant à la fois le chemin du fichier des adresses et le chemin du fichier de contour des communes (dans notre cas,communes-20220101.shp), indiquer le créer un environnement virtuel Python3.10 (pratique non nécessaire mais recommandée) puis lancer les commandes :

```
python3.10 -m pip install -r requirements.txt
python3.10 main_atelier.py

```

### Nettoyage, géocodage, visualisation du fichier des adresses, et essais de contours non officiels, pour le département de l'Ariège.
#### Données nécessaires
  * Récupérer les données sources
  * Récupérer les données des contours des communes ([fichier utilisé dans ce cadre](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/))


#### Déploiement
Déposer ces fichiers de données à la racine du dépôt, modifier si utile le code en indiquant le chemin du fichier de contour des communes (dans notre cas,communes-20220101.shp), créer un environnement virtuel Python3.10 (pratique non nécessaire mais recommandée) puis lancer les commandes :

```
python3.10 -m pip install -r requirements.txt
python3.10 main.py <NOM_FICHIER_SOURCE_ADRESSES_REU>

```

## About
Preparatory work for the publication of polling place shapes as open data. 
### Resources
### License
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/datagouv/bureau-vote).
[ Activity](https://github.com/datagouv/bureau-vote/activity)
[ Custom properties](https://github.com/datagouv/bureau-vote/custom-properties)
### Stars
**28** stars 
### Watchers
**8** watching 
### Forks
[ **4** forks](https://github.com/datagouv/bureau-vote/forks)
No releases published
##  [Packages 0](https://github.com/orgs/datagouv/packages?repo_name=bureau-vote)
No packages published 
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/datagouv/bureau-vote).
##  [Contributors 5](https://github.com/datagouv/bureau-vote/graphs/contributors)
## Languages
  * [ Jupyter Notebook 99.6% ](https://github.com/datagouv/bureau-vote/search?l=jupyter-notebook)
  * Other 0.4%


You can’t perform that action at this time. 

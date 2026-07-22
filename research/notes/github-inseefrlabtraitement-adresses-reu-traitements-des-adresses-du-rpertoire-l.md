---
title: 'GitHub - InseeFrLab/traitement-adresses-REU: Traitements des adresses du Répertoire
  Électoral Unique · GitHub'
id: github-inseefrlabtraitement-adresses-reu-traitements-des-adresses-du-rpertoire-l
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- reu-insee
- code-source
created: '2026-07-21T18:36:09.338039Z'
updated: '2026-07-21T18:39:17.798189Z'
source: https://github.com/InseeFrLab/traitement-adresses-REU
source_domain: github.com
fetched_at: '2026-07-21T18:36:09.299540Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: Dépôt officiel INSEE (11 stars, réalisé entre octobre 2022 et juin 2023 en
  collaboration avec la DINUM/Etalab) documentant l'intégralité de la chaîne de traitement
  ayant permis la diffusion open data des adresses et bureaux de vote du REU. Contient
  4 documents méthodologiques (doc/methodologie.html, dictionnaires de variables des
  deux tables, document d'architecture des scripts pour la reproductibilité) et les
  scripts source (dossier src/, majoritairement Jupyter Notebook + Python). Cette
  chaîne de traitement est la source primaire de la table diffusée sur data.gouv.fr
  (extraction REU de septembre 2022), et documente en amont la méthode de nettoyage/anonymisation
  par recours à la Base d'Adresses Nationale citée par le blog INSEE.
---

*Suggested by [[jeu-de-donnes-bureaux-de-vote-et-adresses-de-leurs-lecteurs-datagouvfr]] — code de traitement des adresses REU cité comme référence du jeu de données*

[Skip to content](https://github.com/InseeFrLab/traitement-adresses-REU#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/InseeFrLab/traitement-adresses-REU) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/InseeFrLab/traitement-adresses-REU) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/InseeFrLab/traitement-adresses-REU) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/traitement-adresses-REU).
/ **[traitement-adresses-REU](https://github.com/InseeFrLab/traitement-adresses-REU) ** Public
  * [ Notifications ](https://github.com/login?return_to=%2FInseeFrLab%2Ftraitement-adresses-REU) You must be signed in to change notification settings
  * [ Fork 0 ](https://github.com/login?return_to=%2FInseeFrLab%2Ftraitement-adresses-REU)
  * [ Star  11 ](https://github.com/login?return_to=%2FInseeFrLab%2Ftraitement-adresses-REU)


[**2** Branches](https://github.com/InseeFrLab/traitement-adresses-REU/branches)[](https://github.com/InseeFrLab/traitement-adresses-REU/tags)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
Jun 28, 2023 [95c54ce](https://github.com/InseeFrLab/traitement-adresses-REU/commit/95c54ce913ce1b677f4f9b2a3e26811130210d9c) · Jun 28, 2023
## History
[2 Commits](https://github.com/InseeFrLab/traitement-adresses-REU/commits/main/)Open commit details 2 Commits  |  
|   | Jun 27, 2023  |  
|   | Jun 27, 2023  |  
|   |   |   | Jun 27, 2023  |  
|   |   |   | Jun 27, 2023  |  
|   |   |   | Jun 28, 2023  |  
|   |   |   | Jun 27, 2023  |  
|   |   |   | Jun 27, 2023  |  
| View all files |  
## Repository files navigation
# Traitement des adresses du Répertoire Électoral Unique
Vous trouverez ici à titre informatif l'ensemble des codes de traitement sur les données du REU ayant permis la diffusion des adresses et bureaux de vote du fichier, ainsi que la documentation associée. Ce travail a été réalisé par l'Insee entre octobre 2022 et juin 2023 avec la collaboration de la Dinum (Etalab). Pour plus de détails, vous pouvez consulter la page méthodologique ici : `doc/methodologie.html`.
## Les données diffusées sur [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/)
Le travail réalisé permet la publication de 2 fichiers :
  * La table des adresses normalisées et géolocalisées du REU 
    * Dictionnaire des variables : `doc/dictionnaire_donnees_adresses.html`
  * La table des bureaux de vote du REU 
    * Dictionnaire des variables : `doc/dictionnaire_donnees_bv.html`


Ces deux fichiers ont pu être construits à partir de données brutes correspondent à une extraction des adresses du Répertoire Électoral Unique réalisée en septembre 2022.
## La documentation liée aux données publiées
Quatre fichiers de documentation sont disponibles dans le dossier _doc_ :
  * Le dictionnaire des variables de la table des adresses
  * Le dictionnaire des variables de la table des bureaux de vote
  * Un document méthodologique détaillant le travail effectué sur les données du REU
  * Un document présentant l'architecture des scripts du dossier _src_ à des fins de reproductibilité


## Les codes
Le dossier _src_ rassemble l'ensemble des scripts ayant permis la diffusion des adresses et bureaux de vote du REU. Pour plus de détails sur l'articulation des fichiers et leur rôle, vous pouvez consulter la page consacrée à la reproductibilité du projet : `doc/reproductibilite.html`.
## Licence
L'ensemble des informations (dictionnaire des variables, documentation et codes) sont mis à disposition sous [Licence Ouverte 2.0](https://spdx.org/licenses/etalab-2.0.html) (voir le fichier [LICENCE.md](https://github.com/InseeFrLab/traitement-adresses-REU/blob/main/LICENCE.md)).
## About
Traitements des adresses du Répertoire Électoral Unique 
### Resources
### License
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/traitement-adresses-REU).
[ Activity](https://github.com/InseeFrLab/traitement-adresses-REU/activity)
[ Custom properties](https://github.com/InseeFrLab/traitement-adresses-REU/custom-properties)
### Stars
**11** stars 
### Watchers
**5** watching 
### Forks
[ **0** forks](https://github.com/InseeFrLab/traitement-adresses-REU/forks)
No releases published
##  [Packages 0](https://github.com/orgs/InseeFrLab/packages?repo_name=traitement-adresses-REU)
No packages published 
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/traitement-adresses-REU).
##  [Contributors 1](https://github.com/InseeFrLab/traitement-adresses-REU/graphs/contributors)
  * [ **antoine-palazz** Antoine Palazzolo ](https://github.com/antoine-palazz)


## Languages
  * [ Jupyter Notebook 82.4% ](https://github.com/InseeFrLab/traitement-adresses-REU/search?l=jupyter-notebook)
  * [ Python 17.5% ](https://github.com/InseeFrLab/traitement-adresses-REU/search?l=python)
  * [ Shell 0.1% ](https://github.com/InseeFrLab/traitement-adresses-REU/search?l=shell)


You can’t perform that action at this time. 

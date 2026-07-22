---
title: 'GitHub - InseeFrLab/mapvotr: Package de production de contours de bureaux
  de vote à partir des adresses du REU · GitHub'
id: github-inseefrlabmapvotr-package-de-production-de-contours-de-bureaux-de-vote-pa
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- contours-geographiques
- code-source
- reu-insee
created: '2026-07-21T18:30:11.771750Z'
updated: '2026-07-21T18:39:17.677445Z'
source: https://github.com/InseeFrLab/mapvotr
source_domain: github.com
fetched_at: '2026-07-21T18:30:11.662882Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: Package R officiel InseeFrLab (17 stars) produisant des contours approximés
  de bureaux de vote à partir des adresses géolocalisées du REU — équivalent institutionnel
  INSEE de l'outil Python d'Etalab (github.com/etalab/bureau-vote). Maintenu activement
  jusqu'en juillet 2024 (ajout de Mayotte à la fonction epsg_from_cog pour gérer les
  projections spécifiques aux territoires d'outre-mer), ce qui illustre les difficultés
  de généralisation géographique (DOM/TOM) de ces méthodes de contourage. Documentation
  méthodologique renvoie à l'article de blog INSEE 'à chaque bureau de vote ses électeurs'.
---

*Suggested by [[issues-inseefrlabmapvotr-github-2]] — issue #3 mentions decouplage_bv function - likely handles bureau de vote splits across elections*

[Skip to content](https://github.com/InseeFrLab/mapvotr#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/InseeFrLab/mapvotr) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/InseeFrLab/mapvotr) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/InseeFrLab/mapvotr) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/mapvotr).
/ Public
  * [ Notifications ](https://github.com/login?return_to=%2FInseeFrLab%2Fmapvotr) You must be signed in to change notification settings
  * [ Fork 3 ](https://github.com/login?return_to=%2FInseeFrLab%2Fmapvotr)
  * [ Star  17 ](https://github.com/login?return_to=%2FInseeFrLab%2Fmapvotr)


[**4** Branches](https://github.com/InseeFrLab/mapvotr/branches)[](https://github.com/InseeFrLab/mapvotr/tags)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
[Merge pull request](https://github.com/InseeFrLab/mapvotr/commit/257bc5d9711ea6cc51642f20b1ac88478484d864) [#10](https://github.com/InseeFrLab/mapvotr/pull/10) [from cedricr/add_mayotte](https://github.com/InseeFrLab/mapvotr/commit/257bc5d9711ea6cc51642f20b1ac88478484d864) Open commit details Jul 22, 2024 [257bc5d](https://github.com/InseeFrLab/mapvotr/commit/257bc5d9711ea6cc51642f20b1ac88478484d864) · Jul 22, 2024
## History
[45 Commits](https://github.com/InseeFrLab/mapvotr/commits/main/)Open commit details 45 Commits  |  
|   |   |   | Jun 28, 2023  |  
|  [Merge pull request](https://github.com/InseeFrLab/mapvotr/commit/257bc5d9711ea6cc51642f20b1ac88478484d864 "Merge pull request #10 from cedricr/add_mayotte

Ajout de Mayotte à epsg_from_cog") [#10](https://github.com/InseeFrLab/mapvotr/pull/10) [from cedricr/add_mayotte](https://github.com/InseeFrLab/mapvotr/commit/257bc5d9711ea6cc51642f20b1ac88478484d864 "Merge pull request #10 from cedricr/add_mayotte

Ajout de Mayotte à epsg_from_cog")  | Jul 22, 2024  |  
|   |   | [supprimer infos importantes](https://github.com/InseeFrLab/mapvotr/commit/e4b2b05f15b5cbe43eb5ea72ef38fc9f22891e55 "supprimer infos importantes")  | Jul 7, 2023  |  
|   | Jun 29, 2023  |  
|   | Jul 17, 2024  |  
| [pkgdown/favicon](https://github.com/InseeFrLab/mapvotr/tree/main/pkgdown/favicon "This path skips through empty directories")  | [pkgdown/favicon](https://github.com/InseeFrLab/mapvotr/tree/main/pkgdown/favicon "This path skips through empty directories")  |   | Jun 16, 2023  |  
|   |   |   | Jun 29, 2023  |  
|   |   |   | Jul 17, 2024  |  
|   |   |   | May 23, 2023  |  
|   |   | [import from gitlab.insee](https://github.com/InseeFrLab/mapvotr/commit/feebc82416a563db03250de4067ae0d1f8205bf3 "import from gitlab.insee")  | May 23, 2023  |  
|   |   |   | Jul 17, 2024  |  
|   |   | [import from gitlab.insee](https://github.com/InseeFrLab/mapvotr/commit/feebc82416a563db03250de4067ae0d1f8205bf3 "import from gitlab.insee")  | May 23, 2023  |  
|   |   | [import from gitlab.insee](https://github.com/InseeFrLab/mapvotr/commit/feebc82416a563db03250de4067ae0d1f8205bf3 "import from gitlab.insee")  | May 23, 2023  |  
|   |   |   | Jul 17, 2024  |  
|   |   |   | Jun 29, 2023  |  
|   |   |   | Jun 15, 2023  |  
|   |   |   | May 23, 2023  |  
| View all files |  
## Repository files navigation
# mapvotr 
Production de contours approximés de bureaux de votes (BV) à partir de la [base des adresses géolocalisées du Répertoire électoral unique (REU)](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/) diffusée par l'Insee.
## Premiers pas
**Installation**

```
devtools::install_github("InseeFrLab/mapvotr")

```

Pour un exemple d'utilisation et pour davantage d'informations sur la méthode, se référer à la documentation en ligne de [mapvotr](https://inseefrlab.github.io/mapvotr/index.html)
## En savoir plus
  * [Article de blog documentant la génèse et un cas d'utilisation du package](https://blog.insee.fr/a-vote-a-chaque-bureau-de-vote-ses-electeurs)
  * [Outil similaire développé en python par Etalab](https://github.com/etalab/bureau-vote)


## About
Package de production de contours de bureaux de vote à partir des adresses du REU 
### Resources
### License
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/mapvotr).
[ Activity](https://github.com/InseeFrLab/mapvotr/activity)
[ Custom properties](https://github.com/InseeFrLab/mapvotr/custom-properties)
### Stars
**17** stars 
### Watchers
**2** watching 
### Forks
[ **3** forks](https://github.com/InseeFrLab/mapvotr/forks)
No releases published
##  [Packages 0](https://github.com/orgs/InseeFrLab/packages?repo_name=mapvotr)
No packages published 
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/InseeFrLab/mapvotr).
##  [Contributors 4](https://github.com/InseeFrLab/mapvotr/graphs/contributors)
  * [ **jpramil** Julien PRAMIL ](https://github.com/jpramil)
  * [ **actions-user** ](https://github.com/actions-user)
  * [ **antoine-palazz** Antoine Palazzolo ](https://github.com/antoine-palazz)
  * [ **cedricr** Cedric R. ](https://github.com/cedricr)


## Languages
  * [ R 100.0% ](https://github.com/InseeFrLab/mapvotr/search?l=r)


You can’t perform that action at this time. 

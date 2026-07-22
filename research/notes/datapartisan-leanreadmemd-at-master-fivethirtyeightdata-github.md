---
title: data/partisan-lean/README.md at master · fivethirtyeight/data · GitHub
id: datapartisan-leanreadmemd-at-master-fivethirtyeightdata-github
tags:
- projections-electorales-bureaux-2027-b0b1c4
- partisan-lean
- redistricting
- combinaison-scrutins
created: '2026-07-21T18:30:37.556485Z'
updated: '2026-07-21T18:39:17.711543Z'
source: https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md
source_domain: github.com
fetched_at: '2026-07-21T18:30:37.513656Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'README technique du jeu de données ''Partisan Lean'' de FiveThirtyEight
  (dernière mise à jour sept. 2022) : formule exacte de la pondération multi-scrutins
  utilisée pour estimer le penchant partisan d''un État ou d''une circonscription
  indépendamment du candidat en lice. Formule : 50% du différentiel de marge de l''unité
  par rapport à la nation lors de la présidentielle la plus récente, 25% du même différentiel
  lors de la présidentielle précédente, et 25% d''un ''lean'' législatif d''État calculé
  sur les résultats populaires cumulés des 4 élections les plus récentes à la chambre
  basse de l''État. Chiffre positif = penchant démocrate, négatif = penchant républicain.
  Point méthodologique explicite important : les partisan leans ne sont PAS comparables
  d''une année sur l''autre car ils intègrent à chaque cycle un nouveau découpage
  électoral (redistricting) et des changements de méthodologie — le jeu de données
  distingue des versions 2018, 2020, 2021 (pré-redécoupage, pour élections spéciales
  du 117e Congrès) et 2022 (post-redécoupage 2021-22). Directement transposable à
  Axe 2 de la question de recherche française : c''est un exemple concret et documenté
  de pondération multi-scrutins (présidentielle t, présidentielle t-1, législatives
  locales x4) pour construire un indice de rapport de force local indépendant du bruit
  d''un seul scrutin, avec gestion explicite du problème de changement de découpage
  entre élections.'
---

[Skip to content](https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/fivethirtyeight/data/blob/master/partisan-lean/README.md).
/ Public
  * [ Notifications ](https://github.com/login?return_to=%2Ffivethirtyeight%2Fdata) You must be signed in to change notification settings
  * [ Fork 11.1k ](https://github.com/login?return_to=%2Ffivethirtyeight%2Fdata)
  * [ Star  17.4k ](https://github.com/login?return_to=%2Ffivethirtyeight%2Fdata)


## Collapse file tree
## Files
Search this repository(forward slash)` forward slash/`
/
# README.md
Copy path
More file actions
More file actions
## Latest commit
Sep 9, 2022
[698baa1](https://github.com/fivethirtyeight/data/commit/698baa119ef3e28bb103f11689c636c0edd38357) · Sep 9, 2022
## History
[History](https://github.com/fivethirtyeight/data/commits/master/partisan-lean/README.md)
Open commit details
History
13 lines (8 loc) · 1.65 KB
/
# README.md
Copy path
## File metadata and controls
  * Preview
  * 

13 lines (8 loc) · 1.65 KB
Copy raw file
Download raw file
You must be signed in to make or propose changes
More edit options
Edit and raw actions
# FiveThirtyEight's Partisan Lean
This directory contains the data for FiveThirtyEight's partisan lean metric, or the average margin difference between how a state or district votes and how the country votes overall. Positive numbers mean Democratic leans, while negative numbers mean Republican leans.
This version of partisan lean, meant to be used for congressional and gubernatorial elections, is calculated as 50 percent the state or district’s lean relative to the nation in the most recent presidential election, 25 percent its relative lean in the second-most-recent presidential election and 25 percent a custom state-legislative lean based on the statewide popular vote in the four most recent state House elections.
The current partisan leans are meant to be used for the 2022 midterm elections; they take election results through 2021 into account and correspond to the district lines as they stood after the 2021-22 redistricting process. The partisan leans in the “2021” folder were meant to be used for 2021-22 special elections; they take election results through 2020 into account and correspond to the district lines for the 117th Congress, before redistricting took place. Past partisan leans for the 2018 and 2020 election cycles are also available. Due to redistricting and changes in methodology, partisan leans are not comparable across years.  
| Column  | Description  |  
| --- | --- |  
|  `state`/`district`  | The state or district the partisan lean is calculated for.  |  
| `2022`  | Partisan lean index for the 2022 midterm elections, taking election results through 2021 into account and corresponding to post-redistricting congressional maps.  |  
You can’t perform that action at this time. 

---
title: datagouvfr_data_pipelines/data_processing/elections/aggregation/README.md at
  main · datagouv/datagouvfr_data_pipelines · GitHub
id: datagouvfr_data_pipelinesdata_processingelectionsaggregationreadmemd-at-main-dat
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-crosswalk-bureaux-fiabilite
- code-source
created: '2026-07-21T19:44:55.599989Z'
updated: '2026-07-21T19:45:43.994321Z'
source: https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md
source_domain: github.com
fetched_at: '2026-07-21T19:44:55.562120Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'README de 12 lignes documentant le job data_processing_elections : fichier
  source dag.py, fréquence de mise à jour MANUELLE (pas automatique/schedulée), déclenchée
  à chaque nouvelle publication du MIOM (Ministère de l''Intérieur et des Outre-mer).
  Confirme que l''agrégation n''est PAS un pipeline continu mais une opération ponctuelle
  ré-exécutée à la main par l''équipe data.gouv.fr après chaque scrutin, ce qui explique
  le décalage temporel et les bugs de correspondance signalés et corrigés a posteriori
  dans les discussions du jeu de données (ex: Montbéliard, préfixes DOM-TOM).'
---

*Suggested by [[aggregation]] — README describing aggregation pipeline methodology (rendered blob page)*

[Skip to content](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md).
/ **[datagouvfr_data_pipelines](https://github.com/datagouv/datagouvfr_data_pipelines) ** Public
  * [ Notifications ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines) You must be signed in to change notification settings
  * [ Fork 7 ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines)
  * [ Star  18 ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines)


## Collapse file tree
## Files
Search this repository(forward slash)` forward slash/`
/
# README.md
Copy path
More file actions
More file actions
## Latest commit
success
Apr 1, 2026
[413383b](https://github.com/datagouv/datagouvfr_data_pipelines/commit/413383bbec5d24e0fc62f0f76e4431bfa5d3b119) · Apr 1, 2026
## History
[History](https://github.com/datagouv/datagouvfr_data_pipelines/commits/main/data_processing/elections/aggregation/README.md)
Open commit details
History
12 lines (10 loc) · 671 Bytes
/
# README.md
Copy path
## File metadata and controls
  * Preview
  * 

12 lines (10 loc) · 671 Bytes
Copy raw file
Download raw file
You must be signed in to make or propose changes
More edit options
Outline
Edit and raw actions
# Documentation
## data_processing_elections  
| Information  | Valeur  |  
| --- | --- |  
| Fichier source  | `dag.py`  |  
| Description  | Ce traitement permet d'agréger les données des élections dans deux fichiers qui seront mis à jour à chaque nouvelle publication du MIOM.  |  
| Fréquence de mise à jour  | Manuelle  |  
| Données sources   | Toutes les données des élections publiées par le MIOM sur data.gouv.fr (liste dans la description du JDD de sortie)  |  
| Données de sorties  | [Dataset données des élections agrégées](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/)  |  
| Channel Tchap d'information  | bot-datagouv-dataeng  |  
You can’t perform that action at this time. 

---
title: Jeu de données - Données des élections agrégées | data.gouv.fr
id: jeu-de-donnes-donnes-des-lections-agrges-datagouvfr
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- reconciliation-identifiants
- ministere-interieur
- crosswalk
created: '2026-07-21T18:30:33.516328Z'
updated: '2026-07-21T18:39:17.701641Z'
source: https://www.data.gouv.fr/datasets/donnees-des-elections-agregees
source_domain: www.data.gouv.fr
fetched_at: '2026-07-21T18:30:33.479898Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Dataset central de data.gouv.fr agrégeant les résultats électoraux officiels
  du Ministère de l''Intérieur (présidentielle, législatives, européennes, municipales,
  régionales, départementales, cantonales) au niveau bureau de vote. Deux fichiers
  : general-results.csv (participation, blancs, nuls par bureau et par scrutin) et
  candidats-results.csv (résultats par candidat par bureau), joints par id_election
  (format année_type_tour, ex. ''2022_pres_t1'') + id_brut_miom. POINT CLÉ pour la
  réconciliation : jointure documentée avec le REU INSEE via une ''table de conversion
  des identifiants des bureaux de vote (table-bv-reu.csv)'' — c''est le crosswalk
  explicite entre identifiants électoraux (Ministère Intérieur) et identifiants REU
  (INSEE). Structure des données modifiée en janvier 2026 (avertissement de rupture
  de schéma). Pipeline de mise à jour open source : github.com/datagouv/datagouvfr_data_pipelines/tree/main/data_processing/elections.
  Limite documentée : pas de données au niveau bureau de vote pour certains scrutins
  anciens (ex. départementales 2021, municipales 2008 hors communes >3500 habitants).'
---

*Suggested by [[donnes-lections-datagouvfr]] — jeu de données agrégées officielles utilisé pour l'inférence par régression sur résultats*

Jeu de données - Données des élections agrégées | data.gouv.fr
Qualité des métadonnées :
  * Description des données renseignée
  * Fichiers documentés
  * Licence renseignée
  * Fréquence de mise à jour respectée
  * Formats de fichiers standards
  * Couverture temporelle renseignée
  * Couverture spatiale renseignée
  * Tous les fichiers sont disponibles


[En savoir plus sur cet indicateur](https://guides.data.gouv.fr/guides/guide-qualite/ameliorer-la-qualite-dun-jeu-de-donnees-en-continu/ameliorer-le-score-de-qualite-des-metadonnees "En savoir plus sur cet indicateur - ouvre une nouvelle fenêtre")
# Données des élections agrégées 
Description
> /!\ la structure des données a évolué en janvier 2026
Ce jeu de données contient deux fichiers créés à partir des fichiers contenant les résultats des élections, publiés par le Ministère de l'Intérieur et des Outre-mer :
  * Résultats généraux (general-results.csv) : contient les chiffres de participation, de votes blancs et nuls, par bureau de vote, pour chaque élection.
  * Résultats par candidat (candidats-results.csv) : contient les résultats des votes pour chaque candidat par bureau de vote.


La colonne id_election contient l'information de l'élection concernée (année, type, tour), par exemple : 2022_pres_t1 pour le premier tour de l'élection présidentielle de 2022. Les deux tables sont rapprochables par les colonnes id_election et id_brut_miom. Ces données sont également rapprochables du [Répertoire électoral unique](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/) publié par l'INSEE. Les jointures se font par l'intermédiaire de la [table de conversion des identifiants des bureaux de vote (table-bv-reu.csv)](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/).
Le code permettant de mettre à jour ce jeu de données est ouvert et disponible [ici](https://github.com/datagouv/datagouvfr_data_pipelines/tree/main/data_processing/elections).
Sources des données agrégées
  * [Départementales 2021 T2](https://www.data.gouv.fr/fr/datasets/elections-departementales-2021-resultats-du-2eme-tour/)
  * [Départementales 2021 T1](https://www.data.gouv.fr/fr/datasets/elections-departementales-2021-resultats-du-1er-tour/)
  * [Municipales 2008](https://www.data.gouv.fr/fr/datasets/elections-municipales-2008-communes-de-plus-de-3-500-habitants-resultats-par-bureaux-de-vote-1/) (uniquement les communes de plus de 3500 habitants ; votes blancs et nuls réunis dans la colonne `Nuls`)
  * (pas de données au niveau bureau de vote)


Lire plus Producteur 
    
## [data.gouv.fr  ](https://www.data.gouv.fr/organizations/data-gouv-fr) Contacts 
    
[Support DataGouv](https://www.data.gouv.fr/fr/support/ "Support DataGouv")(Contact) Licence
    [Licence Ouverte / Open Licence version 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence) Dernière mise à jour
    7 juillet 2026
Vues
50.95K
depuis juin 2023
**+ 806** en juil. 2026
Téléchargements
82.4K
depuis juin 2023
**+ 622** en juil. 2026
Qualité des métadonnées:
Bon (100 %) 
## [Fichiers (8)](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees)
## [Réutilisations et API (24)](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/reuses_and_dataservices)
## [Discussions (17)](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/discussions)
## [Ressources communautaires ](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/community-resources)
## [Informations ](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/informations)
4 fichiers principaux
4 fichiers de documentation

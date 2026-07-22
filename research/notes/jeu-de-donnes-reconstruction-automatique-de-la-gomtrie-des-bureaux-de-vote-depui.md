---
title: Jeu de données - Reconstruction automatique de la géométrie des bureaux de
  vote depuis INSEE REU et OpenStreetMap | data.gouv.fr
id: jeu-de-donnes-reconstruction-automatique-de-la-gomtrie-des-bureaux-de-vote-depui
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- contours-geographiques
- reu-insee
created: '2026-07-21T18:30:22.510048Z'
updated: '2026-07-21T18:39:17.690866Z'
source: https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap
source_domain: www.data.gouv.fr
fetched_at: '2026-07-21T18:30:22.473120Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Méthode alternative (tierce, Makina Corpus / Frédéric Rodrigo, licence ODbL)
  de reconstruction des contours de bureaux de vote depuis le REU INSEE : diagrammes
  de Voronoï contraints par la voirie OpenStreetMap, complétés par des zones environnantes
  sans adresses. Pour les communes à bureau unique, utilise directement le contour
  communal ; pour les communes multi-bureaux, seules les zones avec adresses d''électeurs
  sont couvertes (incomplétude documentée). Code : github.com/makinacorpus/bureaux-de-vote-reconstruction.
  Démontre l''existence d''au moins 3 méthodes indépendantes et non officielles de
  contourage (Etalab/data.gouv Voronoï pur, INSEE mapvotr, Makina Corpus Voronoï+OSM),
  aucune ne faisant autorité.'
---

Jeu de données - Reconstruction automatique de la géométrie des bureaux de vote depuis INSEE REU et OpenStreetMap | data.gouv.fr
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
# Reconstruction automatique de la géométrie des bureaux de vote depuis INSEE REU et OpenStreetMap 
Description
Reconstruction des géométries de bureau de vote depuis les adresses des électeurs : [Répertoire électoral unique (REU) de l'INSEE](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/)
Utilise une approche basée sur des diagrammes de Voronoï sous contraintes des limites de la voirie d'OpenStreetMap. Les géométries des bureaux sont ensuite complétées par des zones environnantes sans adresses.
Le code source du calculé est disponible sur Github : <https://github.com/makinacorpus/bureaux-de-vote-reconstruction> . Ce code a initialement été mis au point par Makina Corpus. La méthode est détaillée de l'article [Une approche de reconstruction automatique de la géométrie des bureaux de vote](https://makina-corpus.com/sig-cartographie/une-approche-de-reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote).
La méthode de construction utilise les limites de commune pour les communes avec uniquement un seul bureau de vote et une reconstruction de polygones pour les autres. De ce fait les communes avec plusieurs bureaux de votes, seules les zones comportant des adresses d’électeurs sont couvertes.
[Carte de visualisation en ligne](https://makinacorpus.github.io/bureaux-de-vote-reconstruction/#12.35/45.19093/5.72225)
Lire plus Producteur 
    
Ce jeu de données a été publié à l'initiative et sous la responsabilité de Frédéric Rodrigo.  Licence
    [Open Data Commons Open Database License (ODbL)](http://opendatacommons.org/licenses/odbl/summary/) Dernière mise à jour
    11 juillet 2023
Vues
6.94K
depuis juil. 2023
**+ 87** en juil. 2026
Téléchargements
1.03K
depuis juil. 2023
**+ 2** en juil. 2026
Qualité des métadonnées:
Bon (100 %) 
## [Fichiers (2)](https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap)
## [Réutilisations et API (1)](https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/reuses_and_dataservices)
## [Discussions (2)](https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/discussions)
## [Ressources communautaires ](https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/community-resources)
## [Informations ](https://www.data.gouv.fr/datasets/reconstruction-automatique-de-la-geometrie-des-bureaux-de-vote-depuis-insee-reu-et-openstreetmap/informations)
2 fichiers principaux

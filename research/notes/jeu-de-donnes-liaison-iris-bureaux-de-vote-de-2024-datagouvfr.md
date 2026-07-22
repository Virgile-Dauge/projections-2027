---
title: Jeu de données - Liaison IRIS / Bureaux de vote de 2024 | data.gouv.fr
id: jeu-de-donnes-liaison-iris-bureaux-de-vote-de-2024-datagouvfr
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- crosswalk-iris
created: '2026-07-21T20:02:53.872156Z'
updated: '2026-07-21T21:14:01.547445Z'
source: https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024
source_domain: www.data.gouv.fr
fetched_at: '2026-07-21T20:02:53.836971Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Official IRIS-to-bureau-de-vote crosswalk table published on data.gouv.fr
  (producer: Jérémy Perrin, updated 2 April 2026, Licence Ouverte 2.0). Built from
  three layers: 2025 Etalab bureau-de-vote boundaries (reprocessed from the Répertoire
  électoral unique), INSEE IRIS boundaries, and INSEE''s FiLoSoFi 2019 200m population
  grid. Method: distributes each 200m grid cell''s voting-age population between overlapping
  IRIS and bureaux pro-rata to area, then derives the IRIS-bureau liaison matrix from
  these population shares (not simple area-based estimation) — this is exactly the
  join needed to attach census CSP/diplôme data to bureau-level electoral results
  for 2027 projections. Known limitations: bureau numbering in the INSEE contour file
  does not always match numbering used by the Ministry of the Interior in election
  results; flags central Bordeaux and Paris''s first four arrondissements as problem
  zones needing extra care. Used to produce infra-communal electoral graphs on ''Le
  carré social'' (weighting political-family results across corresponding bureaux
  to estimate IRIS-level electoral scores).'
---

Jeu de données - Liaison IRIS / Bureaux de vote de 2024 | data.gouv.fr
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
# Liaison IRIS / Bureaux de vote de 2024 
Description
Contenu
Cette table permet de passer des IRIS aux bureaux de vote de 2024 et inversement.
Objet
Elle permet ainsi de corréler les données électorales (publiées par le ministère de l’Intérieur à l’échelle du bureau de vote) et les données socio-économiques des quartiers (publiées par l’Insee à l’échelle de l’IRIS).
Étant construite à l’aide du carroyage Insee en population à 200 mètres, elle fournit une estimation de la part de population d’un bureau de vote relevant d’un certain IRIS et vice-versa (et non pas d’une simple estimation en superficie).
Sources
La table de liaison a été construite à partir de trois découpages :
  * les **[contours géographiques des bureaux de vote de 2024](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote)** , publiés en 2025 par Etalab à partir d’un retraitement du Répertoire électoral unique
  * les **contours géographiques des IRIS** (ilôts regroupés pour l’information statistique) publiés par l’Insee en format geojson
  * le **[carroyage FiLoSoFi 2019 de la métropole à 200m en population](https://www.insee.fr/fr/statistiques/7655475?sommaire=7655515)** , publié par l’Insee


Méthode
La méthode est détaillée sur le site .
Elle consiste à répartir la population en âge de voter de chaque carreau FiLoSoFi entre les IRIS et bureaux de vote coïncidents au prorata de la superficie, puis à en déduire la matrice de liaison IRIS-bureaux de vote.
Le passage par les carreaux en population permet de fiabiliser l’estimation finale, puisqu’une petite partie d’un IRIS peut parfaitement contenir une grande partie de sa population, ce que les carreaux à 200 mètres permettent de détecter, garantissant ainsi le meilleur fléchage vers le bureau de vote effectif.
Limites
La table est tributaire de la numérotation d’origine des bureaux de vote dans le jeu de contours publié par l’Insee, qui ne coïncide pas toujours avec les numéros de bureaux utilisés par l’Intérieur dans les résultats électoraux.
D’expérience, lors de l’utilisation, une attention particulière doit être apportée au centre de Bordeaux ainsi qu’aux quatre premiers arrondissements de Paris.
Utilisation
Cette table a permis la réalisation de graphes électoraux infra-communaux, publiés sur **[Le carré social](http://www.carre-social.fr)**.
Ces graphes reposent notamment sur le calcul de niveaux électoraux estimés au niveau de l’IRIS, par pondération des résultats des familles politiques sur les bureaux de vote correspondants.
Lire plus Producteur 
    
Ce jeu de données a été publié à l'initiative et sous la responsabilité de Jérémy Perrin.  Licence
    [Licence Ouverte / Open Licence version 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence) Dernière mise à jour
    2 avril 2026
Vues
depuis mars 2026
**+ 61** en juil. 2026
Téléchargements
depuis mars 2026
**+ 25** en juil. 2026
Qualité des métadonnées:
Bon (100 %) 
## [Fichiers (2)](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024)
## [Réutilisations et API (1)](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024/reuses_and_dataservices)
## [Discussions (0)](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024/discussions)
## [Ressources communautaires ](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024/community-resources)
## [Informations ](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024/informations)
1 fichier principal
1 fichier de code source

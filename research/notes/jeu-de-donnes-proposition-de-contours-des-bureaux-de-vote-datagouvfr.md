---
title: Jeu de données - Proposition de contours des bureaux de vote | data.gouv.fr
id: jeu-de-donnes-proposition-de-contours-des-bureaux-de-vote-datagouvfr
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- contours-geographiques
- reu-insee
created: '2026-07-21T18:29:37.918536Z'
updated: '2026-07-21T18:39:17.656292Z'
source: https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote
source_domain: www.data.gouv.fr
fetched_at: '2026-07-21T18:29:37.882640Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Dataset Etalab/data.gouv.fr générant des contours géographiques (GeoJSON
  + PMTiles) des ~70000 bureaux de vote français par diagrammes de Voronoï appliqués
  aux adresses géolocalisées du REU, calqués sur les contours communaux. Avertissement
  explicite : approximation imprécise (le REU associe des adresses à un bureau, ce
  n''est pas une définition de contours géographiques), non-unicité de la méthode,
  ''n''a pas vocation à faire autorité''. Généré depuis un extrait figé de septembre
  2022, non mis à jour (reproductible via le code source github.com/etalab/bureau-vote
  avec des données INSEE plus récentes).'
---

Jeu de données - Proposition de contours des bureaux de vote | data.gouv.fr
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
# Proposition de contours des bureaux de vote 
Description
Éléments de contexte
Suite à la publication du jeu de données [Bureau de vote et adresses de leurs électeurs](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/) [par l'INSEE](https://www.data.gouv.fr/fr/organizations/institut-national-de-la-statistique-et-des-etudes-economiques-insee/) issu du REU (Répertoire Electoral Unique), [le département Etalab](https://www.etalab.gouv.fr/) et l'équipe data.gouv.fr ont travaillé sur la génération de contours des bureaux de vote à partir de ces données.
Comme indiqué dans [la note de blog de l'INSEE](https://blog.insee.fr/a-vote-a-chaque-bureau-de-vote-ses-electeurs/) :
> _Cette base des adresses géolocalisées permet d’approcher les « aires » ou « contours » de bureaux de vote, qui correspondent à la zone géographique regroupant l’ensemble des adresses des électeurs d’un même bureau de vote._
Précautions d’usage
La génération de ces contours est donc une approche, **qui comporte des imprécisions** en raison de la nature même des données (le REU est constitué d'adresses affiliées à un bureau de vote mais n'est pas en soit une définition de contours géographiques) et de la méthode utilisée. Elle est mise à disposition par l'équipe data.gouv.fr pour favoriser la réutilisation des données sources de l'INSEE mais **n'a pas vocation à faire autorité**.
Des méthodes différentes pourront créer des tracés / interpolations possibles différents, car la donnée source n'implique pas leur unicité.
Méthodologie
[Le code source](https://github.com/etalab/bureau-vote/) permettant la génération de ces contours est disponible sur Github. Ceux-ci sont calculés à partir de la méthode des [Diagrammes de Voronoi](https://fr.wikipedia.org/wiki/Diagramme_de_Vorono%C3%AF) appliqués sur les adresses et calqués sur les contours des communes françaises. Ce code est perfectible et toute contribution est la bienvenue (via une issue Github sur le dépôt du code source).
Format des données
Les données sont proposées au format Geojson (format de données géospatiales couramment utilisé pour représenter et échanger des informations géographiques) et Pmtiles (format de tuiles cartographiques optimisé pour le stockage et la diffusion de données cartographiques géospatiales).
L'utilisation des données au format pmtiles permet de facilement sourcer les contours depuis une page web sans avoir à charger d'un coup l'ensemble de la base (le chargement ne se fait que localement en fonction de la position et du niveau de zoom d'un utilisateur). Un exemple est proposé avec la publication d'un fichier html dans la documentation de ce jeu de donnée.
Mises à jour
Il n'est pas prévu de mettre à jour ce jeu de données. La méthode est reproductible avec des données plus récentes publiées par l'INSEE.
Lire plus Producteur 
    
## [data.gouv.fr  ](https://www.data.gouv.fr/organizations/data-gouv-fr) Licence
    [Licence Ouverte / Open Licence version 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence) Dernière mise à jour
    21 juillet 2026
Vues
46.19K
depuis juin 2023
**+ 400** en juil. 2026
Téléchargements
105.88K
depuis juin 2023
**+ 98** en juil. 2026
Qualité des métadonnées:
Bon (100 %) 
## [Fichiers (5)](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote)
## [Réutilisations et API (7)](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote/reuses_and_dataservices)
## [Discussions (5)](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote/discussions)
## [Ressources communautaires ](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote/community-resources)
## [Informations ](https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote/informations)
2 fichiers principaux
2 fichiers de documentation
1 fichier de code source

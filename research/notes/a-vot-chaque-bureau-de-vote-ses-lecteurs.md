---
title: '"A voté" : à chaque bureau de vote ses électeurs'
id: a-vot-chaque-bureau-de-vote-ses-lecteurs
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- reu-insee
- contours-geographiques
- validation-empirique
- socio-demographie
created: '2026-07-21T18:35:55.759555Z'
updated: '2026-07-21T18:39:17.795748Z'
source: https://blog.insee.fr/a-vote-a-chaque-bureau-de-vote-ses-electeurs/
source_domain: blog.insee.fr
fetched_at: '2026-07-21T18:35:55.722824Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Article de blog INSEE (auteurs Insee, ~8 min de lecture) présentant en détail
  la genèse et un cas d''usage du jeu de données REU/bureaux de vote. Contexte : avant
  ce jeu de données, il n''existait aucun fichier national consolidé liant adresses
  et bureaux de vote ; les chercheurs devaient s''adresser préfecture par préfecture
  (article L37 du code électoral) à des formats hétérogènes (listes de rues, plans
  papier). Le projet académique Cartelec (Bussi, Colange, Freire-Diaz, Jadot, 2010)
  est cité comme précédent limité. La loi n°2016-1048 du 1er août 2016 crée le REU
  tenu par l''INSEE. Méthode de purge des données nominatives : les libellés d''adresses
  REU sont remplacés par ceux de la Base d''Adresses Nationale (BAN), seules les adresses
  normalisées anonymisées et leur géolocalisation BAN sont publiées. Limite documentée
  : quelques adresses manquantes (doubles résidences, libellés trop imprécis pour
  la BAN), ''mais ces manques ponctuels n''empêchent pas de construire des contours
  statistiquement pertinents''. Méthode Voronoï détaillée (partition des communes
  par polygones de Voronoï autour de chaque adresse géolocalisée, puis regroupement
  par bureau de vote). Validation empirique : à Strasbourg, comparaison des contours
  MapvotR avec les contours officiels publiés par la mairie — bonne correspondance
  dans les zones denses du centre-ville, divergences localisées dans les zones peu
  denses (zone industrielle du port), mais ''même quand l''emprise des zonages diverge,
  les contours regroupent des populations très similaires, et donc des agrégats sociodémographiques
  proches'' (revenu médian quasi identique entre les deux découpages). Cas d''usage
  empirique présenté : corrélation forte entre niveau de vie médian (Filosofi 2019)
  et taux de participation au 1er tour de la présidentielle 2022, visible à l''échelle
  du bureau de vote dans les 25 plus grandes villes françaises avec un plateau autour
  de 80% de participation, corrélation invisible à l''échelle communale faute d''observations.
  Argumente que la maille bureau de vote offre ''un nombre beaucoup plus grand d''observations...
  Les résultats économétriques sont donc nettement plus robustes'' qu''au niveau communal.'
---

*Suggested by [[jeu-de-donnes-bureaux-de-vote-et-adresses-de-leurs-lecteurs-datagouvfr]] — article de blog INSEE présentant la méthodologie et un cas d'usage du REU pour les contours de bureaux de vote*

Gérer le consentement
Pour offrir les meilleures expériences, nous utilisons des technologies telles que les cookies pour stocker et/ou accéder aux informations des appareils. Le fait de consentir à ces technologies nous permettra de traiter des données telles que le comportement de navigation ou les ID uniques sur ce site. Le fait de ne pas consentir ou de retirer son consentement peut avoir un effet négatif sur certaines caractéristiques et fonctions.
Fonctionnel Fonctionnel Toujours activé 
L’accès ou le stockage technique est strictement nécessaire dans la finalité d’intérêt légitime de permettre l’utilisation d’un service spécifique explicitement demandé par l’abonné ou l’utilisateur, ou dans le seul but d’effectuer la transmission d’une communication sur un réseau de communications électroniques.
Préférences Préférences
L’accès ou le stockage technique est nécessaire dans la finalité d’intérêt légitime de stocker des préférences qui ne sont pas demandées par l’abonné ou l’internaute.
Statistiques Statistiques
Le stockage ou l’accès technique qui est utilisé exclusivement à des fins statistiques. Le stockage ou l’accès technique qui est utilisé exclusivement dans des finalités statistiques anonymes. En l’absence d’une assignation à comparaître, d’une conformité volontaire de la part de votre fournisseur d’accès à internet ou d’enregistrements supplémentaires provenant d’une tierce partie, les informations stockées ou extraites à cette seule fin ne peuvent généralement pas être utilisées pour vous identifier.
Marketing Marketing
L’accès ou le stockage technique est nécessaire pour créer des profils d’internautes afin d’envoyer des publicités, ou pour suivre l’utilisateur sur un site web ou sur plusieurs sites web ayant des finalités marketing similaires.
  * [Gérer {vendor_count} fournisseurs](https://blog.insee.fr/politique-de-cookies-ue/#cmplz-tcf-wrapper)
  * [En savoir plus sur ces finalités](https://cookiedatabase.org/tcf/purposes/)


Accepter Refuser Voir les préférences Enregistrer les préférences [Voir les préférences](https://blog.insee.fr/politique-de-cookies-ue/#cmplz-manage-consent-container)


[Aller au contenu](https://blog.insee.fr/a-vote-a-chaque-bureau-de-vote-ses-electeurs/#content)
[Conditions de vie et société](https://blog.insee.fr/category/conditions-de-vie-societe/) | [Territoires, villes et quartiers](https://blog.insee.fr/category/territoires-villes-et-quartiers/)
# « A voté » : à chaque bureau de vote ses électeurs
Quel lien y a-t-il entre la sociologie des différents quartiers au sein d’une ville et leur vote ? Les résultats d’une élection sont analysés à différentes échelles géographiques, la plus fine étant habituellement celle de la commune. Il est ainsi classique de relier le taux de participation à une élection dans une commune au revenu de ses habitants. Mais il était jusqu’à présent compliqué d’analyser de façon précise les différences de vote pouvant exister par quartier au sein d’une commune, dans les 6 800 communes contenant plusieurs bureaux de vote.
L’Insee vient d’y remédier, en mettant à disposition les données permettant de tracer des contours géographiques pour chaque bureau de vote, sous la forme d’un fichier qui relie les adresses des électeurs (adresses anonymisées issues du Répertoire électoral unique REU) et leur bureau de vote de rattachement. L’Insee fournit également des programmes informatiques pour utiliser ces données qui permettent d’approximer des « aires » ou « contours » de bureaux de vote et de les croiser avec d’autres informations (niveau de vie, âge de la population, etc.). Couplées aux résultats électoraux mis à disposition par le ministère de l’Intérieur et des Outre-mer pour chaque bureau de vote, ces données permettent ainsi d’étudier les comportements électoraux à un niveau infra-communal.
Depuis longtemps, chercheurs et journalistes souhaitent mettre en regard les résultats des élections avec les caractéristiques sociodémographiques des électeurs à une échelle géographique infra-communale. Mais jusqu’à récemment, il n’existait pas de fichier national consolidé contenant le lien entre les adresses des électeurs et leur bureau de vote. Pour étudier la géographie du vote, il fallait recueillir les informations auprès de chaque préfecture de département (elles sont communicables dans les conditions définies par l’article L 37 du code électoral). Ces informations, aux formats très divers (fichiers textuels comportant des noms de rues, plans au format papier, etc.), étaient difficilement exploitables. Ainsi, la géographie du vote était principalement analysée au niveau communal et supra-communal, faute de pouvoir facilement obtenir des informations à l’échelle infra-communale. Le projet [Cartelec](http://www.lecfc.fr/new/articles/205-article-8.pdf), porté par une équipe de chercheurs il y a une dizaine d’années, a représenté néanmoins une initiative importante en ce sens, dans la limite des informations disponibles à l’époque.
La loi n° 2016-1048 du 1er août 2016, modifiant l’article 16 du code électoral, a créé un répertoire électoral unique et permanent (REU), tenu par l’Insee pour la gestion du processus électoral. Le REU contient, entre autres, les adresses des électeurs inscrits sur les listes électorales et leur bureau de vote. À la suite de l’avis favorable rendu par la Commission d’accès aux documents administratifs, et en concertation avec le ministère de l’Intérieur et des Outre-mer, l’Insee a développé une méthode permettant de publier certaines informations issues du REU en données ouvertes (ou _open-data_), tout en ne divulguant aucune information sur les noms et prénoms de personnes. Le projet a bénéficié du soutien de la Direction interministérielle du numérique (Dinum – [Etalab](https://www.etalab.gouv.fr/)), l’organisme public qui coordonne la politique d’ouverture et de partage des données publiques. Ce billet de blog présente la démarche que l’Insee a menée pour permettre la diffusion et l’utilisation de ces données.
## Des données géolocalisées anonymisées…
Les données du REU proviennent des services des mairies lorsqu’ils valident l’inscription électorale d’un électeur. Même si l’on élimine les données de noms et prénoms des électeurs, leurs adresses peuvent contenir des éléments directement nominatifs (par exemple, des « chez M. X » pour les personnes hébergées chez un tiers). Pour « purger » les adresses de toute information directement nominative, l’Insee a remplacé les libellés d’adresses du REU par ceux de la [Base d’Adresses Nationale (BAN)](https://adresse.data.gouv.fr/) : seules ces adresses normalisées et anonymes sont publiées en données ouvertes. Elles sont accompagnées de la géolocalisation issue de la BAN.
Ce fichier de correspondance entre les adresses des électeurs et les bureaux de vote permet de construire le zonage d’habitation des électeurs par bureau de vote afin de le rapprocher de diverses données statistiques. Il peut manquer quelques adresses, notamment si des habitants disposent d’un autre logement dans une autre commune où ils sont inscrits sur les listes électorales, ou encore si certaines adresses n’ont pas pu être correctement retrouvées dans la BAN (leur libellé étant, par exemple, trop imprécis). Mais ces quelques manques ponctuels n’empêchent pas de construire des contours statistiquement pertinents.
## … pour construire les contours des bureaux de vote…
En définitive, les utilisateurs disposent à présent d’un fichier standardisé, comprenant une liste d’adresses géolocalisées, des variables décrivant la qualité de la géolocalisation, et le bureau de vote auquel chaque adresse est rattachée (la [documentation technique](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/) de constitution du fichier et les [codes](https://github.com/InseeFrLab/traitement-adresses-REU) écrits dans le langage de programmation Python associés sont disponibles). À noter que le REU est un répertoire vivant, mis à jour en permanence : le fichier des adresses diffusé aujourd’hui a été produit à partir d’une photographie de ce répertoire en septembre 2022.
Cette base des adresses géolocalisées permet d’approcher les « aires » ou « contours » de bureaux de vote, qui correspondent à la zone géographique regroupant l’ensemble des adresses des électeurs d’un même bureau de vote.
En pratique, il existe de multiples manières d’approximer les contours de bureaux de vote, qui n’ont généralement pas de tracé formalisé. L’Insee a construit une méthode de production automatisée de ces contours à partir des adresses géolocalisées du REU _via_ la BAN, reposant sur les polygones de Voronoï, pour aider à réaliser des études statistiques. Un polygone de Voronoï est une zone géométrique délimitée autour d’une adresse géolocalisée, qui contient tous les points de l’espace qui sont plus proches de cette adresse que de toute autre adresse géolocalisée (_figure 1_). Dans un premier temps, les polygones de Voronoï permettent ainsi de créer une partition des communes étudiées. Dans un second temps, le regroupement de ces polygones par bureau de vote permet de constituer une approximation des contours des bureaux de vote.
### Figure 1 – Exemple de polygones de Voronoï (traits fins) pour une distribution de points
_Sources : Insee REU, Filosofi 2019 ; Mairie de Strasbourg._
Cette méthode est mise à disposition _via_ la publication d’un programme informatique en langage R dans une librairie nommée _MapvotR_ , [en libre accès sur la plateforme de diffusion des codes de l’Insee](https://github.com/inseeFrLab/mapvotr). Les hypothèses et techniques utilisées y sont explicitées de façon totalement transparente (en particulier la manière de repérer et traiter les adresses probablement mal positionnées). L’utilisateur est libre d’améliorer et d’adapter le code à son cas d’utilisation, il peut aussi y suggérer des corrections si nécessaire.
À noter que la Direction interministérielle du numérique (Dinum) propose également un [outil informatique](https://github.com/etalab/bureau-vote), écrit en Python et complémentaire de _Mapvot_ _R_ , pour exploiter la base de donnée des adresses diffusée par l’Insee.
Certaines communes publient déjà les contours de leurs bureaux de vote, ce qui permet de comparer leur découpage communal avec celui produit par _MapvotR_. Sur l’exemple de Strasbourg (_figure 2_), les approximations réalisées par l’Insee épousent globalement bien les [contours publiés par la mairie](https://data.strasbourg.eu/explore/dataset/bureaux-de-vote/information/) dans les zones denses du centre-ville (même si elles sont visuellement moins harmonieuses, car elles ne sont pas découpées à partir des lignes de la voirie). Il est néanmoins possible d’observer des différences (un exemple est visible au nord-est de la carte de Strasbourg, dans la grande zone industrielle autour du port fluvial), mais celles-ci sont essentiellement situées dans des zones très peu denses, où la position géographique d’un petit nombre de ménages peut grandement influencer l’emprise du contour. Par conséquent, même quand l’emprise des zonages diverge, les contours regroupent des populations très similaires, et donc des agrégats sociodémographiques proches. À titre d’exemple, la _figure 3_ permet d’observer le revenu médian calculé sur les contours de la mairie de Strasbourg et sur les contours approximés par _MapvotR_ : les différences sont en général très faibles.
### Figure 2 – Contours des bureaux de vote à Strasbourg selon la mairie (en haut) et approximés à partir des adresses du REU (en bas)
_Sources : Insee, REU ; Mairie de Strasbourg_.
### Figure 3 – Les contours approximés de Strasbourg contiennent des populations aux revenus médians très similaires aux contours diffusés par la mairie
_Sources : Insee REU, Filosofi 2019 ; Mairie de Strasbourg._
## … et habiller ensuite ces « contours » de données, pour éclairer le débat public
Une fois les contours de bureaux de vote définis, il devient possible de caractériser la population résidente et de mettre en regard son comportement de vote.
L’Insee fournit plusieurs sources de données permettant d’obtenir des informations socio-démographiques des populations à l’échelle infra-communale. Parmi elles, le dispositif sur les revenus localisés sociaux et fiscaux ([Filosofi](https://www.insee.fr/fr/metadonnees/source/serie/s1172)) contient des informations agrégées sur le revenu déclaré, le revenu disponible des ménages, et la pauvreté monétaire à l’iris et pour les quartiers prioritaires de la politique de la ville. Aux mêmes niveaux géographiques, le recensement de la population fournit des statistiques sur les caractéristiques des habitants (répartition par sexe, âge, profession, nationalité, mode de transport pour aller travailler, etc.) et de leur logement (type de logement, type de construction, nombre de pièces, etc.). En plus des données à l’iris et au quartier, Filosofi est consultable sous forme de données carroyées. Les données individuelles ne sont évidemment pas mises à disposition de tous pour des raisons de respect de la confidentialité, mais elles peuvent être accessibles (sans les patronymes) aux chercheurs qui en font la demande _via_ le [Centre d’accès sécurisé des données](https://www.casd.eu/source/fichier-localise-social-et-fiscal/?tab=28) et après avis du [Comité du secret statistique](https://www.comite-du-secret.fr/). De nombreuses autres sources peuvent aussi être mobilisées pour caractériser les contours de bureau de vote, telles que le fichier des allocataires des caisses d’allocations familiales ou celui des inscrits à Pôle emploi par exemple.
Ces caractéristiques des électeurs à l’échelle des contours de bureaux de vote peuvent alors être mises en regard des résultats électoraux fournis par le [ministère de l’Intérieur et des Outre-mer](https://www.elections.interieur.gouv.fr/resultats/resultats-de-toutes-elections#resultatselectionspresidentielles) et disponibles en données ouvertes sur [data.gouv.fr](https://www.data.gouv.fr/fr/pages/donnees-des-elections/). Ces résultats portent sur les différentes élections (présidentielles, législatives, etc.) et sont souvent ventilés par bureaux de vote. Pour les élections présidentielles, elles contiennent pour chaque tour les résultats des différents candidats, le taux de participation, les votes blancs et nuls.
Ainsi, les données et les programmes _MapvotR_ mis à disposition par l’Insee simplifient l’étude du comportement électoral en fonction des caractéristiques des populations et des quartiers. Par exemple, on peut analyser la relation entre l’âge moyen des populations et les résultats d’un candidat ou d’un groupe de candidats aux élections présidentielles toutes choses égales par ailleurs (en contrôlant des effets liés aux revenus des habitants, à l’agglomération, etc.), la relation entre le niveau de vie de la population et la participation aux élections, l’existence (ou non) de traditions politiques locales indépendantes des caractéristiques socio-démographiques actuelles des populations, etc.
Par ailleurs, l’utilisateur dispose d’un nombre beaucoup plus grand d’observations à l’échelle des bureaux de vote qu’il n’en disposait à l’échelle communale. Les résultats économétriques sont donc nettement plus robustes.
## Un exemple : l’étude de la participation électorale en fonction du revenu
Prenons l’exemple du taux de participation au premier tour de l’élection présidentielle de 2022, en regard du niveau de vie médian en 2019 dans les 25 plus grandes communes françaises. La _figure 4b_ , disponible à l’échelle des bureaux de vote, confirme la relation forte entre niveau de vie et taux de participation au sein des villes étudiées. Chaque point sur la figure représente un bureau de vote : en général, plus le niveau de vie médian du contour du bureau de vote est élevé, plus les électeurs inscrits sur ce bureau se sont déplacés pour voter. Ce phénomène est moins visible à l’échelle communale du fait du faible nombre de points : chaque point représente ici une commune (_figure 4a_). Cette relation croissante entre niveau de vie et taux de participation, avec un plateau autour de 80 % de participation, se retrouve dans chacune des 25 villes étudiées (_figure 5_). De nouveaux territoires à explorer s’ouvrent donc pour la sociologie électorale. ■
### Figure 4 – Une forte corrélation entre niveau de vie et taux de participation électorale
_Sources : Insee REU, Filosofi 2019 ; ministère de l’Intérieur._
### Figure 5 – Un lien de corrélation semblable au sein de l’ensemble des communes étudiées
_Note : chaque courbe correspond, pour une commune donnée, à la tendance de la relation entre le taux de participation et le niveau de vie médian observée à l’échelle des bureaux de votes.Sources : Insee REU, Filosofi 2019 ; ministère de l’Intérieur._
## Pour en savoir plus
  * Bussi M., Colange C. et Freire-Diaz S ., Jadot A., 2010, « [Un outil d’analyse électorale en cours de création, un SIG au niveau des bureaux de vote français](http://www.lecfc.fr/new/articles/205-article-8.pdf) », Comité français de cartographie, CFC n° 125, septembre
  * Insee, 2023, «[ Guide du secret statistique ](https://www.insee.fr/fr/information/1300624)», avril
  * [fichier de correspondance entre les adresses des électeurs et les bureaux de vote](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/)
  * [package _MapvotR_](https://github.com/inseeFrLab/mapvotr)


_Crédits photo : © Chlorophylle – stock.adobe.com_
### Plus d'articles
###  [Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026](https://blog.insee.fr/premiers-resultats-du-rp-exhaustif-a-mayotte/ "Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026")
###  [Mayotte enfin comptée, et après ?](https://blog.insee.fr/mayotte-enfin-comptee-et-apres/ "Mayotte enfin comptée, et après ?")
###  [Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte](https://blog.insee.fr/le-recensement-2025-de-mayotte/ "Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte")
###  [Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?](https://blog.insee.fr/pourquoi-la-stat-publique-s-interesse-aux-logements/ "Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?")
###  [Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026](https://blog.insee.fr/premiers-resultats-du-rp-exhaustif-a-mayotte/ "Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026")
###  [Mayotte enfin comptée, et après ?](https://blog.insee.fr/mayotte-enfin-comptee-et-apres/ "Mayotte enfin comptée, et après ?")
###  [Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte](https://blog.insee.fr/le-recensement-2025-de-mayotte/ "Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte")
###  [Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?](https://blog.insee.fr/pourquoi-la-stat-publique-s-interesse-aux-logements/ "Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?")
###  [Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026](https://blog.insee.fr/premiers-resultats-du-rp-exhaustif-a-mayotte/ "Les premiers résultats du recensement exhaustif à Mayotte : 323 200 habitants au 1er janvier 2026")
###  [Mayotte enfin comptée, et après ?](https://blog.insee.fr/mayotte-enfin-comptee-et-apres/ "Mayotte enfin comptée, et après ?")
###  [Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte](https://blog.insee.fr/le-recensement-2025-de-mayotte/ "Carnet de bord d’une opération exceptionnelle : le recensement 2025 de Mayotte")
###  [Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?](https://blog.insee.fr/pourquoi-la-stat-publique-s-interesse-aux-logements/ "Mais pourquoi la statistique publique s’intéresse-t-elle à nos logements ?")
prev
next
⌛ 8 minutes
## Partager
## Auteurs/Autrices
  * Insee
  * Insee


Gérer le consentement

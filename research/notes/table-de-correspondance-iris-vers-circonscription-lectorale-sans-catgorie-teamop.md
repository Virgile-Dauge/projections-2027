---
title: 'Table de correspondance IRIS vers circonscription électorale? - Sans catégorie
  - #TeamOpenData'
id: table-de-correspondance-iris-vers-circonscription-lectorale-sans-catgorie-teamop
tags:
- projections-electorales-bureaux-2027-b0b1c4
- donnees-bureaux-vote
- crosswalk-iris
created: '2026-07-21T20:03:26.688214Z'
updated: '2026-07-21T21:14:01.555520Z'
source: https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125
source_domain: teamopendata.org
fetched_at: '2026-07-21T20:03:26.647986Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'TeamOpenData forum thread (May-June 2023) in which a civic-tech practitioner
  asks for an IRIS-to-legislative-circonscription correspondence table and is told
  none exists as a clean N:1 mapping: a member (''datageek'') recommends manually
  crossing IGN''s IRIS-GE contours with data.gouv.fr''s ''Contours détaillés des circonscriptions
  des législatives'' via GIS overlay, noting the boundaries ''coincide fairly well
  but not exactly'' and that the hardest step is choosing a method to redistribute
  the population of an IRIS split by a circonscription boundary (crude area-based
  redistribution is called out as the ''most hazardous'' option). This is the coarser
  IRIS→circonscription problem (not IRIS→bureau specifically), documented here as
  evidence that no official crosswalk existed pre-2023 and that practitioners independently
  converged on the same area/population-weighted GIS-overlay approach later formalized
  in the 2024 IRIS/bureau liaison table.'
---

[Passer au contenu principal](https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125#main-container)
  * [ Sujets  ](https://teamopendata.org/latest "Tous les sujets")


​  Catégories 
  * [ Veille  ](https://teamopendata.org/c/veille/5)
  * [ Toutes les catégories  ](https://teamopendata.org/categories)


​  Étiquettes 
  * [ opendata  ](https://teamopendata.org/tag/opendata)
  * [ collectivités  ](https://teamopendata.org/tag/collectivit%C3%A9s)
  * [ recherche  ](https://teamopendata.org/tag/recherche)
  * [ emploi  ](https://teamopendata.org/tag/emploi)
  * [ événement  ](https://teamopendata.org/tag/%C3%A9v%C3%A9nement)
  * [ Toutes les étiquettes  ](https://teamopendata.org/tags)


#  [ Table de correspondance IRIS vers circonscription électorale? ](https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125)
vous avez sélectionné **0** message.
[ tout sélectionner ](https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125)
[ annuler la sélection ](https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125)
mai 2023 
1/20 
mai 2023 
19 juin
Hello,
J’ai cherché sans trouver une table de correspondance de l’IRIS vers la circonscription législative. Est-ce quelqu’un a une idée de où (si) je pourrais trouver ça, ou à défaut, trouver un autre moyen de faire correspondre des IRIS avec des circonscriptions législatives ?
Merci d’avance 
  * #### créé
mai 2023 
  * #### [dernière réponse 19 juin  ](https://teamopendata.org/t/table-de-correspondance-iris-vers-circonscription-electorale/4125/20)
  * 19
#### réponses
  * 2,4 k
#### vues
  * 5
#### utilisateurs
  * 7
#### J'aime


datageek
Il me semble qu’il n’y a pas de correspondance N → 1 entre les deux, ce serait trop simple.
Les IRIS sont ici: [IRIS... GE | Géoservices 9](https://geoservices.ign.fr/irisge) Les circo ici: [Contours détaillés des circonscriptions des législatives - data.gouv.fr 24](https://www.data.gouv.fr/fr/datasets/contours-detailles-des-circonscriptions-des-legislatives/)
Reste plus qu’à faire un croisement géographique entre les deux… et voir là où ça coince !
Effectivement, c’est à peu près là que je me suis arrêté et que j’ai posté en espérant que quelqu’un avait déjà passé cette étape Visiblement, ça sera moi ! Merci pour ton retour en tout cas, c’est sympa.
datageek
Cela dit, ça coïncide quand même pas mal, à quelques détails près…
[ Capture d’écran du 2023-05-31 21-39-301070×1326 132 KB ](https://teamopendata.org/uploads/default/original/2X/c/cb5d6e312a899aa534a72220d7756c6e5ed92755.png "Capture d’écran du 2023-05-31 21-39-30")
Rouge: IRIS GE Noir: circonscriptions législatives
Le pointillé rouge sans noir indique une différence.
Le plus difficile étant de choisir la méthode pour redistribuer la population d’un iris coupé par une limite de circonscriptions. La plus hasardeuse consiste à le faire en fonction de la surface de l’iris. Mais la moitié d’un Iris peut très bien n’accueillir que 2% de la population.
Le bon compromis c’est d’ajouter le carroyage 200m de l’Insee, pour savoir combien d’habitants compte chaque partie de l’Iris. J’avais fait ce choix dans le cadre d’une enquête data pour Médiacités, pour définir le profil social des habitants de chaque secteur de collège. Mon notebook python est [disponible ici 5](https://github.com/Denis-Vannier/colleges_mediacites_lille/blob/main/PROFILS_SOCIAUX_2019_SECTEURS_COLLEGES_LILLE.ipynb).
datageek
Tout dépend de ce qu’on veut faire, mais oui, si c’est pour reprendre les données INSEE à l’IRIS et les croiser avec les circonscriptions, c’est une bonne méthode.
C’est celle que j’ai utilisé pour le projet Datacirco à l’Assemble Nationale pour les données sur la population, le logement, etc.
Pour info, au delà des PDF, il y a les données agrégées qui sont téléchargeables (CSV, etc).
Ok je vois, merci beaucoup à vous deux [@cquest](https://teamopendata.org/u/cquest) et [@DenisVannier](https://teamopendata.org/u/denisvannier) ! Je vous tiens au courant 
datageek
Pour la matrice de poids de transition entre les découpages insee et des découpages électoraux, on peut également utiliser le nombre d’électeurs, qu’on connaît grâce aux listes électorales. L’INSEE et le Ministère de l’intérieur devraient publier sous peu (mais bon, j’ai appris à me méfier, vu l’absence de suites données à cette demande de 2020 : [Extraction de la correspondance adresses/bureaux de vote du REU - Une demande d'accès à l'information à Institut national de la statistique et des études économiques - Ma Dada 4](https://madada.fr/demande/extraction_de_la_correspondance)…) une agrégation du Répertoire électoral unique (REU), donnant les adresses uniques correspondant à chaque bureau de vote. On peut espérer qu’ils y incluront également le nombre d’électeurs inscrits correspondant… Pour voir un exemple d’utilisation de la liste électorale pour construire une matrice de poids de transition entre deux découpages, voir :
[http://joelgombin.github.io/makingof.html 5](http://joelgombin.github.io/makingof.html)
datageek
D’après les dernières infos, il n’y aura que le lien adresse / bureau de vote, pas le nombre d’inscrits… ce qui rend ce jeu de donnée fort peu intéressant.
Il veulent organiser un hackathon avec juste ça… bonne chance !
datageek
ça reste le plus essentiel (sans ça on ne peut pas calculer les périmètres des BV) mais c’est dommage en effet de se priver de cette information qui ne coûte pas plus cher mais serait très utile…
J’imagine que quelqu’un qui aurait obtenu les listes électorales pourrait le faire assez facilement à partir de la prochaine publication de l’INSEE et Ministère de l’Intérieur, puis publier ça en licence libre ? Il suffirait juste de compter le nombre de lignes pour chaque bureau de vote, ce qui n’est pas compliqué dès lors qu’il y a une correspondance adresse + bureau de vote. Évidemment les listes évoluent avec le temps, mais pas non plus de manière fondamentale, donc ça serait déjà une bonne base.
En tout cas, merci [@joel](https://teamopendata.org/u/joel) pour ta solution détaillée, je n’ai pas encore accès aux données donc difficilement pour l’instant de voir comment je pourrai mettre cela en oeuvre, mais ça reste dans un coin de ma tête 
Excellente nouvelle, ce projet de publication. On peut maintenant envisager un cartographie des bureaux de vote pour l’ensemble de la France. Reste que la définition des périmètres implique pas mal de nettoyage manuel (certains électeurs sont domiciliés en plein milieu d’un autre secteur de vote, pour plein de raisons, ce qui complique les traitements automatiques) Et quelques communes n’ont pas encore compris que la répartition des électeurs se fait une base géographique et pas alphabétique, et la préfecture ne vérifie pas toujours (on vous voit la Haute-Garonne…). Le nombre d’électeurs par adresse permettait justement de régler une partie du problème.
datageek
Quand la répartition est géographique… ce qui n’est pas systématique, et quand elle l’est ce n’est pas forcément par un zonage polygonal (répartitions par rue entières, qui se croisent).
Petite commune avec 2 bureaux… l’un de A à M et l’autre de N à Z, les deux dans la même école…
Il n’y a aucune règle pour la répartition si ce n’est de limiter le nombre d’électeurs par bureaux à environ un millier.
Alors si, c’est bien ce que prévoit le code électoral (article L16), et c’est redit dans une circulaire du 17 janvier 2017. Dans plusiers préfectures, les fonctionnaires en charge des élections m’ont confirmé qu’ils doivent vérifier que les bureaux de vote définis par les maires correspondent à des périmètres géographiques. Et si un électeur déménage au sein de la commune, il est aussi amené à changer de bureau de vote.
Les préfectures demandent donc aux communes de leur adresser des cartes de leurs bureaux de vote et pas seulement une liste de noms. Mais dans la pratique, certaines communes « oublient » de transmettre la carte ou le descriptif des périmètres et la préfecture n’insiste pas. (C’est le cas par exemple à Fonsorbes, près de Toulouse, où un bureau de vote a été redécoupé sur une base alphabétique. Ca passe, tant qu’on ne s’amuse pas à géolocaliser les électeurs).
Sur la dizaine de département que j’ai traitée, la règle des périmètres (même s’il peut y avoir des multi-polygones), est bien respectée. Ce qui l’est moins, c’est le cas des électeurs qui déménagent à l’intérieur de la commune mais restent rattachés à leur ancien bureau de vote…
datageek
C’est en effet nouveau… depuis la modification de 2016 et en vigueur que depuis 2019.
Pas sûr que les listes électorales aient toutes été revues !
À confirmer, mais on peut peut-être espérer qu’avec la mise en oeuvre du répertoire électoral unique, les préfectures aient fait un petit coup de ménage dans les listes ?
16 jours plus tard
Pour information, la base de données évoquée ci-dessus vient de sortir : [Bureaux de vote et adresses de leurs électeurs - data.gouv.fr 16](https://www.data.gouv.fr/fr/datasets/bureaux-de-vote-et-adresses-de-leurs-electeurs/).
3 ans plus tard
C’est enfin le Noël des IRIS :
J’ai construit la liaison en passant par les carreaux de 200 mètres FiLoSoFi, afin de pallier au risque mentionné ici.
Le jeu sera relativement facile à actualiser une fois que ( / si …) l’Insee actualise son jeu des contours des bureaux de vote à partir du Répertoire électoral unique de 2026.
2 mois plus tard
datageek
ah tiens de mon côté pour les besoins de [https://andre.vote 7](https://andre.vote) j’ai produit ma propre correspondance avec une méthodologie différente, quand j’aurai un peu de temps je comparerai pour voir si ça converge !
1 mois plus tard
datageek
j’ai publié ces données ici : [Jeu de données - Profil sociodémographique des bureaux de vote — France métropolitaine (INSEE RP 2022 & Filosofi 2021) | data.gouv.fr 5](https://www.data.gouv.fr/datasets/profil-sociodemographique-des-bureaux-de-vote-france-metropolitaine-insee-rp-2022-filosofi-2021)
Le coeffficient de corrélation entre mes poids et ceux de [@jeremy.perrin](https://teamopendata.org/u/jeremy.perrin) est de 0.94, c’est donc très convergent. L’écart le plus fort est en milieu urbain, là où il y a de grands ensembles (puisque je m’appuie sur le nombre de logements).
Répondre
###  Sujets nouveaux et non lus   
|  Sujet  |  Réponses  |  Vues  |  Activité  |  
| --- | --- | --- | --- |  
|  [3 ans pour l’instance Panoramax d’OSM France qui lance un appel aux dons](https://teamopendata.org/t/3-ans-pour-linstance-panoramax-dosm-france-qui-lance-un-appel-aux-dons/4941)  |  
|  [Identifiants SITADEL <-> parcelle cadastrale](https://teamopendata.org/t/identifiants-sitadel-parcelle-cadastrale/4976)  |  
|  [Du temps passé devant le tribunal](https://teamopendata.org/t/du-temps-passe-devant-le-tribunal/4957)  |  
|  [Package Python pour les données de la justice administrative](https://teamopendata.org/t/package-python-pour-les-donnees-de-la-justice-administrative/4922)  |  
|  [Enquête sur les usages et besoins en IA dans les TPE/PME](https://teamopendata.org/t/enquete-sur-les-usages-et-besoins-en-ia-dans-les-tpe-pme/4966)  |  
###  Vous voulez en savoir plus ? [Parcourez toutes les catégories](https://teamopendata.org/categories) ou [affichez les derniers sujets](https://teamopendata.org/latest). 
​ Invalid date  ​ Invalid date 

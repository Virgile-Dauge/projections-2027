---
title: Ce qui explique vraiment les différences de vote RN entre les villes et les
  campagnes | Alternatives économiques
id: ce-qui-explique-vraiment-les-diffrences-de-vote-rn-entre-les-villes-et-les-campa
tags:
- projections-electorales-bureaux-2027-b0b1c4
- methodologie-regression
- alternatives-economiques
- gradient-urbanite
created: '2026-07-21T18:37:27.598433Z'
updated: '2026-07-21T18:39:17.819968Z'
source: https://www.alternatives-economiques.fr/explique-vraiment-differences-de-vote-rn-entre-villes-cam/00111777
source_domain: www.alternatives-economiques.fr
fetched_at: '2026-07-21T18:37:27.562703Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Olivier Bouba-Olga (géographe, Univ. Poitiers) & Vincent Grimault, Alternatives
  Économiques (2024) — méthodologie indépendante (régression multivariée à l''échelle
  des intercommunalités, pas des bureaux de vote) qui corrobore la conclusion de Souidi
  & Vonderscher : l''écart brut de vote RN entre rural et urbain aux législatives
  2024 (10,9 points) tombe à seulement 1,3 point pour le rural et 3 points pour le
  périurbain une fois neutralisés les effets de composition sociale (âge, CSP, diplôme,
  revenu, mobilité domicile-travail). Modèle testé sur 4 blocs (gauche/centre/droite/extrême
  droite) avec variables socio-démographiques par intercommunalité ; le modèle explique
  72% des différences intercommunales de vote RN. Électorat-type RN : faible part
  de jeunes 15-29 ans, forte part de 60-74 ans, forte part d''ouvriers/retraités,
  faible part de cadres sup., forte part de CAP/BEP, faible part de diplômés du supérieur,
  déplacements domicile-travail en voiture, faibles inégalités de revenu intra-territoriales.
  Persistance d''un effet périurbain net de 3 points (spécificité propre au périurbain,
  plus fort que le rural isolé une fois contrôlé) attribué à des enjeux d''accessibilité
  aux services. Invalide la ''théorie du gradient d''urbanité'' (l''altérité urbaine
  rendrait plus tolérant) au profit d''une explication sociale (diplôme, CSP, âge).
  Cartographie les écarts résiduels (RN sur/sous-performant p/r à la sociologie locale)
  : sous-représentation dans le sud, surreprésentation dans le nord — signale des
  facteurs historiques/politiques non capturés par le modèle socio-démographique.
  Note méthodologique complète disponible en PDF : https://blogs.univ-poitiers.fr/o-bouba-olga/files/2024/07/Note-m%C3%A9thodo.pdf'
---

*Suggested by [[la-france-politique-de-2024-portrait-gographique-et-social-fondation-jean-jaurs]] — Alternative methodology (Bouba-Olga & Grimault) cross-checking the same RN-vote-by-commune-type finding*

[ Aller au contenu principal](https://www.alternatives-economiques.fr/ce-qui-explique-vraiment-les-differences-de-vote-rn-entre-les-villes-et-les-campagnes#main-content)
Affiches de campagne pour les élections législatives à Saint-Hilaire-de-Clisson (Loire-Atlantique) le 22 juin 2024. © Mathieu Thomasset - Hans Lucas/AFP
Les différences géographiques de vote continuent à défrayer la chronique, avec toujours la même tendance à opposer vote des villes et vote des champs, sans analyser plus en détail l’origine de ces différences.
Incontestablement, si l’on regarde les résultats bruts et que l’on prend des grands agrégats, le vote pour le Rassemblement national (RN) semble d’autant plus fort que l’on s’éloigne des centres-ville.
Ainsi, si l’on regroupe les listes présentes au premier tour des élections législatives 2024 en quatre grands blocs (gauche, centre, droite, extrême droite), et qu’on observe les scores électoraux à l’échelle des communes en les classant entre territoires urbains, périurbains et ruraux sur la base de la grille communale de densité, on obtient des résultats très différents d’un type de territoire à l’autre.
###  Résultats bruts : l'extrême droite domine nettement dans le périurbain et le rural
Moyenne des scores obtenus par les différents blocs politiques au premier tour des élections législatives de 2024, selon le type de territoire, en %
Source : ministère de l'Intérieur, calculs Olivier Bouba-Olga
© Alternatives Économiques
Voir les données en plein écran Voir les données en plein écran Fermer
Les scores du bloc de gauche sont plus élevés dans l’urbain et plus faibles dans le rural, avec peu de différences entre périurbain et rural. C’est l’inverse pour le bloc de l’extrême droite.
Le centre et la droite obtiennent des scores plus homogènes pour les différentes densités des territoires. Le centre, comme la gauche, réussit mieux en ville qu’à la campagne, mais avec des écarts moindres. La droite, elle, a un profil similaire à l’extrême droite… mais de façon nettement moins prononcée.
L’âge, la CSP et le diplôme déterminants
Marine Le Pen serait-elle donc la reine incontestée des champs et Mélenchon le roi des villes ? Ce genre de raisonnement est trompeur, car il postule que le territoire voterait. Or, ce ne sont pas les hectares ou « l’esprit du territoire » qui glissent un bulletin dans l’urne, mais bien des électeurs en chair et en os. Pour mesurer ce que le territoire fait (ou pas) comme différence, il faut neutraliser ce que les géographes appellent les effets de composition sociale.
Prenons un exemple : on sait que le fait de détenir (ou pas) un diplôme est décisif en matière de vote. [Plus on est diplômé, moins on vote RN et plus on vote à gauche](https://www.alternatives-economiques.fr/8-graphiques-comprendre-resultats-elections-legislatives-2024/00111621). Or, la répartition des diplômés est très inégale en France : ils sont surreprésentés en ville et sous-représentés à la campagne. Pour connaître l’effet propre du territoire sur le vote, il faut donc neutraliser tous ces effets de composition. Mais avant de les neutraliser, il faut déjà… les identifier !
Pour ce faire, nous avons testé plusieurs variables socio-économiques relatives à l’âge, la CSP (catégorie socioprofessionnelle), le diplôme, le revenu et la mobilité sur les scores électoraux des quatre principaux blocs dans les intercommunalités françaises. Cela permet de distinguer l’influence propre de chaque variable, indépendamment de celle des autres. Les lecteurs les plus intéressés par la méthodologie pourront r[etrouver ici une courte note qui la détaille.](https://blogs.univ-poitiers.fr/o-bouba-olga/files/2024/07/Note-m%C3%A9thodo.pdf "\(s'ouvre dans une nouvelle fenêtre\)")
Electorat type
Cet exercice statistique permet de dresser un « électorat type » pour chaque bloc.
Pour l’extrême droite, le score est d’autant plus important que les intercommunalités regroupent une part faible de jeunes (15-29 ans) et une part forte de personnes âgées (60-74 ans), que la part des ouvriers et des retraités est élevée et celle des cadres supérieurs est faible, que la proportion de personnes diplômées de CAP ou de BEP est forte et que celle de diplômés du supérieur est faible, que les déplacements domicile-travail se font en voiture et que les inégalités de revenu au sein du territoire sont faibles.
Pour le bloc de gauche, les résultats sont à l’exact inverse : les variables socio-économiques qui ont des effets très positifs sur le vote d’extrême droite exercent des effets très négatifs pour le bloc de gauche, et inversement. Une petite différence pour la structure par âge apparaît, avec un effet plus fort de la part des 45-59 ans, qui joue négativement sur le vote de gauche.
Pour la majorité présidentielle (bloc du centre), les coefficients sont plus faibles. Difficile ici d’établir des corrélations certaines. Cependant, on peut noter que les coefficients qui ressortent le plus correspondent à des territoires au niveau de vie élevé, au taux de pauvreté faible, où la part des diplômés du supérieur est importante et celle des non-diplômés faible.
Maintenant que les variables les plus décisives sont identifiées, l’enjeu est de mesurer leur influence sur les écarts entre vote des villes et vote des champs. Les différences de structure par âge et de niveaux de diplômes entre rural et urbain, notamment, expliquent-elles ou non, en totalité ou en partie, les différences géographiques de scores de l’extrême droite ?
En neutralisant les effets de composition sociale, le résultat principal que nous obtenons est le suivant : l’écart brut entre rural, périurbain et urbain, présenté dans le graphique ci-dessus, de l’ordre de 11 points de pourcentage, tombe à 1,3 point pour le rural et à 3 points pour le périurbain ! Il est donc très sensiblement réduit. Concrètement, cela signifie que les écarts de vote entre rural et urbain sont pour une large part le résultat d’effets de composition sociale.
###  Corrigé de la composition sociale, l'écart urbain-rural est très faible
Ecart brut et net entre les résultats électoraux des villes, des campagnes et du périurbain pour le vote de l'extrême droite aux législatives de 2024, en points de pourcentage
Au premier tour des élections législatives de 2024, l'extrême droite a obtenu des scores "bruts" supérieurs de 10,9 points dans le rural par rapport aux territoires urbains. Mais une fois neutralisés les effets de composition sociale, l'écart n'est plus que de 1,3 point.
Source : ministère de l'Intérieur, calculs Olivier Bouba-Olga 
© Alternatives Économiques
Voir les données en plein écran Voir les données en plein écran Fermer
Deuxième résultat, on observe une spécificité périurbaine supérieure à celle du rural : l’effet « net » du territoire est encore de 3 points après correction de la composition sociale, ce qui n’est pas rien. Il semble donc que vivre dans le périurbain, pousse, toutes choses égales par ailleurs, à voter davantage RN que dans les campagnes isolées ou en ville.
Les classes moyennes et populaires se sont déplacées
Comment expliquer ces résultats ? Si le vote des villes et le vote des champs sont essentiellement affaire de composition sociale, y répondre suppose d’expliquer pourquoi la composition sociale de ces territoires diffère autant. Une partie de l’explication tient sans doute à l’évolution combinée des marchés du travail et des marchés du foncier : on observe une concentration forte des emplois les plus qualifiés dans les plus grandes villes, occupés par des cadres supérieurs qui y résident et qui sont les moins enclins à voter Rassemblement national.
Les classes moyennes et populaires, de leur côté, qui se sont mises à voter de plus en plus pour le RN, se sont déplacées – par contrainte ou par choix – en dehors du cœur des villes pour accéder à la propriété, certaines dans le périurbain, d’autres dans le rural plus isolé, avec en contrepartie, pour un grand nombre d’entre elles, un allongement des trajets domicile-travail à parcourir en voiture.
Ajoutons à cela que, si l’écart du vote rural/urbain est fortement réduit par la prise en compte de la composition sociale, il n’est pas annulé. Plusieurs facteurs pourraient être avancés pour expliquer l’écart : par exemple les problèmes d’accessibilité à l’ensemble des services et équipements (santé, éducation, commerces, loisirs…), plus prégnants dans le périurbain et dans le rural.
Les classes moyennes et populaires qui y sont localisées disent régulièrement que ces problèmes d’accessibilité aux services, de dévitalisation de certains centres-ville, entraînent chez elles un sentiment d’abandon, ce qui peut renforcer encore leur choix de l’extrême droite, qui surfe sur leur mal-être en accusant les immigrés ou les « assistés » de profiter des mannes de l’action publique à leur détriment.
Enfin, d’autres variables restent à observer. Notre modèle économétrique, qui ne comprend qu’un petit nombre de variables, est relativement bien indicatif : il « explique » 72 % des différences intercommunales de vote. Pour autant, ce n’est pas 100 %, ce qui signifie que certaines communes s’écartent du modèle, avec un score sensiblement plus élevé, ou à l’inverse plus faible que ce que prédit le modèle compte tenu de la structure par âge, par diplôme, de l’appartenance régionale et du degré de ruralité de la commune. La carte ci-dessous permet de les repérer.
###  Ces territoires où le RN surperforme ou sous-performe par rapport à la sociologie des habitants
Score de l'extrême droite au premier tour des élections législatives, selon qu'il est inférieur ou supérieur à ce que les caractéristiques sociales des populations des territoires laissent attendre en moyenne, par commune
Source : Résultats fournis par le ministère de l’Intérieur, calculs Olivier Bouba-Olga
© Alternatives Économiques
Voir les données en plein écran Voir les données en plein écran Fermer
On observe une distinction claire entre le sud du pays, où dominent les sous-représentations, et la partie nord, où les surreprésentations sont plus importantes. A ce stade, la statistique doit passer le relais aux sciences humaines : histoire politique, histoire économique, tissu industriel, relations sociales… de nombreuses variables explicatives entrent en jeu.
Toutes ces analyses sont-elles utiles ? Notre conviction est que oui. Le fait de montrer que le vote dépend de caractéristiques sociales plus que du lieu de vie permet d’invalider les interprétations en termes de gradient d’urbanité, très souvent reprises, plus ou moins consciemment, dans les médias.
Cette « théorie » du gradient d’urbanité consiste à affirmer que le vote d’extrême droite est plus fort dans le rural parce que les électeurs y sont moins confrontés à l’altérité, ce qui conduit à s’enfermer et à adhérer aux thèses des partis populistes. A l’inverse, vivre dans l’urbain conduirait ses habitants à interagir avec un ensemble de personnes différentes, les rendant plus tolérantes et moins enclines à céder aux votes extrêmes. Cette dimension n’est probablement pas complètement saugrenue dans certains choix individuels.
Mais cette étude, comme de nombreuses autres, montrent que cette théorie explique très mal ce qui se joue vraiment : ce sont les diplômes, la catégorie sociale et l’âge qui comptent, bien plus que la localisation dans le rural ou dans l’urbain.
Enfin, en termes de politiques publiques, la surreprésentation du vote pour l’extrême droite dans le périurbain par rapport au rural et à l’urbain pose la question de l’action publique à destination de ces territoires intermédiaires, sans doute trop oubliés.
Notes de bas de page
## Notes
Fermer
  * 1
Le bloc de gauche rassemble les listes suivantes : Extrême gauche, Parti communiste français, La France insoumise, Parti socialiste, Parti radical de gauche, Les Ecologistes, Divers gauche, Union de la gauche, Ecologistes.
  * 2
Le bloc du centre rassemble les listes suivantes : Renaissance, Modem, Horizons, Ensemble, Divers centre, Union des démocrates et indépendants.
  * 3
Le bloc de droite rassemble les listes suivantes : Les Républicains, Divers droite.
  * 4
Le bloc extrême droite rassemble les listes suivantes : Droite souverainiste, Rassemblement national, Reconquête, Union de l’extrême droite, Extrême droite
  * 5
Communes denses ou de densité intermédiaire.
  * 6
Pour cette catégorie, on utilise la catégorie de l’Insee « rural sous influence ». Elle désigne les communes peu denses situées dans une aire d’attraction des villes de 50 000 habitants ou plus.
  * 7
Pour cette catégorie, on utilise la catégorie de l’Insee « rural autonome ». Elle désigne les communes peu denses hors aire d’attraction des villes ou appartenant à une aire de moins de 50 000 habitants.
  * 8
Voir cet article pour des précisions sur la définition du rural et de l’urbain à partir de la grille communale de densité : https://geoconfluences.ens-lyon.fr/actualites/eclairage/grille-densite-zonage-aires-urbaines-definition-rural



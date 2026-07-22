---
title: 'Note méthodologique concernant l’article : « Vote RN : ce qui'
id: note-mthodologique-concernant-larticle-vote-rn-ce-qui
tags:
- projections-electorales-bureaux-2027-b0b1c4
- methodologie-regression
- correlation-socio-demo
- donnees-communales
created: '2026-07-21T18:38:29.186725Z'
updated: '2026-07-21T18:39:17.834827Z'
source: https://blogs.univ-poitiers.fr/o-bouba-olga/files/2024/07/Note-m%C3%A9thodo.pdf
source_domain: blogs.univ-poitiers.fr
fetched_at: '2026-07-21T18:38:29.186514Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Olivier Bouba-Olga, note méthodologique complète (juillet 2024, Université
  de Poitiers) détaillant la régression sous-jacente à l''article Alternatives Économiques
  sur vote RN villes/campagnes. Fournit le tableau complet des coefficients de corrélation
  simple entre variables socio-démographiques par intercommunalité et scores des 4
  blocs politiques (législatives 2024, 1er tour) : corrélations extrême droite les
  plus fortes avec CAP/BEP (+0,72), déplacement domicile-travail en voiture (+0,72),
  diplômés du supérieur (-0,78), cadres sup. (-0,76), part 15-29 ans (-0,60), rapport
  interdécile de revenu (-0,60), part ouvriers (+0,57), part 60-74 ans (+0,51). Régression
  économétrique au niveau commune (variable expliquée : score extrême droite, référence
  = urbain) : rural autonome +1,3 point, rural sous influence (périurbain) +3,0 points,
  part 15-29 ans -0,4, part diplômés du supérieur -0,8, avec effets fixes régionaux
  marqués (Hauts-de-France +10,2, PACA +12,7, Bretagne -8,8, Pays de la Loire -6,3,
  Corse -6,5) — variance expliquée totale 72%. Tableau 1 des scores bruts par type
  de commune : extrême droite 31,0% en urbain, 42,2% en rural sous influence, 41,9%
  en rural autonome (écart brut ~11 points, réduit à 1,3-3 points net des effets de
  composition sociale). Confirme le rôle prépondérant de la composition socio-démographique
  locale (diplôme, CSP, âge, mobilité) sur l''effet géographique brut, avec un résidu
  régional non expliqué encore substantiel (jusqu''à +12,7 points en PACA).'
raw_file: raw/note-mthodologique-concernant-larticle-vote-rn-ce-qui.pdf
---

*Suggested by [[ce-qui-explique-vraiment-les-diffrences-de-vote-rn-entre-les-villes-et-les-campa]] — Full methodological note for the intercommunalité-level regression cited by the Alternatives Économiques article*

Note méthodologique concernant l’article : « Vote RN : ce qui 
explique vraiment les différences villes – campagnes » 
 
Dans l’article, nous tentons d’identifier des liens éventuels entre des variables socio-économiques 
relatives à l’âge, la CSP, le diplôme, le revenu et la mobilité, et aux scores des 4 principaux blocs 
(Gauche, centre, droite, extrême droite). Pour cela, nous avons calculé des coefficients de corrélation, 
qui varient entre -1 et +1. Plus ils sont proches de 1, plus la relation est forte et positive, plus ils sont 
proches de -1, plus la relation est forte et négative. Quand les coefficients s’approchent de 0, il n’y a 
pas de relation statistique. On peut retenir un seuil de +0,5 (ou de -0,5) pour se focaliser sur les 
corrélations les plus importantes. Les coefficients qui sont dans ce cas sont en gras dans le tableau. 
Coefficients de corrélation simple 
Score des 4 principaux blocs 
Gauche 
Centre 
Droite Extrême-
Droite 
Structure par âge 
part 15-29 ans 
0.63 
0.21 
-0.14 
-0.60 
part 30-44 ans 
0.44 
0.15 
-0.07 
-0.46 
part 45-59 ans 
-0.56 
-0.15 
0.14 
0.49 
part 60-74 ans 
-0.51 
-0.18 
0.10 
0.51 
part 75 ans et plus 
-0.39 
-0.13 
0.09 
0.37 
Catégories socio-professionnelles 
part agriculteurs 
-0.38 
-0.12 
0.15 
0.30 
part artisans, commerçants, chefs d'entreprise 
-0.25 
-0.09 
0.06 
0.21 
part ouvriers 
-0.56 
-0.25 
0.19 
0.57 
part employés 
-0.02 
-0.17 
-0.04 
0.17 
part professions intermédiaires 
0.32 
0.23 
-0.11 
-0.38 
part cadres sup. 
0.64 
0.34 
-0.10 
-0.76 
part retraités 
-0.54 
-0.15 
0.11 
0.51 
Niveaux de diplôme 
non diplômés 
-0.44 
-0.40 
0.15 
0.61 
CAP, BEP 
-0.68 
-0.26 
0.14 
0.72 
niveau bac 
-0.32 
-0.16 
-0.04 
0.38 
diplômés du supérieur 
0.66 
0.37 
-0.15 
-0.78 
Mobilités 
déplacement domicile-travail en voiture 
-0.67 
-0.20 
0.04 
0.72 
actifs occupés travaillant dans une autre commune 
-0.21 
-0.05 
0.08 
0.19 
temps de trajet domicile-travail 
-0.36 
-0.14 
-0.04 
0.41 
actifs occupés à plus de 30 minutes du travail 
-0.33 
-0.15 
0.04 
0.40 
Niveau et inégalités de revenu 
revenu disponible médian 
0.15 
0.34 
0.02 
-0.44 
rapport interdécile de revenu 
0.57 
0.15 
-0.05 
-0.60 
taux de pauvreté 
0.32 
-0.22 
-0.11 
-0.02 


---

Seuls les blocs de gauche et de l’extrême-droite sont concernées, les coefficients prennent des 
valeurs sensiblement plus faibles pour le centre et la droite. 
Pour l’extrême-droite, le score est d’autant plus fort que les intercommunalités regroupent une part 
faible de jeunes (15-29 ans) et une part forte de 60-74 ans, que la part des ouvriers et des retraités 
est forte et celle des cadres supérieurs est faible, que la proportion de personnes diplômés de CAP ou 
de BEP est forte et que ceux de diplômés du supérieur est faible, que les déplacements domicile-
travail se font en voiture et que les inégalités de revenu au sein du territoire sont faibles. 
Pour le bloc de gauche, les résultats sont à l’exact inverse : les effets très positifs de l’extrême droite 
exercent des effets très négatifs pour le bloc de gauche, et inversement. Une petite différence pour la 
structure par âge apparaît, avec un effet plus fort de la part des 45-59 ans, qui joue négativement sur 
le vote de gauche. 
Pour la majorité présidentielle (bloc du centre), les coefficients sont plus faibles, mais ceux qui 
ressortent le plus (supérieurs à 0,3) correspondent à des territoires au niveau de vie élevé, au taux de 
pauvreté faible, où la part des diplômés du supérieur est importante et celle des non-diplômés faible. 
En complément, nous proposons de réinterroger la question rural-urbaine, en nous situant 
maintenant à l’échelle des communes, l’idée étant de définir l’urbain, le périurbain et le rural sur la 
base de la grille communale de densité1. 
 
urbain : communes denses ou de densité intermédiaire 
 
rural sous influence : communes peu denses situées dans une aire d’attraction des villes de 
50 000 habitants ou plus 
 
rural autonome : communes peu denses hors aire d’attraction des villes ou appartenant à une 
aire de moins de 50 000 habitants. 
Nous approchons ainsi respectivement les territoires urbains, périurbains (rural sous influence) et 
ruraux (rural autonome). Quand on compare les scores bruts des 4 principaux blocs, on observe 
des différences très importantes. 
Tableau 1 : moyenne des scores des différents blocs par type de commune 
dominante 
Gauche 
Centre 
Droite 
Extrême-Droite 
urbain 
35.6 
26.1 
11.2 
31.0 
rural sous influence 
24.8 
24.8 
14.8 
42.2 
rural autonome 
24.2 
23.1 
18.0 
41.9 
Total 
31.3 
25.4 
13.0 
35.2 
Les scores du bloc de gauche sont plus élevés dans l’urbain et plus faibles dans le rural, avec peu de 
différence entre rural sous influence et rural autonome. C’est l’inverse pour le bloc de l’extrême-
droite. Pour le centre et la droite, les différences entre les deux types de territoires ruraux sont un 
peu plus marquées, mais inversés : score plus élevé dans l’urbain, intermédiaire pour le rural sous 
influence et plus faible dans le rural autonome pour le bloc du centre, c’est l’inverse pour le bloc de 
droite.  
 
1 Voir cet article pour des précisions sur la définition du rural et de l’urbain à partir de la grille communale de 
densité : 
https://geoconfluences.ens-lyon.fr/actualites/eclairage/grille-densite-zonage-aires-urbaines-
definition-rural  


---

Ces différences géographiques peuvent cependant être le produit des différences socio-économiques 
identifiées plus haut. Elles peuvent également être le résultat de différences régionales, plus que de 
différences rural-urbain. Pour en juger, nous avons estimé les scores à la commune de l’extrême 
droite sur un ensemble de variables d’intérêt : le caractère urbain, rural autonome ou rural sous 
influence de la commune, leur structure par âge et par diplôme, et leur appartenance régionale.  
Tableau 2 : analyse économétrique des scores de l’extrême-droite 
variable expliquée : score extrême-droite 
Urbain 
réf. 
Rural autonome 
1.3 
Rural sous influence 
3.0 
Part des 15-29 ans 
-0.4 
Part des 65 ans et plus 
-0.1 
Part des non-diplômés 
-0.6 
Part des diplômés du supérieur 
-0.8 
Auvergne-Rhône-Alpes 
réf. 
Bourgogne-Franche-Comté 
2.2 
Bretagne 
-8.8 
Centre-Val de Loire 
1.1 
Corse 
-6.5 
Grand Est 
3.3 
Hauts-de-France 
10.2 
Normandie 
0.3 
Nouvelle-Aquitaine 
-2.4 
Occitanie 
5.1 
Pays de la Loire 
-6.3 
Provence-Alpes-Côte d'Azur 
12.7 
Île-de-France 
-1.5 
variance expliquée 
72% 
Le résultat principal que nous obtenons est le suivant : l’écart brut entre rural autonome ou rural sous 
influence et urbain observé dans le tableau 1, de l’ordre de 11 points de pourcentage, tombe à 1,3 
point pour le rural autonome et à 3 points pour le rural sous influence. Il est donc très sensiblement 
réduit, les écarts de vote entre rural et urbain sont pour une large part le résultat d’effets de 
composition sociale. Deuxième résultat, cette réduction est plus forte dans le rural autonome que 
dans le rural sous-influence, l’écart de 3 points reste non négligeable, les effets de composition 
sociale n’expliquent pas tout. 
Olivier Bouba-Olga 

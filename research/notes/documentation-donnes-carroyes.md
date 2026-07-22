---
title: DOCUMENTATION – données carroyées
id: documentation-donnes-carroyes
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-implementation-bureau-ei-et-covariables
- insee-filosofi
- donnees-carroyees
created: '2026-07-21T19:34:39.792835Z'
updated: '2026-07-21T19:40:55.089100Z'
source: https://www.insee.fr/fr/statistiques/fichier/7655513/documentation_donnees-carroyees_filosofi2019.pdf
source_domain: www.insee.fr
fetched_at: '2026-07-21T19:34:39.792569Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Official INSEE documentation (PDF, 19 pages) for the Filosofi 2019 200m/1km/natural-level
  gridded (''carroyées'') dataset. Confirms the variable list for the 200m grid: it
  DOES include age-structure variables (9 age brackets: ind_0_3, ind_4_5, ind_6_10,
  ind_11_17, ind_18_24, ind_25_39, ind_40_54, ind_55_64, ind_65_79, ind_80p, ind_inc)
  and household-composition/housing variables (men_1ind, men_5ind, men_prop, men_fmp
  monoparental, men_coll, men_mais, log_av45/45_70/70_90/ap90/log_soc, men_surf) alongside
  income/poverty fields (ind_snv = summed winsorized standard of living, men_pauv
  = poor households, potentially truncated at 80%). It does NOT include CSP (occupation
  category/PCS) or education/diploma-level variables at any grid size -- those fields
  are absent from the Filosofi source entirely (Filosofi is a fiscal/tax-return-derived
  dataset, not the census, so PCS and diploma are structurally out of scope, not just
  suppressed at fine granularity). 79% of 200m cells (representing 20% of population)
  are below the 11-household confidentiality threshold and use imputed values (indicator
  i_est_200); the ''natural level'' grid (variable cell size, 200m-64km) has zero
  imputation. Full field dictionary, confidentiality/imputation methodology, and per-département
  winsorization thresholds are included verbatim.'
raw_file: raw/documentation-donnes-carroyes.pdf
---

*Suggested by [[la-france-politique-de-2024-portrait-gographique-et-social-fondation-jean-jaurs]] — cited as source for carreaux 200m methodology*

DOCUMENTATION – données carroyées
FILOSOFI 2019
Table des matières
Introduction....................................................................................................................................................... 1
 I. Source Filosofi 2019.....................................................................................................................................2
1 Champ géographique...............................................................................................................................2
2 Champ statistique – Concept de ménage fiscal / logement occupé..........................................................3
3 Cas des enfants majeurs rattachés fiscalement à leurs parents...............................................................3
4 Niveau de vie, notion de revenu disponible..............................................................................................4
5 Règles de confidentialité...........................................................................................................................4
II. Contenu des fichiers diffusés........................................................................................................................5
1 Les différentes tailles de grille...................................................................................................................5
2 Les variables présentes dans les fichiers.................................................................................................6
3 Précisions sur les variables......................................................................................................................8
III. Méthodologie utilisée pour le niveau « naturel » et les imputations...........................................................11
1 Le niveau « naturel »...............................................................................................................................11
2 Imputation des carreaux de 200 m.........................................................................................................12
3 Imputation des carreaux de 1 km............................................................................................................14
4 Quelques chiffres....................................................................................................................................15
5 Utilisation des fichiers de données à 200 m............................................................................................15
6 Modes opératoires..................................................................................................................................15
7 Précautions............................................................................................................................................. 15
IV. Géolocalisation des données fiscales........................................................................................................16
1 Méthode de géolocalisation....................................................................................................................16
2 Précision de localisation.........................................................................................................................16
3 Projections géographiques.....................................................................................................................17
V. Annexe........................................................................................................................................................ 18
Seuils de winsorisation départementaux...................................................................................................18
Introduction
Le carroyage est une technique de quadrillage consistant à découper le territoire en carreaux pour y diffuser 
de l’information statistique à un niveau faiblement agrégé. Le maillage du territoire qui en résulte est plus ou 
moins fin selon la taille de carreau choisie. Le carroyage nécessite de disposer initialement de données pour
lesquelles on connaît précisément la position géographique de chaque observation.
Les carreaux permettent de s’affranchir des limites administratives habituelles et peuvent être assemblés
pour construire ou approcher n’importe quelle zone d’intérêt. L’information statistique sur un tel zonage peut
ensuite être facilement retrouvée en rassemblant les données des carreaux qui le constituent.
L’Insee a diffusé une première fois en 2013 des données issues de la source fiscale Revenus Fiscaux
Localisés (RFL) 2010 à la maille de carreaux de 200 m de côté. En 2019, un deuxième jeu de données
carroyées a été publié, à partir d’une source différente (Filosofi 2015 – Fichier localisé social et fiscal) et
d’une nouvelle méthodologie (les grilles superposées, voir infra). En 2022, le millésime Filosofi 2017 carroyé
a été diffusé.
Cette note présente la nouvelle publication des données carroyées de l'Insee, réalisée à partir de Filosofi
2019, et reprenant la méthodologie utilisée pour les précédents millésimes.
Documentation des données carroyées Filosofi 2019
1


---

 I. Source Filosofi 2019
La source « Fichier Localisé Social et Fiscal » (Filosofi) permet une observation du revenu disponible des
ménages (ce dont ils disposent au cours d’une année pour consommer et épargner) à un niveau territorial
infra-communal. La source Filosofi permet en outre de disposer de caractéristiques socio-démographiques
ou de caractéristiques au niveau des logements occupés. Au niveau national, l'enquête Revenus fiscaux et
sociaux (ERFS) reste la source de référence pour l’observation du revenu disponible, des inégalités de
niveaux de vie et de la pauvreté. En effet, il existe de légères différences méthodologiques entre ERFS et
Filosofi qui ne permettent pas d'avoir les mêmes résultats au niveau national.
Le millésime Filosofi de l'année 2019 est élaboré à partir des revenus perçus en 2019 qui ont été déclarés
en 2020 et de la taxe d'habitation au 1er janvier 2020.
Le rapprochement des fichiers fiscaux opéré dans le cadre du processus de Filosofi permet de constituer
des ménages fiscaux lorsqu’à une année donnée N coïncident au moins une déclaration indépendante des
revenus de l'année N (un, deux foyers fiscaux ou plus) et l’occupation d’un même logement connu à la taxe
d’habitation au 1er janvier de l'année N+1.
Le rapprochement avec les fichiers sociaux permet en outre de reconstituer pour chaque ménage fiscal
l'ensemble  des  prestations  sociales  perçues.  Ce  rapprochement  est  réalisé  à  partir  d’informations
communes dans les fichiers (nom, prénom, date de naissance, commune de résidence, etc.). L’Insee
collecte également les montants annuels des prestations légales de la branche vieillesse et de la branche
famille relevant du régime agricole (CCMSA). Pour le régime général, la Cnaf fournit un fichier exhaustif des
allocataires et du montant de leurs prestations sociales au cours de l'année et la Cnav fournit un fichier
exhaustif  des  prestations  versées  en  décembre.  Les  montants  annuels  des  prestations  sont  ensuite
reconstitués par extrapolation, en utilisant notamment les informations disponibles sur la composition des
familles.
Dans Filosofi, les revenus financiers non soumis à déclaration sont imputés selon un modèle construit à
partir de l’enquête Patrimoine de l’Insee : une probabilité de détention et un montant de détention sont
estimés en fonction d’un certain nombre de caractéristiques observables du ménage (revenus, âge, situation
familiale…) pour sept produits financiers (livrets exonérés, LEP, livrets jeune, CEL, PEL, assurances-vie et
PEA).
Les impôts retenus pour le calcul du revenu disponible (cf. infra) sont : l’impôt sur le revenu, la taxe
d’habitation, la CSG, la CRDS et le prélèvement social sur les revenus du patrimoine.
On peut se reporter à la documentation de la source Filosofi sur le site de l’Insee (cf. sources et méthodes 
Filosofi, janvier 2020). 
La source Filosofi diffère de la source RFL 2010, utilisée pour les informations diffusées avant 2013.
1
Champ géographique
Le  champ  géographique  de  diffusion  est  calé  sur  le  champ  de  Filosofi,  constitué  de  la  France
métropolitaine, de la Martinique et de La Réunion. La qualité insuffisante de l’appariement des fichiers
fiscaux des autres départements d’Outre-Mer ne permet pas de reconstituer les ménages fiscaux comme
pour la France métropolitaine, la Martinique et La Réunion.
Documentation des données carroyées Filosofi 2019
2


---

2
Champ statistique – Concept de ménage fiscal / 
logement occupé
Le champ statistique couvert est celui des  ménages fiscaux, constitué par le regroupement des foyers
fiscaux répertoriés dans un même logement. L’existence d’un ménage fiscal, une année donnée, tient au fait
que coïncident une déclaration indépendante de revenus pour l’année N et l’occupation d’un logement connu
à la taxe d’habitation (TH) au 1er janvier de l’année N+11. Par exemple, un couple de concubins au sein
duquel chacun remplit sa propre déclaration de revenus constitue deux foyers fiscaux mais un seul ménage
fiscal parce que les membres du couple sont répertoriés dans le même logement. Les couples de concubins
sont donc traités de la même façon qu’un couple marié ou pacsé dans la constitution des ménages fiscaux .
Sont respectivement exclus et absents des ménages fiscaux :
•
les contribuables  vivant  en  collectivité  (foyers  de  travailleurs,  maisons  de  retraite,  centres
d'hébergement, maisons de détention…) ;
•
les sans-abri.
Il y a plus de 28 millions de ménages fiscaux dans le millésime Filosofi de l'année 2019 sur le champ de la
France métropolitaine, de la Martinique et de La Réunion. Ces ménages regroupent un peu plus de 64,2
millions d’individus.
La majorité des ménages rattachent leur déclaration à leur résidence principale. Une petite partie (0,15 %) la
rattachent à leur résidence secondaire et sont donc localisés à cet endroit dans les données.
Par  ailleurs,  environ  80 000  ménages  fiscaux  (cas  des  indépendants  notamment)  ont  un  revenu
disponible strictement négatif. Ils ne sont pas pris en compte ici, ni dans les données diffusées par ailleurs
à partir de la source Filosofi.
Les données sur les logements portent sur les logements  occupés par les ménages fiscaux : les
logements vacants ne sont donc pas inclus dans les statistiques diffusées.
3
Cas des enfants majeurs rattachés fiscalement à 
leurs parents
Les règles fiscales autorisent les parents à  rattacher  leurs enfants majeurs ou mariés  à leur  propre
déclaration de revenus s’ils sont âgés de moins de 21 ans quelle que soit leur situation, ou s’ils sont âgés de
moins de 25 ans et poursuivent leurs études, ou s’ils sont handicapés quel que soit leur âge.
Les enfants majeurs rattachés à la déclaration fiscale de leurs parents peuvent occuper un logement
indépendant. Par construction, ils sont pourtant inclus dans le ménage de leurs parents.
En effet, la situation familiale, décrite dans la déclaration de revenus des parents, ne permet pas de repérer
si les enfants majeurs, comptés fiscalement à charge, occupent ou non le même logement que leurs
parents. Par conséquent, si ces enfants, majeurs ou mariés, occupent un autre logement, leur inexistence,
en tant que foyer fiscal, entraîne l’impossibilité de les créer en tant que ménage fiscal. Cette situation
concerne essentiellement des étudiants. Par comparaison avec le recensement de la population, cela
génère une sous-estimation du nombre de ménages et d’habitants des villes étudiantes et une surestimation
de la taille des ménages des parents. En termes d’évaluation des niveaux de revenus des ménages, cela
apparaît en revanche cohérent dans la mesure où ces étudiants sont effectivement à la charge de leur
famille.
1
Depuis l’annonce de la suppression progressive de la  taxe d’habitation, la couverture du fichier associé 
se dégrade. Les variables fondées sur des informations issues de la taxe d’habitation doivent donc être 
utilisées avec prudence. 
Documentation des données carroyées Filosofi 2019
3


---

La variable « Nombre d’individus âgés de 18 à 24 ans » est impactée par ces règles fiscales : elle est donc à
prendre avec prudence,  en  particulier  dans les villes étudiantes où  elle sera  bien plus faible que  la
population réellement présente.
4
Niveau de vie, notion de revenu disponible
Le revenu disponible est le revenu à la disposition du ménage pour consommer et épargner.
Il comprend le revenu déclaré (revenus d’activité, indemnités de chômage, retraites et pensions et certains
revenus  du  patrimoine),  les  revenus  financiers  non  soumis  à  déclaration  imputés  par  l’Insee  (livrets
exonérés, livrets jeunes, PEA, LEP, CEL, PEL, produits d’assurance-vie), les prestations sociales reçues
(prestations familiales, minima sociaux, prime d’activité et allocations logement) . Au total de ces ressources,
on déduit les impôts directs : impôt sur le revenu, taxe d’habitation, contribution sociale généralisée (CSG),
contribution au remboursement de la dette sociale (CRDS) et autres prélèvements sociaux sur les revenus
du patrimoine. La taxe foncière n’est pas prise en compte dans le calcul du revenu disponible, tout comme
certains  revenus  non  soumis  à  déclaration  n’ayant  pas  pu  être  imputés  dans  Filosofi  (heures
supplémentaires non déclarées notamment, et prime exceptionnelle de pouvoir d’achat).
Le revenu disponible par unité de consommation (ou niveau de vie) est le revenu disponible du ménage
rapporté au nombre d’unités de consommation qui le composent. Diviser le revenu disponible par le nombre
d’unités  de  consommation  présente  l’avantage  de  prendre  en  compte  les  diverses  compositions  des
ménages et donc les économies d’échelle liées à la vie en groupe. L’utilisation du revenu rapporté au
nombre d’unités de consommation du ménage est préconisée car celui-ci devient un revenu par équivalent
adulte, comparable d’un lieu à un autre et entre ménages de compositions différentes. Par exemple, un
célibataire ayant un revenu de 1 500 € par mois a un niveau de vie moins élevé qu’un couple de deux
personnes percevant chacune 1 500 €.
Alors que les revenus disponibles concernent le ménage, le niveau de vie représente ce dont dispose un
individu pour vivre, compte tenu de la composition du ménage auquel il appartient. En effet, tous les
individus d’un même ménage sont censés posséder le même niveau de vie, celui du ménage dont ils font
partie, par convention.
Le calcul du nombre d’unités de consommation (UC) d’un ménage est basé sur l'attribution à chaque
personne d’un poids en rapport avec sa part supposée dans la consommation du ménage. L’échelle
actuellement utilisée (dite de l'OCDE) retient la pondération suivante :
•
1 UC pour le premier adulte du ménage ;
•
0,5 UC pour les autres personnes de 14 ans ou plus ;
•
0,3 UC pour les enfants de moins de 14 ans.
5
Règles de confidentialité
Les données Filosofi 2017 sont produites à partir de données fiscales. Leur diffusion doit donc respecter la
règle d’au moins 11 ménages par unité géographique d’observation. Lorsque ce seuil n’est pas atteint,
l’information n’est pas diffusée en l’état.
En  utilisant  une  grille  de  carreaux  de  200  mètres  de  côté,  79 %  des  carreaux  habités  de  France
métropolitaine comprennent moins de 11 ménages fiscaux et doivent faire l’objet d’une imputation. Ils
représentent 20 % de la population totale. Dans cette version des données carroyées, l’Insee propose aux
utilisateurs, sur les carreaux de 200 m et de 1 km pour lesquels l’information ne peut pas être diffusée, une
valeur « imputée » à l’aide d’une méthode détaillée dans la partie III. Méthodologie utilisée pour le niveau
« naturel » et les imputations. Cette imputation est signalée à l’utilisateur par une variable indicatrice.
De plus, le paragraphe  Précisions sur les variables décrit le traitement particulier de certaines
variables sensibles.
Documentation des données carroyées Filosofi 2019
4


---

II. Contenu des fichiers diffusés
1
Les différentes tailles de grille
Les données carroyées sont disponibles sur trois niveaux de grille :
•
Grille de carreaux au niveau naturel
•
Grille de carreaux de 1 km de côté
•
Grille de carreaux de 200 m de côté
Fichier de données carroyées sur grille de niveau « naturel » : pas de
données imputées, mais un pavage de carreaux de taille variable
La  grille  de  niveau  naturel  correspond  à  un
partitionnement du territoire en carreaux de différentes
tailles (de 200 m jusqu’à 64 km) permettant de diffuser
toutes les informations sans imputation des données,
tout en respectant le secret fiscal.
On commence par couvrir le territoire avec des carreaux
de  64 km.  Les  divisions  successives  permettent  de
passer de carreaux de 64 km à 32 km, puis 16 km, 8 km,
4 km, 2 km, 1 km et enfin 200 m.
Les divisions s’arrêtent :
– soit lorsque les carreaux obtenus sont de taille 200 m
– soit lorsque la prochaine division entraînerait qu’un ou
plusieurs  carreaux  ne  respectent  pas  le  seuil  de
confidentialité fixé à 11 ménages.
Dans les territoires peu denses, la division s’arrête tôt,
sur des carreaux de taille élevée. Dans les territoires très
denses, les données sont disponibles à 200 m.
Pour chaque carreau, les valeurs des variables diffusées
sont exactes (aux arrondis près, voir le paragraphe
Arrondis des valeurs à une décimale
 
 ). Il n’y a pas 
 
 
d'imputation contrairement aux deux fichiers qui suivent
 
 2 . 
carreaux_nivNaturel
Fichier de données carroyées sur grille de carreaux de 1 km de côté
(présence de données imputées)
La grille de niveau 1 km correspond à un pavage du territoire
français  par  des  carreaux  de  1 km  de  côté.  Sur  certains
carreaux, le nombre de ménages fiscaux est inférieur à 11.
Dans ce cas, la donnée qui est présente dans le fichier est
imputée et le carreau aura sa variable indicatrice i_est_1km
égale à 1.
Dans le fichier Métropole,  64 % des carreaux de 1 km font
l’objet d’une imputation ; ils représentent 9 % de la population.
Dans le fichier Martinique,  27 % des carreaux de 1 km font
l’objet d’une imputation ; ils représentent 4 % de la population.
Dans le fichier La Réunion,  31 % des carreaux de 1 km font
l’objet d’une imputation ; ils représentent 4 % de la population.
Dans  l’image  ci-contre,  les  carreaux  faisant  l’objet  d’une
imputation sont hachurés.
carreaux_1km
2 Seule la variable de nombre de ménages pauvres peut avoir subi une troncature à l'échelle des carreaux 
de 200 mètres composant le carreau naturel (voir le paragraphe Arrondis des valeurs à une décimale).
Documentation des données carroyées Filosofi 2019
5


---

Fichier de données carroyées sur grille de carreaux de 200 mètres de
côté (présence de données imputées)
La grille de niveau 200 mètres correspond à un pavage du
territoire français par des carreaux de 200 mètres de côté.
Sur certains carreaux, le nombre de ménages fiscaux est
inférieur à 11. Dans ce cas, la donnée qui est présente dans
le fichier est imputée et le carreau aura sa variable indicatrice
i_est_200 égale à 1.
Dans le fichier Métropole, 79 % des carreaux de 200 m font
l’objet  d’une  imputation ;  ils  représentent  20 %  de  la
population.
Dans le fichier Martinique, 68 % des carreaux de 200 m font
l’objet  d’une  imputation ;  ils  représentent  22 %  de  la
population.
Dans le fichier La Réunion, 54 % des carreaux de 200 m font
l’objet  d’une  imputation ;  ils  représentent  10 %  de  la
population.
Dans  l’image  ci-contre,  les  carreaux  faisant  l’objet  d’une
imputation sont hachurés.
carreaux_200m
2
Les variables présentes dans les fichiers
Variables communes aux trois grilles
NOM
DESCRIPTIF
TYPE
ind
Nombre d'individus
numérique
men
Nombre de ménages
numérique
men_pauv
Nombre de ménages pauvres (potentiellement tronqué à 
80 %)
numérique
men_1ind
Nombre de ménages d'un seul individu
numérique
men_5ind
Nombre de ménages de 5 individus ou plus
numérique
men_prop
Nombre de ménages propriétaires
numérique
men_fmp
Nombre de ménages monoparentaux
numérique
ind_snv
Somme des niveaux de vie winsorisés des individus
numérique
men_surf
Somme de la surface des logements* du carreau
numérique
men_coll
Nombre de ménages en logement collectif
numérique
men_mais
Nombre de ménages en maison
numérique
log_av45
Nombre de ménages vivant dans des logements* construits 
avant 1945
numérique
log_45_70
Nombre de ménages vivant dans des logements*construits 
entre 1945 et 1969
numérique
log_70_90
Nombre de ménages vivant dans des logements* construits 
entre 1970 et 1989
numérique
log_ap90
Nombre de ménages vivant dans des logements* construits 
depuis 1990
numérique
log_inc
Nombre de ménages vivant dans des logements* dont la date
de construction est inconnue
numérique
log_soc
Nombre de ménages vivant dans des logements* sociaux
numérique
ind_0_3
Nombre d'individus de 0 à 3 ans
numérique
ind_4_5
Nombre d'individus de 4 à 5 ans
numérique
ind_6_10
Nombre d'individus de 6 à 10 ans
numérique
Documentation des données carroyées Filosofi 2019
6


---

ind_11_17
Nombre d'individus de 11 à 17 ans
numérique
ind_18_24**
Nombre d'individus de 18 à 24 ans**
numérique
ind_25_39
Nombre d'individus de 25 à 39 ans
numérique
ind_40_54
Nombre d'individus de 40 à 54 ans
numérique
ind_55_64
Nombre d'individus de 55 à 64 ans
numérique
ind_65_79
Nombre d'individus de 65 à 79 ans
numérique
ind_80p
Nombre d'individus de 80 ans ou plus
numérique
ind_inc
Nombre d'individus dont l'âge est inconnu
numérique
* le nombre de logements correspond aux logements occupés par des ménages fiscaux.
**comme indiqué dans le paragraphe Cas des enfants majeurs rattachés fiscalement à leurs parents,
les individus de 18 à 24 ans peuvent être rattachés fiscalement au foyer de leurs parents, entraînant un biais
dans la mesure de la population de cette tranche d’âge réellement présente sur le carreau.
Variables complémentaires de la grille de niveau naturel
NOM
TYPE
DESCRIPTIF
idcar_nat
caractère
Identifiant basé sur la norme Inspire3 : « CRS » pour « coordinate 
reference system » + code_crs (code projection EPSG) + « RES » pour 
« résolution » + taille_carreau_en_mètres + « m » + « N » pour Nord + 
coordonnée_y_coin_inférieur_gauche + « E » pour Est + 
coordonnée_x_coin_inférieur_gauche
tmaille
numérique
Taille en mètres du côté du carreau
Variables complémentaires de la grille de 1 km
NOM
TYPE
DESCRIPTIF
idcar_1km
caractère
Identifiant basé sur la norme Inspire² : « CRS » pour « coordinate 
reference system » + code_crs (code projection EPSG) + « RES » pour 
« résolution » + « 1 000 m » + « N » pour Nord + 
coordonnée_y_coin_inférieur_gauche + « E » pour Est + 
coordonnée_x_coin_inférieur_gauche
i_est_1km
numérique
- Vaut 2 si le carreau donne les vraies valeurs mais le nombre de ménages
affiché apparaît comme inférieur à 11 pour des questions d'arrondis (voir
Arrondis des valeurs à une décimale)
- Vaut 1 si le carreau est imputé par une valeur approchée,
- Vaut 0 dans les autres cas.
lcog_geo
caractère
Code officiel géographique au 1er janvier 2020 de la ou des commune(s) 
dans laquelle se trouve le carreau. En effet, si le carreau est à cheval sur 
plusieurs communes (intersection géographique avec la BDTopo), 
lcog_geo est alors la concaténation des codes des différentes communes 
intersectées, triées par surface d'intersection décroissante. Exemple pour 
un carreau à cheval majoritairement sur la commune 01002 mais 
également sur la commune 01001 : « 0100201001 ».
Variables complémentaires de la grille de 200 m
NOM
TYPE
DESCRIPTIF
idcar_200m
caractère
Identifiant basé sur la norme Inspire² : « CRS » pour « coordinate 
reference system » + code_crs (code projection EPSG) + « RES » pour 
« résolution » + « 200m » + « N » pour Nord + 
coordonnée_y_coin_inférieur_gauche + « E » pour Est + 
3
cf. Data specification on Statistical Units – INSPIRE (2013-12-10  page 20 et suivantes)
Documentation des données carroyées Filosofi 2019
7


---

coordonnée_x_coin_inférieur_gauche
idcar_1km
caractère
Identifiant du carreau de 1 km auquel appartient le carreau de 200 m
idcar_nat
caractère
Identifiant du carreau de niveau naturel auquel appartient le carreau de 
200 m
i_est_200
booléen
Vaut 1 si le carreau est imputé par une valeur approchée, 0 sinon.
i_est_1km
booléen
Vaut 1 si le carreau de 1 km auquel est rattaché le carreau de 200 m est 
imputé par une valeur approchée, 0 sinon.
lcog_geo
caractère
Code officiel géographique au 1er janvier 2020 de la ou des commune(s) 
dans laquelle se trouve le carreau. En effet, si le carreau est à cheval sur 
plusieurs communes (intersection géographique avec la BDTopo), 
lcog_geo est alors la concaténation des codes des différentes communes 
intersectées, triées par surface d’intersection décroissante. Exemple pour 
un carreau à cheval majoritairement sur la commune 01002 mais 
également sur la commune 01001 : « 0100201001 ».
3
Précisions sur les variables
Âge
L’âge des individus est calculé à partir des données de la déclaration de revenus, par différence entre
l’année des revenus de la déclaration et l’année de naissance. Dans certains cas, le nombre de personnes
du foyer fiscal est supérieur au nombre d’années de naissance renseignées dans la déclaration. L’âge des
individus sans année de naissance est alors classé dans la catégorie « âge inconnu ».
Le rattachement des étudiants au foyer fiscal de leurs parents entraîne un biais dans la localisation des
jeunes de 18 à 24 ans (cf. Cas des enfants majeurs rattachés fiscalement à leurs parents). Il convient
donc de traiter avec prudence les effectifs de cette tranche d’âge.
Statut d’occupation (propriétaires / locataires)
Le statut d’occupation du logement (locataire / propriétaire) est établi à partir de la taxe d’habitation. La
différence entre le nombre total de ménages et le nombre de ménages propriétaires donne le nombre de
ménages locataires.
Nature du local (maison, logement collectif)
La nature des locaux (individuels ou collectifs) est établie à partir de la taxe d’habitation. La différence entre
le nombre total de ménages et le nombre total de ménages en logement collectif (appartement) donne le
nombre de ménages en logement individuel, soit principalement des maisons mais aussi d’autres types de
logement (caravanes…), très peu nombreux.
Surface
La surface est la surface totale en mètres carrés des logements occupés. Elle est fournie par la taxe
d’habitation. Pour 113 000 ménages dont la surface du logement était manquante ou inférieure à 4 m², la
valeur de surface du logement a été imputée par la surface moyenne par individu dans la commune,
multipliée par le nombre d’habitants du logement dont la surface est imputée4.
4
Dans les données carroyées de Filosofi 2015, ces valeurs manquantes ont été imputées à 0, ce qui peut 
biaiser l’évolution temporelle de cet indicateur pour certains carreaux.
Documentation des données carroyées Filosofi 2019
8


---

Logement social
Une indicatrice de logement social a été construite pour améliorer les statistiques sur les occupants de ces
logements et diffère donc de celle existant dans les fichiers fiscaux. Elle ne distingue pas les HLM des SEM
et les logements conventionnés des non conventionnés. Elle permet de caractériser le parc des occupants
des logements sociaux.
Date de construction du logement
L’ancienneté du logement est établie à partir de la taxe d’habitation.
Ménages monoparentaux
À partir de la source Filosofi, le ménage monoparental est constitué de la façon suivante :
– Un ménage fiscal identifié comme « parent isolé » dans la déclaration de revenus (case cochée) est
considéré comme un ménage monoparental.
– Si la case n’est pas cochée, on peut cependant identifier des ménages monoparentaux :
•
Un  ménage  fiscal  composé  d’un  seul  foyer  fiscal est  considéré  comme  un  ménage
monoparental  s’il  est  composé  de  plusieurs  personnes  et  que  le  déclarant  principal  est
célibataire, divorcé ou veuf. 
•
Un ménage fiscal composé de deux (respectivement trois) foyers fiscaux est considéré comme
un ménage monoparental si :
➢
le référent fiscal du ménage n’est ni marié ni pacsé ;
➢
le déclarant principal de l’autre foyer fiscal (respectivement des deux autres foyers fiscaux)
n’est ni marié ni pacsé et n’a personne à sa charge dans son foyer fiscal ;
➢
la différence d’âge entre les 2 personnes (respectivement entre les 2 personnes déclarantes
et le référent fiscal) est comprise entre 15 et 41 ans.
→ cas d’un parent avec un (respectivement deux) grand(s) enfant(s).
Au-delà de trois foyers fiscaux, le ménage fiscal est considéré comme un ménage complexe.
NB : Comme dans toutes les classifications usuelles de type de ménage, aucune limite d’âge n’est fixée pour
les enfants, qui peuvent être adultes et même âgés. Cela signifie qu’un déclarant de 60 ans qui vit avec un
déclarant de 90 ans sont considérés comme un ménage monoparental, au même titre qu’un ménage
comprenant un déclarant de 30 ans avec un enfant de 5 ans.
Les enfants faisant une déclaration séparée et résidant dans le logement constituent un foyer fiscal séparé
mais font partie du même ménage fiscal.
À noter que le nombre de familles monoparentales est surestimé par rapport à celui du recensement, car les
enfants en garde alternée sont comptés pour 0,5 dans le foyer fiscal de chacun de leurs 2 parents.
Arrondis des valeurs à une décimale
Toutes les variables produites dans les bases de données sont  arrondies à une décimale. Certaines
variables, décrites ci-dessous, font éventuellement l’objet de traitements supplémentaires particuliers.
Cas des variables ventilées :
Dans les données carroyées, deux variables sont ventilées :
•
le nombre de personnes par carreau est ventilé par tranche d’âge,
Documentation des données carroyées Filosofi 2019
9


---

•
le nombre de ménages par carreau est ventilé par type de logement (maison ou logement collectif)
et selon l'année de construction du logement qu’ils occupent (avant 1945, entre 1945 et 1969, de
1970 à 1989, après 1990 ou date inconnue).
Lorsque les données sont imputées, elles comprennent plusieurs décimales. En arrondissant toutes ces
variables, il peut se produire que pour certains carreaux, le nombre de personnes ne soit pas exactement
égal à la somme des nombres de personnes par catégorie d’âge, ou alors le nombre de ménages ne soit
pas exactement égal à la somme des nombres de ménages par type de logement ou année de construction.
Afin de corriger ces incohérences, on arrondit les variables ventilées de sorte que la somme des arrondis
soit égale à l’arrondi de la somme.
Cas du nombre de ménages
Au niveau naturel, les données ne sont pas imputées, mais elles correspondent à la somme des
données des carreaux de 200 m qui le constituent. Pour cette raison, la valeur obtenue peut ne pas être
entière. Dans de rares cas, l'arrondi sur le nombre de ménages peut conduire à afficher un nombre compris
entre 10,6 et 11 (voir paragraphe suivant Niveau naturel).
Cas du nombre de ménages pauvres par carreau
Le nombre de ménages pauvres fait l’objet d’une imputation particulière. En effet, cette variable subit une
troncature si le taux de ménages pauvres dépasse 80 % à l’échelle des carreaux de 200 m. Toujours du fait
des arrondis au dixième, ayant lieu après cette troncature, le ratio entre le nombre de ménages pauvres et le
nombre total de ménage peut être légèrement supérieur à 80 %.
Winsorisation des niveaux de vie
La winsorisation est une technique statistique de traitement des valeurs extrêmes d’une distribution, qui
consiste à ramener à un seuil donné toutes les valeurs situées au-delà, ou en deçà, de ce seuil. Ces seuils
peuvent être des quantiles particuliers de la distribution.
Pour la diffusion des données carroyées, les niveaux de vie des individus5 sont préalablement « winsorisés »
avant la constitution des carreaux. Pour chaque carreau est ensuite diffusée la somme des niveaux de vie
des individus de ce carreau.
La winsorisation est effectuée selon des seuils départementaux. Dans un département donné, le niveau de
vie d’un individu est rabaissé au 95e centile de la distribution départementale si son niveau de vie est
supérieur  à  ce  seuil.  Inversement,  son  niveau  de  vie  est  ramené  au  5e centile  de  la  distribution
départementale si son niveau de vie est inférieur à ce seuil. Si son niveau de vie se situe entre ces deux
seuils, aucun traitement n’est effectué. Les seuils départementaux « inférieurs » varient entre 6 700 € et
11 300 €, et les seuils « supérieurs » varient entre 37 800 € et 93 200 €. La liste détaillée de ces seuils est
disponible en annexe (Seuils de winsorisation départementaux).
À la suite de ce traitement, 10 % des individus ont ainsi fait l’objet d’une winsorisation de leur niveau de vie.
838 000 carreaux de 200m de France métropolitaine contiennent au moins un individu dont le niveau de vie
a été winsorisé, soit 37 % du total. À La Réunion, cela concerne un peu moins de 9 600 carreaux, soit 66 %
du total. En Martinique, cela concerne un peu plus de 6 400 carreaux, soit 57 % du total.
5
Le niveau de vie d’un individu est le niveau de vie du ménage auquel il appartient, c’est-à-dire le revenu
disponible du ménage divisé par son nombre d’unités de consommation.
 
Documentation des données carroyées Filosofi 2019
10


---

III. Méthodologie utilisée pour le niveau 
« naturel » et les imputations
Diffuser de l'information sur des carreaux peut poser des problèmes de confidentialité lorsque les carreaux
contiennent trop peu de ménages. La règle de gestion de la confidentialité pour les données fiscales
utilisées est de ne pas diffuser l’information concernant un ensemble formé de 1 à 10 ménages
fiscaux. Pour cela, on adopte deux approches dont les résultats sont le niveau « naturel » et le niveau
imputé (200 m et 1 km). 
1
Le niveau « naturel »
Le niveau qu’on nomme « naturel » correspond à un pavage du territoire, composé de carreaux de taille
variable, qui permet « naturellement » de diffuser de l'information sans imputation. 
Dans l'ordre croissant, les 7 tailles possibles sont 200 m, 1 km, 2 km, 4 km, 8 km, 16 km, 32 km ou 64 km.
Le niveau naturel est donc formé de carreaux appartenant à des grilles régulières de différents niveaux,
emboîtées les unes dans les autres : la grille de 200 m sous-jacente est imbriquée dans la grille de 1 km (25
carreaux de 200 m forment un carreau de 1 km), elle-même imbriquée dans celle de 2 km, etc.
Le niveau naturel forme un pavage complet du territoire habité, c’est-à-dire que chaque ménage appartient à
un  et  un  seul  carreau  du  niveau  naturel.  Cette  grille  a  été
construite de telle sorte qu’aucun de ces carreaux ne comporte
moins de 11 ménages fiscaux. C’est pourquoi dans les zones peu
denses en termes de population, on trouvera des carreaux de
grande  taille  permettant  ainsi  de  rassembler  au  moins  11
ménages fiscaux.
Comment le niveau « naturel » est-il élaboré ?
On part de la grille régulière formée de carreaux de 64 km de
côté et couvrant tout le territoire. Dans chacun de ces grands
carreaux, il y a toujours au moins 11 ménages fiscaux. Ensuite,
pour chaque carreau, on regarde s’il est possible de le subdiviser
en carreaux plus petits sans contrevenir à la règle imposant qu’il
y ait au moins 11 ménages par carreau.
Par exemple, un carreau de 64 km se décompose en 4 carreaux
de 32 km. Si, pour chacun de ces 4 carreaux le nombre de
ménages est toujours supérieur ou égal à 11, alors on décide de
diviser le carreau de 64 km en 4 carreaux de 32 km.
Dans le cas contraire (au moins un des carreaux de la subdivision
comporte moins de 11 ménages, c’est-à-dire entre 1 et 10 ménages, 0 ménage ne comptant pas), on ne
subdivise pas le carreau : on reste alors dans le niveau naturel avec un carreau de 64 km (figure 1).
On effectue cette opération (subdivision en carreaux plus petits ou arrêt des subdivisions) pour chaque
carreau de 64 km. Puis on recommence avec les carreaux de 32 km, puis avec ceux de 16 km, etc. À la fin,
on obtient donc un pavage composé de carreaux de différente taille, les plus petits possibles et assurant
qu’ils comportent tous 11 ménages fiscaux ou plus.
En pratique, le niveau des carreaux de 200 m (voir paragraphe suivant) permet de reconstruire la grille du
niveau naturel, en agrégeant les variables d’intérêt selon la variable idcar_nat qui indique dans quel carreau
de niveau naturel se situe le carreau de 200 m. Les données du niveau naturel diffusées sont celles
Documentation des données carroyées Filosofi 2019
11
Figure 1


---

issues de cette agrégation. Or les valeurs des variables ont été arrondies à une décimale pour le niveau
200 m (cas des carreaux imputés). Cela a pour conséquence que pour certains carreaux du niveau naturel,
les valeurs diffusées diffèrent légèrement des valeurs qu’on aurait obtenues directement ou sans arrondir.
On peut notamment trouver quelques carreaux au niveau naturel dont le nombre de ménages indiqué est
compris entre 10,6 et 11 : cela se produit pour des raisons purement techniques d’arrondis.
2
Imputation des carreaux de 200 m
Le niveau de 200 m avec carreaux imputés est une grille régulière de carreaux de 200 m de côté. La plupart
de ces carreaux (79 %) contiennent moins de 11 ménages fiscaux, mais ils ne concentrent que 20 % de la
population. Pour ces carreaux, on ne peut donc pas directement diffuser l’information des ménages qui y
résident.  Pour pouvoir le faire, il faut regrouper ces carreaux entre eux jusqu’à obtenir des groupes de
carreaux rassemblant au total au moins 11 ménages fiscaux
 
 6 . Chacun de ces groupes rassemble au moins
11 ménages fiscaux. Les carreaux de 11 ménages ou plus sont généralement tout seuls dans leur groupe
mais il arrive, pour certains d’entre eux, qu’ils soient rassemblés dans des groupes avec d’autres carreaux à
faible effectif qui leur sont proches afin, notamment, de respecter le secret statistique dans ces petits
carreaux.
Comment sont déterminés ces groupes ?
Les groupes ne sont pas formés directement à partir des carreaux de 200 m. Dans la pratique, on part du
niveau naturel et on forme des groupes à chaque niveau, en allant vers des niveaux de plus en plus fins.
Si le niveau naturel est arrivé au niveau d’un carreau de 200 m, alors ce carreau contient bien 11 ménages
ou plus et on crée un groupe seulement pour lui (aucun autre carreau n’appartiendra à son groupe).
Au contraire, si le niveau naturel s’est arrêté à un niveau supérieur à 200 m, alors le carreau en question est
divisible en plusieurs sous-carreaux (4 sous-carreaux pour un carreau de 64 km, 32 km, 16 km, 8 km, 4 km
ou 2 km et 25 sous-carreaux pour un carreau de 1 km).
Au moins un de ces sous-carreaux contient moins de 11 ménages par construction. On rassemble tous les
sous-carreaux contenant moins de 11 ménages dans un groupe. Si cet ensemble de carreaux rassemble 11
ménages ou plus alors on s’arrête là. En revanche, si cet ensemble contient moins de 11 ménages, on lui
ajoute un des sous-carreaux restant contenant au moins 11 ménages de façon que le groupe ainsi formé
contienne au moins 11 ménages. On choisit, dans ce cas, parmi les sous carreaux contenant au moins 11
ménages, celui qui compte le moins de ménages.
On progresse ainsi itérativement en passant des niveaux les plus agrégés au niveau le plus fin (carreaux de
200 m). Un groupe peut lui-même être subdivisé en plusieurs sous-groupes lorsqu’on passe à un niveau
plus fin (voir figure 2).
6
Depuis le millésime 2019, le groupe d’imputation de chaque carreau de 200m n’est plus diffusé car ne 
présente pas d’utilité particulière concernant l’utilisation des données.
Documentation des données carroyées Filosofi 2019
12


---

Figure 2 : création des groupes
Lecture : le carreau de 2 km comprend 90 ménages. Lors de la subdivision en 4 carreaux de 1 km, on voit qu’un carreau est sous le 
seuil de 11 ménages. Il va alors être regroupé provisoirement avec le carreau le moins peuplé des 3 carreaux restants. À l’étape 
suivante, l’ensemble des sous-carreaux de 200 m du carreau de 7 restera dans le même groupe, mais ils seront regroupés avec 
seulement 2 autres carreaux (de 4 et 5 ménages) du carreau de 1 km précédent. Le sous-carreau de 12 ménages de ce carreau de 
1 km restera indépendant.
Si le carreau qu’on cherche à subdiviser est déjà affecté dans un groupe, alors tous les sous carreaux
contenant moins de 11 ménages de ce carreau seront affectés au même groupe que celui du carreau du
départ. C’est pour cette raison que des groupes composés de plusieurs carreaux imputés peuvent contenir
plus de 11 ménages, voire plus de 11 carreaux. Parmi tous les groupes formés, un d’entre eux contient un
maximum de 32 carreaux.
Comment est faite l’imputation ?
Une fois les groupes déterminés, on impute à chaque carreau, et pour toutes les variables de diffusion, la
valeur moyenne du groupe pondérée par le nombre d’individus.
Considérons ainsi une variable Y de diffusion (le nombre de ménages propriétaires, par exemple), autre que
le nombre de personnes7. Connaissant la valeur de cette variable Y sur chaque groupe et connaissant le
nombre de personnes par carreau, on peut imputer la valeur de Y sur les carreaux en répartissant la valeur
de Y du groupe proportionnellement au nombre de personnes de chaque carreau.
Par exemple pour le groupe 1 de la figure 3, si 
-
le carreau C5 comporte 7 ménages, 17 personnes et Y = Ya sur ce carreau ;
-
le carreau C8 comporte 4 ménages, 8 personnes et Y = Yb sur ce carreau ;
on estime que la variable Y vaut 
-
(Ya + Yb) * (17 / (17 + 8)) pour C5 ;
-
(Ya + Yb) * (8 / (17 + 8)) pour C8.
7 Le nombre de personnes par carreau est la seule variable diffusée sans restriction, quel que soit leur nombre de ménages (entre 1 et
10, ou 11 et plus).
Documentation des données carroyées Filosofi 2019
13


---

Ainsi, la somme des estimations est bien égale à Ya + Yb = Yg la valeur de Y pour le groupe 1. Cette valeur
Yg n'est pas confidentielle, car elle porte sur au moins 11 ménages fiscaux.
Au final, il y a 213 367 groupes rassemblant 2 carreaux ou plus. Un peu plus de la moitié de ces groupes
sont composés de moins de 9 carreaux.
3
Imputation des carreaux de 1 km
Pour le niveau à 1 km, on utilise le niveau imputé à 200 m. On agrège cette grille de 200 m selon la variable
idcar_1km en faisant pour chaque variable de diffusion la somme des valeurs présentes au niveau 200 m
(que ces valeurs soient issues d’une imputation ou non).
On détermine ensuite la variable i_est_1km. Sa valeur change selon les tables :
•
Dans les tables à 200
 
   m
  , on lui attribue la valeur 0 si les valeurs du carreau correspondent aux
vraies valeurs et 1 sinon. Si pour un carreau de 1 km donné, aucun des carreaux de 200 m le
composant n’est imputé (i_est_200 = 0), alors on en déduit que i_est_1km vaut aussi 0. Sinon, au
moins un des carreaux de 200 m appartient à un groupe de plus de deux carreaux. Si l'ensemble de
ces groupes est entièrement inclus dans le carreau de 1 km alors i_est_1km vaut également 0. En
effet, les valeurs des groupes correspondent aux vraies valeurs.
Dans le cas contraire (au moins un groupe dépasse sur un autre carreau de 1 km) alors i_est_1km
vaut 1 : la valeur du carreau de 1 km ne correspond pas aux vraies valeurs. Cette variable a été
reportée dans la table des carreaux de 200 m afin de savoir directement si en passant au niveau
1 km on aurait des vraies valeurs ou non.
•
Dans les tables à 1
 
   km
  , un traitement supplémentaire a été appliqué sur la variable i_est_1km. Il
peut en effet arriver dans certains cas que pour un carreau de 1 km donné on ait i_est_1km = 0
(dans les bases à 200 m) et qu’on ait pourtant un nombre de ménages strictement inférieur à 11 sur
ce carreau de 1 km (men < 11 et i_est_1km = 0). Cela se produit pour des raisons purement
techniques d’arrondis des valeurs, les valeurs imputées au niveau des carreaux de 200 m étant
arrondies à une décimale (voir partie sur arrondis).
Dans certains cas, on peut avoir plusieurs carreaux de 200 m contenant au total 11 ménages, mais
leur variable nombre de ménages (men) étant arrondie sur ces carreaux, la somme de celle-ci peut
être strictement inférieure à 11 mais très proche de 11 (10,9 ou 10,8). Si on avait fait la somme sans
les arrondis, on aurait bien retrouvé 11. Pour indiquer ces cas à l’utilisateur, la variable i_est_1km est
marquée à 2.
Documentation des données carroyées Filosofi 2019
14
Figure 3 : imputation


---

4
Quelques chiffres
Nombre de
carreaux
Part de
carreaux
non
imputés
Part de
carreaux
imputés
Part de carreaux imputés
comportant initialement 11
ménages ou plus
Part de la population située
dans les carreaux non
imputés
200 m
2 313 783 
21 %
79 %
1 %
80 %
1 000 m
376 307
36 %
64 %
19 %
91 %
Taille des carreaux au niveau naturel
200 m
1 000 m
2 000 m
4 000 m
8000 ou plus
Total
Nombre
24 891
59 084
48 401
11 797
1 074
145 247
Proportion (%)
17
41
33
8
1
100
5
Utilisation des fichiers de données à 200 m
À chaque carreau de 200 m sont associés :
-
une indicatrice qui indique si les valeurs du carreau ont été imputées par la méthode de répartition
décrite plus haut ou non (i_est_200) ;
-
le carreau du niveau supérieur, à savoir un carreau de 1 km de côté (idcar_1km);
-
une indicatrice qui indique si le carreau-père d'1 km de côté est blanchi ou non (i_est_1km);
-
le carreau du niveau naturel le contenant (carreau de 200 m, 1 km, …, ou 64 km) (idcar_nat).
Avec ces informations, il est possible de calculer le niveau naturel, en sommant la valeur des variables des 
carreaux composant les carreaux du niveau naturel. De la même façon, on peut calculer le niveau 1 km en 
agrégeant les données selon la variable idcar_1km.
6
Modes opératoires
Les fichiers sont disponibles en plusieurs formats : shapefiles et geopackage pour les systèmes 
d'information géographique et en format .csv pour les traitements de base de données. 
7
Précautions
Dans le fichier de carreaux à 200 m, 79 % des carreaux font l'objet d’imputation, ce qui implique une grande
vigilance, en particulier lors d’analyses sur des zones peu denses. La moitié des carreaux diffusés ont
moins de 2,6 ménages et moins de 6 individus.
Distribution des carreaux de 200m selon leur nombre d'individus ou de ménages
Quantile
Nombre d’individus
Nombre de ménages*
1 %
1
0,4
10 %
2
0,7
25 %
3
1,1
50 %
6
2,6
75 %
21
8,8
90 %
63
27,0
99 %
340
164,0
Moyenne
27,7
12,3
*le nombre de ménages est établi sur les valeurs des données imputées alors que le nombre d'individus est établi sur 
données réelles.
Champ : France métropolitaine, Martinique, La Réunion.
Documentation des données carroyées Filosofi 2019
15


---

En zone urbaine, du fait des fortes densités, on peut considérer que les données sont fiables pour un
territoire  comptant  un  nombre  relativement  réduit  de  carreaux.  En  zone  rurale,  en  revanche,  il  est
recommandé de ne pas travailler à un niveau en deçà de la taille d’un canton et de lisser les données.
Il est recommandé de ne pas faire d’évolution temporelle avec des millésimes précédemment diffusés des
données carroyées.  En effet, à l’infracommunal, les évolutions entre deux millésimes ne reflètent pas
uniquement l’évolution réelle, elles traduisent aussi les améliorations de géolocalisation des adresses (voire
partie suivante). Par ailleurs, le dispositif Filosofi diffère des revenus fiscaux localisés (RFL). Il ne faut donc
faire aucune analyse en évolution entre les données RFL 2010, Filosofi 2015 et 2017, précédemment
diffusées, et celles faisant l’objet de la présente diffusion.
Il ne faut en aucun cas comparer la somme de la population des carreaux composant une commune
à  la  population  de  la  commune  au  recensement  de  la  population.  Ces  deux  effectifs  seront
nécessairement différents du fait de la différence de concepts dans ces sources.
Du fait de la procédure de winsorisation des niveaux de vie, la somme des niveaux de vie des individus
des carreaux d’une commune sera différente de la somme des niveaux de vie des individus qui
pourrait être diffusée par ailleurs sur insee.fr.
IV. Géolocalisation des données fiscales
1
Méthode de géolocalisation
La géolocalisation est un processus permettant d’attribuer à chaque ménage de la source Filosofi un couple
de coordonnées géographiques (longitude, latitude). Ces coordonnées seront ensuite projetées selon les
différentes  projections  évoquées  ci-dessous  au  paragraphe  3 (projections  différentes  pour  la  France
métropolitaine, la Martinique et La Réunion).
Afin de déterminer ces coordonnées à partir des informations de la source Filosofi, on utilise la parcelle
cadastrale à laquelle est rattaché le logement du ménage. À chaque parcelle correspond une étiquette qui
n'est rien d’autre qu’un point localisé dans l’espace et qui donne des coordonnées géographiques pour la
parcelle en question. On peut donc géolocaliser Filosofi à l’aide des étiquettes de parcelles cadastrales.
C’est le principal moyen utilisé pour géolocaliser les données.
Dans de très rares cas, il n’y a pas d’étiquette à la parcelle cadastrale. Des méthodes d’interpolation des
localisations géographiques sont alors utilisées pour pouvoir in fine attribuer une position géographique au
ménage. Cette position risque alors d’être de moins bonne qualité.
Des vérifications ont été conduites et des traitements ont été réalisés pour permettre une meilleure qualité,
lorsque  le  positionnement  était  visiblement  erroné  (positionnement  dans  des  zones  inhabitables  par
exemple). En revanche, il n’est pas toujours possible de détecter l’ensemble des anomalies et de les traiter
et certaines d’entre elles peuvent perdurer. Elles sont de faible ampleur sur l’ensemble des ménages
localisés.
2
Précision de localisation
La méthode de géolocalisation peut ainsi conduire à des imprécisions géographiques, qui seront d’autant
plus fréquentes que la maille d’analyse est fine.
Le cadastre peut être imprécis dans sa localisation. De plus, le positionnement de l’étiquette cadastrale, et
donc des carreaux habités, de certaines grandes parcelles cadastrales va se faire aléatoirement sur cette
parcelle, parfois loin du bâti (voir exemple ci-dessous).
Documentation des données carroyées Filosofi 2019
16


---

Exemple : Dans la parcelle n°2, les données sont localisées dans le champ situé à l’ouest, alors que la zone habitée est située à l’est.
Cette localisation peut par ailleurs varier d’un millésime de données sur l’autre, entraînant l'apparition à un
endroit et la disparition à un autre d’un carreau habité sur une même parcelle. La comparaison des effectifs
issus de la source RFL2010, Filosofi 2015, 2017 et 2019 est donc fortement déconseillée à un niveau aussi
fin, elle n’aurait pas de sens.
Enfin, il peut arriver que de nombreux logements soient géolocalisés en un unique point géographique,
notamment dans les quartiers de grands-ensembles. Il est conseillé, dans ces zones, d’analyser les données
sur des ensembles de carreaux suffisamment nombreux.
3
Projections géographiques
Les projections cartographiques utilisées sont les suivantes :
•
France métropolitaine : la projection utilisée est la projection Lambert 93 (EPSG 2154). Toutefois, la
grille de carreaux a été produite à partir des données projetées en LAEA (EPSG 3035) qui est la
projection utilisée au niveau européen. Les contours des carreaux ainsi obtenus ont ensuite été
reprojetés en Lambert 93. L’identifiant Inspire du carreau décrit les coordonnées du coin en bas à
gauche du carreau selon la projection LAEA. 
•
Martinique : la projection utilisée est la projection UTM 20N (EPSG 5490). 
•
La Réunion : la projection utilisée est la projection UTM 40S (EPSG 2975). 
Documentation des données carroyées Filosofi 2019
17


---

V. Annexe
Seuils de winsorisation départementaux
Département
5e centile (€)
95e centile (€)
01
10219,1
58424,5
02
9005,9
39925,3
03
9272,5
40282
04
9048
42072,6
05
9678
42514,7
06
8606
52728,3
07
9519
41214
08
8893,2
39351,2
09
8759,5
39122,8
10
9140,8
44247,8
11
8534,9
39975
12
9678,6
41042,8
13
8496
49206
14
10115,3
44607,4
15
10040,6
40256,9
16
9392,5
42332,3
17
10039,6
44946
18
9601,5
41451,3
19
9977
41259,5
21
10305,9
47190,6
22
10322,1
41622
23
8665,5
37808,9
24
9112,9
40254
25
10071
49921
26
9523,4
43862,7
27
9993,9
42371,2
28
10074
43234,9
29
10587,5
42804,6
2A
9014,9
49150
2B
8158,5
45432,7
30
8592,3
42960,7
31
9527
50516
32
9355,3
42055,2
33
9723,6
48482,3
34
8496,8
46031,1
35
10611,4
45220,7
36
9544,5
38760,8
37
9796,8
45236,6
38
10217,4
47351,2
39
10448,7
45009,3
40
10334,4
42275,1
41
9933,1
42193,6
42
9356,5
41865,3
43
10408,8
39749,7
Documentation des données carroyées Filosofi 2019
18


---

44
10592,4
46285,3
45
9738,5
44215,5
46
9196
41794
47
9156
40679,7
48
9396,2
39134,8
49
10372,5
41794,7
50
10476,1
41201,8
51
9405,8
49004
52
9599,1
38699,7
53
10402,9
39520,9
54
9048,5
45460,3
55
9631
40061,9
56
10388,8
43416,4
57
8891,7
48275,7
58
9159,8
39483,2
59
8972,5
44060
60
9882,1
45399,2
61
9335,7
39185,5
62
9254
39105,3
63
9701,1
45222,2
64
10021,4
47335,9
65
9479,1
39879
66
8469,7
41124,9
67
9603,5
48976,5
68
9737,3
55652,8
69
9387
53796,7
70
10119,3
39537,3
71
10037,9
41714,8
72
9780,3
40439,6
73
10643,1
47998,9
74
10469,3
72255,7
75
8063,9
93180,6
76
9480
43707,2
77
9962,2
47158,8
78
10467,1
64758
79
10175,1
40952,4
80
9362
42109,6
81
9368,7
41634,2
82
9169,4
40322
83
9080,3
47174
84
8583,2
43594,7
85
11264
40540
86
9490,2
41965,3
87
9156,9
41853
88
9390
39753,6
89
9554,6
41234
90
9450,6
46180,7
91
9449,2
50588,7
92
9467,8
77439,3
93
6975,6
41120,4
94
8524,6
55850,2
95
8613,3
47595
972
6854,7
45776,5
974
6737,5
45116
Documentation des données carroyées Filosofi 2019
19

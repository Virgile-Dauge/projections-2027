---
title: Activité des résidents en 2020 | Insee
id: activit-des-rsidents-en-2020-insee
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-implementation-bureau-ei-et-covariables
- insee-iris
- csp
created: '2026-07-21T19:36:14.157477Z'
updated: '2026-07-21T19:40:55.091338Z'
source: https://www.insee.fr/fr/statistiques/7704089
source_domain: www.insee.fr
fetched_at: '2026-07-21T19:36:14.119140Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'INSEE ''Base infracommunale (IRIS) - Activité des résidents en 2020'' page:
  confirms that catégorie socio-professionnelle (CSP), employment status, part-time/full-time,
  and age-of-active-population variables are published at IRIS level (~2,000 inhabitants
  per zone, ~15,500 IRIS in France), derived from the population census (Recensement
  de la population), NOT from Filosofi. Variable dictionary sample includes P20_POP1564/1524/2554/5564
  (population by age band 15-64), sex-split equivalents (P20_H*/P20_F*), and P20_ACT1564
  (active population). This is a structurally separate INSEE product from the Filosofi-based
  200m/1km carreaux grid: the carreaux dataset (see [[documentation-donnes-carroyes]])
  has no CSP or education fields at any resolution, while IRIS-level census bases
  like this one and the parallel ''Diplômes - Formation'' base carry exactly those
  variables. Confirms the user''s hypothesis that CSP and diploma-level data require
  IRIS granularity (~2000 inhabitants), not the finer 200m Filosofi grid.'
---

*Suggested by [[documentation-donnes-carroyes]] — verifies that CSP variables are documented at IRIS level, not in Filosofi carreaux*

false
#  Activité des résidents en 2020Recensement de la population - Base infracommunale (IRIS)
Chiffres détaillés
Paru le : Paru le 19/10/2023
- Octobre 2023
**La base infracommunale « Activité des résidents » fournit des données sur les caractéristiques des actifs (sexe, âge, catégorie socio-professionnelle), des salariés et non-salariés (sexe et âge).**
  * **[Téléchargement](https://www.insee.fr/fr/statistiques/7704089#consulter)**
  * [Documentation](https://www.insee.fr/fr/statistiques/7704089#documentation)
  * [Dictionnaire des variables](https://www.insee.fr/fr/statistiques/7704089#dictionnaire)


Consultation de la publication ou de la documentation qui lui est associée  Consulter Documentation Dictionnaire des variables
  * Les données 2020 sont diffusées selon la géographie en vigueur au **1 er janvier 2022**.
  * En complément des données, la base comprend : la liste des variables, des précisions sur l'utilisation des données et la géographie des données ainsi que de la documentation générale.
  * Les bases en téléchargement sont au format Excel (XLSX) et CSV.


**Niveau géographique** : ensemble des IRIS des communes découpées en IRIS, ainsi que les données au niveau communal pour les communes non découpées en IRIS, afin de couvrir l'ensemble du territoire.
Activité des résidents en 2020 - IRIS - France hors Mayotte 
[ (xlsx, 58 Mo)  ](https://www.insee.fr/fr/statistiques/fichier/7704089/base-ic-activite-residents-2020_xlsx.zip)[ (csv, 33 Mo)  ](https://www.insee.fr/fr/statistiques/fichier/7704089/base-ic-activite-residents-2020_csv.zip)
Activité des résidents en 2020 - IRIS - Collectivités d'outre-mer 
[ (xlsx, 41 Ko)  ](https://www.insee.fr/fr/statistiques/fichier/7704089/base-ic-activite-residents-2020-com_xlsx.zip)[ (csv, 18 Ko)  ](https://www.insee.fr/fr/statistiques/fichier/7704089/base-ic-activite-residents-2020-com_csv.zip)
## Pour comprendre
Les communes d'au moins 10 000 habitants et la plupart des communes de 5 000 à 10 000 habitants sont découpées en IRIS. Ce découpage, maille de base de la diffusion de statistiques infracommunales, constitue une partition du territoire de ces communes en "quartiers" dont la population est de l'ordre de 2 000 habitants. La France compte environ 15 500 IRIS dont 750 pour les DOM.
Par extension, afin de couvrir l'ensemble du territoire, on assimile à un IRIS chacune des communes non découpées en IRIS.
## Sources
[Recensement de la population](https://www.insee.fr/fr/metadonnees/source/s1321)
### Définitions
  * [Catégorie socioprofessionnelle](https://www.insee.fr/fr/information/2383278#def_C)
  * [Conditions d'emploi](https://www.insee.fr/fr/information/2383278#def_C)
  * [Population active ayant un emploi (ou actifs ayant un emploi)](https://www.insee.fr/fr/information/2383278#def_P)
  * [Statut professionnel](https://www.insee.fr/fr/information/2383278#def_S)
  * [Temps partiel / temps complet](https://www.insee.fr/fr/information/2383278#def_T)


  *     * ### Liste des variables
      * Géographie (au 01/01/2022) 
        * IRIS : code du département suivi du numéro de commune ou du numéro d'arrondissement municipal suivi du numéro d'IRIS
        * REG : code de la région
        * DEP : code du département
        * UU2020 : code du département ou "00" pour les unités urbaines qui s'étendent sur plusieurs départements voire au-delà de la frontière suivi d'un code sur une position indiquant la taille de la population puis d'un numéro d'ordre à l'intérieur de la taille
        * COM : code du département suivi du numéro de commune ou du numéro d'arrondissement municipal pour Paris Lyon et Marseille
        * LIBCOM : libellé de la commune ou de l'arrondissement municipal pour Paris Lyon et Marseille
        * TRIRIS : code du département suivi d'un numéro d'ordre à l'intérieur du département sur trois positions puis d'un indicateur de TRIRIS
        * GRD_QUART : code du département suivi du numéro de commune ou du numéro d'arrondissement municipal pour Paris Lyon et Marseille suivi du numéro de grand quartier
        * LIBIRIS : libellé de l'IRIS à l'intérieur de la commune ou de l'arrondissement municipal pour Paris Lyon et Marseille
        * TYP_IRIS : type d'IRIS : habitat (H), activité (A), divers (D), Autre (Z)
        * LAB_IRIS : label de qualité de l'IRIS
      * Caractéristiques des actifs 
        * P20_POP1564 : nombre de personnes de 15 à 64 ans
        * P20_POP1524 : nombre de personnes de 15 à 24 ans
        * P20_POP2554 : nombre de personnes de 25 à 54 ans
        * P20_POP5564 : nombre de personnes de 55 à 64 ans
        * P20_H1564 : nombre d'hommes de 15 à 64 ans
        * P20_H1524 : nombre d'hommes de 15 à 24 ans
        * P20_H2554 : nombre d'hommes de 25 à 54 ans
        * P20_H5564 : nombre d'hommes de 55 à 64 ans
        * P20_F1564 : nombre de femmes de 15 à 64 ans
        * P20_F1524 : nombre de femmes de 15 à 24 ans
        * P20_F2554 : nombre de femmes de 25 à 54 ans
        * P20_F5564 : nombre de femmes de 55 à 64 ans
        * P20_ACT1564 : nombre de personnes actives de 15 à 64 ans
        * P20_ACT1524 : nombre de personnes actives de 15 à 24 ans
        * P20_ACT2554 : nombre de personnes actives de 25 à 54 ans
        * P20_ACT5564 : nombre de personnes actives de 55 à 64 ans
        * P20_HACT1564 : nombre d'hommes actifs de 15 à 64 ans
        * P20_HACT1524 : nombre d'hommes actifs de 15 à 24 ans
        * P20_HACT2554 : nombre d'hommes actifs de 25 à 54 ans
        * P20_HACT5564 : nombre d'hommes actifs de 55 à 64 ans
        * P20_FACT1564 : nombre de femmes actives de 15 à 64 ans
        * P20_FACT1524 : nombre de femmes actives de 15 à 24 ans
        * P20_FACT2554 : nombre de femmes actives de 25 à 54 ans
        * P20_FACT5564 : nombre de femmes actives de 55 à 64 ans
        * P20_ACTOCC1564 : nombre de personnes actives occupées de 15 à 64 ans
        * P20_ACTOCC1524 : nombre de personnes actives occupées de 15 à 24 ans
        * P20_ACTOCC2554 : nombre de personnes actives occupées de 25 à 54 ans
        * P20_ACTOCC5564 : nombre de personnes actives occupées de 55 à 64 ans
        * P20_HACTOCC1564 : nombre d'hommes actifs occupés de 15 à 64 ans
        * P20_HACTOCC1524 : nombre d'hommes actifs occupés de 15 à 24 ans
        * P20_HACTOCC2554 : nombre d'hommes actifs occupés de 25 à 54 ans
        * P20_HACTOCC5564 : nombre d'hommes actifs occupés de 55 à 64 ans
        * P20_FACTOCC1564 : nombre de femmes actives occupées de 15 à 64 ans
        * P20_FACTOCC1524 : nombre de femmes actives occupées de 15 à 24 ans
        * P20_FACTOCC2554 : nombre de femmes actives occupées de 25 à 54 ans
        * P20_FACTOCC5564 : nombre de femmes actives occupées de 55 à 64 ans
        * P20_CHOM1564 : nombre de chômeurs de 15 à 64 ans
        * P20_CHOM1524 : nombre de chômeurs de 15 à 24 ans
        * P20_CHOM2554 : nombre de chômeurs de 25 à 54 ans
        * P20_CHOM5564 : nombre de chômeurs de 55 à 64 ans
        * P20_CHOM_DIPLMIN : nombre de chômeurs de 15 ans à 64 ans titulaires d'aucun diplôme ou au plus un CEP
        * P20_CHOM_BEPC : nombre de chômeurs de 15 ans à 64 ans titulaires d'un BEPC, brevet des collèges, DNB
        * P20_CHOM_CAPBEP : nombre de chômeurs de 15 ans à 64 ans titulaires d'un CAP, d'un BEP ou équivalent
        * P20_CHOM_BAC : nombre de chômeurs de 15 ans à 64 ans titulaires d'un Baccalauréat, brevet professionnel ou équivalent
        * P20_CHOM_SUP2 : nombre de chômeurs de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement supérieur de niveau Bac + 2
        * P20_CHOM_SUP34 : nombre de chômeurs de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement supérieur de niveau Bac + 3 ou Bac + 4
        * P20_CHOM_SUP5 : nombre de chômeurs de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement
        * P20_ACT_DIPLMIN : nombre de personnes actives de 15 ans à 64 ans titulaires d'aucun diplôme ou au plus un CEP
        * P20_ACT_BEPC : nombre de personnes actives de 15 ans à 64 ans titulaires d'un BEPC, brevet des collèges, DNB
        * P20_ACT_CAPBEP : nombre de personnes actives de 15 ans à 64 ans titulaires d'un CAP, d'un BEP ou équivalent
        * P20_ACT_BAC : nombre de personnes actives de 15 ans à 64 ans titulaires d'un Baccalauréat, brevet professionnel ou équivalent 
        * P20_ACT_SUP2 : nombre de personnes actives de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement supérieur de niveau Bac + 2
        * P20_ACT_SUP34 : nombre de personnes actives de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement supérieur de niveau Bac + 3 ou Bac + 4
        * P20_ACT_SUP5 : nombre de personnes actives de 15 ans à 64 ans titulaires d'un diplôme de l'enseignement
        * P20_ETUD1564 : nombre d'élèves, étudiants et stagiaires non rémunérés de 15 à 64 ans
        * P20_RETR1564 : nombre de retraités ou préretraités de 15 à 64 ans
        * C20_ACT1564 : nombre de personnes actives de 15 à 64 ans
        * C20_ACT1564_CS1 : nombre d'agriculteurs exploitants actifs de 15 à 64 ans
        * C20_ACT1564_CS2 : nombre d'artisans, commerçants, chefs d'entreprise actifs de 15 à 64 ans
        * C20_ACT1564_CS3 : nombre de cadres et professions intellectuelles supérieures actifs de 15 à 64 ans
        * C20_ACT1564_CS4 : nombre de professions intermédiaires actives de 15 à 64 ans
        * C20_ACT1564_CS5 : nombre d'employés actifs de 15 à 64 ans
        * C20_ACT1564_CS6 : nombre d'ouvriers actifs de 15 à 64 ans
        * C20_ACTOCC1564 : nombre de personnes actives occupées de 15 à 64 ans
        * C20_ACTOCC1564_CS1 : nombre d'agriculteurs exploitants actifs occupés de 15 à 64 ans
        * C20_ACTOCC1564_CS2 : nombre d'artisans, commerçants, chefs d'entreprise actifs occupés de 15 à 64 ans
        * C20_ACTOCC1564_CS3 : nombre de cadres, professions intellectuelles supérieures actifs occupés de 15 à 64 ans
        * C20_ACTOCC1564_CS4 : nombre de professions intermédiaires actives occupées de 15 à 64 ans
        * C20_ACTOCC1564_CS5 : nombre d'employés actifs occupés de 15 à 64 ans
        * C20_ACTOCC1564_CS6 : nombre d'ouvriers actifs occupés de 15 à 64 ans
        * P20_ACTOCC15P : nombre de personnes actives occupées de 15 ans ou plus
        * P20_HACTOCC15P : nombre d'hommes actifs occupés de 15 ans ou plus
        * P20_FACTOCC15P : nombre de femmes actives occupées de 15 ans ou plus
        * P20_ACTOCC15P_TP : nombre de personnes actives occupées de 15 ans ou plus à temps partiel
        * P20_ACTOCC15P_ILT1 : nombre d'actifs occupés de 15 ans ou plus qui travaillent dans la commune de résidence
        * P20_ACTOCC15P_ILT2P : nombre d'actifs occupés de 15 ans ou plus qui travaillent dans une autre commune que la commune de résidence
        * P20_ACTOCC15P_ILT2 : nombre d'actifs occupés de 15 ans ou plus qui travaillent dans une autre commune située dans le département de résidence
        * P20_ACTOCC15P_ILT3 : nombre d'actifs occupés de 15 ans ou plus qui travaillent dans une autre commune située dans un autre département de la région de résidence
        * P20_ACTOCC15P_ILT4 : nombre d'actifs occupés de 15 ans ou plus qui travaillent dans une commune située dans une autre région en France métropolitaine
        * P20_ACTOCC15P_ILT5 : nombre d'actifs occupés de 15 ans ou plus qui travaillent ailleurs, hors de France métropolitaine (Département d'outre-mer, Collectivité d'outre-mer ou à l'étranger)
        * C20_ACTOCC15P : nombre d'actifs occupés de 15 ans ou plus
        * C20_ACTOCC15P_PAS : nombre d'actifs occupés de 15 ans ou plus qui n'utilisent pas de moyen de transport pour aller travailler
        * C20_ACTOCC15P_MAR : nombre d'actifs occupés de 15 ans ou plus qui vont travailler principalement à pied
        * C20_ACTOCC15P_VELO : Nombre d'actifs occupés de 15 ans ou plus qui utilisent principalement un vélo pour aller travailler
        * C20_ACTOCC15P_2ROUESMOT : Nombre d'actifs occupés de 15 ans ou plus qui utilisent principalement un deux-roues motorisé pour aller travailler
        * C20_ACTOCC15P_VOIT : nombre d'actifs occupés de 15 ans ou plus qui utilisent principalement une voiture ou un camion pour aller travailler
        * C20_ACTOCC15P_TCOM : nombre d'actifs occupés de 15 ans ou plus qui utilisent principalement les transports en commun pour aller travailler
      * Caractéristiques des inactifs 
        * P20_INACT1564 : nombre de personnes inactives de 15 à 64 ans
        * P20_HINACT1564 : nombre d'hommes inactifs de 15 à 64 ans
        * P20_FINACT1564 : nombre de femmes inactives de 15 à 64 ans
        * P20_HETUD1564 : nombre d'élèves, étudiants et stagiaires non rémunérés hommes de 15 à 64 ans
        * P20_FETUD1564 : nombre d'élèves, étudiants et stagiaires non rémunérés femmes de 15 à 64 ans
        * P20_HRETR1564 : nombre de retraités ou préretraités hommes de 15 à 64 ans
        * P20_FRETR1564 : nombre de retraités ou préretraités femmes de 15 à 64 ans
        * P20_AINACT1564 : nombre d'autres inactifs de 15 à 64 ans
        * P20_HAINACT1564 : nombre d'autres inactifs hommes de 15 à 64 ans
        * P20_FAINACT1564 : nombre d'autres inactifs femmes de 15 à 64 ans
      * Caractéristiques des salariés 
        * P20_SAL15P : nombre de personnes salariées de 15 ans ou plus
        * P20_HSAL15P : nombre d'hommes salariés de 15 ans ou plus
        * P20_FSAL15P : nombre de femmes salariées de 15 ans ou plus
        * P20_SAL15P_TP : nombre de personnes salariées de 15 ans ou plus à temps partiel
        * P20_HSAL15P_TP : nombre d'hommes salariés de 15 ans ou plus à temps partiel
        * P20_FSAL15P_TP : nombre de femmes salariées de 15 ans ou plus à temps partiel
        * P20_SAL15P_CDI : nombre de personnes salariées de 15 ans ou plus titulaires de la fonction publique ou d'un contrat à durée indéterminée
        * P20_SAL15P_CDD : nombre de personnes salariées de 15 ans ou plus ayant un contrat à durée déterminée
        * P20_SAL15P_INTERIM : nombre de personnes salariées de 15 ans ou plus intérimaires
        * P20_SAL15P_EMPAID : nombre de personnes salariées de 15 ans ou plus Emplois aidés
        * P20_SAL15P_APPR : nombre de personnes salariées de 15 ans ou plus en apprentissage ou stagiaires
      * Caractéristiques des non-salariés 
        * P20_NSAL15P : nombre de personnes non-salariées de 15 ans ou plus
        * P20_HNSAL15P : nombre d'hommes non-salariés de 15 ans ou plus
        * P20_FNSAL15P : nombre de femmes non-salariées de 15 ans ou plus
        * P20_NSAL15P_TP : nombre de personnes non-salariées de 15 ans ou plus à temps partiel
        * P20_NSAL15P_INDEP : nombre de personnes non-salariées de 15 ans ou plus indépendants
        * P20_NSAL15P_AIDFAM : nombre de personnes non-salariées de 15 ans ou plus aides familiaux
        * P20_NSAL15P_EMPLOY : Nombre de personnes non-salariées de 15 ans ou plus employeurs


[Haut de page](https://www.insee.fr/fr/statistiques/7704089)

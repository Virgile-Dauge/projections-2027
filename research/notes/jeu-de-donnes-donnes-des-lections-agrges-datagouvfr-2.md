---
title: Jeu de données - Données des élections agrégées | data.gouv.fr
id: jeu-de-donnes-donnes-des-lections-agrges-datagouvfr-2
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-crosswalk-bureaux-fiabilite
- identifiants-bureaux-vote
- id-brut-miom
- table-bv-reu
created: '2026-07-21T19:40:15.587767Z'
updated: '2026-07-21T19:42:54.303817Z'
source: https://www.data.gouv.fr/datasets/donnees-des-elections-agregees/discussions
source_domain: www.data.gouv.fr
fetched_at: '2026-07-21T19:40:15.553031Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Page discussions (17 fils, 4 clôturés) du jeu de données agrégé data.gouv.fr,
  contenant des retours utilisateurs concrets sur des incohérences d''identifiants
  de bureaux de vote entre millésimes. Un fil du 9-11 février 2026 documente : (1)
  des codes communes DOM-TOM mal convertis lors du passage au format id_brut_miom
  (ex: Mayotte ZM donne 975 au lieu de 976, Nouvelle-Calédonie ZN donne 978 au lieu
  de 988, Polynésie ZP donne 970/977 au lieu de 987, Wallis-et-Futuna ZW donne 970
  au lieu de 986, collisionnant avec de vrais départements DOM) ; (2) un changement
  de format des identifiants de bureaux de vote de Montbéliard entre le 1er tour des
  législatives 2024 tel que publié par le Ministère de l''Intérieur (codes ''0E11'',
  ''0E321'') et ce que produit le pipeline agrégé (codes ''0X01'', ''0X02''), signalé
  explicitement comme ''certains bureaux de vote ne correspondent plus avec ceux donnés
  par le ministère de l''intérieur'' ; (3) un code de bureau corrompu à Montbéliard
  aux municipales 2020 (''25388_0,00E+00'' vs ''25388_0000'' selon le fichier). Le
  producteur (équipe data.gouv) confirme et corrige ces bugs de correspondance au
  fil des signalements, ce qui prouve que la table de conversion table-bv-reu.csv
  et le pipeline id_brut_miom ne sont PAS stables par construction et nécessitent
  une maintenance corrective réactive scrutin par scrutin. La description du dataset
  avertit aussi que ''la structure des données a évolué en janvier 2026''. Un autre
  fil signale un jeu de données concurrent de Sciences Po (DOI 10.21410/7E4/B8OXBK)
  pour chaîner les CANDIDATS (pas les bureaux) d''une élection à l''autre via nom/prénom/date
  de naissance avec un script R de rapprochement gérant homonymies et variations orthographiques.
  Absence totale de circonscriptions pour les législatives 2024 dans le fichier agrégé
  (donnée non fournie par le Ministère à la source).'
---

*Suggested by [[jeu-de-donnes-donnes-des-lections-agrges-datagouvfr]] — checking discussions tab for bureau ID mismatch reports*

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
Votre question porte sur autre chose que ce jeu de données ? [Visiter notre forum](https://forum.data.gouv.fr/)
## 17 discussions dont 4 clotûrées 
Démarrer une nouvelle discussion
Discussion close par le 3 juin 2026
Bonjour, Le nom des candidats (hormis DROM) est manquant dans l'export maj avec les résultats des municipales de 2026. On les voit via l'explorateur en revanche, peut-être une erreur lors de l'export? Merci d'avance, Cordialement, 
—
Posté le 1 avril 2026
— 
Producteur
Bonjour, les noms des candidat.es sont absents du fichier source pour le 1er tour (https://www.data.gouv.fr/datasets/elections-municipales-2026-resultats-du-premier-tour?resource_id=1428132c-ad5e-437e-a928-7c2a254e40eb) et sont donc absents du fichier agrégé par candidat. Ils sont en revanche présents dans le fichier source du 2nd tour (https://www.data.gouv.fr/datasets/elections-municipales-2026-resultats-du-premier-tour?resource_id=1428132c-ad5e-437e-a928-7c2a254e40eb) et également présent dans le fichier agrégé. Cela répond-il à votre question ? 
—
Posté le 1 avril 2026
Bonjour, Oui merci. Cordialement, 
Bonjour, Les données du dictionnaire des nuances ne respectent pas la circulaire INTP2602966C annexe 3. Exemple : le parti socialiste est indiqué EXG alors que la circulaire indique GAU Cordialement, 
—
Posté le 24 mars 2026
— 
Producteur
Bonjour, merci de votre vigilance, nous venons de faire les corrections. 
Discussion close par le 20 mars 2026
Bonjour. Merci beaucoup pour ce jeu de données. Y a-t-il un jeu similaire agrégé par commune ? Merci beaucoup. 
—
Posté le 12 mars 2026
— 
Producteur
Bonjour, ce jeu de données est volontairement à la maille la plus fine (bureau de vote) et contient les codes des échelles supérieures (code département, code commune, code circonscription si disponible dans les données sources) afin de permettre les agrégations. 
Bonjour, Merci pour votre réactivité suite à ma demande précédente. Je reviens vers vous car j'ai rencontré d'autres régressions suite à la dernière mise à jour des données: - Un certain nombre de communes (principalement sur l'outre-mer dont les départements sont sur 3 caractères) ont été exprimées sur 6 caractères au lieu de 5 comme dans la convention INSEE. Par exemple, 971101 au lieu de 97101 en Guadeloupe (971). - J'ai l'impression qu'il y a eu une erreur de correspondance sur certains préfixes pour des communes d'outre-mer. Par exemple, ZM (Mayotte) donne 975xx au lieu de 976xx. - Un autre problème de correspondance concerne les codes des français de l'étranger (ZZ) qui devraient rester en ZZ mais qui sont transformés en 970, 971... ce qui ne correspond pas au code INSEE et collisionne avec les codes de certains départements d'outre-mer. - Certains bureaux de vote ne correspondent plus avec ceux données par le ministère de l'intérieur. Par exemple, aux législatives 2024, à Montbélliard, on a des 0X01, 0X02... au lieu de 0E11, 0E321 au tour 1. Merci d'avance 
Lire plus
—
Posté le 9 février 2026
— 
Producteur
Bonjour, merci pour ce second retour qui nous a permis de corriger les erreurs soulevées dans la version publiée ce jour. Bien à vous. 
—
Mis à jour le 9 février 2026
Bonjour, Merci de nouveau pour votre réactivité. La plupart des problèmes semblent résolus. J'observe encore des soucis de correspondances avec des codes d'outre-mer (sûrement un problème de correspondance code Z* vers 9**): - ZM (Mayotte): j'observe 975 au lieu de 976 (INSEE) - ZN (Nouvelle-Calédonie): j'observe 978 au lieu de 988 - ZP (Polynésie): j'observe 970/977 au lieu de 987 - ZW (Wallis-et-Futuna): j'observe 970 au lieu de 986 Il y aussi encore des problèmes de bureau en 0X*** au lieu de 0E*** pour Montbéliard dans candidats_results. Je rappelle que je ne travaille actuellement que sur les élections européennes, législatives et présidentielles. Peut-être que d'autres élections sont touchées par d'autres problèmes. Je vous remercie d'avance 
Lire plus
—
Posté le 11 février 2026
— 
Producteur
Bonjour, merci pour ces nouveaux retours, nous venons de publier une nouvelle version corrigée. N'hésitez pas à revenir vers nous si vous constatez d'autres incohérences. Bien à vous. 
Discussion close par le 6 février 2026
Bonjour, Bravo à l'équipe de data.gouv pour ce jeu de données agrégé, très utile. A toutes fins utiles, je me permets de signaler aussi que nous avons créé ce jeu de données pour suivre les candidats d'une élection à l'autre. https://data.sciencespo.fr/dataset.xhtml?persistentId=doi:10.21410/7E4/B8OXBK L'approche est différente, les résultats sont par circonscription et on se focalise sur les candidatEs en collectant le maximum d'information pour pouvoir les suivre d'une élection à l'autre. On propose en plus un script R de chaînage sur la base du nom, du prénom et de la date de naissance quand elle est disponible. On essaye de gérer au mieux les problèmes d'homonymie et de variations orthographiques. Bien à vous 
—
Mis à jour le 2 février 2026
— 
Producteur
Bonjour, merci pour ce partage. Je n'arrive pas à trouver ces données sur data.gouv.fr, est-ce qu'elles y sont bien référencées ? Je vois que vous ne faites pas partie de l'organisation Sciences Po (https://www.data.gouv.fr/organizations/sciences-po), dont les jeux de données semblent ne pas avoir été mis à jour depuis un certain temps. Nous pouvons valider une demande de rattachement si vous le souhaitez, afin que vous puissiez faire le nécessaire. Bien à vous. 
—
Posté le 2 février 2026
Merci pour votre réponse. Pour l'instant, le jeu de données n'est que sur le data de Sciences Po. Je pensais faire une mise à jour après les municipales et je réfléchirai à la possibilité de le mettre sur data.gouv également. 
Discussion close par le 4 février 2026
Bonjour, merci beaucoup pour ce travail d'agrégation extrêmement utile. J'ai constaté que le dictionnaire des nuances est incomplet, par exemple (je n'ai pas regardé sur d'autres scrutins) pour les européennes de 2024 il ne comporte pas les nuances LREC et LENS. Je sais que la documentation de ce fichier n'est pas exhaustif, mais sur ce cas précis les données semblent présentes à la source (https://www.archives-resultats-elections.interieur.gouv.fr/resultats/europeennes2024/referentiel.php), aussi je me dis qu'il devrait être possible d'améliorer la complétude de ce fichier ? Merci ! 
Pour le bureau de vote 01001_0001 Jean-Marie le Pen apparait 2 fois (avec les prenoms Jean-Marie & J.Marie et des scores differents), de meme que Patrick Louis (sous les nuance LDD et LDVD). 
—
Posté le 22 août 2025
— 
Producteur
Bonjour, le souci vient des données sources (https://www.data.gouv.fr/datasets/elections-europeennes-2009-resultats-par-bureaux-de-vote/#/resources/be1f18cf-c342-419b-879a-37f5312b9735), dans les premières lignes. Je ne saurais vous dire ce qui a amené à cette situation, d'autant que le nombre de votes est différent pour les deux lignes, je ne pense donc pas effectuer une correction. 
Bonjour, Tout d'abord merci à vous de ce travail! En utilisant ce dataset, j'ai remarqué des données candidats manquants pour les législatives 2024, notamment les candidats ENSEMBLE. Aucune trace par exemple de François Queste dans la circo 6203, ou encore Jean-Pierre Pont dans la circo6205. Pouvez-vous le confirmer ? Je vous remercie d'avance, Bap Triarii 
—
Posté le 14 août 2024
Bonjour, en effet je viens de comparer les données sources et nos fichiers, il semble que les lignes avec François Queste disparaissent dans le processus. Je corrige cela et met à jour le fichier, merci pour cette alerte. J'ai en revanche bien des candidatures au nom de Jean-Pierre Pont, mais peut-être pas dans la circonscription que vous évoquez. Le lien entre bureau de vote et circonscription n'étant pas simple, je ne peux pas vous répondre sur cette circonscription spécifique, mais j'ai autant de lignes (114) que dans le fichier source pour cette candidature. 
Bonjour, Ce serait bien d'avoir une colonne "circonscriptions", ou une table de correspondance "bureaux de vote / circonscriptions". Merci pour ces données. 
—
Posté le 26 juillet 2024
Bonjour, les circonscriptions sont bien dans le fichier (colonnes "Code de la circonscription" et "Libellé de la circonscription") si l'information est dans les données sources du Ministère de l'intérieur. 
—
Posté le 26 juillet 2024
Hélas, pas de circonscriptions pour les législatives 2024 ... Mais elles sont bien là pour les législatives 2022. Merci pour votre réponse. 
—
Posté le 21 août 2025
Les circonscriptions sont toujours manquantes pour les legislatives de 2024. Par ailleurs certains codes de bureaux de vote de Montbeliard son incorrects: '25388_0,00E+00' pour id_election = '2020_muni_t1' et id_brut_miom = '25388_0000' pour id_election = '2024_legi_t1' 
—
Posté le 22 août 2025
— 
Producteur
Bonjour, comme indiqué plus haut, les codes des circonscriptions sont présents uniquement s'ils le sont dans les données sources. Pour les législatives 2024, le MI n'a pas renseigné la circonscription dans les publications. Pour le code du bureau de vote de Montbéliard, la valeur "0,00E+00" est présente dans le fichier source (https://www.data.gouv.fr/datasets/elections-municipales-2020-resultats-1er-tour/#/resources/248f6f21-68ad-45f3-82f5-53fffabce5f3) lignes 14637 et suivantes. Je me note de retraiter cela à l'occasion, merci pour cette alerte. 
Bonjour, Sur Edge ou Chrome, lorsque l'on veut télécharger le fichier il ouvre une page web avec les enregistrements, je ne suis pas trés doué, et je voulais savoir si c'est normal. Sinon sur une version précédente, j'ai constaté que les nuances n'étaient pas systématique, est-ce normal ? Merci d'avance pour votre travail. 
—
Posté le 24 juin 2024
Bonjour, en effet c'est un effet indésirable de l'ajout de certaines métadonnées sur le fichier source, nous allons nous pencher dessus. En attendant, vous pouvez télécharger le fichier via : clic droit sur le bouton "Télécharger" puis "Enregistrer le lien sous". Les nuances sont présentes pour les élections où le fichier d'origine publié par le Ministère de l'Intérieur les contient. 
Bonjour, La question brûlante : quand intégrerez-vous les résultats des élections européennes 2024 ? C'est en ce moment que les analyses doivent se faire. A défaut, savez-vous où les résultats par bureau de vote auraient été publiés sur une base nationale ? Cordialement 
—
Posté le 11 juin 2024
Bonjour, ce jeu de données est une agrégation des données publiées par le Ministère de l'Intérieur, qui a la main sur les données sources. L'équipe de data.gouv.fr est également tributaire de leur mise à disposition par le ministère. Dès que ce sera le cas, les données seront ajoutées à ce jeu de données. D'ici-là, vous pouvez retrouver des données ici : https://www.resultats-elections.interieur.gouv.fr/telechargements/EU2024/ 
—
Posté le 11 juin 2024
Merci pour le lien mais il s'agit des données XML des pages web. Le récupérer sous une forme exploitable est assez fastidieux... (sauf si vous avez un outil à me conseiller...) Et en plus il n'y a pas les bureaux de vote. Ayant été assesseur d'un bureau, je suis surpris qu'on ne puisse vérifier que les résultats aient été correctement remontés et agrégés au niveau supérieur. 
—
Posté le 12 juin 2024
Bonjour, les résultats provisoire ont été publiés par le Ministère hier soir, nous venons de les intégrer aux fichiers agrégés. Nous les remplacerons par les résultats définitifs lorsqu'ils seront publiés. Cordialement. 
—
Posté le 12 juin 2024
Magnifique, merci. 
Super boulot, c'est très pratique, donc merci pour votre travail ! Juste une suggestion : vu la taille des fichiers, peut-être que ça vaudrait le coup de faire une diffusion au format Parquet? Je crois que le fichier candidats au format Parquet ne pèse pas plus de 200Mo, contre quasi 2GB au format CSV. Évidemment, ce n'est pas fondamental, mais ça ne peut pas faire de mal :-) 
—
Posté le 24 avril 2024
Bonjour, c'est un sujet sur lequel nous nous étions penchés sans aller au bout de la démarche, merci pour cette piqûre de rappel. C'est chose faite ! Cordialement. 
—
Posté le 24 avril 2024
Génial ! 
—
Posté le 29 avril 2024
Et merci pour cette conversion Parquet. À l'usage je constate la présence de quelques enregistrements décalés, qui compromettent le bon typage des colonnes numériques. Voici ma requête de reconversion avec DuckDB en un format optimisé (la compression zstd offre un meilleur compromis poids/vitesse de lecture), et avec un résultat allégé (190 Mo -> 110 Mo) copy ( FROM 'candidats_results.parquet' SELECT * replace( replace("% Voix/Ins",',','.')::float AS "% Voix/Ins", replace("% Voix/Exp",',','.')::float AS "% Voix/Exp", Voix::int AS Voix, "N°Panneau"::int AS "N°Panneau" ) WHERE trim(Voix) NOT IN ('LE LARDIN SAINT LAZARE CONTINUONS ENSEMBLE POUR VOUS ET AVEC VOUS', 'BRASPARZH D''AN HOLL','un nouveau départ') ) TO 'candidats_results2.parquet' (compression zstd); 
Lire plus
—
Posté le 3 mai 2024
Bonjour, merci pour ces précisions. Nous étions précédemment plutôt opposés à l'amendement des données malgré ces défauts que nous avions également repérés, car l'idée était de les agréger sans les toucher. Nous revenons finalement sur cette décision avec les fichiers publiés aujourd'hui : les erreurs que vous mentionnez y sont corrigées, et les colonnes correctement typées (ce qui n'était pas possible auparavant). Pour la compression, nous garderons (au moins dans un premier temps) "snappy", qui certes est légèrement moins efficiente (lecture et volume), mais selon la documentation "zstd" n'est pas encore largement adoptée (cf https://github.com/apache/parquet-format/blob/54e6133e887a6ea90501ddd72fff5312b7038a7c/src/main/thrift/parquet.thrift#L459) Bonne journée. 
—
Posté le 5 mai 2024
Bonjour, et merci pour votre prompte réponse et cette nouvelle version, bien plus maniable. Concernant la compression zstd, le lien que vous citez a plus de 6 ans. Aujourd'hui zstd est lu par tous les outils de manipulation de fichiers parquet dont je connais l'existence. zstd permettrait ici de réduire la taille du fichier de 40 % encore. 
—
Posté le 13 mai 2024
Bonjour, en effet je n'ai naïvement pas pensé à regarder le blame. Les fichiers ont été mis à jour en compression zstd. Bonne journée. 
—
Posté le 13 mai 2024
Bonjour, et merci beaucoup pour cette prise en compte ! 
Bonjour, comment se fait-il que les données des élections municipales de 2020 ne soit pas intégré ? Est-il prévu qu'elle le soit ? bonne journée Paul 
—
Posté le 26 octobre 2023
Bonjour, en effet c'est un oubli de notre part. Nous allons faire le nécessaire et vous tiendrons informé dans cette discussion. D'ici là, les données des municipales 2020 sont disponibles ici : - https://www.data.gouv.fr/fr/datasets/elections-municipales-2020-resultats-1er-tour/ - https://www.data.gouv.fr/fr/datasets/municipales-2020-resultats-2nd-tour/ Bonne journée. 
—
Posté le 26 octobre 2023
D'accord, Merci beaucoup ! 
—
Posté le 30 octobre 2023
Bonjour, c'est corrigé ! Bonne journée. 
—
Posté le 16 novembre 2023
Bonjour, merci pour cette correction. Je viens également de m'apercevoir qu'il manque les données pour les municipales de 2008 et de 2001. Est-ce possible de les ajouter ? Bonne soirée Paul 
—
Posté le 16 novembre 2023
Bonjour, Les données publiées par le Ministère de l'intérieur concernant les municipales 2001 sont au niveau de la commune (https://www.data.gouv.fr/fr/datasets/elections-municipales-2001-resultats-572156/), elles ne peuvent pas être intégrées au fichier consolidé qui est à la maille du bureau de vote. Concernant les municipales de 2008, la structure du fichier d'origine (https://www.data.gouv.fr/fr/datasets/elections-municipales-2008-communes-de-plus-de-3-500-habitants-resultats-par-bureaux-de-vote-1/) est moins facile à manipuler que les autres, nous nous y attèlerons ultérieurement. Merci de votre compréhension. Bonne journée. 
—
Posté le 17 novembre 2023
D'accord, merci beaucoup ! 
—
Posté le 18 décembre 2023
Bonjour, les données de l'élection municipales 2020 par bureau de vote sont inexploitables car il y a un décalage dans les colonnes. On se retrouve avec des noms de liste dans certaines colonnes voix. Cela est vrai pour le fichier txt et xlsx. 
—
Posté le 3 septembre 2024
Bonjour, les données des municipales 2008 viennent d'être ajoutées aux fichiers agrégés, avec cependant des contraintes liées aux données sources : uniquement les communes de plus de 3500 habitants ; votes blancs et nuls réunis dans la colonne `Nuls`. Cordialement. 

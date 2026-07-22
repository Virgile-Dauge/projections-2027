---
title: Report des voix entre les deux tours aux élections présidentielles en France
  | Freakonometrics
id: report-des-voix-entre-les-deux-tours-aux-lections-prsidentielles-en-france-freak
tags:
- projections-electorales-bureaux-2027-b0b1c4
- reports-de-voix
- regression-ecologique
- presidentielle-2022
- ecological-fallacy
- donnees-electorales
created: '2026-07-21T18:32:43.317712Z'
updated: '2026-07-21T18:39:17.761682Z'
source: https://web.archive.org/web/20220428115449/https://freakonometrics.hypotheses.org/63489
source_domain: web.archive.org
fetched_at: '2026-07-21T18:32:43.277124Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Billet de blog d''Arthur Charpentier (Freakonometrics, avril 2022, récupéré
  via Wayback Machine car anti-bot bloque le fetch direct) démontrant en R une méthode
  d''inférence des reports de voix par régression/corrélation sur les résultats agrégés
  du 1er et 2nd tour de la présidentielle 2022, au niveau département (~100 unités)
  et commune (36000, filtré >5000/10000 inscrits). Fournit les URLs directes data.gouv.fr
  des fichiers résultats T1/T2 par département et par commune utilisés (ex. loc_dpt_1,
  loc_com_1...). Constats empiriques : forte corrélation positive Le Pen T1 / Le Pen
  T2 par département et par commune (le report se fait vers elle-même) ; corrélation
  négative Macron T1 / Le Pen T2 (les communes qui ont peu voté Macron au T1 n''ont
  pas nécessairement voté Le Pen au T2) ; corrélation négative marquée vote écologiste
  T1 / Le Pen T2. L''auteur signale lui-même le risque de ''ecological fallacy'' (lien
  vers Wikipedia) en interprétant des corrélations agrégées comme des comportements
  individuels -- limite méthodologique centrale pour toute approche de régression
  sur résultats agrégés au niveau fin (axe 1/2).'
---

[ OpenEdition Search ](javascript:;)
All OpenEdition
The Wayback Machine - https://web.archive.org/web/20220428115449/https://freakonometrics.hypotheses.org/63489
Allez, on va profiter des élections présidentielles, à deux tours, en France, pour jouer un peu, maintenant que les données commencent à être disponibles. On peut avoir les données par département (une centaine) ou par commune (36000)  
| 
```
# département
loc_dpt_1 = "https://www.data.gouv.fr/fr/datasets/r/312b99d0-27a7-429e-be8a-b930975545e9"
loc_dpt_2 = "https://www.data.gouv.fr/fr/datasets/r/c7b72e78-5e78-4976-995f-30533f0a35d3"
# commune
loc_com_1 = "https://www.data.gouv.fr/fr/datasets/r/54782507-e795-4f9d-aa70-ed06feba22e3"
loc_com_2 = "https://www.data.gouv.fr/fr/datasets/r/1601b027-48d1-42b1-96f1-b0fb49f55aa3"
download.file(loc_dpt_1,"dpt1.csv")
download.file(loc_dpt_2,"dpt2.csv")
d1 = read.csv("dpt1.csv")
d2 = read.csv("dpt2.csv")
download.file(loc_com_1,"com1.csv")
download.file(loc_com_2,"com2.csv")
c1 = read.csv("com1.csv")
c2 = read.csv("com2.csv")
```
 |  
| --- |  
# département loc_dpt_1 = "https://www.data.gouv.fr/fr/datasets/r/312b99d0-27a7-429e-be8a-b930975545e9" loc_dpt_2 = "https://www.data.gouv.fr/fr/datasets/r/c7b72e78-5e78-4976-995f-30533f0a35d3" # commune loc_com_1 = "https://www.data.gouv.fr/fr/datasets/r/54782507-e795-4f9d-aa70-ed06feba22e3" loc_com_2 = "https://www.data.gouv.fr/fr/datasets/r/1601b027-48d1-42b1-96f1-b0fb49f55aa3" download.file(loc_dpt_1,"dpt1.csv") download.file(loc_dpt_2,"dpt2.csv") d1 = read.csv("dpt1.csv") d2 = read.csv("dpt2.csv") download.file(loc_com_1,"com1.csv") download.file(loc_com_2,"com2.csv") c1 = read.csv("com1.csv") c2 = read.csv("com2.csv")
Commençons par les départements. On peut récupérer les pourcentages de voix obtenus par les différents candidats, au premier tour, et regarder les pourcentages obtenus par Marine Le Pen. Par exemple, on peut regarder, département par département, le score de Marine Le Pen au premier et au second tour, pour vérifier que le report des voix s’opère bien  
| 
```
D1 = d1[d1$cand_nom=="LE PEN",c("dep_code","cand_rapport_inscrits","cand_rapport_exprim")]
D2 = d2[,c("CodeDépartement","LE.PEN.ins","LE.PEN.exp")]
names(D1) = c("dep_code","ins1","exp1")
names(D2) = c("dep_code","ins2","exp2")
D = merge(D1,D2)
par(mfrow=c(1,2))
plot(D$ins1,D$ins2,xlab="inscrits (%), premier tour",ylab="inscrits (%), second tour",col=colr2[1])
plot(D$exp1,D$exp2,xlab="exprimés (%), premier tour",ylab="exprimés (%), second tour",col=colr2[2],main="Le Pen / Le Pen",cex.main=1.1)
```
 |  
| --- |  
D1 = d1[d1$cand_nom=="LE PEN",c("dep_code","cand_rapport_inscrits","cand_rapport_exprim")] D2 = d2[,c("CodeDépartement","LE.PEN.ins","LE.PEN.exp")] names(D1) = c("dep_code","ins1","exp1") names(D2) = c("dep_code","ins2","exp2") D = merge(D1,D2) par(mfrow=c(1,2)) plot(D$ins1,D$ins2,xlab="inscrits (%), premier tour",ylab="inscrits (%), second tour",col=colr2[1]) plot(D$exp1,D$exp2,xlab="exprimés (%), premier tour",ylab="exprimés (%), second tour",col=colr2[2],main="Le Pen / Le Pen",cex.main=1.1)
Comme on pouvait s’y attendre, on a une belle droite de régression, avec les nombres de voix obtenus, relativement aux inscrits, en bleu, et aux exprimés, à droite. Pour Emmanuel Macron au premier et Marine Le Pen au second tour, on a une belle corrélation négative, mais moins prononcée qu’auparavant. Autrement dit, un département qui votait peu Macron au premier tour a beaucoup voté Le Pen au second
Mais là, on parlait des deux candidats qui se sont maintenus. Si on regarde l’autre candidat de l’extrême droite, les reports sont assez étranges… après, les taux étaient “relativement” faibles au premier tour pour Erik Zemmour.
Pour le candidat en tête à gauche, on a une corrélation négative, mais sur les votes exprimées, on observera des outliers en haut à droite, avec manifestement un vote d’opposition au président sortant dans certains départements
Pour le candidat écologiste, la corrélation est elle encore plus clair
autrement dit, quand on a voté écologiste au premier tour, on avait peu tendance à voter Le Pen (ou disons les départements où on votait fortement écologiste n’ont pas voté Le Pen au second [#ecologicalfallacy](https://web.archive.org/web/20220428115449/https://en.wikipedia.org/wiki/Ecological_fallacy), etc).
Mais on peut faire le même exercice par commune. Mon seul soucis a été que les codes communes dans les deux bases étaient différents, donc j’ai utilisé les noms des communes, ce que je n’aime pas faire (avec les accents, les tirets, etc, la fusion peut être assez mauvaises… mais là ça marche bien). Je me suis ensuite limité aux grosses communes, de plus de 10000 inscrits,  
| 
```
C1 = c1[c1$cand_nom=="LE PEN",c("commune_name","cand_rapport_inscrits","cand_rapport_exprim","votants_nb")]
C2 = c2[,c("Commune","LE.PEN.ins","LE.PEN.exp")]
names(C1) = c("com_code","ins1","exp1","taille")
names(C2) = c("com_code","ins2","exp2")
D = merge(C1,C2)
D = D[D$taillegt;5000,]
par(mfrow=c(1,2))
plot(D$ins1,D$ins2,xlab="inscrits (%), premier tour",ylab="inscrits (%), second tour",col=colr2[1])
plot(D$exp1,D$exp2,xlab="exprimés (%), premier tour",ylab="exprimés (%), second tour",col=colr2[2],main="Le Pen / Le Pen",cex.main=1.1)
```
 |  
| --- |  
C1 = c1[c1$cand_nom=="LE PEN",c("commune_name","cand_rapport_inscrits","cand_rapport_exprim","votants_nb")] C2 = c2[,c("Commune","LE.PEN.ins","LE.PEN.exp")] names(C1) = c("com_code","ins1","exp1","taille") names(C2) = c("com_code","ins2","exp2") D = merge(C1,C2) D = D[D$taille&gt;5000,] par(mfrow=c(1,2)) plot(D$ins1,D$ins2,xlab="inscrits (%), premier tour",ylab="inscrits (%), second tour",col=colr2[1]) plot(D$exp1,D$exp2,xlab="exprimés (%), premier tour",ylab="exprimés (%), second tour",col=colr2[2],main="Le Pen / Le Pen",cex.main=1.1)
On peut alors faire le même exercice, avec Le Pen au premier et second tour
ou Macron au premier, Le Pen au second
On observe des beaux nuages, sur la gauche, respectivement en haut et en bas… Beaucoup de communes qui avaient peu voté pour Le Pen semblent avoir eu peur, et on massivement voté au second pour elle. Alors que ce n’est pas trop le cas pour celles où Le Pen avait obtenu beaucoup de voix. Et pour Macron, c’est en bas à gauche, autrement dit, beaucoup de communes qui n’ont pas voté Macron au premier tour n’ont pas pour autant voté Le Pen au second. Pour ceux que ça amuse, les codes sont disponibles pour regarder qui sont ces communes dans les coins.
Pour Zemmour, c’est assez confus, j’avoue, le personnage est déroutant (ou dégoutant ? comme le suggérait le correcteur automatique)
ou alors Jean Luc Mélanchon
ou la relativement franche corrélation des écologistes, qui semblent résolument aller en sens inverse avec le vote d’extrême droite…
### Leave a Reply 
This site uses Akismet to reduce spam. [Learn how your comment data is processed](https://web.archive.org/web/20220428115449/https://akismet.com/privacy/).
## An Open Lab-Notebook Experiment
OpenEdition Books Calenda Hypothèses OpenEdition Journals OpenEdition OpenEdition Search
  *[RSS]: Really Simple Syndication

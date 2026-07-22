# Rapport de churn — étape 0

Mesure du churn (CONTEXT.md) : la grandeur à minimiser est la **part des
inscrits** en zone instable, jamais un compte de communes ou de bureaux —
des unités de tailles trop inégales pour être comparées. L'instabilité est
détectée par commune : le nombre de bureaux change entre les
4 scrutins sources (présidentielle 2022, législatives
2022, législatives 2024, européennes 2024), sans crosswalk REU — comparaison
brute `id_election` × `code_commune` (HANDOFF.md, étape 0).

## Churn national

**14.9%** des inscrits (référence : 2024_legi_t1) sont
situés dans une commune instable et passent en repli à la maille communale
plutôt qu'en jointure directe par bureau — la part des inscrits en zone
instable (CONTEXT.md « Churn »). Pour contexte : cela représente
**1.4%** des 35258 communes du panel, un
compte à part (les communes ont des tailles trop inégales pour être
comparées directement).

## Réconciliation de Paris (second étage du repli)

Paris (75056, département 75) sort du repli communal (issue #14) : c'est la
commune la plus lourde en zone instable (voir top 20 ci-dessous), pour un
outil dont le cœur de cible est le ciblage fin en zone urbaine dense. Ses
bureaux sont réconciliés un à un entre les 4 scrutins
sources plutôt qu'agrégés en un seul bloc départemental.

**Méthode.** La grille cible (bureaux + inscrits) est celle du scrutin le
plus récent (2024_legi_t1). Pour chaque scrutin source, les bureaux
dont l'`id_bv` figure tel quel dans cette grille passent inchangés (statut
`reconcilie`). Le reliquat — voix et participation des bureaux orphelins côté
source — est réalloué **en comptes de voix**, au prorata des inscrits
(jamais de la surface, CONTEXT.md « Repli ») des bureaux orphelins côté
cible (statut `realloue`) ; les ratios se recalculent ensuite depuis ces
comptes, jamais l'inverse. Un bureau cible sans aucun reliquat exploitable
reste `irresoluble` (statut explicite, voix à `null`, jamais un zéro
fabriqué) — distinct à la fois de `joint_valide` (commune stable) et de
`repli` (commune instable non réconciliée).

**Hypothèses et cas non résolus.** Sur les données réelles, l'essentiel du
désaccord entre scrutins parisiens est une pure renumérotation administrative
d'une quarantaine de bureaux contigus (ex. `0201`→`0211` entre 2022 et 2024),
à inscrits quasi identiques : le crosswalk parisien est mécaniquement
trivial, pas un vrai découpage ou une fusion de zones. La réallocation ne
cherche pas à retrouver cette bijection cachée (aucun crosswalk adresses/IRIS
disponible) : elle répartit le reliquat au prorata des inscrits sur
l'ensemble des bureaux orphelins du même scrutin — une approximation très
proche de la vérité dans ce cas précis, qui le serait moins sur une commune
au redécoupage plus disruptif. Le second tour des législatives (ballottage
partiel, pas de second tour dans toutes les circonscriptions) est exclu de la
réallocation : les bureaux non appariés y restent silencieusement absents,
comme pour une commune stable. Le mécanisme (`COMMUNES_RECONCILIATION_BUREAU`)
est générique mais volontairement limité à Paris ici : l'étendre à d'autres
grandes villes à arrondissements (Lyon, Marseille, également instables) est
laissé à une itération suivante.

**Gain chiffré.** Avant réconciliation (Paris à 100 % en repli communal,
comme toute commune instable) : **14.9%** des inscrits en zone
instable. Après réconciliation bureau de Paris : **12.2%** — gain
de **2.8 point(s)**.

## Distribution par département

Triée par inscrits en zone instable décroissant (l'ordre de la charge de
travail) ; le taux instable communal reste en colonne (intensité) mais ne
pilote plus le tri. Ratios recalculés depuis les sommes d'inscrits, jamais
en moyennant des taux communaux.

| Département | Inscrits en zone instable | % des inscrits du département | Communes | dont instables | Taux instable (communes) |
| --- | --- | --- | --- | --- | --- |
| 75 | 1365376 | 100.0% | 1 | 1 | 100.0% |
| 13 | 730998 | 50.8% | 119 | 14 | 11.8% |
| 69 | 381047 | 31.7% | 267 | 16 | 6.0% |
| 33 | 331169 | 28.0% | 535 | 16 | 3.0% |
| 31 | 329157 | 34.6% | 586 | 10 | 1.7% |
| 44 | 316990 | 29.5% | 208 | 16 | 7.7% |
| 92 | 274321 | 27.1% | 36 | 8 | 22.2% |
| 06 | 236995 | 30.2% | 163 | 2 | 1.2% |
| 93 | 203848 | 24.9% | 40 | 9 | 22.5% |
| 49 | 189855 | 31.8% | 178 | 15 | 8.4% |
| 94 | 185266 | 23.0% | 47 | 9 | 19.1% |
| 35 | 170789 | 21.7% | 333 | 13 | 3.9% |
| 34 | 150731 | 17.4% | 342 | 16 | 4.7% |
| 67 | 147938 | 18.8% | 514 | 3 | 0.6% |
| 76 | 144216 | 16.4% | 708 | 7 | 1.0% |
| 74 | 127772 | 22.1% | 279 | 9 | 3.2% |
| 95 | 118045 | 15.9% | 184 | 12 | 6.5% |
| 38 | 104003 | 11.7% | 512 | 5 | 1.0% |
| 51 | 103701 | 27.1% | 613 | 6 | 1.0% |
| 30 | 96714 | 17.2% | 351 | 3 | 0.9% |
| 83 | 92668 | 11.2% | 153 | 9 | 5.9% |
| 85 | 88721 | 15.8% | 259 | 18 | 6.9% |
| 77 | 88182 | 9.6% | 507 | 10 | 2.0% |
| 78 | 85343 | 8.7% | 259 | 8 | 3.1% |
| 11 | 83372 | 29.6% | 433 | 6 | 1.4% |
| 50 | 76689 | 20.0% | 446 | 8 | 1.8% |
| 80 | 76151 | 18.6% | 772 | 4 | 0.5% |
| 988 | 74657 | 33.6% | 33 | 2 | 6.1% |
| 91 | 61771 | 7.7% | 194 | 5 | 2.6% |
| 22 | 61344 | 12.9% | 348 | 4 | 1.1% |
| 973 | 51918 | 47.7% | 22 | 4 | 18.2% |
| 40 | 50096 | 15.0% | 327 | 9 | 2.8% |
| 68 | 49522 | 9.3% | 366 | 2 | 0.5% |
| 59 | 44414 | 2.4% | 648 | 6 | 0.9% |
| 62 | 42917 | 3.9% | 890 | 8 | 0.9% |
| 71 | 40030 | 10.0% | 565 | 5 | 0.9% |
| 987 | 38366 | 18.1% | 48 | 3 | 6.2% |
| 19 | 35478 | 19.2% | 279 | 3 | 1.1% |
| 2B | 30411 | 23.4% | 236 | 3 | 1.3% |
| 29 | 27317 | 3.8% | 277 | 5 | 1.8% |
| 57 | 26742 | 3.6% | 725 | 4 | 0.6% |
| 04 | 24276 | 18.9% | 198 | 10 | 5.1% |
| 26 | 23945 | 6.2% | 363 | 5 | 1.4% |
| 88 | 22560 | 8.2% | 507 | 2 | 0.4% |
| 03 | 20933 | 8.4% | 317 | 1 | 0.3% |
| 27 | 20456 | 4.7% | 586 | 4 | 0.7% |
| 14 | 20453 | 4.0% | 529 | 5 | 0.9% |
| 17 | 19994 | 3.8% | 463 | 6 | 1.3% |
| 25 | 19826 | 5.4% | 571 | 5 | 0.9% |
| 12 | 18608 | 8.5% | 285 | 14 | 4.9% |
| 66 | 18159 | 4.9% | 226 | 5 | 2.2% |
| 45 | 15550 | 3.4% | 325 | 3 | 0.9% |
| 01 | 15053 | 3.4% | 393 | 6 | 1.5% |
| 56 | 14490 | 2.4% | 249 | 3 | 1.2% |
| 32 | 14028 | 9.5% | 461 | 1 | 0.2% |
| 43 | 13607 | 7.5% | 257 | 4 | 1.6% |
| 73 | 11179 | 3.5% | 273 | 4 | 1.5% |
| 08 | 11064 | 6.0% | 449 | 3 | 0.7% |
| 971 | 10472 | 3.3% | 32 | 1 | 3.1% |
| 60 | 9777 | 1.7% | 680 | 8 | 1.2% |
| 86 | 9676 | 3.1% | 266 | 4 | 1.5% |
| 28 | 9277 | 3.0% | 365 | 4 | 1.1% |
| 986 | 9031 | 100.0% | 1 | 1 | 100.0% |
| 84 | 7311 | 1.8% | 151 | 2 | 1.3% |
| 64 | 6973 | 1.3% | 546 | 3 | 0.5% |
| 54 | 6926 | 1.4% | 591 | 2 | 0.3% |
| 16 | 6361 | 2.5% | 364 | 6 | 1.6% |
| 24 | 6223 | 1.9% | 503 | 2 | 0.4% |
| 61 | 5209 | 2.6% | 385 | 3 | 0.8% |
| ZZ | 4600 | 0.3% | 214 | 5 | 2.3% |
| 72 | 4483 | 1.1% | 354 | 2 | 0.6% |
| 42 | 4440 | 0.9% | 323 | 1 | 0.3% |
| 37 | 3832 | 0.9% | 272 | 2 | 0.7% |
| 53 | 3455 | 1.5% | 240 | 1 | 0.4% |
| 47 | 3357 | 1.4% | 319 | 2 | 0.6% |
| 2A | 3211 | 2.8% | 124 | 1 | 0.8% |
| 02 | 2346 | 0.6% | 801 | 6 | 0.7% |
| 41 | 2132 | 0.9% | 267 | 1 | 0.4% |
| 07 | 1895 | 0.7% | 335 | 1 | 0.3% |
| 21 | 1714 | 0.5% | 698 | 2 | 0.3% |
| 05 | 1661 | 1.4% | 162 | 1 | 0.6% |
| 79 | 1603 | 0.6% | 256 | 2 | 0.8% |
| 15 | 1408 | 1.2% | 246 | 1 | 0.4% |
| 82 | 1387 | 0.7% | 195 | 2 | 1.0% |
| 63 | 1325 | 0.3% | 464 | 2 | 0.4% |
| 52 | 975 | 0.8% | 426 | 2 | 0.5% |
| 46 | 851 | 0.6% | 313 | 2 | 0.6% |
| 09 | 659 | 0.6% | 327 | 3 | 0.9% |
| 89 | 553 | 0.2% | 423 | 2 | 0.5% |
| 39 | 285 | 0.1% | 494 | 1 | 0.2% |
| 48 | 240 | 0.4% | 152 | 1 | 0.7% |
| 18 | 206 | 0.1% | 287 | 2 | 0.7% |
| 10 | 0 | 0.0% | 431 | 0 | 0.0% |
| 23 | 0 | 0.0% | 256 | 0 | 0.0% |
| 36 | 0 | 0.0% | 241 | 0 | 0.0% |
| 55 | 0 | 0.0% | 493 | 0 | 0.0% |
| 58 | 0 | 0.0% | 309 | 0 | 0.0% |
| 65 | 0 | 0.0% | 469 | 0 | 0.0% |
| 70 | 0 | 0.0% | 539 | 0 | 0.0% |
| 81 | 0 | 0.0% | 314 | 0 | 0.0% |
| 87 | 0 | 0.0% | 195 | 0 | 0.0% |
| 90 | 0 | 0.0% | 101 | 0 | 0.0% |
| 972 | 0 | 0.0% | 34 | 0 | 0.0% |
| 974 | 0 | 0.0% | 24 | 0 | 0.0% |
| 975 | 0 | 0.0% | 2 | 0 | 0.0% |
| 976 | 0 | 0.0% | 17 | 0 | 0.0% |
| ZX | 0 | 0.0% | 2 | 0 | 0.0% |

## Top 20 communes instables par inscrits

Cible concrète de la réconciliation bureau par réallocation dasymétrique
(CONTEXT.md « Repli ») : où chaque effort récupère le plus d'électorat, à la
granularité fine. Paris (#1) y est déjà traitée (issue #14, cf. section
ci-dessus) ; le reste de la liste reste en repli communal classique.

| Commune | Département | Bureaux | Inscrits |
| --- | --- | --- | --- |
| 75056 | 75 | 902 | 1365376 |
| 13055 | 13 | 497 | 536608 |
| 69123 | 69 | 306 | 296248 |
| 31555 | 31 | 277 | 266176 |
| 06088 | 06 | 256 | 222427 |
| 44109 | 44 | 208 | 198523 |
| 33063 | 33 | 153 | 166593 |
| 67482 | 67 | 146 | 142668 |
| 35238 | 35 | 113 | 124377 |
| 76351 | 76 | 110 | 102073 |
| 51454 | 51 | 106 | 101143 |
| 13001 | 13 | 101 | 95977 |
| 49007 | 49 | 85 | 93543 |
| 30189 | 30 | 86 | 92223 |
| 74010 | 74 | 88 | 86971 |
| 38185 | 38 | 82 | 81634 |
| 80021 | 80 | 73 | 73675 |
| 98818 | 988 | 57 | 72749 |
| 50129 | 50 | 59 | 55387 |
| 44184 | 44 | 54 | 51985 |

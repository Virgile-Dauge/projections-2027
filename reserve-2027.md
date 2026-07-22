# Réserve de voix par bureau × bloc — estimateur v1 (issue #25, ADR 0002)

Couche *estimation* du pivot mobilisation (`docs/adr/0002-pivot-mobilisation-reserve.md`) :
le gisement de voix mobilisables d'un bloc dans une unité (bureau ou commune),
défini par la formule v1 du glossaire (CONTEXT.md « Réserve d'abstention »).
Non backtestable par construction (pas de vérité terrain) — validée par
définition ex ante, analyse de sensibilité (section 3) et appel public à
contradiction, jamais par un gate PASS/FAIL comme les backtests structure/
participation de `projections.backtest` (issue #24).

**⚠ PRÉPARATION SEULEMENT — non publiable en carte tant que la révision (issue #28) n'a pas tranché.** Le gate de publication de la carte mobilisation (ADR 0002 point 5, réutilisation de `projections.backtest.verdict_carte_mobilisation`) est **FAIL** : le backtest participation est sorti rouge (ρ europ. 0,769 < 0,8, voir `backtest-2022-2024.md` §4). Cette table et ce rapport sont publiés tels quels, en préparation de la carte — aucun chiffre n'est caché — mais aucune publication cartographique n'est autorisée avant que la révision d'architecture (#28) ne tranche. Les seuils ne bougent pas.

## Formule

    réserve(unité, bloc) = inscrits × abstention à la présidentielle 2022 T1
                            (scrutin de même enjeu que la cible 2027)
                            × part estimée du bloc (méthode : « proportionnelle_aux_votants »)

Participation dédupliquée par unité avant tout produit (`projections.backtest.calculer_taux_abstention`,
réutilisée telle quelle). Intermittents (votants présidentielle absents des
scrutins intermédiaires) exclus par construction : seul le scrutin de
référence alimente le volume.

## 1. Statut de réconciliation propagé (aucun état silencieux)

Chaque unité de la table réserve porte le statut hérité du panel
(`projections.churn`) : `joint_valide`/`reconcilie`/`realloue` -> maille
bureau ; `repli` -> maille communale (jamais déguisée en bureau). **256448**
lignes unité × bloc au total.

| Statut | Unités |
| --- | --- |
| joint_valide | 62746 |
| realloue | 24 |
| reconcilie | 878 |
| repli | 464 |

## 2. Top gisements

### Par bloc, à la maille de l'unité (bureau ou commune)

| Bloc | Unité | Département | Statut | Maille | Réserve (voix) |
| --- | --- | --- | --- | --- | --- |
| Centre | ZZ119_0001 | ZZ | joint_valide | bureau | 41565 |
| Centre | 13055 | 13 | repli | commune | 40347 |
| Centre | ZZ079_0001 | ZZ | joint_valide | bureau | 31711 |
| Centre | ZZ039_0001 | ZZ | joint_valide | bureau | 22331 |
| Centre | 06088 | 06 | repli | commune | 17782 |
| Centre | 98818 | 988 | repli | commune | 17596 |
| Centre | 69123 | 69 | repli | commune | 17580 |
| Centre | 31555 | 31 | repli | commune | 17044 |
| Centre | 44109 | 44 | repli | commune | 14999 |
| Centre | ZZ139_0001 | ZZ | joint_valide | bureau | 14177 |
| Centre | 33063 | 33 | repli | commune | 13600 |
| Centre | ZZ209_0001 | ZZ | joint_valide | bureau | 13525 |
| Centre | ZZ147_0001 | ZZ | joint_valide | bureau | 12116 |
| Centre | ZZ124_0001 | ZZ | joint_valide | bureau | 11896 |
| Centre | ZZ120_0001 | ZZ | joint_valide | bureau | 11610 |
| Centre | 67482 | 67 | repli | commune | 11477 |
| Centre | 51454 | 51 | repli | commune | 10175 |
| Centre | ZZ183_0001 | ZZ | joint_valide | bureau | 9979 |
| Centre | 76351 | 76 | repli | commune | 9676 |
| Centre | ZZ027_0001 | ZZ | joint_valide | bureau | 9653 |
| Droite | 13055 | 13 | repli | commune | 7450 |
| Droite | ZZ079_0001 | ZZ | joint_valide | bureau | 4716 |
| Droite | 06088 | 06 | repli | commune | 4653 |
| Droite | ZZ119_0001 | ZZ | joint_valide | bureau | 4198 |
| Droite | 98818 | 988 | repli | commune | 3732 |
| Droite | 69123 | 69 | repli | commune | 3567 |
| Droite | 31555 | 31 | repli | commune | 2934 |
| Droite | 44109 | 44 | repli | commune | 2878 |
| Droite | ZZ209_0001 | ZZ | joint_valide | bureau | 2799 |
| Droite | ZZ039_0001 | ZZ | joint_valide | bureau | 2739 |
| Droite | 33063 | 33 | repli | commune | 2434 |
| Droite | 51454 | 51 | repli | commune | 1958 |
| Droite | ZZ124_0001 | ZZ | joint_valide | bureau | 1864 |
| Droite | 67482 | 67 | repli | commune | 1837 |
| Droite | 13001 | 13 | repli | commune | 1798 |
| Droite | ZZ139_0001 | ZZ | joint_valide | bureau | 1745 |
| Droite | 49007 | 49 | repli | commune | 1701 |
| Droite | 30189 | 30 | repli | commune | 1649 |
| Droite | 74010 | 74 | repli | commune | 1569 |
| Droite | 35238 | 35 | repli | commune | 1418 |
| Extrême droite | 13055 | 13 | repli | commune | 53211 |
| Extrême droite | ZZ209_0001 | ZZ | joint_valide | bureau | 25195 |
| Extrême droite | 06088 | 06 | repli | commune | 24160 |
| Extrême droite | ZZ079_0001 | ZZ | joint_valide | bureau | 11302 |
| Extrême droite | 98818 | 988 | repli | commune | 11244 |
| Extrême droite | 51454 | 51 | repli | commune | 9655 |
| Extrême droite | 31555 | 31 | repli | commune | 9339 |
| Extrême droite | 69123 | 69 | repli | commune | 8790 |
| Extrême droite | 76351 | 76 | repli | commune | 8426 |
| Extrême droite | 30189 | 30 | repli | commune | 8267 |
| Extrême droite | ZZ092_0001 | ZZ | joint_valide | bureau | 7499 |
| Extrême droite | 44109 | 44 | repli | commune | 6891 |
| Extrême droite | ZZ039_0001 | ZZ | joint_valide | bureau | 6385 |
| Extrême droite | 67482 | 67 | repli | commune | 6166 |
| Extrême droite | 13001 | 13 | repli | commune | 6127 |
| Extrême droite | ZZ119_0001 | ZZ | joint_valide | bureau | 6003 |
| Extrême droite | 33063 | 33 | repli | commune | 5880 |
| Extrême droite | 34032 | 34 | repli | commune | 5618 |
| Extrême droite | ZZ124_0001 | ZZ | joint_valide | bureau | 5361 |
| Extrême droite | 80021 | 80 | repli | commune | 5307 |
| Gauche | 13055 | 13 | repli | commune | 65355 |
| Gauche | 31555 | 31 | repli | commune | 29247 |
| Gauche | ZZ119_0001 | ZZ | joint_valide | bureau | 25305 |
| Gauche | 44109 | 44 | repli | commune | 23492 |
| Gauche | ZZ039_0001 | ZZ | joint_valide | bureau | 23055 |
| Gauche | 69123 | 69 | repli | commune | 22888 |
| Gauche | ZZ139_0001 | ZZ | joint_valide | bureau | 22804 |
| Gauche | ZZ079_0001 | ZZ | joint_valide | bureau | 21306 |
| Gauche | 06088 | 06 | repli | commune | 19196 |
| Gauche | 67482 | 67 | repli | commune | 16669 |
| Gauche | 33063 | 33 | repli | commune | 16112 |
| Gauche | 35238 | 35 | repli | commune | 15830 |
| Gauche | 76351 | 76 | repli | commune | 13548 |
| Gauche | 38185 | 38 | repli | commune | 12082 |
| Gauche | 51454 | 51 | repli | commune | 11064 |
| Gauche | 49007 | 49 | repli | commune | 10622 |
| Gauche | 30189 | 30 | repli | commune | 10604 |
| Gauche | ZZ027_0001 | ZZ | joint_valide | bureau | 9813 |
| Gauche | ZZ124_0001 | ZZ | joint_valide | bureau | 9460 |
| Gauche | 80021 | 80 | repli | commune | 9454 |

### Par bloc et par département (réserve agrégée par SOMME, jamais une moyenne)

| Bloc | Département | Réserve (voix) |
| --- | --- | --- |
| Centre | ZZ | 423979 |
| Centre | 59 | 135003 |
| Centre | 75 | 103699 |
| Centre | 13 | 94259 |
| Centre | 33 | 80635 |
| Centre | 44 | 79779 |
| Centre | 69 | 77880 |
| Centre | 92 | 76236 |
| Centre | 62 | 72809 |
| Centre | 78 | 70264 |
| Centre | 76 | 64582 |
| Centre | 67 | 62161 |
| Centre | 974 | 58891 |
| Centre | 35 | 58831 |
| Centre | 77 | 58629 |
| Centre | 57 | 58388 |
| Centre | 31 | 57279 |
| Centre | 94 | 56600 |
| Centre | 06 | 56436 |
| Centre | 38 | 56384 |
| Droite | ZZ | 51971 |
| Droite | 59 | 23135 |
| Droite | 75 | 21052 |
| Droite | 13 | 20424 |
| Droite | 78 | 19496 |
| Droite | 92 | 18041 |
| Droite | 69 | 17160 |
| Droite | 77 | 16807 |
| Droite | 06 | 16277 |
| Droite | 987 | 16072 |
| Droite | 974 | 15653 |
| Droite | 44 | 15161 |
| Droite | 83 | 15003 |
| Droite | 33 | 14621 |
| Droite | 91 | 14577 |
| Droite | 67 | 13469 |
| Droite | 62 | 12999 |
| Droite | 988 | 12945 |
| Droite | 94 | 12921 |
| Droite | 57 | 12109 |
| Extrême droite | 59 | 180891 |
| Extrême droite | ZZ | 150404 |
| Extrême droite | 13 | 139229 |
| Extrême droite | 62 | 128122 |
| Extrême droite | 83 | 92163 |
| Extrême droite | 974 | 89720 |
| Extrême droite | 06 | 83607 |
| Extrême droite | 57 | 78531 |
| Extrême droite | 76 | 72069 |
| Extrême droite | 33 | 69202 |
| Extrême droite | 34 | 67424 |
| Extrême droite | 77 | 67117 |
| Extrême droite | 69 | 62293 |
| Extrême droite | 67 | 60985 |
| Extrême droite | 38 | 59241 |
| Extrême droite | 60 | 54602 |
| Extrême droite | 44 | 52190 |
| Extrême droite | 30 | 50089 |
| Extrême droite | 68 | 47921 |
| Extrême droite | 78 | 46735 |
| Gauche | ZZ | 300408 |
| Gauche | 59 | 175004 |
| Gauche | 974 | 148895 |
| Gauche | 93 | 140498 |
| Gauche | 75 | 130811 |
| Gauche | 13 | 129904 |
| Gauche | 971 | 107195 |
| Gauche | 972 | 106669 |
| Gauche | 69 | 98247 |
| Gauche | 44 | 89208 |
| Gauche | 94 | 88691 |
| Gauche | 95 | 84917 |
| Gauche | 33 | 84556 |
| Gauche | 92 | 80484 |
| Gauche | 77 | 80377 |
| Gauche | 91 | 78246 |
| Gauche | 78 | 75214 |
| Gauche | 76 | 73653 |
| Gauche | 62 | 72337 |
| Gauche | 38 | 70901 |

## 3. Distribution de la réserve par bloc

| Bloc | n | min | p25 | médiane | p75 | max | moyenne |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Centre | 64052 | 0.0 | 16.0 | 46.4 | 70.1 | 41564.5 | 60.7 |
| Droite | 64052 | 0.0 | 4.0 | 9.5 | 15.4 | 7449.5 | 13.0 |
| Extrême droite | 64052 | 0.0 | 19.1 | 42.8 | 72.1 | 53211.5 | 58.4 |
| Gauche | 64052 | 0.0 | 13.2 | 40.6 | 72.5 | 65355.1 | 68.0 |

## 4. Sensibilité H1 (analyse ex ante, ADR 0002 point 3)

H1 (CONTEXT.md) : la répartition politique des abstentionnistes ≈ celle des
votants du bureau (méthode par défaut, `proportionnelle_aux_votants`). Variante testée pour
la sensibilité : `uniforme_entre_blocs` (répartition égale entre les blocs
présents). `rho` : Spearman des valeurs de réserve entre les 2 méthodes (1 =
classement inchangé) ; `recouvrement_top_n` : part commune aux 2 top 20 de
gisements (1 = ensembles identiques).

| Bloc | Variante | ρ (valeurs de réserve) | Recouvrement top N |
| --- | --- | --- | --- |
| Centre | uniforme_entre_blocs | 0.922 | 20.0% (top 20) |
| Droite | uniforme_entre_blocs | 0.864 | 20.0% (top 20) |
| Extrême droite | uniforme_entre_blocs | 0.896 | 20.0% (top 20) |
| Gauche | uniforme_entre_blocs | 0.955 | 20.0% (top 20) |

## 5. Lift bureau vs département (réutilisation de la garde anti-hasard #24)

Seule la composante volume de la réserve (abstention présidentielle 2022,
persistance 2022→2024) est backtestable : ce tableau réutilise tel quel le
résultat de `projections.backtest.garde_anti_hasard_participation` (issue #24,
ADR 0002) — la granularité bureau doit battre (>, pas ≥) la granularité
département sur la persistance de l'abstention. La composante « part estimée
du bloc » n'a pas de lift (non backtestable, cf. section 4 ci-dessus).

| Cible | ρ bureau | ρ hasard (lift) | ρ département (lift) | Verdict |
| --- | --- | --- | --- | --- |
| euro | 0.769 | 0.0 (lift 0.769) | 0.284 (lift 0.485) | PASS |
| legi | 0.815 | 0.0 (lift 0.815) | 0.349 (lift 0.466) | PASS |

## Verdict de publication en carte (ADR 0002 point 5)

**⚠ PRÉPARATION SEULEMENT — non publiable en carte tant que la révision (issue #28) n'a pas tranché.** Le gate de publication de la carte mobilisation (ADR 0002 point 5, réutilisation de `projections.backtest.verdict_carte_mobilisation`) est **FAIL** : le backtest participation est sorti rouge (ρ europ. 0,769 < 0,8, voir `backtest-2022-2024.md` §4). Cette table et ce rapport sont publiés tels quels, en préparation de la carte — aucun chiffre n'est caché — mais aucune publication cartographique n'est autorisée avant que la révision d'architecture (#28) ne tranche. Les seuils ne bougent pas.

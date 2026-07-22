# Spot-check des conflits factuels entre drafts

## Conflit 1 : volume de validation d'ecolRxC (493 vs 565)
- Draft A dit : « erreur EI moyenne de 9,78 sur 493 élections réelles »
- Drafts B et C disent : « validé sur 565 jeux de données réels / 565 élections »
- Source check : l'interim implementation-bureau-ei-et-covariables (texte intégral de Pavía & Thomsen lu par l'investigateur) donne 565 élections réelles R×C (NZ 2002-2020 + Écosse 2007) ; le chiffre 493 correspond vraisemblablement au sous-ensemble d'une comparaison spécifique.
- **Verdict :** utiliser « 565 jeux de données réels » (B/C). Ne pas citer 493.

## Conflit 2 : attribution du biais directionnel EI et de la condition CAR
- Draft B attribue le biais directionnel partagé à [[the-future-of-ecological-inference-research-a-reply-to-freedman-et-al-gary-king]] et la condition CAR/covariables à [[improving-ecological-inference-by-predicting-individual]] (Imai & Khanna).
- Drafts A et C attribuent les deux à Kuriwaki & McCartan [[the-role-of-confounders-and-linearity-in]].
- Source check : le claims file et l'interim EI sont sans ambiguïté — la condition CAR, l'estimateur « seine » et la démonstration du biais directionnel (sous-estimation du panachage) viennent de Kuriwaki & McCartan (the-role-of-confounders-and-linearity-in). Imai & Khanna (BISG) est un travail distinct (prédiction individuelle par nom/géographie).
- **Verdict :** citer [[the-role-of-confounders-and-linearity-in]] pour CAR/biais directionnel/« seine ». N'utiliser [[improving-ecological-inference-by-predicting-individual]] que pour l'amélioration par prédiction individuelle (si mentionnée).

## Non-conflits vérifiés
- Effets Pons 2012 (+3,2/+2,8, ~½ avance T1, ~¼ marge T2) : identiques dans les 3 drafts.
- Amplitude RN 2027 (23 % → 33-37 %) : cohérente (C dit 34-37, tolérable — écrire « ~33-37 % »).
- Corrélation 0,89 (gauche, circo, CEVIPOF), 3 000/69 000 REU-MIOM, 97 %/73 % ENEF, fuite LR→RN 50-70 % (Elabe 2027), couverture IC EI 30-53 %, -60 % Marble & Clinton : identiques partout.

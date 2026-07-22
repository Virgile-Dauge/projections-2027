# Corpus-critic results — étape 8 (juillet 2026)

6 gaps (2 critical, 4 high), 3 fetchers, tous traités.

## Gap 1 (critical, overturning) — projection française au bureau hors MRP ?
**Recherche adversariale élargie (6 requêtes au-delà du MRP).** Contre-exemple le plus proche trouvé et fetché :
Souidi & Vonderscher, *Nouvelle cartographie électorale de la France* (Textuel, jan. 2026) — croise les ~70 000
bureaux avec les données sociales INSEE, mais « surtout descriptif », AUCUNE projection 2027 malgré le cadrage
éditorial. Vérifiés aussi : Observatoire des Votes, France2027.eu, quiserapresident.fr, 3 repos GitHub.
**Verdict : la primauté TIENT et se précise** — taxonomie à deux catégories : descriptif-à-maille-fine
(Souidi/Vonderscher, Cagé-Piketty) OU prédictif-à-maille-grossière (instituts, 577 circos), jamais les deux.
→ comparisons.md T5 : confiance ↑, et le rapport doit citer le livre Textuel comme précédent descriptif direct.

## Gap 2 (critical, overturning) — backtest de rang à maille fine ?
Aucune étude de corrélation de rang trouvée (le gap est réel). MAIS : Hanretty 2017 (JEPOP, PDF complet) =
validation empirique EUROPÉENNE d'un modèle small-area contre vérité-terrain (référendum UE, wards→circos,
erreur médiane 1,62pp vs 5,22pp pour l'interpolation dasymétrique naïve). Validation en ERREUR, pas en RANG
(0 occurrence de Spearman/Kendall). + Bracalente et al. (arXiv, Ombrie) : EI small-area sur bureaux italiens.
**Verdict : le pilier ordinal reste théorie + 1 cas US, mais gagne un 2e point de calibration empirique
européen (erreur).** → T1 : confiance inchangée (medium), formulation à calibrer ; le backtest interne
2022→2024 reste la recommandation n°1.

## Gap 3 (high, strengthening) — corrélation géographique RN chiffrée ?
N'existe pas dans la littérature (gap réel confirmé — le CEVIPOF n'a publié que la note « gauche »).
Renforcement qualitatif : FJJ « Retour sur un séisme électoral » (Fourquet/Colange/Manternach) — continuité
géographique RN au niveau bureau 2022→2024 documentée (cas Sarcelles, dichotomie Nord/Sud stable).
→ T pertinentes : le rapport peut affirmer la stabilité qualitative, doit signaler l'absence de coefficient
RN et proposer le calcul comme validation interne (données MI ouvertes).

## Gap 4 (high, overturning) — Bartels 2023 (SOE infranational) ?
Texte intégral inaccessible (Cloudflare), MAIS scope vérifié via blog auteur + repo réplication : le papier
porte sur le côté OFFRE (dépenses de campagne des petits partis allemands, Bundestag 2017 vs Europawahl 2019),
PAS sur la variation géographique infranationale du SOE. **Verdict : menace de renversement neutralisée —
le papier ne teste pas ce que le locus baseline craignait.** → T1 baseline : pas de changement.

## Gap 5 (high, independent-verification) — réplication de la matrice Elabe 2027 ?
Odoxa (avr. 2026, indépendant) corrobore les ordres de grandeur des duels (Philippe 52-48 vs Bardella) ;
2e vague Elabe (IV2, mars 2026) cohérente en interne ; Cluster17 : pas de matrice T2 publiée ; Fondapol
« Qui en 2027 ? » = simulateur à hypothèses manuelles (pas une mesure — mais data point « qui fait ça »).
**Verdict : corroboration directionnelle inter-instituts acquise, réplication complète de la matrice
détaillée toujours absente.** → T3 : confiance ↑ d'un cran sur les ordres de grandeur, caveat maintenu
sur les coefficients fins.

## Gap 6 (high, strengthening) — crosswalk IRIS→bureau ?
**RÉSOLU POSITIVEMENT** : table de liaison IRIS↔bureaux 2024 officielle sur data.gouv (pondération
population via Filosofi 200m, Licence Ouverte, MàJ avr. 2026, mismatches connus documentés : Bordeaux
centre, Paris 1-4) + pipeline OS fonctionnel (raphaeljolivet, geopackage) + critique méthodologique de
l'intersection surfacique (Gombin/Cartelec : biais d'équirépartition ; alternative géocodage BAN).
→ T4 : la voie CSP/diplôme via IRIS passe de « non documentée » à « documentée avec caveats de qualité ».

## Leads non résolus (documentés, non bloquants)
- CEVIPOF « Droite2027 » mars 2026 : login wall Sciences Po (retry possible via `hyperresearch setup`).
- Blumenau/Lauderdale IJF 2020 : Cloudflare, pas de miroir.
- Réplication complète matrice T2 2027 par un 3e institut : n'existe pas encore (surveiller Ifop/Harris).

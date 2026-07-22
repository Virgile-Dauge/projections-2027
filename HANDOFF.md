# HANDOFF — Implémenter les projections 2027 à la maille bureau de vote

Traduction opérationnelle du rapport de recherche
[`research/notes/final_report_projections-electorales-bureaux-2027-b0b1c4.md`](research/notes/final_report_projections-electorales-bureaux-2027-b0b1c4.md)
(état de l'art, 87 sources — version HTML publiée en artifact le 21/07/2026).

**L'architecture retenue** : un pipeline conditionnel à 5 étages, sortie **ordinale**
(classement des bureaux + réserve d'abstention par bloc), **jamais de pourcentage à
intervalle de confiance affiché**. La crédibilité repose sur des backtests auto-produits
et publiés avec les cartes. Les étapes ci-dessous sont ordonnées par dépendance : ne pas
paralléliser 2-3 avant que 0-1 soient vertes.

---

## Étape 0 — Panel de données + crosswalk (CONDITION SUSPENSIVE de tout le reste)

Le rapport est formel : la jointure bureau-à-bureau entre scrutins n'est **pas sûre par
défaut** (numérotation communale sans norme, dérives documentées type Montbéliard,
harmonisation manuelle côté data.gouv). Tout le pipeline dépend de cette étape.

- [ ] **Ingestion des 4 scrutins** depuis le jeu data.gouv « Données des élections agrégées »
      (présidentielle 2022 T1/T2, législatives 2022, européennes 2024, législatives 2024),
      `general-results.csv` + `candidats-results.csv` + **`table-bv-reu.csv`** (crosswalk
      officiel identifiants électoraux ↔ REU). ⚠️ rupture de schéma janvier 2026 documentée.
- [ ] **Parsing** : wide→long, décimales à virgule et suffixe `%` (pièges `docs/heritage-2024.md`),
      clé `id_bv` = code INSEE commune + `_` + code bureau. **Jamais moyenner des %** —
      toujours repasser par les voix.
- [ ] **Mesurer le churn** (LE nombre que personne n'a jamais publié) : comparer le **nombre
      de bureaux par commune** sur les 4 scrutins (`id_election` × `code_commune`, sans REU).
      Toute commune dont le compte change entre deux scrutins = instable.
- [ ] **Stratégie à deux étages** : communes stables → jointure directe par identifiant ;
      communes instables → repli maille communale (approche Cagé-Piketty) ou réallocation
      dasymétrique pondérée par **électeurs inscrits, jamais par surface** (`maup.prorate`).
- [ ] **Nuances → blocs** selon `docs/classification_en_blocs.md` (24 nuances → 5 blocs).

**Livrables** : panel bureau×scrutin×bloc joint + `rapport-churn.md` (taux national,
distribution par département, % d'inscrits en zone stable).
**Critère de sortie** : chaque bureau du panel est soit joint-validé, soit explicitement
en repli, avec le taux publié. *Estimation : ~1-2 jours pour le test de churn seul.*

## Étape 1 — Baseline composite (structure spatiale)

Aucun scrutin seul ne convient (législatives biaisées par l'offre, européennes biaisées
en niveau par l'effet second-ordre, présidentielle 2022 datée par la recomposition).
Construire le premier indice composite type Cook PVI / 538 partisan lean pour la France.

- [ ] Par scrutin : score de chaque bloc par bureau en **écart relatif au national**
      (structure spatiale), pas en niveau brut.
- [ ] Correction d'offre des législatives T1 (circonscriptions sans candidat d'un bloc :
      imputation à documenter — sensibilité type « uncontested districts »).
- [ ] Combinaison pondérée (point de départ : 50 % présidentielle 2022 / 25 % européennes
      2024 / 25 % législatives 2024 corrigées — pondérations à calibrer par le backtest,
      pas à figer). Variante moyenne tronquée à tester.
- [ ] **Terme de dérive 2022→2024** par bureau/bloc (la géographie RN diffuse : +16-18 pts
      hors bastions dans le Sud-Ouest 2017→2024) — extrapolable, pas figé.

**Livrable** : indice composite bureau×bloc + dérive. **Critère de sortie** : le backtest
de l'étape 2 départage composite vs mono-scrutin.

## Étape 2 — Backtests (AVANT toute carte publique)

Personne n'a jamais publié de barre d'erreur à cette maille : le projet doit auto-produire
sa validation. Trois calculs, tous faisables sur les données déjà ingérées :

- [ ] **Backtest de corrélation de rang 2022→2024** : prédire la géographie 2024
      (européennes, puis législatives T1 corrigées) depuis 2022, mesurer Spearman/Kendall
      par bloc — baseline mono-scrutin vs composite. C'est le test que ni Marble & Clinton
      ni Hanretty n'ont fait ; il tranche la thèse « le classement dégrade gracieusement ».
- [ ] **Corrélation géographique RN européennes↔présidentielle** (l'équivalent du 0,89
      CEVIPOF mesuré pour la gauche, absent de la littérature). Si elle est nettement
      plus faible (<0,5), rétrograder le poids des européennes dans le composite.
- [ ] **Distribution du swing RN par bureau** (condition de régularité du résultat
      classement-vs-estimation) : vérifier l'absence de masse au seuil de décision.

**Livrable** : `research/backtest-2022-2024.md` chiffré, destiné à être **publié avec les
cartes**. **Critère de sortie** : corrélation de rang du composite ≥ mono-scrutin, et
seuil de Spearman jugé acceptable documenté (à fixer AVANT de lancer le calcul).

## Étape 3 — Moteur de swing + scénarios nationaux

- [ ] **Swing piecewise par bloc** appliqué au résultat antérieur de chaque bureau
      (formule Wilson & Grofman : `f = s·(1-x)/(1-x̄)` si `s≥0`, sinon `s·x/x̄` —
      quelques lignes ; borné par construction, indispensable au régime RN 23 %→~35 %).
      Pas de swing uniforme : violations de bornes documentées à cette amplitude.
- [ ] **3 scénarios nationaux discrets** (RN bas / central / haut) depuis les sondages —
      jamais de point estimate recalé en continu (une partie du mouvement inter-vagues
      est un artefact de non-réponse différentielle).
- [ ] **Test d'invariance** : recalculer le classement sous les 3 scénarios, mesurer sa
      stabilité. Si le rang est quasi invariant (prédiction du rapport), c'est la preuve
      que la carte livre de la « pertinence locale » découplée de la prédiction nationale.

**Critère de sortie** : classements produits sous 3 scénarios + mesure d'invariance.

## Étape 4 — Second tour (matrices scénarisées)

- [ ] Matrices de transfert **conditionnelles à l'affiche** : structure ordinale stable
      depuis 2015 (gauche-hors-LFI > centre > LR ; pénalité d'étiquette LFI mesurée
      expérimentalement 40 %→32 %), **niveaux** pris dans la source la plus proche du
      scrutin cible (matrice Elabe présidentielle 2027 : fuite LR→RN 50-70 % selon duel ;
      corroboration Odoxa) — jamais les coefficients bruts de 2024.
- [ ] Paramétrer l'érosion du front républicain comme scénario (2024 réel vs 2025 déclaré),
      pas comme constante.
- [ ] *(v2, optionnel)* Estimer les transferts 2022→2024 par inférence écologique
      structure-latente + covariables (ecolRxC / eiPack) en ordres de grandeur agrégés —
      jamais bureau par bureau. À ne faire que si le backtest v1 est vert.

## Étape 5 — Sorties produit (données ; la stack carto est déjà tranchée dans CLAUDE.md)

- [ ] **Deux variables par bureau** : (1) rapport de force projeté en **quantiles/classement**
      (persuasion : bureaux disputés) ; (2) **réserve d'abstention par bloc** (mobilisation :
      soutiens démobilisés). Base expérimentale : effets Pons hétérogènes (+3,4 pts
      immigrés / 0 ailleurs) — la carte laisse l'arbitrage tactique au terrain.
- [ ] Aucun % à IC affiché au bureau ; scénario national affiché comme contexte.
- [ ] **Publier le backtest avec les cartes** (transparence = argument scientifique ET
      militant). Cadrage : « assemblage de briques validées », pas « première française ».

## v2 (conditionnée au backtest) — Covariables

- [ ] Carreaux Filosofi 200 m → bureau : revenu, âge, ménage/logement (natif ; ⚠️ 79 % des
      carreaux imputés en zone peu dense).
- [ ] CSP/diplôme : recensement IRIS → bureau via la **table de liaison IRIS↔bureaux 2024**
      (data.gouv, pondérée population — pas d'intersection surfacique naïve). Template
      OS existant : `raphaeljolivet/eu2024-stats-iris`.
- [ ] Usage : covariables en **correcteur** d'un modèle ancré (swing hétérogène, biais EI),
      jamais en moteur prédictif autonome (échec documenté, la maille fine aggrave).

---

## Garde-fous permanents

1. **Jamais moyenner des pourcentages** — voix, somme, recalcul (`docs/heritage-2024.md`).
2. **Jointure par identifiants + crosswalk, jamais par géométrie** — les contours n'ont
   aucune existence officielle et ne servent qu'à l'affichage.
3. **Sortie ordinale uniquement** — aucun IC n'est calibré à cette maille (couvertures
   réelles 28-53 % toutes familles confondues).
4. **Hypothèse de continuité assumée** : une rupture d'offre 2027 (primaire RN disputée,
   éclatement du bloc central) périme toute baseline 2022-2024 — à afficher comme limite.
5. Le REU date de septembre 2022 ; son rafraîchissement avant 2027 est incertain — les
   recouvrements socio-démographiques (v2) vieillissent, pas les résultats officiels.

## Références rapides

- Rapport complet : `research/notes/final_report_projections-electorales-bureaux-2027-b0b1c4.md`
- Notes d'investigation (détail par sujet) : `research/notes/interim-report-*.md`
- Datasets : « Données des élections agrégées » + `table-bv-reu.csv` + « Liaison IRIS↔bureaux
  de vote 2024 » + « Bureaux de vote et adresses de leurs électeurs » (INSEE/REU) — URLs dans
  les notes `jeu-de-donnes-*` du vault.
- Outils : `maup` (crosswalk/proration), `ecolRxC`/`PyEI`/`eiCompare` (EI), `calibratedMRP`
  (swing calibré), `mapvotr` (contours d'affichage).

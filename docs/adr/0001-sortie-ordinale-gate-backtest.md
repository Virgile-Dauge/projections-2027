# Sortie ordinale uniquement, publication conditionnée à un backtest réfutable

À la maille bureau de vote, aucune famille de méthodes ne produit d'intervalles de confiance calibrés (couvertures réelles 28-53 % ; voir le rapport `research/notes/final_report_projections-electorales-bureaux-2027-b0b1c4.md`, §1.B). Nous décidons donc de ne jamais afficher de pourcentage à intervalle de confiance par bureau : le livrable est un **classement/quantile** (rapport de force projeté + réserve d'abstention par bloc), le scénario national n'étant montré que comme contexte.

Comme personne n'a jamais publié de projection à cette maille en France, aucune validation externe n'existe : le projet auto-produit la sienne. Le **gate de publication**, fixé avant tout calcul (session de cadrage du 2026-07-22) pour rester réfutable :

- Corrélation de rang Spearman **ρ ≥ 0,7** par bloc majeur (a minima Extrême droite et Gauche) sur le backtest 2022→2024, ensemble des bureaux joints ;
- **ρ ≥ 0,5** sur le tercile compétitif de la baseline (les bureaux disputés, là où la carte prétend servir) ;
- le composite doit faire au moins aussi bien que la meilleure baseline mono-scrutin.

Sous ces seuils : révision de l'architecture, pas de publication. Le backtest chiffré est publié avec les cartes. Changer les seuils après avoir vu les résultats équivaudrait à annuler la validation — c'est le caractère irréversible de cette décision.

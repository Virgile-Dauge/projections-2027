# 0005 — Échelle départementale pour la couche réserve

- Status: accepted
- Date: 2026-07-23

## Contexte

La couche réserve (#25, ADR 0002 point 1) code l'intensité visuelle par un quantile ordinal (ADR 0001, sortie
ordinale). Ce quantile était jusqu'ici calculé sur **toute la France** (`quantiles_larges(..., groupe="bloc")`) :
les bastions de gauche saturent l'échelle (tranche 5 partout), et les départements où la gauche est
structurellement faible en ressortent **uniformément pâles** — aucun contraste local, alors que du gisement
mobilisable existe bel et bien à l'intérieur de ces départements. Une carte qui décourage au lieu d'orienter va à
l'encontre de l'objectif produit (issue #37) : permettre de décider **localement** où aller, sans décourager les
militant·e·s des zones où le rapport de force national est mauvais.

CONTEXT.md porte déjà l'entrée glossaire « Tranche départementale » (session de grillade, commit préalable à cet
ADR) : le quantile est recalculé **parmi les unités du même département**, séparément aux deux mailles (bureaux
entre eux, communes entre elles), chaque département affichant ainsi par construction la gamme complète des
tranches.

## Décision

1. **Colonne additionnelle, jamais un remplacement.** `quantiles_larges` (`projections.mobilisation`) accepte
   désormais un `groupe` composite (`["bloc", "code_departement"]`) et un `suffixe` de nom de colonne. La réserve
   embarque `quantile_reserve_<slug>_dep` **à côté de** `quantile_reserve_<slug>` (national, inchangé) : les deux
   colonnes existent dans les tuiles, seule la première est encore affichée par le site. Réversibilité côté client
   seule — recalculer les tuiles n'est pas nécessaire pour revenir en arrière si besoin.
2. **Calcul séparé par maille, sur sa propre population.** `preparer_carte_reserve` (bureaux) et
   `agreger_reserve_commune` (communes, dézoom + repli) appellent chacune leur propre passage départemental,
   exactement comme elles le font déjà pour le quantile national — jamais de mélange bureau/commune dans un même
   classement (des ordres de grandeur trop différents). Les communes en repli participent au quantile communal de
   **leur** département (elles ont une réserve valide à cette maille, cf. `docs/heritage-2024.md`) ; leur marqueur
   de repli (`mob-repli-ligne`) n'est pas affecté par ce calcul.
3. **Site : remplacement sec, pas de sélecteur d'échelle.** `site/main.js` bascule l'opacité de la couche réserve
   sur `quantile_reserve_gauche_dep` (au lieu de `quantile_reserve_gauche`). Aucune bascule national/départemental
   n'est exposée à l'utilisateur : la lecture actionnable est départementale, point ; le national reste dans les
   tuiles pour audit ou reprise future, pas pour choix utilisateur.
4. **Garde-fous, référentiel jamais silencieux (même discipline que « Repli »).** Légende, bandeau et panneau au
   clic annoncent explicitement « tranche X/5 **dans le département** ». Le panneau conserve le **nombre absolu**
   d'inscrits mobilisables à côté de la tranche : un 5/5 dans un département globalement faible peut représenter
   moins de voix en valeur absolue qu'un 3/5 dans un département dense — la tranche dit où regarder localement,
   jamais combien de voix sont en jeu.
5. **Périmètre : réserve seule.** Le rapport de force projeté reste en quantile **national** par bloc, inchangé —
   couche de contexte volontairement grossière (ADR 0002 point 2), où comparer les départements entre eux a du sens
   (« qui est en tête, à gros traits, ici plutôt que là »). L'asymétrie entre les deux couches est assumée et
   expliquée dans la page méthode, pas cachée.
6. **Petits départements : bornage, jamais une erreur.** `quantiles_larges` borne déjà tout bucket non nul dans
   `[1, n]` par construction (`clip`) ; un groupe plus petit que `n` (ex. `975`, Saint-Pierre-et-Miquelon, 4
   bureaux, `n=5`) laisse simplement sa tranche la plus basse vide — comportement arithmétique attendu, documenté
   dans la page méthode, pas un garde-fou supplémentaire à coder. `code_departement` est complet sur les données
   réelles (aucune valeur nulle) et couvre des groupes non numériques valides (`2A`/`2B`, `ZX`, `ZZ`).

## Conséquences

- `projections.mobilisation.quantiles_larges` et `_reserve_large` gagnent une capacité générique (groupe composite,
  suffixe de colonne) réutilisable par un futur découpage différent, sans nouvelle fonction.
- `projections.build_tiles._proprietes_reserve` embarque une propriété de plus par bloc publié dans les tuiles
  (`quantile_reserve_gauche_dep`, seul bloc diffusé sur la carte, décision PR #33 inchangée).
- `site/main.js`/`site/index.html` : dry-switch de l'expression d'opacité + wording légende/bandeau/panneau ;
  aucun nouveau contrôle utilisateur.
- Tuiles à reconstruire et republier pour que la propriété `_dep` existe réellement en production (le gate
  mécanique du backtest, ADR 0001/0002/0003, reste en tête de `build_tiles.main` et n'est pas modifié par cet ADR).
- CONTEXT.md porte déjà l'entrée « Tranche départementale » (glossaire canonique) ; cet ADR documente l'arbitrage
  qui la justifie.

## Alternatives considérées

- **Échelle régionale (maille intermédiaire département/national)** — rejetée : n'existe pas déjà comme colonne de
  contexte dans le panel (chantier data à part), et ne résout qu'à moitié l'aplatissement pour les grandes régions
  elles-mêmes hétérogènes.
- **Sélecteur national/départemental côté site** — rejeté : ajoute un contrôle et une explication supplémentaires
  pour un produit qui préfère une lecture actionnable unique ; le national reste disponible dans les tuiles pour
  qui veut l'auditer, sans façade utilisateur dédiée.
- **Ne pas conserver le quantile national dans les tuiles** — rejeté : supprimerait la réversibilité côté client et
  romprait un contrat déjà publié (propriété consommée par d'éventuels usages tiers des tuiles) pour un gain de
  poids négligeable face au fichier PMTiles complet.

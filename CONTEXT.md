# CONTEXT — Glossaire du domaine

Vocabulaire canonique du projet. Les issues, docs et noms de code utilisent ces termes-là, pas leurs synonymes.

## Unités et identifiants

- **Bureau (de vote)** — l'unité atomique du projet (~70 000 en France). Juridiquement un rattachement d'adresses par arrêté préfectoral, **pas** une zone géométrique : les contours n'ont aucune existence officielle et ne servent qu'à l'affichage.
- **id_bv** — clé de jointure d'un bureau : code commune (5 caractères — code INSEE en chiffres, ou `ZZ`+numéro pour les bureaux de l'étranger) + `_` + code bureau.
- **Crosswalk** — table de correspondance des identifiants de bureaux entre deux référentiels ou deux scrutins. La jointure inter-scrutins se fait par identifiants + crosswalk, jamais par géométrie.
- **Churn** — instabilité du découpage en bureaux entre deux scrutins. Détecté par commune (le nombre de bureaux change d'un scrutin à l'autre) ; mesuré canoniquement en **part des inscrits** en zone instable — la grandeur à minimiser est l'électorat mal identifié localement, jamais un compte de communes ou de bureaux (des unités de tailles trop inégales pour être comparées).
- **Commune stable / instable** — stable : même nombre de bureaux sur les 4 scrutins sources → jointure directe par id_bv. Instable : le compte change → repli.
- **Repli** — traitement d'une commune instable : agrégation à la maille communale, ou réallocation dasymétrique pondérée par les électeurs inscrits (jamais par la surface).
- **Panel** — la table bureau × scrutin × bloc issue de l'étape 0, chaque bureau étant soit joint-validé soit explicitement en repli.

## Scrutins et blocs

- **Scrutins sources** — les 4 scrutins passés utilisés : présidentielle 2022 (T1/T2), législatives 2022, législatives 2024, européennes 2024.
- **Scrutin cible** — la présidentielle 2027.
- **Nuance** — l'une des 24 étiquettes officielles attribuées par les préfets à chaque candidat.
- **Bloc** — regroupement des nuances en 5 familles : Gauche / Centre / Droite / Extrême droite / Divers (voir `docs/classification_en_blocs.md`).
- **Correction d'offre** — imputation, pour les législatives T1, d'un score aux blocs sans candidat dans une circonscription. Sans elle, les législatives ne mesurent pas un rapport de force.

## Modèle

- **Baseline (composite)** — indice partisan par bureau × bloc : structure spatiale relative (écart au national) combinée sur plusieurs scrutins sources, pondérée vers le récent. L'équivalent français du Cook PVI — n'existe pas encore ailleurs.
- **Dérive** — terme d'évolution 2022→2024 de la structure spatiale d'un bloc par bureau, extrapolable (capte la diffusion RN hors bastions).
- **Swing** — report d'un écart national sur chaque bureau. Toujours **piecewise** (par morceaux, formule Wilson-Grofman, borné dans [0,1]) et **par bloc** — jamais uniforme.
- **Élasticité** — réactivité d'un bureau au swing national (de combien il bouge par point de swing), distincte de son penchant (baseline).
- **Scénario** — hypothèse nationale discrète (RN bas / central / haut) tirée des sondages. Le niveau national entre toujours en scénarios, jamais en point recalé en continu.
- **Matrice de transfert** — répartition des voix d'un bloc du T1 vers les candidats du T2, conditionnelle à l'affiche du duel. Structure ordinale stable empruntée à 2024, niveaux pris dans la source la plus proche du scrutin cible.
- **Backtest** — validation auto-produite : prédire la géographie 2024 depuis 2022 et mesurer la corrélation de rang (Spearman/Kendall) par bloc. Publié avec les cartes.

## Produit

- **Sortie ordinale** — le livrable par bureau est un classement/quantile, jamais un pourcentage à intervalle de confiance affiché.
- **Rapport de force (projeté)** — variable produit n°1 : position du bureau dans le classement du duel de blocs — cible les bureaux disputés (persuasion).
- **Réserve d'abstention** — variable produit n°2 : abstention par bureau croisée avec la structure de blocs — cible les soutiens démobilisés (mobilisation). Calculable sans swing.
- **Carte structurelle** — première carte publique (jalon v1) : baseline + réserve d'abstention, sans scénario national. Publiée dès que crosswalk, baseline et backtest sont verts.
- **Carte scénarisée** — carte v1.1 : classement recalculé sous les 3 scénarios nationaux (swing + second tour).
- **Tracer bullet** — PMTiles descriptif (résultats 2024 bruts par bloc) + site MapLibre minimal, construit dès que le panel existe pour valider la chaîne données→tuiles→site de bout en bout.

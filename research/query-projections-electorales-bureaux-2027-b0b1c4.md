---
vault_tag: projections-electorales-bureaux-2027-b0b1c4
created: 2026-07-21T18:19:00+00:00
source: user-prompt
---

# Cadrage de la recherche — prompt hyperresearch

Prompt destiné à une session hyperresearch sur l'état de l'art des projections électorales. Rédigé le 21/07/2026, à affiner avant lancement.

---

**Question de recherche.** État de l'art des méthodes de projection de résultats électoraux passés sur un scrutin futur, appliqué au cas suivant : projeter, **au niveau du bureau de vote** (~70 000 bureaux en France), un rapport de force pour la présidentielle française de 2027, à partir des résultats officiels du ministère de l'Intérieur (présidentielle 2022, législatives 2022 et 2024, européennes 2024) et des dynamiques nationales mesurées par sondages. Finalité : des cartes open source destinées aux militant·es de terrain pour prioriser leurs actions face au Rassemblement national — l'exigence est donc la **pertinence locale** (où l'action a de l'impact), pas la prédiction du résultat national.

**Axe 1 — Gradation des méthodes.** Cartographier les familles de méthodes du plus simple au plus sophistiqué (swing uniforme, swing proportionnel, matrices de transfert / inférence écologique, MRP, modèles bayésiens type forecasting électoral, autres), et pour chacune : précision attendue à maille fine, complexité de mise en œuvre, données requises, limites documentées, usages réels (médias, académiques, campagnes). Qui fait ça en France (instituts de sondage, chercheurs, médias) et comment ?

**Axe 2 — Choix des données sources (partie intégrante du problème).** Pour chaque méthode, quelles élections passées sont pertinentes et pourquoi. Traiter explicitement : le biais des législatives (offre incomplète — tous les blocs ne se présentent pas partout, candidatures uniques, front républicain, désistements) et comment le corriger ou le contourner ; la valeur des européennes comme mesure « sincère » à la proportionnelle ; l'obsolescence de la présidentielle 2022 face aux recompositions ; la combinaison de plusieurs scrutins. Couvrir aussi le problème pratique du **changement des découpages de bureaux de vote entre élections** (méthodes de réconciliation / crosswalk documentées, jeux de données existants type INSEE / data.gouv).

**Ouverture (secondaire, ne pas creuser).** Outils open source existants implémentant ces méthodes (packages R/Python d'inférence écologique, de MRP, etc.).

**Hors scope.** La stack de visualisation et de diffusion des cartes (tuiles, bibliothèques carto, hébergement).

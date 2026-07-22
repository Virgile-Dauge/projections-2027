# Coverage Matrix — query phrase → atomic item mapping

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| « état de l'art des méthodes de projection de résultats électoraux passés sur un scrutin futur » | Sub-Q1 (familles de méthodes) | OK — couvre toute la littérature, pas seulement la France | No |
| « au niveau du bureau de vote (~70 000 bureaux en France) » | Entité maille géographique ; scope_condition maille | OK | No |
| « rapport de force pour la présidentielle française de 2027 » | Entité scrutin cible ; time_horizon | OK | No |
| « résultats officiels du ministère de l'Intérieur » | Entité source de données ; time_periods | OK | No |
| « présidentielle 2022, législatives 2022 et 2024, européennes 2024 » | 4 entités élections sources + time_periods | OK — chacune listée séparément | No |
| « dynamiques nationales mesurées par sondages » | Entité sondages nationaux ; Sub-Q8 (combinaison) | OK — l'intégration sondages→local est un required_field | No |
| « cartes open source destinées aux militant·es de terrain » | scope_condition finalité | OK | No |
| « prioriser leurs actions face au Rassemblement national » | Entité RN ; scope_condition finalité | OK | No |
| « pertinence locale (où l'action a de l'impact), pas la prédiction du résultat national » | scope_condition critère de qualité ; Sub-Q10 (recommandation) | OK — critère d'évaluation distinct explicite | No |
| « swing uniforme » | Entité méthode | OK | No |
| « swing proportionnel » | Entité méthode | OK | No |
| « matrices de transfert / inférence écologique » | Entité méthode | OK — les deux lectures (matrices de transfert électorales ET inférence écologique académique type King) couvertes par la même entité, à traiter comme famille double | No |
| « MRP » | Entité méthode | OK | No |
| « modèles bayésiens type forecasting électoral » | Entité méthode | OK | No |
| « autres » | Entité « autres méthodes » | OK — catégorie ouverte préservée | No |
| « précision attendue à maille fine, complexité de mise en œuvre, données requises, limites documentées, usages réels (médias, académiques, campagnes) » | required_fields des 6 entités méthode ; Sub-Q2 | OK — 5 champs nommés | No |
| « Qui fait ça en France (instituts de sondage, chercheurs, médias) et comment ? » | Sub-Q3 ; entité praticiens | OK | No |
| « quelles élections passées sont pertinentes et pourquoi » | Sub-Q4 | OK — par méthode | No |
| « biais des législatives (offre incomplète […] candidatures uniques, front républicain, désistements) » | Sub-Q5 | OK — tous les mécanismes cités repris dans required_fields | No |
| « valeur des européennes comme mesure “sincère” à la proportionnelle » | Sub-Q6 | OK | No |
| « obsolescence de la présidentielle 2022 face aux recompositions » | Sub-Q7 | OK | No |
| « la combinaison de plusieurs scrutins » | Sub-Q8 | OK | No |
| « changement des découpages de bureaux de vote entre élections » | Sub-Q9 ; required_fields maille | OK | No |
| « méthodes de réconciliation / crosswalk documentées » | Sub-Q9 | OK | No |
| « jeux de données existants type INSEE / data.gouv » | Sub-Q9 ; time_periods reference-datasets | OK — REU/répertoire + contours | No |
| « Outils open source existants […] (packages R/Python d'inférence écologique, de MRP) » | Sub-Q11 ; entité outils ; scope_condition « ne pas creuser » | OK — secondaire, profondeur bornée | No |
| « Hors scope. La stack de visualisation et de diffusion » | scope_condition HORS SCOPE | OK — exclusion explicite | No |

Zéro ligne Gap = YES. Décomposition validée.

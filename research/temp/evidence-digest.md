# Evidence digest — projections-electorales-bureaux-2027-b0b1c4

Index de preuves filtré (confidence=high OU evidence empirique/statistique), 115 claims retenus sur l'ensemble du corpus. Chaque claim : texte, citation verbatim, note source.

## Claims consensuels [consensus — 3+ sources indépendantes]

- **[consensus]** À maille fine (circonscription et en-dessous), AUCUNE famille de méthodes ne produit d'intervalles de confiance calibrés : MRP sous-couvre (Lauderdale et al. ; Buttice & Highton : 28% de couverture au mieux pour des IC à 90%), les IC des méthodes EI RxC couvrent la vérité 30-53% du temps (validation NZ/Écosse), et tous les modèles de swing échouent sur la direction du changement local (sign accuracy ~0,5, Wilson & Grofman).
  - Implication : Le livrable doit vendre des CLASSEMENTS et des ORDRES DE GRANDEUR, jamais des points de pourcentage à IC affichés au bureau.
  - Sources : [model-based-pre-election-polling-for-national-and], [uc-davis-previously-published-works], [an-evaluation-of-the-performance-and-suitability-of-rc-methods-for-ecological-in], [models-of-inter-election-change-in]
- **[consensus]** Les législatives françaises sont structurellement biaisées comme mesure du rapport de force national : offre incomplète (7,5 candidats/circo en 2024 vs 11,5 en 2022), candidatures uniques, désistements massifs (210+ en 2024), et le codage des circonscriptions sans candidat d'un bloc change matériellement toute mesure d'évolution (leçon générale : Wilson & Grofman sur les uncontested districts).
  - Implication : Le T1 des législatives est utilisable seulement avec correction d'offre ; le T2 ne mesure pas un rapport de force mais un comportement de barrage conditionnel.
  - Sources : [rsultats-du-premier-tour-des-lgislatives-de-2024], [sondages-lgislatives-2024-pourquoi-il-faut-se-mfier-des-proj], [les-franais-et-les-lections-lgislatives], [models-of-inter-election-change-in]
- **[consensus]** Le front républicain 2024 a fonctionné mais asymétriquement : les reports vers un candidat Ensemble/LR (~97% des électeurs NFP) ont été bien meilleurs que vers un candidat NFP (~73%, et nettement moins si LFI — pénalité d'étiquette mesurée expérimentalement).
  - Implication : Toute matrice de transfert 2027 doit être conditionnelle à l'identité du candidat, pas seulement au bloc.
  - Sources : [elections-lgislatives-2024], [rsultats-du-premier-tour-des-lgislatives-de-2024], [lgislatives-2024-comment-les-reports-de-voix-du-front-rpubli]
- **[consensus]** Les résultats officiels par bureau de vote existent en open data (numérisation ministère de l'Intérieur depuis ~2002), avec un crosswalk officiel identifiants électoraux ↔ REU (table-bv-reu.csv, pipeline actif), mais les CONTOURS géographiques des bureaux n'ont aucune existence officielle : les arrêtés définissent des listes d'adresses, et les 3 reconstructions publiques (Etalab, INSEE mapvotr, Makina) sont explicitement approximatives et non-autoritaires.
  - Implication : La jointure inter-scrutins se fait par IDENTIFIANTS + crosswalk REU, pas par géométrie ; les contours ne servent qu'à l'affichage.
  - Sources : [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr], [jeu-de-donnes-proposition-de-contours-des-bureaux-de-vote-datagouvfr], [github-inseefrlabmapvotr-package-de-production-de-contours-de-bureaux-de-vote-pa], [une-approche-de-reconstruction-automatique-de-la-gomtrie-des-bureaux-de-vote-mak], [thomas-piketty]
- **[consensus]** Le découpage des bureaux change réellement entre scrutins (numérotation communale sans norme, redécoupages locaux) — toute comparaison inter-élections à cette maille exige une table de réconciliation, et les analogues internationaux quantifient le coût de l'ignorer (US : ~1/6 des comtés touchés par cycle ; mismatch de contours → jusqu'à 11-12% des voix mal allouées).
  - Implication : Le crosswalk est un composant de premier ordre du projet, pas un détail d'implémentation.
  - Sources : [jeu-de-donnes-bureaux-de-vote-et-adresses-de-leurs-lecteurs-datagouvfr], [thomas-piketty], [united-states-precinct-boundaries-and-statewide-partisan-election-results-scient], [github-mgggmaup-the-geospatial-toolkit-for-redistricting-dat], [changing-precinct-boundaries-who-is-affected-and-electoral]
- **[consensus]** Aucun institut, média ou laboratoire n'a publié de MRP pour une élection française ; la pratique française = matrices de transfert déclaratives (sondages jour du vote / intentions) + ajustements locaux ad hoc pour les projections en sièges, et estimations 20h par panel de bureaux dépouillés comparés aux scrutins antérieurs.
  - Implication : Le projet ne peut copier aucune implémentation française existante à maille bureau — le plus proche parent méthodologique est l'écosystème anglo-saxon (PVI/baseline, MRP UK, VEST US).
  - Sources : [absence-de-mrp-publi-pour-une-lection-franaise-constat-document-juillet-2026], [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives], [les-franais-et-les-lections-lgislatives], [prsidentielle-la-mthode-des-sondeurs-pour-estimer-les-rsultats-dimanche-20-heure]
- **[consensus]** Entre swing uniforme et proportionnel, aucune supériorité empirique consistante n'existe ; les praticiens sérieux blendent les deux et ajoutent des couches d'ajustement ; les différences deviennent importantes uniquement aux grandes amplitudes de swing (violations de bornes).
  - Implication : Le choix uniforme/proportionnel n'est pas le vrai enjeu ; le comportement aux bornes (RN en forte hausse projetée) l'est.
  - Sources : [uniform-swing-versus-proportional-swing-which-is-best], [vote-and-seat-projection-methodology-by-ric-grenier], [models-of-inter-election-change-in], [swingometrics-methodology-swingometer]
- **[consensus]** Le porte-à-porte a des effets électoraux réels, persistants et HÉTÉROGÈNES (persuasion ~1/4 de la marge Hollande 2012, randomisé par bureau de vote ; mobilisation +3,4pp chez les immigrés vs 0 ailleurs) — c'est l'hétérogénéité qui justifie le ciblage, donc les cartes.
  - Implication : La carte a une base causale : l'effet marginal d'une heure de militantisme varie selon le bureau — c'est exactement ce que le livrable doit estimer.
  - Sources : [will-a-five-minute-discussion], [increasing-the-electoral-participation-of-immigrants-experimental-evidence-from], [door-to-door-canvassing-campaigns-sway-voter-decisions], [2-rinvention-et-rationalisation-du-porte-porte-aux-lections-municipales-de-2014]
- **[consensus]** La recomposition 2017-2024 est réelle et documentée : tripartition installée (≈32/32/32 en 2022), bloc central effondré sous 15% aux européennes 2024, électorat RN homogène et stable, gauche hétérogène (LFI/PS/EELV), droite LR en voie d'absorption partielle par le RN — la présidentielle 2022 seule est une baseline datée.
  - Implication : Une baseline multi-scrutins pondérée vers 2024 est mieux fondée qu'une baseline présidentielle 2022 pure.
  - Sources : [the-beginning-of-the-end-of-tripartition-european-elections-and-social-inequalit], [note-obe-n2025-14-dissolution-un-an-aprs-cepremap-algan-finchelstein-de-laubier], [rsultats-du-premier-tour-des-lgislatives-de-2024], [thomas-piketty]
- **[consensus]** Les projections en sièges publiées par les instituts français en 2024 ont collectivement échoué (les 24 donnaient le RN en tête) parce qu'elles ne pouvaient pas anticiper les désistements ni les reports du front républicain — un échec de DONNÉES D'OFFRE, pas de méthode statistique.
  - Implication : La qualité d'une projection française dépend d'abord de la modélisation de l'OFFRE (qui est au second tour, qui se désiste) — heureusement, une présidentielle simplifie radicalement ce problème (offre nationale unique).
  - Sources : [lgislatives-2024-pourquoi-les-instituts-de-sondages-ont-chou-prdire-les-rsultats], [rsultats-des-lgislatives-2024-on-vous-explique-pourquoi-il-faut-prendre-les-proj], [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]

### Swing uniforme / proportionnel / piecewise

- The BES 2015 nowcast estimates constituency-level vote share by modeling individual vote-switching to/from each party since the previous election, conditioned on constituency characteristics, rather than applying a single national swing figure uniformly. (empirical)
  > We estimate a vote switching model to and from each party that takes variation by constituency characteristics into account (e.g. who won the seat previously, the vote share of the origin and destination parties; the level of immigration etc.).
  - Chiffres : 632 constituencies, BES Internet Panel wave 4
  [british-election-study-2015-general-election-constituency-forecast-the-british-e]
- Different plausible methodological assumptions (which survey question to use for vote intention, how to allocate undecided respondents) produce materially different constituency-level seat forecasts, prompting the BES team to average across four assumption combinations. (empirical)
  > Because they produce quite different results we show seat estimates based on four combinations of assumptions... We take the average, because we do not have strong reasons to choose between the different assumptions and an average of multiple forecasts generally performs better than a single forecast.
  - Chiffres : 4 assumption combinations
  [british-election-study-2015-general-election-constituency-forecast-the-british-e]
- Les auteurs identifient quatre 'swing circos' (circonscriptions où le vote a basculé de façon marquée d'un scrutin à l'autre entre 2017 et 2024) comme catégorie d'analyse rétrospective de la volatilité électorale, pas comme sortie d'un modèle prédictif tourné vers 2027. (empirical)
  > L'ouvrage introduit la notion de « swing circos » — circonscriptions fluctuantes où le vote peut basculer d'une élection à l'autre — et en identifie quatre particulièrement déterminantes.
  - Chiffres : 4 swing circos
  [cartographie-bureaux-de-vote-rn-et-conditions-de-vie]
- MRP's principal value-add over uniform swing applied to national poll averages is at the seat level, not the national vote-share level: MRP gave the Conservatives 359 seats vs 346 from a Scotland-adjusted uniform swing applied to the same underlying national vote shares, a 13-seat gap. (empirical)
  > The largest difference is that the MRP model's estimate of Conservative seats (359) is 13 higher than the estimate (346) stemming from the Scotland-adjusted swing.
  - Chiffres : 359 seats MRP, 346 seats Scotland-adjusted uniform swing, 13-seat gap
  [different-methods-similar-outcome-comparing-the-poll-of-polls-with-mrp-lse-briti]
- Plain uniform swing applied to an electoral pendulum ignores that one side's marginal seats can be systematically closer than the other's, producing a biased seat-count estimate even at zero net national swing: in the 2022 Australian pendulum, Labor's ten closest seats averaged a 1.34% margin versus the Coalition's 2.72%, so Labor was expected to lose about 5 seats to random variation at zero swing versus only 2 for the Coalition. (empirical)
  > Labor's average margin in its ten closest seats is 1.34% while the Coalition's is 2.72% - a remarkable difference... if there is zero swing, then just based on this difference between how close each side's marginals are, Labor would be expected to drop around five of its seats to the Coalition, while the Coalition would only drop around two back the other way.
  - Chiffres : Labor closest-10 average margin 1.34%, Coalition closest-10 average margin 2.72%, Labor expected losses at zero swing ~5 seats, Coalition expected losses at zero swing ~2 seats
  [dr-kevin-bonham-the-2022-pendulum-only-slightly-favours-the-coalition]
- A conditional-probability pendulum model converts each seat's uniform-swing-implied margin into a win probability using an empirically measured standard deviation of two-party-preferred swing (3.3%, measured across the last six Australian federal elections), rather than deterministically calling every seat above/below the swing threshold. (statistical)
  > I get the standard deviation in 2PP swings across the last six federal elections at around 3.3%.
  - Chiffres : 3.3% standard deviation of seat-level 2PP swing
  [dr-kevin-bonham-the-2022-pendulum-only-slightly-favours-the-coalition]
- Under a plain uniform-swing pendulum, the Coalition needed 51.2% two-party-preferred for a majority and only 48.5% to win more seats than Labor (an asymmetric threshold caused by seat distribution, not vote share alone), illustrating that uniform swing thresholds for 'winning' differ meaningfully by party even holding methodology fixed. (empirical)
  > If we apply uniform swing, then the Coalition needs 51.2% for a majority, 48.5% to win more seats than Labor and 48.3% to prevent Labor winning a majority, so Labor wins a majority with 51.8%.
  - Chiffres : Coalition majority threshold 51.2% 2PP, Coalition plurality threshold 48.5% 2PP, Labor majority threshold 51.8% 2PP
  [dr-kevin-bonham-the-2022-pendulum-only-slightly-favours-the-coalition]
- In the 2024 UK general election campaign, competing MRP models built on similar underlying poll data produced sharply divergent seat projections: YouGov/Sky News projected Labour 422 seats vs Conservatives 140, while More in Common projected Labour 382 seats vs Conservatives 180 — a 40-seat swing between two contemporaneous MRP models. (empirical)
  > The YouGov MRP predicted that Labour would win 422 seats, up 220 from 2019, while the Conservatives would lose 225, leaving them with just 140... A separate MRP from More in Common released on Monday predicted a smaller win for Labour, of 382 seats, and 180 seats for the Conservatives.
  - Chiffres : 422 seats Labour (YouGov), 140 seats Conservative (YouGov), 382 seats Labour (More in Common), 180 seats Conservative (More in Common)
  [how-mrp-modelling-works-and-what-it-means-for-the-general-election-the-week]
- A reusable probabilistic swing model applied to Australian federal electoral pendulums uses a per-seat standard deviation of 3.3% (average deviation from uniform swing measured across the last six federal elections) combined with a +/-1 percentage point incumbency adjustment (sophomore surge for new incumbents, penalty for retiring/defeated incumbents). (statistical)
  > Standard deviation for every electorate, 3.3%. This is a measure of how far we expect each electorate to deviate from uniform swing, on average... If a new (i.e. sophomore) incumbent is contesting in this electorate, I added 1% onto the 2pp for that incumbent's party.
  - Chiffres : 3.3% standard deviation, +/-1% incumbency adjustment
  [how-predictive-is-the-pre-election-pendulum]
- A uniform-swing-based probabilistic seat model, when fed the actual final two-party-preferred result (not polling), forecasts Australian federal Labor/Coalition seat totals to within an average of +/-2.0 to 2.5 seats across ten elections from 1993 to 2019. (empirical)
  > If a uniform swing model is given the correct 2pp result ahead of time, it'll be able to get the seat totals for the major parties to within +/- 2 to 3 seats on average.
  - Chiffres : Labor average difference +/-2.5 seats, Coalition average difference +/-2.0 seats, 1998 Labor: predicted 71.4 vs actual 67 (4.7 off), 2001 Labor: predicted 65.1 vs actual 65 (0.1 off)
  [improving-seat-forecasts-based-on-the-uniform-swing-model]
- Adjusting uniform swing for a candidate/incumbency effect (worth roughly 1 point of two-party-preferred vote for major-party incumbents) reduces average forecast error across 1993-2019 Australian elections from 2.7% to 2.4%, an 11% relative error reduction. (empirical)
  > On average, adjusting for candidate effects reduces the average 2pp error from 2.7% to 2.4%. While that might not sound like a lot, this amounts to an 11% reduction in the average error.
  - Chiffres : 2.7% baseline error, 2.4% adjusted error, 11% relative reduction, ~1 point incumbency boost
  [improving-seat-forecasts-based-on-the-uniform-swing-model]

### Matrices de transfert / reports de voix / front republicain

- Sur les mêmes données, la méthode King's EI (1997) produit des erreurs très importantes et inverse parfois le sens des relations substantielles trouvées dans les données individuelles, contrairement à Thomsen. (empirical)
  > King's EI estimates the total percentage of those voting for Bush and the Senate Democrat as 0.19% (compared to 3.13% using the actual ballot image data and 3.44% using Thomsen's approach)
  - Chiffres : 0.19% (King EI) vs 3.13% (vérité) vs 3.44% (Thomsen), facteur d'erreur jusqu'à 21x
  [ecological-inference-under-unfavorable-conditions-straight]
- L'Enquête électorale française vague 7 (Ipsos, août 2024) repose sur un échantillon de 11 204 personnes interrogées en ligne du 26 juillet au 1er août 2024, avec une marge d'erreur de ±0,7 point pour un score de 20% (IC 95%) — taille d'échantillon nettement supérieure aux sondages électoraux classiques (souvent 1000-2000 personnes). (empirical)
  > 11 204 personnes, constituant un échantillon national représentatif de la population française... pour un échantillon de 11 204 personnes, si le score mesuré est de 20%, il y a 95% de chances pour que la valeur réelle se situe aujourd'hui entre 19,3% et 20,7% (plus ou moins 0,7 point).
  - Chiffres : 11 204 personnes, ±0,7 point, 26 juillet - 1er août 2024
  [elections-lgislatives-2024-2]
- Dans un test expérimental randomisé où chaque tiers de l'échantillon se voit présenter une hypothèse de candidat NFP différent (Parti socialiste, écologiste, ou La France insoumise) face au RN au second tour, la propension globale à voter pour le candidat NFP baisse de 40% (candidat PS) à 38% (candidat écologiste) puis 32% (candidat LFI) -- une preuve par sondage expérimental (et non seulement par régression a posteriori sur résultats) de la pénalité spécifique de l'étiquette LFI. (statistical)
  > Question : « Dans votre circonscription, au second tour, si le candidat de la coalition de la gauche « Le Nouveau Front Populaire » était du XX et était opposé au RN et ses alliés au second tour…?» Base : Chaque parti a été présenté à un tiers de l'échantillon ... 40 / 38 / 32 % Voterait pour le NFP
  - Chiffres : 40%, 38%, 32%
  [elections-lgislatives-2024]
- Les électeurs RN et alliés souhaitent très majoritairement (77%) qu'aucune consigne de vote ne soit donnée par leur camp en cas de duel Nouveau Front Populaire vs Ensemble sans candidat RN au second tour, plutôt qu'un report vers l'un des deux autres blocs (16% souhaiteraient un report vers Ensemble). (statistical)
  > 4 / 3 / 16 / 77 Qu'ils appellent à voter pour le candidat du Nouveau Front Populaire [...] Qu'ils appellent à voter pour le candidat d'Ensemble [...] Qu'ils ne donnent pas de consigne de vote
  - Chiffres : 4%, 3%, 16%, 77%
  [elections-lgislatives-2024]
- A la veille du second tour des législatives 2024, 59% des sondés pronostiquaient une victoire en sièges du RN et ses alliés à l'Assemblée nationale, mais seulement 40% le souhaitaient -- un écart de 19 points entre pronostic perçu et préférence réelle. (statistical)
  > 24 / 17 / 59 [pronostic NFP/Ensemble/RN] ... 31 / 29 / 40 [souhait NFP/Ensemble/RN]
  - Chiffres : 59%, 40%, 24%, 17%, 31%
  [elections-lgislatives-2024]
- 74% des sondés se déclaraient insatisfaits de l'action d'Emmanuel Macron à la veille du second tour des législatives 2024, avec un écart très fort selon le vote au premier tour (12% de satisfaits chez les électeurs NFP, 68% chez les électeurs Ensemble, 37% chez LR, 7% chez RN). (statistical)
  > % Pas satisfait: 74 ... % Satisfait: 26
  - Chiffres : 74%, 26%, 12%, 68%, 37%
  [elections-lgislatives-2024]
- The BES vote-switching constituency nowcast, updated on election day itself with the latest polls, predicted Labour as the largest party in the 2015 UK general election with no party reaching a majority — a prediction the actual result (Conservative majority) directly contradicted. (empirical)
  > unlike most other prediction models we are predicting Labour to be the largest party, albeit with a very small lead in seats.
  - Chiffres : SNP: >50 of 59 Scottish seats predicted, Lib Dems: 23 seats predicted
  [general-election-constituency-forecast-update-the-british-election-study]
- Predicting individual-level ethnicity from voter registration records and Census surname data via Bayes' rule (BISG) achieves 6% false-positive rate for Black voters and 3% for Latino voters while maintaining true-positive rate above 80%, validated against 9 million real Florida voter records with self-reported ethnicity. (empirical)
  > We find that it is possible to reduce the false positive rate among Black and Latino voters to 6% and 3%, respectively, while maintaining the true positive rate above 80%.
  - Chiffres : 9 million records, 6% FPR Black, 3% FPR Latino, >80% TPR
  [improving-ecological-inference-by-predicting-individual]
- A separate user reported a corrupted/malformed bureau-de-vote code for Montbéliard in the 2020 municipales source file itself (spreadsheet scientific-notation artifact), propagating into the aggregated dataset as a mismatched key relative to the 2024 législatives code for the same commune. (empirical)
  > certains codes de bureaux de vote de Montbeliard son incorrects: '25388_0,00E+00' pour id_election = '2020_muni_t1' et id_brut_miom = '25388_0000' pour id_election = '2024_legi_t1'
  - Chiffres : 25388_0,00E+00, 25388_0000
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr-2]

### Inference ecologique (methodes, validations, critiques)

- In non-Hispanic subgroup estimates for Los Angeles and Stockton, King's EI method again performs worse than the neighborhood model and is sometimes worse than plain ecological regression, extending the original critique beyond the minority-group estimates. (empirical)
  > King's method does not appear in the table because in each case it does less well than the neighborhood model; furthermore, in each of the Los Angeles data sets, it does less well than ecological regression.
  - Chiffres : Party affiliation Z = -33.0, Education Z = 24.0, High Hispanic party affiliation Z = -18.2
  [a-rejoinder-to-king]
- On King's own preferred South Carolina poverty-by-sex dataset (used as a validation case in his 1997 book), the neighborhood model outperforms King's EI method for both men and women when tested against Census Bureau ground truth. (empirical)
  > King's method succeeds only in the sense that the estimate is within 1.1 standard errors of truth; the neighborhood model comes much closer to the mark, both for men and women.
  - Chiffres : Men in poverty: truth 12.9%, neighborhood 15.0%, King's method 5.8% +/- 6.6% (Z=-1.1), Women in poverty: truth 17.7%, neighborhood 15.7%, King's method 24.2% +/- 6.1% (Z=1.1)
  [a-rejoinder-to-king]
- Le papier ne rapporte aucune métrique de corrélation de rang (Spearman/Kendall) ni de backtest de validation contre une vérité-terrain externe ; c'est un travail de mesure/explication rétrospective des transitions de vote, pas un exercice de validation prédictive. (empirical)
  > we propose an ecological inference methodology to estimate the number of vote transitions within small homogeneous areas and to assess the relationships between these counts and local characteristics through multinomial logistic models
  - Chiffres : 0 occurrences de 'Spearman', 0 de 'Kendall', 0 de 'rank', 0 de 'backtest'
  [a-small-area-ecological-approach-for-estimating-vote-changes]
- Sur données réelles à vérité terrain (résultats de vote panaché officiellement publiés en Nouvelle-Zélande et en Écosse), les intervalles de confiance à 95% des trois principales méthodes d'inférence écologique RxC (Goodman, EI-MD/eiPack, EI-ML/Greiner-Quinn) ne contiennent la vraie valeur que 30 à 40% du temps, loin de la couverture nominale attendue de 95%. (empirical)
  > The confidence intervals of the EI-MD in its full form cover the true value only in about 30–40% of the cases... these results cast serious doubts on the ability of such techniques to live up to their promises of accuracy.
  - Chiffres : couverture EI-MD forme complète: 30-40%, couverture Goodman: ~30%, meilleur cas (ratio bureaux/coefficients > 2): EI-MD ~53%, attendu: 95%
  [an-evaluation-of-the-performance-and-suitability-of-rc-methods-for-ecological-in]
- La fiabilité des estimations d'inférence écologique RxC se dégrade pour les partis plus larges (grande part de vote) et pour les tables de contingence de plus grande dimension, et s'améliore avec un ratio bureaux de vote/coefficients à estimer plus élevé. (empirical)
  > the estimated 95% confidence interval is less likely to contain the true values in the case of larger contingency tables both in terms of number of columns and rows... the number of polling stations is positively correlated with precise confidence intervals.
  - Chiffres : critère recommandé: au moins 2 bureaux de vote par coefficient estimé
  [an-evaluation-of-the-performance-and-suitability-of-rc-methods-for-ecological-in]
- RN's seat count rose from 8 seats (2017) to 89 (2022) to 142 (2024), reflecting a sequence across three legislative elections useful for tracking geographic entrenchment over time. (statistical)
  > le RN enregistre une puissante progression en nombre de sièges : 142 en 2024, contre 89 en 2022 et seulement 8 en 2017.
  - Chiffres : 8 seats 2017, 89 seats 2022, 142 seats 2024
  [comprendre-la-gographie-du-vote-rn-en-2024-institut-terram]
- La majorité de la variation temporelle observée dans les sondages d'opinion au niveau État est due à la variabilité d'échantillonnage plutôt qu'à de véritables changements d'opinion ; une fois cette variabilité filtrée, la variance des estimations lissées beta_ij est 3 à 5 fois inférieure à la variance brute des sondages. (statistical)
  > In a typical state, the variance in the poll results was three to five times greater than the variance in beta_ij hat.
  - Chiffres : variance x3 à x5 supérieure dans sondages bruts, 98% des variations journalières de pi_ij < 0.5 point
  [dynamic-bayesian-forecasting-of-presidential]
- Ecological correlations computed at the aggregate (state/area) level can have the opposite sign from the true individual-level correlation, demonstrating the ecological fallacy is not a minor bias but can fully reverse an inference. (empirical)
  > The correlation between the 48 pairs of numbers is .53... In reality, the association is negative: the correlation computed at the individual level is −.11. The ecological correlation gives the wrong inference.
  - Chiffres : Ecological correlation +.53, Individual correlation -.11
  [ecological-inference-and-the-ecological-fallacy]
- A replication using 1995 Current Population Survey data (nativity vs. high income) shows the same sign reversal: ecological correlation of +.52 implies foreign-born have higher incomes, but the true individual-level relationship is negative and the gap is driven by immigrants concentrating in richer states. (empirical)
  > About 35% of the native-born have high incomes, compared to 28% for the foreign-born. The correlation at the individual level is −.05.
  - Chiffres : Ecological correlation +.52, Native-born high income 35%, Foreign-born high income 28%, Individual correlation -.05
  [ecological-inference-and-the-ecological-fallacy]
- On a controlled comparison where ground truth is known (nativity/income), the crude neighborhood model beats both ecological regression and King's random-coefficients EI method by a wide margin, with the regression-based methods overestimating foreign-born high-income share by roughly threefold. (empirical)
  > Table 2... 'random' is King's random-coefficients model, as implemented in his EZIDOS software... In a variety of test applications where all the data are available, the neighborhood model gives more accurate estimates for demographic groups than ecological regression or random-coefficients models.
  - Chiffres : Truth: native-born 35%, foreign-born 28%, Neighborhood model: 34%/36%, Ecological regression: 29%/85%, King's random-coefficients (EZIDOS): 30%/72%
  [ecological-inference-and-the-ecological-fallacy]
- L'estimateur de Thomsen (1987), fondé sur une théorie latente de choix binaire, reste robuste (biais faible) même quand les unités agrégées sont hétérogènes racialement et politiquement, contredisant l'hypothèse d'homogénéité qui sous-tend théoriquement l'estimateur. (empirical)
  > Using ballot image data as our measure of actual vote proportions, we find that the Thomsen estimator is robust to individually and collectively diverse settings.
  - Chiffres : indice de dissimilarité 2.72% (Miami-Dade), 3.50% (Palm Beach), 5.15% (Sarasota), 6.59% (Lee), 2.8 millions de bulletins
  [ecological-inference-under-unfavorable-conditions-straight]
- Le package ecolRxC, extension RxC générale de l'approche à structure latente de Thomsen (1987) et Park (2008), atteint une précision comparable aux deux méthodes considérées jusque-là comme les plus précises de la littérature (ei.MD.bayes et nslphom), validée sur 493 élections réelles à vérité terrain connue. (empirical)
  > ecolRxC, with default options, records an average EI error of 9.78, a figure quite similar to the numbers 10.52 and 9.77 reported in Pavía and Romero (2023) for ei.MD.bayes and nslphom, respectively.
  - Chiffres : EI error baseline (indépendance) = 36.98, ecolRxC = 9.78, ei.MD.bayes = 10.52, nslphom = 9.77, 565 datasets
  [ecolrxc-ecological-inference-estimation-of-r-c-tables-using-latent-structure-app]
- La précision de l'inférence écologique de type RxC se dégrade avec un faible nombre d'unités locales, une taille de table de contingence élevée, une hétérogénéité accrue entre unités locales, et une relation plus faible entre lignes et colonnes — ce qui explique la moins bonne performance en Écosse qu'en Nouvelle-Zélande. (empirical)
  > An analysis of the features affecting the accuracy of estimates reveals that ecolRxC, like other ecological inference models, faces challenges when the number of polling stations is small and the dimension of the contingency tables... increases.
  - Chiffres : diversité intra-district moyenne Écosse: 0.13-0.17, Nouvelle-Zélande: 0.20-0.25
  [ecolrxc-ecological-inference-estimation-of-r-c-tables-using-latent-structure-app]
- PyEI bundles multiple ecological-inference model families (iterative 2x2 Bayesian EI, RxC multinomial-Dirichlet EI via PyMC) in one Python library, along with shared uncertainty quantification, diagnostics, and cross-method comparison tooling, aimed at analysts inferring group-level voting behavior (e.g. racial bloc voting) from precinct-level aggregate election and demographic data. (empirical)
  > PyEI brings together a variety of inference methods in one place and facilitates reporting and plotting results; quantifying the uncertainty associated with results under a given model; making comparisons between methods; and bringing relevant diagnostic tools to bear on ecological inference methods.
  - Chiffres : v1.1.4 latest release, Jun 18 2025
  [github-mgggecological-inference-ecological-inference-in-python-github]
- eiCompare implements and directly compares three distinct ecological-inference estimator families for the same precinct-level dataset: Goodman's ecological regression (fast, deterministic baseline), King's (1997) iterative Bayesian 2x2 EI, and RxC multinomial-Dirichlet EI for simultaneous multi-candidate/multi-group estimation -- giving practitioners a built-in method-sensitivity check. (empirical)
  > The package provides three EI methods: Goodman's Regression (ei_good()) -- A fast, deterministic method based on ecological regression. Useful as a baseline estimate. Iterative EI (ei_iter()) -- King's (1997) iterative 2x2 ecological inference method with Bayesian estimation. RxC EI (ei_rxc()) -- Multinomial-Dirichlet model for simultaneous estimation across all race-candidate pairs.
  - Chiffres : v3.0.6
  [github-rpvoteeicompare-comparing-ecological-inference-techniques-github]

### MRP et post-stratification

- The 2017 YouGov MRP model correctly predicted 93% of individual constituency results, including shock outcomes in Canterbury and Kensington. (empirical)
  > It predicted 93% of the constituency results correctly and anticipated shock outcomes such as those in Canterbury and Kensington.
  - Chiffres : 93% of constituency results correct
  [different-methods-similar-outcome-comparing-the-poll-of-polls-with-mrp-lse-briti]
- YouGov's 2017 MRP model reported 95% confidence intervals per constituency but stated it would still expect the interval to be wrong (miss the true outcome) in 30 to 40 of the ~650 constituencies. (statistical)
  > Even these are not fail-safe: we would still expect the interval to be wrong in 30 to 40 constituencies.
  - Chiffres : 30 to 40 constituencies, 95% confidence interval
  [how-the-yougov-model-for-the-2017-general-election-works]
- The calibration approach extends to PRECINCT-level estimates -- below the county/district level -- by initializing precinct predictions from county-level MRP and calibrating to observed precinct-level vote share, and this precinct-level extension also reduces error by about 60%, comparable to the county-level gain, in real 2022 Michigan election data. (empirical)
  > Our precinct-level extension reduces error by 60%... We also show how our calibration approach can be used to generate estimates for smaller nested geographies, such as precincts, even in the absence of poststratification data at this level.
  - Chiffres : 60% error reduction (precinct level)
  [improving-small-area-estimates-of-public-opinion-by-calibrating-to-known-populat]

### Modeles bayesiens de forecasting

- Le prior structurel (forecast historique hi basé sur les fondamentaux macroéconomiques, ex. Time-for-Change) est incorporé via une distribution Normale informative sur beta_iJ, avec une précision tau_i choisie par l'analyste ; une sensibilité analysis montre que tau_i ne doit généralement pas dépasser 20 sous peine d'intervalles crédibles trop étroits (surconfiance). (statistical)
  > A sensitivity analysis in Section 4.4 indicates that tau_i should not generally exceed 20... Values of tau_i > 20 generate credible intervals that are misleadingly narrow.
  - Chiffres : tau_i = 10 (early), tau_i = 20 (late), seuil tau_i > 20
  [dynamic-bayesian-forecasting-of-presidential]
- Sur l'élection 2008, le modèle Votamatic final atteint un écart absolu moyen (MAD) de 1.4% au niveau État, avec plus de la moitié des 50 États prédits à moins de 1% du résultat réel, et une seule erreur de vainqueur (Indiana) contre 4 à 9 erreurs pour les modèles structurels seuls. (empirical)
  > By Election Day, both sets of forecasts indicate a MAD of 1.4%, with more than half of states (27) predicted within 1% of the actual result... the only state incorrectly predicted by the model using trial-heat polls through Election Day was Indiana.
  - Chiffres : MAD 1.4%, 27/50 États à moins de 1%, 1 erreur de vainqueur (Indiana), vs. 4-9 erreurs pour modèles structurels seuls
  [dynamic-bayesian-forecasting-of-presidential]
- Les gains de précision les plus importants apportés par les sondages surviennent dans les 6 dernières semaines de campagne ; des sondages menés 4 mois avant l'élection ne réduisent le MAD que de 0.3 à 1 point, ce qui limite fortement l'utilité prédictive d'un modèle bayésien loin de l'échéance électorale. (empirical)
  > The largest improvements occur in the final 6 weeks of the campaign, when the polls become most informative about the election outcome... even polls conducted 4 months before the election reduce the MAD of the (early) Time-for-Change forecast by 0.3%, and the MAD of the normal vote forecast by 1%.
  - Chiffres : 0.3 point (early model, 4 mois avant), 1 point (normal vote model, 4 mois avant), gains concentrés sur 6 dernières semaines
  [dynamic-bayesian-forecasting-of-presidential]
- En backtest sur l'élection 2016 (résultat surprenant, mal anticipé par la plupart des agrégateurs), le modèle Economist prédit correctement 48 États sur 51 avec un score de Brier pondéré par collège électoral de 0.0726, comparé à 46/51 États et 0.0928-0.0936 pour les deux variantes de 538 (polls-plus / polls-only). (empirical)
  > economist (backtest) | 0.0725679 | 0.0508319 | 48 ... 538 polls-plus | 0.0928000 | 0.0664000 | 46 | 538 polls-only | 0.0936000 | 0.0672000 | 46
  - Chiffres : 48/51 États corrects (Economist), 46/51 États corrects (538 x2), ev_wtd_brier 0.0726 (Economist) vs 0.0928/0.0936 (538)
  [github-theeconomistus-potus-model]

### Combinaison de scrutins / indices partisans composites

- FiveThirtyEight calcule son indice de partisan lean par État/circonscription comme une pondération de 50% de l'écart de marge à la nation lors de la présidentielle la plus récente, 25% lors de la présidentielle précédente, et 25% d'un lean législatif d'État basé sur le vote populaire cumulé des 4 dernières élections à la chambre basse. (empirical)
  > This version of partisan lean... is calculated as 50 percent the state or district's lean relative to the nation in the most recent presidential election, 25 percent its relative lean in the second-most-recent presidential election and 25 percent a custom state-legislative lean based on the statewide popular vote in the four most recent state House elections.
  - Chiffres : 50% présidentielle t, 25% présidentielle t-1, 25% lean législatif (4 dernières élections chambre basse)
  [datapartisan-leanreadmemd]
- FiveThirtyEight affirme explicitement que ses indices de partisan lean ne sont pas comparables d'une année à l'autre en raison du redécoupage électoral (redistricting) et des changements de méthodologie, et publie des versions distinctes 2018, 2020, 2021 (pré-redécoupage) et 2022 (post-redécoupage). (empirical)
  > Due to redistricting and changes in methodology, partisan leans are not comparable across years.
  - Chiffres : 4 versions distinctes : 2018, 2020, 2021, 2022
  [datapartisan-leanreadmemd]
- FiveThirtyEight publie des scores d'élasticité politique (sensibilité au climat national) à deux mailles : par État/DC et par circonscription (les 435 districts de la Chambre), dérivés des caractéristiques démographiques des électeurs plutôt que d'une régression directe sur les résultats électoraux passés. (empirical)
  > An elasticity score measures how sensitive a state or district it is to changes in the national political environment. elasticity-by-district.csv contains the elasticity scores for all 435 congressional districts.
  - Chiffres : 435 circonscriptions couvertes
  [fivethirtyeight-elasticity]
- Le redécoupage partisan réduit la réactivité (élasticité) sièges-votes de la Chambre des représentants au vote national : un point de pourcentage supplémentaire de vote populaire national ne rapporte que 7.8 sièges en moyenne sous le plan adopté, contre 9.2 sièges sous le plan non-partisan de référence. (statistical)
  > we find that an additional percentage point increase in national popular vote nets each party only 7.8 seats, on average, versus 9.2 under the non-partisan baseline.
  - Chiffres : 7.8 sièges/point (plan adopté), 9.2 sièges/point (baseline non-partisane), baisse d'environ 15% de réactivité
  [gerrymandering]
- L'indice Baseline d'Inside Elections combine tous les résultats d'élections fédérales et d'État (Chambre, Sénat, gouverneur, et postes constitutionnels d'État) sur les 4 derniers cycles électoraux (2016-2022), soit plus de 750 courses et environ 7 950 résultats répartis sur les 435 circonscriptions de la Chambre, pour estimer le score qu'un candidat 'typique' de chaque parti obtiendrait dans chaque circonscription. (empirical)
  > Inside Elections' Baseline captures a congressional district's political performance by combining all federal and state election results over the past four election cycles into a single score... over 750 races in total, or approximately 7,950 results when broken down across all 435 seats.
  - Chiffres : 750+ courses, ~7 950 résultats, 435 sièges, 4 cycles (2016-2022)
  [inside-elections-baseline]
- Le score Baseline 2022 est corrélé à 97% avec le résultat présidentiel 2020 et à 95% avec le résultat de l'élection à la Chambre 2022 dans chaque circonscription, ce qui montre qu'un indice composite multi-scrutins reste fortement aligné avec les scrutins individuels de référence tout en en lissant la volatilité. (statistical)
  > a district's 2022 Baseline margin was 97 percent correlated with the results of the 2020 presidential election, and 95 percent correlated with the 2022 House race.
  - Chiffres : corrélation 97% avec présidentielle 2020, corrélation 95% avec législatives 2022
  [inside-elections-baseline]
- L'écart entre le résultat réel d'un candidat et son score Baseline structurel mesure la force personnelle du candidat : Biden a dépassé le Baseline démocrate moyen de près de 3 points par circonscription en 2020, contre 1.2 point au niveau État et 4.5 points au niveau national (marge du vote populaire). (statistical)
  > Biden overperformed the Democratic Baseline by an average of nearly 3 points across all districts... at the state level, Biden outpaced the Democratic Baseline by an average of 1.2 points, and nationally, he won the popular vote by 4.5 points.
  - Chiffres : +3 points (niveau circonscription), +1.2 point (niveau État), +4.5 points (niveau national, vote populaire)
  [inside-elections-baseline]
- Le score Baseline final par parti est calculé comme une moyenne tronquée (trimmed mean) excluant à la fois la meilleure et la pire performance de chaque parti sur l'ensemble des scrutins retenus, ce qui élimine l'effet des candidats exceptionnels ou des élections sans opposition réelle. (empirical)
  > To calculate each party's Baseline, simply take the trimmed mean of all previous elections — in other words, an average omitting the highest and lowest values for each party... the 9th's Democratic Baseline is 56.1 percent, while its Republican Baseline is 41.3 percent. The district's Baseline margin — D+14.8 — suggests this seat is a few points more Republican-leaning than the two D+18 federal ra
  - Chiffres : Baseline démocrate 56.1%, Baseline républicain 41.3%, marge Baseline D+14.8 vs D+18 pour présidentielle/Chambre seules
  [inside-elections-methodology]

### Praticiens francais (instituts, estimations 20h, projections sieges)

- An independent (non-Ipsos) October 2025 poll commissioned by Politis from Institut Bona Fide found only 41% of French respondents willing to enact a front républicain in a future national election, with 59% opposed. (statistical)
  > seuls 41 % des Français se déclarent favorables au front républicain. Autrement dit, près de six sur dix refusent aujourd'hui l'idée même d'un barrage face au RN.
  - Chiffres : 41%, 59%
  [alerte-rouge-sur-le-front-rpublicain-politis]
- Hanretty (2017) valide son modèle de régression de Poisson à l'échelle (small-area estimation par interpolation aréale) pour ré-estimer le vote Leave/Remain à la maille des circonscriptions de Westminster contre des résultats infra-locaux réellement connus pour 27 circonscriptions britanniques, obtenant une erreur médiane de 1,62 point de pourcentage contre 5,22 points pour l'interpolation dasymétrique simple. (empirical)
  > half of constituencies had errors equal to or less than 1.62%, compared to an equivalent figure of 5.22% for dasymmetric interpolation
  - Chiffres : 1.62%, 5.22%, 27 constituencies
  [areal-interpolation-and-the-uks]
- Les cinq formes fonctionnelles alternatives testées par Hanretty (Poisson, binomiale négative, log-linéaire, pourcentage, interpolation dasymétrique) produisent des estimations toutes corrélées à plus de 0,9 entre elles, mais les méthodes à base de modèle démographique corrèlent nettement plus fort entre elles (>0,98) qu'avec la dasymétrique simple (~0,93), isolant l'apport spécifique de la modélisation par rapport à une simple répartition proportionnelle de la population. (statistical)
  > correlations between the model-based methods are always higher than the correlations between any model-based method and dasymmetric interpolation.
  - Chiffres : Poisson-Negative binomial: 0.999, Poisson-Percent: 0.996, Poisson-Dasymmetric: 0.928
  [areal-interpolation-and-the-uks]
- Ipsos-Talan estime le résultat national à 20h à partir d'un échantillon d'environ 600 bureaux de vote jugés représentatifs (par type de commune et orientation politique historique du bureau), avec des enquêteurs physiquement présents au dépouillement. (empirical)
  > L'institut envoie ses enquêteurs dans près de 600 bureaux constituant leur échantillon. Chacun d'entre eux assiste au dépouillement et transmet...
  - Chiffres : 600 bureaux
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- Environ 70% des bureaux de l'échantillon Ipsos ferment à 18h, 5-10% à 19h et 20-25% à 20h ; l'estimation à 20h extrapole les tendances des bureaux déjà dépouillés vers ceux qui viennent tout juste de fermer, ce qui peut introduire un biais si la dynamique diffère (ex. sous-estimation de Mélenchon à 18% au lieu de 22% final au 1er tour présidentielle 2022). (empirical)
  > les estimations du score de Jean-Luc Mélenchon avoisinaient 18% à 20 heures avant de remonter au cours de la soirée pour approcher 22% à mesure qu'étaient pris en compte les résultats des grandes villes, où il a fait de meilleurs scores.
  - Chiffres : 70%, 5-10%, 20-25%, 18%, 22%
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- Contrairement aux estimations nationales (fondées sur des résultats réels de bureaux dépouillés), les projections en sièges se fondent sur des enquêtes d'opinion classiques : Harris Interactive interroge 6000 à 7000 personnes le jour du scrutin sur plusieurs hypothèses de second tour, sans connaître les configurations réelles de duels/triangulaires. (empirical)
  > On interroge des personnes sur le second tour sans avoir le résultat du premier, on ne connaît pas encore les duels ou les triangulaires de leur circonscription
  - Chiffres : 6000-7000 personnes
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- Avec les résultats du premier tour 2022, une participation de 60% aurait généré 120 triangulaires (au lieu des 8 réellement observées), et 200 triangulaires avec 65% de participation — la participation est le facteur mécanique majeur amplifiant l'incertitude des projections en sièges. (statistical)
  > L'incertitude des simulations de sièges augmente au soir du premier tour avec le nombre de triangulaires. Par exemple, avec les résultats de 2022, une participation à 60% aurait conduit à 120 triangulaires, et jusqu'à 200 avec 65% de participation
  - Chiffres : 60% participation, 120 triangulaires, 65% participation, 200 triangulaires, 8 triangulaires réelles en 2022
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- Faire varier d'un ou deux points la tendance nationale d'une force politique au premier tour peut faire basculer 30 à 40 sièges dans l'hémicycle projeté — illustration quantitative de la sensibilité extrême des projections en sièges aux petites variations de score national. (statistical)
  > Faire varier d'un ou deux points la tendance d'une force politique au premier tour peut ainsi faire basculer trente à quarante sièges dans l'Hémicycle projeté.
  - Chiffres : 1-2 points, 30-40 sièges
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- Le ministère de l'Intérieur publie les résultats officiels par commune à partir de 20h après dépouillement de près de 70 000 bureaux de vote, les résultats remontant via les préfectures ; les résultats ne sont considérés comme définitifs qu'après validation par le Conseil constitutionnel. (empirical)
  > Le ministère de l'intérieur, chargé de l'organisation des élections, commence à diffuser les résultats par commune à partir de 20 heures, puis il met à jour ses publications en continu... Après la fermeture et le dépouillement de près de 70 000 bureaux de vote, les résultats sont remontés aux préfectures, qui elles-mêmes les envoient au ministère de l'intérieur.
  - Chiffres : 70 000 bureaux de vote, 20h
  [comment-les-instituts-de-sondage-estiment-les-rsultats-des-lections-lgislatives]
- For the March 1998 French regional elections, Ipsos deployed a three-tier nested sampling design (national/regional/departmental) rather than a single flat sample, to produce estimates at multiple sub-national levels simultaneously. (empirical)
  > Pour ce faire, Ipsos fait appel à une quarantaine de bureaux de vote dans chacune de ces régions. Mais il y a encore plus complexe. Dans les trois régions phares du scrutin (Ile-de-France, Nord-Pas-de-Calais, Provence-Alpes-Côte d'Azur), l'opération Ipsos du 15 mars va plus loin dans la précision. Afin d'obtenir des estimation pointues, 30 bureaux de vote ont été sélectionnés dans chacun des dépar
  - Chiffres : 1180 total bureaux de vote, 450 bureaux for national estimate, ~40 bureaux per region across 21 continental regions, 30 bureaux per département in 3 flagship regions, ~1 million registered voters sampled
  [comment-se-fabrique-lopration-estimation-ipsos-ipsos]
- The finer the sub-national estimation granularity, the later the result is available on election night: national estimate at 20h, but Nord-Pas-de-Calais regional/departmental seat projections at 20h, PACA at 21h, and Ile-de-France not until 21h30. (empirical)
  > Voilà qui permettra de donner des projections en sièges dans la région du Nord-Pas-de-Calais dés 20H, en Provence-Alpes-Côte d'Azur à 21H et en Ile-de-France à 21H30.
  - Chiffres : 20h Nord-Pas-de-Calais, 21h PACA, 21h30 Ile-de-France
  [comment-se-fabrique-lopration-estimation-ipsos-ipsos]
- The 1998 Ipsos correspondents in sampled bureaux reported in three sequential phone calls (mid-afternoon turnout, ~19h count of first 200 ballots, ~19h30 full station tally), the same 200-ballot threshold mechanism later documented for the modern national 20h estimate but replicated across a much larger 1,180-station panel to support multi-level output. (empirical)
  > En milieu d'après-midi, ils appelleront l'institut pour donner une indication de participation dans le bureau où ils se trouvent. Vers 19H, ils rappelleront une seconde fois pour fournir les résultats sur les 200 premiers bulletins de vote dépouillés. Leur troisième appel, aux alentours de 19H30 (pour les bureaux qui ferment à 18H), indiquera les résultats complets du bureau.
  - Chiffres : 1180 correspondents, 200 first ballots at second call, three call waves
  [comment-se-fabrique-lopration-estimation-ipsos-ipsos]
- The geography of the RN vote observed in the 2024 legislative first round shows no structural change relative to the traditional RN electoral map, and the same is true of the RN map in the 2024 European elections. (empirical)
  > La géographie du vote observée au soir du premier tour des législatives ne révèle pas de modification structurelle par rapport à la traditionnelle carte du vote RN. C'est également vrai de la carte du vote RN au soir des élections européennes.
  - Chiffres : RN 31.4% European elections 2024, Renaissance 14.6%, RN+allies 33.2% legislative round 1 2024, 18.7% legislative round 1 2022
  [comprendre-la-gographie-du-vote-rn-en-2024-institut-terram]
- RN vote share correlates strongly and consistently with commune size, exceeding 40% in communes under 2,000 inhabitants and being markedly lower in large metropolises, a pattern described as a structural constant of RN's electoral geography. (empirical)
  > Une autre constante de la géographie du vote RN a subsisté pour ces élections législatives de 2024 : sa très inégale intensité selon la variable du nombre d'habitants dans la commune... plus de 40% dans les communes de 2000 habitants et moins.
  - Chiffres : 40% RN in communes <2,000 inhabitants
  [comprendre-la-gographie-du-vote-rn-en-2024-institut-terram]
- L'enquête Ipsos-Talan 'Comprendre le vote' sur les législatives 2024 pondère son échantillon par calage sur marges en utilisant explicitement le vote au premier tour de la présidentielle 2022 ET le vote aux élections européennes 2024 comme variables de recalage, en plus de sexe/âge/CSP/agglomération/région. (empirical)
  > Critères de pondération : sexe, âge, profession de la personne interrogée, catégorie d'agglomération, région, vote au premier tour de l'élection présidentielle 2022 et vote aux élections européennes 2024.
  - Chiffres : 10286
  [elections-lgislatives-2024]
- L'enquête Ipsos-Talan sur les législatives 2024 repose sur un échantillon de 10 286 personnes interrogées en ligne via l'Access Panel Online d'Ipsos les 27 et 28 juin 2024, avec une méthode des quotas (sexe, âge, profession, agglomération, région), certifiée selon la norme ISO 20252. (empirical)
  > 10 286 personnes, constituant un échantillon national représentatif de la population française, inscrites sur listes électorales, âgées de 18 ans et plus. Du 27 au 28 juin 2024
  - Chiffres : 10286
  [elections-lgislatives-2024]
- En comparant le plan de redécoupage congressionnel adopté en 2022 à un ensemble de plans simulés non-partisans par Monte Carlo, le gerrymandering partisan net à l'échelle nationale ne représente qu'un avantage de 2.3 sièges pour les Républicains (8.6 sièges de biais pro-R contre 6.2 sièges de biais pro-D à travers les États, qui s'annulent presque). (statistical)
  > partisan effects are expected to contribute to 8.6 Republican seats and 6.2 Democratic seats over a non-partisan baseline. This nets out to a Republican advantage worth around 2.3 congressional seats.
  - Chiffres : 8.6 sièges biais pro-R, 6.2 sièges biais pro-D, avantage net 2.3 sièges, 20/44 États avec écart significatif à 5%
  [gerrymandering]
- Pour obtenir la majorité à la Chambre sous le plan de découpage adopté en 2022, les démocrates ont besoin d'au moins 51.1% du vote populaire bipartisan national, contre un seuil à peine inférieur (0.14 point de moins) sous le plan non-partisan de référence, ce qui montre que le biais structurel imputable au seul découpage reste faible comparé au biais géographique préexistant. (statistical)
  > To win a majority in the US House of Representatives under the enacted plan, Democrats need more than 51.1% of the national two-party popular vote, just 0.14 percentage points more than under the non-partisan baseline.
  - Chiffres : seuil de majorité 51.1% (plan adopté), 0.14 point d'écart avec baseline non-partisane
  [gerrymandering]
- Calibrating county-level MRP estimates to a known, highly-correlated ground-truth marginal (e.g., the actual gubernatorial election result) reduces county-level estimation error by roughly two-thirds relative to traditional (uncalibrated) MRP, validated on a real 2022 Michigan pre-election poll of abortion-referendum support. (empirical)
  > We find that the method reduces county-level error by nearly two-thirds relative to traditional MRP... Calibrating to the governor race reduces county-level error by about two-thirds in the other elections.
  - Chiffres : ~two-thirds error reduction (county level)
  [improving-small-area-estimates-of-public-opinion-by-calibrating-to-known-populat]
- In the independent Institut Bona Fide n=1500 poll (Oct 2025), willingness to enact a front républicain splits sharply by 2022 presidential first-round electorate: 60% of Macron voters, 61% of Mélenchon voters, but only 15% of Le Pen voters and 5% of Zemmour voters. (statistical)
  > 60% des électeurs centristes, et 60% des électeurs Macron 22, sont prêts au front républicain. [...] 61% des électeurs 2022 de Jean-Luc Mélenchon y sont favorables.
  - Chiffres : 60%, 61%, 15%, 5%
  [institut-bona-fid-x-politis-les-franais-et-le-front-rpublicain]
- By party proximity, only 34% of Les Républicains-aligned respondents say they are willing to vote front républicain (66% opposed), compared to 73% of France Insoumise sympathizers and 71% of PS sympathizers — an independent, non-Ipsos confirmation of the asymmetric right-side erosion documented by Ipsos's Fractures françaises v13 (LR voters' RN transfer rising to 56%). (statistical)
  > Les Républicains* 34% [Oui] [...] 66% [Non] [...] France Insoumise 73% [Oui] [...] Parti Socialiste 71% [Oui]
  - Chiffres : 34%, 66%, 73%, 71%
  [institut-bona-fid-x-politis-les-franais-et-le-front-rpublicain]
- Willingness to enact a front républicain shows a sharp age gradient: 52% of under-35s favorable versus only 37% of those 35 and older, with the 50-64 age bracket the least favorable at 34%. (statistical)
  > 52% des moins de 35 ans se disent prêts à ce front républicain, alors que 63% des plus de 35 ans s'y disent opposés.
  - Chiffres : 52%, 63%, 37%, 34%
  [institut-bona-fid-x-politis-les-franais-et-le-front-rpublicain]
- Institut Bona Fide is methodologically independent of the Ipsos survey family, uses online quota sampling (sex/age/occupation/region strata) with published 95% margins of error (±1.4 to ±3.1pts), and follows the ICC/ESOMAR code, meaning this dataset is a genuinely separate methodological lineage from the Ipsos Fractures françaises series used for the 2024/2025 erosion comparison. (empirical)
  > L'enquête a été réalisée en ligne par l'institut Bona Fide auprès d'un échantillon représentatif de 1500 Français âgés de 18 ans et plus du 23 au 27 octobre 2025. [...] Cette enquête a été réalisée dans le strict respect du code ICC/ESOMAR
  - Chiffres : 1500, ±1.4 points, ±3.1 points
  [institut-bona-fid-x-politis-les-franais-et-le-front-rpublicain]

### Europeennes et theorie du second ordre

- La validation empirique de Hanretty est mesurée en erreur absolue médiane (MAE-like), pas en corrélation de rang (Spearman/Kendall) — le texte ne contient aucune occurrence de ces termes — ce qui signifie que même ce cas européen ne comble pas exactement le pilier théorique 'sortie ordinale/classement' visé par le projet, bien qu'il en soit le complément empirique le plus proche identifié en Europe. (empirical)
  > As the table demonstrates, the correlation between all of the different functional forms is extremely high, and above 0.9 in all cases.
  - Chiffres : 0 occurrences de Spearman/Kendall/rank
  [areal-interpolation-and-the-uks]
- Cette page d'indexation, gelée en octobre 2023 et dont le dépôt a été archivé en mai 2025, ne référence aucun jeu de données pour les élections européennes 2024 ni législatives 2024, ces scrutins étant postérieurs à son dernier commit. (empirical)
  > This repository was archived by the owner on May 19, 2025. It is now read-only. [...] Latest commit ... Oct 25, 2023
  - Chiffres : octobre 2023, mai 2025
  [datagouvfr-pagespagesdonnees-des-elections-et-referendumsmd-at-master-etalabdata]
- 96% des sympathisants déclarés du RN ont voté pour la liste Bardella aux européennes 2024, indiquant une fidélité électorale quasi-totale du socle partisan RN. (statistical)
  > 96 % des personnes qui se disent proches du RN ont voté pour la liste du président de la formation d'extrême-droite. Seules 2 % ont choisi la liste Reconquête.
  - Chiffres : 96%, 2%
  [europennes-2024-tout-savoir-sur-la-sociologie-lectorale-du-scrutin]
- La sociologie du vote RN aux européennes 2024 montre une forte polarisation par catégorie socioprofessionnelle : 54% des ouvriers, 40% des employés et 36% des retraités CSP- votants ont choisi le RN. (statistical)
  > Le Rassemblement National a séduit 54 % des ouvriers, 40 % des employés et 36 % des retraités CSP- qui se sont déplacés pour voter.
  - Chiffres : 54%, 40%, 36%
  [europennes-2024-tout-savoir-sur-la-sociologie-lectorale-du-scrutin]
- L'abstention aux européennes 2024 (48,6% des inscrits) présente un fort gradient d'âge inversé : 60% chez les 18-24 ans et 66% chez les 25-34 ans, contre seulement 29% chez les 70 ans et plus (soit 71% de participation). (statistical)
  > 60 % des 18-24 ans ne se sont pas déplacés. Chez les 25-34 ans, ils sont 66 % à avoir boudé les urnes. La tendance s'inverse passé 35 ans. Ceux qui ont le plus participé se situent dans la tranche 70 ans et plus. 71 % d'entre eux sont allés voter.
  - Chiffres : 48.6%, 60%, 66%, 71%
  [europennes-2024-tout-savoir-sur-la-sociologie-lectorale-du-scrutin]

### Recomposition 2017-2024 / obsolescence de 2022

- In the 2024 legislative first round, RN achieved its largest gains relative to 2017 outside its historical strongholds, notably in the traditionally left-leaning Southwest: +18.1 points in Tarn-et-Garonne, +17.9 in Lot-et-Garonne, +16.8 in Dordogne. (statistical)
  > dans le Sud-Ouest, longtemps considéré comme un bastion de la gauche, il connaît une forte croissance par rapport à 2017 : +18,1 points dans le Tarn-et-Garonne, +17,9 dans le Lot-et-Garonne, +16,8 en Dordogne.
  - Chiffres : +18.1pts Tarn-et-Garonne, +17.9pts Lot-et-Garonne, +16.8pts Dordogne
  [entre-sarkozy-et-le-pen-o-vote-t-on-rn-cartographier-leffet-bardella-le-grand-co]
- RN's historical strongholds intensified sharply between 2017 and 2024 even as the base expanded elsewhere: Haute-Marne rose from 17% (2007 FN level, 2nd department nationally) to 50.8% RN in 2024; Pas-de-Calais reached 48.7%, and Var 49.6%. (statistical)
  > La Haute-Marne affichait 17 % de vote RN (contre 50,8 % en 2024) et était le 2e département à voter RN, derrière l'Aisne.
  - Chiffres : Haute-Marne 17% (2007) to 50.8% (2024), Pas-de-Calais 48.7% (2024), Var 49.6% (2024)
  [entre-sarkozy-et-le-pen-o-vote-t-on-rn-cartographier-leffet-bardella-le-grand-co]

### Decoupages, contours et crosswalks (bureaux, precincts, IRIS, carreaux)

- Le modèle n'utilise les nouvelles limites de circonscription qu'une fois qu'elles ont survécu aux recours judiciaires ; à titre d'exemple daté, au 7 mai 2026 la Californie et le Texas utilisaient déjà les nouveaux découpages tandis que la Virginie et la Floride utilisaient encore les anciens, leurs recours étant toujours pendants. (empirical)
  > The model will only consider new district boundaries once they have survived any legal challenges to them (so as of May 7, 2026 for example, House forecasts for California and Texas use the new district boundaries but House forecasts for Virginia and Florida use the old ones).
  - Chiffres : date de référence : 7 mai 2026
  [2026-forecast-methodology]
- 6800 communes françaises contiennent plusieurs bureaux de vote, ce qui définit le périmètre où une analyse infra-communale du vote apporte une granularité supplémentaire par rapport au niveau communal. (empirical)
  > il était jusqu'à présent compliqué d'analyser de façon précise les différences de vote pouvant exister par quartier au sein d'une commune, dans les 6 800 communes contenant plusieurs bureaux de vote.
  - Chiffres : 6800 communes
  [a-vot-chaque-bureau-de-vote-ses-lecteurs]
- En croisant les contours de bureaux de vote reconstruits avec les données de revenu localisé Filosofi 2019, l'INSEE observe une corrélation forte et croissante entre niveau de vie médian et taux de participation au 1er tour de la présidentielle 2022, visible à l'échelle du bureau de vote dans les 25 plus grandes villes françaises avec un plateau autour de 80% de participation — corrélation peu visible au niveau communal faute d'observations suffisantes. (empirical)
  > plus le niveau de vie médian du contour du bureau de vote est élevé, plus les électeurs inscrits sur ce bureau se sont déplacés pour voter... Cette relation croissante entre niveau de vie et taux de participation, avec un plateau autour de 80% de participation, se retrouve dans chacune des 25 villes étudiées.
  - Chiffres : 25 plus grandes communes, 80% de participation (plateau)
  [a-vot-chaque-bureau-de-vote-ses-lecteurs]
- Le fichier des adresses REU diffusé en 2023 est une photographie figée du répertoire prise en septembre 2022, bien que le REU soit un registre vivant mis à jour en continu — cette obsolescence progressive limite la fraîcheur des contours dérivés. (empirical)
  > le REU est un répertoire vivant, mis à jour en permanence : le fichier des adresses diffusé aujourd'hui a été produit à partir d'une photographie de ce répertoire en septembre 2022.
  - Chiffres : septembre 2022
  [a-vot-chaque-bureau-de-vote-ses-lecteurs]
- CSP (categorie socio-professionnelle), employment status, and full-time/part-time variables are published by INSEE at IRIS granularity (~2,000 inhabitants per zone), derived from the population census, structurally separate from the Filosofi-based gridded ('carreaux') products. (empirical)
  > La base infracommunale «Activite des residents» fournit des donnees sur les caracteristiques des actifs (sexe, age, categorie socio-professionnelle), des salaries et non-salaries (sexe et age).
  - Chiffres : ~15,500 IRIS zones in France, 750 of which are in DOM, ~2,000 inhabitants per IRIS
  [activit-des-rsidents-en-2020-insee]
- L'auteur reconnaît lui-même que les 27 circonscriptions test ne sont pas représentatives de l'ensemble du pays (majoritairement urbaines, plus de la moitié en Écosse, aucune ne coïncidant parfaitement avec les limites d'autorité locale utilisées comme source), ce qui tend à SOUS-ESTIMER l'erreur réelle du modèle sur l'ensemble du Royaume-Uni. (empirical)
  > These constituencies are not representative of the UK as a whole. All are urban. More than half are Scottish. None overlap entirely with local authorities.
  - Chiffres : 27 constituencies
  [areal-interpolation-and-the-uks]
- L'ouvrage 'Nouvelle cartographie électorale de la France' (Souidi & Vonderscher, Textuel, janvier 2026) croise les résultats des ~70 000 bureaux de vote français (2017-2024) avec les données sociales INSEE disponibles au bureau depuis 2023, constituant la cartographie électorale à la maille bureau la plus aboutie identifiée pour la France — mais reste un exercice strictement descriptif/rétrospectif, sans aucune projection vers un scrutin futur. (empirical)
  > les auteurs restent surtout descriptifs. Ils documentent des corrélations entre conditions de vie et choix électoraux sans prétendre établir des causalités univoques.
  - Chiffres : 70 000 bureaux de vote, 304 pages, 24 euros
  [cartographie-bureaux-de-vote-rn-et-conditions-de-vie]
- Une régression multivariée au niveau des intercommunalités (âge, CSP, diplôme, revenu, mobilité) réduit l'écart brut de vote RN entre rural et urbain aux législatives 2024 de 10,9 points de pourcentage à seulement 1,3 point (rural autonome) et 3 points (périurbain) une fois neutralisés les effets de composition sociale, avec un modèle expliquant 72% de la variance. (statistical)
  > En neutralisant les effets de composition sociale, le résultat principal que nous obtenons est le suivant : l'écart brut entre rural, périurbain et urbain... de l'ordre de 11 points de pourcentage, tombe à 1,3 point pour le rural et à 3 points pour le périurbain !
  - Chiffres : 10.9 points, 1.3 point, 3 points, 72%
  [ce-qui-explique-vraiment-les-diffrences-de-vote-rn-entre-les-villes-et-les-campa]
- Entre deux élections présidentielles américaines consécutives (2016-2020), 81,2% des bureaux de vote n'ont subi aucun changement de périmètre affectant leur population, mais les changements restants touchent de façon disproportionnée les zones denses et les populations noires/hispaniques. (empirical)
  > Of the 175,426 precincts election officials created for the 2020 general election, 142,408 or 81.2% had no change from the 2016 general election affecting population.
  - Chiffres : 175,426 precincts, 142,408 unchanged, 81.2%, 33,018 changed precincts, 14,113 precincts retained ≥95% population continuity
  [changing-precinct-boundaries-who-is-affected-and-electoral]
- The key assumption underlying area-based IRIS/bureau crosswalks, 'équirépartition' (homogeneous distribution of voters/residents within each zone), is empirically false and can introduce significant bias for fine-grained sociological analysis. (empirical)
  > L'hypothèse clé de cette méthode est celle dite d'équirépartition : on part du principe que les électeurs/habitants sont répartis de manière homogène au sein de chaque bureau de vote ou IRIS. Or, cette hypothèse est évidemment fausse, et surtout, sur le terrain qui nous intéresse, elle est fausse de telle manière que cela risque d'introduire des biais significatifs.
  - Chiffres : bureau n°1375
  [comment-jai-presque-cartographi-les-lecteurs-fn-ladresse]
- Les résultats officiels de la présidentielle 2022 et des législatives 2022 par bureau de vote sont publiés par le Ministère de l'Intérieur sur data.gouv.fr sous des slugs dédiés distincts par tour (1er et 2nd tour). (empirical)
  > Résultats 1er tour : par bureau de vote (election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour) [...] Résultats 1er tour : par bureau de vote (elections-legislatives-des-12-et-19-juin-2022-resultats-definitifs-du-premier-tour)
  - Chiffres : 2022
  [datagouvfr-pagespagesdonnees-des-elections-et-referendumsmd-at-master-etalabdata]
- The data.gouv.fr aggregated-elections Airflow DAG (task_functions.py, process_election_data task) does not perform the bureau-de-vote to REU identifier crosswalk itself; it merely concatenates already-standardized per-source 'general-results.csv'/'candidats-results.csv' files pulled from a data.gouv.fr organization's community_resources, meaning the actual bureau-ID reconciliation logic ('the magic') is produced upstream by a decentralized, uninspected process. (empirical)
  > # getting preprocessed resources, the magic is there (when creating standardized files), here we only concatenate them
  - Chiffres : 204 lines / 7.39 KB file, organization id 646b7187b50b2a93b1ae3d45
  [datagouvfr_data_pipelinesdata_processingelectionsaggregationtask_functionspy-at]
- The INSEE Filosofi 2019 200m-grid ('carreaux') dataset includes age-structure variables broken into 9 age brackets, contradicting the assumption that gridded data is income/poverty-only. (empirical)
  > ind_0_3 Nombre d'individus de 0 a 3 ans / ind_4_5 / ind_6_10 / ind_11_17 / ind_18_24 / ind_25_39 / ind_40_54 / ind_55_64 / ind_65_79 / ind_80p / ind_inc Nombre d'individus dont l'age est inconnu
  - Chiffres : 9 age brackets plus unknown-age category, ind_18_24 variable flagged as biased due to fiscal attachment of students to parents' household
  [documentation-donnes-carroyes]
- Le travail de traitement des adresses du REU ayant permis la diffusion open data des données de bureaux de vote a été réalisé par l'INSEE entre octobre 2022 et juin 2023, en collaboration avec la DINUM/Etalab, soit environ 8 mois de traitement entre l'extraction des données brutes et leur publication. (empirical)
  > Ce travail a été réalisé par l'Insee entre octobre 2022 et juin 2023 avec la collaboration de la Dinum (Etalab).
  - Chiffres : octobre 2022, juin 2023
  [github-inseefrlabtraitement-adresses-reu-traitements-des-adresses-du-rpertoire-l]
- In a real-world maup worked example, disaggregating vote totals from old precincts to census blocks and reaggregating to new (redrawn) precinct boundaries lost roughly 12% of Democratic votes (23,401 to 20,566) and 11% of Republican votes (3,302 to 2,947) purely due to boundary mismatch between old-precinct and new-precinct shapefiles -- 884 and 1,227 of 3,014 total blocks respectively were unassigned to any precinct in each shapefile. (empirical)
  > So, out of 3,014 total Census blocks, 884 were not assigned to any old precinct and 1,227 were not assigned to any new precinct.
  - Chiffres : 23,401 to 20,566 (SEN18D), 3,302 to 2,947 (SEN18R), 884/3,014 blocks, 1,227/3,014 blocks
  [github-mgggmaup-the-geospatial-toolkit-for-redistricting-data-github]
- maup's smart_repair() function can enforce that repaired precinct geometries nest cleanly within a secondary set of region boundaries (e.g. counties), via the nest_within_regions parameter, addressing the common real-world case where precincts are supposed to nest into higher administrative units but don't due to shapefile stitching artifacts. (empirical)
  > smart_repair allows the user to optionally specify a second shapefile---e.g., a shapefile of county boundaries within a state---and then performs the repair process so that the repaired geometries nest cleanly into the units in the second shapefile.
  - Chiffres : v2.0.0 released Nov 30, 2023, v2.0.3 latest release Aug 20, 2025
  [github-mgggmaup-the-geospatial-toolkit-for-redistricting-data-github]
- A working, reproducible pipeline exists (raphaeljolivet/eu2024-stats-iris) that geographically joins 2024 European election results with 2020 INSEE IRIS-level demographic data across all of metropolitan France, using an automatically reconstructed bureau-de-vote geometry (from INSEE REU + OpenStreetMap) as the intermediate layer, released as an open geopackage. (empirical)
  > Ce projet croise les résultats des élections européennes de 2024 avec les données démographiques INSEE au niveau IRIS (2020), pour l'ensemble de la France métropolitaine. Cette jointure est faite de manière géographique, gràce à la reconstruction de la géométrie des bureaux de vote produite par cet autre projet.
  - Chiffres : 2020, 2024
  [github-raphaeljoliveteu2024-stats-iris-croisement-des-rsultats-aux-lections-euro]
- Quand un precinct est scindé entre plusieurs circonscriptions et qu'aucun scrutin concurrent au même découpage n'existe pour calibrer la répartition des voix (cas d'un scrutin ancien recalculé avec de nouvelles lignes), Inside Elections choisit explicitement de répartir les voix ÉGALEMENT entre circonscriptions plutôt que proportionnellement à la surface ou par estimation visuelle, un choix assumé comme arbitraire mais 'le plus défendable et reproductible'. (empirical)
  > our policy is to allocate a split precinct's votes across all districts evenly. This methodological decision notably differs from other standard techniques, such as assuming votes are allocated proportionally... or even making educated guesses by eyeballing maps.
  - Chiffres : écart max ~2 points entre méthodes de répartition
  [inside-elections-methodology]
- Quand un scrutin concurrent au même découpage existe pour calibrer la répartition d'un precinct scindé, Inside Elections répartit les voix au prorata exact des voix effectivement comptées dans chaque portion lors de ce scrutin simultané, comme illustré par le precinct 14 de Novi (Michigan), scindé entre les 6e et 11e circonscriptions, où 40% des voix démocrates au poste de gouverneur ont été assignées au 6e district car 40% des voix à la Chambre dans ce precinct en provenaient. (empirical)
  > 531 votes to Democratic Gov. Gretchen Whitmer... 40 percent of Democratic votes... were cast from the portion of this precinct located within the 6th District... we would designate 212 of Whitmer's votes — or 40 percent of her 531 total — to the 6th District.
  - Chiffres : 40% des voix démocrates gouvernorales → 6e district, 531 voix Whitmer, 220 voix Dixon, 762 voix totales
  [inside-elections-methodology]
- Le jeu de données REU est basé sur une extraction figée de septembre 2022 et ne sera actualisé que tous les cinq ans, limitant sa capacité à refléter les changements récents de découpage de bureaux de vote. (empirical)
  > Les données brutes utilisées par l'Insee correspondent à une extraction des adresses du Répertoire Électoral Unique réalisée en septembre 2022. [...] Ce jeu de données sera actualisé tous les cinq ans.
  - Chiffres : septembre 2022, 5 ans
  [jeu-de-donnes-bureaux-de-vote-et-adresses-de-leurs-lecteurs-datagouvfr]
- The id_brut_miom bureau-de-vote identifier scheme used to join French election results across cycles produces mismatching codes for the same physical bureau de vote between the Ministry of Interior's own published source data and the aggregated dataset's derived identifiers, requiring manual correction by the maintainers. (empirical)
  > Certains bureaux de vote ne correspondent plus avec ceux données par le ministère de l'intérieur. Par exemple, aux législatives 2024, à Montbéliard, on a des 0X01, 0X02... au lieu de 0E11, 0E321 au tour 1.
  - Chiffres : bureau codes '0X01', '0X02' vs source '0E11', '0E321'
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr-2]
- Overseas French territory (DOM-TOM) département-code prefixes were systematically mis-mapped in the aggregated elections pipeline, causing commune codes for Mayotte, New Caledonia, French Polynesia, and Wallis-et-Futuna to collide with unrelated metropolitan/overseas département codes. (empirical)
  > ZM (Mayotte): j'observe 975 au lieu de 976 (INSEE) - ZN (Nouvelle-Calédonie): j'observe 978 au lieu de 988 - ZP (Polynésie): j'observe 970/977 au lieu de 987 - ZW (Wallis-et-Futuna): j'observe 970 au lieu de 986
  - Chiffres : 975 vs 976, 978 vs 988, 970/977 vs 987, 970 vs 986
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr-2]
- The aggregated elections dataset's own description explicitly warns that its underlying data structure changed in January 2026, and the join mechanism is table-bv-reu.csv linking id_election + id_brut_miom fields to the INSEE REU, confirming the join is a versioned, per-update artifact rather than a fixed static schema. (empirical)
  > /!\ la structure des données a évolué en janvier 2026 ... Les jointures se font par l'intermédiaire de la table de conversion des identifiants des bureaux de vote (table-bv-reu.csv).
  - Chiffres : dataset views: 50.95K since June 2023 (+806 July 2026), downloads: 82.4K since June 2023 (+622 July 2026)
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr-2]
- Certains scrutins historiques agrégés dans ce jeu de données ne disposent pas de résultats au niveau bureau de vote (ex. départementales 2021 T1/T2, municipales 2008 hors communes de plus de 3500 habitants), limitant la profondeur temporelle utilisable pour une analyse fine par bureau. (empirical)
  > Départementales 2021 T2... Départementales 2021 T1... (pas de données au niveau bureau de vote) — Municipales 2008 (uniquement les communes de plus de 3500 habitants ; votes blancs et nuls réunis dans la colonne Nuls)
  - Chiffres : 2021, 2008, 3500 habitants
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr]
- Le slug data.gouv.fr 'elections-legislatives-2024-resultats-du-1er-tour-par-bureau-de-vote' redirige vers une réutilisation municipale isolée (Meudon) et non vers le jeu de données national du Ministère de l'Intérieur, confirmant que ce piège de ciblage n'est pas isolé à un seul scrutin. (empirical)
  > Ce fichier contient les résultats des élections législatives du 30 juin 2024 à Meudon (1er tour), bureau de vote par bureau de vote... Ce jeu de données provient d'un portail externe. Voir la source originale : data.meudon.fr
  - Chiffres : 30 juin 2024
  [jeu-de-donnes-lections-legislatives-2024-rsultats-du-1er-tour-par-bureau-de-vote]

### Sondages et mesure de la dynamique nationale

- Le dépôt NSPPolls est inactif depuis mai 2022 (dernier commit ddcd5ce, 23 mai 2022), avant les présidentielle/législatives suivantes, limitant sa couverture des cycles 2024. (empirical)
  > ## Latest commit May 23, 2022 ddcd5ce
  - Chiffres : 2022-05-23
  [github-nsppollsnsppolls-compilation-des-sondages-produits-loccasion-des-lections]
- L'échec de prédiction de 2016 dans les États du Midwest est attribué principalement à des sondages qui n'ajustaient pas pour la composition partisane de leur échantillon (non-réponse différentielle) ; le modèle 2020 introduit un terme d'ajustement autorégressif spécifique pour corriger ce biais, avec un paramètre de corrélation temporelle rho ~ Normal(0.7, 0.1). (empirical)
  > Poll-aggregation election forecasts performed poorly in 2016, a problem that can be attributed to polls in key midwestern states that did not appropriately adjust for nonresponse (Gelman & Azari, 2017)... ρ ~ Normal(0.7, 0.1).
  - Chiffres : rho ~ N(0.7, 0.1)
  [harvard-data-science-review-issue-24-fall-2020]

### Finalite militante : canvassing et ciblage

- Canvassing accounted for approximately one-half of Hollande's first-round lead and one-fourth of his second-round victory margin in the 2012 French presidential election. (empirical)
  > Multiplying these estimates by the fraction of French doors knocked, I obtain that the canvassing campaign accounted for approximately one-half of Hollande's lead in the first round and one-fourth of his victory margin at the second round.
  - Chiffres : one-half of round-1 lead, one-fourth of round-2 margin
  [door-to-door-canvassing-campaigns-sway-voter-decisions]
- Identical non-targeted canvassing script raised turnout among immigrants by 3.4pp (round 1, from 34.4% base) and 2.8pp (round 2, from 38.7% base) in France's 2010 Ile-de-France regional elections, with no significant effect on non-immigrant turnout. (empirical)
  > Canvassers' visits increased the turnout of immigrants and children of voting age living with them by 3.4 percentage points from a base of 34.4 percent (a 9.9 percent increase) in the first round of voting... The campaign had no impact on the voter turnout of non-immigrants.
  - Chiffres : 3.4 pp (round 1), 34.4% base turnout, 2.8 pp (round 2), 38.7% base turnout, 678 treated addresses / 669 control
  [increasing-the-electoral-participation-of-immigrants-experimental-evidence-from]

### Outils open source

- PyEI is formally published and citable via a peer-reviewed software paper: Knudson, Schoenbach & Becker (2021), 'PyEI: A Python package for ecological inference,' Journal of Open Source Software, 6(64), 3397, doi:10.21105/joss.03397. (empirical)
  > Knudson et al., (2021). PyEI: A Python package for ecological inference. Journal of Open Source Software, 6(64), 3397, https://doi.org/10.21105/joss.03397
  - Chiffres : JOSS vol 6, issue 64, article 3397, doi:10.21105/joss.03397
  [github-mgggecological-inference-ecological-inference-in-python-github]

### Ungrouped

- Le site unehistoireduconflitpolitique.fr met en accès libre les résultats électoraux numérisés des 36 000 communes françaises pour toutes les élections législatives et présidentielles de 1848 à 2022 ainsi que les principaux référendums de 1793 à 2005. (empirical)
  > Grâce à la numérisation des archives électorales au niveau des 36000 communes pour toutes les élections législatives et présidentielles de 1848 à 2022 et les principaux référendums de 1793 à 2005, il devient possible pour la première fois de comparer précisément qui vote pour qui.
  - Chiffres : 36 000 communes, 1848-2022, 1793-2005
  [cartographie-numrique-une-histoire-du-conflit-politique-lections-et-ingalits-soc]
- 79% of 200m grid cells in metropolitan France (representing 20% of the population) fall below the 11-household confidentiality threshold and are statistically imputed rather than directly observed, flagged via indicator variable i_est_200. (statistical)
  > En utilisant une grille de carreaux de 200 metres de cote, 79 % des carreaux habites de France metropolitaine comprennent moins de 11 menages fiscaux et doivent faire l'objet d'une imputation. Ils representent 20 % de la population totale.
  - Chiffres : 79% of 200m cells imputed, 20% of population in imputed cells, confidentiality threshold: 11 households, median cell: 2.6 households, 6 individuals
  [documentation-donnes-carroyes]
- The dataset's poor-household count (men_pauv) and standard-of-living sum (ind_snv) undergo special statistical treatment: men_pauv can be truncated at an 80% poverty rate per 200m cell, and individual income (niveau de vie) is winsorized at department-specific 5th/95th percentile thresholds before being summed per cell. (statistical)
  > Dans un departement donne, le niveau de vie d'un individu est rabaisse au 95e centile de la distribution departementale si son niveau de vie est superieur a ce seuil... A la suite de ce traitement, 10 % des individus ont ainsi fait l'objet d'une winsorisation de leur niveau de vie.
  - Chiffres : lower thresholds range 6,700-11,300 EUR, upper thresholds range 37,800-93,200 EUR, 10% of individuals winsorized nationally, 37% of metropolitan 200m cells contain at least one winsorized individual
  [documentation-donnes-carroyes]
- L'identifiant d'élection id_election encode l'année, le type de scrutin et le tour (ex. 2022_pres_t1 pour le 1er tour de la présidentielle 2022), et sert de clé de jointure entre les tables de résultats généraux et de résultats par candidat via id_brut_miom. (empirical)
  > La colonne id_election contient l'information de l'élection concernée (année, type, tour), par exemple : 2022_pres_t1 pour le premier tour de l'élection présidentielle de 2022. Les deux tables sont rapprochables par les colonnes id_election et id_brut_miom.
  - Chiffres : 2022_pres_t1
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr]
- La structure du jeu de données agrégé a été modifiée en janvier 2026, ce qui constitue une rupture de schéma documentée à prendre en compte pour tout pipeline de traitement s'appuyant sur des versions antérieures. (empirical)
  > /!\ la structure des données a évolué en janvier 2026
  - Chiffres : janvier 2026
  [jeu-de-donnes-donnes-des-lections-agrges-datagouvfr]

## Paires contestées (top clusters du graphe de contradictions)

### election-source-baseline — Quelle élection passée est la bonne baseline pour projeter 2027 au bureau de vote : européennes 2024 « sincères », législatives 2024 locales mais biaisées par l'offre, ou présidentielle 2022 comparable mais obsolète ?
- **Side A** ([sondages-lgislatives-2024-pourquoi-il-faut-se-mfier-des-proj], [the-beginning-of-the-end-of-tripartition-european-elections-and-social-inequalit]) : Les européennes 2024 sont la meilleure photographie : proportionnelle nationale à un tour, offre complète partout, chaque voix compte — directement transposable à une présidentielle multipolaire.
- **Side B** ([still-second-order-european-elections-in-the-era-of-populism], [nine-second-order-national-elections-a-conceptual-framework-], [les-dynamiques-dintention-de-vote-aux-lections-europennes-de]) : Les européennes restent un scrutin de second ordre (Reif & Schmitt) : abstention différentielle massive (~50% vs ~72% présidentielle), vote sanction, prime aux petits partis — le niveau ET la géographie de la participation diffèrent structurellement d'une présidentielle.
- Delta de qualité de preuve : Side B a la littérature académique (SOE testé sur 175 élections) ; side A a la pratique française récente (pondérations Ipsos calées sur européennes 2024, usage Cagé-Piketty). Fight serré — probablement résoluble en distinguant niveau absolu (side B gagne) et structure spatiale relative (side A gagne).

### sophistication-paie-maille-fine — La sophistication méthodologique (MRP, EI, bayésien) améliore-t-elle réellement la projection à maille fine, ou le gain s'évapore-t-il (voire s'inverse) sous le niveau circonscription ?
- **Side A** ([how-the-yougov-model-for-the-2017-general-election-works], [different-methods-similar-outcome-comparing-the-poll-of-poll], [ecolrxc-ecological-inference-estimation-of-r-c-tables-using-]) : Oui : MRP YouGov 2017 a prédit 93% des sièges et les chocs locaux (Canterbury, Kensington) ; la valeur ajoutée du MRP est précisément au niveau siège (écart de 13 sièges vs swing uniforme, LSE) ; ecolRxC/Thomsen atteignent des précisions de transfert bien supérieures à la baseline naïve.
- **Side B** ([uc-davis-previously-published-works], [mrp-poll-puts-reform-ahead-of-labour-and-the-tories-heres-wh], [pitfalls-of-demographic-forecasts-of-us-elections], [an-evaluation-of-the-performance-and-suitability-of-rc-methods-for-ecological-in]) : Non : la corrélation MRP↔vérité varie de 0,17 à 0,87 selon les covariables (Buttice & Highton) ; le sondage classique de More in Common a battu son propre MRP en 2024 ; les modèles de flux BES 2015 ont hérité du biais national ; les 24 projections en sièges publiées en France en 2024 se sont toutes trompées de vainqueur ; les prévisions démographiques sous-performent un 50-50 et la granularité fine AGGRAVE (Pons et al.) ; les IC sont sous-couvrants à maille fine dans toutes les familles (MRP, EI, swing).
- Delta de qualité de preuve : Side B empiriquement plus fort et plus systématique (Monte Carlo, backtests longs, validations ground-truth) ; side A repose sur des succès saillants mais sélectionnés. MAIS side B ne teste presque jamais la maille bureau — les deux extrapolent.

### fiabilite-ei-transferts — L'inférence écologique donne-t-elle des estimations de transferts de voix fiables, et si oui laquelle : Freedman vs King, puis Thomsen vs Dirichlet-multinomial ?
- **Side A** ([ecological-inference-under-unfavorable-conditions-straight], [estimation-of-voter-transitions-based-on-ecological-inferenc], [ecolrxc-ecological-inference-estimation-of-r-c-tables-using-]) : L'EI moderne marche : Thomsen robuste même en conditions défavorables (biais <0,02 dès 50 unités), ecolRxC comparable aux meilleures méthodes, eiPack/Dirichlet gagnant sur données allemandes ; avec ~70k bureaux, la France est un terrain idéal en nombre d'unités.
- **Side B** ([on-solutions-to-the-ecological-inference-problem], [a-rejoinder-to-king], [the-role-of-confounders-and-linearity-in], [an-evaluation-of-the-performance-and-suitability-of-rc-methods-for-ecological-in]) : Non-identifiabilité fondamentale (les DEUX camps Freedman-King en conviennent) : le modèle « neighborhood » naïf bat King 7/9 sur données réelles ; toutes les méthodes EI sous-estiment le panachage avec des biais directionnels systématiques ; IC nominaux 95% couvrant 30-53% ; l'identification exige une condition CAR invérifiable.
- Delta de qualité de preuve : Side B (critique) tient les validations ground-truth les plus propres ; side A tient les comparaisons intra-EI récentes. Fight interne à side A non résolu (Klima: Thomsen incohérent ; Park/Kuriwaki: Thomsen le moins biaisé) — la littérature se contredit selon le jeu de données de validation.

### reutilisabilite-matrices-2024 — Les matrices de transfert mesurées en 2024 (front républicain) sont-elles réutilisables pour projeter 2027 ?
- **Side A** ([elections-lgislatives-2024], [un-front-rpublicain-efficace-mais-illusoire-fondation-jean-jaurs], [les-reports-de-voix-premier-second-tour-ipsos]) : Oui en structure : les taux 2024 sont mesurés avec une précision inédite (ENEF n=11 204, ±0,7pt) ; l'asymétrie NFP→Ens (97%) vs Ens→NFP (73%) est un invariant comportemental documenté depuis 2015.
- **Side B** ([un-barrage-fissur-mais-pas-encore-bris-ltat-du-front-rpublic], [elections-lgislatives-2024], [octobre-2025-13me-edition]) : Non en niveau : l'érosion est rapide et mesurée (2025 : report LR vers barrage effondré, 56% de l'électorat LR irait au RN dans certaines configurations) ; une présidentielle n'est pas une législative (personnalisation, participation +25pts) ; les taux dépendent du candidat exact (pénalité LFI mesurée expérimentalement 40%→32%).
- Delta de qualité de preuve : Les deux côtés s'appuient sur la même famille d'enquêtes Ipsos (redondance partielle) mais à des vagues différentes — le désaccord est surtout TEMPOREL : structure stable, niveaux dérivants. Données d'excellente qualité des deux côtés.

---
title: 2026 Forecast — Methodology
id: 2026-forecast-methodology
tags:
- projections-electorales-bureaux-2027-b0b1c4
- electoral-forecasting
- bayesian-model
- redistricting
- swing-model
- open-source-tool
created: '2026-07-21T18:31:24.120260Z'
updated: '2026-07-21T18:39:17.739649Z'
source: https://www.electionstatsheet.com/model
source_domain: www.electionstatsheet.com
fetched_at: '2026-07-21T18:31:24.084973Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Documentation méthodologique du modèle de Mac Tan (dashboard electionstatsheet.com,
  cycle 2026 Congrès US), open source sur github.com/thisismactan/US-2026. Modèle
  bayésien MCMC (Stan) produisant une distribution jointe complète sur tous les sièges
  Chambre+Sénat, exprimée en part de vote bipartisane (2PV = R_votes/(R_votes+D_votes)).
  Deux composantes combinées par pondération inverse-variance (pas simple moyenne)
  : pred = (swing_pred/swing_var + poll_pred/poll_var) / (1/swing_var + 1/poll_var)
  — propriété clé : si aucun sondage n''existe (var_poll → infini), la prédiction
  converge vers le modèle de swing national seul ; si les sondages sont nombreux et
  fiables (var_poll → 0), elle converge vers les sondages seuls. Le modèle de ''swing
  national'' combine : (a) une baseline partisane = résultat 2PV de la précédente
  élection régulière (hors spéciales) au même poste, SAUF si l''élu sortant se retire,
  l''élection précédente n''était pas disputée, ou le découpage a changé depuis —
  dans ces cas le modèle bascule vers le résultat présidentiel le plus récent dans
  le district/État comme baseline de repli ; (b) l''environnement national mesuré
  par le ''generic congressional ballot'' (écart générique D vs R) issu des sondages
  ; (c) un effet sortant (incumbency) qui s''estompe en l''absence de titulaire, ramenant
  le district vers ses habitudes de vote présidentiel ; (d) une sensibilité accrue
  aux vagues nationales en mi-mandat qu''en année présidentielle. Traitement explicite
  et daté du redécoupage électoral : les nouvelles limites ne sont utilisées qu''une
  fois qu''elles ont survécu aux recours judiciaires (exemple concret cité : au 7
  mai 2026, la Californie et le Texas utilisent déjà les nouveaux découpages, la Virginie
  et la Floride encore les anciens, car leurs recours sont toujours pendants). Pondération
  des sondages selon 6 critères (méthodologie probabiliste vs opt-in, sponsor partisan
  ou non, population LV vs RV, récence <90j, taille d''échantillon >1000, durée de
  terrain) et ajustement temporel : un sondage ancien est recalé de l''écart dont
  le generic ballot a bougé depuis sa réalisation. Sources de données déclarées :
  MIT Election Lab (résultats historiques par circonscription 1976-2024, statique),
  Daily Kos Elections (marges présidentielles par circonscription historique), NYT
  Poll Tracking Project (sondages quotidiens), Ballotpedia (statut de titulaire/candidatures).
  Limites reconnues explicitement par l''auteur : sondages de course à la Chambre
  rares et sujets à un biais de sélection fort (souvent publiés seulement par les
  campagnes qui choisissent de les diffuser) ; pas de prise en compte directe de l''actualité/scandales
  sauf via leur répercussion dans les sondages ; pas de modélisation des candidats
  tiers pouvant faire basculer des courses serrées. Cas d''usage exemplaire pour la
  question française : gestion explicite et documentée du changement de découpage
  électoral entre scrutins (repli sur la présidentielle comme baseline stable quand
  le découpage a changé), et méthode de pondération bayésienne rigoureuse pour combiner
  un swing structurel multi-scrutins avec des sondages locaux disparates en qualité
  et en fréquence.'
---

Technical Documentation
# Methodology
How the model works — from raw data inputs to the forecasts displayed on this dashboard.
## Overview
<p>This dashboard visualizes <a href="https://mactan.substack.com/p/introducing-a-bayesian-2026-congressional">Mac Tan's forecast for the 2026 United States congressional elections</a>. Unlike simple poll averages or pundit ratings, the model produces a <strong class="highlight">full joint probability distribution</strong> across all House and Senate seats — not just a prediction of the outcome in each individual race.</p> <p>In short, it combines what we know about a district from recent history with what polling is telling us right now about the national and local political mood, weights each source according how certain its prediction is, and then runs thousands of simulated elections to generate win probabilities and credible intervals for the outcome in each race.</p> <p>Every number on this site is the direct output of that simulation. When you see "R Win: 63.4%", that means Republicans won the seat in about 6,340 out of 10,000 simulations.</p>
Historical Data ETL
`process_data.R` takes in historical district- and state-level election results and processes them to make them digestible for modeling.
Polling ETL
`process_polls.R` ingests daily polling from The New York Times' poll tracking project, applies weights for poll recency and quality, and computes polling averages at the national, state, and district level.
Stan Markov Chain Monte Carlo
Models for the House and Senate are built in Stan, which models the relationship between the variables in the historical election and polling datasets and draws samples from the posterior distribution of the parameters.
Extracting Forecasts
`house_sim.R` / `senate_sim.R` run the 2026 district- and state-level data through the posterior draws from the Stan models to obtain a posterior distribution for each House and Senate race. These individual results can then be aggregated up to produce forecasts for the entire House and Senate.
## The 2PV Metric
<p>All forecasts are expressed as <strong class="highlight">two-party vote share (2PV)</strong>. Votes for third-party and independent candidates are excluded, collapsing every race into a zero-sum probability space on the interval [0.0, 1.0].</p> <div class="formula-block"><pre>R2PV = R_votes / (R_votes + D_votes) Win condition: R2PV &gt; 0.5 → Republican wins the seat Win condition: R2PV &lt; 0.5 → Democrat wins the seat </pre></div> <p>Win probability in the final output is calculated as the <strong class="highlight">fraction of posterior draws</strong> where a party's 2PV exceeded 0.50. This is a direct integration over the posterior distribution using Hamiltonian Monte Carlo.</p> <div class="formula-block"><pre>P(R wins) = mean(R2PV &gt; 0.5) for sim_id in 1...N Where N = 10,000 posterior draws per seat </pre></div>
## National Swing Model
<p>The national swing model produces a posterior distribution for each district, based on an estimate of its baseline partisanship and the national political environment. Several factors go into this model:</p> <h3>Partisan Baseline</h3> <p>Each district and state starts from a baseline 2PV result, which is the 2PV result in the previous regularly scheduled House or Senate election (excluding special elections). However, often the prior election result doesn't serve as a reasonable baseline: common reasons for this would be that the incumbent is retiring, the previous election wasn't contested, or (in the case of House elections) the district's boundaries have been redrawn since the last election. In these cases the model will rely much more heavily on the most recent presidential election result in the district or state to form a partisan baseline. </p> <h3>National Environment</h3> <p>The generic congressional ballot (the gap between voters who prefer a generic Democrat vs. a generic Republican) average provides an estimate of the national political environment and the extent to which it favors Democrats or Republicans. This is estimated from available polling at any given forecast date. When the generic congressional ballot swings toward one party relative to the previous election, that party will generally perform better in House and Senate races across the board, although polling and other district- and state-specific factors can strengthen, weaken, or overpower this effect.</p> <h3>Incumbency</h3> <p>Incumbents generally do better than generic candidates from their party, even if their advantages are weaker than ever. When there is no incumbent running for re-election, states and districts tend to revert to their presidential voting habits. A race is assumed to have an incumbent running for election until the incumbent has either suspended their campaign or lost renomination.</p> <h3>Midterm</h3> <p>District- and state-level election results tend to be more sensitive to swings in the national political environment during midterms than in presidential elections.</p> <h3>Redistricting</h3> <p>When a House district's boundaries are redrawn (as is happening in a lot of places these days), the previous election results are less useful as a partisan baseline. In districts that have been redrawn since the previous election, the model relies much more heavily on the most recent presidential election result instead of the previous House or Senate election result. The model will only consider new district boundaries once they have survived any legal challenges to them (so as of May 7, 2026 for example, House forecasts for California and Texas use the new district boundaries but House forecasts for Virginia and Florida use the old ones). </p>
## Polling Model
<p>Polls go through adjustment and weighting before being averaged.</p> <h3>Partisan Adjustment</h3> <p>The poll partisanship adjustment is very basic: it adjusts polling results only if the New York Times poll tracker identifies the poll as a partisan poll. This is a hard criterion: it isn't enough for the pollster to generally produce results that lean toward one party; a poll is considered partisan only if it is conducted for a political party, explicitly partisan organization, or a candidate. Polls which are sponsored by one party have their results adjusted slightly away from that party and they are given much less weight in the average. For generic ballot polls, this is the only adjustment performed.</p> <h3>National Environment Adjustment</h3> <p>Polls are snapshots of the political mood at a point in time. A poll conducted six months ago might produce very different results if it were conducted today, even if it was conducted according to the same methodology on the same population using the same questions. To keep Senate and House district-level polling relevant, each state- and district-level poll's result is adjusted by the amount by which the generic ballot average has shifted since the poll was conducted. For example, if a Senate poll conducted six months ago showed a tie, but the generic ballot average has shifted six points more Democratic since then, the Senate poll would be adjusted to be six points more Democratic as well.</p>
### Poll Weighting Factors  
| Factor  | High weight  | Low weight  |  
| --- | --- | --- |  
| Methodology  | True random sampling, probability panes  | Opt-in/non-probability panel  |  
| Pollster sponsorship  | Independent poll conducted for a nonpartisan media organization or university  | Poll conducted on behalf of a candidate or party  |  
| Population  | Likely Voters (LV)  | Registered Voters (RV)  |  
| Recency  | Poll conducted in the past few days  | >Polls older than 90 days old  |  
| Sample size  | N > 1,000  | N < 300  |  
| Time in field  | Poll conducted over several days  | Poll in the field for only one day  |  
## MCMC Simulation
<p>The final prediction is not a point estimate but a full probability distribution. Stan samples thousands of values from the posterior predictive distribution for each seat, capturing correlations across seats (e.g., a strong Democratic wave affects all seats simultaneously).</p> <p>From these draws, this dashboard calculates:</p> <div class="formula-block"><pre>r_prob = mean(draw &gt; 0.5) // Win probability r2p_avg = mean(draw) // Expected r2p r2p_p05 = quantile(draw, 0.05) // 5th percentile r2p_p95 = quantile(draw, 0.95) // 95th percentile </pre></div> <p>The massive raw posterior file (<code>house_district_posterior.csv</code>, ~124MB) is processed daily by the <code>update_data.py</code> worker script, which compresses thousands of rows per district into these five summary statistics and writes a lightweight JSON file for the dashboard to serve.</p>
## Aggregation
<p>For each House and Senate race, the model produces at least a posterior distribution based on national swing as well as (potentially) a posterior distribution based on race-specific polling. These are averaged using <strong class="highlight">inverse-variance weights</strong>, which is to say:</p> <div class="formula-block"><pre>pred = (national_swing_pred/national_swing_var + poll_pred/poll_var) / (1/national_swing_var + 1/poll_var) If var_poll → ∞ (no polls exist): pred → fund_pred If var_poll → 0 (many perfect polls): pred → poll_pred </pre></div> <p>These weights are known to minimize the variance of the final prediction and are also consistent with Bayesian updating of a normal prior with normally distributed data.</p> <div class="callout"><div class="callout-icon">ℹ️</div><p>This means the model gracefully handles the full spectrum from well-polled competitive races (where polls dominate) to deeply red or blue seats with no polling (where the model prediction based on national swing dominates). </p></div>
## Data Sources  
| Source  | Used For  | Update Frequency  |  
| --- | --- | --- |  
| MIT Election Lab (1976–2024)  | Historical district-level results and baselines  | Static  |  
| Daily Kos Elections  | Presidential vote margins in historical congressional districts  | Static  |  
| New York Times Poll Tracking Project  | Generic ballot + district/state polls  | Daily  |  
| Ballotpedia  | Incumbency and candidate filings  | Periodic  |  
| GitHub (thisismactan/US-2026)  | Forecast outputs used by this dashboard  | Daily  |  
## Limitations & Caveats
<p>All forecasts are probabilistic estimates, not predictions. A race with a 90% probability of one candidate winning is <em>not</em> a certainty — it means the model would expect the favored candidate to win 9 out of 10 times under similar conditions. Out of every 10 races where the leading candidate has a 90% probability of winning, it should not be a surprise when the underdog wins one. </p> <p>Key limitations include the following: <br /> - The model does not direct take into account things that happen in the news, like scandal or economic shocks. The forecast will reflect these things only to the extent that those news events are reflected in the polls.<br /> - Polling in low-salience House races is sparse and often of poor quality: typically the only polls of a House race will be those conducted for one of the campaigns which the campaign decides to release. As you might imagine, this can lead to significant selection bias in what House polls we see.<br /> - The model does not account for third-party and independent candidates who could tip results in close races. For the most part the impact of these candidates is limited, but in some races they may have a large impact or may even be running as the de facto Democratic nominee (see Nebraska's Senate election).</p> <p>This dashboard is a visualization layer on top of publicly available research. The underlying model code is open-source and available at <a href="https://github.com/thisismactan/US-2026">github.com/thisismactan/US-2026</a>.</p>

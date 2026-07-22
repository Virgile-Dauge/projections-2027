---
title: Swingometrics | Methodology | Swingometer
id: swingometrics-methodology-swingometer
tags:
- projections-electorales-bureaux-2027-b0b1c4
- swing-methods
- mrp
- uk-elections
- uncertainty-quantification
created: '2026-07-21T18:29:00.839009Z'
updated: '2026-07-21T18:39:17.634332Z'
source: https://swingometer.co.uk/swingometrics
source_domain: swingometer.co.uk
fetched_at: '2026-07-21T18:29:00.804393Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Swingometer.co.uk methodology page for a UK general-election forecasting
  site: poll aggregation weights each poll by recency (exponential decay, ~14.7-day/2-week
  half-life), sample size (sqrt scaling, diminishing returns), and calibrated ''house
  effects'' (pollster bias learned from historical error, coefficients kept proprietary).
  Constituency-level projection uses a modified Uniform National Swing with per-region,
  per-party multiplicative adjustment factors (e.g. amplified Labour swing in London,
  distinct SNP dynamics in Scotland, divergent Red Wall behavior) rather than plain
  UNS; explicitly rejects full MRP as requiring ''extensive demographic modeling and
  granular survey data'' in favour of the UNS-with-regional-adjustments tradeoff between
  accuracy and transparency. Runs 10,000 Monte Carlo simulations sampling from a multivariate
  normal over national vote shares (Conservative-Labour covariance modeled at approx.
  -0.5) plus ~2% additional per-constituency local variance for candidate/tactical-voting
  effects. Quantifies its total forecast uncertainty budget as ~4-6 points, decomposed
  into sampling error (~2%), house effects (~1-2%), late swing (~2-3%, irreducible),
  turnout variation (~1-2%) and tactical voting (~1-3%). Backtested against UK elections
  2015, 2017, 2019, 2024: seat-prediction MAE 19.7, largest-party call correct 4/4,
  majority call correct 3/4, 95% CI coverage 100% (4/4) but 80% CI coverage only 50%
  (2/4) -- i.e. its 80% intervals were too narrow (overconfident) in this small backtest.
  Also incorporates decaying ''international signal'' adjustments from foreign (180-day
  half-life) and local (90-day half-life) elections as small perturbations to poll
  averages. States known limitations: new 2024 constituency boundaries limit historical
  backtesting data, simplified tactical-voting model, and no ability to predict ''black
  swan'' scandal/crisis shocks.'
---

[Forecast](https://swingometer.co.uk/) [Map](https://swingometer.co.uk/map.html) [Polls](https://swingometer.co.uk/polltracker.html) [Scenarios](https://swingometer.co.uk/scenarios.html) [Backtesting](https://swingometer.co.uk/backtesting.html) [Swingometrics](https://swingometer.co.uk/swingometrics.html)
Methodology 
#  Swingometrics 
A deep dive into how we forecast UK elections. Transparent methodology, honest uncertainty, and the mathematics behind our predictions. 
##  Overview 
Swingometer uses a multi-stage probabilistic forecasting pipeline to predict UK general election outcomes. Our approach combines poll aggregation, swing modeling, and Monte Carlo simulation to produce seat projections with properly quantified uncertainty. 
### The Pipeline
Raw Polls → Aggregation → Swing Model → Simulation
Unlike simple poll averages, we account for pollster methodology differences ("house effects"), weight by sample size and recency, and propagate uncertainty through every stage of the model. 
##  Poll Aggregation 
Individual polls are noisy. Different pollsters use different methodologies and have systematic biases. Our aggregation model addresses both issues. 
### Weighted Average
For each party p at time t, the aggregated vote share is:
V̂p,t = Σ(wi × (Vp,i - hp,pollster)) / Σwi
#### Recency Weight
Exponential decay with ~15-day half-life
`w = 2^(-days/14.7)`
#### Sample Weight
Square root scaling (diminishing returns)
`w = √(n/1000)`
#### House Effects
Learned from historical errors
`hp = calibrated`
####  What We Don't Publish 
Exact house effect coefficients are not published. This prevents pollsters from gaming our model and maintains the integrity of our adjustments. The methodology is transparent; the specific calibrations are proprietary. 
##  Swing Calculation 
To translate national polling into constituency-level predictions, we use a modified Uniform National Swing (UNS) model with regional adjustments. 
swing_model.py

```
# Base UNS model
swing = current_national - previous_national

# Apply regional adjustment
regional_swing = swing × regional_factor[region][party]

# Project constituency result
new_share = previous_share + regional_swing
```

Regional factors capture systematic differences in how national swings play out locally. London typically sees amplified Labour swings; Scotland has unique SNP dynamics; the "Red Wall" areas may swing differently than traditional Labour heartlands. 
#### Why Not MRP?
Multilevel Regression with Poststratification (MRP) is powerful but requires extensive demographic modeling and granular survey data. Our UNS-with-adjustments approach provides a good balance of accuracy and transparency. Future versions may incorporate MRP elements. 
##  Monte Carlo Simulation 
Rather than producing a single "best guess," we run 10,000 simulated elections. Each simulation samples from our uncertainty distributions, producing a range of plausible outcomes. 
simulation.py

```
for sim in range(10_000):
    # Sample national vote with polling uncertainty
    national = sample_multivariate_normal(
        mean=aggregated_polls,
        cov=correlation_matrix
    )

    # For each constituency
    for seat in constituencies:
        # Add local variance
        local = national + random_normal(0, σ_local)
        projected = apply_swing(seat.previous, local)
        winner = argmax(projected)

    # Count total seats
    results.append(count_seats())
```

#### Correlation Structure
Conservative and Labour vote shares are negatively correlated (~-0.5). When one rises, the other typically falls. We model this covariance structure. 
#### Local Variance
Each constituency has ~2% additional uncertainty beyond national swing, capturing local candidate effects, tactical voting, and constituency-specific factors. 
From these 10,000 simulations, we extract summary statistics: mean seats, confidence intervals, and outcome probabilities. An 89% probability of Labour majority means Labour wins 326+ seats in 8,900 of our 10,000 simulations. 
##  Quantifying Uncertainty 
Honest uncertainty quantification is central to our approach. We prefer calibrated probabilities to false precision.   
| Source  | Magnitude  | Reducible?  |  
| --- | --- | --- |  
| Sampling Error  | ~2%  | Partially (more polls)  |  
| House Effects  | ~1-2%  | Partially (historical data)  |  
| Late Swing  | ~2-3%  | No  |  
| Turnout Variation  | ~1-2%  | Partially  |  
| Tactical Voting  | ~1-3%  | Partially  |  
| Total Uncertainty  | ~4-6%  | —  |  
#### Calibration Goal
A well-calibrated model means events we give 80% probability should happen approximately 80% of the time. We'd rather be honestly uncertain than confidently wrong. 
##  International Signals 
Foreign election results can provide weak signals about UK political dynamics. We incorporate these with appropriate skepticism. 
🇺🇸
#### US Elections
"Special relationship" sentiment effects. Democratic wins may boost Labour perception; Republican wins may energize right-wing movements. 
🇪🇺
#### EU Elections
Proxy for European populism trends. Strong showing for far-right parties across Europe may correlate with Reform UK support. 
#### Signal Decay
International signals lose relevance over time:
Signal weight = α × 2^(-t / 180 days) 
Half-life of 6 months. After 1 year, signal strength is ~25% of original.
##  Live Signal Effects 
See how foreign and local election signals adjust our poll aggregation in real-time. These adjustments are small but help capture political momentum that polls may lag in reflecting. 
### Signal Breakdown by Party
How each signal type adjusts poll averages (percentage points)  
| Party  | Polls Only  | + Foreign  | + Local  | = Final  |  
| --- | --- | --- | --- | --- |  
|  Reform  | 25.2%  | —  | -1.22  | 24.2%  |  
|  Conservative  | 19.6%  | —  | +0.07  | 19.9%  |  
|  Labour  | 20.7%  | —  | +0.26  | 21.2%  |  
|  Lib Dems  | 11.7%  | —  | -0.74  | 11.1%  |  
|  Green  | 13.4%  | —  | -0.46  | 13.1%  |  
### Polls Only vs With Signals
REF
Polls: 25.2%
Final: 24.2%
-1.22
CON
Polls: 19.6%
Final: 19.9%
+0.08
LAB
Polls: 20.7%
Final: 21.2%
+0.27
LD
Polls: 11.7%
Final: 11.1%
-0.74
GRN
Polls: 13.4%
Final: 13.1%
-0.45
Polls Only
With Signals
### Signal Decay Over Time
Signals lose relevance over time. Foreign elections have a 180-day half-life; local elections have a 90-day half-life. 
50d100d150d200d250d300d350d20%40%60%80%100%180d90d
Foreign (180-day half-life)
Local (90-day half-life)
##  Backtesting 
We validate our model by testing against historical elections. Using only data available before each election, we generate predictions and compare to actual results.   
| Metric  | Target  | Backtest Result  |  
| --- | --- | --- |  
| 95% CI Coverage  | 95%  | 100% (4/4)  |  
| 80% CI Coverage  | 80%  | 50% (2/4)  |  
| Seat Prediction MAE  | <20  | 19.7  |  
| Largest Party Accuracy  | 90%+  | 100% (4/4)  |  
| Majority Call Accuracy  | —  | 75% (3/4)  |  
#### Historical Elections Tested
2024 LAB 412 2019 CON 365 2017 CON 317 2015 CON 331
##  Known Limitations 
#### New Constituency Boundaries
The 2024 election used new boundaries, limiting historical data. We use notional results but these add uncertainty. 
#### Tactical Voting
Our simplified tactical voting model may miss nuanced local dynamics, especially in three-way marginal seats. 
#### Black Swan Events
Models assume continuity. Major unexpected events (scandals, crises) are not predictable and can invalidate forecasts. 

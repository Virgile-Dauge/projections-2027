---
title: Harvard Data Science Review • Issue 2.4, Fall 2020
id: harvard-data-science-review-issue-24-fall-2020
tags:
- projections-electorales-bureaux-2027-b0b1c4
- electoral-forecasting
- bayesian-model
- polling-bias
created: '2026-07-21T18:28:52.275429Z'
updated: '2026-07-21T18:39:17.631554Z'
source: https://sites.stat.columbia.edu/gelman/research/published/Harvard_Data_Science_Review.pdf
source_domain: sites.stat.columbia.edu
fetched_at: '2026-07-21T18:28:52.275144Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Heidemanns, Gelman & Morris (Harvard Data Science Review, oct. 2020) : description
  formelle et publiée (peer-reviewed) du modèle Economist 2020, complément académique
  du dépôt GitHub. Combine deux prédictions par pooling partiel : (1) un modèle ''fondamentals''
  (Time-for-Change d''Abramowitz augmenté d''un terme d''interaction croissance économique
  x part d''électeurs swing selon l''American National Election Study, pour capter
  l''affaiblissement de l''effet économique dans un électorat polarisé) qui fixe le
  prior sur mu_b au jour de l''élection ; (2) une marche aléatoire corrélée entre
  États pour les tendances d''opinion state-level, où la matrice de corrélation Sigma
  est estimée à partir des résultats électoraux passés et de variables comme le niveau
  d''éducation, les éléments hors-diagonale négatifs étant mis à zéro puis la matrice
  rééchelonnée. Concept clé : quand un État n''est pas sondé (ex. Oregon), sa tendance
  suit celle d''un État corrélé sondé (ex. Washington) avec une incertitude ajoutée.
  Détaille aussi les termes de biais : effets ''maison'' (pollster), effets de population
  sondée (likely/registered voters), effets de mode d''enquête (téléphone/en ligne),
  et surtout un terme d''ajustement pour la non-réponse partisane différentielle (processus
  autorégressif, corrélation rho ~ Normal(0.7, 0.1)) introduit après l''échec de 2016
  où les sondages des États du Midwest n''ajustaient pas pour la composition partisane
  de leur échantillon — erreur documentée comme cause principale de la sous-estimation
  de Trump en 2016 (référence Gelman & Azari 2017, ''The mythical swing voter'' de
  Gelman/Goel/Rivers/Rothschild 2016, et Shirani-Mehr et al. 2018 sur le biais vs
  variance des sondages électoraux). Les auteurs reconnaissent explicitement des limites
  : hyperparamètres et prévisions fondamentals non divulgués car propriétaires à The
  Economist ; le modèle ne traite pas les tiers partis ; incertitude de mesure non
  identifiable par construction ; le modèle a corrigé pour 2020 des bugs et choix
  de modélisation ''questionnables'' découverts après la mise en production initiale
  de juin 2020 — aveu rare de fragilité méthodologique documentée publiquement.'
raw_file: raw/harvard-data-science-review-issue-24-fall-2020.pdf
---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic
Bayesian Forecasting
Model for the US
Presidential Election
Merlin Heidemanns1 Andrew Gelman1 G. Elliott Morris2
1Department of Statistics and Department of Political Science, Columbia University, New York,
New York, United States of America,
2The Economist, The Economist Group, District of Columbia, United States of America
Published on: Oct 27, 2020
DOI: https://doi.org/10.1162/99608f92.fc62f1e1
License: Creative Commons Attribution 4.0 International License (CC-BY 4.0)


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
2
ABSTRACT
During modern general election cycles, information to forecast the electoral outcome is plentiful. So-called 
fundamentals like economic growth provide information early in the cycle. Trial-heat polls become informative 
closer to Election Day. Our model builds on (Linzer, 2013) and is implemented in Stan (Team, 2020). We 
improve on the estimation of state-level trends, the internal consistency of different predictions at the state and 
national level, and provide an adjustment for differential nonresponse bias across the cycle. The model forecast 
a Democratic win with probability in the 80–90% range during most of the 2020 U.S. presidential election 
campaign, conditional on the two major candidates staying in the race, no major third-party challenges, and no 
unprecedented challenges with turnout or vote counting.
Keywords: poll aggregation, election, forecasting, fundamentals, Bayesian
Media Summary
We forecast vote intentions for Election Day by combining fundamentals and trial-heat polls. Fundamentals 
such as economic growth and presidential approval are highly predictive early in the electoral cycle. Trial-heat 
polls become more predictive as we approach Election Day. Our model focuses on the internal consistency of 
predictions at different levels, e.g., how likely is a win in a particular state if the candidate leads with a certain 
margin at the national level. Our model also includes an adjustment for differential nonresponse of Democratic 
and Republican voters to correct for polling artifacts that in 2016 led to short-term shifts in poll numbers as 
more or fewer partisan supporters participated throughout the cycle. The model forecast a Democratic win with 
probability in the 80–90% range during most of the 2020 U.S. presidential election campaign, conditional on 
the two major candidates staying in the race, no major third-party challenges, and no unprecedented challenges 
with turnout or vote counting.
1. Introduction
We constructed an election forecasting model for The Economist that builds on Linzer’s (2013) dynamic 
Bayesian forecasting model and provides an election day forecast by partially pooling two separate predictions: 
(1) a forecast based on historically relevant economic and political factors such as personal income growth, 
presidential approval, and incumbency; and (2) information from state and national polls during the election 
season. The two sources of information are combined using a time-series model for state and national opinion. 
Our model also accounts for some aspects of non-sampling errors in polling. The model is fit using the open-
source statistics packages R and Stan (R Core Team, 2020; Stan Development Team, 2020) and is updated 
every day with new polls. The forecast is available and is conveyed with several dynamic graphics displaying 
data and predictions of electoral and popular votes at the national and state level. See also: a description of the 


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
3
model-building process and all code. This paper provides a more formal description of our statistical model 
than is available elsewhere. While more thorough, the model code posted on the GitHub page should be seen 
as the authoritative source of how the model works, following the principle that ‘code never lies.’ We also 
describe how our model builds on the existing literature surrounding Bayesian election forecasts, namely in 
accounting for political polarization and differential partisan nonresponse in the polls.
2. Polls
We include polls at the national and state level and take each poll to be an estimate of that day’s average 
support for the Democratic and Republican candidates for president (ignoring respondents who express no 
opinion or support other candidates), with modeled bias and variance. Our goal is to estimate national and state-
level trends in support for the candidates. We start by considering how we model individual polls before 
discussing how individual components are modeled.
For each poll  the number of respondents indicating their support for the Democratic candidate is given by 
 
with 
 being the total number of respondents supporting one of the major party candidates. We start with the 
binomial sampling model: 
We model 
 conditional on whether poll  is at the state or national level. We model state polls in state 
 at 
time 
 as 
and national polls as 
In our notation, we are using superscripts as names and subscripts as indexes; for example, in the expression, 
, the parameter is named 
 and it is indexed by state  and date .
The most important term in the above formulas is 
, which represents the underlying support for the 
Democrat in state  at time . For national polls, these are summed over the 
 states (including 
Washington, D.C.) with weights 
 that sum to 1 and which are proportional to the number of votes in the state 
in the previous election. Our model does not account for third parties and would need to be expanded to apply 
to an election with large third-party vote shares.
The other terms in the above model, 
, represent different sources of bias arising from the well known fact 
that opinion polls are not actually random samples of the voting population: Such a feat would be impossible 
given high nonresponse rates of modern surveys.
i
yi
ni
y ∼
i
Binomial(θ , n ).
i
i
θi
i
s[i]
t[i]
θ =
i
logit
(μ
+
−1
s[i],t[i]
b
α +
i
ζ
+
i
state
ξ
)
s[i]
θ =
i
logit
(
w μ
+
−1
∑s=1
S
s
s,t[i]
b
α +
i
ζ
+
i
national
w ξ ).
∑s=1
S
s s
μs,t
b
μb
s
t
μs,t
b
s
t
S = 51
ws
α,ζ,ξ


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
4
We expand the shared bias term in the state and national poll models as, 
including house effects 
, polling population effects 
, polling mode effects 
, an adjustment trend term for 
nonresponse bias  and an indicator  equal to 1 if the pollster does not adjust for partisanship and 0 otherwise, 
measurement error , and state-level error .
In the following, we cannot disclose most of the specific information on the hyperparameters, as well as the 
fundamentals-based forecast, as these are proprietary to The Economist. Hyperparameter choices for past 
election cycles can be gleaned from the code provided in the GitHub repository for those elections.
2.1. State-level trends
We share information across states contemporaneously and over time. We accomplish this by treating the 
development of state-level public opinion as a correlated random walk for which we have prior information 
from the fundamentals-based prediction at 
 (Election Day).
The random walk component connects days for which we have polls and interpolates for days without polls in 
between. Our uncertainty for days without data is a function of our encoded prior model of how much public 
opinion can change from day to day as well as the polling data from other states. We cross-validated this value 
on the 2008, 2012, and 2016 elections and the first months of 2020.
The correlation in the random walk imposes our assumption on the estimates that in the absence of data similar 
states will move in similar ways, i.e., if we have polls for Washington but not for Oregon, then the daily trend 
for Oregon will look similar to the trend in Washington with added uncertainty. We set the details of this 
correlation matrix so as to obtain reasonable results for national and state-level swings. We estimated the 
correlation matrix  from past election results and other relevant state-level predictors such as education. We 
set off-diagonal elements smaller than zero to zero and then scale the matrix to achieve the desired degree of 
day-to-day change.
Then, the process takes the form 
where 
 is the estimate from the fundamentals model.
2.2. House, population, and mode effects
We include adjustment terms for pollsters, polled population (e.g. likely voters and registered voters), and 
polling mode (e.g. live caller or online). We know that pollsters can favor either party, and that the same 
applies to the polled population and how the populations are being polled. Our priors for the parameters are 
centered at 0 with different standard deviations:1 
α =
i
μ
+
p[i]
c
μ
+
r[i]
r
μ
+
m[i]
m
zϵ
,
t[i]
μc
μr
μm
ϵ
z
ζ
ξ
t = T
Σ
μ ∣μ
t
b
t−1
b
∼MVN (μ
, Σ ),
t−1
b
b
μT
b


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
5
This implies that we are estimating the deviation given this year’s polling data, thus not using potential 
information about the quality of the pollsters or the reliability of likely voter adjustments from past data, out of 
concern that these may not provide reliable indications for the current election.
2.3. Partisan nonresponse adjustment term
Poll-aggregation election forecasts performed poorly in 2016, a problem that can be attributed to polls in key 
midwestern states that did not appropriately adjust for nonresponse (Gelman & Azari, 2017). This adjustment 
is represented by an autoregressive process to allow the party adjustment to vary over time at the national level; 
see Gelman et al. (2016). If a pollster does not adjust for the partisan composition of their sample, shifts in 
support can reflect a changing sample composition. We rely on the difference between adjusting and non-
adjusting polls to estimate the extent to which non-adjusting polls are biased: 
2.4. Measurement error
We add additional uncertainty to each poll where the scale varies based on whether it is a state or a national 
poll. These terms are unidentifiable, i.e., given 
 polls, there are 
 independently and identically distributed 
terms, but we adjust our uncertainty in the poll estimates, for example for poll specific design effects or 
deviations from truly random samples. That is, we assume 
2.5. Correlated state errors
We include state and national level polling error terms, which allows for unmodeled measurement error for 
each poll beyond the stated margin of error (Shirani-Mehr et al., 2018). We treat state level polling error terms 
as correlated across states with a scaled version of the same correlation matrix we use for changes in 
underlying opinions across states: 
μc
μr
μm
∼Normal(0, σ )
c
∼Normal(0, σ )
r
∼Normal(0, σ ).
m
ξ ∣ρ, σ
1
ξ
ξ ∣ξ
, ρ, σ
t
t−1
ξ
ρ
∼Normal
0,
σ
(
1 −ρ2
1
ξ)
∼Normal ρξ
, σ
 for t = 2, … , T
(
t−1
ξ)
∼Nnormal 0.7, 0.1 .
(
)
N
N
ζi
national
ζi
state
∼Normal(0, σ
)
national
∼Normal(0, σ
).
state


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
6
Furthermore, we consider the same relationship as with 
 for the national polls where we include the 
weighted sum of the state-level error term as the national level error. The weights again are the forecast state-
level shares, and for these we simply have used voter turnout in the previous presidential election.
3. Fundamentals
The fundamentals-based model combines the previous electoral outcome with economic and political factors, 
based on the “time for change” model of Abramowitz (2008), but we add an interaction term between 
economic growth and the share of swing voters in the electorate, as measured by the American National 
Election Study, to allow for dampening effects of economics in polarized elections. We predict the incumbent 
vote share by state in previous elections using a regularized linear model and predict the incumbent vote share 
in 2020 with the parameter estimates. We set the prior for 
 on Election Day to the fundamentals-based 
prediction.
4. Putting the Pieces Together
We combine the two forecasts by using the fundamentals-based prediction as the prior for Election Day. The 
random walk prior on 
 can be visualized as going backward in time from Election Day to the current day of 
polling. Thus, the model updates the prior for Election Day by the poll-based forecast for Election Day. Figure 
1 shows the model fit for 2016. As with other forecasts, our model overstates the strength of Hillary Clinton in 
key midwestern states (see Michigan in the graph) because of failures in the state polls, but its hierarchical 
model with multiple error terms allows the model to avoid the over-certainty that could arise from simple poll 
averaging.
The current prediction for 2020 can be found on the website of The Economist.
ξ ∼MVN(0, Σ ).
ξ
μb
μb
μb


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
7
5. Calibration, Uncertainty, and What Is Forecast
The model estimates a large number of parameters with a relatively small number of polls. To estimate the 
parameters, we must supply relevant prior information. These pertain to our chosen priors, the predictors in the 
fundamentals-based forecast, and the construction of the covariance matrix that shares information across 
states. Model results are thus sensitive to these choices. In making these choices, we want to avoid unwarranted 
precision (e.g., a prediction that Biden will win Florida and with 95% probability that his share is between 51% 
to 52%) and unwarranted uncertainty (e.g., Biden’s share will be between 40% and 60% with 95% probability). 
As part of the Bayesian workflow, we started with values that we deemed reasonable a priori such as a 3% 
polling error for each poll based on historical data, but also evaluated the model output to determine whether 
the model gave sensible results. For example, based on our knowledge of the electorate in Florida, believing 
that the Republican candidate could win the state with 60% of the vote would be deemed unreasonable given 
increased partisanship and its status as a swing state.
Figure 1. Some summaries of the model, as fit retrospectively to using state and 
national polls from 2016. These graphs illustrate that our data and model are fitting national 
as well as separate state trends,


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
8
We model vote intentions rather than the electoral outcome. Our prediction for the Electoral College translates 
directly from our forecast vote intentions, i.e., winning Maine in 70 out of 100 simulations on average. We for 
example do not consider the effect of COVID-19 on turnout or absentee ballot rejection rates that might 
differentially penalize the Democratic candidate.
Finally, there will always be the potential for further checking and improvement of the model. In the four 
months between the initial release of our model in June, 2020, and the time of this writing, we have discovered 
or have been informed of several questionable predictions from our model as revealed in its fit to the current 
and previous elections, leading us back to our code, where we discovered some bugs and questionable 
modeling choices. One advantage of openness—our code is available on Github, updated predictions appear on 
The Economist site every day, and we have had several free-flowing discussions on our blog (examples one and 
two)—is that we have engaged a broad community of active readers who have helped us poke at our 
predictions in many different ways. The model described in the present article should be thought of not as a 
final product but rather as a step along a continuing path. Gelman et al. (2020) provide further discussion of the 
choices we and others have made in modeling and communicating election forecasts.
6. Conclusion
Forecasting an election is complex and can be framed as even more so in an unfamiliar environment. 
Potentially widespread absentee voting may change both turnout as well as the share of the population whose 
votes are counted. Economic shocks usually reflect negatively on the incumbent but may not if induced due to 
a global pandemic. Pollsters may be more actively partisan than they were in previous elections. Overall, our 
model accounts for a variety of factors and treads carefully when it comes to choosing between overconfidence 
and expressed helplessness due to the plethora of unfamiliar events. That is, we focus on the factors we can 
credibly model but also believe that this election, at least with respect to modeling vote intentions, is not 
fundamentally different from the previous elections we used to calibrate it.
Disclosure Statement
Merlin Heidemanns, Andrew Gelman, and G. Elliott Morris have no financial or non-financial disclosures to 
share for this article.
References
Abramowitz, A. I. (2008). Forecasting the 2008 presidential election with the time-for-change model. PS: 
Political Science & Politics, 41(4), 691–695. https://doi.org/10.1017/S1049096508081249
Gelman, A., & Azari, J. (2017). 19 things we learned from the 2016 election (with discussion). Statistics and 
Public Policy, 4(1), 1–10. http://dx.doi.org/10.1080/2330443X.2017.1356775


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
9
Gelman, A., Goel, S., Rivers, D., & Rothschild, D. (2016). The mythical swing voter. Quarterly Journal of 
Political Science, 11(1), 103–130. http://doi.org/10.1561/100.00015031
Gelman, A., Hullman, J., Wlezien, C., & Morris, G. E. (2020). Information, incentives, and goals in election 
forecasts. Judgment and Decision Making, 15(5), 863–880.
Linzer, D. A. (2013). Dynamic Bayesian forecasting of presidential elections in the states. Journal of the 
American Statistical Association, 108(501), 124–134. https://doi.org/10.1080/01621459.2012.737735
R Core Team. (2020). R: A language and environment for statistical computing. R Foundation for Statistical 
Computing. https://www.R-project.org/
Shirani-Mehr, H., Rothschild, D., Goel, S., & Gelman, A. (2018). Disentangling bias and variance in election 
polls. Journal of the American Statistical Association, 113(522), 607–614. 
https://doi.org/10.1080/01621459.2018.1448823
Stan Development Team. (2020). Stan modeling language. http://mc-stan.org/
©2021 Merlin Heidemanns, Andrew Gelman, and G. Elliott Morris. This article is licensed under a Creative 
Commons Attribution (CC BY 4.0) International license, except where otherwise indicated with respect to 
particular material included in the article.
Footnotes
References
1.  We are following the convention of Stan, where the univariate normal distribution is parameterized by its 
mean and standard deviation, and the multivariate normal distribution is parameterized by its mean vector 
and covariance matrix. ↩
Abramowitz, A. I. (2008). Forecasting the 2008 presidential election with the time-for-change model. PS: 
Political Science & Politics, 41, 691–695. ↩
Gelman, A., & Azari, J. (2017). 19 things we learned from the 2016 election (with discussion). Statistics and 
Public Policy, 4, 1–10. ↩
Gelman, A., Goel, S., Rivers, D., & Rothschild, D. (2016). The mythical swing voter. Quarterly Journal of 
Political Science, 11, 103–130. ↩
Gelman, A., Hullman, J., Wlezien, C., & Morris, G. E. (2020). Information, incentives, and goals in election 
forecasts. Judgment and Decision Making, 15, 863–880. ↩
Linzer, D. A. (2013). Dynamic Bayesian forecasting of presidential elections in the states. Journal of the 
American Statistical Association, 108, 124–134. ↩


---

Harvard Data Science Review • Issue 2.4, Fall 2020
An Updated Dynamic Bayesian Forecasting Model for the US Presidential Election
10
Shirani-Mehr, H., Rothschild, D., Goel, S., & Gelman, A. (2018). Disentangling bias and variance in 
election polls. Journal of the American Statistical Association, 113, 607–614. ↩
Team, R. C. (2020). R: A language and environment for statistical computing. R Foundation for Statistical 
Computing. https://www.R-project.org/ ↩
Team, S. D. (2020). Stan modeling language. http://mc-stan.org/ ↩

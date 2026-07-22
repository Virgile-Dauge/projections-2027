---
title: Dynamic Bayesian Forecasting of Presidential
id: dynamic-bayesian-forecasting-of-presidential
tags:
- projections-electorales-bureaux-2027-b0b1c4
- electoral-forecasting
- bayesian-model
- mrp
created: '2026-07-21T18:28:48.201826Z'
updated: '2026-07-21T18:39:17.628511Z'
source: https://votamatic.org/wp-content/uploads/2013/07/Linzer-JASA13.pdf
source_domain: votamatic.org
fetched_at: '2026-07-21T18:28:48.201544Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Linzer (JASA 2013), papier fondateur du modèle ''Votamatic'' qui a inspiré
  les modèles Bayésiens électoraux modernes (Economist, ex-538). Combine un modèle
  structurel historique (fondamentaux macro : croissance PIB, popularité présidentielle)
  donnant un prior par État hi, avec les sondages state-level agrégés en temps réel
  via un modèle hiérarchique dynamique. Spécification : pi_ij = logit^-1(beta_ij +
  delta_j), où beta_ij capture la tendance long terme propre à l''État et delta_j
  l''effet national de court terme (convention, actualité) commun à tous les États
  — separation clé qui permet de ''borrow strength'' entre États peu sondés en empruntant
  l''info aux autres États via la corrélation nationale delta_j. Prior sur beta_iJ
  (jour J = élection) ~ Normal(logit(hi), s_i^2), précision tau_i choisie par l''analyste
  (sensibilité testée : tau_i ne doit pas dépasser 20 sous peine d''intervalles crédibles
  trop étroits). Random-walk inversé ancré au jour de l''élection relie les jours
  sans sondage. Appliqué à 2008 : MAD final de 1.4% par État, un seul État mal prédit
  (Indiana) sur 50, fourchette de votes électoraux 338-387 (réel: 365) contre un intervalle
  bien plus large (250-450) chez le modèle concurrent Lock & Gelman (2010) qui n''utilisait
  qu''une seule vague de sondages. Limite explicite reconnue par l''auteur : le modèle
  reste peu fiable plusieurs mois avant l''élection car les sondages précoces sont
  bruités par nature, pas seulement rares ; l''essentiel du gain de précision se concentre
  sur le dernier mois-deux avant le scrutin. Directement transposable à la problématique
  française comme référence méthodologique pour un modèle bayésien combinant plusieurs
  strates de données passées (fondamentaux + scrutins antérieurs) avec des priors
  state/circonscription-level, mais nécessiterait un fort volume de sondages infranationaux,
  largement absent en France au niveau bureau de vote.'
raw_file: raw/dynamic-bayesian-forecasting-of-presidential.pdf
---

Dynamic Bayesian Forecasting of Presidential
Elections in the States
Drew A. LINZER
I present a dynamic Bayesian forecasting model that enables early and accurate prediction of U.S. presidential election outcomes at the
state level. The method systematically combines information from historical forecasting models in real time with results from the large
number of state-level opinion surveys that are released publicly during the campaign. The result is a set of forecasts that are initially as good
as the historical model, and then gradually increase in accuracy as Election Day nears. I employ a hierarchical speciﬁcation to overcome
the limitation that not every state is polled on every day, allowing the model to borrow strength both across states and, through the use of
random-walk priors, across time. The model also ﬁlters away day-to-day variation in the polls due to sampling error and national campaign
effects, which enables daily tracking of voter preferences toward the presidential candidates at the state and national levels. Simulation
techniques are used to estimate the candidates’ probability of winning each state and, consequently, a majority of votes in the Electoral
College. I apply the model to preelection polls from the 2008 presidential campaign and demonstrate that the victory of Barack Obama was
never realistically in doubt.
KEY WORDS:
Politics; Polls; Public opinion; Voting.
1. INTRODUCTION
Every four years, American political pundits and analysts
spend endless hours dissecting the presidential election cam-
paign and trying to forecast the winner. These efforts increas-
ingly rely upon the interpretation of quantitative historical data
and the results of preelection (or trial-heat) public opinion polls
asking voters their preferred candidate for president. The 2008
presidential campaign in particular witnessed a remarkable in-
crease in the number of preelection polls conducted at the state
level, where presidential elections are ultimately decided. By
Election Day, more than 1700 distinct state-level surveys had
been published by media organizations and private polling ﬁrms,
in every U.S. state, totaling over one million individual inter-
views (Pollster.com 2008). In the most competitive swing states,
new polls were released almost daily as Election Day neared.
The widespread availability of these survey ﬁndings critically
shaped both how the campaign was reported in the news media
and how the presidential candidates were perceived by vot-
ers (Becker 2008; Pew Research Center 2008; Traugott and
Lavrakas 2008).
State-level preelection survey data represent a rich—if ex-
tremely noisy—new source of information for both forecasting
election outcomes and tracking the evolution of voter prefer-
ences during the campaign. Interest in measuring and predict-
ing these outcomes is not limited to those in the media whose
job is to explain campaign trends to the public (Broh 1980;
Stovall and Solomon 1984; Rhee 1996; Rosenstiel 2005). Polit-
ical strategists who make decisions about the allocation of hun-
dreds of millions of dollars worth of advertising and manpower
need to be able to ascertain candidates’ relative positioning in
the electorate, and their potential to carry various states on the
way to winning the presidency (Center for Responsive Politics
2008; Jamieson 2009). In addition, academic researchers have
Drew A. Linzer is Assistant Professor, Department of Political Science,
Emory University, Atlanta, GA 30322 (E-mail: dlinzer@emory.edu). I am grate-
ful to Cliff Carrubba, Tom Clark, Justin Esarey, and Andrew Gelman for feed-
back on earlier versions of this article. Nigel Lo provided helpful research
assistance. A special debt is owed to my colleague Alan Abramowitz, who
could not have been more generous with his time, his insight, and his data.
long been interested in the factors that predict presidential elec-
tion outcomes (e.g., Lewis-Beck and Rice 1992; Campbell and
Garand 2000), the forecasting value of historical models ver-
sus preelection public opinion polls (Brown and Chappell 1999;
Holbrook and DeSart 1999), the earliness with which accurate
forecasts can be made (Gelman and King 1993; Erikson and
Wlezien 1996; Wlezien and Erikson 1996), the dynamics be-
hind public opinion during the campaign (Campbell, Cherry, and
Wink 1992; Erikson and Wlezien 1999; Wlezien and Erikson
2002; Romer et al. 2006; Panagopoulos 2009a), and the ex-
tent to which campaigns affect the eventual result (Shaw 1999;
Hillygus and Jackman 2003; Vavreck 2009). The aim of this
article is to produce quantities of interest to each of these con-
stituencies: state- and national-level estimates of not only the
current preferences of voters at every point in the campaign,
but also forecasts of presidential candidates’ vote shares and
probabilities of victory on Election Day.
I introduce a dynamic Bayesian forecasting model that uniﬁes
the regression-based historical forecasting approach developed
in political science and economics with the poll-tracking capa-
bilities made feasible by the recent upsurge in state-level opin-
ion polling. Existing historical models are designed to predict
presidential candidates’ popular vote shares, at a single point
in time—usually 2–3 months in advance of an election—from
structural “fundamentals” such as levels of economic growth,
changes in unemployment rates, whether the incumbent is run-
ning for reelection, and so forth (e.g., Bartels and Zaller 2001;
Abramowitz 2008; Erikson and Wlezien 2008; Campbell 2008b;
Fair 2009). In line with theories of retrospective voting, voters
tend to punish incumbent party candidates when times are bad,
and reward them when economic and social conditions are more
favorable (Kinder and Kiewiet 1991; Nadeau and Lewis-Beck
2001; Duch and Stevenson 2008).
Although predictions from structural models can be sur-
prisingly accurate, they are also subject to a large amount of
© 2013 American Statistical Association
Journal of the American Statistical Association
March 2013, Vol. 108, No. 501, Applications and Case Studies
DOI: 10.1080/01621459.2012.737735
124


---

Linzer: Dynamic Bayesian Forecasting of Presidential Elections
125
uncertainty. Most historical forecasts are based on data from
just 10 to 15 past elections, and many only generate national-
level estimates of candidates’ vote shares. Unless the funda-
mentals clearly favor one candidate over the other, it is difﬁcult
for structural models to conﬁdently predict the election win-
ner. Moreover, in the event that an early forecast is in error,
structural models contain no mechanism for updating predic-
tions once new information becomes available closer to Elec-
tion Day. In 2008, for example, Democrat Barack Obama won
the presidency with 53.7% of the major-party vote—a sizeable
margin, by historical standards. Yet many published forecasts
were unsure of an Obama victory. Two months before the elec-
tion, Erikson and Wlezien (2008) gave Obama a 72% chance
of winning. Lewis-Beck and Tien (2008) judged the race to be
a toss-up. Campbell (2008b) predicted that Republican John
McCain would win, with 83% probability. In closer elections,
the problem is ampliﬁed: political scientists completely failed
to predict the victory of Republican George W. Bush in 2000
(Campbell 2001).
Preelection polls provide contextual information that can be
used to correct potential errors in historical forecasts, increas-
ing both their accuracy and their precision. Polls conducted just
before an election generate estimates that are very close to the
eventual result, on average (Traugott 2001, 2005; Pickup and
Johnston 2008; Panagopoulos 2009b). Earlier in the campaign,
polls are less effective for forecasting (e.g., Campbell and Wink
1990; Gelman and King 1993; Campbell 1996), but remain
useful for detecting trends in voter preferences. Survey-based
opinion tracking presents certain challenges, however. First, not
every state is polled on every day, leading to gaps in the time
series. Data are especially sparse in less-competitive states and
early in the campaign. Second, measured preferences ﬂuctuate
greatly from poll to poll, due to sampling variability and other
sources of error. Such swings have been prone to misinterpre-
tation as representing actual changes in attitudes. Some amount
of multisurvey aggregation and smoothing is therefore neces-
sary to reveal any underlying trends (Erikson and Wlezien 1999;
Jackman 2005; Wlezien and Erikson 2007).
Theintegratedmodelingframeworkthat I describewill enable
researchers to reﬁne and update structural state-level election
forecasts in real time, using the results of every newly available
state-level opinion poll. Older polls that contribute less to the
forecast are used to estimate past trends in state-level opinion.
To handle the uneven spacing of preelection polls, the model
borrows strength hierarchically across both states and days of
the campaign. It also detects and accounts for campaign effects
due to party conventions or major news events that inﬂuence
mass opinion in the short term, but may or may not be related to
the election outcome (Finkel 1993; Holbrook 1994; Shaw 1999;
Wlezien and Erikson 2001).
The result is a set of election forecasts that are produced early
in the campaign and become increasingly accurate as Election
Day nears, yet remain relatively stable over time. Because these
forecasts depend on reported levels of support for each candi-
date in the trial-heat polls, my model also yields daily estimates
of current opinion in each state at any point during the cam-
paign, with associated measures of uncertainty. The model fur-
ther generates logically valid estimates of the probabilities that
either candidate will win each state and the Electoral College
vote as a whole, as a function of the available polling data, the
prior certainty in the predictions of the historical model, and the
proximity to Election Day.
I apply the model to the dual problems of tracking state-level
opinion and forecasting the outcome of the 2008 U.S. presiden-
tial election, using the beneﬁt of hindsight to evaluate model
performance. I simulate the campaign from May 2008 through
Election Day, November 4, updating the model estimates from
each new poll as they are released. Contrary to much of the
media commentary at the time, Obama’s victory was highly
predictable many months in advance of the election.
2. RESEARCH BACKGROUND
Presidential elections in the United States are decided at the
state level, through the institution of the Electoral College.
Within each state, candidates are awarded electoral votes on
a winner-take-all basis, with the number of electoral votes per
state equal to a state’s total number of federal representatives
and senators. (There are minor exceptions to this rule in Maine
and Nebraska.) The candidate receiving a majority of electoral
votes wins the election. In recent elections, outcomes in most
states have not been competitive. In these safe states, the winning
candidate is largely predetermined, even if the exact percentage
of the vote that each candidate will receive remains unknown.
The division of the country into Republican “red states” and
Democratic “blue states” has been much remarked upon (e.g.,
Farhi 2004; Dickerson 2008). Most observers consider 30–35
of the 50 states to be safe, with each side containing a similar
number of electoral votes.
Presidential elections are, as a result, effectively won or lost
in a smaller number of pivotal swing or battleground states.
Florida and Ohio stand out as the most prominent recent ex-
amples. Outcomes in the swing states are, by their very nature,
more important—and more difﬁcult—to predict in advance. It
is especially in the swing states where the potential value of
preelection polling to forecasting and opinion tracking is the
greatest.
2.1 Characteristics of Trial-Heat Polls
Preelection polls are typically conducted as random samples
of registered or “likely” voters who are asked their current pref-
erences among the presidential candidates. The wording of the
2008 Washington Post-ABC News tracking poll, for example,
reads: “If the 2008 presidential election were being held to-
day and the candidates were Barack Obama and Joe Biden, the
Democrats, and John McCain and Sarah Palin, the Republicans,
for whom would you vote?” Pollsters tabulate the answers to this
question and report the percentages of voters providing each re-
sponse. Most polls also record the percentage of voters who are
undecided; others tally support for nonmajor-party candidates
as well.
Many factors can cause the results of a survey to deviate from
a state’s actual vote outcome. Sampling variability is the largest
single source of error, accounting for half or more of the total
variation in trial-heat estimates during the campaign (Erikson
and Wlezien 1999; Wlezien and Erikson 2002). In addition,
differences between polling organizations in survey design,
question wording, sampling weights, and so forth all contribute


---

126
Journal of the American Statistical Association, March 2013
to the larger total survey error (Weisberg 2005; Biemer 2010).
House effects arise when polling ﬁrms produce survey estimates
that are systematically more or less favorable to particular
parties or candidates (McDermott and Frankovic 2003; Wlezien
and Erikson 2007). Fortunately, the bias arising from such ef-
fects usually cancels out by averaging over multiple concurrent
surveys by different pollsters (Traugott and Wlezien 2009).
Anomalous survey results will be most damaging to estimates of
state opinion when there are few other polls to validate against.
The timing of polls also affects their predictive accuracy. Polls
ﬁelded early in the campaign are much more weakly correlated
with the election outcome than polls conducted just before Elec-
tion Day. During the race, voters’ reported preferences ﬂuctuate
in response to salient campaign events, and as they learn more
about the candidates (Gelman and King 1993; Stevenson and
Vavreck 2000; Arceneaux 2006). For voters who are undecided
or who have devoted minimal effort to evaluating the candi-
dates, intense and consistently favorable media coverage of one
of the candidates—as occurs during the party conventions, for
example—can sway individuals to report preferences that dif-
fer from their eventual vote choice (Zaller 1992). Many voters
simply wait until the end of the campaign to make up their mind.
2.2 Current Survey-Based Approaches to Forecasting
One approach to using preelection polls for election forecast-
ing is to include early measures of presidential approval, policy
satisfaction, support for the incumbent party candidate, or other
relevant attitudes as an independent variable in a broader histor-
ical model ﬁtted to past election data (e.g., Campbell 2008b;
Erikson and Wlezien 2008). The primary limitation of this
method is that, as emphasized by Holbrook and DeSart (1999),
the regression weights estimated for the opinion variable are
subject to uncertainty (sample sizes are typically small), and
may have changed since earlier elections. The poll results used
as inputs for the model will also contain error, and may differ
from the true state of opinion at any point in the campaign.
A second strategy uses trial-heat survey data to update histor-
ical model-based forecasts in a Bayesian manner (e.g., Brown
and Chappell 1999; Strauss 2007; Rigdon et al. 2009; Lock and
Gelman 2010). Yet no current methods are general enough to
use data from all available state-level opinion polls in real time.
Bayesian techniques for estimating trends in voter preferences
using preelection polls either do not produce forecasts until very
late in the campaign (Christensen and Florence 2008) or require
that the election outcome is already known (Jackman 2005),
making forecasting impossible.
3. A DYNAMIC BAYESIAN FORECASTING MODEL
I show how a sequence of state-level preelection polls can
be used to estimate both current voter preferences and forecasts
of the election outcome, for every state on every day of the
campaign, regardless of whether a survey was conducted on that
day. Forecasts from the model gradually transition from being
based upon historical factors early in the campaign to survey
data closer to Election Day. In states where polling is infrequent,
the model borrows strength hierarchically across both states
and time, to estimate smoothed within-state trends in opinion
between consecutive surveys. This is possible because national
campaign events tend to affect short-term voter preferences in
all 50 states in a consistent manner. The temporal patterns in
state-level opinion are therefore often similar across states.
3.1 Speciﬁcation
Denote as hi a forecast of the vote share received by the
Democratic Party candidate in states i = 1, . . . , 50, based upon
a historical model that produces predictions far in advance of
Election Day. There are a variety of approaches to generating
these baseline forecasts (e.g., Rosenstone 1983; Holbrook 1991;
Campbell 1992; Lock and Gelman 2010). Since no deﬁnitive
model exists, the choice of how to estimate hi—and how much
prior certainty to place in those estimates—is left to the analyst.
Values chosen for hi should be theoretically well motivated,
however, as they will be used to specify an informative Bayesian
prior for the estimate of each state’s election outcome, to be
updated using polling data gathered closer to the election.
As the campaign progresses, increasing numbers of preelec-
tion polls are released. Let j = 1, . . . , J index days of the cam-
paign so that j = 1 corresponds to the ﬁrst day of polling and
j = J is Election Day. The model can be ﬁtted on any day of
the campaign, using as many polls are presently available. The
J days prior to Election Day need not include the dates of every
preelection poll, if an investigator wishes to disregard polls con-
ducted far ahead of the election. On day j of the campaign, let
Kj represent the total number of state-level polls that have been
published until that point. Denote the number of respondents
who report a preference for one of the two major-party candi-
dates in the kth survey (k = 1, . . . , Kj) as nk, and let yk be the
number of respondents who support the Democratic candidate.
The proportion of voters in state i on day j who would tell
pollsters that they intend to vote for the Democrat, among those
with a current preference, is denoted πij. Assuming a random
sample,
yk ∼Binomial(πi[k]j[k], nk),
(1)
where i[k] and j[k] indicate the state and day of poll k. In prac-
tice, house effects and other sources of survey error will make
the observed proportions, yk/nk, overdispersed relative to the
nominal sample sizes n. As I will demonstrate, the amount of
overconﬁdence that this produces in the model’s election fore-
casts is minimal. Correcting for overdispersion by estimating
ﬁrm-speciﬁc effects is impractical because most pollsters only
conduct a very small share of the surveys. Alternatively, deﬂat-
ing nk and yk by a multiplicative factor will lead to underesti-
mation of the temporal volatility in πij, which actually worsens
the problem of overconﬁdence in the election forecasts.
The Election Day forecast in state i is the estimated value of
πiJ. On any day during the campaign, πij are estimated for all
J days, both preceding and following the most recent day on
which a poll was conducted. As voter preferences vary during
the campaign, estimates of πij are only expected to approximate
the vote outcome for j close to J. Undecided voters are excluded
from the analysis because it is not known how they would vote
either on day j (if forced to decide) or on Election Day. If unde-
cided voters disproportionately break in favor of one candidate
or the other, it will appear as a systematic error in estimates of


---

Linzer: Dynamic Bayesian Forecasting of Presidential Elections
127
πiJ once data have been collected through day J. The results I
present do not show evidence of such bias.
The daily πij are modeled as a function of two components:
a state-level effect βij that captures the long-term dynamics of
voter preferences in state i, and a national-level effect δj that
detects systematic departures from βij on day j, due to short-
term campaign factors that inﬂuence attitudes in every state by
the same amount:
πij = logit−1(βij + δj).
(2)
I place both βij and δj on the logit scale, as πij is bounded by zero
and one. Values of δj < 0 indicate that on average, the Demo-
cratic candidate is polling below the election forecast; δj > 0
indicates that the Democrat is running ahead of the forecast.
Separating the state-level from national-level effects enables
the model to borrow strength across states when estimating πij.
The trends in all states’ πij are estimated simultaneously. How-
ever, each state will have intervals when no polls are conducted.
To help ﬁll these gaps, the δj parameter detects common pat-
terns in the multivariate time series of voter opinion in other
states on day j. If and when opinions across states do not trend
together, this will also be detectable by the model.
I anchor the scales of βij and δj on Election Day by ﬁx-
ing δJ ≡0. This is an identifying restriction that implies
πiJ = logit−1(βiJ). State-level historical forecasts hi are then in-
corporated into the model through an informative Normal prior
distribution over βiJ,
βiJ ∼N

logit(hi), s2
i

.
(3)
Denote the prior precision as τi = s−2
i . The τi are speciﬁed by
the analyst. Smaller values of τi indicate less certainty in the
respective hi, which upweights the inﬂuence of the polling data
on estimates of βiJ and πiJ. Larger values of τi place greater
certainty in the historical forecast and make estimates of βiJ and
πiJ less sensitive to new polling data. Overconﬁdence in hi can
lead to misleadingly small posterior credible intervals around
estimated ˆπiJ, so caution is required. A sensitivity analysis in
Section 4.4 indicates that τi should not generally exceed 20.
When estimating πiJ weeks or months ahead of the election,
there will be a gap in the polling data between the last published
survey and Election Day. To bridge this interval, and to connect
the days in each state when no polls are released, both βij and δj
are assigned a Bayesian reverse random-walk prior, “beginning”
on Election Day. The idea is similar to Strauss (2007). As shown
by Gelman and King (1993), although historical model-based
forecasts can help predict where voters’ preferences end up on
Election Day, it is not known in advance what path they will
take to get there. Each day’s estimate of βij is given the prior
distribution
βij|βi,j+1 ∼N

βi,j+1, σ 2
β

,
(4)
where the estimated variance σ 2
β captures the rate of daily change
in βij. Likewise,
δj|δj+1 ∼N

δj+1, σ 2
δ

,
(5)
where σ 2
δ captures the rate of daily change in δj. Both σβ and
σδ are given a uniform prior distribution.
3.2 Interpretation
The Election Day forecast in each state is a compromise
between the most recent poll results and the predictions of the
structural model. Posterior uncertainty in πiJ will depend on
the prior τi, the number and size of the available polls, and the
proximity to Election Day. On day j < J of the campaign, the
forward trend in βij shrinks via the reverse random-walk process
toward the prior distribution of βiJ. The δj similarly converge
ahead to δJ ≡0. If the election is soon, δj will already be near
zero, and βij will have little time to “revert” to the structural
prior (Equation (3)). As a result, estimates of πiJ will be based
primarily on each state’s survey data.
For forecasts of πiJ made farther ahead of the election, the
forward path of πij after polling ends is more dependent on the
structural prior. If τi is large, βij converges quickly to logit(hi),
so πiJ converges to hi. If τi is smaller, the forward sequence in
βij moves more slowly away from its value on day j, so future
estimates of πij will be driven by the trend in δj as it returns to
zero on day J. Candidates who are running behind the forecast
(δj < 0) will gain support, while those who are ahead of the
forecast (δj > 0) will trend downward.
As older polls are superseded by newer information, they
contribute less to the forecast, but they leave behind the histor-
ical trends in βij and δj up to the current day of the campaign.
Combining the daily estimates of βij and δj (Equation (2)) pro-
duces estimates of underlying state voter preferences πij over
the duration of the campaign. This series is both important to
analysts and useful for posterior model checking of proper ﬁt
of the model to the data. Past estimates of δj indicate the mag-
nitude and direction of national campaign effects. Comparing
the trends in δj with βij reveals the relative volatility in voters’
preferences due to state- or national-level factors. Changes in
the ﬁltered state-level preferences βij can also suggest evidence
of successful local campaign activity, as distinct from national-
level shifts in opinion.
In studies where the result of the election is known, as when
researching trends in voter preferences from past elections, hi
can be set equal to the outcome in state i. We would then ﬁx
βiJ ≡logit(hi) instead of specifying the prior distribution in
Equation (3), since forecasting (based upon estimating πiJ) is
no longer of interest.
3.3 Estimation
Given Kj state-level preelection polls, and 50 historical fore-
casts hi with prior precision τi, the Bayesian model may be
estimated using a Markov chain Monte Carlo (MCMC) sam-
pling procedure. I implement the estimator in the WinBUGS
and R software packages (Lunn et al. 2000; Sturtz, Ligges, and
Gelman 2005; R Development Core Team 2011). This produces
a rich (and large) set of parameter estimates: the average pref-
erences of voters, πij, as they would be reported to pollsters in
each state at each day in the campaign, the trend in national-level
campaign effects δj, the ﬁltered state-level vote preferences βij,
and the state-level Election Day forecasts, πiJ. Measures of un-
certainty for each estimated parameter are based on the spread
of the simulated posterior draws.
One limitation is that for forecasts made far in advance of
Election Day, the model becomes slow to converge due to the


---

128
Journal of the American Statistical Association, March 2013
lack of available polling data. A slight modiﬁcation to the spec-
iﬁcation of the βij parameters makes the problem tractable and
accelerates MCMC convergence. Rather than let βij vary by day,
I divide the J days of the campaign into J/W short spans or
windows of W days apiece. In Equation (2), I replace βij with
βit[j], which denotes the value of β in state i for the time pe-
riod t = 1, . . . , J/W containing day j. The prior distribution in
Equation (3) is assigned to βit[J]. Parameters δj are still esti-
mated for each of the J days of the campaign, and the election
forecast remains πiJ. Values of W equal to just 3–5 days can
signiﬁcantly improve the estimation process, without substan-
tively altering the election forecast. This simpliﬁcation works
because while δj ﬂuctuates quite a bit on a day-to-day basis, βij
changes far more gradually over time (see Figure 8).
Following estimation, the posterior probability that the
Democratic candidate will win the election in state i is calcu-
lated as the proportion of posterior draws of πiJ that are greater
than 0.5. The probability that the Democratic candidate wins the
presidency can be similarly computed directly from the MCMC
draws. An alternative approach using just the state probabilities
was proposed by Kaplan and Barnett (2003). I select the 50 pos-
terior draws of πiJ produced in a single iteration of the sampling
algorithm, and tally the total number of electoral votes in states
where the Democratic candidate is forecast to receive more than
50% of the two-party vote. I then add the three electoral votes of
the District of Columbia, which is reliably Democratic. Repeat-
ing this calculation across multiple sampling iterations produces
a distribution of predicted electoral vote outcomes. The propor-
tion of these outcomes in which the Democratic candidate re-
ceives an absolute majority—270 or more—of the 538 electoral
votes is the Democratic candidate’s probability of victory.
4. APPLICATION: THE 2008 U.S. PRESIDENTIAL
ELECTION
The 2008 U.S. presidential election was widely predicted
to result in a victory for Democrat Barack Obama (Campbell
2008a). The Republican candidate, John McCain, suffered from
two major drags on his candidacy: an extremely low approval
rating for the incumbent Republican president, George W. Bush;
and a weak economy, whether measured in terms of gross do-
mestic product (GDP) growth, consumer satisfaction, unem-
ployment rates, or other factors. Yet as a candidate, Obama
consistently lagged behind expectations in national preelec-
tion polls—even falling behind McCain for a brief period af-
ter the Republican National Convention in early September
(Pollster.com 2008). News reports quoted worried Democrats
suddenly wondering if Obama would lose after all (e.g., Kuhn
and Nichols 2008). Contributing to the uncertainty were the lin-
gering effects of the unusually long Democratic primary battle
between Obama and then-Senator Hillary Clinton, and questions
about what effect Obama’s race might have on the willingness
of white voters to support him in the November election.
I simulate the process of forecasting the 2008 election and
tracking state-level opinion in real time during the campaign,
leading up to Election Day. This enables us to answer a series
of key questions: By how much did voter preferences change
over the course of the campaign? What were the short-term
effects of campaign events on reported voter preferences? Which
were the actual swing states and how soon was this knowable?
Finally, how early, and with what precision, was the election
outcome predictable from a combination of structural factors
and preelection polls?
4.1 State-Level Polling Data
During the campaign, survey researchers and media organiza-
tions released the results of 1731 state-level public opinion polls
asking voters their current choice for president (Pollster.com
2008). The quantity of interest will be the Obama share of the
state-level major-party vote, measured as the proportion of re-
spondents favoring Obama out of the total number supporting
either Obama or McCain. Polls conducted during the primary
season, before the nominations of Obama and McCain were
assured, asked only about a hypothetical matchup between the
two candidates.
More than 150 distinct entities published state-level polls in
2008. Although the median number of polls among all ﬁrms was
just two, the seven most active ﬁrms—Rasmussen, SurveyUSA,
the Quinnipiac University Poll, Research 2000, Zogby, Ameri-
can Research Group, and PPP—were responsible for 64% of the
state surveys. The median survey contained 600 respondents. On
average, 91% of those polled reported a preference for Obama
or McCain; unsurprisingly, the proportion of undecided voters
was larger in early polls and decreased closer to Election Day.
As most polls spend multiple days in the ﬁeld to complete the
sample, I will consider each poll to have “occurred” on the ﬁnal
day in which interviews were conducted.
Toward the end of the campaign, the rate of preelection polling
accelerated, with more than half of all surveys being ﬁelded in
the ﬁnal 2 months before Election Day (Figure 1). There were
also more polls ﬁelded in states that were expected to be closely
competitive: Florida and Ohio were each surveyed 113 times,
Pennsylvania was surveyed 101 times, and another 85 polls
were conducted in North Carolina (Figure 2). On the low end,
fewer than 10 polls were conducted in Hawaii, Delaware, Mary-
land, and Vermont, all safe Democratic states—and in Idaho and
Nebraska, both safe Republican states. States such as Mis-
souri, Indiana, Georgia, and Montana are among the most
interesting from a forecasting perspective because the out-
comes in these states were very close despite being polled
relatively infrequently.
Months prior to Election Day
Cumulative number of polls fielded
12
11
10
9
8
7
6
5
4
3
2
1
0
0
500
1000
1500
2000
Figure 1. Cumulative number of state-level presidential preelection
polls ﬁelded in advance of the 2008 election. Source: Pollster.com
(2008).


---

Linzer: Dynamic Bayesian Forecasting of Presidential Elections
129
0.3
0.4
0.5
0.6
0.7
0
20
40
60
80
100
120
Obama vote share
Number of polls per state
AL
AK
AZ
AR
CA
CO
CT
DE
FL
GA
HI
ID
IL
IN
IA
KS
KY
LA
ME
MD
MA
MI
MN
MS
MO
MT
NE
NV
NH
NJ
NM
NY
NC
ND
OH
OK
OR
PA
RI
SC
SD
TNTX
UT
VT
VA
WA
WV
WI
WY
Figure 2. More polls were ﬁelded in states that were expected to
be competitive, as indicated by the closeness of Obama’s eventual vote
share to 50%.
4.2 The Historical Forecast
Forecasting presidential elections using a structural model
imposes a trade-off between earliness and accuracy. I produce
both an inaccurate early forecast and an accurate late forecast
based on the Abramowitz (2008) Time-for-Change model. The
late forecast, available about 10 weeks prior to Election Day,
predicts the national-level vote share for the incumbent party
candidate from three variables: the annualized growth rate of
second quarter GDP, the June approval rating of the incumbent
president, and a dummy for whether the incumbent party has
been in ofﬁce for two or more terms. For the earlier forecast,
available up to 6 months in advance, I use a variation of the
model ﬁtted to changes in ﬁrst quarter GDP, and the March
presidential approval rating. I initially base structural forecasts
on the early model, and then switch to the late model as soon as
it would have become available. From 15 previous presidential
elections, the early forecast predicted Obama to receive 56.8%
of the major-party vote in 2008. The more proximate late fore-
cast predicted that Obama would receive 54.3%. Both forecasts
overestimated Obama’s actual vote share of 53.7%.
To translate national forecasts to the state level, I exploit a
20-year pattern in presidential election outcomes. Since 1980,
state-level Democratic vote shares have tended to rise and fall
in national waves, by similar amounts across states. In 2004,
Democrat John Kerry received 48.8% of the two-party presi-
dential vote. Assuming that the same trend would continue in
2008 (as it did), the Time-for-Change model predicts an average
state-level gain by Obama of 8% early and 5.5% late.
I calculate hi by ﬁrst adding to Kerry’s 2004 state-level vote
shares either 5.5% or 8% depending upon the timing of the
forecast. I then adjust the forecast by a further 6% in candi-
dates’ home states, adding in for Hawaii (Obama) and Texas
(Bush in 2004), and subtracting away for Arizona (McCain)
and Massachusetts (Kerry in 2004). This correction was esti-
mated from past elections by Holbrook (1991) and Campbell
(1992), and also employed by Lock and Gelman (2010). Com-
pared with the actual result, the early Time-for-Change forecast
had a state-level mean absolute deviation (MAD) of 3.4%, and
the late forecast had a MAD of 2.6%. I set τi = 10 for the early
forecast, and a more conﬁdent τi = 20 for the late forecast.
To test the sensitivity of the forecasts to the choice of hi, I
examine an alternative model based on the idea of a Democratic
normal vote. For this, I set hi equal to the mean Democratic vote
share in each state over the previous four presidential elections:
1992 and 1996, which were won by Democrats, and 2000 and
2004, which were won by Republicans. In 2008, this would have
systematically underpredicted Obama’s vote share by 1.8%, on
average, with a MAD of 4.2%. I hold τi = 10.
4.3 Updating Forecasts Using Preelection Polls
I consider all state-level polls ﬁelded within the ﬁnal 6 months
of the campaign. The ﬁrst set of election forecasts is produced
with 4 months remaining, in July 2008. I then move forward
through Election Day, 2 weeks at a time. At each step, I update
the election forecasts and estimates of current opinion using
all newly available polls. In total, I ﬁt the model nine times:
with 16, 14, 12, . . . , 2 weeks left in the campaign, and again on
Election Day. Parameter estimates are based on three sequences
of 200,000 MCMC iterations, discarding the ﬁrst half as burn-
in and thinning to keep every 300th draw. I specify a 3-day
window (W = 3) for parameters βit[j]. MCMC convergence
is assessed by values of the Gelman–Rubin statistic ˆR ≈1,
and visual conﬁrmation that the three sequences are completely
mixed (Gelman and Rubin 1992; Brooks and Gelman 1998).
Three snapshots of estimates of ˆπij in the competitive states of
Florida and Indiana demonstrate the real-time performance of
the model (Figure 3). Although a large number of polls were con-
ducted in Florida, Indiana was surveyed only six times between
May and August. The early trend estimate in Indiana therefore
draws heavily from patterns of public opinion in the other 49
states, illustrating the power of the model to detect subtle cam-
paign effects. The downtick in support for Obama between the
2- and the 3-month mark, for example, coincides with the se-
lection by John McCain of Sarah Palin as his Vice Presidential
nominee, and the ensuing Republican National Convention. It
is evident that ˆπij identiﬁes the central tendency in the polls.
With 2 months remaining in the campaign, polls in Florida
indicated that support for Obama was below both the Time-for-
Change forecast and the Obama’s actual (eventual) vote share. In
Indiana, Obama was slightly ahead of the historical forecast, but
this was atypical: in most states, as in Florida, fewer voters than
expected were reporting a preference for Obama. As a result,
estimates of ˆδj < 0; so after the ﬁnal day of polling, ˆπij trended
upward to Election Day. In Florida, ˆπij moved closer to both
the structural forecast and the actual outcome. In Indiana, ˆπij
moved away from the structural forecast, but again toward the
actual outcome—thus correcting the substantial −5.5% error in
the original Time-for-Change forecast.
One month before the election, support for Obama increased
nationwide, but the model forecasts remained stable. The 90%
highest posterior density (HPD) interval for the Florida forecast
fell from ±3.5% to ±2.6%, and for the Indiana forecast from
±3.6% to ±2.8%. Finally, on Election Day, the model predicted
with 90% probability that Obama would win between 50.1% and
51.9% of the major-party vote in Florida, and between 48.4%
and 50.5% in Indiana. The actual outcome was 51.4% in Florida
and 50.5% in Indiana.


---

130
Journal of the American Statistical Association, March 2013
Figure 3. Forecasting the 2008 presidential election in real time. Results are shown for Florida and Indiana. The vertical axis is the percentage
supporting Obama; points denote observed poll results. Horizontal lines indicate the late Time-for-Change forecast (dashed) and the actual
election outcome (solid). The jagged gray line is the state-level daily estimate of voter preference for Obama, ˆπij. After the ﬁnal day of polling,
these trends project ahead to the Election Day forecast, ˆπiJ, plotted as ■. Shaded areas, and the vertical bar on Election Day, denote 90% posterior
credible intervals.
In the complete set of simulations, incorporating polling data
into the prior structural forecasts steadily reduces the MAD be-
tween the state-level election forecasts and the actual outcomes
(Figure 4). The largest improvements occur in the ﬁnal 6 weeks
of the campaign, when the polls become most informative about
the election outcome (e.g., Campbell 1996). Yet even polls con-
ducted 4 months before the election reduce the MAD of the
(early) Time-for-Change forecast by 0.3%, and the MAD of the
normal vote forecast by 1%. The state-level election forecasts
converge in a stable manner toward the election outcomes and
are not oversensitive to short-term changes in current opinion.
By Election Day, both sets of forecasts indicate a MAD of 1.4%,
with more than half of states (27) predicted within 1% of the
Figure 4. Sequential reduction in MAD of state-level election fore-
casts by incorporating trial-heat polls. Dotted lines indicate MAD of
baseline structural predictions. Points show forecast MAD, updating
from the Time-for-Change and normal vote models. With 10 weeks re-
maining, estimates based on the Time-for-Change model switch from
the early to the late forecast.
actual result. The largest forecast errors arose in infrequently
polled safe states.
Accurate forecasting of vote shares aids in predicting the
winner of each state. This is most important in competitive
swing states, where the difference of a few percentage points
could decide the election. The baseline structural forecast using
the Time-for-Change model mispredicted seven states early and
four late: Arkansas, Indiana, Missouri, and North Carolina. The
normal vote forecast mispredicted nine states. By comparison,
the only state incorrectly predicted by the model using trial-heat
polls through Election Day was Indiana (Figure 5). Even so,
Obama’s vote share in Indiana was in the 90% HPD interval of
ˆπiJ, as noted.
Estimates of uncertainty in ˆπiJ enable early identiﬁcation of
states in which the election is likely to be close. I consider a
state to be a swing state when the posterior probability of a
Democratic victory is between 10% and 90%. The number of
swing states declined during the campaign, as more informa-
tion from polls became available (Figure 5). Large states that
proved pivotal to Obama’s victory—including Florida, Ohio,
and Virginia—were already nearly certain to be won by Obama
with a month or more remaining. The battleground states of
Missouri, Montana, North Carolina, and Indiana were likewise
identiﬁable far in advance of the election. The surprising com-
petitiveness of states such as Arkansas, West Virginia, North
Dakota, and Nevada through the ﬁnal 2 weeks of the campaign
was attributable to a combination of limited polling and late-
breaking voter preferences in these states.
Aggregating the state-level forecasts, Obama’s predicted elec-
toral vote tally was consistently above the 270 needed to win
the presidency (Figure 6). With 2 months remaining in the
campaign, forecasts based on updating the Time-for-Change
model predicted the ﬁnal outcome to within six electoral votes,


---

Linzer: Dynamic Bayesian Forecasting of Presidential Elections
131
Figure 5. Swing states and forecast accuracy. Left: forecasts by updating the Time-for-Change model with preelection polls; D indicates the
model forecasted a Democratic victory, while R indicates the model forecasted a Republican victory. Swing states are denoted as squares. A gray
X indicates that the estimated ˆπiJ mispredicted the state winner. States are sorted by Obama’s ﬁnal vote share; Obama won North Carolina (50.2%
of the major-party vote), but lost Missouri (49.9%). Right: total number of swing states and mispredicted state winners during the campaign.
corresponding to a near certain victory for Obama. On Election
Day, the model projected a range of 338–387 Obama electoral
votes, with 95% probability. Obama actually won 365 electoral
votes, which (in a historical anomaly) included the single elec-
toral vote of Nebraska’s Second Congressional District. Fore-
casts based on updating the normal vote model gave Obama an
87% chance of winning, with 2 months remaining, and over 99%
on Election Day, with between 311 and 378 electoral votes.
Combining a well-motivated structural forecast with infor-
mation from large numbers of preelection polls thus generates
early and accurate predictions of the presidential election out-
come. Updating continually during the campaign also improves
the precision of the forecasts. For comparison, the range of
Obama electoral votes predicted by Lock and Gelman (2010),
who updated a prior structural forecast made close to Election
Day using only one set of state-level preelection polls conducted
9 months before the election, was between 250 and 450. In their
simulations, Obama had a 99.9% chance of victory, but this high
level of certainty was only achievable because Obama won by
a relatively large margin in 2008. In a closer election, much
greater precision would be required to predict the winner with
conﬁdence.


---

132
Journal of the American Statistical Association, March 2013
Figure 6. Distributions of forecasted Obama electoral votes. Verti-
cal bars span 95% of simulated electoral vote forecasts; points denote
the median. A majority is 270.
4.4 Prior Sensitivity Analysis
The choice of τi (Equation (3)) indicates the analyst’s prior
certainty in the structural model forecasts hi, before information
from state-level polls is considered. Although the τi are meant
to specify an informative prior, their selection is not arbitrary.
If τi is very high, the vote forecasts ˆπiJ will not update from
trial-heat polls until just before Election Day. Large values of
τi will also reduce the posterior uncertainty in ˆπiJ, which can
lead to errors in both the identiﬁcation of swing states and
the estimation of the probability of winning each state and the
presidency. Depending on τi, the posterior HPD intervals for ˆπiJ
should be wide enough to include the actual election outcomes
in the expected proportion of states.
I calculate the coverage rate of the nominal 90% Bayesian
posterior credible intervals for ˆπiJ, at various values of τi
(Figure 7). Updating from the Time-for-Change model, setting
τi = 10 early, and τi = 20 late, produces 90% credible inter-
vals for ˆπiJ that include the election outcomes in between 80%
and 90% of states through the ﬁnal 2 weeks of the campaign.
This coverage is achieved despite the overconﬁdence expected
in estimates of ˆπiJ due to house effects and other sources of non-
sampling error. Coverage is somewhat worse under the normal
vote model. Values of τi > 20 generate credible intervals that
are misleadingly narrow.
As Election Day nears, the proportion of states in which the
election outcome is forecasted within the posterior 90% HPD
interval of ˆπiJ falls below 80%. However, this is primarily a
function of limitations and anomalies in the underlying survey
data, rather than the choice of τi. Forecast intervals for ˆπiJ
are least accurate in states with limited numbers of polls, which
prevents averaging to reduce error. Because states that are polled
infrequently also tend to be uncompetitive, there is very little
practical consequence to the narrower than the expected forecast
intervals in these states. Indeed, in the earlier simulation, only
one forecast error occurred in a state not considered a swing
state at the time: Missouri, with 2 weeks remaining (Figure 5).
4.5 Trends in Voter Preferences During the Campaign
Looking back from Election Day, past estimates of ˆπij, ˆβit[j],
and ˆδj reveal how voter preferences evolved during the cam-
paign. In 2008, the opinions that voters held about the presi-
dential candidates changed very gradually over time, compared
with the large ﬂuctuations in the polls. The state with the most
consistent attitudes was Wyoming, where ˆπij varied within a
range of just 4.6% over the ﬁnal 6 months of the campaign.
Preferences in Alaska were the most variable; there, ˆπij ranged
10% from its lowest to its highest point. Among all states’ daily
changes in ˆπij, 98% were by less than 0.5%. In a typical state,
the variance in the poll results was three to ﬁve times greater
than the variance in ˆπij. This suggests that the combined error in
preelection polls due to sampling variability and house effects
may be even greater than what was estimated by Erikson and
Wlezien (1999) and Wlezien and Erikson (2002).
Most of the temporal variation in state-level opinion was
due to national-level campaign effects (Figure 8). Estimates
of ˆδj < 0 reﬂect the fact that Obama ran behind his eventual
election performance in most states for most of the campaign.
Once the common effects of ˆδj are ﬁltered away, the unique state
effects ˆβit[j] demonstrate relative stability. While trends in ˆβit[j]
do occur, they tend to happen in one sustained direction. The
national-level effects evened out approximately 4 weeks before
the election. At that point, voter preferences within individual
states began to move toward the ﬁnal outcome in divergent,
state-speciﬁc directions.
Figure 7. Coverage of nominal 90% posterior credible intervals around ˆπiJ for choices of prior precision τi. Solid lines correspond to the τi
used in the above simulation.


---

Linzer: Dynamic Bayesian Forecasting of Presidential Elections
133
Figure 8. After the election: past state-level trends in ˆβit[j] (gray), and the common trend in ˆδj (black), during the campaign. Some of the most
signiﬁcant short-term changes in ˆδj coincide with major campaign events. Estimates of ˆδj and ˆβit[j] exhibit the same historical trends whether
the structural forecast is based on the Time-for-Change model (shown) or the normal vote model. The online version of this ﬁgure is in color.
5. DISCUSSION
The trend toward increased preelection polling—especially at
the state level—appears likely to continue in the 2012 presiden-
tial campaign, and beyond. Public opinion polls have become
integral to political reporting, and interest in following the “state
of the race” only seems to grow each year. For analysts, the
availability of these survey data creates new opportunities for
statistical models that can apply theories of mass opinion for-
mation and voter behavior to produce better estimates of voter
preferences during the campaign, and forecasts of the outcome
on Election Day.
This article has presented a dynamic Bayesian statistical pro-
cedure for processing and interpreting the results of state-level
preelection opinion polls in real time. Applied to the 2008 pres-
idential election, the model generated a nearly perfect predic-
tion of which states would be won by Barack Obama and John
McCain, and by how much, and estimated with certainty that
Obama would win the presidency. The model also produced
daily estimates of state-level opinion during the campaign and
reliably predicted which states would be most competitive on
Election Day.
The results of my analysis highlight a number of lessons
about presidential campaigns and elections. First, presidential
election forecasts can, and should, be made at the state level.
State-level outcomes can be predicted accurately and reliably
by combining readily available historical and public opinion
data. Furthermore, these forecasts need not be overly sensi-
tive to short-term ﬂuctuations in voter preferences during the
campaign. Most of the variation in preelection polls is due to
sampling variability. But even after averaging this away, much
of the remaining day-to-day variation in state-level opinion is
attributable to national-level campaign effects. By smoothing
and ﬁltering the trial-heat polling data, it is possible to produce
election forecasts that converge toward the outcome in a gradual
and stable manner. During the campaign, any report suggesting
that voter preferences have changed by more than a few tenths
of a percent on a daily basis should be treated with suspicion.
There nevertheless remain inherent limitations to what can
be learned from state-level public opinion data—no matter how
many surveys are released in an election cycle. With current
numbers of polls, it is relatively easy to forecast the outcomes
of state-level presidential elections on the eve of the election,
as I have shown. The challenge remains to produce accurate
forecasts many months in advance. My solution seeks to com-
bine the best features of structural forecasts and preelection
polls, downweighting the historical forecasts over time in favor
of the information contained in more recent survey data. But
even so, the biggest forecasting improvements only occur 1 or
2 months in advance of the election. This is not because there
is not enough polling data, but because the polling data them-
selves are noisy and, far before Election Day, subject to inac-
curacies. Future research into presidential campaign dynamics
may yet discover new ways to extract meaning from those early
polls.
[Received May 2011. Revised May 2012.]
REFERENCES
Abramowitz, A. I. (2008), “Forecasting the 2008 Presidential Election With the
Time-for-Change Model,” PS: Political Science & Politics, 41, 691–695.
[124,129]
Arceneaux, K. (2006), “Do Campaigns Help Voters Learn? A Cross-National
Analysis,” British Journal of Political Science, 36, 159–173. [126]
Bartels, L. M., and Zaller, J. (2001), “Presidential Vote Models: A Recount,”
Political Science & Politics, 34, 9–20. [124]
Becker, B. (2008, October 28), “Competing Web Sites Track Election
Polls,” The New York Times [online]. Available at http://www.nytimes.
com/2008/10/28/world/americas/28iht-polls.1.17304703.html?pagewanted=
all. [124]
Biemer, P. P. (2010), “Overview of Design Issues: Total Survey Error” in Hand-
book of Survey Research (2nd ed.), eds. P. V. Marsden and J. D. Wright,
Bingley, England: Emerald Group Publishing, pp. 27–57. [126]
Broh, C. A. (1980), “Horse-Race Journalism: Reporting the Polls in the 1976
Presidential Election,” Public Opinion Quarterly, 44, 514–529. [124]
Brooks, S. P., and Gelman, A. (1998), “General Methods for Monitoring Con-
vergence of Iterative Simulations,” Journal of Computational and Graphical
Statistics, 7, 434–455. [129]
Brown, L. B., and Chappell, H. W., Jr. (1999), “Forecasting Presidential Elec-
tions Using History and Polls,” International Journal of Forecasting, 15,
127–135. [124,126]
Campbell, J. E. (1992), “Forecasting the Presidential Vote in the States,”
American Journal of Political Science, 36, 386–407. [126,129]
——— (1996), “Polls and Votes: The Trial-Heat Presidential Election Forecast-
ing Model, Certainty, and Political Campaigns,” American Politics Research,
24, 408–433. [125,130]


---

134
Journal of the American Statistical Association, March 2013
——— (2001), “The Referendum That Didn’t Happen: The Forecasts
of the 2000 Presidential Election,” Political Science & Politics, 34,
33–38. [125]
——— (2008a), “Editor’s Introduction: Forecasting the 2008 National Elec-
tions,” PS: Political Science & Politics, 41, 679–682. [128]
——— (2008b), “The Trial-Heat Forecast of the 2008 Presidential Vote: Per-
formance and Value Considerations in an Open-Seat Election,” PS: Political
Science & Politics, 41, 697–701. [124,126]
Campbell, J. E., Cherry, L. L., and Wink, K. A. (1992), “The Convention Bump,”
American Politics Research, 20, 287–307. [124]
Campbell, J. E., and Garand, J. C. (eds.) (2000), Before the Vote: Forecast-
ing American National Elections, Thousand Oaks, CA: Sage Publications.
[124]
Campbell, J. E., and Wink, K. A. (1990), “Trial-Heat Forecasts of the Presiden-
tial Vote,” American Politics Research, 18, 251–269. [125]
Center for Responsive Politics. (2008), “U.S. Election Will Cost $5.3 Billion,
Center for Responsive Politics Predicts” [online] Available at http://
www.opensecrets.org/news/2008/10/us-election-will-cost-53-billi.html.
[124]
Christensen, W. F., and Florence, L. W. (2008), “Predicting Presidential and
Other Multistage Election Outcomes Using State-Level Pre-Election Polls,”
The American Statistician, 62, 1–10. [126]
Dickerson, J. (2008, September 30), “So You Think You’re a Swing Voter?
Think Again: It Depends on Whether You Live in a Swing State,” Slate
[online]. Available at http://www.slate.com/id/2201071. [125]
Duch, R. M., and Stevenson, R. T. (2008), The Economic Vote: How Political and
Economic Institutions Condition Election Results, Cambridge: Cambridge
University Press. [124]
Erikson, R. S., and Wlezien, C. (1996), “Of Time and Presidential Election
Forecasts,” PS: Political Science and Politics, 29, 37–39. [124]
——— (1999), “Presidential Polls as a Time Series: The Case of 1996,” Public
Opinion Quarterly, 63, 163–177. [124,125,132]
——— (2008), “Leading Economic Indicators, the Polls, and the Presidential
Vote,” PS: Political Science & Politics, 41, 703–707. [124,126]
Fair, R. C. (2009), “Presidential and Congressional Vote-Share Equations,”
American Journal of Political Science, 53, 55–72. [124]
Farhi, P. (2004, November 2), “Elephants Are Red, Donkeys Are Blue; Color Is
Sweet, So Their States We Hue,” The Washington Post, p. C01. [125]
Finkel, S. E. (1993), “Reexamining the ‘Minimal Effects’ Model in Recent
Presidential Campaigns,” The Journal of Politics, 55, 1–21. [125]
Gelman, A., and King, G. (1993), “Why Are American Presidential Election
Campaign Polls So Variable When Votes Are So Predictable?” British Jour-
nal of Political Science, 23, 409–451. [124,125,126,127]
Gelman, A., and Rubin, D. B. (1992), “Inference From Iterative Simulation
Using Multiple Sequences,” Statistical Science, 7, 457–511. [129]
Hillygus, D. S., and Jackman, S. (2003), “Voter Decision Making in Elec-
tion 2000: Campaign Effects, Partisan Activation, and the Clinton Legacy,”
American Journal of Political Science, 47, 583–596. [124]
Holbrook, T. M. (1991), “Presidential Elections in Space and Time,” American
Journal of Political Science, 35, 91–109. [126,129]
——— (1994), “Campaigns, National Conditions, and U.S. Presidential Elec-
tions,” American Journal of Political Science, 38, 973–998. [125]
Holbrook, T. M., and DeSart, J. A. (1999), “Using State Polls to Forecast Pres-
idential Election Outcomes in the American States,” International Journal
of Forecasting, 15, 137–142. [124,126]
Jackman, S. (2005), “Pooling the Polls Over an Election Campaign,” Australian
Journal of Political Science, 40, 499–517. [125,126]
Jamieson, K. H. (ed.) (2009), Electing the President, 2008: The Insiders’ View,
Philadelphia: University of Pennsylvania Press. [124]
Kaplan, E. H., and Barnett, A. (2003), “A New Approach to Estimating the
Probability of Winning the Presidency,” Operations Research, 51, 32–40.
[128]
Kinder, D. R., and Kiewiet, D. R. (1991), “Sociotropic Politics: The American
Case,” British Journal of Political Science, 11, 129–161. [124]
Kuhn, D. P., and Nichols, B. (2008, September 10), “Autumn Angst: Dems
Fret About Obama,” Politico [online]. Available at http://www.politico.
com/news/stories/0908/13357.html. [128]
Lewis-Beck, M. S., and Rice, T. W. (1992), Forecasting Elections, Washington,
DC: CQ Press. [124]
Lewis-Beck, M. S., and Tien, C. (2008), “The Job of President and the Jobs
Model Forecast: Obama for ’08?” PS: Political Science & Politics, 41,
687–690. [125]
Lock, K., and Gelman, A. (2010), “Bayesian Combination of State Polls and
Election Forecasts,” Political Analysis, 18, 337–348. [126,129,131]
Lunn, D. J., Thomas, A., Best, N., and Spiegelhalter, D. (2000), “WinBUGS—A
Bayesian Modelling Framework: Concepts, Structure, and Extensibility,”
Statistics and Computing, 10, 325–337. [127]
McDermott, M. L., and Frankovic, K. A. (2003), “Review: Horserace Polling
and Survey Method Effects: An Analysis of the 2000 Campaign,” Public
Opinion Quarterly, 67, 244–264. [126]
Nadeau, R., and Lewis-Beck, M. S. (2001), “National Economic Voting in U.S.
Presidential Elections,” The Journal of Politics, 63, 159–181. [124]
Panagopoulos, C. (2009a), “Campaign Dynamics in Battleground and Nonbat-
tleground States,” Public Opinion Quarterly, 73, 119–129. [124]
——— (2009b), “Polls and Elections: Preelection Poll Accuracy in the 2008
General Elections,” Presidential Studies Quarterly, 39, 896–907. [125]
Pew Research Center.
(2008, October 22), “Winning the Media Cam-
paign: How the Press Reported the 2008 Presidential General Elec-
tion,” Project for Excellence in Journalism [online]. Available at
http://www.journalism.org/node/13307. [124]
Pickup, M., and Johnston, R. (2008), “Campaign Trial Heats as Election Fore-
casts: Measurement Error and Bias in 2004 Presidential Campaign Polls,”
International Journal of Forecasting, 24, 272–284. [125]
Pollster.com. (2008), “The Polls: The 2008 Presidential Election” [online].
Available at http://www.pollster.com/polls/2008president. [124,128]
R Development Core Team. (2011), R: A Language and Environment for Sta-
tistical Computing [online], Vienna, Austria: R Foundation for Statistical
Computing. Available at http://www.R-project.org. [127]
Rhee,
J.
W.
(1996),
“How
Polls
Drive
Campaign
Coverage:
The
Gallup/CNN/USA Today Tracking Poll and USA Today’s Coverage of the
1992 Presidential Campaign,” Political Communication, 13, 213–229. [124]
Rigdon, S. E., Jacobson, S., Tam Cho, W. K., and Sewell, E. C. (2009), “A
Bayesian Prediction Model for the U.S. Presidential Election,” American
Politics Research, 37, 700–724. [126]
Romer, D., Kenski, K., Winneg, K., Adasiewicz, C., and Jamieson, K. H. (2006),
Capturing Campaign Dynamics, 2000 and 2004: The National Annenberg
Election Survey, Philadelphia: University of Pennsylvania Press. [124]
Rosenstiel, T. (2005), “Political Polling and the New Media Culture: A Case of
More Being Less,” Public Opinion Quarterly, 69, 698–715. [124]
Rosenstone, S. J. (1983), Forecasting Presidential Elections, New Haven, CT:
Yale University Press. [126]
Shaw, D. R. (1999), “A Study of Presidential Campaign Event Effects From
1952 to 1992,” Journal of Politics, 61, 387–422. [124,125]
Stevenson, R. T., and Vavreck, L. (2000), “Does Campaign Length Matter?
Testing for Cross-National Effects,” British Journal of Political Science, 30,
217–235. [126]
Stovall, J. G., and Solomon, J. H. (1984), “The Polls as a News Event in the 1980
Presidential Campaign,” Public Opinion Quarterly, 48, 615–623. [124]
Strauss, A. (2007), “Florida or Ohio? Forecasting Presidential State Out-
comes Using Reverse Random Walks,” Working Paper, Princeton University.
[126,127]
Sturtz, S., Ligges, U., and Gelman, A. (2005), “R2WinBUGS: A Package for
Running WinBUGS From R,” Journal of Statistical Software, 12, 1–16.
[127]
Traugott, M. W. (2001), “Trends: Assessing Poll Performance in the 2000
Campaign,” Public Opinion Quarterly, 65, 389–419. [125]
——— (2005), “The Accuracy of the National Preelection Polls in the 2004
Presidential Election,” Public Opinion Quarterly, 69, 642–654. [125]
Traugott, M. W., and Lavrakas, P. J. (2008), The Voter’s Guide to Election Polls,
Lanham, MD: Rowman & Littleﬁeld Publishers, Inc. [124]
Traugott, M. W., and Wlezien, C. (2009), “The Dynamics of Poll Performance
During the 2008 Presidential Nomination Contest,” Public Opinion Quar-
terly, 73, 866–894. [126]
Vavreck, L. (2009), The Message Matters: The Economy and Presidential Cam-
paigns, Princeton, NJ: Princeton University Press. [124]
Weisberg, H. F. (2005), The Total Survey Error Approach: A Guide to the New
Science of Survey Research, Chicago, IL: University of Chicago Press. [126]
Wlezien, C., and Erikson, R. S. (1996), “Temporal Horizons and Presidential
Election Forecasts,” American Politics Research, 24, 492–505. [124]
——— (2001), “Campaign Effects in Theory and Practice,” American Politics
Research, 29, 419–436. [125]
——— (2002), “The Timeline of Presidential Election Campaigns,” The Journal
of Politics, 64, 969–993. [124,125,132]
——— (2007), “The Horse Race: What Polls Reveal as the Election Campaign
Unfolds,” International Journal of Public Opinion Research, 19, 74–88.
[125]
Zaller, J. (1992), The Nature and Origins of Mass Opinion, Cambridge:
Cambridge University Press. [126]

---
title: Model-Based Pre-Election Polling for National and
id: model-based-pre-election-polling-for-national-and
tags:
- mrp
- academic-paper
- mrp-canonical
- ecological-inference
created: '2026-07-21T18:30:13.657112Z'
updated: '2026-07-21T18:39:17.679825Z'
source: https://benjaminlauderdale.net/files/papers/mrp-polling-paper.pdf
source_domain: benjaminlauderdale.net
fetched_at: '2026-07-21T18:30:13.656822Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Lauderdale, Bailey, Blumenau & Rivers (LSE/YouGov/UCL/Stanford, Dec 2017)
  — the canonical methods paper behind YouGov''s MRP pre-election polling, published
  later in International Journal of Forecasting. Builds directly on Gelman & Little
  (1997) and Park, Gelman & Bafumi (2004) MRP theory, extended to pre-election forecasting
  via a three-way decomposition: (1) conditional vote-choice distribution p(V|X,T=1)
  given demographic/political type X and turnout T, (2) conditional turnout distribution
  p(T=1|X), (3) poststratification frame f(X) — the population count of each type,
  drawn from census and other admin data. Reports results across three applications:
  2016 EU referendum (local-authority estimates correlated with actual results at
  r=0.92, national margin error 2.6pp, despite no directly comparable past referendum
  to anchor the poststratification), 2016 US presidential election (national margin
  error 1.7pp; correctly identified Trump''s Electoral College path to victory despite
  predicting a narrow Clinton popular-vote win; state-level estimates suffered notable
  attenuation bias), and 2017 UK general election (national margin error 0.9pp; correctly
  predicted Conservative failure to win a majority — the only pre-election forecast
  to do so; captured both Labour gains in decades-held Conservative seats (Kensington,
  Canterbury) and Conservative gains in decades-held Labour seats (Middlesbrough South
  & East Cleveland, Stoke-on-Trent South)).\n\nMethodologically load-bearing points
  for fine-grained projection: contrasts MRP against poll-of-polls/uniform-swing and
  against Wang et al. (2014)''s Xbox-poll MRP (750,000 responses, 93% male, 65% aged
  18-29, ~15,000 obs/state) — argues Wang et al.''s huge per-unit sample sizes undercut
  the central MRP value proposition of borrowing statistical strength across sparse
  units; the YouGov UK application used far smaller samples per constituency (632
  constituencies, 8 parties) yet outperformed all pre-election forecasts and uniform-swing
  benchmarks. Explicitly names three unresolved limitations: (1) attenuation bias
  — systematic underprediction of a party''s strength where it is strong and overprediction
  where weak, partially mitigated via cross-level interactions between individual-level
  and constituency-level past vote but with ''varying success''; (2) undercoverage
  of interval estimates at the constituency/district level, because non-sampling error
  is hard to fold into calibrated uncertainty; (3) the model does not attempt to model
  shifts in turnout patterns at individual or aggregate level, treating turnout as
  roughly static — flagged as improvable given richer panel + validated turnout data.
  Notes UK constituency-level modelling (632 units, more covariates available at second
  level) outperformed US state-level modelling (51 units, fewer covariates, higher
  electoral-vote sensitivity to a handful of errant state calls) despite far more
  raw data per US state.'
raw_file: raw/model-based-pre-election-polling-for-national-and.pdf
---

Model-Based Pre-Election Polling for National and
Sub-National Outcomes in the US and UK
Benjamin E Lauderdale, London School of Economics*
Delia Bailey, YouGov
Jack Blumenau, University College London
Douglas Rivers, Stanford University and YouGov
December 23, 2017
Abstract
We describe a strategy for applying multilevel regression and post-stratiﬁcation (MRP)
methods to pre-election polling. Using a combination of contemporaneous polling, census
data, past election polling, past election results, as well as other sources of information, we
are able to construct probabilistic, internally consistent estimates of national vote and the
sub-national electoral districts that determine seats or electoral votes in many electoral sys-
tems. We report on the performance of three applications of the general framework conducted
and publicly released in advance of the 2016 UK Referendum on EU Membership, the 2016 US
Presidential Election, and the 2017 UK General Election.
1
Introduction
Election polling in the US and UK has suﬀered several high proﬁle failures in recent years, some
real and some merely perceived. While the accuracy of polling in established democracies in na-
tional elections has in fact been roughly constant for the past half century (Jennings and Wlezian,
2017), there are nonetheless periodic, high proﬁle polling misses (Sturgis et al., 2016; Rivers and
Wells, 2015). This is hardly surprising given the quality of data used by pre-election polling, little
of which comes from probability samples, and none of which involves high response rates. But
even if these data quality problems were corrected, national polling does not always answer the
questions of interest, which ofen concern electoral outcomes that depend on results in a very
large number of sub-national units (states, electoral districts or constituencies) that cannot be
polled individually at reasonable expense. Both the problems of sample representativeness and
the problem of sub-national elections can be addressed by better modelling (Wang et al., 2014).
In this study, we describe our approach to applying the logic of multilevel regression and
post-stratiﬁcation (MRP; Gelman and Little, 1997; Park et al., 2004) to pre-election polling. We
begin by describing the typical approaches taken to electoral polling and sub-national electoral
*Please send correspondence to b.e.lauderdale@lse.ac.uk
1


---

results prediction, and the beneﬁts of addressing these problems in a common modelling frame-
work. We then state the problem as a three-way decomposition: 1) estimating the distribution
of vote choice conditional on turnout and demographic and political types, 2) estimating the
distribution of turnout conditional on demographic and political types, and 3) estimating the
population joint distribution of demographic and political types. This approach allows us to gen-
erate sub-national estimates for electoral quantities of interest and sub-population estimates
for understanding patterns of vote intention and change across politically relevant groups. In
practice, this approach may improve national vote share estimates as well, although this is dif-
ﬁcult to test without application to a very large number of elections.
We report here on three applications of this analysis strategy—to the 2016 UK Referendum
on EU Membership, the 2016 US Presidential Election, and the 2017 UK General Election—using
estimates that we published online in advance of each event. While the details of performance
vary across these applications, in general all three models performed well. The magnitude of the
errors on the national vote share margin between the top two alternatives were all reasonable
(2.6% EU 2016, 1.7% US 2016, 0.9% UK 2017), but we acknowledge that it is possible to get lucky
on a single outcome quantity in three elections. The sub-national estimates successfully cap-
tured the novel patterns of voting in the referendum as well as non-uniform patterns of swings
in the US and UK elections. In the EU referendum, we generated local authority level estimates
that correlated with the results at r=0.92, despite the lack of any directly comparable past elec-
toral results. In the US Presidential Election, the point estimate was for a narrow Clinton victory.
However, the model correctly identiﬁed Trump’s electoral college advantage—even though the
electoral college advantage in 2012 was in Obama’s favour—and therefore that Trump’s most
likely victory scenarios involved losing the national popular vote. In the UK general election,
the model correctly predicted Labour gains in several seats that had been held by the Conser-
vatives for decades (Kensington, Canterbury) while also correctly predicting Conservative gains
from Labour in constituencies the latter had held for decades (Middlesbrough South and East
Cleveland, Stoke-on-Trent South). The detailed performance assessments that we report be-
low identify several areas of potential improvement, which we discuss more extensively in the
conclusion.
2
Election Polling and Prediction
2.1
Traditional electoral polling
Traditional electoral polling methods follow the logic of social surveys despite the fact that elec-
toral polling is almost never based on probability samples. Nearly all UK pollsters use methods
that can be understood as involving some kind of more or less sophisticated quota sampling
followed by some set of post-stratiﬁcation adjustments (Sturgis et al., 2016). Practice in the
US is more varied, but broadly follows the same procedures. First, a non-probability sample
is collected by telephone or online. Second, a set of weights Wi(Xi) are estimated that match
the sample marginal distributions of measured covariates to known eligible voter population
targets. This is typically done using raking/calibration (Sturgis et al., 2016). Third, turnout prob-
ability weights Ti are constructed from stated intention to turnout, for each sampled respon-
2


---

dent. In practice, these are ofen binary, reﬂecting some simple cutoﬀrules in stated intention
to turnout, but more generally can reﬂect best estimates of the probability that the particular
respondent will turnout. Finally, the estimate of the national vote share for party k is formed
by multiplying these two sets of weights by the probability Vik that the respondent will vote for
party k.
P
i VikTiWi(Xi)
P
i TiWi(Xi)
(1)
Like the turnout probability, these Vik are usually binary assessments based simply on stated
vote intention, but can reﬂect an estimate of the probability that the particular respondent
will in fact vote for a given party. Within this general procedure, there is a variety of practice
regarding exactly how each component of the above equation is generated from the polling
response, particularly surrounding the treatment of people who say they do not know how they
will vote, and people who express varying conﬁdence that they will turnout.
The historical performance of election polling is mixed. Jennings and Wlezian (2017) show
that the predictive performance of national polls in established democracies has been stable
over the past half century, even as sampling methods and response rates have evolved. It is
clear, however, that there are ofen systematic biases on top of sampling variability. Aside from
accuracy concerns, one important limitation of these traditional methods is that they do not
provide reliable estimates for public opinion in electorally relevant sub-national geographic
units, unless separate polls are conducted in each sub-national geographic unit. This is usu-
ally prohibitively expensive. In the UK, for example, conducting a 1000 person poll in every
parliamentary constituency would require polling 650,000 individuals. Further, because rak-
ing/calibration match marginal rather than joint distributions of characteristics, these methods
also may not provide reliable estimates for non-geographic sub-populations (age groups, edu-
cation levels, etc) that may be of interest in advance of an election.
2.2
Poll aggregation models
In contexts where many polls are conducted and published, several academic and non-academic
researchers have demonstrated that it is possible to eﬀectively aggregate those polls to produce
ensemble estimates. Poll aggregation methods aim to correct for pollster-speciﬁc biases in
order to estimate the true level of support for diﬀerent voting alternatives (Jackman, 2005), and
combine national-level information with sub-national information to construct estimates of the
probability of diﬀerent election outcomes (Silver, 2017; Linzer, 2013; Hanretty et al., 2016a). Poll
averaging replaces the assumption that an individual pollster has unbiased procedures with an
assumption that the average pollster is unbiased.
In US presidential elections, poll aggregation has proved eﬀective at translating the many
state polls conducted by diﬀerent pollsters into national estimates. While no pollster ﬁelds polls
in every state, at least a few polls are conducted in most states over the period of the campaign.
However, in a UK election, with 650 constituencies and a short campaign period, constituency
polling does not generally occur to any signiﬁcant degree.1 A large number of national polls are
conducted, some with substantial sample sizes, but this still translates into small numbers of
1In only one election cycle (2015) have a non-trivial number of constituency polls been conducted, and even then
only about 20% of constituencies over the entire year preceding the election.
3


---

responses at the constituency level.
2.3
Multilevel regression and post-stratiﬁcation
In recent years, researchers in statistics and political science have shown that it is possible
to construct high quality sub-national (small area) estimates of public opinion using multilevel
regression and post-stratiﬁcation methods, typically referred to as MRP (Gelman and Little, 1997;
Park et al., 2004). These methods rely on multilevel regression models to utilise small numbers
of observations in each sub-national unit in order to discover patterns in opinion as a function of
the demographic composition and other measurable features of those sub-national units. These
patterns are then mapped out onto all sub-national units through post-stratiﬁcation of ﬁtted
values from the model. There have been applications of this methodology to measuring public
opinion on a variety of politically relevant geographies, including US states (Lax and Phillips,
2009), US congressional districts (Tausanovitch and Warshaw, 2013), German electoral districts
(Selb and Munzert, 2011), Swiss Cantons (Leemann and Wasserfallen, 2017a), UK parliamentary
constituencies (Hanretty et al., 2016b), and others.
These studies of public opinion have typically targeted the full adult population. Pre-election
polling has the additional step of distinguishing voters and non-voters among the voting eligible
population. The only published academic study that we know of applying MRP to pre-election
polling is by (Wang et al., 2014). In their study of the 2012 US presidential election, those au-
thors used an unusually large sample—750,000 responses—from an unusually unrepresentative
data source—an XBox poll with a 93% male and 65% 18-29 years old sample—to estimate vote
shares for Barack Obama and Mitt Romney in 50 US states plus the District of Columbia. While
an impressive demonstration of using modelling to rescue low quality ”big” data, this is well
outside the scope of most pre-election polling, which involves much smaller, higher quality
samples. Further, it is not the most convincing illustration of the power of model-based meth-
ods for generating small area estimates, as that study used an average of 15,000 observations
per state. Such massive sample sizes reduce the need to leverage patterns across sub-national
units, which is a major potential upside to model-based approaches to analysing survey data.
In this paper, we use a much smaller, but higher quality sample, to get estimates of the 2016
US presidential election that are comparable in quality to those Wang et al recovered for the 2012
US election and the most successful 2016 US polling aggregators. For the UK general election
we use a smaller overall sample, and generate estimates for eight parties in 632 constituencies
that were far more accurate than any other pre-election analysis as well uniform swing heuristics
applied to the actual national or regional swings. The UK general election example demonstrates
the potential of MRP, because there are few viable alternatives to model-based methods in
electoral systems with large numbers of ﬁrst-past-the-post electoral districts.
4


---

3
Methods
3.1
Decomposition of the Problem
We denote the electoral alternative chosen by individual i as an unordered categorical variable
Vi ∈1, . . . , Kvote. In our examples, these correspond to {Leave, Remain}, {Clinton, Trump, John-
son, Stein, Other} or {Conservative, Labour, Liberal Democrat, etc}. Whether an eligible elector
turns out to vote is a binary variable Ti ∈0, 1. Finally, a ‘voter type’ is a vector of measurable
characteristics Xi ∈X for an eligible voter i. These might include age, gender, education, vote
in preceding elections, geographic location, etc. For each voter type, there are three important
quantities that we would like to know:
1. Conditional voting distribution: p(Vi|Xi, Ti = 1). What proportion of each type will vote for
each of the alternatives among those who do vote?
2. Conditional turnout distribution: p(Ti = 1|Xi). What proportion of each voter type will
turn out to vote?
3. Poststratiﬁcation frame: f (Xi) or p(Xi). How many or what proportion of eligible voters
are of each type?
The proportion of voters turning out to vote is then:
P
Xi∈X p(Ti = 1|Xi)f (Xi)
P
Xi∈X f (Xi)
and the vote share for alternative k is:
P
Xi∈X p(Vi = k|Xi, Ti = 1)p(Ti = 1|Xi)f (Xi)
P
Xi∈X p(Ti = 1|Xi)f (Xi)
(2)
Note that we can sum over relevant subsets of types rather than all types ∈X, in order to
calculate turnout or vote counts/shares on geographic or demographic subsets of electorate.
The crucial distinction between this approach, and the weighting approach followed by most
polling, is seen by comparing Equations 1 and 2. In the weighting approach, the sum is over
the sampled observations; in the modelling approach, the sum is over the set of voter types.
Thus, when weighting, the key estimation step is the construction of weights Wi(Xi) for each
observation in the sample that match sample and population moments of a set of covariates for
which the population distribution is known. In the modelling approach, the primary estimation
exercise is to construct an outcome model p(Vi = k|Xi, Ti = 1) that describes vote choice as a
function of voter types, over which the population distribution is known.
This is not the only decomposition we could adopt for this problem. There are two simpler
two-component decompositions that have been previously applied. The ﬁrst of these is that
used by Wang et al. (2014) when they post-stratify to an exit poll from the previous presiden-
tial election. The exit poll sample is a sample from p(Ti = 1, Xi) = p(Ti = 1|Xi)p(Xi) at the
last election, thus combining the second two components of our three-way decomposition into
a single step of estimating the demographic distribution of those who will turnout, given the
assumption that it will be the same as in the previous election. The second two-component
5


---

decomposition treats non-voting as a voting choice category symmetrically with the voting al-
ternatives, estimating p(Vi, Ti = 1|Xi) = p(Vi = k|Xi, Ti = 1)p(Ti = 1|Xi) in a single step.
The reason that we explicitly specify the three-component decomposition here is that we
separately model turnout rates and vote choices for demographic types, using diﬀerent data
sources. We do this because several of the problems facing pre-election non-probability sam-
ples are far more severe for turnout than for vote choice. First, turnout self-reports have well-
known social desirability biases (Bernstein et al., 2001; Holbrook and Krosnick, 2010), while vote
choice only sometimes has a signiﬁcant social desirability bias. Second, not turning out to vote
is associated with unit non-response to political surveys (Jackman and Spahn, 2016), while vote
choice is less systematically associated with unit non-response. These two points, taken to-
gether, suggest that typical pre-election surveys are likely to face more serious problems of
representativeness and misreporting with respect to turnout than with respect to vote. Fortu-
nately, while pre-election survey estimates of turnout are problematic, the demographics of
turnout are usually broadly stable across elections. In this paper, we use high quality surveys
from the preceding comparable election to estimate turnout patterns at that election, and as-
sume they will not change much in the present election. While this means we do not aim to
predict how turnout might be changing in the present election versus that preceding election,
it also avoids the very large errors that can result from relying on uncalibrated prospective self-
reports.2
4
Applications
4.1
Political Context
The UK Referendum on EU Membership was held on 23 June 2016. The results of the referendum
were reported for each of the 380 local authorities in England, Scotland and Wales (Great Britain),
for Northern Ireland, and for Gibraltar. We modelled the 380 local authorities in Great Britain
and added ﬁxed priors for the relatively small number of votes in Northern Ireland and Gibraltar.
The only electoral outcome of consequence was whether the national vote share for Leave was
greater than 50% of the valid votes. 51.9% of votes were for Leave, a 3.8% margin of victory over
Remain.
The 2016 US Presidential Election was held on 8 November. The results of the election were
reported at the county level in nearly all of the 51 states, however the electoral outcomes rel-
evant to determining the vote count in the electoral college were the state plurality winners,
plus the plurality winners in the congressional districts of Maine and Nebraska. We modelled
all states and congressional districts. Hillary Clinton won 48.2% of the national popular vote
versus Donald Trump’s 46.1%, a 2.1% national vote margin, however due to narrow Trump victo-
ries in several key states, he won states and districts awarding 306 electoral votes versus 232 for
Clinton.3
The 2017 UK General Election was held on 8 June. The results of the election were reported
2Implicit in this approach is that most consequential changes in results from election to election are due to changes
in vote choices rather than changes in who turns out, or at least that these are the only changes we can reliably predict.
3These are the nominal electoral vote totals before seven members of the electoral college failed to vote for the
candidate they were slated to vote for. The oﬃcial record for each candidate is 304 for Trump and 227 for Clinton.
6


---

at the level of the 650 parliamentary constituencies. Our modelling only concerned the 632
constituencies in Great Britain,4 the remaining 18 seats in Northern Ireland elect MPs from a
diﬀerent set of parties. In Great Britain, the Conservative party received 43.5% of the vote to
41.0% for Labour, a national vote margin of 2.5%. The electoral outcome is determined by the
plurality winner in each constituency. Among the parties competing in Great Britain, Conserva-
tives won 317 seats (-13 versus 2015), Labour 262 (+30), the Scottish National Party 35 (-21), the
Liberal Democrats 12 (+4), Plaid Cymru 4 (+1), Greens 1 (nc), UKIP 0 (-1) and Other 1 (nc).
All three of these votes were close relative to the magnitude of historical polling errors and
also in the sense that the key electoral outcomes were uncertain before the election. Indeed
all three had outcomes that were surprising to the majority of election observers and led to
substantial ﬁnancial market movements as the results became clear. We reported our estimates
for the EU referendum online in the form of an article on YouGov’s website5 on June 21, and
provided updates with the ﬁnal days’ data via Twitter. For the US presidential election, we posted
daily updates on YouGov’s website from 3 October until a ﬁnal release on 7 November using data
through 6 November.6 For the UK general election, we posted daily updates on YouGov’s website
from 31 May until a ﬁnal release on 7 June using data through 6 June.7.
4.2
Frame Construction
Our information about the population joint distribution of demographic variables is captured in
the form of a ”frame”, a rectangular dataset representing a very large sample of the population
with micro-level data of the variables of interest, adjusted through weighting to maintain con-
sistency with known marginal targets. The creation of a frame for each application is described
in detail below. The input data ﬁles vary by application, but the overall logic of the construction
process is similar across them.
First, a high quality survey of the population is selected as the base frame, with micro data
responses on basic demographics like age, gender, educational attainment, race and ethnicity,
and geographic locale. This is typically a publicly available Census ﬁle. Then, additional ge-
ographies of interest (target) are imputed onto the base dataset at the lowest level geography
available. The prior probability for the target geographic units is estimated by the proportion
of population of the source geography within the target. The likelihood for a given respondent
is estimated by published tables describing the joint distribution of demographics in the tar-
get geography if available, and assuming independence of published marginal tables otherwise.
The new geographies are sampled from a multinomial distribution, with probability equal to the
prior times the likelihood. Then, for political applications, voting behavior is imputed onto the
frame from a separate survey using multinomial regression. Finally, the frame base weights are
raked to published vote totals, population demographics, and estimates of the electorate size.
In Table 1 we report the speciﬁc steps taken in each application, and the data sets used.
The frames generated in this way are approximations to the true population distributions of
4Great Britain will be used here as a slightly inaccurate shorthand for England, Scotland and Wales.
5https://yougov.co.uk/news/2016/06/21/yougov-referendum-model/
6https://today.yougov.com/us-election/
7https://yougov.co.uk/uk-general-election-2017/ When the Times published our initial estimates on 31
May that the Conservative party was likely to lose its majority, the value of the £ immediately declined by a half percent.
http://www.bbc.co.uk/news/business-40101566
7


---

2016 UK Referendum on EU Membership
0
Base ﬁle: 2011 UK Census Microdata Individual Safeguarded Sample (Local Authority)
1
Impute local authority district conditional on local authority group
2
Impute constituency conditional on local authority district
3
Impute 2015 general election turnout conditional on demographics (2015 BES face-to-face
validated vote)
4
Impute 2015 general election vote choice for voters conditional on demographics and
region (YouGov)
5
Rake to regional margins for constituency by vote and region by age by gender by quali-
ﬁcations
6
Post-stratify on vote, constituency and census marginals
2016 US Presidential Election
0
Base ﬁle: 2012 ACS
1
Impute congressional district conditional on PUMA and demographics
2
Rake to ACS demographics and observed state level turnout
3
Impute registration and turnout conditional on demographics and state
4
Rake to demographics and turnout by state for 18+ citizens
5
Rake 2012 exit poll to ACS demographics and actual vote by state
6
Impute 2012 vote conditional on demographics by region
7
Rake to demographics and 2012 vote by state for voters
8
Rake to demographics and 2012 vote by congressional district for voters
9
Increment age by 4, apply survival weights
10
Impute education for 18-21 year olds
11
Impute registration for 18-21 year olds from CPS 2012
12
Rake to 2016 census population projections for demographics
2017 UK General Election
0
Base ﬁle: 2016 Annual Population Survey (Jan - Dec)
1
Impute constituency conditional on region and demographics
2
Rake YouGov 2015 general election data to demographics and known vote totals at re-
gional level
3
Rake YouGov EU referendum data to demographics and known vote totals at regional level
4
Impute 2015 turnout using pooled 2010 and 2015 BES face-to-face validated vote
5
Impute 2015 vote for voters using weighted YouGov data
6
Impute referendum vote conditional on 2015 vote + demographics using weighted YouGov
data
7
Rake to constituency margins for demographics, 2015 vote, and estimated referendum
vote
Table 1: Procedure followed to generate population frames for each application.
8


---

the included demographic, geographic and past vote variables that they include. For nearly all
variables, we have known marginal distributions of all variables at the geographic level we are
interested in, or good approximations thereof. The information about the conditional distri-
butions comes from a variety of sources, and is less reliable. Nonetheless, this information is
important to include. Leemann and Wasserfallen (2017b) show that in MRP applications like this
one, using the product of the marginal distributions to deﬁne the post-stratiﬁcation distribution
yields identical estimates to the true joint distribution, so long as the model is linear and has
no interactions (for logistic models the equivalence is approximate). Put diﬀerently, without in-
formation about the conditional distributions, we could only reliably apply a linear and additive
model. Such a model would be unsatisfactory in these applications, there is very clear evidence
of signiﬁcant interactions in the vote choice models for all three applications.8
4.3
Turnout Model Speciﬁcation
For each application, we estimated the conditional probability of turnout p(Ti = 1|Xi) as a
function of covariates using a high quality, face-to-face probability survey conducted afer one or
more prior election. For the EU referendum model, we used the 2015 British Election Study (BES)
post-election survey observations for which vote validation was completed using the marked
electoral register afer the election. For the US presidential election model, we used the Current
Population Survey (CPS) round completed afer the 2012 US presidential election, relying on self-
reported voter turnout. For the UK general election model, we pooled both the 2010 and 2015
BES post-election surveys, afer verifying that the demographics of turnout in both surveys were
largely similar. This yielded turnout model data sets for the three applications of 2955, 68167,
and 6449 observations, respectively.
For all three applications, the turnout model took the form of a multilevel binary logistic
regression model. For the EU referendum model and the US presidential election model, no
survey weights were used; for the UK general election model, BES weights were used via a quasi-
likelihood approach. The variables used in each model (including interactions) are listed in
Table A2 in the appendix.
None of these data sets provided a wholly satisfactory measure of turnout in the election
preceding the one being studied: for the BES data there is a self-reported recall of behaviour ﬁve
years previous, for the CPS there is no measure at all. As a result, for all three data sets, we im-
puted turnout at the previous election in such a way as to not distort the demographic patterns
of turnout in the data, while also yielding a high level of serial correlation in voter turnout. In
each case, we randomly assigned previous election turnout in the turnout data set, conditional
on reported/validated turnout in the observed election, such that the transition rates between
turning out and not turning out matched either our priors (UK) or those from state voter ﬁles
(US). These imputed values then became regressors in the turnout model, ensuring that our
modelled electorate mostly (but not entirely) consisted of individuals who voted in the previ-
ous election. Once we ﬁt these models to the relevant data, we then used the model to construct
turnout probabilities/weights p(Ti = 1|Xi) for each observation in the post-stratiﬁcation frame.
8For example, entering 2015 general election vote and 2016 referendum vote additively into the vote choice model
for the 2017 UK general election does not ﬁt the data as well as allowing the association with referendum preferences
to vary by 2015 vote choice.
9


---

4.4
Vote Choice Model Speciﬁcation
For each application, we estimated the conditional probability of voting for each alternative
p(Vi|Xi, Ti = 1) as a function of covariates using data collected from YouGov’s online panel. Re-
spondents were selected from YouGov’s panel on a daily basis, using YouGov’s sample matching
procedure Rivers and Bailey (2009).
The vote choice prompts were as follows. For the EU referendum, the question was ”Should
the United Kingdom remain a member of the European Union or leave the European Union?”
with alternatives of ”Remain a member of the European Union”, ”Leave the European Union”,
”Would not vote” and ”Don’t know”. For the US election, among those who did not indicate an
intention not to vote in a preceding question, we asked ”Who will you vote for in the election
for President in November?” with alternatives of ”Hillary Clinton (Democrat)”, ”Donald Trump
(Republican)”, ”Gary Johnson (Libertarian)”, ”Jill Stein (Green)”, ”Other”, and ”Not sure”. For the UK
general election, we provided a list of the candidates standing for election in the respondent’s
constituency, with the form ”¡Name¿ - ¡Party¿”, plus ”Other”, ”Will not vote” and ”Don’t Know”.
For purposes of modelling vote choice among voters, we excluded ”Not sure” and ”Don’t
Know” responses. For the US presidential model, there were ﬁve outcome categories: Clinton,
Trump, Stein, Johnson and Other. For the UK general election model, there were eight out-
come categories: Conservative, Labour, Liberal Democrat, UKIP, Green, SNP, PC and Other. We
estimated separate models of the same form for England, Scotland and Wales, so not all eight
outcome categories were used in any given model. We modeled the probability of voting for
parties that were not standing in a respondent’s constituency as zero. The variables used in
each model (including interactions) are listed in Table A1 in the appendix. The models all in-
clude individual vote at the previous election plus interactions thereof that we deemed to be
politically relevant in each case. For example, in the US Presidential election, we interacted 2012
election vote with race of the respondent, as we did not expect to see similar patterns of switch-
ing between parties for black and white respondents (on the logistic scale). For the UK general
election, we interacted 2015 vote with constituency-level vote shares, as switching to and from
diﬀerent parties is predicted by the relative competitiveness of parties in a given constituency.
For all three applications, we used a relatively large time window of data, but modeled time
trends within that data window. For the EU referendum and US presidential election we used a
14 day window, for the UK general election we used a 7 day window. Our ﬁnal estimates in these
three applications were based on 48738, 81246, and 55707 panelist responses, respectively.
Once we ﬁt these models to the relevant data, we then used the model to construct ﬁtted vote
choice probabilities p(Vi|Xi, Ti = 1) for each observation in the post-stratiﬁcation frame. When
constructing ﬁtted values for the purposes of post-stratiﬁcation, we set the date variable to the
most recent day, thus “adjusting” for time trends within the data window. In all applications, in
order to capture our best guess of the scale of non-sampling errors that we could not explicitly
model, we also added additional gaussian noise at the post-stratiﬁcation stage, at both the
national level and the sub-national level.
10


---

Vote Choice
Result
Estimate
Low
High
EU Referendum
Leave
51.9
50.6
48.8
52.4
Remain
48.1
49.4
47.6
51.2
US Presidential
Trump
46.1
44.1
43.0
45.2
Clinton
48.2
47.9
46.8
49.1
UK General
Conservative
43.4
41.6
39.2
43.9
Labour
41.0
38.2
36.1
40.6
Liberal Democrat
7.6
9.0
7.9
10.3
UKIP
1.9
3.5
2.9
4.1
Green
1.7
2.0
1.7
2.4
SNP
3.1
3.8
3.4
4.2
Plaid Cymru
0.5
0.5
0.4
0.6
Table 2:
National vote shares for major alternatives with mean posterior estimates and 95%
predictive interval lower and upper bound.
4.5
Aggregation
To form estimates, we generate turnout frequency weights by multiplying the population frame
frequency weights by the ﬁtted turnout probabilities for each observation in the post-stratiﬁcation
frame. The resulting turnout frequency weights are eﬀectively a post-stratiﬁcation frame for vot-
ers, rather than the electorate. We then multiply these turnout frequency weights by the ﬁtted
vote choice probabilities for each observation in the post-stratiﬁcation frame to get the esti-
mated breakdown of each frame observation across the available vote choices. This can then
be aggregated to the national level, the sub-national level, or by any other demographic variable
that we have in the post-stratiﬁcation frame in order to form estimates for that level of aggrega-
tion. We saved full posterior distributions for the electorally relevant sub-national aggregates
by post-stratifying at each iteration of the MCMC simulation.
We implemented the turnout model, the vote model and the post-stratiﬁcation in Stan (Car-
penter et al., 2017). Given that we were posting estimates daily, and several aspects of the
model were computationally expensive (large sample sizes, many parameters and multinomial
outcomes) we used multiple, relatively short simulation chains estimated in parallel. The ref-
erendum model used four chains of 500 iterations (250 iteration initial burn-in discarded), the
presidential model used 36 chains of 25 iterations (25 iteration burn-in), and the general election
model used 4 chains of 125 iterations (75 iteration burn-in). Despite the extremely short chains
used for the US election, and the modest samples overall, we did not see evidence of instability
across runs. All three applications had estimation times that were roughly eight hours, which
was our target to facilitate daily updates. Shorter estimation times for equivalent models may
have been possible using alternative parameterisations that yield better performance in Stan.
11


---

EU2016
Leave − Remain Margin
Density
−5
0
5
10
0.00
0.05
0.10
0.15
0.20
0.25
Result
US2016
Trump − Clinton Margin
Density
−8
−6
−4
−2
0
2
0.00
0.10
0.20
0.30
Result
GE2017
Conservative − Labour Margin
Density
−10
−5
0
5
10
0.00
0.05
0.10
0.15
0.20
Result
Figure 1:
Posterior predictive distributions and results for national vote share margin, in the
referendum (lef), the presidential election (center), and in the general election (right).
5
Results
5.1
National Vote Shares
Figure 1 shows the election results in comparison to the posterior distributions for the key elec-
toral margin in each election (Leave - Remain; Trump - Clinton; Conservative - Labour). In all
three cases, the national margins fall in a region of the posterior distribution with a reasonable
level of density, suggesting that our national-level uncertainty in the margin was plausibly cal-
ibrated, at least given what we can learn from three results. Table 2 shows the election results
in comparison to the mean posterior and central 95% posterior interval for the voting alterna-
tives. The largest error for any individual party in any of the applications was Labour, which we
underestimated by 2.8 percentage points. In contrast to the national margins, many of the party
vote shares fell outside the interval estimates. In both the US and UK elections this was due
to the “major parties” overperforming the estimates while the minor parties generally under-
performed. This may reﬂect a more general problem in polling of ﬁrst-past-the-post electoral
systems, where tactical decisions to vote for major parties may not be expressed to pollsters.
5.2
Sub-National Vote Shares
While for the EU Referendum, the national vote totals were the only relevant electoral outcome,
for the US Presidential Election and the UK General Election, it is the sub-national vote totals
that matter. In the US presidential election, the plurality winner in each state (plus those in
Maine and Nebraska’s congressional districts) determines the distribution of electoral college
votes and thus the winner of the election. In the UK general election, the plurality winner in
each of the 650 constituencies is seated in parliament. The posterior distribution of our model
over vote shares for each candidate in each of these sub-national geographies thus implies a
posterior distribution over these electoral outcomes.
Figure 2 shows the posterior distributions of (nominal) electoral college votes for Clinton in
the 2016 US presidential election and seats for Con, Lab, LD, SNP and PC in the 2017 UK general
election. The number of electoral votes secured by Clinton was at the very low end of the range
we observed in our posterior sample, owing to her surprising loss of Michigan combined with
her losing all of the predicted close states. Nonetheless, her result was not outside the range
12


---

Clinton 
Expected EC votes = 318
Electoral college votes
Proportion of simulations
200
250
300
350
400
0.00
0.05
0.10
0.15
0.20
Con
Expected seats = 302
Seat count
Proportion of simulations
240
280
320
360
0.00
0.10
0.20
Lab
Expected seats = 269
Seat count
Proportion of simulations
220
240
260
280
300
320
0.00
0.10
0.20
0.30
LD
Expected seats = 12
Seat count
Proportion of simulations
5
10
15
20
0.00
0.10
0.20
0.30
SNP
Expected seats = 44
Seat count
Proportion of simulations
20
30
40
50
0.0
0.1
0.2
0.3
0.4
0
1
2
3
4
5
PC
Expected seats = 2
Seat count
Proportion of Simulations
0.00
0.10
0.20
0.30
Figure 2: Posterior distributions of electoral votes in the US presidential election (top lef) and
for major and minor parties in the UK general election, with actual results depicted by a vertical
line.
of our simulated election results. The seat totals for all the UK parties were generally located
within the posterior distributions we estimated, with the largest surprise being Plaid Cymru’s
single seat gain.9
Looking at the vote share predictions in each reporting electoral unit, our estimates broadly
tracked the results in the relevant sub-national areas in all three applications (Fig 3), however we
see signiﬁcant undercoverage of our interval estimates and some degree of attenuation bias. In
all three cases we underestimated voting alternatives where they were strong and overestimate
them where they were weak. A simple linear regression estimate of the marginal change in our
prediction as a function of the marginal change in the result is 0.75 for the referendum, 0.79 for
the presidential election, and 0.80 for the general election.
We suspect there were a few reasons for the general pattern of attenuation bias, as well
as the diﬀerences across applications. The ﬁrst reason is that in general random eﬀects and
multilevel models tend to have this kind of attenuation bias. Such models reduce estimation
variance, but are biased towards the overall mean in their predictions. The second reason is that
individual-level behaviour is not fully explained by individual-level characteristics: individuals
in politically extreme places vote diﬀerently from those in moderate places, even conditional
on their observed characteristics and lagged vote. This meant that at the individual-level, the
patterns of switching among supporters of each party were very diﬀerent in diﬀerent states. In
the US model, we included an interaction of congressional district 2012 vote share and individual
9The PC went from 3 to 4 seats by gaining Ceredigion constituency by a margin of 104 votes or 0.2% The Ceredigion
constituency has four competitive parties, which is extremely unusual, and thus is likely to deviate from the patterns of
voting for those parties in other constituencies.
13


---

Leave − Remain Margin
 Coverage = 0.72
Result
Prediction
−60
−40
−20
0
20
40
60
−60
−40
−20
0
20
40
60
Trump − Clinton Margin
 Coverage = 0.55
Result
Prediction
−20
0
20
40
−20
0
20
40
Con − Lab Margin
 Coverage = 0.86
Result
Prediction
−80
−60
−40
−20
0
20
40
60
80
−80
−60
−40
−20
0
20
40
60
80
Figure 3: Predicted margin by actual margin, for local authorities in the referendum (lef), states
in the presidential election (center), and constituencies in the general election (right).
2012 vote to try to capture this. In the UK general election model, we added an interaction of
constituency vote share with individual lagged referendum and 2015 vote to enable to the model
to discover this kind of pattern, which may have helped reduce (but not eliminate) attenuation
bias. Because the referendum was cross-cutting with respect to prior election results, these
contextual eﬀects were probably smaller in that application. One of our key conclusions from
these applications is that careful model speciﬁcation is essential in applying MRP to pre-election
polling, additive models without interactions involving political context performed less well in
our model testing.
We can report some comparisons of ﬁt to similar applications. Preceding the EU referendum,
Chris Hanretty published local authority level estimates before the election based on an alter-
native multilevel regression (but not post-stratiﬁcation) strategy, which generated estimates
that correlated with both our estimates and the results at the same r=0.92. His estimates only
aimed to generate the relative levels of the local authority reporting areas in a hypothetical
50-50 referendum, not the absolute level of support.
As previously discussed, Wang et al. (2014) used a multilevel regression and post-stratiﬁcation
approach in 2012 to map responses from a survey conducted on XboxLive onto electoral out-
comes in 51 Electoral College races (excluding the Maine and Nebraska congressional district
races). They report that the ”mean and median absolute errors of our [Obama vote share] esti-
mates on the day before the election are just 2.5 and 1.8 percentage points, respectively.” When
we assess our state-level estimates by these two metrics, using Clinton vote share, we calculate
absolute errors of 2.5 and 1.9 percentage points, respectively. The 2012 election was a much
easier election for prediction than 2016, as changes in relative state-level results were smaller
between 2008 and 2012 than between 2012 and 2016.
For 2016, we can compare our estimates to those produced by a number of forecasters, most
of whom pooled all (or most) publicly released state and national polls. Our RMSE was similar
to, but slightly worse than, those of FiveThirtyEight.com, the New York Times, and the Prince-
ton Election Consortium (PEC).10 Since these forecasters pooled all publicly available state and
national polls, this implies that the informational content of our MRP analysis was nearly that
10We do not report assessments of the probabilities of state-level victory because there is no standard way to assess
the correlation of the state-level outcomes. For example, by Brier score, the PEC is among the best forecasts, but in fact
the PEC indicated that a Clinton victory was certain, because (like the Brier score metric) it failed to take into account
the possibility that state-level errors would be correlated.
14


---

Table 3: Comparison to uniform swing model and forecasts based on aggregations of state-level
polling (RMSE) for the 2016 US Presidential election.
Model
RMSE (Top Two Margin)
538 (polls plus)
7.0
Princeton Election Consortium
7.0
New York Times
7.0
538 (polls only)
7.1
YouGov
7.3
Uniform swing
7.5
PollSavvy
8.0
HuﬀPost
10.7
Table 4: Comparison to uniform swing models and Hanretty forecast (RMSE and % correctly
predicted) for the 2017 UK Presidential election.
Model
Con
Lab
LD
UKIP
Green
SNP
PC
Other
% correct
YouGov model
4.4
4.7
2.5
2.4
0.9
3.3
3.6
1.6
92.9
Uniform swing (Regional)
4.6
4.1
3.6
3.8
1.9
3.8
2.9
1.9
91.6
Uniform swing (Country)
5.4
4.1
3.8
4.3
2
3.8
2.9
1.9
91.8
Uniform swing (GB)
5.9
4.7
3.8
3.8
1.8
11.9
3.3
1.9
91.1
Hanretty
5.3
6.1
3.7
1.9
1.9
4.7
4.1
2.3
86.2
of all other published polling for the election. All of these forecasts and our model provided
a slight improvement on the RMSE that would have resulted from applying the correct 2012-
2016 national vote share swing to the 2012 state-level margins, which indicates that all of these
analyses were able to recover some information about relative state-level movements versus
2012.
For the UK election, we provide comparisons with both the pre-election estimates produced
by Chris Hanretty (Hanretty, 2017) pooling public national and regional polls, and also with esti-
mates constructed afer the election which apply uniform swings to the party vote shares based
on the actual election swings from 2015 to 2017. We use three diﬀerent measures of swing for
this comparison: at the national level (Great Britain), at the country level (England, Scotland and
Wales), and at the regional level. Table 4 presents the party-speciﬁc RMSE and percentage of
constituency winners correctly predicted for each of these approaches. Compared to Hanretty’s
pre-election forecast, our model has a lower RMSE for all parties except for UKIP, and we correctly
predict 92.9% of constituency results compared with 86.2% for the Hanretty model. Our model
has lower RMSEs for most parties and correctly predicts a larger percentage of constituency re-
sults versus any of the uniform swing models, even though the uniform swing models use true
swings that were not known in advance of the election. This indicates that our model was able
to measure variation in swings across diﬀerent kinds of constituencies, even within UK regions.
5.3
Sub-National Turnout
We have only indirect ways of assessing the performance of our turnout model. To assess
individual-level turnout, we would have to rely on exit poll data, which is variably available
15


---

55
60
65
70
75
80
55
60
65
70
75
80
Turnout (EU Referendum)
Correlation = 0.55
Result
Prediction
Scotland
England and Wales
70
75
80
85
90
70
75
80
85
90
Turnout (US Presidential)
Correlation = 0.77
Result
Prediction
40
50
60
70
80
40
50
60
70
80
Turnout (UK General)
Correlation = 0.6
Result
Prediction
Scotland
England and Wales
Figure 4: Predicted turnout by actual turnout among the registered electorate, for local authori-
ties in the EU referendum (lef), states in the US presidential election (center), and constituencies
in the UK general election (right).
across the diﬀerent cases and can be problematic. We can, however, look at the extent to which
the turnout rates that we expected at the sub-national level match the observed turnout rates
at that level. In all three applications we see moderate correlations, with some indirect evidence
that turnout was responsible for some prediction error.
In both the EU referendum and the UK general election, the turnout estimates had one ob-
vious source of error: the relative turnout in Scotland was down and the relative turnout ev-
erywhere else in the UK was up relative to the 2015 general election. Given the SNP’s takeover
of almost all Scottish parliamentary seats in 2015 this turnout shif was perhaps not surprising,
but we made no explicit eﬀorts to model it in either case. Within Scotland, and within the rest of
the UK, the turnout model performed decently at estimating relative turnout rates, suggesting
the the demographic patterns of relative turnout were not substantially changed other than this
national-level discrepancy. For the referendum, the estimated Leave share rises from 50.6 in our
pre-election estimates to 51.0 if we replace the turnout estimates with the true turnout rates for
each local authority, reducing the error on the margin from 2.6% to 1.8%. For the 2017 general
election, the same calculation moves our estimate of Con 41.6 - Lab 38.2 (Con +3.4) to Con 41.2 -
Lab 39.0 (Con +2.2). This is a better match to the true margin between the two parties (Con +2.5)
because turnout was indeed up in Labour strongholds in relative terms, however the levels of
support are still too low for both major parties. In the US presidential election, the correspond-
ing analysis is less informative because of the smaller number of sub-national units, and the
national vote margin only changes by 0.1% when using the true state turnouts.
There is no clear pattern across the three applications, and as noted above this is a very
indirect test of whether the turnout model was responsible for the errors we see. The real risk is
not so much mispredicting the relative turnout across electoral units, but rather mispredicting
the relative turnout across groups within electoral units. With data from the 2016 CPS in the
US and the 2017 British Election study in the UK equivalent to the data sets we used to ﬁt the
turnout model, we could evaluate the performance of the model if we use those data in place
of the data from the preceding elections. However, as we noted when we set out our estimation
strategy, the question is not whether such errors occurred, but whether it is possible to do better
prospectively by using self-reported likelihood to turnout measures. This is an important area
for future development.
16


---

G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GG
G
G
G
G
G
G
G
0.0
0.2
0.4
0.6
0.8
1.0
Leave vote by qualifications and 2015 vote
Proportion of 2015 voters
None
Level 1
Level 2
Level 3
Level 4+
Other
Con 2015
Lab 2015
LD 2015
UKIP 2015
SNP/PC 2015
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
0.0
0.2
0.4
0.6
0.8
1.0
Trump vote by education and 2012 vote
Proportion of 2012 voters
No High School
High School
Some College
College
Post Graduate
Republican 2012 voter
Democrat 2012 voter
0.0
0.2
0.4
0.6
0.8
1.0
Conservative 2017 vote by qualifications and 2015 vote
Proportion of 2015 Voters
Does not apply
None
Level 1
Level 2
Level 3
Level 4
Level 5
Other
Con 2015
Lab 2015
LD 2015
UKIP 2015
Green 2015
SNP 2015
PC 2015
Figure 5: Vote choice by qualiﬁcations/education and previous election vote in the EU referen-
dum (lef), in the US presidential election (center), and in the UK general election (right).
5.4
Demographic Patterns
While our focus here has been on the performance of these methods for electoral prediction,
a major beneﬁt of MRP for pre-election polling is that it can reveal politically important demo-
graphic shifs in voting patterns that are occurring in the electorate. A common theme in these
three elections were shifs in voting by age and by education. Here we show the interaction
of education with vote in the preceding election. In the EU referendum, educational qualiﬁca-
tions were very strongly predictive of referendum vote within supporters of a 2015 party. Aside
from 2015 UKIP voters, who supported Leave at very high rates regardless of education level,
among 2015 supporters of all other parties, there are very large diﬀerences in support for Leave
versus Remain by education. Among 2015 Conservative voters, the diﬀerence between those
with no qualiﬁcations (less than GCSEs or equiv) support for Leave was about 20 points higher
than among those with Level 4+ (BA or higher qualiﬁcations). For Labour, Liberal Democrat and
SNP/PC 2015 supporters, these diﬀerences were even larger, reaching 30-40 points. In the US
presidential and UK general elections, education predicted patterns of switching to a consid-
erable extent. Trump disproportionately gained low education Obama voters and retained low
education Romney voters. In the 2017 general election, the Conservatives retained about 90%
of their 2015 voters with lower levels of qualiﬁcations, but only 80% of those with higher levels
of qualiﬁcations. They also gained larger shares of the Liberal Democrat and Labour voters with
low levels of qualiﬁcations than those with high.
6
Conclusion
As we have demonstrated, using MRP to conduct pre-election polling estimates for sub-national
electoral units is promising, but there are several remaining challenges highlighted by the per-
formance of the models that we document. First, there is a general problem of attenuation
bias: the tendency to underpredict voting alternatives where they are strong and overpredict
them where they are weak. We were able to partially mitigate this through the use of cross-level
interactions of individual and constituency/district vote, with varying success across applica-
17


---

tions. Fortunately, attenuation bias tends to lead to larger errors in less competitive electoral
units, and to balance out in the aggregate national estimates. Second, we see undercoverage
of the constituency/district level results in all our applications. The diﬃculty of incorporating
uncertainty due to non-sampling errors into the model estimation makes it diﬃcult to gener-
ate properly calibrated interval estimates, even when error magnitudes are not large. Third, a
major limitation of our strategy is that we do not attempt to model shifs in turnout patterns
at either the individual or aggregate level. While this avoids large errors in the modelled voting
population, and we believe there are good reasons to be skeptical of naive use of self-reported
likelihood to turnout, given suitably rich panel data on likelihood to vote, combined with vali-
dated turnout data, it should be possible to improve on this strategy.
We have not provided explicit performance comparisons of the approach we describe versus
classical methods for adjustment and turnout modelling. This is because it is diﬃcult to do so in
a way that is fair. A comparison on the basis of the national vote totals provides three meaningful
data points, and it is easy for either our methods or standard methods to get lucky through
counterbalancing sources of error. Further, if the same information on the marginal distributions
of the same variables are used for weighting as we used for our post-stratiﬁcation frame, the
aggregate estimates will be nearly identical. A comparison on the basis of sub-national numbers
will favour our method because classical methods are not designed to produce these estimates.
Our primary aim is not to demonstrate that weighting based methods are worse than model
based methods, but rather to demonstrate how MRP methods can be applied to pre-election
polling and that they can provide suﬃciently high quality sub-national vote share estimates in
order to model electoral outcomes in a variety of electoral systems.
Comparing the two elections where the sub-national units matter for electoral outcomes, it
is clear that our strategy performed better in the UK general election than in the US presidential
election. This may be for idiosyncratic reasons having to do with the elections and how we
constructed the models. However it may be that constructing good estimates for 51 states is
actually more diﬃcult than for 632 constituencies, because the latter support more covariates
at the second level of the multilevel regression and provide greater opportunity for errors to
counter-balance. The widely varying state electoral votes make close US elections extremely
sensitive to a few errant state results. Even though we had far more data per US state than per
UK constituency, the diﬃculty of modelling was also greater, as well as the sensitivity of the
aggregate prediction to sub-national prediction errors.
In general, while the setup costs of moving pre-election polling to a model-based approach
are substantial, in these cases we believe that the payoﬀs were also substantial. In each appli-
cation the errors of the national vote share estimates were low, and our estimates were close
to the key results in what turned out to be a close vote. In the two UK cases, the model got
the key national electoral outcome right, and in the US case identiﬁed that a Trump electoral
college victory would be combined with Clinton winning a narrow popular plurality. While the
state-level estimates for the US election suﬀered from signiﬁcant attenuation bias that needs to
be better addressed, the constituency-level estimates for the UK general election outperformed
all benchmarks. Indeed, they were the only pre-election seat forecast that correctly indicated
that the Conservatives would fail to secure a majority.
18


---

Table A1:
Variables included in the vote choice models for each application. The number of
levels is given in brackets for categorical variables.
2016 EU Referendum
2016 US Presidential Election
2017 UK General Election
I – GE2015 vote [7]
I – 2012 vote [5]
I – GE15 vote [9]
I – Qualiﬁcations [6]
I – Qualiﬁcations [5]
I – Qualiﬁcations [8]
I – Age [14]
I – Age [15]
I – Age [14]
I – Gender [2]
I – Gender [2]
I – Gender [2]
I – Days ago [14]
I – Days ago [14]
I – Days ago [7]
I – Race [4]
I – Political Attention [8]
I – Marital status [5]
I – EU16 vote [3]
C – Constituency [632]
D – Congressional District [436]
C – Constituency [632]
C – Region [11]
S – State [51]
C – Region [11]
C – Population density
S – Region [9]
C – Incumbency [3]
C – % EU passport
D – District 2012 vote
C – Standing [2]
C – % Born in UK
S – State 2012 vote
C – Incumbent EU16 position [2]
C – % Christian
C – % ‘Leave’ 2016
C – % Muslim
C – % Long term unemployed
C – % Industry agriculture
C – % Industry manufacturing
C – % Degree
C – Population density
C – % Retired
C – GE15 sharep
C – % Asian
C – % Black
C – % Employed
C – % Long term unemployed
C – Deprivation index
C – UKIP 2015 share
I * I – GE15 vote * Qualiﬁcations
I * D – 2012 vote * District 2012 vote
I * I – EU16 vote * GE15 vote
I * I – GE15 vote * Age
I * I – 2012 vote * Days ago
I * I – Age * GE15 vote
I * S – 2012 vote * Region
C * I * I – GE15 sharep * GE15 vote * EU16 vote
I * I – 2012 vote * Qualiﬁcations
C * I * I – GE15 share2
p * GE15 vote * EU16 vote
I * I – 2012 vote * Race
I * S – Race * State
I * S – Race * Region
I * I – Race * Gender
I * I – Race * Educ
I * I – Race * Age
I * I – Qualiﬁcations * Age
I * I – Qualiﬁcations * Gender
I * S – Gender * Region
Note: I = Individual-level variable; C = Constituency-level variable; D = Congressional district-
level variable; S = State-level variable
19


---

Table A2: Variables included in the turnout models for each application. The number of levels
is given in brackets for categorical variables.
2016 EU Referendum
2016 US Presidential Election
2017 UK General Election
I – GE2015 vote [7]
I – 2012 turnout [3]
I – GE15 turnout [3]
I – Qualiﬁcations [6]
I – Education [5]
I – Qualiﬁcations [8]
I – Age [14]
I – Age [15]
I – Age [14]
I – Gender [2]
I – Gender [2]
I – Gender [2]
I – Marital status [5]
I – Political Attention [8]
I – Race [4]
I – EU16 turnout [3]
C – Constituency [632]
S – State [51]
C – Constituency [632]
C – Region [11]
C – Region [11]
C – Population density
C – Population density
C – % EU passport
C – % Born in UK
C – % Christian
C – % Muslim
C – % Industry agriculture
C – % Degree
C – % Retired
C – % Asian
C – % Black
C – % Employed
C – % Long term unemployed
C – UKIP 2015 share
C – Deprivation index
I * I – Age * Qualiﬁcations
I * I – Age * Qualiﬁcations
I * I – Race * Gender
I * I – Race * Qualiﬁcations
I * I – Race * Age
I * S – Race * State
I * I – State * Qualiﬁcations
I * I – State * Age
I * I – State * Gender
Note: I = Individual-level variable; C = Constituency-level variable
20


---

10
20
30
40
50
60
70
10
20
30
40
50
60
70
Con
 RMSE = 4.44
 Coverage = 0.86
Result
Prediction
20
40
60
80
20
40
60
80
Lab
 RMSE = 4.67
 Coverage = 0.87
Result
Prediction
0
10
20
30
40
50
60
0
10
20
30
40
50
60
LD
 RMSE = 2.46
 Coverage = 0.88
Result
Prediction
0
10
20
30
40
50
60
0
10
20
30
40
50
60
Green
 RMSE = 1.06
 Coverage = 0.94
Result
Prediction
0
5
10
15
20
25
0
5
10
15
20
25
UKIP
 RMSE = 2.8
 Coverage = 0.48
Result
Prediction
20
30
40
50
20
30
40
50
SNP
 RMSE = 3.32
 Coverage = 0.98
Result
Prediction
0
10
20
30
40
0
10
20
30
40
PC
 RMSE = 3.59
 Coverage = 0.92
Result
Prediction
Figure A1: Predicted vs actual vote shares for UK parties by parliamentary constituency in the 2017 UK general election.
21


---

References
Bernstein, R., A. Chadha, and R. Montjoy (2001). Overreporting voting: Why it happens and why
it matters. Public Opinion Quarterly 65, 22–44.
Carpenter, B., A. Gelman, M. D. Hoﬀman, D. Lee, B. Goodrich, M. Betancourt, M. Brubaker, J. Guo,
P. Li, and A. Riddell (2017). Stan: A probabilistic programming language. Journal of Statistical
Sofware 76(1).
Gelman, A. and T. C. Little (1997). Poststratiﬁcation into many categories using hierarchical logistic
regression. Survey Methodology 23(2), 127–135.
Hanretty, C. (2017). Electionforecast.co.uk.
Hanretty, C., B. Lauderdale, and N. Vivyan (2016a). Combining national and constituency polling
for forecasting. Electoral Studies 41, 239–243.
Hanretty, C., B. E. Lauderdale, and N. Vivyan (2016b). Comparing strategies for estimating con-
stituency opinion from national survey samples. Political Science Research and Methods,
1–21.
Holbrook, A. L. and J. A. Krosnick (2010). Social desirability bias in voter turnout reports: Tests
using the item count technique. Public Opinion Quarterly 74(1), 37–67.
Jackman, S. (2005). Pooling the polls over an election campaign. Australian Journal of Political
Science 40(4), 499–517.
Jackman, S. and B. Spahn (2016). ”why does the american national election study overestimate
voter turnout?”. Working Paper.
Jennings, W. and C. Wlezian (2017). Election polling errors across time and space. Working Paper.
Lax, J. R. and J. H. Phillips (2009). How should we estimate public opinion in the states? American
Journal of Political Science 53(1), 107–121.
Leemann, L. and F. Wasserfallen (2017a). Extending the use and prediction precision of subna-
tional public opinion estimation. American Journal of Political Science.
Leemann, L. and F. Wasserfallen (2017b). Extending the use and prediction precision of subna-
tional public opinion estimation. American Journal of Political Science.
Linzer, D. A. (2013). Dynamic bayesian forecasting of presidential elections in the states. Journal
of the American Statistical Association 108(501), 124–134.
Park, D. K., A. Gelman, and J. Bafumi (2004). Bayesian multilevel estimation with poststratiﬁca-
tion: State-level estimates from national polls. Political Analysis 12(4), 375–385.
Rivers, D. and D. Bailey (2009). Inference from matched samples in the 2008 u.s. national elec-
tions. American Association of Public Opinion Research – Joint Statistical Meetings.
Rivers, D. and A. Wells (2015). Polling error in the 2015 uk general election: An analysis of yougov’s
pre and post-election polls. Technical report, YouGov.
22


---

Selb, P. and S. Munzert (2011). Estimating constituency preferences from sparse survey data using
auxiliary geographic information. Political Analysis 19(4), 455–470.
Silver, N. (2017). 538 2016 election forecast.
Sturgis, P., N. Baker, M. Callegaro, S. Fisher, J. Green, W. Jennings, J. Kuha, B. Lauderdale, and
P. Smith (2016). Report of the inquiry into the 2015 british general election opinion polls.
Technical report, British Polling Council.
Tausanovitch, C. and C. Warshaw (2013). Measuring constituent policy preferences in congress,
state legislatures, and cities. The Journal of Politics 75(2), 330–342.
Wang, W., D. Rothschild, S. Goel, and A. Gelman (2014).
Forecasting elections with non-
representative polls. International Journal of Forecasting 31(3), 980–991.
23

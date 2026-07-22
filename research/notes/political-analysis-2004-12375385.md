---
title: Political Analysis (2004) 12:375–385
id: political-analysis-2004-12375385
tags:
- mrp
- academic-paper
- mrp-canonical
- mrp-foundational
created: '2026-07-21T18:35:36.606044Z'
updated: '2026-07-21T18:39:17.780963Z'
source: https://sites.stat.columbia.edu/gelman/research/published/parkgelmanbafumi.pdf
source_domain: sites.stat.columbia.edu
fetched_at: '2026-07-21T18:35:36.605832Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Park, Gelman & Bafumi (Political Analysis, 2004) — THE canonical MRP paper
  that introduced multilevel regression + poststratification for estimating state-level
  opinion from national polls, building on Gelman & Little (1997) and extending the
  ''synthetic voter type'' approach pioneered by Pool et al. (1965, 480 types) and
  Weber et al. (1972-73, 960 types) to 3,264 demographic-x-state cells (sex x ethnicity
  x 4 age categories x 4 education categories x 50 states + DC). Two-step procedure:
  (1) fit a multilevel logistic regression for individual binary response y given
  demographics and state of residence, producing a shrinkage-estimated average response
  p_j for every cross-classified cell j; (2) reweight cell estimates by their US Census
  adult population counts N_j to produce a population-weighted state average. Validated
  against actual 1988 and 1992 US presidential vote outcomes using CBS News/New York
  Times pre-election polls; multilevel modeling is shown to outperform both ''no pooling''
  (raw disaggregation, unacceptably variable with sparse per-state samples) and ''complete
  pooling'' (national average applied uniformly, which suppresses real state-level
  variation) baseline estimators. Explicitly states the authors'' primary intended
  use case is NOT election forecasting but estimating public opinion on general policy
  issues at the state level — pre-election polls were chosen merely because they are
  conveniently externally validatable against a known outcome.'
raw_file: raw/political-analysis-2004-12375385.pdf
---

*Suggested by [[how-the-yougov-model-for-the-2017-general-election-works]] — canonical Park/Gelman/Bafumi 2004 MRP paper cited by Lauderdale et al. and requested by batch instructions*

Political Analysis (2004) 12:375–385
doi:10.1093/pan/mph024
Bayesian Multilevel Estimation with
Poststratification: State-Level Estimates
from National Polls
David K. Park
Department of Political Science and Applied Statistics,
Washington University, St. Louis, MO 63130
e-mail: dpark@artsci.wustl.edu
Andrew Gelman
Departments of Statistics and Political Science, Columbia University,
New York, NY 10027
e-mail: gelman@stat.columbia.edu
Joseph Bafumi
Department of Political Science, Columbia University, New York, NY 10027
We ﬁt a multilevel logistic regression model for the mean of a binary response variable
conditional on poststratiﬁcation cells. This approach combines the modeling approach often
used in small-area estimation with the population information used in poststratiﬁcation (see
Gelman and Little 1997, Survey Methodology 23:127–135). To validate the method, we
apply it to U.S. preelection polls for 1988 and 1992, poststratiﬁed by state, region, and the
usual demographic variables. We evaluate the model by comparing it to state-level election
outcomes. The multilevel model outperforms more commonly used models in political
science. We envision the most important usage of this method to be not forecasting
elections but estimating public opinion on a variety of issues at the state level.
1
Introduction
Hundreds of national opinion polls are conducted every year. These polls may, among
other things, inform election prospects or reveal issue stances among the public. They are
generally based on national random digit dialing with corrections for nonresponse based
on demographic factors such as sex, ethnicity, age, and education. Often it is desirable to
estimate opinions at lower levels such as individual states or congressional districts.
Certainly scholars and politicians interested in public opinion (and political responses to
opinion) would ﬁnd such data enormously useful and interesting. While some state-level
polling is conducted, their nonuniformity hinders comparisons among states.
Political Analysis, Vol. 12 No. 4,  Society for Political Methodology 2004; all rights reserved.
Authors’ note: We thank the reviewers for their helpful comments and the National Science Foundation for
ﬁnancial support.
375


---

One of the ﬁrst projects to use national opinion polls to estimate opinions at the state level
was undertaken by Pool et al. (1965). They used national polls and voting and census data to
construct 480 synthetic voter types based on a variety of socio-demographic factors.1 They
determined the percent of each type in each state and estimated state-level results. In the early
1970s, Weber et al. (1972–1973) expanded the number of voter types from 480 to 960
categories and were able to estimate state-level opinions on a variety of issues (for recent
research on state-level estimates, see Erikson et al. 1993, Berry et al. 1998, and Brace et al.
2002).
We extend the work of Pool et al. (1965) and Weber et al. (1972–1973) by expanding the
number of synthetic voter types from 960 to 3264 and, more important, ﬁtting a multilevel
regression model while simultaneously correcting for nonresponse. In addition to allowing
for more categories, our work moves beyond these precursors in political science by
performing shrinkage estimation for individual categories and sets of categories (e.g., states).
We demonstrate the method by application to a set of 1988 and 1992 national
preelection polls. This is a useful testing ground for our method because polls immediately
before an election can be externally validated by comparing them to the vote outcomes.
Thus we apply our method to preelection polls not to forecast elections but rather to
provide an improved estimate for state-level opinions. Preelection polling is simply
a convenient and easily validated example (see Jackman and Rivers 2001 for a recent
example of state-level election forecasting via a dynamic Bayesian hierarchical model).
2
Overview
We construct a multilevel logistic regression model for the mean of a binary response
variable conditional on poststratiﬁcation cells. This approach combines the modeling
approach often used in small-area estimation with the population information used in
poststratiﬁcation (Gelman and Little 1997). The procedure has two steps:
1. Fit a multilevel regression model2 for the individual response y given demographics
and state of residence. This model thus estimates an average response for each cross
classiﬁcation j of demographics and state, pj. In our example, we have sex (male
or female), ethnicity (African-American or other), age (4 categories), education (4
categories), and 50 states, for a total of 3200 categories. If the District of Columbia
is included, we have 3264 categories. The demographic categories we use are those
used by national survey organizations in their weighting (see Voss et al. 1995).
2. From the U.S. census, we get the adult population Nj for each category j. The
estimated population average of the response y in any state s is then
hs ¼
P
js Njpj
P
js Nj
;
with each summation over the 64 demographic categories in the state.
1The project was also the basis for a satirical novel by Eugene Burdick (1964) titled The 480.
2Many statistical applications involve multiple parameters that can be regarded as related in some way by the
structure of the problem, implying that a joint probability model for these parameters should reﬂect the
dependence among them. It is natural to model such a problem within a multilevel framework, with observable
outcomes modeled conditionally on certain parameters, which themselves are given a probabilistic speciﬁcation
in terms of further parameters. See Kreft and de Leeuw (1998), Snijders and Bosker (1999), Bryk and
Raudenbush (2001), and Gelman et al. (2003) for introductions to multilevel models from classical and Bayesian
perspectives.
376
David K. Park, Andrew Gelman, and Joseph Bafumi


---

This procedure uses a large number of categories because (a) we are interested in
separating out the response by state, and (b) nonresponse adjustments force us to include
the demographics. As a result, any given survey will have few or no data in many
categories. This is not a problem, however, if a multilevel model is ﬁtted. Each factor or set
of interactions in such a model is automatically given a variance component. This
inferential procedure works well and outperforms standard survey weighted estimates
when estimating state-level outcomes.
3
The Model
3.1
Multilevel Logistic Regression Model for Binary Data
We label the survey response yi as 1 for supporters of the Republican candidate and 0 for
supporters of the Democrat (with the undecideds excluded), with Pr(yi ¼ 1) ¼ logit1(Xbi).
More generally, the model could apply to any yes/no survey response. The respondent-level
design matrix X is all 0’s and 1’s with indicators for the demographic variables in survey
weighting: sex, ethnicity, age, education, interaction of sex and ethnicity, and age and
education.3 We also include in X indicators for the 50 states plus the District of Columbia
and for the ﬁve regions of the country (Northeast, Midwest, South, West, and the District of
Columbia, which is considered as a separate region because of its distinctive voting
patterns). As part of a general approach for multilevel models, we give each batch of
regression coefﬁcients with greater than two groups an independent normal distribu-
tion centered at 0 and with standard deviation estimated from data. This allows us to
estimate these parameters as varying effects, taking advantage of the multilevel structure of
the data.
There is no gain to multilevel modeling for batches with J , 3 groups when prior
distributions are noninformative (see, e.g., Gelman et al. 2003 and Gelman 2004), so for
simplicity we model sex and ethnicity as regression coefﬁcients with no multilevel
structure. The data model looks as follows:
Prðyi ¼ 1Þ ¼ logit1ðb0 þ bfemale femalei þ bblack blacki
þ bfemale:black femaleiblacki þ bage
ageðiÞ
þ bedu
eduðiÞ þ bage:edu
ageðiÞ;eduðiÞ þ bstate
stateðiÞÞ:
ð1Þ
We then set up a state-level model with region indicators and a measure of previous
Republican vote share as predictors:
bstate
j
; Nðbregion
regionðjÞ þ bv:prevv:prevj; r2
stateÞ:
More precisely, v.prev is the average Republican vote share in the three previous elections,
adjusted for home-state and home-region effects in the previous election.
We assign normal distributions to the varying coefﬁcients. These distributions have
means 0 (no loss of generality given the inclusion of the constant term b0 in the data
3These are the interactions used by polling organizations for survey weighting (see Voss et al. 1995). The goal of
our demographic adjustments is not to estimate demographic parameters but to adjust for demographics during
poststratiﬁcation.
377
Bayesian Multilevel Estimation


---

model) and standard deviations rage, redu, rage,edu, rregion, estimated from data given
noninformative uniform prior densities.4
3.2
Generalizations of the Model
There are certain generalizations that are particularly appropriate for the study of public
opinion. Here we brieﬂy outline how to extend the model in two ways: handling leaners
and undecided voters, and restricting to subsets of the population such as registered or
likely voters, or supporters of the two major parties. The model can be generalized in other
ways, such as including effects for survey organizations by adding appropriate group-level
predictors (Jackman and Rivers 2001).
First, leaners are traditionally included as full supporters of candidates, and voters who are
undecided or express no opinion are typically treated as missing data or discarded. These
data-analytic simpliﬁcations are generally reasonable in the context of U.S. politics (see, e.g.,
Gelman and King 1993). In other opinion settings, however, it might be more informative to
include the partial information provided by intermediate responses. Our model can be
immediately generalized to an ordered probit to directly model intermediate opinions.
Second, this model can be made more complicated to account for turnout and third-
party candidates. For example, consider the 1992 presidential election. In that election,
there was an unexpectedly large voter turnout rate that accompanied a particularly strong
showing for a third-party candidate. Thus we estimate three separate models. In the ﬁrst
model, we label the survey response yi as 1 for respondents registered or expected to vote
and 0 for everyone else. The second model is restricted to the respondents who were
registered or expected to vote; in this second model, yi ¼ 1 for all respondents who are
expected to vote for either of the two major-party candidates and 0 for everyone else. The
third model is restricted to the respondents who were registered or expected to vote and
who expressed a preference for one of the two major-party candidates. Then the proportion
of registered or likely voters in any state s who support the Republican candidate, among
those with a major-party preference, is
h1992
s
¼
P
js Njp1
j p2
j p3
j
P
js Njp1
j p2
j
;
where p1
j , p2
j , p3
j are the vectors of cell probabilities for each of the three models, and with
each summation over the 64 demographic categories in the state.
4
Data
For 1988 and 1992, we use a CBS News/New York Times national poll conducted during the
week before the U.S. Presidential elections. In 1988, there were a total of 2193 respondents in
the sample; in 1992 there were 4650 respondents. Following the standard convention, we
place leaners among the full supporters. Respondents were excluded if any of the categories
for sex, ethnicity, age, or education were missing. Even though no data were included from
Alaska and Hawaii, they are included in the model. The preferences in these states are
estimated based on the demographic coefﬁcients and previous Republican vote share.
4Various noninformative prior distributions have been suggested for scale parameters in multilevel models.
Gelman (2004) demonstrates that serious problems exist with the inverse-gamma family of noninformative prior
distributions and suggests the use of a uniform prior on the multilevel standard deviation parameters.
378
David K. Park, Andrew Gelman, and Joseph Bafumi


---

The Census Bureau provides the joint adult population distributions of the demographic
variables within each state.5 For example, we know from the census that there were 66,177
adults who lived in Alabama, were male, not black, aged 18–29, and did not have a high
school diploma.
5
The Estimated Model
5.1
Fitting the Model
We ﬁt the model using the Bayesian software WinBUGS (Spiegelhalter et al. 1999) as
called from R (R Development Core Team 2003) using Gelman’s (2003) Bugs.R. We use
a multiplicative and additive redundant parameterization to speed convergence. The Gibbs
sampler can be slow to converge because of posterior dependence among parameters.
Paradoxically, adding new parameters, thus performing the random walk in a larger space,
can reduce dependence in the larger parameter set and improve the convergence of the
Markov chain simulation.6
Approximate mixing of three parallel simulated chains was achieved after 5000
iterations.7 We construct summary plots of the multilevel model. With a binary outcome,
we plot Pr(y ¼ 1) ¼ E(y) as a function of the predictors. Because the model has many
predictors, instead of plotting E(y) as a function of each of the demographic inputs, we plot
E(y) as a function of the combined linear predictor:
ui ¼ bfemale femalei þ bblack blacki þ bfemale:black femalei blacki
þ bage
ageðiÞ þ bedu
eduðiÞ þ bage:edu
ageðiÞ;eduðiÞ:
The estimates, 50% intervals, and 95% intervals8 for the demographic coefﬁcients are
displayed in Fig. 1. As can be seen from the graph, the demographic factors other than
ethnicity are estimated to have little predictive power for this particular example. The
multilevel model tends to shrink the coefﬁcient estimates to zero. This is particularly true
for the 16 age and education interactions. However, we follow the lead of the polling
organization in keeping these predictors in the model since they can be important for some
survey questions.
The regression prediction can then be written as
Prðyi ¼ 1Þ ¼ logit1ðb0 þ bstate
stateðiÞ þ uiÞ;
where ui represents the combined linear predictor. We can plot this for each state. Figure 2
shows the result for a selection of eight states. The solid lines display the estimated logistic
5Census of Population and Housing 1990: Subject Summary Tape File (SSTF) 6, Education in the United States.
6For further discussion on efﬁcient Gibbs samplers for multilevel models, see Gelman et al. (2003), sections 11.8
and 15.4.
7We independently simulated three sequences with starting points drawn from an overdispersed distribution. We
monitored convergence by computing the potential scale reduction, ^R, for all scalar estimands of interest and
continued the simulation until ^R was near 1 for all estimands of interest.
8A Bayesian (probability) interval for an unknown quantity of interest can be regarded as having a high probability
of containing the unknown quantity, in contrast to a frequentist (conﬁdence) interval, which may be strictly
interpreted only in relation to a sequence of similar inferences that might be made in repeated practice. Increased
emphasis has been placed on interval estimation rather than hypothesis testing, and this provides a strong impetus
to the Bayesian viewpoint, since it seems likely that most users of standard conﬁdence intervals give them
a common-sense Bayesian interpretation (Gelman et al. 2003).
379
Bayesian Multilevel Estimation


---

regression in each state; thus in any state the probability of supporting, George Bush
ranges from about 10% to 70% depending on the demographic variables, most importantly
ethnicity. Roughly speaking, African-Americans have about a 10% probability of
supporting Bush while others have about a 60% probability. Other demographic variables
only slightly affect the predicted probability. The variation among states is fairly small but
turns out to be important in allowing us to estimate average opinion by state. Changes of
only a few percent in preferences can have a large political impact.
The gray lines on the graphs represent uncertainty in the state-level coefﬁcients, bstate
j
.
Alaska has no data at all, but the inference there is still reasonably precise—its bstate
j
is
estimated from its previous election outcome, its demographic and regional predictors
(Alaska is categorized as a western state), and the distribution of the errors from the state-
level regression. In general, the larger states such as California have more precise estimates
than the smaller states such as Delaware; with more data in a state j, it is possible to
estimate bstate
j
more accurately.
Figure 3 displays the estimated logistic coefﬁcients for the 50 states, grouping them by
region and, within each region, showing the multilevel regression on v.prev, the measure of
Republican vote in the state in previous presidential elections. Region and previous vote
give good but not perfect predictions of the state-level coefﬁcients in the public opinion
model.
female
black
female x black
18−29
30−44
45−64
65+
no h.s.
high school
some college
college grad
18−29 x no h.s.
18−29 x high school
18−29 x some college
18−29 x college grad
30−44 x no h.s.
30−44 x high school
30−44 x some college
30−44 x college grad
45−64 x no h.s.
45−64 x high school
45−64 x some college
45−64 x college grad
65+ x no h.s.
65+ x high school
65+ x some college
65+ x college grad
−2.5
−2.5
−2
−2
−1.5
−1.5
−1
−1
−0.5
−0.5
0
0
0.5
0.5
1
1
Fig. 1
Estimates, 50% intervals, and 95% intervals for the demographic coefﬁcients in the logistic
regression of the probability of supporting George Bush in polls before the 1988 presidential
election. Recall that a change of x on the logistic scale corresponds to a change of at most x/4 on the
probability scale. Thus demographic factors other than ethnicity have very small estimated predictive
effects on vote preference.
380
David K. Park, Andrew Gelman, and Joseph Bafumi


---

5.2
Using the Model Inferences to Get State-Level Estimates
The logistic regression model gives the probability that any adult will prefer Bush, given
the person’s sex, ethnicity, age, education, and state. We can now compute weighted
averages of these probabilities to represent the proportion of Bush supporters in any
speciﬁed subset of the population.
We ﬁrst compute the expected response ypred—the probability of supporting Bush for
each of the categories j ¼ 1, . . ., J ¼ 3264 deﬁned by the model. Since we have 1000
simulation draws, we compute a 1000 3 3264 matrix in R:
ypred ¼ logit1ðb0 þ bfemale femalej þ bblack blackj
þ bfemale:black femalej blackj þ bage
ageðjÞ
þ bedu
eduðjÞ þ bage:edu
ageðjÞ;eduðjÞ þ bstate
stateðjÞÞ
ð2Þ
for j ¼ 1 to 3264. This is the same as Eq. (1) except with j in place of i, a notational change
we make to emphasize that now that we have ﬁt the model, we are applying it to
population categories j rather than survey respondents i.
−2.0
−1.0
0.0
0.0
0.4
0.8
Alaska
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
Arizona
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
Arkansas
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
California
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
Colorado
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
Connecticut
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
Delaware
linear predictor
Pr (support Bush)
−2.0
−1.0
0.0
0.0
0.4
0.8
District of Columbia
linear predictor
Pr (support Bush)
Fig. 2
Estimated probability of a survey respondent supporting Bush for president in 1988 as
a function of the linear predictor for demographics in each state (displaying only a selection of eight
states to save space). Dots show the data (y-jittered for visibility), and the heavy and light lines show
the median estimate and 20 random simulation draws from the estimated model.
Northeast
R vote in prev elections
regression intercept
0.5
0.6
0.7
−0.5
0.5
CT
ME
MD
NH
NJ
PA
RI
VT
WV
Midwest
IL
INKS
MN
NE
ND
OH
SD
South
FL
GA
LA
NC OK
SC
TN
TX
VA
West
AK
AZ
CA
CO
HI
ID
MT NV
NM
OR
UT
WA
WY
0.0
0.5
0.6
0.7
0.5
0.6
0.7
0.5
0.6
0.7
R vote in prev elections
R vote in prev elections
R vote in prev elections
regression intercept
−0.5
0.5
0.0
regression intercept
−0.5
0.5
0.0
regression intercept
−0.5
0.5
0.0
NY
MOMI
WI
IA
AR
KY
MS
AL
DE
MA
Fig. 3
Estimates and 50% intervals for the state coefﬁcients bstate
j
, plotted versus previous state vote
v.prevj, in each of the four regions of the United States in 1988. The estimated group-level regression
line, bstate
j
¼ bregion
k
þ bv:prev
j
 v.prevj, is overlaid on each plot (corresponding to the regions k ¼ 1,2,3,4).
381
Bayesian Multilevel Estimation


---

We use the notation Nj for the number of adults as obtained from the 1990 census and pj
to represent the probability of supporting Bush for each category j. For each state s, we are
estimating the average response in the state,
ypred
s
¼
P
js Njpj
P
js Nj
;
summing over the 64 demographic categories within each state. The above calculations
work because we have already prepared a 3264 3 6 matrix from the 1990 census, with
columns N, indicators for female and ethnicity, and indexes for age, education, and state.
We can then summarize these 1000 simulations to get a point prediction and uncertainty
intervals for the proportion of adults in each state who supported Bush at the time of the
surveys.
5.3
Comparing Public Opinion Estimates to Election Outcomes
The estimates of the model come from opinion polls taken just before the election, and
they can be externally validated by comparing them to the actual outcomes. We can thus
treat this as a sort of laboratory for testing the accuracy of multilevel models and any other
methods that might be used to estimate state-level opinions from national polls.
Figure 4 shows the actual outcomes for each state in 1988, compared to the model-
based estimates of the proportion of Bush supporters. Validating by comparing to the
actual election, the ﬁt is pretty good, with no strong systematic bias and an average
absolute error of only 4.0%; for 1992 it is 3.5%.
By comparison, Fig. 5 shows the predictive performance of the estimates based on
complete pooling of states (estimating opinion based solely on demographics, thus setting
bstate
j
¼ 0 for all states) and no pooling (corresponding to completely separate estimates for
each state, thus setting rstate ¼ rregion ¼ ‘) for 1988. The complete pooling model
generally shrinks the state estimates too close toward the mean, whereas the no-pooling
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
multilevel model
1988
Estimated Bush support
Actual election outcome
0.40
0.50
0.60
0.40
0.50
0.60
multilevel (excluding D.C.)
Actual election outcome
Estimated Bush support
a
b
Fig. 4
For each state, the proportion of the two-party vote received by George Bush in 1988, plotted
versus the support for Bush in the state, as estimated from a multilevel model (a) applied to pre-
election polls. The second plot (b) excludes the District of Columbia in order to more clearly show
the 50 states.
382
David K. Park, Andrew Gelman, and Joseph Bafumi


---

model does not shrink enough. To make a numerical comparison, the mean absolute error
of the state estimates is 4.0% for the multilevel analysis, compared to 5.4% for complete
pooling and 10.4% for no pooling. For 1992, Fig. 6 compares the multilevel and no-
pooling models. Similar to 1988, the no-pooling model does not shrink enough. The mean
absolute error of the state estimates is 3.5% for the multilevel analysis, compared to 9.7%
for the no-pooling model.9
6
Discussion
We generated estimates of state-level vote choice opinions employing national data. The
accuracy of these estimates was shown by comparison to actual vote outcomes. We use
a Bayesian approach in this paper because of its generality and conceptual simplicity
(Gelman et al. 2003); however, the key is really the placing of the model within
a multilevel framework. Multilevel modeling is appropriate since the data have
a hierarchical demographic and geographic structure (see Kreft and de Leeuw 1998;
Snijders and Bosker 1999; Bryk and Raudenbush 2001). This pattern of interlocking
clustering is common in data sets employed by social scientists.
As we have seen in this paper, multilevel modeling outperforms the simpler complete-
pooling and no-pooling estimates, which is no surprise: not pooling ignores information
and can give unacceptably variable inferences, and complete pooling suppresses variation
that can be important or even the main objective of a study. These extreme alternatives can
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
complete pooling (no state effects)
1988
Estimated Bush support
Actual election outcome
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
no pooling of state effects
Estimated Bush support
Actual election outcome
a
b
Fig. 5
For each state, Bush’s vote in 1988 plotted versus his support in the polls, as estimated from
(a) the complete-pooling model (using demographics alone with no state predictors), and (b) the no-
pooling models (estimating each state separately). The three states in the no-pooling model with
estimated 100% support for Bush were Utah (n ¼ 12), Vermont (n ¼ 2), and Wyoming (n ¼ 2). The
complete-pooling and no-pooling models correspond to rstate ¼ rregion ¼ 0 and ‘, respectively.
Compare to Fig. 4a, which shows results from the multilevel model (with rstate and rregion estimated
from data).
9We use the three-step model to correct for nonregistrants and supporters of other candidates (mostly Perot). We
do not bother to include the complete-pooling model for 1992 because, as seen in 1988, it generally shrinks the
state estimates too close to the mean and therefore does not offer a credible alternative to the multilevel model.
383
Bayesian Multilevel Estimation


---

in fact be useful as preliminary estimates, but ultimately we prefer the partial pooling that
comes out of a multilevel analysis.
We adopt multilevel modeling to the sample survey context via poststratifying, using
census data to weight our estimates by demographic characteristics per state. This allows
us to use all the information in classical survey weights (in contrast to some modeling
approaches that do not use information relevant to the data collection). In survey
terminology, poststratiﬁcation allows our estimates to correct for nonresponse bias as well
as would be done using classical weighting.
Moving forward, multilevel modeling and poststratiﬁcation can be used to estimate
state-level opinions on a variety of topics, such as ideology, partisanship, death penalty
attitudes, or spending on the poor (Park 2004). Further, opinions can be estimated at levels
other than the state. For example, researchers may be interested in estimating the opinions
of populations in congressional districts or counties. It will also be interesting to study time
trends in state and local opinions. We leave this to future research.
References
Berry, W. D., E. J. Ringquist, R. C. Fording, and R. L. Hanson. 1998. ‘‘Measuring Citizen and Government
Ideology in the American States, 1960–93.’’ American Journal of Political Science 42:327–348.
Brace, P., K. Sims-Butler, K. Arcenaux, and M. Johnson. 2002. ‘‘Public Opinion in the American States: New
Perspectives Using National Survey Data.’’ American Journal of Political Science 46:173–189.
Bryk, A. S., and S. W. Raudenbush. 2001. Hierarchical Linear Models: Applications and Data Analysis
Methods, 2nd ed. Thousand Oaks, CA: Sage.
Burdick, E. 1964. The 480. New York: McGraw-Hill.
Erikson, R. S., G. C. Wright, and J. P. McIver. 1993. Statehouse Democracy: Public Opinion and Policy in the
American States. Cambridge: Cambridge University Press.
Gelman, A. 2003. Bugs.R: Functions for Calling Bugs from R. (Available from http://www.stat.columbia.edu/
;gelman/bugsR.)
Gelman, A. 2004. ‘‘Prior Distributions for Variance Parameters in Hierarchical Models.’’ Unpublished manuscript.
Gelman, A., J. B. Carlin, H. S. Stern, and D. B. Rubin. 2003. Bayesian Data Analysis, 2nd ed. London: Chapman
and Hall.
Gelman, A., and G. King. 1993. ‘‘Why Are American Presidential Election Campaign Polls So Variable When
Votes Are So Predictable?’’ British Journal of Political Science 23:409–451.
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
multilevel model
1992
Estimated Bush support
Actual election outcome
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
no pooling of state effects
Estimated Bush support
Actual election outcome
a
b
Fig. 6
For each state, Bush’s vote in 1992 plotted versus his support in the polls, as estimated from
(a) the multilevel model, and (b) the no-pooling model (estimating each state separately). The no-
pooling model corresponds to rstate ¼ rregion ¼ ‘.
384
David K. Park, Andrew Gelman, and Joseph Bafumi


---

Gelman, A., and T. C. Little. 1997. ‘‘Postratiﬁcation into Many Categories Using Hierarchical Logistic
Regression.’’ Survey Methodology 23:127–135.
Jackman, S., and D. Rivers. 2001. ‘‘State Level Election Forecasting during Election 2000 via Dynamic Bayesian
Hierarchical Modeling.’’ Presented at the Annual Meeting of the American Political Science Association, San
Francisco, CA.
Kreft, I. G. G., and J. de Leeuw. 1998. Introducing Multilevel Modeling. Thousand Oaks, CA: Sage.
Park, D. 2004. ‘‘Multilevel Models of Representation in the U.S. States.’’ Ph.D. dissertation. Department of
Political Science, Columbia University.
Pool, I. d. S., R. P. Abelson, and S. L. Popkin. 1965. Candidates, Issues, and Strategies. Cambridge, MA: MIT
Press.
R Development Core Team. 2003. R: A Language and Environment for Statistical Computing. Vienna, Austria:
R Foundation for Statistical Computing. (Available from http://www.R-project.org.)
Snijders, T. A. B., and R. Bosker. 1999. Multilevel Analysis: An Introduction to Basic and Advanced Multilevel
Modeling. Thousand Oaks, CA: Sage.
Spiegelhalter, D., A. Thomas, and N. Best. 1999. WinBugs Version 1.4. Cambridge, UK: MRC Biostatistics Unit.
Voss, D., A. Gelman, and G. King. 1995. ‘‘Preelection Survey Methodology: Details from Eight Polling
Organizations, 1988 and 1992.’’ Public Opinion Quarterly 59:98–132.
Weber, R. E., A. H. Hopkins, M. L. Mezey, and F. Munger. 1972–1973. ‘‘Computer Simulation of State
Electorates.’’ Public Opinion Quarterly 36:49–65.
385
Bayesian Multilevel Estimation

---
title: The Role of Confounders and Linearity in
id: the-role-of-confounders-and-linearity-in
tags:
- inference-ecologique
- ei-empirique
- ei-methodologie
- confondeurs
created: '2026-07-21T18:28:14.718957Z'
updated: '2026-07-21T18:39:17.618718Z'
source: https://arxiv.org/pdf/2601.07668
source_domain: arxiv.org
fetched_at: '2026-07-21T18:28:14.718578Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Kuriwaki & McCartan (arXiv 2601.07668, July 2026) reassess ecological inference
  by placing it in a missing-data/causal-inference framework: they formalize a coarsening-at-random
  (CAR) identification condition analogous to selection-on-observables, and show the
  accounting identity forces the outcome to be partially linear in category shares
  — motivating a doubly-robust estimator (''seine'', McCartan and Kuriwaki 2025) that
  plugs covariates into this linear structure. Empirically, using ground-truth validation
  datasets, they find EVERY tested method (Goodman regression, King''s 1997 EI, Rosen
  et al.''s RxC multinomial-Dirichlet, Thomsen) systematically overestimates racial
  polarization in voting (e.g. King''s model estimates a 72-point White-Black Democratic
  registration gap vs. a true 54-point gap) and underestimates ticket-splitting (true
  rate 16% in WI-08 vs. 9% from best-fit line; national CD-level mean absolute error
  ~3.4 points, all methods biased in the same direction). The Thomsen model achieves
  the lowest mean absolute error for ticket-splitting among all methods tested but
  is limited to the 2x2 case with no covariates and no local (precinct-level) estimates.
  A key mechanism identified: CAR violations arise because ticket-splitters/racial
  minorities are non-randomly distributed across geographies in ways correlated with
  the outcome (e.g. concentrated-area Black voters are more Democratic-leaning than
  dispersed-area Black voters), which is exactly the French bureau-de-vote context
  risk (urban/rural composition effects).'
raw_file: raw/the-role-of-confounders-and-linearity-in.pdf
---

The Role of Confounders and Linearity in
Ecological Inference: A Reassessment
Shiro Kuriwaki‗
Department of Political Science
Yale University
Cory McCartan
Department of Statistics
Pennsylvania State University
July 2026
Abstract
Estimating conditional means using only the marginal means available from aggregate
data is known as the ecological inference problem. We reassess this literature, arguing that
it has understudied two issues: how practitioners should control for confounding, and
how methodologists can leverage the linearity inherent in the structure of the problem. On
the former, we formalize ignorability conditions like those in causal inference and outline
consistent plug-in estimators: These are credible when covariates make the ignorability
condition plausible. On the latter, we show that aggregation restricts the target function
to be partially linear.
Such linearity clarifies the connections between King’s (1997)
methodology, its predecessors, and subsequent developments. That motivates a recent
doubly-robust technique that enters covariates flexibly while leveraging linearity. Finally,
we test these methods in datasets where the ground truth is fortuitously observed. In these
common applications, all methods tested were prone to overestimating racial polarization
and underestimating split-ticket voting.
1
Introduction
Estimating conditional means with only marginal means that come from aggregate data
is commonly known as the ecological inference problem (EI). These estimation challenges
are central in many political science applications, where for example voters’ choices and
administrative data are aggregated to geographical districts.1 Researchers since Robinson
(1950) have been aware that such relationships between aggregate data may not correspond
to the underlying relationship between individuals, calling incorrect inferences an ecological
fallacy. They have produced a long literature with statistical methods to make valid inferences
from aggregate data. Even after the publication of King’s (1997) A Solution to the Ecological
‗To whom correspondence should be addressed. Email: shiro.kuriwaki@yale.edu. We thank P. M. Aronow,
Adam Chapnik, Gary King, Mason Reece, and Jesse Shapiro for helpful comments.
1. Substantive questions that grapple with these ecological inference problems include: the degree of racially
polarized voting (Greiner and Quinn 2010), the gender gap (Teele 2024), the prevalence of ticket splitting (Burden
and Kimball 2009), the role of job loss on voting for Brexit (Colantone and Stanig 2018), and partisan differences
in pandemic exposure (Elzayn et al. 2025). While others use survey data to circumvent the ecological inference
problem (Baccini and Weymouth 2021), survey samples and self-reported vote choice may be unrepresentative.
The same problem arises in economics (where consumers’ purchasing choices for goods are aggregated into
regional markets), public health (where residents’ health outcomes are aggregated into census areas to preserve
privacy), and other disciplines that use census statistics.
1
arXiv:2601.07668v2  [stat.AP]  1 Jul 2026


---

Confounders and Linearity in Ecological Inference
Inference Problem, over twenty distinct sets of authors have proposed methods and adjustments
for ecological inference (Appendix A).
Despite the range of existing methods, the concern persists that aggregate data could result
in an ecological fallacy. Some practitioners take a cautious stance, refusing to make any
inferences with aggregate data. A wider community, including those beyond academia,
uses the existing EI methods regularly—EI is widely used to draw inferences about racially
polarized voting in Voting Rights Act cases in the U.S.—and sometimes without interrogating
the possibility of an ecological fallacy. However, the conditions under which these fallacies
can occur are rarely articulated precisely.
In this paper, we provide a reassessment of ecological inference methods.2 The existing
methodological literature on EI tends to treat EI as an almost unique problem requiring unique
solutions. We go beyond a mere review of this past work, and instead provide a reformulation
that explains the ecological inference problem within a framework of missing data, causal
inference, and linear regression modeling. By placing EI in this more general framework,
users can rely on intuition from statistical first principles on how and when ecological fallacies
occur. Our reassessment is also empirical. We evaluate both well-established and new EI
methods on common examples in political science, and show why each tends to underestimate
or overestimate the quantity of interest.
Our paper consists of three major parts. After an illustrative example of the ecological fallacy,
we first define our quantities of interest and the estimation challenge. The goal is to identify
a conditional expectation of an outcome Y conditional on a categorical predictor variable
X, using data that has been coarsened into groups (often, geographies) that contain a mix
of categories of X. For example, we are interested in the population average of vote choice
conditional on racial group identification, but electoral districts coarsen observed data into
groups that are each a mixture of White voters, Black voters, and Hispanic voters.
We show that a sufficient condition for identification is that the expectation of the outcome,
within individuals of a certain predictor group, is independent of the prevalence of the
predictor group, after controlling for a set of observed covariates. Formally, this amounts
to a coarsening at random or CAR condition (Heitjan and Rubin 1991). Our particular use of
CAR for ecological inference is akin to selection on observables in causal inference. Although
many researchers have referred to a similar identification condition over time (King 1997;
Hanushek et al. 1974; Glynn et al. 2008; Chambers and Steel 2001), none to our knowledge
have formalized the identification condition nonparametrically and conditional on covariates,
as we do here. All methods of ecological inference fail to consistently estimate the quantity of
interest when this condition does not hold.
We further show in this reformulation that aggregation itself, inherent in ecological data,
provides additional valuable structure when incorporating covariates: the outcome is always
partially linear in the categories of interest under CAR. This makes estimation for the
practitioner more straightforward: interact each covariate, possibly after some transformation,
with the predictor variable and run a linear regression of the outcome on these interactions.
In the second part of the paper, we re-characterize existing methods for ecological inference in
this framework. Although prominent existing methods do not explain their models in this
2. As we explain below in Section 3.1, we limit our review to EI methods that produce point estimates, as
opposed to the partial-identification literature that focuses on bounding the unknown quantities of interest.
2


---

Confounders and Linearity in Ecological Inference
way, their models can be represented by a certain linear regression as well. Our reformulation
shows that count models that were developed to handle more than two outcome values,
commonly known as R×C EI methods, impose a markedly different regression model than
King’s (1997) original formulation, and introduce a new set of conditions not previously
understood. We also discuss how the linear regression framework leads to novel methods that
can not only include confounders but are doubly robust to functional form misspecification of
the confounders (McCartan and Kuriwaki 2025).
In the third part of the paper, we explore how these methods perform in practice. We use real
datasets from two common use cases of ecological inference in political science. We chose
particular datasets that reveal the ground truth quantity of interest, so that we can evaluate
the methods. In the example of estimating the partisan leanings of racial groups, we show
that ecological inference estimates tend to overestimate the degree of racial polarization. We
show this is partly because the types of Black voters who reside in neighborhoods with higher
proportions of Black residents disproportionately affect the estimates for Black voters overall.
In the example of estimating how voters vote jointly across two offices, such as President and
U.S. House, we show that ecological inference tends to underestimate the prevalence of ticket
splitting—voters who back different parties for different offices. This is because ticket splitting
voters are scarcest in precisely the areas with high leverage in the regression. These two cases
feature different patterns, but the regression framework we advance helps practitioners make
sense of why these estimation errors arise.
2
An Example of the Fallacy
An illustrative example of a classic ecological fallacy will help foreground our formal treatment
of the problem. In the U.S. presidential election of 1968, George Wallace, the third-party
candidate who had the most segregationist policy platform in this election, won over a third
of the vote in the former Confederate states. Understanding the source of voter support for
Wallace by racial group is of interest to research on American Politics, especially in the context
of 1968, when the New Deal coalition among White voters is thought to have fallen apart.
A single summary of the voteshare is reported in each geography, each of which contains a
mix of Black and non-Black voters. This makes it impossible to back out the Wallace voteshare
among Black and non-Black voters separately in each geography. However, if the Wallace
voteshare is 1 point lower in a county that is 61% Black vs. an otherwise equivalent county that
is 60% Black, we might infer that Black voters do not vote for Wallace at all. A simple intuition
for ecological inference, then, is to plot the Wallace vote against the racial composition, and
extend the slope of the line to a hypothetical, 100% Black county.
Figure 1 shows such a scatterplot of these two observed variables. In South Carolina, county-
level voteshare for Wallace is negatively correlated with the prevalence of Black voters.3 From
this aggregate data one might guess that individual Black voters do not support Wallace:
counties with fewer of these voters tend to have fewer Wallace votes. However, in neighboring
North Carolina, the relationship flips. Counties with a higher Black population, covering the
coastal Piedmont region, are where Wallace wins the most votes. A naive observer might
conclude that Black voters were more likely to vote for Wallace than non-Black voters in North
Carolina.
3. This figure is complicated by differential turnout by race; see Appendix D.1.
3


---

Confounders and Linearity in Ecological Inference
South Carolina Counties
North Carolina Counties
0%
25%
50%
75%
100%
0%
25%
50%
75%
100%
10%
20%
30%
40%
50%
Black Residents
George Wallace Votes (1968)
Figure 1: Examples of the Ecological Fallacy. X-axis shows the Black population from the 1970
Census as a share of the overall voting-age population (VAP). The y-axis shows the total number of
votes cast for George Wallace as a share of VAP. The estimated VAP turnout in the two states was
54%, which was in turn split across Nixon (21%), Wallace (17%), and Humphrey (16%).
Observers of these elections knew that such results could not be taken to indicate Black
voters preferred Wallace. Newly enfranchised Black voters would have little reason to vote
for Wallace, a candidate explicitly running against the Civil Rights movement. Indeed, an
academic survey of this election showed that only 0.3% of Black survey respondents who
reported voting in the former Confederate states reported voting for Wallace (Wright 1977;
Kovenock and Prothro 1968). Instead, they reasoned that White voters reacted to the Civil
Rights Act of 1964 and the Voting Rights Act of 1965, turned against the incumbent Democratic
administration and cast their votes for the Southern candidate, Wallace (Wright 1977; Phillips
2014; Schoenberger and Segal 1971). The Wallace support among non-Black, White voters in
North Carolina was higher specifically in the areas where there were relatively more Black
voters, thus creating an ecological fallacy. The next section formalizes this intuition.
3
Confounding and Linearity in Ecological Inference
We clarify how certain variables confound the identification of the estimand, and show how a
linear model structure arises naturally from the necessary identification assumption. This
implies a certain linear regression that accounts for potential confounders is the correct
approach to infer individual means from aggregate data.
We conclude by putting our
identification result in the context of existing literature.
3.1
Quantities of interest
The ecological inference problem is estimating the expectation of a variable Y given a categorical
variable X when individual observations are averaged according to a grouping variable G.
We let individuals belong to one of K categories of X, and denote Xik to be a binary variable
indicating whether individual i belongs to category k. We use the notation I to indicate a set
of individuals, so, for example, Ik indicates all individuals who are of category k. We use N to
count these individuals, so Nk is the number of individuals in the set Ik. The outcome Y is
typically categorical in political science applications, and represented as a vector of indicator
variables, but it need not be.
4


---

Confounders and Linearity in Ecological Inference
The first quantity of interest is the conditional mean of the outcomes among all individuals in
category k,
Bk := 1
Nk ∑
i∈Ik
Yi.
(1)
We may refer to this as the global parameter. Next, the local parameters are the conditional
average for each geography g,
Bgk :=
1
Ngk ∑
i∈Igk
Yi,
(2)
where Igk again refers to individuals who are in both category k and geography g. To
disambiguate between X and G, we refer to levels of X as categories (indexed by k) and G as
geographies (indexed by g), although in practice G can represent non-geographic categories
as well. The global parameter Bk is exactly a weighted average of the local parameters Bgk
where the weights are the size of category k in each geography.4
A key identity relates these quantities of interest to the data and is a core characteristic of the
ecological inference problem. Using Bg to denote the K-length vector [Bg1, ..., BgK] for each
geography g, we have
Lemma 3.1 (Accounting identity). For any geography g, the aggregate outcome mean is exactly a
linear combination of the local conditional means:
Yg = B⊤
g Xg.
(3)
Proof. First notice that because the category X is discrete, the sum of outcomes Y in the entire
geography can be partitioned into K terms: ∑i∈Ig Yi = ∑i∈Ig1 Yi + · · · + ∑i∈IgK Yi. Then, each
sum can be rewritten as a product of the composition X and the local conditional means, Bg,
Yg = 1
Ng ∑
i∈Ig
Yi
= 1
Ng
Ng1
Ng1 ∑
i∈Ig1
Yi + · · · + 1
Ng
NgK
NgK ∑
i∈IgK
Yi
= Ng1
Ng
Bg1 + · · · + NgK
Ng
BgK
= Xg1Bg1 + · · · + XgKBgK.
(4)
The third line follows from Eq. 2, and the final line holds because the proportion of the
geography g that is also of category k is exactly the sample mean of Xk.
This identity, which holds exactly in finite samples, is helpful for subsequent estimation because
it restricts the functional form of possible models to one that is linear in the composition of
categories.
Thus far, the global and local parameters are finite sample quantities. Quantifying the
statistical performance of our estimators requires that we introduce a notion of randomness.
4. That is, Bk = (∑g NgkBgk)/(∑g Ngk) holds exactly. See the appendix for a derivation.
5


---

Confounders and Linearity in Ecological Inference
Here, we conceptualize a superpopulation from which geographies are drawn to define
a superpopulation version of our parameters, which we term the (global) estimand. The
expectation of our conditional means over a hypothetical infinite sample of geographies is
β := E[B],
(5)
where each element of β is βk = E[Bk]. This expectation, and all subsequent expectations
in this paper, is effectively an average over an infinite sample of hypothetical geographies,
and allows us to compute confidence intervals. Practitioners may often be interested in B
itself, rather than its superpopulation mean. When the number of geographies is large, the
difference between B and β is negligible compared to the variation in the Bg. Alternative
conceptualizations of randomness within the finite sample setting include a Bayesian approach,
which treats B as a random variable with a prior rather than as a parameter, and a design-based
approach, which treats each individual’s choice of geography as the source of randomness.
3.2
Connection to missing data and causal inference
From this setup, it is clear that ecological inference is a missing data problem: marginal means
are observed while the conditional mean is not. We propose that in particular, causal inference
using potential outcomes provides an intuitive and illuminating analogy for understanding
the subsequent identification conditions. Several aspects of the causal setup map more cleanly
to ecological inference than the missing data setup does.
The key accounting identity in ecological inference is analogous to the key relationship in
causal inference. In causal inference with a binary treatment D for unit i, we have
Yi = Yi(1)Di + Yi(0)(1 −Di),
(6)
where the potential outcomes Yi(0) and Yi(1) are unobserved and are effectively coarsened into
observed Yi by the treatment assignment Di. Causal estimands usually involve expectations
over the unobserved potential outcomes.
For example, the average treatment effect is
E[Y(1) −Y(0)] = E[Y(1)] −E[Y(0)]. The relationship in Eq. 6 maps well to the accounting
identity (Eq. 3) with two racial categories,
Yg = Bg1Xg1 + Bg2Xg2
= Bg1Xg1 + Bg2(1 −Xg1),
(7)
where Bg1 and Bg2 are the unobserved local parameters, which are coarsened into the local
mean Yg by aggregation based on the racial composition Xg1. These local parameters can
be viewed as the potential outcomes for geography g if in fact its racial composition were
homogeneously one group or the other and voter behavior were held constant. And as in
causal inference, our quantities of interest, β1 = E[B1] and β2 = E[B2], are averages of these
unobserved potential outcomes.
Thus, in both causal inference and ecological inference, we observe a linear combination of
unobserved or missing data, and hope to infer the average value of the missing data across
the population. The fundamental problem of causal inference embodied in Eq. 6 is that there are
twice as many unobserved potential outcomes as there are individuals, so the estimand is
unidentified without further assumptions. Eq. 7 makes clear that ecological inference also
involves attempting to identify two parameters for every data point.
6


---

Confounders and Linearity in Ecological Inference
The main difference between the two problems is also illuminating: in the causal setup above,
treatment Di is binary, whereas in ecological inference, the corresponding variable Xg1 is
a proportion. This is not to say that EI is causal inference with a continuous treatment:
with binary Di exactly one potential outcome is observed for each individual. A continuous
treatment would require a different potential outcome for each of the infinitely-many treatment
values. In EI, we observe a continuous mixture of a finite number of unobserved B for each
geography. The continuous nature of this mixture pays dividends in carrying out estimation,
and in understanding threats to inference, as we discuss below.
There are other related ways in which the causal inference analysis is fruitful. The conditions
needed to identify the ecological inference estimands are similar to the familiar ignorability
conditions in causal inference. As we show below, we can therefore motivate the importance
of controlling for confounders and positivity conditions in the same way as in causal inference
designs.
3.3
Identifying the global estimand
The presence of more unobserved missing values than observations means that neither
causal nor ecological estimands can be identified without further assumptions. In causal
inference, this problem is often tackled by making an ignorability assumption that the missing
potential outcomes are unrelated to the treatment assignment. This assumption is satisfied in
a randomized experiment.5
The analogous assumption in ecological inference is also sufficient for identification, with
a small twist: we must also consider how the unobserved Bg relate to Ng, the number of
individuals in each geography. Specifically, if
E[Bg|Xg = x, Ng = n] = E[B]
for every value of x, n,
(8)
we say that the assumption of coarsening completely at random (CCAR) holds. The following
proposition shows that this assumption is sufficient to identify β = E[B]. The proof is in
Appendix B.
Proposition 3.1 (Identification under CCAR). If CCAR holds, then β is identified as the (population)
regression coefficients of Y on X,
β = E[XX
⊤]−1 E[XY].
In other words, a regression of Yg on Xg with no intercept can consistently estimate β, as long
as one believes that CCAR holds. In the ecological inference context, this estimator is known
as Goodman regression or ecological regression.6
Compare CCAR to the mean-independence condition (or weak ignorability) used to estimate
the average treatment effect in causal inference. That condition states that the treatment
variable is mean-independent with the missing data, i.e., E[Y(d)|Di = d] = E[Y(d)] for
d = 0 and d = 1. This matches the CCAR assumption, where the assignment of voters to
locations, which generates X and N, plays the role of the treatment assignment D. If weak
ignorability holds, then a simple regression of Y on D—which is mathematically identical
to a difference in means between the treated and control groups—consistently estimates the
5. Assuming full treatment compliance, no spillover, and so on.
6. Goodman (1953) itself, however, warned against making a CCAR-like constancy assumption (Wakefield
2004).
7


---

Confounders and Linearity in Ecological Inference
average treatment effect. Thus, Goodman’s regression can be thought of as the analog to the
causal difference-in-means estimator.
Is coarsening completely at random plausible in practice? Consider again the 1968 election
example. In this case, CCAR means that the average Wallace support among White voters
in heavily White areas is equivalent to that in other areas, or the population as a whole. For
instance, this means White voters in rural lowland counties with a higher proportion of Black
voters and White voters in mountainous counties with few racial minorities support Wallace
at the same level in expectation. CCAR is implausible in this setting, and is incompatible with
the social scientist’s interest in how different individuals sort into different geographies. This
helps explain why the simple linear regression shown in Figure 1 for North Carolina has the
wrong slope.
If CCAR is implausible, what is to be done? In causal inference, an assumption of complete
randomization can be weakened to hold conditional on covariates, which is known as a
selection-on-observables assumption. The same idea applies to ecological inference: covariates
can solve the ecological fallacy under certain conditions.
Suppose there exists a variable Zg (in general, a vector) that is observed at the geography level.
For example, Z can be the income in a geography, or a binary variable indicating whether the
geography is a certain region of the state. Then, if
E[Bg | Zg = z, Xg = x, Ng = n] = E[Bg | Zg = z]
for every value of z, x, n,
(9)
we say that coarsening at random (CAR) holds.7 The intuition of this equation is that among
geographies with a particular set of covariate features Zg = z, knowing Xg and Ng does
not change the expected value of Bg. CCAR is a special case of CAR where Zg contains no
covariates at all. Versions of this assumption have been discussed, often informally, in the
literature, a history we review in Section 3.7 below. This assumption is sufficient to identify
the quantity of interest β, as the following proposition formalizes.
Proposition 3.2 (Identification under CAR). For all categories k, if coarsening at random holds, β
is identified as8
βk = E

E[Y | Z = z, Xk = 1]
Ngk
E[Ngk]

.
At first glance, Proposition 3.2 may appear very different from Proposition 3.1. However,
when CCAR holds and Z is empty, E[Y | Z, Xk = 1] = E[Y | Xk = 1] is constant, and so
the identification expression simplifies to βk = E[Y | Xk = 1]. The value of the Goodman
regression when Xk = 1 and all other Xk′ = 0 is exactly the coefficient on Xk, which is the
identification result in Proposition 3.1.
7. Note that compared to Imai et al. (2008), who discuss similar assumptions, our acronyms are reversed: there,
CAR is the stronger assumption (our CCAR), and CCAR (where the first C stands for “conditional”) is the weaker
assumption. We have opted for CCAR/CAR here to match the existing MCAR/MAR terminology in the missing
data literature.
8. Following convention and the previous proposition, we suppress the subscript g for variables inside
superpopulation expectations. But we make an exception for the denominator E[Ngk] in order to distinguish it
from the total number of category-k individuals, Nk. The ratio Ngk/ E[Ngk] represents how much geography g’s
category-k population differs from the typical geography, and merely re-weights the geographies to represent
individuals instead of geographies. When every geography contains the same number of category-k individuals,
the proposition is that βk = E[E[Y | Z = z, Xk = 1]].
8


---

Confounders and Linearity in Ecological Inference
Just as Proposition 3.1 implies a certain natural plug-in estimator (Goodman’s regression),
Proposition 3.2 does as well. To estimate the conditional average for category k:
Procedure 1
1. Fit a regression model of Y on some function of X and Z.
2. For each observation in the regression, produce fitted values ˆy on a hypothetical dataset
where all geographies contain only individuals of category k, such that Xgk = 1 and
Xgk′ = 0 for the other categories k′ ̸= k, while other values Z are held at their observed
values,
3. Then ˆβk is the average over these fitted values ˆy, weighted by Ngk, the number of
individuals in category k in each geography g.
The plug-in and aggregation steps are straightforward, but what is challenging is the first step
of estimating the unknown CEF E[Y | Z = z, Xg = x]. We discuss the aspects of this problem
in several steps, starting with a simple functional form (Section 3.5), increasing robustness to
functional form misspecification (Section 4.4), and accounting for unobservable confounders
(Section 5).
3.4
Identifying the local estimand
The accounting identity also clarifies that, unfortunately, point identification of the local Bg is
impossible without further assumptions: each observation contributes K unknown parameters
(the entries of Bg), so there are K times as many parameters as observations. Existing literature
has taken one of two approaches to this challenge.
The accounting identity allows for partial identification, that is, estimating strict bounds on the
possible values the unobserved parameters can take. As an extreme example, if geography g
is composed exclusively of category k, the local estimand Bgk must be exactly the observed
outcome Yg. In general, when Y is a bounded variable, the quantities of interest Bgk are
bounded by a function of the compositions and the outcome, a constraint first noted by Duncan
and Davis (1953). King (1997) combined these Duncan–Davis bounds with the Goodman
regression framework, and others have explored how these bounds generalize for other
quantities of interest (Cross and Manski 2002) or how they can be narrowed with additional
assumptions (Jiang et al. 2020; Elzayn et al. 2025).
Our paper does not focus on partial identification so that we keep the focus on the bias in point
estimates. However, the Duncan–Davis bounds contain information that is certainly helpful
in their own right. In some extensions, the bounds can be sufficiently narrow to be useful, and
bounds may also test the plausibility of the identifying assumptions we introduced above: if,
even with many observations, the point estimates are outside the bounds, then the identifying
assumptions are likely violated.
Another approach is to take a Bayesian perspective and treat the Bg as parameters. While
a consistent estimate of each Bg is still impossible, the Bayesian approach at least allows
uncertainty quantification for these local estimands. This is the approach that King (1997) and
follow-up work take, as we elaborate in more detail below. In particular, King constructed
the prior on Bg hierarchically and in a way that incorporated the bounds on Yg, so that the
posterior estimates of Bg lie within the Duncan–Davis bound automatically. A challenge with
this approach is the sensitivity to the particular prior distribution chosen, and especially the
9


---

Confounders and Linearity in Ecological Inference
assumptions that distribution makes about correlations between the elements of Bg.9 This
is the same challenge that arises in Bayesian causal inference, where sample-level causal
estimands depend on untestable assumptions about the joint distribution of the potential
outcomes.
However, unlike causal inference, it may be possible to make some inferences about the
distribution of Bg from the data. McCartan and Kuriwaki (2025) show that the covariance
of the local estimands can be identified under a second-moment independence condition
conditional on covariates, i.e., that E[BgB⊤
g | Zg, Xg, Ng] = E[BgB⊤
g | Zg]. This is a similar but
stronger assumption to CAR. They use this additional assumption to construct asymptotically
valid confidence intervals for the local estimands. While these intervals will not shrink to
zero as more data are collected, due to the fundamental unidentifiability, they provide useful
uncertainty quantification, just as Bayesian approaches to ecological inference aim to do.
3.5
The role of linearity
Proposition 3.2 shows that enough covariates can identify ecological inference parameters, yet
the question of how to estimate these quantities remains, because the functional form with
which collected covariates interact is unknown. Fortunately, the accounting identity Eq. 3,
combined with CAR, restricts the true regression function of Y on Z and X to be partially linear
in X. This proves helpful in estimation.
Why does partial linearity arise in ecological inference specifically? Note that the CAR
assumption implies the following structure for Bg:
Bg = E[Bg | Zg, Xg] + εg
= E[Bg | Zg] + εg
with
E[εg | Xg] = 0
(10)
where the second line is directly due to CAR in Eq. 9. The residuals εg are conditionally
mean-zero because the residuals from any conditional expectation are orthogonal to the
conditioning variables. Eq. 10 merely re-expresses the CAR assumption in a form that will
prove more convenient, but it highlights a crucial implication of CAR: on average, the local
estimand is a function only of Zg, with residual variance unrelated to Xg.
Now, substituting Eq. 10 into Eq. 3 and denoting E[Bg | Zg] as f (Zg), some (unknown)
vector-valued function of the covariates, we have that
Yg = ( f (Zg) + εg)⊤Xg = f (Zg)⊤Xg + ε⊤
g Xg.
Taking conditional expectations of both sides, we find
E[Yg | Zg, Xg] = f (Zg)⊤Xg
= f1(Zg)Xg1 + · · · + fK(Zg)XgK,
(11)
because the residual term εg is conditionally mean-zero. The left-hand side of Eq. 11 is the
conditional expectation function (CEF) of Yg on Zg and Xg, which appears in Proposition 3.2.
What the right-hand side of Eq. 11 shows is that the CEF has a partially linear structure: it is
linear in Xg with coefficients that depend, possibly nonlinearly, on the covariates Zg. This
9. In the framework of King (1997), the covariance of the entries in Bg is what specifies the angle at which the
global estimate is projected down to the tomography line to make a point estimate.
10


---

Confounders and Linearity in Ecological Inference
type of model is also known as a varying coefficient model (Hastie and Tibshirani 1993; Fan
and Zhang 1999).
Now, to make the exposition in this section more concrete, suppose we are further willing to
assume the coefficient functions f (Zg) (that is, E[Bg | Zg]) are simply linear in Zg. Let p be
the number of covariates in Zg, then we can write such a model as
fk(Zg) = γk0 + γk1Zg1 + · · · + γkpZgp,
where the regression coefficient γkj is indexed by each predictor category k and the covariate
index j ∈{0, 1, . . . , p}.
We refer to this assumption as a linearity-in-covariates assumption (not to be confused with the
CEF being always linear in X). This is a strong assumption—in reality, each covariate could
enter f in a nonlinear form, or interact with other covariates—but it helps illuminate what
linearity-in-X buys us. We relax this assumption in Section 4.4.
Substituting this expression into Eq. 11, we have:
E[Yg | Zg, Xg] = γ10Xg1 + γ11Zg1Xg1 + · · · + γ1pZgpXg1
|
{z
}
For outcome category 1
+ · · ·
+ γK0XgK + γK1Zg1XgK + · · · + γKpZgpXgK
|
{z
}
For outcome category K
.
(12)
This CEF is fully linear, and so in this case an ordinary least squares regression is an appropriate
estimator for these coefficients. In other words, to estimate β, regress the outcome on pairwise
interactions of each of the p covariates Zg with the K categories X, then generate estimates
following Procedure 1. Usually, the modeler faces the problem of not knowing how the
variables X and Z should enter the regression: whether they should be logged, squared,
binned, or interacted. In ecological inference problems, there is no such ambiguity for X: it
should be fully interacted with Z and enter the regression linearly.
We consider Eq. 12 to be a generalization of Goodman’s regression to the case where covariates
are included. 10 Though Eq. 12 requires a linear-in-covariates assumption about f (Zg), even
without it, Eq. 11 follows immediately from the CAR assumption alone.
3.6
Implications of linearity
The connection between aggregation and linear regression under CAR is useful beyond
justifying the use of linear regression. The connection allows us to use familiar intuition
about linear regression to understand tradeoffs in ecological modeling and anticipate when
ecological inference will fail.
To demonstrate these connections, we introduce in Figure 2 (a) a simple simulated example.
We generated 20 synthetic precincts with two racial groups that satisfy the CCAR assumption,
with the global parameter β set to (0.5, 0.2).11 In this sample, B1 was 0.508. We then fit an
10. That is, if Zg is empty because CCAR holds, then f (Zg) = β and Eq. 11 exactly expresses Goodman’s
regression.
11. Each precinct’s Bg were drawn from a tightly distributed bivariate truncated normal distribution as in the
model of King (1997).
11


---

Confounders and Linearity in Ecological Inference
OLS regression of the implied Y on X. The line evaluated at X1 in this particular example was
0.509, quite close to β1 and even closer to the finite-sample B1. We also ran King’s (1997) model
on the same 20 data points, as a preliminary illustration of our point that King’s estimator can
be represented by a particular Goodman regression. Its estimate for B1 was 0.511, also quite
similar. This example illustrates Proposition 3.1 that, under CAR (or CCAR), estimates of β
can be obtained by plugging in X1 = 1 and X1 = 0 into a simple regression.
OLS: 0.51
King ei: 0.50**
Truth: 0.51
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
X1
Y
OLS: 0.94
King ei: 0.79
Truth: 0.52
OLS w/controls
     0.51
King ei: 0.59
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
X1
Y
Figure 2: Intuition for EI as linear regression. A simulated example where the quantity of interest
is β1 = 0.5. In panel (a), n = 20 data points are simulated from the model of King (1997). A
simple OLS fit evaluated at X1 = 1 provides an estimate that agrees with both King’s EI algorithm
and the ground truth. In panel (b), an outlier with high leverage is added to the dataset, shown
in the top-right part of the figure. The resulting OLS fit severely overestimates the truth, as does,
to a lesser extent, King’s EI. However, if the outlier differs with the other n = 20 points on some
covariate Z, controlling for Z in the OLS reduces the bias significantly.
The near-perfect accuracy of the ecological inference in Figure 2 (a) is, however, fragile. There
are at least three major ways in which we can characterize the direction of potential errors.
Fragility in extrapolation
In many EI examples involving geographic units, perfect residential
sorting (Xk = 1 or 0) is rare, so producing the plug-in estimates from Procedure 1 usually
involves inevitable extrapolation from the observed data. This is clearly seen in Figure 2 (a),
where the observed X1 are clustered near zero. As a result, the Goodman estimate for this
category is unstable, because much extrapolation is required. Extrapolations can lead to even
impossible, out-of-bounds estimates that are negative or above 1. Finite-sample variation
combined with extrapolation can produce negative estimates even when CCAR holds. This
feature of the estimator explains why EI applications typically find that estimates for small
minority groups are highly variable or impossible.
Influence and high-leverage points
Intuition about high-leverage or influential points in
linear regression also carries over to ecological inference.12 In Figure 2 (b) we illustrate the
influence of such a point by adding a single, high-influence observation to the sample. This
precinct has X1 = 0.9. It also has a different outcome than the other distribution: Bg1 = 1,
12. An influential point is an observation that has a disproportionate effect on the slope of a regression (Blackwell
2025; Chatterjee and Hadi 1986). Specifically, influence is computed by the leverage of a point multiplied by its
outlier value from the leave-one-out regression.
12


---

Confounders and Linearity in Ecological Inference
Bg2 = 0, resulting in Yg = 0.9. The Cook’s distance of this observation (a standard measure of
influence) is 34.6, compared to less than 0.2 for all other observations. As a result, the slope of
the OLS line changes drastically, and the extrapolated estimate at X = 1 is now off by over 40
percentage points, even though the global parameter B1 only increased to 0.53. King (1997)’s
estimate of the same data is less drastically off, but not much better. Both methods fail on
panel (b) because of the violation of CCAR: the geography with an especially large X is also
the one with an especially high B1 value. The lesson here is that the connection to regression
serves as a reliable diagnostic to anticipate or identify possible violations.
Fortunately, the use of control variables can reduce the undue impact of influence points. In
the same example in Figure 2 (b), if there is a third variable Z that distinguishes this influence
point from the remaining 20 observations, the regression may be corrected.13 Applying the
Procedure 1 to the data assuming linearity in the single covariate generates a linear fit that is
0.51 when evaluated at X1 = 1 and Z = 0, as shown by the dashed line in the figure. The
covariate helps satisfy the CAR assumption while decreasing the residual variance of the
regression, and the overall estimate is much improved.
Positivity violations
Finally, the linear regression intuition is also helpful in highlighting
the need for positivity: sufficient variation in X, including residual variation after accounting
for covariates. This is the EI analogue of the overlap assumption in causal inference, which
requires that each individual has a nonzero probability of receiving each type of treatment.
The precision in a linear regression estimate is generally increasing in the variation in the
predictor variable. Small variation in X thus poses an estimation problem even if CCAR holds.
For example, estimates of the gender gap in elections are typically unstable because gender
ratios in most geographies are near parity, which means little variation (not to speak of the
significant extrapolation to a hypothetical single-sex geography) (Teele 2024). In regressions
with covariates, the relevant identifying variation is the residual variation in X remaining
after holding covariates fixed.14 In the extreme case where Z is collinear with X and thus
explains all of its variance, then the regression model cannot be estimated even though CAR
technically holds.15
This poses a tradeoff: including control variables will improve the plausibility of CAR but may
also remove variation in X necessary for estimation. For example, return to the 1968 election
in Figure 1 and imagine controlling for the proportion of the population in each county that
was enslaved in 1860. This variable is a strong predictor of the proportion of Black voters in a
county and also of the voteshare for Gov. Wallace. It is more plausible to believe that, among
counties with a similar history of slavery, White voters’ support for Wallace is unrelated to the
proportion of Black voters. However, the near-collinearity of the covariate with Xg1 means
that the regression will be highly unstable.
Fundamentally, ecological inference requires exogenous variation in X, from which estimates
of Y for each category can be extrapolated. When the covariates needed to satisfy CAR also
13. In this example, we suppose that Z = 1 for the influence point and it is a small random Normal error centered
at 0 and with a standard deviation of 0.001 for the other 20 observations.
14. Precisely, the coefficient on one variable (X) can be obtained by a sub-regression of the outcome residualized
by the other covariates (Z) on that one variable (X) residualized in the same way, by the Frisch-Waugh-Lovell
theorem.
15. Notice that CAR trivially holds if we let Z = X. But this trick cannot estimate β due to its complete collinearity.
13


---

Confounders and Linearity in Ecological Inference
mop up all of the variation in X, then there is simply not enough information left in the data
to make an estimate.
3.7
On the history of controlling for confounders
Many methodologists have been aware of the sort of conditional identification condition we
show here. Goodman (1959) himself stated the CCAR assumption and considered several
ways covariates could make CAR hold [612, 622–644]. Hanushek et al. (1974) proposed a
linear regression with covariates, but included no interactions.
King (1997) presents a conditional independence assumption briefly in its chapter on linear
contextual effects and avoiding aggregation bias, but does not formalize an identification result
[170–171]. Imai et al. (2008) identifies the need for a coarsening at random assumption condi-
tional on covariates, but relies on a particular distributional model for the parameters.16 Other
work has focused on model misspecification and bias under no covariates (e.g. Ansolabehere
and Rivers 1995; Cho and Gaines 2004) while rarely discussing the use of covariates. This
direction in the literature is notable since, as Lewis (2001, 175) observes, “many scholars have
considered aggregation bias (the violation of [the constancy] assumption) to be the problem in
making ecological inferences” (emphasis ours).
Controlling for covariates may have sat uneasily with the desire to not control out intermediate
mechanisms. This logic may have been reinforced by court rulings in the late 80s that focused
the research question on the mere existence of racially polarized voting, regardless of its
underlying causes.17 Some scholars took this to mean that one should not control for covariates
in ecological inference (King 1997, 171). The use of covariates also went against Achen and
Shively (1995), which argued that the biases of ecological regression, “are not curable by
. . . controlling for demographic variables” at the individual level (92–94). Our theoretical
results clarify that one should control for covariates such that CAR holds (a statement about
aggregate level ignorability, not individual level predictive accuracy), and then combine the
estimated ceteris paribus coefficients into the conditional mean of interest.
4
Comparison of Methods for Ecological Inference
Our regression framework lets us re-assess the differences across the EI methods commonly
used by practitioners. Existing models achieve identification using one of two approaches: A
parametric approach, which relies on specific distributional or functional form assumptions
controlled by a finite number of parameters, or a non-parametric approach, which does not rely
on such assumptions for accurate inference.
4.1
King’s 2×2 ecological inference model
One achievement of King’s 1997 model is that it provides point estimates of the local means
Bg. Starting from the accounting identity with K = 2 categories and a binary Y, King moves
to a parametric Bayesian regression in which the coefficients (Bg1, Bg2) are jointly drawn from
a bivariate Normal distribution truncated to the unit square:
Bg
iid
∼N [0,1]2(µ, Σ),
16. Neither of these sets of authors considers the role of Ng in the identification assumption.
17. Thornburg v. Gingles, 478 U.S. 30 (1986).
14


---

Confounders and Linearity in Ecological Inference
where [0, 1]2 denotes truncation to a unit square, µ is the location parameter, and Σ is the
covariance matrix. The truncation is applied so that the Bg remain properly between 0 and 1,
since King’s model applies only to binary Y.
The estimation of each local estimand is best understood by first considering the easier setting
of when Bg is untruncated. Such a model is well-studied as a random coefficient model
(Griffiths 1972; as cited in Anselin and Cho 2002). In this case, the MLE for the local estimand
for each geography g, conditional on Σ, is given by
ˆBg =
ˆB
|{z}
global estimate
+ ΣXg(X
⊤
g ΣXg)−1 (Yg −X
⊤
g ˆB)
|
{z
}
residuals
.
(13)
That is, the estimates are the combination of the global estimate and the residual of the linear
regression reweighted by the covariances of the two coefficients. Intuitively, King’s model
produces unit-level estimates by allocating the residuals from a certain weighted Goodman
regression in accordance with an estimate of the covariance matrix Σ.
The implications for identification remain the same in Goodman and King’s models. We can
rewrite King’s model for Bg in terms of the global parameter B = E[Bg] and a residual term
εg. To do so, define mg = µ −B. Unlike with an untruncated Normal, mg is not always 0,
because the truncation can shift the mean of the distribution away from its location parameter
µ. Then we can write
Bg = B + εg,
εg
iid
∼N [0,1]2−B(mg, Σ),
(14)
where [0, 1]2 −B is the unit square shifted by the vector B. Since εg is drawn independent
of X, by construction, we have E[εg | Xg] = 0, so E[Bg | Xg] = B. This is exactly the CCAR
assumption. Thus King (1997)’s model makes the same strong assumption as Goodman’s
regression for identification. Since the model does not involve covariate adjustment, it does
nothing to ameliorate aggregation bias due to confounders (Rivers 1998; Lewis 2001).18
Substituting the reexpression into each geography’s accounting identity, we have
Yg = B⊤Xg + εg,
(15)
where εg = ε⊤
g Xg.19 This is exactly the form of the CEF that follows from the CCAR assumption
(see also Eq. 10), on which Goodman’s regression is based. The difference is that Goodman’s
regression makes only the assumption that E[εg | Xg] = 0, whereas King’s model assumes
a specific distribution for the error term εg. This distribution is not the same for every
observation, and in fact depends on the coefficients Bg, the same way that the error term in a
generalized linear model depends on the linear predictor. Still, this added assumption often
leads to improved estimation in finite samples relative to untruncated regression because
information on each accounting identity is incorporated for each local estimate, and the global
estimates are produced as a mean of these local estimates.
18. King (1997) defines aggregation bias in a looser way. Chapter 9 of the book discusses covariate adjustment,
but also appears to consider out-of-bounds estimates as a type of aggregation bias. It is true that the truncation
imposed here ultimately reduces estimation error in many cases. However, we agree with Lewis’ (2001) (175)
interpretation that King’s main method “should be thought of as a ‘solution’ in the sense that, assuming its
assumptions hold, it allows the user to make more efficient estimates [of the global parameter] than can be made
using conventional regression techniques and also allows the estimation of [local parameters].”
19. We replace the local coefficients in the accounting identity with Eq. 14, and rearrange in terms of the global
parameter.
15


---

Confounders and Linearity in Ecological Inference
This model, however, requires more advanced computational techniques than linear regression:
because εg is a linear combination of (correlated) truncated Normal variables, it is not even
truncated Normal itself. There is no closed-form expression for its distribution and so direct
maximum likelihood estimation is not feasible. Instead, King reparametrizes the model so that
the Bg can be analytically integrated out, leveraging that (a) the restriction of the truncated
bivariate Normal distribution to the tomography line is still a (univariate) truncated Normal
distribution, and (b) univariate truncated Normal distributions have a closed-form CDF and
normalizing constant (King 1997, Appendix D). King’s original computational proposal
remains a good strategy for the 2×2 case, even as more advanced generic Markov chain Monte
Carlo (MCMC) methods have been developed.
4.2
Other parametric models
Other models impose distributional assumptions on different latent quantities. Imai et
al. (2008) extend King’s fully parametric framework by modeling the local parameters on a
logit scale, allowing more covariates and a flexible mixture of distributions, while preserving
the geography-level accounting identity.
The older Thomsen model (Thomsen 1987) may be best thought of as estimating an individual
IRT model with aggregate means. Voter’s latent utilities are distributed as bivariate Normal,
and the method uses proportion Y and X transformed by a probit function to estimate the
distribution’s correlation parameters. It constrains that distribution so that the observed X or
Y matches the CDF evaluated at 0 on each respective dimension. This model does not leverage
the accounting identity or the linear structure of the problem. It also does not produce local
estimates or use covariates.
Yet other approaches cast estimation as constrained optimization. For instance, Pavía and
Romero (2024) estimate global parameters that minimize the discrepancy between local margins
and fitted margins under an L1 norm.20 These approaches are analogous to parametric models
in that they must minimize some user-specified loss function, but differ in that this loss
function is not connected to a statistical model or estimand.
Finally, the neighborhood model (Freedman et al. 1991) allows local parameters to arbitrarily
vary across geographies, while assuming them to be identical for all groups within a geography:
Bg = bg · 1 for each g,
(16)
where bg is a scalar parameter and 1 is a K-length vector of ones. Substitution of Eq. 16 into
the accounting identity immediately gives Yg as estimates of bg. In essence, the neighborhood
model replaces CCAR with its own strong ignorability assumption. The model can also only
hold at one level of aggregation: if the assumption in Eq. 16 holds at the precinct level, then it
cannot generally also hold at the county level (Gelman et al. 2001).
4.3
Count models and beyond the 2×2 case
Researchers are interested in modeling discrete choice behavior across more than two choices.
However, in these higher dimensions, known as the R×C case, King (1997)’s sampling strategy
20. In our notation, they obtain a ˆB that minimizes the sum of |Yg −ˆB⊤Xg| across geographies.
16


---

Confounders and Linearity in Ecological Inference
faces challenges because multivariate truncated Normal distributions involve intractable
normalizing constants.21
Instead, researchers have turned to modeling the counts of individuals in each geography. In
the 2×2 case, the number of individuals with Y = 1 is the fraction (B1X1 + B2X2) multiplied
by the total population N, so the count approach models a binomial count process with
probability BX and trials N, or Binom(N, BX). Initially proposed by Brown and Payne (1986)
and developed for the 2×2 case in King et al. (1999) and Wakefield (2004), this model can then
be extended to a multinomial for more categories. Both count models and models of fractions
can be thought of as a linear regression. We review two prominent models, Rosen et al. (2001)
and Greiner and Quinn (2009). The count models can extend to multiple outcome choices, as
we will show, but they also bring their own modeling challenges.
Formally, we generalize Y to be multivariate instead of binary by letting it take on one of J
levels, and let Mg1, . . . , MgJ be the counts of the number of individuals in each level of Y in
geography g. The parameter Bg is now a matrix, with K rows and J columns. For example,
Bg,white,dem is the proportion of White voters in geography g who vote for the Democratic
candidate.
King’s 1997 model is expressed in terms of the local finite-sample parameters Bg, which must
strictly satisfy the accounting identity (Eq. 3). The R×C models take a different approach,
parametrizing the model in terms of βg, the superpopulation counterpart to Bg. Rosen
et al. (2001), in the widely used eiPack R package, propose a simple count model for Mg:
Mg
|{z}
[J×1]
iid
∼Multinom(Ng, β⊤
g Xg
| {z }
[J×1]
) for each g.
(17)
Because βg are superpopulation parameters, which may be different from the unobserved
Bg, they need not satisfy the accounting identity. This additional wiggle room aids greatly in
estimation of the local parameters: the accounting identity is satisfied only in expectation.
The choice of Multinomial distribution, however, limits the expressive power of the model and
imposes several substantive assumptions. Eq. 17 is appropriate when each outcome choice in a
geography g is a draw from a single J-length probability vector, identically and independently
from other individuals in the geography. This sits uneasily with the possibility that outcomes
vary with group membership k. For example, suppose K = 2 and all White voters in precinct
g prefer Republicans (βg,white,dem = 0) while an equally sized group of Black voters all prefer
Democrats (βg,black,dem = 1). Then Eq. 17 assumes that all the voters in the precinct, White and
Black, vote for Democrats with the same probability of 0.5. While on average this produces
the correct number of Democratic votes in the precinct, the model formally rules out both
heterogeneity and correlation in individuals’ outcomes within precincts, even as it attempts to
model different outcomes by group.
Further, Rosen et al. (2001) as well as Brown and Payne (1986) adopt a Dirichlet prior for each
row (group membership) of βg, with each Dirichlet being independent. In the racial voting
example, the probability a White voter in geography g votes for a Democrat is estimated
independently from the probability that a Black voter in that same geography votes for a
21. Recent expectation propagation (EP) methods can quickly produce accurate approximations (Cunningham
et al. 2011). Progress has also been made in sampling quickly from truncated multivariate Normal distributions,
using elliptical slice sampling (Wu and Gardner 2024).
17


---

Confounders and Linearity in Ecological Inference
Democrat. This is a marked departure from King’s 1997 model, where this pair of parameters
are drawn from a bivariate distribution with an estimated correlation parameter. The Dirichlet
distribution (with J parameters) is less flexible than a Normal distribution (with J + J(J −1)/2
parameters). Specifically, under Dirichlet, the correlation between any two entries is pre-
determined by the mean of each entry and the overall dispersion of the distribution, whereas
the correlation in a multivariate Normal can be freely specified.
Greiner and Quinn (2009) directly addressed these drawbacks of the Rosen et al. (2001) model
by proposing a more flexible model which allows for more correlation within βg. They use
a slightly different count model which models the local counts NgkBgk for each category k
individually rather than the totals across categories Mg:
NgkBgk
| {z }
[J×1]
iid
∼Multinom(Ngk, βgk) for each g, k,
where Bgk and βgk are now [J × 1] vectors describing the conditional outcomes for individuals
in category k and geography g. This setup at least reflects that voters in different racial groups
vote differently.22 Further, to allow for more correlation across each row of βg, Greiner and
Quinn (2009) transform each row βgk to a vector of J −1 logits, picking one of the J choices as
the reference category. These logit preferences are then modeled as a multivariate Normal
distribution, which allows for correlation across the K categories. Unfortunately, their R
implementation is no longer publicly available on CRAN.
Despite these differences in model, the CEF of the outcome is still linear for both R×C models,
just as it is for King’s model and Goodman’s regression. For both models, we have
E[Mg | Ng, Xg] = Ngβ⊤
g Xg.
Thus both models can still be viewed as (multivariate) linear regressions, with residuals
distributed as a discrete mixture of Multinomials.
4.4
Semiparametric modeling
While past ecological inference methods do allow users to incorporate covariates, all of them
impose specific functional forms and are not especially concerned about researcher degrees of
freedom.23 We conclude this section by considering an alternative semiparametric approach
that makes no parametric distribution assumptions about the error term but still estimates the
global estimand correctly, as long as CAR holds. Theoretical developments in semiparametric
statistics apply well to ecological inference because of the accounting identity.
Recall that Eq. 11, reproduced below, always holds once CAR is satisfied with covariates Z:
E[Yg | Zg, Xg] = f (Zg)⊤Xg.
22. A parallel in the 2×2 case is Wakefield (2004)’s contribution over that of King et al. (1999)’s 2×2 setup.
23. Both King (1997) and eiPack’s implementation of Rosen et al. (2001) allow βg to be further modeled as a
linear function of user-specified covariates, but allow no other functional form. As of writing, eiPack only accepts
one covariate, and King (1997) cannot generate estimates when the covariate matrix is rank deficient. Hanushek
et al. (1974) include covariates as controls but do not interact them as Eq. 12 suggests. Modeling the coefficients as
a linear function of the X variables themselves has also been attempted, and is referred to as the linear contextual
model (Blalock 1984).
18


---

Confounders and Linearity in Ecological Inference
Thus, if f (Zg) could be estimated, then following Proposition 3.2, we could estimate β
without any additional assumptions. We now relax the linearity-on-covariates assumption by
expanding Zg into a rich basis Φ(Zg), such as splines, interactions, or trees.24 Well-developed
statistical theory establishes that if the basis expansion Φ is rich enough, and grows richer as
the sample size increases, then f (Zg) can be consistently estimated nonparametrically (see, e.g.
Shen and Wong 1994).
In practice, this involves picking a specific basis expansion Φ, interacting the expanded
Φ(Zg) with Xg, as in Eq. 12, and then regressing Yg on these terms. Linear-in-covariates
is then one out of many possible functional forms. The large number of terms in the basis
expansion Φ means that ordinary least squares will likely overfit, or be unable to be fit at all.
A penalized regression is therefore recommended. The value of the penalty can be selected by
leave-one-out cross-validation, for which a closed-form expression exists for ridge regression.
To achieve the best statistical properties, one additional ingredient is needed: the so-called
Riesz representer for β. For our purposes here, the Riesz representer for racial group k is a set
of weights, one for each geography g, such that weighted averages of Yg with these weights
can estimate β. It can be thought of as a generalization of the inverse propensity score model
for the treatment (here, Xk) in causal inference. Just like the augmented inverse propensity
weighting (AIPW) estimator from causal inference, we can combine the Riesz representer
weights with the fitted regression function to produce a statistically improved estimate of
β. This combination is referred to as double/debiased machine learning (DML, Chernozhukov
et al. 2018).25
We briefly summarize the approach of McCartan and Kuriwaki (2025), which implements this
approach in the R package seine (standing for semiparametric ecological inference):
Procedure 2
1. Fit the linear regression model of Y on expanded covariate bases Φ(Zg) interacted with
Xg.
2. Calculate the Riesz representer weights αk for each racial group k (McCartan and
Kuriwaki 2025).
3. Plug in Xgk = 1 (and Xgk′ = 0 for all k′ ̸= k) into the fitted regression model, which
produces predictions ˆfk(Zg).
4. Augment the fitted regressions with the Riesz representer to form the score for each
geography g and category k,
24. The bases package (McCartan 2025) provides a convenient way to incorporate such preprocessing steps
within the ecological inference procedure.
25. The use of the Riesz representer is motivated by the following challenge. When there are many terms in
Φ(Zg), the ridge penalty in the regression will be large, and the resulting regularization bias will lead to bias in
the primary estimate of β. This is a well-known problem when estimating a high-dimensional nuisance function
(i.e., a function that is not the main parameter of interest, here, f). DML methods address this by learning a
second nuisance function known as the Riesz representer. The DML estimator that combines the two functions is a
generalization of the AIPW estimator (Robins et al. 1995). Like AIPW, DML is doubly robust, and so tolerates
misspecification of either nuisance function, as long as the other is correctly specified.
19


---

Confounders and Linearity in Ecological Inference
sgk = ˆfk(Zg) |G|
g’s share
of group k
z}|{
Ngk
Nk
|
{z
}
imputation
+
ˆαk (Yg −ˆYg)
|
{z
}
debiasing correction
,
where |G| is the number of geographies and ˆYg := ∑k ˆfk(Zg)Xgk is the outcome average
implied from the fitted model.
5. Use the mean of the scores sgk across geographies as the estimate of βk. The standard
deviation of the scores divided by the square root of the number of geographies serves
as its standard error.
This approach has several advantages over EI methods that do not include covariates or only
include covariates through limited functional forms. It is consistent under much weaker
assumptions and has the smallest possible variance as the amount of data increases. By
construction, the regression respects the partially linear form of Eq. 11, since Xg is interacted
with Φ(Zg), while allowing for nonlinearities through the analyst’s use of a basis expansion.
Computationally, it is fast to fit, because both the regression for f and the estimator for the
Riesz representer α have closed-form solutions, and, unlike the early DML literature, we need
not estimate these two components using held-out split samples of the data (Chen et al. 2022).
When outcome Yi is binary or categorical, bounds can be imposed at step 1 to improve the
efficiency of the regression, although the final debiased estimate need not itself satisfy those
bounds. seine also provides estimates for the local parameters, using the Duncan–Davis
bounds under additional assumptions.
5
Empirical Validation
We next turn to two empirical applications of these ecological inference methods, which
illustrate the challenge of meeting the CAR condition. While violations of the assumption are
not observed in practical applications, in rare cases, the ground truth estimand is observed.
We discuss two common applications in political science, each organized by the patterns in
the observable data, the performance of methods in estimating the unobserved quantities of
interest, and patterns of confounding.
5.1
Partisanship and vote choice by race
In the most common application of ecological inference, the outcome Y is an individual’s vote
choice for a candidate or party, and X is the race/ethnic membership of the voter (Greiner
and Quinn 2010; Freedman et al. 1991; Kuriwaki, Ansolabehere, et al. 2024). When a White
majority votes predominantly for Republicans while a sizable Black and Hispanic population
votes predominantly for Democrats, for example, U.S. jurisprudence of the Voting Rights
Act has recognized a need for states to redraw their districts in a way that essentially lets
Democrats win office. Determining if these conditions are met is an ecological inference
problem, because election reporting units contain a mix of White and non-White voters. While
past work has examined ecological inference methods on these problems (see Appendix D),
none have considered how including covariates affects predictive accuracy.
20


---

Confounders and Linearity in Ecological Inference
Here we use North Carolina voters’ party registration on the voter file as a proxy for their
partisan voting behavior, and evaluate how well key ecological inference methods can recover
party registration by race.
Voter files in North Carolina are public, individual-level administrative datasets that include
a registrant’s self-identified racial group, party registration, and precinct. Although party
registration is not vote choice, the two are heavily correlated (Kuriwaki, Ansolabehere, et
al. 2024).
(a) Ground Truth Joint Distribution
Charlotte
Raleigh
Greensboro
Durham
Winston−Salem
Fayetteville
Cary
Wilmington
High Point
Concord
Black
10%
30%
50%
70%80%90%
Charlotte
Raleigh
Greensboro
Durham
Winston−Salem
Fayetteville
Cary
Wilmington
High Point
Concord
Hispanic
5%
10%
15%
20%
25%
(b) Geography of Racial Minorities
Figure 3: The Distribution of Party and Race Registration in North Carolina. We use the voter
file as a proxy validation for measuring racially polarized voting. Panel (a) shows the joint distribution
of party and race as recorded in the state’s public voter file. Cells show row percentages within
each race, and are the quantities of interest. Panel (b) shows the geographic distribution of the two
racial minorities. Black registrants live in the Northeast part of the state (Piedmont) and around
large cities. Hispanic registrants constitute only 5% of the entire dataset and are concentrated in
rural parts of the state.
The North Carolina dataset covers 2,465 precincts, with each precinct averaging about 1,600
voters (See Section D for details on data construction).26 The state is evenly divided between
registered Democrats (31%), Republicans (31%), and non-affiliated voters, but racial groups
sort into distinct party patterns. Only about 19% of White voters register as Democrats, while
74% of Black voters do the same (Figure 3a).
The CCAR condition is violated if voters of the same racial group lean toward different
parties depending on how prevalent their group is in the local geography. Black voters are
about 20% of the dataset, and concentrated around a few of the major cities—Greensboro
and Charlotte—but especially concentrated in the Black Belt of the northeast coastal plains
(Figure 3b). A few precincts are almost completely composed of Black voters: 3 out of the 2,465
precincts are over 95% Black and 17 are over 90% Black. Hispanic voters are only 5% statewide,
but also nonrandomly dispersed. No precinct is more than 27% Hispanic, and about 200
precincts are between 10% and 20% Hispanic. They tend to be concentrated in suburbs around
the center of the state, and residential patterns are correlated with manufacturing, agriculture,
and food processing (Figure 3b).
We test four methods on this data: (1) the semiparametric estimator seine with covariates
26. Although some of these include non-voting active registrants, we refer to all individuals as voters for
simplicity.
21


---

Confounders and Linearity in Ecological Inference
entering through a tensor-product sieve expansion, (2) an OLS regression with no covariates
(i.e., Goodman regression), (3) Rosen et al.’s count model, as implemented in eiPack (Lau
et al. 2007), with no covariates, modeling the 4-by-4 matrix at once, and (4) King’s 2×2 method
applied to each racial group and each outcome separately. The covariates we included in seine
were precinct level education, age, and income as measured from the American Community
Survey, urbanicity as measured by distance to a major city or university, and population
density.
19%
74%
33%
truth: 
0%
25%
50%
75%
100%
Hispanic Voters
Black Voters
White Voters
Registered Democrat
Estimates
seine
(partially linear regression, covariates)
Goodman
(OLS, no covariates)
King's ei
(2 x 2)
Rosen et al.
(count model, 3 x 4)
Figure 4: Accuracy of EI Methods in Uncovering Partisanship among Racial Groups. Ecologi-
cal inference estimates for the percentage of each racial group that is registered for the Democratic
Party, with 95% and 50% confidence intervals. The true values of the registrations are shown in
gray vertical lines and labelled. Estimates from different methods are shown with the black line.
seine includes the covariates education, median income, median age, density, and distance to a
city/university. Rosen et al.’s model refers to the multinomial Dirichlet model available in eiPack.
Estimates for other outcomes are shown in table form in Table S1.
The resulting estimates appear in Figure 4 with the ground truth as a reference point. seine
estimates 17.5% of White voters are registered Democrats with a 95% CI of [0.159, 0.191], where
the true value is 19.5%, and it estimates that 44% of White voters are registered Republicans
with a 95% CI of [0.422, 0.469], where the true value is 42.2%. Neither the Goodman regression
nor King’s EI method have confidence intervals that cover the truth. Their point estimates are
farther from the true values, and their intervals are narrower. Among Hispanic voters, shown
in the bottom row, conventional methods also have worse estimates. Goodman underestimates
the Democratic percentage among Hispanics; the King model estimates overestimate it by
more. This is an unusual case where the Goodman regression and the King model give
opposite answers. seine correctly estimates the Hispanic degree of party registration.
Black voters have more stubborn estimation challenges.
All methods overestimate the
Democratic percentage among Black voters by about 10–20 points. The seine methods come
the closest but the confidence interval does not cover the true values. The overestimation of
Democratic leaning among Black voters also goes hand-in-hand with the underestimation
of the Republican leaning of Black voters. The linear regression-based model gives negative
estimates of −2.0% and −1.6% (Table S1). King and Rosen’s models are advantaged by
constraining estimates to be valid proportions between 0 and 1.
Concerningly, all models miss in the direction of overestimating White vs. Black racial polariza-
tion. In truth, there is a 54 point gap in Democratic party registration between White voters
(19.5% registered Democrat) vs. Black voters (73.8%, see Figure 3 (a)). However, King’s model
estimates the White-Black gap to be 72 points. It makes that mistake by underestimating
22


---

Confounders and Linearity in Ecological Inference
the Democratic registration of White voters by six points and overestimating the Democratic
registration of Black voters by twelve. Adding covariates (seine) reduces this estimation error
by 6 percentage points, but the implied racial gap is still an overestimate.
Finally, Rosen et al.’s count model produces biased estimates similar to linear regression, but
suffers from an additional challenge: Its estimates are highly sensitive to the presence of rare
outcome categories in a way that other methods are not. The count model’s estimates are
similar to the others only when Libertarian votes are grouped together with one of the three
larger groups before estimation. When the small Libertarian outcome choice (comprising
0.6% of the population) is treated as a fourth category instead of being lumped together into
the third, its estimates for other outcome groups change, for example missing the estimate of
Black voters’ Democratic registration by over 40 points (Appendix Table S2).
White
Black
Hispanic
0
25
50
75
0
25
50
75
0
25
50
75
0%
20%
40%
60%
80%
Distance from Nearest City or University (miles)
% Republican
Figure 5: Potential Confounders for Racially Polarized Voting. Each point is a precinct, sorted
by distance to a nearest city or university, a potential confounder, on the horizontal axis. The vertical
axis shows the ground truth level of Republican registration in those racial groups in those precincts
(the local parameter b of interest). A GAM regression showing the line of best fit is shown in blue. A
sample of 500 precincts with at least 20 voters in all three racial groups is shown for clarity.
What sort of confounding does the inclusion of covariates help solve? One potential confounder
is the urbanicity of an area. Urbanicity is clearly correlated with the prevalence of a racial
group. If urbanicity is also correlated with how Democratic the White voters in that region
are, for example, estimates will be biased. In Figure 5, we operationalize urbanicity as the
distance from the center of a large city (as in Rodden 2019) or a R1 university, and show its
relationship with the parameter of interest. The Republican preference of racial groups indeed
differs systematically by the urbanicity of the precinct. White and Hispanic voters in the urban
core are systematically less Republican than in distant areas. Moreover, the relationship is
nonlinear in the distance metric. This suggests that allowing covariates to enter the model in a
flexible functional form as we do with seine’s bases is important. The limited impact of the
covariate in Figure 4 may be due to the limited variability that exists in racial composition
once urbanicity is controlled for.
5.2
Ticket splitting
In studies of ticket splitting the outcome Y is a vote choice in one office, and X is the vote
in another. A voter who votes for party A’s candidate in one office but votes for party B’s
candidate in another office is called a ticket splitter. The prevalence of these ticket splitters
shapes the degree of divided government and measure the degree of nationalized partisan
23


---

Confounders and Linearity in Ecological Inference
behavior. Each geographic unit provides the voteshares of candidates in their respective
contests separately.
We use a tranche of anonymous ballot records (cast vote records) to observe the ground truth
rates of ticket splitting exactly. This dataset from 2020 (Kuriwaki, Reece, et al. 2024) records a
ballot’s vote choice for every contest on a ballot, including President and U.S. House. It also
records the precinct in which the vote was cast. We seek to estimate ticket-splitting rates for
U.S. House candidates in 63 congressional districts.
In this dataset, 5.2% of those who voted for a major-party presidential candidate split their
ticket in the U.S. House race for the opposite party, and 3.9% of them abstained or voted
third party.27 Our validation of EI for ticket splitting is the most comprehensive to date (see
Section D).
As one example, consider the ballots from a part of Wisconsin’s 8th congressional district,
where 16% of those who voted for Joe Biden voted for the Republican incumbent Michael
Gallagher.28 Figure 6(a) shows the observable, aggregate voteshares at the precinct level
in this district. The incumbent’s overperformance appears constant across all levels of the
presidential Democratic lean in the precinct. The best fit line evaluated at X = 1 is at 9%,
which is a substantial underestimate of the true ticket splitting rate of 16%. The line evaluated
at X = 0 implies an impossible value: that 102% of Trump voters voted for Gallagher.
We find that the methods tend to underestimate the degree of ticket splitting, or, in other
words, overestimate the degree of partisan congruence in the two offices. Figure 6(b) compares
the estimates on the vertical axis with the CD-level ground truth on the horizontal axis. The
first Multinomial Dirichlet model by Rosen et al. (2001) estimates ticket splitting rates that
are too low, with over half of the estimates being underestimated by 2 to 3 points.29 King’s
1997 model in the second panel generates estimates that have a lower absolute error than the
count models. Most estimates still underestimate the true levels of ticket splitting by the same
amount.
The Thomsen model, shown in the third facet, does quite well, achieving the lowest mean
absolute error. This is consistent with a similar investigation by Park et al. (2014). The model’s
transformation of input data to the probit scale is consequential for data near the extremes.
We have found that the Thomsen model tends to do well when the global parameters are
small. However, this method is restricted to the 2×2 case, does not support covariates, and
does not produce local estimates. It too tends to underestimate ticket splitting.
The linear regression yields similar, if somewhat noisier, patterns. In panels four and five, we
estimated the regression component by specifying the ridge regression to estimate a solution
that is strictly within [0, 1].30 The models thus avoid producing negative, infeasible estimates
that linear regression is prone to give in this case. Without covariates, the mean absolute
27. Using the covariates we later discuss, we can project our estimates to a hypothetical national population.
Across all 435 congressional districts, we estimate a ticket splitting rate of 5.9% and an abstention/third-party rate
of 4.0%.
28. This may be due to Gallagher’s name recognition as an incumbent, his candidate quality, or his moderate
stance relative to Donald Trump (Kuriwaki 2026).
29. As in our results for North Carolina, differentiating between 4 outcome categories makes the errors even
worse than the binarized version shown here.
30. Misspecifications in flexibly modeling f (Zg) could produce implausible estimates that are out of the possible
range of Y. In these cases, the seine software uses quadratic programming which enforces that the predicted
values of the regression when each Xgk is set to 1 must lie within the range of Y (e.g., 0 to 1).
24


---

Confounders and Linearity in Ecological Inference
Truth: 0.16
0%
25%
50%
75%
100%
0%
25%
50%
75%
100%
Biden (D) Presidential Vote
Gallagher (R) House Vote
(a) Precinct values in WI-08
Med: −2.7p
MAE: 5.7p
Covrg.: 0.29
Med: −2.5p
MAE: 2.9p
Covrg.: 0.08
Med: −2.2p
MAE: 2.4p
Covrg.: 0.17
Med: −2.9p
MAE: 3.4p
Covrg.: 0.10
Med: −2.5p
MAE: 3.1p
Covrg.: 0.16
Med: −3.4p
MAE: 4.1p
Covrg.: 0.32
Multinomial−Dirichlet
King 1997
Thomsen 1987
Goodman + Bounds
Seine Regr. + Bounds
Seine DML
0%
25%
50%
75% 0%
25%
50%
75% 0%
25%
50%
75%
0%
20%
40%
60%
0%
20%
40%
60%
True Ticket Splitting
EI Estimate
(b) Validation of Global Estimates
Figure 6: Predictive Performance of Ticket Splitting. (a) Example of precinct-level data in
Wisconsin’s 8th congressional district. Dotted line indicates a 45 degree line, and blue line is the
OLS best fit. Cross indicates the true percentage of Biden voters who split their ticket for Gallagher.
(b) Each facet shows estimates of congressional district (CD)-level ticket splitting for a given method.
All facets use the same n = 63 CDs. Estimates in the first rows come from Rosen et al. (2001), King
(1997), and Thomsen (1987). The second row comes from the seine software.
Avg. is mean error, MAE is mean absolute error, and Covrg. is empirical coverage of the estimated
95% confidence intervals.
error is 3.4 points, with estimates again underestimating ticket splitting by the same amount.
Including covariates in the regression improves estimates modestly,31 to comparable error
magnitudes as the King model. Finally, while the DML estimate is not bounded and thus has
higher error, its estimated standard errors have the coverage rate closest to nominal coverage
among the six examples tested.
A particular form of CAR violation appears to explain the underestimation of ticket splitting.
In Figure 7, we plot how the degree of ticket splitting in each partisan group varies by the
partisan lean of the precinct. Biden voters are least likely to split their ticket when they are in
nearly unanimous Biden precincts (left panel). Similarly, Trump voters are least likely to split
their ticket when they are in nearly unanimous Trump precincts (right panel).
Put together, voters in precisely the precincts that have disproportionate leverage in the regres-
sion are systematically different from other voters, in a way that is prone to underestimation
of ticket splitting. Furthermore, because the confounding is due to the group composition
itself, controlling for relevant confounders leaves little variation to identify the parameters.
5.3
Sensitivity to Confounders
In practical applications, there is no ground truth to validate against. Practitioners cannot
tell how much the use of covariates actually improves the estimates. Further, although the
semiparametric estimator removes some researcher degrees of freedom, researchers still
31. We include the following covariates: county-level median income, county-level proportion White, county
population density, county-level proportion of elderly residents, and indicators for five equally populated bins of
the precinct-level presidential vote. The limited impact of covariates we see in this example may be due to the fact
that the covariates we could collect (county-level) were much coarser than the geographic units (precinct-level).
25


---

Confounders and Linearity in Ecological Inference
among Biden voters
among Trump voters
0%
25%
50%
75%
100% 0%
25%
50%
75%
100%
0%
10%
20%
30%
Precinct−level Vote for Biden
Ticket Splitting
Figure 7: Variation in Ticket Splitting Rates. The relationship between X and quantities of
interest across a random sample of 500 precincts with more than 100 voters for visual clarity. Each
point is a sampled precinct, sorted on the horizontal axis by the percentage of total votes for the
Democratic presidential candidate. Local estimands Bg are heavily correlated with X.
choose which basis expansion to use. And fundamentally, these methods can only use
covariates that are observed by the researcher. In short, CAR is an untestable assumption.
The sensitivity analysis developed in new work can address these concerns, and applying it to
the three examples in the paper is instructive.
Suppose that CAR holds conditional on observed covariates Z and an unobserved variable
U. We denote the estimand for category k when conditioning under both Z and U as βk, and
denote the (incorrect) result in the short regression where the unobserved U is not included as
βshort. McCartan and Kuriwaki (2025), extending work from Chernozhukov et al. (2026), show
that the bias from the short regression, bias := βshort
k
−βk, has magnitude bounded by:
|bias| ≤ρ S Cγ Cα,
(18)
where ρ is a correlation that has a maximum value of 1, S is a scaling factor that can be
estimated by observed data, and the two variables C are confounding measures that are
interpretable as the relevance of the unobserved variable:32
C2
γ = R2
Y∼U|X,Z
and
C2
α ≈increasing in R2
X∼U|Z.
(19)
Each R2 above is a partial R2 of linear regressions using our variables.33 That is, the worst
case absolute bias of the observable estimate can be bounded under scenarios of hypothetical
confounding between the confounder and the outcome (Cγ) and the confounder and the
predictor (Cα). We can suggest reasonable values of these quantities by benchmarking with
values that replace U with observed variables.
Figure 8 plots the resulting biases. Each panel is best read in three steps: start with the
point estimate given by the regression, find a value of the contour lines that would reverse
32. See McCartan and Kuriwaki (2025) for a more detailed discussion of the interpretation of C2α.
33. The partial R2
y ∼u|x is computed by first regressing y and u on x and taking residuals, and then calculating
the standard R2 of the residuals of y on the residuals of u.
26


---

Confounders and Linearity in Ecological Inference
0.005
0.120
0.200
0.600
1.000
2.000
state
pop_city
educ_coll
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6 0.8 1.0
Predictor confounding (R²)
Outcome confounding (R²)
E(Wallace | White) − E(Wallace | Black)
Observed estimate = −0.098
Wallace Vote
0.10
0.25
0.50
0.67
med. income
urbanicity
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6 0.8 1.0
Predictor confounding (R²)
Outcome confounding (R²)
E(Dem | Black) − E(Dem | White)
Observed estimate = 0.668
North Carolina
0.01
0.02
0.05
% college
Hispanic
0.00
0.05
0.10
0.15
0.00
0.05
0.10
0.15
Predictor confounding (R²)
Outcome confounding (R²)
E(House R | President D)
Observed estimate = 0.010
Ticket Splitting
Figure 8: Evaluating Sensitivity to Unobserved Confounding. Contour lines show the absolute
value of the bias that an unobserved confounder could induce in the point estimate as a function of
its confounding with the outcome (y-axis) and conditioning predictor variable (x-axis). Axes are on
the square-root scale. Each panel is titled by the quantity of interest and its point estimate using
the observed covariates. See appendix for data and implementation details.
the estimate to a substantial amount, then ask whether such an unobserved confounder is
plausible given the benchmarked observed covariates.
The first example of the Wallace vote differential between White and non-Whites has the
wrong sign (−0.098). Any combination of the confounding values C that leads to a contour
value of about that magnitude could, in other words, mask a true null. To assess whether a
bias of such magnitude could plausibly occur, we look to the associated confounding of the
existing covariates, shown as orange points. The variable state has the highest associated bias
of nearly 1, meaning that omitting that variable could induce a bias of nearly 1 on the –1 to 1
scale. This is consistent with the large state-by-state heterogeneity we see in the raw data of
Figure 1.
The other panels lead to different conclusions. In the middle North Carolina panel, the point
estimate is of the correct sign, but overestimated by about 10 points. Leaving out each of
the existing covariates, such as urbanicity and income, only leads to additional biases of less
than 0.10. It is hard for us to think of a covariate not already in the model that would be
strong enough to overturn the result to zero, and so we remain confident in the finding of
racially polarized registration. In the right panel, the estimate for ticket splitting is only a
single percentage point. The benchmark covariate’s associated bias is small, but so are the
estimates themselves. Here we conclude that controlling for other covariates could reasonably
affect the estimate.
6
Conclusion
This paper offers a perspective to understand the problem of inferring conditional means
from aggregate data, a technique known as ecological inference. Our framework shows how
all ecological inference methods for point identification are fundamentally similar in their use
of regression. Existing literature on ecological inference often treats linear regression as a
simplistic approximation to a more complicated data structure. But that may have obscured
the fundamental problem of controlling for confounders. Unless these are controlled for,
27


---

Confounders and Linearity in Ecological Inference
ecological inference of any sort introduces bias. The recent literature has also underemphasized
how the fact of linearity in aggregate data aids estimation of models with covariates, which in
turn invites recent innovations in semiparametric models.
Using this framework, we evaluated two applications of ecological inference in political science
where ground truth is observed. EI estimates of racial differences in partisanship tend to be
overestimated because racial minorities are typically more Democratic-leaning in concentrated
areas than in diverse ones. EI estimates of ticket splitting tend to be underestimated in
recent elections because the correlation of voteshares between offices is strong, and a party’s
supporters tend to split their ticket less in concentrated areas than in diverse ones. In the first
example, inclusion of covariates reduces the impact of ecological fallacies, while improvements
in point estimates are less clear in the second. The intuition and challenges of observational
causal inference, such as controlling for confounders while retaining enough variation in the
residualized treatment for stable estimation, carry on to ecological inference.
In future research, more covariates can be brought to specific empirical problems, possibly
from multiple levels of aggregation where the covariates and group membership are measured
at the individual level but outcomes are measured at the aggregate level, or in cases where
individual survey data is available to assist modeling. Sensitivity analyses can be used to
understand and make more credible ecological inferences. In studies of geographies, modeling
the residential sorting decisions of individuals may be fruitful, as it also can open a framework
for design-based inference (Abadie et al. 2020). Ecological inference is a challenging missing
data problem, but our reassessment points to several promising directions.
References
Abadie, Alberto, Susan Athey, Guido W. Imbens, and Jeffrey M. Wooldridge. 2020. “Sampling-
Based Versus Design-Based Uncertainty in Regression Analysis.” Econometrica 88 (1):
265–296.
Achen, Christopher H., and W. Phillips Shively. 1995. Cross-Level Inference. University of
Chicago Press.
Anselin, Luc, and Wendy K. Tam Cho. 2002. “Spatial Effects and Ecological Inference.” Political
Analysis 10 (3): 276–297.
Ansolabehere, Stephen, and Douglas Rivers. 1995. “Bias in Ecological Regression.” Mas-
sachusetts Institute of Technology.
Baccini, Leonardo, and Stephen Weymouth. 2021. “Gone for Good: Deindustrialization, White
Voter Backlash, and US Presidential Voting.” American Political Science Review 115 (2):
550–567.
Blackwell, Matthew. 2025. A User’s Guide to Statistical Inference and Regression. CRC Press.
Blalock, Hubert M. 1984. “Contextual Effects Models: Theoretical and Methodological Issues.”
Annual Review of Sociology, 353–372.
Brown, Philip J., and Clive D. Payne. 1986. “Aggregate Data, Ecological Regression, and Voting
Transitions.” Journal of the American Statistical Association 81 (394): 452–460.
28


---

Confounders and Linearity in Ecological Inference
Burden, Barry C., and David C. Kimball. 2009. Why Americans Split Their Tickets: Campaigns,
Competition, and Divided Government. University of Michigan Press.
Chambers, Raymond L., and David G. Steel. 2001. “Simple Methods for Ecological Inference
in 2 x 2 Tables.” Journal of the Royal Statistical Society: Series A (Statistics in Society) 164 (1):
175–192.
Chatterjee, Samprit, and Ali S. Hadi. 1986. “Influential Observations, High Leverage Points,
and Outliers in Linear Regression.” Statistical Science, 379–393.
Chen, Qizhao, Vasilis Syrgkanis, and Morgane Austern. 2022. “Debiased Machine Learning
Without Sample-Splitting for Stable Estimators.” Advances in Neural Information Processing
Systems 35:3096–3109.
Chernozhukov, Victor, Carlos Cinelli, Whitney Newey, Amit Sharma, and Vasilis Syrgkanis.
2026. Long Story Short: Omitted Variable Bias in Causal Machine Learning. Technical report.
https://doi.org/10.1162/REST.a.1705.
Chernozhukov, Victor, Whitney K. Newey, and James Robins. 2018. Double/Debiased Machine
Learning Using Regularized Riesz Representers. Technical report. cemmap Working Paper.
Cho, Wendy K. Tam, and Brian J. Gaines. 2004. “The Limits of Ecological Inference: The Case
of Split-Ticket Voting.” American Journal of Political Science 48 (1): 152–171.
Colantone, Italo, and Piero Stanig. 2018. “Global Competition and Brexit.” American Political
Science Review 112 (2): 201–218.
Cross, Philip J., and Charles F. Manski. 2002. “Regressions, Short and Long.” Econometrica 70
(1): 357–368.
Cunningham, John P., Philipp Hennig, and Simon Lacoste-Julien. 2011. “Gaussian Probabilities
and Expectation Propagation.” arXiv preprint arXiv:1111.6832.
Duncan, Otis Dudley, and Beverly Davis. 1953. “An Alternative to Ecological Correlation.”
American Sociological Review 18 (6).
Elzayn, Hadi, Jacob Goldin, Cameron Guage, Daniel E. Ho, and Claire Morton. 2025. “Monotone
Ecological Inference.” National Bureau of Economic Research (34285).
Fan, Jianqing, and Wenyang Zhang. 1999. “Statistical Estimation in Varying Coefficient Models.”
The Annals of Statistics 27 (5): 1491–1518.
Freedman, David A., Stephen P. Klein, Jerome Sacks, Charles A. Smyth, and Charles G. Everett.
1991. “Ecological Regression and Voting Rights.” Evaluation Review 15 (6): 673–711.
Gelman, Andrew, David K. Park, Stephen Ansolabehere, Phillip N. Price, and Lorraine C.
Minnite. 2001. “Models, Assumptions, and Model Checking in Ecological Regressions.”
Journal of the Royal Statistical Society Series A: Statistics in Society 164 (1): 101–118.
Glynn, Adam N., Jon Wakefield, Mark S. Handcock, and Thomas S. Richardson. 2008.
“Alleviating Linear Ecological Bias and Optimal Design with Subsample Data.” Journal of
the Royal Statistical Society Series A: Statistics in Society 171 (1): 179–202.
Goodman, Leo A. 1953. “Ecological Regressions and Behavior of Individuals.” American
Sociological Review 18 (6).
29


---

Confounders and Linearity in Ecological Inference
Goodman, Leo A. 1959. “Some Alternatives to Ecological Correlation.” American Journal of
Sociology 64 (6): 610–625.
Greiner, D. James, and Kevin M. Quinn. 2009. “R x C Ecological Inference: Bounds, Correlations,
Flexibility, and Transparency of Assumptions.” Journal of the Royal Statistical Society Series
A: Statistics in Society 172 (1): 67–81.
. 2010. “Exit Polling and Racial Bloc Voting: Combining Individual-Level and R x C
Ecological Data.” The Annals of Applied Statistics, 1774–1796.
Griffiths, William E. 1972. “Estimation of Actual Response Coefficients in the Hildreth-Houck
Random Coefficient Model.” Journal of the American Statistical Association 67 (339): 633–635.
Hanushek, Eric A., John E. Jackson, and John F. Kain. 1974. “Model Specification, Use of
Aggregate Data, and the Ecological Correlation Fallacy.” Political Methodology, 89–107.
Hastie, Trevor, and Robert Tibshirani. 1993. “Varying-Coefficient Models.” Journal of the Royal
Statistical Society Series B: Statistical Methodology 55 (4): 757–779.
Heitjan, Daniel F., and Donald B. Rubin. 1991. “Ignorability and Coarse Data.” The Annals of
Statistics, 2244–2253.
Imai, Kosuke, Ying Lu, and Aaron Strauss. 2008. “Bayesian and Likelihood Inference for 2x2
Ecological Tables: An Incomplete-Data Approach.” Political Analysis 16 (1): 41–69.
Jiang, Wenxin, Gary King, Allen Schmaltz, and Martin A. Tanner. 2020. “Ecological Regression
with Partial Identification.” Political Analysis 28 (1): 65–86.
King, Gary. 1997. A Solution to the Ecological Inference Problem: Reconstructing Individual Behavior
from Aggregate Data. Princeton University Press.
King, Gary, Ori Rosen, and Martin A. Tanner. 1999. “Binomial-Beta Hierarchical Models for
Ecological Inference.” Sociological Methods & Research 28 (1): 61–90.
Kovenock, David M., and James W. Prothro. 1968. “Comparative State Elections Project, 1968.”
ICPSR Study No. 7508 (Ann Arbor, MI), https://doi.org/10.3886/ICPSR07508.v1.
Kuriwaki, Shiro. 2026. “Ticket Splitting in a Nationalized Era.” The Journal of Politics 88 (1):
47–62.
Kuriwaki, Shiro, Stephen Ansolabehere, Angelo Dagonel, and Soichiro Yamauchi. 2024.
“The Geography of Racially Polarized Voting: Calibrating Surveys at the District Level.”
American Political Science Review 118 (2): 922–939.
Kuriwaki, Shiro, Mason Reece, Samuel Baltz, Aleksandra Conevska, Joseph R. Loffredo, Can
Mutlu, Taran Samarth, Kevin E. Acevedo Jetter, Zachary Djanogly Garai, Kate Murray,
Shigeo Hirano, Jeffrey B. Lewis, James M. Snyder Jr., and Charles Stewart III. 2024. “Cast
Vote Records: A Database of Ballots from the 2020 US Election.” Scientific Data 11 (1): 1304.
Lau, Olivia, Ryan T. Moore, and Michael Kellermann. 2007. “eiPack: R x C Ecological Inference
and Higher-Dimension Data Management.” New Functions for Multivariate Analysis 7 (1):
43.
Lewis, Jeffrey B. 2001. “Understanding King’s Ecological Inference Model: A Method-of-
Moments Approach.” Historical Methods: A Journal of Quantitative and Interdisciplinary
History 34 (4): 170–188.
30


---

Confounders and Linearity in Ecological Inference
McCartan, Cory. 2025. bases: Basis Expansions for Regression Modeling. R package version 0.1.2.
https://corymccartan.com/bases/.
McCartan, Cory, and Shiro Kuriwaki. 2025. “Identification and Semiparametric Estimation of
Conditional Means from Aggregate Data.” arXiv preprint arXiv:2509.20194.
Park, Won-ho, Michael J. Hanmer, and Daniel R. Biggers. 2014. “Ecological inference under
unfavorable conditions: Straight and split-ticket voting in diverse settings and small
samples.” Electoral Studies 36:192–203.
Pavía, Jose M., and Rafael Romero. 2024. “Improving estimates accuracy of voter transitions.
Two new algorithms for ecological inference based on linear programming.” Sociological
Methods & Research 53 (3): 1491–1533.
Phillips, Kevin P. 2014. The Emerging Republican Majority: Updated Edition. Princeton University
Press.
Rivers, Douglas. 1998. “Review of: A Solution to the Ecological Inference Problem by Gary
King.” American Political Science Review 92 (2): 442–443.
Robins, James M., Andrea Rotnitzky, and Lue Ping Zhao. 1995. “Analysis of Semiparametric
Regression Models for Repeated Outcomes in the Presence of Missing Data.” Journal of
the American Statistical Association 90 (429): 106–121.
Robinson, W. S. 1950. “Ecological Correlations and the Behavior of Individuals.” American
Sociological Review 15 (3): 351–357.
Rodden, Jonathan A. 2019. Why Cities Lose: The Deep Roots of the Urban-Rural Political Divide.
Basic Books.
Rosen, Ori, Wenxin Jiang, Gary King, and Martin A. Tanner. 2001. “Bayesian and Frequentist
Inference for Ecological Inference: The R x C Case.” Statistica Neerlandica 55 (2): 134–156.
Schoenberger, Robert A., and David R. Segal. 1971. “The Ecology of Dissent: The Southern
Wallace Vote in 1968.” Midwest Journal of Political Science 15 (3): 583–586.
Shen, Xiaotong, and Wing Hung Wong. 1994. “Convergence Rate of Sieve Estimates.” The
Annals of Statistics, 580–615.
Teele, Dawn Langan. 2024. “The Political Geography of the Gender Gap.” The Journal of Politics
86 (2): 428–442.
Thomsen, Søren Risbjerg. 1987. “Danish Elections 1920-79: A Logit Approach to Ecological
Analysis and Inference.” Politica.
Wakefield, Jon. 2004. “Ecological Inference for 2 x 2 Tables (with Discussion).” Journal of the
Royal Statistical Society Series A: Statistics in Society 167 (3): 385–445.
Wright, Gerald C. 1977. “Contextual Models of Electoral Behavior: The Southern Wallace Vote.”
American Political Science Review 71 (2): 497–508.
Wu, Kaiwen, and Jacob R. Gardner. 2024. “A Fast, Robust Elliptical Slice Sampling Imple-
mentation for Linearly Truncated Multivariate Normal Distributions.” arXiv preprint
arXiv:2407.10449.
31


---

Confounders and Linearity in Ecological Inference
A
Methodological Developments in Ecological Inference
We summarize the proposals made in the literature for ecological inference. The list below
captures, to our knowledge, most of the major work proposing a new method or methodological
adjustment to ecological inference. We omit work whose main purpose is to evaluate the
numerical performance of an existing method.
All of the work cited in this appendix, with the possible exception of the Thomsen model,
leverages the accounting identity. For example, the identity appears as the tomography line in
King’s framework, as linear constraints in the optimization approach, and as the source of the
sharp bounds in Duncan and Davis (1953).
Ecological Inference before 1997
(1) Classical foundations: Robinson (1950), Goodman (1953), Goodman (1959)
(2) Summary of literature and applications to political science: Achen and Shively (1995)
(3) Inclusion of control variables: Hanushek et al. (1974)
(4) Neighborhood model: Freedman et al. (1991)
(5) Latent utility model: Thomsen (1987)
(6) Multinomial models for (R×C) elections: Brown and Payne (1986)
Comment: Our article discusses these foundational papers. Cleave et al. (1995) is a useful
review of this literature. They provide a validation exercise comparing Goodman regression,
Brown and Payne multinomial count models, the Thomsen latent utility model, and raking
with survey data.
Literature adjacent to King (1997), in political science and statistics
(7) Binomial and multinomial count models: beta-binomial models (King et al. 1999),
a binomial model for cell-specific counts rather than row/column-aggregate counts
(Wakefield 2004), R×C multinomial Dirichlet count models (Rosen et al. 2001), R×C
models allowing for correlation across precincts (Greiner and Quinn 2009)
(8) Relaxing parametric assumptions on the error term: Imai et al. (2008)
(9) Geographic adjacency: Calvo and Escolar (2003), Anselin and Cho (2002)
(10) Local smoothing and geographic subgroup clustering: Chambers and Steel (2001), Puig
and Ginebra (2015)
(11) Diagnostic tools for Goodman regression: Gelman et al. (2001)
(12) Integrating survey data: Greiner and Quinn (2010), Glynn et al. (2008)
(13) A fast method-of-moments estimator reallocating residuals: Lewis (2001)
(14) Fast approximations for local estimates: Grofman and Merrill (2004)
(15) Temporal dependency across precincts: Quinn (2004), Lewis (2004)
(16) Using ecological inference output as an independent variable: Herron and Shotts (2003)
Comment: King (1997) is extensively discussed in our paper; also see (13). Both (7) and (8) are
also discussed in the main text. (9) and (10) seek to leverage the information that geographic
adjacency provides when the groupings are geographic and their coordinates are available.
Others have thought to improve estimation by integrating survey data (12). Proposals such as
(15) and (16) consider models and pitfalls for common types of ecological data.
The use of covariates is not the focus for this group of papers. For example, (11) discuss
32


---

Confounders and Linearity in Ecological Inference
diagnostics for when regression is not appropriate, but not covariates. However, some of these
propose ways to incorporate covariates in a particular functional form: Ansolabehere and
Rivers (1995), King et al. (1999), Wakefield (2004), and Park (2008).
Partial identification with bounds
(17) Narrowing Duncan–Davis bounds by assumptions on the functional form of contextual
effects: Jiang et al. (2020), Manski (2018), Elzayn et al. (2025)
(18) Derived bounds in a wider class of regressions: Cross and Manski (2002)
(19) Sampling uncertainty on the bounds: Fan et al. (2016)
Comment: Our article has focused on point estimation. There is a rich literature on partial
identification with bounds in several statistical traditions as well (17). In economics, ecological
inference is treated as an example of a data integration problem—see (18) and (19).
In other disciplinary traditions, work distinct from King’s model
(20) Ecological inferences with continuous predictor (price) and instruments for predictor:
Berry et al. (2004) (BLP); flexible functional forms with microdata: Berry and Haile
(2024)
(21) Modeling with individual data and aggregate outcomes: Flaxman et al. (2015), Rosenman
and Viswanathan (2018), Fishman and Rosenman (2024)
(22) Extensions of Thomsen’s regression: Park (2008) incorporates covariates, while Pavía
and Thomsen (2025) generate local estimates and provide software for R×C tables
(23) Linear programming with constraints: Pavía and Romero (2024)
Comment: The field of industrial organization in economics, as in (20) is an example of
estimating individual parameters with aggregate data. (21) work in settings where a regression
with covariates and outcome are jointly observed at the individual level (in a sample), combined
with a constraint that their sums add up to a certain count. As discussed in our paper,
optimization approaches such as (23) can be thought of as passing parametric assumptions
to the loss function. The Thomsen model has been extended in (22) with similar extensions
discussed in our paper.
B
Proofs of propositions
B.1
Relationship between local and global parameters
The local means are connected to the global mean in a similar way as the individual data are
connected to the local parameters.
Bk := 1
Nk ∑
i∈Ik
Yi = 1
Nk ∑
g ∑
i∈Igk
Yi = 1
Nk ∑
g
Ngk
1
Ngk
| {z }
=1
∑
i∈Igk
Yi = ∑g NgkBgk
∑g Ngk
.
The last equality follows from Eq. 2 and because Nk = ∑g Ngk.
33


---

Confounders and Linearity in Ecological Inference
B.2
Proof of Proposition 3.1
Proof. When Z is empty, CAR and CCAR coincide. In this case, Proposition 3.1 follows
immediately from Proposition 3.2, because as shown in the main text, Proposition 3.2 implies
that the true CEF is linear in Xg.
B.3
Proof of Proposition 3.2
Proof. The CAR assumption implies E[Bg | Zg, Xg] = E[Bg | Zg] by the law of total expectation
(integrating out Ng). Applying this property once to drop the conditioning on Xgk = 1 (which,
by the sum-to-1 constraint, fixes Xg) and applying CAR to condition on Xg and Ng,
E[Ngk E[Yg | Zg, Xgk = 1]] = E[Ngk E[B⊤
g Xg | Zg, Xgk = 1]]
= E[Ngk E[Bgk | Zg, Xgk = 1]]
= E[Ngk E[Bgk | Zg]]
= E[Ngk E[Bgk | Zg, Xg, Ng]]
= E[E[NgkBgk | Zg, Xg, Ng]]
= E[NgkBgk] = E[Ngk]βk.
Dividing by E[Ngk] yields the result.
C
Details on Other Models
C.1
King’s 2×2 model
This appendix gathers additional detail on the ecological inference models surveyed in
Section 4 that is useful for context but not essential to the main argument. Beyond the
discussion in Section 4, a further distinction between King’s model and Goodman’s model is
in its use of the local and global parameters. Goodman’s regression does not estimate the
Bg and can only estimate the superpopulation parameter. In King, the global β is readily
calculable as the mean of the estimated truncated Normal N [0,1]2(µ, Σ) distribution (our µ
corresponds to King’s B). Because the form of King’s model and Goodman’s regression are
the same, they will produce the same estimates for β asymptotically.
In the causal inference analogy, the mean of N [0,1]2(µ, Σ) estimates the superpopulation β,
while the mean of the posterior distribution of Bg estimates the finite-sample effect B. However,
King does not advocate using this as the estimate of β. Rather, because he works in the Bayesian
framework, he recommends estimating B itself from a weighted mean of the estimated Bg.
The posterior distribution of these local parameters is the original N [0,1]2(µ, Σ) distribution
restricted to the tomography line defined by the accounting identity, Yg = Bg1Xg1 + Bg2Xg2.
Beyond very small samples, the difference between B and β is often negligible. Grofman
and Merrill (2004) suggest some approximations to obtain local parameters from a Goodman
regression.
34


---

Confounders and Linearity in Ecological Inference
Table S1: Accuracy of EI Methods in Uncovering Partisanship among Racial Groups, all Out-
come Categories. Estimates are point estimates with standard errors in parentheses. Estimates
are for the conditional expectation E(Outcome | Predictor). The truth column indicates the voter file
ground truth. The estimates for Democrats are shown in Figure 4.
Estimates
Estimand
Truth
Seine
Goodman
Rosen
King
Pr(Dem | White)
0.195
0.176 (0.008)
0.175 (0.005)
0.178 (0.003)
0.138 (0.002)
Pr(Dem | Black)
0.738
0.842 (0.031)
0.848 (0.031)
0.833 (0.015)
0.858 (0.005)
Pr(Dem | Hispanic)
0.332
0.287 (0.042)
0.081 (0.003)
0.123 (0.044)
0.859 (0.011)
Pr(Ind. | White)
0.383
0.374 (0.013)
0.364 (0.011)
0.381 (0.003)
0.398 (0.001)
Pr(Ind. | Black)
0.234
0.199 (0.009)
0.168 (0.006)
0.153 (0.008)
0.224 (0.003)
Pr(Ind. | Hispanic)
0.488
0.638 (0.037)
0.806 (0.031)
0.814 (0.077)
0.275 (0.012)
Pr(GOP | White)
0.422
0.450 (0.011)
0.461 (0.014)
0.441 (0.005)
0.443 (0.001)
Pr(GOP | Black)
0.028
-0.041 (0.007)
-0.016 (0.002)
0.014 (0.008)
0.007 (0.000)
Pr(GOP | Hispanic)
0.180
0.075 (0.043)
0.113 (0.005)
0.063 (0.036)
0.003 (0.000)
D
Details on Empirical Validations
D.1
Wallace 1968: Turnout and the Voting Rights Act
The y-axis in Figure 1 measures Wallace votes as a share of the voting-age population (VAP),
not as a share of votes cast. This complicates the interpretation because 1968 was the first
general election following the Voting Rights Act of 1965, and Black voter registration and
turnout in the South lagged that of White voters. Turnout registration statistics by racial
group are not available for these historical elections, but a 1969 U.S. Census report estimates,
using surveys, that turnout among Black registrants in this election lagged White voters by
approximately 10 points in the South (see http://bit.ly/4lsvOKu). By using VAP as the
denominator, the y-axis in Figure 1 treats not turning out as an implicit outcome category, so
the figure is in part an ecological inference about differential turnout rather than vote choice
alone. This does not affect the substantive conclusion—Black voters overwhelmingly did not
support Wallace—but it should be kept in mind when reading the magnitudes.
D.2
Racial Voting Estimates
The voter file we used to create our precinct data was downloaded from the North Carolina
State Board of Elections (NCSBE) public website in July 2025. We then standardized precinct
labels so that it would match exactly to a precinct in the NCSBE’s precinct 2025 shapefiles.
We merged in covariates by obtaining block-group level ACS 2023 estimates of education,
age, and income, projecting counts to the block level according to total population, and then
aggregated the resulting counts up to the precinct level.
Table S1 compares the estimates of four ecological inference models in tabular form. See
Figure 4 and the main text for the descriptions of each estimate.
Past work has compared different EI methods in the racial polarization application. de
Benedictis-Kessner (2015) evaluates five EI methods on similar voter file data and finds that
King (1997)’s 2×2 and Rosen et al. (2001)’s count model have lower estimation error than
Goodman’s regression, but only explores where and why errors differ across methods in a
35


---

Confounders and Linearity in Ecological Inference
Table S2: Count Models’ Estimates are Sensitive to Treatment of Small Groups. The “3 x
4” column shows estimates from Rosen et al.’s model used in the main text, where the 0.6% of
the population that are registered Libertarian are grouped together with Independents. The “4 x
4” shows the estimates when Libertarians are treated as a separate outcome category. Standard
errors in parentheses. Estimates change substantively by this specification, even those for other
outcome categories (Democrat and Republican). North Carolina data.
Estimates, by eiPack specification
Estimand
Truth
3 x 4
4 x 4
Pr(GOP | White)
0.422
0.441 (0.005)
0.354 (0.005)
Pr(GOP | Black)
0.028
0.014 (0.008)
0.226 (0.011)
Pr(GOP | Hispanic)
0.180
0.063 (0.036)
0.262 (0.005)
Pr(Dem | White)
0.195
0.178 (0.003)
0.279 (0.005)
Pr(Dem | Black)
0.738
0.833 (0.015)
0.424 (0.014)
Pr(Dem | Hispanic)
0.332
0.123 (0.044)
0.359 (0.008)
cursory fashion.34 Barreto et al. (2022) compares differences between King (1997) and Rosen
et al. (2001) methods on election results and finds similar estimates, but does not diagnose
which one more correctly captures the ground truth. Kuriwaki et al. (2024) studies the accuracy
of Rosen et al. (2001)’s method on a Florida voter file and finds that confidence intervals are
too tight.
D.3
Cast Vote Record Data
Figure S1 shows an overview of this data. The table in panel (a) shows row percentages
that sum to 100% in each row. Among the 20 million or so ballots cast for Joseph Biden, the
Democratic candidate for President, 5.6% voted for a Republican candidate, and 4% either
skipped the House race (undervote) or voted for a third-party candidate. In panel (b) we
show the level of ticket splitting among Trump voters (on the horizontal axis) against the
level of ticket splitting among Biden voters in the same district (on the vertical axis). The
two quantities of interest are negatively correlated. Some districts exhibit substantial ticket
splitting for the Republican, and others exhibit splitting for the Democrat. These two variables
cancel out when added to the entire population in (a).
We limit our analysis to the districts that are contested by a Democratic and Republican
House candidate and whose CVR data contain at least 3 different counties. We impose the
latter condition because the covariates we will use are measured at the county level, so a
district contained wholly within one county has no variation in the covariate. The median
congressional district fragment contains 177 precincts.35
34. de Benedictis-Kessner (2015) computes the average precinct-level error in the estimates of percentage White,
Black, and Hispanic voters registering Democrat. He finds that Goodman regression’s error is over 68 points,
Goodman regression with post-hoc truncation has an average error of 25 points, and the King (1997) and Rosen
et al. (2001) methods both have errors around 15 points. Even the smallest of these errors is still substantial. We
suspect that estimating the global parameter (district or statewide quantities) rather than precinct-level local
parameters is much less error-prone. de Benedictis-Kessner (2015) discusses how differences in errors may be
explained by the racial composition of the five states he studies (373) or the racial composition of the county (377)
but does not lay out a specific hypothesis.
35. Ballot records are collected county by county. Each district’s collection of ballots is only a partial set of the
district’s counties. The districts of the final data are in AZ, CA, CO, FL, GA, IL, MD, MI, NJ, NV, OH, OR, TX, and
WI.
36


---

Confounders and Linearity in Ecological Inference
(a) All available records
CA−03
CA−09
CA−16
IL−18
TX−15
TX−28
TX−34
WI−08
0%
5%
10%
15%
20%
0%
5%
10%
15%
20%
Trump voters who vote for Democrat
Biden voters who vote for Republican
(b) Estimands, by district
Figure S1: Ticket Splitting Patterns from Election Data. The distribution of vote choices in
the 2020 election data from ground truth cast vote records. (a) Across all districts available in the
dataset, approximately 5% of Biden voters and Trump voters vote for a different party’s candidates
in the U.S. House race. These quantities of interest are off-diagonal entries and cancel out when
aggregated. (b) Quantities of interest, separated for each congressional district. In typical districts
ticket splitting is asymmetric and benefits one candidate more than their opponent.
Burden and Kimball (1998) and Burden and Kimball (2009) were the first to use ecological
inference methods, applying King’s ((1997)) algorithm on congressional district level aggregate
data. Cho and Gaines (2004) critiqued the uninformativeness of aggregate data in the case
of ticket splitting. Neither work had access to ground truth levels of ticket splitting. Other
countries such as Austria and New Zealand reported vote results in a way that allowed ticket
splitting rates to be computed from ballots (Klima et al. 2016; Pavía and Romero 2024). By
the 2010s, as some U.S. states started to release cast vote records, Park et al. (2014) evaluated
King’s EI model and Thomsen’s nonlinear regression model in ten counties. They did not test
other models or include covariates.
D.4
Sensitivity Analysis
Figure 8 estimates sensitivity bounds with the following specifications.
• Wallace data: We expand the example from Figure 1 to eleven former Confederate states.
We include as covariates a categorical variable for state, proportion of the population
in farm households, proportion of the population with elementary, high school, and
college education, proportion of the population in households in one of four income
brackets. All data is at the county level.
• North Carolina data: We use the same data and covariates in Figure 4.
• Cast vote record data: We use the same data and covariates as used in Figure 6.
For all three datasets, we compute a DML estimate. For computational feasibility we enter the
covariates linearly, without interactions or spline transformation.
37


---

Confounders and Linearity in Ecological Inference
References
Achen, Christopher H., and W. Phillips Shively. 1995. Cross-Level Inference. University of
Chicago Press.
Anselin, Luc, and Wendy K. Tam Cho. 2002. “Spatial Effects and Ecological Inference.” Political
Analysis 10 (3): 276–297.
Ansolabehere, Stephen, and Douglas Rivers. 1995. “Bias in Ecological Regression.” Mas-
sachusetts Institute of Technology.
Barreto, Matt, Loren Collingwood, Sergio Garcia-Rios, and Kassra A. R. Oskooii. 2022.
“Estimating Candidate Support in Voting Rights Act Cases: Comparing Iterative EI and
EI-R x C Methods.” Sociological Methods & Research 51 (1): 271–304.
Berry, Steven, and Philip Haile. 2024. “Nonparametric Identification of Differentiated Products
Demand Using Micro Data.” Econometrica 92 (4): 1135–1162.
Berry, Steven, James Levinsohn, and Ariel Pakes. 2004. “Differentiated Products Demand
Systems from a Combination of Micro and Macro Data: The New Car Market.” Journal of
Political Economy 112 (1): 68–105.
Brown, Philip J., and Clive D. Payne. 1986. “Aggregate Data, Ecological Regression, and Voting
Transitions.” Journal of the American Statistical Association 81 (394): 452–460.
Burden, Barry C., and David C. Kimball. 1998. “A New Approach to the Study of Ticket
Splitting.” American Political Science Review 92 (3): 533–544.
. 2009. Why Americans Split Their Tickets: Campaigns, Competition, and Divided Government.
University of Michigan Press.
Calvo, Ernesto, and Marcelo Escolar. 2003. “The Local Voter: A Geographically Weighted
Approach to Ecological Inference.” American Journal of Political Science 47 (1): 189–204.
Chambers, Raymond L., and David G. Steel. 2001. “Simple Methods for Ecological Inference
in 2 x 2 Tables.” Journal of the Royal Statistical Society: Series A (Statistics in Society) 164 (1):
175–192.
Cho, Wendy K. Tam, and Brian J. Gaines. 2004. “The Limits of Ecological Inference: The Case
of Split-Ticket Voting.” American Journal of Political Science 48 (1): 152–171.
Cleave, N., Philip J. Brown, and Clive D. Payne. 1995. “Evaluation of Methods for Ecological
Inference.” Journal of the Royal Statistical Society Series A: Statistics in Society 158 (1): 55–72.
Cross, Philip J., and Charles F. Manski. 2002. “Regressions, Short and Long.” Econometrica 70
(1): 357–368.
de Benedictis-Kessner, Justin. 2015. “Evidence in Voting Rights Act Litigation: Producing
Accurate Estimates of Racial Voting Patterns.” Election Law Journal 14 (4): 361–381.
Duncan, Otis Dudley, and Beverly Davis. 1953. “An Alternative to Ecological Correlation.”
American Sociological Review 18 (6).
Elzayn, Hadi, Jacob Goldin, Cameron Guage, Daniel E. Ho, and Claire Morton. 2025. “Monotone
Ecological Inference.” National Bureau of Economic Research (34285).
38


---

Confounders and Linearity in Ecological Inference
Fan, Yanqin, Robert Sherman, and Matthew Shum. 2016. “Estimation and Inference in an
Ecological Inference Model.” Journal of Econometric Methods 5 (1): 17–48.
Fishman, Nic, and Evan Rosenman. 2024. “Estimating Vote Choice in US Elections with
Approximate Poisson-Binomial Logistic Regression.” In OPT 2024: Optimization for
Machine Learning.
Flaxman, Seth R., Yu-Xiang Wang, and Alexander J. Smola. 2015. “Who Supported Obama in
2012? Ecological Inference Through Distribution Regression.” In Proceedings of the 21st
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 289–298.
Freedman, David A., Stephen P. Klein, Jerome Sacks, Charles A. Smyth, and Charles G. Everett.
1991. “Ecological Regression and Voting Rights.” Evaluation Review 15 (6): 673–711.
Gelman, Andrew, David K. Park, Stephen Ansolabehere, Phillip N. Price, and Lorraine C.
Minnite. 2001. “Models, Assumptions, and Model Checking in Ecological Regressions.”
Journal of the Royal Statistical Society Series A: Statistics in Society 164 (1): 101–118.
Glynn, Adam N., Jon Wakefield, Mark S. Handcock, and Thomas S. Richardson. 2008.
“Alleviating Linear Ecological Bias and Optimal Design with Subsample Data.” Journal of
the Royal Statistical Society Series A: Statistics in Society 171 (1): 179–202.
Goodman, Leo A. 1953. “Ecological Regressions and Behavior of Individuals.” American
Sociological Review 18 (6).
. 1959. “Some Alternatives to Ecological Correlation.” American Journal of Sociology 64
(6): 610–625.
Greiner, D. James, and Kevin M. Quinn. 2009. “R x C Ecological Inference: Bounds, Correlations,
Flexibility, and Transparency of Assumptions.” Journal of the Royal Statistical Society Series
A: Statistics in Society 172 (1): 67–81.
. 2010. “Exit Polling and Racial Bloc Voting: Combining Individual-Level and R x C
Ecological Data.” The Annals of Applied Statistics, 1774–1796.
Grofman, Bernard, and Samuel Merrill. 2004. “Ecological Regression and Ecological Infer-
ence.” Edited by Gary King, Martin A. Tanner, and Ori Rosen. Ecological Inference: New
Methodological Strategies, Ch. 5.
Hanushek, Eric A., John E. Jackson, and John F. Kain. 1974. “Model Specification, Use of
Aggregate Data, and the Ecological Correlation Fallacy.” Political Methodology, 89–107.
Herron, Michael C., and Kenneth W. Shotts. 2003. “Using Ecological Inference Point Estimates
as Dependent Variables in Second-Stage Linear Regressions.” Political Analysis 11 (1):
44–64.
Imai, Kosuke, Ying Lu, and Aaron Strauss. 2008. “Bayesian and Likelihood Inference for 2x2
Ecological Tables: An Incomplete-Data Approach.” Political Analysis 16 (1): 41–69.
Jiang, Wenxin, Gary King, Allen Schmaltz, and Martin A. Tanner. 2020. “Ecological Regression
with Partial Identification.” Political Analysis 28 (1): 65–86.
King, Gary. 1997. A Solution to the Ecological Inference Problem: Reconstructing Individual Behavior
from Aggregate Data. Princeton University Press.
39


---

Confounders and Linearity in Ecological Inference
King, Gary, Ori Rosen, and Martin A. Tanner. 1999. “Binomial-Beta Hierarchical Models for
Ecological Inference.” Sociological Methods & Research 28 (1): 61–90.
Klima, André, Paul W. Thurner, Christoph Molnar, Thomas Schlesinger, and Helmut Küchen-
hoff. 2016. “Estimation of voter transitions based on ecological inference: An empirical
assessment of different approaches.” ASTA Advances in Statistical Analysis 100 (2): 133–159.
Kuriwaki, Shiro, Stephen Ansolabehere, Angelo Dagonel, and Soichiro Yamauchi. 2024.
“The Geography of Racially Polarized Voting: Calibrating Surveys at the District Level.”
American Political Science Review 118 (2): 922–939.
Lewis, Jeffrey B. 2001. “Understanding King’s Ecological Inference Model: A Method-of-
Moments Approach.” Historical Methods: A Journal of Quantitative and Interdisciplinary
History 34 (4): 170–188.
. 2004. “Extending King’s Ecological Inference Model to Multiple Elections Using
Markov Chain Monte Carlo.” Edited by Gary King, Martin A. Tanner, and Ori Rosen.
Ecological Inference: New Methodological Strategies, Ch. 4.
Manski, Charles F. 2018. “Credible Ecological Inference for Medical Decisions with Personalized
Risk Assessment.” Quantitative Economics 9 (2): 541–569.
Park, Won-ho. 2008. “Ecological Inference and Aggregate Analysis of Elections.” PhD diss.
Park, Won-ho, Michael J. Hanmer, and Daniel R. Biggers. 2014. “Ecological inference under
unfavorable conditions: Straight and split-ticket voting in diverse settings and small
samples.” Electoral Studies 36:192–203.
Pavía, Jose M., and Rafael Romero. 2024. “Improving estimates accuracy of voter transitions.
Two new algorithms for ecological inference based on linear programming.” Sociological
Methods & Research 53 (3): 1491–1533.
Pavía, Jose M., and Søren Risbjerg Thomsen. 2025. “ecolRxC: Ecological Inference Estimation
of R x C Tables Using Latent Structure Approaches.” Political Science Research and Methods
13 (4): 943–961.
Puig, Xavier, and Josep Ginebra. 2015. “Ecological Inference and Spatial Variation of Individual
Behavior: National Divide and Elections in Catalonia.” Geographical Analysis 47 (3): 262–
283.
Quinn, Kevin. 2004. “Ecological Inference in the Presence of Temporal Dependence.” Edited
by Gary King, Martin A. Tanner, and Ori Rosen. Ecological Inference: New Methodological
Strategies, Ch. 9.
Robinson, W. S. 1950. “Ecological Correlations and the Behavior of Individuals.” American
Sociological Review 15 (3): 351–357.
Rosen, Ori, Wenxin Jiang, Gary King, and Martin A. Tanner. 2001. “Bayesian and Frequentist
Inference for Ecological Inference: The R x C Case.” Statistica Neerlandica 55 (2): 134–156.
Rosenman, Evan, and Nitin Viswanathan. 2018. “Using Poisson Binomial GLMs to Reveal
Voter Preferences.” arXiv preprint arXiv:1802.01053.
Thomsen, Søren Risbjerg. 1987. “Danish Elections 1920-79: A Logit Approach to Ecological
Analysis and Inference.” Politica.
40


---

Confounders and Linearity in Ecological Inference
Wakefield, Jon. 2004. “Ecological Inference for 2 x 2 Tables (with Discussion).” Journal of the
Royal Statistical Society Series A: Statistics in Society 167 (3): 385–445.
41

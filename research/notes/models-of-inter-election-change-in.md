---
title: Models of inter-election change in
id: models-of-inter-election-change-in
tags:
- projections-electorales-bureaux-2027-b0b1c4
- swing-methods
- academic
- axiomatic-model
- uncontested-districts
created: '2026-07-21T18:29:37.656784Z'
updated: '2026-07-21T18:39:17.653687Z'
source: https://markcwilson.site/Research/Outputs/GrWi2020.pdf
source_domain: markcwilson.site
fetched_at: '2026-07-21T18:29:37.656507Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Wilson & Grofman (Journal of Theoretical Politics, 2022; OA preprint of
  the published version, journals.sagepub.com/doi/10.1177/09516298221123263) give
  the key theoretical treatment of the uniform-vs-proportional swing debate. They
  define district-level swing s_i = f(x_i, s, x-bar) as a function of a district''s
  prior vote share x_i, the aggregate swing s, and the overall mean x-bar, and propose
  three minimal axioms any swing model should satisfy: (A1) mean swing condition (district-level
  swings must average to the aggregate swing), (A2) respecting bounds (predicted shares
  must stay in [0,1]), (A3) neutrality/symmetry (the model must give consistent results
  regardless of which party is used as reference). They PROVE Uniform Swing satisfies
  A1 and A3 but violates A2 (bounds) whenever a district''s prior share plus swing
  would exceed 100% or go below 0%; Proportional Swing satisfies A1 but violates both
  A2 and A3. They further prove (Proposition 2.7) that NO swing model that is linear
  in s can satisfy both A1 and A2 simultaneously -- a formal impossibility result
  covering the entire family of models that includes uniform and proportional swing.
  They construct a new piecewise-linear model satisfying all three axioms: f(x_i,s,x-bar)
  = s(1-x_i)/(1-x-bar) if s>=0, else s*x_i/x-bar, and show how to add a mean-reversion
  term h(x_i,x-bar)=c(x-bar - x_i) without breaking the axioms. Empirically, on tens
  of thousands of paired U.S. congressional elections 1968-2016 (Katz et al. 2020
  dataset), the three models perform very similarly on winner-prediction (~85-95%)
  and correlation (>80%), but ALL models are bad at predicting the SIGN of district-level
  swing (often near or below 50%, i.e. worse than a coin flip) and all perform poorly
  on close races (winner accuracy ~57-58%, correlation drops to ~21-22%). The piecewise
  model uniquely achieves 100% bounds-compliance while matching or beating uniform/proportional
  on mean-square error and correlation in most subsets. Crucially, they show the treatment
  convention for UNCONTESTED districts (coding them as 100% vs. the common ad hoc
  ''75%'' convention) has a LARGE effect on all models'' measured accuracy -- a methodological
  warning directly relevant to French legislative-election swing measures, which have
  structurally incomplete candidate offers (uncontested-analogue situations from withdrawals/désistements).'
raw_file: raw/models-of-inter-election-change-in.pdf
---

Models of inter-election change in
partisan vote share
Journal Title
XX(X):1–10
c
⃝The Author(s) 2021
Reprints and permission:
sagepub.co.uk/journalsPermissions.nav
DOI: 10.1177/ToBeAssigned
www.sagepub.com/
SAGE
Mark C. Wilson1 and Bernard N. Grofman 2
Abstract
For a two-party electoral competition in a districted legislature, the change in mean vote share for party A from one
election to the next is commonly referred to as swing, though this term also has other meanings in the election literature.
A key question, highly relevant to election forecasting and the measurement of partisan gerrymandering, is: “How do
we expect the swing to be distributed across the districts as a function of previous vote share (and perhaps, other
factors)?”.
The literature gives two main answers to that question: uniform swing and proportional swing. Which is better has been
unresolved for decades. Here we (a) provide an axiomatic foundation for desirable properties of a model of swing; (b)
use those axioms to demonstrate why using uniform swing or proportional swing is a bad idea, (c) provide a reasonably
simple swing model that does satisfy the axioms, and (d) show how to integrate a reversion to the mean effect into
models of inter-election swing.
We show that all the above models can be expected to work well when (a) elections are close, or (b) when we
restrict ourselves to data where swing is low, or (c) when we eliminate the cases where the model is most likely to
go wrong. In particular, sometimes the model tested in the literature is not the standard model, in that either (c1) a
piecewise or truncated variant of the model is being used, or (c2) there is an arbitrarily chosen correction (usually
75%) for districts that are uncontested. As we show empirically with data from U.S. congressional elections, the choice
of such correction makes a substantial difference to results. We also show that in addition to its superior axiomatic
properties, our new model provides an overall equal or better ﬁt on ﬁve indicators: mistakes about directionality of
change, mistakes in winner, estimates that are outside the [0..1] bounds, mean-square error, and correlation between
actual and predicted values. We recommend replacing the uniform and proportional swing models with the new model
in almost all applications.
Keywords
uniform swing, proportional swing, vote share prediction
1
Introduction
There are many situations where we have data at two (or
possibly more than two) points in time, and we are interested
in comparing values between and among the data points for
each subject or case. One such situation is an experiment in
which there is a treatment effect which results in an overall
mean change of s units in some variable of interest after the
intervention. The situation in which we are chieﬂy interested
here is a two-party plurality vote contest (parties A and B)
in the set of electoral units (districts, states, etc), for which
we have data at two distinct points in time. For simplicity, we
assume an idealized situation in which there are K districts
each of equal size, and turnout is equal in each district.
Consider two elections, one at time t = 1 and one at time
t = 2. Let xi denote the vote share of a given party at time
1 in district i, and x′
i the vote share at time 2 in that district.
We use bars to denote mean values over districts, so that x
denotes the mean over all districts of xi, namely the overall
vote fraction for that party.
The aggregrate inter-election swing 1 is simply x′ −x,
and we denote this by s. By symmetry, in a two party contest,
swing for party A is swing against party B, and conversely.
At the district level we denote by si the district-level inter-
election district swing x′
i −xi.
A key problem in election forecasting and the study of
partisan gerrymandering, among other areas, is simply: given
s and the previous election result, estimate si for each i.
The literature gives two main answers to the above question:
uniform swing and proportional swing.
Butler, in a chapter in McCallum and Readman (1999,
pp. 263–265) is credited with ﬁrst using uniform swing to
model British elections. While its limitations for multi-party
contexts were noted by Butler and by later authors such
as Curtice and Steed (1982); Rose (1991); Dorling et al.
(1993), the concept has nonetheless subsequently become a
workhorse model in the U.K. Multiparty competition in the
U.K. is often dealt with by focusing on competition between
1University of Massachusetts Amherst
2University of California Irvine
Corresponding author:
Mark C. Wilson
Department of Mathematics & Statistics
University of Massachusetts Amherst
Amherst, MA 01002 USA
Email: markwilson@umass.edu
Prepared using sagej.cls [Version: 2017/01/17 v1.20]


---

2
Journal Title XX(X)
the two largest parties. The use of the uniform swing model
was promoted by Butler and Van Beek (1990) and is now
common in the U.S., with a similar way of treating multi-
party competition. Following Gelman and King (1994),
swing is sometimes taken to be uniformly distributed with a
stochastic error term with mean zero and some ﬁxed variance
(often estimated from data on the standard deviation of past
inter-election vote share shifts in the polity). Some stochastic
versions of swing include covariates, such as incumbency,
in the model (see e.g. Katz et al. (2020)). When we study
congressional elections in the U.S. we also restrict ourselves
to two-party competition.
Proportional swing, on the other hand, posits that each
unit experiences the same percentage change from one
election to the next, and thus units that have higher starting
values experience greater absolute vote changes. We believe
that this model was ﬁrst proposed by Berrington (1965),
where it was offered as an alternative to uniform swing.
In subsequent literature, proportional swing has become the
main alternative to uniform swing.
Even in the context of two-party politics the use of
these models has always been problematic, since each had
properties that made a good ﬁt to empirical data implausible.
And yet, when applied to British elections, by Butler and
then by other authors in every post-WWII British National
Election Study, or in U.S. congressional and other elections,
the ﬁt of these models, especially uniform swing, has been
shown to be amazingly good – see e.g. Butler and Stokes
(1969, pp. 140-151) and Katz et al. (2020). The remarkable
empirical ﬁt of uniform swing led Butler and Stokes (1969)
to talk about the “paradox of swing”. They suggested that,
on theoretical grounds, proportional swing should work
better. Work of Johnston (1981, 1983) showed that uniform
swing did not perform perfectly in all situations and any
explanation for its effectiveness must be rather complex.
However proportional swing did not win out. As Gershuny
(1974, p. 116) puts it, after arguing for fundamental ﬂaws
with the proportional swing model: “The mass of the
evidence is however that swings are virtually equal across
constituencies.” And this is a ﬁnding that has been conﬁrmed
by subsequent decades of observations.
We ﬁnd neither swing model to be satisfactory. While
many authors have criticized the uniform swing and
proportional swing models, to our knowledge no author has
systematically sought to enumerate the desirable properties
of a model of inter-election swing. In Section 2, we consider
a general deterministic model of inter-election swing, of the
form
si = f(xi, s, xi)
where xi is the vote share of party A in the ith district at time
1. We provide an axiomatic characterization of the properties
we wish the function f to satisfy.
Having identiﬁed three key axioms, we next turn to
evaluating uniform swing and proportional swing with
respect to the axioms, discovering as we should have
expected, that neither of these models is fully satisfactory.
In Section 2.2, we show that uniform swing violates one of
the three conditions, and proportional swing violates two of
them.
We next look to see whether there are any functions that
do satisfy all the axioms. After proving an impossibility
result applicable to a large family of models including both
uniform and proportional swing, we ﬁnd a positive solution
in Section 2.2.3, via a piecewise deﬁned function that we feel
has strong substantive arguments for adoption, and which has
the simplest functional form we can ﬁnd.
We also show how to incorporate a reversion (sometimes
called “regression”) to the mean effect while still satisfying
our ﬁrst three axioms. In its simplest form reversion
to the mean posits that outcomes are a product of
fundamental factors and idiosyncratic factors some of which
will be constituency-speciﬁc. Idiosyncratic features can be
represented as stochastic errors occurring with mean zero.
Since errors are posited to be uncorrelated across elections,
the implication of a reversion to the mean effect is that
on average, outcomes will reﬂect fundamentals. But then
especially large victories (defeats) are likely to involve
idiosyncratic features which cannot be expected to persist
into the next election. In the concluding discussion we will
consider factors other than a reversion to the mean effect
that might be added to more realistically model inter-election
swing.
In Section 3 we consider how our axiomatic results
relate to empirical analyses, beginning with “toy” results
to illuminate the properties of the various models and
culminating in analyses of two-party vote share in tends of
thousands of pairs of adjacent U.S. congressional elections
from 1968-2016. In Section 3.1 we demonstrate with
hypothetical data that, for close districts and small swings, all
models will give very similar predictions. In Section 3.2 we
demonstrate with actual data that we can improve an already
very good ﬁt of these two standard models even further
by changing the structure of the data, either by entirely
eliminating certain extreme cases (uncompetitive districts) or
by recoding uncompetitive districts from 100% to 75%.
Our modiﬁed model provides an overall equal or better ﬁt
to U.S. congressional data than the traditional models, while
having much nicer axiomatic properties.
Our results aid us in making sense of the perceived
good ﬁt of models such as uniform swing, especially once
we recognize that some applications of these models are
not actually uses of the standard model. For example,
when Katz, King and Rosenblatt (2020) assess the ﬁt of
uniform swing and proportional swing they are assigning
non-competitive districts to be 75%-25% districts. In other
studies of U.S. elections, such as ones to calculate seats-
votes relationships, it is very common to see uncompetitive
districts coded as 75% districts (or the replacement of
results in an uncontested election for the constituency with
data from a more competitive constituency wide election
projected into that district) in order to avoid what would
otherwise be seen to be misleading out of bounds results.
Practices such as this recoding are taken for granted as minor.
For example, Katz et al. (2020, endnote 6, p171) view this as
“standard practice.” They also observe that the effects of this
imputation “have no material impact on our results.” While
generally correct, this is too strong a claim, as we discuss
below. We are preparing a companion article with a more
empirical focus, which in particular will study how choices
in how one measures goodness of ﬁt can play a large role in
whether a given swing model gives convincing results.
Prepared using sagej.cls


---

Wilson and Grofman
3
2
Axiomatic properties for functions
modelling inter-election swing
Recall our basic idealized situation. There are K districts of
equal size and two parties, A and B, contesting all districts.
Unless otherwise speciﬁed we state results for party A,
whose vote share is denoted xi.
We use the following toy example throughout, in order to
concretely illustrate ideas.
Example 2.1. (Toy example) There are two parties and two
districts of equal size. Fix a parameter α with 0 ≤α ≤1/2.
In District 1, party A has fraction 1 −α of the votes, and
party B receives α, while these vote shares are reversed in
District 2. The overall vote share of each party is (α + (1 −
α))/2 = 0.5, because the districts have the same size.
Deﬁnition 2.2. The district-level swing in district i is given
by
si := x′
i −xi.
The aggregate swing is given by
s := x′ −x.
Note that since x′ = x + s, we must have 0 ≤x + s ≤1
and so −x ≤s ≤1 −x.
Deﬁnition 2.3. By a naive swing model we mean a
prediction of x′ of the form
x′
i = xi + f(xi, s)
where f ≡fA is a ﬁxed function (depending only on A but
not i or s).
Alternatively, si = f(xi, s) for all i. Note that the district-
level swing depends on the previous vote fraction in that
district, but not on the votes in other districts except via the
overall swing.
There are some obvious requirements for such a predictive
model. The deﬁnition of district-level and aggregate swing
yields
1
K
K
X
i=1
f(xi, s) = s
(mean swing condition).
(a1)
The next condition holds because x′
i is bounded within the
interval [0, 1]:
0 ≤xi + f(xi, s) ≤1
(respecting bounds).
(a2)
We also require a third condition, which we may think of
as a symmetry condition similar to neutrality in social choice
theory, namely that a universal swing model for two-party
competition must give the same answer whether we look at
either party. This translates to
f(xi, s) + f(1 −xi, −s) = 0
(neutrality).
(a3)
If we think of the vote shares of the parties as arranged in
a matrix with one row per party and one column per district,
(a1) can be interpreted as a row sum condition, and (a3) as a
column sum condition.
2.1
Existing models of inter-election swing
As mentioned above, the Uniform Swing model is given by
f(xi, s) = s
for all i.
Thus x′
i = xi + s for all i. In other words, the same net
fraction of voters changes to party i in each district. For
example, in the toy example with α = 0.2, a 6% swing to
A changes its vote in District 1 to 86% and in District 2 to
26%.
Although it is easily seen that Uniform Swing satisﬁes (a1)
and (a3), it does not satisfy (a2). For example, in the toy
model, the upper bound for party A in District 1 is violated
when α > 1/2 and s > 1 −α. Note that the lower bound for
B in District 1 would also be violated.
There is a good reason why we have not presented a naive
swing model satisfying all axioms (a1) – (a3): namely that
no such model exists.
Proposition 2.4. No naive swing model can satisfy both (a1)
and (a2).
Proof. Consider the situation where all district vote shares
are equal, so that xi = x for all i. Then (a1) implies that
f(x, s) = s for all s. Since x can take any value in the
interval [0, 1], this shows that f(xi, s) = s for all s, in
general. In other words, the row sum condition is enough to
yield the uniform swing model, and since the uniform swing
model fails (a2), the claimed impossibility follows.
Thus in order to obtain a broader class of well-behaved
simple models, we need a more general functional form for
f.
Deﬁnition 2.5. A swing model is a prediction of the form
x′
i = xi + f(xi, s, x)
for some function f.
The properties (a1) – (a3) above correspond to analogous
properties, with the same motivations:
1
K
K
X
i=1
f(xi, s, x) = s
(A1)
0 ≤xi + f(xi, s, x) ≤1
(A2)
f(xi, s, x) + f(1 −xi, −s, 1 −x) = 0
(A3)
In our view these three conditions are minimal require-
ments, essential for any logically consistent theory of swing.
The ﬁrst follows directly from the very deﬁnition of district-
level and overall swings. The second guarantees that a
prediction has the correct form and is not logically ruled
out from being correct. The third seems clear because any
universal theory should surely not depend on the speciﬁc
parties involved, or which of them we focus on at the
moment.
The only other prominent swing model in the literature is
Proportional Swing, deﬁned via the formula
f(xi, s, x) = sxi/x.
Prepared using sagej.cls


---

4
Journal Title XX(X)
Note that the deﬁnition implies that
x′
i
x′ = xi
x
so that the relative share among districts of the party’s overall
vote does not change between elections. For example, in the
toy model with α = 0.8, a 6% swing to A is a 12% relative
increase in its overall vote share. The Proportional Swing
prediction in District 1 is 89.6% and in District 2 it is 22.4%.
Of course if we think of this as a −6% swing to B, then
this is a relative decrease of 12% in the overall vote share of
B, and hence the vote fraction of B in the ﬁrst district under
this model should be 17.6% and in the second district 70.4%.
This causes a violation of the bounds condition (A2) and
also shows that (A3) fails. This deﬁciency of Proportional
Swing has been noticed early, for example McLean (1973);
Gershuny (1974).
It is easily veriﬁed that Proportional Swing does satisfy
(A1).
2.2
New models
Beginning with uniform swing and proportional swing
models, a natural question is whether there are small changes
that can be made to one or both of those models that would
satisfy axioms (A1)–(A3). We now explore this, and some
false starts we eventually ﬁnd one, in Section 2.2.3.
Do there exist any models that satisfy all axioms (A1)–
(A3)? The answer is yes, since there are so many degrees
of freedom. Consider the special case with 2 districts. Then
we seek a mapping from a 2 × 2 contingency table with
column sums equal to 1 and ﬁxed row sums r1, r2 to another
such table with r1, r2 replaced by r′
1, r′
2, subject to r1 +
r2 + s = r′
1 + r′
2. We have already accounted for (A1) and
(A3). To satisfy (A2) we require that given a vote share a
for party A in district 1, we can choose vote share a′ for
the same party in the same district such that 0 ≤a′ ≤1 and
0 ≤a + b + 2s −a′ ≤1. This is always possible because of
the constraints on s. Thus it is indeed possible to satisfy all
three axioms. The question is whether we can do so with a
reasonably simple and understandable functional form.
We now look for a model that satisﬁes at least axioms
(A1)–(A3), by considering some models deﬁned by simple
formulae.
2.2.1
Truncations One variant of the uniform swing model
would be simply to impose truncation, i.e., to set xi +
f(xi, s) = 1 if xi + s ≥1 and xi + f(xi, s) = 0 if xi +
s ≤0. Note that this procedure of simply truncating out
of bounds values to be either 0 or 1 was used by
expert witnesses estimating racially polarized voting in
voting rights cases using Goodman’s (Goodman 1953,
1959) method of ecological regression. However, that
methodology has largely been replaced with ecological
inference techniques (King, 1997) that assure that estimates
are within bounds. In any case, in our situation the truncation
procedure leads to failure of axiom (A1).
2.2.2
Models that are linear in s We start with the family
of linear models given by formulae of the type
si = sg(xi, x).
Of course, we mean linear in the variable s — the functional
dependence on x is not speciﬁed. If g(xi, x) = 1, this gives
Uniform Swing. The Proportional Swing model is also in this
family, with g(xi) = xi/x.
Example 2.6. McLean (1973) considers models using
transition matrices, in which we account for the fraction of
voters of party i that vote for party j in the next election
(this includes abstainers as a party). Consider the simple case
of no abstainers and two parties. If a is the fraction who
switch from party 1 to party 2, then in order to satisfy row
and column sums, the matrix must have the form
 a
1−a
1−a
a

.
This leads after some algebra to
x′
i = xi + s(1 −a)(1 −2xi).
In other words, this is a model in the same family with
g(x) = (1 −a)(1 −2x) (swings go against the national one
in districts dominated by party 1, but toward it in districts in
which it is weak). Such a model violates the bounds when
xi = 1 or xi = 0 if the swing is against party i. Furthermore
its behaviour is counterintuitive in that the swing is zero
precisely for elections that are the most competitive.
Such a model satisﬁes (A1) if and only if C is the
reciprocal of the average of g(xi) over all districts: C =
1/g(x). A sufﬁcient condition for symmetry is that g(x) =
g(1 −x), so that the function g is symmetric about x =
1/2. In order to satisfy the bounds condition (A2), we
need g(0) = g(1) = 0, so that swing is zero in completely
lopsided districts. For example, we could use a quadratic
function g(x) = x(1 −x).
So far we are proceeding well, but our search is in fact
pointless, a result that surprised the authors.
Proposition 2.7. No swing model linear in s can satisfy both
(A1) and (A2).
Proof. We recall the toy model where 1/2 > α > 0.
Consider the effect in its strong district of a swing of 1/2
to A. By (A2), we must have
1 −α + 1
2g(1 −α, 1/2) ≤1
so that
g(1 −α, 1/2) ≤2α.
By a similar argument, this time using the lower bound and
considering the effect in the other district of a swing of −2α,
we obtain
g(α, 1/2) ≤2α.
However condition (A1) then implies that 2 = g(1 −
α, 1/2) + g(α, 1/2) ≤4α < 2, a contradiction.
2.2.3
Piecewise linear model In view of the negative
results above, we differentiate between positive and negative
swings. Our experience with the models seen so far leads
after some educated guessing to the following:
f(xi, s, x) =
(
s 1−xi
1−x
if s ≥0;
s xi
x
if s < 0.
Straightforward algebra shows that this model satisﬁes
(A1), (A2) and (A3). This is the simplest functional form
we can ﬁnd for which which (A1)–(A3) are satisﬁed.
Prepared using sagej.cls


---

Wilson and Grofman
5
Note that under this model (as with the previous two),
the sign of the district-level swing is the same as the sign
of the overall swing. Under positive swings, in districts in
which a party is relatively strong (its vote share is more than
its overall average) the district-level swing is smaller than
in districts in which the party is relatively weak. However
for negative swings, an overall swing against the party is
ampliﬁed in its stronger districts and diminished in its weaker
districts.
A substantive argument for this model is as follows. If in
each district there are swing voters as well as partisans of
each party, along lines similar to the argument in McLean
(1973), we may readily imagine that, in districts where A
already scores highly, there are relatively few swing voters
left to convince, so that an overall swing toward A does not
improve that party’s vote share substantially in such districts.
However in districts where A scored relatively low, there is
more chance of winning over swing voters. However if the
swing is away from A, the reverse is true (alternatively, the
same is true of B).
Table 1. Axioms satisﬁed by swing model
Model/Axiom
A1
A2
A3
uniform



proportional



truncated uniform



linear in s


()
piecewise



We note in passing (a fact discovered after the present
article was written) that what Katz et al. (2020) call
proportional swing in their article is revealed by inspection
of their R code to be exactly the piecewise model 2.
2.2.4
Models
incorporating
a
mean-reverting
term
Another condition that is satisﬁed by all the models we have
discussed so far is:
f(xi, 0, x) = 0.
(A4)
This condition says that when there is no aggregate swing,
our best predictor of outcomes in individual districts is that
they will be unchanged from the previous period. We do
not regard this as a desirable property to impose generally
on inter-election swing. The reason is quite simple: (A4)
is inconsistent with observation, in that extremely high or
low vote shares often change between elections even with no
aggregate swing.
Suppose that we add a term h(xi, x) to any of the above
formulae already satisfying all three axioms. Then (A4) no
longer holds, (A1) holds if and only if h has mean zero, while
(A3) holds if and only if h(xi, x) + h(1 −xi, 1 −x) = 0.
The bounds condition would be satisﬁed provided h(xi, x) ≥
0 when x ≤x and h(xi, x) ≤0 when when x ≥x.
The simplest functional form satisfying the
above
conditions on h is h(xi, x) = c (x −xi), for some constant
c > 0. Note that this model implies that the magnitude of
inter-election shift is affected (in a linear way) by how far
away the previous outcome was from the average outcome.
Also note that the model has one free parameter, unlike the
previously considered models.
We note in passing that adding a mean-reverting term to a
model that does satisfy the other axioms, but not the bound
condition (A2), can also work. For example, deﬁne a model
to be afﬁne in s if it has the form
f(xi, s, x) = sg(xi, x) + h(xi, x)
for some function h, so we have added a term independent
of s to a model that is linear in s. Thus every linear model
is an afﬁne model with h = 0. We would like to prove
an impossibility result similar to Proposition 2.7 for afﬁne
models, but such a result is false.
Example 2.8. The afﬁne model with g(xi, x) = 1 and
h(xi, x) = x −xi satisﬁes (A1), (A2) and (A3). Note that
x′
i = x′, so that this model is rather trivial, in that it predicts
the same vote share in each district, independent of the
previous results.
We have not found an afﬁne model with dependence on i
that satisﬁes our three axioms, but neither have we proved it
to be impossible.
3
Behavior of models
In this section, we investigate the behaviour of our models
on some speciﬁc vote distributions.
3.1
Artiﬁcial data
Suppose that we have complete uniformity across districts:
in every district, xi = x. Then, as expected, all the models
discussed above make the same prediction, namely x′
i =
xi + s for each i.
In Table 2 we consider a very polarized version of the toy
model, with 0 ≤α ≤1/4. Note that there are measurable
differences between the predictions made. For example, an
initial vote share for party A of (95%, 5%) in District 1 and
District 2, combined with a swing to party A of 10%, yields
(105%, 15%) for the uniform model and (99%, 21%) for the
piecewise model.
In Table 3 we consider the toy model with two very
competitive districts, where α = 1/2 + ε and 0 ≤ε ≤1/4.
Note that the predictions of all models are the same to
ﬁrst order in ε, and so unlikely to be distinguishable for
fairly small ε. For example, an initial vote share for party
A of (55%, 45%) in District 1 and District 2, combined
with a swing to party A of 10%, yields (65%, 55%) for the
uniform model, (66%, 54%) for the proportional model, and
(64%, 56%) for the piecewise model.
So far we tentatively conclude that for close districts and
small swings, all models will give very similar predictions.
On lopsided districts, they will not agree in their vote share
prediction, but the predicted winner will be the same in most
cases unless the swing is very large.
3.2
Real data
We considered real data taken from the dataset Katz et al.
(2019) used in Katz et al. (2020), consisting of district-level
data on Democratic and Republican vote share for elections
in United States state legislatures over the period 1968-
2016, containing over 140000 data points. The basic unit
of analysis is an election in a ﬁxed district in a ﬁxed state,
at two successive elections between which redistricting has
not occurred. This gave just over 73000 units. Uncontested
Prepared using sagej.cls


---

6
Journal Title XX(X)
Table 2. Predictions for “polarized” example with 2 parties and 2 districts, swing of 2α to A
model / (party, district)
(A,1)
(A,2)
(B,1)
(B, 2)
original
1 −α
α
α
1 −α
uniform
1 + α
3α
−α
1 −3α
proportional
1 + 3α −4α2
α + 4α2
α −4α2
1 −5α + 4α2
piecewise
1 −α + 4α2
5α −4α2
α −4α2
1 −5α + 4α2
Table 3. Predictions for “competitive” example with 2 parties and 2 districts, swing of 2ε to A
model / (party, district)
(A,1)
(A,2)
(B,1)
(B, 2)
original
1/2 −ε
1/2 + ε
1/2 + ε
1/2 −ε
uniform
1/2 + ε
1/2 + 3ε
1/2 −ε
1/2 −3ε
proportional
1/2 + ε −4ε2
1/2 + 3ε + 4ε2
1/2 −ε + 4ε2
1/2 −3ε −4ε2
piecewise
1/2 + ε + 4ε2
1/2 + 3ε −4ε2
1/2 −ε −4ε2
1/2 −3ε + 4ε2
elections are a prominent feature of US elections, and we
need to deal with that issue. We made 3 versions of the
dataset: uncontested elections count as 0.75 vote share to
the winner and 0.25 to the other party; uncontested elections
count vote share 1.0 to the winner; all uncontested elections
are removed from the dataset. We adapted code from Katz
et al. (2019); all our code is available at Harvard Dataverse
Wilson (2021). 3
We compare performance of swing models as follows.
Given as input the entire vote counts for all parties and
districts for Election 1, and the popular vote counts from
Election 2 (from which we can compute the swing to/from
each party), we compute the prediction of each model for
Election 2 for each party in each district. We measure quality
of prediction in ﬁve ways: the fraction of units in which the
winner is correctly predicted; the fraction of times when the
district-level sign is correctly predicted the fraction of units
in which the vote share prediction stays in bounds; the the
mean squared error in vote share prediction; the Pearson
correlation between the real and predicted vote share data.
Note that all three models predict the sign of each district-
level swing to be the same as the sign of the aggregate
swing. Thus all should give the same result for sign in most
cases, but in the case where the original vote share is 100%
(dataset unc1.0) and there is positive aggregate swing, the
uniform and proportional will predict +1 for sign whereas
the piecewise will predict 0. If the following election is also
uncontested, the piecewise model outperforms the others.
Results of our tests are displayed in Table 4, displayed to 3
signiﬁcant ﬁgures. Bold entries indicate the best performance
among the models on the given measure corresponding to
the column for the given dataset. Note that the piecewise
measure always has perfect performance on the bounds
measure. We show the results for the ﬁrst and fourth quartile
in Tables 5 and 6. Table 7 describes the behavior on close
races (winner scores in the range [50%, 52.5%]).
First, the results show that the convention we choose for
treating uncontested elections has a large inﬂuence on the
ability of the methods to predict the winner or the sign of the
district-level swings, as well as the correlation.
Second, all models had difﬁculty in predicting the
sign of district-level swings, scoring around 50% or even
substantially lower, worse than ﬂipping a coin, in some
scenarios. They all performed much better on the other
measures. Of course, piecewise swing never violates the
bounds, so it scores perfectly on this measure. However the
other models also scored very highly on this measure except
when uncontested elections are given vote share 1 for the
winner, and even then they scored over 80%. The correlation
scores were all over 80%.
Third, as expected, for small swings the predictions of
all three models are almost indistinguishable, except when
uncontested elections are given vote share 1 for the winner,
when uniform swing performs relatively poorly on the sign
and bounds measures. For the uniform and piecewise models
the probability of predicting the winner was around 93%,
89%, and 85% under the three conventions, and in each case
the two probabilities differ by less than 0.2%. The similarity
was even greater in the correlation, while the mean-square
error had somewhat larger differences but still of the order of
1-2%,
Fourth, there was a consistent very small advantage to
uniform swing in predicting the winner, and to the piecewise
model in predicting sign, mean-square error and correlation.
Drilling deeper into the data, we considered the subsets
of the three datasets for which the aggregate swing is in the
ﬁrst quartile (“elections with small swing”), or in the fourth
quartile (“elections with large swing”). We also looked at
elections whose variance in district-level swing was in the
ﬁrst quartile as opposed to those in the fourth quartile.
The relative performance of methods was almost identical
those in the overall dataset, with a tiny advantage to uniform
swing in predicting the winner, but the piecewise model
leading on the other four indicators. All methods found it
noticeably easier to predict the winner, and harder to predict
the sign of the district-level swing, when dealing with small
swings, and the reverse was true for large swings.
Finally, we considered the performance of the models on
close races, which we deﬁned to be those pairs of contested
elections where the winner scored between 50% and 52.5%
in the second election. All measures performed relatively
poorly in this case at predicting the winner, scoring only
around 57% — as expected, close races are harder to call.
Although they did better on predicting the sign of the
district-level swing, the correlation dropped to just over 20%.
However, the piecewise model did at least as well as the
others on every measure.
Prepared using sagej.cls


---

Wilson and Grofman
7
Table 4. Results for swing models on dataset from Katz et al. (2020). Bold entries indicate the best performance among the
models on the given measure corresponding to the column for the given dataset.
dataset
model / measure
winner
sign
bounds
mean-square
ρ
unc0.75
uniform
0.932
0.497
1.000
0.00747
0.903
unc0.75
proportional
0.933
0.497
0.999
0.00756
0.902
unc0.75
piecewise
0.930
0.497
1.000
0.00728
0.903
unc1.0
uniform
0.904
0.498
0.832
0.0381
0.817
unc1.0
proportional
0.904
0.539
0.884
0.0389
0.813
unc1.0
piecewise
0.892
0.604
1.000
0.0360
0.818
cont only
uniform
0.855
0.678
1.000
0.00521
0.891
cont only
proportional
0.853
0.678
0.999
0.00533
0.889
cont only
piecewise
0.852
0.678
1.000
0.00509
0.891
Table 5. Results for swing models on dataset from Katz et al. (2020), ﬁrst quartile mean swing. Bold entries indicate the best
performance among the models on the given measure corresponding to the column for the given dataset.
dataset
model / measure
winner
sign
bounds
mean-square
ρ
unc0.75
uniform
0.951
0.385
1.000
0.00734
0.909
unc0.75
proportional
0.951
0.385
1.000
0.00735
0.909
unc0.75
piecewise
0.951
0.385
1.000
0.00730
0.909
unc1.0
uniform
0.951
0.411
0.835
0.0367
0.826
unc1.0
proportional
0.951
0.463
0.873
0.0368
0.826
unc1.0
piecewise
0.951
0.517
1.000
0.0362
0.826
cont only
uniform
0.886
0.528
1.000
0.00548
0.882
cont only
proportional
0.886
0.528
1.000
0.00549
0.882
cont only
piecewise
0.886
0.528
1.000
0.00544
0.883
Table 6. Results for swing models on dataset from Katz et al. (2020), fourth quartile mean swing. Bold entries indicate the best
performance among the models on the given measure corresponding to the column for the given dataset.
dataset
model / measure
winner
sign
bounds
mean-square
ρ
unc0.75
uniform
0.894
0.672
1.000
0.00734
0.895
unc0.75
proportional
0.890
0.672
0.998
0.00754
0.891
unc0.75
piecewise
0.884
0.672
1.000
0.00698
0.895
unc1.0
uniform
0.857
0.604
0.840
0.0414
0.802
unc1.0
proportional
0.854
0.642
0.894
0.0426
0.792
unc1.0
piecewise
0.838
0.705
1.000
0.0372
0.805
cont only
uniform
0.816
0.842
1.000
0.00509
0.887
cont only
proportional
0.811
0.842
0.996
0.00530
0.882
cont only
piecewise
0.806
0.842
1.000
0.00489
0.888
Table 7. Results for swing models on dataset from Katz et al. (2020), close races. Bold entries indicate the best performance
among the models on the given measure corresponding to the column for the given dataset.
dataset
model / measure
winner
sign
bounds
mean-square
ρ
cont only
uniform
0.576
0.734
1.000
0.00429
0.212
cont only
proportional
0.576
0.734
1.000
0.00432
0.211
cont only
piecewise
0.581
0.734
1.000
0.00368
0.218
4
Discussion and conclusion
Why axioms?
Our approach here is inﬂuenced by that of Taagepera (1999,
2007) where great attention is paid to the functional form
of relationships and how these are affected by boundary
conditions that rule out certain outcomes as logically
impossible. Taagepera (2008) argues that political science
research is overly wedded to statistical models and to
linear models, and that this unbalances and limits the
ﬁeld. Searching for predictive models that respect logical
constraints and are grounded in substantive theories of
political behavior is not only more likely to yield useful
models, but spurs investigation of fundamental principles.
Shugart and Taagepera (2017) lay out theoretical reasons
why we might expect observed mean values of some
key election parameters (e.g., effective number of political
parties) to be a function of the geometric mean of worst case
and best case scenarios. Of course, for any speciﬁc county in
any given election the actual results will not match the mean
a priori expectation, but it is still useful to derive axiomatic
expectations about the likely mean outcomes for a set of
countries, and to test to see how well those expectations
are fulﬁlled. Their derivation of interlocking models for
distribution of seats, votes, numbers of parties, etc, in the
context of simple electoral systems, is a good example of
the kind of result we seek by setting out on the path of
axiomatics.
Prepared using sagej.cls


---

8
Journal Title XX(X)
In the context of electoral swing, even if a purely statistical
or machine learning approach could discover a good ﬁt
to existing data, our conﬁdence in its performance on
necessarily out-of-sample, future data should not be high.
The total number of political elections in human history is
not large compared to the enormous corpuses typical in areas
considered to be machine learning success stories.
Our theoretical analysis showed that the piecewise model
has much better axiomatic properties than the better known
uniform and proportional models. Our toy models suggest
strongly that the piecewise model will give results very close
to the uniform and proportional swing models for “normal”
elections, but more accurate predictions for districts where
the previous result was not close and/or swings are large.
Empirical issues
On the dataset we analysed, uniform and piecewise models
appear to perform similarly, each scoring slightly better than
the proportional model on most criteria, and the differences
in the model predictions are very small in most cases.
Interestingly, the piecewise model is slightly worse than
the others at predicting the winner in many cases, but has
better ability to predict the sign of district-level swings,
generally lower mean square error on each dataset, and better
correlation than the other models. It also performs better on
close races, although all models perform fairly poorly in that
case. We reemphasize that the choice made in how to deal
with uncontested elections is very important.
The uniform swing model has been considered for decades
to give a “good enough” ﬁt to data, despite having weak
theoretical foundations. It is very hard in many cases to
distinguish predictions made using uniform swing from
those using the theoretically superior piecewise model. For
readers with a practical inclination, this should bolster their
belief that uniform swing works well in practice. However,
we advise caution for several reasons. First, none of the
models here works particularly well in predicting results of
close elections or when swings are large. If we are only
interested in the winner, swings are small and the previous
election is not close, it is easy to guess who will win this time.
Second, as mentioned above, the total number of political
elections held in the history of humankind is still rather
small, and so any conclusion based on real data should
be treated cautiously. It is easy for any model to ﬁt well
on particular datasets. For example, over a limited range
of values a linear approximation can ﬁt very well a non-
linear curve, but extrapolating that linear function will yield
very erroneous estimates. Third, swing models are used not
only for election forecasting but also for applications such
as the study of counterfactual elections, for example when
considering partisan gerrymandering or electoral system
design more generally, and these may take us outside the
realm of small swings. Fourth, our results here may have
wider application beyond the electoral context, for example
to experiments whose treatment condition may have variable
effects on subjects. In those situations the still-mysterious
conﬂuence of factors that cause uniform swing to work well
in many political contexts may not eventuate at all.
Future work
One way to relax our constraints is to consider probabilistic
models (all models in the current paper are deterministic
“mean-ﬁeld approximations”), as in Note 2 below. We expect
that for probabilistic models, axioms similar to (A1) – (A3)
will be needed, but for means of random variables rather than
deterministic values. In the rest of this section we restrict to
the deterministic case, which is the main focus of this paper.
We expect that improvements in deterministic models will
yield substantial insight into improving stochastic ones.
Clearly, we have not explored the entire space of swing
models satisfying our three axioms. There is still plenty of
room for exploration of further swing models, which balance
predictive accuracy with functional simplicity, substantive
explanations and good axiomatic properties. Although the
three models we focused on here have similar performance,
none of them is very good at predicting close elections, and
there is surely a reasonable chance of ﬁnding a model with
better performance. In order to do this, it may be necessary to
move beyond models satisfying (A4), for example by adding
a reversion to the mean effect as described above.
Further, while we have shown how to incorporate a
regression to the mean effect, there are other potentially
important factors we have not incorporated. In particular,
we assume that swing moves in the same way in each
of the districts as it does for the polity as a whole.
But that assumption is violated if, for example, there is
a simultaneous realigning trend that works differently in
different parts of the country, e.g. rural areas shifting
Republican while suburban areas shift Democrat in the USA.
While such realigning trends may largely be swamped by
election speciﬁc tides, in some elections realigning effects
will be dominant in at least some parts of the nation (or state).
Note that in addition to the conditions (A1) – (A4), all our
basic models (not containing any term involving reversion to
the mean) also satisfy:
sgn(si) = sgn(s)
for all i.
(A5)
In other words, the district-level swings all have the same
sign as the overall swing. The scenario described above
shows that this may not always be satisﬁed, and this is borne
out on real data. Electoral tides do not always move in the
same direction across all districts – a fact which is concealed
by the degree to which prediction errors cancel out. Relaxing
the constraint (A5) will therefore probably be necessary.
In the electoral context there are a number of additional
substantive factors that in future might usefully be examined,
including
• a simple realigning reversal tide effect in which areas
previously providing strong support to one party begin
to shift in the direction of the other party;
• a polarizing effect, such that areas previously strong
for one party generally become stronger still, with the
potential, as noted above, for realigning tides to be
moving in opposite directions in different parts of a
polity;
• an intimidation effect that makes the most successful
incumbents less likely to face strong challengers.
The ﬁrst of these could be represented via a reversion to
the mean effect, while the second two involve movements
Prepared using sagej.cls


---

Wilson and Grofman
9
in the other direction. Adding a linear correction, as we
discussed in Section 2.2.4, maintains axiomatic properties
(provided the slope is of the correct sign) and gives a better
ﬁt to data. The question of how to determine the slope of the
linear correction in a principled way, in order to capture the
interplay of the above three factors, we leave for a companion
paper now in preparation.
Conclusion
Given the axiomatic superiority of the piecewise model,
its grounding in a substantive theory of electoral change,
and the simplicity of the piecewise formula, we recommend
its adoption wherever uniform or proportional swing have
previously been used. At the very least, anyone using
uniform swing should understand its sensitivity to choices
made about how to treat data violations of the bounds
condition. We agree with Taagepera that it is simply is
a bad idea to ﬁt data with a model that is known to
generate out of bounds estimates, even if the ﬁt of the
more plausible model is only marginally better by various
statistical measures. Moreover, even if we shift from a
deterministic form of uniform swing to a probabilistic form
the problem of out of bounds results does not go away.
We make one last observation. This essay is intended to
be a theoretical contribution that lays out conditions that
any plausible theoretic model of inter-election change should
satisfy, in order to move move beyond simple curve-ﬁtting.
The empirical analyses we provide are intended to be
illustrative. We are preparing a companion paper that argues
that the alleged empirical good ﬁt of uniform swing (and
other models) depends very much on the measures of ﬁt
we use. In particular, the implied assumption (A5), that in
each constituency swing is always in the same direction as
it is polity wide, is not satisﬁed in practice, and we need to
understand the conditions under which fundamental failure
of the uniform swing model can be expected to occur in real
data.
Acknowledgements
We thank Jonathan Katz for helpful input.
Notes
1.
We do have to be careful with nomenclature, since “swing”
is also used in the electoral systems and party literatures to
refer to “responsiveness”, namely the percentage change in seat
share for each one percentage point change in vote share (see
e.g., Tufte, 1973). That usage of “swing” has been extensively
studied both theoretically and empirically. Here we will use the
term “swing” only to refer to the magnitude of inter-election
shifts in votes.
2.
Jonathan Katz (personal communication): “I was not able to
ﬁnd any actual formal deﬁnition of proportional swing in the
literature . . . I wrote the code this way because it works in
the sense of making the means correct for both positive and
negative swings, which is what is needed.”
3.
Note that in the literature there are other ways to impute vote
shares in uncontested elections, such as looking at presidential
or gubernatorial races. Not only would this take us outside the
scope of the current paper, it is clear that such a change in
methodology would not change the results enough to change
our basic conclusion about the relative performance of the three
models.
References
Berrington HB (1965) The general election of 1964. Journal of the
Royal Statistical Society. Series A (General) 128(1): 17–66.
Butler D and Stokes D (1969) Political Change in Britain: Forces
Shaping Electoral Choice. St Martin’s.
Butler D and Van Beek SD (1990) Why not swing? Measuring
electoral change. PS: Political Science and Politics 23(2): 178–
184. Publisher: JSTOR.
Curtice J and Steed M (1982) Electoral choice and the production
of government: the changing operation of the electoral system
in the United Kingdom since 1955. British Journal of Political
Science 12(3): 249–298.
Dorling DFL, Pattie CJ and Johnston RJ (1993) Measuring electoral
change in three-party systems: An alternative to swing. PS:
Political Science and Politics 26(4): 737–741.
Publisher:
JSTOR.
Gelman A and King G (1994) A uniﬁed method of evaluating
electoral systems and redistricting plans. American Journal of
Political Science : 514–554.
Gershuny J (1974) The non-paradox of swing. British Journal of
Political Science 4(1): 115–119.
Goodman LA (1953) Ecological regressions and behavior of
individuals. American Sociological Review 18: 663–664.
Goodman LA (1959) Some alternatives to ecological correlation.
American Journal of Sociology 64(6): 610–625.
Johnston RJ (1981) Changing Voter Preferences, Uniform Electoral
Swing, and the Geography of Voting in New Zealand, 1972-
1975.
New Zealand Geographer 37(1): 13–18.
Publisher:
Wiley Online Library.
Johnston RJ (1983) Spatial continuity and individual variability: A
review of recent work on the geography of electoral change.
Electoral Studies 2(1): 53–68. Publisher: Elsevier.
Katz JN, King G and Rosenblatt E (2019) Replication Data for:
Theoretical Foundations and Empirical Evaluations of Partisan
Fairness in District-Based Democracies. DOI:10.7910/DVN/
FTYHPJ.
URL https://doi.org/10.7910/DVN/
FTYHPJ.
Katz JN, King G and Rosenblatt E (2020) Theoretical foundations
and empirical evaluations of partisan fairness in district-based
democracies. American Political Science Review 114(1): 164–
178.
McCallum R and Readman A (1999) The British general election
of 1945. British general elections 1945-92. Macmillan.
McLean I (1973) The problem of proportionate swing. Political
Studies 21(1): 57–63.
Rose R (1991) The ups and downs of elections, or look before
you swing. PS: Political Science and Politics 24(1): 29–33.
Publisher: JSTOR.
Shugart MS and Taagepera R (2017) Votes from seats: Logical
models of electoral systems. Cambridge University Press.
Taagepera R (1999) Ignorance-based quantitative models and their
practical implications. Journal of Theoretical Politics 11(3):
421–431.
Taagepera R (2007) Predicting party sizes: The logic of simple
electoral systems. Oxford University Press.
Prepared using sagej.cls


---

10
Journal Title XX(X)
Taagepera R (2008) Making social sciences more scientiﬁc: The
need for predictive models. OUP Oxford.
Wilson MC (2021) Replication data for: Swing models.
DOI:
10.7910/DVN/PKA2L9.
URL https://doi.org/10.
7910/DVN/PKA2L9.
Prepared using sagej.cls

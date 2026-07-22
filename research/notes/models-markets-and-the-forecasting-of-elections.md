---
title: Models, Markets, and the Forecasting of Elections*
id: models-markets-and-the-forecasting-of-elections
tags:
- electoral-forecasting
- forecast-ensembling
- prediction-markets
created: '2026-07-21T18:27:32.713655Z'
updated: '2026-07-21T18:39:17.611466Z'
source: https://arxiv.org/pdf/2102.04936
source_domain: arxiv.org
fetched_at: '2026-07-21T18:27:32.713365Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Sethi, Seager, Cai, Benjamin & Morstatter (May 2021, arXiv:2102.04936) compare
  daily probabilistic forecasts for 2020 US presidential battleground states from
  two sources over 7 months: a statistical poll-and-fundamentals model (The Economist
  model, via G. Elliott Morris) and PredictIt prediction-market prices. Finding: the
  market was more accurate months before the election, the model became more accurate
  as election day approached; a simple unweighted average of the two beat either source
  overall in aggregate accuracy, even though neither source was uniformly dominated
  (no single average beats both components on every state-date pair) — the two error
  types are complementary, with the model ''confidently wrong'' in some states and
  the market ''excessively uncertain'' in others. Proposes a trading-bot method for
  generating hybrid forecasts (budget, tunable risk preference, beliefs inherited
  from the statistical model) and a novel ''profitability test'' as an evaluation
  criterion for forecast quality, orthogonal to standard accuracy scores. Relevant
  to the research query mainly as a documented case for ensembling structurally different
  forecast types (poll-based statistical models vs. market/crowd-based estimates)
  rather than as a source on constituency/bureau-level projection methods.'
raw_file: raw/models-markets-and-the-forecasting-of-elections.pdf
---

Models, Markets, and the Forecasting of Elections*
Rajiv Sethi†
Julie Seager‡
Emily Cai§
Daniel M. Benjamin¶
Fred Morstatter||
May 26, 2021
Abstract
We examine probabilistic forecasts for battleground states in the 2020 US presidential election,
using daily data from two sources over seven months: a statistical model based on election
polls and fundamentals, and prices from a prediction market. We ﬁnd systematic differences
in accuracy over time with the market performing better months before the election, and the
model performing better as the election approached. A simple average of the two forecasts
performs better than either one of them overall, even though no average can outperform both
component forecasts for any given state-date pair. This effect arises because the model and
the market make different kinds of errors in different states: the model was conﬁdently wrong
in some cases, while the market was excessively uncertain in others. We propose a method
for generating hybrid forecasts based on a trading bot endowed with a budget, tunable risk
preferences, and beliefs inherited from the model. We also propose and conduct a proﬁtability
test that can be used as a novel criterion for the evaluation of model forecasting performance.
*We thank G. Elliott Morris for providing us with daily forecast data from the Economist model, Parker Howell
at PredictIt for access to daily price data, and Pavel Atanasov, David Budescu, Jason Pipkin, David Rothschild, and
partcipants at the 2021 DIMACS Workshop on Forecasting for comments on an earlier version. Rajiv Sethi thanks the
Radcliffe Institute for Advanced Study at Harvard University for fellowship support.
†Department of Economics, Barnard College, Columbia University, and the Santa Fe Institute
‡Department of Economics, Barnard College, Columbia University
§Fu Foundation School of Engineering and Applied Science, Columbia University
¶Information Sciences Institute, University of Southern California
||Information Sciences Institute, University of Southern California
arXiv:2102.04936v4  [econ.GN]  25 May 2021


---

1
Introduction
The forecasting of elections is of broad and signiﬁcant interest. Predictions inﬂuence contributions
to campaigns, voter turnout, candidate strategies, investment decisions by ﬁrms, and a broad
range of other activities. But accurate prediction is notoriously challenging, and each approach to
forecasting has signiﬁcant limitations.
In this paper we compare two very different approaches to the forecasting of elections, demon-
strate the value of integrating them systematically, and propose a method for doing so. One is a
model-based approach that uses a clearly identiﬁed set of inputs including polls and fundamen-
tals to generate a probability distribution over outcomes (Heidemanns et al., 2020). Daily state-
level forecasts based on such a model were published by The Economist for several months leading
up to the 2020 presidential election in the United States. Over the same period, a market-based
approach to prediction was implemented via decentralized trading on a peer-to-peer exchange,
PredictIt, which operates legally in the United States under a no action letter from the Commod-
ity Futures Trading Commission. Daily closing prices on this exchange, suitably adjusted, can be
interpreted as probabilistic forecasts.
Models and markets both respond to emerging information, but do so in different ways. Most
models are backward-looking by construction; they are calibrated and back-tested based on ear-
lier election cycles, and built using a set of variables that have been selected prior to the prediction
exercise. New information is absorbed only when it starts to affect the input variables, for instance
by making its presence felt in polling data or economic indicators. By contrast, markets are fun-
damentally forward-looking, and can rapidly incorporate information from novel and essentially
arbitrary sources, as long as any trader considers this to be relevant. Information that affects the
prices at which traders are willing to buy and sell contracts changes the market equilibrium, and
hence the implied probabilistic forecasts derived from prices.
Each approach has strengths and weaknesses. New information that knowledgeable observers
know to be relevant—such as debate performances, military strikes, or sharp changes in unem-
ployment claims—can be reﬂected in market prices almost instantaneously, while it leads to much
more sluggish adjustments in model forecasts. However, markets can be prone to herding, cogni-
tive biases, excess volatility, and even active manipulation. Models are generally not vulnerable
to such social and psychological factors, but to avoid overﬁtting, they need to identify a relatively
small set of variables in advance (possibly extracted from a much larger set of potentially relevant
variables), and this can lead to the omission of information that turns out to be highly relevant
in particular instances. Market forecasts face no such constraint, and traders are free to use any
inputs, including model predictions, in forming their assessments.
We show that data from the Economist model and the PredictIt market for the seven months
2


---

leading up to the 2020 election exhibits the following patterns. Using mean Brier scores as a mea-
sure of accuracy, the market performs signiﬁcantly better than the model during the early part of
the period, especially during the month of April, and somewhat worse from September onward.
Averaging over the entire period and across all battleground states, the two mechanisms exhibit
comparable performance. However, they generate quite different forecasts for individual states,
and make errors of different kinds. For example, the model was conﬁdent but wrong in Florida
and North Carolina, while the market was excessively uncertain in Minnesota and New Hamp-
shire. This raises the possibility that a simple average of the two predictions could outperform
both component forecasts in the aggregate, by avoiding the most egregious errors. We verify that
this is indeed the case. Even though no average can ever outperform both components for any
given state-date pair, the simple average does so in the aggregate, across all states and periods.
A simple average of model and market forecasts is a crude approach to generating a syn-
thetic prediction. The fact that it nevertheless exhibits superior performance to either component
suggests that more sophisticated approaches that combine models and markets could be very
promising. Such hybrid forecasting can be approached from two different directions. Models
could directly incorporate prediction market prices as just another input variable, in combination
with polls and fundamentals, or markets could be extended to allow for automated traders en-
dowed with budgets and risk preferences that act as if they believe the predictions of the model.
Following the latter approach, we show below how a hybrid prediction market can be designed
and explored experimentally.
We also conduct a performance test, by examining the proﬁtability of a bot that held and up-
dated beliefs based on the model forecasts throughout the period. We show that a bot of this kind
would have made different portfolio choices in different states, building a large long position in
the Democratic candidate in some states, while switching frequently between long and short posi-
tions and trading much more cautiously in others. It would have made signiﬁcant proﬁts in some
states and lost large sums in others, but would have made money on the whole, for a double digit
return. As a check for robustness, we consider how performance would have been affected had
one or more closely decided states had a different outcome. This proﬁtability test can be used as a
novel and dynamic criterion for a comparative evaluation of model performance more generally.
2
Related Literature
Forecasting elections based on fundamental factors such as economic conditions, presidential ap-
proval, and incumbency status has a long history (Fair, 1978; Lewis-Beck and Rice, 1984; Abramowitz,
1988; Campbell and Wink, 1990; Norpoth, 1996; Lewis-Beck and Tien, 1996). In 2020 such models
faced the difﬁculty of an unprecedented collapse in economic activity in response to a global pan-
3


---

demic, and were forced to make a number of ad hoc adjustments (Abramowitz, 2020; J´erˆome et al.,
2020; DeSart, 2020; Enns and Lagodny, 2020; Lewis-Beck and Tien, 2020; Murr and Lewis-Beck,
2020; Norpoth, 2020). While they varied widely in their predictions for the election, the average
across a range of models was reasonably accurate (Dassonneville and Tien, 2020).
Traditional models such as these typically generate forecasts with low frequency, often just
once in an election cycle. More recently, with advances in computational capacity, data processing,
and machine learning, models have been developed that rapidly incorporate information from
trial heat polls and other sources to generate forecasts at daily frequencies. In the 2020 cycle
there were two that received signiﬁcant media attention, published online at FiveThirtyEight and
The Economist; see Silver (2020) and Heidemanns et al. (2020) for the respective methodologies.
We focus on the latter because it has greater clarity and transparency, though our analysis could
easily be replicated for any model that generates forecasts for the same set of events.
Prediction markets have been a ﬁxture in the forecasting ecosystem for decades, dating back
to the launch of the pioneering Iowa Electronic Markets in 1988 (Forsythe et al., 1992). This market,
like others that followed in its wake, is a peer-to-peer exchange for trading contracts with state-
contingent payoffs. Buyers pay a contract price and receive a ﬁxed payment if the referenced event
occurs by an expiration date, and get no payment otherwise. The contract price is commonly inter-
preted as the probability of event occurrence. The forecasting accuracy of such markets has been
shown to be competitive with those of opinion polls and structural models (Leigh and Wolfers,
2006; Berg et al., 2008a,b; Rothschild, 2009).
A prediction market is a type of crowdsourced forecasting pool that leverages a market struc-
ture, similar to a stock market, to efﬁciently combine judgments, provide timely responses, and
incentivize truthful reporting of beliefs (Wolfers and Zitzewitz, 2004). Forecasting crowds are not
constrained by a ﬁxed methodology or a preselected set of variables, and if suitably diverse, can
include a range of ideas and approaches. Crowdsourcing forecasts have been demonstrated to be
more accurate than experts’ predictions (Satop¨a¨a et al., 2014), which can be attributed to pooling
and balancing diverse opinions (Budescu and Yu, 2007). A market can predict well even if indi-
vidual participants predict poorly, through endogenous changes in the distribution of portfolios
over time (Kets et al., 2014).
The value of combining or aggregating forecasts derived from different sources has been dis-
cussed by many authors; see Clemen (1989) for an early review and Rothschild (2015) and Graefe
et al. (2015) for more recent discussions. We propose a novel method for aggregating predictions
through the actions of a trading bot that internalizes the model and is endowed with beliefs, a
budget, and risk preferences. In some respects the activities of this trader resemble those of a tra-
ditional specialist or market maker, as modeled by Glosten and Milgrom (1985) and Kyle (1985),
as well as algorithmic traders of more recent vintage, as in Budish et al. (2015) and Baron et al.
4


---

(2019). But there are important differences, as we discuss in some detail below.
3
Data
Heidemanns et al. (2020) constructed a dynamic Bayesian forecasting model that integrates infor-
mation from two sources—trial heat polls at the state and national level, and fundamental factors
such as economic conditions, presidential approval, and the advantage of incumbency—while
making allowances for differential non-response by party identiﬁcation and the degree of political
polarization. The model builds on Linzer (2013), and uses a variant of the Abramowitz (2008)
fundamentals model as the basis for a prior belief. State-level forecasts based on this model were
updated and published daily, and we use data for the period April 1 to November 2, 2020, stop-
ping the day before the election.
For the same forecasting window, we obtained daily closing price data for state markets from
the PredictIt exchange. These prices are for contracts that reference events, and each contract pays a
dollar if the event occurs and nothing otherwise. For example, a market based on the event ”Which
party will win Wisconsin in the 2020 presidential election?” contained separate contracts for the
“Democratic” and “Republican” nominees. At close of trading on November 2, the eve of the
election, the prices of these contracts were 0.70 and 0.33 respectively. These cannot immediately
be interpreted as probabilities since they sum to something other one.1 To obtain a probabilistic
market forecast, we simply scale the prices uniformly by dividing by their sum. In this instance
the market forecast for the likelihood of a Democratic victory is taken to be about 0.68.
Traders on PredictIt were restricted to a maximum position size of $850 per contract. The ef-
fects on predictive accuracy of such restrictions is open to debate, but the limits do preclude the
possibility that a single large trader could dominate or manipulate the market and distort prices,
as was done on the Intrade exchange during the 2012 cycle (Rothschild and Sethi, 2016). Further-
more, despite the restrictions on any individual trader’s position sizes, total trading volume on
this exchange was substantial. Over the seven-month period under consideration, for markets
referencing outcomes in thirteen battleground states, more than 58 million contracts were traded.
Our focus is on 13 swing states that were all considered competitive to some degree at various
points in the election cycle: Arizona, Florida, Georgia, Iowa, Michigan, Minnesota, Nevada, New
Hampshire, North Carolina, Ohio, Pennsylvania, Texas, and Wisconsin. We exclude states that
were considered non-competitive both because there is little disagreement between the model
1This is a consequence of the fee structure on Predictit, which took ten percent of all trader proﬁts. In the absence of
fees, a trader could sell both contracts and effectively purchase $1.03 for $1.00, making the prices unsustainable. The
Iowa Electronics Market does not charge fees and the prices of complementary contracts on that exchange preclude such
arbitrage opportunities.
5


---

and the market, and also because much of the disagreement that exists arises because the incentive
structure created by markets distorts prices as they approach extreme levels.2
Figure 1 shows the probability of a Democratic victory in eleven of the thirteen states based on
the model and the market.3 As can be seen, both the levels and trends diverge quite substantially.
The model began to place extremely high likelihood (close to 100 percent) on a Democratic victory
in Michigan, Wisconsin, Nevada, and Pennsylvania as the election approached, while the market
forecast was much less certain, especially for Pennsylvania.
Figure 1: Probabilities of a Democratic Victory in Selected States, based on Model and Market
As Figure 1 reveals, the model predictions span a larger subset of the probability space than
the market predictions do, especially over the latter part of the period. This can be seen more
clearly clearly in Figure 2, which shows the frequencies with which speciﬁc probabilities appear
in the data, aggregating across all thirteen states. The range of the market data is considerably
more compressed.
2Speciﬁcally, as the price of a contract approaches 1 for events that are considered very likely, contracts will have
high market prices and negligible potential gain, while betting against the event will have negligible cost and high gain
with low probability. This results in a demand-supply imbalance that distort prices away from underlying beliefs.
3Two of the states—New Hampshire and Minnesota—have been dropped from the ﬁgure for visual clarity; these
exhibit roughly similar patterns to the state of Nevada.
6


---

Figure 2: Frequency Distributions for Model and Market Predictions
Given this, one might expect that at any given probability level, more states would appear
at least once over the period of observation. However, this is not the case. At most seven states
appear at any given prediction point in the market, and this happens just once at probability point
0.63. The model has more than 25 prediction points at which seven or more states appear, and the
peak is 10 states at probability point 0.54. That is, not only does the model span a larger range
of probabilities, it also has greater movement across this range for individual states. These dis-
crepancies indicate differences in the ways in which models and markets aggregate information.
The market forces updates to be frequent (because the number of traders is large) and to be small
(because no individual can move prices much). Small, frequent updates have been asociated with
better accuracy among forecasters (Atanasov et al., 2020).
4
Performance
A standard tool for assessing the accuracy of probabilistic forecasts is the Brier score (Brier, 1950).
In the case of binary outcomes this is just the mean squared error. Letting pit denote the probability
7


---

assigned in period t to a Democratic victory in state i, the score is given by
sit = (pit −ri)2,
where ri = 1 if state i is resolved in favor of the Democratic nominee and ri = 0 otherwise.
We have n = 13 events (corresponding to outcomes in the battleground states), for each of
which there are 216 forecasts on consecutive days. Aggregating across all events we obtain a time
series of the average Brier score:
st = 1
n
n
∑
i=1
(pit −ri)2.
This can be computed for models and markets separately, resulting in the plots in Figure 3. As
we have already seen, the market forecasts were much less variable over time, both for individ-
ual states and in the aggregate. Looking at relative performance, we see that markets were sig-
niﬁcantly more accurate on average during the early part of the forecasting window. This was
followed by a period of roughly comparable performance, with the model pulling ahead as the
election approached.
Figure 3: Mean Brier Scores for the Model and Market over Time
Averaging across time as well as states, we can obtain a scalar measure of overall performance
8


---

for each method as follows:
s = 1
nT
T
∑
t=1
n
∑
i=1
(pit −ri)2,
where T = 216 is the number of periods in the forecasting window. On this measure we ﬁnd
virtually identical average forecasting performance across methods:
smodel
=
0.1523
(1)
smarket
=
0.1539
(2)
However, this conceals signiﬁcant differences in performance over time as are evident in Figure 3.
As an alternative performance measure, consider calibration curves for the model and market
forecasts, shown in Figure 4. Again, the small number of total events being forecast leads to a
lot of volatility, since the inclusion or exclusion of a single state at a prediction point can shift the
realized outcome sharply. At the extreme points of the range, where only one state appears, the
realizations for all forecasts have to be either zero or one. As is apparent from the ﬁgure, the model
is quite well calibrated across the range of forecasts. The market forecasts span a more compressed
range, as we have already seen, and the calibration appears less impressive.
Figure 4: Calibration Curves for the Model and Market
9


---

One factor that may have distorted prices as the election approached was a staggering increase
in volume in the wake of a sustained inﬂow of funds. This can be seen in Figure 5, which shows
the total number of contracts traded daily in the thirteen battleground states over the seven month
period, using a log scale. Daily volume by the end of the period was a thousand times as great as
at the start. In fact, volume continued to remain extremely high even after the election was called
on November 7, driven in part by traders who were convinced that the results would somehow
be overturned. On November 8, for instance, there were more than 2.7 million contracts traded
for six key contested states (Arizona, Georgia, Michigan, Nevada, Pennsylvania, and Wisconsin).
All of these had been called for Biden but the implied market forecast for the Democrat ranged
from 0.86 in Arizona to 0.93 in Nevada. This suggests that even leading up to the election, a group
of traders convinced that a Trump victory was inevitable and willing to bet large sums on it were
having signiﬁcant price effects (Strauss, 2021).
Figure 5: Trading Volume for Major Party Contracts in Thirteen Battleground States
Even setting aside this consideration, it is important to note that our comparison between
model and market performance ought not to be seen as deﬁnitive. Although we examine more
than 2,800 predictions for each mechanism over the seven month period, they reference just thir-
teen events, and the scores are accordingly very sensitive to changes in outcome. For example, the
model assigned a 97 percent likelihood of a Biden victory in Wisconsin on the eve of the election,
10


---

and this state was decided by less than 21,000 votes, about 0.6 percent. Had there been a different
outcome in Wisconsin (or indeed in Michigan, Pennsylvania, or Nevada, all of which were close,
and all of which the model predicted Biden would win with probability 93 percent or higher) the
model’s measured performance would have been much worse. The value of examining relative
performance lies in identifying systematic variation across time, the nature of errors, and the value
of hybridization. We consider this next.
5
Synthetic Forecasts
As a ﬁrst step to demonstrating the value of combining model and market forecasts, we compute
for each state-date pair the simple average estimate for the probability of a Democratic victory.
Brier scores for this synthetic forecast are shown in Figure 6, along with the separate model and
market scores shown earlier in Figure 3.
By construction, for any given state-date pair, the score for the synthetic forecast must lie be-
tween model and market scores; it cannot be lower than both. But this is no longer true when we
average across states at any given date. In fact, as Figure 6 clearly shows, there are many dates on
which the synthetic forecast performs better than both model and market. Of the 216 days in the
series, there are 87 on which the synthetic forecast beats both model and market, including each
of the 26 days leading up to the election. Furthermore, across the entire time period and all states,
the hybrid forecast received a Brier score of
shybrid = 0.1499.
(3)
Comparing (3) to (1)–(2) we see that the simple average of the two component forecasts outper-
formed both market and model.
How can a simple average of two forecasts be superior to each of the component forecasts?
The reason is that the Brier score penalizes large errors, and the model and market make such
errors in different ways and for different states. Consider, for example, the scores for just the
November 2nd forecasts, which are shown in Figure 7 for each of the states. For any given state
the hybrid forecast Brier score necessarily lies between the two other scores. But averaging across
states for this date, we get scores of 0.1414 for the market, 0.1339 for the model, and 0.1228 for the
hybrid forecast. The market fared poorly in states such as New Hampshire and Minnesota, for
which it did not make conﬁdent forecasts even though they ended up not being especially close.
The model fared poorly in Florida and North Carolina, where it predicted Democratic wins with
probabilities 0.78 and 0.67 respectively, neither of which materialized.
11


---

Figure 6: Mean Brier Scores for the Model, Market, and a Simple Average over Time
To summarize, the model fared poorly in states that it conﬁdently expected to go to Democratic
nominee, and which he ended up losing in the end. The market fared poorly in a number of states
where it correctly predicted that the Democrat would win, but with much lower conﬁdence than
the model. The hybrid forecast could not beat both model and market for any given state, but was
able to beat both when averaging across states, by avoiding the most egregious errors.
The simple unweighted average, taken uniformly across time, is the crudest possible way of
generating a hybrid forecast.4 One alternative is to use prediction market prices as direct inputs in
the model, along with information from trial-heat polls and fundamentals. A different approach,
which we describe next, consists of constructing markets in which a model is represented by a
virtual trader.
4See, however, Dawes (1979) on the ”robust beauty” of linear models and how even unsophisticated models succeed
at rule-based prediction and minimizing error.
12


---

Figure 7: Brier Scores for Market, Model, and Hybrid Forecasts on November 2
6
Hybrid Prediction Markets
Algorithmic trading is a common feature of modern ﬁnancial markets, where low latency can be
highly rewarding (Budish et al., 2015; Baron et al., 2019).5 In this sense markets for stocks and
derivatives are already hybrid markets. But algorithms in these settings operate as part of an or-
ganic trading ecosystem, competing with each other and more traditional strategies implemented
by fund managers and retail investors. In order to construct a hybrid prediction market that can
be tuned and tested experimentally, we propose a somewhat different approach.
Given a model that generates forecasts updated with relatively high frequency, one can insert
into the market a trading bot that acts as if it believes the model forecast. In order to do so, the
bot has to be endowed with a budget and preferences that exhibit some degree of risk aversion.
These parameters can be tuned in experimental settings to examine their effects on forecasting
accuracy. The bot posts orders to buy and sell securities based on its beliefs (derived from the
model), its preferences, and its existing portfolio, which consists of cash and various asset posi-
tions. These orders either trade immediately or enter the order book, providing opportunities for
human traders to bet on or against the referenced event if their own assessments of its likelihood
5Algorithmic trading was also extremely common on the Intrade prediction market (Rothschild and Sethi, 2016),
even though it is disallowed on PredictIt.
13


---

differ. And through the process of trading, the cash and asset holdings of the bot evolve over time,
affecting the prices and sizes of its orders.
To be precise, consider a model that generates a joint distribution over the electoral outcomes
in m jurisdictions, where each jurisdiction has n candidates on the ballot.6 Let S denote an n × m
matrix that represents an outcome realization, with typical element sij ∈{0, 1}. Columns sj of
S correspond to jurisdictions, and sij = 1 indicates that candidate i is the (unique) winner in
jurisdiction j. Let Ωdenote the set of all possible electoral outcomes, and let p : Ω→[0, 1] denote
the probability distribution over these outcomes generated by the model.
Now suppose that for each jurisdiction there exists a prediction market listing n contracts, one
for each candidate. In practice, there will be distinct prices for the sale and purchase of a contract,
the best bid and best ask prices. We return to this issue in Section 8 below, but assume for the
moment that there is no such difference, and that each contract is associated with a unique price at
which it can be bought or sold.7 Let Q denote a set of prices in these markets, with typical element
qij ∈[0, 1]. Here qij is the price at which one can purchase or sell a contract that pays a dollar if
candidate i wins in jurisdiction j, and pays nothing otherwise. Columns qj of Q contain the prices
for each of the i contracts in jurisdiction j.
Next consider a virtual trader or bot that represents the model in the market, in the sense that
it inherits and updates beliefs over the set of outcomes based on the output of the model. At any
given point in time, this trader in this market will be holding a portfolio (y, Z), where y is cash
and Z is a n × m matrix of contract holdings. Element zij ∈R is the number of contracts held by
the trader that reference candidate i in jurisdiction j. It is possible for zij to be negative, which
corresponds to a short position: if candidate i wins in jurisdiction j then a trader with zij < 0
will pay (rather than receive) a dollar per contract. Buying a contract referencing candidate i in
jurisdiction j lowers cash by qij and raises zij by one unit, while selling such a contract raises cash
by qij and lowers zij by one unit. Let zj denote column j of Z, the contract holdings in the market
corresponding to jurisdiction j.
If the outcome is S ∈Ωwhen all contracts are resolved, the terminal cash value or wealth
resulting from portfolio (y, Z) is
w = y + ∑
j∈M
s′
jzj,
where M = {1, ..., m} is the set of jurisdictions. A risk-neutral trader would choose a portfolio that
maximizes the expected value E(w) of terminal wealth, given her beliefs p and the market prices
Q, subject to solvency constraints that are discussed further below. A risk-averse trader, instead,
6There is no loss of generality in assuming that all jurisdictions have the same number of candidates, since any with
fewer than n candidates can be assigned notional candidates who win with zero probability.
7For battleground state markets on PredictIt the bid-ask spread was typically just a penny, which large numbers of
contracts available for purchase and sale at most times.
14


---

will maximize expected utility, given by
E(u) = ∑
S∈Ω
p(S)u
 
y + ∑
j∈M
s′
jzj
!
,
where u : R+ →R is strictly increasing and concave.
Given a starting portfolio (y, Z), beliefs p, preferences u, and prices Q, let X denote an n × m
matrix of trades, where xij ∈R is the (possibly negative) number of contracts purchased that
reference candidate i in jurisdiction j. Column j of X, which registers trades involving jurisdiction
j, is denoted xj. The set of trades will be chosen to maximize
E(u) = ∑
S∈Ω
p(S)u
 
y + ∑
j∈M

s′
j(zj + xj) −q′
jxj
!
.
(4)
If xij > 0 then contracts are purchased, zij rises by this amount, and y falls by the cost of the
contracts. If xij < 0 then contracts are sold, zij falls by this amount, and y rises by the cost of the
contracts.
A trading bot programmed to execute transactions in accordance with the maximization of (4)
will trade whenever there is a change in model output p or in market prices Q. Any such trades
must be consistent with solvency even in the worst case scenario.8 That is, the trading bot chooses
X to maximize (4) subject to the constraint:
y + min
S∈Ω∑
j∈M

s′
j(zj + xj) −q′
jxj

≥0.
We next consider whether a bot trading daily in accordance with the model beliefs and a particular
speciﬁcation for preferences u, facing actual prices on PredictIt, would have made money.
7
A Proﬁtability Test
The analysis in the previous section can be put to use to develop an alternative measure of model
performance, both relative to the market and to other models. Speciﬁcally, one can ask the hypo-
thetical question of whether a bot endowed with model beliefs would have been proﬁtable over
the course of the forecasting period, when matched against the actual market participants. And
one can use the level of proﬁts or losses to compare different models, and obtain a performance
criterion in which early and late forecasts are treated differently in a systematic and dynamic man-
ner. Proﬁtability of a model is also a necessary condition for survival, without which the model
8Most prediction markets, including PredictIt, operate under a 100 percent margin requirement to ensure contract
fulﬁllment with certainty, so that there is no counter-party risk or risk borne by the exchange itself.
15


---

could not have a signiﬁcant and persistent effect on market prices. If the model makes losses con-
sistently its budget will diminish endogenously and it will become negligible relative to the rest of
the market. Therefore only a proﬁtable model can yield hybrid forecasts that differ meaningfully
from market forecasts.
In order to implement this idea, we endowed a trading bot with a cash position y = $1000 and
a contract position z = 0. Each market has two contracts referencing the same event and we take
the average of daily closing prices and allow the bot to meet all demand at this price. In practice,
the price available to the bot could be slightly better as it could pick the better-priced contract or
slightly worse from the bid-ask spread. Given the bot budget, its trades have a negligible effect
on the order book. Additionally, we need to specify preferences for the bot. A useful class of
functions for which the degree of risk aversion can be tuned for experimental purposes is that
exhibiting constant relative risk aversion (CRRA):
u(w) =



1
1−ρw1−ρ,
if ρ ≥0, ρ ̸= 1
log(w),
if ρ = 1
where ρ is the degree of relative risk-aversion. We report results below for the case of log utility.
One piece of information that is unavailable to us is the complete daily probability distribution
p(S) over the set of possible outcomes, where |S| = 213 = 8192. What we have, instead, are the
daily marginal distributions for each state. Since state outcomes cannot be treated as independent,
this is a signiﬁcant loss of information. Nevertheless, we can show that a bot operating with this
limited information would have been proﬁtable overall, despite making losses in several states.
We ﬁrst illustrate this for the state of Wisconsin. Negative values of z correspond to bets against
the Democratic nominee. The evolution of z over time for Wisconsin is shown in Figure 8. Initially
the market considered a Biden victory to be more likely than the model did, so the bot entered a
short position (negative z) in this contract. This started to change towards the end of April, and
the bot started to cover this short position by buying contracts, eventually ending up with a long
position (positive z) that grew unevenly but substantially over time until the election.
There are several ﬂuctuations and interruptions in this growth, reﬂecting changes in beliefs
and prices that warranted a less aggressive posture. But by the eve of the election the bot held
less than $90 in cash, along with almost 1,500 contracts. This portfolio had a market value of
almost 1,100 on November 2. That is, the bot could have sold all contracts at the then-prevailing
market price and ended up with a ten percent return without taking any risk into election day,
insulated completely from the eventual outcome. These proﬁts were generated by buying and
holding contracts that had subsequently risen in price, or by buying and selling along the way.
But the bot did not liquidate its position, and once the contracts were resolved, ended up with a
16


---

cash position of $1,574 for a 57% return. Had Biden lost Wisconsin this would have resulted in a
substantial loss, exceeding 90%.
Figure 8: Evolution of Contract Holdings for Wisconsin
Repeating this analysis for the other twelve states, we get the paths shown in Figure 9. In
all cases the bot began by betting against a Democratic victory but quickly changed course in
many states. Several states follow the same pattern as Wisconsin, in that a large positive position
was built up over time. These states resulted in signiﬁcant proﬁts (Michigan, Minnesota, New
Hampshire, Pennsylvania) or signiﬁcant losses (Florida). There are also some states in which
trading was much more cautious, because model forecasts and market prices were not far apart.
And in many states contract holdings switched often from short to long and back again.
Additional details for all states, including ﬁnal portfolios, terminal payoffs, proﬁts, and rates
of return, may be seen in Table 1. Only in Texas did the bot hold a short position in a Democratic
victory on the even of the election; elsewhere the model favored the Democrat to a greater degree
than the market. The market value of all portfolios on the eve of the election was just slightly
greater than the starting value of $13,000. That is, if the bot had liquidated all positions immedi-
ately prior to resolution it would have basically broken even. But the eventual payoff was much
larger, with a proﬁt exceeding $2,000 and a 16% return, as proﬁts in some states outweighed losses
17


---

in others. In general the bot made money where the Democrat won and lost where the Republican
prevailed, with the single exception being Texas.9
Figure 9: Bot Contract Holdings for 12 battleground States.
The payoffs and proﬁts shown in Table 1 are based on the actual election outcomes. As a
check on robustness, one might ask how the model would have performed if one or more close
states had been decided differently. There were three states that were especially close, decided
by less than one percentage point: Georgia (0.24 percent), Arizona (0.31 percent) and Wisconsin
(0.62 percent). All three were won by the Democrat. Table 2 shows the payoffs and proﬁts that
would have accrued to the bot had one or more of these been won by the Republican instead. In
each case proﬁts would have been lower, since the bot was betting on a Democratic victory in all
three states. If any one of these states had been decided differently, proﬁts would still have been
positive. However, if the Democrat had lost Wisconsin along with one or both of Georgia and
Arizona, it would have made a loss overall, largely because the model’s very high conﬁdence that
the Democrat would win Wisconsin led the bot to accumulate a substantial number of contracts.
9In Texas the cash position exceeded the value of the portfolio on election day, because the contract position was
negative; had Biden won Texas the bot would have had to pay out about $37 and would have ended up with a loss in
this state.
18


---

State
Cash
Contracts
Value
Payoff
Proﬁt
Return
Arizona
$566.45
748.55
$944.35
$1,314.99
$314.99
31%
Florida
$339.96
1351.73
$904.28
$339.96
–$660.04
–66%
Georgia
$743.54
735.23
$1,034.72
$1,478.76
$478.76
48%
Iowa
$855.20
722.99
$1,039.50
$855.20
–$144.80
–14%
Michigan
$68.29
1383.63
$1,004.27
$1,451.92
$451.92
45%
Minnesota
$54.98
1305.55
$1,021.09
$1,360.53
$360.53
36%
Nevada
$190.84
1094.15
$976.93
$1,284.99
$284.99
28%
New Hampshire
$72.74
1274.46
$984.85
$1,347.20
$347.20
35%
North Carolina
$607.15
880.03
$1,004.03
$607.15
–$392.85
–39%
Ohio
$904.82
669.22
$1,096.97
$904.82
–$95.18
–10%
Pennsylvania
$138.91
1359.79
$921.43
$1,498.70
$498.70
50%
Texas
$1,027.13
–36.95
$1,016.47
$1,027.13
$27.13
3%
Wisconsin
$89.92
1484.09
$1,088.83
$1,574.01
$574.01
57%
Total
$13,037.72
$15,045.36
$2,045.36
16%
Table 1: Terminal portfolios, payoffs, and proﬁts in battleground states.
The hypothetical proﬁts in Table 2 provide a measure of robustness by identifying the number
of close states (based on some speciﬁed threshold) that would have to ﬂip in order for the model to
incur a loss. In this case the critical number or ”robustness diameter” is two. For a more granular
robustness measure, one could ask how many votes would be required to ﬂip in order for the
bot to lose money, and in this case the critical number is 31,141 votes (in Arizona and Wisconsin).
In comparing the performance of two or more models against the market, one can consider both
proﬁtability (which depends in part on pure chance) and the robustness diameter in this way.10
Flipped State(s)
Margin
Payoff
Proﬁt
Rate
Georgia
11,780
$14,310.14
$1,310.14
10.08%
Arizona
10,458
$14,296.82
$1,296.82
9.98%
Wisconsin
20,683
$13,561.27
$561.27
4.32%
Georgia, Arizona
22,238
$13,561.60
$561.60
4.32%
Georgia, Wisconsin
32,463
$12,826.05
–$173.95
–1.34%
Arizona, Wisconsin
31,141
$12,812.73
–$187.27
–1.44%
Georgia, Arizona, Wisconsin
42,921
$12,077.51
–$922.49
–7.10%
Table 2: Hypothetical payoffs and proﬁts if the closest states had been decided differently.
The proﬁtability test explored here may be improved by using the complete model-derived
probability distribution over outcomes rather than just the marginal distributions for each state,
10Note, however, that the risk preferences assigned to the bot will affect the aggressiveness of trading, position sizes,
proﬁtability, and the robustness diameter.
19


---

and by allowing cash to ﬂow freely across markets. This offers the possibility of evaluating a
model based on its deep structure, including correlations across states, rather than just on the
derived marginal distributions for each state. It therefore provides a new and dynamic evaluation
criterion that can be used to compare models with each other, and to assess the value of hybrid
forecasting more generally.
8
The Model as Market Maker
To this point we have not distinguished between bid and ask prices, which will typically differ
and cause the purchase price to be slightly higher that the sale price. We have also assumed that
any demands or supplies can be met at prevailing market prices. But in the absence of any prices
at which trading can occur, the bot representing the model can post prices at which it would be
willing to trade, thus providing liquidity to the market. This is important for the development of
experimental markets which are not already populated with a large number of active traders.
As an example consider a model that forecasts a single event with n ≥2 options or bins, each
of which has a corresponding contract. That is, if the outcome is in bin i then that contract pays
out while the others expire worthless. Suppose that a model generates a probability distribution
p∗= (p∗
1, ..., p∗
n) over the possible outcomes. At any point in time, the trading bot will have a
cash position y ≥0 and asset position z = (z1, ..., zn), where each zi can be positive or negative
(representing a long or short position). The bot is endowed with a utility function u(w) where w is
the cash holding after resolution. This is uncertain at the time of trading, and the bot places orders
in order to maximize expected utility as before.
Now consider any particular bin or outcome interval i. We need to ﬁnd the highest price at
which the bot will be willing to buy shares, and the lowest prices at which it will sell. We also
need to compute the quantities posted at those prices. Suppose that at any hypothetical price pi
in market i the bot places an order to buy xi shares in this market. Then, given the beliefs p∗, its
expected utility is
E(u) = p∗
i u(zi + xi + y −pix) + ∑
j̸=i
p∗
j u(zj + y −pixi).
(5)
Maximizing this yields a demand x(pi) for any market i and price pi. Let pb
i and ps
i denote the
highest price at which x(pi) > 0 and the lowest price at which x(pi) < 0 respectively. Then bot
places orders to buy xi(pb
i ) shares at price pb
i orders to sell xi(ps
i) shares at price ps
i in each market
i. Note that all buy and sell prices are functions of (y, z) and will change each time the bot is able
to buy or sell any contracts.
The bot is effectively acting as a market marker, as in Glosten and Milgrom (1985) and Kyle
20


---

(1985), but instead of making inferences from the trading activity of counterparties, it derives and
updates its beliefs based on the model. It acts as an informed trader rather than an uninformed
market maker, and is willing to take and hold large directional positions.
To illustrate, consider forecasting problem with three options or bins, and a model that assigns
probability p∗= (0.3, 0.5, 0.2). The problem could involve discrete outcomes that can take one of
three values, or continuous outcomes that can fall into three speciﬁed ranges. The model forecast
is represented in the market by a bot having initial cash endowment y = $1000 and preferences
given by u(w) = log(w). The bot initially holds no contracts, so z = (0, 0, 0).
To begin with, the bot places six orders, one to buy and one to sell in each of the three bins,
resulting in the following order book:
Bin
Bid Price
Bid Quantity
Ask Price
Ask Quantity
1
0.29
48
0.31
46
2
0.49
40
0.51
40
3
0.19
64
0.21
60
This is what human traders see when they view the market. For each bin the prices posted by the
bot straddle the beliefs generated by the model, though this can change as cash and asset positions
are altered through the process of trading, as we shall see momentarily. The bid-ask spreads are
tight, and there is plenty of liquidity available for humans who wish to trade.
Now suppose that the offer to buy 48 shares at 0.29 is met (a human trader chooses to bet
against the event corresponding to Bin 1, paying 0.71 per contract for 48 contracts, each of which
will pay out a dollar if this event does not occur). Then the asset position of the bot goes to
z = (48, 0, 0) and its cash position goes to 1000 −0.29(48) = 986.08. At this point he bot cancels
all remaining orders and starts afresh, placing six new orders by maximizing (5) with the current
portfolio as starting point. As a result, prices and quantities change in all markets, not just in the
market in which the transaction occurred, resulting in the following order book:
Bin
Bid Price
Bid Quantity
Ask Price
Ask Quantity
1
0.28
51
0.30
47
2
0.50
28
0.51
11
3
0.20
17
0.21
42
Note that the bot is now willing to sell shares in the ﬁrst bin at price 0.30, even though this
exactly matches its belief. This is because it can secure a reduction in the risk of its portfolio,
without lowering expected value. In fact, if it continues to accumulate shares in the ﬁrst bin, it
will offer to sell at prices below 0.30, lowering expected return but also lowering risk.
21


---

A naive observer of this market will see a bot acting as a market maker, placing orders on both
sides of the market, and canceling and replacing these whenever any order is met. But the strategy
implemented by the bot is not that of a traditional market maker; it is maximizing expected utility
subject to model-based beliefs about the various outcomes. In fact, when the model is updated
the bot’s imputed beliefs p∗change, and it will respond by canceling and replacing all orders,
possibly resulting in the immediate execution of trades against humans. And human traders can
trade against each other, or post limit orders that compete with those posted by the bot.11
A market of this kind could easily be implemented experimentally, with bot preferences and
budgets adjusted to test for effects on predictive performance. And unlike some existing experi-
mental exchanges such as the Iowa Electronic Markets, there will be substantial liquidity available
to human traders at all times. No matter what the model forecast or trading history, at least one
side of the order book will always be populated. As a result the spreads between bid and ask
prices will be narrower, providing greater incentives for market participation.
Social inﬂuence can be beneﬁcial or harmful to predictive accuracy (Gelman and Rothschild,
2016; Toyokawa et al., 2019). Our proposed hybrid prediction market aims to harness beneﬁcial
social inﬂuence by anchoring trader beliefs on objective, model-based predictions. Through this
process the model forecasts enter market prices, integrated with the beliefs of human traders.
Over time, the bot’s inﬂuence on market prices will grow if it makes money, and shrink if it loses.
This is as it should be—a model that predicts poorly should have diminishing inﬂuence on the
hybrid forecast over time.
9
Discussion
The analysis in this paper ought not to be seen as a meaningful horse race between models and
markets, since all the forecasts reference just thirteen closely connected and correlated events, and
a different outcome in a couple of states could have resulted in a very different evaluation of per-
formance. Instead, our primary contribution should be seen as the development of a particular
approach to hybrid forecasting that can be implemented, calibrated and tested empirically. It is
important to be attentive to concerns about external validity, however, since real-world markets
have recently been prone to high volatility arising from the spread of misinformation or coordi-
nated attempts to inﬂate prices (Strauss, 2021; Phillips and Lorenz, 2021).
Models extrapolate from available data in a manner that is potentially objective, transparent,
and consistent. They are designed to produce good average calibration across the probability
11The hybrid prediction market described here is accordingly quite different from one in which an automated market
maker is a counterparty to all trades, and sets prices based on a potential function (Hanson, 2003; Chen and Pennock,
2007; Sethi and Vaughan, 2016).
22


---

space. Markets aggregate real-time human judgement and provide agility and versatility. They
balance a pool of knowledge, and are able to extrapolate from sparse data further from resolution.
We have shown that even a crude simple average of these methods can outperform each one of
them when examining data from the 2020 US presidential election. The lesson here is that hybrid
forecasting methods are well worth developing.
This can be done in a number of ways. The most obvious is to simply construct a simple or
weighted average, as in Rothschild (2015), which has been found to be quite effective relative to
more complex aggregation procedures (Clemen, 1989; Graefe et al., 2015). Along similar lines,
one could include prediction market prices as inputs into existing models, along with trial-heat
polls and fundamental factors, calibrated based on historical data. Alternatively, one could make
model outputs available to human forecasters to use as they see ﬁt when soliciting their beliefs
about events (Abeliuk et al., 2020). Yet another possibility involves tapping the wisdom of crowds
by asking survey respondents to predict the voting behavior of those in their social circles (Galesic
et al., 2018). The method proposed in this paper differs from all of these, and involves bringing
models into direct interaction with humans in prediction markets through the actions of virtual
traders. Each of these hybridization approaches is promising in its own right, and has the potential
to sharpen predictive accuracy, not just for elections but for important and relatively infrequent
events more generally.
References
Andr´es Abeliuk, Daniel M Benjamin, Fred Morstatter, and Aram Galstyan. Quantifying machine
inﬂuence over human forecasters. Scientiﬁc Reports, 10(1):1–14, 2020.
Alan I Abramowitz.
An improved model for predicting presidential election outcomes.
PS:
Political Science & Politics, 21(4):843–847, 1988.
Alan I Abramowitz. Forecasting the 2008 presidential election with the time-for-change model.
PS: Political Science and Politics, 41(4):691–695, 2008.
Alan I Abramowitz. It’s the pandemic, stupid! a simpliﬁed model for forecasting the 2020 presi-
dential election. PS: Political Science & Politics, pages 1–3, 2020.
Pavel Atanasov, Jens Witkowski, Lyle Ungar, Barbara Mellers, and Philip Tetlock. Small steps
to accuracy: Incremental belief updaters are better forecasters. Organizational Behavior and
Human Decision Processes, 160:19–35, 2020.
Matthew Baron, Jonathan Brogaard, Bj¨orn Hagstr¨omer, and Andrei Kirilenko. Risk and return in
high-frequency trading. Journal of Financial and Quantitative Analysis, 54(3):993–1024, 2019.
23


---

Joyce Berg, Robert Forsythe, Forrest Nelson, and Thomas Rietz. Results from a dozen years of
election futures markets research. Handbook of Experimental Economics Results, 1:742–751,
2008a.
Joyce E Berg, Forrest D Nelson, and Thomas A Rietz. Prediction market accuracy in the long run.
International Journal of Forecasting, 24(2):285–300, 2008b.
Glenn W Brier.
Veriﬁcation of forecasts expressed in terms of probability.
Monthly Weather
Review, 78(1):1–3, 1950.
David V Budescu and Hsiu-Ting Yu. Aggregation of opinions based on correlated cues and advi-
sors. Journal of Behavioral Decision Making, 20(2):153–177, 2007.
Eric Budish, Peter Cramton, and John Shim. The high-frequency trading arms race: Frequent batch
auctions as a market design response. The Quarterly Journal of Economics, 130(4):1547–1621,
2015.
James E Campbell and Kenneth A Wink. Trial-heat forecasts of the presidential vote. American
Politics Quarterly, 18(3):251–269, 1990.
Yiling Chen and David M Pennock. A utility framework for bounded-loss market makers. In
Proceedings of the Twenty-Third Conference on Uncertainty in Artiﬁcial Intelligence, pages 49–
56, 2007.
Robert T Clemen.
Combining forecasts: A review and annotated bibliography.
International
journal of forecasting, 5(4):559–583, 1989.
Ruth Dassonneville and Charles Tien.
Introduction to forecasting the 2020 us elections.
PS:
Political Science & Politics, pages 1–5, 2020.
Robyn M Dawes. The robust beauty of improper linear models in decision making. American
psychologist, 34(7):571, 1979.
Jay A DeSart. A long-range state-level forecast of the 2020 presidential election. PS: Political
Science & Politics, pages 1–4, 2020.
Peter K Enns and Julius Lagodny. Forecasting the 2020 electoral college winner: The state presi-
dential approval/state economy model. PS: Political Science & Politics, pages 1–5, 2020.
Ray C Fair.
The effect of economic events on votes for president.
Review of Economics and
Statistics, pages 159–173, 1978.
Robert Forsythe, Forrest Nelson, George R Neumann, and Jack Wright. Anatomy of an experi-
mental political stock market. The American Economic Review, pages 1142–1161, 1992.
24


---

Mirta Galesic, W Bruine de Bruin, Marion Dumas, A Kapteyn, JE Darling, and E Meijer. Asking
about social circles improves election predictions. Nature Human Behaviour, 2(3):187–193, 2018.
Andrew Gelman and David Rothschild. Something’s odd about the political betting markets.
Slate, July 12, 2016.
Lawrence R Glosten and Paul R Milgrom. Bid, ask and transaction prices in a specialist market
with heterogeneously informed traders. Journal of Financial Economics, 14(1):71–100, 1985.
Andreas Graefe, Helmut K¨uchenhoff, Veronika Stierle, and Bernhard Riedl. Limitations of ensem-
ble bayesian model averaging for forecasting social science problems. International Journal of
Forecasting, 31(3):943–951, 2015.
Robin Hanson. Combinatorial information market design. Information Systems Frontiers, 5(1):
107–119, 2003.
Merlin Heidemanns, Andrew Gelman, and G Elliott Morris. An updated dynamic Bayesian fore-
casting model for the US presidential election. Harvard Data Science Review, October 27, 2020.
Bruno J´erˆome, V´eronique J´erˆome, Philippe Mongrain, and Richard Nadeau. State-level forecasts
for the 2020 us presidential election: Tough victory ahead for biden. PS: Political Science &
Politics, pages 1–4, 2020.
Willemien Kets, David Pennock, Rajiv Sethi, and Nisarg Shah. Betting strategies, market selection,
and the wisdom of crowds. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence,
volume 28, 2014.
Albert S Kyle. Continuous auctions and insider trading. Econometrica, pages 1315–1335, 1985.
Andrew Leigh and Justin Wolfers.
Competing approaches to forecasting elections: Economic
models, opinion polling and prediction markets. Economic Record, 82(258):325–340, 2006.
Michael S Lewis-Beck and Tom W Rice. Forecasting presidential elections: A comparison of naive
models. Political Behavior, 6(1):9–21, 1984.
Michael S Lewis-Beck and Charles Tien. The future in forecasting: Prospective presidential mod-
els. American Politics Quarterly, 24(4):468–491, 1996.
Michael S Lewis-Beck and Charles Tien. The political economy model: A blue wave forecast for
2020. PS: Political Science & Politics, pages 1–4, 2020.
Drew A Linzer. Dynamic bayesian forecasting of presidential elections in the states. Journal of the
American Statistical Association, 108(501):124–134, 2013.
Andreas E Murr and Michael S Lewis-Beck. Citizen forecasting 2020: A state-by-state experiment.
PS: Political Science & Politics, pages 1–5, 2020.
25


---

Helmut Norpoth. Of time and candidates: A forecast for 1996. American Politics Quarterly, 24(4):
443–467, 1996.
Helmut Norpoth. Primary model predicts trump reelection. PS: Political Science & Politics, pages
1–4, 2020.
Matt Phillips and Taylor Lorenz. ’dumb money’ is on gamestop, and it’s beating wall street at its
own game. The New York Times, January 27, 2021.
David Rothschild. Forecasting elections: Comparing prediction markets, polls, and their biases.
Public Opinion Quarterly, 73(5):895–916, 2009.
David Rothschild. Combining forecasts for elections: Accurate, relevant, and timely. International
Journal of Forecasting, 31(3):952–964, 2015.
David M Rothschild and Rajiv Sethi. Trading strategies and market microstructure: Evidence from
a prediction market. Journal of Prediction Markets, 10(1):1–29, 2016.
Ville A Satop¨a¨a, Jonathan Baron, Dean P Foster, Barbara A Mellers, Philip E Tetlock, and Lyle H
Ungar. Combining multiple probability predictions using a simple logit model. International
Journal of Forecasting, 30(2):344–356, 2014.
Rajiv Sethi and Jennifer Wortman Vaughan. Belief aggregation with automated market makers.
Computational economics, 48(1):155–178, 2016.
Nate Silver. How ﬁvethirtyeight’s 2020 presidential forecast works—and what’s different because
of covid-19. ﬁvethirtyeight.com, 2020. Accessed: 01-14-2021.
Ilana E. Strauss. The Dark Reality of Betting Against QAnon. The Atlantic, January 1, 2021.
Wataru Toyokawa, Andrew Whalen, and Kevin N Laland. Social learning strategies regulate the
wisdom and madness of interactive crowds. Nature Human Behaviour, 3(2):183–193, 2019.
Justin Wolfers and Eric Zitzewitz. Prediction markets. Journal of Economic Perspectives, 18(2):
107–126, 2004.
26

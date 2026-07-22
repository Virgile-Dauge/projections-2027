---
title: putting-ecological-inference-to-the-test-part-1
id: putting-ecological-inference-to-the-test-part-1
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-sophistication-vs-degradation-maille-fine
- inference-ecologique
- donnees-bureaux-vote
- maille-fine
created: '2026-07-21T19:35:34.158959Z'
updated: '2026-07-21T19:42:36.635421Z'
source: https://www.dataforprogress.org/blog/2019/8/1/putting-ecological-inference-to-the-test-part-1
source_domain: www.dataforprogress.org
fetched_at: '2026-07-21T19:35:34.110940Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Data for Progress (McAuliffe & Fishman, Aug 2019), Part 1 of a simulation-based
  validation of their individual-covariate/aggregate-observation ''ecological inference''
  (EI) method against a baseline that has both individual-level covariates AND individual-level
  vote-choice observations (impossible in real applications but usable as ground truth
  in simulation). Data: 2018 MA-7 Democratic primary voter file, simulated vote choice
  following a known linear model, evaluated via simulation-based calibration (SBC):
  z-scores, shrinkage, and rank statistics. Finding: EI point estimates (z-scores)
  performed AS WELL AS OR SLIGHTLY BETTER on average than the individual-level baseline
  despite EI only observing precinct-aggregated vote counts -- aggregation noise appeared
  to act as a regularizer/''noise filter'' rather than degrading point accuracy. However,
  EI''s posterior was overdispersed (S-shaped rank-statistic distribution vs near-uniform
  for individual-level), meaning EI CIs are wider/less well-identified (lower shrinkage)
  even though point estimates held up. Authors caveat this is a single-election, correctly-specified-model
  simulation and results may not generalize; EI validity requires residuals uncorrelated
  with precinct covariates. Relevant precedent for testing EI methods at precinct
  level specifically (not just district/state), though it is not itself a below-district
  validation against REAL vote-choice ground truth (which is unobservable) -- it is
  a synthetic-data recovery test.'
---

Putting Ecological Inference to the Test, Part 1
[⌃](https://www.dataforprogress.org/blog/2019/8/1/putting-ecological-inference-to-the-test-part-1)
Back [ All Polling ](https://www.dataforprogress.org/latest-polling) [ Briefs ](https://www.dataforprogress.org/blog) [ Reports ](https://www.dataforprogress.org/memos)
Back [ All Issues ](https://www.dataforprogress.org/issues) [ Artificial Intelligence ](https://www.dataforprogress.org/artificial-intelligence) [ Climate ](https://www.dataforprogress.org/climate) [ Disability ](https://www.dataforprogress.org/disability) [ Economy ](https://www.dataforprogress.org/economy) [ Education ](https://www.dataforprogress.org/education) [ Electoral Politics ](https://www.dataforprogress.org/electoral-politics) [ Family Care ](https://www.dataforprogress.org/family-care) [ Foreign Policy ](https://www.dataforprogress.org/foreign-policy) [ Health Care ](https://www.dataforprogress.org/healthcare) [ Immigration ](https://www.dataforprogress.org/immigration) [ Judiciary ](https://www.dataforprogress.org/judiciary) [ LGBTQ+ Rights ](https://www.dataforprogress.org/lgbtq) [ Social Justice ](https://www.dataforprogress.org/social-justice) [ State & Local Polling ](https://www.dataforprogress.org/state-local-polling) [ Voting Rights & Democracy ](https://www.dataforprogress.org/democracy) [ Workers' Rights ](https://www.dataforprogress.org/worker-rights-polling)
Back [ Our Mission ](https://www.dataforprogress.org/our-mission) [ Our Impact ](https://www.dataforprogress.org/our-impact) [ Our Team ](https://www.dataforprogress.org/our-team) [ Our Methodology ](https://www.dataforprogress.org/our-methodology) [ Our Research Philosophy ](https://www.dataforprogress.org/our-research-philosophy) [ Media ](https://www.dataforprogress.org/media) [ Jobs ](https://www.dataforprogress.org/jobs)
# Putting Ecological Inference to the Test, Part 1
By Colin McAuliffe ([@ColinJMcAuliffe](https://twitter.com/colinjmcauliffe)) and Nic Fishman ([@njwfish](https://twitter.com/njwfish))
We have been developing a [new methodology](https://www.dataforprogress.org/blog/2019/5/9/inferring-vote-choice-without-a-survey) for the so-called ecological inference (EI) problem, which attempts to recover information about individuals from aggregated data. We’ve used this method to create “ecological exit polls” for primaries where conventional polling is not available. 
This has helped us gain some insights on who votes for progressive primary challengers and develop predictive models for field campaigns based on those findings. For example, we [found](https://www.dataforprogress.org/blog/2019/5/11/republicans-delivered-the-democratic-primary-election-to-dan-lipinski) that virulent homophobe and anti-choice crusader Dan Lipinski owes his narrow primary victory over Marie Newman to people who frequently vote in Republican primaries, thanks to the open primary system in Illinois. 
Since this is a new methodology, we’ve been working hard to validate its efficacy in a number of different ways. Here we’ll go through the results of a simulation study we conducted as a part of that validation process. The results are encouraging so far, and we plan to build on this work with a series of more comprehensive validations in the future.
To recap, we have two major sources of data available to us. The first is a voter file which has records of which individuals turned out to vote in a particular election. We have a rich dataset of covariates for each voter, but their actual vote choice is unknown. We also have the vote counts reported in each precinct. We use the voter file to specify a model for vote choice based on individual-level covariates, which we link to precinct observations by averaging the individual vote choice probabilities by precinct. 
The fact that we specify the model at the individual level is what distinguishes our method from techniques which regress precinct-level aggregate covariates directly on precinct-level aggregate observations. The table below shows the differences between a classical model that directly regresses aggregate covariates on aggregate observations, our EI model which has individual covariates but aggregate observations, and a model which has both individual level covariates and observations. We don’t consider the aggregate/aggregate model (model 1) in this post, since we want to be able to predict model scores at the individual level and models of this type can’t do that. We’re primarily interested in the performance of model 2 by comparing it to model 3 as a baseline. In reality, we can never actually run model 3 on election results since the vote choice of each individual is unknown (and if it was we wouldn’t need ecological inference anyway!). However we can use model 3 as a baseline because the ‘ground truth’ data is simulated. These example equations use a linear model, but this EI framework is not limited to linear models and many other model families are possible. For example, we’ll describe a deep learning approach in a future post.
For compactness and computational efficiency, we compute the precinct averaged probabilities by multiplying a sparse indicator matrix by the individual probabilities as follows. For person in precinct , and precinct containing voters, let 
Where
Then the precinct average of the individual probabilities k can be computed with a matrix-vector multiplication
As a side note, an alternative approach would be to model this problem with a Poisson-Binomial distribution rather than a binomial distribution with an averaged rate parameter, but we have not explored implementing this yet.
While we can specify a model at the individual level thanks to the voter file, there is no guarantee that we can properly identify the parameters of that model since information is lost when votes are aggregated by precinct. To study this, we conducted a simulation experiment where vote choice is known and follows a simple linear model. We repeatedly generate simulated data, fit the EI model to it, and compute various statistics to assess how well the EI model recovered the ‘true’ model parameters. The steps are as follows
The Z scores tell us how well we recovered the true parameter values from the simulated data, and the shrinkage tells us how much we reduced our uncertainty about a parameter value after observing data. Ideally, the z score should be close to zero, meaning the inference was accurate, and the shrinkage should be close to one, meaning the model is well identified. The rank statistic is an additional tool that can help us diagnose several other potential problems in our inference method. Further details on this procedure can be found in [these](https://arxiv.org/pdf/1804.06788.pdf) [references](https://github.com/betanalpha/jupyter_case_studies/blob/master/principled_bayesian_workflow/principled_bayesian_workflow.ipynb). 
While the vote choice data in this exercise is simulated, the covariates come from real people in the voter file who participated in real elections, in this case, the 2018 MA7 primary. This helps us get a sense of how actually existing patterns of voter sorting can affect our inferences. For both these elections, we run a simulation using the EI model and a second simulation that directly fits a logistic model (model 3 in the table above) on individual vote choice Vi*(data that we do not have in real life situations). This is a conventional logistic model which gives us an idea of what baseline performance should look like.
The distribution of the rank statistic will be uniform for a well-calibrated inference procedure, which we can examine by comparing how well the empirical distribution of the rank statistic follows a straight line. 
For the conventional individual level inference we get pretty close to uniformity, but for ecological inference we see an S-shaped distribution. This indicates that the posterior computed with EI is overdispersed, meaning it is more uncertain than it should be. Comparing the z-scores and shrinkage statistic tells a similar story. EI has lower values for the shrinkage statistic, meaning it’s not as well identified as individual level inference. The z-scores look pretty similar, however, meaning that the EI point estimate didn’t suffer from any loss in accuracy.
In fact, a closer look at the z-scores suggests that the EI point estimate performed better on average than individual inference. So what’s going on here? For EI, we only observe vote counts that are aggregated by precinct. This clearly adds uncertainty to our inferences, but perhaps this is also acting as a sort of noise filter, reducing the chances that model infers an incorrect value. So while the EI problem clearly imposes some unique challenges as we try to traverse the bias-variance tradeoff, we can clearly still recover useful information.
This experiment was encouraging, although fairly limited in scope. There is no guarantee that these results will generalize because the difficulties in identification for EI will depend on how well-sorted voters are by salient characteristics, making every election unique.For classical EI, it’s necessary to show that the model residuals are not correlated with any aggregate covariate, and the validity of our EI framework is likely subject to closely analogous (if not completely identical) conditions. 
This experiment also assumed that the underlying data generating process was very simple and that our model was correctly specified, conditions that are never true in practice. Ultimately, our goal is not to make parameter inferences but to make correct predictions about individual’s vote choices, so in a follow-up post we’ll report an additional simulation study to assess our predictive performance.
Colin McAuliffe ([@ColinJMcAuliffe](https://twitter.com/colinjmcauliffe)) is a co-founder of Data for Progress. 
Nic Fishman ([@njwfish](https://twitter.com/njwfish)) is a senior advisor to Data for Progress. 
[Colin McAuliffe](https://www.dataforprogress.org/blog?author=53f3ce5fe4b0f3ac304bf98c)August 1, 2019
[ Facebook0 ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.dataforprogress.org%2Fblog%2F2019%2F8%2F1%2Fputting-ecological-inference-to-the-test-part-1)[ Twitter ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.dataforprogress.org%2Fblog%2F2019%2F8%2F1%2Fputting-ecological-inference-to-the-test-part-1&text=We+have+been+developing+a+%3Ca+...)[ LinkedIn0 ](https://www.linkedin.com/shareArticle?mini=true&source=Data+For+Progress&summary=We+have+been+developing+a+%3Ca+...&url=https%3A%2F%2Fwww.dataforprogress.org%2Fblog%2F2019%2F8%2F1%2Fputting-ecological-inference-to-the-test-part-1)[ Reddit ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.dataforprogress.org%2Fblog%2F2019%2F8%2F1%2Fputting-ecological-inference-to-the-test-part-1)[ 0 Likes ](https://www.dataforprogress.org/blog/2019/8/1/putting-ecological-inference-to-the-test-part-1)

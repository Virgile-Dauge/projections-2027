---
title: Why polls fail to predict elections
id: why-polls-fail-to-predict-elections
tags:
- electoral-forecasting
- poll-bias
- social-desirability-bias
created: '2026-07-21T18:27:38.153585Z'
updated: '2026-07-21T18:39:17.613968Z'
source: https://arxiv.org/pdf/2101.11389
source_domain: arxiv.org
fetched_at: '2026-07-21T18:27:38.153300Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Zhou, Serafino, Cohan, Caldarelli & Makse (Jan 2021, arXiv:2101.11389) analyze
  raw microdata from a pollster that failed to predict Alberto Fernández''s landslide
  win over Mauricio Macri in Argentina''s August 2019 PASO primary (a shock that triggered
  a market crash). Beyond well-documented low response rates, they identify two specific
  bias mechanisms in the raw/re-weighted longitudinal survey data: (1) mis-representation
  of the underlying population in the sampling frame, and (2) social-desirability
  bias — respondents concealing intent to vote for the more ''controversial''/anti-establishment
  candidate. They propose a longitudinal opinion-tracking alternative using social-media
  big-data analytics, machine learning classification of user political stance, and
  network theory, which correctly predicted Fernández''s overwhelming 2019 victory
  where all traditional pollsters failed. Directly relevant to the research query''s
  Axe 2 concern about data-source bias: documents a general and reproducible failure
  mode (social-desirability under-reporting for the ''controversial'' side) analogous
  to the risk of under-measuring Rassemblement National support in French phone/online
  polls, and offers a non-poll validation method (social-media signal) as an independent
  cross-check on national dynamics.'
raw_file: raw/why-polls-fail-to-predict-elections.pdf
---

Why polls fail to predict elections
Zhenkun Zhou,1 Matteo Seraﬁno,2 Luciano Cohan,3
Guido Caldarelli,4, 5, 6, 7 and Hern´an A. Makse8, ∗
1College of Statistics, Capital University of
Economics and Business, Beijing 100070, China
2IMT School for Advanced Studies, 55100 Lucca, Italy
3Seido, Buenos Aires, Argentina
4Department of Molecular Sciences and Nanosystems,
Ca’ Foscari University of Venice, 30172 Venice, Italy
5European Centre for Living Technology, 30124 Venice, Italy
6Institute for Complex Systems, Consiglio Nazionale
delle Ricerche, UoS Sapienza, 00185 Rome, Italy
7London Institute for Mathematical Sciences,
W1K2XF London, United Kingdom
8Levich Institute and Physics Department,
City College of New York, New York, NY 10031, USA
1
arXiv:2101.11389v1  [cs.SI]  27 Jan 2021


---

Abstract
In the past decade we have witnessed the failure of traditional polls in predicting presidential
election outcomes across the world. To understand the reasons behind these failures we analyze
the raw data of a trusted pollster which failed to predict, along with the rest of the pollsters,
the surprising 2019 presidential election in Argentina which has led to a major market collapse
in that country. Analysis of the raw and re-weighted data from longitudinal surveys performed
before and after the elections reveals clear biases (beyond well-known low-response rates) related
to mis-representation of the population and, most importantly, to social-desirability biases, i.e.,
the tendency of respondents to hide their intention to vote for controversial candidates. We then
propose a longitudinal opinion tracking method based on big-data analytics from social media,
machine learning, and network theory that overcomes the limits of traditional polls. The model
achieves accurate results in the 2019 Argentina elections predicting the overwhelming victory of
the candidate Alberto Fern´andez over the president Mauricio Macri; a result that none of the
traditional pollsters in the country was able to predict. Beyond predicting political elections, the
framework we propose is more general and can be used to discover trends in society; for instance,
what people think about economics, education or climate change.
∗hmakse@ccny.cuny.edu
2


---

Traditional polling methods [1] using random digit dial phone interviews, opt-in samples
of online surveys, and interactive voice response are failing to predict election outcomes
across the world [2–4]. The failure of traditional surveys has also been widely discussed in
the press [5] and on the specialized literature [4]. For instance, the victory of Donald Trump
in the US 2016 presidential election came as a shock to many, as none of the pollsters and
political journalists and pundits, including those in Trump’s campaign, could predict this
victory [4, 6].
The reasons for the failure of pollsters to predict elections are believed to be many [4, 6].
First reason is that the percentage of response to traditionally conducted surveys has de-
creased and it is becoming increasingly diﬃcult to get people’s opinion [4, 7]. Response
rates in telephone polls with live interviewers continue to decline, as it has reached 6%
lower limit recently [7]. Response rates could be even lower for other methodologies, like
internet polling or interactive voice response. Compounded with declining response rates is
the concomitant problem of mis-representation of the survey samples. That is, the sample
surveyed by pollsters does not represent the demographic distributions of the general pop-
ulation. This problem is ameliorated by reweighting the surveys sample according to the
general demographics of the population in a process called sample-balancing or raking [8, 9].
However, in countries where the vote is not obligatory, re-weighting a sample to the general
population demographics (obtained from Census Bureau [1, 4]) fails since the general popu-
lation demographics does not match necessarily the demographics of the voter turnout: it is
impossible to predict which demographic groups will turn out at the voting station. Thus,
if an underrepresented group in the polls, ’the hidden vote’, decides to vote on election date,
the re-weighting fails leading to highly inaccurate results. The issue is believed to be one of
the major reasons for the generalized failure of pollsters to predict the triumph of Trump
in the 2016 US presidential election, where groups generally deﬁned as ’white voters with-
out college degree’ mostly voted for Trump but were undersampled by all pollsters. Even
with this historical information at hand, which supposedly allowed pollsters to resample
their surveys more carefully, pollsters again under-predicted the support for Trump in the
subsequent 2020 presidential election in some states or under-predicted the voter turnout
supporting Biden in newly created battleground states like Georgia, USA [10]. The inabil-
ity to accurately predict the voter turnout to deal with sampling mis-representation might
render the pollsters obsolete.
3


---

While there is increasing evidence [4, 7] that the nonresponse and mis-representation
bias might be the reason that polls are not producing accurately matched election results,
these may not be the only problem of traditional methods of polling. Traditional surveys
in heavily polarized campaigns are aﬀected by social-desirability biases (also called Bradley
eﬀect) [11, 12], i.e. the tendency of subjects to give socially desirable responses instead of
choosing responses that are reﬂective of their true feelings. For instance, the tendency of
survey respondents not to tell the truth of intention of support for controversial candidates
which could open themself to social ostracism. Respondents may feel under pressure to
provide ’politically correct’ answers producing highly-biased results towards the publically
accepted candidate by the media, in detriment of the controversial one. This mechanism
is also believed to have been at place in the massive failure of pollsters to predict 2016 US
election as Trump voters generally can go undetected or even lie to traditional pollsters. We
will show below, that it was also the major reason for the pollsters failure to predict the 2019
Argentina election, which also involved a controversial candidate (Cristina Fern´andez) who
was heavily under-predicted in traditional polls. Furthermore, polls are not able to detect
sudden change of opinion due to some particular events or circumstances, since the process
of opinions collection is time consuming. All these peculiarities together makes impossible
for traditional polls to correctly predict the results of elections.
Monitoring social networks [13, 14] represents an alternative for capturing people’s opin-
ions since it overcomes the low-response rate problem and it is less susceptible to social-
desirability biases [11, 12]. Indeed, social media users continuously express their political
preferences in online discussions without being exposed to direct questions. One of the most
studied social networks is the microblogging platform Twitter [15–18]. Twitter’s based work
generally consist of three main steps: data collection, data processing and data analysis.
The collection of the tweets is often based on the public API of Twitter. It is a common
practice to collect tweets by ﬁltering according to speciﬁc queries, as for example the name
of the candidates in the case of elections [17]. Data processing includes all those techniques
which aim to guarantee the credibility of the Twitter dataset. This is, for example, bots
detection and spam removal [18]. Data analysis, the core of all these studies, can be sim-
pliﬁed in four main approaches: volume analysis, sentiment analysis, network analysis and
artiﬁcial intelligence (AI) [13].
Scholars used the number of mentions for a party of a candidate in order to forecast the
4


---

result of the 2009 German parliament election [19]. While their technique has attracted
many criticisms [20], their work was of inspiration to many other researchers. Gaurav et
al. [21] proposed a model, based on the number of times the name of a candidate is men-
tioned in tweets prior to elections, to predict the winner of three presidential elections held
in Latin America (Venezuela, Paraguay, Ecuador) from February to April, 2013. Based on
volumetric analyses are also the works of Lui et al. [22] and Bermingham [23]. Ceron et al.
[24] performed a sentiment analysis study on the tweets to check the popularity of political
candidates in the Italian parliamentary election of 2011 and in the French presidential elec-
tion of 2012. Caldarelli et al. [25] used the derivative of the volume to forecast the results of
Italian elections. Singh et al. [26] employed sentiment analysis to predict victory of Trump
in the election of 2016. The same author proposed a method [27] based on sentiment anal-
yses and machine learning on historical data to predict the number of seats that contesting
parties were likely to win in the Punjab election of 2017. Other works [28, 29] used social
networks analyses in order to identify the position of a party in the online community by
measuring its centrality. The most supported parties are in general those with an higher
centrality. Bovet et al. [17, 18] used a machine learning model based on in-house training
set produced by hashtags from Twitter supporters to reproduce the polling trends leading
to the 2016 US presidential election.
Despite the large amount of literature, the debate about whether Twitter or other social
media outlets can be used to infer political opinions is still open. Online social networks
are continuously ﬁlled by false, erroneous data through trolls, bots and misinformation
campaigns to a level that distinguish between what is genuine and what is not is in general
diﬃcult [18, 30]. By virtue of this, the great challenge of algorithms and AI is to discover
and interpret real data from ‘junk data’ that could lead to accurate predictions of electoral
or opinion trends.
A crucial limitation of social media based methods is also the mis-
representation bias. While social media solves the low response rates by ’surveying’ millions
of users with non-intrusive methods, these large number of respondents might not represent,
again, the demographics of the voting population. Thus, the opinions of Twitter users may
not be representative of the entire population [31] and re-sampling methods need to be used,
importing along them the same problems that plagued the traditional polls.
In this work we ﬁrst investigate why the traditional polls fail to predict elections. We
focus on the results of the recent primary presidential election in Argentina on August 2019
5


---

and the subsequent presidential election on October 2019, which represents a classic example
of a massive failure of the trusted pollsters in predicting a polarized election electorate, which
in this case, led also to massive markets collapses in the country, since investors largely bet
on the pollster predictions.
This study is possible thanks to the exclusive access to the raw data of longitudinal
surveys conducted by one of the most reliable pollsters in Argentina, Elypsis [32].
The
analyzed data include the original responses of subjects before performing the re-weighting
for sampling bias and the subsequent results obtained after re-weighting. More importantly,
the data includes a longitudinal study on the same 1,900 respondents before and after the
election which allows to precisely study the social-desirability bias when the same voter
change the response after the result of the election is known. This represents an unique
opportunity to discover why the traditional polls have failed as pollsters do not normally
share their raw data before re-weighting or sample-balancing [8, 9] and few results have
been performed on the same respondents before and after an election. The raw data of this
pollster ﬁrm have been obtained by exclusive arrangement with the pollster responsible for
conducting the polls of Elypsis (co-author Luciano Cohan) who has later founded his own
company (Seido).
We ﬁnd that a poor demographic representation combined with the inconsistency of
opinion’ respondents before and after the elections are the main reasons of the polls failure.
We ﬁnd a large mis-representation of the sample in the surveys as compared with the voting
population, which in Argentina is the general population since voting is obligatory and voter
turnout is quite high at +80%. Even after re-weighting, this large sample bias produces
highly inaccurate results since important segments of society are highly underrepresented in
the polls. Beyond this sampling problem, the main problem we ﬁnd is a clear tendency for
the respondents to not tell the truth about their preference for a candidate (Fernandez) who
was controversial and highly underdog in all polls and the media. This social-desirability
bias was the main culprit for the failure of the polls.
To overcame these problems, we propose an AI model to predict electorate trend using
opinions extracted from social media like Twitter. By using machine learning ﬁrst developed
in [17] we uncover political and electoral trends without directly asking people what they
think, but trying to predict and interpret the enormous amount of data they produce in
online social media [17, 18, 33, 34]. Thus, these big-data analysis overcomes the low response
6


---

rate problem. By re-weighting the Twitter populations to the Census data, we match the
distribution of the population’ statistics and the statistics of the real population (given by the
Census Bureau) [31] thus minimizing the sampling bias of Twitter. Since social media users
freely express their opinions in social media and our methods are not interventionist, the
data are, in principle, free of social-desirability bias. The real time data processing which
underlies our AI algorithm allows us to detect sudden change of opinions, and therefore
diﬀerent loyalty classes towards each candidate.
We will show that a cumulative longitudinal analysis tracking users over time performed
on the loyalties classes to the candidates considerably improves previous results of [17], based
on instantaneous predictions. Instantaneous predictions, as well as pollsters predictions, are
subject to high ﬂuctuations which undermine the reliability of the prediction itself. Instead,
here we show that taking into account the cumulative opinions of users over a long period
of time produces a reliable predictor of people’s opinion. These improvements allow us to
obtain an accurate prediction on a diﬃcult election, which dodged all pollsters in Argentina.
Thus, we validate the algorithm on the primary and general election in Argentina. Our
results in this particular case show that AI can capture the public opinion more precisely
and more eﬃciently than traditional polls.
I.
WHY POLLSTERS ARE FAILING TO PREDICT ELECTIONS?
The events leading up to the recent primary election in Argentina are a telling example
of the failure of the polling industry [32, 35, 36]. On the primary election day on August
11, 2019 (called PASO in Spanish: Primarias, Abiertas, Simult´aneas y Obligatorias; in
English: Open, Simultaneous, and Obligatory Primaries), none of the pollsters in the country
predicted the wide 16% margin of presidential candidate Alberto Fern´andez (AF) over the
president Mauricio Macri (MM) [We clarify that primaries in Argentina are obligatory,
happening for all political parties at the same time, and the two main parties presented only
one candidate each, thus transforming the primaries into a de-facto presidential contest.]
Figure 1 shows the comparison between the oﬃcial results (in red), our prediction (in
blue, Model 3 explained below) and the polling average, computed as the average of the
top ﬁve most trusted pollsters in Argentina [32, 36], i.e. Real Time Data, Management &
Fit, Opinaia, Giacobbe and Elypsis (in green). Macri was clearly defeated by Fernandez by
7


---

+16%, a result captured by our predictions. While the average pollster predicted Fernandez
with a slight advantage in the primary, the estimated percentage of each candidates were, in
general, really close reaching in some occasion a diﬀerence of just one percentage point [37].
Elypsis in particular predicted that Macri would win for one percentage point [38]. This
virtual tie predicted by the pollsters was largely considered to be a win for the incumbent
candidate Macri since he was supposed to gain all the votes left by the third party options
in the subsequent presidential election and eventually win the election in a runoﬀ.
It is worth to stress at this point that Macri (right-leaning candidate) made of the in-
ternationalization of the market one of the main points of his campaign (favoring foreign
investors and pro-business) while Fern´andez (left-leaning candidate) was instead supporting
a national market. As a result of the predictions supported by all Argentinian pollsters giv-
ing Macri as the winner, the bond market rose excessively in the days preceding the primary
election. The subsequent defeat of Macri by 16 percentage points at the primaries leads to a
historic collapse of the MERVAL index by 40%, the bond market collapsed and some banks
lost 1 billion dollars in the bet overnight [39, 40].
The failure of traditional polls is not associated with the impossibility of giving the ex-
act right percentage for the candidates, but rather with the impossibility of predicting the
enormous gap between them. The Argentina primaries elections are not the only exam-
ple of pollsters’ failure. Unpredictable results seems to be associated whenever one of the
candidates is a controversial ﬁgure in the political scenario. In Argentina, the eventual vice-
presidential candidate accompanying Alberto Fern´andez was previous Argentinian president
Cristina Fern´andez de Kirchner (CFK), who had faced corruption allegations and judicial
processes and many Argentinians and the traditional media viewed as a controversial and
divisive ﬁgure in Argentina politics [41] and who is usually viliﬁed by the traditional media.
Notorious examples are Trump in the American presidential election of 2016 or Bolsonaro
in the Brazilian general election of 2018. In the case of the Argentina primaries, the pollster
failure led to economic disruption of the country at a national/international level [39].
Below we analyze the raw data of one of the most reliable polls, Elypsis (trusted specially
by the president Macri and international investors [32, 37, 39, 40]) which as all the pollsters
failed to predict the large gap between the two candidates for the primaries elections.
Figure 2a shows the age-gender distribution of the respondents to the survey conducted
by Elypsis immediately before the PASO elections. Elypsis employs a combination of IVR
8


---

of landline numbers complemented with online opt-in samples from Facebook. The vast
majority of these online panels in Argentina, as well as in US, are made up of volunteers
who were recruited online and who received some form of compensation for completing
surveys, such as small amounts of money or frequent ﬂyer miles. Fig. 2b shows the number
of respondents for Fern´andez (light blue), Macri (red) and Third Party (grey) grouped by
age and gender.
The Elypsis sample is peaked around the 50 years old group.
This is
strikingly diﬀerent from the national population statistics obtained from the Argentinian
Census Bureau shown in Fig. 2e.
Elypsis data does not have signiﬁcant coverage among people younger than 30, even
though it has been conducted in Facebook. It shows a heavier tail on the right for older
groups, while the national population (Census Bureau) has a less pronounced peak around
the group of 30 years old and an heavier tail on the left for younger groups. The largest
sampled group surveyed by Elypsis are females between 51 and 65 years old who are over-
whelming in favor of Macri. In fact, in all groups above 30 years old, Macri is the clear
favorite in the Elypsis poll. On the contrary, Twitter represents better the younger gener-
ations. It is important to consider again that the vote is obligatory in Argentina and it is
permitted above 16 years, and the turnout of the youngest is quite substantial, thus, any
pollster that does not capture their preferences is, in practice, doomed to fail.
To deal with the mis-representation problem, pollsters adjust their raw results to pop-
ulation benchmarks distributions given by the Census Bureaus [1, 4] by weighting the raw
data (sample-balancing or raking [8, 9]). The poll sample is weighted so it matches the
population on a set of relevant demographic or political variables, for instance, age, gender,
location and other socio-economic variables, like education level or income. Studies of the
eﬀectiveness of various weighting schemes suggest they reduce some (30 to 60%) of the er-
ror introduced by the biased sample, see [1]. However, when the raw data distribution is
drastically under/over sampled as the Elypsis case, a small error in the most representative
groups would propagate to produce inaccurate result.
As discussed above, the mis-representation is not the only problem which traditional
pollsters methods face. Next, we analyze the longitudinal data taken on the same 1,900
respondents by Elypsis before and after the elections to investigate the social-desirability
bias. We start with Fig. 3a showing the Elypsis respondent distributions after PASO (notice
that these respondents from the previous one, and this is the reason why the age distribution
9


---

change respect to the previous ﬁgure). By comparing Fig. 2a before PASO with Fig. 3a
after PASO we ﬁrst notice a change in the voters distributions. Younger groups are better
represented after the election when compared to Fig. 2a, although the data are still highly
biased towards older generations. This implies that younger groups were, at least, more
prone to answer the polls after the election than before.
Surprisingly, the female group with ages between 30 and 50 years voted for Fern´andez as
indicated after the PASO polls, while before the PASO they responded mainly in favor of
Macri. The male group of the same age shows a similar behavior, even if less pronounced.
Let us notice that, according to Fig. 2b, the groups of females/males between 30 and 50
years old are the most represented in the Census data and therefore may have an higher
impact on the ﬁnal result. These results can only be explained by admitting that voters did
not say the true.
This is further corroborated by this unique longitudinal panel, as seen in Table I, revealing
that people lied and hid their true voting intentions to the pollsters before the elections.
More speciﬁcally, when comparing “Who are you going to vote in the PASO” with “Who did
you vote in the PASO” - using the same sampling and postratiﬁcation methodology than in
the Pre-PASO survey - it is found that about 18% of the people did not disclose their true
vote, and the hidden vote was not unbiased.
• 91% of those who said “I will vote for Fernandez” did so, but only 83% in the case of
Macri, who lost 6% to AF.
• “Secondary candidates” voters were much more volatile, Only 56% of those who said
that they were going to vote for (third candidate) Lavagna disclosed their true vote,
and 54%, 53% and 59% in the case of other candidates Del Ca˜no, Espert and Gomez
Centurion respectively.
• Alberto Fern´andez got almost 19% of the votes of those who chose a secondary candi-
date in the Pre Paso Poll, and Mauricio Macri only 9%.
• Alberto Fern´andez received 46% of the votes of those who answered ”Blank, Null or
Unknown” before the PASO.
But, who hid - or not disclosed - their real vote? We ﬁnd no signiﬁcant diﬀerence between
men and women or between education levels but we see a clear pattern in age demographics.
10


---

33% of those between 16 and 30 years changed their vote vs. their Pre PASO answer and
only 13%, 10% and 14% on those between 31 and 50, 51 and 65 and more than 65, see Table
II.
What did those who did not disclose their vote think about the candidates?
Where
they ”closeted Kirchnerists” (party of AF and CFK) or did they bridge the gap between
Macri-Fern´andez?
”Regular” images of Cristina Fern´andez, Macri and Alberto Fern´andez were much lower
among those that did reveal their vote than among those who did not, see Table III. Those
who hid their votes look more nonpolarized, with a ”Regular” image - No positive nor
negative - of 21% on average, vs 6%/10% of those who revealed the vote. CFK’s negative
image is higher than MM (48% vs 38%) in ”non-revealers” and the opposite hold in the
revealers (43% vs 50%). 35% of the ”non-revealers” did not have (or hid) their opinion of
Alberto Fernandez vs. 8% in the revealers.
This combined information shed light on PASO results and Polls consensus miss. In the
PASO, AF was able to catch votes from all the candidates, and seduce voters from within
the gap, ”moderate” voters who had a negative image of CFK and MM. He succeeded in
standing himself as the ”third candidate” bridging the gap, something that was not being
fully captured by the polls, or that was decided at the last minute. This feature is most
striking in young people, who may both have more ”volatile” opinions and less prone to
reveal them on traditional polls.
This hidden-vote factor can explain by itself as much as 10% diﬀerence between ”ex-ante”
forecast and real results. Thus, standard polls methods failure may not have been related
only to a bias in the sampling but, in the extraction of ”True” information from surveyed
people.
Understanding why people lie is not the topic of this work even if, according to the liter-
ature the reasons could be many and related to desirability-bias. On one hand, participants
may typically rush through the surveys to obtain their rewards and don’t respond thought-
fully [4]. On the other hand, social-desirability bias [11, 12], i.e. the tendency of survey
respondents to answer questions in a manner that will be viewed favorably by others [4, 12]
is another reason for people to hide their preference for controversial candidates like CFK,
which leads to biased results.
In view of how the above issues of low response rate, mis-representation and the social
11


---

desirability bias/lies (which in the case of Elypsis biased more the younger representative)
undermined the predictions on the Argentinian primary elections, we next search for suit-
able replacement using sampling methods for the modern era of big-data science. In this
scenario, a good candidate to substitute traditional polls is social media (Twitter in our
study) which solves in one shot both the law response rate (million of people express their
political preferences in the microblogging platform) and the social desirability biases. This
is because social media users do not answer to any question, but freely express their ideas
in a social medium platform. However, one may argue that Twitter is generally bias to-
wards young people thus providing a biased sample. Thus, proper re-weighting of the data
is needed, although the eﬀects of re-weighting are expected to be less pronounced than in
the polls of Elypsis. Below we introduce an AI model that builds up on previous work in
[17] combining machine learning, network theory and big-data analytic techniques, that is
able to overcome the problems presented so far and that correctly predicted the outcome of
the 2019 Argentina primary and general elections.
II.
METHODOLOGY
The algorithm we propose improves upon previous work from [17] and consists of four
phases (see Fig. 4): data collection, text and user processing, tweets classiﬁcation with
machine learning and opinion modeling. While the ﬁrst two phases are of standard practice in
the literature, tweets classiﬁcation by means of ML models only recently took place [17, 18],
given the impossibility to classify by hand millions and millions of data. Opinion modeling,
the core of our election prediction model, is an attempt to instantly capture people’s opinion
through time by means of a social network. To improve upon [17], we consider the cumulative
opinion of people and deﬁne ﬁve prediction models based on diﬀerent assumptions on the
loyalty classes of users to candidates, homophily measures and re-weighting scenarios of the
raw data. Below we explain each phase, highlighting the steps that make our full-ﬂedge AI
predictor a good candidate substitute for the traditional pollster methods.
Data collection. By means of the Twitter public APIs, we collected tweets from March
1, 2019 until October 27, 2019, ﬁltered according to the following queries (corresponding
to the candidates’ name and handlers of the 2019 Argentina primary election): Alberto
AND Fernandez, alferdez, CFK, CFKArgentina, Kirchner, mauriciomacri, Macri, Pichetto,
12


---

MiguelPichetto, Lavagna. Only tweets in Spanish were selected. Figure 5a shows the daily
volume of tweets collected (brown line) while Fig. 5b shows the daily number of users (green
line). In blue we report the daily number of tweets/users which are classiﬁed, i.e. they posted
at least one classiﬁed tweet. Users are classiﬁed with machine learning as supporters of Macri
(Fig. 5d, red line) if the majority of their daily tweets are classiﬁed in favor of Macri (Fig.
5c, red line) or as supporters of Fern´andez in the other way around (blue line in Fig. 5d
and c). Hereafter we use FF to indicates the Fern´andez-Fern´andez formula and with MP we
refers to the Macri-Pichetto formula (the outgoing president/vice-president candidate).
The activity of tweets/users shows a peak on August 11, 2020, i.e. the day of the primary
election. In the period from March to October, we collected a daily average of 282,811 tweets
posted by a daily average of 84,062 unique users. We daily classiﬁed 75% of these tweets
and ∼76% of the users ( see Table VIII and Table VII in the Supplementary Information
). In total, by the end of October we collected around 110 million tweets broadcasted by
6.3 million users. This large amount of tweets collected has no precedent and is relevant in
the light of considering that Argentina is one of the most tweeting per capita countries in
the world.
User and text processing. Below we explain the tasks that need to be applied to the
raw data before any analysis is performed.
Bots detection. The identiﬁcation of software that automatically injects information in
the Twitter’ system, is of fundamental importance to discern between “fake” and “genuine”
users [30], the latter representing the real voters. According to [17] a good strategy is to
extract the name of the Twitter client used to post each tweet from their source ﬁeld and
kept only tweets originating from an oﬃcial Twitter client. Figure 6a and b show the daily
number of tweets posted by bots and the daily volume of bots, respectively. Figure 6c and
d show the daily volume of classiﬁed tweets/bots. The daily average of bots between March
and October is 732 with an overall daily activity (in average) of 2,243 tweets. The daily
classiﬁed tweets are 1,617 while the daily classiﬁed bots are 560 bots. As for “genuine” users,
a bot is classiﬁed if it share at least 1 classiﬁed tweet. In the entire dataset we found around
20,000 bots which posted 538,350 tweets. Let us notice that even though we classiﬁed the
bots, they are not used for the ﬁnal prediction since they do not corresponds to real voters.
Text standardization. Stop words removal and word tokenization are of common practice
in Data mining and Natural language processing (NLP) techniques [43, 44]. For example,
13


---

we keep the URLs as tokens since they usually point to resources determining the opinion
of the tweet, through replacing all URLs by the token “URL”.
Tweets classiﬁcation. To build the training set we analyze the hashtags in Twitter.
Users continuously labels their tweet with hashtags, which are acronyms able to directly
transmit the user feeling/opinion toward a topic. We hand labeled the top hashtags used in
the dataset (see Table IX in the Supplementary Information ). They are classiﬁed either as
pro M(acri), F(ern´andez) or T(hird party) candidate, depending on who they support (with
Third party we refer to the supporters of Lavagna, Espert and other secondary candidates).
Hashtag co-occurrence network. In order to check the quality of the classiﬁcation of the
classiﬁed hashtags we build the hashtag co-occurrence network H(V, E) and statistically
validate its edges [17, 45]. In the co-occurrence network the set of vertices v ∈V represents
hashtags, and an edge eij is drawn between vi and vj if they appear together in a tweet.
We test the statistical signiﬁcance of each edge eij by computing the probability pij (p-value
of the null hypothesis) to observe the corresponding number of co-occurrences by chance
only knowing the number of occurrences ci and cj of the vertices vi and vj, and the total
number of tweets N. Fig. 7 shows the validated network. We only keep those edges with a
p-value p < 10−7. The blue community contains the hashtags in favor of Fern´andez, the red
community those in favor of Macri and the green one (a very small group) are those in favor
of the Third candidate. A look at the typologies of hashtags reveals the ﬁrst diﬀerences in the
supporters. Those in favor of Cristina Kirchner are much more passionate than the follower
of Macri. For example, Kirchner’s type of hashtags are #FuerzaCristina, #Nestorvuelva,
#Nestorpudo or they are very negative to Macri as #NuncamasMacri. On the other hand,
Macri’s group is smaller and less passionate with hashtags like #Cambiemos or #MM2019
(see Fig. 8), while support for the third candidate has not taken traction and its electoral
base on Twitter is very small.
In principle, counting the users and tweets according to the hashtags they use would
predict the victory of Fern´andez over Macri. However this conclusion would be based only
on ∼10,000 users (those expressing their opinion through hashtags). In order to get the
opinion of all the users we train a machine learning model that classiﬁes each tweet as
AF, MM or Third party. (In what follows we also refer to the formulas FF for Fern´andez-
Fern´andez and MP for Macri-Pichetto, the ﬁnal formulas in the presidential contest). We
use the previous set of hashtags expressing opinion to build a set of labeled tweets, which
14


---

are used in turn to train a machine learning classiﬁer. We use all the tweets (before August)
which contain at least one of the classiﬁed hashtags to train the model. In the case of more
than one hashtag for a tweet, we consider it only if all the hashtags are in favor of the same
candidate. The use of hashtags that explicitly express an opinion in a tweet represents a
“cost” in terms of self-exposition by Twitter users [46] and therefore allows one to select
tweets that clearly state support or opposition to the candidates. The training set consists
of 228,133 tweets, i.e. the 0.33% of the total amount of collected tweets and the ∼90%
of the hand-classiﬁed tweets (253,482 tweets). In order to ﬁnd the best classiﬁer we used
ﬁve diﬀerent classiﬁcation models, the logistic regression (LR) with L2 regularization, the
support vector machine model (SVM), the Naive Bayes method (NB), the Random Forest
(RF) and the Decision Tree (DT). All these models are validated on the remaining 10%
of the classiﬁed tweets (25,349). Table IV shows the results for the models. The logistic
regression performs better than the other models with an average group accuracy equals
to 83%. Also recall and F1-score are equal to 83%. Support Vector Machine is the second
classiﬁed, with an average accuracy of 81%. It follows the Naive Bayes with and average
accuracy of 79.5%, the Random Forest and the Decision Tree.
We recall that the logistic regression assigns to each tweet a probability p of belonging to
a class. In our case such probability goes to one if the tweet supports Macri while it goes zero
if it supports Fern´andez. As it is shown in Fig. 9 the distribution of p contains two peaks,
one on the left and one on the right, divided by a plateau. This is an encouraging result,
since it proofs the eﬃcacy of the model to discern between the two classes. We classify a
tweet in favor of Macri if p ≥0.66, in favor of Fern´andez if p ≤0.33. Tweets with a value of
p in the plateau are instead unclassiﬁed, meaning that the tweet does not contain suﬃcient
information to be classiﬁed in either camp. According to this rule, in average we classify
211,229 genuine tweets and 1,617 “fake” tweets per day (see Table VIII and Table VII in
the Supplementary Information ).
Opinion modeling. We can infer users’ opinion from the majority of the tweets they
post. Let nt,F be the number of tweets posted by a given user at time t in favor of Fern´andez
and let nt,M be those supporting Macri. We deﬁne an instantaneous opinion over a window
of length w and a cumulative average opinion as follow. In the ﬁrst case, a user is classiﬁed
as a supporter of Fern´andez (at a given day t = d) if Pd
t=d−w+1 nt,F > Pd
t=d−w+1 nt,M,
i.e if the majority of the tweets posted in the last w days were in favor of Fern´andez.
15


---

The user is classiﬁed as a supporter of Macri if Pd
t=d−w+1 nt,F < Pd
t=d−w+1 nt,M. If none
of the previous conditions is met, i.e.
if Pd
t=d−w+1 nt,F = Pd
t=d−w+1 nt,M then the user
is classiﬁed as undecided.
Let us notice that when w goes to one we have the ‘most’
instantaneous prediction, that is the prediction based on what people think in the last
day. This instantaneous prediction model was used in Ref. [17] to match the results of the
AI model to the aggregate of polls from the New York Times in the 2016 US election with
excellent results. However, this predictor did not match the results of the electoral college,
which required stratiﬁcation by states. Thus, we further develop the AI model of [17] to add
other predictors beyond the instantaneous measures.
Traditional polls’ data collection is an instantaneous prediction with a value of w that
can go from few days up to few weeks, which is the time of collection of the poll data and
this corresponds roughly to our instantaneous measurement above. However, the fact that
we are able to track the same user over long period of time in Twitter allows us to extend
the window of observation as far as we want to then deﬁne a new measure that we call the
cumulative opinion. The cumulative opinion in our model is deﬁned by extending w to the
initial date of collection for every time d of observation, i.e., w = d, thus considering the
opinion of a user based on all the tweets he/she posted from time t = 0 upto the observation
time d. That is, our prediction is longitudinal as we are able to follow the opinion of the
same user over the entire period of observation of several months. In terms of traditional poll
methods, a cumulative opinion would be obtained in a panel collecting for each respondent in
the sample and for each day starting from t = 0 her/his preference toward a candidate. This
possibility, which would require an unimaginable amount of eﬀort and time for traditional
poll methods, it is quite straightforward when it come to social media and big-data analyses.
We start by investigating the instantaneous response of the users in a ﬁxed window
of time.
Figure 10a shows the Twitter supporters dynamics over time obtained with a
window average, w = 14 days. Users are classiﬁed as MP (in red), FF (in blue) or Others
(in green). Figure 10b shows the supporters dynamic (thick lines) compared with Elypsis
prediction (thin dashed lines) without considering the undecided users in the normalization.
In the same plots we also report the oﬃcial results for both primaries and general elections.
The comparison between the two pictures stands out as a approximate correlation between
the Elypsis and the AI results for each candidate.
However, in the comparison among
candidates predictions may sometimes diﬀers, as for example, right before the beginning of
16


---

August, Elypsis gave as favorite MP while the AI instantaneous prediction was in favor of
FF. Overall, as for the pollsters results, window average analyses are representative of the
instantaneous sentiment of the people. As we see from the ﬁgures, instantaneous opinions
are aﬀected by considerable ﬂuctuations [17] which make the prediction not reliable. In
Fig. 14 in the Supplementary Information we compare the average window opinion with
other pollsters (Real Time Data, Management & Fit, Opinaia, Giacobbe and Elypsis). An
interpolation (thin lines) shows similar trends as the AI-model window average, stressing
that the conclusions made so far are more general then the simple comparison with Elypsis.
In fact in [17] we have shown that the instantaneous predictions of the AI model follows quite
closely the aggregation of polls obtained from the New York Times, ‘The Upshot’, yet, it
does not reproduce the results of the electoral college which requires a segmentation by states
where proper prediction of rural and non-rural areas becomes the key and considering the
cumulative opinion, not the instantaneous one, opinion of each users is crucial to correctly
predict the elections.
Thus, we next study the opinion of each user by considering the cumulative number of
tweets over the entire period of observation to deﬁne classify the voter’s intention (Model
0). This cumulative approach takes into consideration the all the tweets together for each
user since the ﬁrst time they enter in the dataset and based the voter intention on all of
them. This cumulative approach can only be done with Twitter and not with traditional
polls, except for short times and particular cases as done by Elypsis before and after PASO.
Figure 11 shows the cumulative opinion from March 1 until a few days before the general
elections. We can see that this approach captures the huge gap between the candidates,
both for the primary election and the general election ( vertical lines from the left to the
right). While a low precision is of secondary importance when the diﬀerence between the
opponents is high, it plays a central role when they have a close share of supporters. As
an extreme example, in an almost perfect balanced situation the change of mind of just few
people may ﬂip the ﬁnal outcome. If on the one hand a cumulative approach do reduce the
ﬂuctuations in the signal, it is also less sensitive to sudden change of opinion. A person
can support a candidate until few days before the elections, for then change her/his mind
because of some particular facts. This and other possibilities can be taken into account
only by a model based on cumulative analyses, but able to capture the degree of loyalty
of people towards the candidates over time. Diﬀerently from the traditional surveys, the
17


---

real time data processing that underlies our AI algorithm gives the possibility to take into
consideration this scenario. To understand how diﬀerent re-weighting scenarios aﬀect the
results, below we introduce diﬀerent loyalty classes of users towards the candidates and then
we deﬁne several models matching the criteria previously discussed. These loyalty classes
can be only deﬁned when we consider the cumulative opinion in a longitudinal study and
cannot be investigated by traditional polls.
Loyalty classes.
We deﬁne 5 classes of loyalty for users.
Here we consider the MP
supporters, but the deﬁnitions below similarly applied to the other candidates.
• Ultra Loyal (UL): users who always tweet only for the same candidate, namely
PT
t=T0(
nM,t
nM,t+nF,t+nT,t) = 1.
where with nx,t we indicate the number of tweets that
a given user post in favor of x, with x ∈{ Macri, Fern´andez, Third party}.
Diﬀerently from the ultra loyal, which continuously post in favor of a candidate, the
other classes take into consideration a possible change of opinion of a user. In order to
detect sudden twist of opinions we focus on the classiﬁcations of the last k tweets posted by
the users. We deﬁne:
• Loyal MP →MP: a user which is MP since the majority of tweet are for MP, but she/he
also supported MP in the last k tweets. Mathematically speaking PN
n=N−k nM,n >
PN
n=N−k nF,n + nT,n. N is the total number of tweets posted by the user.
• Loyal MP →FF: users that are MP by the total cumulative count but they have
tweeted for FF in the recent k tweets. In formula: PN
n=N−k nF,n > PN
n=N−k nM,n+nT,n
• Loyal MP →TP: users supporting the third party in the last k tweets, i.e. PN
n=N−k nT,n >
PN
n=N−k nM,n + nF,n.
• Loyal MP →Undecided: all other individuals classiﬁed as MP but not included above.
Let us remind that unclassiﬁed refers to all those users who do not have any classiﬁed
tweet. Fig. 12 shows the cumulative prediction for each class, with T0= March 1, 2019 and
k = 10. The Ultra Loyal class for Fern´andez (FF) represents ∼33% of the populations
while only ∼20% of the populations is Ultra Loyal towards Macri (MP). Loyal MP→MP
and loyal FF→FF represents between the 8% and the 13% of the entire Twitter population.
18


---

The percentage of the undecided is around 8% and the third party percentage. The other
classes are close to 1 or 2%. In the next section we use these classes in order to deﬁne a
better predictor.
AI Models. The loyalty classes introduced so far are one of the main diﬀerences with
the other Twitter based studies: we use the machine learning classiﬁer (logistic regression
here) to deﬁne the loyalty of a user and not to make predictions. We do that by grouping
supporters as follows:
• Fern´andez supporters: all those users which are ultra loyal FF, loyal FF→FF, loyal
FF→MP, loyal FF →Undecided.
• Macri supporters: all those users which are ultra loyal MP, loyal MP→MP, loyal
MP→FF, loyal MP→Undecided.
In each group we put those users we are almost sure who they support because of their
activity over time.
However, as we saw in the previous section, undecided may play a
central role in a scenario where few percentage points can ﬂip the ﬁnal result. Furthermore,
understanding unclassiﬁed users (i.e. those users which do no not have any classiﬁed tweet)
will also improve the ﬁnal statistic. In order to take into account all the reasonable scenario
we deﬁne three diﬀerent models (starting from the classiﬁcation in Fern´andez and Macri
of above) and validate them against the ﬁnal results of the election. Table V resumes the
details of each model.
Model 1: All the users belonging to one of the following classes are grouped in the third
party: Undecided→MP, Undecided→FF, Undecided→Undecided and Unclassiﬁed.
Model 2: Instead of simply grouping the undecided in a third party, we use network
homophily to infer their political orientation.
A user is classiﬁed as MP(Undecided) if
the majority of her/his neighbors (in the indirected retweet network) support Macri. The
same deﬁnitions applied for the other cases. In this model, FF(Undecided) are considered
supporters of Fern´andez and MP(Undecided) supporters of Macri. Undecided(Undecided)
and Unclassiﬁed belong to the third party.
Model 3: We use network homophily to determine the political orientation of both
undecided and unclassiﬁed users. FF(Undecided) and FF(Unclassiﬁed) are considered sup-
porters of Fern´andez and MP(Undecided) and MP(Unclassiﬁed) supporters of Macri. Un-
decided(Undecided), Unclassiﬁed(Unclassiﬁed) belong to the third party, see Fig 13.
19


---

In the next section we compare the performances of these models on the Argentina
election.
III.
AI-BASED FORECAST FOR THE ARGENTINIAN ELECTION
The models introduced so far allow us to deﬁne the daily supporters of each candidate
according to their retweet activity. Indeed supporters are deﬁned not simply according to
the classiﬁcation of the majority of their retweet, but on the basis of the loyalty classes
they belong. Similarly to the simple tweets classiﬁcation, we can deﬁne for each model an
instantaneous (window average) and a cumulative (average) opinion.
Fig. 10 shows that an instantaneous indicator provides an approximate ﬁtting to the
results of polls. We have already used this indicator, in our previous study of the 2016
US presidential election, to precisely ﬁt the New York Times Aggregator of Polls at The
Upshot’ [17, 47]. This aggregator uniﬁes a thousands polls and weight them with proprietary
information to produce a weighted average of all the most trustable pollster in USA. While
this analysis is interesting and give the opportunity to predict instantaneous changes in
electoral opinion, this indicator does not provide the electorate opinion as a whole and it is
not the most important predictor of the election outcome. It is not the greatest information
that can be extracted from social networks, either, and indeed, it failed to predict the US
2016 election and the present Argentina 2019.
The estimator that predictor better the
election is provided when we consider the cumulative number of users from the beginning of
measurements, and not just the behavior of the users in a small window of observation.
For this reason here we directly focus on the cumulative prediction for the models intro-
duced in the previous section. Table VI reports the prediction of each model right before
the day of the general election day: October 27, 2019. The oﬃcial results saw the victory
of Fern´andez with 48.24%. Macri scored 40.28% and the Third Party with 19.48%. The
average predictions obtained by averaging the results of the ﬁve models are consistent (in-
side the standard error) with the oﬃcial outcome. Indeed, we obtain (49.3 ± 2.1)% for FF,
(36.8 ± 2.9)% for MP and (13.9 ± 4.8)% for the Third Party. This in an outstanding result
which highlights the importance of considering loyalty classes for Political elections. In order
to establish the best among the ﬁve models we compute the mean absolute error between
each model’ prediction and the ﬁnal results. Let Y = {yc} with c ∈{FF, MP, TP} be the
20


---

prediction of one model and let X = {xc} with c ∈{FF, MP, TP} be the oﬃcial results.
We deﬁne the MAEi (mean absolute error) for model i as
P
i∈c(|xi−yi|)
3
.
Table VI shows the MAE for each model. Model 3, based on the homophily detection for
the undecided is the best predictor with a mean absolute error of 0.53. This model predicted
48.9% for FF (an overestimation of 0.66 points if compared to the oﬃcial result), 39.6% for
MP (an underestimation of 0.68 points) and 11.6% for the Third Party. As a matter of fact,
the AI model introduced so far is capable of predicting the Argentinian general elections, by
giving a percentage of electors for each candidate close to the oﬃcial one and outperforming
traditional polls methods. See Fig. 1b.
Maybe the most important result is the performance of our algorithm before the PASO,
where all the pollsters failed too predict the +16% points diﬀerence between the two can-
didates (by strongly underestimating their gap). Model 3 predicts a diﬀerence of almost
18% points in favor of FF, close to the oﬃcial result.
While the PASO results appears of secondary importance, they play a central role in
the Argentina political campaign and they are the most diﬃcult to guess because it’s the
ﬁrst time the citizens oﬃcially expressed their opinion on the election. Figure 1 shows how
traditional pollsters modiﬁed their prediction after the primary elections, somehow ﬁtting
them with the PASO results. How they modiﬁed their predictions is still not clear and some
of the pollsters (Elypsis for example) did not release any prediction after the PASO.
A study of the hashtags and queries of the followers of the FF formula indicates that
the vast majority of the people focused more on the poor economic situation in which the
country was instead of the judicial cases of corruption that aﬀect the FF candidates. Most
of the hashtags reﬂect sentiment of hunger, chaos, crisis and despair. On the other hand,
the expression of the followers of Macri-Pichetto is reﬂected in hashtags to give strength to
the president but they do not reﬂect a feeling for the economic and political situation, but
more a moral support, perhaps of resignation. The followers of Macri do not express too
much their concerns about judicial cases of corruption either.
Finally, let us notice that the cumulative average depends on the initial time T0. This
value determines the initial ﬂuctuations of the cumulative average, which generally stabilize
into a value that it is diﬃcult to change unless a big swing in opinion of the electorate. To
investigate this eﬀect, we have recalculated the cumulative average by changing the origin of
measurement T0 in Fig. As we see from this ﬁgure, the predictions for the general elections
21


---

cluster around the same value. We use this ﬂuctuations to compute the error associate to our
ﬁnal predictions. We deﬁne the error as the standard deviation over the results of diﬀerent
realizations with t < T0. Regarding Model 3, the estimated average error is 0.53%. This
result strengths the goodness of our prediction, consistent, inside the error bars, with the
ﬁnal results.
IV.
CONCLUSION
One of the fundamental tools of artiﬁcial intelligence in social networks is that it captures
changes in people’s opinions without any intervention and for an extended time. Then AI
can capture the sentiment of the millions of users who constantly express themselves on the
internet and change or maintain their positions. AI can also ﬁlter this information from ma-
nipulators and bots and can reduce it to its essence, by overcoming the problems traditional
pollsters face: low response rate, social desirability biases and the mis-representation of the
population.
The results of our analyses show that AI applied to big-data can be used to successfully
understand people’ opinions over time. The possibility of following the opinion of the same
people through time, and therefore the chance of deﬁning loyalty classes is a fundamental step
in order to make good predictions. AI allows both to get the percentage of supporters toward
a candidate and reveals what is behind these numbers, giving an idea of people sentiments.
This is of particular importance when one of the candidates is a controversial politician
and can generate diﬀerent feelings leading to strong polarization and biased responses to
pollsters, which are not trusted anymore by the great majority of people.
We expect that in the future traditional surveys may be incrementally replaced by these
new non-intrusive methods. AI is a thermometer that provides the key to predicting not
only the elections but the great trends that develop at the local and global levels. We have
shown how AI allows to synthesize the opinion of millions of people including those silent
majorities of hidden voters who would not be heard otherwise. We must not ignore that
people are tired of answering surveys. AI can then deduce, predict, interpret and understand
what people want to express.
22


---

Acknowledgements: GC acknowledges support from EU project, HUMANE-AI-NET
(grant number 952026). HAM owns shares of Kcore Analytics.
23


---

Fernandez
Macri
Others
0
10
20
30
40
50
%
Primary election
Oﬃcial results
AI Predictions
Polling average
(a)
Fernandez
Macri
Others
0
10
20
30
40
50
%
General election
Oﬃcial results
AI Predictions
Polling average
(b)
FIG. 1. Comparison between polling average (green), oﬃcial results (red) and our prediction (blue)
for both the (a) Primary (2019-08-11) and the (b) General election (2017-10-27).
24


---

female 16-29
male 16-29
female 30-49
male 30-49
female 50-64
male 50-64
female >=65
male >=65
0.00
0.05
0.10
0.15
0.20
0.25
0.30
(a)
(>16, <=30, Female, FF)
(>16, <=30, Female, MP)
(>16, <=30, Female, Others)
(>16, <=30, Male, FF)
(>16, <=30, Male, MP)
(>16, <=30, Male, Others)
(>30, <=50, Female, FF)
(>30, <=50, Female, MP)
(>30, <=50, Female, Others)
(>30, <=50, Male, FF)
(>30, <=50, Male, MP)
(>30, <=50, Male, Others)
(>51, <=65, Female, FF)
(>51, <=65, Female, MP)
(>51, <=65, Female, Others)
(>51, <=65, Male, FF)
(>51, <=65, Male, MP)
(>51, <=65, Male, Others)
(>65, Female, FF)
(>65, Female, MP)
(>65, Female, Others)
(>65, Male, FF)
(>65, Male, MP)
(>65, Male, Others)
0
100
200
300
400
500
600
(b)
female 15-29
male 15-29
female 30-49
male 30-49
female 50-64
male 50-64
female >=65
male >=65
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
Proportion
Census
(c)
FIG. 2.
(a) Elypsis demographics before PASO. (b) Elypsis polling results before PASO separated
by age and gender (Macri=red, Fern´andez= blue, Others=grey). Results are highly biases to older
than 50 as compared with Census distribution. (c) Argentina Census Bureau 2010 demographic
distribution by age and gender.
25


---

female 16-29
male 16-29
female 30-49
male 30-49
female 50-64
male 50-64
female >=65
male >=65
0.00
0.05
0.10
0.15
0.20
0.25
(a)
(>16, <=30, Female, FF)
(>16, <=30, Female, MP)
(>16, <=30, Female, Others)
(>16, <=30, Male, FF)
(>16, <=30, Male, MP)
(>16, <=30, Male, Others)
(>30, <=50, Female, FF)
(>30, <=50, Female, MP)
(>30, <=50, Female, Others)
(>30, <=50, Male, FF)
(>30, <=50, Male, MP)
(>30, <=50, Male, Others)
(>51, <=65, Female, FF)
(>51, <=65, Female, MP)
(>51, <=65, Female, Others)
(>51, <=65, Male, FF)
(>51, <=65, Male, MP)
(>51, <=65, Male, Others)
(>65, Female, FF)
(>65, Female, MP)
(>65, Female, Others)
(>65, Male, FF)
(>65, Male, MP)
(>65, Male, Others)
0
50
100
150
200
250
300
350
(b)
FIG. 3.
(a) Elypsis demographics after PASO. (b) Elypsis polling results after PASO separated
by age and gender (Macri=red, Fern´andez= blue, Others=grey).
Tweets
collecting
User DQGWH[W
preprocessing
Opinion 
modeling
Tweets
classiﬁcation
Election 
Prediction
Results
Population
reweighting
Network 
homophily 
Applying
Adjusting
FIG. 4. The ﬂow of election prediction algorithm.
26


---

Who will you vote?
Who did you vote?
Was Pre PASO vote true?
AF-CFK MM-MP Other Yes
No
AF-CFK
91%
2%
8%
91%
9%
MM-MP
6%
83%
11% 83%
17%
Lavagna
19%
9%
72% 56%
44%
Del Cano
25%
0%
75% 54%
46%
Espert
19%
14%
67% 53%
47%
Gomez Centurion
10%
8%
83% 69%
31%
Blank or Null
23%
4%
73% 47%
53%
Unknown or Others
53%
11%
36%
TABLE I. Vote disclosure analysis: “Who are you going to vote in the PASO” with “Who did
you vote in the PASO” - using the same sampling and post-stratiﬁcation methodology than in the
Pre-PASO survey [42].
Revealed Not Revealed
Man
83%
17%
Woman
81%
19%
Between 16 and 30
67%
33%
Between 31 and 50
87%
13%
Between 51 and 65
90%
10%
More than 65
89%
11%
Full Secondary
81%
19%
Incomplete Secondary
81%
19%
Full or incomplete Univ.
86%
14%
Total
82%
18%
TABLE II. Hidden vote by demographics [42].
27


---

Image % of the total
Revealed
Not Revealed
Positve Negative Regular NS/NC Positve Negative Regular NS/NC
CFK
45%
43%
6%
5%
20%
48%
22%
11%
MM
36%
50%
10%
4%
26%
39%
21%
14%
AF
45%
39%
7%
8%
15%
28%
28%
35%
TABLE III. CFK, AF, and MM Image as % of the total [42].
28


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
0.25
0.50
0.75
1.00
1.25
1.50
n° of tweets
×106
Classiﬁed tweets
Collected tweets
(a)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
1
2
3
4
n° of users
×105
Classiﬁed users
Collected users
(b)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
1
2
3
4
5
6
n° of tweets
×105
FF
MP
(c)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
0.25
0.50
0.75
1.00
1.25
1.50
n° of users
×105
FF
MP
(d)
FIG. 5. (a) Daily volume of collected (brown line) and classiﬁed (green line) tweets. (b) Daily
volume of collected (brown line) and classiﬁed (green line) users. (c) Daily tweets supporting the
FF/MP formula. (d) Daily users supporting the FF/MP formula.
29


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
2
4
6
8
n° of tweets
×103
Classiﬁed tweets
Collected tweets
(a)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
0.5
1.0
1.5
2.0
n° of users
×103
Classiﬁed users
Collected users
(b)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
0.5
1.0
1.5
2.0
2.5
3.0
n° of tweets
×103
FF
MP
(c)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
2
4
6
8
n° of users
×102
FF
MP
(d)
FIG. 6.
Bots analysis: (a) Daily volume of collected (brown line) and classiﬁed (green line)
tweets.
(b) Daily volume of collected (brown line) and classiﬁed (green line) users.
(c) Daily
tweets supporting the FF/MP formula. (d) Daily users supporting the FF/MP formula.
30


---

FIG. 7. Hashtag co-occurrence network from March to August 2019. In blue the hashtags in favor
of Alberto Fern´andez and Cristina Fern´andez de Kirchner, in red the hashtags in favor of Macri
and in green those in favor of the Third party.
31


---

(a)
(b)
FIG. 8. Hashtag clouds. The dimension of the words is proportional to their frequency in the
dataset. (a) The blue hashtags are the most frequently used in the tweets in favor of Fern´andez.
(b) The red hashtags are those in favor of Macri.
32


---

Model Precision (FF) Recall (FF) F1 (FF) Precision (MP) Recall (MP) F1 (MP)
LR
0.83
0.83
0.83
0.83
0.83
0.83
SVM
0.81
0.81
0.81
0.81
0.80
0.81
NB
0.79
0.80
0.80
0.80
0.79
0.80
RF
0.74
0.80
0.77
0.79
0.72
0.75
DT
0.76
0.76
0.76
0.76
0.76
0.76
TABLE IV. Performance of the classiﬁcation models: Logistic Regression (LR),Supporting Vector
Machine (SVM), Naive Bayes (NB), Random Forest (RF) an Decision Tree (DT).
33


---

0.0
0.2
0.4
0.6
0.8
1.0
p
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
P(p)
FIG. 9. Probability distribution of p = probability of voting for Macri (p = 0 corresponds to
Fern´andez) obtained by the Logistic Regression model.
34


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
10
20
30
40
50
%
FF (AI)
MP (AI)
Others (AI)
(a)
2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
30
40
50
60
70
%
FF
MP
FF (Elypsis)
MP (Elypsis)
(b)
FIG. 10. (a) Instantaneous prediction of the AI model obtained in a moving window of w=14
days. Vertical lines are ( from the left to the right ) the day of the primaries and general elections
respectively. The circles represents the oﬃcial results for the primaries while the stars those for
the general elections. (b) Previous results compared with polls from Elypsis. Thick lines represent
AI prediction while dashed line represent the Elypsis predictions.
35


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
40
50
60
%
FF
MP
FIG. 11. Simple cumulative predictions obtained without deﬁning the loyalty classes (Model 0).
36


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
date
0
10
20
30
40
%
Ultra loyal FF
Ultra loyal MP
Loyal FF - FF
Loyal FF - MP
Loyal FF - Undecided
Loyal MP - MP
Loyal MP - FF
Loyal MP - Undecided
Undecided
3rd party
FIG. 12. Cumulative users’ opinion for each loyalty class over time.
37


---

2019-03-05
2019-04-14
2019-05-24
2019-07-03
2019-08-12
2019-09-21
2019-10-31
date
10
20
30
40
50
%
FF
MP
Third party
FIG. 13.
Cumulative MODEL 3 prediction of the AI model and comparison with primary on
August 11, 2019 and general election results on October 27, 2019. Model 3 is the best ﬁt to the
real data.
38


---

MODEL 1 Supporters (Users)
FF
Ultra loyal MP, loyal MP→MP, loyal MP→FF and loyal MP→Undecided
MP
Ultra loyal FF, loyal FF→FF, loyal FF→MP, loyal FF →Undecided
Third party Undecided→MP, Undecided→FF, Undecided→Undecided, Unclassiﬁed
MODEL 2
FF
Ultra loyal FF, loyal FF→FF + loyal FF→MP + loyal FF→Undecided, FF(undecided)
MP
Ultra loyal FF, loyal FF→FF, loyal FF→MP, loyal FF →Undecided, MP(undecided)
Third party Undecided(undecided), Unclassiﬁed
MODEL 3
TABLE V. The deﬁnition of three models according opinion modeling.
MODEL
FF (%)
MP (%)
Third party (%)
MAE (%)
1
45.9
32.5
21.6
6.71
2
49.1
34.0
16.8
4.21
3
48.9
39.6
11.5
0.53
TABLE VI. Models’ prediction results for the general election on October 27.
39


---

[1] R. Tourangeau, F. G. Conrad and M. P. Couper, M. P. The Science of Web Surveys. Oxford
University Press, New York, (2013). https://www.aapor.org/AAPOR Main/media/MainSite
Files/Sampling-Methods-for-Political-Polling 1.pdf
[2] C. Durand and A. Blais Quebec 2018: A Failure of the Polls?, Canadian Journal of Polit-
ical Science/Revue canadienne de science politique, 53, 133–150, (2019). (2020).
[3] A. Bekele. Are faulty opinion polls to blame for Brexit?. (2018). Retrieved from https://di
gitalcommons.whitworth.edu/sirc/2018/ie1/6/.
[4] C. Kennedy et al. Ad Hoc Committee on 2016 Election Polling, An Evaluation of 2016 Election
Polls in the U.S. American Association for Public Opinion Research, AAPOR report (2016).
Retrieved from https://www.aapor.org/Education-Resources/Reports/An-Evaluation-
of-2016-Election-Polls-in-the-U-S.aspx.
[5] The Economist.
A new iPhone feature poses a threat to opinion pollsters (2019).
URL
https://www.economist.com/united-states/2019/09/26/a-new-iphone-feature-pose
s-a-threat-to-opinion-pollsters.
[6] J. Jacobs and B. House, Trump Says He Expected to Lose Election Because of Poll Results.
Bloomberg, (2016). Retrieved from https://www.bloomberg.com/politics/articles/20
16-12-14/trump-says-he-expected-to-lose-election-because-of-poll-results.
[7] C. Kennedy and H. Hartig. Response rates in telephone surveys have resumed their decline.
Pew Research Center, (2019). https://www.pewresearch.org/fact-tank/2019/02/27/res
ponse-rates-in-telephone-surveys-have-resumed-their-decline.
[8] M. Battaglia, D. Izrael, D. Hoaglin, and M. Frankel. Tips and Tricks for Raking Survey Data
(a.k.a. Sample Balancing). American Association for Public Opinion Research. JSM, 4740-
4745 (2004).
[9] D. Izrael, D. Hoaglin, and Michael P. Battaglia. A SAS Macro for Balancing a Weighted
Sample. Statistics and Data Analysis, Paper 258-25 (2000).
[10] D. Leonhardt ‘A Black Eye’: Why Political Polling Missed the Mark. Again. Retrieved from
https://www.nytimes.com/2020/11/12/us/politics/election-polls-trump-biden.ht
ml.
[11] J. G. Payne The Bradley eﬀect: Mediated reality of race and politics in the 2008 US presidential
40


---

election. American Behavioral Scientist, 54(4), 417–435, (2010).
[12] I. Krumpal. Determinants of social desirability bias in sensitive surveys: a literature review.
Quality & Quantity. 47, 2025–2047, (2013).
[13] M. Zolghadr, S. A. A. Niaki and S. T. A. Niaki. Modeling and forecasting US presidential
election using learning algorithms. Journal of Industrial Engineering International, Volume
14, pp. 491-500, (2018).
[14] K. Ravi and V. Ravi. A survey on opinion mining and sentiment analysis: Tasks, approaches
and applications. Knowledge-Based Systems, Volume 89, Pages 14-46, (2015).
[15] K. Jaidka et al. Predicting elections from social media: a three-country, three-method compar-
ative study. Asian Journal of Communication, 1-21, (2018).
[16] A. Jungherr Twitter use in election campaigns: a systematic literature review. J Inf Technol
Polit 13(1), 72–91, (2016.)
[17] A. Bovet, F. Morone, H. A. Makse, Validation of Twitter opinion trends with national polling
aggregates: Hillary Clinton vs Donald Trump, Sci. Rep. 8673, (2018).
[18] A. Bovet, H. A. Makse, Inﬂuence of fake news in Twitter during the 2016 US presidential
election, Nature Comm. 10, 7, (2019).
[19] A. Tumasjan et al. Predicting elections with twitter: What 140 characters reveal about political
sentiment. Fourth international AAAI conference on weblogs and social media, (2010).
[20] A. Jungherr et al. Why the pirate party won the german election of 2009 or the trouble with
predictions: A response to Tumasjan, a., sprenger, to, sander, pg, & welpe, im “predicting
elections with twitter: What 140 characters reveal about political sentiment”. Social science
computer review, 30, 329–234, (2012).
[21] M. Gaurav, et al. Leveraging candidate popularity on Twitter to predict election outcome. In
Proceedings of the 7th workshop on social network mining and analysis (pp. 7–16), (2013).
[22] C. Lui et al. On the predictability of the US elections through search volume activity (Report
no. 23). Retrieved from http://repository.wellesley.edu/scholarship/23/, (2011).
[23] A. Bermingham, and A. F. Smeaton. On using Twitter to monitor political sentiment and
predict election results. In Sentiment analysis where AI meets psychology (SAAIP) (pp. 2–10),
(2011).
[24] A. Ceron et al. Every tweet counts? How sentiment analysis of social media can improve our
knowledge of citizens’ political preferences with an application to Italy and France. New media
41


---

& society, 6, 340–358, (2014).
[25] G. Caldarelli et al. A multi-level geographical study of Italian political elections from Twitter
data. PloS one, 9, (2014).
[26] P. Singh et al. Forecasting the 2016 US presidential elections using sentiment analysis. Con-
ference on e-Business, e-Services and e-Society, 412–423, (2017)
[27] P. Singh et al. Can twitter analytics predict election outcome? An insight from 2017 Punjab
assembly elections. Government Information Quarterly, (2020).
[28] M. Newman. Networks: An introduction. New York, NY: Oxford University Press, (2010).
[29] A. Cuzzocrea et al. Edge betweenness centrality: A novel algorithm for QoS-based topology
control over wireless sensor networks. Journal of Network and Computer Applications, 35(4),
1210–1217, (2012).
[30] Y. Wu et al. A novel framework for detecting social bots with deep neural networks and active
learning. Knowledge-Based Systems, Volume 211, 106525, (2021).
[31] L. Bode and K. Dalrymple. Politics in 140 characters or less: Campaign communication,
network interaction, and political participation on Twitter. Journal of Political Marketing, 15,
311–232, (2016).
[32] Clar´ın, 10/12/2019. Retrieved from (in Spanish): https://www.clarin.com/politica/encu
estadoras-fuego-erraron-paso-dicen-octubre 0 T72H9hdl.html.
[33] A. Bovet, S. Pei, F. Morone, H. A. Makse, The Science of Inﬂuencers Using Mathematically
Rigorous Theories - Understanding the Future of Society, Biology, Markets and Ecosystems
(Springer Nature, Switzerland, 2019) forthcoming.
[34] B. Jasny and R. Stone, Prediction and its limits. Science Vol. 355, Issue 6324, pp. 468-469,
(2017).
[35] 2019 Argentine general election. Retrieved from https://en.wikipedia.org/wiki/2019 A
rgentine general election#Opinion polls.
[36] Compilation of Argentina election polls for PASO and general elections. Retrieved from https:
//es.wikipedia.org/wiki/Anexo:Encuestas de intencion de voto para las eleccione
s presidenciales de Argentina de 2019.
[37] Clar´ın, 10/12/2019. Retrieved from (in Spanish): https://www.clarin.com/opinion/intri
gas-casa-rosada-pases-factura-city-lunes-negro 0 jnggAIsh5.html.
[38] Impulso Baires, 10/12/2019. Retrieved from (in Spanish): https://www.impulsobaires.co
42


---

m.ar/nota/275336/bomba-inversores-demandarian-a-elypsis-por-la-encuesta-del-
viernes-y-los-k-cargarian-con-denuncia-penal-para-investigar-a-operadores.
[39] Hedge Fund Loses $1 Billion in One Month on Argentina Bet. Retrieved from https://www.
wsj.com/articles/hedge-fund-loses-1-billion-in-one-month-on-argentina-bet-11
567696547.
[40] Autonomy Capital lost 16% in Argentina market rout. Retrieved from https://www.ft.com
/content/29764546-c821-11e9-a1f4-3669401ba76f.
[41] Argentina’s Cristina Kirchner, facing corruption allegations, mounts unlikely comeback. Wash-
ington Post. Simeon Tegel. July 29, 2019. Retrieved from https://www.washingtonpost.c
om/world/the americas/argentinas-cristina-kirchner-facing-corruption-allegat
ions-mounts-unlikely-comeback/2019/07/28/3f3a31d4-a3dd-11e9-a767-d7ab84aef3e
9 story.html.
[42] SEIDO - Special Report: Lie to Me. Retrieved from: https://us3.campaign-archive.com
/?e=&u=e02ede36ce39515be5fb17728&id=3bf5cf2e90.
[43] Manning, C. and Schutze, H. Foundations of statistical natural language processing. MIT pres
s, (1999).
[44] D. Li, and Y. Liu. Deep learning in natural language processing. Springer, (2018).
[45] R. Martinez et al. Disentangling categorical relationships through a graph of co-occurrences.
Physical Review E, 84, (2011).
[46] A. Ceron et al. Using sentiment analysis to monitor electoral campaigns:
method mat-
ters–evidence from the united states and Italy. Soc. Sci. Comput. Rev. 33, 3–20, (2015).
[47] New York Times. New York Times National Polling Average (2016). Retrieved from: http:
//www.nytimes.com/interactive/2016/us/elections/polls.html.
43


---

Supplementary Information
Tweets
Bots
Users
Total
538359
67336507
Daily
2243
280568
Daily classiﬁed
1617
211229
Daily classiﬁed MP
619
114653
Daily classiﬁed FF
998
96576
TABLE VII. Tweets statistics.
We report the Total number of tweets collected.
The average
daily number of tweets classiﬁed (Daily classiﬁed) and the average daily classiﬁed tweets for each
candidate.
Users
Bots
Users
Total
17953
2252551
Daily
732
83330
Daily classiﬁed
560
63808
Daily classiﬁed MP
198
31497
Daily classiﬁed FF
362
32310
TABLE VIII. Users statistics. We report the Total number of users collected. The average daily
number of users classiﬁed (Daily classiﬁed) and the average daily classiﬁed users for each candidate.
44


---

2019-03
2019-04
2019-05
2019-06
2019-07
2019-08
2019-09
2019-10
2019-11
30
40
50
60
70
Percent
FF
MP
FF (trusted polls)
MP (trusted polls)
FIG. 14. Instantaneous prediction compared with trusted polls. Thick lines represent AI prediction
and dashed line represent trusted polls.
2019-03
2019-04
2019-05
2019-06
2019-07
2019-08
t0
10
20
30
40
50
60
Percent
FF
MP
third party
FIG. 15. Cumulative prediction with T0 =March, 1 until few days (August 1) before PASO.
45


---

#
Hashtag
Camp
Count
1
sisepuede
M
216757
2
macri
M
102172
3
albertopresidente
K
65644
4
axelgobernador
K
60920
5
juntosporelcambio
M
52617
6
yovotomm
M
49557
7
ladamosvuelta
M
47546
8
cfk
K
38718
9
cambiemos
M
38538
10
sevan
K
32110
11
habraconsecuencias
K
28406
12
24a
M
23819
13
macrihacetecargo
K
21364
14
novuelvenmas
M
21054
15
cronicaanunciada
K
20293
16
frentedetodos
K
18115
17
albertoycristina
K
17482
18
sinceramente
K
15403
19
juntossomosimparables
M
14405
20
sevanenprimeravuelta
K
14091
TABLE IX: The top 25 hashtags from March and July in
2019. The camp ﬁeld represents the classiﬁcation: M stays
for Macri and K for Fern´andez (from the name of the running
mate Cristina Fern´andez de Kirchner. Count indicates the
number of time a given hashtag appears in the dataset.
46


---

#
Hashtag
Camp
Count
1
cambiemos
M
150754
2
macri
M
120363
3
cfk
K
63052
4
sinceramente
K
56198
5
habraconsecuencias
K
52896
6
novuelvenmas
M
39352
7
juntosporelcambio
M
35186
8
macritevuelvoaelegir
M
32241
9
cronicaanunciada
K
30954
10
massa
K
29565
11
axelgobernador
K
29039
12
navarro2019
K
27885
13
defensoresdelcambio
M
27010
14
fuerzacristina
K
21342
15
andatemacri
K
19486
16
chaumacri
K
19184
17
debodecir
M
19173
18
hayotrocamino
K
19152
19
mm2019
M
16117
20
sracristinalecuentoque
M
16082
TABLE X: The top 25 hashtags from August and October in
2019. The camp ﬁeld represents the classiﬁcation: M stays for
Macri and K for Fern´andez (from the name of the running
mate Cristina Fern´andez de Kirchner. Count indicates the
number of time a given hashtag appears in the dataset.
47

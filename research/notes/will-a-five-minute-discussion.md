---
title: Will a Five-Minute Discussion
id: will-a-five-minute-discussion
tags:
- electoral-canvassing
- ciblage-terrain
- pons
- field-experiment
- precinct-randomization
- ciblage-swing-voters
created: '2026-07-21T19:07:58.967540Z'
updated: '2026-07-21T19:40:55.075123Z'
source: https://www.povertyactionlab.org/sites/default/files/research-paper/Will-a-five-minute-discussion-change-your-mind_Pons_March2017.pdf
source_domain: www.povertyactionlab.org
fetched_at: '2026-07-21T19:07:58.967302Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Pons (2016/2017 working paper version of AER 2018), ''Will a Five-Minute
  Discussion Change Your Mind?'' The canonical field-experiment source for precinct-level
  canvassing effects in France. From 1 Feb to 6 May 2012, ~80,000 PS activists knocked
  on 5 million doors (out of ~34,600 zip-code territories partitioned into 3,260 randomization
  territories) during Hollande''s 2012 presidential campaign; Pons was one of three
  national field directors and embedded the randomization directly into campaign operations.
  Randomization was stratified: territories divided into strata of 5 precincts ranked
  by an estimated ''potential to win votes'' score; within each stratum, 4 of 5 precincts
  (80%) were randomly assigned to treatment (allocated to canvassers), 1 to control.
  Where territory boundaries were unknown (no comprehensive precinct-boundary database
  exists in France), randomization fell back to the municipality level. This precinct-level
  randomization (not individual-level, as in prior US GOTV literature) was possible
  because of the campaign''s five-million-door scale, and it aligns the unit of treatment
  with the unit at which French vote shares are administratively recorded. Door-to-door
  visits had no significant effect on turnout, but raised Hollande''s vote share by
  3.2 points (round 1) and 2.8 points (round 2), significant at 5%; canvassing accounted
  for roughly half of Hollande''s round-1 lead and one-fourth of his round-2 victory
  margin. Effects persisted: PS candidates gained an estimated 0.66-0.7 points in
  the 2012 legislative elections in visited precincts (larger than the victory margin
  in 5.9% of constituencies won by PS), and persistence to the 2014 European elections
  was about 47% of the original effect size, then decayed further. A seemingly-unrelated-regressions
  (SUR) test comparing turnout vs. vote-share impacts finds the vote-share gain is
  not explained by mobilizing left-wing non-voters alone; persuasion of swing/undecided
  voters is the dominant channel (persuasion rates of 9.6% and 13.0% in rounds 1 and
  2, comparable to the 15.6% and 11.5% turnout-persuasion rates found in Gerber &
  Green 2000 and Green et al. 2003). Only 48% of doors knocked were actually opened,
  and imperfect compliance (not-all-treatment precincts were fully canvassed) required
  an IV/local-average-treatment-effect design distinguishing intent-to-treat from
  treatment-on-treated. Campaign cost was M, 38x less than Obama 2012''s US budget,
  implying door-to-door was systematically favored in France as the cost-efficient
  mobilization channel. Directly relevant to axis 1 of the research query: this is
  the empirical basis for treating door-knocking allocation as causally meaningful
  at bureau-de-vote granularity in France, and for skepticism about assuming campaign-driven
  local swings are uniform.'
raw_file: raw/will-a-five-minute-discussion.pdf
---

*Suggested by [[door-to-door-canvassing-campaigns-sway-voter-decisions]] — primary source paper cited by secondary summary*

 
Will a Five-Minute Discussion 
Change Your Mind? A Countrywide 
Experiment on Voter Choice in 
France 
 
 
Vincent Pons 
 
 
 
Working Paper 16-079 


---

 
 
Working Paper 16-079 
 
Copyright © 2016, 2017 by Vincent Pons 
Working papers are in draft form. This working paper is distributed for purposes of comment and discussion only. It may 
not be reproduced without permission of the copyright holder. Copies of working papers are available from the author. 
 
 
 
Will a Five-Minute Discussion Change 
Your Mind? A Countrywide Experiment 
on Voter Choice in France 
 
Vincent Pons 
Harvard Business School 
 


---

WILL A FIVE-MINUTE DISCUSSION CHANGE YOUR MIND?
A COUNTRYWIDE EXPERIMENT ON VOTER CHOICE IN FRANCE∗
Vincent Pons
Harvard Business School†
March 2017
Abstract
This paper provides the rst estimate of the eect of door-to-door canvassing on ac-
tual electoral outcomes, via a countrywide experiment embedded in François Hollande's
campaign in the 2012 French presidential election. While existing experiments random-
ized door-to-door visits at the individual level, the scale of this campaign (ve million
doors knocked) enabled randomization by precinct, the level at which vote shares are
recorded administratively. Visits did not aect turnout, but increased Hollande's vote
share in the rst round and accounted for one fourth of his victory margin in the second.
Visits' impact persisted in later elections, suggesting a lasting persuasion eect.
JEL Codes: C93, D72, D83, O52
∗I am grateful to Esther Duo, Benjamin Olken, Stephen Ansolabehere, Daniel Posner, Alan Gerber,
Todd Rogers, Daniel Hidalgo, Jens Hainmueller, Daron Acemoglu, and Benjamin Marx for suggestions that
have improved the paper.
†Vincent Pons, Harvard Business School, BGIE group, Soldiers Field, Boston, MA 02163; vpons@hbs.edu;
+1 617 899 7593
1


---

1
Introduction
Consumers and voters base their economic and political decisions on preferences and beliefs
shaped by their direct observations, the communication they receive, and discussions with
others. Interpersonal discussions contribute to the spread of information and peer eects in
technology adoption (e.g., Foster and Rosenzweig, 1995; Conley and Udry, 2010), educational
choices (e.g., Bobonis and Finan, 2009), or nancial decisions (e.g., Duo and Saez, 2003;
Banerjee et al., 2013), and political discussions are commonly seen as the healthy expression
of a functioning democracy. To the extent that democracy revolves around the deliberation
and transformation of people's preferences, rather than the simple aggregation of their votes,
discussion may actually be as important a condition of democracy as the electoral participa-
tion of all citizens (Habermas, 1996; Elster, 1998). The importance people attach to political
discussions is illustrated by DellaVigna et al. (2017)'s result that many of us vote in order
to later be able to tell others.
But discussions also aect future political behavior. In their pioneering study on the 1940
U.S. presidential election, Lazarsfeld et al. (1944) nd that most voters got their information
about the candidates from family members, friends, and colleagues, rather than from the
media, and Nickerson (2008) and Bond et al. (2012) provide direct evidence of the diusion
of voter turnout o- and online in more recent elections. While diusion can be driven both
by discussion and direct observation of others' actions, lab and eld studies which narrow
the focus to interpersonal discussions (e.g., through group deliberations and deliberative
polls) do tend to conrm their inuence on the opinions of participants (e.g., Myers and
Bishop, 1970; Isenberg, 1986; Luskin et al., 2002; Druckman, 2004; but see Farrar et al.,
2009), including on issues as resistant to change as intergroup prejudices (Broockman and
Kalla, 2016).
In an eort to leverage the power of personal discussions, electoral campaigns around the
globe increasingly rely on targeted appeals delivered to voters door-to-door (Bergan et al.,
2005; Hillygus and Shields, 2014; Issenberg, 2012). But whether doorstep discussions between
2


---

canvassers and voters can actually increase voter support is anything but certain: partisan
activists may expose voters to more precise and newer information, but their arguments,
explicitly driven by electoral motives, may inspire less trust than those of regular discussion
partners or even random strangers. Starting with the seminal work of Gerber and Green
(2000), get-out-the-vote eld experiments conducted in a wide variety of settings have found
large eects of door-to-door canvassing on voter turnout (Gerber and Green, 2015), leaving
the question of its impact on vote shares unanswered.
This paper provides the rst estimate of the impact of door-to-door visits on actual
electoral outcomes. Using administrative records, it reports the results of a precinct-level
countrywide experiment embedded in François Hollande's campaign in the 2012 French pres-
idential election. From 1 February 2012, which was 11 weeks before the rst round of the
election, up until the second round on 6 May 2012, an estimated 80,000 left-wing activists
knocked on ve million doors to encourage people to vote for the candidate of the Parti
Socialiste (PS), the mainstream center-left party in France. The author's involvement as
one of the three national directors of the eld campaign provided a unique opportunity to
evaluate its eect on the results of the election. Canvassers' visits did not signicantly aect
turnout, but they had large and persistent eects on vote share.
Dierently from the present experiment, existing studies have typically conducted ran-
domization of door-to-door eorts at the individual or household level, with important con-
sequences for outcome measurement. These evaluations can adequately estimate the eect
of door-to-door canvassing on voter turnout, which in many countries is recorded at the indi-
vidual level and made publicly available. However, they are less suited to measure the eect
of the visits on voter choices which, of course, are secret. Some studies resort to polling to
construct a close approximation: vote intention or, after the election took place, self-reported
vote (e.g., Arceneaux, 2007; Arceneaux and Kolodny, 2009; Arceneaux and Nickerson, 2010;
Bailey et al., 2016; Barton et al., 2014; Dewan et al., 2014). Unfortunately, for all its merits,
randomization does not eliminate traditional survey biases. In phone surveys, response rates
3


---

to questions on self-reported vote are typically as low as 10 or 15 percent (e.g., Barton et
al., 2014; Pew Research Center, 2012), and there is ample evidence that questions on polit-
ical behavior are particularly prone to misreporting, including overreporting for the winner
(e.g., Wright, 1993; Atkeson, 1999; Campbell, 2010). An additional concern is that these bi-
ases might dier between treatment and control individuals (e.g., Cardy, 2005; Bailey et al.,
2016; Gelman et al., 2016). The present experiment overcomes these obstacles by conducting
the randomization at the precinct level, at which administrative records of vote shares are
available, while including a number of precincts large enough to secure sucient statisti-
cal power. Prior to this study, neither the implied number of activists nor the campaign
apparatus required to organize them had been available to researchers (Arceneaux, 2005).
An additional benet of the large scale of this experiment is the implied external validity.
Existing get-out-the-vote experiments, even when they involve political parties and nonpar-
tisan organizations, are conducted at a much smaller scale than most actual campaigns.
This allows the researchers and the hierarchy of the campaign (the principal) to carefully
select activists (the agent) who will interact with voters and to closely control the content
of their discussions. In large-scale campaigns, scope for control is much more limited and
the principal-agent problem is more acute, which may lower the impact (Enos and Hersh,
2015). Results from framed get-out-the-vote experiments themselves show that quality mat-
ters (e.g., Nickerson, 2007), and evidence from other contexts suggests that interventions
generating large eects in a small, controlled setting may become unimpactful when they
are scaled up (e.g., Banerjee et al., 2008; Grossman et al., 2015). The present experiment, em-
bedded into a large-scale presidential campaign, overcomes the external validity limitations
of prior studies. One aspect of the limited control of the candidate's central team over local
activists, however, was that only a subset of territories that participated in the door-to-door
campaign also participated in the experiment. I use daily reports entered by canvassers on
the campaign website and their responses to a post-electoral online survey to identify which
territories did indeed use the randomization lists. In these territories alone, precincts and
4


---

municipalities collectively containing 5.02 million registered citizens were randomly assigned
to either a control or a treatment group.
The randomization was conducted within strata of ve precincts characterized by their
estimated potential to win votes. Four precincts (80 percent) of each stratum were randomly
assigned to the treatment group, and one (20 percent) to the control group. A subset of the
treatment precincts  those with the highest potential to win votes  were allocated to the
canvassers (more details in Section 3.1). Like in a standard encouragement design, I estimate
the eect of a precinct being assigned to the treatment group (the intent-to-treat eect of
the campaign) by comparing electoral outcomes in control and treatment precincts, and the
eect of a precinct being allocated to canvassers (a local average treatment eect) by using
random treatment assignment as an instrument. This strategy allowed me to maximize the
eectiveness of the campaign while preserving the validity of the experimental design.
All results are based on ocial election outcomes at the precinct level. Surprisingly,
the door-to-door visits did not signicantly aect voter turnout. Had randomization been
conducted at the individual level, as in existing studies, and only voter turnout been recorded,
I would have concluded  wrongly  that the campaign had no signicant impact. Instead,
I nd that it increased François Hollande's vote share in precincts allocated to canvassers
by 3.2 and 2.8 percentage points in the rst and second rounds of the presidential elections,
respectively. These estimates correct for the imperfect compliance of the canvassers with
their allocated lists of precincts, and are signicant at the 5 percent level. Multiplying these
estimates by the fraction of French doors knocked, I obtain that the canvassing campaign
accounted for approximately one half of Hollande's lead in the rst round and one fourth of
his victory margin at the second round.
The scale of the study also facilitated the assessment of downstream eects.
While
transitory shocks to voter turnout have been found to generate persistent eects due to
long-lasting impact of the shocks themselves or to habit formation (Gerber et al., 2003;
Meredith, 2009; Davenport et al., 2010; Garcia Bedolla and Michelson, 2012; Fujiwara et al.,
5


---

2016), the present study is the rst to show that eects on vote choice can persist as well. In
fact, contrasting with Gerber et al. (2011), the impact of the visits almost entirely persisted in
the subsequent parliamentary elections held one month after the presidential vote. Overall,
door-to-door canvassing increased the vote share obtained by Parti Socialiste candidates in
these elections by 0.7 percentage points. This eect was larger than the victory margin of
members of parliament from the PS elected in 2012 in 5.9 percent of the constituencies.
Persistence to the 2014 European elections was smaller (about 47 percent of the original
eect) and at the limit of statistical signicance.
Finally, I discuss possible interpretations of the results. Although I cannot directly test
them, examining the eects of the visits on the vote shares of other candidates provides
suggestive evidence. The rst and, to me, most likely interpretation, is that the results
were driven by a persuasion eect. An alternative interpretation is that the door-to-door
visits increased the participation of left-wing supporters, and that they demobilized an equal
number of supporters of other parties. Of all types of voters, those who could be deemed
most likely to feel cross-pressured and thus demobilized are probably the supporters of
the far-right candidate Marine Le Pen, many of whom used to vote left and still maintain
leftist preferences on economic issues. However, her vote share was unaected, making the
persuasion interpretation more likely than demobilization. Two dierent mechanisms may
have driven the persuasion eect of the visits: canvassers may have persuaded voters by
changing their preferences on some political issues or by changing their beliefs about the
quality of the PS and of its candidate. The short average length of the visits makes the rst
mechanism unlikely. Instead, the fact that most voters that were canvassed had never been
visited by a political activist before makes the second mechanism, a shift in the perception
of the quality of candidate and party, more plausible. In addition, the increase of Hollande's
vote share was a result of his taking votes away from right-wing candidates more than from
other left-wing candidates.1 But right-wing voters could be deemed less susceptible to align
1Nicolas Sarkozy, the incumbent and candidate of the right-wing Union pour la Majorité Présidentielle,
was the only opponent mentioned in the toolkit distributed to canvassers and, naturally, his presidency was
6


---

their preferences with the political agenda of Hollande than voters supporting other left-
wing candidates, who naturally oered a closer ideological platform. This again makes it
less likely that voters' political preferences changed, and more likely that their beliefs about
the PS and its candidate did.
Overall, the results suggest that in elections of very high salience, voter outreach methods
will have little eect on turnout, but that interpersonal discussions can have a large and long-
lasting persuasion eect.
This paper contributes to a growing literature providing causal evidence on the drivers
and eects of persuasive communication (see DellaVigna and Gentzkow (2010) for an overview).
While the access to and information provided by the TV (Simon and Stern, 1955; Gentzkow,
2006; DellaVigna and Kaplan, 2007; Enikolopov et al., 2011), the radio (Adena et al., 2015),
newspapers (Gerber et al., 2009; Gentzkow et al., 2011; Chiang and Knight, 2011), or the
internet (Falck et al., 2014; Campante et al., 2014) have the potential to profoundly shape
voters' political preferences and, depending on the context and the media, substantially in-
crease (e.g., Gentzkow et al., 2011) or decrease (e.g., Falck et al., 2014) voter turnout, the
eects of political ads disseminated by electoral campaigns through the very same channels
are more modest, overall. Neither Ashworth and Clinton (2007), nor Krasno and Green
(2008) nd substantial eects of TV campaign ads on aggregate turnout, Broockman and
Green (2014) do not nd that online ads have any eect on voters' evaluation of candidates,
or even name recognition, and Gerber et al. (2011) only nd very short-lived eects of TV
and radio ads on recipients' voting preferences. Yet, Spenkuch and Toniatti (2016) nd
that TV ads aect the electoral results by altering the composition of the electorate, even
though they leave aggregate turnout and preferences unaected. Both Panagopoulos and
Green (2008) and Larreguy et al. (2016) also report eects of radio ads on vote shares, which
disproportionately benet challengers.
Well-powered precinct-level randomized evaluations of eld campaigns, including those
discussed in many conversations. However, the main objective of the campaign conveyed to the canvassers
was not persuading Sarkozy's voters but mobilizing left-wing non-voters (see Section 2.3 for more details).
7


---

fully embedded in a candidate's campaign, have studied the eects on vote shares of campaign
activities that require fewer human resources and are less direct and personal than door-to-
door canvassing, such as direct mail (e.g., Rogers and Middleton, 2015), phone and robo calls
(e.g., Shaw et al., 2012), and town hall meetings (e.g., Wantchekon, 2003). These types of
contact generate relatively larger eects for weaker candidates (Gerber, 2004; Fujiwara and
Wantchekon, 2013). The messages also generate larger eects when they emphasize valence
rather than ideology (Kendall et al., 2015), and, in developing countries, clientelist rather
than public policy platforms (Wantchekon, 2003). 2
Although logistically more demanding, door-to-door visits are more direct and personal
than other types of eld campaign contacts and mass media advertisements. The interactive
discussions to which they lead naturally adapt to respondents' prole and questions, thus
potentially aecting voter choice in a dierent and perhaps more dramatic way than other
forms of persuasive communication. In fact, their eect on the decision to vote is itself very
dierent (e.g., Gerber and Green, 2000).
The remainder of the paper is organized as follows. Section 2 provides more background
information on François Hollande's door-to-door campaign and on the 2012 and 2014 elec-
tions in France. Section 3 describes the experimental design and its implementation. Section
4 evaluates the overall impact of the door-to-door canvassing visits on voter turnout and vote
shares in the presidential elections and in the following elections. Section 5 interprets the
results, and Section 6 concludes.
2The paper also speaks to a growing literature, in developing countries, which estimates the impact of
election-related eld campaigns targeting issues beyond voter turnout and vote choice, such as corruption
(Banerjee et al., 2011; Chong et al., 2015), electoral misbehavior and violence (Aker et al., 2011; Collier and
Vicente, 2014), or trust in the institutions (Marx et al., 2016).
8


---

2
Setting
2.1
The 2012 and 2014 French elections
In 2012, France elected both a new president and a new National Assembly. Presidential
elections in France have two rounds, with the two candidates achieving the highest vote
shares in the rst round going on to the second. Turnout in the rst round of presidential
elections on 22 April 2012 was 79.5 percent of registered citizens. 3
Nicolas Sarkozy, the
incumbent and candidate of the right-wing Union pour la Majorité Présidentielle (UMP), and
François Hollande, the candidate of the left-wing Parti Socialiste (PS), obtained respectively
27.2 percent and 28.6 percent of the votes and qualied for the second round (see Figure
1). Compared to the 2007 presidential election, François Bayrou, the centrist candidate, lost
over half of his vote share (9.1 percent compared to 18.6 percent), and the far-left candidates'
portion became marginal (1.7 percent compared to 5.8 percent). The vote share of Marine
Le Pen, 17.9 percent, was the highest ever obtained by her party, the far-right Front National
(FN). Voter turnout in the second round, on 6 May, was high again at 80.4 percent, and
François Hollande was elected President with 51.6 percent of the votes.
French parliamentary elections use single-member constituencies. Similarly to the pres-
idential elections, they consist of two rounds, unless one candidate obtains more than 50
percent of the votes in the rst. Unlike in the presidential elections, all candidates who
obtain a number of votes higher than 12.5 percent of registered citizens in the rst round
can compete in the second, but in most cases that is only two candidates. The 2012 parlia-
mentary elections took place on 10 and 17 June. Turnout was 57.2, then 55.4 percent  far
lower than in the presidential elections, and lower than the previous parliamentary elections.
This conrms the lesser salience of parliamentary elections in the minds of voters, as well as
a general declining trend of turnout (Figure 2). The PS candidates won in 49 percent of the
3In France, voter turnout is computed as the fraction of number of votes cast over the number of registered
citizens.
Turnout gures reported throughout the paper follow this convention.
Since the door-to-door
canvassing campaign started after the registration deadline of 31 December 2011, it could not aect the
number of registered citizens.
9


---

constituencies.
In order to examine the long-run eect of the door-to-door visits, I include the 2014
European elections in the analysis.4
These elections took place on 25 May.
Unlike the
presidential and parliamentary elections, the European elections use the proportionality
rule, and France is divided into seven large European constituencies. Only 42 percent of
the voters participated in these elections and the PS suered a major defeat. Its candidates
ranked third in all the constituencies, behind the lists of the UMP and of the FN.
2.2
Electoral campaigns in France vs. the United States
Among the many dierences between French and U.S. electoral campaigns, at least three
should be emphasized here:
funding, distribution of media access, and eld activities.
François Hollande's 2012 campaign spent 29 million dollars, 38 times less than Barack
Obama's 1.107 billion dollars. The bulk of Obama's money was spent on radio and tele-
vision advertising. Instead, all French radio and TV channels were mandated to give equal
coverage to the campaign of each of the 12 candidates before the rst round. Similarly,
between rounds, they had to give equal coverage to Sarkozy and Hollande: in France, can-
didates do not compete using TV ads.
As a result, one might hypothesize that French
campaigns put relatively more emphasis on the recruitment of volunteers and that they se-
lect their eld campaign methods with great care. On the contrary, until recently, French
political parties allocated few resources to the recruitment, training, and coordination of
activists. In addition, local units of the PS were largely autonomous and free to choose their
own campaign methods. Although it had once been common, door-to-door canvassing had
progressively been replaced by other more impersonal techniques, such as handing out yers
in public places, or dropping them in mailboxes (Liegey et al., 2013). By 2012, only few
4In 2014, France also held municipal elections. However, the political orientation (left, right, etc.) of
the candidates is only known in 27 percent of the municipalities, those with more than 1,000 inhabitants.
Moreover, in these municipalities, the vast majority of candidates run under aliations which are not en-
dorsed by a national party, such as PS or UMP. Given the low resulting statistical power, I do not include
the municipal elections in the analysis.
10


---

areas saw frequent door-to-door canvassing (Lefebvre, 2016).
Two factors explain the emphasis the PS placed on canvassing during the 2012 presidential
election.
First, the 2008 campaign of Barack Obama generated unusual levels of public
attention and enthusiasm across France. Prominent French politicians and think tanks called
for an adoption of U.S. electoral and campaign practices, including the organization of large
eld campaigns (Terra Nova, 2009). The second factor, as in the United States, was academic
research: the rst French randomized evaluation of a door-to-door canvassing get-out-the-
vote eort (Pons and Liegey, 2016) aided in convincing the PS to scale up the method for
the 2012 presidential election.5
As a result of these dierent factors, the objective set for Hollande's 2012 door-to-door
canvassing campaign was ambitious: to knock on ve million doors, or roughly 15 percent
of all French dwellings.
2.3
François Hollande's 2012 door-to-door canvassing campaign
Four days after the second round of the presidential election, all 9,227 activists with an
active prole on Hollande's campaign website received an email invitation to take an online
anonymous survey. 2,126 (23.0 percent) responded, of whom 1,972 (92.8 percent) had par-
ticipated in the door-to-door canvassing campaign (Table 1). This survey, although likely
not representative due to the low response rate, provides useful insights about the prole of
the local activists. French political parties have a relatively large number of active mem-
bers. On the one hand, this provided Hollande's campaign with a large number of highly
motivated volunteers: 87 percent respondents reported participating in three or more rounds
of door-to-door canvassing, and 38 percent in more than ten. On the other hand, many of
these volunteers were unaccustomed to welcome newer activists who were not ocial party
members. As a result, by the end of the campaign, only 12 percent of the respondents were
5Liegey et al. (2013) examine at greater length the dierent steps through which the PS progressively
adopted door-to-door canvassing as the preferred eld campaigning strategy from 2010 to 2012.
11


---

sympathizers involved in a campaign for the rst time, while 79 percent were ocial mem-
bers of the PS. Relatedly, two thirds of the canvassers were over 46 years old, reecting the
skewed age pyramid of PS members.
As another consequence of the overwhelming presence of PS members among activists,
the campaign could and had to rely extensively on the preexisting structure of the party. The
vast majority of the eld organizers coordinating the volunteers were themselves members
and, often, heads of local units of the PS, and most of the départements' 6 coordinators had
preexisting responsibilities within the party. As a result, the campaign had direct authority
neither on the eld organizers, nor on the départements' coordinators. Dierent was the
status of 15 eld-based regional coordinators, who were paid by the central campaign team
and worked full time under its authority. They assisted in organizing door-to-door sessions
and monitoring activists, whom they encouraged and helped with reporting their activity
on the campaign's website. Finally, 150 highly motivated and educated national trainers
were recruited. Every Saturday, they were sent to the local headquarters of the campaign
across France to train eld organizers. The trainings revolved around role playing and taught
eld organizers how to train and coordinate volunteers themselves. Of respondents to the
post-electoral survey, 59 percent had attended a training session. This eort addressed a real
need: only 22 percent of the respondents had frequently done door-to-door canvassing before
the campaign. The trainings emphasized a simple message: the eld campaign was about
door-to-door canvassing, and nothing else. The emphasis placed on door-to-door canvassing
was also evident in the campaign material: in addition to leaets, canvassers received door-
hangers dedicated to the door-to-door campaign (see Figure H4 in Appendix H).
To ensure that the intervention would be administered uniformly, the training course
was identical everywhere, and all canvassers received a toolkit with detailed instructions and
advice on how to start and lead the conversations. The full toolkit is available in Appendix
H (Figure H1). As in most GOTV interventions, the instructions provided by the central
6Départements are one of the three levels of government below the national level, between the region and
the municipality. There are a total of 101 départements.
12


---

campaign team were intended as a general canvass, which would be adapted according to each
voter's type, interests, and questions.7 The mobilization of left-wing voters was highlighted
as the main objective, as it seemed easier and more likely to win votes than persuading
undecided voters, who are the second traditional target of partisan campaigns. Reecting
this strategic choice, canvassers were instructed to provide basic information systematically
about the date of the election, the location and opening times of the poll oce, and the
name of the PS candidate. They urged people to vote, and to vote for Hollande, using
general arguments about the importance of voting and of the forthcoming elections as well
as personal examples and stories. The discussions usually lasted from one to ve minutes.
At the end of the discussion, the canvassers typically gave their interlocutor some campaign
literature: a thematic leaet or a 23-page booklet summarizing François Hollande's platform.
When no one opened, a leaet or doorhanger was left on the door.
After each canvassing session, activists registered on the campaign's website could report
the number of doors knocked and opened, the precinct covered, and provide additional
comments. In total, 14,728 reports were entered over the entire course of the campaign,
many of which encompassed multiple canvassing sessions, conducted by dierent teams or
on dierent dates. 1,955 users (21.2 percent of all users with an active prole on the website)
entered at least one report, and an additional 1,420 activists (15.4 percent of those registered
on the website) were mentioned in at least one report. As a counterpart to the reporting, the
website allowed activists to follow the progress of the campaign in their area. In addition,
eld organizers and départements' coordinators had access to a country map which color-
coded the départements based on the numbers of doors knocked. Figure 3 shows snapshots of
the maps for the ve last weeks of the campaign, and Figure H3 in Appendix H presents the
guide distributed to eld organizers on how to use the website, with annotated screenshots
of its dierent parts. In some areas, however, eld organizers and activists never registered
7As Gerber and Green (2015) note in their seminal book on GOTV campaigns, scripts are helpful to
guide canvassers, but they are not a substitute for informal and personalized discussions, which are central
to the eectiveness of door-to-door canvassing.
13


---

on the campaign platform, and even when they did, they only reported a fraction of all
doors knocked. With the help of the regional coordinators of the campaign, this fraction
was estimated département by département to infer the total number of doors knocked.
The scope of the campaign was without comparison in any previous door-to-door eorts
of a French political party or organization: overall, approximately ve million doors were
knocked, of which slightly more than one third were reported on the website.
Figure 4 plots the number of doors knocked over time as reported on the website. As
is clear from this graph, the pace of the campaign was very slow until six weeks prior to
the rst round. It then increased gradually and reached its peak between the two rounds.
Underlying this long-term trend, short-term weekly cycles are easily identiable. Each week,
the canvassing sessions took place mostly on Fridays and Saturdays. On average, the door-
opening rate was high, around 48 percent, and activists usually worked in pairs.
3
Experimental Design and Implementation
3.1
Randomization
Denition of territories as a set of contiguous municipalities
Before the start of the door-to-door campaign, I split the entire country into territories
dened as a set of contiguous municipalities sharing a common zip code. 8 Any new activist
registering on the campaign's website was allocated to the territory corresponding to his zip
code and put in touch with the corresponding PS local unit.
8There was one exception to this rule: in each département, zip codes with fewer than 5,000 registered
citizens were subsumed under the same territory.
14


---

Denition of the target number of registered citizens in each territory
The overall objective of knocking on ve million doors was translated into a target number
of registered citizens for each territory, 
TA.9 This variable was set proportionally to the
total number of registered citizens in the territory and to a proxy for the potential to win
votes, 
PO.

PO was dened as the fraction of nonvoters multiplied by the left vote share
among active voters, each taken from the results of the second round of the 2007 presidential
elections.10
Level of randomization
Randomization was done within each of 3,260 territories separately. In territories where the
geographical boundaries of the electoral precincts were known for all or most municipali-
ties, based on the 2011 voter rolls, randomization was done at the precinct level. 11 In the
remaining territories, randomization was done at the municipality level. Henceforth, for con-
ciseness, I designate the unit of randomization as precincts, even when the randomization
was done at the municipality level.12
9The objective communicated to the canvassers in each territory was expressed as a number of doors. To
translate the target number of registered citizens into a target number of doors, I assumed that each door
represented 1.4 registered citizens on average, a ratio obtained by dividing the total number of registered
citizens in France, 46.0 million, by the total number of dwellings, 33.2 million.
10This denition of 
PO could only be applied directly to precincts whose boundaries had not changed
since 2007. In these precincts, I regressed 
PO (computed using this denition) on characteristics constructed
based on the 2011 voter rolls (average building size, this variable squared, the proportion of buildings with
fewer than 5, between 5 and 15, or more than 15 registered citizens, average age, this variable squared,
the proportion of citizens younger than 25, and the proportion of citizens older than 65). I then used the
estimated coecients to predict (or, technically, construct) 
PO in precincts whose boundaries had changed
since 2007.
11There does not exist any comprehensive database of the boundaries of French voter precincts, which are
drawn by the municipalities. However, to organize its 2011 primary elections, the PS had collected voter
registers in all suciently large municipalities. These voter registers indicate the address and precinct of
each registered citizen and could thus be used to infer the geographical boundaries of the corresponding
precincts.
12The list of 3,260 territories excludes 279 territories each counting a unique municipality of unknown
precinct boundaries: in these territories, the single municipality had to be allocated to canvassers in any
case (so that they could participate in the door-to-door campaign), preventing randomization.
15


---

Randomization
The randomization rule was identical across all territories. It was designed in a way that
ensured that precincts allocated to canvassers had the highest possible estimated potential
to win votes 
PO compatible with running an experiment. I proceeded in three steps, which
Figure 5 illustrates using the hypothetical example of a territory with an arbitrary number
(17) of precincts.
The rst step was the stratication. I computed 
PO in each precinct of the territory, and
ranked precincts from the highest to the lowest 
PO. I grouped precincts in strata of ve: the
territory's rst stratum comprised the ve precincts with the highest 
PO, the second stratum
the ve precincts ranked immediately below, and so on until the last stratum, composed
of the ve or fewer remaining precincts.
The rst stratum of any territory was always
included in the randomization. In some territories, additional strata were also included in
the randomization, as will become clear from the second and third steps.
The second step was the randomization itself.
Focusing rst on the territory's rst
stratum, I randomly assigned its precincts to the treatment and control groups, using random
numbers generated in Stata. When the rst stratum included ve precincts, exactly four
(80 percent) of these precincts were randomly assigned to the treatment group, and one
(20 percent) to the control group. In the small set of territories in which the rst stratum
included fewer than ve precincts (due to the territory itself including fewer than ve), each
precinct was assigned with an 80 percent probability to the treatment group and with a 20
percent probability to the control group.
In the third step, I dened the list of precincts of the rst stratum which canvassers
would be asked to cover. This list was prepared before the start of the campaign. Precincts
allocated to canvassers included only treatment precincts (and no control precincts), but
not necessarily all treatment precincts. The treatment precinct with the largest potential

PO was always allocated to the canvassers.
If the number of citizens registered in this
precinct was larger than the target number of registered citizens for the territory

TA, no
16


---

other treatment precinct was allocated to the canvassers. If its number of registered citizens
was lower than 
TA, the treatment precinct with the second largest 
PO was also allocated
to the canvassers. Then again, if the combined number of registered citizens in the rst and
second treatment precincts was larger than 
TA, no other treatment precinct was allocated to
the canvassers. Otherwise, the treatment precinct with the third largest 
PO was allocated
to the canvassers and the same rule was used one last time to decide whether or not to also
allocate the fourth (and last) treatment precinct to the canvassers.
In the vast majority of territories, the total number of registered citizens in the treatment
precincts of the rst stratum was higher than 
TA, and no other stratum was included in
the randomization. If (and only if) the total number of registered citizens in the treatment
precincts of the rst stratum remained lower than 
TA, the second stratum was also included
in the randomization.
The second and third steps were then repeated on this stratum.
If needed, additional strata were included until the total number of registered citizens in
treatment precincts allocated to canvassers was equal or higher than 
TA.
Discussion of the randomization
Two aspects of this randomization are unusual, without posing any threat to the validity of
the design. First, it is unusual not to allocate all treatment units to receive the intervention.
However, there are other randomization designs in which only a fraction of the treatment
units end up receiving the intervention. For instance, in encouragement designs, a random
group of subjects is oered an intervention, and only a (non-random) subset takes it (e.g.,
Hirano et al., 2000; Duo and Saez, 2003). In these designs, we typically think of take-up
(conditional on treatment) as being driven by idiosyncratic (often unobservable) character-
istics of individuals. For example, in a medical experiment, individuals who comply with
the treatment may be unobservably dierent from non-compliers. In my experiment, such
non-compliance is present by design. The objective in allocating only a fraction of the treat-
ment precincts to the canvassers was to ensure that they would focus their eorts on the
17


---

treatment precincts in which the potential to win votes was deemed highest. Importantly,
similarly as in an encouragement design, the fact that the assignment of units to the treat-
ment and control groups was entirely random makes it possible to estimate the impact of
the door-to-door campaign causally, despite the fact that not all treatment precincts were
allocated to canvassers. As shown in the empirical strategy in the next subsection, all results
rely on the randomization as the unique source of identication.
Second, randomized experiments typically select the sample in a rst step, and randomly
assign sample units to the treatment and control groups in a second step. These two steps
were not entirely separate in the present experiment. As mentioned above, the rst stratum
of each territory was always included in the randomization, and in a few territories additional
strata were included as well. The unusual aspect is that the decision to include an additional
stratum in the randomization, in a particular territory, depended in part on which precincts
had been assigned to treatment and control in strata already included. The probability that
a second stratum would need to be included was slightly lower when the smallest precinct of
the rst stratum was assigned, by chance, to the control group, than when it was assigned to
the treatment group (as being assigned to the control group increased the likelihood that the
combined number of registered citizens in all treatment precincts of the rst stratum would
be higher than 
TA). The same holds for the likelihood that a third stratum would need to be
included in the randomization, conditionally on having included two strata already, and so on
for the subsequent strata. Importantly, this does not alter the symmetry between treatment
and control precincts in the nal sample.13 In addition, I check the robustness of the results
to restricting the analysis to subsamples dened by the rst stratum of each territory (which,
again, always had to be included in the randomization) or the smallest set of strata of each
13To convince oneself of this, rst consider the set of rst strata of all territories (whether a second stratum
was also included or not). By construction, the assignment of the precincts to the treatment and control
groups in these rst strata was random. Then consider the second stratum of all territories in which a
second stratum was included (whether a third stratum was also included or not). Again, by construction,
the assignment to treatment and control in these second strata was random. The same holds for the group
of third strata, and so on. Therefore, adding all groups of strata together, the assignment of precincts to the
treatment and control groups was random.
18


---

territory which, based on the rule above, would be included in the randomization under
any possible treatment assignment in lower-numbered strata. 14 In these two subsamples,
the separation between sample selection and randomization is satised. The corresponding
tables are included in Appendix C (tables C1 through C3 and C4 through C6, respectively).
All main results are robust to both restrictions.
3.2
Empirical strategy
I estimate the eect of door-to-door canvassing on voter turnout and vote shares at the
2012 presidential election as well as the 2012 parliamentary elections and the 2014 European
elections. To preserve the integrity of the randomization, treatment precincts not allocated
to canvassers are maintained in the treatment group in all regressions. To account for the fact
that not all treatment precincts were allocated to the canvassers, I estimate two parameters
of interest for each electoral outcome. First, I show the eect of a precinct being assigned
to the treatment group (the intent-to-treat eect of the campaign), using the following OLS
specication:
Yi = α1 + β1Ti + X
′
iλ1 +

s
δs
i1 + ϵi1
(1)
where Yi is the outcome in precinct i, Ti is a dummy equal to 1 if the precinct was
assigned to the treatment group and 0 if it was assigned to the control group, δs
i1 are strata
xed eects, and Xi is a vector of controls.
Secondly, I evaluate the eect of a precinct being actually allocated to canvassers (a local
average treatment eect) with the following specication:
14The rst stratum of each territory always falls in this set. The second stratum also falls in this set if,
in the event that the smallest precinct of the rst stratum was assigned by chance to the control group, the
total number of registered citizens in the treatment precincts would remain lower than 
TA. And so on for
the subsequent strata.
19


---

Yi = α2 + β2Ai + X
′
iλ2 +

s
δs
i2 + ϵi2
(2)
where Ai is a dummy equal to 1 if the precinct was allocated to the canvassers and 0
otherwise, and is instrumented with Ti as shown in the following rst-stage equation:
Ai = a + bTi + X
′
iλ +

s
δs
i + νi
(3)
The validity of the 2SLS estimates relies on the fact that the rule used to allocate treat-
ment precincts to canvassers did not generate any deer: of the treatment precincts that
were not allocated to the canvassers, none would have been allocated to them if they had
been in the control group (since no control group precinct was allocated to the canvassers in
the rst place).
In all tables, I present estimates of Equation [1] in Panel A, and estimates of Equation
[2] in Panel B. The key coecients of interest are β1 and β2, which indicate respectively the
eect of the door-to-door visits in precincts that were assigned to the treatment group and
the eect in treatment precincts that were allocated to canvassers. These eects combine
the direct impact of the visits on voters who received them with potential spillovers on other
voters from the same precincts who did not receive the visit but talked to voters who did.
The research design cannot distinguish between direct and indirect impacts.
All regressions use within estimators and robust standard errors. 15 I use three distinct
specications. The rst does not control for any variable except for the strata xed eects.
The second controls for 
PO (the proxy for the potential to win votes), which was used to
15The main tables do not cluster the standard errors since the unit of observation is the same as the
unit of randomization (the precinct). The results are robust to using regular cluster robust standard errors
at the level of the territory or département or allowing for correlation of the error terms at the level of
the départements or the regions with the wild cluster bootstrap procedure (Cameron et al., 2008) and pairs
cluster bootstrap procedure (Esarey and Menger, 2017). All results with clustered standard errors are shown
in Appendix D (Tables D1 through D8).
20


---

construct the strata, as well as a baseline measure of the outcome at the 2007 presidential
election. The third and main specication also controls for the number of registered citizens
as well as the level and the ve-year change of the following census variables: the size of
the municipality; the share of men; the share of the population below 14, between 15 and
29, between 30 and 44, between 45 and 59, between 60 and 74, and above 75; the share
of the working population; and the rate of unemployment. 16 Finally, regressions estimating
the eect of the campaign at the parliamentary elections control for constituency xed ef-
fects to account for dierences in the number and identity of competing candidates across
constituencies.
3.3
Identication of territories which followed the randomization
plan
In each territory, the list of allocated precincts and, when available (and when the ran-
domization had been done at the precinct, not municipality, level), a list of voter addresses
corresponding to these precincts, could be downloaded as Excel les by the eld organizers
from their personal account on the campaign's website. However, a large fraction of ter-
ritories which participated in the door-to-door campaign did not use the list of allocated
precincts, for two main reasons: never getting access to this list, as no eld organizer in
the territory registered on the campaign website and downloaded the list; and local units of
the PS deciding autonomously which areas to cover. In sum, the diculties that even the
most professional campaigns face to control the selection of political activists' demographic
characteristics and ideology (Enos and Hersh, 2015) extended in this election to controlling
where activists campaigned.
16Until 1999, a general census was conducted in the entire country every ve to ten years. Since 2006, the
French national statistics agency (Insee) publishes yearly census results at the municipality level based on
data collected continuously over ve years. For instance, the 2006 census results are based on data collected
from 2004 to 2008. The Insee emphasizes that any evolution should be observed over a span of ve years
or more to ensure that the comparison relies on entirely dierent datasets (Insee, 2014). Accordingly, I use
census results for 2006 and 2011.
21


---

This resulted from the few resources available to the central team to coordinate the
campaign locally, which limited eorts to encourage activists to register on the website and
use the lists prepared by the central team: as mentioned in Section 2.3, the central team
only directly hired and managed 15 regional coordinators. Second, the campaign website
was not as advanced as technological tools used by recent U.S. campaigns. In particular,
it did not provide maps of allocated precincts and did not allow activists to prepare walk
lists for door-to-door sessions organized in these precincts. In U.S. campaigns, such features
foster use of the website and compliance with addresses or precincts deemed priority by
the campaign's analytics team. Instead, in this campaign, many groups of activists found
it easier to campaign in areas that they already knew, including their own neighborhood.
Third, the fact that many local units of the PS came up with their own prioritization of areas
to cover reects the fact that these units preexisted the campaign, and it echoes their culture
of relative autonomy with respect to the hierarchy of the party and, a fortiori, with respect
to the presidential candidate and his central team. Local units which did not follow the list
of allocated precincts instead targeted areas based on their own understanding of electoral
dynamics on their turf and a set of priorities, which included of course the presidential
election, but also gave weight to strategic considerations pertaining to future local races in
which members of the unit would compete.
Estimates of the eects of the campaign in territories that did not use the list of allocated
precincts should be null in expectation, as areas covered in these territories are orthogonal to
randomization. Including these territories in the analysis will decrease precision and may add
noise, due to, for instance, tiny underlying dierences between treatment and control areas,
or non-zero correlation between random assignment and actual coverage in these areas. In
fact, estimates presented in Tables A2 and A3 in Appendix A  that include all territories,
whether or not they used the list of allocated precincts  are close to zero but consistent
with substantial positive or negative eects on turnout and vote shares in territories that
did use the lists.
22


---

Instead, the analysis below uses data from territories that used the list of allocated
precincts and thus actually participated in the experiment. I identify these territories by
combining two independent sources of information: responses to a question included in
the postelectoral online survey on the use of allocated precincts, and daily reports entered
by activists on the campaign website.
Did at least one survey respondent based in the
territory mention that local activists in this territory used the list of allocated precincts? Or
does the territory show at least one report indicating the precinct covered, signalling actual
usage of the campaign website and accountability with respect to precincts allocated by the
campaign's central team? The main results shown below are based on all territories which
verify either the rst or the second criterion.17 For robustness, I also show results based on
sets of territories characterized using only one of the two criteria.
791 territories verify either the rst or the second criterion. This corresponds to 24.3
percent of all 3,260 territories, and 42.3 percent of the corresponding population. In these
791 territories, 966 strata containing 4,674 precincts and 5.02 million registered voters were
included in the randomization.18 80.2 percent (3,748) of the precincts were randomly assigned
to the treatment group and 19.8 percent (926) were assigned to the control group. 57.1
percent (2,139) of the treatment precincts were allocated to canvassers.
Since the randomization was conducted on precincts dened according to the 2011 voter
rolls, all results need to exclude precincts whose boundaries changed between 2011 and 2012.
In addition, specications controlling for past outcomes need to exclude precincts whose
boundaries had changed between 2007 and 2011. As a result, depending on the specication,
the total number of precincts used in the tables is either 3,397 (in specications that do not
17The survey question used to construct the rst criterion was Did you (or your local unit) use the list
of priority polling stations or municipalities that was provided by the campaign? and the possible answers
were I never heard of this list (1), We did not use this list at all, or only very little (2), We used this
list partially (3), and We went to almost all the priority polling stations or cities (4). I consider that the
criterion is satised when at least one survey respondent based in the territory provided the fourth answer.
The results are robust (and nearly identical) to including territories in which at least one survey respondent
provided the third or fourth answer.
18In most (87.6 percent) of the territories, only one stratum was included in the randomization. In 7.3
percent of the territories, two strata were included, and in the remaining 5.1 percent three or more strata
were included.
23


---

control for past outcomes) or 2,665 (in specications that do). 19
3.4
Imperfect compliance
Even in territories that used the lists of allocated precincts, compliance with these lists
remained imperfect. In some cases, the number of canvassers was too small to cover all
allocated precincts, and in others, canvassers covered precincts other than those allocated.
Failure to account for the imperfect compliance with the lists of allocated precincts would
lead to underestimate the impact of the visits.
Therefore, in addition to the eects reported in the tables, of a precinct being assigned to
the treatment group and of a precinct being allocated to the canvassers, which are estimated
using Equations [1] and [2], respectively, I compute a third eect. I scale up raw regression
estimates from Equation [1] by a factor inversely proportional to the dierential intensity of
the campaign in treatment and control precincts: m =
1
fT −fC , where fT (resp. fC) denotes
the fraction of registered citizens that were reached by the campaign in treatment (resp.
control) precincts. This accounts both for the fact that not all treatment precincts were
allocated to the canvassers and for imperfect compliance on the part of canvassers, and it
provides an estimate of the eect of the visits in precincts that were covered by canvassers
and would not have been covered if they had not been assigned to the treatment group. 20
fT and fC can be rewritten as fT = xT N
NT
and fC = xCN
NC , where N is the total number
of registered citizens reached by the campaign, NT (resp. NC ) is the number of registered
citizens in treatment (resp. control) precincts, and xT (resp. xC) is the fraction of doors
knocked that were located in treatment (resp. control) precincts. Since treatment precincts
19Each year, municipalities can add new precincts, merge existing precincts, or move precinct boundaries,
to take into account changes in the number of registered citizens in each neighborhood. The 2011 voter
rolls collected by the PS provide a precise description of precinct boundaries in that year. I further identify
boundaries' changes before and after 2011 based on changes in the number of precincts in a given municipality
as well as changes in the number of registered citizens contained in each precinct.
20I compute this eect (by scaling raw ITT estimates by the multiplier) instead of estimating it with an IV
regression (where precinct coverage would be instrumented by treatment) since available information on the
extent to which a particular precinct was covered is imperfect and missing for a large fraction of precincts.
24


---

include both precincts allocated to canvassers and precincts not allocated to them, fT can
further be rewritten as fT = xT N
NT
= (xT,A+xT, ¯
A)N
(NT,A+NT, ¯
A) , where the subscript T, A (resp. T, ¯A )
designates allocated (resp. non-allocated) treatment precincts.
Therefore,
m = 1
N ×
1
(xT,A+xT, ¯
A)
(NT,A+NT, ¯
A) −xC
NC
(4)
I call m the dierential intensity multiplier. Its size is driven by two factors. The rst
was the decision to allocate only a fraction of the treatment precincts to the canvassers:
if canvassers had fully complied with the corresponding list, then we would have xT,A = 1,
xT, ¯
A = xC = 0, N = NT,A, and the complier would be equal to
NT,A+NT, ¯
A
NT,A
=
NT
NT,A, which is the
ratio between the number of registered citizens in all treatment precincts and in the subset
of treatment precincts allocated to canvassers. The second factor is canvassers' imperfect
compliance with the list of allocated precincts, which further increases the multiplier.
I compute the multiplier for the rst and second rounds separately: m1 and m2. From
voter rolls, in territories which participated in the experiment, NT,A = 2, 486, 941, NT, ¯
A =
1, 613, 156, and NC = 924, 159. Further, using door-to-door reports indicating the precinct
covered, I calculate that, by the second round, 72.5 percent of doors knocked were located in
treatment precincts allocated to canvassers, 14.1 percent in treatment precincts not allocated
to them, and 13.3 percent in control precincts: x2
T,A = 72.5%, x2
T, ¯
A = 14.1%, and x2
C = 13.3%.
Finally, based on the assessment that the door-to-door campaign knocked on the initial target
number of doors overall, N 2 ≃Na, and I get the second round multiplier m2 ≃6.0. Based on
door-to-door reports, contacts which occurred before the rst round account for 76.5 percent
of all doors knocked: N 1 = 0.765 × N 2. In addition, x1
T,A = 73.0%, x1
T, ¯
A = 14.0%, and
x1
C = 13.0%. Thus, I get the rst round multiplier m1 ≃7.3.
Unlike the results from Equations [1] and [2] shown in the tables, the exact magnitude of
the multiplier depends on the accuracy of the canvassers' reports and of the overall scale of
25


---

the campaign N, and it should thus be interpreted with caution. Overestimating N would
mean underestimating m (which is inversely proportional to it) and, thus, underestimating
the eect of the campaign in precincts that were covered by canvassers and would not have
been covered if they had not been assigned to the treatment group.
4
Results
4.1
Verifying randomization
Randomization ensures that all observable and unobservable characteristics should be sym-
metrically distributed between treatment and control precincts. Table 2 veries this for a
series of observed characteristics. It presents summary statistics separately for the control
and treatment groups. I also show the dierence between the means of the two groups and
report the p-value of a test of the null hypothesis that they cannot be distinguished from
each other. Overall, precincts in the two groups are very similar. I regress the treatment
dummy on all characteristics included in Table 2 and test for their joint signicance. I fail to
reject the null (p-value of 0.97). One of the dierences shown in Table 2 is signicantly dif-
ferent from zero at the 5 percent level, however: the number of registered citizens, a variable
which can be particularly important for turnout. For all results shown below, I include this
variable as a control in one of the specications. This has only a minimal impact, including
in regressions measuring the impact on turnout. The results are also robust to trimming the
5 or 10 percent of precincts with the largest number of registered citizens (Tables included
in Appendix E).
The average precinct contained 1,110 registered citizens. All 22 metropolitan French
regions were represented in the sample. The municipality of the average precinct contained
67,000 citizens. In the municipality of the average precinct, 49 percent of the inhabitants
were men, 36 percent were under 30 years old, 40 percent were between 30 and 60 years old,
and 24 percent were older than 60. The working population accounted for 72 percent of all
26


---

people aged 15 to 64, of which 12 percent were currently unemployed, and median income
was about 19,000 euros.
Finally, baseline participation, measured at the 2007 presidential election, was 84 percent,
and the vote share of the PS candidate, Ségolène Royal, was 28 percent at the rst round
and 52 percent at the second round of this election. Treatment precincts are slightly more
to the left, and characterized by a slightly lower participation than control precincts. Given
the high correlation between electoral outcomes in the past and present, most specications
in the analysis below control for baseline electoral outcomes.
4.2
First stage
As discussed in Section 3.1, not all treatment precincts were allocated to the canvassers. In
all tables that follow, I present estimates of Equation [1], which evaluates the eect of a
precinct being assigned to the treatment group, in Panel A, and estimates of Equation [2],
which evaluates the eect of a precinct being allocated to canvassers, in Panel B. Equation
[2] instruments the dummy allocated to canvassers with the treatment assignment dummy.
The estimation of the corresponding rst stage equation (Equation [3]) is presented in Table
3.
I control for strata xed eects in column 1, and nd a rst stage of 0.565. In addition
to strata xed eects, columns 2 through 7 also control for variables included in some of the
2SLS specications: past outcome (turnout of PS vote share at the rst round, second round,
or averaged over both rounds of the 2007 presidential elections), and additional controls (the
number of registered citizens in the precinct or municipality, as well as the level and the
ve-year change of the census variables). All estimates are signicant at the 1 percent level,
and similar in size.
27


---

4.3
Eects on the 2012 presidential election
4.3.1
Voter turnout
The impact of the door-to-door visits on voter turnout in the 2012 presidential election
is analyzed in Table 4. I use as the outcome voter turnout in the rst round (columns 1
through 3), in the second round (columns 4 through 6), and averaged over the two rounds
(columns 7 through 9). In the control group, 79.5 and 80.1 percent of the voters participated
in the rst and second rounds. Door-to-door canvassing had no signicant eect on voter
turnout in either the rst or the second round. The point estimates are relatively small in all
specications, whether or not control variables are included. Considering the upper bound of
the 95 percent condence interval, I can reject any eect higher than 0.40 percentage points
in the rst round at the 5 percent level and any eect higher than 0.20 percentage points in
the second round, in the specication including all controls (columns 3 and 6). I do not nd
any signicant impact of the door-to-door visits either on subsamples of territories identied
as following the list of allocated precincts based only on canvassers' reports (Table B2 in
Appendix B) or their answers to the postelectoral survey (Table B5).
4.3.2
Vote shares obtained by François Hollande
I now examine the impact of door-to-door canvassing on the vote shares obtained by François
Hollande. As shown in Table 5, François Hollande obtained 31.6 percent of the votes in
the control group in the rst round and 57.6 percent in the second round. In treatment
precincts, the door-to-door visits increased his vote share by 0.63 percentage points in the
rst round (Panel A, column 1) and by 0.48 percentage point in the second round of the
presidential election (column 4). These estimates are signicant at the 1 and 10 percent
level respectively. When I control for past outcomes, 
PO, the number of registered citizens,
and census variables, I obtain estimates of 0.44 and 0.46 percentage points at the rst and
second rounds, both signicant at the 5 percent level (columns 3 and 6). In precincts that
28


---

were actually allocated to canvassers, the eects were 0.84 and 0.87 percentage points (Panel
B, columns 3 and 6). Applying the rst and second rounds dierential intensity multipliers
computed in Section 3.4 to Panel A's ITT estimates, I obtain eects of 3.24 percentage
points and 2.75 percentage points in the rst and second rounds. This measures the impact
of the visits in precincts that were covered by canvassers and would not have been covered
if they had not been assigned to the treatment group. Again, I check the robustness of
the results to restricting the sample to territories identied as following the list of allocated
precincts based only on canvassers' reports (Table B3 in Appendix B) or their answers to
the postelectoral survey (Table B6). In the rst subsample, the eect of the door-to-door
visits was 0.29 and 0.35 percentage points in the rst and second rounds, but only the latter
estimate is signicant (at the 10 percent level). In the second subsample, the eects were
0.76 and 0.50 percentage points, but only the former estimate is signicant (at the 5 percent
level).
4.3.3
Vote shares of other candidates
The correlate of the positive eect of door-to-door canvassing on the vote share obtained by
François Hollande in the rst round is a negative eect on the vote shares of other candidates.
In Table 6, I assess the extent to which the dierent candidates were aected.
Columns 1 and 2 are identical to columns 1 and 3 of Table 5, and they are included for
reference only. The combined eect of the door-to-door visits on the vote shares of the right-
wing candidates Nicolas Sarkozy and Nicolas Dupont-Aignan was negative, slightly smaller
than the eect on Hollande's vote share (=0.43 percentage points), and signicant at the 1
percent level (Panel A, column 10). Scaled by the dierential multiplier, this corresponds to
an eect of -3.14 percentage points. Instead, the eect on the vote shares of the candidates
of the far-left (Philippe Poutou and Nathalie Arthaud) was close to 0 (column 4). The eect
on vote shares of the centrist candidate, François Bayrou, and of other left-wing candidates
(Eva Joly and Jean-Luc Mélenchon) was negative but not statistically signicant (columns
29


---

6 and 8). The eect on the vote share of the far-right candidate, Marine Le Pen, was also
small and non-signicant, although positive (column 12).
4.4
Eects on the 2012 parliamentary elections and the 2014 Euro-
pean elections
4.4.1
Voter turnout
I now investigate whether the eects of the visits were short-lived or whether they persisted
in the rst and second rounds of the 2012 parliamentary elections, which took place one
month after the presidential, and in the 2014 European elections, which took place two years
later. Tables 7 and 8 examine the eects on voter turnout and on the vote shares of PS
candidates, respectively.
As expected, I nd a signicant eect on voter turnout neither in the parliamentary
(Table 7, columns 3 and 4) nor the European elections (column 5).
4.4.2
Vote shares of candidates of the Parti Socialiste
I now examine the impact of the visits on vote shares of PS candidates. Columns 1 and
2 of Table 8 are identical to columns 3 and 6 of Table 5. They show the impact of the
door-to-door visits on François Hollande's vote shares at the 2012 presidential election and
are included for reference only. This eect translated into eects of 0.94 and 0.73 percentage
points, signicant at the 1 percent level, on the vote share of PS candidates in the rst and
second rounds of the 2012 parliamentary elections (Panel A, columns 3 and 4). Remarkably,
part of the eect persisted in the 2014 European elections, although the point estimate of
0.37 percentage points is only signicant at the 10 percent level (column 5).
While columns 1 through 5 use expressed votes as the denominator to compute vote
shares, columns 6 through 10 use registered voters as the denominator. Dierently from
participation and expressed votes, the number of registered voters is stable across elections.
30


---

Thus, although a less common and intuitive outcome, vote shares dened as a fraction
of registered voters  instead of expressed votes  facilitates the comparison of the eect
size across elections. Most of the eect of the visits on the vote share of Hollande in the
presidential election persisted in the parliamentary elections one month later: the eect at
the rst round of these elections was even slightly larger (0.42 percentage points against 0.35
percentage points for the rst round of the presidential election), but it was smaller and
non-signicant at the second round. Persistence two years later at the European elections
was smaller (0.17 percentage points, or about 47 percent of the original eect)  and using
this denition of vote shares, the eect is no longer statistically signicant.
4.5
Placebo checks on the 2007 presidential elections
I conduct a placebo exercise using results from the 2007 presidential elections. I run the
three exact same specications as for the main results. For sociodemographic controls, I use
2006 data (instead of the 2011 controls used in the main regressions). For past outcomes,
I control for the results of the 2002 presidential elections. All regressions exclude precincts
whose boundaries were changed between 2007 and 2011.
Regressions controlling for the
2002 outcomes also exclude precincts whose boundaries were changed between 2002 and
2007. Table 9 shows the impact on turnout and Table 10 the impact on Ségolène Royal's
vote share (the candidate of the Parti Socialiste at the 2007 presidential elections).
In the second round of the 2007 elections, turnout and Royal's vote share were very
close in treatment and control precincts. The dierence is close to 0 and not statistically
signicant across all three specications shown in columns 4 through 6 of Tables 9 and 10.
The stratication of the randomization on the potential to win votes, itself estimated based
on the 2007 second round results, ensured symmetry of the treatment and control groups on
these outcomes.
In the rst round of the 2007 elections, instead, turnout was lower and Royal's vote share
31


---

higher in treatment precincts. These dierences are signicant at the 10 percent level in
the specication controlling only for strata xed eects (column 1). They are no longer
statistically signicant when controlling for past outcome and additional controls (column
3). In particular, controlling for past outcome, the dierence in Royal's vote share in the
rst round is close to 0 (Table 10, columns 2 and 3), showing that rst round voting behavior
was not on dierential trends in the treatment and control precincts. Thus, the 2012 and
2014 rst round results shown above, which control for the 2007 outcomes, should not be
driven by underlying dierences.
Averaging over both rounds, neither turnout nor Royal's vote share are signicant in any
of the specications (columns 7 through 9). Controlling for past outcomes and additional
controls, the dierence between treatment and control precincts is very close to zero.
5
Interpretation of the results
5.1
Eect on the overall election outcome
Point estimates of the eects of the door-to-door visits on the vote shares of François Hol-
lande and Nicolas Sarkozy at the rst round of the presidential elections are 3.24 and -3.14
percentage points respectively in precincts that were covered by canvassers and would not
have been covered had they not been assigned to the treatment group. 21 Assuming that the
impact was of same magnitude in all precincts covered, and since the canvassers covered ap-
proximately 11 percent of all French households before the rst round and 15 percent before
the second round, I obtain that the door-to-door canvassing campaign increased François
Hollande's national vote share by 0.37 percentage points in the rst round of the presiden-
tial elections and that it decreased Nicolas Sarkozy's vote share by 0.36 percentage points.
Overall, it thus accounted for about one half of Hollande's 1.45 percentage point lead in the
rst round.
21As discussed in Section 4.3.2, these eects are computed by applying the rst and second rounds dier-
ential intensity multipliers to ITT estimates.
32


---

The eect on Hollande's vote share in the second round was 2.75 percentage points,
implying an increase of his national vote share by 0.41 percentage points. Since there were
only two candidates in the second round, it was automatically mirrored by a negative eect
of the same size on the vote share of Sarkozy: in total, the visits increased Hollande's victory
margin by 0.83 percentage points. Since Hollande won with 51.6 percent of the votes, against
48.4 for Sarkozy, the eect of door-to-door canvassing accounted for about one fourth of the
victory margin.
Finally, taking into account the imperfect compliance and the fraction of addresses cov-
ered, I estimate that door-to-door canvassing increased PS candidates' vote shares by 0.66
percentage points, on average, in the second round of the parliamentary elections. This is
by no means negligible: PS candidates won by an even lower margin in 5.9 percent of the
constituencies (15 out of 254) in which they won in the second round.
5.2
Persuasion vs. mobilization
Two mechanisms could explain the impact on the vote share of François Hollande: the
persuasion of undecided active voters (who would have voted for another candidate absent
the visits) and the mobilization of left-wing non-voters (who would have stayed home).
To assess the importance of the second mechanism, I use a seemingly unrelated regressions
(SUR) framework, compare the impact on turnout and on vote shares, and test the hypothesis
that they are equal. I use the number of registered citizens as the denominator for both
outcomes, to ensure their comparability. The results are shown in Table G1 in Appendix G.
The eect on voter turnout was negative in the second round but positive in the rst round,
where it corresponds to 30.5 percent of the eect on vote share (column 3). Imprecision
in the point estimates implies that the real contribution of the mobilization channel may
of course have been larger. However, it is unlikely to explain all the vote share increase: I
reject (at the 5 or 10 percent level) the null hypothesis that the eects on turnout and vote
33


---

shares were equal, in all but one specication. These results suggest that the increase in
Hollande's vote share was driven by persuasion more than by the mobilization of left-wing
non-voters.22
An alternative interpretation is possible. The door-to-door visits may have demobilized
right-wing voters at the same time as they increased participation on the left, translating into
small net eects on turnout but large eects on vote shares. By improving the short-term
opinions of François Hollande, visits from canvassers may have contradicted the partisan
predispositions of supporters of other candidates and generated psychological tension (Fio-
rina, 1976). One response to cognitive dissonance is to avoid situations likely to increase
it (Festinger, 1957, 1962)  which in this context would be to forego voting in the election.
It is dicult to disentangle these two interpretations using aggregate data, but for a few
reasons demobilization of other candidates' supporters, while not entirely implausible, seems
less likely than persuasion. First, existing experiments nd that partisan eld campaigns
increase turnout among supporters of other parties or leave it unaected, not that they de-
crease it (Nickerson, 2005; Arceneaux and Kolodny, 2009; Foos and de Rooij, 2017). Second,
while negative political ads can decrease voter turnout in certain contexts (Ansolabehere et
al. 1994; Krupnikov 2011; but see Wattenberg and Brians, 1999; Goldstein and Freedman,
2002), the campaign relied on positive rather than negative arguments, as can be seen in the
toolkit and eld organizers' guide included in Appendix H (Figures H1 and H2), consistent
with the emphasis put on the mobilization of left-wing supporters. Third, of all types of
voters, those that could have been deemed most likely to feel cross-pressured after the visit of
François Hollande's canvassers are probably the supporters of Marine Le Pen. Indeed, many
voters of the Front National are former voters of the left, and many maintain leftist prefer-
22This interpretation may seem at odds with the fact that the campaign gave priority to the mobilization of
left-wing supporters. However, any precinct allocated to canvassers represents several hundreds of registered
citizens. As a consequence, in each precinct, these citizens display a wide array of proles. In particular, even
in precincts with a large number of left-wing nonvoters, a majority of voters participate in the presidential
elections, and many of them vote for right-wing candidates. In sum, although the main target of the campaign
were left-wing nonvoters, only a minority of the people with whom the canvassers interacted corresponded
to this type.
34


---

ences on economic issues (Perrineau, 2005; Mayer, 2011). 23 The visits could have awakened
this past loyalty and created a tension with the voters' new allegiance to the far-right. But as
shown in Section 4.3.3, the visits did not decrease the vote share of the far-right candidate.
If indeed the eects were obtained by persuading swing voters to vote left, what fraction
were persuaded? Since 48 percent of the doors knocked by canvassers opened, I scale the
point estimates by
1
0.48 and nd that 6.7 percent and 5.7 percent of the voters living in
households that opened their door were persuaded to vote for François Hollande in the rst
and second rounds of the presidential elections.24 Applying the denition of persuasion rate
proposed by DellaVigna and Kaplan (2007), I compare these fractions to the fractions of
control group voters who supported candidates other than François Hollande in the rst and
second rounds (respectively 70.1 percent and 44.0 percent). I compute that the fraction of
voters who changed their behavior in response to the visits were 9.6 percent and 13.0 percent
respectively. These persuasion rates are of the same order of magnitude as those measured
by studies that examine the impact of door-to-door canvassing on the decision to vote or not
(see DellaVigna and Gentzkow, 2010). For instance, using turnout as their outcome, Gerber
and Green (2000) and Green et al. (2003) nd persuasion rates of door-to-door canvassing
of 15.6 percent and 11.5 percent respectively. The persuasion rates obtained in the present
23In the one-dimensional representation of the political spectrum, the localization of the FN on the far right
makes it the party most distant from the PS. But in France as in most Western European countries and the
U.S., the left-right split has not one, but at least two dimensions, sociocultural and economic, which overlap
only imperfectly (e.g., Lipset, 1959; Fleishman, 1988; Knutsen, 1995). On the sociocultural dimension, the
platforms of the FN and the PS are diametrically opposed: vehement anti-immigrant positions and a model of
authoritarian and closed society on one side; a pro-immigration stance and a model of open and libertarian
society on the other (e.g., Pettigrew, 1998; Arzheimer, 2009; Mayer, 2013). On the economic dimension,
however, the distance between the FN and the PS, which traditionally promotes state interventionism against
economic liberalism, is much smaller. It has further decreased since Marine Le Pen succeeded her father
as the leader of the FN in 2011.
Her program for the 2012 election asked for a more protective state
and more public services  two points that closely echoed the program of the PS. Together with anti-elite
stances directed against the corrupt political establishment and the privileged few, this economic platform
was designed to attract blue-collar workers, mid-level employees, and other groups exposed to unemployment
and precariousness, which until recently largely supported the left.
24This scaling assumes, rst, that on average households that opened their doors contained as many
registered citizens as those that did not, and it considers as treated all citizens living in a household that
opened its door, regardless of whether or not they interacted personally with the canvasser. Second, I assume
that the precinct-level eects of the visits were driven by voters (and household members) who received them,
and not by spillovers on voters who did not interact with canvassers but were persuaded by talking with
voters who did.
35


---

experiment also compare with those associated with new exposure to media  4.4, 11.6,
and 7.7 percent for TV (Gentzkow, 2006; DellaVigna and Kaplan, 2007; Enikolopov et al.,
2011), 19.5 and 12.9 percent for newspaper (Gerber et al., 2009; Gentzkow et al., 2011)  and
they are substantially higher than the persuasion rates of all of a candidates' combined TV
advertising (an average 0.7 percent in Spenkuch and Toniatti (2016)) or political endorsement
by a newspaper (an average 4.3 percent in Chiang and Knight (2011)).
5.3
Beliefs vs. preferences
Persuasion can aect behavior through dierent mechanisms (DellaVigna and Gentzkow,
2010). Canvassers may have persuaded voters by changing their preferences on some po-
litical issues or by changing their beliefs about the quality of Hollande. The short average
length of the visits makes the rst mechanism unlikely.
The fact that most voters that
were canvassed had never been visited by a political activist before (Lefebvre, 2016) makes
the second mechanism more plausible: these novel and surprising visits sent a strong signal
about the quality of the PS and its candidate. According to this interpretation, the voters
were persuaded by the signal sent by the canvassers' presence more than by their specic
arguments.
Door-to-door canvassing contrasted with the idea that the political world is
solely populated by politicians who do not care about what voters think. 25 It showed that
Hollande and his supporters were willing to bridge the gap with voters and it put forth the
image of the PS as a modern and innovative party.
This interpretation is in line with theories of costly signalling such as laid out by Coate
and Conlin (2004), where voters do not know whether candidates are qualied and candidates
use campaign resources to convey information about their qualications. Although I cannot
directly test this interpretation, the eects of the visits on the vote shares of other candidates
of dierent political aliations provide some (granted, limited) empirical support. As shown
25According to a survey conducted after the 2012 presidential elections, 71 percent of French people feel
that politicians care little or not at all about what they think and 66 percent do not trust political parties
(Cevipof, 2012).
36


---

in Section 4.3.3 and Table 6, the visits decreased the vote shares of right-wing candidates
by 0.43 percentage points, which is almost as large as the eect on Hollande's vote share
(0.44 percentage points) and much larger than the eect on the vote shares of other left-
wing candidates (- 0.11 percentage points).
The eect, compared to vote shares in the
control group, is more than twice as large for right-wing candidates than other left-wing
candidates. Again using the SUR framework, I cannot reject that the eects were the same
(p-value of 0.21, as shown in Table G2, column 4). It remains that, taken at face value, the
estimates suggest the increase of Hollande's vote share was obtained by taking votes from
right-wing candidates more than from other left-wing candidates.
But right-wing voters
were ideologically more distant from Hollande. They could thus be deemed less susceptible
to align their preferences with his political agenda than voters supporting other left-wing
candidates, who oered a closer ideological platform. This again makes it less likely that
voters' political preferences changed, and more likely that their beliefs about the PS and its
candidate did.
5.4
Mechanisms underlying eect persistence
I nally discuss the persistence of the eect of the visits on vote shares obtained by left-wing
candidates. Nearly all the original eect carried over to the 2012 parliamentary elections
which took place one month later. This suggests that most voters persuaded by the visits
were active voters, who participated not only in the presidential election but also in these
lower salience elections, and that they were consistent in who they voted for. In addition,
around 40 percent of the original eect carried over to the 2014 European elections. Although
at the margin of statistical signicance, this nding is perhaps all the more striking as the
PS suered an important defeat in the latter elections.
The persistence of the eect in the parliamentary and European elections can come from
two main channels, direct and indirect. First, the direct eect of the visits may have been
37


---

long-lived: it is possible that the canvassers durably changed voters' beliefs about the quality
of the PS (or changed voters' preferences). Second, voting for a PS candidate today may in
itself increase the likelihood to vote for a PS candidate in the future. Multiple mechanisms
may explain this habit formation, including cognitive dissonance (Festinger, 1957, 1962),
or increased expressive utility of voting for this particular party. 26 Existing evidence that
documents persistence of electoral behavior has mostly focused on voter turnout (Gerber
et al., 2003; Meredith, 2009; Davenport et al., 2010; Garcia Bedolla and Michelson, 2012;
Fujiwara et al., 2016). While estimates of the magnitude of persistence dier, Fujiwara et
al. (2016) nd that habit formation alone can generate near-to-full persistence of the impact
of rainfall shocks on participation four years later. Beyond voter turnout, Mullainathan and
Washington (2009) and Kaplan and Mukand (2014) nd, respectively, long-lasting eects of
participation in U.S. presidential elections on presidential opinion ratings, and persistence of
the eect of 9/11/01 attacks on party of registration. Our study complements this literature
by showing that transitory shocks to vote choice can generate persistent eects as well.
This result contrasts with Gerber et al. (2011) who nd rapid decay of the eects of TV
and radio ads on voting preferences, with two possible interpretations. The rst is that the
personal and interactive aspects of the door-to-door visits generate direct eects of a dierent
nature than TV ads: while the latter only prime evaluative criteria, as hypothesized by the
authors, the former actually change voters' views, with consequences lasting after the contact
26Two additional mechanisms may have contributed to the large eects at the parliamentary elections,
even though they are unlikely to account for the bulk of them. The rst is that the impact of the campaign
may have interacted with Hollande's victory: while some voters were directly persuaded by the visits, others
may have only been persuaded to vote on the left after they witnessed Hollande's victory, for instance
because after the canvassers' visit they remained reluctant to vote left out of disbelief that the left had any
chance to win the elections. The second is that some canvassers engaged in door-to-door canvassing between
the presidential and parliamentary elections and that they disproportionately covered treatment precincts.
While the list of precincts and addresses allocated to canvassers remained available only until the presidential
election, some activists who had canvassed these areas before the presidential election may have returned
there and canvassed them again before the parliamentary elections. Note however that the opposite may
have happened too (canvassers going to areas which they had not been allocated during the presidential
campaign, in an eort to cover their entire territory) and that the campaign for the parliamentary elections
was of a much lower intensity than the presidential campaign. Additional canvassing is even less likely to
explain the (lower) persistence at the European elections, where the intensity of the eld campaign was much
lower still.
38


---

was forgotten. The second interpretation is that direct eects of both types of campaigning
on voter preferences are short lived, and that persistence mostly comes from the indirect vote
choice channel. While the campaign studied in this paper continued until the day before the
election and did aect vote choice in that election, the advertisement campaign evaluated
by Gerber et al. (2011) stopped nine months before and likely failed to aect decisions,
preventing persistence through vote choice.
6
Conclusion
This paper reports the results of a countrywide eld experiment conducted during François
Hollande's door-to-door campaign in the 2012 French presidential election. The campaign
spanned all French regions, encompassed very dierent types of areas, from Paris to rural
villages, and reached an estimated ve million households. The study contributes to a large
literature on the drivers and eects of persuasive communication, and extends it in three
important directions.
First, while targeted appeals transmitted in one-on-one discussions have been repeatedly
found eective in increasing voter participation, the existing evidence comes from framed
eld experiments which can carefully select the agents carrying out these interventions, and
control the content of their conversations. Results obtained in these settings may not fully
extend to large-scale campaigns like the one studied here, which typically lack such control,
even when they are managed very professionally (Enos and Hersh, 2015). Second, and more
important, the large scale of the experiment enabled, for the rst time, randomization to
be conducted at the precinct level while maintaining high statistical power. Unlike in prior
studies randomized at the individual or household level, I can thus measure the impact of the
door-to-door visits both on voter turnout and on actual vote shares, using ocial precinct-
level election results. This provides the rst hard evidence that door-to-door campaigns
actually aect electoral outcomes, and constitutes perhaps the main contribution of this
39


---

paper.
Third, I discuss important challenges inherent to embedding an experiment in a
large campaign and ways to address them eectively. For the implementing organization,
the cost of giving up on covering areas deemed strategic but allocated to the control group
may be particularly dissuasive when stakes are as high as during a presidential electoral
campaign. The randomization rule was thus designed to ensure that precincts allocated
to canvassers had the highest possible expected potential to win votes compatible with
running an experiment. In addition, resources to ensure that all local units of the Parti
Socialiste and the estimated 80,000 activists who took part in the campaign downloaded
the lists of allocated precincts and followed these lists were scarce, creating a threat for
the implementation of the randomization plan. I combine two independent data sources 
reports entered by local activists on the campaign website and answers to a postelectoral
survey  to identify which territories used the list of allocated precincts. Estimates of the
impact of the campaign are comparable in the sets of territories identied based on either of
these datasets.
In the combined sample of 791 territories that participated in the experiment, accounting
for 5.02 million registered voters, I nd that door-to-door canvassing did not signicantly
aect voter turnout but increased François Hollande's vote share by 3.24 percentage points
in the rst round of the election and 2.75 percentage points in the second in precincts that
were covered by canvassers and would not have been covered if they had not been assigned
to the treatment group.
Assuming that the eect was of similar magnitude in all areas
covered by the campaign, this accounted for approximately one half of Hollande's lead in
the rst round and one fourth of his victory margin at the second round. At the same time,
the intervention decreased the vote share obtained by the right-wing candidates, with no
signicant eects on the vote shares of other candidates in the center, on the left, or on the
far-right. Although several interpretations for this are possible, the most plausible is that the
eects were obtained by persuading swing voters to vote left, rather than by mobilizing left-
wing nonvoters or demobilizing opponents. The eect of the doorstep discussions persisted
40


---

in the 2012 parliamentary elections, which took place one month later  and even to the
2014 European elections, though the eect is far weaker.
These results are surprising, given that the campaign material and instructions, though
mentioning the right-wing incumbent Nicolas Sarkozy, focused on the mobilization of left-
wing nonvoters. The lack of mobilizing impact of door-to-door canvassing also stands in
contrast to the ndings of most previous eld experiments conducted in a variety of con-
texts and countries, including during a partisan door-to-door campaign in France (Pons
and Liegey, 2016). It may be explained by the very high salience that characterizes French
presidential elections. A review of U.S. experimental results conducted by Arceneaux and
Nickerson (2009) nds that the eectiveness of door-to-door outreach is conditioned by vot-
ers' baseline propensity to vote. In the context of high-turnout elections, campaigns can
mobilize low-propensity voters. But even in presidential elections, voter turnout is much
lower in the U.S. than in the context of this study. The level of political awareness is high
in French presidential elections, and encouragement to vote by friends and family members
at its peak. As a result, there may simply have been no one left to mobilize.
On the other hand, the large persuasion impact of the campaign suggests that one-on-
one discussions have a strong potential to shift people's decisions even when the principal's
control on the campaign's agents is limited. This nding may have implications that reach
beyond political campaigns to persuasive communication directed at consumers, donors, or
investors. Further research should test systematically the generalizability of these ndings by
identifying the conditions under which one-on-one discussions and other modes of persuasion
are most eective. In the current context, two dimensions may have contributed to the
large persuasion impact of door-to-door canvassing. First, the signal of quality sent by the
visits may have mattered more than the actual content of the discussions, and it may have
been all the stronger, as most voters contacted by the campaign had never been canvassed
before. Conversely, the eect of persuasive communication may dampen as a larger number
of political parties or companies engage in one-on-one discussions with voters or consumers.
41


---

Second, the diversity of political parties and platforms in France results in weaker partisan
aliations and more frequent changes in vote choice than in bipartisan contexts, such as in
the U.S. Further research could test whether the persuasion eect varies negatively with the
intensity of preexisting voters' partisan aliations or preexisting consumers' attachment to
specic brands.
42


---

References
Adena, Maja, Ruben Enikolopov, Maria Petrova, Veronica Santarosa, and Ekate-
rina Zhuravskaya, Radio and the Rise of the Nazis in Prewar Germany, The Quarterly
Journal of Economics, 2015, 130 (4), 18851939.
Aker, Jenny C., Paul Collier, and Pedro Vicente, Is Information Power? Using Cell
Phones during an Election in Mozambique, World Development, 2011, (May), 153.
Ansolabehere, Stephen, Shanto Iyengar, Adam Simon, and Nicholas Valentino ,
Does Attack Advertising Demobilize the Electorate?, The American Political Science
Review, 1994, 88 (4), 829838.
Arceneaux, Kevin, Using Cluster Randomized Field Experiments to Study Voting Be-
havior, The Annals of the American Academy of Political and Social Science, sep 2005,
601 (1), 169179.
, I'm Asking for Your Support: The Eects of Personally Delivered Campaign Messages
on Voting Decisions and Opinion Formation, Quarterly Journal of Political Science, 2007,
2 (1), 4365.
and David W. Nickerson, Who is Mobilized to Vote?
A Re-Analysis of Eleven
Randomized Field Experiments, American Journal of Political Science, 2009, 53 (1),
116.
and
, Comparing Negative and Positive Campaign Messages: Evidence From Two
Field Experiments, American Politics Research, 2010, 38 (1), 5483.
and Robin Kolodny, Educating the least informed: Group endorsements in a grass-
roots campaign, American Journal of Political Science, 2009, 53 (4), 4365.
Arzheimer, Kai, Contextual factors and the extreme right vote in Western Europe, 1980-
2002, American Journal of Political Science, 2009, 53 (2), 259275.
Ashworth, Scott and Joshua D. Clinton, Does Advertising Exposure Aect Turnout?,
Quarterly Journal of Political Science, 2007, 2 (August 2005), 2741.
43


---

Atkeson, Lonna Rae, Sure, I Voted for the Winner! Overreport of the Primary Vote
for the Party Nominee in the National Election Studies, Political Behavior, 1999, 21 (3),
197215.
Bailey, Michael, Daniel J. Hopkins, and Todd Rogers, Unresponsive and Unper-
suaded: The Unintended Consequences of Voter Persuasion Eorts, Political Behavior,
may 2016, 38, 134.
Banerjee, Abhijit V., Arun G. Chandrasekhar, Esther Duo, and Matthew O.
Jackson, The diusion of micronance, Science, 2013, 341 (6144), 1236498.
, Esther Duo, and Rachel Glennerster, Putting a Band-Aid on a Corpse: Incentives
for Nurses in the Indian Public Health Care System, Journal of the European Economic
Association, jan 2008, 6 (2-3), 487500.
, Selvan Kumar, Rohini Pande, and Felix Su, Do informed voters make better
choices? Experimental evidence from urban India, Working paper, 2011.
Barton, Jared, Marco Castillo, and Ragan Petrie, What Persuades Voters? A Field
Experiment on Political Campaigning, Economic Journal, 2014, 124 (574), 293326.
Bergan, Daniel E., Alan S. Gerber, and Donald P. Green, Grassroots mobilization
and voter turnout in 2004, Public Opinion Quarterly, 2005, 69 (5), 760777.
Bobonis, Gustavo J. and Frederico Finan, Neighborhood Peer Eects in Secondary
School Enrollment Decisions, Review of Economics and Statistics, 2009, 91 (4), 695716.
Bond, Robert M., Christopher J. Fariss, Jason J. Jones, Adam D. I. Kramer,
Cameron Marlow, Jaime E. Settle, and James H. Fowler, A 61-million-person
experiment in social inuence and political mobilization, Nature, 2012, 489 (7415), 295
298.
Broockman, David E. and Donald P. Green, Do Online Advertisements Increase
Political Candidates' Name Recognition or Favorability? Evidence from Randomized Field
Experiments, Political Behavior, 2014, 36 (2), 263289.
and Joshua Kalla, Durably reducing transphobia: A eld experiment on door-to-door
canvassing, Science, 2016, 352 (6282), 220224.
44


---

Cameron, A. Colin, Jonah B. Gelbach, and Douglas L. Miller, Bootstrap-Based
Improvements for Inference with Clustered Errors, Review of Economics and Statistics,
2008, 90 (3), 414427.
Campante, Filipe, Ruben Durante, and Francesco Sobbrio, Politics 2.0: the Mul-
tifaceted Eect of Broadband Internet on Political Participation, NBER Working Paper
19029, 2014, (April).
Campbell, James E., Explaining Politics, Not Polls: Reexamining Macropartisanship
with Recalibrated NES Data, Public Opinion Quarterly, 2010, 74 (4), 616642.
Cardy, Emily Arthur, An Experimental Field Study of the GOTV and Persuasion Ef-
fects of Partisan Direct Mail and Phone Calls, The Annals of the American Academy of
Political and Social Science, sep 2005, 601 (1), 2840.
Cevipof, Enquête post-électorale de l'élection présidentielle 2012 CEVIPOF, 2012,
(http://www.cevipof.com/fr/2012/recherche/postelect).
Chiang, Chun Fang and Brian Knight, Media bias and inuence: Evidence from
newspaper endorsements, Review of Economic Studies, 2011, 78 (3), 795820.
Chong, Alberto, Ana L. De La O, Dean Karlan, and Leonard Wantchekon , Does
Corruption Information Inspire the Fight or Quash the Hope? A Field Experiment in
Mexico on Voter Turnout, Choice, and Party Identication, Journal of Politics, 2015, 77
(1), 5571.
Coate, Stephen and Michael Conlin, A Group Rule: Utilitarian Approach to Voter
Turnout: Theory and Evidence, American Economic Review, 2004, 94 (5), 14761504.
Collier, Paul and Pedro C. Vicente, Votes and Violence: Evidence from a Field Ex-
periment in Nigeria, Economic Journal, 2014, 124 (574), 327355.
Conley, Timothy G. and Christopher R. Udry, Learning about a New Technology:
Pineapple in Ghana, American Economic Review, 2010, 100 (1), 3569.
Davenport, Tiany C., Alan S. Gerber, Donald P. Green, Christopher W.
Larimer, Christopher B. Mann, and Costas Panagopoulos, The enduring eects
45


---

of social pressure: Tracking campaign experiments over a series of elections, Political
Behavior, 2010, 32 (3), 423430.
DellaVigna, Stefano and Ethan Kaplan, The Fox News Eect: Media Bias and Vot-
ing, Quarterly Journal of Economics, 2007, 122 (3), 11871234.
and Matthew Gentzkow, Persuasion: Empirical Evidence, Annual Review of Eco-
nomics, 2010, 2, 643649.
, John A. List, Ulrike Malmendier, and Gautam Rao, Voting to Tell Others,
Review of Economic Studies, 2017, 84, 143181.
Dewan, Torun, Macartan Humphreys, and Daniel Rubenson, The elements of
political persuasion: Content, Charisma and Cue, Economic Journal, 2014, 124 (574),
257292.
Druckman, James N., Political Preference Formation: Competition, Deliberation, and
the (Ir)relevance of Framing Eects, The American Political Science Review, 2004, 98
(4), 671686.
Duo, Esther and Emmanuel Saez, The role of information and social interactions in
retirement plan decisions: Evidence from a randomized experiment, Quarterly Journal of
Economics, 2003, 118 (3), 815842.
Elster, Jon, Deliberative Democracy, Cambridge, UK: Cambridge University Press, 1998.
Enikolopov, Ruben, Maria Petrova, and Ekaterina Zhuravskaya, Media and Po-
litical Persuasion: Evidence from Russia, American Economic Review, 2011, 101 (7),
32533285.
Enos, Ryan D. and Eitan D. Hersh, Party Activists as Campaign Advertisers: The
Ground Campaign as a Principal-Agent Problem, American Political Science Review,
2015, 109 (2), 252278.
Esarey, Justin and Andrew Menger, Practical and Eective Approaches to Dealing
with Clustered Data, Political Science Research and Methods, 2017.
46


---

Falck, Oliver, Robert Gold, and Stephan Heblich, E-Lections: Voting Behavior and
the Internet E-Lections: Voting Behavior and the Internet, American Economic Review,
2014, 104 (7), 22382265.
Farrar, Cynthia, Donald P. Green, Jennifer E. Green, David W. Nickerson, and
Steven Shewfelt, Does Discussion Group Composition Aect Policy Preferences? Re-
sults from Three Randomized Experiments, Political Psychology, 2009, 30 (4), 615647.
Festinger, Leon, A Theory of Cognitive Dissonance, California: Stanford University Press,
1957.
, Cognitive dissonance, Scientic American, 1962, 207 (4), 93107.
Fiorina, Morris P., The Voting Decision: Instrumental and Expressive Aspects, Journal
of Politics, 1976, 38 (2), 390413.
Fleishman, John A., Attitude organization in the general public: Evidence for a bidi-
mensional structure, Social Forces, 1988, 67 (1), 159184.
Foos, Florian and Eline A. de Rooij, The role of partisan cues in voter mobilization
campaigns: Evidence from a randomized eld experiment, Electoral Studies, 2017, 45,
6374.
Foster, Andrew D. and Mark R. Rosenzweig, Learning by Doing and Learning from
Others: Human Capital and Technical Change in Agriculture, Journal of Political Econ-
omy, 1995, 103 (6), 11761209.
Fujiwara, Thomas and Leonard Wantchekon, Can informed public deliberation over-
come clientelism? Experimental evidence from Benin, American Economic Journal: Ap-
plied Economics, 2013, 5 (4), 241255.
, Kyle Meng, and Tom Vogl, Habit formation in voting: Evidence from rainy elec-
tions, American Economic Journal: Applied Economics, 2016, 8 (4), 160188.
Garcia Bedolla, Lisa and Melissa R. Michelson, Mobilizing inclusion: Transforming
the electorate through get-out-the-vote campaigns, New Haven: Yale University Press, 2012.
47


---

Gelman, Andrew, Sharad Goel, Douglas Rivers, and David Rothschild, The
Mythical Swing Voter, Forthcoming in Quarterly Journal of Political Science, 2016.
Gentzkow, Matthew, Television and Voter Turnout, The Quarterly Journal of Eco-
nomics, 2006, 121 (3), 931972.
, Jesse M. Shapiro, and Michael Sinkinson, The Eect of Newspaper Entry and
Exit on Electoral Politics, American Economic Review, 2011, 101 (7), 29803018.
Gerber, Alan S., Does campaign spending work? Field experiments provide evidence and
suggest new theory, American Behavioral Scientist, 2004, 47 (5), 541574.
and Donald P. Green, The Eects of Canvassing, Telephone Calls, and Direct Mail
on Voter Turnout: A eld experiment, American Political Science Review, 2000, 94 (3),
653663.
and
, Get out the vote, Brookings Institution Press, 2015.
, Dean Karlan, and Daniel Bergan, Does the Media Matter? A Field Experiment
Measuring the Eect of Newspapers on Voting Behavior and Political Opinion, American
Economic Journal: Applied Economics, 2009, 1 (2), 3552.
, Donald P. Green, and Matthew Green, Partisan mail and voter turnout: results
from randomized eld experiments, Electoral Studies, dec 2003, 22 (4), 563579.
, James G. Gimpel, Donald P. Green, and Daron R. Shaw, How Large and Long-
lasting Are the Persuasive Eects of Televised Campaign Ads? Results from a Randomized
Field Experiment, American Political Science Review, 2011, 105 (1), 135150.
Goldstein, Ken and Paul Freedman, Campaign Advertising and Voter Turnout: New
Evidence for a Stimulation Eect, The Journal of Politics, 2002, 64 (3), 721740.
Green, Donald P., Alan S. Gerber, and David W. Nickerson, Getting Out the Vote
in Local Elections: Results from Six Door-to-Door Canvassing Experiments, Journal of
Politics, 2003, 65 (4), 10831096.
Grossman, Guy, Macartan Humphreys, and Gabriella Sacramone-Luz , Infor-
mation Technology and Political Engagement:
Mixed Evidence from Uganda, 2015,
(http://www.columbia.edu/Cmh2245/papers1/GHS_Scale.pdf).
48


---

Habermas, Jürgen, Between Facts and Norms: Contributions to a Discourse Theory of
Law and Democracy., Cambridge, MA: MIT Press, 1996.
Hillygus, D. Sunshine and Todd G. Shields, The Persuadable Voter: Wedge Issues in
Presidential Campaigns, Princeton: Princeton University Press, 2014.
Hirano, Keisuke, Guido W. Imbens, Donald B. Rubin, and Xiao-Hua Zhou ,
Assessing the eect of an inuenza vaccine in an encouragement design, Biostatistics,
2000, 1 (1), 6988.
Isenberg, Daniel J., Group Plarization: A Critical Review and Meta-Analysis, Journal
of Personality and Social Psychology, 1986, 50 (6), 11411151.
Issenberg, Sasha, The Victory Lab: The Secret Science of Winning Campaigns, New York,
NY: Crown, 2012.
Kaplan, Ethan and Sharun Mukand, The Persistence of Political Partisanship: Evi-
dence from 9/11, Mimeo, University of Maryland, 2014.
Kendall, Chad, Tommaso Nannicini, and Francesco Trebbi, How Do Voters Re-
spond to Information? Evidence from a Randomized Campaign, American Economic
Review, 2015, 105 (1), 322353.
Knutsen, Oddbjørn, The impact of old politics and new politics value orientations on
party choice a comparative study, Journal of Public Policy, 1995, 15 (1), 163.
Krasno, Jonathan S. and Donald P. Green, Do Televised Presidential Ads Increase
Voter Turnout? Evidence from a Natural Experiment, The Journal of Politics, 2008, 70
(1), 245261.
Krupnikov, Yanna, When does negativity demobilize? Tracing the conditional eect of
negative campaigning on voter turnout, American Journal of Political Science, 2011, 55
(4), 797813.
Larreguy, Horacio A., John Marshall, and James M. Snyder Jr, Leveling the
Playing Field: How Campaign Advertising Can Help Non-Dominant Parties, No. w22949.
National Bureau of Economic Research, 2016.
49


---

Lazarsfeld, Paul Felix, Bernard Berelson, and Hazel Gaudet, The People s Choice:
How the Voter Makes Up His Mind in a Presidential Campaign, New York: Duell, Sloan
and Pearce, 1944.
Lefebvre, Rémi, La modernisation du porte-à-porte au Parti socialiste. Réinvention d'un
répertoire de campagne et inerties militantes, Politix, 2016, 113 (1), 91.
Liegey, Guillaume, Arthur Muller, and Vincent Pons, Porte-à-Porte: Reconquérir la
démocratie sur le terrain, Calmann-Lévy, 2013.
Lipset, Seymour Martin, Democracy and working-class authoritarianism, American
Sociological Review, 1959, 24 (1), 482501.
Luskin, Robert C., James S. Fishkin, and Roger Jowell, Considered Opinions:
Deliberative Polling in Britain, British Journal of Political Science, 2002, 32 (03), 455
487.
Marx, Benjamin, Vincent Pons, and Tavneet Suri, Voter Mobilization Can Backre:
Evidence from Kenya, Working paper, 2016.
Mayer, Nonna, Why Extremes Don't Meet: Le Pen and Besancenot Voters in the 2007
French Presidential Election, French Politics, Culture & Society, dec 2011, 29 (3), 101
120.
, From Jean-Marie to Marine Le Pen: Electoral Change on the Far Right, Parliamentary
Aairs, dec 2013, 66 (1), 160178.
Meredith, Marc, Persistence in political participation, Quarterly Journal of Political
Science, 2009, 4 (3), 187209.
Mullainathan, Sendhil and Ebonya Washington, Sticking with Your Vote: Cognitive
Dissonance and Political Attitudes, American Economic Journal: Applied Economics,
2009, 1 (1), 86111.
Myers, David G. and George D. Bishop, Discussion eects on racial attitudes, Sci-
ence, 1970, 169, 778779.
50


---

Nickerson, David W., Partisan Mobilization Using Volunteer Phone Banks and Door
Hangers, The ANNALS of the American Academy of Political and Social Science, 2005,
601 (1), 1027.
, Quality is job one: Professional and volunteer voter mobilization calls, American Jour-
nal of Political Science, 2007, 51 (2), 269282.
, Is Voting Contagious?
Evidence from Two Field Experiments, American Political
Science Review, 2008, 102 (1), 4957.
Panagopoulos, Costas and Donald P. Green, Field Experiments Testing the Impact of
Radio Advertisements on Electoral Competition, American Journal of Political Science,
2008, 52 (1), 156168.
Perrineau, Pascal, La dynamique du vote Le Pen. Le poids du gaucho-lepénisme, in
Pascal Perrineau and Colette Ysmal, eds., Le vote de crise. L'élection présidentielle de
1995, Paris: Presses de Sciences Po, 2005.
Pettigrew, Thomas F., Reactions toward the new minorities of Western Europe, Annual
review of sociology, 1998, 24, 77103.
Pew Research Center, Assessing the representativeness of public opinion surveys, 2012.
Pons, Vincent and Guillaume Liegey, Increasing the Electoral Participation of Immi-
grants - Experiment Evidence from France, Harvard Business School Working Paper, No.
16-094, 2016.
Rogers, Todd and Joel A. Middleton, Are Ballot Initiative Outcomes Inuenced by the
Campaigns of Independent Groups? A Precinct-Randomized Field Experiment Showing
That They Are, Political Behavior, 2015, 37 (3), 567593.
Shaw, Daron R., Donald P. Green, James G. Gimpel, and Alan S. Gerber, Do
robotic calls from credible sources inuence voter turnout or vote choice? Evidence from
a randomized eld experiment, Journal of Political Marketing, 2012, 11 (4), 231245.
Simon, Herbert A. and Frederick Stern, The Eect of Television upon Voting Behavior
in Iowa in the 1952 Presidential Election., American political science review, 1955, 49 (2),
470477.
51


---

Spenkuch, Jorg L. and David Toniatti, Political Advertising and Election Outcomes,
Working paper, 2016.
Terra Nova, Moderniser la Vie Politique: Innovations Américaines, Leçons pour la France,
Rapport de la mission d'étude de Terra Nova sur les techniques de campagne américaines ,
2009, (http://www.acteurspublics.com/les/nominations/rapportus.pdf).
Wantchekon, Leonard, Clientelism and Voting Behavior: Evidence from a Field Experi-
ment in Benin, World Politics, 2003, 55 (03), 399422.
Wattenberg, Martin P. and Craig Leonard Brians, Negative Campaign Advertising:
Demobilizer or Mobilizer?, The American Political Science Review, 1999, 93 (4), 891899.
Wright, Gerald C, Errors in Measuring Vote Choice in the National Election Studies,
1952-88, American Journal of Political Science, 1993, 37, 291316.
52


---

FiguresandTables
Figure1.Resultsofthe2012and2014elections
1.7%
13.4%
28.6%
9.1%
27.2%
1.8%
17.9%
FarͲleft
Left,otherthanPS
PS(F.Hollande)
Center
UMP(N.Sarkozy)
Right,otherthanUMP
FarͲright
79.5
%
80.4
%
0%
20%
40%
60%
80%
100%
Firstround
Second
round
Presidentialelection,2012
Voterturnout
Voteshares,firstround
Parliamentaryelections, 2012
51.6%
48.4%
PS(F.Hollande)
UMP(N.Sarkozy)
Voteshares,secondround
1.0%
17.4%
29.4%
6.8%
27.1%
3.5%
13.8%
FarͲleft
Left,otherthanPS
PS
Center
UMP
Right,otherthanUMP
FarͲright
Voteshares,firstround
10.6%
48.5%
3.8%
33.6%
2.6%
0.5%
Left,otherthanPS
PS
Center
UMP
Right,otherthanUMP
FarͲright
Fractionofseats
57.2
%
55.4
%
0%
20%
40%
60%
80%
100%
Firstround
Second
round
Voterturnout
Europeanelections,2014
42.4
%
0%
20%
40%
60%
80%
100%
1.6%
18.5%
14.0%
9.9%
20.8%
7.5%
24.9%
FarͲleft
Left,otherthanPS
PS
Center
UMP
Right,otherthanUMP
FarͲright
Voteshares,firstround
13.5%
17.6%
9.5%
27.0%
32.4%
Left,otherthanPS
PS
Center
UMP
FarͲright
Fractionofseats
Voterturnout
Source:FrenchMinistryoftheInterior
Notes:Inthefirstroundofthepresidentialelection,thefarͲleftcandidateswerePhilippePoutou(NouveauPartiAnticapitaliste)andNathalie
Arthaud(LutteOuvrière).TheleftcandidatesotherthanFrançoisHollandewereJeanͲLucMélenchon(FrontdeGauche)andEvaJoly(Europe
EcologielesVerts).ThecentercandidatewasFrançoisBayrou(Mouvementdémocrate).TherightcandidateotherthanNicolasSarkozywas
NicolasDupontͲAignan(DeboutlaRépublique).
53


---

0%
20%
40%
60%
80%
100%
1955
1965
1975
1985
1995
2005
2015
Figure2.TurnoutatFrenchpresidential,parliamentary,
andEuropeanelections,1958Ͳ2014
Presidential
elections
Parliamentary
elections
Europeanelections
Source:FrenchMinistryoftheInterior
Notes:French turnoutratesarecomputedusingthenumberofregisteredcitizens(ratherthanthenumberof
eligiblecitizens)asthedenominator.Turnoutshownforthepresidentialandparliamentaryelectionsistheaverage
betweentheturnoutatthefirstandsecondrounds.
54


---

Figure3.Weekly progress ofthecampaign,bydépartement
April6th
April13th
April20th
April27th
May4th
Notes: These mapsshowtheadvancementofthecampaignagainsttheinitialobjectivessetintermsof
numberofdoorstoknock.
Progressof
thecampaign
strong
weak
Progressof
thecampaign
strong
weak
Progressof
thecampaign
strong
weak
Progressof
thecampaign
strong
weak
Progressof
thecampaign
strong
weak
55


---

0
10000
20000
30000
40000
50000
60000
70000
80000
90000
100000
Figure4.Dailynumberofdoorsknockedintheentire
country
Notes: Iplotthenumberofdoorsknockedbycanvassersasreportedbythemonthecampaign'swebsite.
Second
round
First
round
56


---

Figure5.Randomizationrule,andallocationoftreatmentprecinctstocanvassers
Example:
*Ahypotheticalterritorywithatotalof17precincts
*TA,thetargetnumberofregisteredcitizenstobecoveredbythecampaignintheterritory,wasdetermined(beforetherandomization)tobe3174
Step1:Stratification
Step2:Randomization
Step3:AllocationofTreatment(T)precinctstocanvassers
ComputethepotentialtowinvotesPOineachprecinct.
Firststratum(alwaysincludedintherandomization):
RankprecinctsfromhighesttolowestPOandbuildstrataof5precincts:
*the5precinctswiththehighestPOareallocatedtothe1ststratum
Randomlyassigntheprecinctsinthe1st
AllocateallorasubsetoftheTreatmentprecinctsofthe1ststratum
*thenext5precinctsareallocatedtothe2ndstratum,andsoon.
stratumtotheTreatmentandControl
tothecanvassers:

groups:
*allocateonlythefirstTreatmentprecinct,withthelargestPO,ifits
*4precinctsareassignedtoTreatment
numberofregisteredcitizensislargerthanthetargetTA
*1precinctisassignedtoControl.
*otherwise,alsoallocatethesecondTreatmentprecinct,andsoon.
1
1033
0.103
10
961
0.121
1
2
918
0.083
15
1246
0.120
1
Inthisexample:
3
1175
0.093
5
1158
0.119
1
Thetotalnumberofreg.citizensinthe2firstTreatmentprecincts
4
1184
0.103
9
962
0.117
1
(10,5)is2119,whichislowerthanTA(3174).Thetotalnumberofreg.
5
1158
0.119
17
1021
0.104
1
citizensinthe3firstTreatmentprecincts(10,5,9)is3081,whichis
6
854
0.082
1
1033
0.103
2
higherthanTA.Thus,the3firstTreatmentprecinctsareallocatedto
7
963
0.092
4
1184
0.103
2
thecanvassers,butthe4th(17)isnot.
8
876
0.097
8
876
0.097
2
9
962
0.117
16
1098
0.096
2
10
961
0.121
3
1175
0.093
2
11
997
0.067
7
963
0.092
3
10
961
0.121
1
1
10
961
0.121
1
1
1
13
907
0.087
13
907
0.087
3
15
1246
0.120
1
0
15
1246
0.120
1
0
0
14
971
0.067
2
918
0.083
3
5
1158
0.119
1
1
5
1158
0.119
1
1
1
15
1246
0.120
6
854
0.082
3
9
962
0.117
1
1
9
962
0.117
1
1
1
16
1098
0.096
18
1218
0.076
3
17
1021
0.104
1
1
17
1021
0.104
1
1
0
17
1021
0.104
14
971
0.067
4
18
1218
0.076
11
997
0.067
4
SecondstratumandhigherͲnumberedstrata:
Ifthetotalnumberofreg.citizensinthe4Treatmentprecinctsofthe1ststratumishigherthanTA,the1ststratum
isthesinglestratumoftheterritoryincludedintherandomization.
If,ontheotherhand,thetotalnumberofreg.citizensinthe4Treatmentprecinctsofthe1ststratumislowerthanTA,the
2ndstratumoftheterritoryisalsoincludedintherandomization(step2)andallorasubsetofitsTreatmentprecincts
areallocatedtothecanvassers(step3).
Thenagain,if(andonlyif)thetotalnumberofreg.citizensinthe8Treatmentprecinctsofthe1stand2ndstratais
lowerthanTA,the3rdstratumisalsoincludedintherandomization.Andsoon.
Inthisexample:
Thetotalnumberofreg.citizensinthe4Treatmentprecinctsofthe1ststratumis4103,whichishigherthanTA(3174).
Thus,nootherstratumisincludedintherandomization.IfinsteadTAhadbeensetto5174(forinstance),the2ndstratum
wouldhavebeenincludedintherandomizationandoneatleastofitsTreatmentprecinctsallocatedtothecanvassers.
Allocat
ed
Stratum
Precinct
ID
#reg.
citizens
PO
Stratum Treatm
ent
Precinct
ID
#reg.
citizens
PO
Stratum Treatm
ent
PO
Precinct
ID
#reg.
citizens
PO
Precinct
ID
#reg.
citizens
57


---

Table1:Canvassers'profileandfeedbackonthecampaign(postͲelectoralsurvey)
PanelA.Canvassers'profile
Age
29orless
11.1%
30Ͳ45
23.0%
46Ͳ59
36.1%
60andbeyond
29.4%
NonͲresponse
0.5%
Responsibilitieswithinthecampaign
Volunteer
58.8%
Fieldorganizerorheadoflocalunit
37.1%
Départementcoordinator
4.2%
NonͲresponse
0.0%
RelationshiptoPartiSocialiste
Memberforfiveyearsormore
52.0%
Memberforlessthanfiveyears
27.3%
Sympathiserandhadpreviouslybeeninvolvedinacampaign
8.3%
Sympathiserandisinvolvedinacampaignforthefirsttime
12.4%
NonͲresponse
Previousfieldcampaigningexperience
HadneverdonedoorͲtoͲdoorcanvassing
43.2%
HaddonedoorͲtoͲdoorcanvassingafewtimes
34.5%
HadoftendonedoorͲtoͲdoorcanvassing
22.2%
NonͲresponse
0.1%
PanelB.Involvementinthecampaign
AttendedatrainingsessionondoorͲtoͲdoorcanvassing?
Yes
59.0%
No
41.0%
NonͲresponse
NumberofdoorͲtoͲdoorsessionstakenpartto
1to2
13.3%
3to10
48.4%
Morethan10
38.2%
NonͲresponse
0.1%
Typeofareascanvassed
Bigcities(morethan100000inhabitants)
25.4%
MiddleͲsizecities(10000Ͳ100000)
47.2%
Ruralareas(<10000)
27.4%
NonͲresponse
0.1%
Didyou(oryourlocalunit)usethelistofprioritypollingstationsor
municipalitiesthatwasprovidedbythecampaign?
Ineverheardofthislist
29.1%
Wedidnotusethislistatall,oronlyverylittle
16.3%
Weusedthislistpartially
11.2%
Wewenttoalmostalltheprioritypollingstationsorcities
43.5%
NonͲresponse
0.0%
Notes:Ireporttheresponsesofcanvasserstoanonlinevoluntarypostelectoralsurvey
administeredduringtheweekfollowingthesecondroundofthe2012presidentialelection.N
=1,972.
58


---

Table1(cont.):Canvassers'profileandfeedbackonthecampaign(postͲelectoralsurvey)
PanelB.Involvementinthecampaign(cont.)
Didyouusethetoolkitsprovidedbythecampaign?
No
33.8%
Sometimes
43.7%
Yes,mostofthetime
22.5%
NonͲresponse
0.0%
HowmuchdoorͲtoͲdoorcanvassingdidyoudo,compared
withothercampaignactivities?
IdidsomedoorͲtoͲdoorcanvassing,butmostlyotheractivities
24.0%
IdidasmuchdoorͲtoͲdoorcanvassingasothercampaignactivities
48.4%
ImostlydiddoorͲtoͲdoorcanvassing
27.6%
NonͲresponse
0.0%
Weretheresympathisersinyourlocalcanvassers'team?
Yes
70.7%
No
29.3%
NonͲresponse
0.0%
DidyourteamtrytorecruitsympathisersfordoorͲtoͲdoorcanvassing?
Yes
65.1%
No
34.9%
NonͲresponse
0.0%
PanelC.Canvassers'feedbackonthecampaign
Overall,whatdoyouthinkofdoorͲtoͲdoorcanvassing?
Iwillnotdoitagain
0.8%
Oneshoulddosome,butnotmorethanothercampaignactivities
38.5%
Itisareallygoodtechniqueandshouldbeofthemaincampaignactivities 60.8%
NonͲresponse
0.0%
IfyoulikedoorͲtoͲdoorcanvassing,whyso?
Itisgoodtotakepartinalargeandcountrywidecampaignactivity
6.9%
Itiseffective
31.0%
Itisfun
2.5%
Itisagoodwaytospreadtheideasandvaluesoftheleft
31.3%
Itisanenrichingexperience
27.2%
NonͲresponse
1.0%
Overall,howhelpfulwasthesupportprovidedby
thenationalteamandthedépartement'steam?
Itwasveryhelpful
49.3%
Itwassometimehelpful
48.0%
Thelessweseethem,thebetterweare
2.7%
NonͲresponse
Overall,onascalefrom1to5(where1meansuselessand5excellent)
howdidyoulikethewebplatform"ToushollandeTerrain"?
1
1.6%
2
7.6%
3
28.3%
4
41.4%
5
21.1%
NonͲresponse
0.0%
Notes :Ireporttheresponsesofcanvasserstoanonlinevoluntarypostelectoralsurvey
administeredduringtheweekfollowingthesecondroundofthe2012presidentialelection.N
=1,972.
59


---

Table2:Summarystatistics
Mean
SD
Mean
SD
PanelA.Electoraloutcomes
Randomizationatprecinctlevel
0.504
0.500
0.504
0.500
0.992
3397
Numberofregisteredcitizens
1014.3
1097.6
1133.8
1605.3
0.022
3397
Potentialtowinvotes,PO
0.089
0.035
0.089
0.033
0.970
3397
Voterturnout,2007pres.election,firstround
0.843
0.050
0.840
0.048
0.231
2665
Voterturnout,2007pres.election,secondround
0.837
0.045
0.836
0.045
0.675
2665
PSvoteshare,2007pres.election,firstround
0.274
0.081
0.279
0.081
0.172
2665
PSvoteshare,2007pres.election,secondround
0.515
0.103
0.516
0.101
0.743
2665
PanelB.Location
Populationofthemunicipality
68310.9
277136.8
66254.4
273841.2
0.863
3397
Region
IleͲdeͲFrance
0.160
0.367
0.160
0.367
0.994
3397
ChampagneͲArdenne
0.028
0.166
0.028
0.164
0.927
3397
Picardie
0.053
0.225
0.054
0.226
0.953
3397
HauteͲNormandie
0.043
0.203
0.041
0.199
0.861
3397
CentreͲValdeLoire
0.058
0.234
0.058
0.235
0.958
3397
BasseͲNormandie
0.024
0.152
0.025
0.156
0.851
3397
Bourgogne
0.039
0.193
0.039
0.193
0.999
3397
NordͲPasͲdeͲCalais
0.016
0.127
0.019
0.136
0.663
3397
Lorraine
0.043
0.203
0.045
0.207
0.839
3397
Alsace
0.016
0.127
0.019
0.137
0.616
3397
FrancheͲComté
0.024
0.152
0.024
0.153
0.984
3397
PaysͲdeͲlaͲLoire
0.067
0.250
0.064
0.245
0.815
3397
Bretagne
0.058
0.234
0.061
0.240
0.731
3397
PoitouͲCharentes
0.024
0.152
0.024
0.154
0.939
3397
Aquitaine
0.045
0.206
0.044
0.204
0.927
3397
MidiͲPyrénées
0.040
0.196
0.040
0.196
0.997
3397
Limousin
0.034
0.182
0.030
0.172
0.637
3397
RhôneͲAlpes
0.113
0.317
0.109
0.312
0.786
3397
Auvergne
0.040
0.196
0.040
0.195
0.962
3397
LanguedocͲRoussillon
0.046
0.210
0.046
0.209
0.992
3397
ProvenceͲAlpesͲCôteͲd'Azur
0.028
0.166
0.028
0.166
0.990
3397
Corse
0.001
0.039
0.001
0.038
0.993
3397
PanelC.Sociodemographiccharacteristicsofthepopulationofthemunicipality
Shareofmen
0.488
0.023
0.487
0.024
0.273
3397
Shareofthepopulationwithage
0Ͳ14
0.182
0.038
0.181
0.037
0.541
3397
15Ͳ29
0.175
0.052
0.175
0.053
0.923
3397
30Ͳ44
0.196
0.034
0.195
0.032
0.810
3397
45Ͳ59
0.207
0.033
0.205
0.033
0.222
3397
60Ͳ74
0.148
0.042
0.149
0.043
0.325
3397
75andolder
0.093
0.038
0.094
0.040
0.521
3397
Withinpopulationof15Ͳ64
Shareofworkingpopulation
0.726
0.052
0.723
0.054
0.185
3397
Shareofunemployed(amongworkingpopulatio
0.123
0.050
0.124
0.051
0.575
3397
Medianincome
19234.3
3850.1
19262.1
3911.2
0.870
3246
Controlgroup
Treatmentgroup
PͲvalue
Treatment
=Control
Number
ofobs.
Notes :Foreachvariable,Ireportthemeansandstandarddeviationsinboththecontrolgroupandthetreatmentgroupandindicatethe
p Ͳvalueofthedifference.Theunitofobservationistheunitofrandomization(precinctormunicipality).
60


---

Table3.Firststage
Nocontrol
(1)
(2)
(3)
(4)
(5)
(6)
(7)
Treatment
0.5652
0.5233
0.5247
0.5238
0.5241
0.5245
0.5240
(0.0137)
(0.0173)
(0.0172)
(0.0172)
(0.0173)
(0.0172)
(0.0172)
Stratafixedeffects
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
x
2007outcomecontrolledfor
Voter
turnout,
round1
Voter
turnout,
round2
Voter
turnout,
average
Vote
share
Royal,
round1
Vote
share
Royal,
round2
Vote
share
Royal,
average
Observations
3390
2660
2660
2660
2660
2660
2660
RͲsquared
0.258
0.424
0.423
0.424
0.423
0.424
0.424
MeaninControlGroup
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
Withcontrols
Notes :ThetableshowsfirststageresultsfromEquation[3].Theunitofobservationistheunitofrandomization(precinct,or
municipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects.Regressionsincolumns2through7controlforPO(proxyforthepotentialtowin
votes)andforpastoutcomes,measuredatthelevelofrandomization:voterturnoutorvoteshareobtainedbySégolèneRoyal
inthefirstround,inthesecondround,oraveragedoverbothroundsofthe2007presidentialelection.Additionalcontrols
includethenumberofregisteredcitizensintheprecinctormunicipalityaswellasthelevelandthefiveͲyearchangeofthe
followingcensusvariables:themunicipality'spopulation,theshareofmen,theshareofdifferentagegroups(from0to14;
from15to29;from30to44;from45to59;from60to74;above75),theshareofworkingpopulation,andtheshareof
unemployedpopulationamongtheworkingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2007,whichexplains
thelowernumberofobservations.
61


---

Table4:Impactonvoterturnout
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
PanelA.ITTEstimation
Treatment
0.0001
0.0008
0.0011
Ͳ0.0005
Ͳ0.0011
Ͳ0.0008
Ͳ0.0002
Ͳ0.0001
0.0002
(0.0016)
(0.0015)
(0.0015)
(0.0015)
(0.0015)
(0.0014)
(0.0015)
(0.0014)
(0.0014)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
3390
2660
2660
3390
2660
2660
3390
2660
2660
RͲsquared
0.000
0.328
0.410
0.000
0.255
0.326
0.000
0.328
0.405
MeaninControlGroup
0.7951
0.8081
0.8081
0.8014
0.8122
0.8122
0.7983
0.8101
0.8101
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0001
0.0015
0.0021
Ͳ0.0009
Ͳ0.0021
Ͳ0.0015
Ͳ0.0004
Ͳ0.0001
0.0004
(0.0029)
(0.0029)
(0.0028)
(0.0027)
(0.0028)
(0.0028)
(0.0027)
(0.0027)
(0.0026)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
3390
2660
2660
3390
2660
2660
3390
2660
2660
Voterturnout
Firstround
Secondround
Averageoffirstandsecond
rounds
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowstheeffect
ofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunitofrandomization(precinct,or
municipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects.Regressionsincolumns(2),(5),and(8)alsocontrolforPO(proxyforthepotentialtowinvotes)and
forpastoutcomes,measuredatthelevelofrandomization.Additionalcontrolsincolumns(3),(6),and(9)includethenumberofregistered
citizensintheprecinctormunicipalityaswellasthelevelandthefiveͲyearchangeofthefollowingcensusvariables:themunicipality's
population,theshareofmen,theshareofdifferentagegroups(from0to14;from15to29;from30to44;from45to59;from60to74;
above75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongtheworkingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2007,whichexplainsthelower
numberofobservations.
62


---

Table5:ImpactonHollande'svoteshare
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
PanelA.ITTEstimation
Treatment
0.0063
0.0050
0.0044
0.0048
0.0053
0.0046
0.0056
0.0049
0.0043
(0.0023)
(0.0019)
(0.0018)
(0.0028)
(0.0019)
(0.0018)
(0.0024)
(0.0017)
(0.0016)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
3390
2660
2660
3390
2660
2660
3390
2660
2660
RͲsquared
0.003
0.516
0.528
0.001
0.632
0.645
0.002
0.645
0.655
MeaninControlGroup
0.3157
0.2994
0.2994
0.5757
0.5597
0.5597
0.4457
0.4295
0.4295
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0112
0.0094
0.0084
0.0084
0.0099
0.0087
0.0098
0.0092
0.0081
(0.0041)
(0.0036)
(0.0035)
(0.0050)
(0.0036)
(0.0035)
(0.0042)
(0.0031)
(0.0030)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
3390
2660
2660
3390
2660
2660
3390
2660
2660
Averageoffirstandsecond
rounds
Hollande'svoteshare
Firstround
Secondround
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowstheeffect
ofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunitofrandomization(precinct,or
municipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects.Regressionsincolumns(2),(5),and(8)alsocontrolforPO(proxyforthepotentialtowinvotes)and
forpastoutcomes,measuredatthelevelofrandomization.Additionalcontrolsincolumns(3),(6),and(9)includethenumberofregistered
citizensintheprecinctormunicipalityaswellasthelevelandthefiveͲyearchangeofthefollowingcensusvariables:themunicipality's
population,theshareofmen,theshareofdifferentagegroups(from0to14;from15to29;from30to44;from45to59;from60to74;
above75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongtheworkingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2007,whichexplainsthelower
numberofobservations.
63


---

Table6:Impactonallparties'voteshares
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
(10)
(11)
(12)
PanelA.ITTEstimation
Treatment
0.0063
0.0044
0.0000
0.0003
Ͳ0.0022
Ͳ0.0011
Ͳ0.0008
Ͳ0.0007
Ͳ0.0037
Ͳ0.0043
0.0006
0.0016
(0.0023)
(0.0018)
(0.0004)
(0.0005)
(0.0017)
(0.0017)
(0.0010)
(0.0010)
(0.0021)
(0.0016)
(0.0018)
(0.0016)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
x
Observations
3390
2660
3390
2660
3390
2660
3390
2660
3390
2660
3390
2660
RͲsquared
0.003
0.528
0.000
0.056
0.001
0.271
0.000
0.231
0.001
0.526
0.000
0.434
MeaninControlGroup
0.3157
0.2994
0.0192
0.0200
0.1539
0.1514
0.0837
0.0865
0.2455
0.2528
0.1792
0.1873
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0112
0.0084
0.0000
0.0007
Ͳ0.0040
Ͳ0.0022
Ͳ0.0015
Ͳ0.0014
Ͳ0.0066
Ͳ0.0082
0.0011
0.0031
(0.0041)
(0.0035)
(0.0007)
(0.0009)
(0.0030)
(0.0033)
(0.0018)
(0.0020)
(0.0037)
(0.0030)
(0.0031)
(0.0030)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
x
Observations
3390
2660
3390
2660
3390
2660
3390
2660
3390
2660
3390
2660
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowstheeffectofaprecinctbeingallocatedto
canvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunitofrandomization(precinct,ormunicipality).Robuststandarderrorsareinparentheses.
ThefarͲleftcandidates(columns3and4)wereNathalieArthaud(endorsedbyLutteOuvrière)andPhilippePoutou(LigueCommunisteRévolutionnaire).Thecandidatesontheleft
otherthanFrançoisHollande(columns5and6)wereEvaJoly(EuropeEcologieLesVerts)andJeanͲLucMélenchon(FrontdeGauche).Thecandidateonthecenter(columns7and8)
wasFrançoisBayrou(Modem).Thecandidatesontheright(columns9and10)wereNicolasSarkozy(UnionpourunMouvementPopulaire)andNicolasDupontͲAignan(Deboutla
République).Thecandidateonthefarright(columns11and12)wasMarineLePen(FrontNational).
Allregressionsincludestratafixedeffects.RegressionsinevenͲnumberedcolumnscontrolforPO(proxyforthepotentialtowinvotes),pastoutcomes,measuredatthelevelof
randomization,andadditionalcontrols.AdditionalcontrolsincludethenumberofregisteredcitizensintheprecinctormunicipalityaswellasthelevelandthefiveͲyearchangeof
thefollowingcensusvariables:themunicipality'spopulation,theshareofmen,theshareofdifferentagegroups(from0to14;from15to29;from30to44;from45to59;from60
to74;above75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongtheworkingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2007,whichexplainsthelowernumberofobservations.
Right
FarͲright
Leftotherthan
Hollande
Hollande
FarͲleft
Center
64


---

Table7:Impactonvoterturnoutatthefollowingelections
Firstround
Secondround
Firstround
Secondround
(1)
(2)
(3)
(4)
(5)
PanelA.ITTEstimation
Treatment
0.0011
Ͳ0.0008
Ͳ0.0024
Ͳ0.0025
0.0014
(0.0015)
(0.0014)
(0.0022)
(0.0024)
(0.0027)
Stratafixedeffects
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
Constituencyfixedeffects
x
x
Observations
2660
2660
2660
2443
2544
RͲsquared
0.410
0.326
0.347
0.307
0.226
MeaninControlGroup
0.8081
0.8122
0.5884
0.5680
0.4457
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0021
Ͳ0.0015
Ͳ0.0046
Ͳ0.0049
0.0026
(0.0028)
(0.0028)
(0.0042)
(0.0046)
(0.0051)
Stratafixedeffects
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
Constituencyfixedeffects
x
x
Observations
2660
2660
2660
2443
2544
Voterturnout
2012presidentialelection
2012parliamentaryelections
2014european
elections
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelB
showstheeffectofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunit
ofrandomization(precinct,ormunicipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects,controlforPO(proxyforthepotentialtowinvotes),pastoutcomes,measuredatthe
levelofrandomization,andadditionalcontrols.Additionalcontrolsincludethenumberofregisteredcitizensintheprecinctor
municipalityaswellasthelevelandthefiveͲyearchangeofthefollowingcensusvariables:themunicipality'spopulation,the
shareofmen,theshareofdifferentagegroups(from0to14;from15to29;from30to44;from45to59;from60to74;above
75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongtheworkingpopulation.Regressionsin
columns(3)and(4)alsocontrolforconstituencyfixedeffectstoaccountfordifferencesinthenumberandidentityof
competingcandidatesacrossconstituencies,atthe2012parliamentaryelections.
65


---

Table8:ImpactonvotesharesofPScandidatesatthefollowingelections
Firstround
Secondround
Firstround
Secondround
Firstround
Secondround
Firstround
Secondround
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
(10)
PanelA.ITTEstimation
Treatment
0.0044
0.0046
0.0094
0.0073
0.0037
0.0035
0.0032
0.0042
0.0031
0.0017
(0.0018)
(0.0018)
(0.0026)
(0.0024)
(0.0021)
(0.0015)
(0.0016)
(0.0018)
(0.0019)
(0.0012)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
x
x
x
x
x
Constituencyfixedeffects
x
x
x
x
Observations
2660
2660
2660
2443
2544
2660
2660
2660
2443
2544
RͲsquared
0.528
0.645
0.692
0.827
0.302
0.480
0.602
0.624
0.726
0.239
MeaninControlGroup
0.2994
0.5597
0.3246
0.4545
0.1425
0.2355
0.4241
0.1876
0.2481
0.0605
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0084
0.0087
0.0181
0.0142
0.0070
0.0067
0.0061
0.0080
0.0060
0.0032
(0.0035)
(0.0035)
(0.0050)
(0.0048)
(0.0039)
(0.0029)
(0.0030)
(0.0034)
(0.0037)
(0.0022)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
x
ControlforpastoutcomeandPO
x
x
x
x
x
x
x
x
x
x
Additionalcontrols
x
x
x
x
x
x
x
x
x
x
Constituencyfixedeffects
x
x
x
x
Observations
2660
2660
2660
2443
2544
2660
2660
2660
2443
2544
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowstheeffectofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation
[2]).Theunitofobservationistheunitofrandomization(precinct,ormunicipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects,controlforPO(proxyforthepotentialtowinvotes),pastoutcomes,measuredatthelevelofrandomization,andadditionalcontrols.Additionalcontrolsincludethe
numberofregisteredcitizensintheprecinctormunicipalityaswellasthelevelandthefiveͲyearchangeofthefollowingcensusvariables:themunicipality'spopulation,theshareofmen,theshareofdifferentage
groups(from0to14;from15to29;from30to44;from45to59;from60to74;above75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongtheworkingpopulation.Regressionsin
columns(3),(4),(8),and(9)alsocontrolforconstituencyfixedeffectstoaccountfordifferencesinthenumberandidentityofcompetingcandidatesacrossconstituencies,atthe2012parliamentaryelections.
PSvoteshareasfractionofexpressedvotes
2012presidentialelection
2012parliamentaryelections
2014
european
elections
PSvoteshareasfractionofregisteredvoters
2012presidentialelection
2012parliamentaryelections
2014
european
elections
66


---

Table9:PlaceboͲImpactonvoterturnoutin2007
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
PanelA.ITTEstimation
Treatment
Ͳ0.0026
Ͳ0.0026
Ͳ0.0023
Ͳ0.0005
0.0001
0.0003
Ͳ0.0015
Ͳ0.0011
Ͳ0.0009
(0.0014)
(0.0014)
(0.0014)
(0.0012)
(0.0013)
(0.0012)
(0.0012)
(0.0012)
(0.0012)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
Controlforpastoutcome
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
2660
2133
2133
2660
2133
2133
2660
2133
2133
RͲsquared
0.002
0.267
0.301
0.000
0.196
0.243
0.001
0.303
0.341
MeaninControlGroup
0.8428
0.8494
0.8494
0.8373
0.8432
0.8432
0.8400
0.8463
0.8463
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
Ͳ0.0048
Ͳ0.0049
Ͳ0.0044
Ͳ0.0009
0.0001
0.0005
Ͳ0.0029
Ͳ0.0021
Ͳ0.0017
(0.0026)
(0.0028)
(0.0027)
(0.0023)
(0.0024)
(0.0024)
(0.0023)
(0.0023)
(0.0023)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
Controlforpastoutcome
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
2660
2133
2133
2660
2133
2133
2660
2133
2133
Firstround
Secondround
Averageoffirstandsecond
rounds
Voterturnout
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowsthe
effectofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunitofrandomization
(precinct,ormunicipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects.Regressionsincolumns(2),(5),and(8)alsocontrolforpastoutcomes,measuredatthe
levelofrandomization.Additionalcontrolsincolumns(3),(6),and(9)includethenumberofregisteredcitizensintheprecinctor
municipality,themunicipality'spopulation,theshareofmen,theshareofdifferentagegroups(from0to14;from15to29;from30
to44;from45to59;from60to74;above75),theshareofworkingpopulation,andtheshareofunemployedpopulationamongthe
workingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2002,whichexplainsthe
lowernumberofobservations.
67


---

Table10:PlaceboͲImpactonRoyal'svotesharein2007
(1)
(2)
(3)
(4)
(5)
(6)
(7)
(8)
(9)
PanelA.ITTEstimation
Treatment
0.0050
0.0015
0.0007
0.0009
Ͳ0.0013
Ͳ0.0014
0.0029
Ͳ0.0002
Ͳ0.0006
(0.0027)
(0.0024)
(0.0023)
(0.0029)
(0.0024)
(0.0023)
(0.0026)
(0.0020)
(0.0020)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
Controlforpastoutcome
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
2660
2133
2133
2660
2133
2133
2660
2133
2133
RͲsquared
0.002
0.371
0.395
0.000
0.495
0.509
0.001
0.525
0.541
MeaninControlGroup
0.2740
0.2620
0.2620
0.5146
0.5056
0.5056
0.3943
0.3838
0.3838
PanelB.Instrumentalvariableestimation:"allocatedtocanvassers"instrumentedwith"treatment"
Allocatedtocanvassers
0.0093
0.0028
0.0015
0.0016
Ͳ0.0025
Ͳ0.0028
0.0055
Ͳ0.0004
Ͳ0.0011
(0.0049)
(0.0045)
(0.0045)
(0.0054)
(0.0046)
(0.0046)
(0.0048)
(0.0039)
(0.0039)
Stratafixedeffects
x
x
x
x
x
x
x
x
x
Controlforpastoutcome
x
x
x
x
x
x
Additionalcontrols
x
x
x
Observations
2660
2133
2133
2660
2133
2133
2660
2133
2133
Averageoffirstandsecond
rounds
Royal'svoteshare
Firstround
Secondround
Notes :PanelAshowstheeffectofaprecinctbeingassignedtothetreatmentgroup(ITTresultsfromEquation[1]).PanelBshowsthe
effectofaprecinctbeingallocatedtocanvassers(2SLSresultsfromEquation[2]).Theunitofobservationistheunitofrandomization
(precinct,ormunicipality).Robuststandarderrorsareinparentheses.
Allregressionsincludestratafixedeffects.Regressionsincolumns(2),(5),and(8)alsocontrolforpastoutcomes,measuredatthe
levelofrandomization.PastPSvoteshareatthesecondroundofthe2002presidentialelectionisproxiedbythesumoffirstround
votesharesofallLeftͲwingcandidatessincethePScandidate(LionelJospin)failedtoqualifyforthesecondround(heunexpectedly
arrivedthird,behindtheRightandFarͲrightcandidates).Additionalcontrolsincolumns(3),(6),and(9)includethenumberof
registeredcitizensintheprecinctormunicipality,themunicipality'spopulation,theshareofmen,theshareofdifferentagegroups
(from0to14;from15to29;from30to44;from45to59;from60to74;above75),theshareofworkingpopulation,andtheshareof
unemployedpopulationamongtheworkingpopulation.
Regressionscontrollingforpastoutcomesneedtoexcludeprecinctswhoseboundarieshadchangedafter2002,whichexplainsthe
lowernumberofobservations.
68

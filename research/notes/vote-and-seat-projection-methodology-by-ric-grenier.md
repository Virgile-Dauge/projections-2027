---
title: Vote and seat projection methodology - by Éric Grenier
id: vote-and-seat-projection-methodology-by-ric-grenier
tags:
- projections-electorales-bureaux-2027-b0b1c4
- swing-methods
- production-methodology
- canada
created: '2026-07-21T18:28:15.644759Z'
updated: '2026-07-21T18:39:17.621508Z'
source: https://www.thewrit.ca/p/vote-and-seat-projection-methodology
source_domain: www.thewrit.ca
fetched_at: '2026-07-21T18:28:15.604379Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Éric Grenier (The Writ, ex-CBC Poll Tracker) publishes the full production
  methodology for his Canadian federal riding-level vote/seat projection model (launched
  March 2026). Riding baseline = 50/50 average of proportional swing and uniform swing
  applied to the previous election result in that riding, using regional polling averages
  (polls weighted 70% recency / 25% sample size up to n=1,500 / 5% pollster track
  record). After the 50/50 swing blend, discretionary adjustment layers are applied
  for: byelection results as new baseline, incumbency effects (+/-3-4 points when
  an incumbent departs), floor-crossing, independents, party-leader-in-riding boosts,
  candidates with prior provincial/territorial office, and withdrawn-or-absent candidates
  (redistributed to other parties by fixed rules). Adjustment sizes are calibrated
  by backtesting the swing model against real results in past elections. National/provincial
  vote projections are built bottom-up by summing riding projections weighted by turnout
  share (not a separate top-down poll average) so an incumbent-loss shock in one province
  lowers that party''s projected province vote even if the polling average is unchanged.
  Seat projection uses 10,000 Monte Carlo simulations per update; probability ranges
  are calibrated from 2011-2025 backtested party/region-specific over/under-performance
  of polls (e.g. Conservatives historically beat their polls, NDP underperforms),
  producing asymmetric confidence bands and Safe/Likely/Lean/Close/Edge/Toss categories
  that are NOT based on a uniform margin threshold.'
---

SubscribeSign in
Discover more from The Writ
Insights and analysis on Canadian politics and elections.
Over 16,000 subscribers
Already have an account? Sign in
# Vote and seat projection methodology
### Full methodology for The Writ's vote and seat projection model
Mar 17, 2026
Share
The following is the full explanation of the methodology behind _The Writ_ ’s federal vote and seat projection model.
#### [The Writ's Federal Vote and Seat Projections · 17 mars ](https://www.thewrit.ca/p/the-writs-federal-vote-and-seat-projections)
While I’ve been building and running election models for over 15 years and ran the CBC’s _Poll Tracker_ in the 2015, 2019, 2021 and 2025 elections (as well as for a handful of provincial elections), this model is newly-designed from the ground up. I wrote about some of my thought processes during the development of the model here:
#### [Model Development Diary #1: Which way to swing? · 17 août 2025 ](https://www.thewrit.ca/p/model-development-diary-1-which-way)
#### [Model Development Diary #2: Do candidates matter? · 21 décembre 2025 ](https://www.thewrit.ca/p/model-development-diary-2-do-candidates)
_The Writ_ ’s vote and seat projection model was launched in March 2026. Prior data was loaded into the model to calculate projections stretching back to the April 2025 election for comparison purposes.
This projection model will always be in a state of evolution as changes will be made when required (and, if significantly changing the model, explained in full). While I’ve taken as many steps as possible to reduce the amount of my own subjective judgment that is applied to the projections, there might arise some situations in which there are few or no historical precedents to use as guidance. In those cases, some _ad hoc_ adjustments to the projection model might be made by me.
### Calculating the polling average
National and regional polls are weighted by three factors.
The first is the date of the poll, based on the mid-point of the poll’s field dates. Outside of a campaign, polls with a mid-point date within the last week are given a full weight, while during a campaign full weights are given to polls with a mid-point date within the last three days. Outside of a campaign, the date weight of a poll is reduced by 7% per day, while during a campaign it is reduced by 25% per day.
The second weight is the sample size, with larger sample sizes given more weight than smaller sample sizes, up to a limit of 1,500.
The third weight is the track record of a polling firm, with polling firms with a better track record give more weight than polls with a worse track record.
The relative weights of these three factors is 70%, 25% and 5%, respectively, with the sample size and track record weight reduced at the same pace as the date weighting. After each poll is assigned a weight, it is then used to calculate an average in a given region. Polling averages are calculated for each region and sub-region, depending on what data is available.
### Riding-level projections
For each region with a polling average, a baseline riding projection is calculated for each riding in that region. The riding projection is a 50/50 combination of a proportional and uniform swing model.
With proportional swing, a party’s result in a riding in the previous election is adjusted proportionally by how a party’s support has shifted in the region as a whole since that election.
With uniform swing, a party’s result in a riding is adjusted uniformly by how a party’s support has shifted in the region as a whole.
The average between the proportional and uniform swing is then calculated for each party in each riding, and then those numbers are adjusted to ensure support adds up to 100%.
The projection for each riding in each region with a polling average is then assigned a weight according to the weight of all the polls in the polling average for that region, and a weighted average riding projection is then calculated for every riding.
At this point, adjustments are made to the projection to take into account local factors. This include:
  * **Byelections:** When a seat has changed hands in a byelection, the vote projection in the region where and when the byelection was held is used as the new baseline from which to apply the proportional and uniform swing. When a seat hasn’t changed hands, the previous general election result is still used as the baseline. Regardless of whether the riding changed hands or not, the error range for the riding’s projection is widened to increase the level of uncertainty.
  * **Incumbency:** Based on historical precedent, the presence of an incumbent marginally boosts support for the Liberals or NDP, largely at the expense of the other party. The lack of an incumbent penalizes the party that lost the incumbent by between three to four points, with different parties getting a corresponding boost depending on which party has lost the incumbent.
  * **Floor-crossing:** The party that has welcomed a floor-crossing MP receives a boost that comes at the expense of the party that lost the floor-crossing MP. The size of that boost can be adjusted according to the circumstances but is based on past precedent.
  * **Independents:** The presence, or departure, of significant Independent MPs or candidates is taken into account.
  * **Party leaders:** A party leader running in a riding for the first time gets a significant boost in the model, based on past precedents. A party whose leader has vacated a riding is penalized to a greater extent than when it is a normal incumbent MP that has retired. 
  * **Candidates with previous electoral experience:** New candidates who have previously sat in a provincial or territorial legislature or who were leaders of a provincial or territorial party are awarded a boost which comes at the expense of other parties, depending on the party of the candidate.
  * **Withdrawn or no candidate:** When a major party withdraws a candidate but that candidate will still be present on the ballot as a candidate for that party, a smaller share of what the candidate would have normally been expected to get is awarded to the party. That reduction is awarded to other parties depending on which party withdrew their candidate. When a major party has no candidate on the ballot, the share that would have been projected for a candidate from that party is distributed to other parties in different amounts depending on which party does not have a candidate. When a party did not run a candidate in the last election, previous results are used to estimate that party’s support.


The size of boosts or penalties assessed is determined by looking at how past actual election results compared to expected results when applying the mixed uniform/proportional swing model to those past elections.
Once these adjustments are complete, a final projection for the riding can be calculated. These are the numbers that you can find on the Riding Projections page.
### Vote projection
The national, provincial and regional vote projections are calculated by summing the riding projections. In other words, the weighted polling average and the vote projection are two separate things, and only the vote projection is presented.
The projection for each province is calculated by weighting each riding projection by the average of 1) the riding’s share of the province’s total eligible voting population in the last election and 2) the riding’s share of the province’s total actual voters in the last election. With each riding assigned a turnout weight, they can then be combined to calculate the vote projection for the province as a whole.
This means that the vote projection takes into account not only turnout dynamics but also the adjustments made to each individual riding. A party losing a large number of incumbents in a province, for example, would be projected to take less of the vote than the polling average would suggest.
To calculate the national (and, in the case of Atlantic Canada, regional) vote projection, the provincial vote projections are weighted by the share of each province’s national turnout in the last election. Different provinces have consistently and predictably had higher or lower turnout than the country as a whole.
Since the national vote projection is dependent on the provincial vote projections, single-province or region polls can influence the national vote projection.
Sub-regional vote projections presented with the Riding Projections (such as for Toronto or Montreal) are a simple average of the individual riding projections in that region, with a few exceptions made for regions with ridings with significantly smaller populations or lower turnout.
### Seat projection
The Seat Projection is simply the number of ridings in which a party is projected to be leading.
However, each party in each riding also has a lower and higher range of likely support. These ranges are based on the past performance of this model when applied to elections between 2011 and 2025, meaning the ranges take into account both the errors in the model itself and in the polls. For that reason, the ranges aren’t a simple +/- calculation, with the likelihood of the result being higher or lower than the projection being equal. The precise projection for each riding _does not_ take into account the past errors in the polls, but the projection ranges _do_ take into account past polling error.
This means that parties that have historically beaten their polls (such as the Conservatives) have a higher high range and a lower low range than parties that have historically under-performed their polls (such as the New Democrats). These tendencies to under- or out-perform the polls is calculated for each party in each region. In some regions, for example, parties have largely matched their polls while they haven’t in others. Alberta and Saskatchewan for the Conservatives are good examples of where the polls have been off by greater amounts than in other regions.
These upper and lower ranges are then used to determine which seats are in contention for each party at each confidence level. More seats are in contention at the 95% confidence level, where the ranges are greater, than at the 75% confidence level, where the ranges are smaller. 
The classification of a projection as Safe, Likely, Lean, Close, Edge and Toss reflects at which level of confidence does a seat become contested. If a seat is projected as “Safe”, it means that with the widest projected ranges for every party the leading party’s floor is higher than every other party’s ceiling at the 95% confidence level. “Likely” represents the 85% to 95% range, “Lean” the 75% to 85% range, “Close” the 65% to 75% range, “Edge” the 55% to 65% range, and “Toss” is 55% and less. 
Since the upper and lower ranges differ for each party, in each region and at each confidence level, the classification of a projection is not uniformly based on the same margins. Two seats contested by the Conservatives and Liberals with the same margin between the two parties might be an “Edge” call in Ontario and a “Lean” call in Alberta because of how the ranges for the two parties differ from region to region. For example, a Liberal lead in Alberta is going to be more uncertain than a Conservative lead of the same size in the province, because the Conservative floor is higher than the Liberals’ floor.
The precise riding projections do not take into account these past polling performances, however, because polling errors are not consistent from one election to the next. Rather than risk adding to potential errors, I have decided to let the riding projections reflect the seats each party _should_ be able to win based on where the polls are, and let the projection classifications reflect the certainty (or uncertainty) of those projections.
### Calculating probabilities and the Avg. Projection
Using the ranges at each confidence level, the number of seats being contested between two or more parties is calculated. Then, a proportion of these contested seats are randomly assigned to each party to give each party a total of seats won. The result is one election simulation that incorporates the uncertainty in the riding projections. This process is repeated 10,000 times to simulate 10,000 individual election results.
The presented “chances of winning” the election is the equivalent of the share of times one party has the most seats and/or crosses the 172-seat threshold for a majority government in those 10,000 simulations.
The high and low seat projection ranges reflect the 95th percentile of outcomes in those 10,000 simulations, while the Avg. Projection is the average outcome of those simulations. As the simulations rely on the projection ranges for each individual riding, which themselves are calculated by assessing the tendency for parties to out- or under-perform their polls and the model, the ranges and the Avg. Projection take into account the likelihood that parties will beat or under-perform their polls and the model.
  * **Any questions regarding the model? Leave them as a comment below orsend me an email.**


[Leave a comment](https://www.thewrit.ca/p/vote-and-seat-projection-methodology/comments)
[1](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-1)
My research has suggested that there is no meaningful increase in accuracy for election polls with a national sample size of more than 1,500 interviews.
[2](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-2)
If a party has gone from 10% to 20% in a region, doubling its support, its support in each riding in that region is doubled as well, for example from 15% to 30% in an individual riding.
[3](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-3)
If a party has gone from 10% to 20% in a region, increasing its support by 10 percentage points, its support in each riding in that region is increased by 10 percentage points, for example from 15% to 25% in an individual riding.
[4](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-4)
There is no boost for the presence of a Conservative or Bloc incumbent, as research suggests that incumbents from these parties have done no better than a generic candidate would have been expected to do in past elections.
[5](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-5)
For example, Newfoundland and Labrador’s share of national turnout has, on average, been 11% lower than its share of the national population over the last four elections, while Prince Edward Island’s has been 13% higher. Turnout in the Northwest Territories and Nunavut are also well below the national average, while they are higher in New Brunswick and Alberta.
[6](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-6)
The northern ridings in Saskatchewan and Manitoba, for instance, take up a smaller share of the Rural Saskatchewan and Rural Manitoba regions.
[7](https://www.thewrit.ca/p/vote-and-seat-projection-methodology#footnote-anchor-7)
If you guess that a party will under-perform the polls but, instead, the party out-performs the polls, your projection will be even worse than if you had made no assumptions about polling error in the first place.
#### Subscribe to The Writ
By Éric Grenier · Thousands of paid subscribers
Insights and analysis on Canadian politics and elections.
By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).
7 Likes∙ 
Share
#### Comments
TopLatestDiscussions
[Ontario pushes Liberals higher in seat projection](https://www.thewrit.ca/p/ontario-pushes-liberals-higher-in)
[Federal Projection Update for April 7, 2026](https://www.thewrit.ca/p/ontario-pushes-liberals-higher-in)
Apr 7 •
[Barring a polling upset, Mark Carney's Liberals will win](https://www.thewrit.ca/p/barring-a-polling-upset-mark-carneys)
[Some doubt remains about a majority victory, but the data suggests the Conservatives have come up short in key battlegrounds.](https://www.thewrit.ca/p/barring-a-polling-upset-mark-carneys)
Apr 28, 2025 •
[Who do Canadians think was the country's best prime minister?](https://www.thewrit.ca/p/best-pm-poll)
[An exclusive poll by Pollara for The Writ gives us the answer!](https://www.thewrit.ca/p/best-pm-poll)
Jan 23, 2023 •
See all
### Ready for more?
© 2026 Éric Grenier[Privacy](https://substack.com/privacy)[Terms](https://substack.com/tos)[Collection notice](https://substack.com/ccpa#personal-data-collected)
[Substack](https://substack.com) is the home for great culture
#### Cookie Policy
We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our [privacy policy](https://substack.com/tos).
ManageRejectAccept

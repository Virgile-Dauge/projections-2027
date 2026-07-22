---
title: How Predictive is the Pre-Election Pendulum?
id: how-predictive-is-the-pre-election-pendulum
tags:
- projections-electorales-bureaux-2027-b0b1c4
- swing-methods
- conditional-probability-model
- australia
- backtesting
created: '2026-07-21T18:35:51.880055Z'
updated: '2026-07-21T18:39:17.793250Z'
source: https://armariuminterreta.com/2021/08/11/how-predictive-is-the-pendulum/
source_domain: armariuminterreta.com
fetched_at: '2026-07-21T18:35:51.836981Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Armarium Interreta (August 2021) tests whether the pre-election electoral
  pendulum, converted into seat-win probabilities via Kevin Bonham''s method, actually
  predicts the post-election electoral map, using AEC two-party-preferred data for
  all ten Australian federal elections back to 1993. Reconstructs Bonham''s probabilistic
  model with parameters: per-seat standard deviation of 3.3% (average deviation from
  uniform swing across the last six federal elections), a +/-1 point incumbency/personal-vote
  adjustment for sophomore MPs and retiring/defeated incumbents respectively, and
  a rule mapping newly-created electorates to a ''retirement'' of whichever party
  previously held the seats it was carved from. Establishes the empirical track record
  used to validate uniform-swing-based conditional probability seat models before
  they are refined further (as in the companion ''Improving Seat Forecasts'' piece),
  and documents the standard-deviation and incumbency-adjustment parameters as reusable
  inputs for any seat-probability model built on top of simple swing.'
---

*Suggested by [[improving-seat-forecasts-based-on-the-uniform-swing-model]] — author's own earlier post establishing the track record of pendulum-based conditional probability models*

No truth stands alone.
In Australian politics, there’s often some discussion over whether a certain 2-party swing would be enough for one side or another to win a majority, with reference to the electoral pendulum prior to the election. Such a pendulum lines up all the Labor-held seats on one side, and all the Coalition-held seats on another, and (usually) assumes some kind of uniform swing to see how many seats would fall given a certain 2-party swing.
Uniform swing is a fairly useful assumption in a broad, general sense – the overall seat count is usually not too far off the projected figures from a uniform swing. However, leaving aside the problem with assuming every seat will swing the same way, uniform swing projections can be misleading when one side of the pendulum differs systematically from the other. For example, if Labor holds 14 marginal seats on margins of victory less than 3%, while the Coalition has just 4 marginals where they won by less than 3%, then even with very little overall swing we might expect the Coalition to make gains _on net_ as they would have more opportunities to win close seats from Labor than Labor would from them.
With that in mind, Dr Kevin Bonham [has recently released a probabilistic model](https://kevinbonham.blogspot.com/2021/08/the-2022-pendulum-only-slightly-favours.html) which estimates the probability that Labor or the Coalition wins each seat (given a certain two-party-preferred vote) and adds them up to produce an expected number of seats for each side (I highly suggest giving it a read to get a feel for the methodology used). He concludes that the 2022 pre-election pendulum slightly favours the Coalition, suggesting that Labor would need to win **51.2%** of the two-party-preferred to be better-than-even odds of winning a majority, while the Coalition would need to win **50.7%** of the two-party-preferred to have a greater than 50% chance of holding onto their majority.
Let’s take this as given; that is to say, if Labor wins 51.2% of the two-party-preferred on the pre-election pendulum, let’s assume they are roughly even-odds for a majority. What I’m interested in examining is this: given what we know of the pre-election pendulum, does that actually predict anything about what two-party-preferred they need to win on the actual map come election day?
Or, put another way: given historical shifts in the electoral map, does analysis of what the electoral map prior to the election actually tell us anything about what the electoral map on election day look like?
## Probabilistic modelling of the electoral pendulum
To undertake this analysis, I’ve extracted the 2-party-preferred figures for every electorate from Australian Electoral Commission (AEC) data, going back to 1993. As the AEC provides both the vote data as well as their estimates of the 2-party-preferred swing in every electorate, I was able to rebuild the pre-election pendulum for all ten federal elections going all the way back to 1993.
I’ve put together a probability model as similar as possible to Dr Bonham’s, using the following conditions:
  * Standard deviation for every electorate, 3.3%. This is a measure of how far we expect each electorate to deviate from uniform swing, on average.
  * If a new (i.e. sophomore) incumbent is contesting in this electorate, I added 1% onto the 2pp for that incumbent’s party. If an incumbent is either retiring or was defeated at the last election, I subtracted 1% from the 2pp for that incumbent’s party. This is to model the gain/loss of a personal vote – the share of an electorate who votes for their incumbent MP but who wouldn’t otherwise vote for the incumbent’s party.
  * I did not include Dr Bonham’s disendorsement adjustment, as I didn’t have enough data on which candidates were or were not disendorsed at past elections.
  * If a new electorate was created out of electorates all held by one party, I modelled it as having had a retirement from that party. For example, when the Division of Solomon was created, I modelled it as having had a Labor retirement, as it was created out of the Labor-held Division of Northern Territory.
  * I assumed any crossbenchers would hold their seats, and no new crossbenchers would be elected.


(The 2pp adjustments only apply to the pre-election figures, as they are meant to adjust for changes in incumbent status since the last election. When modelling post-election figures, I take the 2pp result as given and simply model a uniform swing onto it.)
Using this model, I estimated the 2pp required for either Labor or the Coalition to have a greater than 50% chance to win a **majority** (50% of seats, + 1) or to win a **plurality** (more seats than either party; realistically this means more seats than either side) on both the pre- and post-election pendulums. This allows us to compare how different the pre-election pendulum and the post-election pendulum ended up being by contrasting the predicted 2pp each side needed for a better-than-even-odds shot at majority/plurality to the 2pp they actually wound up requiring.
Here, I’ve listed the 2pp needed by each opposition to be better than even odds for a majority at each election going back to 1993:
### Opposition 2-party-preferred needed to have a greater than 50% chance of majority
(if you’re on a mobile device, scroll right for full data or turn your device landscape)  
| Election  | Estimated 2pp needed, pre-election estimates  | 2pp needed, post-election pendulum  | Difference  |  
| --- | --- | --- | --- |  
| Election  | Estimated 2pp needed, pre-election estimates  | 2pp needed, post-election pendulum  | Difference  |  
| --- | --- | --- | --- |  
| Average  | 50.7%  | 50.8%  | 0.6%  |  
| 1993  | 50.6%  | 50%  | 0.6%  |  
| 1996  | 50%  | 50.4%  | 0.4%  |  
| 1998  | 51.7%  | 51.8%  | 0.1%  |  
| 2001  | 51.5%  | 51.1%  | 0.4%  |  
| 2004  | 51.2%  | 51.5%  | 0.3%  |  
| 2007  | 51.5%  | 50.9%  | 0.6%  |  
| 2010  | 51%  | 50.8%  | 0.2%  |  
| 2013  | 49.8%  | 50.3%  | 0.5%  |  
| 2016  | 51.8%  | 51.4%  | 0.4%  |  
| 2019  | 50.9%  | 53%  | 2.1%  |  
| Average  | 50.7%  | 50.8%  | 0.6%  |  
| --- | --- | --- | --- |  
In general, oppositions have typically found it difficult to win a majority in recent years, with them needing to win an average **50.8%** of the 2-party-preferred to be better than even odds for a majority in their own right.  Of course, that is not the same thing as what they need to govern. If an opposition is just one or two seats short of a majority in its own right, most of the time they will be able to form government anyhow.  More importantly, there is a fairly strong correlation between the 2pp “predicted” before the election and the estimated 2pp they would have needed on election day:
The diagonal black line represents where the points would be, if the prediction was perfect. Points closer to the line are more accurate predictions. Unsurprisingly, 2019 is a stand-out in this regard.
Apart from 2019, the 2pp-required prediction by the model usually correlates pretty strongly with the 2pp-required estimated by the model using the actual election results. It’s also not too clear how much we should factor the 2019 election into our analysis. On the one hand, 2019 was exceptional for the mid-term switch in PM from one who did particularly well in inner metro areas to one who did particularly well in outer suburbs and the regions. Since something like that doesn’t seem to be happening this time around, it could be argued that we should discount 2019, in which case the post-election 2pp-needed figure differs from the pre-election 2pp-needed figure by just 0.4%.
On the other hand, it can be argued that the shifts seen in 2019 may either reverse at the next federal election (as both sides overperformed in some seats, e.g. Capricornia and Higgins) or may continue (as part of a global realignment of voters with tertiary qualifications towards the left and voters without such qualifications towards the right), in which case we might be concerned about a 2019-style shift in the electoral map at the next election. Furthermore, there is some pandemic-related weirdness going on with some states (e.g. Labor over-performing in Queensland and Western Australia; although I wouldn’t touch either state breakdown with a [Division-of-Durack](https://upload.wikimedia.org/wikipedia/commons/7/79/Division_of_DURACK_2016.png)-sized pole given historical errors) which may produce further shifts in the map.
All things considered, it’s probably best to include 2019 in the average; in which case the estimated margin of error on the 2pp needed for Labor to be even-odds to win a majority would be about +/- 1.5%.  Given the big outlier that is the 2019 federal election, I felt using a normal distribution would not be appropriate (possibly high kurtosis). I’ve estimated margin of error using a t8 distribution instead.  In other words, given historical shifts between the pre-election and the post-election pendulum, when we get the final results Labor may have ended up needing between **49.7%** to **52.7%** of the two-party-preferred to be even-odds for a majority depending on where swings end up. Note that the probability is not evenly distributed throughout that margin of error; in other words it is more likely that the actual 2pp Labor ends up needing is somewhere between 50.6% – 51.8% than it is that Labor will end up needing just 49.8% of the 2pp.
Instead of analysing things on a government-vs-opposition basis, another metric I can use to analyse how much an electoral pendulum favours one side is what I call the tipping-point metric. I’ve defined this as the point at which both sides have a roughly 50% chance to win more seats than the other; it can be used to estimate how skewed an electoral map is. For example, if Labor needs to win 51% of the 2pp to be even-odds to win more seats than the Coalition, then the map is probably at least somewhat skewed against Labor.
As per Dr Bonham’s analysis, the tipping-point for the electoral pendulum ahead of the 2022 election is about 49.75%. I’ve listed the predicted and actual tipping-points for each election as per the model (figures are Coalition two-party-preferred):
### Predicted versus actual tipping-point votes per election
(if you’re on a mobile device, scroll right for full data or turn your device landscape)  
| Election  | Predicted tipping-point  | Actual tipping-point  | Difference  |  
| --- | --- | --- | --- |  
| Election  | Predicted tipping-point  | Actual tipping-point  | Difference  |  
| --- | --- | --- | --- |  
| Average  | 0.6%  |  
| 1993  | 50.5%  | 49.6%  | 0.9%  |  
| 1996  | 49.7%  | 49.6%  | 0.1%  |  
| 1998  | 48.9%  | 48.5%  | 0.4%  |  
| 2001  | 49%  | 49.2%  | 0.2%  |  
| 2004  | 49.3%  | 49.1%  | 0.2%  |  
| 2007  | 48.9%  | 49.6%  | 0.7%  |  
| 2010  | 50.5%  | 49.9%  | 0.6%  |  
| 2013  | 49.1%  | 49.4%  | 0.3%  |  
| 2016  | 48.8%  | 49.5%  | 0.7%  |  
| 2019  | 50.2%  | 48%  | 2.2%  |  
| Average  | 0.6%  |  
| --- | --- |  
These figures are pretty similar to what we saw with the 2pp needed by the opposition for a majority; an average shift of about **0.6%** between the tipping-point predicted before the election and the actual tipping-point on election day, with an unusually large shift in 2019.
However, there are some interesting differences of note. Firstly, in our sample, the actual tipping-point on election day tends to end up in Labor two-party-preferred territory. Or, in other words, the final, post-election pendulum tends to be skewed against Labor, even if the electoral map drawn prior to the election favours Labor.  The reason varies from election to election: for example, in 1993, Labor won big swings to it mostly in safe and Labor-leaning seats (e.g. Calwell, Grayndler, Lalor, Maribyrnong) meaning that a lot of its vote ended up “wasted” in landslide victories in seats it would have won anyhow.More recently, in the 2019 election, while the pre-election electoral map appeared to be fairly balanced (if anything with a very small skew to Labor), Labor ended up winning big swings to it in mostly safe or Coalition-leaning seats (e.g. Higgins, Wentworth, Warringah, Curtin, Kooyong) while suffering big swings against it in marginals (e.g. Capricornia, Dawson, Herbert, Forde), meaning that it would require a greater share of the 2-party-preferred to win more seats than the Coalition on the post-election pendulum. 
I would advise not taking too much notice of this; as our previous table demonstrates, in general it is fairly hard for oppositions to win a majority, and Labor has been the opposition at seven of the ten elections in our sample. Although I don’t have the exact data to construct a pendulum for it, the tipping-point in the 1990 election would almost certainly require the Coalition to win a decent majority on the 2-party-preferred vote, as Labor managed to win a majority at that election despite narrowly losing the 2pp.
Secondly, and more importantly, unlike the 2pp-required-for-even-chance-at-majority metric, there is relatively little correlation between the tipping-point prior to an election and the actual tipping-point estimated from the election results:
Black line represents where the points would lie if the predictions were perfect. Points closer to the black line represent more accurate predictions.
The significant outlier that is 2019 is a large chunk of the reason why there is pretty much no correlation; if I toss it out of the dataset, the amount of variance explained by our model’s predictions (the R2 value listed) goes up to 0.84. Still, as I’ve noted above, it probably is best to keep 2019 in rather than toss it out; on that basis it’s probably fair to say there is relatively little correlation between whether the pendulum prior to an election favours one side and whether the actual pendulum after the election still favours that side.
## What does this mean for the next federal election?
From Dr Bonham’s analysis, the pendulum is very slightly tilted to the Coalition, with Labor needing a 2pp of **51.2%** to be even-odds for a majority while the Coalition needs just **50.7%** to have even-odds of holding theirs (and a tipping-point of Coalition **49.75%**). This is in line with recent history as oppositions have historically needed about 50.8% of the 2pp to win a majority on the pre-election pendulum, while governments have historically needed about 50.2% of the same.
However, given the historical average for pendulum shifts, the actual pendulum which happens on election day could require Labor to win anywhere between **49.7%** and **52.7%** of the 2-party-preferred to be even-odds for a majority, with a plausible tipping point (or map skew) between Coalition **51.4%** to Coalition **48.1%** (though, as noted above, it is more likely to be somewhere in the middle of those ranges than towards the extremes).
In other words – the skew to the Coalition is fairly small, and is subject to a great deal of uncertainty as to whether it will persist on Election Day. Small changes in how each party does in different regions – e.g. the Coalition rebounding in seats like Warringah, Wentworth and Curtin, or Labor overperforming in newly marginal seats such as Higgins and Flinders – could easily remake the map and shift the 2pp needed by either side for a majority. While the pre-election 2pp-required-by-opposition-for-even-odds-at-majority  I would abbreviate this, but my writing style sounds enough like a stuffy academic already. No need for me to go about inventing inscrutable acronyms as well.  is usually fairly predictive of the actual 2pp required by the opposition for even odds at a majority, the pre-election map skew (as measured by the tipping-point 2pp) has historically not been very predictive of which side the post-election map will favour. Pending further shifts (e.g. retirements, strong independent challengers), it’s probably best to take the map as fairly balanced, for now.
The data used in this piece (and the pendulums + models for every election dating back to 1993) are available for download [here](https://github.com/ArmariumInterreta/Armarium/blob/master/PendulumPredictiveness/PastAusElectionPendulums.xlsx?raw=true).
[Copy Link](https://armariuminterreta.com/#copy_link "Copy Link")[Email](https://armariuminterreta.com/#email "Email")[Facebook](https://armariuminterreta.com/#facebook "Facebook")[Twitter](https://armariuminterreta.com/#twitter "Twitter")[WhatsApp](https://armariuminterreta.com/#whatsapp "WhatsApp")[Tumblr](https://armariuminterreta.com/#tumblr "Tumblr")[Reddit](https://armariuminterreta.com/#reddit "Reddit")[Pocket](https://armariuminterreta.com/#pocket "Pocket")
## Add Your Comment 
You must be [logged in](https://armariuminterreta.com/wp-login.php?redirect_to=https%3A%2F%2Farmariuminterreta.com%2F2021%2F08%2F11%2Fhow-predictive-is-the-pendulum%2F) to post a comment.
We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits, as well as personalising marketing. By clicking “Accept”, you consent to cookies.
Manage consent
Close
#### Privacy Overview
This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the ...
Necessary 
Necessary
Always Enabled
Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.
Non-necessary 
Non-necessary
Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website.
[×](javascript:void\(0\)) [Home](https://armariuminterreta.com/) [Politics](https://armariuminterreta.com/politics/) [Economics](https://armariuminterreta.com/econ/) [Projects](https://armariuminterreta.com/projects/)
[×](javascript:void\(0\))
You appear to be using an outdated browser, for which this site is not optimised.
For your security, we strongly recommend you download a newer browser.
Although any of the latest browsers will do, we suggest the latest version of Firefox.
[Download Firefox here](https://www.mozilla.org/en-US/firefox/new/)
(Click on the button in the top-right to close this reminder)
Copy link
✓
Merci d'avoir partagé!
Instantly find any service to add to

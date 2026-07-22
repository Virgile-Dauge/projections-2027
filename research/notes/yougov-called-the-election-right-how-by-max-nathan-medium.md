---
title: YouGov called the election right. How? | by Max Nathan | Medium
id: yougov-called-the-election-right-how-by-max-nathan-medium
tags:
- mrp
- uk-mrp
- mrp-methodology
- yougov
created: '2026-07-21T18:30:35.231336Z'
updated: '2026-07-21T18:39:17.703625Z'
source: https://maxnathan.medium.com/yougovs-big-data-model-predicted-the-2017-general-election-result-34aea5ed8d4a
source_domain: maxnathan.medium.com
fetched_at: '2026-07-21T18:30:35.190018Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: commentary
content_type: blog
deprecated: false
summary: 'Max Nathan (Professor of Economic Geography, UCL, June 2017) breakdown of
  why YouGov''s MRP got 2017 right when other polls failed: correctly predicted the
  national result and 93% of individual constituency outcomes, including the Canterbury
  upset (first Labour win since 1918). Lists the 5-step pipeline: (1) weekly individual-level
  panel data (~50k interviews/week) on vote intention plus detailed characteristics
  including past vote; (2) build a typology of voter types; (3) fit a predictive model
  per voter type; (4) estimate the geographic spread of each type per constituency
  using British Election Study + ONS area classifications; (5) aggregate to constituency
  vote estimates — contrasted with traditional polling''s direct-sample-to-national-projection
  via weights. Attributes MRP''s edge to larger sample, micro-to-macro local-issue
  capture (e.g., Canterbury hospital-closure crisis), fine-grained + high-frequency
  updating, and improving model quality over successive election cycles; flags earlier
  MRP variants correctly called the 2016 Leave vote and did well in the 2016 US presidential
  election.'
---

[Sitemap](https://maxnathan.medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)
Sign up
Get app
Sign up
# **YouGov called the election right. How?**
Follow
4 min read Jun 12, 2017
Share
Press enter or click to view image in full size
Political scientist Matthew Goodwin eats his book live on TV.
This General Election has been full of surprises. So I’ve been digging into [the YouGov MRP voting model](https://yougov.co.uk/news/2017/06/09/the-day-after/), pretty much the only one that got the 2017 Election result correct.
Given [all the](https://www.theguardian.com/commentisfree/2017/jun/10/jeremy-corbyn-general-election--labour-rewrites-rules) [current](http://www.telegraph.co.uk/news/2017/06/11/watch-labour-moderates-now-flock-corbyn/) [humble pie](https://www.theguardian.com/commentisfree/2017/jun/10/i-was-wrong-about-jeremy-corbyn-still-doubt-him) and [book eating](https://www.youtube.com/watch?v=FOqPlIzvS1Q) by pundits who didn’t spot the result coming, this seems worth doing. I also think there are also some useful takeaways for cities, especially as devolution rolls on.
YouGov’s MRP (multilevel regression and post-stratification) method **not only got the national result right** , but **correctly predicted results in 93% of seats**. [Compare this to most other polls](https://www.ft.com/content/dac3a3b2-4ad7-11e7-919a-1e14ce4af89b) [£, and chart below]. The model somehow also predicted the Canterbury result, where Labour won for the first time since 1918.
It turns out that earlier versions of an MRP model also [spotted the Leave vote in 2016](http://www.benjaminlauderdale.net/wp/?p=210), and did pretty well in the US 2016 Presidential Election. Though this version seems to have worked better, for reasons I’ll come back to. Remember, this is a predictive method — how might people vote in the future? — that did about as well as the main exit poll — which asked people *how they just voted*. (John Curtice has more on how UK exit polling is done [here](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-985X.2007.00536.x/full).)
So how does the MRP model work? [Here’s an overview](https://yougov.co.uk/news/2017/05/31/how-yougov-model-2017-general-election-works/). YouGov describe this as a Big Data approach; it seems to involve bespoke data and data science methods, but also lots of public datasets, aka ‘administrative Big Data’. The key steps seem to be:
**1/** YouGov have weekly individual-level data on voting intention and detailed characteristics (including past voting). They run around 50k online interviews per week, and [anyone can sign up](https://yougov.co.uk/account/register/); **2/** They use this to build a typology of voter types; **3/** For each voter type, they then fit a model that predicts voting intention; **4/** For each constituency, they then estimate how these types are spread (using public resources like the [British Election Study](http://www.britishelectionstudy.com/) and other ONS resources, perhaps [these](https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications/2011areaclassifications));**5/** They work out how the vote should go in each constituency. By contrast, traditional polls tend sample about 1,000 people, then project direct from respondents to the whole UK, using weights to compensate for demographics, voting intention and so on.
## Get Max Nathan’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
This helps us see why an MRP approach might work better than conventional methods:
  * **First, MRP has a much bigger starting sample.** More observations = sharper results.
  * **Second, MRP is micro-to-macro** : it models each constituency individually, so stands a better chance of picking up local issues (such as the hospital closure crisis which helped drive the Canterbury result).
  * **Third, MRP is both fine-grained and high-frequency.** The only pundits to pick up on the reality of #GE2017 got out there on the ground. Given the complexity of UK politics right now, we also need methods to get at this complexity in a structured way.
  * **Fourth, MRP methods should get better over time.** you end up with loads of high-frequency training data, and this progressively makes the model better.


This doesn’t mean that conventional polling has had its day – e.g. Survation were [also on the money](http://survation.com/weve-changed-polling-methodology-since-2015/). But it’s notable that most conventional polls fell over this time, just as they did in the 2015 General Election. I suspect that these four factors helped YouGov pick up**higher turnout for younger voters** faster than most pollsters (and many mainstream journalists), as well as **shifts in other age groups**. [This post](https://twitter.com/benlauderdale/status/874175733601579009) by Ben Lauderdale, one of their chief modellers, seems to supports that. (Note that we won’t _know_ turnout by age for sure until the next BES in a few months. If modelling can get us to a decent understanding faster, that’s very useful.) [ As Sam Freedman points out](https://twitter.com/samfr/status/873585120355246082), it also helps show precisely, and in close to real time, the huge damage the Conservative manifesto did to the party’s chances.
**Micro-to-macro techniques like MRP could be** **useful for Mayoral elections and city politics**. With a 50k in sample, could you train the model on a city-region like the West Midlands using public data? If so, this feels much more useful and adaptable than one-off traditional polling. YouGov say their model works at local authority level, so some version of this could probably be done now. However, I suspect that even a big national sample might be too sparse for very local analysis, say at neighbourhood level. In this latter case, **you could also imagine building a richer, locally-specific model for a whole conurbation** — like the West Midlands or Greater Manchester — using a big base of local respondents.
This would be expensive — but **for a local university, or a group of them, it would be a super interesting (and public-spirited) long term investment**.
Birmingham University’s [city-regional lab City-REDI](http://www.birmingham.ac.uk/schools/business/research/city-redi/index.aspx) will be exploring this further in the coming months.
_Thanks to_ _for comments on an earlier draft._
Follow
## [Written by Max Nathan](https://maxnathan.medium.com/?source=post_page---post_author_info--34aea5ed8d4a---------------------------------------)
Professor of Economic Geography at UCL. Also CEP Urban Programme. Co-founder @centreforcities & @whatworksgrowth. My views. I’m at [max-nathan.github.io](http://max-nathan.github.io).
Follow
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.

---
title: How the YouGov model for the 2017 General Election works
id: how-the-yougov-model-for-the-2017-general-election-works
tags:
- mrp
- uk-mrp
- mrp-methodology
- yougov
created: '2026-07-21T18:29:26.061936Z'
updated: '2026-07-21T18:38:49.833463Z'
source: https://yougov.co.uk/politics/articles/18266-how-yougov-model-2017-general-election-works
source_domain: yougov.co.uk
fetched_at: '2026-07-21T18:29:26.024555Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: YouGov's official explainer (Doug Rivers, chief scientist) of the MRP methodology
  used for the 2017 UK general election. ~7,000 daily panellists (50,000/week) yield
  only ~75 respondents per constituency/week, too sparse for direct estimates, so
  MRP pools data across constituencies via a model relating interview date, constituency,
  demographics, and past vote to current voting intention, then post-stratifies against
  ONS census counts, British Election Study, and past results. Model built by Ben
  Lauderdale (LSE) with YouGov Data Science (Doug Rivers), fit via Hamiltonian Monte
  Carlo in Stan (developed by Andrew Gelman at Columbia). States explicitly that MRP
  output is a snapshot of current intention, not a forecast, and that the reported
  95% CI is expected to be wrong in 30-40 of 650 constituencies.
---

Basculer vers le site français [ Basculer vers le site français ](https://yougov.com/fr-fr)
### Doug Rivers, YouGov's chief scientist, sets out how YouGov's 2017 General Election model works
Every day YouGov interviews approximately 7,000 panellists about their voting intentions in the 2017 General Election. Over the course of a week, data are collected from around 50,000 panellists. While this is a much larger sample than our usual polls, the samples in each of the 650 Parliamentary constituencies are too small (on average, only 75 voters per constituency per week) to produce reliable estimates.
In the 2016 EU Referendum, in the 2016 US Presidential election, and again in the 2017 UK General Election, YouGov is using a recently developed technique called Multilevel Regression and Post-stratification (or 'MRP' for short) to produce estimates for small geographies (local authorities for the EU referendum, states in the 2016 American Presidential election, and Parliamentary constituencies for the 2017 General Election).
The idea behind MRP is that we use the poll data from the preceding seven days to estimate a model relating interview date, constituency, voter demographics, past voting behaviour, and other respondent profile variables to their current voting intentions. This model is then used to estimate the probability that a voter with specified characteristics will vote Conservative, Labour, or some other party. Using data from the UK Office of National Statistics, the British Election Study, and past election results, YouGov has estimated the number of each type of voter in each constituency. Combining the model probabilities and estimated census counts allows YouGov to produce a fairly accurate estimate of the number of voters in each constituency intending to vote for a party on each day.
It is important to understand the limitations of the model results. First, they are estimates of current voting intentions, not a forecast of how people will vote on 8 June. Panellists tell us how they intend to vote, but they may change their minds and we do not attempt to quantify this uncertainty. Second, the samples in each constituency are too small to be reliable by themselves and are subject to more than just sampling error. To compensate for small sample sizes, we rely on a model that pools data across constituencies. This uses data from panellists who live in other constituencies to augment the small number of actual interviews conducted in a constituency. The model is based on the fact that people with similar characteristics tend to vote similarly, but not identically, regardless of where they reside. While this has worked well in the past (our MRP model in the 2016 EU Referendum consistently showed that more voters favoured leave than remain, and that Hillary Clinton would win the popular vote in the 2016 US Presidential election by a narrow margin, but that midwestern battleground states were too close to call), models cannot produce estimates as accurate as a full scale poll in each constituency.Using MRP, we have classified constituencies as safe, likely, or leaning to a party or as a toss-up. The displays for each constituency provide a vote estimate for each party and a 95% confidence interval. These are the model's best guess of what a large poll would show if it were conducted in that constituency on the same day. Readers should focus on the confidence intervals as giving a more reliable estimate of current voting intentions. Even these are not fail-safe: we would still expect the interval to be wrong in 30 to 40 constituencies.The model was developed primarily by Professor Ben Lauderdale of the London School of Economics in conjunction with YouGov's Data Science team, headed by Doug Rivers of Stanford University. The data are streamed directly from YouGov's survey system to its Crunch analytic database. From there, the models are fit using Hamiltonian Monte Carlo with the open source software Stan. Stan was developed at Columbia University by Andrew Gelman and his colleagues, with support from YouGov and other organisations. YouGov will be updating the model estimates on a daily basis.
[**You can download a .csv file of the raw data here (new data will be available each time the model is updated)**](https://yg-infographics-data.s3.amazonaws.com/uk-elections-2017/figures/party_constituency_vote_shares.csv)
[**Subscribe to the YouGov newsletter**](https://yougov.com/en-gb/articles/18266-how-yougov-model-2017-general-election-works?marketo=newsletter)
## Related topics
## Related content
[ YouGov News Tracker: 19-20 July 2026 Article ](https://yougov.com/en-gb/articles/55207-yougov-news-tracker-19-20-july-2026)[ Voting intention, 19-20 July 2026: Ref 23%, Con 21%, Lab 20%, Grn 14%, LD 12% Article ](https://yougov.com/en-gb/articles/55205-voting-intention-19-20-july-2026-ref-23-con-21-lab-20-grn-14-ld-12)[ Greater Manchester 2026 mayoral by-election voting intention Article ](https://yougov.com/en-gb/articles/55197-greater-manchester-2026-mayoral-by-election-voting-intention)[ What do Labour members think should be the biggest priorities for Andy Burnham? Article ](https://yougov.com/en-gb/articles/55181-what-do-labour-members-think-should-be-the-biggest-priorities-for-andy-burnham)[ As his time as prime minister comes to an end, what do Britons think of Keir Starmer? Article ](https://yougov.com/en-gb/articles/55184-as-his-time-as-prime-minister-comes-to-an-end-what-do-britons-think-of-keir-starmer)[ Half of Britons have seen AI-generated actors in ads – and they don’t like them Article ](https://yougov.com/en-gb/articles/55180-half-of-britons-have-seen-ai-generated-actors-in-ads-and-they-dont-like-them)[ YouGov News Tracker: 12-13 July 2026 Article ](https://yougov.com/en-gb/articles/55173-yougov-news-tracker-12-13-july-2026)[ UK Advertisers of the Month 2026 Article ](https://yougov.com/en-gb/articles/53980-uk-advertisers-of-the-month)[ Voting intention, 12-13 July 2026: Ref 24%, Con 19%, Lab 19%, Grn 15%, LD 13% Article ](https://yougov.com/en-gb/articles/55167-voting-intention-12-13-july-2026-ref-24-con-19-lab-19-grn-15-ld-13)[ Big YouGov Voter Study 2026: What do Restore Britain supporters see in the party? Big Survey ](https://yougov.com/en-gb/articles/55157-big-yougov-voter-study-2026-what-do-restore-britain-supporters-see-in-the-party)[ Big YouGov Voter Study 2026: How has the Lib Dem coalition changed over the last two years? Big Survey ](https://yougov.com/en-gb/articles/55156-big-yougov-voter-study-2026-how-has-the-lib-dem-coalition-changed-over-the-last-two-years)[ Big YouGov Voter Study 2026: What do Green voters think of the party? Big Survey ](https://yougov.com/en-gb/articles/55154-big-yougov-voter-study-2026-what-do-green-voters-think-of-the-party)[ Big YouGov Voter Study 2026: How solid is Reform UK's rise? Big Survey ](https://yougov.com/en-gb/articles/55153-big-yougov-voter-study-2026-how-solid-is-reform-uks-rise)[ Big YouGov Voter Study 2026: What has happened to the Conservatives’ 2024 voters? Big Survey ](https://yougov.com/en-gb/articles/55152-big-yougov-voter-study-2026-what-has-happened-to-the-conservatives-2024-voters)[ Big YouGov Voter Study 2026: Why have some voters stayed loyal to Labour over Keir Starmer’s premiership? Big Survey ](https://yougov.com/en-gb/articles/55151-big-yougov-voter-study-2026-why-have-some-voters-stayed-loyal-to-labour-over-keir-starmers-premiership)[ Big YouGov Voter Study 2026: Which voters abandoned Labour over Keir Starmer’s premiership and why? Big Survey ](https://yougov.com/en-gb/articles/55150-big-yougov-voter-study-2026-which-voters-abandoned-labour-over-keir-starmers-premiership-and-why)[ Big YouGov Voter Study 2026 Big Survey ](https://yougov.com/en-gb/articles/55149-big-yougov-voter-study-2026)[ UK Word of Mouth Risers 2026 Article ](https://yougov.com/en-gb/articles/54202-uk-word-of-mouth-risers-2026)[ Most Britons say Nigel Farage is ‘very sleazy’ Article ](https://yougov.com/en-gb/articles/55146-most-britons-say-nigel-farage-is-very-sleazy)[ UK Biggest Brand Movers 2026 Article ](https://yougov.com/en-gb/articles/54668-uk-biggest-brand-movers-2026)[ YouGov News Tracker: 5-6 July 2026 Article ](https://yougov.com/en-gb/articles/55141-yougov-news-tracker-5-6-july-2026)[ Decisive but untrustworthy: how do Britons feel about Nigel Farage? Article ](https://yougov.com/en-gb/articles/55137-decisive-but-untrustworthy-how-do-britons-feel-about-nigel-farage)[ Snap poll: Britons tend to oppose Nigel Farage by-election Article ](https://yougov.com/en-gb/articles/55135-snap-poll-britons-tend-to-oppose-nigel-farage-by-election)[ Labour members on the next chancellor, tax, welfare, and the triple lock Article ](https://yougov.com/en-gb/articles/55121-labour-members-on-the-next-chancellor-tax-welfare-and-the-triple-lock)[ Voting intention, 5-6 July 2026: Ref 25%, Con 21%, Lab 20%, Grn 13%, LD 12% Article ](https://yougov.com/en-gb/articles/55116-voting-intention-5-6-july-2026-ref-25-con-21-lab-20-grn-13-ld-12)[ 250 years after independence: how do Britons see the USA? Article ](https://yougov.com/en-gb/articles/55101-250-years-after-independence-how-do-britons-see-the-usa)[ YouGov News Tracker: 29-30 June 2026 Article ](https://yougov.com/en-gb/articles/55097-yougov-news-tracker-29-30-june-2026)[ How do Britons see the parties, summer 2026? Article ](https://yougov.com/en-gb/articles/55091-how-do-britons-see-the-parties-summer-2026)[ UK climate change attitudes unchanged by heatwave Article ](https://yougov.com/en-gb/articles/55086-uk-climate-change-attitudes-unchanged-by-heatwave)[ How would Britain vote, two years since the 2024 election? Article ](https://yougov.com/en-gb/articles/55084-how-would-britain-vote-two-years-since-the-2024-election)[ Voting intention, 28-29 June 2026: Ref 24%, Con 20%, Lab 20%, Grn 13%, LD 13% Article ](https://yougov.com/en-gb/articles/55066-voting-intention-28-29-june-2026-ref-24-con-20-lab-20-grn-13-ld-13)[ How popular is Donald Trump in Europe? June 2026 Article ](https://yougov.com/en-gb/articles/55067-how-popular-is-donald-trump-in-europe-june-2026)[ How popular are national leaders in Europe? June 2026 Article ](https://yougov.com/en-gb/articles/55068-how-popular-are-national-leaders-in-europe-june-2026)[ Views of Andy Burnham’s character have become more negative since May Article ](https://yougov.com/en-gb/articles/55061-views-of-andy-burnhams-character-have-become-more-negative-since-may)[ What do Britons think about the UK’s relationship with the US – in their own words Article ](https://yougov.com/en-gb/articles/55051-what-do-britons-think-about-the-uks-relationship-with-the-us-in-their-own-words)[ Who would make the best prime minister? June 2026 Article ](https://yougov.com/en-gb/articles/55048-who-would-make-the-best-prime-minister-june-2026) Load more 
## Our use of cookies
We use cookies to improve the functionality and performance of our website, to analyse web traffic and for advertising purposes. [Learn more](https://platform.yougov.com/legal/privacy-notice)
Cookies Settings
Don’t Accept Accept
## Privacy Preference Centre
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences, or your device, and is mostly used to make the site work as you expect. The information does not usually identify you directly, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to learn more and change our default settings. Blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://yougov.co.uk/about/policy)
Allow All
### Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources, so we can measure and improve the performance of our site. They help us know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies, we will not know when you have visited our site.
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third-party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
  * checkbox label label


Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices

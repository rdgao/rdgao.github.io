---
title: 'Neuronal Timescales - the Director''s Cut: Third Research Paper Published (Part 2/3)'
tags: [Reflections, Mind & Brain, Science Communication]
status: publish
type: post
published: False
header:
  overlay_image: /assets/images/blog/2021-01-13-schematic.png
  overlay_filter: rgba(0,0,0,0.8)
  teaser: /assets/images/blog/2021-01-13-schematic.png
classes:
  - wide

toc: true
toc_label: "outline"
toc_icon: "space-shuttle"

permalink: /blog/:year/:month/:day/

excerpt: " "
---

/assets/images/blog/2021-01-20-

This is Part 3 (of 3) of the blog series on neuronal timescales, you can find here [Part 1][part_1] and [Part 2][part_2]. .

# 10. tenured professor runs own analysis...(October 2019)

...and graduate student proceeds to *almost* break it. 

Part 2 got to the end of Christmas 2019. For this final story, I have to rewind a little bit, back to late October of 2019. This is right around SfN2019 in Chicago, and I gave a poster presentation on all the new results so far, including the anatomy and gene expression correlates. It went really well, and it was the last SfN as graduate students for the rest of the original cohort in the lab (but the first time shotgunning a beer for some). Right around then, we were starting to think about writing this work up and publishing it, reasonably confident that it would be quick (it was not) and that I'd be graduating soon (I did not). 

![two_weeks][two_weeks]

For a paper like this to be meaningful, at the end of the day, you need to show some kind of behavioral relevance, otherwise "it's just a methods paper". This is especially true if most of the results, while cool, was recapitulating existing knowledge from non-human work. So we got to brainstorming. I say "we", but in this particular case, it was actually just Brad, and I didn't have much to do with prototyping this idea until we were ready to QA/refine the code and make the figures (though I almost broke the analyses a few times). I have two very vivid memories that summarize how this happened, and both had the flavor of "I thought tenured professors didn't run their own analyses anymore."

**Moment 1:** I'm sitting in lab minding my own business, as one does pre-pandemic, probably making my SfN poster. Brad comes in and goes "yoooo check this out". We had talked about trying to show some behavioral relevance already, but apparently he couldn't bear waiting for me to start digging around, so he went and did it himself. Obviously we weren't going to run our own experiment at this point of the project (and given the historical precedent, or the lackthereof), so he found a human ECoG dataset collected during a working memory task that a friend from Bob Knight's lab had deposited on CRCNS (the other patron saint of my PhD). This is vivid in my mind because we were sitting at the round kitchen table in the lab, and Brad described the experiment to me, and asked whether I think timescale would increase or decrease during working memory maintenance...

The structure of the task was classical as far as working memory experiments go: there's a pre-stimulus baseline period, then a set of visual stimuli comes on the screen, then a blank delay period, then a cue for context-dependent recall response. In this case, there's a pretty straightforward hypothesis: if working memory is the active maintenance of information, then it would be reasonable to expect the neural activity in those involved regions to have "more history", or longer timescale. It's a rather naive guess, but I went with it and said "increase", and he had this dramatic slow-roll with a suppressed smugness on his face: it actually turned out to be true! We scrolled through dataframes in a Jupyter notebook and he called up the pre vs. post t-test statistics, and yup, there it was. During the delay period (holding onto information), timescale in all the recorded regions saw an increase relative to baseline (obviously the nice figure here was my doing, tyvm).

![pre_post][pre_post]

I was swelling with pride—my associate professor of an advisor is ready to become a PhD student again. But seriously, it was really weird and really fun to have that role reversal.

![PIs_code][PIs_code]

**Moment 2:** before the pandemic, Eric and I got into a nice habit of going to this bar in San Diego for house music on Wednesday nights (RIP Blonde). On one such Wednesday, we were at said bar and I'm shuffling my feet, and I get a Slack message from Brad:

![mind_blown][mind_blown]

Note the timestamp (it was actually 11PM PST, so not quite as bad as it looks...for both of us). This was apparently 2 days after Moment 1 above (and 2 days before flying out to Chicago), where I said I was going to check over his code, and I obviously hadn't looked at it in the ensuing 48 hours. I don't want to make it seem here like Brad's always on my ass after work hours, because he never is. I'm usually the one sending random messages in the dead of night because that's when I work sometimes. But here we are on a Freaky Friday Wednesday, and I remember this SO vividly because I'm now standing in the middle of this tiny crowded dance floor staring at my phone. Alright, my interest is piqued, shoot: 

so what he had done was, beyond looking at within-individual timescale changes from pre- to post-delay period, he looked for *across-individual* trends. Specifically, was there a relationship between a person's modulation of timescale and their average performance on this working memory task? This would be kind of crazy cool even without making any causal claims, because it's a direct correlate of behavioral outcome. And yeah, consider my mind blown, because it turned out, across the 15 or so people in the dataset, the worse their average performance was, the less their timescale increased from pre- to post-delay, and this was only true for PFC. 

![pfc_wm][pfc_wm]

Going all the way back to the radioactive decay analogy: the more volatile (shorter timescale) the element was, the faster all of it disappears, and the less useful it would be for reconstructing events farther back in history. Except, in the case of brain activity, we are apparently able to modulate the timescale of our neural activity based on behavioral demands, and the longer the modulation, the better performance one got (or vice versa, not sure), at least in this very simple task. There are lots of caveats and open questions here, especially in the causal direction of the modulation (is it brain modulating behavior, or behavior modulating brain, and where do neuromodulators come in?)

These were precious moments, from which came the core of the final analysis in the paper (Figure 4A-D). Of course, the "checking it twice" part of making a list again took way longer than making the list itself. In this particular case, I inherited the notebooks, refactored, broke the analysis, fixed it, broke it some more, fixed it some more, ran it through the gauntlet of tests until we were both reasonably confident that the result was not a fluke. These next two snippets of messages perfectly capture the sentiment of this particular analysis, and as a whole, the project (and really, *science*).

![holyshit][holyshit]

![fixedit][fixedit]

[two_weeks]:two_weeks.png#center
[pre_post]:pre_post.png#center
[PIs_code]:PIs_code.png#center
[mind_blown]:mind_blown.png#center
[pfc_wm]:pfc_wm.png#center
[holyshit]:holyshit.png#center
[fixedit]:fixedit.png#center

---
# 11. the wrap-up (January - March 3324917, 2020)
As I'd mentioned, it did not take two weeks from then to finish the paper. But this wasn't due to anything extraordinarily frustrating or stupid, it was just plain academic optimism and the inability to estimate time into the future. I had presented this complete set of results (including the behavioral stuff above) a few times, including to my PhD committee in my pre-defense meeting in January 2020. We collected all the feedback, prioritized the most damning criticisms, and did some extra work to address them. Protip: obviously, comments and feedback from trusted advisors almost always improve the project. But there's an additional art to getting your paper trashed preemptively, so that you can address those shortcomings before the first round of reviewers have an opportunity to trash it harder. This saves time and emotional turmoil for everybody. 

In this case, there were concerns over the validity of the correlations between the cortical timescales and the T1T2 and gene expression maps. I did a couple of things to mitigate that, including the gene ontology analysis, as well as redoing everything with the addition of regressing out the T1T2 map from both the timescale and the gene maps, then correlating their residuals as a way of asking "which genes relate to timescales above and beyond what's expected from this primary anatomical hierarchy?" Just like the previous sentence, none of this is terribly...sexy, let's say, in the context of the main results, i.e., finding the correlations in the first place. But I think I've realized in the course of my PhD that, almost always, the time consuming part is not the original discovery itself, but the checking and rechecking everywhichway afterwards. 

Or maybe it's not, maybe the endless thirst in finding out the answer for that very first time makes time itself feel like it's running faster, and everything afterwards just feels like a big fucking drag. Alas, that's science today: gone are the days where you can cook something up and send in a 2-page Nature Letter, literally like a correspondence to your bud. But I suppose that's a good thing, and makes for better science. Plus, we have computers, Google, and open source data and software packages, like scipy, pandas, [NAPP][napp], and [this package][brainsmash] for spatial autocorrelation-preserving surrogate analysis, which, forunately for me, came out right around the time we needed it. Can you imagine trying to code this thing up by myself for this project? It'd be a primo hackjob. All these things make my life infinitely easier as a scientist, and none of this would be possible without them. This really made me appreciate how much foresight the people that started these various large-scale efforts had, like HCP, the Allen Institute, and CRCNS, as well as the various open source software development communities, obviously. I don't know how well I'll keep to this because laziness, but reflecting on this right now makes me genuinely want to not write shit code-not from a perspective of "that's obviously the right thing to do", but from a deep place of appreciation inside my heart, because maybe one day someone else would find a few lines I wrote useful.

rest of early 2020, pandemic
writing it up, markdown cells in JN, using pandas
2 months holed up, then desert
submission, Nature
eLife
final thoughts



[brainsmash]:
[napp]: https://www.nature.com/articles/s41593-020-00744-x

<iframe width="560" height="315" src="https://www.youtube.com/embed/9FjhTtNDbjw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



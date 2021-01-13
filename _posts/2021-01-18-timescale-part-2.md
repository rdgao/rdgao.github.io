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

excerpt: "Life's comedy is inspired by tragedies, especially someone else's. From that perspective, this blog post probably won't be anywhere nearly as entertaining as the [organoid one][org_blog], because I'm not unleashing 5 year's worth of pent up frustration and despair in one sitting. It was all quite pleasant, actually."
---

/assets/images/blog/2021-01-13-


# 5. discovery! progression of timescales in human cortex (early 2019)

2019, new year new me—well I threw up in an LCBO bag on the TTC at 3am after a NYE rager (wow remember real-life parties?), so maybe not, but hey at least it wasn't the actual vomit comet. Damn, I gotta do stuff to graduate though? After we were both convinced that I didn't fuck something up in the analyses, Brad, of course, was like "well you gotta check it in humans...have people shown this for the whole humans cortex???" I don't know, because **I haven't read any papers yet,** but I don't think so. Worth a shot I guess? 

I go on Google, type in "big human ECoG dataset" (or something of that nature, I shit you not), and stumble onto this [MNI open iEEG database][mni_ieeg]—with task-free recordings from 1700 electrodes in 100+ epilepsy patients. I have never seen this before in my entire life of parasiting other people's ECoG data, must be a scam. I download the data, holy shit it's manually cleaned and organized by brain region, all the data nicely living in a big matrix of time-by-channel, with metadata for electrode location in MNI coordinates, PLUS patient age and sex. Seriously, *how lucky can you get*? Running this through a modified version of the macaque ECoG pipeline probably took a week or two tops. Plot timescale estimates by brain region: boom, **neuronal timescale follows sensory processing hierarchy in humans as well—fast timescales in primary sensory and motor regions, slow timescales in multi-modal and association regions (frontal, hippocampus, etc.).**

This was essentially the main innovation of the paper, and it really was this easy and fast. On top of that, because the dataset came with patient age information, it was natural to check if there was an across-subject relationship between timescale and age. To be completely honest, this could've gone either way at the time and it would've made sense: I don't know if I would've hypothesized timescale to increase or decrease with age, though I think that was mostly due to my own ignorance of the aging literature. In any case, a quick check showed that, indeed, timescale tends to decrease with age, and in almost all areas of the brain. Later analyses and converging evidence from various branches of literature would strongly suggest that this is what we should expect. I think I was also starting to read a bit more into the timescale literature by this time, because my prayers were heard by the LFP gods and our Cosyne abstract was accepted as a poster presentation ****against all spiking odds! 

**Another technical side note**: to give a little more context, most of the investigation on neuronal timescale, like that John Murray 2014 paper, happens in model organisms (rodents, monkeys) where people can record single neuron action potentials, and there's a particular way timescale is computed from spikes. The last 5 years' worth of research in that area has shown time and time again that there is a hierarchy of timescales in both rodents and monkeys, so it should be the case in humans as well (your *reject-because-no-novelty* radar should be going off). But for whatever reason—presumably spike chauvinism—mainstream people weren't really doing this in time series data like LFP and ECoG, and you can't really get that many neurons from the human cortex, so it remained to be confirmed. The one exception I know is that of Chris Honey's [earlier human ECoG work in 2009][honey_2009], which already implicated a temporal processing hierarchy in the human auditory pathway by looking at broadband (or high gamma) timescales. So really, we didn't invent anything new here, except to stumble upon a different (though slightly more accurate) way of estimating timescales from the frequency domain, and to apply it to a much larger human ECoG dataset 10 years later. Also, re: the difference between spiking and current timescales, our method presumably measures a fundamentally different process, so maybe there is something new?

[mni_ieeg]:

[honey_2009]:

# 6. it's better to be lucky (Cosyne, March 2019)

holy shit I'm in Lisbon, Portugal. I'm really, really thankful for the collaboration that came out of this conference, because otherwise I'd feel very guilty about the fact that Brad keeps funding my exotic international work-vacations. 

So I'm there by myself in Lisbon, and I don't really have other professional relationships because LFP and oscillations are the "exhaust fumes of cortical computation" (hahah I will never let this go). I spent the first two nights working on a (rejected) grant and then the poster itself, as per usual. During my layover at London Heathrow, somebody said Lisbon is like a depressed version of Barcelona, because its all fun until suddenly everything shuts down at 12am. Not like I was going to go out by myself, but I did forget to bring a power adapter and ended up walking around the whole city the night I landed, trying to find a 7/11-like place to purchase one (did not succeed). Some hotel front desk person tried to sell me a lost-and-found one for 50 euros. Okay bro. I was eventually fortunate enough to make some friends of friends and had some dinner companions. None of this is relevant to the story, I just thought it was hilarious how woefully prepared I was.

Anyway, the night of my poster presentation, I'm standing there with a box of *pasteis de natas* because nobody was going to come to a LFP poster, *especially* if it's not one of the *Gangulis, Sahanis, Harrises, or the likes,* so I might as well enjoy myself. Incredibly enough, John Murray (of *Murray et al. 2014*) showed up, and I kinda, I don't know, couldn't digest the natas for a bit, because I thought he'd think it all sucks or that it's derivative (*because I quite literally ripped the numbers from his paper*). But we actually had a great conversation, and he'd suggested comparing the human cortical timescale maps to these "T1T2" (wtf was a T1T2?) and "gene expression" gradients from [Burt et al., 2019][burt_2020], to see if there was a nice anatomical correlate to these dynamical timescales.

A bit later in the night, Thomas Pfeffer (my now co-author) came to check out the poster as well. I think we actually talked the night before at his poster, because I knew him from a brief Twitter exchange some years ago about this EI-balanced CROS model his friend was working on, so I recognized his name. He thought my poster was really nice, and suggested, uh, *comparing the human cortical timescale maps to these "T1T2" and "gene expression" gradients from Burt et al., 2019* (wtf was a T1T2 gradient???). Even more graciously, he says that his lab mate had made these maps for some other thing, and that he could just email them to me, free of charge. All I'd have to do is align my timescale maps in the same spatial coordinate frame and run some correlation.

This is what I mean by **it's better to be lucky**. More specifically, it's better to be lucky enough to meet friendly, knowledgeable, and helpful people. Tom and I ended up hanging out a bit more the rest of the conference, especially during the workshops in Cascais. We found another LFP enthusiast in Martin Vinck, who liked the Voytekian line of work, and shared fables of when oscillations were all the rage at Cosyne some 10 years ago. The last night of the workshops was capped off with him playing the piano in the conference hotel bar and then buying us these gigantic German-sized pints before the wrap-up party (who did not attend himself because it was his kid's birthday the next day). Funny enough, Martin later became the handling editor for the paper at *eLife*. That's just how it all worked out. I guess I'm writing this because this kind of stuff really gets me thinking about how amazingly weird life is. Sure, it was really nice that the collaboration ended up being productive and we had a friendly editor, but it's not what I'm gonna be thinking about when I'm dead, you know? All that stuff pales in comparison to the memories of "*...uh is that Zach Mainen DJing at this club party?*", and walking around the beach boardwalk in Cascais for lunch together talking about how hard academia is. Well, pretty luck that this was at least part of my job.

![cascais](cascais.png)

I emailed Tom to ask about the data a few weeks after I got home (now April/May 2019), and that lab mate of his turned out to be Rudy van den Brink (our final co-author), who had already done a bunch of work to turn these "T1T2" and "gene expression" maps from voxel space to cortical surface space, and it was literally was just in a big feature-by-region matrix ready to go...so, what **IS** a T1T2 and gene expression map? 

[burt_2020]

# 6b. (long) technical tangent 2: cortical gradients and hierarchies

Context: at this point in the story, all we had was timescale values from the task-free MNI dataset (and the macaque results). It was a semi-replication and extension of existing ideas to humans, which was awesome, but ultimately, what's the "new thing"? Tom's idea was that we could look at how brain *structure* relates to these timescale values. This would give us a clue about how brain anatomy shapes brain dynamics. 

What I had literally zero idea of, prior to having that conversation, was this recent explosion of works measuring anatomical hierarchy in the brain (in rodents, macaques, and humans), especially by ways of "macroscale cortical *gradients"*. There's a pretty influential idea in neuroscience that the brain is *hierarchically* organized (Google "Van Essen diagram" for nightmare). It's actually a pretty loosely used word (see [Hilgetag et al., 2020][hilgetag_2020]), but here, I'll just handwave and say that there's a progression of anatomical features along the cortex, which enables different stages of cortical computation. Put more concretely, the sensory/motor areas of our brains smoothly transition into the multimodal association areas, like from primary motor cortex to the prefrontal cortex, which follows the progression of *functional hierarchy*, where motor cortex is responsible for immediate motor outputs, and prefrontal cortex is necessary for planning sequences of actions over longer term. This forms the "sensory-to-association axis", and I hope it's starting to smell familiar.

![huntenburg](huntenburg.png)

Unbeknownst to me, a bunch of recent works, taking advantage of technical advances in various imaging methods as well as really big open data collection efforts like the Human Connectome Project (HCP) and Allen Brain Atlas, have measured various anatomical features across the entire human neocortex. Many of these features follow this S-to-A axis, and these are what we colloquially call cortical gradients or maps, because they (more or less) vary smoothly across the entire human cortex. T1T2 ("tee-one-tee-two") and gene expression, likewise, are two such measurements of brain anatomy/structure at two different spatial scales: 

T1T2 (technically "T1w/T2w ratio") is a non-invasive metric derived from MRI. It's a proxy for how much grey matter myelination there is in an area, which is a proxy for the ratio of feedforward vs. feedback inputs to an area, which is a proxy of where along the processing chain an area sits, i.e., "anatomical hierarchy". Don't worry, it took me many, many days to get this straight, and I still need to pause to think about it when I see my own figure. The important bit is, the more "association-y" an area purportedly is, the less grey matter myelination there is, and hence the lower T1T2 value it registers from MRI. This is something you can get relatively painlessly: just stick someone in an MRI scanner, and out comes these values. I don't know, I obviously don't collect my own data, and thank god for the HCP so I don't need to.

![T1T2_gradient](T1T2_gradient.png)

Cortical gene expression, on the other hand, is NOT something you can get painlessly. The Allen Brain Institute collected 6 post-mortem human donor brains ~10 years ago, and was able to measure the expression of some 20 thousand genes at many different sites. Roughly speaking, "expression of gene X" in a brain area = "how much protein X" there is in that brain area. **HUGE disclaimer**: MORE OR LESS, probably more less than more more—it's a big ongoing area of research, and there's more caveats than results, that's why we have jobs. But again, for brevity's sake, more gene expression = more protein. What are these proteins? They are the shit that makes up everything in your body. In this particular case, we are interested in little machineries that can define cell types, facilitate transport of ions in and out of neurons, or form neurotransmitter receptors at synapses. Amazingly enough, the expression of these 20 thousand genes follow, to a first approximation, the same sensory-to-association axis: some types of synaptic protein become more abundant going along that gradient, and some become less so, some follow more closely, others not so much, etc.

![gene_gradient](gene_gradient.png)

With these maps—which albeit are average measurements taken from different people at different times, so no causal claims here—we can get a pretty crude but comprehensive look at what anatomical features are related to timescale, i.e., how *structure may shape dynamics*. The prediction is that timescale should inversely correlate with T1T2 (because timescale increases going up the hierarchy while T1T2 decreases), and that depending on which of the 20k genes we are looking at, there would be different expected correlations with timescale. For example, if a gene encodes for a synaptic receptor that prolongs synaptic currents, it should positively correlate with the timescale gradient, and vice versa. 

Of course, both of those predictions were confirmed, otherwise I wouldn't be writing this.

![structural_corr](structural_corr.png)

All this stuff is the kind of random shit that I'd never expect to learn, but end up having to by pure coincidence, and that's kinda how it goes in the PhD—rabbit hole after rabbit hole. I enjoyed it, and it obviously made the science much more interesting, because now we're making a link between brain structure and brain dynamics. The actual "result" in those figures took, I don't know, 10 minutes to get? because you just throw these arrays in a loop and correlate. The work leading up to that point, and certifying those results afterwards are the things that took much longer (if Glasser parcellation, multiple comparison, and spatial autocorrelation means anything to you). Also, I gotta say, it's funny now to write about how I didn't know any of the literature beforehand, but it damn sure would have made my life easier if I had read those gradient papers earlier.

[hilgetag_2020]

# 7. tenured professor runs own analysis...(Fall 2019)

...and graduate student proceeds to *almost* break it. 

Now we're around SfN 2019 (October) and I gave a poster presentation on all the new results so far, including the anatomy and gene expression correlates. It went really well, and it was the last SfN as graduate students for the rest of the original cohort in the lab (but the first time shotgunning a beer for some). Right around then, we were starting to think about writing this work up and publishing it, reasonably confident that it would be quick (it was not) and that I'd be graduating soon (I did not). 

![two_weeks](two_weeks.png)

For a paper like this to be meaningful, at the end of the day, you have to show some kind of behavioral relevance, otherwise "it's just a methods paper". This is especially true if most of the results, while cool, was recapitulating existing knowledge from non-human work. So we got to brainstorming. I say "we", but in this particular case, it was actually just Brad, and I had pretty much nothing to do with this except to refine the code and make the figures, while almost breaking the analyses (...a few times). I have two very vivid memories that summarize how this happened, and both had the flavor of "I thought tenured professors didn't run their own analyses anymore."

**Moment 1:** I'm sitting in lab minding my own business, as one does pre-pandemic. Brad comes in and goes "YO check this out". Apparently, he couldn't bear waiting for me to start digging around behavioral data, so he went and did it himself. Obviously we weren't going to run our own experiment at this point of the project (and given the historical precedent, or the lackthereof), so he found a human ECoG dataset collected during a working memory task that a friend from Bob Knight's lab had deposited on CRCNS (the other patron saint of my PhD). 

The structure of the task was classical as far as working memory experiments go: there's a pre-stimulus period, then stimuli, then a delay period, then a cue for context-dependent recall. In this case, there's a pretty straightforward hypothesis: if working memory is the active maintenance of information, then it would be reasonable to expect the neural activity in those involved regions to have "more history", or longer timescale. It's a rather naive first guess, but it actually turned out to be true. He scrolled through dataframes in a neatly formatted Jupyter notebook and called up the pre vs. post t-test statistics, and yup, there it was: during the delay period (holding onto information), timescale in all the recorded regions saw an increase relative to baseline. 

![pre_post](pre_post.png)

I sat there swelling with pride—my associate professor of a PI is ready to become a PhD student again :')

![PIs_code](PIs_code.png)

**Moment 2:** before the pandemic, Eric and I got into a nice habit of going to this bar in San Diego for house music on Wednesday nights (RIP Blonde). On one such Wednesday, I'm at the said bar shuffling my feet, and I get a message from Brad:

![mind_blown](mind_blown.png)

Note the timestamp (it was actually 11PM PST, so not quite as bad as it looks...for both of us). This was apparently two days after moment 1 above (and 2 days before flying out to Chicago), where I said I was going to check over his code, and I obviously hadn't looked at it in the ensuing 48 hours. I don't want to make it seem like Brad's on my ass after work hours, because he never is. I'm usually the one sending random messages in the dead of night because that's when I work sometimes. But here we are on a Freaky Friday Wednesday, and I remember this SO vividly because I'm now standing in the middle of this tiny crowded dance floor staring at my phone. Alright, my interest is piqued, shoot: 

so what he had done was, beyond looking at within-individual timescale changes from pre- to post-delay period, he looked for *across-individual* trends. Specifically, was there a relationship between a person's modulation of timescale and their average performance on this working memory task? This would be kind of crazy cool even without making any causal claims, because it's a direct correlate of behavioral outcome. And yeah, consider my mind blown, because it turned out, across the 15 or so people in the dataset, the worse their average performance was, the less their timescale increased from pre- to post-delay, and this was only true for PFC. 

![pfc_wm](pfc_wm.png)

Going all the way back to the radioactive decay analogy: the more volatile (shorter timescale) the element was, the faster all of it disappears, and the less useful it would be for reconstructing events farther back in history. Except, in the case of brain activity, we are apparently able to modulate the timescale of neuronal activity based on behavioral demands, and the longer the modulation, the better performance one got, at least in this very simple task. There are lots of caveats and open questions here, especially in the causal direction of the modulation (is it brain modulating behavior, or behavior modulating brain, and what did neuromodulators do?)

These were precious moments, from which came the core of our final analysis. Of course, the "checking it twice" part of making a list again took way longer than making the list itself. In this particular case, I inherited the notebooks, refactored, broke the analysis, fixed it, broke it some more, fixed it some more, ran it through the gauntlet of tests until we were both reasonably confident that the result was not a fluke. These next two snippets of messages perfectly capture the sentiment of this particular analysis, and as a whole, the project (and really, *science*).

![holyshit](holyshit)

![fixedit](fixedit)


---

<iframe width="560" height="315" src="https://www.youtube.com/embed/9FjhTtNDbjw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



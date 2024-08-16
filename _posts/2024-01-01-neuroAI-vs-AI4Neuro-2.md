---
title: "Beyond #NeuroAI, we need #AI4Neuro---and we're going to suck at it (at first). [Part 2]"
tags: [Reflections, General Science, Science Communication, Data & Technology]
status: publish
type: post
published: False #True
header:
  overlay_image: /assets/images/blog/default_header.jpg
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/default_header.jpg
classes:
  - wide
permalink: /blog/:year/:month/:day/

excerpt: ""
---


I didn’t forget about this. My laptop bricked back in February and somehow the one meaningful thing I lost was this uncommitted draft. The thought of re-writing this was dreadful, so I didn't, and then...life happened, and all of a sudden it’s August. At least I knew not to promise posting once a week this year.

So, a brief recap: in the [previous post][neuroai1], I used “computational neuroscience” as an analogy to illustrate the difference about developing and using computations **for** neuroscience vs. understanding computations **in** neural systems, and that while the two are equally valuable perspectives, methodologies, and branches of neuroscience, the latter is what is predominantly accepted as "computational neuroscience" (for example, at COSYNE and CCN).

It took me some time to understand this, and it makes a lot of sense in hindsight. But it was certainly very frustrating for a while, when it felt like somebody (me) working on developing computational methods for analyzing neural signals---but not prescribing to a specific computational view of the brain---might as well be speaking German in discussions of “so what do you do?” The correct response, in some sense, should have been “computational biology”.

TL;DR: that’s basically today's take-home message about NeuroAI: in principle, NeuroAI could simply be the (entire) intersection of AI and neuroscience, but it's not. I’m not saying there's a right or wrong definition, I’m just saying a naive entrant into this field would be perfectly justified in thinking that.



For this post, I try to find out what NeuroAI is, empirically, by reading what Google had to say about NeuroAI. I had a budding suspicion for a while now that my idea of NeuroAI was, well, naively broad. Spoiler alert, at least empirically speaking, that’s true.

Concisely stated, my reading is that the key part of NeuroAI---Neural and Artificial Intelligence---is squarely centered on *Intelligence*. Put differently, *Artificial Intelligence* here is not a compound word as it’s often used now to describe your favorite text-to-image model, but that *Artificial* should be more lumped with *Neural*, as in, (Neural+Artificial) Intelligence. It would be equally valid to have called it Artificial and Neural Intelligence, or even more broadly, Artificial and Biological Intelligence, which I would have personally preferred for this new field, but I think this gets too close to being *Cybernetics,* which reminds us of communism in the 60s.

Once I started digging, it actually made me feel kind of stupid for not realizing it sooner, because it's usually plainly stated within the first one or two sentences, and in a totally non-controversial way. But hopefully by the end of this you will get a better idea as to what alternatives---aside from computation and intelligence---there could be for the role of AI in neuroscience.

https://www.aisnakeoil.com/p/scientists-should-use-ai-as-a-tool



### What is NeuroAI
*So what is NeuroAI?* For the observant reader and seasoned researcher, you probably know where I'm going with this. Similarly, I know who I am now and what I like for breakfast, so in some sense, it's irrelevant for me what NeuroAI is or is not---I know who I need to talk to and where, within and outside the community of NeuroAI researchers. But in case there is a fresh and excited grad student out there who is developing new computational methods based on state of the art AI, whether for the goals of studying neurobiology or simply as an AI researcher, you might find this useful for navigating NeuroAI.

I have to start with the caveat that I'm, obviously, not the person that came up with this name, nor do I have anything to do with it, I just read papers and talk to the people who **do** do NeuroAI research. I'm only a weird person at the intersection of AI and neuroscience, so by no means is this a prescriptive definition of NeuroAI, just my understanding.

And where else to turn to than this [perspective paper][perspective (Zador et al., 2023)] titled: *Catalyzing next-generation Artificial Intelligence through NeuroAI*? It's a nice read, I especially enjoy when such papers come with a historical perspective. A big part of the paper makes the argument that "next-generation" AI will need sensorimotor embodiment, something that is a god-given for animals in the world that *engage their environments, behave flexibly, and compute efficiently*, but tremendously difficult for human-engineered AI systems. No surprises here, since it comes from a group of people who are, I would say, first and foremost neuroscientists. I agree with the take, but I won't discuss the paper beyond this sentence:

> "The emerging field of NeuroAI, at the intersection of neuroscience and AI, is based on the premise that a better understanding of neural computation will reveal fundamental ingredients of intelligence and catalyze the next revolution in AI."


### Our survey results indicate that...




### What NeuroAI is not


---

### A brief critique of computation
People say that if you do your PhD in something, you realize that nothing is real and that we actually don't know anything about that something. I think this is true. The first (and last) thing you learn in Cognitive Science (at least at UCSD) is that we don't know (or agree on) what cognition is, much less "intelligence". This fundamentally shaped (or biased) how I think about "computation" in the context of neuroscience and cognition. I don't want to spend too much time on this, because my current gripe is not really with NeuroAI's focus on intelligence-as-computation, but rather the lack of other interesting development and application of AI in neuroscience, as we will see later. Also, people much more qualified than me have had detailed and pointed commentaries on this topic. For example, [van Rooij et al.][vanrooij_etal] had this banger of a sentence in the abstract: 

> When we think these systems capture something deep about ourselves and our thinking, we induce distorted and impoverished images of ourselves and our cognition. In other words, AI in current practice is deteriorating our theoretical understanding of cognition rather than advancing and enhancing it.

I think this might be worded a bit too strongly, but I don't fundamentally disagree, though I would replace `deteriorating` with `limiting`, and `...AI in current practice...` with `...our obsession with computing devices since the conception of the field...`. Lest we forget the days when we thought the brain computes via symbolic programs and spatiotemporal filters. I'm pretty sure I've seen this invoked somewhere, possibly Twitter, but if it hasn't been accredited to anyone yet, then I claim this theorem: 

> "Any state-of-the-art computing device / algorithm is, for some time, how the brain works."

Is this unproductive? Not necessarily, but if you subscribe to this paradigm, then you probably shouldn't spend too much time on neuroscience, because you'll always be lagging behind everyone else, searching for these equivalences rather than inventing new ones. Instead, do machine learning (or math).

Anyway, aside from the general critiques of the dominant notion of cognition, e.g., based on perspectives like embodiment and [behavior through evolution][cisek2019] (another absolute banger), my one specific issue here is actually rather technical, and it hinges on the **notion of representation**:

Computation, defined as transformations between input and output signals, is not an unreasonable conceptual model for what the brain needs to do, functionally speaking. However, since (as far as we know) these transmissions and transformations have to operate on physical signals (so, telepathy excluded), the crucial part of computation is that there is recoverable information encoded. Specifically, the operations on the physical stand-in, be it analog (continuous voltage) or digital (0 or 5V) signal, translate to the intended transformations on the representation or "information" we actually care about.

Obviously, in systems we design, whether it's digital or analog filters, the software in your Roomba, or AI systems, we **know** the underlying representations because we specified them (but more on that last one in a second). What I mean is that every symbol, letter, and byte maps to something, simply because we enforced this mapping. To be a bit more academic, they are externally [grounded][grounding] to something, and by our design. However, in systems we didn't design, like the brain, we have no prior on what is, or even what should be, represented, nor what that representation looks like. So we have to infer or reconstruct it, which is apparently really fucking difficult (though it appears to be difficult to reconstruct [even in systems][jonas2017] we **did** design). I mean that's basically what a significant of neuroscience is up to.

As far as I know, the one and only paradigm we have for the last 60 years is to search for neural correlates of induced or measurable stimulus and behavioral, and assume that coinciding neural activity is the representation thereof. Sometimes it's referred to as the "neural code", and we can argue about whether the code is implemented via firing rate or spike timing, or maybe it's done by the astrocytes. We can also refine the criterion with which we judge the validity of the representation, like response reliability, signal-to-noise ratio over ambient activity, or predictability with sophisticated decoding algorithms. But we basically assume this representation exists, that we can find it, and furthermore, that it's stationary, up to context-dependent modulations (note, though, recent [discussions][repdrift] on [representational drift][driscoll2022]).

Dynamics, Watson Governor [prinz2000]

Of course, this is becoming slightly more complicated now with AI systems growing more complex. We know the representation at the input layer because we encoded them to be pixels or word-embedding vectors or whatever, but we quickly lose track of that representation the deeper it traverses through the system, both relative to the original representation space and relative to something that we can perceive and intuitively make sense of.


If that's already taken, I actually have addendum to this, which states:

> "Any state-of-the-art algorithm for analyzing brain signals is, for some time, how the brain works."


So if not computation, then what?


[repdrift]:https://www.thetransmitter.org/learning/what-drifting-representations-reveal-about-the-brain/
[driscoll2022]:https://www.sciencedirect.com/science/article/pii/S0959438822001039
[jonas2017]:https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005268
[grounding]:https://en.wikipedia.org/wiki/Symbol_grounding_problem
[prinz2000]:https://barsaloulab.org/Online_Articles/2000-Prinz_Barsalou-chap-embodied_representation.pdf
[cisek2019]:https://link.springer.com/article/10.3758/s13414-019-01760-1
[neuroai1]:../_posts/2024-01-01-neuroAI-vs-AI4Neuro-1.md
[vanrooij_etal]:https://osf.io/preprints/psyarxiv/4cbuv

---

### AI for Neuroscience


[wiki_aiwinter]:https://en.wikipedia.org/wiki/AI_winter
[tweet_mineault]:https://twitter.com/patrickmineault/status/1730989784678490589
[tweet_rg]:https://twitter.com/_rdgao/status/1731376771763757298
[wiki_compneuro]:https://en.wikipedia.org/wiki/Computational_neuroscience
[trends]:https://trends.google.com/trends/explore?q=NeuroAI,AI4neuro&hl=en-GB
[mattis_ai4neuro]:https://github.com/amathislab


Fitting enough, NeurIPS---`Neural Information Processing Systems`---was arguably the modern ancestor conference for NeuroAI ("modern" because it came after "cybernetics", which was too...Soviet Union to catch on?). NeurIPS was a place for works looking at how information processing or computation happens in neural and neural-like systems, before weirdly finding itself being **the** place for completely brain-free machine learning papers for some time. Now, in 2024, as the economy goes to shit and big tech companies no longer giving 6-figure salaries to anybody that's ever written a line of `loss.backward()`, maybe we will see NeurIPS coming back to being the playground of computer neuroscientists? If the trend from this year holds up, we'll have gone full circle and come back to analyzing powerful-for-its-time artificial computing systems as we imagine how brains do things, or even as artificial brains, and this, my friends, is a tale as old as time itself. 

But if history serves us correctly, this will not be how we solve neuroscience. Or at least, this alone will not be the way. Strangely enough, I'm convinced of this after being at NeurIPS---and after visiting the Deutsches Museum and playing with some really fun fundamental physics demos--- We need an AI4Neuroscience. 

Computational neuroscience
the method becomes the model
measurements


 (no, the "neurons" in a deep neural network are not neural and we're not having this discussion here)


---
[perspective]:https://www.nature.com/articles/s41467-023-37180-x
[neurips_mineault]:https://airtable.com/appWMCgd7CqsVIRza/shrTRBBqmrT74fZLb/tbl1t9cr5qpkYsrpb



What are the defining characteristics of representations?
How stable are representations?
Are representations embodied? Are representations (a)modal? What does it mean for a representation to be modal or amodal?
What do representations look like at the neurobiological level?
Are representations distributed and extended? What does it mean for a representation to be or to not be distributed?
Do representations necessarily exist through relations (distinctions, oppositions) to other representations?
Is conscious experience exhausted by representations?
What explanatory power exactly does Cognitive Science acquire by positing representations? Are there important questions that Cognitive Science can solve without the use of representations? Are there any domains where positing representations needlessly complicate or overburden analyses of phenomena?
Could Cognitive Science exist without representations? If no - why? If yes - what would it look like?
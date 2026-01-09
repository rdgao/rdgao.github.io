---
title: "Beyond #NeuroAI, we need #AI4Neuro---and we're going to suck at it (at first). [Part 3]"
tags: [Reflections, General Science, Science Communication, Data & Technology]
status: publish
type: post
published: False
header:
  overlay_image: /assets/images/blog/default_header.jpg
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/default_header.jpg
classes:
  - wide
permalink: /blog/:year/:month/:day/

excerpt: ""
---

> "...I'm hoping for there to be a similar community for creating, curating, and contributing to a body of research that uses ML and AI to advance our understanding of neuroscience, neurobiology, and neurological disorders." 
Me, January, 2024

Okay I'm gonna be real here, back when I first started writing this ["series"][neuroai1] in 2024, it was mostly to rant about yet another rebranding of "computational neuroscience" that's focused on a theory of [intelligence centered on computation][neuroai2], and again one with little room for methodological research in service of all the other (arguably bigger) branches of neuroscience. I also didn't think *#AI4Neuro* would actually become a thing, nor that I would at some point *have to* seriously write about what I thought it was or should be. That was future-Richard's problem. 

Well past-Richard is a dick (get it?), especially since now-Richard is supposedly building a group *today* that plans to do "AI4Neuro" research. So I figured it might finally be high time to think hard about this, if for nobody else but myself, to have some intelligible framework to guide our work.

As prescient as I was, it turns out I had even less time for composing internet rants. Time flies and it's been a very interesting **2 years (!!)** witnessing the explosion of AI4Science as a whole, and now, AI4Neuroscience. So much so that this particular topic required multiple workshops across the world this year (and several at NeurIPS alone!), and even more already planned for 2026.

So, for once, I can be less grumpy, and write a weirdly positive and constructive blog post. Again, big disclaimer: these are my personal opinions (unless I've inadvertently regurgitated something insightful that's already been said), and do not represent 1) those of my current or past employers, 2) any member of the community, nor 3) a comprehensive scientific review. 

On that last point, like most AI research, there are way too many things happening way too quickly, and if I don't cite something, it's because I'm ignorant and it didn't pop up in the last 2 months—you can either drag me on social media or submit a PR on GitHub.

---
### Foundations: the long and short of it.
aka, too long; didn't read:

If #NeuroAI is using AI as a model of biological computation and intelligence towards building better AI inspired by the brain, then #AI4Neuro is to leverage AI to help neuroscience research, even (and especially) those unconcerned with "intelligence" per se. 

Put succinctly, this finale of the AI/Neuro manifesto has three main premises:

1. **AI4Neuro is methodological research:** meaning, not only *using* AI, but developing, understanding, documenting, and educating about the use of AI methods for various aspects of neuroscience research.

2. **AI is unlikely going to discover something *fundamentally new* about the brain:** with the exception that exponential continuous progress at some point starts to look like (or enable) a discontinuous, qualitative change in paradigm.

3. **AI _can and will_ accelerate neuroscience research:** the more productive question, at least on the timescale of the next 5-10 years, is how to use AI in interesting and clever ways to help us do neuroscience better, faster, and cheaper. We can do this without burning a hole in the ozone layer or through our pockets.

* **A corollory,** and perhaps the most important part: don't let AI do your homework without having the ability to check over it yourself. This is true no matter how you use AI, and we'll look at what "checking our answers" means in this context.

Okay, let's dive in.

---
### What is ~~AI4Neuro~~ AI, for Neuroscientists?

Depending who's reading this and what kind of media you consume, "AI" can be anything ranging from ChatGPT, our formless Savior of Humanity, the Terminator, or linear regression. When I first got around to thinking more about this, I realized I don't even know what "AI4Neuro" actually means, and a large part of that is because it's hard to nail down what "AI" means today.

There are certainly instances of things that clearly fall into the bucket of AI4Neuro, like GPT-style foundation models of brain data and using LLMs for research. I can't say why I think that, but they smelled right. But it's hard to come up with principles to guide our thinking about the subject by looking at individual examples alone.

At the same time, it's maybe too ambitious to come up with a general definition of AI, and I'm certainly not qualified to do that. But in the realm of things that neuroscience and neuroscientists are concerned with, I think there is a definition that can be useful to guide our adoption of AI in advancing brain research.

---

When I ask myself this question, the first answer I came up with is this: 

`When I say "AI", >95% of the time I actually mean machine learning (ML), but I decide to use AI instead for better marketing / recruiting / asking for money`. 

For whatever reason, AI is the term that took off in the public consciousness, not ML, and so when talking to a potential funder, generalist reviewer, or student, they might not appreciate what "ML" means, but they certainly are looking for "AI", because that was in the funding call. I feel a little dirty every time I do it. I'm including this because it's only a half-joke, since there is a very real hype / bubble around AI that we can honestly acknowledge (and take advantage of, if you're morally flexible).

Okay—honest, but not very useful. More importantly, there are actually some key differences between ML and AI. In particular, the latter suffers from a few critical issues we should be aware that the former (defined by, for example, the contents of the [Bishop book][bishop_prml]) does not, or at least not universally. It's precisely these issues that should inform how we think about, use, and improve the adoption of AI in neuroscience (and scientific research in general).

***So, what is AI, for a neuroscientist?***

For me, a useful working definition in 2026 really boils down to **data-constrained artificial neural networks assisted by dedicated accelerator hardware and software**. 

So deep learning, basically, but the important properties are that "AI" **(1)** approximates functions using flexible and expressive modules (i.e., various neural network layers) **(2)** learned from training data and **(3)** through optimizing an objective or loss function. 


*This, by the way, is [Wikipedia's definition](https://en.wikipedia.org/wiki/Artificial_intelligence), which references the classical AI-as-human-intelligence ideas (GOFAI-y) in the first paragraph, then lists full-fledged modern "AI" applications in the second.*

![](/assets/images/blog/2025-12-29/wikipedia_AI.png)

*I don't adopt either definition here because for a (neuro)scientist developing and using AI in their research, direct application of LLMs still only represents a small fraction (though we will have a dedicated discussion on them later), and it's more useful to think about the components powering those applications. In 2026, that is **mostly** deep learning.*


> *"wow thanks dude, you wrote 3 blog posts just to bring us back to 2012 and tell us about deep learning?"*

Yes, but a better question to ask is, **why is this the right cut-off for "AI"?**

---
### We don't know what we're doing anymore.

To explain why, it's illustrative to think about "pre-AI" days of computational neuroscience, by which I again mean the [broader one][neuroai1]—not only *neural computation*, but developing and using computational tools in general:

Whether you're doing data analysis or modeling, neuroscience research on a computer almost surely means you are interested in building some kind of **transformation or function**, which we can abstract away as a box that processes input data and produces output data. 

The input / output could be neural data, behavioral data, experimental stimuli, whatever. Basically, in goes some stuff, out comes some stuff, and the actual research work often is to design the box and/or make it better at doing what we want it to do, defined by a task around the input and output data. This could mean better prediction accuracy on unseen data, or providing a better match to how the brain does something.

By and large, for such a box in the pre-AI days, **(1)** we knew exactly what the function is supposed to be and what it's supposed to do, **(2)** they "work the same way" no matter what data they see, and **(3)** we know exactly how to (re)make the box. Phrased more technically, you might call them analytical—or at least interpretable—forward mapping, data-dependence, and inference procedure. **Having this understanding** about our algorithms guides our thinking and implicitly provides safeguards when using them for scientific research.

As a trivial example, the `Fourier Transform` and `digital filters` work the same way and is derived the same way no matter what data you apply them on. The recipe for getting the coefficient from data is fixed, and so is what the transformations do. There is actually no "inference" procedure or data-dependence and the forward mapping is analytically defined. The method development component of research then involves designing better algorithms and settings by, e.g., stacking multiple such transformations, but in a way where we always knew what's going on.

Take `PCA` and `linear regression` as slightly less trivial examples: yes, the resulting weights and components are data-dependent, but given a dataset, we know exactly how to get there, and we are fairly comfortable with our description of "what they do", i.e., linear projections optimizing for a specific objective. In fact, optimizing for a different objective (e.g., L1) gets you an entirely different name and model inference procedure.

The line starts to blur slightly when hyperparameters are involved, like in `regularized regression`, because the eventual hyperparameters (and therefore model) is optimally chosen based on cross-validation on data. But even in those cases, how the box functions and how it's constructed doesn't fundamentally depend on those hyperparameters or data. The transformations are the same, only the specific "amount" changes.

This, by the way, is part of the reason why I made a distinction between machine learning and deep learning / "AI". But the more important one is that in many statistical ML models, much of the work was somebody painstakingly designing a interpretable *(forward) model / function* and / or the corresponding *inference / modeling-fitting* algorithm (one of my favorite examples [here][ladenbauer2019]), for a given objective function (e.g., maximum likelihood). Yes, the process of finding the model given the dataset is empirical and often stochastic, but the model itself and the formula to get there tend not to be black boxes.

<!-- Related, whenever I write about the pain and complexity of deriving likelihoods and inference procedures, I automatically think of [this paper][ladenbauer2019] and the related works it builds on. It's mindboggling. Particularly topical is this innocuous sentence buried in the math:

> "Notably, for the leaky I&F model this likelihood is mathematically guaranteed to be free from local maxima [61] so that any optimization algorithm will converge to its global maximum, which ensures reliable and tractable fitting." -->

**To summarize**, the ingredients we have are *the data*, *the intended function* (what it's supposed to do), *the objective function* (when is it doing a good job), and *the inference procedure* (how to find a good function). The product or "artifact" we care about is typically only the eventual function / transformation itself, like the filter coefficients, regression weights, or model parameters.

For scientific research, it's usually good if we understood well these ingredients, where the function is "the box" and what we spend the most time thinking about, so that we can in turn use them to analyze and interpret the brain data we didn't understand. As exemplified above, pre-AI artifacts in computational neuroscience rarely violated this assumption of understanding for all 3 components simultaneously. An individual person using a function might not understand everything, but *somebody* did.

[ladenbauer2019]:https://www.nature.com/articles/s41467-019-12572-0

---
### *"I laugh in the face of danger."*

Hopefully now it's clear why I settled on deep learning as the boundary between pre-AI and AI. Again, "AI" here is (or uses) deep learning to approximate an unknown and often ill-defined function, by optimizing for a *general and interchangeable* objective function that has very little to do with the specific problem, on a particular dataset of finite size, using stochastic optimization algorithms.

In other words, it flaunts its disregard for these requirements, and laughs in the face of danger. In fact, you could almost define "AI" as `an artifact for which we don't know exactly what it does, nor how exactly we arrived at it.` 

What AI offers is powered precisely by its violation of the "need to know", enabled by the flexibility and a lack of specifications unless absolutely necessary. In fact, a tenet of modern AI / ML is to have as few "inductive biases" as possible and just let data shape the very flexible function approximator (aka Transformer lol). This flexibility, coupled with clever ways of representing (i.e., tokenizing) your data as input to the network—and of course, a shitload of data and compute—resulted in not only powerful language models, but really interesting multi-purpose and context-sensitive models that can deal with messy, heterogeneous brain data.

But the **difference is that**, after crafting such a flexibly tailored transformation, you produce an artifact that is in principle a function like before, but now one that has been irrevocably embedded into it the decisions surrounding idiosyncratic data, loss function, and hyperparameters. 

This presents a fundamentally different picture, where now "the box" contains not only the function we wanted to design, but everything else in the workflow. The worst part is, not only do we not know well the other stuff that's in the box, we don't even really know what the function itself—the original and now *inner* box—"does".

To be clear, this is not some groundbreaking insight I personally have about AI or deep learning. There have always been communities that worked on theoretical understanding and interpretability of deep learning (e.g., [Andrew Saxe][saxe2013], [Andrew Gordon Wilson][wilson2025], some non-Andrews too...), as well as more "defensively framed" topics like robustness, safety, and fairness. 

It goes without saying that a solid theoretical understanding goes hand in hand with improving the methods in a principled way. It's just that these topics became sort of niche silos in the context of "mainstream" AI research where one *could* get away without considering anything other than raw predictive performance. This is often a (valid) criticism of the thousands of papers trying to make a 0.XXX% gain on a benchmark table, but doesn't necessarily need to be: Since deep learning in the end involves an engineered system towards fundamentally *application-driven* goals, it's okay if the box *just works* without bothering too much about **"understanding"** (granted that it doesn't do something accidentally racist or drive a car off a cliff).

[wilson2025]: https://arxiv.org/abs/2503.02113
[saxe2013]: https://arxiv.org/abs/1312.6120

---
### Science needs tools it can trust.

But this is not the case for scientific research, especially neuroscience, because...well, understanding is unfortunately *kinda the whole point*.

And I'm resurfacing these old insights and concerns because while AI researchers have been grappling with and making these issues known against the tide of "standard" AI research (remember when a [Stochastic Parrot][bender2021] tried to slow a GPU-powered tank column?), they are not necessarily in the minds of neuroscientists trying to use AI for their research. 

Actually, scratch that. Don't just keep these "peripheral" issues—interpretability, robustness, safety, *understanding*—"in mind". These research directions are *central* to the usage of AI in scientific research, and neuroscience in particular. It's actually the whole thing.

Speaking of "peripheral" issues, there are a lot. A [recent paper][channing2025] nicely outlined many of the sociological challenges for AI4Science that we should aspire to overcome, especially with respect to fairness in the context of access and recognition. Those are important concerns with widespread impact, but there are also a lot of boring, technical issues that can make AI4Science go sideways. 

And hence premise #1: **overcoming these technical issues through methodological research, with the goal of understanding, is what AI4Neuro is!** 

It has been said of NeuroAI before that using neural networks as a model of how the brain works is unproductive because we're modeling a thing we don't understand with another thing we don't understand. I think the same goes for AI4Neuro as well: *we can't use a tool we don't understand to understand a thing we don't understand*.

---

### Towards a happier marriage.

To grossly caricaturize two whole fields: AI research has the mindset of "let's build something that works, and we can figure out why (or why not) later...in the supplementals, if there's time", while computational neuroscience has had the luxury of "we can trust these techniques, because we built and understand (and derived) them." 

But things are a bit different when AI is involved, and if you now simply put these two attitudes together as the "intersection of AI and neuroscience", it's a slow disaster waiting to happen...or silently burn a hole through the ozone layer for no real reason. We cannot by default adopt the mindset of "let's iterate through the config files until we find something that works", or at least not as the primary goal and certainly not the only goal.

Instead, methodological research now not only includes building new tools and techniques, but also in characterizing and understanding them. No tool is or method is perfect, and it's just as important to know when and why something doesn't work as when and why something does. In this light, treating "AI" as just another scientific tool or technique, like a microscope or a statistical test, seems more appropriate. As a researcher, you would never just start acquiring random images with a microscope without at least knowing how it works, nor do you need to be the person that built it end-to-end. But you *do* need to know enough about it to not misuse or abuse it.

So what are the things we need to be aware of about AI in the context of neuroscience? There are a obviously a lot of situation-specific details, mostly involving the type of data you work with (images, text, time series), where and how you aquired the data, experimental configuration management and reproducibility, etc. But on a higher level, a useful mantra I've adopted is this: 

**only use AI when you can trust or independently verify its answer. If you can't, figure out how.**

It's pretty simple, actually, and again, is like any other tool. I didn't invent this. This is the operating principle for how a lot of people use ChatGPT. It just so happens that it applies to the individual components, i.e., deep learning, as well, on a different resolution, and the "figure out how" part is where the novel methodological research happens.

---

### Hah! We never knew what we were doing in the first place.

Why do I keep making a point to single out neuroscience? Because, well, we currently suck at it.

This was pretty much the main point I had wanted to convey 2 years ago, as you can tell by the title, and it hasn't changed much: There has been a massive adoption of AI in many scientific fields, you can tell by the names that pop up as NeurIPS workshops: AI4Physics, AI4Biology, AI4Materials, AI4Earth, etc. Those fields have seen a lot of successes with their usage of AI (though many valid criticisms and debunked "discoveries" too). Can we just import their playbook and do the same in neuroscience? 

I would argue no, and it's because the application of AI in those fields can be better thought of as AI-assisted engineering, rather than "science". That's not to say that engineering is not science or is not a part of science. That's precisely the point: fields with well-defined engineering problems (e.g., protein folding, material design, climate modeling) can leverage AI more effectively to solve those problems because they have a clearer idea of what the problem is, what a solution looks like, and how to verify that solution. In particular, many of those fields have well-defined and trusted theories and models that can be turned into gold standard, 



These are lofty aspirations, and sure it's good to keep in mind, but does it actually impact day to day research concrete? I have a very simple proposition: think about why it doesn't work. 

[channing2025]: https://arxiv.org/abs/2509.06580
[bender2021]: https://dl.acm.org/doi/10.1145/3442188.3445922



---

To be clear, I'm not saying this is groundbreaking insight, because indeed the same problems that plagued deep learning for neuroscience still do in 2026. But in the context of the all-knowing "AI", it's interesting to revisit these issues to see that while raw performance (e.g., predictive accuracy) has steadily improved with dataset and model size and technical sophistication, the conceptual problems are just as relevant, and present as opportunities for better rounded AI4Neuro research.

AI4Science as a research field, in some ways, should be synonymous with interpretability, robustness, and safety.




[neuroai1]:https://www.rdgao.com/blog/2024/01/01/
[neuroai2]:https://www.rdgao.com/blog/2024/08/14/
[bishop_prml]: https://www.amazon.ca/Pattern-Recognition-Machine-Learning-Christopher/dp/0387310738

### Is there something special about *AI4X-science*?
Check the Channing paper, but brief note about domain expertise and especially respecting the idiosyncrasies of the data.

### Some great examples of AI4Neuro



In other words, insofar as AI4Neuro aims to help neuroscience and our understanding of the brain, the actual object of study is often the workflows and ML models (but brain data is obviously a part of it). It's like building microscopes or digital filters: the actual work per se is in physics or computer science, even though it's in service of neuroscience.



- If NeuroAI is using AI as a model for biological / neuronal computation and intelligence, then what is AI4Neuro?
- It's exactly what it sounds like: using AI for neuroscience research? How?
- Well that's a great question---how, and when, can we actually use AI for neuroscience?
- Before we answer that, there's the question of what "AI" even means. These days, when the word pops up on the news, it roughly equates to large language models (LLMs) and their secondary products, like language-based chat interfaces (ChatGPT), language-vison models (Stable Diffusion), etc. That's a good case. The bad cases are when whoever wrote that has no idea what the hell they meant by that. That's more common than you'd think, to be honest, and I've also done exactly that (mostly in grant-writing and other simiar advertising contexts).
  - I have no idea what "AI" means because it very much depends on context. But for the most part, it either means LLMs, or machine learning more broadly, which in 2025 means data-constrained, GPU-accelerated optimization with artificial neural networks (aka, deep learning). This is in contrast to, say, classical statistical machine learning.
- At its core, that means a deep "model" that approximates a function empirically, learned through data. The main difference is, we can be much, much more liberal about the kind of function, and more importantly, the form of the inputs and outputs such models can deal with, compared to 10 years ago. 
- Two classical examples are signal processing functions (i.e., filters) which have or are well-defined operations (let's call that zeroth order), and statistical models whose parameters are fit through maximum likelihood inference or expectation-maximization (first-order).
- These are loose "categories", but the point is, they are functions or models where we know what exactly how it works in the forward direction, and how to arrive at these model parameters, or both.
- Deep learning or AI or whatever you want to call it, is changing that. We now have models where, although we define every single component in every module in the network (we know exactly what the attention operation is doing), we only define what we like it to do in terms of the I/O response, molded into the best approximator we can through the data we expose it to. Aside from that, we have very little idea 1) what it actually ends up doing, in terms of interpretable / understandble functions, and 2) how it got to such a solution.
- 






- spiking vs. LFP timescales in a granular fashion in Ana's data. 
  - finding categorical motifs (like oscillations) but in spiking data
  - dimensionality analysis
- statistical baseline for dimensionality stuff
- autocorrelation and (power law) covariance modes in indepedendent Poisson processes
















And *in those 18 months* since I first found this "NeuroAI vs. AI4Neuro" hill to die on, NeuroAI seems to no longer be the esoterica du jour. Don't get me wrong, people are still asking interesting questions about computation and representation, and there was even an [NeuroAI workshop at NeurIPS][neuroai_neurips] last December, where I learned that Sir Karl Friston himself was a bit of a NeuroAI enthusiast. Nevertheless, NeuroAI doesn't seem to be the only game in town anymore when it comes to AI and brains.


Instead, I feel like there came a turning point during the last 6-12 months, where communities are emerging that rallied around systematic efforts in using AI for neuroscience (...but for some reason almost always associated with "foundation models"). I especially appreciate the efforts in curating brain datasets and benchmarks, as well as to think more deeply about the opportunities and challenges in applying the LLM-based AI playbook (and beyond) to advance neuroscience.

Better late than never, these emerging trends are the perfect backdrop to motivate my unemployed ass to finish writing up these thoughts. So, after drawing the analogy of neural computation vs. computational (neuro)biology in Part I, and dissecting what NeuroAI is and is not in Part II, here comes Part III, the finale (fucking finally):

---
# What is AI4Neuro, and why are we going to suck at it?

**tldr;** I'm going to spare the drama and give you the punchline right here:

In my personal opinion, *AI4Neuro* is concerned with the overarching research questions of **how to effectively, efficiently, and responsibly use AI to advance basic, translational, and clinical neuroscience,** in particular with considerations of the idiosyncracies and heterogeneities of brain and behavioral data.

It's not about just doing it, but thinking about how to do it right. So, applying "AI out of the box" on brain data is not necessarily AI4Neuro. Banging your head against the wall over why that doesn't just work the way somebody has promised or assumed to work---even though nobody has done it for this particular problem in this particular way before---is. That is what *research* is.

In other words, AI4Neuro is not just the intersection of AI and neuroscience minus NeuroAI. Rather, the actual work lies in figuring out where this intersection begins and ends, i.e., **when and how** to integrate and leverage "AI" (as we know it today) into the scientific process currently employed to study the brain with all its oddities and limitations.

As a result, doing this kind of research means not only methodological development from the AI side and data-curation from the neuroscience side. It requires reflection and dialogue at the meta level about what AI is and is not, and how the solutions it represents can be matched to open the unidentified and undiscovered locks posed by neuroscience questions of very specific flavors.

And why do I think that we will suck at it?

Because AI is not magic: it can help us efficiently solve well-posed and well-constrained problems, especially **problems with solutions that can be verified**. Unfortunately, neuroscience doesn't have many of those problems yet. Frankly speaking, AI will suck at neuroscience for the same reason why we have sucked at neuroscience: 

**AI-powered telescope won't ever help pre-Copernican astronomers understand the universe.**

In the rest of this article, I will try to convince you why I think this is, and what I think we can do to move forward.

---
### How did we get here?
First, a quick recap: by late 2023, the intersection of neuroscience and AI seemed to be fully subsumed by the line of research called "NeuroAI", which, after some digging, I realized to have a very specific ideological commitment. Namely, NeuroAI looks for principles of **computation** (and representation) that are shared between biological and artificial networks, where computation is typically taken to be synonymous with---or at least necessary for---intelligence.

On the other hand, there exists a large body of research at this intersection of AI and neuroscience that did **not** necessarily care for how brains compute things, or at least did not place universal computation at its center. In particular, lots of people developed and applied AI tools for problems in areas spanning from fundamental neurobiology and systems neuroscience to clinical neuroscience and neuroengineering.

But like other "methods people", it felt like these people were relegated to being the data analysts of their subfield of neuroscience: second fiddle to experimentalists that collected the data, but not weird enough to be considered a "theorist", so works are scattered across different subfields and venues like bioinformatics and neural engineering.

The interesting thing here is that we're at a stage where "AI", namely ChatGPT, is pervasive enough in our daily lives that it feels like a common commodity, but at the same time, to actually use AI on research or clinical data, is a non-trivial problem that brings a whole world of pain (more on this later).

And people are starting to realize this! 

Linear regression and FFTs became part of stable software way before neuroscientists needed them, and so when the time came to blindly use them, we did. But this is not the case with AI, not yet.


- I feel like an old man yelling at the sun: is it really transformational, or just another one of the same
- sometimes reading what exists at the intersection of neuroscience and AI makes me think I'm going insane

- how is AI used now: ML, stats, etc.? What is AI?
- gotta end with foundation models
- AI scientist and the scientific process: scientists are obviously not gonna replace themselves
- defend against two problems: false positives, false negatives, OOD, interpretability
- neuroscience lacks clear metrics of success
- need a lot---A LOT---of data

- how should one use AI? only when you can check the answer, mopping up
- gold standard in AI for biology and physics, alphafold
- where are we now with neuroscience: pre-Copernican and ether
- how do we move forward? the data revolution in ML
- can we link neuroscience and behavior without positing computation or cognition as an intermediate?

- It's not unique to neuroscience or even the sciences, how best to deploy AI in a useful manner is an open question in many settings, like in business organization 

> To get organizational gains requires organizational innovation, rethinking incentives, processes, and even the nature of work. But the muscles for organizational innovation inside companies have atrophied. For decades, companies have outsourced this to consultants or enterprise software vendors who develop generalized approaches that address the issues of many companies at once. That won’t work here, at least for a while. Nobody has special information about how to best use AI at your company, or a playbook for how to integrate it into your organization. Even the major AI companies release models without knowing how they can be best used. They especially don’t know your industry, organization, or context.

15 times to [use AI][mollick_15times], and then another billion examples of where to [use AI][carlini_useAI] (“helping me learn” and “automating boring tasks”), already 6 and 12 months old, respectively, highlight both how useful AI has gotten, and how quickly we have recalibrated our expectations of their abilities.

[Jagged frontier][mollick_jagged] figuring out which of the things that AI is really good at fits which of the problems neuroscience has, and what are the immediate next steps in development to make the fit better

Do we need to really think deeply about this problem? Or just [use Transformers?][wilson_mysterious]

[miolane_2025]:https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003230

[wilson_mysterious]:https://arxiv.org/abs/2503.02113

[mollick_organization]:https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
[mollick_15times]:https://www.oneusefulthing.org/p/15-times-to-use-ai-and-5-not-to
[carlini_useAI]:https://nicholas.carlini.com/writing/2024/how-i-use-ai.html
[mollick_jagged]:https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf

[neuroai_neurips]: https://neurips.cc/virtual/2024/workshop/84721






  



















The core of AI in NeuroAI is that we can fit a model of computation to the data, i.e., computational tasks performed by humans and animals, whether that's classifying MNIST and ImageNet or solving a two-bit working memory task. 
Extrapolating from this principle, but replacing "model of computation" by model of X, how can we leverage AI in similar ways?
In other words, how can we use AI to fit other models, or models of other phenomena, to data?

- differentiability
- parameter inference for simulators
- "implicit models", i.e., data analysis
- blackbox control
- ???


- AI in biology, physics, climate sciences:
https://www.aisnakeoil.com/p/scientists-should-use-ai-as-a-tool


- known knowns and unknown unknowns: chatGPT


---



### AI for Neuroscience


[wiki_aiwinter]:https://en.wikipedia.org/wiki/AI_winter
[tweet_mineault]:https://twitter.com/patrickmineault/status/1730989784678490589
[tweet_rg]:https://twitter.com/_rdgao/status/1731376771763757298
[wiki_compneuro]:https://en.wikipedia.org/wiki/Computational_neuroscience
[trends]:https://trends.google.com/trends/explore?q=NeuroAI,AI4neuro&hl=en-GB
[mattis_ai4neuro]:https://github.com/amathislab


<!-- Fitting enough, NeurIPS---`Neural Information Processing Systems`---was arguably the modern ancestor conference for NeuroAI ("modern" because it came after "cybernetics", which was too...Soviet Union to catch on?). NeurIPS was a place for works looking at how information processing or computation happens in neural and neural-like systems, before weirdly finding itself being **the** place for completely brain-free machine learning papers for some time. Now, in 2024, as the economy goes to shit and big tech companies no longer giving 6-figure salaries to anybody that's ever written a line of `loss.backward()`, maybe we will see NeurIPS coming back to being the playground of computer neuroscientists? If the trend from this year holds up, we'll have gone full circle and come back to analyzing powerful-for-its-time artificial computing systems as we imagine how brains do things, or even as artificial brains, and this, my friends, is a tale as old as time itself. 

But if history serves us correctly, this will not be how we solve neuroscience. Or at least, this alone will not be the way. Strangely enough, I'm convinced of this after being at NeurIPS---and after visiting the Deutsches Museum and playing with some really fun fundamental physics demos--- We need an AI4Neuroscience. 

Computational neuroscience
the method becomes the model
measurements


 (no, the "neurons" in a deep neural network are not neural and we're not having this discussion here)


---
[perspective]:https://www.nature.com/articles/s41467-023-37180-x
[neurips_mineault]:https://airtable.com/appWMCgd7CqsVIRza/shrTRBBqmrT74fZLb/tbl1t9cr5qpkYsrpb
 -->


---
title: "Beyond #NeuroAI, we need #AI4Neuro---and we're going to suck at it (at first). [Part 1]"
tags: [Reflections, General Science, Science Communication, Data & Technology]
status: publish
type: post
published: True
header:
  overlay_image: /assets/images/blog/2024-01-01/neuroai.png
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2024-01-01/neuroai.png
classes:
  - wide
permalink: /blog/:year/:month/:day/

excerpt: "Is NeuroAI and AI4Neuro the new Computational Neuroscience and Computational Neuroscience?"
---

2023 came and went, and I somehow logged exactly 0 blog posts...for the first time since starting this blog in 2014. So I've resolved (once again) to write more and write more regularly, and as a consequence, post less polished thoughts. With that in mind, I'm going to start the year with a bang and potentially generate some good old ([niche][trends]) academic controversy:

> **Forget about NeuroAI, let's do more AI4Neuro{-science, -systems, -biology}.**

No, of course, don't forget about NeuroAI. But I think the latter---AI4Neuro---is quite different, and equally, if not more, important for neuroscience. When reading this, **please remember that I'm not a prescriptivist or gatekeeper** for who gets to do what in which field (or at least, I'm not trying to be). I'm simply making the case for calling something what it is, especially when it's different from something else.

---
Maybe we will look back on 2023 and chuckle at our collective naivety ([yet again][wiki_aiwinter]), but with the increasing popularity and uptake of OpenAI's ChatGPT throughout the year, and the introduction of Google's Project Gemini in December, 2023 felt like the first time in a while where we can talk about artificial intelligence (AI) in earnest and without a hint of sarcasm or irony (at least, if you wanted to). 

Sure, it's not A-**General**-I yet and these systems and algorithms have tons of limitations surrounding their robustness, safety, ethics, lack of embodiment and intuitive physics, and they still make a lot of plain dumb mistakes. But in situations where I used to be much more comfortable referring to something as machine learning (ML), today, a system that helps me code, think through problems at a conceptual level, and generate "new" (i.e., stolen and recombined) images and sentences seems, undeniably, to be AI.

2023 also seemed to be the flagpole-in-the-ground year for "NeuroAI"---an intersection and marriage of subfields in neuroscience and ML/AI---with a kind of "declaration of independence" [position paper][perspective] authored by some of the biggest who's-whos in computational neuroscience and ML, as well as the emergence of [beautifully curated resources][neurips_mineault] cataloguing the breakout of NeuroAI onto premier ML/AI conferences. In fact, it was Patrick's [original tweet][tweet_mineault] collecting NeuroAI papers at NeurIPS that got me thinking in the first place: [am I doing NeuroAI][tweet_rg], and *what is NeuroAI*?

After going to NeurIPS, absorbing the dizzying array of new research (and hand grenades), and chewing on these questions over the last month during the holidays, I came to this conclusion:

> **I am not really doing #NeuroAI**;
> 
> (for the most part, and unless you are looking to give money for neuro + AI research, in which case, I am). 
> 
> **Instead, I'm much more interested in doing AI for neuroscience (#AI4Neuro).** 

And because of this, I'm hoping for there to be a similar community for creating, curating, and contributing to a body of research that uses ML and AI to advance our understanding of neuroscience, neurobiology, and neurological disorders.

---
### Why the kerfuffle? 
"But Richard", you might say, "NeuroAI already has Neuro **and** AI in the name, so it is clearly a superset of what you're asking for, why do you want *yet another* field with its own name???"

Yes, I admit, it seems like a trivial and uncontroversial semantic debate. But you know me, I love pointless semantic debates, and I need to pump out CONTENT.

No but seriously: I think that while NeuroAI has a research agenda that is by nature very much related and complementary to AI4Neuro, at its core, it has a very different priority and asks fundamentally different questions. That being the case, I think clearly delineating the conceptual differences between the two would be beneficial, otherwise we run the risk of doing one as a "side hobby" while primarily pursuing the other. In fact, *I think we have already been doing this, under a different name.* And since science is a sociological construct and that we're in the age of hashtags, #AI4Neuro needs its own branding goddamnit!

So in this multi-part blog post series, I'm going to explain what NeuroAI---to the best of my understanding, and with references, of course---is and is not, and why AI4Neuro is a separate research direction that should come with a set of **different and clearly defined** priority, philosophy, and methodologies. 

Following that, I will talk about why I think we currently, and will continue to, suck at AI4Neuro for a little while, at least compared to, e.g., AI4Physics, and hence precisely the reason why it requires collective effort of all the brilliant minds out there to think about some very different problems. The spoiler for the final takeaway is that, while I think developing and applying ML/AI tools in neuroscience will undoubtedly advance the field, it's rather the active exercise of thinking about **how neuroscience research can be done in a way that's more amenable to using AI tools** that may potentially push it out of the current, "pre-Copernican" ages.

But to conclude this first introductory post, I will set up the punchline with a detour, to give you some context for why I was thinking about (i.e., triggered by) this nomenclature thing between NeuroAI and AI4Neuro. It takes us back to my early grad school years, circa 2014-2017, and the confusion between "*computational* neuroscience" vs. "computational *neuroscience*".

---
### "Computational Neuroscience"
For the most part, my PhD was about developing and applying computational methods for problems in neuroscience, such as signal processing for analyzing neural time series, or statistics and "data science" for multi-modal brain data, including text and images. So I thought it wasn't unreasonable to believe that my research was in "computational neuroscience", and that I should talk to other "computational neuroscientists" at conferences like "COmputational" and SYstems NEeuroscience.

This was, for the most part, a disaster: for some reason, it just so happened that the computational neuroscientists from computational neuroscience graduate programs that I was talking to at these conferences were by and large doing something entirely different and had little interest in talking to me. It wasn't that people were mean or antisocial, and maybe I was communicating my work poorly, but it simply felt like the goals and problems of my work was not something they were familiar with.

But how could that be??? We were all, after all, computational neuroscientists, right? Wrong. As the years went on, I realized that a big part of computational neuroscience---arguably its dominant view---isn't really about using computational methods *per se*, but that it is first and foremost a specific perspective of neuroscience, namely, that the brain is a computational device. So really, a majority of computational neuroscience research was about "the computational brain", and how neural circuits implement computational algorithms, similar to how logic circuits in physical computers and the embedded software can implement the representation, transformation, and transmission of information (*Narrator: "we will come back to this."*).

In other words, most of modern computational neuroscience was actually theoretical neuroscience working under a very specific perspective or assumption (one might even call ideology), and confusingly, it just happen to also employ computers and computational methods. Many to most even developed and applied new computational methods for analyzing data, but it was, at the end of the day, for extracting insights about *computations* in the brain. But the people that were "just" developing computational methods for neuroscience and neurobiology? They were (and I was) like these weird niche people doing data analysis for experimentalists, on whom we depended for our existence and livelihood (not untrue).

At this point, especially if you are a computational neuroscientist, you might either disagree vehemently or simply shrug:

You might disagree with the premise that computational neuroscience is narrowly defined as being about neural computations. After all, the Wikipedia article on [Computational Neuroscience][wiki_compneuro] says this (which feels very much like it was edited and approved by an Eastern European researcher over 50.):

> "Computational neuroscience focuses on the description of biologically plausible neurons (and neural systems) and their physiology and dynamics, and **it is therefore not directly concerned** with biologically unrealistic models used in connectionism, control theory, cybernetics, quantitative psychology, machine learning, artificial neural networks, artificial intelligence and computational learning theory;"

If this resonates with you, I'm afraid you are one of these weird people, like me, that is into biology but can't deal with the mess in a wetlab. But if you actually believe that modern computational neuroscience is not concerned with machine learning and artificial neural networks, well, I don't know what blissful hole you live under, but you should come out and play with the rest of us.

On the other hand, you might shrug and say, "well, what's the alternative to studying neural computation?" 

Sure, maybe that's what the brain does at the end of the day, but that's not the point. The point is that "computational biology" and "computational physics", as fields, are not primarily interested in the *computational properties* of biological and physical systems, but why is computational neuroscience? This will be an important point for the final part of the series, when we look at how AI4Physics and AI4StructuralBiology are done differently.

Nobody ever told me I was weird or unimportant, but I have talked to people like me who have similarly felt that they were just data analysts that work with neuroscience data. There's nothing wrong with that, and those data analysis skills turned out to be hot commodity when "data science" rolled around, with the kinds of time series, image, and tabular data that companies were dying for somebody to extract gold from. 

But beyond that, I, like many of the others, do want to understand and contribute to a theoretical understanding of "how the brain works". It's just that I thought it was more important to see the brain as a biological and electrochemical system than as a computer. I wanted a "computational neuroscience" that was dedicated to computational tools for neurobiology, including models, statistical methods, machine learning, and now, AI.

And I still do, which is the reason why we are here today. At this point, you might be wondering "why the hell did I just read this?" Well, just replace computational neuroscience with NeuroAI, and you can basically skip the next parts of the series, where I want to make the case that we should avoid the same confusion with **neuro** and **AI** as we did with computational neuroscience. Not only because of a petty semantic disagreement, but **because it will influence our understanding of "how the brain works".**


[wiki_aiwinter]:https://en.wikipedia.org/wiki/AI_winter
[neurips_mineault]:https://airtable.com/appWMCgd7CqsVIRza/shrTRBBqmrT74fZLb/tbl1t9cr5qpkYsrpb
[tweet_mineault]:https://twitter.com/patrickmineault/status/1730989784678490589
[tweet_rg]:https://twitter.com/_rdgao/status/1731376771763757298
[wiki_compneuro]:https://en.wikipedia.org/wiki/Computational_neuroscience
[trends]:https://trends.google.com/trends/explore?q=NeuroAI,AI4neuro&hl=en-GB
[perspective]:https://www.nature.com/articles/s41467-023-37180-x
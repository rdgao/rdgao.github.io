---
title: 'Can we ever accomplish non-consensual brain-reading? [Part 2] (3/52)'
tags: [Brain & Cognition]
status: publish
type: post
published: true
categories: []
header:
  overlay_image: /assets/images/blog/2017-01-23-mindreading1.png
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2017-01-23-mindreading1.png

excerpt: "All this is to say, there
is some non-zero correlation between the brain activity of two different
people describing similar things, but it is definitely not quite to the level
of thought-reading across different people."
---
Jan 22, 2017

Two days after I wrote last week's blog piece, someone mentions in class that
somebody had just done a study where they found common representation of
memory across different people's brains. I thought to myself, "well that is
just absurd." But that someone happened to be Terry Sejnowski, so I thought he
probably knows what he's talking about. So I dug up the study, which, as it
turns out, was only published about a month ago. Well, after having read
through it, I wouldn't quite say there was common representation of thought
between people, but it was interesting enough that I thought it warranted an
unexpected Part 2 to last week's post.

The paper in question is "[Shared memories reveal shared structure in neural
activity across individuals](https://www.ncbi.nlm.nih.gov/pubmed/27918531)",
from (mainly) Uri Hasson's group in Princeton. Before I get into it, I want to
review why I thought inter-subject decoding is an impossibility (for a
detailed exposition, go to previous post). There are 3 main reasons: first,
brains between different individuals are not the same anatomically; second,
you need to build a different brain-to-thought dictionary for each person; and
three, each person's thoughts are contextualized by their own lives, e.g.,
"apple" does not mean the same to me as it is to you if I've only ever eaten
green apples and you, red. The third reason is more or less the motivation for
the second, but solving either of them will bypass the decoding problem, hence
I included them as distinct.

**Overcoming the the challenges of inter-subject decoding**  
Well, I still maintain that we cannot achieve non-consensual thought-reading,
but this study WAS able to find shared structure in neural activity across
different individuals. How? Their experimental design directly overcame two of
the three issues I raised above. The setup was as follows: each participant
comes in to the lab and lies in an MRI scanner for an hour while watching a
movie (BBC's Sherlock woohoo!) and getting their brain scanned. Afterwards,
they were told to recount the story from the movie while also getting their
brain scanned. Finally, the brain data is organized by scene, where brain
activity from the same scene is averaged across time. This is done for all 17
subjects, and there are two main comparisons of interest here: similarity of
brain activity of the same person between watching and recounting the same
scene, and similarity of brain activity of two different people recounting the
same scene.

So how did they overcome two of the issues I mentioned? First, the
experimenters transformed all the brain data to a common space, an "average
brain" of some sort. There are several of these average templates in the fMRI
world, they basically need to pick one, and warp and stretch every
individual's brain such that it matches this anatomical average. This gets
past the "different brains" problem. Second - and this is subtle but very
important - the participants all watched the same movie! By doing so, all the
memories or "thoughts" about events in the movie are more or less
contextualized by the same things, i.e., scenes before and after. Of course,
they can never be exactly the same. For example, someone who is a self-
proclaimed Cumberbitch (me) will probably react very differently (emotionally)
to scenes which he is in, compared to someone who hates his acting and British
accent. In addition, objects in the scene may trigger spontaneous thoughts
from a participant's own life, like seeing a horse and remembering their own
horse-riding experience, which cannot happen for someone that's never ridden
one. But by and large, the same sensory cues are used by everyone to stitch
the story together into a coherent movie. And in this way, they have
manufactured "shared memories".

So, were they successful in finding shared structure between people who shared
a similar experience? Well, successful enough to get published. Again, there
are a few possible comparisons they look at here, but I will just focus on the
one: similarity of brain activity of two different people recounting the same
scene. The brain data for each person is basically two 2-dimensional matrices,
scene-by-brain region (voxel), since they collapsed all the measurements
during a scene into a single average. One of the matrices is made from the
watching data, which we don't care about, and one from the recounting data.

**Recounting for different people**  
This is our main question: when two people talk (and think) about the same
experience, do they evoke similar patterns of brain activity? In this study,
they didn't quite look at the one-to-one comparison. Instead, they compared an
individual's brain activity to the average of everyone else's. The math is
super simple: for a single brain area (voxel), correlate the scene values of a
single person with that of the average of the rest, and do this for all the
voxels in the brain. To test for significance, they compared to a null
distribution built from the correlation between different scenes (which should
be around zero). Figure 3 from the paper illustrates this result (below). Sub-
panel b shows the areas of the brain for which there was significant
correlation, mostly covering the higher visual areas, temporal regions, and
posterior medial cortex (PMC, circled). They further show that at the PMC
voxels, most people's correlation ranged between 0.1 to 0.3, which is
presumably the best region they could find. These seem like small numbers, and
they are, but compared to pure chance, they're still pretty good considering
all the noise and extraneous influences onto every person's brain while
recounting the movie, and that's not considering how their memories all differ
in a different way from the original movie itself. All this is to say, there
is some non-zero correlation between the brain activity of two different
people describing similar things, but it is definitely not quite to the level
of thought-reading across different people.

![](/assets/images/blog/2017-01-23-mindreading1.png)

**In conclusion**  
So in conclusion, while this is not at all the same as reading one person's
thoughts from their brain activity based on another person's thought-to-brain
dictionary, it's still an advance in the general direction, though I'm not
sure we'll ever get there asymptotically, especially when we're talking about
non-consensually. There are some implications, however. For one, we've known
for a while that sensory representation share some structure across different
people, like how everyone's visual cortex is in the back of their head, but
"memory" representation seems to also share some spatial structure. Now, we
can talk about what "memory" really is, is it even a separate thing from
replaying of sensory experiences, but that's for another time. The paper also
describes several other findings that are interesting, such as the similarity
of brain activity, within the same person, between watching and describing the
movie. Intuitively, we'd expect that memories should be pretty similar, but
not exactly the same, as the sensory experience itself, though there's no
reason why they should share any similarity in the spatial structure of their
representation. But that is what the study has found (also with correlation
between 0.1 to 0.3). One caveat here is that finding correlation between brain
activity is not the same as actual decoding, i.e. interpreting the memory
itself based on the brain activity. When the space of possible memories is
limited to a pool of 50 movie scenes, it becomes a relatively straightforward
classification task (which they perform, as another experiment), which means
you can have zero knowledge about the visual & audio features and still be
able to guess the scene. But in general, brain-reading that might be used in
any meaningful way will have to be able to decode the visual/audio/affective
features AS images/sounds/emotions, not just a categorical scene label.

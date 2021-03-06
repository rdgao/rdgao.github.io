---
title: 'Seminar Reflection - Complementary Learning Systems'
tags: [Brain & Cognition]
status: publish
type: post
published: true
categories: []
#header:
  #overlay_image: /assets/images/blog/default_header.jpg
  #overlay_filter: rgba(0,0,0,0.2)
  #teaser: /assets/images/blog/default_header.jpg

#excerpt: ""
---
Yesterday over lunch, I was lamenting over the fact that all these damn papers
I read seem to not go anywhere permanent in my brain. I mean, I can recall one
when I read the title and tell you what it's about and its key findings, but I
can't spontaneously do it, without trigger. Whether this is normal or not, and
I have a hunch that it is, I don't really care, all I want to do is remember
the things I read and be able to wield these facts in a meaningful manner.

Lo and behold, I watched my first online research talk yesterday afternoon,
held at UCSD no less. The talk was given by Dr. Jay McClelland from Stanford.
I personally am not familiar with his work at all, though that's decidedly my
problem (I think he's pretty famous in the field). The talk though, piqued my
interest a few weeks ago when I first received the promo email (and about 5
more after that first one) for the lecture series. The talk, and I'm directly
quoting, is about the [complementary learning
systems](http://tdlc.ucsd.edu/research/DNS/speakers/McClelland.html) in the
brain, the supposed "fast" and "slow" learning systems and how they interact
with each other to form new memories. Here, I shall attempt to regurgitate
everything I heard yesterday. Why? You will see at the end.

But before I start, I have to make a very important disclaimer that **1)**
this (obviously) isn't my work, and I'm literally recalling from my memory as
to what he said, and **2)** since I didn't write this (I mean, I'm WRITING it,
but more like making a transcript), I don't have any of the sources he
provided, like I usually try to do for my science-y posts. At one point or
another, I most definitely WILL visit the literature he's citing, but not
today, because I need to write this today, and there are, like always, about
100 papers cited in the talk, which I actually find very nice since it means I
get to skip all the boring literature review. And actually, the major portion
of the talk was a setup of our current knowledge, which is what I found most
interesting. Not that his actual work wasn't interesting, it's
just...unassuming, if that's the right word.

The POINT is, read on at your own discretion, and take away what you will. I
took it in good faith that his sources are valid, but in no way should you,
nor should you trust in my ability to recall what he said.

* * *

The complementary learning systems refer to two distinct masses of structures
in the brain. The canonically "fast system" refers to the hippocampus (HPC),
or the entirety of the medial temporal lobe (MTL) - this is sort of in the
middle/core area of your brain, away from the outer cortices, if you think of
it as a sphere. We know it's associated with fast learning because it's
important in forming short term memories. The evidence for this comes from
lesion studies, which is a fancy way of saying removing it, where patients
without sections of the HPC loses the ability to make new semantic memories
(facts) almost completely, while their ability to form procedural (learned
abilities, like juggling) memories stay intact. One specific patient is very
famous for this, and he goes by the name [Henry
Molaison](http://en.wikipedia.org/wiki/Henry_Molaison), or H.M, prior to his
death.

The other part of the complementary system is the neocortex, which is a quite
broad umbrella that includes e.g. your frontal lobe, temporal lobe, etc.
Basically, these places are the permanent storage of the things you know about
life - apple is red, sky is blue, I live in Toronto, etc. It's said that the
neocortex learns new facts extremely slowly, on the order of weeks, and this
comes from rat studies, I believe. Also, before going further, it was stated
that the "connectionist" assumption is required, which says that memories, or
information in general, are stored in the particular pattern that neurons are
connected, and hence, activated. It seems to me like that's the basis of
neuroscience, but it's cool to be reminded that that, in fact, is still an
assumption, simply one that is heavily subscribed to.

So how do these two systems play with each other? Well, one theory is that
while the neocortex holds the known information, any new information is first
represented in the MTL. And there's a stage called memory consolidation, which
sees the transfer of knowledge, if you will, from the MTL to the neocortex.
Several findings suggest this, which are actually pretty cool. For one rat
experiment, it's been reported that during sleep, the hippocampus plays back
the memory that the rat experienced during the day, in the pattern very
similar to the activation. This alone doesn't seal the deal, since it could
just be played back...for fun? It doesn't necessarily need an audience, and
who's to say the audience IS the neocortex, as the recipient of the new
memory. Alas, crude as they are, lesion studies often prove the most
enlightening. It was found that in experiments where the rat needs to memorize
a certain pattern, like routes in a maze or something, those with this short
term memory intact can perform well on the same task the next day. But if you
remove the hippocampus soon after the initial learning, the rat suddenly
doesn't know what to do anymore. In other words, the later you remove the
hippocampus, the better the rat is able to perform. This is pretty
convincingly in favor of the idea that the MTL is, in fact, a temporary
storage for new memories, and this was my first big takeaway: **new memories
don't consolidate in the cortex right away, and if you want something to
stick, you have to keep at it for a while**. Because while the hippocampus
acts as a short term storage, the amount of new things we learn every day is
of course greater than what the buffer can hold - IF you're forgetting things,
that is. Totally not saying that this is scientifically correct, but I'm
relating this "fact" to the effectiveness of repetitions in learning, and the
common saying that you need 21 days for a habit to form. I guess this means I
have to keep reading the same paper for a while...

This model was all fine and dandy, until a new experiment showed that if the
new thing being learned is not completely new, and that it relates
(conceptually or semantically) somehow to existing knowledge, then the rat's
ability to permanently store this knowledge becomes much greater, i.e. faster
consolidation to long term memory, less affected by HPC lesion. This next part
I'm a bit fuzzy on, but it was shown that there is an increase of chemical
expression (or was it gene?) during the consolidation of new memories, and for
the 3 different memory conditions - completely new, new but related,
completely old - the "new but related" condition (the rat, more accurately)
showed the highest increase in the expression of this thing that I forgot. The
point is, and this was my second big takeaway: **learning new things is easier
and faster if they are related to old things, or rather, if you have a
conceptual model already in place.** This seems intuitive from our everyday
experiences, but why should it be true from a neuroscience perspective?
Furthermore, it is in disagreement from the neat separation that hippocampus
is for short term storage, and neocortex is for long term storage.

So the above was all background, and I believe Dr. McClelland's new work is in
demonstrating this finding in an artificial neural network. In a network
representing semantically represented things (e.g bird-can-fly, tree-is-
plant), upon the insertion of a new item, it was found that the new item can
be integrated faster and with less disruption to the original network if it's
similar to an existing concept. In other words, adding "salmon" to this
network of semantic concepts is easier if, say, "trout" already exists, both
in terms of integrating "salmon", as well as not screwing up the known
relations such that it says something stupid like fish-can-fly...until you try
to add flying fish anyway. I think this is very cool, in that the artificial
network can magically mimic its biological counterpart- I say magic not to be
cheeky, but to say that there is no reason that the artificial and the
biological SHOULD match, because it's not for certain that our biological
neural network is even represented accurately by the artificial, not in the
current framework at least.

* * *

That concludes my regurgitation, as you can see, it's very rough and missing
quite a few pieces of crucial information. But the reason I was adamant in
writing it down was exactly in accordance with my first takeaway: that
repetition aids memory formation. I totally didn't have to write it on my
public blog, because who knows who will take this misinformation and runaway
to say something completely unjustified. But in the end, my conscience is
kosher because of all the "DON'T TAKE WHAT I SAY HERE TO BE TRUE" qualifiers I
put down, because I don't have the pressure to write anything actually useful
(lol) and prescriptive like most pop science websites do. DO check out the
sources if you're interested, a great place to start: James McClelland. I'll
try to come back and put in some papers at the bottom of this once I do my own
research, if I remember (and that's a BIG if). Also, as always, feel free to
tell me that you thought of something interesting while reading, or that I was
right or wrong or whatever, or that I'm an idiot (but you won't be adding
anything new).

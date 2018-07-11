---
title: We suck at statistics
categories:
- Science
tags: []
status: publish
type: post
published: true
meta: {}
---

Over the weekend, many of you participated in my little psychology experiment
for a course. Before I go into it, I just want to give a shout out to all
those that responded, which was way more than I had expected. Even the couple
of you that gave non-sense answers >_>.....your effort is duly noted.

So what was the mumbojumbo about? Well for anyone that didn't do the survey,
you can give it a try [here](http://goo.gl/forms/kpiYExG4jM) before reading
on. The complete write-up is [here](/s/Assignment1.pdf), it's a bit tongue-in-
cheek because I thought this whole project was a waste of time, so it might be
an enjoyable read, though it's probably easier to just read the summary that
I'm about to write.

The experiment was an adaptation of a study done around 30 years ago. The
original question that was posed to participants was as follows:

_Linda is 31 years old, single, outspoken, and very bright. She majored in
philosophy. As a student, she was deeply concerned with issues of
discrimination and social justice, and also participated in anti-nuclear
demonstrations._  
Which is more probable?  
1\. Linda is a bank teller.  
2\. Linda is a bank teller and is active in the feminist movement

Surprisingly (or not), the original finding was that way more people chose the
second, the conjunction of the two probabilities, as more likely than the
first, henceforth dubbed the conjunction fallacy. To see why option 2 is NOT
more likely, consider that 2 is a subset of 1, and for 2 to occur, 1 must also
occur, hence 1 will always be equally or more likely than 2. Formally put, the
probability of two events P(A,B), will always be less than the probability of
its constituents: P(A,B) < P(A), P(B).

Half of you that have done the survey and is currently reading is probably
thinking to yourself, "well shit", because that's how many of you screwed this
up, 50%. Despite what I thought about the project, I DID think that more of my
sample population would do better, since most of my Facebook associates are
university grads and probably have a degree in a STEM field. Worry not though.
In the past 30 years, this experiment has been done to death, with different
manipulations to control for different things, and it has even been done with
statistical experts, i.e. grad students, statisticians, etc, to no (or very
little) avail: the conjunction effect remains. And people have had all sorts
of explanations for this, the most popular one being that option 2 was more
"representative" of Linda than option 1, hence it seems more likely to us. To
take it a step further, the fathers of this experiment, Kahneman & Tversky,
postulated two systems of human reasoning. System 1 is fast and imprecise, and
uses "heuristics" to make quick judgements in the real-world, and system 2 is
more logical and follows formal mathematical steps. I'm not really doing it
justice, neither am I trying to, go read Wikipedia if you're interested. My
personal opinion is that a psychological theory already has limited
credibility if it's supported only by behavioral experiments, but I'm just a
grad student and this guy has a Nobel Prize in Economics, so what the hell do
I know? In any case, this phenomenon is probably real, it just depends on how
you explain it.

My experiment, though, was not to reproduce the findings in a modern world. As
much as I would have liked to coast on the assignment, this class actually has
a letter grade. No, I had a hypothesis that unfortunately took all week for me
to conjure up, and it was this:

What if you inserted a third statement, one that was a lot closer in
probability to the constituent (option 1). Would the difficulty in ranking
those two options then jumpstart your system 2, which then carries over to
your judgement of the conjunction option? In other words, your system 1
(heuristics) operates in a large scale regime, and is only able to make
decisions up to a certain limited resolution. If you have two choices that
appear too similar heuristically, you might be forced to activate your formal
statistical system, which really separates fine-grained things. It's like
comparing whether or not you want to eat out, and whether you want to eat
pizza or burgers for lunch, and the latter is SO MUCH HARDER. In comparison,
an unrelated statement, or one that was much farther away in probability,
would not result in activation of your system 2. I drew a nice little picture
to outline this:

![](/squarespace_images/static_5351781ce4b0757a373c3d73_535182ade4b0bcfb2b4574dd_5451f209e4b04057136b5eb0_1414656522347__img.jpg_)

I like how the red squiggly lines are so bait. Yeah I screenshot this from
Word, sue me. Go read the PDF if you're not here for the humor. Carrying on,
so the prediction would be, in the experimental condition (the close
condition), people would display less conjunction fallacy, since system 2 was
activated and carried over. Conversely, people in the control condition (the
far condition) would do worse, because it was so easy to rank the additional
statement that no extra thought was given. So I retrofitted the problem (Linda
is now a consultant rather than a banker because times are hard and girls
gotta get paid), and added an additional, different, option. The control
option was "Linda graduated from college/university", which she obviously did,
because she majored in philosophy. Luckily, most of you got this. The
experimental option was "Linda is a consultant and works more than 40 hours a
week." Confession time: I had originally intended the experimental option to
be MUCH closer in likelihood to the constituent (Linda is a consultant),
because I thought it was common knowledge that consultants work 50-60 hours
minimum. That's actually why I put MANAGEMENT consultant, because they're
usually the crazy people. But apparently this was NOT common knowledge,
probably because not everyone that answered tried applying for a consulting
job. I digress. Luckily, this additional one ended up being much closer to the
conjunction option, i.e. 50% of the people ranked "Linda is consultant and
works more than 40 hours" higher in likelihood than "Linda is consultant and
activist", and vice versa. Go to end of the [PDF](/s/Assignment1.pdf) to see
the full ranking tally.

Well, what was the main finding?

*Drum roll*

![Science and
Whatever](/squarespace_images/static_5351781ce4b0757a373c3d73_535182ade4b0bcfb2b4574dd_5451f617e4b0f2185905eedc_1414657560475_results.jpg_)
Science and Whatever

What are the 3 bars? They represent the percentage of people that correctly
ranked the constituent to be more likely than the conjunction, i.e. P(Linda is
consultant) > P(Linda is consultant AND something else). How these were
calculated was basically, ignoring the third option, to see if the constituent
was ranked higher than the conjunction. And in the case of the experimental
condition, there were two conjunction options, hence two blue bars.

The red bar is the result from the control condition, where the "something
else" is "activist". The middle blue bar is the same "something else" but in
the experimental condition, and this is really where the money is at. Remember
that the hypothesis was that people exposed to the more difficult (closer)
choices would use their system 2 and thus do better on this task? Well they
did, by a whooping 6%. I'll be honest with you, I don't even know how to put
error bars on a statistic like this, what's my measurement error? What's my
variance if I had one trial. lol. No, you don't need to remind me how shoddy
this science is, though I'd be happy to hear about it, because I may or may
not make such mistakes on actual science, whenever it is that I get to do
that. Besides, blame yourselves for not participating enough, I COULD have had
statistical significance. In any case, whereas any normal person sees this and
says "this really doesn't seem like anything", I will go the scientist way and
say, "this preliminary result warrants further investigation, preferably with
money for fancy brain technology." The one good thing was that, at least the
exact same percentage ranked the OTHER conjunction as more likely, so it
counts as like a second trial, if you squint a little.

The takeaway? Half of you suck at statistics. Either that, or you knew what I
was looking for and cooperated (subconsciously, which is a [real
thing](http://en.wikipedia.org/wiki/Demand_characteristics)), in which case,
d'awww :'). Okay really though, don't feel bad if you got it wrong, this is
just how you evolved to adapt to the environment around you. If you made the
statistically correct choice all the time, yeah your life would be more
"correct", but you'd spend 200% more time doing literally any little thing.
This is where the 80-20 rule comes in, otherwise known as "fuck it I'll just
wing it". The best part of this is what some of you wrote for the
justification, because it's scary how well some people justified their wrong
answer, like it almost makes you feel stupid for thinking statistically. Full
data set is
[here](https://docs.google.com/forms/d/1B5T_UfqXe9MrXci45Vh3k8JgKnaFHwnrLTWHvnB5zGE/edit?usp=sharing)
if anybody's interested. Also it was funny because even though the responses
are anonymous, I could pretty much tell who's writing what, especially things
like "too lazy".

Once again, a big thank you to everyone that participated and contributed
meaningfully. As much as I thought this to be a pointless waste of time, it
was fun to engage people I know in this shoddy science, which by the way is
NOT what I do professionally. So hopefully the next time one of you gets
involved with my experiments, it will be some really cool shit, or maybe I'll
just need to borrow your brain, or something. As always, comments and
suggestions are very welcome, about the writing or the science, or if you just
have beef with experimental psychology, then we can have a drink and complain
all about it.

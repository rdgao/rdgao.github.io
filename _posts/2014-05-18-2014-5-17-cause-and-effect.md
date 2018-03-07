---
title: Cause and Effect
categories:
- Science
- Rambling
tags: []
status: publish
type: post
published: true
meta: {}
---

Correlation neither is nor implies causation- it's simply more useful.

Something that's been bothering me for a while is this notion of cause and
effect. On the one hand, it seems painfully obvious that causal relationships
exist, e.g. the letters do not appear on the screen if I do not hit the keys.
But on the other hand, how does one observe causality? What are the necessary
conditions behind one event causing another?

We might say that one necessary prerequisite is that the cause precedes the
effect, or, more rigorously stated, anything that can be a cause must be in
the light cone of the effect. In other words, the cause must be sufficiently
before the effect in order for it to be deemed causal, and the time period is
determined by the spacetime coordinates of the events and, of course, the
speed of light.

Surely, this is not unreasonable to ask for, at least from the perspective of
physics, but what next? Is everything in the past a cause of an effect in the
future? Intuition says no, the caveat being that some causes may not be very
obvious, with the "butterfly effect" becoming something of a cliche. Then we
might move onto a stricter criterion, let's say, the effect cannot occur
without the cause. A brief review of logical expressions on Wikipedia [1]
informs me that there are then two kinds of causes: necessary causes and
sufficient causes. To my understanding, necessary causes are, obviously,
necessities, and all of the necessary causes combine to form a single
sufficient cause, motivating the effect thereafter. Sufficient causes, on the
other hand, can single-handedly enable the effect, in other words, the first
sufficient cause is a necessary cause, but no particular one is a necessity.
It then becomes crucial to distinguish whether a cause is necessary,
sufficient, or both.

But what we've resolved thus far is only that there are different kinds of
causes, but nothing about what a cause actually is. And how can we talk about
causation without mentioning its ugly sibling, the fundamental point of
confusion: correlation? Putting that aside momentarily, though, let's delve
into the problem of induction, the line of reasoning that infers future from
past. This is perhaps the most crucial concept in the scientific inquiry,
which ironically is not the concern of scientists, falling instead in the
domains of philosophy of science. The problem of induction has been discussed
by Western philosophers (*the extent of my knowledge from a 200-level course)
dating back to ancient Greece, sprinkled with resolutions from prominent
mathematicians and scientists, but the problem still stands: any experimental
observations cannot be guaranteed to apply to the future. To put it more
bluntly, "causation" has no place in the future in that one cannot extrapolate
"A causes B" with 100% confidence. Actually, in that sense, correlation holds
just as little water in the future, protected only by the margin of error
we've given ourselves.

Thus, we can relieve ourselves in eliminating the concerns of the future, at
least for now, and simply ask: did A cause B in our past observations? In
Granger's original econometric causality paper [2], he states, or rather,
defines, causality as "Y is causing X if we are better able to predict X using
all available information than if the information apart from Y had been used."
In other words, since we don't quite know what we mean by "causing", we will
just define A to be causing B if A's past _correlates_ with B's present (or
future, as observed in the past). This can be quite rigorously measured, and
extends naturally into intuitively causal relationships, such as the fingers
hitting the keyboard. The crucial insight here is that, _Y's past is a better
predictor of X's future than X's past itself, given all available
information_. In a way, Y can be thought of as an orthogonal linear basis in
the causal space of X, along with many others, hidden and visible. Indeed,
imagine letters appearing on the screen: no other variable correlates with the
appearance of a specific letter on the screen better than the pressing of a
specific key, other than perhaps the command signals residing in our nervous
system. Additionally, Granger adds the qualifier that for non-stationary
processes, the existence of causality may not be constant over time. On the
one hand, this is quite a reasonable statement in itself, given the metric
defined, as well as the unpredictable nature of non-stationary processes. On
the other hand, though, it does nothing for our intuition, as the question
remains still: how is A causing B if A only causes B sometimes?

I will conclude the referenced discussion here, with the disclaimer that
Granger intended this type of causality to be only applicable in economics
[2], and perhaps other social (read:vague) sciences. I'm confident that I will
revisit this discussion in due time, likely after absorbing more of the
historical discussions that have preceded me. As for now, I am satisfied with
the separation of causality in philosophical terms versus in scientific terms,
borrowing from Granger's Causality. I think we can all agree that correlation
is necessary for causation and that, as discussed above, strong correlation in
the face of all available information is as good as causation. But as a
reasoning human being, it's been hard to reconcile this lack of causation with
my linear line of reasoning- if A then B. Although, it seems that scientists
and successful thinkers alike have become extremely proficient at forgoing
this notion of cause and effect, which may or may not turn out to be fool's
gold. Instead, the pragmatic focuses on maximizing certainty in correlations,
and leaves the absolute to the philosophers.

_____

[1] Wikipedia contributors. Necessity and sufficiency. Wikipedia, The Free
Encyclopedia. April 25, 2014, 02:53 UTC. Available at:
[http://en.wikipedia.org/w/index.php?title=Necessity_and_sufficiency&oldid=605695523](http://en.wikipedia.org/w/index.php?title=Necessity_and_sufficiency&oldid=605695523).
Accessed May 18, 2014.  
[2] Granger, C. W. J. (1969). "Investigating Causal Relations by Econometric
Models and Cross-spectral Methods". _Econometrica_ **37** (3): 424–438.
[doi](http://en.wikipedia.org/wiki/Digital_object_identifier)
:[10.2307/1912791](http://dx.doi.org/10.2307%2F1912791).
[JSTOR](http://en.wikipedia.org/wiki/JSTOR)
[1912791](http://www.jstor.org/stable/1912791)  
[3] Wikipedia contributors. Granger causality. Wikipedia, The Free
Encyclopedia. April 2, 2014, 05:39 UTC. Available at:
[http://en.wikipedia.org/w/index.php?title=Granger_causality&oldid=602374976](http://en.wikipedia.org/w/index.php?title=Granger_causality&oldid=602374976).
Accessed May 18, 2014.


---
title: 'Can we ever accomplish non-consensual brain-reading? [Part 1] (2/52)'
tags: [Brain & Cognition]
status: publish
type: post
published: true
categories: []
header:
  overlay_image: /assets/images/blog/2017-01-23-mindreading1.png
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2017-01-23-mindreading1.png

excerpt: "In other words, in order to read my thoughts from my brain
activity, you would need to make a whole new dictionary, just for me, which
requires my active participation. You wouldn't be able to take someone else's
brain-dictionary and use that to interpret my thoughts."
---
Jan 14, 2017

Back when I worked at InteraXon ([Muse](http://www.choosemuse.com/)) making
the consumer EEG device, we often get investors and journalists that visit to
check out our tech. Part of my job was to strap them with our 4-channel EEG
and take them through a demo app. The number one joke that everybody tells,
upon seeing their brainwave on the computer screen, is: "Hey, I have a brain!
My wife never believed me!" (For some reason, they were almost always men).

The second most common comment I got, though, is: "you can't read my thoughts
with this, right?" I could never tell whether they were joking. I think some
were, but some were seriously concerned. In fact, we had a company template
for responding to that question on the website, which is to compare the EEG
headset to a heart rate monitor, with which one can only gather a person's
general state of being, but not any precise thoughts.

Well, fast forward 3 years. Here I am, In the middle of a PhD studying
computational and cognitive neuroscience. The technology we were using was
obviously not good enough for brain reading, neither would the state-of-the-
art science be today. But what about the future? Can we EVER get to a point
where our thoughts can be monitored, discreetly and non-consensually, via
brain signals?

The answer: I don't think so. I doubt we will ever get to a point where any
individual can be pulled into a brain recording room and have their private
thoughts read by someone else, perhaps our new Big Brother government. But if
that WAS possible, it would have some pretty crazy implications on how our
brain works. Let me explain.

* * *

**Intra-subject Brain-Reading**  
We are currently getting closer to a particular kind of thought-reading from
brain signals: intra-subject decoding. The gist of these experiments is: a
subject is instructed to observe many stimuli of the same kind, such as
thousands of pictures or soundbites. Meanwhile, their brain signal is
recorded, via neuroimaging (fMRI) or electrophysiology (EEG). This procedure
generates a dictionary of sort, where a particular pattern of brain activation
is mapped one-to-one with a particular image, for example. It's important to
use many different stimuli in order to probe the full extent of the brain
response. At the same time, however, it would be unnecessary to show them
every image imaginable. This is because most types of stimuli, like images,
can be deconstructed into some fundamental elements. To give a more intuitive
example, there are countless numbers of possible English sentences, but there
are way fewer English words. And if we assume that a person's brain reliably
responds to individual words differently, then as long as we know the word-to-
brain response mapping, it would be possible, theoretically, to reconstruct
any sentence they are hearing by piecing together their response word by word.
Images work similarly, but instead of smaller, discrete elements, they're
decomposed into edges, angles, colors, etc.

All that is to say, to read someone's thoughts from their brain, we would
first need to build up a brain-dictionary that contains all of a person's
possible responses. From that point, we can then predict their response to,
say, images we haven't shown them. Conversely, by looking at their brain
response, it is possible to reconstruct what image they are seeing, even if
it's one they've never seen before. Watch this cool
[demo](https://www.youtube.com/watch?v=6FsH7RK1S2E) from UC Berkeley. The
reconstructed images (or movie), at this point in time, is pretty poor. We can
get a gist of what the original movie looks like when they're shown side by
side, but as you can see, it's still very blobby. This, however, is likely to
improve very rapidly, and is not the main theoretical limitation.
Hypothetically, if you had access to every single neuron's activity and enough
training examples (e.g., images shown), it's conceivable that one could then
get a good rough estimate of somebody's perception and internal thoughts. And
voila, we have intra-subject thought-reading.

**Inter-subject Brain-Reading**  
If the above is true, why wouldn't someone then be able to forcibly or
discreetly record my brain activity and read my thoughts? The answer, or at
least I think, is that the brain-to-thought dictionary is not generalizable
across people. In other words, in order to read my thoughts from my brain
activity, you would need to make a whole new dictionary, just for me, which
requires my active participation. You wouldn't be able to take someone else's
brain-dictionary and use that to interpret my thoughts. In technical terms, we
say that the representation is not invariant across brains (inter-subject),
and that the way information is encoded depends on the substrate that it's
encoded on. To give a counter example, writing the same word on different
types of paper with different colored pens does not change the information
transcribed, at least with regards to the meaning of that word.

Here, I say "I think" because this is not certain to be an impossibility, but
is very unlikely for two reasons. First, our brains are all very different
physically, so it's impossible to find common anatomical mappings of the same
information between different people. As of right now, we know that, for
example, the back of the brain in almost everybody (visual cortex) encodes
visual information, so that's in a way invariant. But it would be very
difficult to be more precise than that, because there aren't a lot of common
landmarks to orient a common decoder. Second, if it turned out that
information is represented in the brain not spatially, but temporally, via the
exact timing a particular sequence of neurons fire (which we don't know), it
is even less likely that a decoder can transfer between two people, because
your brain would have to save the appropriate sequence for the appropriate
concept, lest you never experience that concept in your life. Given the above,
unless someone kidnapped you, strapped you into a brain scanner while feeding
you thousands of stimuli while recording your brain response, they will not be
able to interpret your thoughts from your brain. So all thought-reading in the
future will likely have to be consensual, though they could very well kidnap
you...but that's outside the bounds of theory.

**Theoretical Considerations & Implications**  
At the end of the day, this is still a mystery because of a central question:
how does a brain - any brain - represent information? Or what is the [neural
code](http://haxbylab.dartmouth.edu/publications/HCG14.pdf), as people like to
say. As unlikely as I think non-consensual thought-reading is, it does appear
that some information IS invariant across different people. For example, most
people have tonotopic mapping of sounds, where sounds similar in pitch are
represented closer together in the cochlea & auditory cortex. The same is true
to an extent for visual information and motion. But I believe this is due to
commonality in our experiential world: since all of us see vertical lines all
the time, they are then likely to be represented prominently and similarly in
our brains, though you will still need to find some landmark to orient two
brains to. And as we move to more abstract ideas, such as a particular thought
or idea or feeling, it's likely represented differently because we experience
them so differently. This implies that, if we had a brain decoder that worked
well for several different individuals, then they will have had similar life
experiences, at least with respect to the particular concepts or thoughts
being decoded. But who knows, maybe there is some genetic program that drives
our neural representation to be more similar than we currently understand, or
there may really be an universal neural code that we haven't discovered -
those are the crazy implications for how our brain works if we were able to
realize non-consensual inter-subject decoding in the future.

Question that I can't answer but I think is analogous: can we decode the
software state of a computer, given that we know its hardware architecture,
operating system, and have realtime recording of all transistor states in the
CPU and memory? My guess is yes, since knowing the OS basically means that we
know the mapping of a particular computer. Someone educate me please.

* * *

Addendum: I found this paper ([Inter-subject neural code converter for visual
image representation](https://www.ncbi.nlm.nih.gov/pubmed/25842289)) trying to
solve the exact problem that I've raised above, translating one person's
brain-dictionary to another's. The key here, as I outlined, is that they still
need to build both people's dictionaries, and then finding some transformation
that maps one person's brain activity onto the other's, for the same stimulus.

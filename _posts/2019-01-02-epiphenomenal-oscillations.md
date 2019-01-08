---
title: 'The (Epi)Phenomenal Oscillation, Spike, and LFP'
tags: [Mind & Brain]
status: publish
type: post
published: true
header:
  overlay_image: /assets/images/blog/2018-09-09-CCNbanner.png
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2018-09-09-CCNbanner.png

classes:
    - wide

excerpt: "The one where I write down all in the same place why oscillations and LFPs are not epiphenomenal because I'm tired of having the same damn argument over and over again."
---

Since Day 1 in the Voytek lab, Brad has floated around the idea of writing an "oscillation is epiphenomenal" review paper to argue that oscillations don't actually "do anything", in an effort to check ourselves and our starting assumptions that oscillations __are__ important. It wasn't really an actual project, but more of a challenge for us to be critical of our own work, and that of the field as a whole. Not that we tried very hard, but I don't think we found a lot of concrete published evidence outlining a solid argument from the ground up for either position, aside from theoretical contributions like Communication Through Coherence [(Fries, 2015)][ctc], though it's certainly a talking point in the community now. For example, see the recent [Cardin][cardin]/[Sohal][sohal] JNeuro dual-perspective on gamma oscillations, though these already accept the premise that gamma oscillations are important, or are at least useful for dissecting local circuits.

Fast forward to present day: I don't know why, but over the last 6 months or so, I've had several arguments in person and on [Twitter][osc_tweet] about this particular thing, usually starting with me getting heated over someone saying "oscillations/LFPs are epiphenomenal", or something to that effect, as per this recent article in [Scientific American][sci_am] (and accompanying [response from Miller Lab][miller]). It occurred so frequently and with such conviction from its proponents that I really don't think we need to write that review article anymore, since people are already convinced. Over the course of these arguments, however, I have yet to hear a solid case for why somebody should take the position, empirical or otherwise, that oscillations or LFPs are epiphenomenal and, as such, should be ignored in our neuroscience inquiry. It's also unclear just how many people actually take those positions, and to what degree. I have, however, gained an understanding of the different reasons why people might __think__ that it's sensible to ignore oscillations from a "theoretical" point of view (and usually in favor of spikes), and typically it stems from some unchecked assumptions/ epistemological position. Keep in mind, this is my limited sampling from anecdotal experience.

Look - I'm obviously not claiming to be impartial here. This is the only hill I've ever lived on throughout my PhD so I will probably die on it too. But I think I'm more than willing to concede to better positions should they be convincing. I'm not saying we know where oscillations and LFPs come from, nor why they __definitively are__ important/causal/non-epiphenomenal - far from it. However, throwing this squiggly baby out with the bathwater, especially in light of established relationships between brain and behavior in the cognitive literature (a quick example [here][attention]), seems premature and ungrounded, especially when the arguments seem to come from truths derived from first principle, of which there are little in neuroscience.

So I'm writing this blog post for two purposes: first, it's to collect, outline, and refute a handful of arguments for why "oscillations/LFPs are epiphenomenal"; second, it's to invite better counterarguments for me to consider, in case I should move on to doing something better after this final stretch of the PhD trudging through OscillationLand.

---

# Disentangling the question
Before delving into it, I have to clarify some terminology. Up to this point, I've been using oscillations and local field potentials (LFPs) together and interchangeably. I did this because these two terms are routinely conflated/combined when this debate comes up, and we need to be precise about what we're actually talking about from here on out.

__Oscillation__, in the context of electrophysiology, typically refers to rhythmic activity commonly recorded in the extracellular space of the brain tissue, hence the overlapping reference to LFPs. However, oscillations can be (and are routinely) recorded intracellularly as rhythmic membrane voltage fluctuations, or even in synaptic current/conductance changes, with evidence showing that the two are closely linked, e.g., [(Okun et al., 2010,][okun][ Haider et al., 2016)][haider]. Hence, "oscillation" from now on refers to rhythmic electrical patterns recorded in/on the brain, regardless of the specific modality. There's an ongoing debate on what exactly counts as an "oscillation" - how stable, how many cycles, minimum amplitude, etc - even in our lab, but that's a totally separate issue that cannot be addressed here.

__Local field potentials (LFPs)__, on the other hand, refers to the low-frequency component (<500Hz) of the extracellular recording, in contrast to the >300Hz action potential waveforms (spikes). Historically, at least in systems neuroscience literature, LFPs are exclusively recorded for oscillations: theta in the rodent hippocampal circuit, slow waves in slices _in vitro_, or under anesthesia/sleep _in vivo_, further entangling LFP and oscillations. Personally, I use LFP as a stand-in for all low-frequency recordings, which would then include MEG, EEG, and ECoG. I'm aware that this is sometimes a __bad habit__, because the biophysics of these signals are vastly different. However, what they have in common is that they reflect (usually) slow integrated transmembrane currents, (usually) stemming from synaptic inputs [(Buzsaki et al., 2012)][buzsaki]. In addition, these different signals are sometimes acquired for different types of neuronal/cortical dynamics, like ERPs & oscillations in EEG, and broadband fluctuations in ECoG. Thus, lumping them together (under "LFP") is a convenient way to refer to all these signals of interest quickly, so I will continue to do so here with the above disclaimer that you should probably not do this formally.

__Epiphenomenon__, to be honest, is a word whose contextual usage I don't fully appreciate nor understand, given my limited training in philosophy.

![][webster]

From this, I assume when people refer to oscillations and LFPs as epiphenomenal, they mean that they have no __additional__ causal influence over the primary causal phenomenon, which is typically assumed to be the neuronal spiking that does the causing. One thing to keep in mind about "epiphenomenon": what do we actually mean by cause and effect here? I raise this question because there isn't a one-size-fits-all answer, but depends on what you're investigating, more or less.

---

With those definitions out of the way, I'm going to unpack "are oscillations/LFPs epiphenomenal" into the following questions and address them individually:

1. "Are LFPs epiphenomenal?" - do extracellular (non-synaptic/gap-junction) fields impact neuronal activity or cognition/behavior?

2. "Are oscillations epiphenomenal?” - do macro/mesoscale oscillatory activity impact neuronal activity, over and above the spikes that generate the oscillations?

3. "Are LFPs exhaust fumes?" - are LFP & other field recordings useful over and above recording the spikes that contribute to generating them?

4. (Bonus) "Are spikes epiphenomenal?" - what is cause and what is effect?

---

# 1. "Are LFPs epiphenomenal?"
Depending on your stance on whether we know what the true causal agent in the system is & what is being caused, this question can be interpretted two ways. The first asks whether neurons can be [ephaptically coupled][wiki_eph], such that non-spiking activity can influence spiking. In other words, can changes in the extracellular fields (non-synaptic and gap-junction) impact neuronal spiking activity over and above the synaptic currents that were a direct result of spikes?

A handful of recent studies (that I'm aware of) have demonstrated ephaptic coupling in neurons: for example, in the fly olfactory system [(Su et al., 2012)][fly_olf] and rodent cerebellum [(Han et al., 2018)][rod_cer] (also see [Anastassiou et al., 2011][ephaptic] for a more comprehensive review). Additionally, one of my all time favorite papers [(Fröhlich & McCormick, 2010)][endogenous] showed that an applied external field can entrain spiking in ferret cortical slice, parametrically to the oscillatory field frequency. Finally, even if it hasn't been shown extensively, it's perfectly conceivable that glial currents [(Martinez-Banaclocha 2018)][ephaptic_glial] or even non-spiking related calcium currents in neurons can set up a strong enough external field to influence nearby neurons. Given the above evidence, and the fact that an action potential is simply ions rapidly shifting across the membrane, it would be hard to make the case that LFPs __definitively__ cannot influence spikes.

If we do not assume that spikes are the __one true causal agent__ in the nervous system for behavior, and allow for the possibility that cognition or subjective experience can arise from non-spiking mechanisms, such as hormonal changes __directly__, then it would be an even bigger claim (without evidence) to say that LFPs absolutely cannot contribute directly to cognition, as an aggregate or emergent field phenomenon. This is a can of worms I don't want to open here, because that requires us to change our minds about the fact that __spikes are king__ in cognition. In either of the two interpretations, however, it's my personal opinion that these are interesting and potentially fruitful avenues of investigation. Just because spikes have been good to us in the last 100 years, doesn't mean we can't stray a little?

---

# 2. "Are oscillations epiphenomenal?”
We know that oscillatory or rhythmic inputs will causally bias/entrain spiking timing (spike-field coupling). This is not really up for debate, given the large body of empirical evidence for several well-characterized circuits in the brain, such as theta and gamma in the hippocampus, nor is it very surprising, since periodic synaptic bombardment will cause periodic threshold crossing, and generate periodic downstream spiking. Instead, when someone says oscillations are epiphenomenal, (I believe) what they typically mean is that macro/mesoscale oscillatory activity do not impact neuronal activity __over and above__ the spikes that generated the oscillations. Hence, the spikes are the true causal agents. If my inference is correct, this assumes that any oscillations recorded - both intracellularly and extracellularly - are a direct product of synaptic currents induced by rhythmic spikes...

...and that's a __huge__ assumption: as is the case with LFPs, we simply do not know for certain whether all oscillatory dynamics are caused by neuronal spiking. On the one hand, glial and non-AP-induced neuronal transmembrane currents are legitimate candidates to be detected as oscillations, especially, once again, large-scale calcium waves that arise as a nonlinear function of spikes/firing rate. Additionally, oscillations may occur as a result of anatomical arrangement or cellular (structural) morphology which enables, for example, some kind of (stochastic) resonance phenomenon. Given that action potential generation is inherently a limit cycle process and that constant current stimulation will cause periodic spiking in neurons, it's not inconceivable that something __more__ than just the incoming spikes determine the resulting oscillatory dynamics. Finally, there's a question of "how direct is a __direct__ consequence?" If an action potential arrives and induces a ringing/resonant response in a neuron lasting tens of milliseconds, was that spike still really causal to that oscillation?

Let's delve into that last question in more detail: if we generously accept to limit our position that all recorded oscillations are strictly spike-caused, then we can operationalize oscillations in a way that contrast single unit spikes. Namely, oscillations are population dynamics that are due to aggregate activity of neurons, in which the particular identity of the neuron is unimportant, and all that matters is that there is “enough contributions to the wave.” There are then 3 broad possibilities for how spikes map to oscillations (or population dynamics in general, like ERPs or "packets" [(Luczak et al., 2015)][luczak]):

1. __One-to-one__: specific configurations of __spike timing and cellular identity__ will effectively combine to generate a unique oscillation, such that the oscillation can be inversely mapped to the constituent spikes, and thus we can focus just on the spikes to begin with. This realization would deem the aggregate oscillatory signal to be epiphenomenal in the system.

2. __One-to-many__: specific configurations of spike timing and cellular identity can generate many __different__ oscillations under different circumstances, e.g., via short-term synaptic adaptation. Here, it would be important to specify what “different” oscillations would mean, and from whose perspective.

3. __Many-to-one__: different configurations of spike timing and cellular identity can give rise to the __“same”__ recorded oscillation, from the perspective of the downstream spike-field coupled neurons. Here, "same" is most likely in the sense of within acceptable error, and not identical. This effectively serves as a collapse of dimensionality - e.g., 1000 unique neurons reduced to a 2-dimensional limit cycle through projection.

In the "one-to-many" case, the oscillation effectively serves as a “state signal” - a measurement that will tell us something about the current state of the brain - be it structural or historical - over and above what can be (easily) inferred from identified single unit spike timing/rate. In the many-to-one case, the oscillation is simply the output of population coding within the neural dynamical system. If we accept that neurons can relinquish their identity to contribute to a robust population code, and that the population dynamic that makes up the lower-dimensional manifold is ultimately the true object of interest (just check the last 5 years of abstracts at Cosyne ;]), then why would we think otherwise for a population signal that is precisely that, but only oscillatory? If anything, given the existing theoretical tools, we should prefer to study stable behaviors like limit cycles, and possibly strange (chaotic) attractors. So the question is, what type of behavior (motor or otherwise) is well-supported by a limit cycle, keeping in mind that the action potential itself is a trajectory around a limit cycle (see, e.g., [Pandarinath et al., 2018][lfads]).

Without going on too far of a tangent, the point is this: possibilities 2 and 3 both challenge the notion that spikes are the __only__ causal agent in the brain, or that knowing spikes is necessary and sufficient for fully characterizing brain state. In other words, if we recorded all the spikes at this instant, we will still not be able to reconstruct the oscillation (or many other such state signals), and vice versa. Again, without sufficient (or any) evidence that possibility 1 is true, why would we assume it to be, _a priori_?

---

# 3. "Are LFPs exhaust fumes?"
This is a somewhat famous quote, but I'm not sure where it originated from. I'm not even 100% sure what it means, but I take it to question whether LFPs & other field recordings are useful over and above recording the spikes that contribute to generating them. This can refer to LFPs in general, or specific classes of dynamics, such as oscillations. If you're onboard with the above two points I already laid out, then this is a non-question: LFPs are useful because it provides extra information about the state of the system over and above spikes. Case closed.

But if you got to this point and are still staunchly against even the __possibility__ that LFPs/oscillations may provide additional information, then maybe a pragmatic argument could convince you that it's useful to record and analyze them. For one, LFPs have been shown to be correlated with intracellular membrane potential and synaptic currents, especially near times of spiking (e.g., [Atallah et al., 2009][atallah], [Okun et al., 2010][okun], [Haider et al., 2016][haider]). Whether or not membrane potential is an epiphenomenon is up to you, I will just say that it's a hell of a lot easier to stick an electrode somewhere __near__ some cells, than to stick one __into__ a cell, assuming you can accept some loss of signal fidelity. This also gets at the question of whether we can/do have sufficient analytical techniques to actually make sense of the LFP, as its own thing or as a surrogate for membrane voltage/aggregate synaptic currents. If/when we do, it becomes an extremely cheap and efficient way to sample spiking & synaptic activity. Disclosure & shameless self-promotion: I'm totally biased here, because it's a huge part of what we do ([Gao et al., 2017][gao], [Cole et al., 2018][cole]).

A similar argument can be made about the LFP as a surrogate for population spiking activity. High-frequency (broadband) signal power in ECoG is already routinely used as a proxy for local population firing rate changes. Essentially, it's a one-dimensional readout of a (potentially) high-dimensional neural dynamical system in the patch of cortex under the electrode, and it's working pretty well for human cognitive neuroscience (I won't even bother to put citations here, just Google ECoG + high gamma). My current pet theory is that we can stretch this a little further: instead of being 1-D, the LFP can be decoded as a low-(but multi-)dimensional readout, analogous to the output of PCA/[TCA][tca]/[LFADS][lfads]/[etc][dim_red] on population firing rate, but initial results are...not promising.

![][lol]
lol.

Anyway, not only is it currently clinically impossible to get human single-unit recordings with broad coverage, single-units are much less stable in chronic recordings for experiments or brain-computer interface (BCI) usage [(Dickey et al., 2009)][dickey]. The identity of the recorded cell can change within a few days, but LFPs easily sample (the same) volumes of several cubic millimeters that's fairly stable, unless there's physical trauma. The same probably can be said for deep brain stimulation devices. Yes, we can work on shoving as many tetrodes and Neuropixel probes into the brain as possible, and maybe one day, just sprinkle some Neurodust. For real, if I had a wet lab and a shit ton of money, I'd probably try to do that too. But I'd like to use an analogy here: there are two possible locations where some treasure is buried. At one site, the hole is already miles deep and thousands of people are still competing furiously and throwing money into engineering better and more sophisticated tools to dig just incrementally deeper. At the other site, it's basically you, and all you need is a shovel and some math to get started. Oh also, we're pretty sure there is definitely treasure buried at both locations. Only downside is that nobody digging at the other hole cares about what you find (_\*cough\* COSYNE \*cough\*_).

---

# 4. "Are spikes epiphenomenal?"
The main points of this section have already been said [elsewhere][miller], and it boils down to the irrational confidence of our state of knowledge about the brain. For some reason, single-unit action potential holds an epistemologically higher position for a lot of researchers than every other signal in neuroscience, at least when you have access to them. It's certainly not true that it's __only__ because of historical reasons - spikes have been very informative for furthering our understanding of how the brain works, especially in early sensory/motor systems where stimulus/behavior correlates well with single unit and population firing rate. However, to ignore everything else __in favor__ of spikes doesn't make sense, __especially__ since the fullband signal is already recorded. If you don't want to analyze the LFP, ship it our way, or upload it to [CRCNS][crcns] or any other data repository (if you cut your spikes and throw out the raw recording, you have a bigger problem).

Why doesn't ignoring other signals make sense from first principle? A few reasons: first, just because spikes have historically been shown to be useful for decoding and inferring receptive fields, doesn't mean it's the __only__ informative signal. I get that the precedence is very strong here, but that's not really a logical argument. You might argue that recording spikes in an experiment is more cost-efficient because we know they'll probably do __something__ interesting, but again, you already have the fullband signal to start with. Maybe we can hold a competition: everyone gets $X dollars and an hour to drop the same number of wires into the rat hippocampus, and whoever can decode place most accurately wins the competition. This means you're not turning the wires until you can find a place cell, or any cells. See [Agarwal et al., 2014][agarwal].

Second - subscribing to the cortical computation framework momentarily - there's no reason to believe __a priori__ that spikes are doing the heavy-lifting in a computational sense. You could argue that spikes are "encoding", in that they are literally the messages transmitted between neurons, such that they encode and communicate the result of some computation. But spikes __do not__ compute! The cells "compute", dendrites "compute", the axon hillock "computes". In that sense, __spikes are epiphenomenal__: they are the secondary consequences of dendritic computation, of which you can fully infer by knowing the incoming synaptic inputs and biophysical properties of the neuron. Spikes are the exhaust fumes of synaptic integration.

Finally, as I alluded to before, it's unclear what "cause" and "effect" refer to in the causal system we are studying. Actually, there's probably no true answer to this since it's dependent on our perspective, agreed upon by the community as a whole. Typically, we assume that spikes are causal to behavior, and presumably, to internal (invisible) cognition as well. However, this is an axiom, not a fact. In other words, spikes were chosen by us - neuroscientists - to be the precise level of causal interaction, and it's unclear whether this was ever, or can be, explicitly tested. One can imagine going lower, pegging synapses or even individual channels as the "causal" agent, and one wouldn't be wrong. Just as one example, synapses are [probabilistic][prob_syn]. Hence, action potentials do not reliably trigger the same downstream effects, but neurotransmitter release does.

On the other hand, "effect" is just as ill-defined explicitly. One could make the argument that outward behavior is ultimately what matters, and firing rate directly influences the efferent muscle fibers, hence spikes are causal to behavior. However, even putting aside the same counterpoint regarding probabilistic synapses, other (non-nervous system) factors contribute to the specific action of the muscle itself given the same spiking input. Just because neuroscientists study the nervous system, doesn't mean we should ignore causes that are non-neuronal. Besides, the entire subfield of cognitive neuroscience is dedicated to studying (mostly) non-motor behavior, and it's not inconceivable that cognition arises from emergent phenomena that cannot be linearly decomposed into spikes from neurons. Not saying that's true, the point simply is that we don't know.

___

So, what do the above arguments convey? At the bare minimum, I hope that they challenged the position that spikes are the only causal/important signals in the brain, derived from first principles and existing empirical evidence. If it really grinds your gears, you should set out to prove that the converse is true, that LFPs do not provide information additional to spikes - that would be extremely useful too to have experimental confirmation.

Practically, I hope more people start to look at the relationship between LFPs/oscillations and spikes, as well as behavior, to see what information overlap exists between these signals, and how they may be uniquely informative. If you're recording spikes, there's really no reason to not save and look at the LFPs - it's literally free information for you to mine with the data you already have.

Or, you know, don't. That probably contributes to my job security for the next little while.

<iframe width="560" height="315" src="https://www.youtube.com/embed/211D6KOAzIQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/211D6KOAzIQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

[ctc]:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4605134/
[cardin]: http://www.jneurosci.org/content/36/41/10496
[sohal]:http://www.jneurosci.org/content/36/41/10489
[sci_am]:https://www.scientificamerican.com/article/do-brain-waves-conduct-neural-activity-like-a-symphony/
[miller]:http://ekmillerlab.mit.edu/2018/11/29/a-controversy-about-whether-brain-waves-play-a-functional-role/
[osc_tweet]:https://twitter.com/_rdgao/status/1068214736045522945
[okun]:https://www.ncbi.nlm.nih.gov/pubmed/20335480
[haider]:https://www.ncbi.nlm.nih.gov/pubmed/27021173
[buzsaki]:https://www.ncbi.nlm.nih.gov/pubmed/22595786
[wiki_eph]:https://en.wikipedia.org/wiki/Ephaptic_coupling
[fly_olf]:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3518700/
[rod_cer]:https://www.ncbi.nlm.nih.gov/pubmed/30293822
[ephaptic]:https://www.ncbi.nlm.nih.gov/pubmed/21240273
[endogenous]:https://www.ncbi.nlm.nih.gov/pubmed/20624597
[ephaptic_glial]:https://www.ncbi.nlm.nih.gov/pubmed/28793233
[luczak]:https://www.ncbi.nlm.nih.gov/pubmed/26507295
[lfads]:https://www.ncbi.nlm.nih.gov/pubmed/30224673
[atallah]:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702525/
[cole]:https://www.biorxiv.org/content/early/2018/10/25/452987
[gao]:https://www.ncbi.nlm.nih.gov/pubmed/28676297
[tca]:https://www.ncbi.nlm.nih.gov/pubmed/29887338
[dim_red]:https://www.ncbi.nlm.nih.gov/pubmed/25151264
[dickey]:https://www.ncbi.nlm.nih.gov/pubmed/19535480
[crcns]:https://crcns.org/data-sets
[agarwal]:https://www.ncbi.nlm.nih.gov/pubmed/24812401
[prob_syn]:https://www.ncbi.nlm.nih.gov/pubmed/19377502

[webster]:/assets/images/blog/2019-01-02-webster.png
[lol]:/assets/images/blog/2019-01-02-trajectory.jpg

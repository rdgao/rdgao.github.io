---
title: "Research"
layout: single
permalink: /research/

author_profile: True
read_time: false
share: false
classes: wide

toc: true
toc_label: "Research Areas"
toc_icon: "space-shuttle"

gallery_overview:
  - url: /assets/images/projects/automind1.png
    image_path: /assets/images/projects/resized/automind1.png
  - url: /assets/images/projects/gbi1.png
    image_path: /assets/images/projects/resized/gbi1.png
  - url: /assets/images/projects/nfp5.png
    image_path: /assets/images/projects/resized/nfp5.png
  
gallery_automind:
  - url: /assets/images/projects/automind1.png
    image_path: /assets/images/projects/resized/automind1.png
  - url: /assets/images/projects/automind2.png
    image_path: /assets/images/projects/resized/automind2.png
  - url: /assets/images/projects/automind3.png
    image_path: /assets/images/projects/resized/automind3.png

gallery_ai4n:
  - url: /assets/images/projects/gbi1.png
    image_path: /assets/images/projects/resized/gbi1.png
  - url: /assets/images/projects/ai4n3.png
    image_path: /assets/images/projects/resized/ai4n3.png
  - url: /assets/images/projects/ai4n2.png
    image_path: /assets/images/projects/resized/ai4n2.png

gallery_nfp:
  - url: /assets/images/projects/nfp5.png
    image_path: /assets/images/projects/resized/nfp5.png
  - url: /assets/images/projects/nfp3.png
    image_path: /assets/images/projects/resized/nfp3.png
  - url: /assets/images/projects/org3.png
    image_path: /assets/images/projects/resized/org3.png

gallery_meta:
  - url: /assets/images/projects/meta1.png
    image_path: /assets/images/projects/resized/meta1.png
  - url: /assets/images/projects/meta2.png
    image_path: /assets/images/projects/resized/meta2.png
  - url: /assets/images/projects/meta3.png
    image_path: /assets/images/projects/resized/meta3.png
---
# Overview
My work is motivated by the intersection of a few questions:
- **What can brain signals tell us** about the cellular and network properties of the underlying neural circuits, and how do they relate to brain function, disorders, cognition, and behavior?
- **How do we leverage computational methods** from data science and machine learning to address those questions, for all kinds of different signals from different organisms?
- **How can we define things more precisely** to effectively facilitate scientific communication and progress?

{% include gallery id="gallery_overview" %}
**On the methodological side**, in addition to "general-purpose" data analysis and machine learning workflows, I know how to do a few things relatively well, like:
- turning complicated time series into sines and cosines (**spectral analysis**),
- turning complicated high-dimensional distributions into Gaussians (**probabilistic machine learning**), 
- and making realistic-looking fake data (**generative models and computational simulations**).

**On the neuroscience side**, I'm interested in "how the brain works" across different scales in time and space, and especially in connecting brain dynamics to structure and behavior. 

Below are representative examples of my research projects in computational neuroscience and cognitive science. Code and papers are included wherever possible. You can find all of them on [Google Scholar][g_scholar], [GitHub][gh_rgao], or my [CV][cv].

---

# Inverse modeling of neural circuits

In physical sciences, we build "mechanistic models" of phenomena we're interested in and can simulate on the computer. Often, the goal is to find parameter values of the model that reproduces the experimental data you observe. This is known as *inverse modeling*, *data assimilation*, *parameter inference*, etc. The result is an *in silico* replica of the real system, which allows you to do things like infer quantities you cannot observe or test hypothetical interventions. 

{% include gallery id="gallery_automind" %}

In a number of works, I build models of neural population activity and then try to work backwards to infer variables about the underlying circuit from recordings of brain signals. The models vary in complexity, sometimes requiring more involved inference methods, such as simulation-based inference with conditional neural density estimators.

<!-- **Why**: Features of the neural population dynamics, like oscillations and asynchronous activity, are routinely used in systems and cognitive neuroscience as biomarkers of behavior, cognition, and disease, yet we have very little idea about how these mesoscale population-level signals come about. Personally, rather than just measuring them, I think having a theory-driven forward model of the signals we use would help us in better linking them with the behavioral variables we're ultimately interested in. -->

**Deep inverse modeling reveals dynamic-dependent invariances in neural circuit mechanisms (2024)**\
***RG**, Deistler, M., Schulz, A., Gonçalves, P. J., Macke, J. H.*\
<a href='https://www.biorxiv.org/content/10.1101/2024.08.21.608969v2' class='btn btn--success'>Paper</a>
<a href='https://github.com/mackelab/automind' class='btn btn--info'>Code</a>

**Inferring synaptic excitation-inhibition balance from field potentials (2017)**\
***RG**, Peterson, E. J., Voytek, B.*\
<a href='https://www.ncbi.nlm.nih.gov/pubmed/28676297' class='btn btn--success'>Paper</a>
<a href='https://github.com/voytekresearch/EISlope' class='btn btn--info'>Code</a>
<a href='/first-research-paper-published/' class='btn btn--danger'>Blog Post</a>

---
# Machine learning and AI for (neuro)science

Modern deep learning-based probabilistic ML algorithms are great at learning from noisy data---both real and fake---to produce high-quality synthetic samples (i.e., emulation). I'm interested in leveraging them in two main ways:

{% include gallery id="gallery_ai4n" %}

First, deep learning modules can be trained on simulated data from mechanistic models and "plugged into" novel probablistic algorithms for inference, e.g., in the context of simulation-based inference. Second, generative models can be made to mimic real experimental recordings in a supervision-free manner, and later be used for a variety of applications, e.g., simulation / emulation, forecasting, denoising, data augmentation for downstream tasks, etc.

**Generalized Bayesian inference for scientific simulators via amortized cost estimation (2024)**\
***RG**\*, Deistler, M.\*, Macke, J. H.*\
<a href='https://proceedings.neurips.cc/paper_files/paper/2023/hash/fdd565f63f49776bef620e0ce368a492-Abstract-Conference.html' class='btn btn--success'>Paper</a>
<a href='https://github.com/mackelab/neuralgbi' class='btn btn--info'>Code</a>

**Generating realistic neurophysiological time series with denoising diffusion probabilistic models (2024)**\
*Vetter, J., Macke, J. H.+, **RG**+*\
<a href='https://linkinghub.elsevier.com/retrieve/pii/S2666389924001892' class='btn btn--success'>Paper</a>
<a href='https://github.com/mackelab/neural_timeseries_diffusion' class='btn btn--info'>Code</a>

**Latent Diffusion for Neural Spiking Data (2024)**\
*Kapoor, J.\*, Schulz, A.\*, Vetter, J., Pei, F., **RG**+, Macke, J. H.+*\
<a href='https://arxiv.org/abs/2407.08751' class='btn btn--success'>Paper</a>

---
# Neural data science and time series analysis

There are tons of different kinds of measurements we can make from the brain, producing large databases of multi-modal data that provide us with different perspectives into brain structure, dynamics, function, and development.

{% include gallery id="gallery_nfp" %}

I typically analyze electrophysiological time series (e.g., EEG, ECoG, LFP, spiking) as the starting point to derive novel, informative features, with a special emphasis on aperiodic and oscillatory patterns. They can then be related to measurements of other modalities, such as structural imaging, gene expression, and behavior. I work with data from any and all model organisms, including humans, non-human primates, rodents, and brain organoids.

**Neural timescales from a computational perspective (2024)**\
*Zeraati, R.\*, Levina, A., Macke, J. H., **RG**\**\
<a href='https://arxiv.org/abs/2409.02684' class='btn btn--success'>Paper</a>

**Neuronal timescales are functionally dynamic and shaped by cortical microarchitecture (2020)**\
***RG**, van den Brink, RL., Pfeffer, T., Voytek, B.*\
<a href='https://elifesciences.org/articles/61277' class='btn btn--success'>Paper</a>
<a href='https://github.com/rdgao/field-echos/' class='btn btn--info'>Code</a>


**Complex oscillatory waves emerging from cortical organoids model early human brain network development (2019)**\
Trujillo, C. A.\*, **RG**\*, Negraes, PD.\*, [...] Voytek, B.+, Muotri, AR.+\
<a href='https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(19)30337-6' class='btn btn--success'>Paper</a>
<a href='https://github.com/voytekresearch/OscillatoryOrganoids' class='btn btn--info'>Code</a>
<a href='/oscillating-organoids/' class='btn btn--danger'>Blog Post</a>

**NeuroDSP: A package for neural digital signal processing (2019)**\
*Cole, S., Donoghue, T., **RG**, Voytek, B.*\
<a href='https://joss.theoj.org/papers/10.21105/joss.01272' class='btn btn--success'>Paper</a>
<a href='https://github.com/neurodsp-tools/neurodsp' class='btn btn--info'>Code</a>


---
# (Re)defining cognition, and (automated) metascience
Science is a social construct. This does not mean that our discoveries are any less real or factual, but that we're constantly working towards some kind of agreement. A necessary but messy component of this negotiation process is language and conceptual terminology: *Do you mean the same thing as me when we say "X"?*

{% include gallery id="gallery_meta" %}

I'm really interested in how concepts evolve over time and can mean different things for different people, and I happen to get into "semantic debates" semi-regularly. Of particular interest to me are conceptual definitions surrounding neural dynamics, as well as processes of cognition (inspired by the [Cognitive Atlas][cog_atlas]).

**Decoupling Measurements and Processes: On the Epiphenomenon Debate Surrounding Brain Oscillations in Field Potentials (2024)**\
*van Bree, S.\*, Levenstein, D., Krause, MR., Voytek, B., **RG**\**\
<a href='https://osf.io/preprints/psyarxiv/knjfw' class='btn btn--success'>Paper</a>

**What happened to cognitive science? (2019)**\
*Núñez, R., Allen, M.\*, **RG**\*, Miller Rigoli, C.\*, Relaford-Doyle, J.\*, Semenuks, A.\**\
<a href='https://www.nature.com/articles/s41562-019-0626-2' class='btn btn--success'>Paper</a>
<a href='https://github.com/rdgao/WH2CogSci' class='btn btn--info'>Code</a>

**Automated generation of cognitive ontology via web text-mining (2017)**\
***RG**, Donoghue, T., Voytek, B.*\
<a href='https://drive.google.com/file/d/1DrRsczm4CqP4_XbEcPOssXjPE7Y48vef/view' class='btn btn--success'>Paper</a>
<a href='https://github.com/voytekresearch/IdentityCrisis' class='btn btn--info'>Code</a>


---
# PhD Dissertation
You can find my full thesis [here][thesis], and the defense talk is available on [YouTube][yt_defense], thanks to the pandemic. This summarizes my PhD work (2014-2020).

<iframe width="560" height="315" src="https://www.youtube.com/embed/zqmZkZOxguc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


[yt_defense]:https://www.youtube.com/watch?v=zqmZkZOxguc
[thesis]:/assets/docs/paper_pdfs/thesis_final.pdf
[g_scholar]:https://scholar.google.com/citations?user=a2o9IKYAAAAJ
[cog_atlas]:http://www.cognitiveatlas.org/
[neurosynth]:http://neurosynth.org/

[cv]: /assets/docs/cv.pdf
[gh_rgao]: https://github.com/rdgao
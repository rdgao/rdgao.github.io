---
title: "Projects"
layout: single
permalink: /projects/

author_profile: True
read_time: false
share: false
classes: wide

gallery_NFP:
  - url: /assets/images/projects/nfp0.png
    image_path: /assets/images/projects/thumbnail/nfp0.png
  - url: /assets/images/projects/nfp1.png
    image_path: /assets/images/projects/thumbnail/nfp1.png
  - url: /assets/images/projects/nfp2.png
    image_path: /assets/images/projects/thumbnail/nfp2.png

gallery_ORG:
  - url: /assets/images/projects/org0.png
    image_path: /assets/images/projects/thumbnail/org0.png
  - url: /assets/images/projects/org1.png
    image_path: /assets/images/projects/thumbnail/org1.png
  - url: /assets/images/projects/org2.png
    image_path: /assets/images/projects/thumbnail/org2.png

gallery_COG:
  - url: /assets/images/projects/cog0.png
    image_path: /assets/images/projects/thumbnail/cog0.png
  - url: /assets/images/projects/cog1.png
    image_path: /assets/images/projects/thumbnail/cog1.png
  - url: /assets/images/projects/cog2.png
    image_path: /assets/images/projects/thumbnail/cog2.png
---
Collected below are projects for my own PhD research in computational and cognitive (neuro)science, stuff I contribute to, as well as some fun personal projects. Associated code and papers are included wherever possible. You can find all of them on [Google Scholar][0].

---
# Modeling and Decomposing Neural Field Potentials
**What**: In this set of works, I build computational models of neural field potentials (e.g., [ECoG](https://en.wikipedia.org/wiki/Electrocorticography)) from populations of neurons, and then try to work backwards and infer variables about the neural population from both simulated and experimental field potential recordings.
{% include gallery id="gallery_NFP" %}
**Why**: Features of the neural field potentials, such as oscillations and asynchronous activity, are routinely used in cognitive neuroscience as biomarkers of behavior, cognition, and disease, yet we have very little idea about how these mesoscale population-level signals come about. Personally, rather than just measuring them, I think having a theory-driven forward model of the signals we use would help us in better linking them with the behavioral variables we're ultimately interested in.

### Measuring Asynchronous (Stochastic) Population Firing (on-going)
<a href='https://github.com/voytekresearch/spectralCV' class='btn btn--info'>GitHub</a>

### Inferring Synaptic Excitation-Inhibition Balance (2017)
<a href='https://github.com/voytekresearch/EISlope' class='btn btn--info'>GitHub</a>
<a href='https://www.ncbi.nlm.nih.gov/pubmed/28676297' class='btn btn--success'>Paper</a>
<a href='/2017-9-18-2552-first-research-paper-published/' class='btn btn--danger'>Blog Post</a>
### Relating Spectral Power Law Changes to Population Firing Rate (2016)
<a href='https://github.com/voytekresearch/tutorials/blob/master/PowerLawPSD.ipynb' class='btn btn--info'>GitHub</a>
<a href='https://www.physiology.org/doi/abs/10.1152/jn.00722.2015' class='btn btn--success'>Paper</a>
<a href='http://voyteklab.com/interpreting-the-electrophysiological-power-spectrum/' class='btn btn--danger'>Blog Post</a>

<a href='https://fakeneurons.shinyapps.io/anotb/anotb.Rmd' class='btn btn--info'>App</a>  *beautiful shiny.io app courtesy of [Erik Peterson][1]*

---
# Development of Network Activity in Brain Organoids
**What**: Collaborating with the [Muotri Lab][2] at UCSD, we (read: they) have developed human induced pluripotent stem cell (hiPSC)-derived brain organoids that display spontaneous and oscillatory network activity over a long developmental period. My role has since been to analyze the electrophysiological data (spiking and LFP) to characterize the developmental trajectory of network activity and relating it to structural and molecular variables, as well as unexpectedly learning a lot about electrical activity-dependent neurodevelopment *in-vivo*.
{% include gallery id="gallery_ORG" %}
**Why**:
Figuring out how neurons in the brain organize themselves over time, both structurally and dynamically, is one of the biggest ongoing challenges in systems and cognitive neuroscience. Brain organoids have recently emerged as a great model for neurodevelopment, having been shown to mimic *in-vivo* neurodevelopment structurally and in gene expression. By also tracking the emergence of network **dynamics** over time, as well as continuing to engineer models with higher fidelity, I'm hoping we can dissect how neural circuits organize themselves from the moment neurodevelopment begins, and learn when and how it goes wrong in diseases.

### Nested Oscillatory Network Dynamics in Human Cortical Organoids (preprint)
<a href='https://github.com/voytekresearch/OscillatoryOrganoids' class='btn btn--info'>GitHub</a>
<a href='https://www.biorxiv.org/content/early/2018/06/29/358622' class='btn btn--success'>Paper</a>

(repo contains code for preprocessing Axion Maestro multi-electrode array data.)

---
# Defining "Cognition" and "Cognitive Processes"
**What**: This hacked-up project that first took a week to implement has turned into a full ideological commitment. I scraped from scientific publications usages of "cognitive processes" words, like 'attention' and 'memory', and compare 1) which of these cognitive processes are similar, at least from the (crude) perspective of how scientists use them, and 2) how cognitive scientists and neuroscientists use them differently.
{% include gallery id="gallery_COG" %}
**Why**:
Much of cognitive science and cognitive neuroscience aim to characterize and understand "cognitive processes" - processes of the mind that are internal to the organism. Going into my PhD as a freshly minted engineer, it bothered me to no end that there were very few concrete and non-circular definitions for these processes. Precisely because they are internal processes, definitions are hard to pin down, so I took a behaviorist approach and looked at how cognitive scientists and neuroscientists use them in relation to each other in practice - sometimes using the same words to mean very different things - by generating a data-driven ontology scrapped from scientific abstracts. Inspired by [Cognitive Atlas][3], [Neurosynth][4], [ERP-SCANR][5], and [BrainSCANR][6].

### Automated Generation of Cognitive Ontology via Web Text-Mining
<a href='https://github.com/voytekresearch/IdentityCrisis' class='btn btn--info'>GitHub</a>
<a href='https://mindmodeling.org/cogsci2017/papers/0395/paper0395.pdf' class='btn btn--success'>Paper</a>

---
# Other Science Projects
### Parameterizing Neural Power Spectra - Fitting Oscillatory Peaks and 1/f background (FOOOF).
<a href='https://github.com/voytekresearch/fooof' class='btn btn--info'>GitHub</a>
<a href='https://www.biorxiv.org/content/biorxiv/early/2018/04/11/299859.full.pdf' class='btn btn--success'>Paper</a>
### neurodsp - Toolbox for Analyzing Time Series Data in Neuroscience
<a href='https://github.com/voytekresearch/neurodsp' class='btn btn--info'>GitHub</a>

[0]:https://scholar.google.com/citations?user=a2o9IKYAAAAJ
[1]:https://twitter.com/parenthetical_e
[2]:https://medschool.ucsd.edu/som/pediatrics/research/labs/muotri-lab/Pages/default.aspx
[3]:http://www.cognitiveatlas.org/
[4]:http://neurosynth.org/
[5]:http://tomdonoghue.github.io/ERP_SCANR/
[6]:http://blog.brainscanr.com/

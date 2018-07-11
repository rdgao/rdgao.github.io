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
    image_path: /assets/images/projects/thumbnail/tn_nfp0.png
  - url: /assets/images/projects/nfp1.png
    image_path: /assets/images/projects/thumbnail/tn_nfp1.png
  - url: /assets/images/projects/nfp2.png
    image_path: /assets/images/projects/thumbnail/tn_nfp2.png

gallery_ORG:
  - url: /assets/images/projects/org0.png
    image_path: /assets/images/projects/thumbnail/tn_org0.png
  - url: /assets/images/projects/org1.png
    image_path: /assets/images/projects/thumbnail/tn_org1.png
  - url: /assets/images/projects/org2.png
    image_path: /assets/images/projects/thumbnail/tn_org2.png
---
Collected below are projects for my own PhD research in computational and cognitive (neuro)science, stuff I contribute to, as well as some fun personal projects. Associated code and papers are included wherever possible.

---
# Modeling and Decomposing Neural Field Potentials
**What**: In this set of works, I build computational models of neural field potentials (e.g., [ECoG](https://en.wikipedia.org/wiki/Electrocorticography)) from populations of neurons, and then try to work backwards and infer variables about the neural population from both simulated and experimental field potential recordings. This has been half the bulk of my PhD work.
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
**What**: Collaborating with the [Muotri Lab][2] at UCSD, we (read: they) have developed human induced pluripotent stem cell (hiPSC) derived brain organoids that display spontaneous and oscillatory network activity over a long developmental period. My role has since been to analyze the electrophysiological data (spiking and LFP) to characterize the developmental trajectory of network activity and relating it to other variables, as well as unexpectedly learning a lot about electrical activity-dependent neurodevelopment *in-vivo*.
{% include gallery id="gallery_ORG" %}
**Why**:
It was a huge surprise for both labs when we saw that the organoids exhibited nested oscillatory dynamics that went from regular to irregular
### Nested Oscillatory Network Dynamics in Human Cortical Organoids (preprint)
<a href='https://github.com/voytekresearch/OscillatoryOrganoids' class='btn btn--info'>GitHub</a>
<a href='https://www.biorxiv.org/content/early/2018/06/29/358622' class='btn btn--success'>Paper</a>

(linked repo contains code for preprocessing Axion Maestro multi-electrode array data.)

---
# Defining "Cognition" and "Cognitive Processes"

---
# Non-linear Dynamical Systems Analysis of Neural Signals

[1]:https://twitter.com/parenthetical_e
[2]:https://medschool.ucsd.edu/som/pediatrics/research/labs/muotri-lab/Pages/default.aspx

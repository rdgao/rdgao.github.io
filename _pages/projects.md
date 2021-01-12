---
title: "projects"
layout: single
permalink: /projects/

author_profile: True
read_time: false
share: false
classes: wide

gallery_NFP:
  - url: /assets/images/projects/nfp1.png
    image_path: /assets/images/projects/thumbnail/nfp1.png
  - url: /assets/images/projects/nfp4.png
    image_path: /assets/images/projects/thumbnail/nfp4.png
  - url: /assets/images/projects/nfp3.png
    image_path: /assets/images/projects/thumbnail/nfp3.png

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
Collected below are projects for my own PhD research in computational neuroscience and cognitive science, stuff I contribute to, as well as some fun personal projects. Associated code and papers are included wherever possible. You can find all of them on [Google Scholar][g_scholar].

---
# dissertation
You can find my full thesis [here][thesis], and the defense talk is available on [YouTube][yt_defense], thanks to the pandemic. This pretty much summarizes most of the works listed below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zqmZkZOxguc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---
# topic: decomposing neural field potentials
**what**: In this set of works, I build computational models of neural field potentials (e.g., [ECoG](https://en.wikipedia.org/wiki/Electrocorticography)) from populations of neurons, and then try to work backwards and infer variables about the neural population from both simulated and experimental field potential recordings.
{% include gallery id="gallery_NFP" %}
**why**: Features of the neural field potentials, such as oscillations and asynchronous activity, are routinely used in cognitive neuroscience as biomarkers of behavior, cognition, and disease, yet we have very little idea about how these mesoscale population-level signals come about. Personally, rather than just measuring them, I think having a theory-driven forward model of the signals we use would help us in better linking them with the behavioral variables we're ultimately interested in.

### measuring neuronal timescales across human cortex (2020)
<a href='https://github.com/rdgao/field-echos/' class='btn btn--info'>GitHub</a>
<a href='https://elifesciences.org/articles/61277' class='btn btn--success'>Paper</a>

### measuring asynchronous (stochastic) population firing (on-going)
<a href='https://github.com/voytekresearch/spectralCA' class='btn btn--info'>GitHub</a>
<a href='/assets/docs/paper_pdfs/gao_ccn2018.pdf' class='btn btn--success'>Paper</a>

### inferring synaptic excitation-inhibition balance (2017)
<a href='https://github.com/voytekresearch/EISlope' class='btn btn--info'>GitHub</a>
<a href='https://www.ncbi.nlm.nih.gov/pubmed/28676297' class='btn btn--success'>Paper</a>
<a href='/first-research-paper-published/' class='btn btn--danger'>Blog Post</a>

### relating spectral power law changes to population firing rate (2016)
<a href='https://github.com/voytekresearch/tutorials/blob/master/PowerLawPSD.ipynb' class='btn btn--info'>GitHub</a>
<a href='https://www.physiology.org/doi/abs/10.1152/jn.00722.2015' class='btn btn--success'>Paper</a>
<a href='http://voyteklab.com/interpreting-the-electrophysiological-power-spectrum/' class='btn btn--danger'>Blog Post</a>

<a href='https://fakeneurons.shinyapps.io/anotb/anotb.Rmd' class='btn btn--info'>App</a>  *beautiful shiny.io app courtesy of [Erik Peterson][e_peterson]*

---
# topic: development of network activity in brain organoids
**what**: Collaborating with the [Muotri Lab][muotri_lab] at UCSD, we (read: they) have developed human induced pluripotent stem cell (hiPSC)-derived brain organoids that display spontaneous and oscillatory network activity over a long developmental period. My role has since been to analyze the electrophysiological data (spiking and LFP) to characterize the developmental trajectory of network activity and relating it to structural and molecular variables, as well as unexpectedly learning a lot about electrical activity-dependent neurodevelopment *in-vivo*.
{% include gallery id="gallery_ORG" %}
**why**:
Figuring out how neurons in the brain organize themselves over time, both structurally and dynamically, is one of the biggest ongoing challenges in systems and cognitive neuroscience. Brain organoids have recently emerged as a great model for neurodevelopment, having been shown to mimic *in-vivo* neurodevelopment structurally and in gene expression. By also tracking the emergence of network **dynamics** over time, as well as continuing to engineer models with higher fidelity, I'm hoping we can dissect how neural circuits organize themselves from the moment neurodevelopment begins, and learn when and how it goes wrong in diseases.

### complex oscillatory waves emerging from cortical organoids model early human brain network development
<a href='https://github.com/voytekresearch/OscillatoryOrganoids' class='btn btn--info'>GitHub</a>
<a href='https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(19)30337-6' class='btn btn--success'>Paper</a>
<a href='/oscillating-organoids/' class='btn btn--danger'>Blog Post</a>

(repo contains code for preprocessing Axion Maestro multi-electrode array data.)

---
# topic: defining "cognition"
**what**: This hacked-up project that first took a week to implement has turned into a full ideological commitment. I scraped from scientific publications usages of "cognitive processes" words, like 'attention' and 'memory', and compare 1) which of these cognitive processes are similar, at least from the (crude) perspective of how scientists use them, and 2) how cognitive scientists and neuroscientists use them differently.
{% include gallery id="gallery_COG" %}
**why**:
Much of cognitive science and cognitive neuroscience aim to characterize and understand "cognitive processes" - processes of the mind that are internal to the organism. Going into my PhD as a freshly minted engineer, it bothered me to no end that there were very few concrete and non-circular definitions for these processes. Precisely because they are internal processes, definitions are hard to pin down, so I took a behaviorist approach and looked at how cognitive scientists and neuroscientists use them in relation to each other in practice - sometimes using the same words to mean very different things - by generating a data-driven ontology scrapped from scientific abstracts. Inspired by [Cognitive Atlas][cog_atlas], [Neurosynth][neurosynth], [ERP-SCANR][erp_scanr], and [BrainSCANR][brain_scanr].

### automated generation of cognitive ontology via web text-mining
<a href='https://github.com/voytekresearch/IdentityCrisis' class='btn btn--info'>GitHub</a>
<a href='/assets/docs/paper_pdfs/Gao2019_CCN.pdf' class='btn btn--success'>Paper</a>

---
# other science projects
### what happened to cognitive science?
<a href='https://github.com/voytekresearch/fooof' class='btn btn--info'>GitHub</a>
<a href='https://www.nature.com/articles/s41562-019-0626-2' class='btn btn--success'>Paper</a>

### parameterizing neural power spectra
<a href='https://fooof-tools.github.io/fooof/' class='btn btn--info'>GitHub</a>
<a href='https://www.nature.com/articles/s41593-020-00744-x' class='btn btn--success'>Paper</a>

### neurodsp - toolbox for analyzing time series data in neuroscience
<a href='https://github.com/neurodsp-tools/neurodsp' class='btn btn--info'>GitHub</a>
<a href='https://joss.theoj.org/papers/10.21105/joss.01272' class='btn btn--success'>Paper</a>

[yt_defense]:https://www.youtube.com/watch?v=zqmZkZOxguc
[thesis]:/assets/docs/paper_pdfs/thesis_final.pdf
[g_scholar]:https://scholar.google.com/citations?user=a2o9IKYAAAAJ
[e_peterson]:https://twitter.com/parenthetical_e
[muotri_lab]:https://medschool.ucsd.edu/som/pediatrics/research/labs/muotri-lab/Pages/default.aspx
[cog_atlas]:http://www.cognitiveatlas.org/
[neurosynth]:http://neurosynth.org/
[erp_scanr]:http://tomdonoghue.github.io/ERP_SCANR/
[brain_scanr]:http://blog.brainscanr.com/

---
created: 2026-04-27
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/woodman-2014.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/semanticscholar-f45e6044c92f.md
- raw/papers/semanticscholar-4d73a30d5c84.md
tags:
- software-eeglab
title: EEGLAB
type: entity
updated: '2026-05-18'
---

EEGLAB is a neuroimaging platform for electroencephalography (EEG) and magnetoencephalography (MEG) data analysis, interoperating with Brainstorm and FieldTrip within the [[neuroimaging-eeg]] and [[neuroimaging-meg]] software ecosystem [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. As a cornerstone environment in [[computational-neuroscience]] workflows, it processes empirical electrophysiological recordings that serve as inputs to larger modeling and simulation frameworks. MLE-Toolbox, a comprehensive open-source MATLAB toolbox for end-to-end MEG/EEG analysis inspired by widely used neuroimaging platforms, provides native interoperability with EEGLAB alongside Brainstorm and FieldTrip, allowing researchers to build on established workflows while incorporating automated artifact rejection, source localization, and network analysis methods [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. In [[connectome]]-based whole-brain modeling, EEG and MEG signals furnish the empirical data that simulation platforms such as [[the-virtual-brain]] seek to reproduce through forward models, enabling direct comparison between simulated and observed brain activity [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. This interplay between empirical electrophysiological analysis and computational simulation positions EEGLAB as a node in the toolchain linking recorded brain dynamics to network-level modeling.

## Key Features

* Core functionality for [[neuroimaging]] and [[computational-neuroscience]] workflows
* Integration with Python ecosystem and neuroimaging toolchains
* Open-source with active community maintenance

## Relationship to Whole-Brain Modeling

EEGLAB is often used alongside [[tvb]] and other simulation platforms in pre-processing or post-processing pipelines for [[connectome]]-based brain modeling.

## Related Software
* Antspy
* [[arbor]]
* [[bids]] Validator
* Bidscoin
* [[brainstorm]]
* [[eegnet]]
* [[labstreaminglayer]]
* [[limo]]

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f))
2. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain [[connectivity]]*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))
3. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
4. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072))
5. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2026). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research.*. [[brain-stimulation]]. [DOI](https://doi.org/10.1016/j.brs.2025.103016))
6. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo [[fmri]] denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198))

## ORPHAN PAGE CONTEXT (limo)
---
created: 2025-01-15
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/sanz-leon-2013.md
- raw/papers/woodman-2014.md
tags:
- software-modeling
- [[neuroimaging-eeg]]
- [[neuroimaging-meg]]
- statistical-analysis
- eeglab
title: Limo
type: entity
updated: '2026-05-04'
---

# Limo

## Overview

Limo ([[linear]] Modeling) is a MATLAB-based toolbox for the statistical analysis of electroencephalography (EEG) and magnetoencephalography (MEG) data. The toolbox implements mass univariate linear modeli
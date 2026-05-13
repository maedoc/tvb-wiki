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
updated: '2026-05-13'
---

EEGLAB is an open-source MATLAB toolbox for processing and analyzing electroencephalography ([[eeg]]) data that has become a standard platform for EEG preprocessing and independent component analysis ([[ica]]) [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. Originally introduced by Delorme and Makeig, the toolbox provides a graphical user interface and scripting environment for data import, filtering, artifact rejection, event-related potential analysis, and spectral decomposition [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. Its analysis conventions are widely adopted: researchers routinely follow EEGLAB guidelines for preprocessing resting-state and task-based recordings [[raw/papers/semanticscholar-93016091487b.md|Eroğlu (2025)]], and the toolbox is considered a gold-standard environment alongside [[mne-python]] and [[fmriprep]] in the broader neuroimaging community [[raw/papers/semanticscholar-8006c459587d.md|Schwartz et al. (2025)]]. EEGLAB interoperates natively with established platforms such as [[brainstorm]] and [[freesurfer]], allowing researchers to leverage existing workflows while exchanging data through standardized structures [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. The toolbox is also distributed as a core electrophysiology component within containerized neuroimaging suites, supporting reproducible analysis across workstations and high-performance computing environments [[raw/papers/Renton2024.md|Renton et al. (2024)]]. Clinical and cognitive studies employ EEGLAB for microstate analysis, [[functional-connectivity]] estimation, and spectral power mapping [[raw/papers/semanticscholar-c8ef0398ea18.md|Yang et al. (2025)]]; [[raw/papers/semanticscholar-0175970c7639.md|Avital et al. (2025)]], while downstream packages such as [[limo]] and PSGpower build on its algorithms for specialized statistical and sleep-science applications [[raw/papers/semanticscholar-41c14ba9b00d.md|Fitzroy et al. (2025)]].

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
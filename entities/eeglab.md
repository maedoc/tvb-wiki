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

EEGLAB is an open-source MATLAB toolbox that has become the standard for EEG preprocessing and independent component analysis ([[ica]]) within the [[neuroimaging]] software ecosystem [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. Originally introduced by Delorme & Makeig (2004) as a platform for analysis of single-trial EEG dynamics, it furnishes core capabilities for data import, ICA-based artifact decomposition, event-related potential (ERP) analysis, and structured preprocessing workflows that inform downstream modeling pipelines [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. The toolbox natively supports the .set/.fdt data format and is integrated into broader MATLAB-based neuroimaging environments alongside platforms such as [[brainstorm]] and [[freesurfer]], enabling researchers to leverage established workflows while benefiting from additional automation and analysis modules [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. In [[connectome]]-based whole-brain modeling, empirical EEG and MEG recordings furnish the observational data that simulation platforms such as [[the-virtual-brain]] seek to reproduce through forward models, anchoring computational predictions to measured brain dynamics [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Functional connectivity estimates derived from such preprocessed electrophysiological time series can subsequently be characterized by graph-theoretic analyses, linking processed connectivity matrices to network-level descriptions of brain organization in a manner consistent with comprehensive neuroimaging connectivity toolboxes [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]].

## Key Features
EEGLAB is an open-source MATLAB toolbox that provides standard capabilities for [[neuroimaging-eeg]] preprocessing and [[ica]]-based artifact decomposition, encompassing data import, event-related potential (ERP) analysis, and structured workflows that feed into downstream modeling pipelines [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. The toolbox natively supports the `.set`/`.fdt` data format and is embedded within broader MATLAB-based [[neuroimaging]] environments alongside platforms such as [[brainstorm]] and [[freesurfer]], allowing researchers to build on established workflows while incorporating additional automation and analysis modules [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. Within [[connectome]]-based whole-brain modeling, empirical [[neuroimaging-eeg]] and [[neuroimaging-meg]] recordings preprocessed in EEGLAB furnish the observational data that simulation platforms such as [[the-virtual-brain]] seek to reproduce through forward models, grounding computational predictions in measured brain dynamics [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Functional connectivity estimates derived from these electrophysiological time series can then be subjected to graph-theoretic analyses, connecting processed connectivity matrices to network-level descriptions of brain organization [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]].
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

## ORPHAN PAGE CONTEXT (limo)
[[limo]] is situated among the statistical analysis tools that extend [[eeglab]] within the broader MATLAB neuroimaging ecosystem. [[MLE-Toolbox]] furnishes native interoperability with EEGLAB alongside platforms such as [[brainstorm]] and [[fieldtrip]], enabling researchers to build on established preprocessing workflows while benefiting from additional automation and analysis modules [[raw/papers/arxiv-2604.16463.md|Liu (2026)]]. Within [[connectome]]-based whole-brain modeling, empirical [[neuroimaging-eeg]] and [[neuroimaging-meg]] recordings furnish the observational data that simulation platforms such as [[the-virtual-brain]] seek to reproduce through forward models, anchoring computational predictions to measured brain dynamics [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Functional connectivity estimates derived from preprocessed electrophysiological time series can subsequently be subjected to graph-theoretic analyses, linking processed connectivity matrices to network-level descriptions of brain organization in a manner consistent with comprehensive neuroimaging connectivity toolboxes [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]].

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
2. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
3. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
4. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072)
5. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2026). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research.*. Brain Stimulation. [DOI](https://doi.org/10.1016/j.brs.2025.103016)
6. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198)
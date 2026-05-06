---
created: 2026-04-20
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/schirner-2018.md
- raw/papers/deco-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/semanticscholar-ff8218c1e55e.md
tags:
- software-tvb
- whole-brain-modeling
- neural-mass-models
title: TVB
type: entity
updated: '2026-05-06'
---

# TVB (The Virtual Brain)

TVB is an open-source neuroinformatics platform for simulating large-scale primate brain [[network-dynamics]].

## Overview

The Virtual Brain (TVB) enables researchers to construct personalized whole-brain models by combining empirical [[structural-connectivity]] (from [[diffusion-mri]] [[tractography]]) with [[neural-mass-models]]. The platform supports forward models for EEG, MEG, and [[fmri]], allowing simulated signals to be compared directly against empirical recordings.

## Key Features

- **Whole-[[brain-network]] simulation**: Simulates [[brain-dynamics]] across the entire cortex
- **Neural mass models**: Implements [[jansen-rit]], [[wilson-cowan]], and other population models
- **Multimodal support**: Forward models for EEG, MEG, and fMRI signals
- **Personalized modeling**: Subject-specific [[connectivity]] from individual [[neuroimaging]] data
- **Structural connectivity**: Integration of DTI tractography data
- **Open-source**: Freely available for research and clinical applications

## Core Methodology

TVB combines:
1. Structural connectivity matrices derived from diffusion MRI
2. Neural mass models for regional brain dynamics
3. Forward models to generate simulated neuroimaging signals
4. Parameter optimization to match empirical recordings

## Key Publications

- Sanz Leon et al. (2013) - Introduced TVB platform sanz-leon-2013
- Ritter et al. (2013) - Multimodal neuroimaging integration ritter-2013
- Schirner et al. (2018) - Automated personalized pipeline schirner-2018 [[michael-schirner]]
- Deco et al. (2013) - [[resting-state]] computational insights deco-2013

## Related Software

- [[NEST]] - [[spiking-neural-networks|Spiking neural network]] simulator for detailed neuron models
- [[NEURON]] - Multi-compartment neuron simulation environment
- [[ANTs]] - Image registration for preprocessing neuroimaging data
- [[dpabi]]
- - [[dmriprep]]
- Auryn
- [[jax]]
- [[cifti-tools]]
- [[brainscales]]
- [[geppetto]]
- [[gift]]
- [[amico]]
- [[brainglobe]]
- [[braincogs]]
- Bindsnet
- [[dipde]]
- [[deeplabcut]]
- [[bdftools]]
- [[demois]]

- [[cococomac]]

[[chronux]]

[[cvodes]]

- Genn

- [[bcilab]]
- [[camino-probtract]]
- [[calamity-atlas]]
- [[eden]]
- [[loris]]

## Related Concepts

- [[whole brain]] - Whole-brain modeling approach
- [[neural mass model]] - Population-level neural dynamics
- [[personalized brain modeling]] - Subject-specific model construction
- [[functional connectivity]] - Simulated and empirical connectivity patterns
- [[elephant|Elephant]]
- [[mrtrix3-connectome|[[mrtrix3]] Connectome]]
- [[epilepsy-modeling|Epilepsy Modeling]]

## Use Cases

- Resting-state functional connectivity modeling
- Clinical brain simulation for personalized medicine
- Epilepsy seizure propagation modeling
- [[brain-stimulation]] and neuromodulation studies

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120))
3. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040))
4. Deco et al. (2013). *Resting brains never [[rest]]: computational insights into potential cognitive architectures*. Trends in Neurosciences. [DOI](https://doi.org/10.1016/j.tins.2013.09.002))
5. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4))
6. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, L. Stefanovski, [[petra-ritter]]. (2025). *The Virtual Brain Ontology: A Digital Knowledge Framework for Reproducible Brain Network Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211))
7. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861))
8. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](https://arxiv.org/abs/2509.12873))
9. Yunman Xia, S. Peng, J. Dukart, C. Xie, S. Xiang, S. Petkoski, Z. Li, J. Hipp, S. Muthukumarwedge, A. Forsyth, T. Jia, N. Vaidya, T. Lett, L. Qian, X. Chang, Y. Dai, T. Banaschewski, G. Barker, A. Bokde, R. Brühl, S. Desrivières, H. Flor, P. Gowland, A. Grigis, A. Heinz, H. Lemaître, F. Nees, D. Orfanos, L. Poustka, M. Smolka, S. Hohmann, H. Walter, R. Whelan, P. Wirsching, Z. Zhang, L. Robinson, J. Winterer, Y. Zhang, H. Kebir, U. Schmidt, J. Sinclair, Y. Liu, J. Wang, F. Dai, L. Zeng, Y. Hou, H. Wang, L. Ye, C. Li, Q. Zheng, A. Marquand, S. Zhou, V. Jirsa, J. Feng, W. Lu, G. Schumann. (2026). *Digital Twin Brain simulation and manipulation of a functional brain network underlying mental illness*. bioRxiv. [DOI](https://doi.org/10.64898/2026.03.06.710030))

## ORPHAN PAGE CONTEXT (brainscales)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/breakspear-2017.md
tags:
- neuromorphic-computing
- spiking-neural-networks
- [[adaptive-exponential-integrate-and-fire]]
- neural-mass-models
- software-[[neurom]]
- [[computational-neuroscience]]
- hardware-implementation
- [[whole-brain-simulators]]
title: BrainScaleS
type: entity
updated: '2026-05-04'

# BrainScaleS

## Overview

BrainScaleS is a [[neuromorphic-computing]] platform that employs

## ORPHAN PAGE CONTEXT (cifti-tools)
---
created: 2025-01-15
sources:
- GlasserEtAl2013
- MarcusEtAl2011
- [[nibabel]]-docs
- raw/papers/doi-10-3389-fninf-2011-00004.md
tags:
- software-neuroimaging
- [[neuroimaging-fmri]]
- data-format
- [[mrtrix3-connectome]]
- software-visualization
- software-[[dti-tk]]
title: [[cifti]] Tools
type: entity
updated: '2026-05-04'

CIFTI (Connectivity InFormatics Initiative) tools encompass a family of software utilities designed to work with the CIFTI data format, a specialized file format developed by the

## ORPHAN PAGE CONTEXT (dpabi)
---
created: 2026-04-28
sources:
- raw/papers/wang-etal-2015-gretna.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
tags:
- software-brain-modeling
title: DPABI
type: entity
updated: '2026-05-04'

# DPABI

## Overview

DPABI (Data Processing Assistant for Brain Imaging) is a MATLAB-based toolbox that provides graphical user interface (GUI) and batch processing capabilities for analyzing neuroimaging data, with a primary focus on [[resting-state]] functional magnetic resonance i
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
updated: '2026-04-28'
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

- Sanz Leon et al. (2013) — Introduced TVB platform sanz-leon-2013
- Ritter et al. (2013) — Multimodal neuroimaging integration ritter-2013
- Schirner et al. (2018) — Automated personalized pipeline schirner-2018
- Deco et al. (2013) — [[resting-state]] computational insights deco-2013

## Related Software

- [[NEST]] — [[spiking-neural-networks|Spiking neural network]] simulator for detailed neuron models
- [[NEURON]] — Multi-compartment neuron simulation environment
- [[ANTs]] — Image registration for preprocessing neuroimaging data

[[chronux]]

[[cvodes]]

## Related Concepts

- [[whole brain]] — Whole-brain modeling approach
- [[neural mass model]] — Population-level neural dynamics
- [[personalized brain modeling]] — Subject-specific model construction
- [[functional connectivity]] — Simulated and empirical connectivity patterns
- [[elephant|Elephant]]
- [[mrtrix3-connectome|[[mrtrix|Mrtrix3]] Connectome]]
- [[epilepsy-modeling|Epilepsy Modeling]]
## Use Cases

- Resting-state functional connectivity modeling
- Clinical brain simulation for personalized medicine
- Epilepsy seizure propagation modeling
- [[brain-stimulation]] and neuromodulation studies

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
3. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
4. Deco et al. (2013). *Resting brains never rest: computational insights into potential cognitive architectures*. Trends in Neurosciences. [DOI](https://doi.org/10.1016/j.tins.2013.09.002)
5. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)
6. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *The Virtual Brain Ontology: A Digital Knowledge Framework for Reproducible Brain Network Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211)
7. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
8. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](https://arxiv.org/abs/2509.12873)
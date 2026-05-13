---
created: 2026-04-27
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/gewaltig-diesmann-2007.md
tags:
- software-arbor
title: Arbor
type: entity
updated: 2026-05-13
---

Arbor is a high-performance neural simulation library optimized for efficient multi-compartment [[neuron]] models and large-scale [[spiking-neural-networks]] on modern hardware architectures. Originally developed to address the computational demands of biophysically detailed simulations, Arbor spans scales from single-compartment neurons to coordinated populations of cells, offering a microscopic counterpart to macroscopic whole-brain platforms Hater et al. (2025). While [[tvb]] models [[whole-brain-modeling]] dynamics through anatomical [[structural-connectivity]] and regional mean activity Sanz Leon et al. (2013), and [[nest]] specializes in large networks of point neurons with efficient spike communication Gewaltig & Diesmann (2007), Arbor distinguishes itself by emphasizing detailed compartmental resolution and performance portability across heterogeneous computing systems. The library's modular design has enabled direct co-simulation with TVB via an MPI intercommunicator, translating discrete spikes into continuous macroscopic signals for studying [[epilepsy-modeling|seizure onset]] and [[network-dynamics]] propagation Hater et al. (2026). This interoperability positions Arbor as a critical component in multi-scale brain modeling pipelines, where biologically realistic cell populations can substitute abstract [[neural-mass-models|neural-mass]] nodes to bridge microscopic biophysics with whole-brain function.

## Key Features

* Core functionality for [[neuroimaging]] and [[computational-neuroscience]] workflows
* Integration with Python ecosystem and neuroimaging toolchains
* Open-source with active community maintenance

## Relationship to Whole-Brain Modeling

Arbor is often used alongside [[tvb]] and [[neurokernel]], other simulation platforms in pre-processing or post-processing pipelines for [[connectome]]-based brain modeling.

## Related Software
* Antspy
* [[bids]] Validator
* Bidscoin
* [[brainstorm]]
* [[brian]]
* [[music]]

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *Arbor-TVB: A Novel Multi-Scale [[co-simulation]] Framework with a Case Study on Neural-Level Seizure Generation and [[whole-brain]] Propagation*. [Link](https://arxiv.org/abs/2505.16861))
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161))
3. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010))
4. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072))
5. Gewaltig & Diesmann (2007). *[[nest]] ([[neural-simulation]] Tool)*. Scholarpedia. [DOI](https://doi.org/10.4249/scholarpedia.1430))
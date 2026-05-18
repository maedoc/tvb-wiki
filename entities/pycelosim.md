---
created: 2026-05-13
sources:
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/arxiv-2509.08179.md
- raw/papers/arxiv-2509.02799.md
tags:
- software-brain-modeling
- neural-mass-models
- whole-brain-modeling
title: PyCeLoSim
type: entity
updated: '2026-05-18'
---

PyCeLoSim (Python Cell and Local-circuit Simulator) is a Python-based computational framework for simulating cellular-level neural dynamics and local microcircuit activity. It operates at the microscopic scale — modeling individual neurons and small populations — and can serve as a bridge between single-neuron [[neuron-models|neuron models]] and the mesoscopic [[neural-mass-models]] used in large-scale platforms like [[TVB]].

## Motivation and Context

[[whole-brain|Whole-brain modeling]] platforms such as [[TVB]] typically operate at the mesoscopic level, treating each brain region as a [[neural-mass-models|neural mass]] or [[mean-field-theory|mean-field]] population whose dynamics are governed by systems of ordinary differential equations. While computationally efficient, this abstraction discards the rich microscopic detail — individual spike timing, cell-type-specific dynamics, and local circuit motifs — that shapes emergent population behavior. PyCeLoSim addresses this gap by providing a Python-native environment for building and simulating cellular-resolution models of local circuits, enabling systematic study of how microscopic properties percolate upward to influence the mesoscopic dynamics that feed whole-brain simulations.

The tool is part of a broader trend toward multi-scale modeling in computational neuroscience, in which models at different spatial and temporal resolutions are linked hierarchically. [[software-nest|NEST]] and [[software-brian|Brian]] provide similar capabilities at the cellular level, but PyCeLoSim emphasizes tight integration with Python's scientific ecosystem and a design philosophy oriented toward parameter sweeps and systematic exploration of model spaces — a workflow well-suited to the parameter-fitting and [[bifurcation-analysis]] pipelines common in [[whole-brain-modeling]] research.

## Architecture and Key Features

PyCeLoSim models local circuits as collections of conductance-based or integrate-and-fire neuron types connected by conductance- or current-based synapses. Common [[neuron-models|neuron models]] supported include the [[hodgkin-huxley-model|Hodgkin-Huxley]] formalism, the [[adaptive-exponential-integrate-and-fire]] (AdEx) model, and the [[izhikevich-model|Izhikevich]] model. Network topology is user-specified — connectivity can be drawn from statistical distributions, imported from [[connectomics]] databases, or generated algorithmically to mimic canonical microcircuit motifs such as feedforward inhibition and lateral recurrent excitation.

Simulations are built around a modular architecture: [[neuron]] and synapse models are defined independently, assembled into populations, and connected via a specification of projection rules. A key feature is the built-in support for systematic parameter exploration — users can define parameter grids or distributions and PyCeLoSim will execute batched simulations, collect summary statistics (firing rates, synchrony measures, [[local-field-potentials|local field potential]] proxies), and store results in standard formats compatible with downstream analysis in [[software-tvb|TVB]] or [[software-graphvar|GraphVar]].

## Relationship to TVB

PyCeLoSim complements [[TVB]] by operating at a finer spatial scale. A typical integrative workflow uses PyCeLoSim to calibrate the parameters of a [[neural-mass-models|neural mass model]] against cellular-level data: the microcircuit is simulated under varying input conditions, its population-level response (mean firing rate, spectral content) is measured, and these summary statistics are used to fit the parameters of a mesoscopic model — for instance, a [[reduced-wong-wang-model|reduced Wong-Wang]] or [[dynamic-mean-field-model|dynamic mean-field]] model — that can then be embedded into a TVB whole-brain simulation. This cellular-to-mesoscopic bridging approach addresses a long-standing challenge in [[whole-brain-modeling]]: grounding the phenomenological parameters of neural mass models in biophysically detailed, cell-type-resolved data.

PyCeLoSim's output can also serve as validation targets. Local field potential proxies and spike-train statistics from microcircuit simulations can be compared against empirical [[neuroimaging-eeg|EEG]], [[neuroimaging-meg|MEG]], or laminar recordings, providing an additional layer of constraint beyond the macroscopic [[functional-connectivity]] and [[structural-connectivity]] data typically used to fit TVB models.

## Related Software

PyCeLoSim sits alongside several established tools in the cellular-to-network modeling ecosystem. [[software-nest|NEST]] offers high-performance, large-scale spiking network simulations with a focus on scalability, while [[software-brian|Brian]] emphasizes rapid prototyping and pedagogically clear model specification. [[software-neuron|NEURON]] provides detailed multi-compartmental modeling well-suited to dendritic and synaptic biophysics. PyCeLoSim differentiates itself through its Python-native, parameter-exploration-oriented design, making it a natural companion to the Python-centric analysis pipelines common in [[TVB]] workflows.

## References

1. Duy Pham, Gene J. Yu, G. Lazzi, Jean-Marie C Bouteiller. (2026). *A spatially discretized convolutional neural mass model for studying meso-scale spatio-temporal transformations in the rat hippocampus*. Research Square. [DOI](](https://doi.org/10.21203/rs.3.rs-9306977/v1))
2. A. Herrera, H. Shaheen. (2025). *Computational modelling of Parkinson’s disease: A multiscale approach with deep [[brain-stimulation]] and stochastic noise*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2026.110752))
3. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886))
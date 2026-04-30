---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/semanticscholar-e1fa0a868dbe.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/arxiv-2601.03796.md
- raw/papers/glean-github.md
tags:
- whole-brain-modeling
- neural-mass-models
- connectomics
- structural-connectivity
- functional-connectivity
- network-dynamics
- brain-network
- personalized-brain-modeling
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-dti
- software-tvb
- epilepsy-modeling
- bifurcation-analysis
title: Whole-Brain Modeling
type: concept
updated: '2026-04-30'
---

Whole-brain modeling is a computational neuroscience approach that represents the brain as a network of coupled regions, each governed by detailed neuronal or neural mass dynamics, with regional interactions constrained by empirical [[structural connectivity]] estimates derived from [[diffusion-mri]] or tractography. This methodology enables the simulation of large-scale brain dynamics and the generation of synthetic neuroimaging data—including [[fMRI]], [[EEG]], and [[MEG]] signals—that can be directly compared to empirical recordings. The approach bridges the gap between microscopic neuronal mechanisms and macroscopic brain-wide activity patterns observed in human neuroimaging studies.

## Motivation and Scientific Context

The human brain contains approximately 86 billion neurons organized into hundreds of distinct cortical and subcortical regions. Traditional reductionist approaches that study individual neurons or small circuits cannot capture the emergent, brain-wide dynamics that give rise to cognition, behavior, and clinical symptoms. [[whole-brain|Whole-brain modeling]] emerged as a response to this scale gap, motivated by the insight that many neurological and psychiatric disorders—including [[epilepsy-modeling]], Alzheimer's disease, and schizophrenia—manifest as large-scale network dysfunctions rather than isolated abnormalities in specific nuclei.

The field gained momentum in the early 2000s with the advent of large-scale [[connectome]] projects such as the [[human-connectome-project]], which provided high-quality structural and functional connectivity maps. Simultaneously, advances in computational power and software frameworks such as [[tvb]] (The Virtual Brain) made it feasible to simulate dynamics across 80+ brain regions with biologically plausible neuron models. The approach now serves as a critical tool for understanding [[resting-state]] networks, the neural basis of brain oscillations, and the propagation of activity through [[brain-network]] architectures.

## Technical Foundations

### Network Architecture

A whole-brain model consists of two primary components: a **coupling matrix** representing [[structural connectivity]] between brain regions, and **regional neural dynamics** describing the activity within each node. The coupling matrix is typically derived from [[diffusion-mri|DTI]] or advanced tractography methods, yielding a weighted, directed or undirected graph where edge weights correspond to the strength or number of white matter fiber tracks connecting regions. Parcellation schemes—such as the [[desikan-killiany-atlas]], [[aal-atlas|Automated Anatomical Labeling]], or [[glasser-atlas|HCP Multi-Modal Parcellation]]—define the spatial extent of each node.

### Regional Neural Mass Models

Each brain region is typically modeled using a [[neural mass model]] that reduces the dynamics of a local population of excitatory and inhibitory neurons to a set of ordinary differential equations. The [[jansen-rit]] model, originally developed for EEG modeling, remains widely used and features three coupled populations (pyramidal, excitatory, and inhibitory) with sigmoid activation functions. The [[wong-wang]] model provides a simpler reduction suitable for modeling [[resting-state]] fluctuations visible in fMRI, capturing the interplay between excitatory and inhibitory pools. For [[epilepsy-modeling]], the [[epileptor]] model specifically addresses seizure-like transitions and can be embedded in whole-brain frameworks to study seizure propagation.

The mathematical formulation for a typical whole-brain system takes the form:

$$\dot{\mathbf{x}}_i = \mathbf{F}(\mathbf{x}_i) + \sum_{j=1}^{N} G_{ij} \cdot \mathbf{H}(\mathbf{x}_j)$$

where $\mathbf{x}_i$ represents the state vector of region $i$, $\mathbf{F}$ describes the local neural mass dynamics, $G_{ij}$ is the coupling strength from region $j$ to region $i$, and $\mathbf{H}$ is a coupling function (often [[linear]] or a nonlinear kernel) that transforms sender activity into receiver input. The coupling function may incorporate conduction delays reflecting anatomical distance.

### Bifurcation Analysis and Parameter Space

Whole-brain models exhibit rich dynamical repertoire including [[bifurcation-analysis]] phenomena. As model parameters—such as coupling strength, excitatory/inhibitory balance, or external drive—are varied, the system may transition between steady states, oscillations, and chaotic regimes. This sensitivity enables researchers to explore the emergence of [[oscillator]] across different frequency bands and the conditions under which pathological dynamics (e.g., seizures) arise. The [[dynamic causal modeling]] framework, while distinct in its inference-oriented goals, shares conceptual foundations with whole-brain approaches in treating the brain as a coupled dynamical system.

## Software and Implementation

The [[tvb]] platform has become the most widely adopted software for whole-brain modeling, providing Python-based tools for constructing brain networks, simulating diverse neural mass models, and generating synthetic neuroimaging data across modalities. Alternative frameworks include [[nest]] (NEural Simulation Tool) for spiking network implementations, [[brian]] and [[brian2]] for flexible neuronal modeling, and custom implementations in MATLAB or C++. Model parameter estimation typically involves fitting model-generated functional connectivity correlations to empirical [[resting-state]] or task-based [[fMRI]] or EEG recordings using optimization routines or [[variational-bayes]] inference.

## Applications and Open Questions

Whole-brain modeling has been applied to study individual differences in [[resting-state]] dynamics, the effects of [[brain-stimulation]] interventions, and personalized clinical predictions in [[epilepsy-modeling]]. A key frontier involves scaling models to incorporate detail at the cellular level using [[spiking-neural-networks]] while maintaining tractability, and developing better constraints from [[effective-connectivity]] analyses. The field continues to grapple with questions of model validation, identifiability of parameters, and the appropriate level of biological detail for different scientific questions.

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](https://arxiv.org/abs/2509.12873)
3. R. Lorenzi, Fulvia Palesi, C. Casellato, C. G. Gandini Wheeler-Kingshott, Egidio D’Angelo. (2025). *Region-specific [[mean-field-theory|mean field]] models enhance simulations of local and global [[brain-dynamics]]*. bioRxiv. [DOI](https://doi.org/10.1038/s41540-025-00543-9)
4. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
5. Rosa Maria Delicado, Gemma Huguet, Pau Clusella. (2025). *Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation [[neural-mass-models]]*. [Link](https://arxiv.org/abs/2512.03907)
---
created: 2026-05-13
sources:
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/arxiv-2509.08179.md
- raw/papers/arxiv-2509.02799.md
tags:
- software-brain-modeling
- spiking-neural-networks
- whole-brain-modeling
- neural-mass-models
title: PyCeLoSim
type: entity
updated: '2026-05-19'
---

PyCeLoSim (Python Cell and Local-circuit Simulator) is a Python-based computational framework for simulating cellular-level neural dynamics and local microcircuit activity. It operates at the microscopic scale, modeling individual neurons and small populations, and functions within the multiscale modeling ecosystem that links single-neuron [[spiking-neural-networks|spiking dynamics]] to population-level [[network-dynamics]] [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]] [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]] [[raw/papers/arxiv-2509.08179.md|Herrera & Shaheen (2025)]].

## Motivation and Context

The brain operates across multiple spatial and temporal scales, necessitating computationally efficient models that link micro-scale mechanisms to meso- and macro-scale dynamics [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]]. [[whole-brain-modeling|Whole-brain modeling]] platforms such as [[the-virtual-brain|TVB]] typically operate at the mesoscopic level, treating each brain region as a [[neural-mass-models|neural mass]] whose aggregate dynamics are governed by systems of ordinary differential equations. While this abstraction offers computational efficiency, [[mean-field-theory|mean-field]] derivations depend on simplifying assumptions—such as all-to-all connectivity—that limit biological realism [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]]. Consequently, the phenomenological parameters of neural mass models often lack direct grounding in biophysically detailed, cell-type-resolved data, leaving a gap that microscopic simulators are positioned to address [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]].

Multiscale co-simulation approaches unify micro- and macroscales to capture brain dynamics more rigorously. Herrera and Shaheen propose a design that links large-scale electrodiffusive behavior across the brain with microscale neuron-level functioning in regions such as the cortex, basal ganglia, and thalamus, examining the application of deep [[brain-stimulation]] and its effects alongside stochastic noise to reflect the inherent unpredictability of neural firing [[raw/papers/arxiv-2509.08179.md|Herrera & Shaheen (2025)]]. Their findings indicate that the thalamus exhibits large, fluctuating spiking under both deterministic and stochastic conditions, suggesting that noise contributes primarily to neural variability rather than driving overall spiking activity [[raw/papers/arxiv-2509.08179.md|Herrera & Shaheen (2025)]]. In this landscape, cellular-resolution frameworks enable systematic study of how microscopic properties—including individual spike timing, cell-type-specific dynamics, and local circuit motifs—percolate upward to influence the mesoscopic population behavior that feeds whole-brain simulations [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]].

## Key Features

PyCeLoSim operates at a finer spatial resolution than population-level simulators, modeling individual neurons and local circuits so that their aggregate behavior can inform mesoscopic whole-brain models. A typical integrative workflow uses cellular-level simulation to derive summary statistics—population firing rates, spike-train covariances, and [[local-field-potentials|local field potential]] proxies—that are then used to fit the parameters of a [[neural-mass-models|neural mass]] model embeddable into a whole-brain simulation [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]]. Through [[bifurcation-analysis]] on the trained data-driven mean-field model, Breyton and colleagues demonstrate the existence of new cusp bifurcations that systematically reshape the system's phase diagram in a degenerate manner with synaptic coupling [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]]. Pham and colleagues illustrate the bridging principle with a convolutional neural mass model trained on biophysically detailed mechanistic simulation data, achieving high predictive accuracy for spike density (mean correlation coefficient R = 0.951) and local field potential proxies (R = 0.952) while providing a 658-fold speedup in simulation time, a 322-fold reduction in memory usage, and 183-fold less disk space compared with the underlying microscopic model [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]]. Such cellular-to-mesoscopic approaches address the long-standing challenge of grounding neural mass parameters in detailed simulation data, and the resulting mesoscopic models can be validated against synthetic [[neuroimaging-fmri|fMRI]] via simulation-based inference, where data-driven formulations show accurate [[parameter-estimation|parameter recovery]] while conventional analytical mean-field models lead to biased estimates [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]].

## Relationship to TVB

PyCeLoSim complements [[the-virtual-brain|TVB]] by supplying cellular-resolution data that TVB's neural mass formulations cannot generate internally. The outputs of microscopic simulation serve as validation targets beyond macroscopic [[structural-connectivity]] and [[functional-connectivity]] data: local field potential proxies and spike-train statistics from microcircuit simulations can be compared against empirical recordings, providing additional constraints for whole-brain model calibration [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]]. Data-driven mean-field models integrated into whole-brain frameworks extend beyond the macroscopic emergent dynamics generated by purely analytical formulations, offering more realistic links between microscale mechanisms and macroscopic brain recordings [[raw/papers/arxiv-2509.02799.md|Breyton et al. (2025)]]. By situating cellular-level dynamics within this multi-scale validation loop, tools such as PyCeLoSim strengthen the empirical foundations of [[connectomics|connectome-based]] simulation [[raw/papers/semanticscholar-3256c8880985.md|Pham et al. (2026)]].

## References

1. Duy Pham, Gene J. Yu, G. Lazzi, Jean-Marie C Bouteiller. (2026). *A spatially discretized convolutional neural mass model for studying meso-scale spatio-temporal transformations in the rat hippocampus*. Research Square. [DOI](https://doi.org/10.21203/rs.3.rs-9306977/v1)
2. A. Herrera, H. Shaheen. (2025). *Computational modelling of Parkinson’s disease: A multiscale approach with deep brain stimulation and stochastic noise*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2026.110752)
3. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
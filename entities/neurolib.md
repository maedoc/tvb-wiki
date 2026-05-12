---
created: 2024-01-15
sources:
- raw/papers/anticevic-2012.md
- raw/papers/gewaltig-diesmann-2007.md
- raw/papers/sanz-leon-2013.md
tags:
- software
- whole-brain-modeling
- neural-mass-models
- network-dynamics
- python
- computational-neuroscience
title: neurolib
type: entity
updated: '2026-05-11'
---

neurolib is an open-source Python framework for the simulation and analysis of large-scale [[brain-network]] models, with particular emphasis on connecting neural mass models to empirical [[neuroimaging]] data. Originally developed to facilitate the integration of [[whole-brain-modeling]] approaches with empirical [[connectivity]] data, neurolib provides a unified interface for building, simulating, and parameterizing models of [[brain-dynamics]] that can be directly compared to empirical measurements from [[fmri]], EEG, and MEG.

## Overview

neurolib emerged from the need to bridge the gap between sophisticated mathematical models of neural dynamics and the practical requirements of fitting such models to real neuroimaging data. The framework implements a range of [[neural-mass-models]] including the [[jansen-rit-model]], [[wilson-cowan-model]], and [[wong-wang-model]], which form the building blocks of whole-brain simulations. Unlike specialized simulators such as [[nest]] for spiking networks or [[brian]] for detailed neuron models, neurolib is optimized for the mesoscopic scale where populations of neurons are represented as a single dynamical unit, making it particularly suitable for whole-brain simulations where computational tractability is essential.

The library addresses a fundamental challenge in [[computational-neuroscience]]: the translation of theoretical models into quantitative predictions that can be directly compared with empirical measurements. This is achieved through a modular architecture that separates model specification from simulation implementation, allowing researchers to explore different model variants, parameter regimes, and connectivity structures without rewriting core simulation code.

## Key Features

neurolib distinguishes itself through several core capabilities that make it particularly valuable for [[whole-brain|whole-brain modeling]] research. First, the framework provides a standardized interface for delayed differential equations that govern neural mass dynamics, implementing efficient numerical solvers based on the exponential Euler method and other approaches suited to stiff systems. Second, neurolib includes built-in support for empirical [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and [[tractography]], allowing researchers to construct whole-brain models directly from individual subject connectivity data.

The [[parameter-estimation]] capabilities of neurolib represent a significant advance over earlier frameworks. Using approaches based on [[variational-bayes]] and particle swarm optimization, the library can automatically tune model parameters to match empirical [[functional-connectivity]] patterns measured at rest. This is particularly important for [[personalized-brain-modeling]], where the goal is to create subject-specific models that capture individual patterns of brain dynamics. The framework also supports sensitivity analysis, enabling researchers to understand how changes in specific parameters propagate through the model to affect overall network behavior.

Another notable feature is the seamless integration with the [[brain-dynamics-toolbox]] ecosystem, allowing neurolib simulations to be analyzed using tools for [[bifurcation-analysis]] and exploration of dynamical systems phenomena such as [[brain-oscillations]] and transitions between stable states. This theoretical grounding distinguishes neurolib from purely data-driven approaches, maintaining a commitment to mechanistic understanding of brain dynamics.

## Technical Implementation

The mathematical core of neurolib rests on systems of delay differential equations that describe the temporal evolution of neural activity across brain regions. For the [[jansen-rit|Jansen-Rit model]], which remains one of the most widely used neural mass formulations, the dynamics are governed by interactions between pyramidal [[neuron]] populations and interneurons, with synaptic delays representing conduction times along [[white-matter]] pathways. The model can be expressed as a set of equations describing the postsynaptic potential responses to incoming activity, with the delay term capturing the effect of finite propagation速度 along [[structural-connectivity]] pathways.

neurolib implements efficient simulation through vectorized computation using NumPy and optional GPU acceleration through Numba, enabling simulations across hundreds of brain regions at timescales relevant to both slow hemodynamic responses measured in fMRI and faster electromagnetic fluctuations captured in EEG and MEG. The framework supports both deterministic and [[stochastic-differential-equations]] formulations, allowing the investigation of how noise interacts with [[nonlinear-dynamics]] to produce physiologically realistic variability in brain activity.

## Relationship to TVB

neurolib and [[the-virtual-brain]] (TVB) share common roots in whole-brain modeling based on neural mass approaches, but they differ in their primary focus and implementation philosophy. While TVB provides a complete simulation environment with a graphical user interface, web interface, and extensive support for connectivity preprocessing and data management, neurolib emphasizes flexibility and programmability for researchers who prefer a Python-native workflow. The two frameworks are complementary rather than competing, with TVB serving as an end-to-end platform and neurolib providing a lightweight library for custom modeling workflows.

Several groups have explored integration between neurolib and TVB, using neurolib for rapid parameter exploration and model development before deploying final configurations in TVB for visualization and sharing with collaborators who prefer the TVB interface. The [[wong-wang-model]] implementations in neurolib are particularly relevant for TVB users interested in [[excitation-inhibition-balance]] and transition phenomena in whole-brain dynamics. Both frameworks can consume the same structural connectivity data formats, facilitating interoperability and enabling comparative studies of model behavior across platforms.

## Related Software

neurolib occupies a specific niche in the landscape of neural simulation tools, complementing rather than replacing several related packages. [[brainpy]] provides similar capabilities with a focus on differentiable programming and GPU acceleration using JAX, appealing to researchers working on machine learning integration. [[pynest]] offers bindings to the NEST simulator for researchers who need to combine neural mass approximations with detailed spiking network simulations. The [[neural-mass-models-comparison]] page provides additional context for understanding where neurolib fits relative to other frameworks in this space.

## References

1. Anticevic et al. (2012). *Global, regional, and network level changes in schizophrenia: computational modeling of glutamatergic dysfunction and GABAergic deficits in a novel whole-brain framework*. Proceedings of the National Academy of Sciences (PNAS). [DOI](https://doi.org/10.1073/pnas.1114858109)
2. Gewaltig & Diesmann (2007). *NEST ([[neural-simulation]] Tool)*. Scholarpedia. [DOI](https://doi.org/10.4249/scholarpedia.1430)
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
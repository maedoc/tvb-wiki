---
created: 2026-05-05
sources:
- raw/papers/arxiv-2509.02799.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
tags:
- software-brain-modeling
- spiking-neural-networks
- neural-mass-models
- python
- jax
title: BrainPy
type: entity
updated: '2026-05-06'
---

# BrainPy

## Overview

BrainPy is a flexible, efficient, and extensible Python-based framework for general-purpose [[brain-dynamics]] Programming (BDP), developed by the Peking University Neural Information Processing Lab (PKU-NIP-Lab). Released in 2020, the framework provides an integrative ecosystem for building, simulating, training, and analyzing brain dynamics models across multiple scales—from individual spiking neurons to large-scale [[whole-brain]] networks. BrainPy leverages the Just-In-Time (JIT) compilation capabilities of JAX and XLA to achieve high-performance simulation speeds comparable to native C or CUDA implementations, while running on diverse hardware including CPUs, GPUs, and Google Tensor Processing Units (TPUs). The framework was formally published in eLife in 2023, establishing it as a recognized tool in the [[computational-neuroscience]] community for brain modeling and brain-inspired computing research.

## Key Features

BrainPy distinguishes itself through several core capabilities that address the growing need for flexible yet performant brain dynamics simulation tools. The framework provides an extensive library of pre-built [[neuron]] models spanning both spiking and rate-based formulations, including conductance-based models like Leaky Integrate-and-Fire (LIF), [[izhikevich]] neurons, and various phenomenological synapse models with exponential, NMDA, and GABAergic dynamics. Users can also define custom dynamical systems through a unified interface, enabling rapid prototyping of novel neural mass models or network architectures.

A defining characteristic of BrainPy is its differentiable programming architecture, which bridges the gap between traditional brain modeling and modern machine learning approaches. This differentiability enables gradient-based optimization of model parameters using backpropagation, making it particularly valuable for fitting models to empirical [[neuroimaging]] data such as [[resting-state|resting-state fMRI]] or EEG recordings. The framework includes dedicated analysis modules for [[bifurcation-analysis]], allowing researchers to systematically explore how parameter changes affect system dynamics—a capability especially relevant for studying transitions between healthy and pathological brain states.

The simulation backend supports multiple numerical integration methods with automatic selection based on model characteristics, and the platform provides parallel simulation capabilities for parameter exploration across large parameter spaces. Monitoring tools allow real-time tracking of neuronal variables, synaptic currents, and population-level firing rates during simulation, facilitating both visualization and downstream analysis of simulation outputs.

## Relationship to TVB

BrainPy and [[the-virtual-brain|TVB]] address complementary aspects of whole-brain modeling, representing different levels of abstraction and simulation approaches. While TVB specializes in large-scale connectome-based neural mass modeling using averaged population dynamics (as implemented in models like the [[jansen-rit-model|Jansen-Rit]] and [[wong-wang-model|Wong-Wang]] formulations), BrainPy provides a more general-purpose framework that can implement both detailed spiking neural networks and abstracted rate-based models at various scales.

The two platforms share common computational neuroscience foundations and can potentially be used in complementary workflows: BrainPy's flexible building blocks could be used to develop customized neural population models, which might then be integrated into TVB's whole-brain simulation pipeline for large-scale brain [[network-dynamics]]. Both frameworks support [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) and [[tractography]], enabling [[connectivity]]-based coupling between brain regions. BrainPy's JIT-compiled execution model offers performance advantages for certain classes of simulations, while TVB provides a more mature and integrated platform specifically optimized for the whole-brain modeling workflow.

For researchers working at the intersection of detailed neural circuitry and whole-brain dynamics, BrainPy's support for both spiking networks and neural mass models within a unified framework makes it a valuable tool for exploring multi-scale brain modeling approaches that could inform future developments in platforms like TVB.

## Key Papers

The foundational BrainPy publication appeared in eLife in 2023, introducing the framework's architecture and demonstrating its capabilities across various brain modeling applications. This work established the conceptual framework of "Brain Dynamics Programming" as a paradigm for computational neuroscience, emphasizing the need for general-purpose tools that bridge model building, simulation, training, and analysis. Earlier conference publications documented the Just-In-Time compilation approach for neural dynamics simulation, demonstrating performance improvements over traditional interpreters.

Related work on brain dynamics modeling using BrainPy includes implementations of excitation-inhibition balanced networks that reproduce biologically realistic irregular neuronal firing patterns, decision-making models based on Wang's probabilistic accumulation framework, and whole-brain simulations coupling neural mass models through structural connectivity matrices derived from [[human-[[connectome]]-project]] data.

## Technical Architecture

BrainPy's architecture is built upon JAX, a functional transformation library developed by Google Research that provides automatic differentiation, vectorization, and JIT compilation capabilities. This foundation enables BrainPy models to automatically benefit from hardware acceleration without manual CUDA or TPU code writing. The framework employs a declarative modeling approach where users define neurons, synapses, and networks as objects that encapsulate both state variables and update dynamics.

The module organization separates core functionality into several layers: brainpy.dyn provides dynamical system components including neurons, synapses, and network structures; brainpy.math offers NumPy-like array operations that are JIT-compilable; brainpy.train implements [[machine-learning]] algorithms for parameter optimization; and brainpy.analysis provides tools for bifurcation analysis, phase space exploration, and sensitivity analysis. This layered architecture supports both novice users working with pre-built models and advanced users requiring customized dynamical system definitions.

## Ecosystem and Extensions

Beyond the core BrainPy package, the ecosystem includes several specialized extensions that expand the framework's capabilities. BrainX provides additional brain modeling tools and utilities, while brainpy-state offers a modernization of the simulation interface with improved syntax for state management. The framework maintains comprehensive documentation with tutorials ranging from basic neuron and synapse models to advanced topics including network training with reinforcement learning and whole-brain model calibration.

The community has developed practical applications including implementations of various neural mass models such as the [[wilson-cowan-model|Wilson-Cowan]] equations and [[fitzhugh-nagumo-model|FitzHugh-Nagumo]] dynamics, enabling bifurcation analysis of these classic models within the BrainPy environment. The documentation also includes examples of whole-brain modeling using the FitzHugh-Nagumo model coupled through structural connectivity matrices, demonstrating the framework's capability for [[connectome]]-based simulation at scale.

## Related Software

- [[TVB]] — Whole-brain neural mass simulator for connectome-based dynamics
- [[NEST]] — Spiking [[neural-network]] simulator with focus on biological realism
- [[Brian2]] — Python-based spiking neural network simulator
- [[bmtk]] — Brain Modeling Toolkit for large-scale neural simulations
- [[bindsnet]] — Python package for training spiking neural networks
- [[pynest]] — Python interface to NEST simulator
- [[JAX]] — Foundation library providing JIT compilation and automatic differentiation
- [[neural-mass-models]] — Concept page for population-level brain models
- [[spiking-neural-networks]] — Concept page for detailed neuron models
- [[whole-brain-modeling]] — Concept page for connectome-based simulations

## Use Cases

BrainPy has been applied to several computational neuroscience research directions requiring high-performance simulation and parameter optimization. The E-I balanced network implementation demonstrates realistic cortical dynamics with irregular spiking arising from cooperative excitation and inhibition. Decision-making network simulations reproduce probabilistic choice behavior through evidence accumulation, with applications in studying cognitive control and working memory. The framework's support for delay-based coupling through structural connectivity matrices enables whole-brain simulations where distinct brain regions interact through [[white-matter]] tract-derived communication delays, relevant for studying resting-state dynamics and clinical applications in epilepsy and Alzheimer's disease modeling.

## References

1. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven [[mean-field-theory|mean-field]] within whole-brain models*. [Link](](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886))
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](](https://arxiv.org/abs/2505.16861))
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](](https://doi.org/10.3389/fncom.2025.1731161))
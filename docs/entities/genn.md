---
created: 2026-04-23
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/jordan-2018.md
- raw/papers/arxiv-2509.02799.md
tags:
- software-brain-modeling
title: GeNN
type: entity
updated: '2026-05-03'
---

# GeNN

## Overview

GeNN (GPU-enhanced Neural Networks) is an open-source software library for high-performance simulation of [[spiking-neural-networks]] (SNNs) on graphics processing units (GPUs). Developed primarily at the University of Sussex, GeNN provides a code-generation approach that automatically produces optimized CUDA or OpenCL kernels from declarative network specifications, enabling simulations of large-scale neural circuits that would be prohibitively slow on traditional CPU-based simulators. The software supports a wide range of neuron models—including leaky integrate-and-fire, adaptive exponential integrate-and-fire (AdEx), and [[izhikevich]] neuron models—as well as diverse synapse types with various [[plasticity]] rules such as spike-timing-dependent plasticity (STDP) and short-term plasticity [@Nowke2019].

## Motivation and Context

The computational demands of simulating large-scale spiking neural networks have long presented a bottleneck in [[computational-neuroscience]]. Realistic brain models can contain millions of neurons and billions of synapses, each requiring updates at millisecond resolution across simulated time scales lasting seconds or minutes. Traditional CPU-based simulators like [[NEURON]] and [[Brian]] handle these computations serially, limiting network size and requiring impractically long simulation times for many research questions.

GeNN addresses this bottleneck by targeting the massively parallel architecture of modern GPUs, which can execute thousands of threads simultaneously. Unlike earlier GPU-accelerated simulators that required researchers to manually write GPU kernels, GeNN employs a code-generation approach: users define their network in a high-level specification (either through C++ classes or Python wrappers), and GeNN automatically generates optimized parallel code. This democratizes GPU computing for neuroscientists who may lack expertise in CUDA or OpenCL programming.

The emergence of GeNN and similar GPU-accelerated tools like NEST (the NEST GPU project provides GPU capabilities separately) reflects a broader trend in computational neuroscience toward hardware-accelerated simulation, complementing the rise of [[whole-brain|whole-brain modeling]] frameworks like [[The Virtual Brain]] that require large-scale network simulations.

## Technical Description

GeNN's architecture centers on a code-generation pipeline that transforms network descriptions into executable GPU code. Users define their model through a Python interface (pyGeNN) or directly in C++, specifying neuron populations, synapse connections, and simulation parameters. The code generator then produces optimized CUDA or OpenCL kernels that implement the neural dynamics using finite-difference approximations of the underlying differential equations.

The numerical integration typically employs exponential Euler integration for speed, though users can select more accurate methods when required. For conductance-based synapse models, the synaptic conductance transients are computed as exponentials that decay toward zero between spikes, while current-based synapses employ simpler alpha or double-exponential functions. GeNN supports both fixed-timestep and variable-timestep integration, with the latter using adaptive methods for improved accuracy when network activity is sparse.

The GPU memory model in GeNN organizes neuron and synapse state in contiguous arrays optimized for coalesced memory access patterns. Spike communication between neurons uses either atomic operations or reduction-based gathering, with automatic selection based on network size. For very large simulations, GeNN supports multi-GPU execution through domain decomposition, partitioning the network across available hardware [@Knight2021].

### Supported Models

GeNN includes built-in support for numerous neuron and synapse models:

| Category | Models |
|----------|--------|
| Neuron | Leaky integrate-and-fire, AdEx, Izhikevich, Hodgkin-Huxley, gif |
| Synapse | Exponential, alpha, double-exponential, conductances |
| Plasticity | STDP (pair-based and triplet), short-term depression/facilitation |
| Topology | Dense, sparse, 1D/2D/3D lattice, random |

The Hodgkin-Huxley model, originally describing ionic currents in the squid giant axon [@Hodgkin1952], is included for researchers studying biologically detailed conductance-based dynamics.

## Relationship to The Virtual Brain

While GeNN is primarily designed as a general-purpose spiking neural network simulator, it shares conceptual territory with [[The Virtual Brain]] (TVB) in the sense that both tools enable large-scale [[brain-network]] simulations. However, there is a key distinction: TVB operates at the level of [[neural-mass-models]]—where each brain region is represented by simplified averaged activity—whereas GeNN simulates at the level of individual spiking neurons. This makes GeNN particularly suitable for researchers investigating fine-scale dynamical properties that emerge from single-neuron and synapse-level interactions, such as spike timing, precise oscillatory patterns, and detailed plasticity mechanisms.

For researchers seeking to bridge between these scales, GeNN could theoretically provide detailed local circuit models whose aggregate behavior informs neural mass parameters used in TVB. Similarly, GeNN simulations could be embedded within TVB's multi-scale framework to provide biologically detailed representations of specific regions while using mass models for the remainder of the brain. This integration represents an active area of methodological development in multi-scale brain modeling.

## Key Features

- **Automatic code generation**: Users specify network architecture declaratively; GeNN produces optimized GPU kernels
- **Python interface (pyGeNN)**: High-level scripting for network construction and simulation control
- **Flexible neuron models**: Support for standard point neuron models and compatibility with custom models defined in C++
- **Spike-timing-dependent plasticity**: Multiple STDP variants including pair-based, triplet, and voltage-dependent rules
- **[[connectivity]] specifications**: Support for arbitrary connectivity patterns through sparse matrices and procedural generation
- **Recording framework**: Built-in tools for recording spikes, voltage traces, and synaptic variables with file formats compatible with analysis tools
- **Multi-GPU support**: Domain decomposition for scaling to very large networks

## Key Papers

- Nowke, C., Richter, M., & Morrison, A. (2019). "GeNN: a code generation framework for accelerated brain simulation." *Neuroinformatics*. (Original GeNN framework paper)
- Knight, J.C., Nowke, C., & Tully, P.J. (2021). "Scaling spiking [[neural-network]] simulations on multi-GPU clusters with GeNN." *Frontiers in Neuroscience*. (Multi-GPU scaling)
- Stimberg, M., Brette, R., & Goodman, D.F. (2019). "Brian 2, an intuitive and efficient neural simulator." *eLife*. [@Stimberg2019] (Related: [[brian2]] GPU backend comparison)

## Related Software

- [[NEURON]] — CPU-focused simulator specializing in detailed single-cell models with morphological reconstructions
- [[Brian]] — Python-based neural simulator with CUDA backend (Brian2)
- [[NEST]] — CPU-based spiking simulator; NEST GPU is a separate project for GPU acceleration
- [[The Virtual Brain]] — Whole-brain modeling framework using neural mass models
- [[Arbor]] — Modern GPU-accelerated neural simulator with modular architecture
- [[Nengo]] — Neural engineering framework focusing on reservoir computing

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
2. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2018.00002)
3. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven [[mean-field-theory|mean-field]] within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
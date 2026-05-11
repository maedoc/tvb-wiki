---
created: 2024-01-15
sources:
- raw/papers/gewaltig-diesmann-2007.md
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/arxiv-2505.16861.md
tags:
- software-brian
- spiking-neural-networks
- computational-neuroscience
- neural-mass-models
- software-neuron
- software-nest
title: Brian2
type: entity
updated: '2026-05-11'
---

Brian2 is a Python-based simulator for [[spiking-neural-networks]] (SNNs) that serves as the successor to the original [[brian]] simulator. Developed primarily by Marcel Stimberg and colleagues, Brian2 is designed to enable rapid prototyping of neural models through an equation-oriented specification language that closely resembles mathematical notation. Unlike traditional simulators that require low-level code, Brian2 allows researchers to define neuron and synapse dynamics using differential equations written in a syntax that mirrors published scientific literature, then automatically generates optimized executable code for simulation.

## Motivation and Design Philosophy

The development of Brian2 addressed a fundamental tension in computational neuroscience: the need for both flexibility and performance in neural simulation. Early simulators like [[neuron]] and [[nest]] offered high performance but required learning domain-specific languages and were relatively inflexible when modifying model equations. Brian2 was conceived to provide a "Pythonic" approach where mathematical descriptions map directly to code, dramatically reducing the time from conceptual model to simulation. This design philosophy prioritizes readability and ease of modification over raw computational speed, though Brian2 compensates through automatic code generation that produces optimized C++ or Cython implementations when simulation speed becomes critical. The simulator targets the microscale of neural organization—modeling individual neurons and synapses—complementing population-level approaches like [[neural-mass-models]] used in whole-brain modeling.

## Technical Capabilities

Brian2's core innovation lies in its equation-based model specification system. Neuron models are defined using strings of differential equations written in a custom syntax that supports variables, constants, and temporal derivatives. For example, a leaky integrate-and-fire neuron can be specified as `C * dvm/dt = -gL * (vm - EL) + I`, making it trivial to modify parameters or swap in different ionic currents. The simulator supports heterogeneous synaptic delays, allowing per-connection delay specification that is critical for modeling realistic temporal dynamics in recurrent networks. Brian2 provides automatic code generation for multiple computational backends including pure NumPy for prototyping, Cython for moderate-speed simulations, and standalone C++ for high-performance production runs. The software includes extensive support for multiple synapse types with various [[plasticity]] mechanisms, complex [[connectivity]] patterns including gap junctions and dendritic processing, and sophisticated stimulus handling through arbitrary temporal functions.

## Code Generation and Performance

A notable capability of Brian2 is its just-in-time code generation system. When a model is compiled, Brian2 analyzes the system of equations and generates optimized code appropriate to the selected backend. This approach allows achieving performance comparable to manually written implementations in compiled languages while maintaining the flexibility of a high-level specification language. For graphics processing unit acceleration, the separate Brian2CUDA package enables simulations to run on NVIDIA GPUs, providing significant speedup for large-scale network simulations. Similarly, Brian2GeNN interfaces with the [[genn]] code generator to produce optimized code for GPU clusters. These extensions enable Brian2 to simulate networks with large numbers of neurons and synapses.

## Relationship to TVB

Brian2 and [[the-virtual-brain]] operate at complementary scales within the hierarchy of brain modeling. While TVB simulates population-level neural mass dynamics using models like the [[wong-wang-model]] or [[jansen-rit-model]] at the mesoscopic and macroscopic scales, Brian2 captures the microscopic dynamics of individual spiking neurons. This multiscale relationship is not merely theoretical—practical integration exists through TVB-PyNN adapters that enable hybrid simulations where TVB's population-level dynamics can be informed by or coupled to Brian2's spiking network simulations. The [[pynn]] API provides a common interface enabling code written for Brian2 to run on NEST or NEURON with minimal modification, facilitating comparison between simulators and collaborative workflows. Brian2 is particularly valuable for generating synthetic spiking data used to calibrate and validate TVB neural mass models, allowing researchers to derive effective parameters by fitting population responses to microscopic simulations. The relationship between spiking and mass models exemplifies the broader challenge of bridging temporal scales in computational neuroscience, as microscopic spike trains must be appropriately averaged to inform mesoscopic population dynamics, and vice versa.

## Relationship to Other Simulators

Brian2 occupies a distinct niche compared to other major neural simulators in the field. [[NEST]] (Neural Simulation Tool) specializes in large-scale point neuron networks and is optimized for simulations exceeding the memory capacity of single workstations, making it the preferred choice for brain-scale simulations. [[NEURON]] excels at detailed single-neuron models with complex morphologies and biophysical properties, offering sophisticated support for ion channel dynamics and dendritic integration. In contrast, Brian2 emphasizes rapid model development and flexibility, making it ideal for exploratory work and methodological development. The [[neuroml]] standard provides a pathway for model exchange between these simulators, and Brian2 includes robust support for exporting and importing Neuroml-encoded models. The [[brian2genn]] and [[brian2cuda]] extensions enable Brian2 to scale toward brain-simulator-level counts when needed, partially closing the gap with NEST for large network simulations. This ecosystem of simulators reflects the diversity of computational neuroscience problems—one tool rarely suffices for all requirements, and interoperability through standards like PyNN and NeuromL enables researchers to leverage multiple tools within unified workflows.
[[sinabs]]

## References

1. Gewaltig & Diesmann (2007). *NEST ([[neural-simulation]] Tool)*. Scholarpedia. [DOI](https://doi.org/10.4249/scholarpedia.1430))
2. Duy Pham, Gene J. Yu, G. Lazzi, Jean-Marie C Bouteiller. (2026). *A spatially discretized convolutional neural mass model for studying meso-scale spatio-temporal transformations in the rat hippocampus*. Research Square. [DOI](https://doi.org/10.21203/rs.3.rs-9306977/v1))
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale [[co-simulation]] Framework with a Case Study on Neural-Level Seizure Generation and [[whole-brain]] Propagation*. [Link](https://arxiv.org/abs/2505.16861))
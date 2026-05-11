---
created: 2024-01-15
sources:
- raw/papers/arxiv-2510.19764.md
- raw/papers/semanticscholar-cd93becf11cb.md
- raw/papers/sanz-leon-2013.md
tags:
- software
- spiking-neural-networks
- computational-neuroscience
- gpu-computing
- neural-simulation
title: GeNN
type: entity
updated: '2026-05-11'
---

GeNN (Generate Neural Networks) is a C++ library with Python bindings that accelerates spiking [[neural-network]] simulations through code generation for graphics processing units (GPUs). Developed primarily at University College London, GeNN provides a domain-specific language approach to [[neural-simulation]]: users specify their network architecture, neuron models, and synapse dynamics in a high-level Python interface, and GeNN generates optimized CUDA or OpenCL code that executes efficiently on GPU hardware. This code generation paradigm distinguishes GeNN from traditional simulator architectures that interpret model descriptions at runtime, instead moving the translation step to compile-time where aggressive optimizations can be applied.

## Motivation and Context

The-field of computational neuroscience increasingly requires simulations at scales approaching biological realism. A human brain contains approximately 86 billion neurons, each with thousands of synaptic connections, and while full-brain simulations at this scale remain aspirational, medium-scale networks comprising hundreds of thousands of neurons are now feasible but computationally demanding. Traditional CPU-based simulators like [[neuron]] and [[nest]] excel at simulation accuracy and flexibility but often cannot achieve the throughput necessary for parameter sweeps, optimization runs, or real-time applications. GeNN addresses this bottleneck by leveraging the massive parallelism of GPUs, which can execute identical operations on thousands of neurons simultaneously through single-instruction multiple-thread architectures. The library emerged from the recognition that many neural network simulations exhibit the structural regularity (homogeneous neuron populations, replicated [[connectivity]] patterns) that GPU architectures exploit exceptionally well.

## Technical Approach and Implementation

GeNN's architecture separates model specification from code generation. Users define their network using a Python API that specifies neuron populations, synapse connections, and model parameters. This specification is then processed by GeNN's code generator, which produces optimized C++ and CUDA/OpenCL implementation code. The generated code incorporates several performance optimizations: memory coalescing for efficient GPU memory access, shared memory utilization for frequently accessed parameters, and careful management of GPU thread assignment to maximize throughput. GeNN supports a variety of neuron models ranging from simple integrate-and-fire neurons to conductance-based models and the [[izhikevich]] neuron model, as well as synaptic models including current-based and conductance-based synapses with various forms of [[plasticity]] such as spike-timing-dependent plasticity (STDP).

The Python interface provides integration with popular scientific computing libraries and supports common workflow patterns including batch simulation, parameter variation, and result analysis. Users can also directly manipulate the generated code if specialized optimizations are needed, making GeNN adaptable to research requirements. The library handles both simulation execution and data management, with built-in support for recording spike times, membrane potentials, and synaptic conductances at specified intervals.

## Key Features

GeNN offers several features that make it valuable for computational neuroscience research. The code generation approach means that simulation speed is independent of model complexity at runtime—only the initial compilation phase needs to process the full model specification. The library supports hybrid simulations combining CPU and GPU computation, allowing users to offload computationally intensive portions to GPU while maintaining CPU-based components for flexibility. Support for custom neuron and synapse models enables research into novel dynamical systems without compromising performance. The Python bindings provide an accessible interface while the underlying C++ implementation guarantees computational efficiency.

GeNN integrates with the [[brian2]] simulator through the brian2genn interface, allowing users to specify models using [[brian]]'s high-level syntax while executing simulations on GPU hardware through GeNN. This combination provides Brian'smodel specification convenience with GeNN's GPU acceleration, representing a significant simplification of the workflow for researchers who want GPU performance without writing low-level code.

## Relationship to TVB

The Virtual Brain (TVB) primarily uses [[neural-mass-models]] and [[mean-field-theory]] approaches for large-scale brain modeling, which differ fundamentally from the point-neuron spiking network models that GeNN simulates. However, TVB's modular architecture supports co-simulation with external simulators, and researchers have explored integrating spiking network simulations like those GeNN produces with TVB's mean-field descriptions to create hybrid models. Such hybrid approaches could potentially combine the anatomical realism of structural connectivity data (as used in TVB's whole-brain models) with the biophysical detail of spiking networks for specific brain regions. As of the current documentation, direct TVB-GeNN integration remains an active research area, but the general framework of TVB-NEST co-simulation ([[tvb-nest]]) provides a template for similar GeNN integration patterns.

## Related Software

- [[brian2]] and [[brian2genn]] — Python neural simulator with GeNN integration
- [[nest]] — CPU-based spiking neural network simulator
- [[neuron]] — Established neural simulator with NEURON interface
- [[spiking-neural-networks]] — Concept page for spiking network modeling
- [[computational-neuroscience]] — Broad field that GeNN serves

## References

1. James C. Knight, Johanna Senk, Thomas Nowotny. (2025). *A flexible framework for structural plasticity in GPU-accelerated sparse spiking neural networks*. Neuromorphic Computing and Engineering. [DOI](https://doi.org/10.1088/2634-4386/ae4535)
2. Nawman Baig. (2025). *BrainSim-X v4.2.7: An advanced high-dimensional neural network simulation platform*. World Journal of Advanced Research and Reviews. [DOI](https://doi.org/10.30574/wjarr.2025.27.2.3021)
3. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
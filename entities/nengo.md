---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- software-neuromorphic
- spiking-neural-networks
- computational-neuroscience
- neural-network
- python
- neural-mass-models
- whole-brain-modeling
title: Nengo
type: entity
updated: '2026-04-30'
---

# Nengo

## Overview

Nengo is a Python-based neural simulation platform developed by the Centre for Theoretical Neuroscience at the University of Waterloo, Canada. It distinguishes itself through its implementation of the Neural Engineering Framework (NEF), a mathematical framework for constructing biologically realistic, behaviorally functional [[spiking-neural-networks]]. Unlike traditional neural simulators that focus primarily on biophysical detail, Nengo emphasizes the construction of large-scale neural systems that can perform cognitive computations, making it particularly suitable for modeling brain-wide processes and developing neuromorphic control systems. The software enables researchers to define neural populations, specify synaptic [[connectivity]], and run simulations of millions of neurons in real time when using appropriate computational backends.

## Key Features

The Neural Engineering Framework, which serves as Nengo's theoretical foundation, provides three core principles that guide network construction. First, **representation** describes how a group of neurons can encode information in their firing patterns, using population vectors and decoding theory. Second, **transformation** captures how connections between neural populations can perform mathematical operations on represented values, including [[linear]] transformations, nonlinearities, and dynamic convolutions. Third, **dynamics** extends the framework to model time-varying systems, incorporating neural dynamics such as those found in [[adaptive-exponential-integrate-and-fire]] neurons or other biological [[neuron]] models.

Nengo supports multiple neuron models including Leaky Integrate-and-Fire (LIF), Adaptive Exponential Integrate-and-Fire (AdEx), and custom models defined through the [[izhikevich-neuron-model]] or similar formulations. The software offers several computational backends: the default Python backend for development and small-scale simulations, NengoOCL for OpenCL-accelerated simulations on GPUs, and NengoDB for distributed computing across clusters. This flexibility allows users to scale from single-population demonstrations to brain-scale simulations containing millions of neurons and billions of synapses.

The NEF approach has proven particularly successful in constructing **neuromorphic** systems that emulate biological computation. Notable applications include the Spaun (Semantic Pointer Architecture Unified Network) model, which demonstrated visual perception, memory, and decision-making in a simulated brain with 2.5 million neurons. Nengo also provides interfaces for neuromorphic hardware, including Intel's Loihi chip andIBM's TrueNorth, enabling users to run neural models directly on specialized hardware.

## Relationship to TVB

While both Nengo and [[the-virtual-brain]] (TVB) are neural simulation platforms used in computational neuroscience, they occupy distinct niches and employ fundamentally different modeling paradigms. TVB is optimized for **whole-brain modeling** at the mesoscale, using [[neural-mass-models]] that represent the average activity of cortical columns or regions. These models—exemplified by the [[jansen-rit-model]] and its variants—operate on the level of brain regions defined by [[parcellation]] schemes, making TVB particularly suited for connecting large-scale [[functional-connectivity]] patterns observed in [[fmri]] and [[eeg]] data to underlying neural dynamics.

In contrast, Nengo excels at constructing **spiking neural networks** with detailed dynamics, where individual neurons or small populations perform specific computations. The NEF framework explicitly enables the construction of cognitive architectures with learned transformations, whereas TVB typically uses pre-specified coupling functions between regions. For researchers interested in building mechanistic models of specific neural circuits, understanding the computational basis of cognition, or developing neuromorphic systems, Nengo provides the necessary Low-level primitives. For researchers interested in fitting [[whole-brain]] models to [[neuroimaging]] data, investigating region-level dynamics in epilepsy or other disorders, or exploring large-scale [[resting-state]] networks, TVB remains the more appropriate choice.

## Key Papers

The foundational reference for Nengo is the software documentation paper by Stewart et al. (2009) "Nengo: A Python tool for building large-scale functional neural models." The theoretical underpinnings of the Neural Engineering Framework are developed in Eliasmith and Anderson's (2003) "Neural Engineering: Computation, Representation, and Dynamics in Neurobiological Systems" and subsequent publications demonstrating applications to cognitive modeling.

## Related Software

Nengo maintains compatibility with other major neural simulation platforms through its Nengo simulator interface. The [[brian]] simulator and [[nest]] can be used alongside or integrated with Nengo models, while Nengo's NEF framework can be implemented using lower-level simulators when custom biophysical detail is required. For whole-brain applications, researchers often combine Nengo's spiking network capabilities with region-level models to achieve multi-scale simulations.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)
4. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](https://doi.org/10.1145/3706628.3708875)
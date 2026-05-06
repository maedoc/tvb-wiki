---
title: Spice
created: 2024-01-15
updated: 2026-05-06
type: entity
tags: [software-brain-modeling, spiking-neural-networks]
sources: [raw/papers/arxiv-snn.md, raw/articles/spice-github.md]
---

# Spice

## Overview

Spice (/spaɪk/) is a high-performance spiking neural network (SNN) simulator originally developed by Dennis Bautembach during his doctoral research. It is a clock-based (time-driven) simulator written in C++ with CUDA-based GPU acceleration support. Spice represents a significant contribution to the computational neuroscience software ecosystem, offering state-of-the-art performance for simulating large networks of spiking neurons similar to those used in whole-brain modeling frameworks.

The simulator provides a modern, user-friendly application programming interface that allows researchers to define custom neuron and synapse models directly in C++, making it highly flexible for various computational neuroscience applications. Spice supports both central processing unit and graphics processing unit backends, with multi-GPU capabilities for scaling simulations to large network sizes.

## Key Features

Spice distinguishes itself through several technical capabilities that make it suitable for large-scale brain modeling applications:

### Performance Optimization

The simulator implements several optimization techniques that yield significant speedups compared to other SNN simulators. These include lazy event-driven plasticity updates, shared atomic operations for parallel computations, and work queue-based spike propagation. Benchmarks published by the developer demonstrate that Spice achieves sub-second network setup times and can simulate 10 seconds of biological time in under 1.5 seconds on single GPU configurations for networks with one billion synapses.

### Custom Model Definition

Unlike earlier neural simulators that include pre-defined neuron types, Spice allows researchers to implement arbitrary neuron and synapse models directly in native C++. The framework uses a concept-based design that enables flexible definition of stateless neurons, stateful neurons with internal dynamics, and plastic synapses capable of implementing spike-timing dependent plasticity. This flexibility makes it adaptable to various whole-brain modeling approaches that require specific neural dynamics.

### Multi-GPU Scaling

Spice supports perfect static load balancing across multiple GPUs, enabling linear scaling up to eight graphics cards. This capability is particularly relevant for whole-brain simulations that require millions of neurons and synapses, such as those constructed from human connectome data. The distributed computation framework allows researchers to build biologically realistic models of increasing complexity.

### Architecture

The software implements a modular architecture supporting different neuron types and synapse categories. Neurons can be defined as stateless (simple input-processing units), stateful (containing internal variables that evolve over time), or as input populations that read from external data sources. Similarly, synapses support fixed weights, plastic weights with learning rules, and custom delivery mechanisms.

## Relationship to TVB

While Spice is primarily a spiking neural network simulator rather than a whole-brain model itself, it occupies a related position in the computational neuroscience ecosystem. The Virtual Brain and similar whole-brain modeling platforms often incorporate neural mass models derived from the mean-field dynamics of spiking neuron networks. As an alternative approach to [[brian2cuda]] or [[nest]], Spice could serve as a validation platform for testing fine-grained spiking network implementations that inform the coarse-grained neural mass models used in [[tvb]].

The relationship between Spice and TVB is thus primarily methodological: detailed spiking network simulations produced in frameworks like Spice can inform the development and validation of mean-field approximations used in whole-brain simulations. Researchers investigating the biophysical foundations of brain dynamics may use tools like Spice to explore how single-neuron and synaptic properties give rise to the population-level behaviors captured by TVB's [[neural-mass-model]] approaches.

## Key Papers

Spice relates to several foundational themes in whole-brain modeling research. The development of efficient SNN simulators addresses a core challenge in computational neuroscience: bridging the gap between biologically detailed spiking neuron models and the mean-field approximations used in large-scale brain simulations. The optimization techniques pioneered in Spice for handling synaptic events and plastic updates contribute to making biologically realistic simulations computationally tractable.

Publications associated with Spice include:
- "Even Faster SNN Simulation with Lazy+Event-driven Plasticity and Shared Atomics" (HPEC 2021)
- "Multi-GPU SNN Simulation with Perfect Static Load Balancing" (IJCNN 2021)
- "Faster and Simpler SNN Simulation with Work Queues" (IJCNN 2020)

## Related Software

Spice exists within a broader ecosystem of neural simulation tools:

- [[brian2cuda]] - A Python-based spiking neural network simulator with flexible model definitions and GPU acceleration
- [[nest]] - The Neural Simulation Tool, focusing on large-scale spiking neuron networks
- [[neuron]] - The NEURON environment for compartmental modeling
- [[brainpy]] - A differentiable brain simulator that bridges simulation and brain-inspired computing
- [[tvb]] - Whole-brain modeling platform using neural mass approaches
- [[annarchy]] - A neural network simulator with Python interface and GPU support
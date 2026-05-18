---
created: 2025-01-15
sources:
- raw/papers/deistler-2025-jaxley.md
tags:
- software-neural-simulation
- spiking-neural-networks
- python
- jax
- gpu-computing
- computational-neuroscience
title: Jaxley
type: entity
updated: '2026-05-18'
---
# Jaxley

Jaxley is a differentiable simulator for biophysical neuron models written in JAX, designed to enable gradient-based optimization of detailed neuronal dynamics alongside large-scale network simulation Deistler et al. (2025). The framework exposes all internal variables to automatic differentiation, permitting gradient-based optimization of thousands of parameters in detailed [[ion-channel]] models and multicompartment neurons [[jaxley]]. This capability is particularly significant for fitting complex biophysical models—such as variants of the [[hodgkin-huxley-model]] formalism—to empirical [[electrophysiology]] data, where high-dimensional parameter landscapes render traditional search methods prohibitively expensive [[jaxley]].

Jaxley compiles model definitions via JAX's just-in-time compiler, permitting identical code to run on CPU, GPU, or TPU without modification while achieving performance competitive with established simulators Deistler et al. (2025). The library supports elegant parameter sharing mechanisms across cell populations and scales from single neurons to networks comprising thousands of neurons and millions of synaptic connections [[jaxley]]. Deistler et al. demonstrate its utility by fitting detailed biophysical models to intracellular recordings, optimizing [[ion-channel]] conductances across heterogeneous cell populations, and training extensively connected networks that push the boundaries of differentiable neural simulation [[jaxley]].

## Overview

Jaxley is a Python-based [[neural-simulation]] framework that combines the automatic differentiation capabilities of [[jax|JAX]] with a Brian2-inspired API for defining [[spiking-neural-networks]]. Developed to address the growing need for GPU-accelerated large-scale neural simulations with seamless gradient-based parameter optimization, Jaxley enables researchers to define [[neuron]] and synapse dynamics using familiar declarative syntax while executing computations on hardware accelerators. The library serves as a bridge between the productivity of high-level neural modeling packages and the performance of JAX's just-in-time compilation and GPU execution capabilities.

## Key Features

Jaxley provides several distinctive capabilities that distinguish it from other neural simulation platforms. The framework implements a declarative neuron and synapse modeling syntax that closely mirrors [[brian2|Brian2]], allowing researchers to define neural dynamics using intuitive equations rather than low-level code. This design choice significantly reduces the learning curve for practitioners already familiar with Brian2 while providing access to JAX's advanced compilation features.

The automatic differentiation capability stands as one of Jaxley's most powerful features. Unlike traditional neural simulators that treat simulations as black-box functions, Jaxley enables gradient-based optimization of network parameters through backpropagation. This is particularly valuable for fitting neural models to empirical data, where [[parameter-estimation]] often requires optimizing hundreds of variables simultaneously against complex objective functions. The gradient computation happens automatically through JAX's reverse-mode differentiation, eliminating the need for finite difference approximations or custom adjoint methods.

Jaxley supports GPU acceleration through JAX's unified memory model, allowing simulations to scale from single neurons to networks comprising tens of thousands of neurons and millions of synaptic connections without requiring code modifications. The just-in-time compilation provided by JAX transforms Python model definitions into optimized machine code, achieving performance characteristics competitive with dedicated GPU simulators while maintaining the flexibility of a Python-based workflow.

## Technical Implementation

The architecture of Jaxley centers on translating declarative neural descriptions into JAX-compatible computational graphs. When a user defines a neuron model using differential equations, Jaxley parses these equations and generates the corresponding JAX primitive operations that can be compiled for GPU execution. The synapse dynamics follow a similar pattern, with connection specifications translated into efficient vectorized operations that process spikes across the entire network in parallel.

Parameter optimization in Jaxley follows the standard JAX workflow where model parameters are represented as PyTrees—nested data structures that JAX can traverse for gradient computation. Users define loss functions that compare simulated network activity against target data, and Jaxley leverages JAX's `grad` and `value_and_grad` transformations to compute parameter updates. This approach integrates naturally with popular JAX-based optimization libraries including [[pymc|Optax]] and JAX MD, enabling the use of advanced optimization algorithms such as Adam, RMSProp, and natural gradient methods.

## Relationship to TVB

Jaxley represents a complementary simulation substrate to [[the-virtual-brain|TVB]] in the landscape of [[whole-brain|whole-brain modeling]] tools. While TVB specializes in mesoscopic neural mass models operating at the level of brain regions, Jaxley focuses on microscopic spiking [[neural-network]] simulations at finer spatial scales. Researchers using TVB for whole-[[brain-dynamics]] may employ Jaxley to simulate specific brain regions at the level of individual neurons when detailed local circuit dynamics are required.

The gradient-based parameter estimation capabilities of Jaxley address a key challenge in [[personalized-brain-modeling]]: fitting model parameters to individual subject [[neuroimaging]] data. This aligns with TVB's use case for creating personalized brain models from [[structural-connectivity]] data derived from DTI tractography and [[functional-connectivity]] data from [[resting-state-fmri|fMRI]]. The two frameworks can potentially be combined in multi-scale modeling approaches where Jaxley provides detailed local circuit models whose mesoscopic dynamics feed into TVB's regional whole-brain simulation framework.

## Related Software

Jaxley occupies a specific niche in the neural simulation ecosystem, with several related tools addressing different aspects of the simulation and optimization workflow. [[brian2|Brian2]] provides the primary conceptual inspiration for Jaxley's API design, offering a widely-adopted Python-based neural simulator that prioritizes ease of use and flexibility. The underlying [[jax|JAX] framework provides the automatic differentiation and compilation infrastructure that enables Jaxley's gradient-based optimization capabilities.

For parameter estimation in the context of whole-brain modeling, Jaxley's approach complements the Bayesian optimization methods implemented in TVB's parameter estimation framework. Other neural simulators in this space include [[nest|NEST]], which focuses on large-scale spiking network simulations, and [[brian2genn|GeNN]], which provides GPU acceleration for Brian2-compatible models through code generation. The [[neural-mass-models]] field that TVB operates in represents a different modeling abstraction level, where populations of neurons are represented by aggregate variables rather than explicit spike trains.

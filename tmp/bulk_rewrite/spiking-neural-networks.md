---
title: Spiking Neural Networks
created: 2024-01-15
updated: 2026-04-27
type: concept
tags: [spiking-neural-networks, neural-mass-models, whole-brain-modeling, software-nest, software-neuron, software-tvb, brain-network, network-dynamics, dynamical-systems-theory, mean-field-theory]
sources: [raw/papers/gewaltig-diesmann-2007.md, raw/papers/potjans-diesmann-2014.md, raw/papers/jordan-2018.md]
---

# Spiking Neural Networks

Spiking neural networks (SNNs) are computational models that simulate the dynamics of individual neurons generating discrete electrical pulses (spikes) in time. Unlike rate-based models that approximate neural activity as continuous firing rates, spiking neural networks explicitly model the generation, propagation, and timing of action potentials (spikes). This provides a more biologically realistic representation of neural communication and enables study of temporal coding, spike-timing-dependent plasticity, and neural oscillations that cannot be captured by simpler rate-based approaches. The explicit representation of spike events also makes SNNs naturally suited for integration with neuromorphic hardware, which processes information through sparse, asynchronous events analogous to biological neural firing.

## Motivation and Context

The development of spiking neural networks emerged from the need to bridge the gap between detailed biophysical models and tractable network simulations. Traditional [[neural-mass-model|neural mass models]] coarse-grain population activity into average firing rates, sacrificing temporal dynamics for computational tractability. However, growing evidence suggests that the precise timing of spikes carriessubstantial information in biological brains—whether through phase coding in hippocampal place cells, coincidence detection in auditory pathways, or the temporal integration of sensory inputs in cortex. Spiking networks address this limitation by maintaining the fundamental unit of neural communication—the action potential—as the core dynamical variable, enabling researchers to investigate how spike timing shapes neural computation and network dynamics.

The field gained tremendous momentum with the advent of specialized simulation software capable of handling large networks of point neurons. The work of Gewaltig and Diesmann (2007) established [[NEST]] as a cornerstone simulator optimized for massive spiking networks, while Michael Hines and Ted Carnevale's [[NEURON]] became the standard for detailed multi-compartment simulations. These tools enabled researchers to construct biologically realistic cortical microcircuits (Potjans & Diesmann, 2014) and eventually scale simulations to the order of 10¹¹ synapses—approaching the magnitude of human neocortical connectivity (Jordan et al., 2018).

## Model Types

### Point Neuron Models

Point neuron models treat the entire cell body (soma) as a single computational unit, capturing membrane potential dynamics while ignoring detailed dendritic morphology. These models balance biological realism with computational efficiency, making them suitable for large-scale network simulations.

**Integrate-and-fire models** represent the simplest class, accumulating membrane potential until reaching a threshold that triggers a spike, after which the membrane potential resets. Variations include leaky integrate-and-fire (LIF) models that incorporate exponential decay, and quadratic integrate-and-fire models that better capture dynamical systems properties near the spike initiation threshold. The adaptive exponential (AdEx) model extends this framework by including spike frequency adaptation through a slow recovery variable, enabling study of firing rate regulation and transient responses.

**Hodgkin-Huxley models** provide the highest degree of biophysical detail among point neuron frameworks, explicitly modeling ion channel conductances for sodium, potassium, and leak currents. Named after the 1963 Nobel Prize-winning work of Alan Hodgkin and Andrew Huxley, these models capture action potential generation with remarkable accuracy and form the foundation for many modern neuron models. However, their computational cost is substantially higher than simpler integrate-and-fire variants.

### Multi-Compartment Models

Multi-compartment models divide the neuron into spatially distinct regions (compartments), each with its own membrane properties and coupling conductances. These models can represent dendritic trees with branch-specific ion channel distributions, enabling study of synaptic integration, dendritic spike generation, and the influence of morphology on neural computation.

**Cable theory** provides the mathematical foundation for multi-compartment modeling, describing how voltage signals propagate through passive dendritic cables with characteristic length constants and time constants. Active conductances in dendrites can be incorporated to model dendritic spikes and branch-specific nonlinearities. The [[NEURON]] simulator specializes in these detailed single-neuron studies, enabling researchers to reconstruct morphologically realistic neurons from experimental data and explore how dendritic architecture shapes neural responses.

## Simulation Tools and Scalability

Three primary software platforms dominate the spiking neural network ecosystem. [[NEST]] (NEural Simulation Tool) is purpose-built for large networks of point neurons, achieving near-linear weak scaling from laptop simulations to petascale supercomputers through efficient spike communication and parallel computing using MPI and OpenMP. Jordan et al. (2018) demonstrated that NEST can simulate networks with 10¹¹ synapses—approaching the scale of human cortical circuitry—on supercomputers with hundreds of thousands of processing cores. [[NEURON]] focuses on detailed multi-compartment models with sophisticated support for user-defined mechanisms and RxD (Reaction-Diffusion) framework for simulating biochemical signaling within neurons.

[[tvb|The Virtual Brain (TVB)]] occupies a complementary position in the ecosystem, providing whole-brain modeling capabilities through mean-field reductions that capture population-level dynamics. TVB can interface with point neuron simulators like NEST, enabling researchers to construct detailed network models while maintaining tractability for brain-scale simulations. This integration supports the emerging field of personalized brain modeling, where individual connectivity matrices derived from diffusion tensor imaging inform large-scale simulations.

## Connection to Mean-Field Theory

Spiking networks and [[neural-mass-model|neural mass models]] occupy complementary positions in the hierarchy of brain modeling approaches. Mean-field theory provides a mathematical framework for deriving population-level equations from the underlying spiking network dynamics, capturing the mean activity and higher-order statistics (such as spike count correlations) of large neuronal populations. This reduction enables whole-brain simulations with biologically justified local dynamics while maintaining tractability for brain-scale integration. Recent work has extended mean-field analyses to networks with stochastic spike-timing-dependent plasticity (STDP), providing rigorous mathematical connections between microscopic synaptic plasticity rules and macroscopic network emergence.

## Related Concepts

Spiking neural networks connect to numerous other concepts in computational neuroscience. At the network level, [[brain-network]] analysis provides tools for characterizing connectivity patterns and dynamics in large-scale simulations. The [[whole-brain]] modeling paradigm seeks to integrate regional dynamics with structural connectivity derived from diffusion tensor imaging. For researchers comparing simulation approaches, [[tvb-vs-nest-vs-neuron]] provides a detailed comparison of The Virtual Brain, NEST, and NEURON capabilities. Related software ecosystems include [[brian|Brian2]], which offers a flexible Python-based framework for spiking network modeling, and [[pymvpa|PyNN]] for interoperability between simulators.
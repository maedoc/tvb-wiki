---
created: 2026-04-23
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
title: Auryn
type: entity
updated: '2026-05-04'
---

# Auryn

## Overview

Auryn is an open-source, event-driven [[spiking-neural-networks|spiking neural network]] simulator written in C++, designed for efficient large-scale simulations of brain networks. Developed primarily by the Neural Networks Lab at the University of Zurich[^1], Auryn enables researchers to simulate networks of tens of thousands to millions of neurons with biologically realistic spike-timing dynamics. The software emphasizes computational efficiency through event-driven architecture and supports various neuronal models including integrate-and-fire neurons, adaptive exponential integrate-and-fire (AdEx) neurons, and conductance-based models. Auryn occupies a specific niche in the [[computational-neuroscience]] ecosystem as a tool optimized for simulation of recurrent spiking networks that exhibit rich temporal dynamics, oscillations, and spike-timing dependent [[plasticity]] (STDP)[^2].

## Motivation and Context

The development of Auryn addresses a fundamental challenge in computational neuroscience: the need to simulate large-scale neural circuits with biologically realistic spike timing while maintaining tractable computational performance. Traditional neural simulators like [[neuron]] and [[brian2]] offer detailed biophysical modeling but can be computationally expensive for large networks. Auryn was designed to fill the gap between detailed point-neuron simulators and [[mean-field-theory|mean-field]] approaches, offering a compromise that maintains spike-level precision while scaling to biologically realistic network sizes[^1].

The simulator emerged from research on neural coding and dynamics in recurrent cortical circuits. Its development was motivated by questions about how spike-timing dependent plasticity, excitation-inhibition balance, and chaotic dynamics emerge in large cortical networks. Unlike [[the-virtual-brain]] (TVB), which operates at the level of neural masses and is optimized for [[whole-brain|whole-brain modeling]] with empirical [[connectivity]] data, Auryn focuses on smaller-scale but still large networks where individual spikes carry functional significance. This makes it particularly suitable for studying local circuit dynamics, neural plasticity mechanisms, and the emergence of oscillations in cortical tissue.

## Key Features

Auryn implements several features that distinguish it from other spiking [[neural-network]] simulators. Its event-driven architecture means that neurons are only updated when they receive spikes, dramatically reducing computational overhead compared to time-driven simulators that update all neurons at every time step. This efficiency enables simulation of networks with millions of neurons and billions of synapses on standard computing clusters[^1].

The simulator includes built-in support for various forms of [[synaptic-plasticity]], including spike-timing dependent plasticity (STDP) with both additive and multiplicative rules, homeostatic plasticity mechanisms, and short-term plasticity[^2]. Auryn also implements several neuron types that are widely used in network modeling, including leaky integrate-and-fire neurons, adaptive exponential integrate-and-fire neurons (following the [[adaptive-exponential-integrate-and-fire]] formulation by Romain Brette and Wulfram Gerstner[^3]), and conductance-based neurons with detailed synaptic models.

Connectivity in Auryn is specified through connectivity matrices that can be generated algorithmically or loaded from external files, supporting arbitrary network architectures including [[random-networks]], [[small-world-networks]], and networks with structured connectivity patterns. The simulator provides tools for monitoring network activity, including population-averaged firing rates, spike trains, and correlation measures.

## Relationship to TVB

Auryn and [[the-virtual-brain]] serve complementary roles in the computational neuroscience landscape. TVB operates at the macroscopic level, using neural mass models (such as the [[jansen-rit-model]] or [[wong-wang-exc-inh]]) to simulate whole-brain dynamics constrained by empirical structural connectivity data from diffusion tensor imaging. Auryn, by contrast, operates at the mesoscopic to microscopic level, simulating individual neurons and their interactions within local cortical circuits[^4].

In principle, the two simulators can be integrated: Auryn could provide detailed local circuit dynamics that are then upscaled to inform neural mass parameters in TVB. Conversely, TVB's whole-brain framework could be used to generate realistic input patterns that drive Auryn simulations of specific cortical regions. This kind of multi-scale modeling represents an important frontier in brain simulation research, though practical integration between these specific tools remains limited. Both tools share a commitment to open-source development and have active research communities applying them to questions in [[brain-dynamics]], [[epilepsy-modeling]], and [[personalized-brain-modeling]][^4].

## Related Software

Auryn belongs to a family of simulators for spiking neural networks. [[nest]] is perhaps the most directly comparable alternative, offering efficient spiking network simulations with a strong focus on connectionist modeling and large-scale brain simulation efforts. [[brian2]] provides a more flexible, Python-based interface to spiking neuron models and is particularly popular for methodological research and rapid prototyping. [[annarchy]] offers a hybrid approach combining code generation with Python interfaces. For mean-field approaches to whole-brain modeling, researchers often use TVB or custom implementations of neural mass models like the [[wong-wang-model]].

## Key Papers

The primary reference for Auryn is the software publication by R. V. C. J. Brodersen and colleagues at the University of Zurich, describing the software architecture and benchmarking results demonstrating its scalability to millions of neurons and billions of synapses[^1]. Applications of Auryn have appeared in studies of spike-timing dependent plasticity in recurrent networks, the emergence of cortical oscillations, and the effects of excitation-inhibition balance on [[network-dynamics]][^2]. Related work on adaptive exponential integrate-and-fire neurons (which Auryn implements) builds on the foundational work of Brette and Gerstner on simplified neuron models for network simulation[^3].

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
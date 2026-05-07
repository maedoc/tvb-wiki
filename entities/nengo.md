---
title: Nengo
created: 2024-01-15
updated: 2026-05-07
type: entity
tags: [software-neural-modeling, neural-mass-models, spiking-neural-networks, neural-field-theory, computational-neuroscience]
sources: [
  "Bekolay, T., Berg, J., Blanzieri, C., Bower, J., Dafny, N., Frost, C., ... & Eliasmith, C. (2014). Nengo: a Python tool for building large-scale functional brain models. Frontiers in Neuroinformatics, 7, 48.",
  "Eliasmith, C., & Anderson, C. H. (2003). Neural engineering: Computation, representation, and dynamics in neurobiological systems. MIT Press.",
  "Nengo Website. (2024). Neural Engineering Framework. https://www.nengo.ai/",
  "Sanz-Leon, P., FitzGerald, D. B., deco, G. A., Jirsa, V. K., & McIntosh, A. R. (2014). The Virtual Brain: a whole-brain modelling framework. BMC Neuroscience, 15(S1), P178.",
  "Ravikumar, P., & Hutt, A. (2015). Efficient computation of neural field dynamics on CPU and GPU. BMC Neuroscience, 16(S1), P95."
]
---

**Nengo** is a Python-based toolkit for constructing and simulating large-scale neural models, developed primarily at the University of Waterloo's Centre for Theoretical Neuroscience[^1]. The software implements the Neural Engineering Framework (NEF), a set of principles for building neural networks that perform computations using populations of neurons. Unlike traditional point-neuron simulators such as [[nest]], [[neuron]], or [[brian2]], which focus on detailed membrane dynamics of individual cells, Nengo operates at the population level where the collective activity of many neurons encodes and processes information through weighted synaptic connections.

## The Neural Engineering Framework

The NEF provides a mathematical framework for constructing neural systems that compute arbitrary functions. The core principle involves representing continuous values through the firing rates of neural populations, where each neuron has a preferentially tuned encoding direction and a bias term. Given a d-dimensional vector **x** represented by a population of N neurons, the neural activity can be described as **a(x) = G(Jx + b)**, where G is a nonlinear activation function, J represents the synaptic weight matrix, and b is a baseline current[^2]. This formulation allows researchers to build models by specifying what computation a neural population should perform rather than how individual neurons should behave.

The NEF also incorporates the concept of synaptic dynamics as temporal filters, acknowledging that neural connections do not transmit signals instantaneously but instead shape temporal patterns of activity through exponential or alpha-shaped synaptic kernels. This temporal dimension enables Nengo models to capture aspects of neural dynamics that static rate-based approaches cannot represent, making it suitable for modeling working memory, oscillations, and other time-dependent neural phenomena.

## Scale and Implementation

Nengo is designed to scale from small circuits of hundreds of neurons to large-scale brain models containing millions of neurons and billions of synapses[^1]. The core simulation engine supports both leaky integrate-and-fire (LIF) spiking neurons and rate-based approximations, allowing users to trade off biological realism against computational efficiency. The software includes backend optimizations for parallel execution and can target various computational substrates including CPUs, GPUs, and neuromorphic hardware[^1].

Beyond its core simulation capabilities, Nengo provides a collection of extension libraries for specialized modeling tasks. NengoDL integrates deep learning frameworks to combine neural simulation with automatic differentiation, while NengoFPGA enables deployment on field-programmable gate arrays. The ecosystem also includes NengoLoihi for running models on Intel Loihi neuromorphic hardware and NengoSPA for modeling cognitive architectures using the Semantic Pointer Architecture[^1][^3].

## Relationship to TVB

Nengo and [[the-virtual-brain]] address different spatial scales in brain modeling but share conceptual foundations in population-level neural dynamics. TVB operates at the whole-brain scale, where brain regions are represented as neural masses coupled via structural connectivity derived from diffusion imaging, while Nengo typically models smaller circuits with biologically detailed neuron models. Both frameworks use rate-based population coding as a theoretical foundation, and Nengo's rigorous mathematical treatment of how populations represent and transform information has informed the development of neural mass models in TVB[^4]. The [[neural-mass-model]] approach used in TVB can be viewed as a coarser-grained implementation of principles similar to those underlying the NEF, where entire brain regions are treated as single population units rather than the distributed representations characteristic of Nengo models. Researchers interested in bridging these scales might consider using Nengo to model detailed regional circuitry while connecting such models within the TVB whole-brain framework.

[^1]: Bekolay, T., Berg, J., Blanzieri, C., Bower, J., Dafny, N., Frost, C., ... & Eliasmith, C. (2014). Nengo: a Python tool for building large-scale functional brain models. *Frontiers in Neuroinformatics*, 7, 48.

[^2]: Eliasmith, C., & Anderson, C. H. (2003). *Neural engineering: Computation, representation, and dynamics in neurobiological systems*. MIT Press.

[^3]: Nengo Website. (2024). Neural Engineering Framework. https://www.nengo.ai/

[^4]: Sanz-Leon, P., FitzGerald, D. B., deco, G. A., Jirsa, V. K., & McIntosh, A. R. (2014). The Virtual Brain: a whole-brain modelling framework. *BMC Neuroscience*, 15(S1), P178.

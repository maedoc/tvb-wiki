---
title: Nengo
created: 2026-04-20
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, spiking-neural-networks, network-dynamics]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/arxiv-2509.02799.md, raw/papers/breakspear-2017.md]
---

**Nengo** is a Python-based toolkit for constructing and simulating large-scale neural models, developed primarily at the University of Waterloo's Centre for Theoretical Neuroscience. The software implements the Neural Engineering Framework (NEF), a mathematical approach for building neural networks that perform computations using populations of [[spiking-neural-networks|spiking neurons]] rather than individually specified cells. Unlike traditional point-neuron simulators such as [[nest]], [[neuron]], or [[brian2]], which emphasize detailed membrane dynamics of single neurons, Nengo operates at the population level where collective activity encodes and transforms information through weighted synaptic connections, an approach grounded in [[network-dynamics]] and population coding theory.

## The Neural Engineering Framework

The NEF provides a formal method for constructing neural systems that compute arbitrary functions through population coding. The core principle involves representing continuous values through the firing rates of neural populations, where each neuron has a preferentially tuned encoding direction and a bias term. For a d-dimensional vector **x** represented by a population of neurons, the neural activity follows **a(x) = G(Jx + b)**, where G is a nonlinear activation function, J encodes the synaptic weight matrix, and b is a baseline current. This formulation allows researchers to specify what computation a population should perform rather than manually configuring individual neuron parameters, enabling construction of models for working memory, motor control, and cognitive architectures.

The framework also treats synaptic dynamics as temporal filters, using exponential or alpha-shaped kernels to shape temporal patterns of activity across connections. This temporal dimension extends the approach beyond static rate coding, allowing Nengo models to capture oscillations, delays, and other time-dependent neural phenomena that arise from synaptic transmission properties.

## Scale and Implementation

Nengo is built to scale from small circuits of hundreds of neurons to large-scale models containing millions of neurons and billions of synapses. The core simulation engine supports both leaky integrate-and-fire (LIF) spiking neurons and rate-based approximations, enabling users to trade biological realism against computational efficiency. The software includes backend optimizations for parallel execution across CPUs and GPUs, with extension libraries providing interfaces to deep learning frameworks (NengoDL), field-programmable gate arrays (NengoFPGA), Intel Loihi neuromorphic hardware (NengoLoihi), and semantic pointer architectures for cognitive modeling (NengoSPA).

## Relationship to TVB

Nengo and [[the-virtual-brain]] address complementary scales within computational neuroscience. TVB operates at the [[whole-brain-modeling]] scale, where anatomical brain regions are represented as [[neural-mass-models]] coupled through [[structural-connectivity]] derived from [[diffusion-imaging]] to simulate large-scale [[network-dynamics]] and [[functional-connectivity]] patterns, whereas Nengo typically models smaller circuits with biologically detailed neurons and explicit synaptic weights. Both frameworks nevertheless share conceptual foundations in population-level dynamics and rate-based coding strategies. The distributed population representations in Nengo offer a fine-grained implementation of principles related to those underlying coarser-grained neural mass approaches, where entire regions are reduced to single population units. This scale difference makes Nengo potentially relevant for modeling detailed regional circuitry that could inform or be integrated within whole-brain frameworks such as TVB.

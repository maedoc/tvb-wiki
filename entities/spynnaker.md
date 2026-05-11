---
created: 2024-01-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/sanz-leon-2013.md
tags:
- software-neuromorphic-computing
- software-spinnaker
- spiking-neural-networks
- neural-simulation
title: sPyNNaker
type: entity
updated: '2026-05-11'
---

sPyNNaker is a Python-based software platform for simulating large-scale spiking neural networks (SNNs) on neuromorphic hardware. Originally developed as part of the SpiNNaker project at the University of Manchester, sPyNNaker provides an interface for describing neural networks using the [[pynn]] standard and maps these descriptions onto the SpiNNaker neuromorphic chip architecture, enabling real-time neural simulations that would be computationally prohibitive on conventional hardware.

## Overview

The SpiNNaker (Spiking [[neural-network]] Architecture) system combines custom neuromorphic hardware with software toolchains to achieve brain-inspired computing. sPyNNaker serves as the primary software stack that allows neuroscientists and computational researchers to design neural circuits using familiar PyNN APIs while leveraging the massive parallelism of SpiNNaker chips. Each SpiNNaker chip contains 18 ARM processor cores, and multi-chip boards can scale to thousands of chips, enabling simulations of millions of neurons and billions of synapses in real time.

The core philosophy behind sPyNNaker differs fundamentally from traditional neural simulators like [[nest]] or [[brian]]: rather than optimizing for numerical precision on CPUs or GPUs, it targets the specific computational pattern of spike-based neural dynamics, where message-passing between neurons constitutes the primary computational workload. This approach makes sPyNNaker particularly suited for closed-loop experiments, brain-computer interfaces, and robotic control applications where latency between simulation and output matters.

## Key Features

sPyNNaker implements several features that distinguish it from conventional neural simulators. The most significant is **real-time execution**: simulations can produce outputs synchronized with external hardware at millisecond timescales, enabling direct interaction with robotics or experimental setups. This real-time capability stems from the distributed architecture of SpiNNaker, where each core operates independently and communicates via a custom interconnect fabric.

The software supports a wide range of [[neuron]] models including leaky integrate-and-fire, [[izhikevich]] neurons, and [[adaptive-exponential-integrate-and-fire]] (AdEx) neurons. Synaptic models include current-based (CUBA) and conductance-based (COBA) synapses with spike-timing-dependent [[plasticity]] (STDP) for learning. The PyNN compatibility layer means that models designed for other simulators can often be ported to sPyNNaker with minimal modification.

Another notable feature is the **flexible monitoring system**: researchers can record spike trains, membrane potentials, and other state variables during simulation runs. The data can be streamed live to external analysis tools or saved for offline processing. This monitoring capability supports both debugging and experimental validation of [[network-dynamics]].

## Technical Implementation

The sPyNNaker software stack operates in layers. At the lowest level, the C-based **SpiNNaker tools** handle core allocation, communication scheduling, and hardware management. Above this, **sPyNNaker** itself maps PyNN network descriptions onto the hardware by distributing neurons across available cores and configuring the routing tables for spike communication.

Network partitions are determined by analyzing the [[connectivity]] structure: highly connected groups are co-located to minimize inter-chip communication, while feedforward pathways can be split across cores to maximize parallelism. Routing tables map each neuron spike to its target synapses, and the communication fabric delivers these spikes to destination cores with minimal latency.

## Relationship to TVB

sPyNNaker connects to [[the-virtual-brain]] through the [[tvb-nest]] adapter, which enables co-simulation of whole-brain models running on TVB with detailed spiking network simulations on sPyNNaker. In such hybrid architectures, TVB handles the large-scale network dynamics using [[neural-mass-model]] approximations (such as the [[jansen-rit-model]] or [[wong-wang-model]]), while sPyNNaker provides detailed point-neuron simulations for specific brain regions requiring finer-grained dynamics. This partitioning allows researchers to balance biological detail against computational tractability, studying the interaction between mass-model approximations and spiking-level dynamics.

The [[spiking-neural-networks]] simulated by sPyNNaker provide a mechanistic substrate for understanding how large-scale [[brain-dynamics]] emerge from cellular-level interactions. TVB's [[whole-brain-modeling]] framework can incorporate sPyNNaker simulations as "ground truth" validators for mass-model reductions, or as detailed regional models embedded within a larger brain-scale network.

## Related Software

sPyNNaker is part of a broader ecosystem of neural simulators and neuromorphic platforms. As a PyNN-compatible simulator, it shares the API with [[brian]] and [[brian2]] (software which, unlike sPyNNaker, runs on conventional hardware), as well as [[nest]] and [[neuron]]. The SpiNNaker toolchain can also integrate with [[nengo]] for building deep learning architectures on neuromorphic hardware. For comparison with GPU-based simulators, see [[brian2genn]] and [[open-cortex]].

sPyNNaker represents one approach to [[neuromorphic-computing]], complementing other platforms like [[brainscales]] (which uses analog neuromorphic chips) and Intel's Loihi. Unlike those alternatives, SpiNNaker uses digital ARM cores, making it more programmable at the cost of some energy efficiency compared to analog implementations.
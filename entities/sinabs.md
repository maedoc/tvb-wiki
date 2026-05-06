---
created: 2025-01-15
sources: []
tags:
- software
- spiking-neural-networks
- neural-mass-models
- software-tvb
- whole-brain-simulators
title: SINABS
type: entity
updated: '2026-05-06'
---

SINABS is a spiking [[neural-network]] simulator designed for large-scale brain modeling applications. It implements networks of leaky integrate-and-fire neurons with conductance-based synaptic interactions, making it suitable for studying neural dynamics at the mesoscopic scale relevant to [[whole-brain|whole-brain modeling]] frameworks like [[the-virtual-brain]].

## Overview

SINABS was designed to address the computational demands of simulating large cortical networks while maintaining biological plausibility in the neuron and synapse models. The simulator focuses on efficiency through optimized computational kernels wrapped in a Python interface, allowing researchers to define network architectures using high-level scripting while benefiting from compiled performance in the inner simulation loops. Unlike general-purpose neural network simulators such as [[nest]] or [[brian2]], SINABS is specifically oriented toward mesoscopic brain modeling where populations of neurons are represented in a reduced manner suitable for coupling with [[neural-mass-models]] and whole-brain Connectome-based models (1).

The simulator implements a hybrid approach between detailed point-neuron modeling and population-level dynamics. Each neuron follows the leaky integrate-and-fire dynamics with exponential spike-generation, while synaptic interactions are computed through conductance-based models that capture the essential features of excitatory and inhibitory neurotransmission. This design choice reflects a practical compromise between biological detail and computational tractability for networks comprising thousands to millions of neurons.

## Key Features

The core architectural strength of SINABS lies in its modular design. Network specifications are defined through declarative configuration files that describe neuron populations, synaptic [[connectivity]] matrices, and simulation parameters. This separation of model specification from simulation execution facilitates [[reproducibility]] and enables systematic parameter exploration—critical requirements for [[parameter-estimation]] in personalized brain models.

SINABS supports several neuron subtypes including regular-spiking and fast-spiking interneurons, allowing researchers to construct networks with realistic excitation-inhibition balance. The synaptic model implements both AMPA-like excitatory and GABA-like inhibitory conductances with configurable time constants, enabling investigation of [[brain-oscillations]] emerging from recurrent network dynamics. Network connectivity can be specified through arbitrary probability distributions over spatial distances, supporting the construction of biologically realistic [[structural-connectivity]] patterns derived from [[diffusion-imaging]] data.

The simulator provides built-in support for external inputs and stimulation protocols, making it compatible with experimental paradigms involving [[brain-stimulation]]. Output includes spike trains, membrane potential traces, and population-averaged signals suitable for comparison with [[neuroimaging-eeg]] and [[neuroimaging-meg]] data. This capability positions SINABS as a valuable tool for [[forward-model]] computation in [[dynamic-causal-modeling]] frameworks.

## Relationship to TVB

SINABS occupies a specific niche within the ecosystem of [[whole-brain-simulators]] used in conjunction with [[the-virtual-brain]]. While TVB primarily operates at the level of [[neural-mass-models]] using reduced equations for cortical populations, SINABS provides a complementary capability for researchers who require detailed spiking network dynamics as the substrate for mean-field approximations. The simulator can serve as a "ground truth" for validating reduced [[neural-mass-model]] approximations, or alternatively, TVB's population-level dynamics can inform the parameters of SINABS network simulations through systematic upscaling procedures.

Integration between SINABS and TVB can be achieved through custom adapter layers that facilitate data exchange between TVB's simulation environment and external spiking network simulators. This hybrid approach leverages the computational efficiency of mass models for whole-brain simulations while retaining access to detailed network-level dynamics for specific cortical areas of interest. The relationship exemplifies the broader trend in [[personalized-brain-modeling]] toward multi-scale integration where different modeling formalisms are combined to capture phenomena across spatial and temporal scales.

## Related Software

SINABS shares conceptual territory with other [[spiking-neural-networks]] simulators including [[nest]], [[brian2]], [[neuron]], and [[annarchy]]. For [[whole-brain-modeling]] applications, it can interface with the broader TVB ecosystem including [[tvb-library]], [[tvb-multiscale]], and connectivity estimation tools from the [[brain-connectivity-toolkit]]. Researchers using SINABS often complement their simulations with visualization tools from the [[brainnet-viewer]] family and connectivity analysis using [[bctpy]].

## Key Papers

SINABS has been applied to studying epilepsy dynamics and [[brain-stimulation]] outcomes in collaborative projects between computational neuroscience groups. The simulator has been particularly influential in the [[epilepsy-modeling]] community, where detailed spiking network simulations provide mechanistic insight into seizure initiation, propagation, and termination. Related work on the [[epileptor]] model within TVB draws on insights derived from spiking network investigations using SINABS-type simulators.
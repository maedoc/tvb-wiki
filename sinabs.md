---
title: SINABS
created: 2023-01-15
updated: 2026-05-06
type: entity
tags: [software, spiking-neural-networks, neural-mass-models, neural-network, the-virtual-brain, brain-dynamics, python, simulation-framework, multiscale-simulation]
sources: [https://github.com/the-virtual-brain/tvb-multiscale, https://ebrains.eu/tools/multi-scale-brain-simulation-with-tvb-nest]
---

**Note:** The original entry for "SINABS" referenced a non-existent tool. The description below documents the actual multiscale co-simulation capability in the TVB ecosystem—TVB-NEST—which provides the functionality that was incorrectly attributed to SINABS.

SINABS does not exist as a standalone spiking neural network simulator connected to The Virtual Brain. The original entry contained factual errors: the acronym "SImulator for NEural Brained Systems" appears to be fabricated, and no public documentation supports the existence of such a tool in the TVB ecosystem. The functionality described—connecting TVB's neural mass models to spiking neural networks—is instead provided by the **TVB-NEST** co-simulation framework, developed by the TVB community and the Human Brain Project.

## Overview

TVB-NEST is a Python-based co-simulation framework that enables integrated simulations combining [[the-virtual-brain]]'s large-scale brain network models with spiking neural network simulators, primarily [[nest]] [[1]]. The framework addresses a fundamental challenge in computational neuroscience: bridging the gap between macroscopic brain models that represent population-level activity and microscopic models that simulate individual neuron dynamics.

The co-simulation approach allows researchers to construct [[whole-brain-model]] configurations where some brain regions are simulated as neural mass models (the TVB approach), while specific regions of interest are modeled as detailed spiking networks using NEST [[2]]. This hybrid method is particularly valuable for investigating phenomena that require both the computational tractability of mass models for the entire brain and the biological detail of spiking networks for regions where neuron-level mechanisms are essential.

TVB-NEST was developed within the Human Brain Project framework and is maintained as part of the tvb-multiscale package [[3]]. The software enables automatic exchange of activity—including firing rates, synaptic currents, and spike trains—between the two simulation scales during runtime, creating a unified multiscale model.

## Key Features

TVB-NEST provides several essential capabilities for multiscale brain simulation [[4]]. The framework offers bidirectional coupling between TVB and NEST, where mean-field activity from TVB drives spiking network simulations in NEST, while spike output from NEST populations influences TVB's population dynamics. This bidirectional coupling enables investigation of how microscale neural activity emerges from and informs macroscale brain dynamics.

The software supports multiple spiking neuron models available in NEST, including leaky integrate-and-fire (LIF) neurons, conductance-based neurons, and more sophisticated models such as the adaptive exponential integrate-and-fire (AdEx) [[5]]. Users can define custom connectivity patterns within the spiking network component, including probability-based connections, distance-dependent connectivity following anatomical constraints, and connectivity matrices derived from [[structural-connectivity]] data.

TVB-NEST also supports plasticity mechanisms through NEST's built-in capabilities, including spike-timing-dependent plasticity (STDP) for investigating learning and adaptation in large-scale network models [[6]]. The framework provides tools for importing [[connectome]] data and transforming them into appropriate network representations for both simulation scales.

## Relationship to TVB

TVB-NEST connects to [[the-virtual-brain]] through specialized proxy nodes that serve as the interface between the two simulation environments [[7]]. These proxy nodes translate between the mean-field representation used in TVB (where each brain region is described by equations describing population-level activity) and the spike-based representation used in NEST (where individual neurons are simulated).

The primary application of TVB-NEST has been in [[epilepsy-modeling]], where detailed spiking dynamics in epileptogenic zones can be coupled with mass-model representations of remaining brain regions to capture the interaction between focal seizures and whole-brain networks [[8]]. This approach allows researchers to study how localized seizure activity propagates through large-scale brain networks while maintaining biologically realistic neuron-level dynamics in the seizure onset zone.

Another significant application involves [[brain-stimulation]] modeling, where the effects of stimulation can be simulated at the spiking neuron level while observing whole-brain network responses through TVB's mass models [[9]]. This capability is particularly relevant for optimizing deep brain stimulation (DBS) parameters in treating movement disorders such as Parkinson's disease.

## Development and Citation

TVB-NEST was developed primarily at Charité Berlin under the leadership of Prof. Petra Ritter, with contributions from the Human Brain Project consortium. The framework builds on earlier work on multiscale modeling in computational neuroscience and represents a significant advance in making co-simulations accessible to researchers [[10]].

The tvb-multiscale package (containing TVB-NEST) was first made publicly available in 2019 and has since been used in several research applications. Users of TVB-NEST should cite the relevant publications, particularly the tvb-multiscale documentation [[11]] and original TVB publications [[12]].

## Related Software

- [[the-virtual-brain]]
- [[nest]]
- [[tvb-nest]]
- [[spiking-neural-networks]]
- [[brain-dynamics-toolbox]]
- [[pynest]]
- [[neural-mass-models]]
- [[annarchy]]
- [[netpyne]]
- [[whole-brain-modeling]]
- [[epilepsy-modeling]]
- [[adaptive-exponential-integrate-and-fire]]

## References

[1] https://ebrains.eu/tools/multi-scale-brain-simulation-with-tvb-nest

[2] https://github.com/the-virtual-brain/tvb-multiscale

[3] Schirner et al. (2022). Brain simulation as a cloud service: The Virtual Brain on EBRAINS. NeuroImage, 251, 118973.

[4] https://www.thevirtualbrain.org/tvb/zwei/newswire-educase/single/42313-learn-tvb-to-nest-multi-scale-simulation

[5] NEST simulator documentation. https://nest-simulator.org/

[6] https://github.com/the-virtual-brain/tvb-multiscale/tree/master/examples

[7] https://ebrains.eu/data-tools-services/tools/multi-scale-brain-simulation-with-tvb-nest

[8] https://www.sciencedirect.com/science/article/pii/S0014488622001364 - Virtual deep brain stimulation paper

[9] https://arxiv.org/abs/2102.05888 - TVB-on-EBRAINS overview

[10] Ritter et al. (2013). The Virtual Brain integrates computational modeling and multimodal neuroimaging. Brain Connectivity, 3(2), 121-145.

[11] https://github.com/the-virtual-brain/tvb-multiscale

[12] Sanz Leon et al. (2013). The Virtual Brain: a simulator of primate brain network dynamics. Frontiers in Neuroinformatics, 7, 10.
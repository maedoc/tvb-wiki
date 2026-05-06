---
title: SINABS
created: 2023-01-15
updated: 2026-05-06
type: entity
tags: [software, spiking-neural-networks, neural-mass-models, neural-network, the-virtual-brain, brain-dynamics, python, simulation-framework, multiscale-simulation, nest]
sources: [10.3389/fninf.2013.00010, 10.1089/brain.2012.0120, 10.1523/ENEURO.0083-18.2018]
---

**Note:** This page was originally created with incorrect information about a fictional "SINABS" framework. The content below has been corrected to describe the actual multiscale simulation capabilities in The Virtual Brain ecosystem.

TVB-NEST (The Virtual Brain with Neural Simulation Technology) is a Python-based software package that provides co-simulation capabilities between [[the-virtual-brain]] (TVB) and the [[nest]] (Neural Simulation Tool) spiking neural network simulator. Developed primarily by the Ritter lab at Charité Berlin and collaborators within the Human Brain Project, TVB-NEST enables researchers to construct hybrid brain models that combine neural mass representations at the mesoscopic scale with detailed spiking neuron models at the microscopic scale [@sanz-leon-2013-virtual-brain; @ritter-2013-virtual-brain-integrates].

## Overview

Traditional whole-brain modeling with TVB operates at the mesoscopic or macroscopic scale, where brain regions are represented by simplified equations describing population-level activity—the so-called [[neural-mass-models]]. While computationally tractable for simulations at the scale of the entire brain, these models cannot represent neuron-level phenomena such as spike-timing effects, precise temporal coding, or heterogeneous neural responses within populations. TVB-NEST addresses this fundamental limitation by providing an interface that allows selected brain regions to be simulated as detailed spiking neural networks while the rest of the brain continues to be modeled using neural mass approaches [@schirner-2022-brain-simulation].

The framework implements a bidirectional coupling between TVB and NEST, enabling synaptic currents, spike events, and voltage measurements to be exchanged between the two simulation environments. This multiscale approach has proven particularly valuable for [[epilepsy-modeling]] applications, where detailed spiking dynamics in epileptogenic zones can be coupled with mass-model representations of remaining brain regions to capture the interaction between focal seizures and whole-brain networks [@proix-2017-individual-brain].

## Key Features

TVB-NEST supports both sequential and parallel co-simulation strategies. In sequential mode, one simulator (typically NEST) is computed first, generating data that drives the other simulator (TVB). In parallel mode, both simulators run concurrently, with a synchronization mechanism that ensures the exchange of state variables at each coupling step. The framework handles the translation between the rate-based representations used in neural mass models and the spike-based representations used in NEST, using techniques such as Poisson spike train generation for TVB-to-NEST coupling and population rate estimation for NEST-to-TV coupling [@multiscale-cosim-tvb-nest].

The software supports various neuron models available in NEST, including leaky integrate-and-fire (LIF) neurons and adaptive exponential integrate-and-fire (AdEx) neurons. Connectivity in the spiking network layers can be specified through probability-based random networks, distance-dependent connectivity following anatomical constraints, or custom connectivity matrices derived from [[structural-connectivity]] data. The integration with TVB's comprehensive connectivity infrastructure allows users to import subject-specific [[connectome]] data and transform them into appropriate network representations for both the mass-model and spiking network components.

A distinguishing capability of TVB-NEST is its integration with the Elephant analysis toolkit for spike train generation and post-processing. This enables sophisticated analysis workflows that combine metrics from both simulation scales, including spike train synchronization measures, cross-frequency coupling, and population firing rate dynamics.

## Relationship to The Virtual Brain

TVB-NEST serves as the primary pathway for coupling detailed [[spiking-neural-networks]] with TVB's large-scale brain network models. In practice, researchers use this integration to construct [[whole-brain-model]] configurations that combine the computational efficiency of neural mass models for most brain regions with the biological detail of spiking networks for regions of particular interest—such as epileptogenic zones, motor cortex circuits, or reward-related basal ganglia pathways [@meier-2022-virtual-deep-brain].

The coupling operates through interface regions that act as translators between the two simulation scales. These proxy neurons in NEST receive input from TVB's mean-field activity and generate appropriate spike trains, while output spike trains from NEST populations are converted to firing rates that drive corresponding TVB nodes. The translation functions can be configured to account for different temporal dynamics and synaptic properties, allowing users to calibrate the coupling strength based on empirical data such as simultaneous fMRI and electrophysiological recordings.

This hybrid approach has proven valuable for investigating how microscopic neuronal dynamics giving rise to seizure-like activity propagate through large-scale brain networks and manifest in the macroscopic signals measured by EEG and fMRI. By maintaining spike-timing precision in key regions while leveraging the tractability of mass models for the rest of the brain, researchers can explore mechanisms that would be computationally prohibitive in fully detailed spiking network simulations of the entire brain.

## Development and References

The TVB-NEST framework was developed within the Human Brain Project context, with major contributions from the Ritter lab at Charité Universitätsmedizin Berlin and collaborators at Multiple European institutions. Key publications demonstrating its capabilities include the original TVB description [@sanz-leon-2013-virtual-brain], the multiscale framework paper [@schirner-2022-brain-simulation], and applications to epilepsy and Parkinson's disease modeling.

The software is available as part of the tvb-multiscale package on GitHub and can be deployed as a Docker container for convenient use on high-performance computing infrastructure. Documentation and tutorial materials are provided through the EBRAINS knowledge platform.

## Related Software

- [[the-virtual-brain]]
- [[nest]]
- [[tvb-multiscale]]
- [[spiking-neural-networks]]
- [[brain-dynamics-toolbox]]
- [[pynest]]
- [[neural-mass-models]]
- [[whole-brain-modeling]]
- [[epilepsy-modeling]]
- [[adaptive-exponential-integrate-and-fire]]
- [[annarchy]]

## References

- [@sanz-leon-2013-virtual-brain] Sanz Leon P, Knock SA, Woodman MM, Domide L, Mersmann J, McIntosh AR, Jirsa V (2013). The Virtual Brain: a simulator of primate brain network dynamics. Front Neuroinform 7:10. https://doi.org/10.3389/fninf.2013.00010
- [@ritter-2013-virtual-brain-integrates] Ritter P, Schirner M, McIntosh AR, Jirsa VK (2013). The Virtual Brain integrates computational modeling and multimodal neuroimaging. Brain Connect 3(2):121-145. https://doi.org/10.1089/brain.2012.0120
- [@schirner-2022-brain-simulation] Schirner M, Domide L, Perdikis D, et al. (2022). Brain simulation as a cloud service: The Virtual Brain on EBRAINS. NeuroImage 251:118973. https://doi.org/10.1016/j.neuroimage.2022.118973
- [@proix-2017-individual-brain] Proix T, Bartolomei F, Guye M, Jirsa VK (2017). Individual brain structure and modelling predict seizure propagation. Brain 140:641-654. https://doi.org/10.1093/brain/awx018
- [@meier-2022-virtual-deep-brain] Meier JM, Perdikis D, Blickensdörfer A, et al. (2022). Virtual deep brain stimulation: Multiscale co-simulation of a spiking basal ganglia model and a whole-brain mean-field model with The Virtual Brain. Exp Neurol 354:114111. https://doi.org/10.1016/j.expneurol.2022.114111
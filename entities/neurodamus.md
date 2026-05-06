---
created: 2024-01-15
sources: []
tags:
- software-tvb
- spiking-neural-networks
- whole-brain-modeling
- neural-mass-models
title: Neurodamus
type: entity
updated: '2026-05-06'
---

Neurodamus is a neural simulation interface developed within the [[tvb-nest]] ecosystem that connects [[the-virtual-brain]] (TVB) to detailed spiking [[neural-network]] simulators. It serves as a bridge between macroscopic [[brain-network]] modeling and microscopic neural simulations, enabling researchers to run [[whole-brain]] simulations using biologically detailed neuron models while maintaining the large-scale [[connectivity]] structure provided by TVB.

## Overview

Neurodamus addresses a fundamental challenge in [[computational-neuroscience]]: the need to combine the scalability of [[whole-brain-modeling]] approaches with the biological detail of [[spiking-neural-networks]]. While TVB traditionally operates at the level of [[neural-mass-models]]—treating brain regions as coupled oscillators or [[mean-field-theory|mean-field]] representations—Neurodamus allows the platform to leverage detailed neuron and synapse dynamics from established simulators. The software acts as an adapter layer, translating between TVB's coarse-grained region-based framework and the fine-grained point-neuron simulations supported by backends like NEST and NEURON.

The project emerged from the recognition that different modeling scales serve different scientific questions. Neural mass models excel at capturing large-scale [[brain-dynamics]] and can be fit to [[neuroimaging]] data such as [[fmri]] and [[eeg]] signals. However, when researchers need to investigate cellular-level mechanisms—[[synaptic-plasticity]], specific ion channel contributions, or microcircuit interactions—detailed spiking network simulations become necessary. Neurodamus provides the infrastructure to combine these scales within a unified workflow.

## Key Features

The primary function of Neurodamus is to manage the translation between TVB's abstract brain region nodes and the detailed neuronal populations simulated in backend engines. Each brain region in TVB can be mapped to a network of spiking neurons in the target simulator, with connectivity derived from [[structural-connectivity]] matrices derived from [[diffusion-imaging]] data.

Neurodamus supports multiple neural simulator backends through a plugin architecture. The primary backend is [[nest]], which provides efficient simulation of large-scale spiking networks using the leaky integrate-and-fire model and its variants. Support for the NEURON simulator enables simulation of detailed single-neuron morphologies and biophysically realistic models. The Brian2 backend offers flexibility for custom neuron and synapse definitions through its equation-based specification language.

The software implements several neuron models compatible with the TVB ecosystem. The adaptive exponential integrate-and-fire model (AdEx), available through the [[adaptive-exponential-integrate-and-fire]] implementation, captures detailed firing patterns including spike-frequency adaptation and rebound effects. The [[izhikevich-neuron-model]] provides a computationally efficient approximation to various firing regimes. These neuron models can be combined with different synapse models capturing excitatory and inhibitory dynamics with biologically realistic temporal properties.

Parameter optimization represents another key capability. Neurodamus integrates with TVB's parameter estimation framework, allowing researchers to fit microscopic model parameters to match observed macroscopic dynamics. This addresses the challenging problem of constraining detailed neuron models using [[functional-connectivity]] measurements from [[resting-state]] [[fmri]] or [[meg]] data.

## Relationship to TVB

Neurodamus is tightly integrated with TVB through the [[tvb-nest]] module, which provides the main interface for running combined simulations. The workflow typically begins with TVB generating or loading a connectivity matrix—either from public datasets like [[hcp-dataset]] or from custom [[diffusion-imaging]] data processed through tools like [[mrtrix3-connectome]]. This connectivity matrix is then used to construct the interregional coupling in the spiking network simulation.

The simulation proceeds in a hybrid mode where TVB handles the macroscopic coupling between brain regions while Neurodamus manages the microscopic dynamics within each region. Signals can be extracted at multiple levels: spike trains from individual neurons, local field potentials computed from synaptic currents, or population firing rates that feed back into TVB's neural mass framework.

This integration makes Neurodamus particularly valuable for [[personalized-brain-modeling]] applications. Researchers can construct patient-specific whole-brain models by combining individual [[structural-connectivity]] data with detailed neural simulations. Applications include [[epilepsy-modeling]] where detailed neuron models help capture seizure dynamics, and [[brain-stimulation]] studies where precise timing of neural responses matters.

## Related Software

Neurodamus connects TVB to the broader ecosystem of neural simulation tools. [[nest]] provides the primary backend for large-scale parallel simulations, while [[neuron]] enables biophysically detailed single-neuron modeling. [[brian2]] offers flexibility for custom model specification. The [[tvb-multiscale]] framework extends these capabilities further, allowing coordination across multiple simulation engines simultaneously. Researchers comparing different approaches may consult the [[tvb-vs-nest-vs-neuron]] comparison as well as the [[neural-mass-models-comparison]] overview.
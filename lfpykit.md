---
title: LFPykit
created: 2024-01-15
updated: 2026-05-11
type: entity
tags: [software-brian, software-neuron, forward-model, volume-conduction, local-field-potentials, spiking-neural-networks, neural-simulation, software-modeling]
sources: []
---

LFPykit is a Python library that provides modular kernel functions for computing extracellular electric potentials (local field potentials, LFP) from detailed spiking neural network simulations. The library enables biophysically principled calculation of LFP signals by solving the volume conduction problem for arbitrary arrangements of neurons and electrodes, making it an essential tool for linking microscopic neural activity to macroscopic electrophysiological measurements such as EEG and MEG.

## Overview

The local field potential represents the summed electrical activity from millions of synapses and dendritic currents in the vicinity of a recording electrode. While simplified neural mass models like those used in [[the-virtual-brain]] often treat LFP as a static coupling to mean neural activity, LFPykit enables calculation of LFP from detailed biophysical simulations where each neuron contributes according to its morphology and position in 3D space. The library implements a linear framework where the LFP at any point in space is computed as a weightedsum of contributions from current sources (sink/source pairs representing synaptic inputs or active channels) distributed throughout neuronal morphologies. This approach rests on volume conductor theory, assuming the extracellular medium is a homogeneous, isotropic conductor—a reasonable first-order approximation for brain tissue at scales relevant to LFP measurements.

The name "LFPykit" reflects its role as a toolkit that complements the main [[lfpy]] library. While LFPy provides the full simulation environment and integration with specific simulators, LFPykit distills the core computational kernels into a lightweight, reusable module that can be embedded in other frameworks or used for rapid prototyping of LFP calculation methods.

## Key Features

LFPykit provides several computational modules that form the building blocks of extracellular potential calculation. The core functionality revolves around the concept of point-source approximation combined with line-source approximation for dendritic cables, allowing accurate LFP computation even for neurons with complex morphologies.

The library implements the "CSD (current source density) method" for LFP calculation, where synaptic currents are modeled as point sources at synaptic locations and the extracellular potential is computed using Green's functions for the volume conductor. This approach scales linearly with the number of current sources, making it feasible for simulations with thousands of neurons.

LFPykit supports multiple formulations of the volume conduction problem, including the classic point-source approximation, line-source approximation for cylindrical dendrites, and hybrid approaches that combine morphological accuracy with computational efficiency. The kernel functions are implemented in pure NumPy, making them portable and easily modifiable for custom geometries or conductivity profiles.

A key feature is the integration with morphological reconstructions from neuromorpho and other databases, allowing users to import realistic neuron geometries and compute LFP from simulations using these detailed morphologies. The library also provides tools for electrode positioning and LFP sampling at arbitrary 3D coordinates, supporting both intracortical recordings (laminar probes, tetrodes) and boundary element methods for scalp potentials.

## Relationship to TVB

The relationship between LFPykit and [[the-virtual-brain]] represents a bridge between two scales of brain modeling. TVB operates at the whole-brain level, using neural mass models like the [[jansen-rit-model]] or [[wong-wang-model]] to simulate large-scale brain dynamics based on [[structural-connectivity]] derived from diffusion imaging. These models produce mean activity estimates for brain regions but typically lack the biophysical detail needed to compute LFP from individual synaptic events.

LFPykit operates at the cellular and microcircuit level, requiring detailed simulations of spiking neurons with realistic morphologies. While TVB's core workflow does not directly use LFPykit, the two frameworks can be combined in a multi-scale modeling approach. For example, TVB's region-level dynamics could inform the input patterns to a detailed cortical microcircuit model built using [[brian2]] or [[neuron]], and LFPykit could then compute the LFP that would be recorded from such a microcircuit. This hierarchical approach allows researchers to investigate how whole-brain network dynamics manifest in electrophysiological signals.

The forward modeling capabilities of LFPykit are particularly relevant for TVB's [[forward-model]] module, which computes observable signals (fMRI BOLD, EEG, MEG) from simulated neural activity. While TVB currently uses simplified leadfield approaches, LFPykit's biophysically detailed volume conduction kernels could provide more accurate forward models for EEG/MEG source reconstruction, especially when the goal is to understand the relationship between cellular-level activity and macroscopic signals.

## Related Software

LFPykit is part of a broader ecosystem of computational neuroscience tools for neural simulation and signal calculation. It builds on the foundational work of [[lfpy]] which provides the primary Python interface for LFP calculation from NEURON simulations. The library complements [[brian2]] and [[neuron]] by providing post-processing tools for extracting extracellular potentials from simulations run in these frameworks.

For forward modeling and source localization, LFPykit interfaces with concepts from [[volume-conduction]] theory and draws on methods implemented in [[mne-python]] for EEG/MEG analysis. The [[local-field-potentials]] page provides additional context on the biophysical basis of these signals.

The computational approach in LFPykit relates to the broader class of [[spiking-neural-networks]] simulations where detailed neuron models are used to understand neural coding and circuit dynamics. Researchers combining TVB's whole-brain approach with LFPykit's cellular-resolution modeling can explore questions ranging from how [[brain-oscillations]] emerge from network interactions to how targeted [[brain-stimulation]] would affect both local circuits and distributed brain networks.
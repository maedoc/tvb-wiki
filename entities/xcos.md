---
title: XCOS
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [neural-mass-models, whole-brain-modeling, software-tvb, network-dynamics]
sources: []
---

# XCOS

## Overview

XCOS represents a neural mass modeling framework used within whole-brain simulation environments, particularly associated with The Virtual Brain (TVB) ecosystem for simulating large-scale brain dynamics. Neural mass models like XCOS abstract the collective activity of large neuronal populations into simplified mathematical descriptions, enabling tractable simulations of whole-brain activity while retaining key dynamical features observed in neuroimaging data such as [[fmri|functional magnetic resonance imaging (fMRI)]] and [[eeg|electroencephalography (EEG)]].

Neural mass models form a critical bridge between detailed biophysical simulations (such as those conducted in [[nest]] or [[neuron]]) and population-level descriptions used for clinical and cognitive applications. XCOS follows the tradition of models pioneered by [[jansen-rit|Jansen and Rit]] and later extended by researchers like [[viktor-jirsa]] and [[olaf-sporns]], providing a computationally efficient representation of cortical dynamics that can be parameterized using empirical connectivity data from diffusion imaging (see [[dti|diffusion tensor imaging]]).

## Technical Foundation

The mathematical formulation of neural mass models like XCOS typically employs systems of ordinary differential equations that describe the evolution of mean activity in distinct neural populations. Common formulations include populations of excitatory and inhibitory neurons, with coupling terms representing synaptic connections. The dynamics often exhibit rich oscillatory behavior, including alpha rhythms (8-12 Hz), beta rhythms (13-30 Hz), and gamma oscillations (>30 Hz), which are fundamental to understanding cognitive processes (see [[brain-oscillations]]) and clinical conditions like epilepsy (see [[epilepsy-modeling]]).

The relationship between structural connectivity (derived from [[dti]] tractography) and functional connectivity (measured via [[fmri]] or [[eeg]]) represents a core research question that models like XCOS help address. The framework enables researchers to perform *in silico* experiments manipulating structural connectivity, coupling strength, and neural parameters to understand how large-scale brain networks generate observed patterns of activity (see [[structural-connectivity]] and [[functional-connectivity]]).

## Relationship to TVB and Other Frameworks

Within the TVB ecosystem, XCOS serves as one of several neural mass model implementations available for whole-brain simulations. The Virtual Brain provides an interface for integrating personalized connectivity data (often from the [[hcp-dataset|Human Connectome Project]] or [[uk-biobank|UK Biobank]]) with these models to create individualized brain models for clinical applications (see [[personalized-brain-modeling]]).

Related models in the TVB library include the [[jansen-rit-model]], [[wong-wang-model]], and the [[epileptor]] model, each designed for different research applications. The Jansen-Rit model remains one of the most widely used neural mass models, particularly for generating simulated EEG and MEG data. The Wong-Wang model provides a more abstract description of cortical dynamics useful for studying resting-state networks (see [[resting-state]]). The Epileptor model specifically addresses seizure dynamics and has been used for predicting epileptic seizures (see [[seizure-prediction]]).

XCOS differs from these specific implementations in its focus on generic oscillatory dynamics, providing a flexible framework that can be adapted to various modeling questions. Researchers can customize parameters to match specific frequency bands or dynamical regimes of interest, making it useful for exploratory modeling and hypothesis generation.

## Key Parameters and Applications

Typical parameters in neural mass models like XCOS include:

- **Coupling strength**: The strength of connections between brain regions, often derived from empirical [[structural-connectivity]] data
- **Population time constants**: The characteristic timescales of neural responses
- **Excitatory/inhibitory balance**: The relative strength of excitatory and inhibitory processes (see [[excitation-inhibition-balance]])
- **Noise**: Stochastic inputs that drive the system and enable transitions between dynamical states

Applications include:

- Understanding the neural basis of [[resting-state]] networks
- Modeling changes in brain dynamics during development (see [[neurodevelopment]]) and aging (see [[aging-brain]])
- Investigating alterations in brain connectivity in conditions like [[schizophrenia-models]] and [[alzheimers-modeling]]
- Optimizing [[brain-stimulation]] protocols for therapeutic intervention

## Relationship to Other Entities

XCOS exists within a broader ecosystem of whole-brain modeling tools. Key related software platforms include:

- [[the-virtual-brain|TVB]]: The primary simulation environment where XCOS is implemented
- [[nest]]: Simulator for spiking neural networks offering higher biological detail
- [[brian]]: Another spiking neural network simulator with emphasis on flexibility
- [[neuroml]]: Standardized language for describing neuronal models

The field of [[computational-neuroscience]] provides the theoretical foundations for models like XCOS, drawing on [[dynamical-systems-theory]], [[mean-field-theory]], and [[neural-field-theory]]. Parameter estimation techniques (see [[parameter-estimation]]) are essential for fitting models to individual subject data.

## Open Questions and Future Directions

Several key challenges remain in neural mass modeling:

1. **Multi-scale integration**: Linking neural mass descriptions with detailed single-neuron or circuit-level models (see [[spiking-neural-networks]])
2. **Personalization**: Improving methods for estimating model parameters from limited neuroimaging data
3. **Validation**: Developing robust benchmarks for comparing model predictions to empirical observations (see [[model-validation]])
4. **Clinical translation**: Translating modeling insights into clinical applications for individualized treatment planning

The development of [[dynamic-causal-modeling]] and its applications in [[computational-psychiatry]] represent important frontier areas where models like XCOS may contribute to understanding psychiatric conditions through a mechanistic lens.

## Summary

XCOS represents an important component in the toolkit of whole-brain modeling, providing a computationally tractable framework for simulating large-scale neural dynamics. As part of the TVB ecosystem, it enables researchers to investigate how structural connectivity shapes functional brain activity, with applications spanning basic neuroscience, clinical research, and personalized medicine. The continued development of neural mass models, including improvements in parameter estimation and validation against empirical data, positions these approaches as valuable tools for understanding the complex dynamics of the human brain.
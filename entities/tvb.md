---
title: TVB
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [software-tvb, whole-brain-modeling, neural-mass-models]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/ritter-2013.md, raw/papers/schirner-2018.md, raw/papers/deco-2013.md]
---

# TVB (The Virtual Brain)

TVB is an open-source neuroinformatics platform for simulating large-scale primate brain network dynamics.

## Overview

The Virtual Brain (TVB) enables researchers to construct personalized whole-brain models by combining empirical structural connectivity (from diffusion MRI tractography) with neural mass models. The platform supports forward models for EEG, MEG, and fMRI, allowing simulated signals to be compared directly against empirical recordings.

## Key Features

- **Whole-brain network simulation**: Simulates brain dynamics across the entire cortex
- **Neural mass models**: Implements Jansen-Rit, Wilson-Cowan, and other population models
- **Multimodal support**: Forward models for EEG, MEG, and fMRI signals
- **Personalized modeling**: Subject-specific connectivity from individual neuroimaging data
- **Structural connectivity**: Integration of DTI tractography data
- **Open-source**: Freely available for research and clinical applications

## Core Methodology

TVB combines:
1. Structural connectivity matrices derived from diffusion MRI
2. Neural mass models for regional brain dynamics
3. Forward models to generate simulated neuroimaging signals
4. Parameter optimization to match empirical recordings

## Key Publications

- Sanz Leon et al. (2013) — Introduced TVB platform sanz-leon-2013
- Ritter et al. (2013) — Multimodal neuroimaging integration ritter-2013
- Schirner et al. (2018) — Automated personalized pipeline schirner-2018
- Deco et al. (2013) — Resting-state computational insights deco-2013

## Related Software

- [[NEST]] — Spiking neural network simulator for detailed neuron models
- [[NEURON]] — Multi-compartment neuron simulation environment
- [[ANTs]] — Image registration for preprocessing neuroimaging data

## Related Concepts

- [[whole brain]] — Whole-brain modeling approach
- [[neural mass model]] — Population-level neural dynamics
- [[personalized brain modeling]] — Subject-specific model construction
- [[functional connectivity]] — Simulated and empirical connectivity patterns

## Use Cases

- Resting-state functional connectivity modeling
- Clinical brain simulation for personalized medicine
- Epilepsy seizure propagation modeling
- Brain stimulation and neuromodulation studies

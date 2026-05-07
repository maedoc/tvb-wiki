---
title: Paul Nunez
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neuroimaging-eeg, neural-mass-models, computational-neuroscience, textbook]
sources: [raw/papers/nunez-srinivasan-2006.md, raw/papers/sporns-2011.md, raw/papers/semanticscholar-567c5507b87b.md]
---

Paul Nunez — a researcher whose work on the neurophysics of EEG forms a foundational resource for whole-brain modeling and computational neuroscience.

## Overview

The name "Nunez" in this wiki context refers primarily to Paul L. Nunez, whose textbook *Electric Fields of the Brain: The Neurophysics of EEG* (co-authored with Ramesh Srinivasan) has become a canonical reference for understanding how [[neural-mass-model]] activity at the macroscopic scale gives rise to measurable scalp potentials. While the wiki does not maintain biographical pages for individual researchers, Nunez's textbook represents a critical bridge between the physical principles governing electromagnetic field generation in brain tissue and the mathematical frameworks used in modern [[whole-brain]] simulations.

## Significance for Whole-Brain Modeling

Whole-brain models [[the-virtual-brain]] and similar platform rely on the ability to translate population-level neural activity into predicted observable signals. This translation is mediated by volume conduction theory—the physical framework describing how current sources in the brain produce electric fields in the surrounding tissue and at the scalp surface. Nunez and Srinivasan's textbook provides the rigorous treatment of this forward problem that enables modelers to validate their simulations against empirical [[eeg]] recordings.

The textbook's treatment of source localization methods is particularly relevant for parameter fitting in whole-brain models. When constructing a [[personalized-brain-model]], one typically tunes the model's parameters so that its simulated dynamics reproduce observed resting-state [[functional-connectivity]] patterns. Understanding the relationship between modeled source activity and recorded scalp potentials is essential for validating these models against [[neuroimaging-eeg]] data.

## Key Conceptual Contributions

### Volume Conduction Theory

The textbook provides a comprehensive treatment of volume conduction—the physical process by which ionic currents flowing across neuronal membranes produce extracellular potential fields. These fields propagate through the head's heterogeneous conductivity structure (brain, CSF, skull, scalp) according to quasi-static approximations of Maxwell's equations. The forward problem in [[source-localization]] requires solving these equations to predict scalp potentials given a known configuration of neural sources. Volume conduction theory is thus foundational to any whole-brain model that aims to produce physiologically plausible [[eeg]] predictions.

### Neural Mass Models of EEG Generation

Nunez's work discusses how macroscopic EEG signals emerge from the coordinated activity of large neuronal populations. The textbook connects microscopic mechanisms—synaptic currents, membrane potentials—to macroscopic observables through mean-field approximations. This theoretical framework underpins the [[neural-mass-model]] approach used in many whole-brain simulators, where brain regions are represented as coupled oscillators or neural mass equations rather than as detailed spiking networks.

The book explores several mathematical formulations for relating population-level Synchronous Neural Activity (SNA) to EEG spectral properties, including the relationship between coherence in source activity and the resulting scalp signal complexity.

### Connection Between Micro and Macro Scales

A recurring theme in the textbook is the challenge of linking cellular-level neural activity to mesoscopic and macroscopic scales observable in neuroimaging. This multi-scale problem remains central to whole-brain modeling: current [[whole-brain-modeling]] approaches typically operate at the level of brain regions (parcels), but the parameters of these models must be derived from or validated against phenomena emerging from synaptic and cellular dynamics. Understanding this scale-bridging is essential for developing biologically constrained whole-brain models that go beyond pure curve-fitting.

## Relationship to Related Concepts

The textbook sits at the intersection of several domains relevant to whole-brain modeling. It provides the physical foundation for [[source-localization]] algorithms used in analyzing [[eeg]] and [[meg]] data, informing both empirical studies and model validation. The treatment of [[local-field-potentials]] connects neural mass model outputs to the underlying physiological processes they represent.

In the broader ecosystem of whole-brain modeling resources, Nunez's textbook complements the network-theoretical perspective provided by Sporns's *Networks of the Brain*—while Sporns focuses on the organization of brain connectivity at the systems level, Nunez provides the physical scaffolding for understanding how network-level activity produces measurable electromagnetic signatures. Together, these texts form part of the theoretical foundation upon which modern [[whole-brain]] simulators are built.

The mathematical frameworks discussed in the textbook also relate to other approaches in the field, including [[dynamic-causal-modeling]] (which shares the goal of inverting generative models of neural dynamics) and methods from [[nonlinear-dynamics]] and [[bifurcation-theory]] used to analyze transitions between brain states.

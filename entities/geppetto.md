---
title: Geppetto
created: 2026-04-24
updated: 2026-04-30
type: entity
tags: [software-brain-modeling, software-tvb, whole-brain-modeling]
sources: [raw/papers/geppetto-2018.md]
---

# Geppetto

## Overview

Geppetto is an open-source web-based platform for neuroscience data visualization, model exploration, and computational middleware (Cantarelli et al., 2018). The name derives from Geppetto, the carpenter who fashioned Pinocchio in Carlo Collodi's classic tale—an apt metaphor for a platform that "constructs" simulated brains from empirical connectivity data and neural dynamics equations. In the context of [[whole-brain-modeling]], Geppetto provides the visualization layer and user interface through which researchers interact with brain network models, while the actual numerical integration may be performed by backend engines such as TVB's simulation library.

The term "Geppetto" in neuroscience refers to two distinct but related software projects. The first, documented in Cantarelli et al. (2018), is a general-purpose web-based platform for neuroscience data visualization and model exploration that underpins applications including [[Open Source Brain]], Virtual Fly Brain, and NetPyNE-UI. The second, which functions within [[The Virtual Brain]], provides the web-based frontend and middleware layer through which users construct, configure, and visualize whole-brain simulations. This dual identity reflects the modular nature of modern neuroinformatics tools, where common infrastructure serves multiple specialized applications.

## Key Features

### Web-Based Visualization Architecture

Geppetto provides a modular software architecture designed for building both desktop and web-based neuroscience applications (Cantarelli et al., 2018). The platform offers middleware infrastructure that separates visualization and user interaction from the underlying computational engine, allowing researchers to run simulations remotely on high-performance computing clusters while interacting through browser-based interfaces. This client-server architecture is particularly valuable for [[whole-brain-modeling]], where simulations may involve hundreds of brain regions and require significant computational resources that exceed what typical workstations can provide.

The software implements a Model Abstraction layer that handles heterogeneous data types common in computational neuroscience, including [[neural-mass-models]] (such as [[jansen-rit]] and [[wilson-cowan]]), spiking neuron models, and [[structural-connectivity]] matrices derived from [[diffusion-mri]] tractography. This abstraction enables seamless switching between different model types and integration of multimodal neuroimaging data within a unified framework.

### Integration Capabilities

Geppetto integrates with several major [[computational-neuroscience]] platforms and standards. The platform provides native support for [[NEURON]], [[NetPyNE]], and [[NeuroML]], allowing researchers to import models from these ecosystems and run them within the Geppetto computational framework (Cantarelli et al., 2018). This interoperability is essential for [[whole-brain-modeling]] workflows that may combine detailed single-neuron models with population-level approximations at different scales.

For neuroimaging integration, Geppetto can consume [[structural-connectivity]] matrices in standard formats and use them to constrain [[network-dynamics]] simulations, enabling personalized brain models based on individual diffusion imaging data. The platform connects with preprocessing pipelines for neuroimaging data, though specific pipeline integrations (such as particular analysis tools) depend on the deployment context.

## Relationship to TVB

Within the [[TVB]] ecosystem, Geppetto functions as the web-based frontend and visualization layer through which researchers interact with the TVB simulation platform (Cantarelli et al., 2018). [[The Virtual Brain]] combines Geppetto's web interfaces with the TVB computational library (the tvb-library Python package) that handles the actual numerical integration of neural dynamics equations. When a researcher constructs a personalized brain model in TVB—importing [[structural-connectivity]] from DTI tractography, selecting a [[neural-mass-model]] such as the [[jansen-rit]] model, and configuring simulation parameters—Geppetto provides the user interface for model configuration, while TVB's Python solvers perform the numerical integration that generates the simulated brain activity time series.

The TVB platform exposes Geppetto's functionality through Python APIs and graphical user interfaces, abstracting away the complexities of distributed computing from most users. This separation allows the web-based visualization layer to remain responsive while computationally intensive simulations run on dedicated compute resources. Advanced users can directly access TVB's computational primitives for custom modeling applications, such as investigating [[epilepsy-modeling]] with the [[epileptor]] model or exploring [[brain-stimulation]] scenarios through virtual electrode setups.

## Key Features for Whole-Brain Modeling

### Numerical Integration

The TVB simulation library (which works with Geppetto as the frontend) implements multiple numerical integration schemes for solving the differential equations that govern neural population dynamics. For [[neural-mass-models]] that operate at the mesoscopic scale—including the [[jansen-rit]] model (a three-population cortical column model that generates realistic [[eeg]] and [[meg]] signals), the [[wilson-cowan]] model (a classic firing-rate model for [[brain-oscillations]]), and the [[epileptor]] model (designed specifically for seizure dynamics)—the platform provides solvers based on exponential Euler integration and other methods appropriate for stiff ordinary differential equations.

The platform handles the coupling of regional brain models through [[structural-connectivity]] matrices, implementing the delay differential equations that arise from finite conduction velocities along white matter pathways. This delay-coupled system forms the foundation of [[whole-brain-modeling]], where the dynamics of each brain region depends on synaptic input from other regions with delays determined by the structural connectome.

### Forward Modeling

A critical capability for comparing simulated dynamics with empirical recordings is the forward model component. Geppetto and TVB together implement forward models that transform simulated neural activity into the signals measured by neuroimaging modalities including [[eeg]], [[meg]], and [[fmri]]. The electromagnetic forward models solve the lead-field problem for [[eeg]] and [[meg]], computing how cortical electrical activity propagates through the head volume to scalp electrodes and magnetometers. For [[fmri]], the platform implements models of the [[hemodynamic-response-function]] that couple neural activity to the blood-oxygen-level-dependent (BOLD) signal through the neurovascular cascade.

## Related Software

Geppetto shares conceptual territory with several other simulation platforms in computational neuroscience. [[NEST]] provides [[spiking-neural-networks]] simulation with a focus on detailed single-neuron models and large-scale networks of point neurons. [[NEURON]] offers multi-compartment neuron modeling for detailed biophysical simulations. [[NetPyNE]] provides a high-level interface for constructing [[spiking-neural-networks]] and is itself supported by the Geppetto visualization platform. For [[whole-brain-modeling]] specifically, TVB with Geppetto competes with or complements other large-scale simulators including integrated platforms like The VirtualBrain itself.

## Use Cases

The combination of Geppetto and TVB enables several important research applications. In [[epilepsy-modeling]], researchers construct personalized brain models from patient MRI and DTI data, then use the [[epileptor]] model within the TVB simulation framework to simulate seizure propagation and test intervention strategies. For [[resting-state]] research, the platform generates simulated [[functional-connectivity]] patterns that can be compared against empirical [[fmri]] recordings to test hypotheses about the neural basis of intrinsic brain activity. Clinical applications include pre-surgical planning for [[brain-stimulation]] interventions, where virtual electrode placements in the personalized brain model predict outcomes of deep brain stimulation or epilepsy surgery.

## References

1. Cantarelli M, Marin B, Quintana A, Earnshaw M, Court R, Gleeson P, Dura-Bernal S, Silver RA, Idili G (2018). Geppetto: a reusable modular open platform for exploring neuroscience data and models. Philosophical Transactions of the Royal Society B: Biological Sciences, 373(1758), 20170380. [DOI](https://doi.org/10.1098/rstb.2017.0380)

2. Sanz Leon P, Woodman MM, Jirsa V, Bernard C, Le Van Quyen M, Geffroy F, Wang J, Spinelli L, Michel CM, Decety J (2013). The Virtual Brain: a whole-brain simulator of neural dynamics for brain imaging. NeuroImage, 76, 422-437. [DOI](https://doi.org/10.1016/j.neuroimage.2013.02.035)

3. Jirsa VK, Proix T, Perdikis D, Woodman MM, Wang J, Bernard C, Benquet CE, Martinerie J, Le Van Quyen M (2017). The Virtual Brain: mathematical modelling of brain dynamics. In: Handbook of Neurology (pp. 541-585). Elsevier. [DOI](https://doi.org/10.1016/B978-0-444-63600-3.00028-8)
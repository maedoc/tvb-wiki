---
title: LFPykit
created: 2025-01-15
updated: 2026-05-11
type: entity
tags: [software-neuroscience, lfp, forward-model, volume-conduction, computational-neuroscience, neural-simulation, software-python]
sources: []
---

LFPykit is a Python toolkit for computing local field potentials (LFP) from spiking neural network simulations. It provides a modular framework of volume conductor models and point source dipole implementations that can be combined with various neuron simulators to calculate extracellular potentials in realistic brain tissue. The library serves as the computational backbone for the related LFPy package, offering optimized building blocks for forward modeling of electrophysiological signals.

## Overview

The local field potential represents the summed electrical activity from populations of neurons measured by electrodes in brain tissue. Computing the LFP from detailed neural simulations requires solving the forward problem of electrophysiology—determining how current sources within the tissue generate potential distributions in the surrounding medium. LFPykit implements this by combining biophysical models of current sources (primarily point dipoles representing synaptic currents) with volume conductor models that describe the electrical properties of the extracellular space.

The toolkit separates the computation into two key components: the source model (describing the spatial distribution of current along neuronal morphology) and the volume conductor model (describing how currents propagate through the tissue). This modular design allows users to swap different configurations without rewriting core computational logic. The library supports both transmembrane currents (from synaptic input) and axial currents (from intracellular flow), enabling calculation of LFP from detailed morphologically reconstructed neurons or simplified point neuron models.

## Key Features

LFPykit implements several volume conductor models of increasing biophysical realism. The simplest is the infinite homogeneous medium model, which assumes uniform electrical conductivity throughout the extracellular space—a reasonable approximation for many experimental situations but one that neglects tissue heterogeneity. More sophisticated models include the anisotropic infinite medium (accounting for directional dependence of conductivity due to aligned fiber tracts), the three-shell sphere model (representing different conductivity layers as might occur at the cortical surface), and hybrid models that combine planar boundaries with volumetric anisotropy.

The source computation in LFPykit leverages the point dipole approximation, where each segment of a neuronal morphology is treated as a current dipole. The toolkit provides functions to compute the contribution of each segment to the potential at arbitrary electrode positions, then sums these contributions to yield the total LFP signal. This approach scales efficiently to large populations of neurons because the computation can be parallelized across electrode positions and neuronal sources. The library includes optimized implementations using NumPy vectorization and supports both CPU and GPU backends for large-scale simulations.

A distinctive feature of LFPykit is its emphasis on reproducibility and validation. The toolkit includes reference implementations of analytical solutions for simple geometries, against which more complex models can be tested. This validation framework helps ensure that simulations produce physiologically plausible LFP signals and supports method comparison studies.

## Relationship to TVB

While [[The Virtual Brain]] (TVB) primarily operates at the level of neural mass models and mean-field approximations, the two frameworks can be integrated for multi-scale modeling. TVB's whole-brain simulations often produce macroscale activity that could be refined with biophysically detailed LFP calculations using LFPykit, though such integration remains an active research direction. More directly, LFPykit shares conceptual foundations with TVB's approach to forward modeling—the problem of relating neural activity to measurable signals is central to both platforms, albeit at different spatial scales. TVB's [[forward-model]] capabilities primarily address hemodynamic responses for fMRI, whereas LFPykit tackles the complementary electromagnetic forward problem for electrophysiology.

The two software ecosystems also share a common philosophy of modular design. TVB allows researchers to swap different neural mass models (such as the [[Jansen-Rit]] or [[Wong-Wang]] models) while maintaining the same simulation infrastructure. LFPykit similarly enables swapping different volume conductor models without changing the neural simulation backend. This architectural similarity facilitates potential future integration where TVB could leverage LFPykit for EEG/MEG source modeling in personalized brain models.

## Related Software

LFPykit forms part of a broader ecosystem for neural electrophysiology simulation. [[LFPy]] builds upon LFPykit to provide a complete workflow for calculating LFP from [[NEURON]] or [[Brian]] simulations, handling neuron morphology loading and electrode positioning. The closely related [[LFPykern]] package provides specialized kernel functions for rapid LFP computation. For MEG and EEG source localization, researchers often use [[MNE-Python]], which addresses the inverse problem (reconstructing sources from measured signals) rather than the forward problem that LFPykit solves. [[Electrophysiology]] signal processing more broadly connects to tools like [[ Elephant]] for spike train analysis and [[SpikeInterface]] for extracellular recording analysis.

The forward modeling approach in LFPykit complements other biophysical modeling frameworks including the [[Bold-Model]] in TVB (describing the hemodynamic response to neural activity) and detailed compartment models in [[NEURON]]. For users interested in [[Computational Neuroscience]] at the cellular scale, LFPykit provides a bridge to whole-brain modeling by enabling calculation of mesoscopic signals from detailed network simulations.

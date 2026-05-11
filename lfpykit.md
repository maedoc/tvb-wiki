---
title: LFPykit
created: 2024-01-15
updated: 2026-05-11
type: entity
tags: [software-modeling, forward-model, volume-conduction, local-field-potentials, spiking-neural-networks, neural-simulation, computational-neuroscience]
sources: [raw/papers/linden-2014.md, raw/papers/hagen-2018.md]
---

LFPykit is a Python library that provides freestanding implementations of electrostatic forward models for computing extracellular electric potentials—including local field potentials (LFP), electrocorticography (ECoG), electroencephalography (EEG), and magnetoencephalography (MEG)—from multicompartment neuron models. Developed by the Computational Neuroscience Group at NMBU (Norwegian University of Life Sciences), LFPykit enables biophysically principled calculation of extracellular signals by solving the volume conduction problem for arbitrary neuron morphologies and electrode configurations. The library serves as a modular toolkit that can be integrated with various neural simulators including NEURON, Arbor, Brian2, and the Brain Modeling ToolKit (BMTK), without requiring explicit dependencies on any particular simulation environment.

## Overview

The computation of extracellular potentials from neural activity represents a fundamental challenge in computational neuroscience, bridging the gap between microscopic cellular dynamics and macroscopic electrophysiological measurements. The local field potential emerges from the summed contributions of transmembrane currents flowing across neuronal membranes, particularly in dendritic compartments where synaptic inputs generate sinks and sources that can be detected by nearby electrodes [[raw/papers/linden-2014.md]]. LFPykit implements a rigorous mathematical framework based on volume conductor theory, where the extracellular potential at any point in space is computed as a weighted sum of contributions from transmembrane currents distributed throughout neuronal morphologies.

The library's core innovation lies in its linear response framework. For a multicompartment neuron model with transmembrane currents **I** (nA) distributed across n_seg compartments, the extracellular potential **V_ex** (mV) at measurement sites is computed as a linear transformation **V_ex = MI**, where **M** is a matrix mapping currents to potentials. This elegant formulation allows efficient computation while capturing the biophysical details of how current sources in morphologically complex neurons contribute to extracellular fields [[raw/papers/hagen-2018.md]]. The matrix **M** depends only on the neuron geometry, electrode positions, and the assumed conductivity properties of the extracellular medium—once computed, it can be reused for any number of simulation time steps.

LFPykit distinguishes itself from the related [[lfpy]] library by providing standalone implementations of the forward models without dependencies on specific neural simulators. This modular design allows the computational kernels to be embedded in other frameworks, used for rapid prototyping, or integrated with custom simulation pipelines. The library is particularly valuable for researchers working at the intersection of detailed biophysical modeling and forward models for EEG/MEG source localization.

## Key Features

LFPykit implements several distinct forward models that trade off computational complexity against morphological accuracy. The simplest approach is the **point source potential** model, which treats each neuronal compartment as a point current source located at its midpoint. The contribution from compartment i to measurement site j is computed as M_ji = 1/(4πσ|r_i - r_j|), where σ is the extracellular conductivity and r_i, r_j are the respective coordinates. This approximation works well for distant measurement sites but introduces errors near the cell membrane.

The more accurate **line source potential** model treats each compartment as a line segment with uniform current density, using analytical expressions derived from the cable equation [[raw/papers/linden-2014.md]]. The contribution involves logarithmic terms that properly account for the geometry of cylindrical dendritic segments: M_ji = (1/4πσL_i) log(|(√(h_ji²+r_ji²)-h_ji)/(√(l_ji²+r_ji²)-l_ji)|), where L_i is the segment length, r_ji is the perpendicular distance from the electrode to the segment axis, and h_ji, l_ji characterize the longitudinal distances. This approach captures the near-field behavior of extracellular potentials more accurately and is the default choice for most applications.

For applications requiring complete head models, LFPykit provides the **four-sphere volume conductor** model, which approximates the head as concentric spheres representing brain, cerebrospinal fluid (CSF), skull, and scalp, each with different conductivity values. This model enables computation of EEG signals from current dipole moments and has been validated against more detailed boundary element methods [[raw/papers/hagen-2018.md]]. The library also includes the **New York Head Model**, a detailed individualized head model that provides more accurate forward fields for EEG source localization.

The **current dipole moment** class computes the net current dipole from all transmembrane currents in a neuron, which serves as the primary input for distal measurements like EEG and MEG. This approach leverages the fact that at distances large compared to the neuron size, the field can be characterized by a single dipole vector rather than the full distribution of current sources.

## Technical Implementation

The library defines a base CellGeometry class that represents multicompartment neuron morphology in terms of segment coordinates (x, y, z) and diameters. Each segment is represented as a piecewise linear element between its start and end points, with the transmembrane current density assumed constant along the segment axis. This representation is compatible with morphologies from standard reconstruction formats (SWC, ASC) and databases like NeuroMorpho.White-matter.

All forward models in LFPykit follow a consistent interface pattern. After instantiating a CellGeometry object with the neuron morphology, users create a model object (e.g., LineSourcePotential) specifying electrode positions and conductivity parameters. Calling get_transformation_matrix() returns the linear mapping **M** that can be multiplied by the transmembrane current array from any simulation to obtain extracellular potentials. This separation of geometry computation from simulation allows efficient repeated calculations.

Physical units are standardized throughout: transmembrane currents in nA, spatial coordinates in μm, voltages in mV, and conductivities in S/m. The library does not enforce unit consistency but follows these conventions consistently in its documentation and examples.

## Relationship to TVB

The relationship between LFPykit and [[the-virtual-brain]] represents a bridge between cellular-level biophysical modeling and whole-brain network dynamics. TVB operates at the mesoscopic to macroscopic scale, using [[neural-mass-models]] like the [[jansen-rit-model]] or [[wong-wang-model]] to simulate large-scale brain dynamics informed by [[structural-connectivity]] derived from diffusion tensor imaging. These models produce mean activity estimates for brain regions but typically lack the biophysical detail needed to compute LFP from individual synaptic events.

While TVB's core forward modeling module computes observable signals (BOLD, EEG, MEG) from region-level activity using simplified leadfield approaches, LFPykit provides the biophysically detailed forward kernels necessary for accurate EEG/MEG source reconstruction at cellular resolution. Researchers interested in understanding exactly how microscopic neural activity contributes to macroscopic electrophysiological signals can combine TVB's network dynamics with LFPykit's forward models in a multi-scale framework.

The two frameworks address complementary questions: TVB excels at investigating how large-scale [[brain-network]] dynamics emerge from anatomical connectivity and how alterations in connectivity relate to clinical conditions, while LFPykit is designed to answer how specific cellular-level activity—synaptic currents, dendritic integration, ion channel dynamics—produces the signals measured by electrodes on the scalp or within the brain.

## Related Software

LFPykit integrates with a broader ecosystem of computational neuroscience tools. The primary related tool is [[lfpy]], which provides the full simulation environment and simulator integration, with LFPykit's forward models originally incorporated in LFPy before being separated into a standalone package. The library works with major neural simulators including [[neuron]], [[brian2]], and Arbor, allowing users to run detailed simulations in their preferred environment and post-process with LFPykit.

For MEG and EEG analysis, LFPykit complements [[mne-python]] by providing the forward models that relate neural activity to measurement sensors. The library's dipole-based calculations interface with standard source localization pipelines while maintaining biophysical rigor. The volume conduction models draw on decades of methodological development in the [[forward-model]] literature, and the four-sphere head model represents a standard approach taught in neuroimaging courses.

The computational approach relates to [[spiking-neural-networks]] research where detailed neuron models investigate neural coding and circuit dynamics. Researchers combining whole-brain modeling with LFPykit's cellular resolution can explore questions from how [[brain-oscillations]] emerge from network interactions to how [[brain-stimulation]] (TMS, tDCS) affects both local circuits and distributed brain networks.

## Key Papers

The development of LFPykit is documented in several key publications from the Einevoll group at NMBU. Linden et al. (2014) introduced LFPy as a tool for biophysical simulation of extracellular potentials generated by detailed model neurons, establishing the mathematical framework for line-source calculations that LFPykit implements. Hagen et al. (2018) extended this framework to multimodal modeling, demonstrating how the same framework can compute LFP, ECoG, EEG, and MEG signals with LFPy 2.0, which incorporated the modular design that LFPykit later formalized.
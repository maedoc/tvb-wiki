---
created: 2026-04-23
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/hines-carnevale-1997.md
tags:
- software-brain-modeling
- software-neuron
title: LFPy
type: entity
updated: '2026-05-04'
---

**[[lfp-lib|LFPy]]** is an open-source Python package designed for the simulation of extracellular potentials in biologically detailed neural networks. It computes the [[local-field-potentials|local field potential]] (LFP) that arises from the electrical activity of neurons embedded in a volume conductor, providing a bridge between [[neural-mass-models|neural mass modeling]] at the [[whole-brain]] scale and detailed biophysical simulations at the cellular level. The software enables researchers to predict LFP signals from arbitrarily structured neural networks while accounting for the geometry and electrical properties of the surrounding tissue.

## Motivation and Context

Extracellular recordings are a fundamental technique in [[neural-mass-models|electrophysiology]], providing insights into neural signaling that complement [[fmri|functional magnetic resonance imaging]] and [[meg|magnetoencephalography]]. While intracellular recordings reveal the membrane dynamics of individual neurons, extracellular field potentials reflect the summed activity of many neurons and offer a more scalable approach to monitoring neural circuits. However, interpreting extracellular recordings requires understanding how transmembrane currents generate these fields—a problem known as the forward modeling of the LFP.

The forward problem in bioelectricity involves computing the extracellular potential given a known arrangement of sources (neuronal membranes) and the conductive medium surrounding them. This approach is essential for connecting activity in biologically detailed network models to the signals actually measured by electrodes in experimental and clinical settings. LFPy was developed to make forward modeling accessible to the [[computational-neuroscience]] community, allowing researchers to simulate LFPs from detailed morphological neuron models without implementing the electromagnetic equations from scratch.

## Technical Framework

LFPy implements a two-stage computational pipeline for calculating extracellular potentials. In the first stage, the software leverages the [[NEURON]] simulation environment to compute transmembrane currents for all neuronal compartments in a network model over time. These currents serve as the current sources in the forward calculation. In the second stage, LFPy computes the extracellular potential at arbitrary field points using the lead field matrix approach, which relates each transmembrane current source to the potential it produces at each measurement location.

The extracellular potential φ(r, t) at position r and time t is given by the [[linear]] superposition of contributions from all current sources:

φ(r, t) = Σᵢ G(r, rᵢ) · Iᵢ(t)

where G(r, rᵢ) is the Green's function (or transfer function) that describes the potential at position r produced by a unit current source at position rᵢ, and Iᵢ(t) is the transmembrane current in compartment i at time t. The Green's function depends entirely on the geometry and conductivity of the volume conductor, while the currents are determined by the neural dynamics simulated in NEURON.

## Supported Forward Models

LFPy supports several volume conductor geometries, each corresponding to different assumptions about the extracellular medium:

- **Infinite homogeneous medium**: The simplest model, assuming uniform conductivity in all directions
- **Semi-infinite volume conductor**: Models a planar boundary between brain tissue and a poorly conducting medium (such as air or skull)
- **Multilayer spheres**: Represents tissue layers with different conductivities, such as cortex surrounded by cerebrospinal fluid and skull
- **Axisymmetric slab**: A simplified model for planar layered structures

The choice of volume conductor model depends on the experimental context and the spatial scale of the simulation. For electrode arrays placed on the cortical surface, the multilayer sphere model provides more accurate predictions than the homogeneous assumption, as it accounts for the insulating effects of the skull and cerebrospinal fluid.

## Key Features

LFPy provides several capabilities that make it a versatile tool for extracellular potential simulation:

The software implements the line-source approximation, which treats elongated neuronal processes as line currents rather than point sources. This approach is computationally efficient and accurately captures the contribution of dendrites and axons to the LFP, particularly when the electrode is located close to these processes. Compared to point-source approximations, the line-source method reduces artifacts associated with the singular behavior of the potential near discrete current dipoles.

LFPy supports multimodal signal prediction, allowing researchers to compute not only the LFP but also the extracellular potassium concentration and magnetic fields from the same neural activity data. This feature enables comparison with other measurement modalities and facilitates integration with [[whole-brain-modeling]] frameworks that combine electrophysiological and hemodynamic signals.

The package provides tools for calculating extracellular potentials from arbitrarily structured networks, supporting both random [[connectivity]] and detailed reconstructions from databases such as [[ModelDB]]. Researchers can import morphologically detailed neuron models and specify the spatial arrangement of cells to create customized network simulations.

LFPy includes support for subcellular resolution modeling, enabling the investigation of how activity in specific cellular compartments (such as soma, dendrites, or axon initial segments) contributes to the recorded LFP. This capability is particularly valuable for studying the spatial filtering properties of the extracellular medium and for interpreting the relative contributions of excitatory and inhibitory neurons to field potentials.

The software implements efficient numerical methods for computing the transfer matrix, including the reciprocal method that relates source and field locations. This optimization makes it feasible to simulate LFPs from networks containing thousands of neurons while maintaining reasonable computational costs.

## Relationship to The Virtual Brain

LFPy and [[the-virtual-brain]] (TVB) serve complementary roles in the computational neuroscience ecosystem. TVB is a [[whole-brain-modeling]] platform that operates at the level of neural masses, simulating large-scale [[brain-dynamics]] across multiple brain regions using simplified population models. While TVB excels at capturing regional dynamics and connectivity patterns, it does not presently include biophysically detailed forward modeling of extracellular signals.

LFPy bridges this gap by providing the biophysical layer needed to interpret and validate mesoscopic field potential data. In a typical combined workflow, TVB provides the temporal patterns of activity for each brain region, while LFPy transforms these patterns into the predicted LFP that would be recorded by an electrode array. This integration enables researchers to perform [[personalized-brain-modeling]] by fitting whole-brain models to actual LFP recordings, which is particularly valuable in clinical applications such as [[epilepsy-modeling]] where detailed field potential data is available from intracranial electrodes.

The combination of TVB and LFPy also facilitates validation of whole-brain models against invasive electrophysiological recordings. By computing predicted LFPs from TVB simulations and comparing them to observed data, researchers can assess the biophysical plausibility of large-scale [[network-dynamics]] and refine their models accordingly.

## Key Papers

The foundational references for LFPy are two papers that describe the software's design, implementation, and applications. The first paper (Linden et al., 2013) introduced LFPy as a tool for computing LFPs from network simulations and demonstrated its capabilities using example simulations of cortical pyramidal neurons. The second paper (Hagen et al., 2018) substantially extended the software's functionality to include support for multiple volume conductor models, subcellular resolution analysis, and efficient calculation of magnetic fields.

These papers serve as the primary citations for researchers using LFPy in their work. They provide detailed descriptions of the computational methods, validation against analytical solutions, and example applications to realistic neural modeling scenarios.

## Related Software

LFPy integrates with several related software packages in the computational neuroscience ecosystem:

- **Lfpykit**: A companion Python package that provides general classes for volume conductor modeling and extracellular potential calculation. LFPy builds on lfpykit to extend its functionality to specific use cases involving NEURON simulations.
- **NEURON**: The simulation environment that LFPy uses for computing neural dynamics. NEURON provides the compartmental modeling framework needed to calculate transmembrane currents for neurons with arbitrary morphologies.
- **Brian2**: Another neuron simulator that can in principle be integrated with forward modeling tools, though LFPy specifically targets the NEURON interface.
- **[[nest]]**: A simulator focused on large-scale network dynamics that complements LFPy's detailed single-neuron capabilities.

The modular design of LFPy allows researchers to combine these tools in various configurations depending on their modeling needs. For instance, LFPy can be used with custom NEURON models imported from [[ModelDB]], enabling forward modeling of LFPs from biologically realistic neural networks.

## Development and Community

LFPy is developed as an open-source project with contributions from the computational neuroscience community. The software is maintained by researchers at the University of Oslo and the KTH Royal Institute of Technology, with support from the International Neuroinformatics Coordinating Facility (INCF). The project has received funding from the European Union's Seventh Framework Programme and the Human Brain Project, reflecting its role in advancing standards for neural simulation and data sharing.

The software is distributed under the GNU General

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](https://arxiv.org/abs/2509.12873)
3. Hines & Carnevale (1997). *The NEURON simulation environment*. Neural Computation. [DOI](https://doi.org/10.1162/neco.1997.9.6.1179)
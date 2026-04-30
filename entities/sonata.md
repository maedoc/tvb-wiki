---
created: 2024-01-15
sources:
- Dai et al. 2020
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007696
- https://github.com/AllenInstitute/sonata
- https://github.com/BlueBrain/libsonata
- raw/papers/geppetto-2018.md
- raw/papers/semanticscholar-ff8218c1e55e.md
- raw/papers/semanticscholar-899d3552b2ad.md
- raw/papers/glean-github.md
tags:
- software-brian
- software-nest
- software-neuron
- spiking-neural-networks
- whole-brain-modeling
- connectomics
- bluepyopt
title: SONATA
type: entity
updated: '2026-04-30'
---

## Overview

SONATA (Scalable Open Network Architecture TemplAte) is a data format and software ecosystem for defining, configuring, and running large-scale neuronal network simulations. Originally developed jointly by the [Blue Brain Project](https://bluebrain.epfl.ch/) at EPFL and the Allen Institute for Brain Science, SONATA provides a standardized way to specify point-neuron networks—including cell positions, morphologies, connectivity matrices, and simulation parameters—in a machine-readable HDF5-based format [[Dai et al. 2020]](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007696). The format was designed to address the growing need for interoperability between different [spiking neural network]([[spiking-neural-networks]]) simulators and to enable reproducible, scalable brain modeling at the tissue and whole-brain scale.

## Motivation and Context

Before SONATA, neuronal network models were typically encoded in simulator-specific formats or custom Python scripts, making it difficult to share models across platforms or compare results from different simulators. The proliferation of incompatible file formats created significant barriers to reproducibility and collaboration in computational neuroscience. SONATA emerged as part of the broader effort to standardize brain modeling infrastructure—paralleling developments like [NeuroML]([[neuroml]]) for model specification and [PyNEST]([[pynest]]) for simulator interoperability—by providing a declarative, simulator-agnostic description of network structure and simulation configuration.

The format gained traction as the Blue Brain Project scaled up its cortical microcircuit models from thousands to millions of neurons, requiring a format that could efficiently handle large connectivity matrices, handle morphologies, and support parameterized variations. SONATA's design emphasizes scalability and separation of concerns: network structure, cell models, and simulation configuration are stored in distinct HDF5 groups that can be validated and processed independently [[Dai et al. 2020]](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007696).

## Technical Specification

SONATA defines three primary file types: network files (`.h5`), node files (containing cell definitions and positions), and edge files (containing connectivity). Node files specify cell types, their intrinsic parameters (e.g., leak conductance, time constants for [adaptive-exponential-integrate-and-fire]([[adaptive-exponential-integrate-and-fire]]) or [izhikevich]([[izhikevich-neuron-model]]) models), and optionally their morphological structures. Edge files encode synaptic connections as source-target pairs with associated weight and delay distributions.

The format supports both virtual tissue configurations (where external drives are injected via virtual sources) and detailed recurrent architectures. Simulation configuration—including timestep, duration, electrode locations for LFP recording, and spike recording settings—is specified in a separate Python configuration file that references the SONATA data files. This separation allows users to reuse the same network definition across multiple simulation configurations or parameter sweeps.

## Relationship to TVB and Whole-Brain Modeling

While SONATA was developed primarily for cortical microcircuit and fine-scale network modeling, its concepts have influenced the development of whole-brain simulation frameworks like [The Virtual Brain]([[the-virtual-brain]]). Both approaches share the principle of separating network structure (connectivity, cell populations) from dynamical models and simulation configuration. In practice, TVB's own [neural-mass-model]([[neural-mass-models]]) formulations operate at a coarser level of abstraction than the point-neuron models typical of SONATA, but the underlying need for standardized connectivity inputs—particularly from diffusion imaging-derived [structural-connectivity]([[structural-connectivity]]) matrices—reflects similar interoperability concerns. Tools like [bluepyopt]([[bluepyopt]]) can be used to optimize parameters in SONATA-specified networks, a workflow that parallels TVB's [parameter-estimation]([[parameter-estimation]]) routines.

## Key Features

SONATA offers several distinguishing capabilities that have driven its adoption in the computational neuroscience community. The format employs an HDF5-based binary format that enables efficient storage of millions of connections while maintaining high I/O performance for large-scale simulations [[Dai et al. 2020]](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007696). Its simulator-agnostic specification of network structure allows compatibility with [Brian2]([[brian2]]), [NEST]([[nest]]), and [NEURON]([[neuron]]) through various adapter libraries such as the Brain Modeling Toolkit (BMTK), PyNN, and NetPyNE. The format enforces a clear separation of node (cell), edge (connection), and simulation configuration concerns, enabling modular reuse of network definitions across different simulation contexts. SONATA supports both morphological reconstructions and multi-compartment neuron specifications alongside simpler point-neuron models. Additionally, the `sonata-validate` command-line utility provides built-in validation of network files for compliance with the specification. The format integrates seamlessly with Blue Config and the broader Blue Brain Project simulation ecosystem, facilitating interoperability between different modeling tools developed by the Allen Institute and Blue Brain Project communities.

## Relationship to Other Software

SONATA occupies a similar niche to [NeuroML]([[neuroml]]) in providing declarative model specification, but SONATA's focus on large-scale point-neuron networks and tight integration with specific simulators differentiates it from NeuroML's broader scope spanning multiple cell classes and signal types. Unlike TVB's integrated approach, SONATA adopts a more modular philosophy where the network definition is decoupled from the dynamical model specification and the simulator. The format complements [PyNEST]([[pynest]]) libraries and the broader [netpyne]([[netpyne]]) ecosystem for network specification.

## Limitations and Open Questions

As of 2026, SONATA remains primarily oriented toward point-neuron architectures. Extensions or workarounds are required for full [neural-mass-model]([[neural-mass-models]]) formulations or spatially continuous field models typical of whole-brain simulators. The community has not fully converged on a unified intermediate representation that could bridge SONATA's point-neuron focus with the coarse-grained [neural-mass-model]([[neural-mass-models]]) approaches used in TVB and similar frameworks. Ongoing discussions in the [Open Source Brain]([[open-source-brain]]) community address whether SONATA should extend to support parameter variations for [personalized-brain-modeling]([[personalized-brain-modeling]]) workflows.

## Key Papers

- Dai K, Hernando J, Billeh YN, Gratiy SL, Planas J, Davison AP, et al. (2020). The SONATA data format for efficient description of large-scale network models. PLoS Computational Biology, 16(2), e1007696. https://doi.org/10.1371/journal.pcbi.1007696

- Arkhipov A, Gouwens NW, Billeh YN, Gratiy S, Iyer R, Wei Z, et al. (2018). Visual physiology of the layer 4 cortical circuit in silico. PLoS Computational Biology, 14(11), e1006535.

- Markram H, Muller E, Ramaswamy S, Reimann MW, et al. (2015). Reconstruction and Simulation of Neocortical Microcircuitry. Cell, 163(2), 456-492.

## References

- Dai K, Hernando J, Billeh YN, Gratiy SL, Planas J, Davison AP, Dura-Bernal S, Gleeson P, Devresse A, Dichter BK, Gevaert M, King JGH, Van Geit WAH, Povolotsky AV, Muller E, Courcol J-D, Arkhipov A. (2020). The SONATA data format for efficient description of large-scale network models. PLoS Comput Biol 16(2): e1007696. https://doi.org/10.1371/journal.pcbi.1007696

- Allen Institute for Brain Science. SONATA Data Format Repository. https://github.com/AllenInstitute/sonata

- Blue Brain Project. libSONATA Library. https://github.com/BlueBrain/libsonata

- Dura-Bernal S, Suter BA, Gleeson P, Cantarelli M, Quintana A, Rodriguez F, et al. (2019). NetPyNE, a tool for data-driven multiscale modeling of brain circuits. eLife, 8, e44494.

- Davison AP, Brüderle D, Eppler J, Kremkow J, Muller E, Pecevski D, et al. (2009). PyNN: A Common Interface for Neuronal Network Simulators. Front Neuroinform 2: 11.
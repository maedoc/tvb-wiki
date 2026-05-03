title: NeuroM
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-neuroml, software-visualization, software-brian, computational-neuroscience, neuron, morphometrics, blue-brain-project, ebrains]
sources: [raw/papers/arxiv-1234.56789.md]
---

## Overview

NeuroM is a Python-based toolkit for the analysis and processing of neuronal morphologies, developed by the [[blue-brain-project]] at the École Polytechnique Fédérale de Lausanne (EPFL). The software provides a comprehensive suite of tools for extracting quantitative morphometric features from digitally reconstructed neurons, enabling researchers to characterize axonal and dendritic branching patterns, measure segment lengths and volumes, and perform statistical analyses across populations of neurons. Originally released in 2015[^1], NeuroM has become a standard tool in the [[computational-neuroscience]] community for morphology-related workflows, particularly within the [[human-brain-project]] ecosystem and its successor infrastructure [[ebrains]].

## Key Features

NeuroM offers three primary functionality categories that form the backbone of morphology analysis workflows. First, the **feature extraction engine** provides access to over 50 morphometric quantities[^2] including segment lengths, section lengths, volumes, surface areas, bifurcation angles, branch orders, and path lengths—all accessible through both a Python API and command-line interface. Second, the **validation system** (`neurom check`) performs semantic checks on morphology files to verify structural integrity, including detection of missing parents, invalid soma definitions, zero-length segments, and other common artifacts in digitally reconstructed neurons. Third, the **visualization module** supports 2D and 3D plotting of neuron morphologies as well as dendrogram representations for analyzing hierarchical branching structure.

The software supports standard morphology file formats including SWC, NeuroLucida ASCII, and HDF5-based formats through its dependency on the [[morphio]] library. Morphometrics can be extracted at multiple levels of granularity—individual neurites (axon, basal dendrites, apical dendrites), specific neurite types, or entire neurons—and exported to JSON or CSV format for downstream analysis. The design philosophy emphasizes composability: users can combine orthogonal iterator and morphometric components to implement custom analyses beyond the pre-packaged feature functions.

## Relationship to TVB

While NeuroM operates at the level of individual neuronal morphologies rather than [[whole-brain-modeling]], it maintains indirect relevance to [[the-virtual-brain]] (TVB) in several ways. Detailed single-neuron reconstructions processed by NeuroM can inform biophysically detailed neuron models used in TVB's [[neural-mass-model]] extensions or as part of hybrid multi-scale simulations. Furthermore, the morphometric features extracted by NeuroM—particularly those characterizing dendritic architecture—can inform parameterization of simplified neural models that capture essential anatomical constraints without full morphological detail. NeuroM's integration with the [[ebrains]] research infrastructure positions it as a potential source of morphology data for TVB simulations targeting specific neuron types from the [[allen-brain-atlas]] for experimental validation or clinical applications[^3].

## Key Papers

The primary citation for NeuroM is its Zenodo repository (DOI: 10.5281/zenodo.597333)[^1], which serves as the canonical reference for the software package. The software is closely tied to Blue Brain Project publications on neocortical microcircuit reconstruction, particularly the landmark paper by Markram et al. (2015)[^4] that established the cellular-level modeling framework. Additionally, the neuron classification schemes defining the 55 morphological types (m-types)[^5] used in BBP's cellular-level models are documented in the literature on cortical neuron taxonomy[^6]. Development has been further supported through GitHub issues and the ReadTheDocs documentation.

## Related Software

NeuroM exists within a broader ecosystem of morphology-related tools from the Blue Brain Project. [[neurots]] provides morphology synthesis by generating statistically realistic digital neurons based on topological profiles from reference reconstructions. [[neuror]] offers repair utilities for curating morphologies affected by common histological artifacts such as cut planes from tissue slicing. [[neuron]] (NEURON simulator) and [[brian2]] are related [[spiking-neural-networks]] simulators that can incorporate morphologically detailed neuron models created using NeuroM-processed reconstructions. The [[neuroml]] standard provides a model description language for neuron morphologies that complements NeuroM's analysis capabilities with interoperability features. For visualization, [[brainrender]] and [[neuroMorphoVis]] offer alternative rendering approaches for morphological data. The Allen Institute's [[allen-brain-atlas]] and [[neuromorpho]] database represent major sources of morphology data that can be analyzed using NeuroM, collectively providing access to thousands of digitally reconstructed neurons from various species and brain regions.

## References

[^1]: NeuroM Team. NeuroM: Neuron Morphology Analysis Toolkit. Zenodo. DOI: 10.5281/zenodo.597333. Available at: https://zenodo.org/records/597333

[^2]: NeuroM Documentation. Feature Extraction. Available at: https://neurom.readthedocs.io/

[^3]: Allen Institute for Brain Science. Allen Mouse Brain Atlas. Available at: https://atlas.brain-map.org/

[^4]: Markram, H., Muller, E., Ramaswamy, S., Reimann, M.W., Warren, M., et al. (2015). Reconstruction and Simulation of Neocortical Microcircuitry. *Cell*, 163(2), 456-492. DOI: 10.1016/j.cell.2015.09.029

[^5]: Blue Brain Project. (2023). Neuron Morphology Types and Classification. Available at: https://bbp.epfl.ch/nse-pub/nse1

[^6]: Rezm, S., et al. (2013). Systematic Integration of Morphological and Functional Cortical Neuron Types. *Neural Plasticity*, 2013, 768451. DOI: 10.1155/2013/768451
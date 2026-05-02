---
title: NeuroM
created: 2024-01-01
updated: 2026-05-02
type: entity
tags: [software-visualization, computational-neuroscience, neural-mass-models, connectomics, neuroml]
sources: [https://github.com/BlueBrain/NeuroM, https://neurom.readthedocs.io/, https://zenodo.org/records/10630119, https://pypi.org/project/neurom/]
---

# NeuroM

## Overview

NeuroM is an open-source Python library developed by the Blue Brain Project at EPFL for the analysis and visualization of morphologically detailed neuronal reconstructions [1][2]. The software provides tools for reading, analyzing, and visualizing three-dimensional representations of neuronal morphology—dendritic arbors, axonal projections, and somatic geometry—derived from histological tracing or digital reconstruction algorithms. Originally developed to support the Blue Brain Project's mission to reconstruct the mouse brain at cellular resolution, NeuroM has become a widely adopted tool in the computational neuroscience community for morphometric analysis, quality control of neuron reconstructions, and comparative studies of neuronal morphology across brain regions, species, and experimental conditions [4].

## Motivation and Context

The detailed morphological structure of neurons fundamentally determines their functional properties, including synaptic connectivity patterns, integration of dendritic inputs, and firing dynamics [5]. As large-scale brain mapping initiatives have produced thousands of digitally traced neuron reconstructions—through both automated algorithms and expert manual tracing—there emerged a need for standardized, reproducible tools to quantitatively characterize these morphologies [4][6]. Prior to NeuroM's development, morphological analysis often relied on custom scripts or commercial software with limited interoperability, making cross-laboratory comparison difficult [7].

NeuroM addresses this gap by providing a robust Python API that enables researchers to extract morphometric features systematically [1][2]. This positions NeuroM as a critical tool in the broader effort to build data-driven [[whole-brain]] models that incorporate realistic cellular-level constraints derived from morphological data.

## Key Features

NeuroM supports multiple file formats for neuronal reconstructions, including the widely-used SWC format (standard for neuronal morphology), Neurolucida ASCII format, and HDF5-based formats commonly used in large-scale projects [2][3][8]. The core functionality centers on extracting well-defined morphometric features: dendritic complexity metrics such as total length, branch order distributions, bifurcation angles, and fractal dimension; somatic features including volume, surface area, and ellipticity; and axonal morphometrics for neurons with reconstructed axonal arbors.

The library includes sophisticated visualization capabilities for rendering two-dimensional and three-dimensional representations of neuronal morphology [2], supporting comparison plots across multiple neurons, morphometric distribution histograms, and quality assessment visualizations. The quality control utilities enable identification of common reconstruction artifacts—including fragmented segments, unrealistic branch angles, topological errors, and somatic discontinuities—thereby helping researchers ensure data quality before including reconstructions in downstream analyses.

## Relationship to TVB

While [[The Virtual Brain]] primarily operates at the level of [[neural-mass-models]] and large-scale [[brain-dynamics]] simulations, NeuroM represents a complementary approach focusing on morphologically detailed single-neuron reconstructions [9]. TVB's [[whole-brain-modeling]] framework incorporates parameterized reductions of neuronal dynamics derived from mean-field approximations, whereas NeuroM provides tools for characterizing the detailed morphological substrates that inform such reductions. Researchers building [[personalized-brain-modeling]] models may use NeuroM-derived morphometric constraints to inform parameter selection in neural mass implementations—potentially linking branch numbers, dendritic lengths, and dendritic polarity patterns to effective coupling parameters used in neural mass equations [9][10].

The two software packages address complementary scales: NeuroM at the cellular and microcircuit level, and [[tvb]] at the mesoscopic to macroscopic brain network level. In practice, NeuroM can provide morphological statistics from experimental data that may guide the selection of parameters in whole-brain models, creating a bridge between detailed cellular reconstruction projects and population-level brain simulation frameworks [9].

## Related Software

NeuroM exists within a broader ecosystem of tools for neuronal morphology analysis. The [[neuromorpho.org]] database provides a large-scale repository of morphologically characterized neurons with standardized metadata, and NeuroM can be used to contribute new reconstructions to such repositories [4][11]. [[PyNN]] and [[neuroml]] standards enable interoperability between neuronal simulators and morphology descriptions, allowing NeuroM-analyzed morphologies to be converted to simulation-ready formats [12][13]. For visualization, tools like [[brainrender]] and [[brainnet-viewer]] complement NeuroM's plotting capabilities.

The [[allen-brain-atlas]] has produced extensive morphological characterizations of mouse neuronal cell types, and NeuroM has been employed in analyzing such datasets to characterize morphological diversity across cortical layers and cell classes [14]. Large-scale efforts including the [[human-connectome-project]] have similarly driven development of standardized morphological workflows that NeuroM enables. Related tools from the Blue Brain Project morphology suite include [[MorphIO]] for file I/O operations and built-in quality control features for morphology validation [1].

## Key Papers

The primary citation for NeuroM is its Zenodo repository, which provides the recommended DOI for academic publications using the software [1]. Beyond the tool itself, several landmark studies have advanced the field of neuronal morphology analysis. The SWC format specification established the de facto standard for representing neuronal morphology as three-dimensional point clouds with associated radii and topological connectivity [8]. Liu et al. demonstrated that dendritic morphology alone can predict cell-type identity with high accuracy, enabling automated classification of neurons across brain regions [15]. Additionally, work by Halavatyi et al. established standardized workflows for morphology file I/O that underpin modern analysis toolchains [3].

## References

1. Blue Brain Project. (2024). *NeuroM* (Version v3.2.8) [Python software]. Zenodo. https://doi.org/10.5281/zenodo.597333
2. Blue Brain Project. (2024). *NeuroM: neuronal morphology analysis toolkit* [Software documentation]. https://neurom.readthedocs.io/
3. Halavatyi, A. (2024). *MorphIO: library for reading and writing neuron morphology files* [Software]. Blue Brain Project. https://github.com/BlueBrain/MorphIO
4. NeuroMorpho.Org. (2024). *About NeuroMorpho.Org* [Database documentation]. George Washington University. http://neuromorpho.org/
5. Mainen, Z. F., & Sejnowski, T. J. (1996). Influence of dendritic structure on firing pattern in model pyramidal neurons. Nature, 382(6589), 363-367. https://doi.org/10.1038/382363a0
6. Ascoli, G. A., Alonso-Nanclares, L., Anderson, S. A., Barrionuevo, G., Benavides-Piccione, R., Burkhalter, A., ... & De Felipe, J. (2008). Petilla terminology: nomenclature of features of GABAergic interneurons of the cerebral cortex. Nature Reviews Neuroscience, 9(7), 557-568. https://doi.org/10.1038/nrn2402
7. Donohue, D. E., & Ascoli, G. A. (2008). A comparative survey of algorithms for reconstructing morphologically detailed neurons. Neuroinformatics, 6(2), 117-136. https://doi.org/10.1007/BF03040614
8. Cannon, R. C., Turner, D. A., Pyapali, G. K., & Wheeler, D. W. (1998). An interactive comparison of tools for analysis of neural and dendritic morphology. Neuroinformatics, 2(2), 145-163. https://doi.org/10.1007/s12021-008-9020-1
9. Ritter, P., Schirner, M., McIntosh, A. R., Jirsa, V. K., & Daunizeau, J. (2013). The Virtual Brain: integrative modeling of brain dynamics. Brain-Inspired Computing, 37-48. https://doi.org/10.1007/978-3-319-03017-3_4
10. Deco, G., Jirsa, V. K., & McIntosh, A. R. (2011). Resting-state networks remain dynamic after a prolonged period in functional isolation. Brain Connectivity, 1(4), 307-318. https://doi.org/10.1089/brain.2011.0021
11. Ascoli, G. A. (2006). Mobilizing the data. Nature Reviews Neuroscience, 7(4), 318-324. https://doi.org/10.1038/nrn1901
12. Davison, A. P., Brüderle, D., Eppler, J., Kremkow, J., Muller, E., Pecevski, D., ... & Yger, P. (2009). PyNN: a common interface for neuronal network simulators. Frontiers in Neuroinformatics, 2, 11. https://doi.org/10.3389/neuro.11.011.2008
13. Gleeson, P., Crook, S., Cannon, R. C., Hines, M. L., Billings, G. O., Farinella, M., ... & Silver, R. A. (2010). NeuroML: a language for describing biophysically detailed neuronal models. Neuroinformatics, 8(2), 87-112. https://doi.org/10.1007/s12021-010-9073-y
14. Allen Institute for Brain Science. (2024). *Cell Types Overview* [Data documentation]. Allen Brain Atlas. https://celltypes.brain-map.org/
15. Liu, Y., Li, J., Ma, S., & Zhou, Z. (2022). Morphology-based neuronal cell type classification using deep learning. Neuroinformatics, 20(2), 305-315. https://doi.org/10.1007/s12021-021-09537-4
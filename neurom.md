---
title: NeuroM
created: 2025-01-15
updated: 2026-05-02
type: entity
tags: [software-visualization, software-neuron, computational-neuroscience, neural-mass-models, brain-modeling, neuroml]
sources: [https://zenodo.org/records/10630119, https://github.com/BlueBrain/NeuroM, https://neurom.readthedocs.io/en/v1.4.3/index.html]
---

# NeuroM

## Overview

NeuroM is a Python-based software package developed primarily by the Blue Brain Project at EPFL for analyzing and visualizing the three-dimensional morphology of neurons. The package provides a comprehensive framework for reading, processing, and extracting quantitative features from neuronal morphologies represented in standard file formats such as SWC, HDF5, and NeuroLucida [@neurom-zenodo]. Neuronal morphology—the intricate geometric structure of axons, dendrites, and dendritic spines—constitutes a fundamental determinant of neuronal computational function, and NeuroM enables researchers to systematically characterize this structural diversity across cell types, brain regions, and species.

The software emerged from the need to automate the extraction of morphological metrics that previously required tedious manual measurement, enabling reproducible, large-scale analyses of neuronal anatomy. First released in 2015, NeuroM has undergone continuous development through major version updates, with version 4.0 released in 2024 [@neurom-pypi]. The package serves as both a standalone analysis tool and a library that can be integrated into larger neuroscience analysis pipelines, particularly those involving the [[neuron]] simulator or [[neuroml]] model specifications.

## Relationship to TVB

While [[NeuroM]] is not directly integrated into [[The Virtual Brain]] (TVB), it addresses a complementary aspect of whole-brain modeling: the detailed characterization of individual neuronal morphologies that inform mesoscopic and macroscopic connectome models. Whole-brain modeling frameworks like TVB often rely on simplified neural mass representations that aggregate the computational properties of large neuronal populations; understanding the underlying diversity of neuronal morphologies helps validate and constrain these coarse-grained models. The morphological statistics extracted by NeuroM—such as total dendritic length, branching complexity, and spine density distributions—can inform parameter choices in neural mass models and contribute to more biologically plausible representations of cortical microcircuitry.

## Key Features

NeuroM provides several core analysis capabilities essential for quantitative morphology studies. The package can compute fundamental morphometric metrics including total cable length, number of branches, branch order distributions, bifurcation angles, and soma dimensions. It supports the analysis of dendritic trees and axonal arbors separately, enabling researchers to distinguish between input (dendritic) and output (axonal) structural properties.

The software includes sophisticated filtering and subsetting capabilities, allowing analysts to focus on specific neuronal compartments or exclude artifacts commonly encountered in reconstruction data. NeuroM implements standard morphometric conventions used in the neuroscience community, ensuring compatibility with established datasets in the [[neuromorpho]] database and other public repositories. Visualization tools generate publication-quality renderings of neuronal morphologies, with options to color-code branches by various metrics such as diameter, distance from soma, or branch order.

Additionally, NeuroM supports batch processing of large morphology datasets, making it suitable for meta-analyses across hundreds or thousands of reconstructed neurons. The package relies on the MorphIO library for standardized file handling, facilitating interoperability with other Blue Brain Project tools in the morphology processing ecosystem [@morphio-docs].

## Technical Capabilities

NeuroM is implemented in Python and leverages the MorphIO library as a core dependency for reading and writing neuron morphology files. The architecture separates concerns between data reading, metric computation, and visualization, allowing users to extend functionality through plugin-like modules. The software handles the SWC format widely used for neuronal reconstructions, as well as NeuroLucida ASCII and HDF5-encoded morphologies. Quality control features identify common reconstruction artifacts including duplicate points, unrealistic diameters, and topological errors, supporting automated screening of morphology datasets prior to quantitative analysis.

The package provides both a programmatic API for integration into larger analysis pipelines and command-line applications for common tasks such as morphology validation (`morph_check`) and feature extraction (`morph_stats`). Version 3.0 introduced significant API improvements and performance optimizations for handling large datasets [@neurom-v3].

## Related Software

NeuroM intersects with several other tools in the neuroscience software ecosystem. The [[neuromorpho]] database serves as a public repository of morphological reconstructions that can be analyzed using NeuroM. The [[neuron]] simulator uses morphological reconstructions to define cell geometries in neural simulations, and NeuroM can validate and preprocess morphologies for such simulations. [[neuroml]] provides a standardized format for exchanging neuronal models including morphology descriptions, and NeuroM supports reading and writing NeuroML-compliant files. The [[brian2]] simulator similarly benefits from morphology data processed through tools like NeuroM. Within the Blue Brain Project ecosystem, NeuroM works closely with MorphIO for file format handling, NeuroR for morphology repair, and NeuroTS for synthetic morphology generation [@bbp-morphology-suite]. For visualization beyond what NeuroM provides, researchers often use brainrender or VTK-based viewers for three-dimensional rendering of neuronal morphologies in anatomical context.

## Key Applications

NeuroM has been applied in comparative studies of neuronal morphology across brain regions, species, and developmental stages. Its automated analysis capabilities enable systematic quantification of how dendritic architecture varies between excitatory and inhibitory neurons, or between superficial and deep cortical layers. The software supports investigations into structure-function relationships by providing quantitative morphological descriptions that can be correlated with electrophysiological measurements or connectomic data. In the context of modeling, NeuroM-derived statistics inform the parameterization of morphologically detailed neural simulations and validate the biological plausibility of reconstructed circuits.

The tool has been particularly valuable in the context of the Human Brain Project, where it supports the EBRAINS Cellular Level Simulation Platform by providing standardized morphology analysis capabilities for data quality control and statistical characterization of digital neuron reconstructions [@hbp-funding].

## Key Papers

- Blue Brain Project. (2015-2024). *NeuroM: A light-weight neuron morphology analysis package* (Version 4.0.4) [Software]. Zenodo. https://doi.org/10.5281/zenodo.597333 [@neurom-zenodo]

## References

[@neurom-zenodo]: Blue Brain Project. (2024). NeuroM (Version v3.2.8) [Software]. Zenodo. https://zenodo.org/records/10630119

[@neurom-pypi]: Blue Brain Project. (2024). neurom v4.0.4 [Python package]. PyPI. https://pypi.org/project/neurom/

[@morphio-docs]: Blue Brain Project. MorphIO - A library for reading and writing neuron morphology files. https://morphio.readthedocs.io/en/latest/

[@neurom-v3]: Blue Brain Project. (2022). BlueBrain/NeuroM: v3.2.0 [Software]. Zenodo. https://zenodo.org/records/6524037

[@bbp-morphology-suite]: Blue Brain Project. (2021). BlueBrain/morphology-suite [Software repository]. GitHub. https://github.com/BlueBrain/morphology-suite

[@hbp-funding]: European Commission. Human Brain Project Funding Information. https://www.humanbrainproject.eu/en/about/
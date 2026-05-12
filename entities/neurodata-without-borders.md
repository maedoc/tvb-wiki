---
created: 2026-04-24
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/van-essen-2013.md
- raw/papers/gorgolewski-2016.md
tags:
- software-brain-modeling
title: Neurodata Without Borders
type: entity
updated: '2026-05-11'
---

## Overview

**Neurodata Without Borders (NWB)** is a data standard and file format specification designed to standardize the storage and sharing of neurophysiology data across laboratories, institutions, and analysis tools. Developed through a community-driven process led by the [INCF](](https://www.incf.org/)) [1] and supported by major neuroscience initiatives including the Human [[connectome]] Project [[human-connectome-project]] [2], NWB provides a unified framework for representing [[electrophysiology]] data, imaging data, and behavioral measurements in a way that enables interoperability between different software ecosystems. The format addresses a fundamental challenge in modern neuroscience: the explosion of data from large-scale recordings made possible by technologies like multi-electrode arrays, [[neuromorpho-toolkit]] probes, and high-density [[EEG]] systems, which has outpaced the field's ability to share and integrate data across studies [3].

## Motivation and Context

The neuroscience community has historically suffered from fragmented data formats, with each laboratory developing custom solutions for storing their electrophysiology recordings. This fragmentation creates significant barriers to data reuse, makes it difficult to compare results across studies, and impedes the development of standardized analysis pipelines. Before NWB, researchers spent substantial time converting between formats or writing custom parsers, and collaborative projects often required extensive data harmonization efforts. The NWB initiative emerged from the recognition that sustainable progress in large-scale neuroscience requires agreed-upon standards that balance expressiveness with practical implementation [3].

The development of NWB shares philosophical principles with the [BIDS](](bids)) (Brain Imaging Data Structure) community [4] and broader data-sharing initiatives like the [Human Connectome Project](](human-connectome-project)) [2] and various [INCF](](https://www.incf.org/)) programs. While BIDS primarily addresses [[neuroimaging]] (MRI/[[fmri]]) data, NWB targets neurophysiology, though both standards share common principles for organized, FAIR-compliant data sharing. Unlike earlier efforts that focused on specific modalities, NWB was designed from the ground up to accommodate diverse neurophysiology data types including single-unit recordings, [[local-field-potentials]], electrocorticography, and behavioral time series [3]. The standard builds upon and integrates with existing formats like [NIX](](nix)) [5] and follows principles established by the [BIDS](](bids)) specification for neuroimaging data [4].

## Technical Specifications

NWB organizes data into a hierarchical structure based on the **HDF5** (Hierarchical Data Format version 5) container format, which provides efficient random access to large datasets and supports complex nested data structures [6]. The schema defines standardized containers called **NWBFile** objects that contain metadata about the recording session, subject information, device specifications, and the actual data arrays. Data are stored in named **TimeSeries** objects that include timestamps, sampling rates, and unit information, along with optional metadata about experimental conditions [7].

The NWB schema has evolved through several versions, with NWB 2.x representing a major refactoring that adopted a more flexible and extensible architecture [8]. Version 2.0 introduced the concept of **Acquisition**, **Analysis**, and **Stimulus** data groups, along with standardized representations for electrode layouts, optical physiology data, and behavioral paradigms [7]. The schema supports both **single-module** and **distributed** data storage patterns, enabling researchers to store complete datasets in a single file or reference external files for particularly large recordings. Crucially, NWB provides mechanisms for storing **metadata about preprocessing pipelines**, enabling reproducible analysis by documenting the exact Steps applied to raw data [9].

## Key Features

One of NWB's most important features is its **extensibility** through custom **extensions** that allow researchers to represent data types not covered by the core schema without breaking compatibility with standard tools [7]. This design principle acknowledges that neuroscience data collection methods continue to evolve rapidly, and the standard must accommodate novel experimental paradigms. The NWB ecosystem includes the **nwb-schema** library for validating files against the specification, the **PyNWB** Python API for programmatic file creation and reading [10], and the **MATLAB** SDK for users in that environment [11].

The standard also provides built-in support for **data provenance** tracking, allowing researchers to document the origin of each data element and any transformations applied. This provenance information is essential for reproducible research and enables downstream users to understand exactly what processing has been applied to "raw" data [9]. NWB files can include **metadata about electrode placement** using standardized coordinate systems, which facilitates integration with anatomical atlases like the Desikan-Killiany atlas [[desikan-killiany-atlas]] and [FreeSurfer](](freesurfer)) parcellations [7]. Additional features include support for parallel HDF5 storage for extremely large datasets, integration with the NIX format for enhanced data model coverage [5], and a growing ecosystem of tools including **[[spikeinterface]]** for electrophysiology analysis [12].

## Relationship to TVB

[NWB](](nwb)) is increasingly relevant to The Virtual Brain [[the-virtual-brain]] ecosystem as the field moves toward [[personalized-brain-modeling]] that requires integration of empirical data from multiple sources. TVB's workflow involves importing [[structural-connectivity]] matrices derived from diffusion MRI [[diffusion-mri]] data and fitting [[neural-mass-models|neural mass model]] parameters to empirical recordings, and NWB provides a standardized format for exchanging these diverse data types. The [Human Connectome Project](](human-connectome-project)) [2] and similar initiatives that distribute large datasets often provide data in NWB format or related standards, making NWB an important bridge format for TVB workflows.

Several [[tvb-adapters]] and export utilities now support conversion to NWB format, facilitating the exchange of simulation outputs and empirical data with other neuroscience tools. The integration with BIDS [[bids-derivatives]] for processed data derivatives is particularly valuable, as it enables TVB users to contribute their modeling results to standardized data repositories that follow FAIR (Findable, Accessible, Interoperable, Reusable) principles.

## Related Software

NWB integrates with a broad ecosystem of neuroscience analysis tools beyond [The Virtual Brain](](the-virtual-brain)). Key integrations include:

- **[PyNWB](https://pynwb.readthedocs.io/)**: The primary Python library for reading and writing NWB files, part of the [NEO](](neo)) ecosystem [10]
- **[MATLAB SDK](https://github.com/NeurodataWithoutBorders/matnwb)**: Official MATLAB implementation for NWB file handling [11]
- **[NIX](nix)**: Related data format that shares conceptual lineage with NWB [5]
- **[SpikeInterface](spikeinterface)**: Framework for electrophysiology analysis that includes NWB export capabilities [12]
- **[Neo](neo)**: Python library for neurophysiology data that provides adapters to NWB format
- **DataLad [[datalad]]**: Version control for data that works well with NWB-formatted datasets
- **NIDM-Results [[nidm-results]]**: Standard for statistical results that complements NWB for complete data packages

The standard is maintained by the [INCF](](https://www.incf.org/)) [1] and has become a cornerstone of major neuroscience data infrastructure projects including the [Brain Initiative](](https://braininitiative.org/)) Cellular Census and various UK Biobank [[uk-biobank]] extension projects.

## Key Papers

1. **NWB: Neurodata Without Borders** — The foundational paper describing the NWB initiative, architecture, and use cases for standardized neurophysiology data exchange.

2. **NWB 2.0: The Next Generation of Neurodata Without Borders** — Describes the major schema refactoring in NWB 2.x including the flexible extension system, improved data organization, and enhanced support for diverse experimental paradigms.

3. **PyNWB: Python library for NWB** — Documentation and paper describing the PyNWB programmatic interface for creating and interacting with NWB files.

4. **The [[bids]] Specification** — The foundational paper for the Brain Imaging Data Structure, which shares philosophical principles with NWB for standardized, FAIR-compliant neuroimaging data organization.

5. **Human Connectome Project: A pipeline for processing and sharing highly quantitative neuroimaging and behavioral data at scale** — Describes the HCP data sharing infrastructure that influenced NWB development and continues to serve as a model for large-scale neuroscience data initiatives.

6. **SpikeInterface: A unified framework for spike sorting** — Describes the electrophysiology analysis framework that integrates with NWB for standardized data export.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain [[connectivity]]. [DOI](](https://doi.org/10.1089/brain.2012.0120))
3. (authors unknown). *The WU-Minn Human Connectome Project: An Overview*.
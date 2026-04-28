---
title: OpenNeuro
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [dataset, database, neuroimaging-fmri, neuroimaging-meg, neuroimaging-eeg, preprocessing, reproducibility, data-sharing, bids]
sources: [raw/articles/openneuro-overview.md]
---

# OpenNeuro

## Overview

OpenNeuro is an open-access repository for neuroimaging datasets, primarily focusing on magnetic resonance imaging (MRI) data including functional MRI (fMRI), structural MRI, diffusion MRI (dMRI), and electroencephalography (EEG) and magnetoencephalography (MEG) data. Launched as a successor to the Open fMRI project [1], OpenNeuro provides a standardized platform for sharing raw and preprocessed neuroimaging data following the Brain Imaging Data Structure (BIDS) specification. The platform enables researchers to upload, download, and analyze large neuroimaging datasets freely, facilitating transparent and reproducible research in computational neuroscience and connectomics. As of 2024, OpenNeuro hosts hundreds of datasets comprising tens of thousands of subject sessions [2], making it one of the largest publicly available neuroimaging resources.

## Motivation and Context

The neuroimaging field has historically faced significant barriers to data sharing [3], including inconsistent file formats, lack of standardized metadata, and the substantial cost of storing and serving large imaging datasets. OpenNeuro emerged to address these challenges by providing a community-driven platform that enforces the [[BIDS]] standard at the point of upload, ensuring that all datasets maintain a consistent organizational structure. This standardization is particularly valuable for researchers developing and validating [[whole-brain model]]s, as it enables systematic retrieval of high-quality structural and functional data across large cohorts. The platform emerged from the recognition that large-scale collaborative efforts—such as those facilitated by the [[human-connectome-project]]—demonstrated the scientific value of open neuroimaging data, but required institutional resources that were not universally accessible.

The adoption of OpenNeuro has been particularly important for the [[computational-neuroscience]] community, where [[parameter-estimation]] and model validation require access to diverse, well-characterized datasets. Researchers working with [[neural-mass-models]] and [[dynamic-causal-modeling]] frameworks can download resting-state fMRI data to calibrate their models, while those interested in [[structural-connectivity]] can access diffusion imaging datasets for tractography-based connectivity estimation. The platform thus serves as critical infrastructure supporting the broader shift toward reproducible neuroimaging research.

## Technical Features

OpenNeuro requires all uploaded datasets to conform to the [[BIDS]] specification, a comprehensive standard that defines the file structure and metadata for neuroimaging experiments [4]. The platform integrates with the [[bids-validator]] to automatically check dataset compliance upon upload [5], ensuring that required JSON sidecar files contain necessary information such as echo times, repetition times, and acquisition parameters. Datasets are organized hierarchically by participant and session, with anatomical, functional, and diffusion imaging stored in NIfTI format alongside complementary JSON metadata.

The platform supports multiple neuroimaging modalities commonly used in whole-brain modeling. Structural MRI datasets provide T1-weighted images used for generating [[brain-parcellations]] and anatomical connectivity matrices. Functional MRI data includes both [[resting-state]] and [[task-based]] acquisitions, enabling researchers to extract [[functional-connectivity]] patterns for model comparison. Diffusion MRI datasets support [[tractography]] analysis for constructing [[structural-connectivity]] networks, which serve as anatomical substrates in [[connectome]]-based models. Some datasets also include concurrently recorded [[eeg]] or [[meg]] data, providing complementary electrophysiological measurements for multimodal modeling efforts.

OpenNeuro provides programmatic access through a RESTful API [6], enabling automated dataset retrieval and integration with preprocessing pipelines such as [[fmriprep]] for fMRI data and [[mrtrix3-connectome]] for diffusion imaging. The platform maintains DOIs for each dataset version [7], ensuring citability and allowing researchers to reference specific data releases in their work.

## Relationship to TVB

While OpenNeuro itself is a data repository rather than a modeling platform, it serves as an important data source for [[the-virtual-brain]] (TVB) workflows. TVB requires structural connectivity matrices derived from diffusion imaging and functional time series from fMRI for model initialization and validation. Researchers developing [[personalized-brain-model]]s can download appropriate datasets from OpenNeuro, process them through TVB-compatible pipelines, and generate individualized connectomes. The [[hcp-dataset]] hosted on OpenNeuro is particularly relevant, as it provides high-quality multi-modal data suitable for TVB model construction. Additionally, OpenNeuro provides datasets from studies of neurological and psychiatric conditions—including [[epilepsy-modeling]] and [[schizophrenia-models]] cohorts—that can be used to investigate disease-specific network dynamics using TVB's modeling frameworks. These datasets enable researchers to compare model predictions against empirical observations from patient populations, facilitating translational research into brain disorders and their的网络动态变化机制.

## Key Datasets and Usage

Several landmark datasets on OpenNeuro have become standard benchmarks in the field. The [[hcp-dataset]] provides high-resolution structural and functional MRI from over 1,000 healthy adult subjects, enabling studies of typical brain connectivity and network organization. The UK Biobank imaging dataset, also accessible through OpenNeuro, represents one of the largest single-population neuroimaging resources available. Specialty datasets cover specific populations relevant to computational modeling, including clinical cohorts for [[alzheimers-modeling]] studies and research on brain development.

Researchers typically access OpenNeuro datasets programmatically using tools like [[datalad]] for efficient version-controlled data retrieval, or directly through the web interface for manual downloads. The platform's integration with popular Python libraries including [[nilearn]], [[nibabel]], and [[pybids]] simplifies data loading and preprocessing within analysis pipelines.

## Related Software

OpenNeuro integrates with a broader ecosystem of neuroimaging tools. For preprocessing, [[fmriprep]] provides robust automated fMRI processing compatible with BIDS-input data, while [[mriqc]] generates quality control metrics. Dataset conversion to BIDS format can be accomplished using tools like [[heudiconv]] and [[bidscoin]]. Visualization and analysis are supported through packages including [[nilearn]] for statistical learning on neuroimaging data, [[mne-python]] for electrophysiological analysis, and [[mrtrix3]] for advanced diffusion modeling. The platform also relates to other data repositories including [[brainlife]] and [[neurovault]], which serve complementary roles in the neuroimaging data ecosystem.

## References

[1] Poldrack, R. A., Barch, D. M., Mitchell, J. P., Wager, T. D., Wagner, A. D., Devlin, J. T., ... & Van Essen, D. C. (2013). Toward open sharing of task-based fMRI data: The OpenFMRI project. *Frontiers in Neuroimaging*, 2. https://doi.org/10.3389/fnimg.2013.00034

[2] OpenNeuro Statistics. (2024). OpenNeuro Public Dataset Catalog. Retrieved from https://openneuro.org

[3] Gorgolewski, K. J., & Poldrack, R. A. (2016). A Practical Guide for Improving Transparency and Reproducibility in Neuroimaging Research. *PLoS Biology*, 14(7), e1002506. https://doi.org/10.1371/journal.pbio.1002506

[4] Gorgolewski, K. J., Auer, T., Calhoun, V. D., Craddock, R. C., Das, S., Dyrolf, E. G., ... & Poldrack, R. A. (2016). The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Scientific Data*, 3, 160044. https://doi.org/10.1038/sdata.2016.44

[5] BIDS Validator. (2024). BIDS Specifications and Validator Documentation. https://bids-specification.readthedocs.io

[6] OpenNeuro API Documentation. (2024). RESTful API for OpenNeuro Dataset Access. https://openneuro.org/documentation

[7] Hankin, D. A., & Poldrack, R. A. (2019). DOI Assignment and Versioning for Neuroimaging Data. *Neuroinformatics*, 17(4), 623-631. https://doi.org/10.1007/s12021-019-09413-1
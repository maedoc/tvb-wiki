---
created: 2024-01-15
sources:
- raw/papers/smith-2013-hcp.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-2f16f2f99d6b.md
- raw/papers/semanticscholar-d94ac445ea77.md
- raw/papers/semanticscholar-d70e1661858c.md
tags:
- dataset
- software-visualization
- neuroimaging
- neuroimaging-fmri
- resting-state
title: Nilearn Datasets
type: entity
updated: '2026-05-04'
---

## Overview

[[nilearn]] Datasets is a Python module within the nilearn library that provides convenient access to a collection of sample [[neuroimaging]] datasets for use in research, education, and software testing. The module is designed to simplify the otherwise complex process of downloading, caching, and preparing neuroimaging data for analysis, making it particularly valuable for researchers developing new analysis pipelines, educators teaching neuroimaging concepts, and developers testing brain imaging software. The datasets module is distributed with nilearn and is typically imported via `nilearn.datasets`, offering fetch functions that automatically handle data download, decompression, and standardized directory organization.

## Motivation and Context

The nilearn library emerged from the need to provide neuroscientists with accessible tools for machine learning and statistical analysis of neuroimaging data, particularly in the context of the Python scientific ecosystem (Abraham et al., 2014). Prior to nilearn's development, researchers often faced significant barriers when attempting to learn new analysis methods, as publicly available neuroimaging datasets were scattered across different repositories, used inconsistent file formats, and required substantial preprocessing before they could be used for demonstration purposes. The nilearn datasets module addresses this gap by bundling several canonical neuroimaging datasets directly within the library, enabling users to begin analyzing data within minutes of installation rather than spending hours locating and preparing suitable data.

This module serves multiple purposes within the broader neuroimaging ecosystem. For educational settings, it provides the HAXBY dataset—a classic example of ventral temporal cortex responses to visual objects that has become a standard teaching dataset in [[fmri]] analysis courses (Haxby et al., 2001). For methodological development, the module includes datasets with varying characteristics (single-subject vs. multi-subject, [[resting-state]] vs. task-based, different acquisition parameters) that allow researchers to test their pipelines under diverse conditions. Additionally, the datasets module integrates seamlessly with nilearn's preprocessing and visualization functions, creating a cohesive workflow from data acquisition through results interpretation.

## Key Features and Functions

The nilearn datasets module provides several fetch functions, each designed to retrieve specific well-characterized datasets. The **`fetch_haxby`** function retrieves the famous HAXBY single-subject dataset from a seminal study on object representation in the ventral temporal cortex, which includes both task-based fMRI data and anatomical scans, making it ideal for learning pattern classification and multivariate analysis techniques (Haxby et al., 2001). The **`fetch_development_fmri`** function provides developmental fMRI data, useful for understanding age-related differences in brain function, while **`fetch_adhd`** accesses the ADHD-200 dataset containing neuroimaging data from individuals with attention-deficit hyperactivity disorder and healthy controls (ADHD-200 Consortium, 2012).

For resting-state [[functional-connectivity]] research, the module offers access to datasets from multiple acquisition epochs. The **`fetch_hcp_rest_partition`** and related functions can access raw or preprocessed data from the [[mrtrix3-connectome]], enabling researchers to work with high-quality resting-state fMRI data without necessitating direct interaction with the HCP data portal (Glasser et al., 2013). The datasets module implements smart caching, meaning that once a dataset is downloaded, subsequent calls to fetch functions retrieve data from local storage rather than re‑downloading, significantly improving workflow efficiency for users who repeatedly work with the same datasets.

## Relationship to TVB and Whole-Brain Modeling

While nilearn itself focuses on statistical learning and data analysis rather than biophysical simulation, the nilearn datasets module has indirect but meaningful connections to [[whole-brain|whole-brain modeling]] and [[the-virtual-brain]] workflows. Many whole-brain modeling studies require empirical functional connectivity data to constrain model parameters or validate simulated dynamics against empirical observations. Researchers using [[tvb|The Virtual Brain]] often need to obtain fMRI or EEG datasets to calculate empirical functional connectivity matrices that serve as targets for model fitting. Nilearn's dataset fetching capabilities streamline this data acquisition process, particularly for researchers who are new to neuroimaging analysis and may be unfamiliar with the complex data organization schemes used by large consortia like the HCP or ADHD-200.

Furthermore, nilearn's integration with other Python neuroimaging libraries—such as [[nibabel]] for [[nifti]] file handling, nistats for statistical modeling (now integrated into nilearn), and nilearn's own [[connectivity]] tools—creates potential synergy with TVB's modeling pipeline. Researchers developing hybrid approaches that combine empirical connectivity analysis with biophysical simulation can use nilearn datasets to rapidly prototype analysis methods before applying them to custom datasets. The [[brain-connectivity-toolbox]] (BCT) and nilearn share overlapping functionality in connectivity analysis, and datasets fetched through nilearn can serve as test data for developing connectivity pipelines that later interface with TVB's [[brain-network]] models.

## Related Software and Toolkits

Nilearn Datasets interfaces with several other software tools in the Python neuroimaging ecosystem. nibabel provides the underlying NIfTI file reading capabilities that allow nilearn to handle neuroimaging data in its native format. nilearn itself extends far beyond its datasets module to provide comprehensive functionality for resting-state connectivity analysis, machine learning classification of brain states, and visualization of neuroimaging results. For preprocessing, nilearn works well with [[fmriprep]], and the datasets module can fetch data that has been preprocessed through pipelines like FSL or SPM.

The module also relates to specialized datasets elsewhere in the ecosystem, including the [[hcp-dataset]], [[uk-biobank]] neuroimaging releases, and cohort-specific datasets available through [[openneuro]]. While nilearn datasets does not directly access all these repositories, it establishes patterns for dataset access that have influenced other tools in the ecosystem, and users familiar with nilearn's fetch functions can easily transition to more specialized data access methods when their research requirements demand larger or more specific datasets.

## Open Questions and Limitations

The nilearn datasets module, while valuable for learning and method development, has important limitations that users should recognize. The bundled datasets are relatively small compared to the massive datasets now available through large consortia, and they may not adequately represent the heterogeneity of clinical populations or diverse demographic groups. Researchers conducting clinical or translational studies should not rely exclusively on nilearn datasets for developing biomarkers or diagnostic classifiers, as these models may not generalize beyond the specific characteristics of the sample datasets.

Additionally, the module does not provide tools for advanced dataset management or version control—there is no built-in mechanism to track which version of a dataset was used in a particular analysis, which can complicate reproducible research practices. Users who require full provenance tracking should consider supplementary tools like [[datalad]] for dataset versioning or more formal data management frameworks. Future development of the nilearn datasets module may address these limitations by incorporating more sophisticated metadata handling and expanding the range of available sample datasets to better serve the growing diversity of neuroimaging research applications.

## Key Papers

- Haxby, J. V., Gobbini, M. I., Furey, M. L., Ishai, A., Schouten, J. L., & Pietrini, P. (2001). Distributed and overlapping representations of faces and objects in ventral temporal cortex. Science, 293(5539), 2425-2430.
- ADHD-200 Consortium. (2012). The ADHD-200 dataset: A showcase for resting-state fMRI. Neuroimage, 62, 1303-1314.
- Glasser, M. F., Sotiropoulos, S. N., Wilson, J. A., Coalson, T. S., Fischl, B., Andersson, J. L., ... & Van Essen, D. C. (2013). The minimal preprocessing pipelines for the [[mrtrix3-connectome]]. Neuroimage, 80, 105-124.
- Abraham, A., Pedregosa, F., Eickenberg, M., Gervais, P., Mueller, A., Kossaifi, J., ... & Thirion, B. (2014). Machine learning for neuroimaging with scikit-learn. Neuroimage, 86, 183-197.

## Related Software

- nibabel: Python library for reading and writing neuroimaging data formats
- [[nistats]]: Statistical modeling for neuroimaging (merged into nilearn)
- fMRIPrep: Robust preprocessing pipeline for fMRI data
- FSL: FMRIB Software Library for neuroimaging analysis
- SPM: Statistical Parametric Mapping for neuroimaging
- Brain Connectivity Toolbox: Graph-theoretic analysis of brain networks
- DataLad: Version control for data and code
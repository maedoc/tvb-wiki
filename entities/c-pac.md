---
created: 2026-04-23
sources:
- raw/papers/alfaro-almagro-2018.md
- raw/papers/penny-2004.md
- raw/papers/avants-2011.md
- raw/papers/woodman-2014.md
- raw/papers/sanz-leon-2013.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/semanticscholar-97e6ff441097.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- resting-state
- functional-connectivity
- connectomics
title: C-PAC
type: entity
updated: '2026-04-23'
---

# C-PAC

## Overview

**C-PAC** (Configurable Pipeline for the Analysis of Connectomes) is an open-source, Python-based neuroimaging pipeline platform designed for reproducible preprocessing and analysis of structural and functional MRI data. Developed by the Child Mind Institute, C-PAC has been utilized by research groups analyzing data from large-scale neuroimaging initiatives such as the ABCD (Adolescent Brain Cognitive Development) Study. The platform implements a modular architecture that enables flexible configuration of preprocessing pipelines while maintaining reproducibility—a critical requirement for multi-site studies where scanner differences and protocol variations can introduce confounds. The platform supports both individual and group-level analyses and is particularly strong in resting-state functional connectivity preprocessing, making it relevant for whole-brain modeling workflows that require high-quality empirical data.

## Key Features

### Configurable Pipeline Architecture
C-PAC employs a YAML-based configuration system that allows researchers to define preprocessing steps, parameter choices, and analysis options without modifying source code. This configurability supports multiple "pipeline strategies" for key preprocessing decisions—such as motion correction methods, nuisance regression approaches, and spatial smoothing kernels—enabling systematic comparison of preprocessing choices on downstream connectivity measures.

### Comprehensive Preprocessing
The platform includes modules for standard fMRI preprocessing including slice-timing correction, motion realignment, spatial normalization to standard templates (MNI152), spatial smoothing, and temporal filtering. C-PAC integrates ANTs for robust registration and implements multiple strategies for nuisance signal removal, including CompCor (Component-based Noise Correction), which identifies nuisance components from white matter and CSF signals rather than relying solely on global signal regression.

### Quality Control and Visualization
A distinguishing feature of C-PAC is its integrated quality control (QC) framework, which automatically generates QC images and metrics for each processing stage. These include motion parameter plots, registration overlays, tissue segmentation visualizations, and connectivity matrix quality flags. This emphasis on QC is essential for large-scale studies where manual inspection of all scans is impractical.

### Network and Connectivity Analysis
C-PAC supports seed-based functional connectivity analysis, ROI-to-ROI correlation matrices, and voxel-wise connectivity mapping. It can generate connectivity matrices using standard parcellation atlases including the [[aal-atlas|AAL Atlas]], [[desikan-killiany-atlas|Desikan-Killiany Atlas]], and custom parcellations. The platform also includes group-level statistical analysis capabilities for comparing connectivity patterns across cohorts.

## Key Papers

- **Cameron Craddock, R., et al. (2013)**. The Neuro Bureau Preprocessing Initiative: Open sharing of preprocessed neuroimaging data and derivatives. *Frontiers in Neuroinformatics*, 7, 27. ([doi:10.3389/fninf.2013.00027](https://doi.org/10.3389/fninf.2013.00027)) — Describes the Neuro Bureau Preprocessing Initiative and the development of C-PAC as an open-source pipeline platform.

- **Ciric, R., et al. (2017)**. Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity. *NeuroImage*, 154, 174-187. ([doi:10.1016/j.neuroimage.2017.04.073](https://doi.org/10.1016/j.neuroimage.2017.04.073)) — Comprehensive evaluation of preprocessing strategies including those implemented in C-PAC.

- **Casey, B. J., et al. (2018)**. The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. *Developmental Cognitive Neuroscience*, 32, 43-54. ([doi:10.1016/j.dcn.2018.03.001](https://doi.org/10.1016/j.dcn.2018.03.001)) — Describes the ABCD Study imaging acquisition protocols across 21 sites.

## Relationship to TVB

C-PAC serves a complementary role to [[tvb|The Virtual Brain]] in connectome-based modeling workflows:

1. **Data Preparation**: C-PAC provides standardized preprocessing pipelines that generate quality-controlled functional connectivity matrices and preprocessed time series suitable for TVB empirical validation. The connectivity matrices output from C-PAC can directly inform TVB's functional connectivity constraints or serve as targets for model fitting.

2. **Reproducibility Bridge**: For TVB studies requiring preprocessing of large datasets (e.g., HCP, UK Biobank, or ABCD), C-PAC offers reproducible, well-documented pipelines that can be exactly replicated—addressing a common challenge in computational neuroscience where preprocessing variability affects model validation.

3. **Motion and Artifact Handling**: C-PAC's systematic approach to motion artifact correction and nuisance regression produces cleaner empirical data that may improve the signal-to-noise ratio when comparing TVB simulations to empirical functional connectivity patterns, particularly important for resting-state studies where motion artifacts correlate with distance-dependent connectivity biases.

## Related Software

- [[tvb|The Virtual Brain]] — Whole-brain simulation platform that can use C-PAC-preprocessed connectivity data
- [[ants|ANTs]] — Advanced registration toolkit integrated into C-PAC for robust spatial normalization
- [[nipype|Nipype]] — Python framework for neuroimaging pipelines; C-PAC shares similar architectural principles
- [[fsl|FSL]] — Alternative preprocessing suite with overlapping functionality
- [[hcp-pipelines|HCP Pipelines]] — Minimal preprocessing pipelines for Human Connectome Project data; often compared with C-PAC strategies
- [[nilearn|Nilearn]] — Python library for neuroimaging analysis that can work with C-PAC outputs

## References

1. Craddock, R. C., Sikka, M., Cheung, B., et al. (2013). The Neuro Bureau Preprocessing Initiative: Open sharing of preprocessed neuroimaging data and derivatives. *Frontiers in Neuroinformatics*, 7, 27. [doi:10.3389/fninf.2013.00027](https://doi.org/10.3389/fninf.2013.00027)

2. Ciric, R., Wolf, D. H., Power, J. D., et al. (2017). Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity. *NeuroImage*, 154, 174-187. [doi:10.1016/j.neuroimage.2017.04.073](https://doi.org/10.1016/j.neuroimage.2017.04.073)

3. Casey, B. J., Cannonier, T., Conley, M. I., et al. (2018). The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. *Developmental Cognitive Neuroscience*, 32, 43-54. [doi:10.1016/j.dcn.2018.03.001](https://doi.org/10.1016/j.dcn.2018.03.001)
---
created: 2026-04-23
sources:
- raw/papers/semanticscholar-301489ffb9de.md
- raw/papers/semanticscholar-24420855b2da.md
- raw/papers/semanticscholar-35c59867495b.md
- raw/papers/braph-2 genesis.md
- raw/papers/glean-github.md
tags:
- software-brain-modeling
- software-visualization
- neuroimaging-fmri
- resting-state
- task-based
title: BrainVoyager
type: entity
updated: '2026-05-04'
---

- "Goebel, R., Esposito, F., & Formisano, E. (2006). Analysis of functional image analysis contest (FIAC) data with brainvoyager QX: From single-subject to cortically aligned group general [[linear|linear model]] analysis and self-organizing group independent component analysis. Human Brain Mapping, 27(5), 392-401."
  - "Sorger, B., Reithler, J., Dahmen, B., & Goebel, R. (2012). A real-time [[fmri]] self-regulation approach to the treatment of chronic, treatment-resistant tinnitus. Neuroscience & Biobehavioral Reviews, 37(4), 697-703."
  - "Brain Innovation. BrainVoyager Documentation and User Guides. https://www.brainvoyager.com/"
---

# BrainVoyager

## Overview

**BrainVoyager** is a commercial [[neuroimaging]] software suite developed by Brain Innovation, designed for the advanced analysis and visualization of structural and functional MRI data. First released in the late 1990s, it has become one of the most widely used platforms for cortical surface-based analysis, real-time fMRI (rt-fMRI), and multi-subject data integration in cognitive neuroscience research.

The software is particularly renowned for its **cortex-based alignment (CBA)** approach, which aligns brains based on individual cortical folding patterns rather than volume-based registration, substantially improving cross-subject alignment in functionally corresponding cortical areas. This makes it highly complementary to [[whole-brain|whole-brain modeling]] workflows that require precise anatomical constraints.

## Key Features

### Cortical Surface Analysis
BrainVoyager provides comprehensive tools for reconstructing and analyzing cortical surface meshes from anatomical MRI scans. Key capabilities include:

- **Gray-[[white-matter]] segmentation** with topology correction
- **Inflated, flat, and spherical cortical surface** representations
- **Cortex-based alignment (CBA)** for improved inter-subject registration
- **Multimodal integration** of fMRI, DTI, and anatomical data

### Functional MRI Analysis
The platform offers a complete pipeline for fMRI data processing:

- **Preprocessing**: motion correction, slice scan time correction, spatial/temporal smoothing, and high-pass filtering
- **Statistical analysis**: general linear model (GLM) estimation, random effects group analysis, and multi-voxel pattern analysis (MVPA)
- **Event-related design optimization** and deconvolution techniques
- **[[resting-state]] analysis** including ICA and seed-based [[connectivity]]

### Real-Time fMRI (rt-fMRI)
BrainVoyager was a pioneer in real-time fMRI neurofeedback applications, enabling:

- Real-time data acquisition and analysis during scanning
- Neurofeedback for brain-computer interface (BCI) research
- Quality assurance during data acquisition
- Integration with external stimulation devices

### HCP Format Compatibility
Modern versions support connectivity analysis compatible with the [[mrtrix3-connectome]] (HCP) file formats, allowing seamless exchange of data with other neuroimaging ecosystems.

## Relationship to TVB

While BrainVoyager and [[TVB]] serve different primary purposes—BrainVoyager focuses on preprocessing and analysis of empirical neuroimaging data, while TVB specializes in computational whole-brain simulation—they are highly complementary in the [[connectome]]-based modeling workflow:

### Data Preparation Pipeline
BrainVoyager can provide critical inputs to TVB simulations:

1. **[[structural-connectivity]]**: DTI [[tractography]] processed in BrainVoyager can be exported as connectivity matrices (structural connectivity) for use in TVB
2. **Cortical Surfaces**: High-resolution cortical meshes generated in BrainVoyager can inform spatial embedding of [[neural-mass-models]]
3. **[[parcellation]] Schemes**: Custom or atlas-based parcellations can be exported for network node definitions
4. **fMRI Time Series**: Preprocessed empirical fMRI data can be used to validate TVB simulations through [[functional-connectivity]] and power spectrum comparison

### Comparative Positioning
| Aspect | BrainVoyager | TVB |
|--------|-------------|-----|
| **Primary Focus** | Experimental data analysis | Computational modeling |
| **Forward/Inverse** | Forward (empirical → BOLD) | Forward (neural → BOLD/EEG) |
| Dynamic Causal Modeling | Indirect (via GLM) | Direct (biophysical models) |
| Parameter Estimation | Limited | Advanced (simulation-based) |

Researchers often use BrainVoyager for preprocessing and standard neuroimaging analysis, then export connectivity matrices and surface data to TVB for mechanistic modeling of [[brain-dynamics]].

## Key Papers

BrainVoyager has been cited in thousands of neuroimaging studies. Key methodological publications include:

- **Goebel et al. (2006)** — Introduced the cortex-based alignment methodology, demonstrating substantial improvements in functional correspondence across subjects compared to volume-based registration.

- **Sorger et al. (2012)** — Established BrainVoyager's rt-fMRI neurofeedback capabilities for clinical and research applications.

- **The software is widely used in HCP-derived studies** utilizing CBA for surface analysis, though specific BrainVoyager publications are typically methodological rather than results-focused.

## Related Software

- [[TVB]] — Whole-brain simulation platform that can use BrainVoyager-processed connectivity data
- [[ANTs]] — Alternative neuroimaging registration tools (volume-based)
- [[3D Slicer]] — Open-source alternative for medical image computing
- **Freesurfer** — Open-source cortical surface reconstruction (complementary/alternative to BrainVoyager's surface tools)
- **FSL** — UK-based open-source fMRI analysis suite (volume-based)
- **SPM** — Statistical parametric mapping toolbox for neuroimaging

## References

1. Muhammad Nabi Yasinzai, R. Mito, M. Pedersen. (2025). *BrainScape: An open-source framework for integrating and preprocessing anatomical MRI datasets*. Imaging neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.944))
2. *Patricia Burhunduli, Zhuo Fang, Katie L. Vandeloo, Pierre Blier, Jennifer L Phillips. (2025). *A PRELIMINARY INVESTIGATION OF RESTING STATE FUNCTIONAL CONNECTIVITY NETWORKS IN PATIENTS WITH TREATMENT-RESISTANT DEPRESSION AND A HISTORY OF SUICIDE ATTEMPT*. International Journal of Neuropsychopharmacology. [DOI](](https://doi.org/10.1093/ijnp/pyae059.440))
3. Andrés Perissinotti, A. Farré-Melero, F. López-González, María del Carmen Mallón-Araujo, Julia Cortés, X. Setoain, Andrea Fritsch, Katherine Quintero, Ángel E. Esteban, S. Morbelli, Matteo Bauckneht, A. Miceli, Aida Niñerola-Baizán, Pablo Aguiar, J. Silva-Rodríguez. (2026). *Added value of quantitative [18F]FDG-PET analysis in MRI-negative epilepsy: A simulation-based study using realistic ground-truths*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2026.121740))
4. (authors unknown). *[[braph]] 2.0 [[genesis]]: An Open-Source Toolbox for Brain Connectivity Analysis*.
5. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
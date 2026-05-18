---
created: 2026-04-20
sources:
- raw/papers/van-essen-2013.md
- raw/papers/van-essen-2012.md
- raw/papers/glasser-2013.md
- raw/papers/smith-2013-hcp.md
- raw/papers/ugurbil-2013.md
- raw/papers/barch-2013.md
- raw/papers/power-2011.md
- raw/papers/miller-2016.md
- raw/papers/sporns-tononi-kotter-2005.md
tags:
- database-hcp
- connectomics
- neuroimaging-fmri
- neuroimaging-dti
title: Human Connectome Project
type: entity
updated: '2026-05-18'
---

# Human Connectome Project (HCP)

The Human Connectome Project (HCP) is a major initiative to map human brain [[connectivity]] in unprecedented detail. Led by the WU-Minn consortium, the project was designed to characterize [[structural-connectivity|structural]] and [[functional-connectivity|functional]] brain connectivity in 1,200 healthy young adults using optimized [[neuroimaging-fmri|functional MRI]], [[diffusion-mri|diffusion MRI]], and structural MRI protocols at both 3T and 7T field strengths [[raw/papers/van-essen-2013.md|Van Essen et al. (2013)]]. To achieve this goal, the HCP developed customized 3T and 7T MRI systems, optimized pulse sequences, and rigorous quality assurance procedures that together established a new technical foundation for multimodal neuroimaging [[raw/papers/van-essen-2012.md|Van Essen et al. (2012)]]. The resulting datasets are openly shared with the scientific community and have enabled thousands of studies of human [[connectomics]] worldwide [[raw/papers/van-essen-2013.md|Van Essen et al. (2013)]].

Beyond data acquisition, the HCP introduced standardized minimal preprocessing pipelines that emphasize [[cortical-surface|surface-based analysis]], cross-modal alignment, and minimal yet effective processing to preserve data quality while enabling comparison across subjects [[raw/papers/glasser-2013.md|Glasser et al. (2013)]]. These open-source pipelines implement a surface-based framework for cortical mapping and have become a standard reference for processing multimodal neuroimaging data [[raw/papers/glasser-2013.md|Glasser et al. (2013)]]. By integrating optimized acquisition with standardized preprocessing and open data sharing, the HCP provides a comprehensive resource for studying human brain connectivity in unprecedented detail [[raw/papers/van-essen-2013.md|Van Essen et al. (2013)]].

## Overview

The Human Connectome Project (HCP) is a large-scale effort to map human brain connectivity in unprecedented detail. The project aims to characterize brain connectivity in 1200 healthy young adults and share the data openly with the scientific community.

## History

### Launch (2010)
Funded by 16 components of the NIH Blueprint for Neuroscience Research, with two main consortia:
- **WU-Minn Consortium**: Washington University and University of Minnesota
- **HCP Lifespan**: Developmental and [[aging]] studies

### Phase I (2010-2015)
- Developed optimized imaging protocols
- Collected data from 1200 healthy young adults
- Released standardized preprocessing pipelines

### Phase II (2015-2020)
- Extended to developmental and aging populations
- Enhanced protocols for special populations
- Disease-related connectome projects

## Data Acquisition

### Imaging Modalities
- **Structural MRI**: T1w and T2w at 0.7mm resolution
- **[[neuroimaging-fmri|Functional MRI]]**: [[resting-state]] and task-based
- **[[diffusion-mri]]**: High angular resolution dMRI
- **MEG**: Magnetoencephalography (subset)

### Scanner Specifications
- **3T MRI**: Customized Siemens Prisma systems
- **7T MRI**: High-resolution structural and functional
- **Multiband acceleration**: Faster acquisition

### Tasks
Seven cognitive domains assessed:
1. Emotion processing
2. Gambling (reward/risk)
3. Language (story/math)
4. Motor (tapping)
5. Relational processing
6. Social cognition
7. Working memory

## Data Processing

### Minimal Preprocessing Pipelines
- Surface-based analysis framework
- Cross-modal alignment
- Quality assurance procedures
- Open-source implementation ([[hcp-pipelines]])

### Available Data
- Raw imaging data
- Preprocessed data
- Behavioral measures
- Parcellations and atlases
- Connectivity matrices

## Scientific Impact

### Publications
- >2000 publications using HCP data
- Standard reference for brain connectivity
- Influenced imaging protocols worldwide

### Key Findings
- High-resolution functional network maps
- Individual variability in connectivity
- Structure-function relationships
- Genetic influences on connectivity

## Resources

### Data Access
- **[[connectomedb]]**: Database for downloading data
- **HCP Website**: humanconnectome.org
- **Open Access**: Free to researchers

### Tools
- **HCP Pipelines**: Preprocessing software
- **Workbench**: Visualization and analysis
- **Cloud**: Amazon Web Services hosting

## Related Concepts
- [[connectome]] – Brain connectivity
- [[connectomics]] – Field of connectivity research
- [[structural-connectivity]] – Anatomical connections
- [[functional-connectivity]] – Statistical dependencies
- neuroimaging-[[fmri]] – Functional MRI
- neuroimaging-dti – Diffusion MRI
- multimodal-imaging – Integrated imaging

## Key People
- [[van-der-pol-oscillator]] – Principal Investigator
- kamil ugurbil – Imaging physics
- steven smith – Analysis methods

## References

1. (authors unknown). *The WU-Minn Human Connectome Project: An Overview*.
2. (authors unknown). *The Human Connectome Project: A Data Acquisition Perspective*.
3. (authors unknown). *The Minimal Preprocessing Pipelines for the Human Connectome Project*.
4. (authors unknown). *Resting-State fMRI in the Human Connectome Project*.
5. (authors unknown). *Pushing Spatial and Temporal Resolution for Functional and Diffusion MRI in the Human Connectome Project*.
6. (authors unknown). *Function in the Human Connectome: Task-fMRI and Individual Differences in Behavior*.
7. (authors unknown). *Functional Network Organization of the Human Brain*.
8. (authors unknown). *Multimodal Population Brain Imaging in the [[uk-biobank]]: Prospective Epidemiological Study*.
9. (authors unknown). *The Human Connectome: A Structural Description of the Human Brain*.
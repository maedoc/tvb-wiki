---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-0aeca1b592e6.md
- raw/papers/Renton2024.md
- raw/papers/huntenburg-2018.md
tags:
- software-fsl
- neuroimaging-fmri
- neuroimaging-dti
- image-processing
- statistics
title: FSL
type: entity
updated: '2026-05-06'
---

# FSL

**FSL** (FMRIB Software Library) is a comprehensive library of analysis tools for [[neuroimaging-fmri|functional MRI]] ([[fmri]]), MRI, and DTI brain imaging data. Developed at the Wellcome Centre for Integrative [[neuroimaging]] at the University of Oxford, FSL is one of the most widely used neuroimaging software packages in the world.

## Overview

FSL provides tools for:
- fMRI preprocessing and statistical analysis
- Structural MRI segmentation and registration
- [[diffusion-mri]] [[tractography]] and analysis
- Brain extraction (BET) and tissue segmentation
- General [[linear|linear model]] (GLM) and mixed-effects analysis

## Key Tools

| Tool | Purpose |
|------|---------|
| **BET** | Brain extraction (skull stripping) |
| **FLIRT** | Linear image registration |
| **FNIRT** | Non-linear image registration |
| **FEAT** | fMRI first-level analysis |
| **MELODIC** | Independent component analysis |
| **TBSS** | Tract-based spatial statistics for DTI |
| **BEDPOSTX** | Diffusion parameter estimation |
| **PROBTRACKX** | Probabilistic tractography |

## Relationship to TVB

FSL tools are commonly used in TVB preprocessing pipelines:
- **Brain extraction** (BET) generates the cortical surface mask
- **Segmentation** (FAST) produces grey matter, [[white-matter]], and CSF maps
- **Registration** (FLIRT/FNIRT) aligns subject anatomy to standard atlases
- **Tractography** (BEDPOSTX + PROBTRACKX) generates [[structural-connectivity]] matrices used as TVB input
- [[tbss]] and bedpostx outputs feed into [[whole-brain]] [[connectome]] construction for [[the-virtual-brain]] simulations

## Software Ecosystem

FSL is part of a broader neuroimaging toolchain:
- [[freesurfer]] — cortical surface reconstruction (often used together)
- [[ants]] — alternative registration tool
- [[spm]] — alternative statistical analysis package
- [[mrtrix3]] — alternative DTI/tractography suite
- [[dipy]] — Python-based diffusion analysis

## References

- FSL website: https://fsl.fmrib.ox.ac.uk/
- Smith et al. (2004) — Advances in functional and structural MR image analysis and implementation as FSL
- Jenkinson et al. (2012) — FSL overview paper
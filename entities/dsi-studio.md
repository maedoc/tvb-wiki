---
title: DSI Studio
created: 2026-04-23
updated: 2026-05-04
type: entity
tags:
- software-brain-modeling
- diffusion-imaging
- tractography
- connectomics
- structural-connectivity
- neuroimaging-dti
sources:
- raw/papers/arxiv-2602.09852.md
- raw/papers/semanticscholar-adcab180dcd3.md
- raw/papers/semanticscholar-c393c4c4a671.md
- raw/papers/semanticscholar-fcd025fcc10c.md
- raw/papers/arxiv-2602.18072.md
---

# DSI Studio

## Overview

DSI Studio is an open-source diffusion MRI analysis and tractography software package developed by Fang-Cheng Yeh. It supports multiple diffusion models including diffusion tensor imaging (DTI), diffusion spectrum imaging (DSI), and generalized q-sampling imaging (GQI), and provides tools for fiber tracking, connectivity matrix generation, and network analysis.

## Key Features

- Multi-model diffusion reconstruction (DTI, DSI, GQI)
- Deterministic and probabilistic fiber tracking
- Connectivity matrix generation from tractography
- ROI-based and seed-based tractography
- Tract density imaging (TDI) and track clustering
- Native support for major diffusion MRI formats (DICOM, NIfTI, FSL)

## Relationship to TVB

DSI Studio generates structural connectivity matrices that can be directly imported into TVB as the anatomical scaffold for whole-brain simulations. The fiber count or tract density between regions serves as the weights in TVB's connectivity matrix, while mean tract length estimates inform conduction velocity and delay parameters. This pipeline is commonly used in epilepsy modeling, where patient-specific diffusion MRI tractography defines the structural backbone of the virtual brain.

## Key Papers

- Yeh, F. C., Wedeen, V. J., & Tseng, W. Y. I. (2010). Generalized q-sampling imaging. *IEEE Transactions on Medical Imaging*, 29(9), 1626–1635.
- Yeh, F. C., & Tseng, W. Y. I. (2011). NTU-90: a high angular resolution brain atlas constructed by q-space diffeomorphic reconstruction. *NeuroImage*, 58(1), 91–99.
- Yeh, F. C. (2020). Shape analysis of the human connectome in Alzheimer's disease. *NeuroImage*, 225, 117527.

## Related Software

* [[mrtrix3]]
* [[fsl]]
* [[ants]]
* [[tvb]]
* [[dipy]]
* [[brainlife]]

---
title: "nnU-Net"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [nnu-net, deep-learning, medical-image-segmentation, neuroimaging, python]
sources: []
---

# nnU-Net

**nnU-Net** is a self-configuring deep learning framework for biomedical image segmentation. It automatically adapts its configuration (preprocessing, network architecture, training parameters) to new datasets without manual hyperparameter tuning, making it one of the most successful methods in medical image analysis challenges.

## Overview

nnU-Net is built on U-Net architecture principles but adds automatic pipeline configuration:
- **Automatic preprocessing** — resampling, intensity normalization, patch size selection based on dataset statistics
- **Cross-validation** — built-in k-fold cross-validation for robust evaluation
- **Ensembling** — model ensembles across folds and 2D/3D configurations
- **Post-processing** — connected component analysis for label refinement

## Relationship to TVB

nnU-Net enables automated brain segmentation that feeds into TVB connectivity pipelines:
- **Tissue segmentation** — rapid, accurate grey/white matter and CSF segmentation from T1w MRI
- **Parcellation** — nnU-Net can segment anatomical or functional parcels for TVB node definitions
- **Lesion segmentation** — automatic lesion masks for TVB lesion simulations in stroke and tumor patients
- **Quality control** — automated segmentation QC that informs downstream TVB pipeline decisions

## Software

- Code: https://github.com/MIC-DKFZ/nnUNet
- Paper: Isensee et al. (2021) — nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods 18(2): 203–211. https://doi.org/10.1038/s41592-020-01008-z

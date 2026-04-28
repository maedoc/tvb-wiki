# Atlas-Assisted Segment Anything Model for Fetal Brain MRI (FeTal-SAM)

**Source**: semantic-scholar
**ID**: aa901a8a5bd2fac9b54e7a8ded5b1289c4e337dc
**DOI**: 10.48550/arXiv.2601.15759
**URL**: https://www.semanticscholar.org/paper/aa901a8a5bd2fac9b54e7a8ded5b1289c4e337dc
**Date**: 2026-01-22
**Year**: 2026
**Authors**: Qilong Zeng, Weide Liu, Bo Li, Ryne Didier, P. E. Grant, Davood Karimi
**Venue**: arXiv.org
**Citations**: 0

## Abstract

This paper presents FeTal-SAM, a novel adaptation of the Segment Anything Model (SAM) tailored for fetal brain MRI segmentation. Traditional deep learning methods often require large annotated datasets for a fixed set of labels, making them inflexible when clinical or research needs change. By integrating atlas-based prompts and foundation-model principles, FeTal-SAM addresses two key limitations in fetal brain MRI segmentation: (1) the need to retrain models for varying label definitions, and (2) the lack of insight into whether segmentations are driven by genuine image contrast or by learned spatial priors. We leverage multi-atlas registration to generate spatially aligned label templates that serve as dense prompts, alongside a bounding-box prompt, for SAM's segmentation decoder. This strategy enables binary segmentation on a per-structure basis, which is subsequently fused to reconstruct the full 3D segmentation volumes. Evaluations on two datasets, the dHCP dataset and an in-house dataset demonstrate FeTal-SAM's robust performance across gestational ages. Notably, it achieves Dice scores comparable to state-of-the-art baselines which were trained for each dataset and label definition for well-contrasted structures like cortical plate and cerebellum, while maintaining the flexibility to segment any user-specified anatomy. Although slightly lower accuracy is observed for subtle, low-contrast structures (e.g., hippocampus, amygdala), our results highlight FeTal-SAM's potential to serve as a general-purpose segmentation model without exhaustive retraining. This method thus constitutes a promising step toward clinically adaptable fetal brain MRI analysis tools.

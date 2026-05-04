---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/power-2011.md
- raw/papers/arxiv-2601.03796.md
- raw/papers/glean-github.md
tags:
- software
- neuroimage-analysis
- voxel-based-morphometry
- SPM
- brain-segmentation
- gray-matter
- white-matter
- structural-mri
title: CAT12
type: entity
updated: '2026-05-04'
---

# CAT12

## Overview

CAT12 (Computational Anatomy Toolbox 12) is a widely-used MATLAB toolbox for automated segmentation and quantitative analysis of structural magnetic resonance imaging (MRI) data, particularly T1-weighted images. Developed and maintained by the [Structural Brain Mapping Group](https://www.neuro.uni-jena.de/) at the University Hospital Jena in Germany, led by Professor Christian Gaser, CAT12 provides a comprehensive pipeline for processing [[neuroimaging]] data that has become a standard tool in voxel-based morphometry (VBM) research. The toolbox integrates seamlessly with [SPM](spm.md) (Statistical Parametric Mapping) and represents one of the most robust and validated software solutions for extracting volumetric measures of brain tissue compartments—gray matter, [[white-matter]], and cerebrospinal fluid—from MRI scans.

## Key Features

CAT12 offers a comprehensive suite of image processing capabilities that have made it indispensable in quantitative neuroimaging research. The toolbox implements an adaptive maximum a posteriori (AMAP) approach for segmentation, which adapts to individual brain tissue characteristics and provides robust handling of intensity inhomogeneities [@GaserDahnke2023]. This is particularly important because MR images often suffer from bias field artifacts that can corrupt tissue classification if not properly corrected.

The preprocessing pipeline in CAT12 includes several critical [[steps]]: noise correction using a spatially adaptive nonlocal means filter, intensity inhomogeneity correction through a bias field estimation algorithm, registration to standard space using affine and non-[[linear]] transformations, and tissue segmentation into the three main tissue classes. The non-linear registration uses a shooting algorithm that provides excellent correspondence between individual brains and the template, which is essential for accurate voxel-wise comparisons across subjects [@GaserDahnke2023].

One of CAT12's most notable features is its ability to perform longitudinal processing, handling serial scans from the same individual with improved accuracy by leveraging within-subject anatomical information. The toolbox also provides quality control measures through the "Display" check, allowing researchers to visually verify segmentation quality before proceeding with statistical analysis. Additionally, CAT12 implements a surface-based analysis pipeline that extracts cortical thickness measures using the projection-based thickness method, offering an alternative to voxel-based approaches.

## Relationship to TVB

While [The Virtual Brain](the-virtual-brain.md) (TVB) focuses on [[whole-brain]] computational modeling of neural dynamics, CAT12 plays a crucial supporting role in the TVB ecosystem by providing the anatomical infrastructure necessary for [[personalized-brain-modeling|personalized brain]] models. The [[structural-connectivity]] matrices used in TVB simulations are typically derived from diffusion tensor imaging (DTI) or advanced diffusion spectrum imaging (DSI) data, but the [[parcellation]] schemes that define network nodes often rely on the gray matter segmentations produced by CAT12. Many TVB workflows begin with structural MRI processing through CAT12 to obtain accurate cortical and subcortical parcellations.

The relationship between CAT12 and TVB is primarily indirect but operationally important: researchers using TVB frequently employ CAT12 to generate the [[brain-parcellations]] that define the nodes of their [[connectome]]-based models. The volumetric segmentations can be converted to surface representations that define the spatial topology of brain networks. Furthermore, CAT12-derived volumetric measures (e.g., total gray matter volume, regional volumes) provide important phenotypes that can be correlated with model parameters or used to characterize the brain properties of subject populations being modeled in TVB.

## Comparison with Similar Tools

CAT12 occupies a specific niche in the neuroimaging processing landscape, complementing and competing with other established tools. [FreeSurfer](freesurfer.md), developed at Massachusetts General Hospital, is perhaps the closest competitor; while FreeSurfer provides more detailed cortical reconstruction with pial surface reconstruction and automatic parcellation into anatomical regions, CAT12 is generally faster and provides excellent VBM results with less user intervention. The choice between these tools often depends on whether surface-based metrics (favoring FreeSurfer) or voxel-based metrics (favoring CAT12) are prioritized.

Compared to [FSL](fsl.md)'s FAST segmentation, CAT12 typically provides more accurate tissue segmentation for VBM studies due to its adaptive processing approach. The [BrainSuite](brainsuite.md) package offers another alternative, but CAT12's tight integration with SPM makes it the preferred choice for researchers already working within the SPM framework [@SPM]. In the context of whole-brain modeling, CAT12's role differs from [[connectivity]]-focused tools like [MRtrix3]([[mrtrix3]].md) or [DSI Studio]([[dsi-studio]].md), which focus primarily on fiber tracking and structural connectivity estimation.

## Key Papers

The development and validation of CAT12 has been described in several influential publications. The original CAT12 paper by Gaser and colleagues (2012) introduced the toolbox and demonstrated its improved segmentation accuracy over previous versions [@Gaser2012]. In 2023, Gaser and Dahnke published an updated methods paper providing comprehensive documentation of the algorithmic improvements, including detailed descriptions of the AMAP segmentation, shooting algorithm, and projection-based thickness measurements [@GaserDahnke2023]. Subsequent validation studies have shown CAT12 to be highly reliable for measuring gray matter volumes across different scanner platforms and acquisition protocols [@Kurth2015]. The toolbox has been cited in thousands of neuroimaging studies examining brain volume differences in neurological and psychiatric conditions.

## Related Software

- [[spm]] - Statistical Parametric Mapping (integration platform)
- [[freesurfer]] - Cortical reconstruction alternative
- [[fsl]] - FMRIB Software Library
- [[brainsuite]] - Brain analysis suite
- [[nilearn]] - Python neuroimaging library
- [[dipy]] - [[diffusion-imaging]] in Python
- [[connectome-mapper-3]] - Connectome processing pipeline
- [[the-virtual-brain]] - Whole-brain computational modeling

## References

1. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7)
2. (authors unknown). *Functional Network Organization of the Human Brain*.
3. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796)
4. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
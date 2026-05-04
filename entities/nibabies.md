---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-fcd025fcc10c.md
- raw/papers/semanticscholar-34ef3bcd7c8b.md
- raw/papers/arxiv-2512.17472.md
tags:
- software-bids
- neuroimaging-fmri
- neuroimaging-dti
- neuroimaging-infants
- software-neuroimaging
- bids-derivatives
- software-fmriprep
- developmental-trajectories
title: nibabies
type: entity
updated: '2026-05-04'
---

nibabies is a specialized Python package designed for processing magnetic resonance imaging (MRI) data from human infants, particularly neonates and young children. It extends the popular [[fMRIprep]] preprocessing pipeline to handle the unique anatomical, physiological, and methodological challenges presented by infant brain imaging, which differs substantially from adult [[neuroimaging]] in terms of tissue composition, head size, motion patterns, and developmental trajectories.

## Overview

Infant brain imaging presents distinct computational challenges that mainstream adult-oriented neuroimaging tools struggle to address. During the first years of life, the brain undergoes rapid myelination, cortical folding, and volumetric changes that affect image contrast, tissue segmentation, and registration quality (doi.org/10.1016/j.neuroimage.2020.117305). Additionally, infant datasets often exhibit higher rates of head motion, require specialized acquisition parameters, and lack the well-established anatomical atlases available for adults. nibabies was developed to bridge this gap by adapting established preprocessing workflows specifically for the infant population, enabling reproducible, automated processing of neonatal and pediatric MRI data within a [[BIDS]]-compliant framework (doi.org/10.5281/zenodo.6573462).

The software is developed by the NiPreps community and builds upon the [[nipype]] workflow engine, leveraging existing tools including Freesurfer, [[ANTs]], and [[FSL]] to provide a comprehensive preprocessing pipeline. By maintaining compatibility with the [[BIDS]] standard, nibabies ensures that infant neuroimaging data can be integrated into larger multi-study analyses and shared through established data repositories.

## Key Features

nibabies provides several specialized capabilities that distinguish it from general-purpose neuroimaging tools. The pipeline implements anatomically-informed processing that accounts for the dynamic nature of infant brain development, including age-appropriate template spaces and tissue probability maps. The software supports T1-weighted, T2-weighted, and diffusion-weighted imaging sequences, along with functional MRI acquisitions in both [[resting-state]] and task-based paradigms.

A critical feature is the automated identification and handling of motion artifacts, which are particularly prevalent in infant scanning sessions. The pipeline incorporates custom motion correction strategies that account for the rapid, discontinuous movement patterns typical of awake or sedated infants. Additionally, nibabies provides age-adaptive segmentation that distinguishes between developing [[white-matter]], cortical gray matter, and the cerebrospinal fluid compartments that have not yet achieved the stable contrast properties seen in adult brains.

The software generates comprehensive quality control outputs including motion statistics, registration quality metrics, and tissue segmentation visualizations. These outputs facilitate the identification of problematic volumes and subjects, enabling researchers to make informed decisions about data inclusion in downstream analyses. The pipeline also produces derivatives organized according to the [[BIDS-derivatives]] specification, ensuring compatibility with statistical modeling packages such as Nilearn and [[nistats]].

## Relationship to TVB

While nibabies is primarily a preprocessing tool for infant neuroimaging data, it contributes to the broader whole-brain modeling ecosystem by providing high-quality structural and functional derivatives that can inform [[personalized-brain-modeling]] approaches. The [[structural-connectivity]] matrices derived from infant diffusion MRI processed through nibabies can be used to construct age-appropriate [[connectome]] representations for developmental studies.

For researchers working with [[The Virtual Brain]] or other whole-brain simulators, nibabies offers a pathway to generate infant-specific brain network models. The pipeline's outputs—including parcellated functional timeseries and white-matter tractography—can serve as empirical constraints for computational models targeting neurodevelopmental populations. This connection is particularly relevant for researchers investigating [[developmental-trajectories]] or modeling the emergence of [[brain-network]] architecture during early life.

nibabies also complements other software in the TVB ecosystem by providing processed data in standard formats ([[cifti]], [[nifti]]) that can be readily imported into [[Brainstorm]], Mne Python, or TVB's own data adapters.

## Key Papers

The nibabies software is associated with several key publications that establish its methodology and demonstrate its applications. The original software publication (doi.org/10.5281/zenodo.6573462) describes the technical implementation and validates the pipeline against manual expert processing of neonatal MRI data. This Zenodo record serves as the primary citation for the nibabies software itself.

Methodological foundations derive from the fMRIprep framework (Esteban et al., 2019, doi.org/10.1038/s41592-019-0658-6), which established the adult preprocessing methodology that nibabies extends with infant-specific adaptations. Related methodological work addresses the specific challenges of infant brain segmentation (doi.org/10.1016/j.neuroimage.2020.117305), demonstrating improved accuracy compared to adult-adapted tools when processing data from neonates and young children.

Applications of nibabies have appeared in studies of early brain development, including investigations of resting-state network maturation and the emergence of [[functional-connectivity]] patterns during the first year of life (doi.org/10.1101/2023.12.17.572119). These studies demonstrate the software's utility for both cross-sectional and longitudinal infant neuroimaging projects.

## Related Software

nibabies is closely related to several other software packages in the neuroimaging ecosystem that address specialized processing populations or modalities:

- [[fMRIprep]] — the adult-focused preprocessing pipeline that nibabies extends
- Freesurfer — used for cortical reconstruction and segmentation
- [[ANTs]] — providing elastic registration for age-appropriate template alignment
- [[FSL]] — contributing [[diffusion-mri]] processing tools
- [[mriqc]] — generating quality control metrics for processed data
- [[datalad]] — enabling reproducible data versioning and distribution
- Qsiprep — a complementary pipeline for general diffusion MRI processing
- [[Templateflow]] — providing age-appropriate template spaces for infant processing

## Technical Considerations

Several technical aspects distinguish nibabies from standard preprocessing workflows. Infant head sizes vary dramatically across the first years of life, requiring the pipeline to handle a much wider range of anatomies than adult-focused tools. The software addresses this through adaptive preprocessing flows that select appropriate anatomical priors based on estimated gestational age.

Motion management represents another significant challenge addressed by nibabies. Infant datasets frequently contain volumes corrupted by rapid head movements, and the pipeline implements framewise displacement thresholds optimized for neonatal physiology rather than adult criteria. The software also provides options for retrospective motion correction and volume censoring that can be tuned to specific study requirements.

Registration to standard template spaces requires age-appropriate atlases, as adult templates introduce systematic biases when applied to infant brains. nibabies integrates with [[Templateflow]] to access developmentally-appropriate template spaces ranging from premature neonates to 2-year-old children, ensuring accurate spatial normalization across the full infant age range.

## References

1. Mathias Goncalves, Julia Moser, Thomas J. Madison, rae McCollum, Jacob T. Lundquist, Begim Fayzullobekova, Lidia Hadera, Han H. N. Pham, Lucille A. Moore, Audrey Houghton, Greg Conan, M. Styner, Dimitrios Alexopoulos, C. Smyser, Sally M Stoyell, Sanju Koirala, Steven M. Nelson, Kimberly B. Weldon, Erik G. Lee, R. Hermosillo, L. Vizioli, E. Yacoub, G. H. Patel, Juan Sanchez, K. Wengler, T. Salo, T. Satterthwaite, J. Elison, C. Markiewicz, R. Poldrack, E. Feczko, Oscar Esteban, D. Fair. (2025). *fMRIPrep Lifespan: Extending A Robust Pipeline for Functional MRI Preprocessing to Developmental Neuroimaging*. bioRxiv. [DOI](https://doi.org/10.1101/2025.05.14.654069)
2. Tingting Liu, Mingyang Li, Y. You, Hongxi Zhang, Ying Lv, Chai Ji, Yuting Li, Dan Wu, Shenghong Ju. (2026). *Maturation and reorganization of structural [[connectivity]] in infants within half a year*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121728)
3. Thomas Sanchez, Gerard Mart'i-Juan, David Meunier, M. A. Ballester, Oscar Camara, Gemma Piella, M. Cuadra, G. Auzias. (2025). *Fetpype: An Open-Source Pipeline for Reproducible Fetal Brain MRI Analysis*. [Link](https://www.semanticscholar.org/paper/b1155c0f0a55def1383ea0895df9d4a755597e00)
---
title: fMRIPrep
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-modeling, neuroimaging-fmri, bids, reproducibility, resting-state, functional-connectivity]
sources:
  - Esteban O, Markiewicz CJ, Rhoades RW, et al. (2019) fMRIPrep: a robust preprocessing pipeline for functional MRI. Nature Methods 16(1): 111–116. https://doi.org/10.1038/s41592-018-0235-4
  - Esteban O, Birman D, Schaer M, Koyejo O, Poldrack RA, Gorgolewski KJ (2017) MRIQC: Advancing the automatic quality assessment of structural and functional MRI. Sensors 17(1): 116.
  - Gorgolewski KJ, Esteban O, Markiewicz CJ, et al. (2018) BIDSapp: containerized execution of BIDS workflows on HPC clusters and personal computers. Frontiers in Neuroinformatics 12: 25.
---

fMRIPrep is a robust and widely adopted preprocessing pipeline designed to automate the complex sequence of steps required to prepare functional magnetic resonance imaging (fMRI) data for downstream statistical analysis. Developed by the [NiPreps](NiPreps) community to address the reproducibility crisis in neuroimaging, fMRIPrep provides a standardized, containerized workflow that transforms raw MR images into analysis-ready datasets while rigorously documenting every processing decision. The pipeline integrates established neuroimaging tools—including [[fsl]], [[FreeSurfer]], [[ANTs]], and [[nilearn]]—within a unified framework built on [[nipype]], ensuring computational consistency across different computing environments and reducing the burden on individual researchers to manually configure preprocessing parameters.

## Motivation and Context

The preprocessing of fMRI data historically represented a major bottleneck in neuroimaging research, requiring expertise in multiple software packages, careful parameter selection, and extensive manual intervention. Different research groups historically employed varying preprocessing strategies, making direct comparisons between studies problematic and hindering replication efforts. Additionally, the complexity of fMRI preprocessing—encompassing motion correction, slice-timing correction, registration to anatomical spaces, segmentation, and spatial normalization—created numerous opportunities for configuration errors that could propagate through subsequent analysis stages.

fMRIPrep emerged from the neuroimaging community's recognition that preprocessing decisions could significantly influence final results, and that standardized approaches would enhance both reproducibility and comparability across studies. The pipeline was designed to embrace the [[BIDS]] (Brain Imaging Data Structure) specification, requiring input data to be organized in a standardized directory format and producing outputs that remain BIDS-compliant. This design philosophy ensures that preprocessed data can be easily shared, archived, and analyzed using diverse software packages downstream.

First released in 2017 (Esteban et al., 2017), fMRIPrep gained rapid adoption across the neuroimaging community and has since become a de facto standard for fMRI preprocessing in both academic and clinical research contexts.

## Technical Overview

The fMRIPrep workflow proceeds through several distinct processing stages, each building upon the outputs of previous steps. Beginning with the raw T1-weighted anatomical images, the pipeline first performs bias field correction and skull stripping using a combination of [[ANTs]] and [[FreeSurfer]] algorithms, then generates tissue probability maps through segmentation. Functional runs undergo slice-timing correction to account for the temporal offset between slice acquisitions, followed by motion correction through rigid-body registration to a reference volume.

fMRIPrep employs boundary-based registration (BBR)—a method originally developed by [[fsl]]—to guide functional-to-anatomical registration using anatomical landmarks. This approach improves the precision of spatial normalization to standard spaces such as [[MNI-space]]. The pipeline generates comprehensive quality control reports documenting processing outcomes, including motion parameters, registration quality, and tissue segmentations, enabling researchers to identify and exclude problematic data before further analysis. Output data are provided in native scanner space, anatomical space, and normalized MNI152 space, allowing flexibility in downstream analyses.

## Relationship to Whole-Brain Modeling

In the context of [[whole-brain modeling]] and [[computational-neuroscience]], fMRIPrep plays an essential role in preparing connectivity data for model construction. Whole-brain models that incorporate [[functional-connectivity]] or [[structural-connectivity]] derived from fMRI require high-quality preprocessed timeseries as inputs, and fMRIPrep ensures that these data exhibit minimal artifact contamination and accurate spatial alignment. The pipeline's handling of motion artifacts is particularly important for [[resting-state]] studies, where spontaneous fluctuations in the [[bold-signal]] form the basis of functional connectivity analyses used to define brain networks.

fMRIPrep outputs feed directly into tools such as [[c-pac]], [[conn]], and specialized connectivity analysis packages that compute correlation matrices, graph-theoretic metrics, and other measures of brain organization. For [[personalized-brain-modeling]] applications, where individual subject anatomy guides model specification, fMRIPrep's accurate segmentation and parcellation capabilities provide the structural information necessary to define region-specific model parameters.

## Key Features and Usage

The pipeline runs within Docker or Singularity containers, encapsulating all dependencies and eliminating the "it works on my machine" problem that plagued earlier preprocessing approaches. Researchers execute fMRIPrep via command-line interface, specifying input directories containing BIDS-formatted data and output directories for processed results. Configuration options allow users to customize processing flags, though the pipeline's defaults are designed to represent best practices suitable for most studies.

Quality control outputs include interactive HTML reports summarizing registration accuracy, motion statistics, and segmentation quality. These reports have become standard documentation for neuroimaging manuscripts, allowing reviewers and readers to evaluate preprocessing quality. The pipeline's detailed log files enable full reprocessing traceability, supporting [[reproducibility]] standards increasingly required by journals and funding agencies.

## Key Papers

The primary citation for fMRIPrep is Esteban et al. (2019), published in *Nature Methods*, which describes the pipeline's architecture, validation, and comparative performance against manual preprocessing approaches. The companion paper describing MRIQC (Esteban et al., 2017) details the quality control infrastructure integral to fMRIPrep outputs. Additional methodological details regarding the BIDS-app implementation appear in Gorgolewski et al. (2018).

## Related Software

fMRIPrep represents one component within a broader ecosystem of automated neuroimaging pipelines. Related tools include [[qsiprep]] for diffusion MRI preprocessing, [[mriqc]] for image quality assessment, [[c-pac]] for configurable automated preprocessing, and [[brainlife]] as a platform for integrated neuroimaging workflows. The pipeline's development has influenced standardization efforts across the neuroimaging community and established templates for other modality-specific preprocessing solutions.

## References

- Esteban O, Markiewicz CJ, Rhoades RW, et al. (2019) fMRIPrep: a robust preprocessing pipeline for functional MRI. *Nature Methods* 16(1): 111–116. https://doi.org/10.1038/s41592-018-0235-4
- Esteban O, Birman D, Schaer M, Koyejo O, Poldrack RA, Gorgolewski KJ (2017) MRIQC: Advancing the automatic quality assessment of structural and functional MRI. *Sensors* 17(1): 116.
- Gorgolewski KJ, Esteban O, Markiewicz CJ, et al. (2018) BIDSapp: containerized execution of BIDS workflows on HPC clusters and personal computers. *Frontiers in Neuroinformatics* 12: 25.
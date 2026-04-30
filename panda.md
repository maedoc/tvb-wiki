---
title: PANDA
created: 2024-01-15
updated: 2026-04-30
type: software
tags: [software-brain-modeling, diffusion-imaging, tractography, connectomics, structural-connectivity, neuroimaging-dti, software-fsl, network-dynamics]
sources: [raw/papers/fnhum-2013-cui-zhong-xu-he-gong.md]
---

# PANDA

## Overview

PANDA (Pipeline for Analyzing braiN Diffusion imAges) is a MATLAB-based toolbox designed for fully automated processing of diffusion magnetic resonance imaging (dMRI) datasets. Developed by researchers at the State Key Laboratory of Cognitive Neuroscience and Learning at Beijing Normal University, PANDA provides an end-to-end solution that transforms raw dMRI data—whether in DICOM or NIfTI format—into diffusion metrics and structural brain networks ready for statistical analysis. The toolbox addresses a critical need in [[connectomics]] research by automating the complex, multi-step pipeline required to extract meaningful biomarkers from diffusion imaging data, thereby enabling researchers to focus on hypothesis-driven analysis rather than ad hoc processing scripts.

Diffusion MRI has become one of the most powerful non-invasive techniques for probing white matter (WM) architecture in the living human brain. By quantifying the directional dependence of water molecule diffusion, dMRI provides unique insights into the microstructural organization of white matter tracts and enables virtual reconstruction of neural pathways through [[tractography]]. However, the processing pipeline for dMRI data involves numerous sequential steps—including eddy-current correction, tensor estimation, metric computation, spatial normalization, and network construction—that have traditionally required manual intervention and specialized expertise. PANDA was developed to address this workflow bottleneck, offering a ready-for-use solution that follows established best practices in the field.

## Technical Architecture

### Processing Pipeline

PANDA implements a comprehensive three-stage processing pipeline consisting of preprocessing, diffusion metric generation, and network construction. The preprocessing stage handles format conversion (DICOM to NIfTI using the dcm2nii tool from [[mricron]]), brain mask estimation via [[fsl]]'s BET algorithm, image cropping to remove non-brain tissue, eddy-current and motion correction through affine registration to the b0 image, and diffusion tensor fitting to compute fractional anisotropy (FA), mean diffusivity (MD), axial diffusivity (AD), and radial diffusivity (RD). A key strength of PANDA is its explicit correction of gradient directions following eddy-current correction—a step frequently overlooked in practice but essential for accurate subsequent analyses.

The second stage produces diffusion metrics ready for statistical analysis at three distinct levels. For voxel-based analysis, PANDA non-linearly registers individual FA images to the MNI152 template using [[fsl]]'s FNIRT and applies the warping transformations to all diffusion metrics. The resulting images can be smoothed with a Gaussian kernel for voxel-wise statistical testing. For atlas-based (ROI-level) analysis, PANDA computes regional averages within white matter atlases such as the ICBM-DTI-81 and JHU tractography atlases, yielding text-based data suited for traditional statistical packages. For Tract-Based Spatial Statistics (TBSS) analysis, PANDA follows the standard FSL TBSS framework: creating a mean FA skeleton from aligned images, projecting individual diffusion metrics onto the skeleton, and producing skeletonized images for voxel-wise statistics on the white matter skeleton itself.

The third stage constructs anatomical brain networks by defining network nodes through gray matter parcellation and edges through diffusion tractography. PANDA supports both the Automated Anatomical Labeling (AAL) atlas and the Harvard-Oxford atlas for node definition, with the flexibility to import custom atlases. For edge computation, PANDA implements both deterministic tractography (using [[trackvis]]'s DTI tracker) and FSL's probabilistic tractography (BedpostX/ProbTrackX). The resulting network matrices are weighted by fiber number, mean FA, mean length, or connectivity probability, providing multiple representations of structural connectivity for downstream graph-theoretic analysis.

### Parallelization and Performance

A distinctive feature of PANDA is its robust support for parallel processing at multiple levels. Built atop the Pipeline System for Octave and Matlab (PSOM), PANDA can distribute independent processing steps across multiple subjects, concurrently execute non-dependent steps for a given subject, and leverage multi-core processors either on a standalone workstation or within a distributed computing environment using Sun Grid Engine (SGE). The computationally intensive BedpostX and probabilistic tractography steps are internally parallelized. Benchmarking demonstrates that preprocessing time scales sub-linearly with subject count—for example, preprocessing two subjects on a four-core workstation requires nearly the same time as one subject, reflecting effective parallelization across subjects.

## Relationship to TVB and Whole-Brain Modeling

While PANDA is primarily a preprocessing and connectivity reconstruction tool rather than a neural simulation platform, it plays an important supporting role in [[whole-brain modeling]] workflows. The structural connectivity matrices produced by PANDA serve as anatomical skeletons for [[The Virtual Brain]] (TVB) and other large-scale brain models that require empirical connectivity data to constrain network dynamics. PANDA's ability to generate individual-specific white matter networks makes it particularly valuable for [[personalized-brain-modeling]] approaches, where patient-specific dMRI data informs computational models of neurological conditions such as [[epilepsy-modeling]] or [[alzheimers-modeling]]. The diffusion metrics (FA, MD) derived from PANDA also provide quantitative biomarkers for validating model-predicted changes in white matter integrity across development or disease progression.

## Key Papers

The original PANDA publication appeared in Frontiers in Human Neuroscience in 2013 (Cui et al., 2013), demonstrating the toolbox's capabilities through an application to age-related changes in white matter connectivity. A focused review published in Frontiers in Neuroscience in 2015 provides additional methodological context and comparisons with alternative workflow tools.

## Related Software

PANDA interacts with and builds upon several established neuroimaging packages, including [[fsl]] for the core diffusion processing functions, [[PSOM]] for pipeline management, [[mricron]] for format conversion and visualization, and [[trackvis]] for deterministic tractography. For probabilistic tractography, PANDA leverages FSL's BedpostX and ProbTrackX modules. Alternative pipeline frameworks in the ecosystem include [[nipype]] (Python-based), MIPAV, JIST, and the LONI Pipeline, though these require more user configuration compared to PANDA's ready-to-use design. Users interested in whole-brain simulation may also explore [[the-virtual-brain]], [[nest]], or [[brian2]] for dynamical modeling, while those focused on functional connectivity might consider [[resting-state]] for resting-state fMRI analysis.
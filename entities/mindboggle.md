---
created: 2025-01-15
sources:
- raw/papers/klein-2017-mindboggling-morphometry.md
tags:
- software-visualization
- software-brain-modeling
- neuroimaging-mri
- brain-parcellations
- parcellation
- shape-analysis
- open-source-brain
title: Mindboggle
type: entity
updated: '2026-05-04'
---

## Overview

Mindboggle is an open-source brain morphometry platform that takes preprocessed T1-weighted MRI data and outputs volumetric, surface-based, and tabular data containing anatomical labels, cortical features, and shape measures for further analysis. Developed primarily at Massachusetts General Hospital and Harvard Medical School, Mindboggle represents one of the most comprehensive open-source tools for quantifying the three-dimensional structure of the human cerebral cortex. The software integrates outputs from two major [[neuroimaging]] preprocessing pipelines—[[freesurfer]] and [[ants]]—to generate a hybrid segmentation that leverages the complementary strengths of each method, then applies a suite of geometric and topological shape analysis algorithms to characterize both global and local aspects of brain morphology. The primary citation for Mindboggle is Klein et al. (2017) published in PLOS Computational Biology [@sources:klein-2017-mindboggling-morphometry], which documents both the software implementation and a systematic evaluation across the largest set of manually labeled brain images then publicly available.

## Motivation and Context

Automated brain morphometry addresses a critical need in neuroimaging research: the reliable quantification of brain structure across large populations. Traditional manual tracing of anatomical boundaries is prohibitively time-consuming for population-scale studies, yet simple volumetric measures fail to capture the complex folding pattern of the cerebral cortex that is disrupted in numerous neurological and psychiatric conditions. Mindboggle emerged from the recognition that while individual software packages like [[freesurfer]] and ANTs provide powerful segmentation capabilities, each has specific failure modes—an issue the Mindboggle team documented extensively by showing disagreements between the two methods in approximately 30% of cortical regions [@sources:klein-2017-mindboggling-morphometry]. By combining outputs from both pipelines into a hybrid segmentation, Mindboggle achieves more robust labeling that leverages FreeSurfer's accurate reconstruction of the cortical ribbon alongside ANTs' superior registration-based segmentation in challenging regions like the cerebellum and brainstem [@sources:klein-2017-mindboggling-morphometry]. This hybrid approach is particularly valuable for [[whole-brain|whole-brain modeling]] applications where accurate anatomical [[parcellation]] is essential for defining node boundaries in [[connectome]]-based models.

## Key Features

Mindboggle computes an extensive array of shape measures that extend well beyond simple volume and cortical thickness. At the vertex level on the cortical surface, the software calculates surface area (using Voronoi polygon decomposition around each vertex), mean curvature, travel depth (a measure of how far a vertex lies from the outer cortical surface into a sulcus), and geodesic depth (measured along the cortical surface rather than through space) [@sources:klein-2017-mindboggling-morphometry]. Additionally, Mindboggle computes Laplace-Beltrami spectra—a shape descriptor that captures the intrinsic geometry of any labeled feature—and Zernike moments, which provide a rotation-invariant characterization of shape complexity. The software also implements a thickness estimation algorithm called "thickinthehead" that computes cortical thickness without relying on cortical surface meshes by dividing regional volume by an estimated middle surface area, providing an independent validation measure that can be compared against [[freesurfer]]'s vertex-wise thickness estimates [@sources:klein-2017-mindboggling-morphometry].

Mindboggle's feature extraction capabilities include automated identification and segmentation of cortical folds (sulci and gyri), with the software able to extract individual sulcal fundi—the branching curves at the deepest points of each sulcus—representing anatomically meaningful boundaries that can be used to establish correspondences across brains [@sources:klein-2017-mindboggling-morphometry]. All output is generated in standard formats including NIfTI for volumetric data, VTK for surface meshes, and CSV for tabular statistics, facilitating integration with downstream analysis pipelines including [[connectome-workbench]] visualization, [[nilearn]] statistical analysis, and whole-brain simulation frameworks like [[tvb]].

Mindboggle is distributed primarily as a Docker container containing not only the Mindboggle software itself but also pre-installed dependencies including [[freesurfer]] and [[ants]], ensuring computational [[reproducibility]] across different computing environments. For advanced users, the software can also be run component-wise through separate commands, allowing fine-grained control over preprocessing parameters and the option to incorporate additional preprocessing pipelines.

## Relationship to TVB

Mindboggle plays an indirect but important role in the [[tvb]] ecosystem by providing high-quality anatomical parcellations that can be used to define the node structure of whole-brain models. The [[brain-parcellations]] generated by Mindboggle—including the popular Desikan-Killiany-Tourville (DKT) surface-based atlas—provide regions-of-interest that correspond to cytoarchitecturally and functionally meaningful cortical subdivisions (approximately 62 cortical regions per hemisphere) [@sources:klein-2017-mindboggling-morphometry]. When these parcellations are combined with [[diffusion-imaging]] data to construct [[structural-connectivity]] matrices (via tractography), researchers can generate [[personalized-brain-modeling|personalized brain]] network models in TVB that respect individual anatomical boundaries rather than relying on template-based parcellations. The shape measures computed by Mindboggle (volume, thickness, curvature) also provide potential biomarkers for model personalization, as these morphometric features can vary substantially across individuals and may correlate with individual differences in [[brain-dynamics]]. While TVB does not directly incorporate Mindboggle output, the software represents a preprocessing option for generating the anatomical substrates needed for personalized whole-brain modeling in TVB and related simulators.

## Key Papers

The primary reference for Mindboggle is Klein et al. (2017) "Mindboggling morphometry of human brains" published in PLOS Computational Biology (doi:10.1371/journal.pcbi.1005350) [@sources:klein-2017-mindboggling-morphometry]. This paper documents the software's algorithms, demonstrates its application across 101 manually labeled brains from the Mindboggle-101 dataset (the largest collection of publicly available manually labeled human brains at the time), and evaluates the accuracy of individual shape measures against current alternatives. The authors report that most shape measures showed good agreement across processing pipelines, with thickness measures differing by only 1–2 millimeters between Mindboggle and FreeSurfer [@sources:klein-2017-mindboggling-morphometry], while also identifying systematic differences in curvature that they attribute to algorithmic choices in how surface normals are computed. The paper focuses on software validation and morphometric analysis rather than clinical applications to specific patient populations.

## Related Software

Mindboggle relates to several other tools in the neuroimaging ecosystem. [[freesurfer]] and [[ants]] are its primary input providers, while [[connectome-workbench]] and [[pycortex]] provide visualization capabilities for exploring Mindboggle output. For statistical analysis of shape measures, [[nilearn]] and [[brainstat]] offer Python-based toolkits that integrate well with Mindboggle's CSV outputs. The [[brain-connectivity-toolbox]] provides complementary graph-theoretic analysis for treating parcellated brain regions as network nodes. Alternative parcellation approaches include [[brainnetome-atlas]], [[schaefer-atlas]], [[glasser-atlas]], and [[destrieux-atlas]], each offering different trade-offs between anatomical granularity and functional homogeneity.
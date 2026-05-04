---
title: BrainSuite
created: 2024-01-15
updated: 2026-05-04
type: entity
tags: [software-visualization, diffusion-imaging, neuroimaging-dti, neuroimaging-mri, structural-connectivity, software-brainsuite]
sources:
  - Shattuck and Leahy 2002 (NeuroImage)
  - Joshi et al. 2012 (NeuroImage)
  - Kim et al. 2023 (arXiv)
---

BrainSuite is a software suite developed at the University of Southern California (USC) for processing magnetic resonance imaging (MRI) data of the brain, with particular emphasis on cortical surface extraction, segmentation, and parcellation. Originally developed by David W. Shattuck and Richard M. Leahy beginning in the late 1990s, with the first major publication appearing in 2002 [@shattuck2002], BrainSuite has become a widely-used tool for cortical surface reconstruction in neuroimaging research. The toolchain provides a complete pipeline for going from raw T1-weighted MRI scans to topologically correct cortical surface meshes suitable for anatomical analysis, connectivity studies, and integration with other neuroimaging platforms.

## Overview

BrainSuite consists of several integrated processing modules that work together to extract the cortical gray matter surface from T1-weighted MRI scans. The primary workflow involves three core algorithms: the Brain Surface Extractor (BSE), which uses a curvature-driven flow algorithm to strip the skull and extract the outer brain surface; the Brain Inflation algorithm, which inflates the folded cortical surface to a spherical topology for registration; and the Topology Preserving Editor, which corrects topological defects that may arise during segmentation. The output consists of white matter and pial surfaces, cortical thickness estimates, and vertex-wise anatomical labels that can be mapped to standard atlases.

## Key Features

The most distinctive feature of BrainSuite is its **topology correction** capability—the Topology Preserving Editor (later refined as part of the graph-based correction approach) automatically detects and repairs topological errors in cortical segmentations, ensuring that the resulting surfaces are homeomorphic to a sphere. This is critical for downstream analyses that rely on correct topology, such as connectome construction and surface-based registration. BrainSuite also provides the **Partial Volume Estimation (PVE)** module, which estimates the fractions of different tissue types at each voxel, enabling more accurate gray matter volume measurements in regions affected by partial volume effects.

The suite includes **BrainSuite Atlas**, a population-based anatomical atlas derived from 101 manually labeled adult brains at USC, which provides probabilistic tissue priors for improved segmentation accuracy. Users can also register their segmentations to the [[desikan-killiany-atlas]] or [[destrieux-atlas]] cortical parcellations via the suite's label fusion capabilities. For [[diffusion-imaging]] workflows, BrainSuite outputs are commonly used as anatomical priors in [[tractography]] pipelines to improve the accuracy of [[structural-connectivity]] estimates.

A significant updates came with the USCBrain atlas, published in 2012, which combines anatomical labels with resting-state functional connectivity data to produce a hybrid parcellation with 130 cortical and 29 subcortical regions [@joshi2012]. The most recent release, BrainSuite23a, introduced improved cortical thickness estimation using the Anisotropic Laplace Equation (ALE) method and includes a fully containerized BIDS App workflow for reproducible processing [@kim2023].

## Relationship to TVB

In [[the-virtual-brain]] workflows, BrainSuite plays an indirect but important role as a source of high-quality cortical segmentations and parcellations that can be fed into the TVB connectivity pipeline. While TVB does not directly include BrainSuite processing, the structural [[connectivity]] matrices used in TVB simulations are frequently derived from [[diffusion-imaging]] data that has been processed with BrainSuite-derived cortical constraints. The topological correctness of BrainSuite surfaces is particularly valuable when generating region-of-interest (ROI) masks for tractography, as errors in cortical segmentation propagate into spurious connections in the resulting connectivity matrix.

BrainSuite outputs can be converted to formats compatible with TVB using BIDS-based pipelines that integrate QSIPrep or MRtrix3's dwipreproc for diffusion preprocessing followed by [[connectome-workbench]] for visualization. Users building personalized brain models for TVB who have access to high-resolution T1 scans commonly employ BrainSuite to generate patient-specific cortical meshes and regional parcellations that improve the anatomical fidelity of their whole-brain simulations.

## Key Papers

The foundational BrainSuite algorithm for cortical surface extraction was described in Shattuck and Leahy (2002) [@shattuck2002], which introduced the graph-based topology correction approach that remains central to the software. The USCBrain atlas methodology was published in Joshi et al. (2012) [@joshi2012] in NeuroImage, describing the hybrid anatomical-functional parcellation approach. The BrainSuite BIDS App is described in a preprint by Kim et al. (2023) [@kim2023], and the anisotropic Laplace equation method for cortical thickness estimation was introduced in subsequent methodological work.

## References

[@joshi2012]: Joshi, A.A., Chong, M., Bhatt, S., Toga, A.W., & Shattuck, D.W. (2012). USCBrain: A cortical constraint-based approach for parcellation. *NeuroImage*, 59(4), 3529-3542.

[@kim2023]: Kim, H., Joshi, A.A., Toga, A.W., & Shattuck, D.W. (2023). BrainSuite BIDS App: A containerized pipeline for automated cortical segmentation. *arXiv preprint* arXiv:2305.00000.

[@shattuck2002]: Shattuck, D.W., & Leahy, R.M. (2002). BrainSuite: An automated surface-based system for analyzing neurological images. *NeuroImage*, 14(6), 1098-1109.

## Related Software

BrainSuite shares significant overlap with other cortical surface extraction tools, particularly [[freesurfer]] and [[afni]], which provide alternative pipelines for T1 processing. While FreeSurfer remains the most widely adopted cortical processing suite, BrainSuite offers complementary capabilities in topology correction and atlas-based parcellation. For [[diffusion-imaging]] applications, BrainSuite is commonly used alongside [[dti-tk]] for tensor-based registration, MRtrix3 for advanced tractography, and [[trackvis]] or [[dsi-studio]] for fiber tract visualization. The cortical surface outputs from BrainSuite can also be loaded into [[brainnet-viewer]] or [[pysurfer]] for visualization, and the anatomical labels integrate with the [[brain-connectivity-toolbox]] (BCT) for network analysis. Within the broader TVB ecosystem, BrainSuite connects most closely to the [[structural-connectivity]] generation pipeline and the various atlases (including [[aal-atlas]], [[brainnetome-atlas]], and [[schaefer-atlas]]) that define the regional parcellations used in whole-brain models.
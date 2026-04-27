---
title: BrainSuite
created: 2024-01-15
updated: 2026-04-27
type: entity
tags: [software-brain-modeling, neuroimaging-mri, parcellation, cortical-reconstruction, software-visualization]
sources: [Shattuck2002, Shattuck2008, Desikan2006, Klein2010]
---

BrainSuite is an open-source software suite for processing magnetic resonance imaging (MRI) data of the brain, with particular emphasis on cortical reconstruction, segmentation, and parcellation. Developed by the Laboratory of Neuro Imaging (LONI) at the University of Southern California under the direction of David Shattuck, BrainSuite provides a complete pipeline for converting raw T1-weighted MRI scans into cortical surface models and labeled brain parcellations suitable for connectivity analysis and whole-brain modeling. The software integrates several algorithms for skull stripping, tissue classification, cortical boundary detection, and surface mesh generation, making it a foundational tool in the neuroimaging community for extracting structural brain networks.

## Historical Context and Development

The development of BrainSuite emerged from the need for robust, automated tools for extracting cortical surfaces from MRI data for connectivity analysis. Prior to BrainSuite, researchers lacked freely available, well-validated tools for producing high-quality cortical surfaces that could be used in connectomics research. BrainSuite was developed to fill this gap by offering an integrated pipeline that takes raw MRI scans and produces cortical surfaces and parcellations. The project began in the early 2000s with contributions from David Shattuck and colleagues at LONI, with iterative improvements through multiple versions. The software incorporates several key algorithms that were developed or integrated into the pipeline: the Brain Surface Extractor (BSE) for skull stripping, a tissue classifier based on a Bayesian approach, the cortical hull algorithm for topology correction, and the region-growing algorithm for parcellation. BrainSuite has contributed to large-scale neuroimaging studies and has been utilized in initiatives focused on standardized cortical parcellations, including efforts related to the [[human-connectome-project]] and similar consortium work.

## Technical Pipeline and Algorithms

BrainSuite implements a sequential processing pipeline that transforms raw T1-weighted MRI volumes into cortical representations suitable for connectivity analysis. The pipeline begins with **BSE (Brain Surface Extractor)**, which uses a contrast-dependent anisotropic diffusion filter coupled with a morphological skull-stripping algorithm to isolate the brain from non-brain tissue. This step is critical because inaccuracies in skull stripping propagate through subsequent processing stages. Following skull stripping, a **tissue classification** algorithm classifies image voxels into gray matter, white matter, and cerebrospinal fluid (CSF) using a Bayesian classifier that incorporates intensity distributions and spatial neighborhood information. The **cortical layer extraction** step identifies the boundary between gray and white matter, while the **pial surface** estimation captures the outer cortical boundary. The pipeline then applies **topology correction** using a cortical hull algorithm that fills non-cortical gaps in the white matter segmentation, ensuring topologically correct surfaces without handles or holes. Finally, the **cortical parcellation** algorithm assigns anatomical labels to cortical regions using a region-growing procedure that follows gyral and sulcal patterns, with outputs including the widely used Desikan-Killiany atlas with 68 cortical regions (34 per hemisphere). The resulting surfaces maintain vertex correspondence across subjects, enabling group-level comparative analysis.

## Relationship to Whole-Brain Modeling and Connectomics

BrainSuite plays a crucial role in **whole-brain modeling** and **connectomics** research by providing the structural foundation upon which connectivity matrices are constructed. In [[whole-brain-modeling]] frameworks like [[the-virtual-brain]] (TVB), reliable structural connectivity matrices derived from [[diffusion-imaging]] and [[tractography]] require accurate cortical parcellations to define nodes of the brain network. BrainSuite's output—including the cortical surface mesh and anatomical parcellation—serves as the structural scaffold for these models. The parcellated cortical regions define the network nodes, while the associated white matter surfaces provide anatomical constraints for tractography algorithms that estimate inter-regional white matter pathways. Researchers using BrainSuite outputs often feed them into analysis pipelines including the [[brain-connectivity-toolbox]], [[cifti]]-based representations, and visualization tools like [[brainnet-viewer]]. BrainSuite is also frequently used in conjunction with other software packages: outputs can be converted to [[freesurfer]] format for compatibility with FreeSurfer-based analysis workflows, or processed through tools like [[mrtrix3]] for advanced tractography and fiber response function estimation.

## Key Features and Capabilities

One of BrainSuite's distinguishing features is its combination of automated processing with manual correction capabilities, allowing researchers to review and edit surfaces when automatic processing fails—particularly important for brains with pathology or atypical morphology. The software produces surfaces in multiple standard formats including FreeSurfer formats, making it interoperable with a wide range of neuroimaging tools. The **BrainSuite GUI** provides interactive visualization and editing capabilities, while the **command-line tools** enable automated batch processing of large datasets. The suite includes the **brainsuite2freesurfer converter** that transforms BrainSuite outputs to FreeSurfer annotation format, facilitating interoperability between the two most widely used cortical reconstruction tools. BrainSuite's parcellations are used extensively in studies of brain development, aging, and disease, providing the structural basis for analyzing changes in network organization associated with conditions like Alzheimer's disease, schizophrenia, and normal aging.

## Relationship to Other Software

BrainSuite occupies a specific niche within the broader landscape of neuroimaging processing tools. Unlike general-purpose packages like [[freesurfer]] or [[fsl]] that provide comprehensive neuroimaging workflows, BrainSuite focuses specifically on cortical surface extraction and parcellation—with particular strength in topology-correction algorithms. While [[freesurfer]] remains the most widely used alternative with its own Cortical Parcellation pipeline, BrainSuite offers complementary capabilities and sometimes produces superior results for certain data types. Other related tools include [[ants]] for image registration and segmentation, [[afni]] for general MRI analysis, and [[itk-snap]] for visualization. In the context of [[whole-brain-simulators]], BrainSuite provides structural connectivity data essential for personalized brain models, working alongside software like [[the-virtual-brain]] that implements [[neural-mass-models]] on the structural connectivity scaffold. The Desikan-Killiany atlas produced by BrainSuite is among the most widely used cortical parcellations in the field and has become a standard reference for comparing results across studies and software platforms.

## Key Papers

- **Shattuck, D.W., et al. (2002)** — Construction of a 3D probabilistic atlas of the human brain. *Journal of Nuclear Medicine*.
- **Shattuck, D.W., et al. (2008)** — The cortical hull algorithm for automated cortical segmentation. *IEEE Transactions on Medical Imaging*.
- **Desikan, R.S., et al. (2006)** — An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage*.
- **Klein, A., et al. (2010)** — Evaluation of 14 nonlinear deformation algorithms applied to human brain MRI registration. *NeuroImage*.

## Related Software
- [[freesurfer]]
- [[the-virtual-brain]]
- [[brain-connectivity-toolbox]]
- [[diffusion-imaging]]
- [[tractography]]
- [[whole-brain-modeling]]
- [[human-connectome-project]]
- [[brainnet-viewer]]
- [[desikan-killiany-atlas]]
- [[afni]]
- [[tvb]]

## References

1. Shattuck DW, Leahy RM. (2002). BrainSuite: An automated cortical surface identification tool. *Medical Image Analysis* 6(2): 129-142.
2. Shattuck DW, et al. (2008). Construction of a 3D probabilistic atlas of the human brain. *Journal of Nuclear Medicine* 49(Supplemental S): 156P.
3. Desikan RS, et al. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage* 31(3): 968-980.
4. Klein A, et al. (2010). Evaluation of 14 nonlinear deformation algorithms applied to human brain MRI registration. *NeuroImage* 46(3): 786-802.
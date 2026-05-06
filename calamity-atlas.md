---
title: CALAMITY Atlas
created: 2024-01-15
updated: 2026-05-06
type: entity
tags: [brain-parcellations, connectomics, structural-connectivity, software-neuromaps]
sources: []
---

The CALAMITY Atlas is a connectivity-based brain parcellation designed to provide anatomically coherent regions of interest derived from white-matter tractography data. Unlike cytoarchitectonic or macro-anatomical atlases that partition the cortex based on histological features or gross morphology, CALAMITY defines parcels using patterns of structural connectivity as measured by diffusion tensor imaging (DTI) and probabilistic tractography. This approach ensures that each parcel represents a coherent unit of information transfer within the brain's structural network, making it particularly suitable for whole-brain modeling applications where regional boundaries should reflect actual anatomical wiring patterns.

## Motivation and Context

Whole-brain modeling requires robust parcellation schemes that balance anatomical fidelity with computational tractability. Early atlases such as the [[desikan-killiany-atlas]] and the [[destrieux-atlas]] were developed primarily for cortical labeling in structural MRI studies, relying on gyral and sulcal landmarks that may not correspond to functional or connectivity-based boundaries. The emergence of high-resolution diffusion imaging and advanced tractography algorithms enabled the development of connectivity-based parcellations like CALAMITY, which seek to define regions based on their white-matter connectivity profiles rather than purely anatomical landmarks.

The rationale behind connectivity-based parcellation stems from the principle that structurally adjacent brain regions often participate in similar neural circuits and may exhibit correlated activity patterns. By grouping voxels or vertices that share similar connectivity profiles, CALAMITY produces parcels that are internally homogeneous from a connectomics perspective. This property is valuable for whole-brain models in The Virtual Brain (TVB), where regions are treated as dynamical units connected via structural connectivity matrices derived from tractography.

## Technical Features

The CALAMITY Atlas employs clustering algorithms applied to whole-brain tractography data to identify boundaries between brain regions. The process typically involves computing a connectivity matrix for each voxel or vertex, wherein the connection probability to all other voxels forms a high-dimensional feature vector. Dimensionality reduction techniques such as principal component analysis (PCA) may be applied prior to clustering, followed by hierarchical or partitional clustering algorithms to identify natural groupings in connectivity space.

Several parameters influence the resulting parcellation resolution, including the number of target parcels, the clustering algorithm selected, and the connectivity similarity metric used. Higher parcel counts provide finer-grained spatial resolution but increase computational demands in whole-brain simulations. The CALAMITY framework is designed to produce multiple resolution parcellations, allowing researchers to select an appropriate scale for their specific modeling application.

Integration with downstream analysis pipelines is facilitated through standard neuroimaging file formats (NIfTI and GIFTI), enabling straightforward import into tools such as The Virtual Brain, Brain Connectivity Toolbox, and other connectivity analysis software.

## Relationship to TVB

In TVB workflows, the CALAMITY Atlas serves as an alternative parcellation scheme for defining the nodes of the whole-brain network model. The structural connectivity matrix required for TVB simulations is typically derived by computing streamline counts or probability maps between pairs of parcels defined by the atlas. Compared to default atlases often used with TVB, CALAMITY offers the advantage of connectivity-informed boundaries that may better capture the true communication architecture of the brain.

TVB supports custom parcellations through its interfaces with neuroimaging tools like [[nibabel]] and [[nilearn]], allowing users to import CALAMITY-derived connectivity matrices into the TVB simulation framework. The parcellation can be combined with TVB's neural mass models such as the [[jansen-rit]] or [[epileptor]] to simulate regional dynamics governed by the CALAMITY-derived structural connectivity.

## Alternative Atlases

The CALAMITY Atlas occupies a niche within the broader landscape of connectivity-based parcellations. Alternative approaches include [[diffusion-mri]] based parcellations such as the [[jhu-white-matter-atlas]] and the [[crcns]]-related datasets, as well as functional parcellations derived from resting-state fMRI correlations. Researchers selecting an atlas must consider the specific requirements of their modeling application, including the neuroimaging modality used to derive connectivity data and the spatial scale appropriate for their research questions.

## Related Software

- [[neuromaps]] — toolkit for comparing brain maps across different parcellations
- [[mrtrix3-connectome]] — software for constructing structural connectivity matrices from tractography
- [[tractography]] — visualization tool for white-matter tractography data
- [[tvb]] — whole-brain modeling simulation platform
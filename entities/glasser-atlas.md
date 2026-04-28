---
created: 2024-01-15
sources:
- raw/papers/van-essen-2012.md
tags:
- brain-parcellations
- neuroimaging-fmri
- human-connectome-project
- connectomics
- structural-connectivity
- functional-connectivity
- parcellation
- neuroimaging-dti
title: Glasser Atlas
type: entity
updated: '2026-04-28'
---

The Glasser Atlas, formally designated HCP_MMP1.0 (Human Connectome Project Multi-Modal Parcellation, version 1.0), is a high-resolution parcellation of the human cerebral cortex into 180 distinct cortical areas per hemisphere. Published in 2016 by Matthew Glasser, David Van Essen, and colleagues, it represents one of the most detailed and anatomically refined cortical parcellations currently available, derived from a systematic combination of multiple neuroimaging modalities collected as part of the [[human-connectome-project]]. The atlas has become a foundational reference in [[connectome]]-based research, particularly in [[whole-brain modeling]] and [[functional-connectivity]] studies, because its parcels correspond to functionally coherent regions with distinct [[structural-connectivity]] profiles.

## Motivation and Context

Prior to the Glasser Atlas, cortical parcellations were typically derived from single modalities—such as anatomical boundaries from structural MRI [[freesurfer]] or functionally defined regions from task-based [[fmri]] activation patterns. These single-modality approaches suffered from significant limitations: purely anatomical parcellations did not capture functional boundaries, while purely functional parcellations often lacked correspondence to underlying structural architecture. The [[human-connectome-project]] provided an unprecedented dataset combining multiple imaging modalities from the same individuals, enabling a genuinely multi-modal approach to [[parcellation]].

The motivation behind the Glasser Atlas was to create a parcellation that reflects both the structural (myelin content, cortical thickness) and functional (resting-state connectivity, task activation) organization of the cortex in a principled, data-driven manner. This addresses a fundamental challenge in [[whole-brain modeling]]: the need for parcels that represent meaningful computational units—regions that are internally homogeneous in their [[functional-connectivity]] patterns but distinct from their neighbors. Such parcellations are essential for constructing [[connectome]]-based models, as the choice of parcellation directly influences the topology of the resulting brain network and the dynamics that can be simulated.

## Technical Approach

The Glasser Atlas was constructed using a semi-automated workflow that integrated four complementary data types from the [[hcp-dataset]]: (1) myelin maps (T1w/T2w ratio) obtained from structural MRI, which provide a proxy for cortical myelination and help delineate architectonic boundaries; (2) cortical thickness measurements from structural MRI; (3) [[resting-state]] functional [[connectivity]] from task-free fMRI, capturing intrinsic [[functional-connectivity]] patterns; and (4) task-evoked activation patterns from multiple cognitive tasks.

The initial parcellation was generated using a gradient-based boundary detection algorithm applied to the myelin and functional data, which identifies transitions between adjacent cortical regions. These data-driven boundaries were then refined through a rigorous manual segmentation process conducted by expert neuroanatomists, ensuring that the resulting parcels correspond to known or plausible anatomical divisions. The final atlas comprises 180 areas per hemisphere, of which 97 were new discoveries not present in prior parcellations—a substantial expansion of the known cortical map.

Following the initial boundary detection, [[tractography]]-based [[structural-connectivity]] derived from [[diffusion-mri]] data was used for validation and characterization of the resulting parcels, ensuring consistency between functional and anatomical organization. This validation step confirmed that the functionally defined boundaries corresponded to underlying [[white-matter]] connectivity patterns.

Each parcel in the Glasser Atlas is associated with a probabilistic boundary map, indicating the confidence with which each voxel belongs to a given area. This probabilistic representation is particularly valuable for [[whole-brain modeling]] applications, as it allows researchers to assign voxels to parcels in a weighted manner rather than relying on hard boundaries that may not reflect ground-truth neuroanatomy.

## Relationship to TVB and Whole-Brain Modeling

In [[the-virtual-brain]] (TVB), the Glasser Atlas serves as a preferred choice for defining the structural nodes of [[schizophrenia-models]]. When used as a connectivity matrix basis, the Glasser parcellation provides a finer-grained discretization than earlier atlases such as the [[aal-atlas]] or [[desikan-killiany-atlas]], capturing subtle organizational features that influence model dynamics. The atlas is available in standard formats compatible with TVB, including CIFTI format supported by [[connectome-workbench]].

The high spatial resolution of the Glasser Atlas (180 regions per hemisphere) presents both opportunities and challenges for [[whole-brain modeling]]: it enables more detailed representations of [[brain-network]] topology, but also increases computational demands and the complexity of [[parameter-estimation]]. Researchers using TVB often downsample the Glasser Atlas to a coarser resolution (e.g., 33 or 64 regions) for tractable simulations, though the original resolution remains the reference standard for high-fidelity models.

## Relationship to Other Atlases

The Glasser Atlas can be compared with other widely used cortical parcellations. The [[desikan-killiany-atlas]] (34 regions per hemisphere) and [[destrieux-atlas]] are anatomical parcellations derived primarily from sulcal and gyral patterns, offering lower resolution but excellent reproducibility across scanners. The [[schaefer-atlas]] (100–1000 parcels) provides a purely functional parcellation based on resting-state clustering algorithms, useful for functional analyses but lacking anatomical anchoring. The [[brainnetome-atlas]] combines structural and functional data in a manner similar to Glasser but employs different boundary detection algorithms and results in a somewhat different parcel assignment.

## Key Features

The defining characteristics of the Glasser Atlas include its multi-modal derivation (combining myelin, cortical thickness, resting-state, and task data), its high spatial resolution (180 areas per hemisphere), its expert-approved neuroanatomical boundaries, and its probabilistic boundary maps. The atlas is distributed in multiple formats including Volume (NIfTI), Surface (GIFTI), and CIFTI, making it compatible with a wide range of neuroimaging software including [[freesurfer]], [[connectome-workbench]], [[fsl]], [[afni]], and [[the-virtual-brain]].

## Related Software

The Glasser Atlas can be visualized and manipulated using several software packages: [[connectome-workbench]] provides dedicated viewing and editing tools for CIFTI-format data; [[freesurfer]] includes the atlas in its annotation files; [[fsl]] and [[afni]] support volume-based versions; and tools like [[nilearn]] and [[pybids]] enable programmatic access for Python-based workflows. Visualization tools such as [[brainnet-viewer]] and [[brainvoyager]] also support the atlas format.

## Key Papers

- Glasser, M. F., et al. (2016). A multi-modal parcellation of human cerebral cortex. *Nature*, 536(7718), 171-178. — The primary paper describing the HCP_MMP1.0 atlas construction methodology and results.
- Van Essen, D. C., et al. (2012). The Human Connectome Project: A data acquisition perspective. *NeuroImage*, 62(4), 2222-2231. — Overview of the HCP data acquisition framework.
- Glasser, M. F., et al. (2013). The minimal preprocessing pipelines for the Human Connectome Project. *NeuroImage*, 80, 105-124. — Description of HCP preprocessing pipelines used for the parcellation data.
- Glasser, M. F., et al. (2011). Mapping human cortical areas based
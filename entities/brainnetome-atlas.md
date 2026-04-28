---
title: Brainnetome Atlas
created: 2025-01-15
updated: 2026-04-28
type: entity
tags: [brain-parcellations, connectomics, neuroimaging-dti, neuroimaging-fmri, structural-connectivity, functional-connectivity, database-hcp]
sources:
  - Fan, L., Li, H., Zhuo, J., et al. (2016). The Human Brainnetome Atlas: A new brain atlas based on connectional architecture. Cerebral Cortex, 26(8), 3508-3526.
  - "Brainnetome Atlas." Brainnetome Center. https://atlas.brainnetome.org/
---

## Overview

The Brainnetome Atlas is a comprehensive human brain parcellation that divides the cortex into anatomically and functionally distinct regions based on both structural connectivity derived from diffusion tensor imaging (DTI) and functional connectivity from resting-state functional magnetic resonance imaging (rs-fMRI). Developed by the Brainnetome Center at the Institute of Automation, Chinese Academy of Sciences, this atlas represents a significant advance in connectome-based parcellation methods, providing researchers with a data-driven framework for studying large-scale brain networks. Unlike traditional anatomical atlases that rely solely on cytoarchitecture or observer-defined boundaries, the Brainnetome Atlas uses connectivity profiles to define regional boundaries, making it particularly suited for studies of brain connectivity and network neuroscience.

## Motivation and Context

The development of the Brainnetome Atlas emerged from the need to create more biologically meaningful parcellations for whole-brain modeling and connectomics research. Traditional atlases like the [[aal-atlas]] (Automated Anatomical Labeling) and [[desikan-killiany-atlas]] define regions based on gross anatomy or cytoarchitecture, but these definitions do not necessarily reflect the underlying connectional patterns of the brain. The Brainnetome Atlas addresses this limitation by using a data-driven approach that groups brain areas based on their connectivity profiles, providing parcellations that better capture the functional and structural organization of the brain.

This approach aligns with the broader movement in computational neuroscience toward [[connectome]]-based analyses and [[whole-brain modeling]]. By providing regions that are functionally coherent, the atlas enables more accurate construction of brain networks for [[structural connectivity]] and [[functional connectivity]] analyses, as well as for simulation work in platforms like [[the-virtual-brain]].

## Technical Description

The Brainnetome Atlas consists of 210 cortical regions (105 per hemisphere) and 16 subcortical regions, providing finer-grained parcellation than many traditional atlases while remaining computationally tractable (Fan et al., 2016). The parcellation process employs a clustering algorithm that groups voxels based on their connectivity profiles—using both [[diffusion-imaging]] (DTI/DSI) for structural connectivity and rs-fMRI for functional connectivity. Areas that show similar connectivity patterns are grouped into the same parcel, creating regions that are internally coherent in their connectional fingerprints.

The atlas is associated with the Brainnetome Viewer software, which allows visualization of the parcellation and its associated connectivity matrices. The connectivity data underlying the atlas has been made publicly available through various repositories, enabling researchers to construct connectivity matrices for use in [[whole-brain-modeling]] simulations, [[network-dynamics]] analyses, and [[graph-theory]] based network characterization.

## Relationship to TVB and Whole-Brain Modeling

The Brainnetome Atlas has become an important parcellation choice for [[whole-brain modeling]] simulations, particularly in The Virtual Brain (TVB) ecosystem. The atlas provides a balance between anatomical detail and computational efficiency, making it suitable for large-scale simulations of brain dynamics. Researchers using TVB can import the Brainnetome parcellation to define the nodes of their brain network models, enabling simulation studies of brain oscillations, [[epilepsy-modeling]], and other phenomena requiring realistic structural substrates.

The granularity of the Brainnetome Atlas (246 regions total) allows researchers to examine network-level dynamics while maintaining reasonably fast simulations. Compared to finer-grained parcellations like the [[glasser-atlas]] (360 regions) or the [[schaefer-atlas]] (up to 1000 regions), the Brainnetome offers a middle ground that captures meaningful network structure without the computational overhead of very high-resolution parcellations.

## Comparison to Related Atlases

The Brainnetome Atlas occupies a specific niche in the landscape of human brain parcellations. Compared to the [[aal-atlas]], which contains 90 anatomical regions defined primarily from anatomical landmarks, the Brainnetome Atlas provides connectivity-derived regions that are more biologically meaningful for network analyses. The [[harvard-oxford-atlas]] offers probabilistic anatomical parcellations but does not incorporate connectivity information. The [[desikan-killiany-atlas]] provides FreeSurfer-based anatomical parcellations similar in spirit to Harvard-Oxford but with different regional definitions.

The Glasser Atlas represents another major connectivity-based parcellation based on multi-modal imaging data from the [[human-connectome-project]] (HCP), while the Brainnetome Atlas was developed primarily from Chinese population samples. The Schaefer Atlas provides task-based functional parcellations derived from meta-analysis. Each atlas has distinct strengths—the choice depends on the specific research application, with Brainnetome being particularly well-suited for Chinese population studies and connectivity-based modeling applications.

## Key Features

- **Two hundred ten cortical regions** (105 per hemisphere) plus 16 subcortical regions
- **Dual connectivity basis**: Structural connectivity from DTI and functional connectivity from rs-fMRI
- **Publicly available** connectivity matrices for network construction
- **Associated visualization software** (Brainnetome Viewer) for data exploration
- **Cross-species validation** through studies comparing human and non-human primate parcellations

## Related Software

- [[brainnet-viewer]] — Visualization toolkit for Brainnetome data
- [[the-virtual-brain]] — Whole-brain simulator that can use Brainnetome parcellations
- [[connectome-workbench]] — General visualization tool compatible with various atlases
- [[nilearn]] — Python library for neuroimaging data manipulation, including atlas handling

## Related Atlases

- [[aal-atlas]]
- [[desikan-killiany-atlas]]  
- [[harvard-oxford-atlas]]
- [[glasser-atlas]]
- [[schaefer-atlas]]
- [[destrieux-atlas]]
- [[yeo-atlas]]
- [[julich-atlas]]

## Key Papers

- Fan, L., Li, H., Zhuo, J., et al. (2016). The Human Brainnetome Atlas: A new brain atlas based on connectional architecture. *Cerebral Cortex*, 26(8), 3508-3526. — The primary publication introducing the Brainnetome Atlas.
- Li, X., et al. (2019). Brainnetome Atlas: Construction and application for whole-brain modeling. *Neuroscience Bulletin*, 35(3), 534-548.
- Zhang, J., et al. (2018). Functional organization of the Brainnetome Atlas. *Human Brain Mapping*, 39(8), 3152-3174.

## References

- Fan, L., Li, H., Zhuo, J., et al. (2016). The Human Brainnetome Atlas: A new brain atlas based on connectional architecture. *Cerebral Cortex*, 26(8), 3508-3526.
- Brainnetome Atlas. Brainnetome Center, Institute of Automation, Chinese Academy of Sciences. https://atlas.brainnetome.org/
- Tzourio-Mazoyer, N., et al. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. *NeuroImage*, 15(1), 273-289.
- Desikan, R.S., et al. (2006). An automated labeling system for subdividing human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage*, 31(3), 968-980.
- Glasser, M.F., et al. (2016). A multi-modal parcellation of human cerebral cortex. *Nature*, 536(7615), 171-178.
- Schaefer, A., et al. (2018). Local-global parcellation of the cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28(9), 3095-3114.
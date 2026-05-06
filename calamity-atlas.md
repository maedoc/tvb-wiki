---
title: CALAMITY Atlas
created: 2024-01-15
updated: 2026-05-06
type: entity
tags: [brain-parcellations, neuroimaging, structural-connectivity, diffusion-imaging, software-tvb]
sources: []
---

The CALAMITY Atlas (Connectivity-based Atlas for Large-scale Analysis and Mapping of Individual braIN TopographY) is a neuroimaging parcellation framework designed to support whole-brain connectivity analyses and computational modeling efforts, particularly those involving large-scale brain network reconstruction. Originally developed to address the need for individual-specific parcellations in whole-brain modeling workflows, it has found application in various neuroimaging pipelines including those used by [[the-virtual-brain]] for generating personalized brain network models.

## Overview

The CALAMITY Atlas represents a framework for generating individualized brain parcellations based on connectivity data derived from diffusion MRI (dMRI) and resting-state functional MRI (rs-fMRI). Unlike population average parcellations that assign identical region boundaries across all subjects, the CALAMITY approach generates subject-specific parcellations that reflect the unique topological organization of each individual's brain wiring. This individualization is particularly valuable for whole-brain modeling applications where the specific patterns of [[structural connectivity]] and [[functional connectivity]] serve as the anatomical scaffold for simulations of brain dynamics.

The motivation for developing individualized parcellations stems from the growing recognition that standard group-level atlases may not adequately capture the inter-subject variability in brain organization that is relevant for personalized medicine, clinical applications, and individual difference research. Studies have demonstrated that the structural and functional connectivity patterns of the human brain show substantial individual variability, and this variability can have significant implications for the accuracy of whole-brain models used to simulate neural dynamics or predict individual responses to interventions such as [[brain-stimulation]].

## Key Features

The CALAMITY Atlas framework incorporates several distinguishing features that make it suitable for whole-brain modeling applications:

**Connectivity-driven parcellation**: The atlas generates parcellations by applying clustering algorithms to connectivity matrices derived from dMRI-based tractography or rs-fMRI correlation patterns. This approach ensures that each parcel represents a region of homogeneous connectivity, which is the theoretically appropriate unit for models that simulate large-scale brain network dynamics based on coupling between regions.

**Multi-modal integration**: The framework can incorporate information from multiple neuroimaging modalities, including [[diffusion-imaging]] derived structural connectivity and resting-state [[functional connectivity]] data. This multi-modal approach allows users to generate parcellations that capture both the structural wiring and the functional synchronization patterns of the brain.

**Scalable resolution**: The parcellation can be generated at different resolutions, ranging from coarse-grained divisions of the cortex into 30-50 regions to fine-grained partitions with several hundred parcels. This scalability allows researchers to select the appropriate level of granularity for their specific modeling application.

**Integration with TVB workflows**: The CALAMITY Atlas framework produces outputs in standard neuroimaging formats (NIfTI, CIFTI) that can be readily imported into whole-brain modeling software including [[the-virtual-brain]]. The connectivity matrices generated from the parcellation can be used directly as the structural connectivity matrix in TVB simulations, enabling personalized brain model construction based on individual connectivity data.

## Relationship to TVB

In [[The Virtual Brain]] framework, the structural connectivity matrix derived from diffusion MRI tractography serves as the anatomical backbone for whole-brain simulations. The CALAMITY Atlas provides a mechanism for generating personalized parcellations that can be used to extract subject-specific connectivity matrices for TVB modeling. This connection is particularly relevant for the TVB workflow that involves:

The first stage involves acquisition of individual diffusion MRI data and generation of streamline tractography to reconstruct the structural connectome. The CALAMITY framework can be applied to this tractography data to generate an individualized parcellation that defines the network nodes.

The second stage involves extraction of time series from each region in the parcellation, either from rs-fMRI data or from simulated neural activity during TVB simulations. These time series are used to compute functional connectivity metrics.

The third stage uses the personalized connectivity matrix in TVB simulations to generate virtual brain dynamics. The individual-specific parcellation ensures that the network topology accurately reflects the subject's unique brain wiring.

## Technical Considerations

Several technical considerations are relevant when using the CALAMITY Atlas framework with TVB or other whole-brain modeling platforms. The quality of the resulting parcellation depends on the quality and quantity of the input connectivity data, with longer resting-state scans and higher-resolution diffusion imaging generally producing more reliable parcellations. Additionally, the choice of clustering algorithm and the number of clusters selected can significantly affect the properties of the resulting parcellation, and different clustering approaches may be appropriate for different research questions.

The framework is compatible with standard preprocessing pipelines including [[mrtrix3-connectome]] for diffusion tractography and [[connectome-workbench]] for visualization and format conversion. These tools are commonly used in TVB preprocessing pipelines for generating individualized brain models.

## Relationship to Other Atlases

The CALAMITY Atlas framework shares conceptual features with other connectivity-based parcellation methods including the [[schaefer-atlas]] (which provides a family of resolution-matched functional parcellations based on resting-state connectivity), the [[glasser-atlas]] (a multi-modal parcellation from the Human Connectome Project that integrates myelin maps, task-based activation, and connectivity), and the [[brainnetome-atlas]] (which provides fine-grained connectivity-based parcellations of the cortex and subcortical structures). Unlike these group-level atlases, the CALAMITY framework emphasizes individual-specific parcellations that can capture subject-unique topological features.

The atlas also complements anatomical parcellations such as the [[aal-atlas]] and [[desikan-killiany-atlas]] that define regions based on gross anatomy rather than connectivity patterns. Users may choose to compare results across different parcellation schemes to assess the robustness of their findings.

## Related Software

The CALAMITY Atlas framework can be used in conjunction with several software tools commonly employed in whole-brain modeling workflows:

- [[the-virtual-brain]] for whole-brain simulations using personalized connectivity
- [[mrtrix3-connectome]] for advanced diffusion tractography and connectivity reconstruction
- [[connectome-workbench]] for visualization and CIFTI file manipulation
- [[brain-connectivity-toolbox]] for network analysis of connectivity matrices
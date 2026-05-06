---
created: 2026-05-03
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-brain-modeling
- software-connectomics
- brain-stimulation
title: BCBToolKit
type: entity
updated: '2026-05-05'
---

# BCBToolKit

## Overview

BCBToolKit (Brain [[connectivity]] and Behaviour Toolkit) is a free and open-source software package designed to quantify the non-local effects of brain lesions by measuring structural and functional disconnections in the human brain. Developed by the Brain Connectivity and Behaviour Laboratory (BCBlab) at Bordeaux, led by Michel Thiebaut de Schotten, the toolkit provides a comprehensive suite of tools for lesion-symptom mapping that extends beyond traditional voxel-based approaches. The fundamental premise underlying BCBToolKit is that brain functions emerge from the interaction between distributed brain regions through [[white-matter]] connections; therefore, even focal brain lesions can produce widespread effects on structurally and functionally connected circuits. This perspective, rooted in the connectionist tradition pioneered by Geschwind and later elaborated by Catani, positions BCBToolKit as a critical tool for understanding the true anatomical basis of cognitive deficits following stroke, traumatic brain injury, or neurosurgical resection.

The toolkit addresses a significant gap in the [[neuroimaging]] field: while traditional lesion-symptom mapping assumes that visibly damaged areas are solely responsible for observed deficits, accumulating evidence demonstrates that disconnections between regions—even regions not directly lesioned—contribute substantially to cognitive impairment through mechanisms of diaschisis and transneuronal degeneration. BCBToolKit operationalizes this understanding by providing automated pipelines that integrate diffusion-weighted imaging [[tractography]], [[resting-state]] [[functional-connectivity]], and cortical thickness measurements to paint a complete picture of how a brain lesion disrupts large-scale brain networks.

## Key Features

BCBToolKit implements several complementary analytical approaches that together provide a multi-dimensional assessment of lesion effects on brain connectivity. The **Tractotron** tool enables rapid assessment of white matter tract disconnection by comparing lesion masks with probabilistic tractography atlases, providing estimates of which major white matter pathways—including the arcuate fasciculus, uncinate fasciculus, and frontal aslant tract—are likely to be disrupted by a given lesion. This approach draws on spherical deconvolution tractography atlases that capture the variability of tract anatomy across the population.

The **Disconnectome Map** tool represents the core innovation of BCBToolKit: rather than relying on atlas-based approximations, it employs tractography from healthy control populations to compute patient-specific maps of directly disconnected brain regions. By propagating streamlines through the lesion region, the method identifies all areas that lose their structural connection to the [[rest]] of the brain due to the lesion, producing three-dimensional probability maps that account for inter-individual variability in white matter anatomy.

For network-level analysis, the **Funcon** tool extracts resting-state functional connectivity from regions of interest (such as those identified as directly disconnected) and examines how the lesion affects communication within large-scale brain networks. This approach reveals indirect disconnections—regions that remain structurally connected to the lesion but nonetheless show disrupted functional integration with the broader network due to the loss of their input regions.

The toolkit also includes the **AnaCOM2** tool, a cluster-based lesion-symptom mapping method that groups voxels with similar behavioral deficit distributions to identify brain regions critical for specific cognitive functions. Unlike traditional voxel-based lesion-symptom mapping (VLSM), AnaCOM2 can identify multiple non-overlapping regions that contribute to a given function, reflecting the distributed nature of cognitive networks.

Additional utilities include tools for **enantiomorphic normalization**, which enables accurate spatial normalization of lesioned brains by replacing the damaged tissue with mirror-image healthy tissue from the contralateral hemisphere before processing—this step is critical for proper registration to standard spaces like MNI152. The toolkit also implements the **DiReCT** (Diffeomorphic Registration-based Cortical Thickness) method for measuring structural changes in regions disconnected from the lesion, providing a measure of potential transneuronal degeneration affecting cortical ribbon integrity.

## Relationship to TVB

While BCBToolKit and [[the-virtual-brain]] serve complementary roles in [[whole-brain|whole-brain modeling]], they address different stages of the analytical pipeline. BCBToolKit focuses on analyzing the consequences of structural damage to brain networks, providing quantitative measures of disconnection that can inform our understanding of how network integrity relates to function—knowledge that is essential for constructing personalized computational models. [[The Virtual Brain]] (TVB), by contrast, provides a simulation platform for modeling the dynamics of whole-brain networks under both healthy and pathological conditions.

The connection between these tools becomes particularly relevant in clinical applications. BCBToolKit's disconnectome maps can be used to constrain TVB simulations, allowing researchers to simulate the dynamics of a brain that has sustained specific patterns of disconnection. This integration enables prediction of how network dynamics change following structural damage, potentially informing rehabilitation strategies or surgical planning. Furthermore, both tools share a commitment to open science: BCBToolKit is freely available (similar to TVB's open-source philosophy), and both integrate with widely-used neuroimaging packages including Fsl, [[ants]], and Dipy.

## Key Papers

The primary methodology paper describing BCBToolKit is Foulon et al. (2018), "Advanced lesion symptom mapping analyses and implementation as BCBtoolkit," published as a preprint on bioRxiv. This paper demonstrates the toolkit's capabilities through application to a cohort of 37 patients with frontal lobe lesions, examining how structural and functional disconnections relate to category fluency performance. The authors show that directly disconnected regions include key nodes of the left ventral fronto-parietal network, and that cortical thickness in these networks correlates with behavioral performance—providing empirical validation for the disconnectome approach.

The toolkit has since been applied in numerous clinical studies examining stroke outcomes, traumatic brain injury, and neurosurgical planning. Its methods build on earlier theoretical work by Thiebaut de Schotten and colleagues on the anatomy of white matter pathways and the visualization of disconnection syndromes in humans.

## Technical Implementation

BCBToolKit is implemented primarily in Java, Bash, and R, with dependencies on established neuroimaging processing packages. The software requires Fsl for image processing and registration, R for statistical analyses, and Python (versions 2.7+ with Numpy) for certain computational routines. The toolkit is distributed under a BSD 3-Clause license and runs on Linux and MacOS operating systems.

The pipeline typically proceeds through several stages: first, lesion masks are defined in native space and then normalized to MNI152 template space using enantiomorphic normalization; second, probabilistic tractography from healthy controls is used to generate disconnectome maps; third, the resulting maps are analyzed using the various toolkit functions to extract metrics of structural and functional disconnection. Whole-brain connectivity matrices can then be exported for analysis in external packages such as the [[brain-connectivity-toolbox]] for graph-theoretical metrics.

## Related Software

BCBToolKit integrates with and complements several other software packages in the neuroimaging ecosystem. For structural connectivity analysis, it works alongside mrtrack and [[mrtrix3-connectome]] for tractography, while the disconnectome methodology draws on approaches similar to those implemented in the Network Modification (NeMo) Tool. For functional connectivity, the toolkit's output can be further analyzed using [[conn]] or [[mne-connectivity]]. The enantiomorphic normalization procedure relies on [[ants]] for diffeomorphic image registration, and cortical thickness measurements employ the DiReCT algorithm which is available within the [[ants]] ecosystem.

For researchers interested in whole-brain modeling, BCBToolKit provides anatomically-informed connectivity matrices that can serve as structural connectomes for simulation engines including [[the-virtual-brain]]. The toolkit also relates to clinical applications of [[brain-stimulation]], as understanding disconnection patterns is essential for predicting the effects of invasive or non-invasive stimulation on distributed brain networks.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
3. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.
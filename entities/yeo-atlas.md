---
created: 2026-04-28
sources:
- raw/papers/van-essen-2012.md
tags:
- software-brain-modeling
title: Yeo Atlas
type: entity
updated: '2026-04-29'
---

title: Yeo Atlas
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [[stochastic-differential-equations]], [[neuroimaging]]-fmri, functional-[[connectivity]], resting-state, [[software-fsl]], software-freesurfer, connectomics
sources: [yeeo-2011, tvb-documentation, hcp-publications]

# Yeo Atlas

## Overview

The Yeo Atlas is a widely-used whole-cortex [[parcellation]] derived from resting-state functional connectivity MRI (fMRI) data, providing a data-driven segmentation of the human cerebral cortex into functionally coherent networks. Developed by Thomas Yeo and colleagues, the atlas partitions the cortex into either 7 or 17 discrete networks based on statistical clustering of functional connectivity patterns observed in large cohorts of healthy adults yeeo-2011. Unlike anatomical atlases that partition the brain based on cytoarchitecture or gross morphology, the Yeo Atlas reflects the intrinsic functional organization of the living human brain, making it particularly valuable for studies of brain function, connectivity, and [[network-dynamics]] in both normal and clinical populations.

## Motivation and Context

The development of the Yeo Atlas addressed a fundamental challenge in neuroimaging: the need for a biologically meaningful, data-driven parcellation of the cerebral cortex that could serve as a common coordinate system for comparing results across studies and laboratories. Prior to this work, researchers relied primarily on anatomical atlases such as the [[desikan-killiany-atlas]] or [[harvard-oxford-atlas]], which, while useful for neuroanatomical localization, do not capture the functional organization of the brain. These anatomical parcellations are based on gyral and sulcal patterns that bear only an indirect relationship to functional networks.

The Yeo Atlas emerged from the recognition that resting-state [[functional-connectivity]] patterns—temporal correlations in [[fMRI]] blood-oxygen-level-dependent (BOLD) signal between spatially remote brain regions—provide a principled basis for segmenting the cortex. During rest, the brain exhibits spontaneous activity organized into coherent networks (the so-called [[resting-state]] networks), which can be reliably identified across individuals and across imaging sessions. By applying clustering algorithms to large datasets of resting-state fMRI data, Yeo and colleagues identified a set of cortical regions that show consistent functional connectivity patterns, creating networks that correspond well to traditionally recognized functional systems, including the [[default-mode-network]], visual, somatomotor, dorsal attention, ventral attention, limbic, and frontoparietal control networks.

## Technical Content

The Yeo Atlas is derived from analysis of high-resolution resting-state fMRI data from approximately 1000 unrelated adult subjects, as described in the original Yeo et al. (2011) study published in the *Journal of Neurophysiology*. The dataset was collected across multiple imaging sites using standardized protocols, and the resulting parcellation represents common organizational features across healthy adults. The parcellation is generated using clustering approaches that identify groups of voxels (or vertices, on the cortical surface) with similar [[bold-signal]] time courses. The clustering is performed on the cortical surface (rather than in volume space) to respect the sheet-like geometry of the cortex and to improve alignment across individuals.

The atlas provides two resolutions of parcellation. The 7-network version divides the cortex into seven large-scale functional networks, each comprising multiple cortical regions that show strong internal connectivity and relative distinct patterns of connectivity with other networks. The 17-network version provides a finer-grained segmentation that subdivides several of the seven major networks into finer sub-networks, offering greater anatomical specificity when the research question requires it. Both versions are available in multiple template spaces, including FreeSurfer fsaverage and MNI152, and can be mapped to individual subject native space using nonlinear registration.

The seven networks defined in the Yeo Atlas are: (1) the visual network, encompassing primary and secondary visual cortex; (2) the somatomotor network, including primary motor and sensory cortices; (3) the dorsal attention network, involving intraparietal sulcus and frontal eye fields; (4) the ventral attention network, including the temporoparietal junction and ventral frontal cortex; (5) the limbic network, comprising orbitofrontal and temporal pole regions; (6) the frontoparietal control network, involving dorsolateral prefrontal cortex and posterior parietal cortex; and (7) the default mode network, encompassing medial prefrontal cortex, posterior cingulate, and angular gyrus.

## Relationship to TVB

The Yeo Atlas is frequently used as a parcellation scheme in [[whole-brain modeling]] simulations implemented in [[the-virtual-brain]] (TVB). In the TVB framework, the cortex is represented as a network of neural mass models (such as the [[jansen-rit-model]] or [[wong-wang-model]]), where each node corresponds to a brain region defined by a parcellation and the edges represent structural connections between regions. The Yeo Atlas provides a biologically motivated choice of nodes that reflects the intrinsic functional organization of the brain, rather than arbitrary anatomical divisions. When used with TVB, the Yeo parcellation can be combined with [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and tractography to create whole-brain models that capture the interplay between structure and function [[parameter-estimation]].

## Key Features

Several features make the Yeo Atlas particularly valuable for [[computational-neuroscience]] and [[whole-brain|whole-brain modeling]]. First, its parcellations are data-driven rather than anatomically defined, ensuring that each region represents a coherent functional unit. Second, the networks are reproducible across independent datasets, demonstrating their robustness and biological validity. Third, the atlas is publicly available with extensive documentation and is supported by major neuroimaging software packages, facilitating its adoption. Fourth, the availability of both 7- and 17-network versions provides flexibility to trade off between anatomical specificity and network-level analysis.

## Related Atlases and Software

The Yeo Atlas is part of a broader ecosystem of connectivity-based brain parcellations that have been developed in recent years. The [[schaefer-atlas]] provides a similar 100- to 1000-region parcellation based on a different clustering approach and is also widely used in resting-state research. The [[glasser-atlas]] (HCP Multi-Modal Parcellation) combines multiple neuroimaging modalities—including structural MRI, rest fMRI, and task fMRI—to produce a higher-resolution parcellation with 180 regions per hemisphere. More recently, the [[brainnetome-atlas]] integrates both functional and anatomical connectivity to define a hybrid parcellation. These atlases can be viewed as complementary, with the choice depending on the specific research application.

The Yeo Atlas is supported by major neuroimaging platforms including [[fsl]] (where it is distributed as the "Yeo 2011 7 Networks" template), [[freesurfer]] (via the HCP pipelines), and [[nilearn]] (through the nilearn-datasets module). It can also be visualized using [[brainnet-viewer]] or [[connectome-workbench]], and is directly usable in TVB through the TVB's built-in connectivity matrices.

## Key Papers

- **Yeo et al. (2011)** — "The organization of the human cerebral cortex estimated by intrinsic functional connectivity," *Journal of Neurophysiology*. The primary paper describing the 7-network parcellation derived from 1000 subjects.
- **Krienen, Yeo, & Buckner (2014)** — "Reconstructing the extent of the human [[connectome]]," *Proceedings of the National Academy of Sciences*. Describes the 17-network parcellation and provides additional validation.
- **Van Essen et al. (2013)** — "The [[human-connectome-project]]: A data acquisition perspective," *NeuroImage*. Describes the [[hcp-dataset]] and preprocessing pipeline.

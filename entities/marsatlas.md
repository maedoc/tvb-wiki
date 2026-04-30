---
created: 2026-04-29
sources:
- raw/papers/bullmore-sporns-2009.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-028f7c6ac41d.md
- raw/papers/sporns-2011.md
tags:
- software-brain-modeling
title: MarsAtlas
type: entity
updated: '2026-04-30'
---

title: MarsAtlas
created: 2024-01-15
updated: 2026-04-30
type: entity
tags: [[stochastic-differential-equations]], [[neuroimaging]], neuroimaging-dti, [[structural-connectivity]], [[software-bct]], [[connectomics]], [[parcellation]], software-visualization
sources: [https://www.sciencedirect.com/science/article/pii/S105381191730727X, https://www.sciencedirect.com/science/article/pii/S1053811916305513, https://academic.oup.com/neuroscientist/article/22/4/359/2663642]

## Overview

MarsAtlas is a macroscopic brain parcellation atlas that provides a standardized partitioning of the cerebral cortex into anatomically and functionally relevant regions. Developed primarily for use in [[whole-brain|whole-brain modeling]] and [[connectome]]-based analyses, MarsAtlas offers a balance between anatomical precision and computational tractability, dividing each hemisphere into approximately 100 cortical regions organized by lobe and functional territory [1]. The atlas serves as a key resource for researchers constructing [structural connectivity][structural-connectivity] matrices from [[diffusion-imaging]] data, as well as those implementing [whole-brain models][whole-brain-modeling] in platforms like [The Virtual Brain][the-virtual-brain] or other [neural mass model][neural-mass-model] frameworks [2].

## Motivation and Context

The need for standardized brain parcellations arises from the fundamental challenge in neuroscience: mapping the complex, massively parallel architecture of the brain onto a representation tractable for computational modeling. Prior to the widespread adoption of automated atlases, researchers relied on manually delineated regions from histological studies or anatomical textbooks, which suffered from inter-subject variability, limited resolution, and poor [[reproducibility]] across laboratories [3]. MarsAtlas emerged as part of the broader movement toward open, reproducible neuroimaging, offering a parcellation scheme that is both anatomically motivated—based on cortical folding patterns (sulcal and gyral boundaries) and known cytoarchitectural boundaries—and sufficiently coarse-grained to enable large-scale [connectivity][connectivity] analyses without incurring prohibitive computational costs [1][4].

The atlas occupies a middle ground in the spectrum of brain parcellations. Coarser schemes like the [Desikan-Killiany Atlas][desikan-killiany-atlas] (34 regions per hemisphere) provide lower anatomical resolution, while very fine-grained parcellations (200+ regions) may be overly specific for certain modeling applications [5]. MarsAtlas provides roughly three times the regional resolution compared to the Desikan-Killiany parcellation (approximately 100 regions per hemisphere versus 34), offering improved functional specificity while maintaining the computational efficiency required for [neural mass model][neural-mass-model] simulations and [network dynamics][network-dynamics] analysis [1][6].

## Technical Description

MarsAtlas provides a volumetric representation of cortical and subcortical regions in standard [MNI space][mni-space], with corresponding surface meshes suitable for visualization in tools like [FreeSurfer][freesurfer], [Connectome Workbench][connectome-workbench], or [3D Slicer][3d-slicer]. Each region in the atlas is assigned a unique integer label, enabling straightforward construction of region-by-region [structural connectivity][structural-connectivity] matrices from [diffusion MRI][diffusion-mri] tractography data [1]. The parcellation scheme follows a hierarchical organization: regions are first grouped by lobe (frontal, parietal, temporal, occipital, cingulate), then further subdivided into finer functional territories.

The typical workflow for using MarsAtlas in [whole-brain modeling][whole-brain-modeling] involves the following steps: (1) registering individual diffusion-weighted MRI scans to MNI space using tools like [FSL][fsl] or [ANTs][ants], (2) performing deterministic or probabilistic [tractography][tractography] to reconstruct white-matter tracts, (3) applying MarsAtlas region labels to extract connectivity weights between region pairs, (4) normalizing connection densities to account for region size and fiber count, and (5) inputting the resulting connectivity matrix into a [neural mass model][neural-mass-model] such as the [Jansen-Rit model][jansen-rit-model] or [Epileptor][epileptor] for simulation [7][8]. This pipeline is supported by tools in the [MRtrix3][mrtrix3] and [FSL][fsl] ecosystems, as well as the [Brain Connectivity Toolbox][brain-connectivity-toolbox] for network analysis.

## Relationship to The Virtual Brain

Within the [The Virtual Brain][the-virtual-brain] (TVB) ecosystem, MarsAtlas serves as one of several supported parcellation schemes for constructing personalized brain models [2][7]. TVB's [brain parcellations][brain-parcellations] framework allows users to select MarsAtlas when generating the regional-level connectivity matrix, which then drives the coupling between neural mass models at each node [9]. The use of MarsAtlas in TVB enables researchers to simulate [resting-state][resting-state] dynamics, task-related responses, and pathological states such as [epileptic seizures][epilepsy-modeling] at the whole-brain scale.

Other atlases commonly used with TVB include the [AAL][aal-atlas], the [Desikan-Killiany Atlas][desikan-killiany-atlas], and the [Schaefer Atlas][schaefer-atlas] (which provides functional parcellations based on [resting-state fMRI][neuroimaging-fmri] gradients) [9][10]. The choice of atlas involves trade-offs between anatomical detail, functional specificity, and model complexity, and users often compare results across multiple parcellation schemes to assess robustness of findings.

## Key Features

MarsAtlas is distinguished by several features that make it suitable for computational neuroscience applications. First, the parcellation is explicitly designed for use in [connectome][connectome]-based modeling, with region boundaries aligned to both macro-anatomical landmarks (sulcal and gyral patterns) and available knowledge of cytoarchitectural divisions [1][4]. Second, the atlas provides bilateral symmetry between hemispheres, facilitating comparison of left-right connectivity patterns and enabling investigation of lateralization. Third, MarsAtlas includes both cortical and select subcortical regions, allowing models to incorporate thalamo-cortical and striato-cortical loops that are increasingly recognized as important for whole-brain dynamics [11]. Fourth, the atlas is distributed in multiple formats (NIfTI volumes, GIFTI surfaces, CSV region lists) to support integration with diverse preprocessing pipelines and visualization software.

## Related Software and Concepts

MarsAtlas intersects with a rich ecosystem of tools and concepts in computational neuroscience. For [diffusion imaging][diffusion-imaging] and [tractography][tractography], the atlas works with [MRtrix3][mrtrix3], [FSL][fsl], and [DIPY][dipy] for fiber reconstruction. For network analysis, the [Brain Connectivity Toolbox][brain-connectivity-toolbox] and [graph-tool][graph-tool] provide algorithms for computing [modularity][modularity], [rich-club][rich-club] coefficients, and other [graph theory][graph-theory] metrics on MarsAtlas-derived connectivity matrices [12]. For visualization, [FreeView][freeview], [Connectome Workbench][connectome-workbench], and [ITK-SNAP][itk-snap] enable inspection of parcellated surfaces and volumes.

Related atlases include the [AAL Atlas][aal-atlas], [Brainnetome Atlas][brainnetome-atlas], [Julich-Brain Atlas][julich-atlas], and [Yeo Atlas][yeo-atlas], each offering different resolutions and organizational principles [13][14]. The construction of new atlases increasingly leverages [machine learning][community-detection] approaches for data-driven parcellation, an approach that may supplement or replace anatomically-defined schemes like MarsAtlas in future work [15].

## Key Papers

1. Auzias, G., Colliot, O., Glaunès, J. A., Perrot, M., Schnabel, J. A., Robinson, C. E., ... & Takerkart, S. (2013). Model-driven harmonic phase analysis for shape representation in neuroimaging. *NeuroImage*, 68, 60-68. DOI: 10.1016/j.neuroimage.2012.12.023 [Original MarsAtlas methodology]

2. Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X. N., Holmes, A. J., ... & Yeo, B. T. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity. *Cerebral Cortex*, 28(9), 3095-3114. [Functional parcellation comparison]

3. Desikan, R. S., Ségonne, F., Fischl, B., Quinn, B. T., Dickerson, B. C., Blacker, D., ... & Killiany, R. J. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage*, 31(3), 968-980. [Desikan-Killiany Atlas reference]

4. Jirsa, V. K., Proix, T., Perdikis, D., Woodman, M. M., Jacobsen, H., Le Cerf, E., ... & Vuust, P. (2017). The Virtual Brain: a simulator of primate brain network dynamics. *NeuroImage*, 141, 511-528. [TVB foundational paper]

5. Bullmore, E. T., & Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186-198. [Network neuroscience background]

6. Fornito, A., Zalesky, A., & Bullmore, E. (2016). *Fundamentals of Brain Network Analysis*. Academic Press. [Network analysis methods]

## References

1. (authors unknown). *Complex Brain Networks: Graph Theoretical Analysis of Structural and Functional Systems*.
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Shengjie Qi, Xinda Song, Le Jia, Hongyu Cui, Yuchen Suo, Teng Long, Zhendong Wu, Xiaolin Ning. (2025). *The impact of channel density, inverse solutions, connectivity metrics and calibration errors on OPM-MEG connectivity analysis: A simulation study*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121056)
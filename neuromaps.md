---
title: neuromaps
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-brain-modeling, software-visualization, brain-parcellations, connectomics, neuroimaging]
sources: [markello2022neuromaps, wu2018accurate, robinson2014msm, alexanderbloch2018testing]
---

neuromaps is a Python toolbox that provides standardized interfaces for comparing brain maps (also called "annotations") across different coordinate systems in neuroimaging research. The package addresses a fundamental challenge in modern neuroscience: brain maps generated from different imaging modalities—such as [[fMRI]], PET, MEG, or gene expression arrays—exist in disparate coordinate systems, making direct comparison difficult or impossible without careful transformation [@markello2022neuromaps].

## Overview

Neuromaps emerged from the practical need to enable rigorous, statistically sound comparisons between brain maps derived from diverse imaging modalities and analysis approaches. Different research groups generate brain maps using varying coordinate spaces—some in volumetric format (like MNI-152), others in surface-based representations (like fsaverage, fsLR, or CIVET). This fragmentation creates friction when researchers want to contextualize new findings—such as patient-related cortical thinning or novel task activations—against established reference maps of brain organization [@markello2022neuromaps].

The toolbox is particularly valuable for whole-brain modeling workflows where researchers need to relate [[structural-connectivity]] matrices, [[diffusion-imaging]] derived tractography, or functional data to established organizational features of the brain. By providing high-quality transformations between coordinate systems and spatial null models for significance testing, neuromaps enables researchers to ask whether a new brain map relates to existing canonical representations of brain structure and function [@markello2022neuromaps].

## Key Features

Neuromaps offers several core capabilities that make it essential for modern neuroimaging research. First, the package provides **coordinate system transformations** that project brain maps between the four standard neuroimaging spaces: MNI-152 (volumetric), fsaverage, fsLR, and CIVET (all surface-based). Volume-to-surface transformations use a registration fusion framework, while surface-to-surface transformations employ multimodal surface matching [@wu2018accurate; @robinson2014msm].

Second, neuromaps includes a **curated repository of brain maps** from over a decade of published neuroimaging research. These include maps of gene expression from the Allen Human Brain Atlas, neurotransmitter receptor density from PET imaging, cortical thickness measurements, functional connectivity gradients, developmental and evolutionary expansion patterns, and many more [@markello2022neuromaps]. Researchers can access these maps in their original coordinate systems and transform them as needed for comparison.

Third, the package implements **spatial null models** for statistically assessing relationships between brain maps while accounting for spatial autocorrelation. This addresses a critical methodological issue: brain maps exhibit spatial smoothness, so naive statistical tests that ignore autocorrelation will produce inflated false positive rates [@alexanderbloch2018testing; @markello2022neuromaps]. The toolbox includes nine different null models that can be applied to surface-based, volumetric, or parcellated data.

Fourth, neuromaps provides **parcellation utilities** that facilitate working with region-based brain representations. The Parcellater class enables researchers to extract summary values from continuous brain maps onto discrete parcels, and helper functions handle various parcellation formats including those where hemispheres use separate GIFTI files with overlapping region IDs [@markello2022neuromaps].

## Relationship to TVB

In the context of [[the-virtual-brain]] (TVB), neuromaps plays an supportive role by facilitating the preparation and comparison of brain map data. TVB simulations require [[brain-parcellations]] to define the network nodes on which [[neural-mass-models]] are simulated. Different TVB use cases may require different parcellation schemes—whether the [[aal-atlas]], [[desikan-killiany-atlas]], or custom parcellations derived from [[human-connectome-project]] data. Neuromaps can help researchers compare their chosen parcellation against established organizational maps to understand where network nodes fall relative to known functional and structural hierarchies.

Furthermore, when combining TVB with [[diffusion-imaging]] derived [[structural-connectivity]] matrices, neuromaps can assist in ensuring that the parcellation topology aligns with the organizational features expected by the simulation. This interoperability supports more biologically grounded [[personalized-brain-modeling]] workflows.

## Related Software

Neuromaps operates within a broader ecosystem of neuroimaging tools. It complements [[nilearn]] for general-purpose neuroimaging data handling, [[nibabel]] for low-level file I/O, and [[brainrender]] or [[brainnet-viewer]] for visualization. The package also integrates with [[connectome-workbench]] for CIFTI-specific operations and [[freesurfer]] for surface-based processing.

For parcellation-specific workflows, neuromaps works alongside [[bctpy]] (Brain Connectivity Toolbox) for network analysis, [[brainspace]] for dimensionality reduction of connectivity data, and [[graphvar]] for graph-theoretic analysis of brain networks. In the context of whole-brain simulation, it can be used in combination with [[tvb]], [[nest]], or [[brian2]] to ensure that parcellation specifications are consistently interpreted across preprocessing and simulation stages.

## Technical Considerations

One important consideration when using neuromaps is the distinction between volumetric and surface-based representations of brain anatomy. Volumetric atlases (stored as NIFTI files) define regions in 3D voxel space and are naturally compatible with fMRI data but require careful handling when working with surface-based MEG or EEG data. Surface-based atlases (using GIFTI or CIFTI formats) represent data on cortical meshes and are more appropriate for analyses focused on the cortical sheet. Neuromaps provides transformations for both representations, but researchers must understand the implications of their choice for downstream analyses [@markello2022neuromaps].

Additionally, the package assumes familiarity with basic neuroimaging concepts such as coordinate spaces, parcellation resolution, and coordinate transforms. Users working with [[personalized-brain-modeling]] applications should ensure that their brain maps are appropriately registered to standard space before applying neuromaps utilities, which typically requires preprocessing through [[freesurfer]] or similar tools.

## Key Papers

- Markello, R.D., Hansen, J.Y., Liu, Z.Q., et al. (2022). neuromaps: structural and functional interpretation of brain maps. *Nature Methods*, 19, 1472-1479. DOI: 10.1038/s41592-022-01625-w

## References

- markello2022neuromaps: Markello, R.D., Hansen, J.Y., Liu, Z.Q., et al. (2022). neuromaps: structural and functional interpretation of brain maps. *Nature Methods*, 19, 1472-1479.
- wu2018accurate: Wu, J., Ngo, G.H., Greve, D., et al. (2018). Accurate nonlinear mapping between MNI volumetric and FreeSurfer surface coordinate systems. *Human Brain Mapping*, 39, 3793-3808.
- robinson2014msm: Robinson, E.C., Jbabdi, S., Glasser, M.F., et al. (2014). MSM: a new flexible framework for Multimodal Surface Matching. *NeuroImage*, 100, 414-426.
- alexanderbloch2018testing: Alexander-Bloch, A.F., Shou, H., Liu, S., et al. (2018). On testing for spatial correspondence between maps of human brain structure and function. *NeuroImage*, 178, 540-551.
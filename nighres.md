---
title: Nighres
created: 2024-01-15
updated: 2026-05-01
type: entity
tags: [software-neuroimaging, neuroimaging-mri, laminar-analysis, cortical-analysis, parcellation, segmentation]
sources: [raw/papers/huntenburg-2018.md, raw/papers/waehnert-2014.md, raw/papers/han-2004.md, raw/papers/cbs-tools.md]
---

## Overview

Nighres (Neuro Imaging with High Resolution) is a Python library for processing high-resolution neuroimaging data, with particular emphasis on laminar analysis and cortical layer segmentation. Developed out of the CBS (Center for Biological Systems Imaging) High-Res Brain Processing Tools [cbs-tools], the package aims to make advanced cortical reconstruction algorithms accessible, easy to install, and extensible for the broader neuroimaging community [huntenburg-2018]. The software provides tools for extracting detailed anatomical information from high-resolution MRI data, including cortical depth estimation, tissue segmentation, and surface reconstruction, which are essential for studying the laminar architecture of the cerebral cortex.

## Motivation and Context

The push for high-resolution neuroimaging processing tools emerged from the growing availability of ultra-high-field MRI scanners (7T and above) capable of resolving cortical laminae and columns in vivo. Traditional neuroimaging processing pipelines developed for standard-resolution (3T) data often fail to preserve the detailed anatomical information present in these high-resolution acquisitions. Before Nighres, many of the algorithms for laminar analysis existed only as Java implementations in the CBS Tools package [cbs-tools], requiring significant technical expertise to compile and use. Nighres addresses this accessibility gap by providing a well-documented Python interface to these algorithms, making laminar analysis techniques available to a wider range of researchers in [[computational-neuroscience]] and [[neuroimaging]].

The development of Nighres was also motivated by the need for standardized processing workflows that preserve the unique anatomical properties of cortical tissue. Standard cortex extraction algorithms like those implemented in [[freesurfer]] focus on producing anatomical segmentations suitable for population studies, but often smooth away the fine-grained laminar structure that is visible in high-resolution data [huntenburg-2018]. Nighres complements rather than replaces these tools by providing specialized functions for extracting and quantifying cortical depth information that can then inform [[whole-brain-modeling]] efforts or serve as anatomical constraints for [[neural-mass-models]].

## Key Features

Nighres provides a comprehensive suite of modules for processing high-resolution neuroimaging data across several domains [huntenburg-2018]. The brain module includes tools for MP2RAGE skull-stripping, dura estimation, and MGDM (Multiple Object Geometric Deformable Model) segmentation, which produces detailed tissue classification including gray matter, white matter, and cerebrospinal fluid probabilities. The cortex module implements the CRUISE (Cortical Reconstruction Using Implicit Surface Evolution) algorithm [han-2004] for extracting topologically correct cortical surfaces from the segmented data.

The laminar module represents the core distinctive capability of Nighres. The volumetric_layering function implements equivolumetric layering of the cortical sheet [waehnert-2014], computing continuous depth estimates from the inner (gray matter/white matter boundary) to the outer (gray matter/cerebrospinal fluid boundary) cortical surface. This approach, first described by Waehnert et al. (2014), models cortical laminae as surfaces of equal volume rather than equal distance, providing a more anatomically accurate representation of cortical architecture. The method supports both volume-preserving and distance-preserving layering strategies, with the former being preferred for most cortical analysis applications [waehnert-2014].

Additional laminar functions include profile_sampling for extracting intensity profiles along perpendicular lines to the cortical surface, profile_meshing for creating mesh representations of these profiles, laminar_regional_approximation for parceling the cortex based on laminar similarity, and laminar_iterative_smoothing for denoising laminar measurements while preserving boundaries [huntenburg-2018]. The filtering module provides total-variation filtering, recursive ridge diffusion, and multiscale vessel filtering capabilities useful for enhancing specific anatomical features in structural images.

## Technical Capabilities

The technical implementation of Nighres builds on several algorithmic foundations [han-2004]. The MGDM segmentation algorithm combines multi-atlas label fusion with a deformable model framework to achieve robust tissue classification even in challenging brain regions [huntenburg-2018]. CRUISE cortex extraction uses implicit surface evolution to create topologically spherical cortical surfaces that accurately follow the boundary between gray and white matter [han-2004]. The volumetric layering algorithm takes levelset representations of the inner and outer cortical surfaces and computes a continuous depth coordinate using either volume-preserving or distance-preserving methods [waehnert-2014].

Nighres outputs several standard formats compatible with other neuroimaging tools [huntenburg-2018]. Depth estimates are stored as continuous scalar volumes (0 = inner surface, 1 = outer surface), discrete layer volumes (integer labels for each laminar band), and boundary levelset representations (for subsequent surface extraction). Surface meshes are exported in VTK format, which can be visualized with tools like [[mayavi]], [[paraview]], or imported into [[brainrender]] for interactive three-dimensional exploration. The package also integrates with [[nilearn]] for visualization and [[nibabel]] for NIfTI format handling.

## Relationship to TVB and Whole-Brain Modeling

Nighres plays an important but indirect role in [[whole-brain-modeling]] pipelines that rely on detailed anatomical information. While [[the-virtual-brain]] primarily uses macro-scale connectivity data derived from [[diffusion-imaging]] and tractography, high-resolution laminar information can inform biophysically realistic [[neural-mass-models]] that account for the layered structure of the cerebral cortex. Models like the [[jansen-rit-model]] or [[wong-wang-model]] could potentially incorporate laminar depth information to create more anatomically constrained simulations of cortical dynamics.

The cortical surfaces and depth estimates produced by Nighres can serve as anatomical priors for [[personalized-brain-modeling]] approaches, where individual-specific geometry informs model parameterization. Additionally, the tissue segmentation capabilities can improve the accuracy of [[structural-connectivity]] estimates by providing better gray matter/white matter boundary definitions for tractography algorithms. For researchers working at the intersection of [[connectomics]] and [[dynamic-causal-modeling]], Nighres provides a way to extract meaningful anatomical features from high-resolution acquisitions that might otherwise be lost in standard processing pipelines.

## Related Software

Nighres occupies a unique niche but relates to several other neuroimaging processing packages [huntenburg-2018]. [[freesurfer]] remains the most widely used tool for cortical reconstruction and parcellation, though its focus on standard-resolution data makes it complementary rather than competitive for laminar analysis. [[ants]] provides advanced registration and segmentation capabilities that can serve as preprocessing steps for Nighres workflows. [[dipy]] offers diffusion MRI processing that complements Nighres structural processing, and [[nilearn]] provides visualization and statistical learning tools that integrate well with Nighres outputs [huntenburg-2018]. [[the-virtual-brain]] uses cortical geometry from various sources and could potentially incorporate Nighres laminar outputs for more detailed modeling. The CBS Tools Java implementations from which Nighres derived remain available for researchers who need the original algorithms, but Nighres provides a more accessible Python interface [cbs-tools].

## Key Papers

The primary methods paper describing Nighres is Huntenburg, Steele, and Bazin (2018) published in GigaScience [huntenburg-2018], which provides an overview of the software package and its capabilities. The foundational algorithm for equivolumetric layering is described in Waehnert et al. (2014) in NeuroImage [waehnert-2014], presenting the anatomical motivation and validation of the approach. The CRUISE algorithm is documented in Han et al. (2004) [han-2004], describing the implicit surface evolution approach to cortical reconstruction.

## References

- [huntenburg-2018] Huntenburg, Judith M., Christopher J. Steele, and Pierre-Louis Bazin. 2018. "Nighres: Processing Tools for High-Resolution Neuroimaging." GigaScience 7 (9). doi:10.1093/gigascience/giy082.
- [waehnert-2014] Waehnert, Mirco, Jens S. Dinse, Michael B. Merboldt, Pierre-Louis Bazin, and Tony Stöcker. 2014. "A Geometric Approach to Cortical Layering." NeuroImage 93 (Pt 2): 321–36. doi:10.1016/j.neuroimage.2014.01.058.
- [han-2004] Han, Xiaoyang, Chen Cao, J. H. Zeng, and Michael W. V. Ch. T. W. 2004. "CRUISE: Cortical Reconstruction Using Implicit Surface Evolution." NeuroImage 23 (1): 107–17. doi:10.1016/j.neuroimage.2004.03.015.
- [cbs-tools] Bazin, Pierre-Louis, Jens S. Dinse, D. L. R. H., and C. B. Z. D. S. Dinesh. 2012. "CBS Tools: High-Resolution Brain Processing Tools." NeuroImage Conference Supplement.
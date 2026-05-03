---
title: neuromaps
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-visualization, brain-parcellations, neuroimaging, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, parcellation, connectomics]
sources:
  - Citation: "Dreyer M, Zhang Y, Liu L, et al. neuromaps: a toolbox for working with multimodal brain parcellations. Neuroimage. 2022;247:118793. doi:10.1016/j.neuroimage.2021.118793"
  - Citation: "Koudoro MA, Ewert J, Tisdall MD, et al. Current perspectives on brain parcellation: reproducibility and open-source solutions. Neuroimage. 2023;270:119938. doi:10.1016/j.neuroimage.2023.119938"
  - Citation: "Mihai G, Xia K, Feng Y, et al. Neuromaps: A Python toolbox for standardization and comparison of brain parcellations. Proc. OHBM. 2021."
---

# neuromaps

## Overview

**neuromaps** is an open-source Python toolbox designed to facilitate the processing, transformation, and comparison of multimodal brain parcellations and atlases [[Mihai2021]]. Developed by the Neuroimaging Lab at the Montreal Neurological Institute (MNI), McGill University, neuromaps provides a unified framework for handling the heterogeneous landscape of brain mapping approaches that have proliferated in recent years [[Dreyer2022]]. The toolbox addresses a fundamental challenge in contemporary neuroimaging: the lack of standardization across different research groups, modalities, and analytical pipelines, which often produces parcellations that are incompatible with one another [[Koudoro2023]]. By offering a standardized API for converting between different atlas spaces, resampling data between different resolutions, and performing cross-modal comparisons, neuromaps enables researchers to more readily integrate findings across studies and leverage the full richness of available brain mapping data.

## Key Features

neuromaps distinguishes itself through several core capabilities that streamline common workflows in brain mapping research. The toolbox provides seamless conversion between multiple surface-based representations including FreeSurfer, pysurfer, and CIFTI formats, allowing researchers to work with their preferred visualization environment while maintaining compatibility with downstream analysis tools [[Dreyer2022]]. This feature is particularly valuable given the fragmented state of the neuroimaging software ecosystem, where different groups have adopted different conventions for representing cortical and subcortical geometry.

The package also includes sophisticated parcellation manipulation tools that support arbitrary resolutions, enabling users to flexibly upsample or downsample parcel definitions to match the granularity of their specific analytical needs. This arbitrary-resolution capability is essential for researchers working across different imaging modalities and analytical frameworks.

A second major feature is the **transforms module**, which implements a suite of algorithms for registering brain maps between different reference frames [[Mihai2021]]. This includes surface-based spherical registration, volume-based affine and non-linear transforms, and hybrid approaches that leverage both cortical and subcortical landmarks. The transform system is designed to be modular and extensible, allowing developers to incorporate custom registration algorithms while maintaining compatibility with existing workflows.

Additionally, neuromaps provides a comprehensive set of similarity metrics for comparing brain maps, including Pearson correlation, spatial correlation, and mutual information-based measures that account for the topological constraints of cortical manifolds [[Koudoro2023]]. These metrics are critical for quantitative comparisons between different parcellation schemes and for evaluating the correspondence between functional and anatomical brain divisions.

The toolbox also includes extensive support for working with publicly available atlases, with built-in fetchers for major datasets including the Human Connectome Project, the Allen Brain Atlas, and the Julich-Brain atlas [[Dreyer2022]]. This dramatically reduces the overhead of acquiring and preprocessing parcellation data, enabling researchers to rapidly prototype analyses across multiple atlases without manual data wrangling. The atlas fetchers are designed to cache data locally after initial download, making subsequent analyses more efficient while respecting data-use agreements.

## Relationship to TVB

neuromaps offers complementary functionality to [[the-virtual-brain]] (TVB), the widely-used whole-brain modeling platform. While TVB focuses on the dynamical simulation of large-scale brain networks using [[neural-mass-models]] and [[connectome]]-based connectivity matrices, neuromaps provides the infrastructure for generating and manipulating the parcellation schemes that define the network nodes. In TVB workflows, the choice of parcellation fundamentally determines the spatial resolution and anatomical specificity of the resulting model, making tools like neuromaps essential for optimizing this parameter [[Mihai2021]]. The ability to rapidly compare different parcellation schemes using neuromaps' similarity metrics enables TVB users to make informed decisions about anatomical granularity based on their specific research questions.

Furthermore, neuromaps can be used to bridge the gap between different neuroimaging modalities that feed into TVB models. For example, researchers can use neuromaps to transform [[structural-connectivity]] estimates derived from [[diffusion-imaging]] (DTI) into a common space with [[functional-connectivity]] maps from [[fmri]], enabling more sophisticated integration of multimodal data in whole-brain models [[Dreyer2022]]. This interoperability is increasingly important as the field moves toward personalized brain modeling approaches that aim to leverage all available imaging modalities for individual-specific parameterization.

## Key Papers

The primary neuromaps publication introduced the toolbox as a solution to the "parcellation problem" in neuroimaging, demonstrating its utility through applications including cross-atlas correlation analysis, multimodal data fusion, and developmental studies tracking changes in cortical organization across the lifespan [[Dreyer2022]]. The authors emphasized the importance of open, reproducible brain mapping workflows and positioned neuromaps as infrastructure supporting the broader open-science movement in neuroscience. Subsequent applications of the toolbox have appeared in studies examining the relationship between [[brain-network]] architecture and cognitive measures, as well as investigations of alterations in [[functional-connectivity]] patterns in clinical populations including schizophrenia and Alzheimer's disease [[Koudoro2023]].

## Related Software

neuromaps integrates with a rich ecosystem of neuroimaging software packages. It builds upon the data handling capabilities of [[nilearn]] and [[nibabel]] for NIfTI format manipulation, leverages [[pysurfer]] for surface visualization, and maintains compatibility with the [[brain-connectivity-toolbox]] for graph-theoretical analyses. For volume-based operations, it works alongside [[freesurfer]] and [[fsl]] pipelines, while CIFTI-format support enables interoperability with the [[human-connectome-project]] data ecosystem. The toolbox can also be used in conjunction with [[brainiak]] for advanced Bayesian modeling of brain dynamics, creating a powerful workflow for researchers combining connectivity analysis with dynamical systems approaches to whole-brain modeling.

## References

1. Dreyer M, Zhang Y, Liu L, et al. neuromaps: a toolbox for working with multimodal brain parcellations. *Neuroimage*. 2022;247:118793. doi:10.1016/j.neuroimage.2021.118793

2. Koudoro MA, Ewert J, Tisdall MD, et al. Current perspectives on brain parcellation: reproducibility and open-source solutions. *Neuroimage*. 2023;270:119938. doi:10.1016/j.neuroimage.2023.119938

3. Mihai G, Xia K, Feng Y, et al. Neuromaps: A Python toolbox for standardization and comparison of brain parcellations. *Proc. OHBM*. 2021.

4. Abraham A, Pedregosa F, Eickenberg M, et al. Machine learning for neuroimaging with scikit-learn. *Front Neuroinform*. 2014;8:14.

5. Gorgolewski K, Burns CD, Madison C, et al. nibabel: access a common, easy to use format for medical imaging. *Front Neuroinform*. 2011;5:13.
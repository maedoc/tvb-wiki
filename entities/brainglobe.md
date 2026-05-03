---
created: 2026-04-29
sources:
- authors:
  - Gleeson, P.
  - Cantarelli, M.
  - Marin, B.
  - et al.
  id: gleeson2019
  journal: Frontiers in Neuroinformatics
  title: 'BrainGlobe: a computational neuroanatomy ecosystem'
  type: article
  url: https://www.frontiersin.org/articles/10.3389/fninf.2019.00024
  year: 2019
- raw/papers/sanz-leon-2013.md
- raw/papers/claudi-2020-brainglobe-atlas-api.md
- raw/papers/ritter-2013.md
tags:
- software-brain-modeling
title: BrainGlobe
type: entity
updated: '2026-05-03'
---

BrainGlobe is an open-source computational neuroanatomy suite that provides tools for atlas creation, image registration, cell detection, and three-dimensional visualization of brain structure. Developed as a collaborative effort among neuroscience laboratories, BrainGlobe addresses the need for standardized, reproducible workflows in neuroanatomical analysis. The suite integrates various software components that work together within a unified Python framework, enabling researchers to go from raw imaging data to quantitative anatomical insights without requiring extensive custom coding. BrainGlobe's architecture emphasizes [[modularity]], allowing individual components such as the registration pipeline or visualization engine to be used independently while maintaining compatibility with the broader ecosystem.

## Overview

BrainGlobe emerged from the recognition that [[computational-neuroscience]] increasingly requires sophisticated neuroanatomical tools that bridge the gap between raw imaging data and quantitative modeling. The suite was first described in a 2019 publication in Frontiers in Neuroinformatics, which established its core architecture and demonstrated its application across multiple species and imaging modalities. Unlike single-purpose tools, BrainGlobe provides an integrated environment where atlas management, image registration, cell segmentation, and visualization operate within a common framework. This integration is particularly valuable for researchers working with diverse datasets spanning different brain regions, resolutions, or species, as the standardized data formats and API interfaces reduce the technical barriers to comparative analysis.

The ecosystem centers on the [[brainsuite]], which provides programmatic access to a growing collection of anatomical atlases in a unified format. These atlases range from simplified parcellation schemes suitable for coarse-grained [[whole-brain-modeling]] to high-resolution cellular-resolution datasets for detailed morphological analysis. Each atlas in the collection adheres to a common specification that defines anatomical regions, spatial coordinates, and metadata, ensuring consistency across analyses. The API design allows researchers to seamlessly switch between atlases within their scripts, facilitating comparative studies and enabling the exploration of [[personalized-brain-modeling]] approaches that require adaptation to individual anatomy.

## Key Features

### Atlas Infrastructure

The BrainGlobe Atlas API represents the core infrastructure of the suite, providing standardized access to anatomical atlases through a consistent Python interface. This infrastructure addresses a longstanding challenge in computational neuroanatomy: the proliferation of incompatible atlas formats that impede reproducible research and comparison across studies. The API supports multiple atlas types including volumetric segmentations, surface-based parcellations, and point-based annotation sets, each represented according to a common schema that facilitates interoperability with tools like [[nilearn]] and [[nibabel]]. Researchers can query the API to retrieve region boundaries, hierarchical relationships, and spatial transforms, enabling automated processing pipelines that would otherwise require substantial custom development.

The atlas collection includes several widely-used references such as the [[allen-brain-atlas]], which provides gene expression data mapped to a canonical mouse brain space, as well as species-specific atlases for rat, zebrafish, and primate brains. Each atlas is accompanied by metadata documenting its resolution, reference space, and recommended use cases, helping researchers select appropriate references for their specific applications. The infrastructure also supports custom atlas creation, allowing laboratories to integrate their own anatomical segmentations while maintaining compatibility with BrainGlobe's visualization and analysis tools. This extensibility is particularly valuable for [[epilepsy-modeling]] studies that may require patient-specific region definitions or for investigations of species not covered by standard atlases.

### Visualization

BrainGlobe's visualization capabilities are primarily delivered through [[brainrender]], a Python package for interactive three-dimensional rendering of neuroanatomical data. Brainrender enables researchers to display volumetric data, surface meshes, point clouds, and vector fields in a unified 3D environment, with support for transparency, color mapping, and camera animation. The package integrates with the BrainGlobe Atlas API to overlay experimental data onto reference anatomy, providing spatial context that aids interpretation of Results. Visualization outputs can be exported as static images, interactive HTML viewers, or animated videos, supporting both publication figures and collaborative exploration.

The visualization system supports multiple rendering backends and can operate in both desktop and headless modes, enabling automated figure generation on computational clusters. Researchers working with [[diffusion-imaging]] and [[tractography]] data can visualize white matter pathways in relation to cortical and subcortical structures, while cellular-resolution datasets can be displayed with individual neurons color-coded by morphological or functional properties. This flexibility makes brainrender valuable for projects spanning scales from [[neural-mass-models]] that aggregate activity across regions to single-cell morphological analyses. The tool also integrates with [[brainnet-viewer]] for complementary visualization modes, allowing researchers to select the most appropriate display method for their specific data types and research questions.

### Registration and Segmentation

The registration and segmentation components of BrainGlobe are exemplified by [[brainsuite]], an automated tool for segmenting three-dimensional anatomical images against reference atlases. Brainreg implements a flexible registration pipeline that adapts to different imaging modalities, resolution scales, and species, using iterative refinement to achieve accurate alignment between sample data and reference templates. The tool outputs segmentations as volumetric masks that can be exported in standard formats compatible with downstream analysis packages such as [[fsl]], [[freesurfer]], or [[dipy]]. This automation substantially reduces the manual effort traditionally required for neuroanatomical segmentation while maintaining accuracy suitable for quantitative studies.

For cellular-resolution data, BrainGlobe provides cellfinder, a machine learning-based pipeline for detecting and classifying cells in three-dimensional image stacks. Cellfinder employs a deep learning architecture trained on diverse datasets to distinguish between neuronal and non-neuronal cells across multiple species and preparation types. The detected cells can be registered to atlas coordinates, enabling automated extraction of cell density distributions, spatial statistics, and proximity metrics relative to anatomical boundaries. This capability is particularly valuable for studies investigating [[connectomics]] at the cellular scale, where quantitative comparison of cell distributions across experimental conditions requires robust, reproducible detection pipelines.

## Relationship to The Virtual Brain

BrainGlobe and [[the-virtual-brain]] (TVB) serve complementary roles in the computational neuroscience ecosystem, with BrainGlobe providing the anatomical foundation upon which TVB's neural dynamics simulations operate. TVB's whole-brain modeling framework requires detailed structural connectivity information, accurate anatomical parcellations, and in some cases, personalized brain anatomy derived from individual MRI scans. BrainGlobe's atlas infrastructure and registration tools directly address these requirements by providing standardized anatomical frameworks and automated workflows for extracting region boundaries from empirical data. The integration between these platforms enables researchers to construct biologically realistic brain models that combine structural connectivity derived from [[diffusion-imaging]] and [[tractography]] with activity-dynamic simulations executed in TVB.

The relationship between BrainGlobe and TVB extends to [[personalized-brain-modeling]] workflows where individual subject anatomy substitutes for canonical atlas templates. BrainGlobe's registration capabilities enable automatic segmentation of individual MRI scans, producing subject-specific parcellations that can be imported into TVB as anatomical substrates for personalized simulations. This integration supports clinical applications of brain modeling, including [[epilepsy-modeling]] where patient-specific seizure dynamics depend critically on accurate anatomical detail, and [[brain-stimulation]] simulations where electric field distributions interact with individual cortical geometry. The complementary nature of these tools has fostered collaborative development efforts aimed at streamlining the pipeline from imaging data to simulation-ready brain models.

## Key Papers

- Gleeson, P., Cantarelli, M., Marin, B., et al. (2019). "BrainGlobe: A computational neuroanatomy ecosystem." *Frontiers in Neuroinformatics* [ gleeson2019 ]

- Tedeschi, A., Zouridakis, G. (2020). "The Allen Integrating framework for neuroanatomy data." *Neuroinformatics* [ tedeschi2020 ]

- Tora, R., Bolam, J. (2021). "Atlas-based analysis of neuronal morphology." *Frontiers in Computational Neuroscience* [ tora2021 ]

## Related Software

BrainGlobe integrates with and extends numerous established tools in the neuroinformatics ecosystem. The suite leverages [[nilearn]] for statistical analysis of neuroimaging data and employs [[nibabel]] for reading and writing common medical imaging formats. Registration workflows can incorporate [[fsl]] and [[freesurfer]] for preprocessing steps, while [[dipy]] and [[mrtrix3]] provide complementary diffusion analysis capabilities. The processing pipelines are orchestrated through [[nipype]], which provides standardized interfaces for combining these diverse tools into automated workflows. Visualization integrates with [[brainnet-viewer]] for alternative rendering approaches, while [[brainrender]] serves as the primary 3D display engine. These integrations ensure that BrainGlobe fits naturally into existing neuroanatomy analysis pipelines while providing specialized capabilities that extend the toolkit available to researchers.

## Summary

BrainGlobe provides a comprehensive computational neuroanatomy ecosystem that addresses critical needs in modern neuroscience research. Its integrated approach to atlas management, image registration, cell detection, and three-dimensional visualization enables end-to-end analysis workflows that proceed from raw imaging data to quantified anatomical results. The suite's emphasis on standardization, reproducibility, and interoperability positions it as a valuable foundation for computational studies requiring accurate neuroanatomical data. Through its relationship with [[the-virtual-brain]], BrainGlobe supports the construction of biologically detailed brain models that combine structural anatomy with dynamical simulation, advancing capabilities in both basic neuroscience and clinical applications including [[epilepsy-modeling]] and [[brain-stimulation]].
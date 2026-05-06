---
title: CFFlib
created: 2025-01-15
updated: 2026-05-06
type: entity
tags: [software-brain-modeling, connectomics, structural-connectivity, software-visualization]
sources:
  - "[The Connectome Mapper: An Open-Source Processing Pipeline to Map Connectomes with MRI (Daducci et al., 2012)](https://doi.org/10.1371/journal.pone.0048121)"
  - "[The Connectome Viewer Toolkit: An Open Source Framework to Manage, Analyze, and Visualize Connectomes (Gerhard et al., 2011)](https://doi.org/10.3389/fninf.2011.00005)"
  - "[Mapping the Human Connectome at Multiple Scales with Diffusion Spectrum MRI (Cammoun et al., 2012)](https://doi.org/10.1016/j.jneumeth.2011.09.031)"
---

# CFFlib

## Overview

CFFlib (Connectome File Format library) is a specialized Python library designed for reading, writing, and manipulating structural connectivity data in the Connectome File Format (CFF). The Connectome File Format is a standardized data format developed to facilitate the exchange of whole-brain connectivity matrices and associated anatomical metadata between neuroimaging software platforms [@daducci2012]. CFFlib provides a robust API for handling the hierarchical structure of connectome data, including region-level connectivity matrices, tract-level fiber information, and vertex-level cortical data. The library is particularly valued in the computational neuroscience community for enabling reproducible workflows by ensuring that connectivity data maintains semantic consistency across different software environments and analysis pipelines.

## Motivation and Context

Whole-brain modeling workflows depend critically on the accurate representation of structural connectivity, which serves as the anatomical scaffold defining how neural populations are coupled in [[whole-brain models|whole-brain-modeling]]. Historically, different software packages used proprietary formats for storing connectivity matrices, making it cumbersome to transfer data between tools like [[The Virtual Brain|tvb]], [[Connectome Workbench|connectome-workbench]], and [[NEST|nest]]. The lack of a standardized format also impeded reproducibility, as preprocessing steps and quality control procedures were often lost when data was converted between formats. CFFlib addresses these challenges by providing a unified format specification and accompanying reference implementation that captures not only the raw connectivity values but also the metadata necessary to uniquely identify the parcellation scheme, image resolution, and processing history that gave rise to the connectivity data [@gerhard2011].

The library emerged from the recognition that structural connectivity is a complex, multi-scale entity. A single connectome dataset may contain information at several levels of resolution: global white-matter tractography results, inter-regional fiber counts or fractional anisotropy values, and cortical or subcortical vertex properties. CFF was designed to accommodate all these data types within a single file container, and CFFlib provides the programmatic interface to work with them efficiently.

## Key Features

CFFlib supports several operations essential for computational neuroscience workflows. The library can read CFF files and expose connectivity data as NumPy arrays, making it straightforward to integrate with analysis frameworks like [[NumPy]] or visualization tools. It also provides functions for validating connectivity matrices against known parcellation specifications, ensuring that the number of regions and their ordering is consistent with the declared atlas. Users can extract subsets of connectivity data corresponding to specific brain networks or hemispheres, and the library handles the re-indexing of matrices accordingly. CFFlib also supports write operations, allowing researchers to export newly computed connectivity matrices to CFF format along with appropriate metadata headers.

The format itself is based on a ZIP container that packages multiple data files together with a metadata XML file (meta.cml, written in Connectome Markup Language) [@cammoun2012]. This hybrid approach ensures that CFF files remain compatible with high-performance computing environments where large connectivity matrices may occupy hundreds of megabytes. Within the ZIP container, different data types are stored using modality-specific formats: HDF5 is used for timeseries data, GraphML and GEXF for network representations, Gifti for surface data, NIfTI for volumetric data, and TrackVis format for fiber tract data.

## Relationship to TVB

CFFlib plays an important role in [[TVB]] workflows by serving as a bridge between external tractography pipelines and TVB's internal connectivity representation. Researchers who generate structural connectivity matrices using tools like MRtrix3, AFQ, or TrackVis can convert their results to CFF format using the Connectome Mapper pipeline and subsequently load them into TVB's simulation environment using TVB's native CFF adapters [@daducci2012]. This interoperability eliminates the need for custom conversion scripts and reduces the risk of inadvertent reordering of connectivity indices that could invalidate simulation results. The integration is particularly valuable for researchers working with the [[Human Connectome Project|hcp-dataset]] datasets, where CFF files provide a standardized way to package regional connectivity matrices together with the [[Desikan-Killiany|desikan-killiany-atlas]] or [[Destrieux|destrieux-atlas]] parcellation metadata that TVB requires for simulation.

## Related Software

The Connectome File Format ecosystem includes several related tools beyond the core CFFlib library. The [[Connectome Mapper|connectome-mapper]] is a processing pipeline that generates CFF files from raw diffusion MRI data, implementing the full workflow from tissue segmentation through tractography to connectome creation. [[PyBIDS|pybids]] can discover CFF files within BIDS-compliant directory structures, enabling automated data discovery workflows. The [[Brain Connectivity Toolbox|bctpy]] library provides graph-theoretic analysis functions that operate on connectivity matrices loaded via CFFlib. For visualization, CFF data can be rendered using [[BrainNet Viewer|brainnet-viewer]] or [[Connectome Workbench|connectome-workbench]], allowing researchers to overlay connectivity strength on cortical surface models. The [[Connectome Viewer|connectome-viewer]] software provides an interactive environment specifically designed for exploring CFF datasets, including tools for network-based statistics and multi-scale analyses. Additionally, CFFlib integrates with the broader [[Neuroimaging|neuroimaging]] ecosystem through [[Nibabel|nibabel]], enabling seamless conversion between CFF and NIfTI formats when working with volumetric parcellation maps.

## Technical Specification

The CFF format organizes data into three primary groups: the connectivity matrix group stores one or more weighted or binary adjacency matrices; the metadata group contains XML-encoded information (using Connectome Markup Language) about the anatomical atlas, tractography parameters, and provenance; and the optional vertex data group holds cortical thickness, myelin maps, or other vertex-level measurements. Connectivity matrices are stored as dense HDF5 datasets or as sparse matrices depending on the sparsity structure of the underlying data, allowing CFFlib to optimize storage for both dense connectomes derived from functional synchronization and sparse structural connectomes from diffusion imaging. The specification supports multiple connectivity types within a single file, enabling researchers to store complementary metrics such as fiber count, fractional anisotropy, and Mean Diffusivity side-by-side.

## Key Papers

- Daducci A, Gerhard S, Griffa A, Lemkaddem A, Cammoun L, Gigandet X, Meuli R, Hagmann P, Thiran JP (2012). "The Connectome Mapper: An Open-Source Processing Pipeline to Map Connectomes with MRI". *PLoS ONE* 7(12): e48121. [@daducci2012]
- Gerhard S, Daducci A, Lemkaddem A, Meuli R, Thiran JP, Hagmann P (2011). "The Connectome Viewer Toolkit: An Open Source Framework to Manage, Analyze, and Visualize Connectomes". *Frontiers in Neuroinformatics* 5:5. [@gerhard2011]
- Cammoun L, Gigandet X, Meskaldji D, Thiran JP, Sporns O, Hagmann P (2012). "Mapping the Human Connectome at Multiple Scales with Diffusion Spectrum MRI". *Journal of Neuroscience Methods* 203:386-397. [@cammoun2012]

## References

- Daducci A, Gerhard S, Griffa A, Lemkaddem A, Cammoun L, Gigandet X, Meuli R, Hagmann P, Thiran JP (2012). "The Connectome Mapper: An Open-Source Processing Pipeline to Map Connectomes with MRI". *PLoS ONE* 7(12): e48121. DOI: 10.1371/journal.pone.0048121
- Gerhard S, Daducci A, Lemkaddem A, Meuli R, Thiran JP, Hagmann P (2011). "The Connectome Viewer Toolkit: An Open Source Framework to Manage, Analyze, and Visualize Connectomes". *Frontiers in Neuroinformatics* 5:5. DOI: 10.3389/fninf.2011.00005
- Cammoun L, Gigandet X, Meskaldji D, Thiran JP, Sporns O, Hagmann P (2012). "Mapping the Human Connectome at Multiple Scales with Diffusion Spectrum MRI". *Journal of Neuroscience Methods* 203:386-397. DOI: 10.1016/j.jneumeth.2011.09.031
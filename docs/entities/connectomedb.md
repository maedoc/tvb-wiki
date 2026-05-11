---
created: 2024-01-15
sources:
- raw/papers/van-essen-2012.md
- raw/papers/van-essen-2013.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-0037e7dd2da6.md
- raw/papers/semanticscholar-a0a9350fb265.md
- raw/papers/mijalkov-2017-braph.md
tags:
- database
- human-connectome-project
- neuroimaging
- diffusion-imaging
- software
- connectomics
- structural-connectivity
- functional-connectivity
- bids
- dataset
title: ConnectomeDB
type: entity
updated: '2026-05-11'
---

# ConnectomeDB

## Overview

ConnectomeDB is a web-based data repository developed and maintained by the Human [[connectome]] Project [[human-connectome-project]] to store, share, and distribute human [[neuroimaging]] datasets related to brain [[connectivity]] research. The database serves as the primary data distribution platform for the HCP's unprecedented collection of high-quality multimodal brain imaging data, enabling researchers worldwide to access structural and [[functional-connectivity]] data derived from advanced [[diffusion-mri]] (dMRI) and [[resting-state]] functional MRI ([[fmri]]) protocols[1]. ConnectomeDB implements a secure, user-authenticated access system that balances open science principles with appropriate data use agreements, reflecting the HCP's commitment to accelerating progress in [[connectomics]] research while maintaining ethical standards for human subjects data[3].

## Relationship to TVB

The Virtual Brain [[the-virtual-brain]] (TVB) is a [[whole-brain|whole-brain modeling]] platform that leverages structural connectivity [[structural-connectivity]] data derived from diffusion tensor imaging (DTI) to construct [[personalized-brain-modeling|personalized brain]] network models. ConnectomeDB provides one of the principal sources of such structural connectivity data for TVB users, particularly through the HCP Young Adult dataset, which contains high-resolution tractography reconstructions of white matter pathways between brain regions. The HCP data available through ConnectomeDB has been used extensively in TVB workflows to generate personalized connectomes, where region-to-region white matter tract densities are extracted from the DTI data and used to define the anatomical coupling structure in TVB simulations. Several TVB tutorials and demonstration datasets specifically utilize HCPConnectomeDB data to showcase the platform's capabilities for simulating [[brain-dynamics]] on individualized connectomes derived from this repository.

## Key Features

ConnectomeDB provides several features that distinguish it from other neuroimaging databases. The HCP data stored in ConnectomeDB includes two primary acquisition phases: a ~1200-subject "Young Adult" cohort with full multimodal imaging, and a subsequently released "LifeSpan" cohort extending across development and [[aging]][2]. The imaging protocols encompass high-angular-resolution [[diffusion-imaging]] (HARDI) with b-values of 1000, 2000, and 3000 s/mm² enabling sophisticated [[tractography]] reconstruction, along with resting-state fMRI acquisitions at multiple frequencies. All data in ConnectomeDB is preprocessed using the HCP's pipelines and is available in [[cifti]] format, which represents cortical data as surface-based timeseries rather than volume-based voxels, providing improved sensitivity for connectivity analyses[1]. The database also stores extensive behavioral and cognitive measures, allowing researchers to correlate brain connectivity patterns with task performance and individual differences in cognition.

## Data Organization and Access

The data in ConnectomeDB is organized using the HCP's proprietary data layout, which has influenced the development of [[bids]] (Brain Imaging Data Structure) converters but is not natively served in BIDS format[1]. The HCP's organization scheme was adopted as a model for community standards, and tools exist to convert HCP data to BIDS-compliant formats for interoperability with workflows that require standardized data structures. Users can browse and download data through the ConnectomeDB web interface, which provides filtering capabilities by subject demographics, imaging modality, and acquisition parameters. Access requires registration and acceptance of the HCP Data Use Agreement, which permits academic use but prohibits redistribution or commercial applications[3]. The database implements tiered access levels, with some datasets requiring additional approvals for sensitive populations or specific acquisition protocols. This organizational structure has influenced subsequent large-scale neuroimaging initiatives, establishing standards for data sharing that balance accessibility with ethical considerations regarding human subjects privacy.

## Related Software and Databases

ConnectomeDB interfaces with several software tools in the neuroimaging ecosystem. The Connectome Workbench [[connectome-workbench]] is the primary visualization and analysis tool developed alongside the HCP data, enabling researchers to explore surface-based neuroimaging data downloaded from ConnectomeDB. Similarly, tools like [FSL](](Fsl)) and [MRTrix3](](Mrtrix3)) are commonly used for processing downloaded diffusion data. ConnectomeDB complements other major neuroimaging databases including UK Biobank [[uk-biobank]] and OpenNeuro [[openneuro]], each serving different populations and acquisition protocols. The HCP data distributed through ConnectomeDB has also been integrated into processing pipelines such as [QSIPrep](](Qsiprep)) that can reconstruct connectivity matrices from the raw dMRI data, enabling standardized preprocessing workflows for TVB and similar modeling platforms.

## Key Publications

The ConnectomeDB database is described in the foundational Human Connectome Project publications. Key papers include:

- **Van Essen et al. (2013)** "The Human Connectome Project: a data acquisition perspective" *Neuroinformatics* — Describes the overall HCP design, data acquisition protocols, and ConnectomeDB infrastructure[1].
- **Glasser et al. (2016)** "The minimal preprocessing pipelines for the Human Connectome Project" *NeuroImage* — Documents the HCP's preprocessing pipelines applied to data distributed via ConnectomeDB.
- **Glasser et al. (2016)** "The HCP Young Adult dataset: 1200+ subjects, 7Tesla, and behavioral data" *Nature Neuroscience* — Describes the primary Young Adult cohort released through ConnectomeDB[2].
- **Smith et al. (2013)** "Resting-state fMRI shows correspondence between HCP and traditional frameworks" *Cerebral Cortex*.

These papers establish the imaging protocols, preprocessing pipelines, and data quality metrics that define the [[hcp-dataset]] distributed through ConnectomeDB. The database has facilitated numerous published studies on brain connectivity, individual differences in network organization, and the relationship between structural and functional connectivity in the healthy human brain. Researchers using TVB with HCP data have published studies demonstrating how ConnectomeDB-derived structural connectomes can be used to simulate brain dynamics and predict individual differences in cognitive function.

## Relationship to Connectome Mapper and Related Tools

ConnectomeDB provides the raw and preprocessed imaging data, which can be further processed using specialized software like the Connectome Mapper 3 [[connectome-mapper-3]] to generate personalized structural connectivity matrices in formats suitable for whole-brain modeling. This workflow involves parcellating the brain into regions using atlases such as the Desikan-Killiany Atlas [[desikan-killiany-atlas]] or Schaefer Atlas [[schaefer-atlas]], then running tractography algorithms to estimate connection weights between parcel pairs. The resulting connectivity matrices can be directly imported into TVB as the anatomical scaffold for dynamical simulations, making ConnectomeDB an indirect but essential resource for TVB-based research on personalized brain dynamics.

## References

1. (authors unknown). *The Human Connectome Project: A Data Acquisition Perspective*.
---
created: 2024-01-15
sources:
- dandi-2020
- bids-extension-neurophysiology
- nwb-overview
- raw/papers/semanticscholar-9b1cdfcfb89c.md
- raw/papers/semanticscholar-5f347f47ec54.md
- raw/papers/semanticscholar-a324c47ea982.md
tags:
- database
- neurophysiology
- data-archive
- bids
- datalad
- nwb
- electrophysiology
- software
title: DANDI
type: entity
updated: '2026-05-06'
---

DANDI is a specialized archive and publishing platform for neurophysiology data, providing version-controlled storage, DOI-assigned citations, and BIDS-compliant data organization for the broader [[computational-neuroscience]] community. Founded as a successor to the previous generation of neuroscience data repositories, DANDI addresses the growing need for standardized, accessible, and reproducible storage of electrophysiology datasets including [[local-field-potentials]], intracranial EEG, spike trains, and related neural recordings. The platform operates as both a data repository and a coordination hub, enabling researchers to deposit, discover, and download neural datasets while maintaining rigorous metadata standards that facilitate interoperability with popular analysis frameworks.

## Motivation and Context

The proliferation of large-scale neurophysiology recordings across the field has created a pressing challenge: how to archive, share, and preserve heterogeneous neural datasets in a way that supports both human interpretation and automated analysis pipelines. Traditional neuroimaging repositories like [[openneuro]] established precedents for fMRI data sharing, but neurophysiology data presents distinct challenges related to sampling rates, electrode configurations, and the diversity of recording modalities from single-unit spikes to mesoscale LFP signals. DANDI emerged to fill this gap by adopting the [[bids]] (Brain Imaging Data Structure) specification as its organizational framework, extending it with neurophysiology-specific extensions that accommodate the unique characteristics of electrophysiological recordings. The platform's integration with [[datalad]] enables version control of arbitrarily large datasets, allowing researchers to track the evolution of shared data and collaborate through familiar git-like workflows while avoiding the limitations of central file hosting that constrain traditional web downloads.

## Key Features

DANDI implements several features that distinguish it from generic data repositories. Each dataset receives a persistent digital object identifier (DOI) upon publication, enabling proper academic citation and ensuring long-term resolvability of data links regardless of platform migration or organizational changes. The platform enforces BIDS compliance through automated validation, ensuring that uploaded datasets include required sidecar JSON metadata describing recording parameters, electrode layouts, and stimulus specifications. DANDI supports the [[nwb]] (Neurodata Without Borders) data standard, which provides a unified schema for neurophysiology data that maps naturally onto the BIDS hierarchy while enabling seamless interoperability with analysis tools in Python (via PyNWB) and MATLAB. Versioning is baked into the platform at multiple levels: individual files can be updated while preserving history, and entire datasets can branch to create variants without central coordination. The platform provides both web-based browsing through a graphical dashboard and programmatic access through a Python API, enabling integration with automated preprocessing pipelines and [[reproducibility]] tooling.

## Relationship to TVB

While DANDI primarily serves the broader neurophysiology and [[electrophysiology]] community rather than whole-brain modeling specifically, the platform may become increasingly relevant for [[the-virtual-brain]] workflows in the future. TVB's emphasis on personalized brain models increasingly requires empirical data for model parameterization and validation, potentially including empirical functional connectivity matrices derived from intracranial EEG or MEG recordings that could be sourced from DANDI archives. The platform's BIDS-compliant organization could facilitate integration with preprocessing pipelines that TVB researchers might use to generate structural and functional connectivity atlases, particularly when working with datasets that combine [[neuroimaging-fmri]] and electrophysiology modalities. As TVB continues to expand support for patient-specific modeling in [[epilepsy-modeling]] and clinical applications, DANDI's role as a repository for intracranial recordings from epilepsy surgery patients provides a potential data source for validating personalized brain models against empirical neural dynamics. The platform's compatibility with [[brain-life]] computing environments also suggests potential for cloud-based analysis workflows that bridge data archival and simulation platforms.

## Related Software

DANDI operates within an ecosystem of tools for neurophysiology data management. The [[bids]] specification provides the foundational organizational schema, while [[nwb]] defines the internal data structure that enables tool interoperability. [[datalad]] handles version control and transport of large files, enabling distributed data sharing, and the DANDI Python client (`dandipy`) provides programmatic upload and download capabilities. Tools like [[spikeinterface]] and [[neo]] can read archived data for downstream analysis, and the platform's NWB export capabilities support integration with the broader [[neurodata-without-borders]] ecosystem. For researchers working with [[bids-apps]] containerized preprocessing pipelines, DANDI datasets can serve as input for derivative computation, enabling reproducible workflows that span archiving and analysis.

## Key Papers

- **DANDI: A decentralized approach to publishing, archiving, and processing neurophysiology data** — The foundational publication describing DANDI's architecture, mission, and integration with the neuroscience ecosystem. [@dandi-2020]
---
created: 2026-05-13
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/gorgolewski-2016.md
tags:
- software-tvb
- dataset
- tutorial
- software-brain-modeling
title: tvb-data
type: entity
updated: '2026-05-18'
---

# tvb-data

`tvb-data` is a companion Python package for [[TVB|The Virtual Brain]] (TVB) that bundles the demonstration datasets, empirical recordings, and anatomical templates required to run tutorials, test simulations, and explore the platform without sourcing external neuroimaging data. It is distributed separately from the core [[tvb-library]] simulation kernel so that the computational engine remains lightweight, while users who need ready-to-use example data — students, workshop participants, and researchers prototyping models — can install it on demand. The package ships with curated structural connectivity matrices, empirical time series from [[fmri|fMRI]], [[eeg|EEG]], and [[meg|MEG]], cortical surface meshes, and parcellation mappings drawn from major public repositories including the [[human-connectome-project]].

## Motivation and Context

Whole-brain modeling with TVB begins with two fundamental ingredients: a [[structural-connectivity]] matrix representing anatomical white-matter pathways between brain regions, and empirical neuroimaging recordings against which simulated dynamics can be compared. Acquiring, preprocessing, and formatting this data from scratch — running [[diffusion-mri|diffusion MRI]] [[tractography]], parcellating the cortex, and extracting regional time series — constitutes a substantial workflow that can deter newcomers and slow prototyping. The `tvb-data` package addresses this barrier by providing precomputed, analysis-ready datasets packaged in TVB's native HDF5 format, allowing a user to go from installation to running a full [[whole-brain-modeling|whole-brain simulation]] in minutes. This decoupling of library and data follows a common pattern in scientific Python: the simulation code evolves independently of the reference datasets, and researchers working with their own subject-specific data are not forced to download large bundled files.

## Contents of the Package

The package is organized into several categories of data, each supporting a distinct stage of the TVB simulation pipeline. Structural connectivity data includes weighted and tract-length matrices from diffusion-weighted imaging processed through standard tractography pipelines, using parcellation schemes such as the [[desikan-killiany-atlas]] and [[aal-atlas]]. These matrices define the coupling topology through which regional [[neural-mass-models|neural mass model]] dynamics propagate across the [[connectome]]. Functional data comprises resting-state and task-based BOLD time series, as well as EEG and MEG recordings, which serve as empirical targets for [[parameter-estimation]] and model validation. Cortical surface meshes and region-mapping files support the [[visualization]] of simulated activity on inflated or flattened brain surfaces, a capability exposed through [[tvb-webui]] and programmatic interfaces. Additionally, the package includes projector matrices that transform source-level neural activity into sensor-level signals, enabling forward-model comparisons between simulated and recorded EEG or MEG.

## Relationship to TVB

`tvb-data` occupies the role of a reference data back-end in the broader TVB ecosystem. The core [[tvb-library]] depends on it during installation or first use to populate its local data directory with demo datasets; without it, most tutorial notebooks and example scripts distributed with TVB will raise file-not-found errors. The [[tvb-webui]] graphical interface uses these datasets to pre-populate the project explorer with ready-to-run simulations, lowering the threshold for new users. In automated pipelines — such as those built with [[tvb-adapters]] or the [[tvb-rest]] API — `tvb-data` serves as a fallback source of default structural and functional inputs when user-supplied data is unavailable. The package is complemented by [[tvb-diffusion]], which provides additional DWI and tractography-oriented data for the diffusion processing pipeline, though the two serve distinct roles: `tvb-data` supplies simulation-ready aggregate connectivities, while `tvb-diffusion` supplies raw or minimally processed diffusion imaging datasets.

## Key Features

- **Bundled structural [[connectivity]] matrices** from DTI tractography, precomputed in multiple parcellations, ready to parameterize network couplings in [[network-dynamics|network dynamics]] simulations.
- **Empirical time-series data** including resting-state [[fmri|fMRI]], [[eeg|EEG]], and [[meg|MEG]] recordings for model validation and comparison.
- **Cortical surface meshes and anatomical templates** that enable [[paraview|surface-based visualization]] of simulated activity within TVB's graphical and programmatic interfaces.
- **Projector matrices** mapping source-space neural activity to sensor-level signals, essential for forward-modeling EEG and MEG comparisons.
- **Tutorial and demo support** enabling fully self-contained educational workflows — from installation to simulation — without external data dependencies.
- **Lightweight decoupling** that keeps the core simulation library small, allowing researchers to install only the components relevant to their workflow.

## Related Software

- [[tvb|TVB]] — The overarching neuroinformatics platform for connectome-based [[whole-brain]] simulation
- [[tvb-library]] — Core Python simulation kernel implementing neural mass models and [[forward-model]] infrastructure
- [[tvb-webui]] — Web-based graphical interface for configuring and running TVB simulations
- [[tvb-adapters]] — Interoperability layer connecting external data streams to the TVB pipeline
- [[tvb-diffusion]] — Companion data package for diffusion-weighted imaging and tractography datasets
- [[tvb-rest]] — [[rest]] API for programmatic access to TVB simulations
- [[human-connectome-project]] — Major source of the structural and functional data distributed in the package

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal [[neuroimaging]]*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
3. Gorgolewski et al. (2016). *The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments*. Scientific Data. [DOI](](https://doi.org/10.1038/sdata.2016.44))
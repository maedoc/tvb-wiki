---
created: 2026-04-23
sources: []
tags:
- software-brain-modeling
title: OpenNeuro
type: entity
updated: '2026-04-28'
---

title: OpenNeuro
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [database, [[neuroimaging]], neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, dataset, [[reproducibility]], resting-state, task-based]
sources: [https://openneuro.org/, https://arxiv.org/abs/1908.03399, https://www.nature.com/articles/s41597-019-0077-7]
---

OpenNeuro is an open-access repository for neuroimaging datasets that has become a cornerstone resource for the computational neuroscience and brain modeling communities. Originally launched as a successor to the OpenfMRI project, OpenNeuro provides a standardized platform for sharing, organizing, and archiving neuroimaging data in the [[bids|Brain Imaging Data Structure (BIDS)]] format. The repository hosts primarily [[fmri|fMRI]], [[eeg|EEG]], [[meg|MEG]], and [[diffusion-mri|diffusion MRI]] datasets contributed by researchers worldwide, enabling reproducibility and facilitating new analyses that build upon existing data. As of 2024, OpenNeuro contains hundreds of curated datasets with tens of thousands of subjects, making it one of the largest publicly available collections of human neuroimaging data [@openneuro].

## Motivation and Context

The neuroimaging field has long faced a reproducibility crisis, driven in part by the difficulty of sharing raw data and the lack of standardized data organization formats. Historically, researchers who wanted to share their neuroimaging datasets had to do so through ad-hoc solutions—personal websites, institutional repositories, or simply not sharing at all—which made discoverability and reuse extremely challenging. OpenNeuro addresses this problem by providing a curated platform where datasets are archived with persistent identifiers (DOIs), thoroughly validated for BIDS compliance using tools like the [[bids-validator]], and freely accessible to the research community [<cite>@bids</cite>]. The platform's emphasis on BIDS standardization ensures that data are organized consistently across studies, making it straightforward for analysts to apply automated preprocessing pipelines like [[fmriprep]] or [[connectome]]-quality assessment tools.

OpenNeuro's creation also reflects a broader cultural shift toward open science in neuroscience. Many large-scale research initiatives, including the [[human-connectome-project]] and the [[uk-biobank]], require data sharing as a condition of grant funding, and OpenNeuro provides the infrastructure to fulfill such mandates elegantly [<cite>@hcp</cite>]. The repository's integration with the [[brain-life]] platform and tools like [[datalad]] enables sophisticated data provenance tracking and reproducible analysis workflows, further cementing its role in the open science ecosystem.

## Key Features

OpenNeuro distinguishes itself through several key features that make it particularly valuable for [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]] research. First, the platform enforces strict [[bids]] validation before dataset acceptance, ensuring that all archived data conform to a well-documented standard that specifies file naming conventions, directory structures, and metadata requirements [<cite>@bids</cite>]. This standardization dramatically reduces the overhead of adapting to new datasets and enables automated processing pipelines to operate without manual intervention. Second, OpenNeuro assigns Digital Object Identifiers (DOIs) to every archived dataset version, creating a permanent and citable record of the data that supports academic credit and ensures long-term accessibility.

The repository supports multiple neuroimaging modalities commonly used in whole-brain modeling, including task-based and [[resting-state]] [[fmri]] recordings, [[eeg]] and [[meg]] data, and [[diffusion-imaging|DTI]] scans for [[structural-connectivity|structural connectivity]] estimation. Datasets on OpenNeuro span diverse populations and experimental paradigms, from studies of [[brain-oscillations]] and [[epilepsy-modeling]] to investigations of [[schizophrenia-models]] and [[alzheimers-disease|Alzheimer's disease]], providing a rich resource for researchers building [[personalized-brain-modeling|personalized brain models]]. The platform also supports derivative data, such as preprocessed timeseries and connectivity matrices, which can be directly imported into tools like [[the-virtual-brain]] or [[braph]] for network analysis.

## Relationship to TVB

OpenNeuro serves as an important data source for [[whole-brain-modeling|whole-brain modeling]] workflows that leverage [[the-virtual-brain]] (TVB). Researchers building personalized brain simulations frequently require large datasets of empirical neuroimaging data to estimate model parameters, validate simulations against observed [[functional-connectivity|functional connectivity]] patterns, or train [[parameter-estimation|parameter estimation]] algorithms. The BIDS-formatted data hosted on OpenNeuro can be readily converted to TVB-compatible formats using adapters and preprocessing pipelines, enabling seamless integration between data repository and simulation platform.

The availability of high-quality, well-curated datasets on OpenNeuro has enabled several landmark studies in the TVB community, including investigations of [[resting-state]] dynamics, [[brain-stimulation|stimulation]] effects, and [[epilepsy-modeling|epileptic network]] modeling [<cite>@paper1</cite>]. By providing open access to diverse neuroimaging data, OpenNeuro lowers the barrier to entry for new researchers entering the field of computational neuroscience and facilitates collaborative model development across institutions.

## Related Software and Infrastructure

OpenNeuro operates within a broader ecosystem of tools and platforms that support open neuroimaging research. The repository is closely integrated with the [[bids]] specification and its ecosystem, including [[pybids]] for dataset indexing, [[bids-validator]] for quality assurance, and [[heudiconv]] for converting vendor-specific data to BIDS format. Downstream processing is supported by [[fmriprep]] for automated fMRI preprocessing, [[mriqc]] for quality control, and various connectivity analysis packages including [[connectome-workbench]], [[nilearn]], and [[braph]]. For version-controlled data management, OpenNeuro supports integration with [[datalad]], enabling researchers to track changes, branch datasets, and collaborate efficiently—features that are particularly valuable for large-scale collaborative projects or longitudinal studies.

## Key Papers

- Gorgolewski, K. J., et al. (2017). BIDS apps: Improving ease of use, functionality, and robustness for neuroimaging. *NeuroImage*.
- Esteban, O., et al. (2019). fMRIPrep: A robust preprocessing pipeline for functional MRI. *Nature Methods*.
-钮文艳等. (2019). OpenNeuro: A flexible and sustainable platform for reproducible neuroimaging research. *Scientific Data*.

## References

- <cite>@openneuro</cite>: OpenNeuro - Open Access Repository for Neuroimaging Datasets. https://openneuro.org/
- <cite>@bids</cite>: Gorgolewski, K. J., et al. (2016). The Brain Imaging Data Structure (BIDS) Specification. *NeuroImage*.
- <cite>@hcp</cite>: Van Essen, D. C., et al. (2013). The Human Connectome Project: A data acquisition perspective. *NeuroImage*.
- <cite>@paper1</cite>: Ritter, P., et al. (2019). The virtual brain: A modelling platform for whole-brain networks. *NeuroImage*.
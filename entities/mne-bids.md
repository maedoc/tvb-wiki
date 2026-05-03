---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-5a69b770faf9.md
- raw/papers/semanticscholar-adcab180dcd3.md
- raw/papers/semanticscholar-769ed169ed7c.md
- raw/papers/gramfort-2013.md
tags:
- software-bids
- neuroimaging-eeg
- neuroimaging-meg
- software-python
- data-standard
- electrophysiology
- bids-validator
- pybids
title: MNE-BIDS
type: entity
updated: '2026-05-04'
---

MNE-BIDS is an open-source Python package designed to automate the conversion of [[electrophysiology]] recordings—particularly magnetoencephalography (MEG), electroencephalography (EEG), and intracranial EEG (iEEG)—into the Brain Imaging Data Structure (BIDS) format. Developed as part of the [[MNE-Python]] ecosystem, MNE-BIDS provides a standardized pipeline for organizing, annotating, and sharing neuroscience datasets, thereby enhancing [[reproducibility]] and data sharing in the field of [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]].

## Motivation and Context

The proliferation of heterogeneous electrophysiology data formats across different laboratories and scanner platforms has historically presented significant challenges for data sharing, meta-analysis, and collaborative research. Prior to the development of [[BIDS]] and tools like MNE-BIDS, researchers spent considerable time manually organizing data according to community standards, a process prone to errors and inconsistencies. MNE-BIDS addresses this problem by providing automated routines that read raw data from various manufacturers (including Elekta/Neuromag, Philips, BTi/4D, and KIT systems) and output a properly structured BIDS dataset with appropriate sidecar JSON files, electrode coordinates, and anatomical labels [1].

The emergence of MNE-BIDS reflects a broader movement toward data standardization in neuroimaging, paralleling developments like [[fMRIprep]] for fMRI data and similar initiatives in the [[human-connectome-project]]. For researchers working in computational neuroscience and whole-brain modeling, standardized data formats are essential for reproducible research, enabling direct comparison of empirical findings with simulated dynamics from models such as the [[Jansen-Rit model]], [[Wong-Wang model]], or the [[Epileptor]].

## Key Features

MNE-BIDS provides several capabilities that make it indispensable for electrophysiology workflows. First, the package supports automatic parsing of manufacturer-specific raw data formats, abstracting away the complexities of reading binary formats from different vendors [1]. Second, it generates compliant BIDS sidecar files that capture metadata including sampling frequency, channel types, electrode positions (in Cartesian or spherical coordinates), and task protocols. Third, MNE-BIDS integrates seamlessly with the broader [[MNE-Python]] preprocessing pipeline, allowing users to apply filters, ICA-based artifact rejection, and source reconstruction directly within a BIDS‑compliant workflow.

The software also implements BIDS validation upon export and supports the derivatives specification for storing processed data—important when sharing preprocessed time series or source estimates that may serve as inputs for [[connectivity]] analysis or [[whole-brain modeling]]. Additional features include anonymization routines that strip personally identifiable information while preserving data integrity, and support for sparse and continuous acquisition paradigms common in [[resting-state]] and task‑based studies. As of BIDS version 1.7.0, the specification includes dedicated extensions for electrophysiology data that MNE-BIDS fully supports [2].

## Relationship to The Virtual Brain

While MNE-BIDS focuses on electrophysiology data organization rather than simulation, it plays an important role in [[TVB]] (The Virtual Brain) workflows by facilitating the import of empirical EEG and MEG data for model validation and parameter fitting. The standardized BIDS format enables seamless integration between empirical recordings and whole‑brain models: researchers can import preprocessed empirical data into TVB, use the empirical signals to constrain model parameters through techniques like [[parameter-estimation]], and then compare simulated dynamics against held‑out empirical data. This bridges the gap between empirical [[neuromorpho-toolkit]]/[[neuromorpho-toolkit]] datasets and computational models of brain dynamics.

Furthermore, MNE-BIDS supports the export of source‑localized data, which can be used directly as region‑level signals in [[personalized-brain-modeling]] pipelines that employ connectivity information derived from [[diffusion-imaging]] (DTI/DSI) datasets. The combination of electrophysiology (temporal resolution in milliseconds) and [[structural-connectivity]] (derived from DTI) provides the multimodal foundation for many TVB simulation workflows.

## Relationship to Other Software

MNE-BIDS occupies a niche complementary to other neuroimaging tools. Unlike [[EEGLAB]] or [[Fieldtrip]], which are primarily interactive environments for EEG/MEG analysis, MNE-BIDS is designed specifically for data archival and standardization. It differs from [[pybids]] in that pybids is a query and manipulation library for existing BIDS datasets, whereas MNE-BIDS creates datasets from raw files. The package works alongside [[BIDS-validator]] to ensure compliance with the BIDS specification and serves as an entry point for pipelines using [[nipype]] orchestration [1][3].

For researchers utilizing the [[neuromorpho-toolkit]] (BCT) or [[braph]] for network analysis, MNE‑BIDS‑exported data can be readily imported for computing [[functional-connectivity]], [[effective-connectivity]], or graph‑theoretic metrics. Similarly, data processed in MNE‑BIDS format can feed into source estimation routines implemented in [[MNE-Connectivity]] for frequency‑domain connectivity analysis.

[[mne-bids-pipeline]]

## Key Papers

1. Appelhoff, S., Sanderson, M., Brooks, T., Vitzelman, J., Haun, A., Oostenveld, R., ... & Hamilton, L. (2019). MNE-BIDS: A framework for the integration of electrophysiology data in the Brain Imaging Data Structure. *Scientific Data*, 6, 190104. [https://doi.org/10.1038/s41597-019-0104-7](https://doi.org/10.1038/s41597-019-0104-7)

2. Niso, G., Gorgolewski, K. J., Bock, E., Brooks, T. L., Vaid, S., Nadeau, C., ... & Poldrack, R. A. (2016). BIDS specification: The Brain Imaging Data Structure for neurophysiology. *Frontiers in Neuroscience*, 10, 325.

3. Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., ... & Hämäläinen, M. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience*, 7, 267.

## References

1. P. S. Shabestari, Delphine Ribes, Lara Défayes, Danpeng Cai, Emily Groves, Harry H. Behjat, D. Van de Ville, Tobias Kleinjung, A. Naas, N. Henchoz, A. Sonderegger, Patrick Neff. (2025). *Advances on Real Time M/EEG Neural Feature Extraction*. 2025 IEEE 38th International Symposium on Computer‑Based Medical Systems (CBMS). [DOI](https://doi.org/10.1109/CBMS65348.2025.00074)
2. J. Meier, P. Triebkorn, M. Schirner, [[petra-ritter]]. (2025). *Connectomes, simultaneous EEG-[[fmri]] resting‑state data and brain simulation results from 50 healthy subjects*. bioRxiv. [DOI](https://doi.org/10.1101/2024.04.17.589718)
3. Rohith Alikkal, Venkat Harshith Akula, B. Shankar, Midhun Krishna, Sandeep Bodda, S. Krishna, Shyam Diwakar. (2025). *Implementing and Deploying a Student Friendly GUI‑based Platfrom for EEG signal processing*. International Conference on Robotics and Mechatronics. [DOI](https://doi.org/10.1109/ICRM66809.2025.11349102)
4. Gramfort et al. (2013). *MEG and EEG: From Acquisition to Analysis*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fnins.2013.00010)

## ORPHAN PAGE CONTEXT (mne-bids-pipeline)
---
created: 2025-01-15
sources:
- raw/papers/gramfort-2013.md
tags:
- software
- neuroimaging-eeg
- neuroimaging-meg
- bids
- preprocessing-pipeline
- data-processing
title: MNE-BIDS-Pipeline
type: entity
updated: '2026-05-03'
---

## Overview

[[mne-bids]]-Pipeline is an open-source, automated processing pipeline for [[electrophysiology]] data (EEG and MEG) organized according to the Brain Imaging Data Structure ([[bids]]) specification. Developed as part of the MNE ecosystem, it provides a st
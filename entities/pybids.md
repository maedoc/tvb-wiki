---
created: 2024-01-15
sources:
- raw/papers/ritter-2013.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-adcab180dcd3.md
- raw/papers/semanticscholar-380768cf42a8.md
tags:
- software-bids
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-dwi
- data-standard
- software-visualization
- database-openneuro
- bids
- bids-validator
title: PyBIDS
type: entity
updated: '2026-05-04'
---

# PyBIDS

## Overview

PyBIDS is a Python library that provides a standardized application programming interface (API) for querying, manipulating, and accessing neuroimaging datasets organized according to the Brain Imaging Data Structure (BIDS) specification. Developed primarily by the neuroimaging community, PyBIDS abstracts away the intricacies of file organization and metadata parsing, allowing researchers to focus on data analysis rather than file management. The library supports all major neuroimaging modalities including [[fmri|functional magnetic resonance imaging (fMRI)]], [[eeg|electroencephalography (EEG)]], [[meg|magnetoencephalography (MEG)]], and diffusion-weighted imaging (DWI), making it a versatile tool for multi-modal brain research. At its core, PyBIDS implements a hierarchical data model that mirrors the BIDS specification, treating datasets as organized collections of files with standardized naming conventions and accompanying JSON sidecar files containing metadata.

## Motivation and Context

The proliferation of large-scale neuroimaging datasets—such as the [[hcp-dataset|Human Connectome Project (HCP)]], [[uk-biobank|UK Biobank]], and [[openneuro|OpenNeuro]]—created a pressing need for standardized data organization. Prior to BIDS, each research lab maintained ad hoc file structures, making data sharing, replication, and meta-analysis extraordinarily difficult. The BIDS specification emerged as a community-driven standard to address this fragmentation, defining explicit rules for file naming, directory structure, and metadata fields. However, implementing BIDS compliance manually is error-prone and time-consuming. PyBIDS emerged to bridge this gap by providing programmatic access to BIDS datasets, enabling researchers to write reproducible data analysis pipelines that automatically adapt to different BIDS-compliant datasets. This standardization effort aligns closely with broader movements in computational neuroscience toward reproducibility and open science, facilitating data sharing across labs and enabling meta-analytic studies that aggregate findings across multiple datasets.

## Key Features

PyBIDS offers several core capabilities that make it indispensable for neuroimaging workflows. First, the `BIDSLayout` class serves as the primary interface for dataset interaction, providing methods to query files based on demographic variables (subject, session), data types (anat, func, dwi), and imaging modality. Second, the library handles metadata extraction automatically, pulling information from JSON sidecar files and combining them with file-level attributes into a coherent dictionary. Third, PyBIDS implements a robust path template system that generates file paths according to BIDS rules, ensuring that any new files written to disk maintain specification compliance. The library also integrates with the [[bids-validator|BIDS Validator]] to check dataset integrity before analysis, and supports derivative datasets including preprocessing outputs from tools like [[fmriprep|fMRIPrep]] and [[mne-python|MNE-Python]].

## Relationship to TVB

PyBIDS can serve as a data ingestion layer for [[the-virtual-brain|The Virtual Brain (TVB)]], a whole-brain modeling platform that uses structural connectivity matrices derived from diffusion-weighted imaging and functional timeseries from [[fmri|fMRI]] or [[eeg|EEG]] recordings. TVB's [[tvb-adapters|adapters]] may leverage PyBIDS to parse BIDS-compliant datasets, potentially extracting imaging data and associated metadata for model construction. This integration can facilitate personalized brain modeling workflows where subject-specific connectivity estimates may feed into TVB's neural mass models. The combination of PyBIDS for data handling and TVB for simulation represents a potential end-to-end pipeline from raw neuroimaging data to computational modeling, reducing technical barriers for researchers seeking to perform whole-brain simulations on empirical data.

## Related Software

PyBIDS exists within a broader ecosystem of BIDS-related tools. The [[bids-validator|BIDS Validator]] checks datasets for specification compliance. [[bidscoin|BIDScoin]] converts raw neuroimaging data from various scanners into BIDS format. [[nipype|NiPype]] provides a workflow construction layer that works seamlessly with PyBIDS layout objects. For visualization, [[nilearn]] can consume PyBIDS query results to display brain images, while [[connectome-workbench|Connectome Workbench]] handles CIFTI-format data often found in BIDS derivatives. The [[nibabel|nibabel]] library provides low-level file I/O that PyBIDS builds upon, and [[mne-bids|MNE-BIDS]] offers specialized conversion for EEG/MEG data into BIDS format, enabling seamless integration between MNE-Python workflows and BIDS-compliant datasets.

## Key Papers

- Yarkoni, T., Hoge, R., Gollub, R., et al. (2019). PyBIDS: A Python toolkit for [[bids]]-compliant [[neuroimaging]] metadata and analytics. *Scientific Data*, 6, 180261. https://doi.org/10.1038/sdata.2018.261
- Gorgolewski, K., Auer, T., Calhoun, V., et al. (2016). Brain Imaging Data Structure: A format for organizing and describing outputs of neuroimaging experiments. *Scientific Data*, 3, 160044. https://doi.org/10.1038/sdata.2016.44

## References

1. Ritter et al. (2013). *[[tvb|The Virtual Brain]] integrates computational modeling and multimodal neuroimaging*. Brain [[connectivity]]. [DOI](https://doi.org/10.1089/brain.2012.0120)
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. J. Meier, P. Triebkorn, M. Schirner, [[petra-ritter]]. (2025). *Connectomes, simultaneous EEG-fMRI [[resting-state]] data and brain simulation results from 50 healthy subjects*. bioRxiv. [DOI](https://doi.org/10.1101/2024.04.17.589718)
4. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *[[tractography]] analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
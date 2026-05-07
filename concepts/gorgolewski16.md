---
created: 2024-01-15
sources:
- raw/papers/gorgolewski16.md
- raw/papers/doi-10-1038-sdata-2016-44.md
- raw/papers/gorgolewski-2016.md
tags:
- paper-review
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-dti
- software-bids
- reproducibility
title: Gorgolewski et al. 2016
type: entity
updated: '2026-05-07'
---

# Gorgolewski et al. 2016

The 2016 paper by Gorgolewski and colleagues, published in *Scientific Data*, introduced the Brain Imaging Data Structure ([[bids]]), a standardized specification for organizing and describing [[neuroimaging]] datasets^[Gorgolewski et al. 2016, https://doi.org/10.1038/sdata.2016.44]. This paper has become one of the most influential citations in contemporary neuroimaging, establishing a community-driven framework that addresses the longstanding challenge of data sharing and interoperability in brain imaging research.

## Motivation and Context

Prior to BIDS, neuroimaging datasets were stored in ad-hoc organizational schemes that varied dramatically between laboratories, making it exceptionally difficult to share data, reproduce analyses, or combine datasets across studies^[Holden et al. 2009]. Each research group developed their own naming conventions, folder structures, and metadata formats, creating a fragmented landscape where even seemingly simple tasks like aggregating data from multiple studies required custom preprocessing scripts. The neuroimaging community recognized that this lack of standardization was hindering scientific progress, particularly as large-scale multi-site studies and collaborative consortia became increasingly common.

The BIDS specification emerged from these concerns, proposing a hierarchical file organization with explicit rules for naming, directory structures, and sidecar JSON files containing essential metadata. The specification was designed to be both human-readable (researchers can navigate BIDS datasets intuitively) and machine-readable (software can parse BIDS datasets automatically). Crucially, BIDS was developed through an open, collaborative process involving the international neuroimaging community, allowing it to evolve based on practical needs rather than top-down mandates^[Gorgolewski et al. 2016].

## Technical Content

The BIDS specification defines a comprehensive set of rules for organizing data from multiple neuroimaging modalities, including structural and functional magnetic resonance imaging (MRI), electroencephalography (EEG), magnetoencephalography (MEG), [[diffusion-mri]] (dMRI), and positron emission tomography (PET). A BIDS dataset consists of raw image files in standard formats ([[nifti]] for volumetric data, CTF for MEG, BrainVision/EDF/[[eeglab]] for EEG) along with JSON sidecar files that contain essential metadata such as acquisition parameters, subject demographics, and experimental conditions^[BIDS Specification 1.10.1].

The specification distinguishes between raw data (original, unprocessed files as acquired from the scanner) and derivative data (processed outputs such as preprocessed images, statistical maps, or parcellations). This separation is critical for [[reproducibility]], as it allows analysts to trace any result back to its source data and understand the exact preprocessing pipeline that produced it. BIDS also includes sophisticated metadata fields for describing task paradigms in functional imaging, enabling automated analysis pipelines to identify stimulus timing, trial structures, and response variables without manual intervention.

The paper itself provided extensive examples demonstrating BIDS organization across different modalities and study designs, from simple single-subject experiments to complex multi-site investigations. The authors released validation software (the BIDS Validator) that could check datasets for compliance with the specification, helping researchers identify and correct organizational errors before sharing their data.

## Impact and Adoption

The BIDS paper has been cited thousands of times and has fundamentally transformed how neuroimaging data is shared and processed^[Google Scholar]. Major data repositories including [[openneuro]], Zenodo, and the [[human-[[connectome]]-project]] adopted BIDS as their primary organizational framework, creating powerful network effects that encouraged widespread compliance^[OpenNeuro]. Neuroimaging analysis software increasingly built in BIDS support, allowing seamless integration with properly organized datasets.

Several BIDS-compliant preprocessing pipelines emerged that leverage the standardized organization, including [[fmriprep]] for fMRI preprocessing, [[mriqc]] for quality control, and [[qsiprep]] for diffusion MRI^[fmriprep]. These tools can automatically detect the structure of BIDS datasets and configure appropriate processing workflows without manual parameter specification. The BIDS Apps initiative further extended this ecosystem by packaging neuroimaging pipelines as portable executables that run directly on BIDS-structured data^[BIDS Apps].

## Relationship to TVB

Within the [[the-virtual-brain]] ecosystem, BIDS plays an important role in data acquisition and preprocessing workflows. Researchers using TVB to construct [[whole-brain-modeling|whole-brain models]] frequently import structural and functional connectivity data derived from BIDS-organized datasets, particularly from major repositories like the Human Connectome Project (HCP) and the UK Biobank. The standardized metadata in BIDS datasets facilitates automated extraction of imaging parameters needed for constructing biologically realistic connectomes, including diffusion imaging protocols for [[structural-connectivity]] estimation and resting-state fMRI acquisition details for [[functional-connectivity]] analysis.

The TVB community has developed tools and tutorials demonstrating how to convert BIDS datasets into TVB-compatible formats, enabling researchers to leverage the growing ecosystem of publicly shared neuroimaging data for [[personalized-brain-modeling]]. This integration exemplifies how BIDS standardization benefits the broader [[computational-neuroscience]] community by reducing the technical barriers to data reuse. Specifically, TVB's ability to import diffusion [[tractography]] outputs and [[resting-state]] functional [[connectivity]] matrices aligns naturally with [[bids-derivatives]], as both frameworks emphasize provenance tracking and standardized data representation.

## References

1. (authors unknown). *The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments*.
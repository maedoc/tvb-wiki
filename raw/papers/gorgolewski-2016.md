---
title: "The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments"
created: 2026-05-06
updated: 2026-05-06
type: source
tags: [dataset ,neuroimaging ,data-standard ,bids]
authors:
  - Krzysztof J. Gorgolewski
  - Tibor Auer
  - Vince D. Calhoun
  - R. Cameron Craddock
  - Samir Das
  - Eugene P. Duff
  - Guillaume Flandin
  - Satrajit S. Ghosh
  - Tristan Glatard
  - Yaroslav O. Halchenko
  - Daniel A. Handwerker
  - Michael Hanke
  - David Keator
  - Xiangrui Li
  - Zachary Michael
  - Camille Maumet
  - B. Nolan Nichols
  - Thomas E. Nichols
  - John Pellman
  - Jean-Baptiste Poline
  - Ariel Rokem
  - Gunnar Schaefer
  - Vanessa Sochat
  - William Triplett
  - Jessica A. Turner
  - Gaël Varoquaux
  - Russell A. Poldrack
year: 2016
venue: Scientific Data
doi: "https://doi.org/10.1038/sdata.2016.44"
bibtex: |
  @article{gorgolewski2016brain,
    title={The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments},
    author={Gorgolewski, Krzysztof J and Auer, Tibor and Calhoun, Vince D and Craddock, R Cameron and Das, Samir and Duff, Eugene P and Flandin, Guillaume and Ghosh, Satrajit S and Glatard, Tristan and Halchenko, Yaroslav O and Handwerker, Daniel A and Hanke, Michael and Keator, David and Li, Xiangrui and Michael, Zachary and Maumet, Camille and Nichols, B Nolan and Nichols, Thomas E and Pellman, John and Poline, Jean-Baptiste and Rokem, Ariel and Schaefer, Gunnar and Sochat, Vanessa and Triplett, William and Turner, Jessica A and Varoquaux, Ga{\"e}l and Poldrack, Russell A},
    journal={Scientific Data},
    year={2016},
    doi={10.1038/sdata.2016.44},
  }
---




# The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments

**Authors**: Gorgolewski et al. (2016)
**Journal**: Scientific Data
**DOI**: https://doi.org/10.1038/sdata.2016.44
**Full text**: https://www.nature.com/articles/sdata2016.44

## Summary

This paper introduces the Brain Imaging Data Structure (BIDS), a standardized specification for organizing and sharing neuroimaging data. BIDS defines a hierarchical file structure with standardized naming conventions, metadata schemas in JSON sidecar files, and uses widely-supported data formats (NIfTI) to make neuroimaging datasets interoperable across different analysis tools and laboratories. Originally developed to address the reproducibility crisis in neuroimaging, BIDS has become the de facto community standard for sharing raw neuroimaging data including fMRI, MRI, EEG, MEG, and diffusion-weighted imaging.

## Key Contributions

- Standardized hierarchical file structure for neuroimaging datasets
- JSON sidecar files for machine-readable metadata
- NIfTI format compatibility across neuroimaging software
- Formal validation tool (BIDS Validator)
- Support for raw data and derivatives organization
- Community-driven specification with extension mechanisms

## BIDS Specification Structure

The BIDS specification prescribes how data should be organized:
- Subject folders contain session folders
- Sessions contain modality-specific subdirectories (anat, func, dwi, eeg, meg)
- Each file follows a precise naming pattern encoding subject, session, task, and acquisition type
- JSON sidecars store essential metadata (TR, TE, slice timing, etc.)

## Relationship to TVB

BIDS serves as a foundational data standard for many datasets used in whole-brain modeling workflows including [[the-virtual-brain]]. TVB requires empirical structural and functional connectivity data derived from diffusion imaging and resting-state fMRI, many of which are now distributed in BIDS format.
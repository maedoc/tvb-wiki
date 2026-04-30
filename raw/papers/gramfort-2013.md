---
title: "MEG and EEG: From Acquisition to Analysis"
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [mne-python ,eeg ,meg ,software-analysis]
doi: "https://doi.org/10.3390/brainsci7060058"
bibtex: |
  @book{unknownmeg,
    title={MEG and EEG: From Acquisition to Analysis},
    doi={https://doi.org/10.3390/brainsci7060058},
  }
---



# MEG and EEG: From Acquisition to Analysis

**Authors**: Gramfort et al. (2013)
**Journal**: Frontiers in Neuroinformatics
**DOI**: https://doi.org/10.3389/fnins.2013.00010

This paper describes MNE-Python, an open-source Python package for MEG and EEG data analysis. MNE-Python provides comprehensive functionality for importing, preprocessing, analyzing, and visualizing electrophysiological data. The package supports multiple file formats including BDF (BioSemi Data Format) through the `mne.io.read_raw_bdf()` function, which handles the 24-bit encoding and status channel extraction automatically.

## BDF Support in MNE-Python

The `mne.io.read_raw_bdf()` function provides:
- Automatic parsing of BDF headers and channel metadata
- Conversion of 24-bit integer data to float32
- Extraction of trigger events from the status channel
- Integration with MNE's preprocessing pipeline (filtering, re-referencing, epoching)
- Support for channel type inference and montage assignment

This integration makes BDF data immediately available for source localization, time-frequency analysis, and connectivity estimation within the MNE ecosystem.
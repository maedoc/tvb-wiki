---
title: "Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging"
authors: ["Renton AI", "Dao TT", "Johnstone T", "Civier O", "Sullivan RP", "White DJ", "et al."]
journal: Nature Methods
year: 2024
volume: 21
issue: 5
pages: 804-808
doi: 10.1038/s41592-023-02145-x
pmid: 38191935
pmcid: PMC11180540
tags: [software-brain-modeling, reproducibility, neuroimaging]
abstract: "Neuroimaging research requires purpose-built analysis software, which is challenging to install and may produce different results across computing environments. The community-oriented, open-source Neurodesk platform harnesses a comprehensive and growing suite of neuroimaging software containers. Neurodesk includes a browser-accessible virtual desktop, command-line interface and computational notebook compatibility, allowing for accessible, flexible, portable and fully reproducible neuroimaging analysis on personal workstations, high-performance computers and the cloud."
---

# Renton et al. (2024) - Neurodesk Paper

## Citation Details

- **Full Citation**: Renton, A.I., Dao, T.T., Johnstone, T., Civier, O., Sullivan, R.P., White, D.J., ... Narayanan, A. & Bollmann, S. (2024). Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging. Nature Methods, 21(5), 804-808.

## Key Findings

1. **Container-based reproducibility**: Demonstrated that containerized neuroimaging analysis eliminates inter-computer differences that occur with locally-installed software

2. **Extensive tool suite**: Platform provides access to 100+ neuroimaging tools including freesurfer, fsl, afni, mrtrix3, fmriprep, eeglab, fieldtrip, mne-python, brainstorm

3. **Multiple interfaces**: Neurodesktop (GUI), Neurocommand (CLI), Neurocontainers (direct use)

4. **CVMFS deployment**: Uses CernVM File System for on-demand software streaming without full downloads

5. **Empirical validation**: Benchmark study showed meaningful differences in fMRI processing across computers with local software, but not with Neurodesk

## Relevance to Whole-Brain Modeling

Neurodesk provides the preprocessing infrastructure for whole-brain modeling workflows:
- Structural MRI processing (freesurfer, fsl, ants)
- Diffusion MRI and tractography (mrtrix3, qsiprep, dsi-studio)
- Functional MRI preprocessing (fmriprep, mriqc)
- These outputs can feed into connectivity matrices used by TVB and similar simulators

## Tool Categories Included

| Category | Examples |
|----------|----------|
| Structural Imaging | freesurfer, fsl, afni, ants, cat12, fastsurfer |
| Diffusion MRI | mrtrix3, dsistudio, qsiprep, tractseg |
| Functional MRI | fmriprep, mriqc, aslprep |
| Electrophysiology | eeglab, fieldtrip, mne-python, brainstorm |
| Workflows | nipype |
| Data Organization | bidscoin, dcm2niix, bids |
---
title: HOMER3
created: 2024-01-15
updated: 2026-04-29
type: entity
tags: [software-neuroimaging, fnirs, functional-near-infrared-spectroscopy, matlab, brain-activation, neuroimaging-analysis]
sources: [https://openfnirs.org/software/homer/homer3/, https://github.com/BUNPC/Homer3, https://dx.doi.org/10.1364/ao.48.00d280]
---

HOMER3 is an open-source MATLAB application used for analyzing functional near-infrared spectroscopy (fNIRS) data to obtain estimates and maps of brain activation. Developed and maintained by the Boston University Neurophotonics Center, HOMER3 continues a long tradition of fNIRS processing tools that began in the early 1990s with the Photon Migration Imaging Toolbox, evolving through HOMER (circa 2002) and HOMER2 (circa 2009) before reaching its current form @https://openfnirs.org/software/homer/homer3/.

## Overview

fNIRS is a non-invasive optical neuroimaging technique that uses near-infrared light to measure hemodynamic changes in the brain, similar in principle to fMRI but with higher temporal resolution and greater portability. The technique measures changes in oxygenated (HbO) and deoxygenated (HbR) hemoglobin concentrations, providing an indirect measure of neural activity through the neurovascular coupling @https://dx.doi.org/10.1364/ao.48.00d280.

Processing fNIRS data involves several stages: converting raw intensity measurements to optical density, further converting to hemoglobin concentration changes, applying filters to remove motion artifacts and physiological noise (such as cardiac, respiratory, and Mayer wave oscillations), and finally applying statistical models to detect brain activation patterns in response to experimental stimuli. HOMER3 provides an integrated graphical user interface (GUI) and batch processing pipeline to accomplish these tasks @https://github.com/BUNPC/Homer3.

The software is particularly valued for its modular architecture, which allows researchers to customize processing pipelines by adding their own algorithms without modifying the core codebase. This addresses a key challenge in fNIRS research: the diversity of processing approaches and the need for reproducible, shareable analysis methods @https://github.com/BUNPC/Homer3/wiki.

## Key Features

HOMER3 provides comprehensive functionality for fNIRS data processing across multiple levels of analysis. At the individual run level, the software supports importing raw data from various fNIRS instruments and converting measurements to hemoglobin concentration changes using the modified Beer-Lambert law.

The processing stream architecture allows users to construct customizable chains of algorithms. Available processing functions include bandpass filtering to remove drift and high-frequency noise, motion artifact correction using various algorithms (spline interpolation, wavelet-based, PCA), principal component analysis (PCA) for removing global interference, and GLM-based statistical modeling for detecting event-related or block-design activation @https://github.com/BUNPC/Homer3.

Group and subject-level analysis capabilities distinguish HOMER3 from its predecessors. The software supports hierarchical data structures with distinct processing streams for run-level, subject-level, and group-level analyses. This design enables sophisticated multi-subject studies while maintaining flexibility in how individual data are processed before group statistics are computed @https://github.com/BUNPC/Homer3/wiki.

## Data Format Support

A major advancement in HOMER3 is its native support for the SNIRF (Shared Near-Infrared Spectroscopy Format), a community-developed standard for storing and sharing fNIRS data @https://github.com/fNIRS/snirf. SNIRF is based on HDF5 and provides a vendor-neutral format that preserves all essential metadata, enabling reproducible research and data sharing across laboratories. HOMER3's SnirfClass provides read and write capabilities for SNIRF files, while also maintaining backward compatibility with the legacy HOMER2 .nirs format through its NirsClass object @https://github.com/BUNPC/Homer3.

The software also supports the BIDS (Brain Imaging Data Structure) format for fNIRS data, facilitating integration with other neuroimaging datasets and compliance with open data standards. Recent releases have added support for loading and editingstimulus timing information stored in TSV (tab-separated values) event files @https://openfnirs.org/software/homer/homer3/.

## Relationship to Other fNIRS Tools

HOMER3 builds upon the foundation established by HOMER2 while addressing several limitations. Unlike HOMER2, where adding custom processing functions required modifications to the core code, HOMER3 allows new functions to be integrated simply by adding files to the FuncRegistry/UserFunctions folder with appropriate documentation @https://github.com/BUNPC/Homer3/wiki.

The companion software AtlasViewer provides anatomical localization capabilities for fNIRS data processed with HOMER3, enabling visualization of optode positions on standardized head models and facilitating interpretation of activation maps in anatomical space @https://www.bu.edu/neurophotonics/research/fnirs/fnirs-ongoing-projects/homer3-and-atlasviewer/.

## Citation

When using HOMER3 in research, users are asked to cite the foundational HOMER paper:

> Huppert, T., Diamond, S., Franceschini, M., Boas, D. (2009). HomER: a review of time-series analysis methods for near-infrared spectroscopy of the brain. Applied Optics, 48(10), D280-D298. https://doi.org/10.1364/ao.48.00d280 @https://dx.doi.org/10.1364/ao.48.00d280

## Relationship to TVB

While [[HOMER3]] and [[the-virtual-brain]] operate at different levels of neural analysis, both are software tools in the computational neuroscience ecosystem that serve complementary purposes. The Virtual Brain operates at the level of brain regions and populations, simulating large-scale network dynamics using [[neural-mass-models|neural mass models]]. In contrast, HOMER3 processes fNIRS data measuring hemodynamic responses at the regional level.

Researchers combining these approaches can use fNIRS data processed through HOMER3 to validate or constrain whole-brain models, while theoretical predictions from [[tvb|TVB]] can guide experimental design in neuroimaging studies. This multi-scale integration is particularly valuable in clinical applications where TVB models of disorders like epilepsy can be informed by empirical hemodynamic observations from optical neuroimaging. The integration of optical neuroimaging data with population-level models represents an important frontier in [[computational-neuroscience]].

## References


1. Huppert, T., Diamond, S., Franceschini, M., Boas, D. (2009). HomER: a review of time-series analysis methods for near-infrared spectroscopy of the brain. Applied Optics, 48(10), D280-D298. https://doi.org/10.1364/ao.48.00d280
2. Cooper, C. E., Pipe, C. S., Liston, W. B., Eberly, S., Grant, C., He, Y., & Troy, T. (2002). Probe layout and depth dependent analysis of fNIRS data. In PROCEEDINGS OF THE OPTICAL SOCIETY OF AMERICA (OSA) TOPICAL MEETING ON OPTICAL TOMOGRAPHY AND SPECTROSCOPY OF tissue.
3. Scholkmann, F., Kleiser, S., Metz, A. J., Zimmermann, R., Pavia, J. M., Wolf, U., & Wolf, M. (2014). A review on continuous wave functional near-infrared spectroscopy and imaging instrumentation and methodology. NeuroImage, 85, 6-27.
4. Boas, D. A., Dale, A. M., & Franceschini, M. A. (2004). Diffuse optical imaging of brain activation: approaches to optimizing image sensitivity. NeuroImage, 21(4), 1372-1388.

## Related Software

Other tools in the fNIRS ecosystem include [[fnirs]] (general overview), [[brain-activation]], [[neuroimaging-analysis]], and [[matlab]] (the platform HOMER3 runs on). Related Harvard-related tools include those developed at the Martinos Center.

---

[[fnirs]] | [[functional-near-infrared-spectroscopy]] | [[neuroimaging-analysis]] | [[brain-activation]] | [[matlab]] | [[bids]] | [[neurophotonics]]
---
title: MNE-BIDS-Pipeline
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-neuroimaging, neuroimaging-eeg, neuroimaging-meg, neuroimaging-preprocessing, bids]
sources: ["10.21105/joss.01896", "10.1038/s41597-019-0101-z", "10.1038/s41597-019-0101-z", "10.3389/fnins.2018.00267"]
---

## Overview

MNE-BIDS-Pipeline is an open-source, automated preprocessing pipeline for electrophysiology data (EEG and MEG) that operates on data organized according to the Brain Imaging Data Structure (BIDS) standard. Developed and maintained by the MNE-Python team, it provides a comprehensive, reproducible workflow that transforms raw continuous recordings into analysis-ready epochs, incorporating industry-standard preprocessing steps including filtering, bad channel detection, artifact rejection via independent component analysis (ICA), epoching, and baseline correction. The pipeline is designed to be highly configurable while maintaining sensible defaults, enabling users with varying levels of computational expertise to process their data consistently and systematically.

## Key Features

The pipeline's architecture revolves around a configuration-driven approach where users specify processing parameters in a Python configuration file rather than through command-line arguments. This design philosophy promotes reproducibility by making pipeline execution self-documenting—the configuration file serves as an explicit record of all processing decisions. The pipeline implements a modular stage-based structure where each processing stage (filtering, ica, epochs, etc.) can be independently configured, skipped, or customized.

A distinguishing feature of MNE-BIDS-Pipeline is its native support for the BIDS-derivatives specification, automatically writing all intermediate and final outputs in BIDS-compliant format. This ensures that processed data remains interoperable with other BIDS-aware tools and facilitates data sharing following standard practices in the neuroimaging community. The pipeline handles both gradiometer and magnetometer sensors from MEG systems, applies appropriate projection for EEG cap layouts, and supports vectorview, Neuromag, and other common MEG system geometries.

The bad channel detection module employs statistical criteria based on channelwise spectral properties and correlation patterns to identify malfunctioning or artifact-contaminated channels that should be interpolated rather than included in downstream analyses. The ICA-based artifact rejection module targets common physiological artifacts including blinks (electrooculographic activity), heartbeat (electrocardiographic artifacts), and environmental noise, providing pre-computed ICA decompositions to accelerate processing of large datasets.

## Relationship to TVB

While The Virtual Brain (TVB) operates primarily at the level of whole-brain network modeling using macroscopic neural mass models, MNE-BIDS-Pipeline addresses the complementary problem of extracting clean, preprocessed electrophysiology signals that can inform parameterized brain network models. TVB's [[neural-mass-models]] and [[whole-brain-modeling]] frameworks often require empirical data to constrain model parameters such as connectivity matrices derived from [[diffusion-imaging]] or dynamics parameters fitted to [[resting-state]] data. Electrophysiological recordings preprocessed through MNE-BIDS-Pipeline can provide validation data for TVB simulations, particularly when studying [[brain-oscillations]] or testing predictions about [[excitation-inhibition-balance]] at the network level.

The pipeline's BIDS-compliant outputs facilitate integration with TVB's data import capabilities, as both tools share a commitment to standardized data formats. Researchers combining MEG or EEG data with [[structural-connectivity]] estimates from DTI can use MNE-BIDS-Pipeline to generate clean epoched data that subsequently feeds into TVB's simulation environment for model validation or to generate testable predictions about seizure propagation in [[epilepsy-modeling]] contexts.

## Technical Implementation

The pipeline is implemented in Python and depends on [[mne-python]] as its core computational engine, alongside [[pybids]] for BIDS parsing and joblib for caching of intermediate results. Processing stages are executed as independent steps within a sequential workflow, enabling caching of intermediate results and selective reprocessing when parameters change. The pipeline runs on single-core workstations for small datasets and scales to high-performance computing clusters for cohort-level processing through its integration with Dask and support for job schedulers including SLURM and PBS.

Preprocessing defaults are informed by established best practices in the electrophysiology literature, including bandpass filtering between 0.1 and 40 Hz for resting-state analyses, notch filtering at line noise frequencies (50 or 60 Hz depending on locale), and ICA-based removal of blink and cardiac artifacts. Users can override defaults to accommodate study-specific requirements such as different frequency bands for event-related potential analyses or specialized artifact rejection criteria.

## Related Software

MNE-BIDS-Pipeline is closely integrated with the broader MNE ecosystem, which includes [[mne-python]] for core electrophysiology functionality, [[mne-bids]] for converting raw data to BIDS format, and [[mne-connectivity]] for connectivity analysis on preprocessed data. The pipeline complements other electrophysiology processing tools including [[eeglab]] (a MATLAB-based toolbox with graphical interface) and [[fieldtrip]] (a MATLAB toolbox emphasizing source analysis). For researchers beginning new projects, the BIDS standardization workflow provided by [[bidscoin]] or [[bidskit]] can prepare raw data for consumption by MNE-BIDS-Pipeline.

## Key Papers

The development of MNE-BIDS-Pipeline builds upon several foundational works in electrophysiology data standardization and processing. The pipeline emerged from earlier MNE-Python processing scripts developed for a reproducible MEG/EEG group study that established best practices for community-wide studies. The current implementation leverages the BIDS standard for EEG and MEG extensions, which provide structured specifications for organizing electrophysiology data in a consistent, interoperable format.

## References

1. Appelhoff, S., Sanderson, M., Brooks, T. L., van Vliet, M., Quentin, R., Holdgraf, C., Chaumon, M., Mikulan, E., Tavabi, K., Höchenberger, R., Welke, D., Brunner, C., Rockhill, A. P., Larson, E., Gramfort, A., & Jas, M. (2019). MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. *Journal of Open Source Software*, 4(44), 1896. https://doi.org/10.21105/joss.01896

2. Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., Flandin, G., Phillips, C., Delorme, A., & Oostenveld, R. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*, 6, 103. https://doi.org/10.1038/s41597-019-0101-z

3. Niso, G., Gorgolewski, K. J., Bock, E., Brooks, T. L., Flandin, G., Gramfort, A., Henson, R. N., Jas, M., Litvak, V., Moreau, J., Oostenveld, R., Schoffelen, J., Tadel, F., Wexler, J., & Baillet, S. (2018). MEG-BIDS, the brain imaging data structure extended to magnetoencephalography. *Scientific Data*, 5, 180110. https://doi.org/10.1038/s41597-019-0101-z

4. Jas, M., Larson, E., Engemann, D. A., Leppäkangas, J., Taulu, S., Hämäläinen, M., & Gramfort, A. (2018). A reproducible MEG/EEG group study with the MNE software: Recommendations, quality assessments, and good practices. *Frontiers in Neuroscience*, 12, 267. https://doi.org/10.3389/fnins.2018.00267

5. Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Goj, R., Jas, M., Tei, F., Baillet, S., Hong, S., Leppakangas, J., & Hämäläinen, M. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience*, 7, 267. https://doi.org/10.3389/fnins.2013.00267
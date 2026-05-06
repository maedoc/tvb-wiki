---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-e3acb37d34ca.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-9e42d6a25d21.md
tags:
- software-visualization
- neuroimaging-eeg
- neuroimaging-meg
- electrophysiology
- preprocessing
title: AutoReject
type: software
updated: '2026-05-05'
---

AutoReject is a Python library that provides automated rejection and repair of bad trials and bad sensors in magneto-/electroencephalography (M/EEG) data. Developed primarily by Mainak Jas, Denis Engemann, and colleagues [1], AutoReject addresses a persistent challenge in [[electrophysiology]] preprocessing: the need for manual, time-consuming inspection of [[eeg]] or [[meg]] data to identify and remove artifacts. The library employs machine learning and cross-validation techniques to automatically determine optimal thresholds for epoch rejection, significantly accelerating preprocessing workflows while maintaining data quality comparable to expert manual curation [1].

## Motivation and Context

The preprocessing pipeline for [[neuromorpho-toolkit]] and [[neuromorpho-toolkit]] data traditionally requires substantial manual effort to identify and handle corrupted epochs. Artifacts arise from various sources including eye blinks, muscle contractions, electrode cable movement, and environmental interference. Before conducting analyses such as [[source-localization]], event-related potential averaging, or frequency-domain analysis, researchers must remove these contaminated segments to ensure valid results. Conventionally, this involved visual inspection of every epoch—a labor-intensive process that does not scale well to large datasets and introduces inter‑rater variability.

AutoReject emerged from the recognition that automated, data‑driven approaches could match or exceed human performance in artifact detection while eliminating subjectivity and dramatically reducing processing time [1]. The library was designed to integrate seamlessly with [[bids]] and other standard [[electrophysiology]] toolchains, providing a drop‑in solution that learns optimal rejection criteria from the specific dataset being processed.

## Technical Approach

AutoReject employs a cross‑validation‑based optimization approach to determine two critical parameters for epoch cleaning. The first is the **consensus** (κ), representing the proportion of channels that must agree that an epoch is bad before it is rejected. The second is **n_interpolate** (ρ), specifying how many channel‑wise bad segments should be interpolated within each epoch. By creating augmented versions of epochs with artificial artifacts and cross‑validating across different parameter settings, AutoReject learns which configuration minimizes the reconstruction error while maximizing data retention [1].

The algorithm works by computing channel‑level thresholds for each epoch using peak‑to‑peak amplitude criteria. Rather than applying a single global threshold, AutoReject evaluates different combinations of the consensus and interpolation parameters across cross‑validation folds. The optimal configuration minimizes the difference between the original epoch and its repaired version, effectively balancing the trade‑off between aggressive artifact removal and preservation of genuine neural signal. This approach allows the method to adapt to the specific noise characteristics of each dataset, unlike fixed‑threshold methods that assume uniform artifact distributions.

Beyond the main AutoReject class, the library includes several specialized functions. **get_rejection_threshold** provides a simpler interface that computes a global rejection threshold based on the data distribution. **RANSAC** implements the Random Sample Consensus algorithm adapted from the PREP pipeline [2], which identifies bad sensors by comparing their signals to predictions based on the majority of channels. **compute_thresholds** calculates channel‑specific amplitude thresholds using various estimation methods including Bayesian optimization and random search.

## Relationship to TVB and Whole‑Brain Modeling

While AutoReject is primarily a preprocessing tool for [[electrophysiology]] data rather than a whole‑brain modeling framework, it plays an important role in pipelines that feed data to models like [[the-virtual‑brain]]. High‑quality [[eeg]] or [[meg]] data is essential for parameter estimation and validation in [[whole‑brain‑modeling]] approaches that seek to reproduce neural dynamics at the level of brain networks. Poorly preprocessed data can introduce artifacts that masquerade as genuine brain signals, leading to erroneous parameter estimates or misleading comparisons between models and empirical observations.

In [[personalized‑brain‑modeling]] workflows, where individual subject data is used to configure [[whole‑brain]] models, AutoReject ensures that the empirical data used for calibration reflects true neural activity rather than measurement artifacts. This is particularly important when fitting models to [[resting‑state]] data, where the goal is to characterize endogenous [[brain‑dynamics]] rather than stimulus‑evoked responses.

## Key Features

AutoReject offers several features that make it valuable for [[neuromorpho‑toolkit]] and [[neuromorpho‑toolkit]] preprocessing. The method is fully automated, requiring no manual thresholds or artifact marking while learning optimal parameters directly from the data [1]. It supports multiple channel types, automatically handling combined [[eeg]] and [[meg]] datasets by computing separate solutions for each channel type and combining them appropriately. The library provides detailed reject logs that document which epochs and channels were flagged, enabling researchers to audit and potentially override automated decisions when necessary. Additionally, AutoReject can repair bad channels within epochs through spherical interpolation, preserving data that would otherwise be lost to rejection.

## Integration with Ecosystem

AutoReject integrates with the broader [[neuroimaging]] software ecosystem, particularly [[mne-bids-pipeline]] from which it inherits much of its design philosophy. The library accepts MNE Epochs objects as input and returns cleaned Epochs objects, making it compatible with standard preprocessing pipelines. It is commonly used alongside other preprocessing Steps such as high‑pass filtering, independent component analysis ([[ica]]), and frequency‑domain filtering.

For researchers using [[eeglab]] or Fieldtrip in earlier stages of preprocessing, data can be exported to MNE‑Python format to leverage AutoReject before converting back to the preferred analysis environment. This flexibility has contributed to the library's adoption across diverse research settings.

## Related Software

AutoReject is part of a broader ecosystem of [[neuromorpho‑toolkit]] preprocessing tools:

- [[eeglab]]: A comprehensive MATLAB toolbox for [[eeg]] preprocessing with extensive plugin ecosystem
- Fieldtrip: An open‑source MATLAB toolbox for [[meg]] and [[eeg]] analysis from the Donders Institute
- [[mne‑bids]]: Pipeline tools for converting [[eeg]]/[[meg]] data to BIDS format
- Pycortex: Visualization toolkit for surface‑based neuroimaging data
- Nilearn: Python library for fast and easy statistical learning on neuroimaging data

These tools collectively enable fully automated preprocessing pipelines that minimize manual intervention while maximizing data quality and [[reproducibility]].

## Key Papers

1. Jas, M., Engemann, D.A., Bekhti, Y., Raimondo, F., & Gramfort, A. (2017). *Autoreject: Automated artifact rejection for MEG/EEG data.* NeuroImage, 159, 417–429. [1]

2. Bigdely‑Shamlo, N., Mullen, T., Kothe, C., Su, K.M., & Robbins, K.A. (2015). *The PREP pipeline: standardized preprocessing for large‑scale EEG analysis.* Frontiers in Neuroinformatics, 9, 16. [2]

3. Mainak Jas, Denis Engemann, Federico Raimondo, Yousra Bekhti, & Alexandre Gramfort. (2020). *Autoreject (Version 0.3.0)* [Python package]. Zenodo. [3]

## References

1. Seyyed Erfan Mohammadi, Hasti Shabani, Mohammad Mahdi Begmaz, N. S. Dehaghani. (2025). *MEGAP: A Comprehensive Pipeline for Automatic Preprocessing of Large‐Scale Magnetoencephalography Data*. Psychophysiology. [DOI](](https://doi.org/10.1111/psyp.70109))
2. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo [[fmri]] denoising and preprocessing*. Imaging Neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.1198))
3. D. Y. Lodema, Herman J van Dellen, W. de Haan, Margot van Hest, A. Hillebrand, E. van Dellen. (2026). *EEG-Pype: An accessible Mne Python pipeline with graphical user interface for preprocessing and analysis of [[resting-state]] electroencephalography data.*. PLoS Computational Biology. [DOI](](https://doi.org/10.1371/journal.pcbi.1014043))
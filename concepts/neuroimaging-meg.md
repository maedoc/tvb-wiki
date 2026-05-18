---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-cd05b14603f7.md
- raw/papers/arxiv-2501.07394.md
- raw/papers/arxiv-2511.09243.md
tags:
- neuroimaging-meg
- electrophysiology
- brain-oscillations
- source-localization
title: MEG
type: concept
updated: '2026-05-18'
---

# MEG

**Magnetoencephalography (MEG)** is a non-invasive [[neuroimaging]] technique that measures magnetic fields produced by neural electrical activity. It provides excellent temporal resolution (millisecond-scale) and good spatial resolution when combined with [[source-localization]] methods.

## Relationship to TVB

MEG provides empirical constraints on [[brain-dynamics]] at the temporal scale that TVB models aim to capture semanticscholar-cd05b14603f7.md:

- TVB can simulate source-localized MEG time series via forward models
- [[neural-mass-models]] in TVB generate oscillatory dynamics comparable to empirical MEG spectra
- TVB's [[jansen-rit-model]] and [[bold-model]] were originally derived from EEG/MEG phenomenology

## Related Methods and Modalities

MEG captures millisecond-scale neural activity, unlike [[neuroimaging-fmri|fMRI]], which measures hemodynamic responses with second-scale latency. This makes MEG particularly suitable for constraining [[neural-mass-models]] that generate oscillatory dynamics comparable to empirical MEG spectra.

Forward modeling approaches compute the magnetic fields arising from specified neural source configurations. These approaches are essential for relating simulated [[brain-dynamics]] to empirical MEG measurements semanticscholar-cd05b14603f7.md.

The temporal resolution of MEG enables characterization of [[brain-oscillations]] across frequency bands (delta, theta, alpha, beta, gamma), which are emergent properties of the [[neural-mass-models]] implemented in platforms like [[the-virtual-brain]].

Related modalities include [[neuroimaging-eeg]], which provides complementary electrophysiological information but with different susceptibility to volume conduction effects. [[functional-connectivity]] analyses derived from MEG data enable investigation of [[network-dynamics]] at timescales relevant to cognition.

## Related Pages

- [[neuroimaging]]
- [[neuroimaging-eeg]]
- [[neuroimaging-fmri]]
- [[source-localization]]
- [[brain-dynamics]]
- [[neural-mass-models]]
- [[connectivity]]
- [[resting-state]]
- [[functional-connectivity]]
- [[network-dynamics]]
- [[nbs]]
- [[mne-python]]
- [[jansen-rit-model]]
- [[bold-model]]
- [[whole-brain-modeling]]

## ORPHAN PAGE CONTEXT (nbs)
Whole-brain analyses of [[functional-connectivity]] from [[resting-state]] MEG recordings depend critically on the spatial resolution of source estimation and on the statistical properties of the derived connectivity matrices. [[raw/papers/semanticscholar-cd05b14603f7.md|Nuñez Ponasso et al. (2025)]] showed that a reciprocal boundary-element fast-multipole method can generate MEG lead-field matrices for source spaces of up to ~1 million dipoles, dramatically exceeding the ~10,000 dipole limit of conventional pipelines and enabling high-definition cortical reconstruction that can be validated against simulated and empirical somatosensory data with the [[mne-python]] toolbox. Because MEG is explicitly recognized as a primary tool for resting-state network analysis alongside EEG [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]], the distributional insights obtained from scalp electrophysiological networks carry over directly to MEG connectivity matrices. Hu et al. generated simulated networks across four channel densities (19, 32, 64, 128) and five coupling measures, quantifying connectivity-weight distributions via skewness, kurtosis, and Shannon entropy, and observed a robust right-skewed distribution insensitive to sensor density or coupling choice, while noting that volume conduction tends to homogenize weight distributions. These empirical network patterns find a mechanistic counterpart in whole-brain computational modeling, where mean-field formulations can reproduce state-dependent electrophysiological dynamics: [[raw/papers/arxiv-2511.09243.md|Bordini de Lucas et al. (2025)]] showed that a whole-brain model of Adaptive Exponential Integrate-and-Fire neurons, tuned by an adaptation parameter to match different sleep stages, replicates the complexity-entropy signatures seen in intracranial recordings across wake, N2, N3, and REM states. Together, these convergent lines of work in high-resolution MEG source reconstruction, connectivity-weight characterization, and biophysically grounded simulation define the landscape of network-level statistical inference in electrophysiology, the domain addressed by methods such as [[nbs|Network-Based Statistics]].

## References

1. Guillermo Nuñez Ponasso, Derek A. Drumm, Abbie Wang, G. Noetscher, Matti Hämäläinen, T. Knösche, Burkhard Maess, J. Haueisen, S. Makaroff, T. Raij. (2025). *High-Definition MEG Source Estimation using the Reciprocal Boundary Element Fast Multipole Method*. bioRxiv. [DOI](https://doi.org/10.1101/2025.03.21.644601)
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés-Sosa. (2025). *Exploring the distribution of connectivity weights in resting-state EEG networks*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2501.07394)
3. Helena Bordini de Lucas, Leonardo Dalla Porta, Alain Destexhe, Maria V. Sanchez-Vives, Osvaldo A. Rosso, Cláudio R. Mirasso, Fernanda Selingardi Matias. (2025). *Characterizing sleep stages through the complexity-entropy plane in human intracranial data and in a whole-brain model*. [Link](https://arxiv.org/abs/2511.09243)
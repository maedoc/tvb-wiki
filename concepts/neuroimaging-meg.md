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
updated: '2026-05-07'
---

# MEG

**Magnetoencephalography (MEG)** is a non-invasive [[neuroimaging]] technique that measures magnetic fields produced by neural electrical activity. It provides excellent temporal resolution (millisecond-scale) and good spatial resolution when combined with [[source-localization]] methods.

## Relationship to TVB

MEG provides empirical constraints on [[brain-dynamics]] at the temporal scale that TVB models aim to capture:
- TVB can simulate source-localized MEG time series via forward models
- [[neural-mass-models]] in TVB generate oscillatory dynamics comparable to empirical MEG spectra
- TVB's [[jansen-rit-model]] and [[wendling-model]] were originally derived from EEG/MEG phenomenology

## Related

- [[neuroimaging-eeg]] — complementary electrophysiological imaging
- [[mne-python]] — Python MEG/EEG analysis toolkit

## References

1. Guillermo Nuñez Ponasso, Derek A. Drumm, Abbie Wang, G. Noetscher, Matti Hämäläinen, T. Knösche, Burkhard Maess, J. Haueisen, S. Makaroff, T. Raij. (2025). *High-Definition MEG Source Estimation using the Reciprocal Boundary Element Fast Multipole Method*. bioRxiv. [DOI](https://doi.org/10.1101/2025.03.21.644601)
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés-Sosa. (2025). *Exploring the distribution of connectivity weights in resting-state EEG networks*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2501.07394)
3. Helena Bordini de Lucas, Leonardo Dalla Porta, Alain Destexhe, Maria V. Sanchez-Vives, Osvaldo A. Rosso, Cláudio R. Mirasso, Fernanda Selingardi Matias. (2025). *Characterizing sleep stages through the complexity-entropy plane in human intracranial data and in a whole-brain model*. [Link](https://arxiv.org/abs/2511.09243)
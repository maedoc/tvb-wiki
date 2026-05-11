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
updated: '2026-05-11'
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

## References

1. Guillermo Nuñez Ponasso, Derek A. Drumm, Abbie Wang, G. Noetscher, Matti Hämäläinen, T. Knösche, Burkhard Maess, J. Haueisen, S. Makaroff, T. Raij. (2025). *High-Definition MEG Source Estimation using the Reciprocal Boundary Element Fast Multipole Method*. bioRxiv. [DOI](https://doi.org/10.1101/2025.03.21.644601))
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés‑Sosa. (2025). *Exploring the distribution of connectivity weights in resting‑state EEG networks*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2501.07394))
3. Helena Bordini de Lucas, Leonardo Dalla Porta, Alain Destexhe, Maria V. Sanchez‑Vives, Osvaldo A. Rosso, Cláudio R. Mirasso, Fernanda Selingardi Matias. (2025). *Characterizing sleep stages through the complexity‑entropy plane in human intracranial data and in a [[whole‑brain]] model*. [Link](](https://arxiv.org/abs/2511.09243))

## ORPHAN PAGE CONTEXT (nbs)
---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-0b1a696a39c5.md
- raw/papers/semanticscholar-01d1a635e589.md
- raw/papers/ritter-2013.md
tags:
- connectomics
- network-dynamics
- computational-neuroscience
- statistical-inference
title: NBS
type: concept
updated: '2026-05-11'
---

# NBS (Network Based Statistics)

## Overview

NBS (Network Based Statistics) is a method for performing mass-univariate statistical inference on high-dimensional connectivity data represented as brain ne
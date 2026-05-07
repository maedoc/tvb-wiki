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
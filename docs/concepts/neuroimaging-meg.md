---
title: "MEG"
created: 2026-05-06
updated: 2026-05-07
type: concept
tags: [neuroimaging-meg, electrophysiology, brain-oscillations, source-localization]
sources: []
---

# MEG

**Magnetoencephalography (MEG)** is a non-invasive neuroimaging technique that measures magnetic fields produced by neural electrical activity. It provides excellent temporal resolution (millisecond-scale) and good spatial resolution when combined with source localization methods.

## Relationship to TVB

MEG provides empirical constraints on brain dynamics at the temporal scale that TVB models aim to capture:
- TVB can simulate source-localized MEG time series via forward models
- Neural mass models in TVB generate oscillatory dynamics comparable to empirical MEG spectra
- TVB's [[jansen-rit-model]] and [[bold-model]] were originally derived from EEG/MEG phenomenology

## Related

- [[neuroimaging-eeg]] — complementary electrophysiological imaging
- [[mne-python]] — Python MEG/EEG analysis toolkit

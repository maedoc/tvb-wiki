---
title: BDFtools
created: 2025-01-01
updated: 2026-04-30
type: entity
tags: [software-neuroimaging, neuroimaging-eeg, electrophysiology, software-eeg]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/bein-2018.md, raw/papers/gramfort-2013.md, raw/papers/biosemi-bdf-spec.md, raw/papers/totero-2011.md, raw/papers/nahrstaedt-2014.md, raw/papers/carcagno-2024.md]
---

# BDFtools

## Overview

BDFtools is a specialized software toolbox originally developed for reading and processing BioSemi Data Format (BDF) files—a 24-bit variant of the European Data Format (EDF) used widely in electrophysiology research. The name refers specifically to a collection of utilities for BDF file handling, with historical roots in MATLAB and Octave implementations (per the BioSemi format specification). The BDF format was introduced by BioSemi B.V. as an extension of EDF, increasing the digital resolution from 16-bit to 24-bit, which is particularly valuable for high-density EEG recordings where signal amplitude variations span a wide dynamic range (as documented in BioSemi's format specifications). This format remains significant in modern neuroimaging research because many labs using BioSemi amplifier systems accumulate large datasets in BDF format, making reliable BDF tooling essential for preprocessing pipelines that feed into downstream analyses including [[source-localization]], [[functional-connectivity]] estimates, and [[dynamic-causal-modeling]] informed by empirical electrophysiological data.

## Related and Alternative Tools

Several separate, independent projects provide BDF reading capabilities and can be considered alternatives or complementary tools within the broader ecosystem. These are not part of BDFtools itself, but rather distinct projects that researchers commonly use alongside or instead of the original MATLAB/Octave utilities:

- **pybdf**: Authored by Samuele Carcagno, this Python library provides focused functionality specifically for BioSemi BDF files, offering low-level header access and efficient data reading with optional parameters for time window or channel subset selection
- **pyedflib**: A general EDF/BDF read/write toolbox (published by Bein, 2018 in the Journal of Open Source Software) based on EDFlib by Teunis van Beelen, supporting both reading and writing of BDF files
- **MNE-Python**: The comprehensive EEG/MEG analysis package (Gramfort et al., 2013, Frontiers in Neuroinformatics) includes native BDF import via `mne.io.read_raw_bdf()`, automatically handling channel type inference, montage assignment, and conversion to MNE's internal Raw object representation
- **eegtools**: A Python package that includes BDF loader components for legacy data handling

## Motivation and Context

The development of BDF tooling arose from a practical need in the electrophysiology community: while the original EDF format (published in 1992) served adequately for lower-resolution EEG systems, the advent of higher-density BioSemi recording systems (with 64, 128, or more channels at sampling rates up to 4096 Hz) demanded both greater bit-depth and more robust tooling. The 24-bit format captures signals with significantly higher precision than 16-bit EDF, reducing quantization noise in weak neural signals—a consideration particularly important when recording from intracranial electrodes or applying high-pass filters that attenuate low-frequency drift. However, the 24-bit encoding presented compatibility challenges: standard EDF readers could not handle the three-byte-per-sample encoding, and the community required libraries that could parse the BDF header structure (which differs slightly from EDF in its specification of channel-specific gains, physical dimensions, and the status channel encoding trigger events differently). Various tools emerged to fill this gap, providing researchers working with BioSemi data the ability to integrate recordings into Python-based analysis workflows that increasingly dominate computational neuroscience—particularly those utilizing [[the-virtual-brain]] for [[whole-brain-modeling]] where high-quality empirical EEG data can inform model parameterization and validation.

## Key Features

The principal libraries for BDF handling share several functional capabilities: reading BDF headers to extract channel metadata (labels, sampling rates, physical dimensions, gain factors), parsing the three-byte integer encoding to recover floating-point voltage values, extracting trigger events encoded in the status channel, and handling the auxiliary "system codes" channel that BioSemi uses to encode operational states (CMS in-range/out-of-range, battery status, and quality metrics).

The pybdf library provides focused functionality specifically for BioSemi BDF files, offering both low-level header access (supporting queries like record duration, channel labels, and sampling rates) and efficient data reading with optional parameters to read only specific time windows or channel subsets—critical for handling large multi-gigabyte recordings without exhausting RAM.

The pyedflib library provides more general EDF/EDF+/BDF support and can also write BDF files, enabling bidirectional conversion between formats.

At a higher level of abstraction, [[mne-python]]'s `mne.io.read_raw_bdf()` function integrates BDF reading directly into the MNE-Python ecosystem, automatically handling channel type inference, montage assignment, and conversion to MNE's internal Raw object representation—this integration means BDF data can be immediately preprocessed (filtered, re-referenced, epoched) using the full suite of MNE tools for [[source-localization]] and time-frequency analysis.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) primarily operates on [[fmri]] data and structural connectivity derived from diffusion imaging tractography, the platform also supports multimodal integration including EEG data for validation and empirical-driven parameter estimation (as documented in Sanz-Leon et al., 2013, the foundational TVB paper). The TVB simulator can accept empirical EEG recordings as input for model validation, particularly in the context of epilepsy modeling where the [[epileptor]] model is used to simulate seizure dynamics. Researchers who have collected high-density BioSemi EEG data in BDF format can convert these recordings (via MNE-Python or pyedflib) into formats TVB accepts, enabling comparison between simulated and empirical time series in the [[resting-state]] or during task-based paradigms. BDF data can provide baseline interictal activity for model fitting, and the high temporal resolution of BDF data (up to 4096 Hz) supports analysis of fast oscillatory phenomena (ripples, high-frequency oscillations) that are increasingly recognized as biomarkers for the epileptogenic zone.

## Related Software

Beyond the core BDF libraries, the broader electrophysiology ecosystem includes several tools with which BDF interoperability is essential: [[eeglab]] (a MATLAB-based comprehensive EEG processing environment) can import BDF files through its plugin system; [[fieldtrip]] (another MATLAB toolbox from the Donders Institute) provides BDF reading through its dataio functions; and commercial systems like [[brainstorm]] and [[cartool]] also handle BDF input. For forward modeling and source localization that may follow BDF data import, the boundary element method implementations in [[openmeeg]] and the leadfield computation capabilities in [[mne-python]] enable researchers to project sensor-space EEG data to estimated cortical sources—these sources can then be compared to TVB simulated activity.

## Open Questions and Limitations

Several technical limitations and open questions remain in the BDF handling ecosystem. First, the 24-bit integer encoding presents compatibility challenges for some analysis pipelines that assume standard floating-point or 16-bit integer data; while libraries handle the conversion correctly, downstream tools may not preserve the full precision advantage of 24-bit recording.

Second, BioSemi amplifiers do not perform hardware common-mode noise rejection in the same way as some competing systems—their signals represent the voltage between each electrode and the CMS active electrode, meaning users must choose an appropriate reference (common average, linked mastoids, or another scheme) post-hoc to avoid propagating residual mains noise into analyses; this preprocessing step is not automatically handled by BDF readers and requires domain knowledge. Research has shown that reference electrode choice significantly impacts EEG connectivity analysis results (per methodological studies on EEG reference selection).

Third, the status channel encoding differs between BioSemi systems and can include both trigger codes and system status bits that are partially documented—the community lacks a standardized parser for all edge cases in the system codes channel. This has been noted in discussions within the pyedflib repository and related GitHub issues.

Finally, while the Python ecosystem provides multiple excellent options for BDF reading, the lack of a unified "bdftools" package means users must navigate which library best suits their specific needs (pybdf for focused BioSemi access versus pyedflib for general EDF/BDF interoperability versus MNE-Python for integrated preprocessing), and documentation of best practices for integrating BDF-derived EEG data into [[whole-brain-modeling]] workflows like TVB remains sparse.
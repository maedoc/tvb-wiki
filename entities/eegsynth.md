---
created: 2024-01-15
sources:
- Oostenveld & colleagues
- Donders Centre for Cognitive Neuroimaging
- https://www.eegsynth.org; GitHub Repository
- EEGSynth community
- https://github.com/eegsynth/eegsynth; FieldTrip
- Oostenveld et al. (2011)
- Computational Intelligence and Neuroscience
- https://doi.org/10.1155/2011/156869
tags:
- software
- electrophysiology
- eeg
- brain-computer-interface
- real-time-processing
- neurofeedback
title: EEGSynth
type: entity
updated: '2026-05-05'
---

EEGSynth is an open-source software platform for real-time processing, analysis, and visualization of electroencephalography (EEG) and other electrophysiological signals (Oostenveld & colleagues, Donders Centre for Cognitive [[neuroimaging]]). Originally developed at the Donders Centre for Cognitive Neuroimaging at Radboud University in Nijmegen, Netherlands—most notably by Robert Oostenveld, who also leads the FieldTrip toolbox development—the project was initiated around 2010 as an exploration of affordable open-hardware EEG for creative and research applications (EEGSynth community). Now maintained as a community-driven project registered as a legal Association in France since 2018, EEGSynth enables researchers to build closed-loop experiments, brain-computer interfaces (BCIs), and neurofeedback systems where neural signals are processed and fed back to the subject or experimental setup with minimal latency (GitHub Repository).

## Overview

EEGSynth provides a modular framework for real-time EEG analysis that spans from raw signal acquisition to feature extraction and output generation. The software integrates with multiple data acquisition systems—including OpenBCI, FieldTrip realtime buffer, and LSL-compatible devices—and supports standard EEG formats, making it compatible with a wide range of hardware setups (EEGSynth community). Unlike batch-oriented EEG processing pipelines that operate on already-recorded data, EEGSynth is architected from the ground up for real-time operation, streaming data through a series of processing modules that can be connected, disconnected, and reconfigured on the fly during an experiment.

The architecture consists of input modules that read from EEG amplifiers or recorded files, preprocessing modules for filtering and artifact rejection, feature extraction modules that compute spectral power, spatial filters, or other signal characteristics, and output modules that generate feedback signals, trigger external hardware, or stream data to other software packages. This modular design allows researchers to construct custom processing chains tailored to their specific experimental needs without modifying core code. The modules communicate via Redis, a lightweight in-memory database that serves as a message broker enabling parallel processing of multiple analysis streams (GitHub Repository).

## Key Features

EEGSynth implements several signal processing capabilities essential for real-time [[electrophysiology]] research. Spectral analysis modules compute power in user-defined frequency bands (alpha, beta, gamma, etc.) using sliding window approaches that balance temporal resolution against frequency precision. Spatial filtering options include ICA-based artifact rejection and Laplacian unembedding for improving spatial specificity. The software supports common EEG-derived features such as steady-state visually evoked potentials (SSVEP), motor imagery patterns, and event-related spectral perturbations (EEGSynth community).

A distinguishing characteristic of EEGSynth is its integration with the [[labstreaminglayer]] (LSL) protocol, which provides a standardized mechanism for synchronizing data streams across multiple software and hardware components in real time. This allows EEGSynth to exchange data with stimulus presentation software, eye trackers, motion capture systems, and other data sources with sub-millisecond temporal precision. Additionally, EEGSynth can interoperate with [[openvibe]]—both are independent real-time BCI platforms that can exchange data via LSL, but EEGSynth is not an addon to OpenVibe (GitHub Repository).

The software is designed for command-line operation using Python 3.8+ and Bash scripts, with a graphical user interface for loading and managing patch configurations. It includes modules for MIDI control (allowing EEG signals to control musical synthesizers), OSC (Open Sound Control) for multimedia applications, Art-Net for lighting control, and DMX for stage effects, reflecting its origins in artistic and musical applications (EEGSynth community).

## Relationship to TVB

While EEGSynth is primarily oriented toward real-time experimental applications rather than large-scale brain modeling, it interfaces with TVB-related workflows in several important ways. Raw or preprocessed EEG data from EEGSynth can be exported for offline analysis using TVB's [[connectivity]] pipeline, particularly when constructing [[personalized-brain-modeling|personalized brain]] models from empirical neuroimaging data. The spectral features computed by EEGSynth provide validation targets for [[neural-mass-models]] and [[whole-brain|whole-brain modeling]] simulations that aim to reproduce observed [[brain-oscillations]].

EEGSynth also demonstrates a complementary approach to neural signal analysis compared to TVB's simulation engine. Where TVB solves large-scale dynamical systems on structural connectomes to generate synthetic activity, EEGSynth measures and decodes actual neural signals in real time. Researchers studying brain-oscillations or building personalized brain modeling frameworks may use EEGSynth for data acquisition and TVB for forward modeling, creating a bridge between empirical electrophysiology and computational whole-[[brain-dynamics]]. The connection between the two platforms can be facilitated through LSL, which both systems support for real-time data exchange.

## Key Papers

The EEGSynth project does not have a dedicated primary reference paper, but it is closely associated with the FieldTrip toolbox development led by Robert Oostenveld at the Donders Institute. The seminal FieldTrip paper (Oostenveld, Fries, Maris, & Schoffelen, 2011) established the methodological foundation for many of the real-time processing concepts that EEGSynth implements. Additionally, documentation of specific artistic and research applications—such as the COGITO project transforming EEG into sound for radio telescope transmission—provides evidence of the platform's capabilities (EEGSynth community).

## Related Software

EEGSynth occupies a niche in the real-time EEG processing ecosystem that overlaps with several other software platforms. EEGLAB provides comprehensive offline EEG analysis capabilities and can serve as a preprocessing toolchain for data subsequently used in TVB modeling. OpenVibe offers a visual programming environment for real-time BCI applications with a comparable modular architecture. The MNE-Python connectivity module provides Python-native connectivity analysis tools that can process EEG data exported from EEGSynth. For real-time signal processing in Python, the electrophysiology community also includes pyxdf for reading LSL data streams and neuroconv for format conversions.
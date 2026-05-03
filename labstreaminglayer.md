---
title: LabStreamingLayer
created: 2026-01-15
updated: 2026-05-03
type: entity
tags: [software-visualization, electrophysiology, neuroimaging-eeg, neuroimaging-meg]
sources: []
---

## Overview

LabStreamingLayer (LSL) is an open-source framework for collecting, timestamping, and synchronizing data from multiple biological and physical sensing devices in real time. Originally developed for neuroscience and neuroimaging experiments, LSL provides a standardized protocol and software library for streaming time-series data from devices such as electroencephalography (EEG) systems, magnetoencephalography (MEG) scanners, eye trackers, motion capture systems, and stimulus presentation computers. The framework addresses a fundamental challenge in multimodal neuroimaging: ensuring that data streams from heterogeneous hardware are precisely synchronized and can be aligned for offline analysis or real-time processing applications.

## Motivation and Context

Neuroscience experiments increasingly rely on simultaneous recordings from multiple modalities—for example, combining EEG or MEG with functional magnetic resonance imaging (fMRI), eye tracking, or behavioral measurements. Each device operates on its own internal clock, and naive approaches to synchronization (such as relying on system time or recording start signals) introduce temporal jitter that can obscure millisecond-scale neural dynamics. LabStreamingLayer was developed to solve this synchronization problem by providing a unified streaming architecture based on a client-server model, where each data acquisition device (the "outlet") pushes time-stamped samples to a central "inlet" that can be accessed by one or more consumer applications.

The project emerged from the BCI2000 community and was released as open-source software around 2010. It fills a niche that neither commercial acquisition software nor general-purpose networking tools adequately address: the need for sub-millisecond temporal precision across heterogeneous devices in a research environment. LSL has become a de facto standard in real-time neuroscience, with integration into major software platforms including [[MNE-Python]], [[EEGLAB]], [[OpenVibe]], [[BCI2000]], and [[The Virtual Brain]].

## Technical Architecture

LSL operates on a publish-subscribe model over local area networks (or on a single machine). The core abstraction is the ** Outlet**, which represents a data source, and the **Inlet**, which represents a data consumer. Each data sample carries a timestamp measured against a locally synchronized clock, typically derived from the system's real-time clock or a hardware timing card. The protocol supports multiple data types including scalar values, vectors, matrices, and arbitrary binary data, with sample rates ranging from sub-Hz to tens of kHz.

The software stack comprises three main components. First, the **liblsl** library provides a C++ core with bindings for Python, MATLAB, Java, and C#, enabling integration into virtually any research software environment. Second, the **LSL Apps** collection includes command-line utilities for recording, playback, and network diagnostics. Third, **device SDKs** implement LSL outlets for specific hardware devices—many commercial EEG systems now ship with built-in LSL support, while community-maintained drivers extend compatibility to a wider range of equipment including serial port devices, analog-to-digital converters, and eye trackers from manufacturers like SR Research and Tobii.

Timestamps in LSL are expressed as double-precision floating-point values in seconds, measured relative to an arbitrary but fixed epoch. Crucially, LSL provides a **clock synchronization** mechanism based on a lightweight protocol that estimates and corrects for clock drift between machines, achieving sub-millisecond accuracy under typical network conditions. For applications requiring even tighter synchronization, LSL supports the use of hardware timing cards (e.g., National Instruments DAQ devices) that can pace data acquisition and provide external clock signals.

## Relationship to TVB and Whole-Brain Modeling

In the context of whole-brain modeling, LSL serves as an essential data acquisition layer for feeding empirical data into computational models. [[The Virtual Brain]] (TVB) and related whole-brain simulation platforms require empirical time series—resting-state fMRI bold signals, intracranial EEG recordings, or scalp-level EEG/MEG data—as inputs for model fitting, validation, or real-time brain-state estimation. LSL provides the ingestion pathway for these empirical signals, enabling real-time streaming of neural data directly into TVB's simulation engine.

The combination of LSL with TVB is particularly relevant for **personalized brain modeling** applications, where individual connectivity matrices derived from diffusion tensor imaging (DTI) are combined with individual neural time series to fit personalized model parameters. Real-time LSL streams can feed empirical EEG or MEG data into TVB's parameter estimation pipeline, enabling adaptive closed-loop experiments where brain stimulation or stimulus presentation is guided by the model's inferred state. This architecture underpins emerging research in **epilepsy modeling** and **brain-stimulation** applications, where real-time neural recordings are used to drive orValidate computational models of seizure dynamics.

## Key Features

LSL offers several features that distinguish it from alternative data acquisition frameworks. The **multi-subject, multi-session** design supports recording from multiple participants simultaneously, each with their own outlet chain, which is essential for hyperscanning experiments. The **flexible data format** accommodates both regular time series (fixed sample rate) and irregular event streams (variable sample rate), making it suitable for triggers, markers, and behavioral event codes alongside continuous neural signals. The **zero-copy design** minimizes computational overhead, ensuring that high-channel-count EEG or MEG streams do not introduce latency artifacts. Finally, the **cross-platform** implementation runs on Linux, macOS, and Windows, with full support for both 32-bit and 64-bit architectures.

## Ecosystem and Related Software

LSL integrates with a rich ecosystem of neuroscience analysis tools. [[MNE-Python]] provides an LSL inlet class that无缝streams recorded data into MNE's preprocessing and source estimation pipeline. [[EEGLAB]] offers a plugin for importing LSL streams, enabling real-time visualization and analysis within EEGLAB's graphical environment. [[OpenVibe]] implements LSL as a native acquisition driver, supporting real-time signal processing and brain-computer interface applications. [[BCI2000]] itself can operate as an LSL outlet, allowing legacy BCI2000 paradigms to feed data into the broader LSL ecosystem.

For data standardization downstream of LSL, the framework pairs with [[NeuroData Without Borders]] (NWB), which provides a standardized format for archiving neurophysiological recordings. Tools like [[neuroconv]] facilitate conversion from LSLrecorded data to NWB-compliant formats, ensuring long-term data preservation and interoperability. The [[spikeinterface]] framework similarly supports LSL as an ingestion layer for extracellular electrophysiology data, including spike times and local field potentials.

## Related Software

- [[MNE-Python]]
- [[EEGLAB]]
- [[OpenVibe]]
- [[BCI2000]]
- [[NeuroData Without Borders]]
- [[spikeinterface]]
- [[neuroconv]]
- [[The Virtual Brain]]
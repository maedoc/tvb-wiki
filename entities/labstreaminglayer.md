---
created: 2025-01-01
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/gramfort-2013.md
- raw/papers/arxiv-2509.02799.md
tags:
- software-visualization
- neuroimaging-eeg
- neuroimaging-meg
- electrophysiology
title: LabStreamingLayer
type: entity
updated: '2026-05-04'
---

# LabStreamingLayer

## Overview

LabStreamingLayer (LSL) is an open-source software system for the real-time collection, synchronization, and multiplexing of streaming data from multiple biomedical and scientific data acquisition devices. Developed primarily to address the need for precise temporal alignment of multimodal [[neuroimaging]] and [[electrophysiology]] data in neuroscience experiments, LSL provides a network-based protocol and middleware implementation that enables heterogeneous data sources—ranging from [[eeg]] amplifiers and [[meg]] systems to eye trackers, stimulus presentation computers, and physiological sensors—to stream their data with millisecond-level temporal precision to one or more consumer applications. The system was created by the SCCN (Swartz Center for [[computational-neuroscience]]) at UC San Diego and has become widely adopted in cognitive neuroscience research, providing the backbone for many closed-loop experiment paradigms and brain-computer interface implementations [@kothe2014; @sccn-lsl-wiki].

## Motivation and Context

The fundamental challenge that LSL addresses is the temporal synchronization of multimodal data streams in real-time neuroscience experiments. Traditional data collection approaches often relied on proprietary software from hardware manufacturers, which made it difficult to combine data from different vendors or to implement closed-loop paradigms where neural signals must be analyzed and fed back to the subject within milliseconds. Prior to LSL, researchers had to develop custom hardware interfaces or rely on less precise software synchronization methods that introduced temporal jitter and offset between data streams.

LSL emerged from the need to standardize streaming data formats across different hardware vendors and software platforms. The system operates on a publisher-subscriber model where data acquisition devices or software applications act as "outlets" that broadcast their data onto a local network, while consumer applications act as "inlets" that subscribe to these streams. This architecture allows multiple applications to consume the same data simultaneously, enabling scenarios such as real-time signal processing, stimulus delivery, and data logging running in parallel without interfering with each other [@kothe2014].

## Key Features

LSL provides several features that make it particularly well-suited for neuroscience research applications. The **clock synchronization mechanism** ensures that all data streams are timestamped with high accuracy relative to a master clock, eliminating the need for separate hardware synchronization units in many experimental setups. LSL achieves this through regular clock sampling and [[linear]] regression between local and remote clocks, providing sub-millisecond synchronization across devices on standard Ethernet networks without requiring specialized timing hardware like PTP [@sccn-lsl-wiki; @kothe2014]. The system supports a wide variety of data types including continuous signals (floating-point or integer), event markers, and complex data structures, making it adaptable to virtually any physiological recording modality.

The **multiplexing capability** of LSL allows multiple data streams to be combined into a single unified stream, which is particularly useful for applications that require synchronized access to all modalities. LSL also includes **automatic discovery** functionality through DNS-SD (DNS Service Discovery), which allows consumer applications to automatically detect and connect to available data sources on the local network without manual configuration. The software provides official implementations in C++, Python, MATLAB, and Java, with third-party bindings available for additional languages including Julia and R [@github-lsl].

## Relationship to TVB

While [[the-virtual-brain]] (TVB) is primarily a whole-brain modeling simulator that operates offline, LSL can serve as a complementary tool in closed-loop brain stimulation paradigms where real-time neural data informs the parameters of brain simulations. In such configurations, LSL may be used to stream [[eeg]] or [[meg]] data from a subject to a processing pipeline that estimates model parameters in real-time, which are then fed into a TVB simulation to predict upcoming brain states. Conversely, LSL can also be used to deliver TVB simulation output as visual or auditory feedback to a subject in a neurofeedback setup.

The relationship between LSL and TVB is therefore one of complementary tools rather than direct integration—LSL handles the real-time data acquisition layer while TVB handles the offline or near-real-time simulation layer. Researchers implementing personalized brain modeling workflows may use LSL to collect the empirical neuroimaging data (resting-state [[fmri]], [[eeg]], and [[meg]] recordings) that subsequently inform TVBconnectome-based models via [[parameter-estimation]] procedures.

## Related Software and Tools

LSL integrates with several other software packages in the neuroimaging ecosystem. The [[eeglab]] environment includes the **LSL Plugin** for streaming EEG data directly from LSL streams into EEGLAB for analysis, enabling researchers to combine real-time preprocessing with the extensive analysis capabilities of the EEGLAB toolbox [@eeglab-lsl-plugin]. The [[mne-python]] library provides native LSL support through its `mne.io.Stream` module, allowing seamless integration with the MNE ecosystem for source reconstruction and [[connectivity]] analysis.

For brain-computer interface applications, LSL is commonly used alongside [[bcilab]] (which was developed by the same group at SCCN) to implement real-time classifier training and decoding pipelines. The system also works with [[fieldtrip]] for near-real-time analysis and with the [[brainstorm]] software for visualization. In terms of data format, LSL data can be exported to standard neuroimaging formats like [[nifti]] or BIDS-compliant formats for offline analysis, bridging the gap between real-time experimentation and post-hoc processing in tools like [[freesurfer]] or [[spm]].

## Key Technical Details

The LSL data model consists of **Channels**, **Samples**, and **Streams**. Each stream has a defined number of channels (e.g., 64 channels for a 64-channel EEG system), a sampling rate, and a channel format (float32, int32, etc.). Samples are transmitted either individually or in chunks depending on the application requirements, with the protocol supporting both push-based and pull-based data retrieval patterns. The network protocol uses TCP or UDP transport depending on whether reliability or latency is prioritized, with most real-time applications using UDP to minimize latency at the cost of occasional packet loss.

For timestamp synchronization, LSL employs a hierarchical clock system where one device on the network is elected as the "master clock" (often the device with the most precise timing hardware, such as a National Instruments DAQ board), and all other devices either synchronize to this clock directly or use a local clock that is drift-corrected relative to the master through regular clock sampling and linear regression. This approach achieves sub-millisecond synchronization across devices on standard Ethernet networks without requiring specialized timing hardware [@sccn-lsl-wiki].

## Key Papers

- **Kothe, C. A.** (2014). Lab Streaming Layer (LSL). Poster presentation. SCCN, UC San Diego. [@kothe2014]
- **Kothe, C. A., & Makeig, S.** (2013). BCILAB: A platform for brain-computer interface development. *Frontiers in Neuroscience*, 7, 98. [@makeig2013]

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Gramfort et al. (2013). *MEG and EEG: From Acquisition to Analysis*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fnins.2013.00010)
3. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
---
created: 2024-01-15
sources:
- https://arxiv.org/abs/1905.03790
- https://www.nature.com/articles/s41592-019-0570-0
- https://www.frontiersin.org/articles/10.3389/fnins.2017.00159/full
- https://github.com/billkarsh/SpikeGLX
- https://www.nature.com/articles/s41592-019-0571-z
- https://www.jneurosci.org/content/39/44/8577
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2601.03796.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/biosemi-bdf-spec.md
tags:
- software
- neuroimaging-eeg
- electrophysiology
- neural-recording
- data-acquisition
- neuropixels
title: SpikeGLX
type: entity
updated: '2026-04-30'
---

SpikeGLX is an open-source data acquisition (DAQ) system designed for extracellular [[electrophysiology]] recordings, with particular emphasis on high-density neural probes such as NeuroPixels. Developed primarily by Bill Karsh at Janelia Research Campus (HHMI), SpikeGLX provides a unified software platform for streaming, storing, and synchronizing neural data from multiple electrode arrays simultaneously. The software has become a de facto standard in the electrophysiology community since its initial release, enabling researchers to capture large-scale neural recordings with sub-millisecond temporal precision and electrode-level spatial resolution.

## Motivation and Context

The emergence of large-scale electrophysiology techniques—particularly the development of NeuroPixels probes in 2017 and subsequent generations—created a need for dedicated acquisition software that could handle the massive data throughput these recordings generate. A single NeuroPixels 2.0 probe with 512 channels recording at 30 kHz produces approximately 1 GB of data per minute, requiring specialized file formats and real-time data management capabilities that traditional DAQ systems could not provide. SpikeGLX was developed to address this bottleneck, offering native support for NeuroPixels hardware while maintaining compatibility with other extracellular recording platforms including Michigan probes, Utah arrays, and conventional tetrode arrays.

The software emerged within the broader context of the [[reproducibility]] crisis in neuroscience, where standardized data formats and open-source tools have become increasingly important. SpikeGLX produces output in a native binary format (`.bin` files with accompanying `.meta` metadata files), which can be converted to standard interchange formats such as NIX or [[neurodata-without-borders]] (NWB) using separate downstream tools. This design choice allows the acquisition software to remain focused on its core competency while enabling interoperability with analysis frameworks through well-documented conversion utilities. The flexibility to work with multiple output formats stands in contrast to earlier proprietary systems that locked researchers into vendor-specific formats, limiting collaborative analysis and independent validation of results.

## Key Features

SpikeGLX supports multiple acquisition modes tailored to different experimental requirements. Impedance testing mode allows users to verify electrode [[connectivity]] before recording sessions, identifying faulty channels that might contaminate data. Wideband recording captures the full spectral content of neural signals (0.1 Hz to 20 kHz), enabling subsequent decomposition into action potentials (spikes) and [[local-field-potentials]] (LFPs) during offline analysis. Bandpass filtering during acquisition can reduce storage requirements when only specific frequency bands are of interest.

The software implements sophisticated synchronization mechanisms essential for multi-probe and multi-modal experiments. Hardware synchronizing pulses from stimulus delivery systems, video cameras, and behavior tracking equipment are timestamped with microsecond precision and embedded directly into the data stream. This allows precise alignment of neural activity with behavioral events, a critical requirement for studies of sensorimotor integration, decision-making, and other paradigms requiring correlation of neural and external variables.

SpikeGLX produces output in a self-describing hierarchical data format that stores raw electrophysiology traces alongside associated metadata, electrode positions, and synchronization events. The native `.bin` format stores raw data samples while `.meta` files contain JSON-formatted metadata including channel maps, sampling rates, and hardware configurations. The companion software SpikeGLX-to-NWB converter enables seamless transition to NWB-compliant datasets for integration with analysis frameworks such as [[spikeinterface]] and [[pynest]].

## Technical Specifications

The software operates on standard laboratory PC hardware, requiring a dedicated GPU for real-time visualization of high-channel-count recordings. Data are written to solid-state drives to maintain write speeds commensurate with the incoming data stream. SpikeGLX runs on Windows and Linux operating systems, with the Windows version offering tighter integration with National Instruments DAQ hardware.

Recording sessions are organized into a hierarchical structure: a single recording may contain multiple probes (probe00, probe01, etc.), each with their own set of channels. Channel metadata include physical electrode positions (which can be exported to [[nifti]] format for visualization in tools such as [[fsleyes]]), impedance values, and noise levels. This structured metadata approach facilitates downstream analysis workflows that require knowledge of electrode geometry.

## Relationship to TVB and Whole-Brain Modeling

While SpikeGLX is primarily a data acquisition tool rather than a simulation platform, it plays an indirect but important role in the whole-brain modeling ecosystem. The software enables experimental datasets that characterize neural dynamics at the level of individual neurons and local circuits, providing ground truth data for validating neural-mass-models and whole-brain-model implementations. Researchers using The Virtual Brain can incorporate empirical measurements from NeuroPixels recordings to constrain model parameters through techniques such as [[parameter-estimation]] and variational-bayes.

SpikeGLX recordings are particularly valuable for studying brain-oscillations and local-field-potentials, which serve as macroscale correlates of the neural mass activity simulated in whole-brain models. The high temporal resolution of extracellular recordings enables characterization of phase-amplitude coupling, cross-frequency interactions, and other phenomena that inform the design of neural mass formulations. Additionally, SpikeGLX's support for simultaneous multi-probe recordings provides empirical constraints for structural-connectivity estimates used in connectome-based modeling approaches.

## Related Software and Ecosystem

SpikeGLX integrates with a broader ecosystem of electrophysiology analysis tools. The SpikeInterface package, which provides a unified interface for spike sorting and waveform analysis, accepts SpikeGLX native files directly. Phy offers a graphical user interface for manual spike sorting curation, while KiloSort provides automated clustering algorithms. For LFP analysis, LFPy simulates extracellular potentials using volume conduction models that can be validated against empirical recordings acquired with SpikeGLX.

The software complements other neuroimaging modalities in multi-modal experiments. Combined with fMRI or MEG recordings, SpikeGLX enables investigation of the relationship between microscale neural activity and macroscale brain dynamics—directly relevant to dynamic-causal-modeling and effective-connectivity analyses. The synchronization capabilities support integration with NWB archives for publication and data sharing through resources such as DataLad and OpenNEURO.

## Limitations and Considerations

SpikeGLX represents a specialized tool optimized for high-density probe recordings, and its feature set reflects this focus. Users seeking general-purpose data acquisition for other electrophysiology modalities (e.g., scalp EEG, intracortical LFP) may find alternative platforms such as Open Ephys or FieldTrip more appropriate. The software requires technical familiarity with command-line interfaces and configuration files, presenting a steeper learning curve than point-and-click alternatives.

Storage requirements represent a practical consideration for long-duration recordings. Researchers conducting studies of spontaneous-activity or resting-state dynamics spanning hours or days must budget accordingly for storage infrastructure and implement appropriate data management strategies. Compression utilities included with SpikeGLX can reduce footprint at the cost of requiring recompression before analysis.

Despite these limitations, SpikeGLX has established itself as an essential tool in the modern electrophysiology workflow, enabling experiments that would be impractical with earlier acquisition technology. Its open-source nature and active development community ensure continued utility as neural recording technology advances.

## Key Papers

- Jun, J. J., et al. (2017). Real-time spike sorting platform for high-density extracellular recordings with amplitude thresholding and collision-based discrimination. *Journal of Neuroscience Methods*, 287, 25-37. Introduces the algorithmic foundation for real-time spike detection later integrated into SpikeGLX workflows.

- Steinmetz, N. A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. *Science*, 372(6539), eabf4588. Describes the second-generation NeuroPixels technology and companion data acquisition requirements addressed by SpikeGLX.

- Rübel, J., et al. (2022). NIX Format: A unified repository format for electrophysiology data. *Frontiers in Neuroinformatics*, 16, 870776. Documents the NIX format and its relationship to SpikeGLX data conversion.

## References

1. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
2. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796)
3. Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon. (2026). *Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?*. [Link](https://arxiv.org/abs/2604.03619)
4. (authors unknown). *BioSemi BDF Format Specification*.
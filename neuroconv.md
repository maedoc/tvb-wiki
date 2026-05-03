---
title: NeuroConv
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [neuroconv, nwb, spikeinterface, neo, open-ephys, suite2p, caiman, deeplabcut, python, electrophysiology, software-tools]
sources: [web-search-neuroconv-2026]
---

NeuroConv is a Python package for converting neurophysiology data from a wide variety of proprietary acquisition formats into the [[nwb|Neurodata Without Borders (NWB)]] standard. Developed by CatalystNeuro and the broader NWB community, NeuroConv addresses a critical bottleneck in computational neuroscience: the fragmentation of experimental data across dozens of incompatible file formats produced by different recording systems, analysis packages, and hardware manufacturers. By providing a unified, automated pipeline for data standardization, NeuroConv enables researchers to aggregate, share, and analyze neurophysiology datasets with significantly reduced manual effort and error.

## Motivation and Context

The landscape of neurophysiology data acquisition is remarkably heterogeneous. A typical laboratory may use [[spikeglx|SpikeGLX]] for extracellular recordings, [[open-ephys|OpenEphys]] for broadband electrophysiology, [[suite2p]] or [[caiman]] for calcium imaging analysis, and [[deeplabcut|DeepLabCut]] for behavioral tracking—each producing data in its own proprietary format. Before the advent of standardized data formats like NWB, researchers spent substantial time writing custom parsing scripts for each new dataset, often reinventing wheels and introducing inconsistencies <cite>Rübel et al. 2022</cite>. NWB provides a comprehensive schema for describing neurophysiology experiments, but the burden of actually converting data into NWB format remained substantial <cite>Teeters et al. 2015</cite>. NeuroConv automates this conversion process by providing ready-made interfaces for over 50 supported formats, extracting relevant metadata automatically and writing compliant NWB files using community best practices <cite>Mayorquin et al. 2025</cite>.

## History and Development

NeuroConv originated as **nwb-conversion-tools**, a project initiated in 2019 by CatalystNeuro to address the growing need for automated data conversion pipelines in neurophysiology laboratories. The early versions focused primarily on supporting common electrophysiology formats from recording systems like SpikeGLX, Blackrock, and Neuralynx.

In July 2022, the project underwent a significant rebranding to **NeuroConv** along with a comprehensive reorganization of the codebase and API <cite>Mayorquin et al. 2025</cite>. This renaming reflected the project's maturation from a collection of conversion utilities into a fully-featured, modular data conversion framework. The new name emphasized both the neural data domain focus and the conversion capabilities while aligning with Python package naming conventions.

Following the rename, NeuroConv experienced substantial community growth, with contributions expanding format support to include optical physiology interfaces (calcium imaging, two-photon microscopy), behavioral data streams, and intracellular electrophysiology. The project also integrated more deeply with the broader NWB ecosystem, including native support for data deposition to the [[dandi|DANDI Archive]] <cite>Rübel et al. 2022</cite>. This growth culminated in the first dedicated conference publication describing the software's architecture and design philosophy <cite>Mayorquin et al. 2025</cite>.

## Key Features

NeuroConv provides an extensive set of capabilities designed to handle the complexities of modern neurophysiology data conversion workflows. The package supports an impressive range of data modalities, encompassing extracellular electrophysiology from systems such as [[spikeinterface|SpikeGLX]], [[open-ephys|OpenEphys]], [[neuralynx|Neuralynx]], [[blackrock|Blackrock]], and [[plexon|Plexon]], as well as intracellular electrophysiology from Axon Binary Files. Optical physiology interfaces handle calcium imaging data from [[suite2p]], [[caiman|CaImAn]], and [[scanimage|ScanImage]], while behavioral tracking is supported from tools like [[deeplabcut|DeepLabCut]], [[sleap|SLEAP]], and [[fictrac|FicTrac]].

A distinguishing feature of NeuroConv is its automatic metadata extraction capability. The package parses source files to recover sampling rates, electrode configurations, amplifier settings, and timestamp information, substantially reducing the manual annotation burden that previously fell on researchers attempting to standardize their data.

For handling large-scale datasets, NeuroConv implements chunked reading and streaming write operations that avoid the memory bottlenecks common in naive conversion implementations when processing multi-gigabyte recording files. The library also applies automatic chunking and lossless compression to output NWB files, optimizing storage requirements without sacrificing data fidelity <cite>Mayorquin et al. 2025</cite>.

The package excels at combining multiple heterogeneous data streams within a single NWB file. When experiments involve simultaneous electrophysiology recordings, behavioral tracking, and optical imaging, NeuroConv provides specialized tools for temporal alignment across these modalities, ensuring that timestamps remain synchronized even when the original data sources use different clocks or sampling rates.

## Architecture and Extensibility

NeuroConv employs a modular architecture based on **DataInterface** classes, each of which handles conversion for a specific format or data type. The [[nwb|NWBConverter]] class serves as the main orchestrator, coordinating multiple interfaces and ensuring consistent metadata across the converted file. Users can instantiate appropriate interfaces, extract and customize metadata programmatically, and execute the conversion with a single function call. The architecture is deliberately extensible: researchers can implement custom DataInterface subclasses to support formats not yet included in the core library, and the project welcomes contributions through pull requests. This design philosophy has fostered an active community of contributors extending NeuroConv's capabilities.

## Relationship to TVB and Whole-Brain Modeling

While NeuroConv itself is a data conversion tool rather than a simulation engine, it plays an important supporting role in [[whole-brain-modeling]] workflows. Personalized brain models require empirical data—structural connectivity from [[diffusion-imaging|DTI]], functional dynamics from [[fmri|fMRI]] or EEG recordings, and potentially electrophysiological measurements from intracranial electrodes. NeuroConv facilitates the ingestion of these diverse data sources into unified [[nwb|NWB]] archives that can be subsequently processed by analysis pipelines and imported into modeling frameworks. For researchers using [[the-virtual-brain]] or other [[whole-brain-simulators]], NeuroConv can help standardize the input data, particularly when combining datasets from multiple labs or acquisition systems.

## Key Papers

The primary citation for NeuroConv is the conference paper describing the software and its design philosophy: Mayorquin, H., Baker, C., Adkisson-Floro, P., Weigl, S., Trapani, A., Tauffer, L., Rübel, O., & Dichter, B. (2025). *NeuroConv: Streamlining Neurophysiology Data Conversion to the NWB Standard*. Proceedings of the 24th Python in Science Conference (SciPy 2025). https://doi.org/10.25080/cehj4257

For the NWB standard itself, the comprehensive ecosystem description provides essential background: Rübel, O., Tritt, A., Ly, R., Dichter, B.K., Ghosh, S., et al. (2022). The Neurodata Without Borders ecosystem for neurophysiological data science. *eLife*, 11, e78362. https://doi.org/10.7554/eLife.78362

An earlier foundational paper describing the NWB 1.0 specification: Teeters, J.L., Godbout, J., Rübel, O., et al. (2015). Neurodata without borders: creating a common data format for neurophysiology. *Neuron*, 88(4), 629-634. https://doi.org/10.1016/j.neuron.2015.10.025

## Related Software

- [[nwb|Neurodata Without Borders (NWB)]] — the standard format that NeuroConv converts to
- [[spikeinterface]] — Python library for electrophysiology analysis that integrates with NeuroConv
- [[neo|Neo]] — Python library for handling neurophysiology data formats
- [[nwb]] — the NWB ecosystem and specification
- [[dandi|DANDI]] — archive for publishing and sharing NWB data
- [[open-ephys|OpenEphys]] — recording system with format support in NeuroConv
- [[suite2p]] — calcium imaging analysis with export interfaces in NeuroConv
- [[deeplabcut|DeepLabCut]] — pose estimation for behavior, supported as a data interface

## Installation and Usage

NeuroConv is distributed via PyPI and can be installed with `pip install neuroconv`. Specific format dependencies (such as readers for commercial acquisition systems) can be installed via extras, for example `pip install neuroconv[openephys]` or `pip install neuroconv[spikeglx]`. The documentation provides extensive conversion examples for each supported format, and the API supports both script-based conversions and integration into larger preprocessing pipelines.
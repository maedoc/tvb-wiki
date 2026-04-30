---
created: 2024-01-15
sources:
- garcia-2014
- nix-spec
- elephant-paper
- nwb-spec
- spikeinterface-paper
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/bein-2018.md
tags:
- software
- electrophysiology
- data-formats
- spike-sorting
- python
- elephant
- spikeinterface
- neo
title: Neo
type: concept
updated: '2026-04-30'
---

# Neo

## Overview

Neo is a Python library designed for handling neurophysiology data — that is, electrophysiological recordings from neurons and neural networks. Developed as a community-driven initiative by researchers in computational neuroscience, Neo provides a unified, Python-native data structure for storing, accessing, and analyzing time-series data from diverse recording formats including spike trains, local field potentials (LFP), electroencephalography (EEG), and intracellular recordings. The library serves as a foundational data layer in the Python electrophysiology ecosystem, enabling interoperability between different analysis tools and file formats that would otherwise be incompatible.

## Motivation and Context

The electrophysiology community has long struggled with format heterogeneity. Commercial recording systems (Axon, PatchMaster, Plexon, Blackrock, SpikeGadgets, and many others) each use proprietary file formats, often with limited documentation. Historically, researchers wrote custom parsers for each format, leading to duplicated effort, bugs, and difficulty comparing results across laboratories. Neo emerged to address this problem by providing a common data model designed around the semantics of neurophysiology experiments — with clear structures for timestamps, channels, segments, and recording epochs — implemented as native Python objects.

The library occupies a critical position in the data analysis pipeline, situated between raw data acquisition and higher-level analysis. Unlike tools that focus on specific analyses (such as spike sorting or frequency-domain analysis), Neo concentrates on the data I/O and representation layer, defining what a "recording" means in computational terms and providing robust mechanisms for loading data from disk. This design philosophy allows Neo to serve as a shared foundation that multiple specialized tools can build upon, reducing friction in collaborative workflows and enabling reproducible science.

## Data Model and Architecture

The Neo data model organizes neurophysiology recordings into a hierarchical structure consisting of several core objects. At the highest level, a **Block** represents a single recording session or experiment, which contains one or more **Segment** objects — each segment typically corresponding to a continuous recording epoch (e.g., a trial or a resting-state period). Within each segment, data is stored in **Group** objects (introduced in Neo 0.11 to replace the deprecated ChannelIndex) that group related recording sites such as electrodes from the same shank or pixels from a voltage-sensitive dye, and **AnalogSignal** objects that hold continuous voltage or current traces. Discrete events such as stimuli, behavior markers, or spike times are stored in **Event** and **SpikeTrain** objects respectively.

This hierarchical organization mirrors the structure of typical electrophysiology experiments while providing sufficient flexibility to accommodate diverse experimental paradigms. Neo also supports annotation mechanisms that allow researchers to attach arbitrary metadata to any object in the hierarchy, facilitating integration with domain-specific conventions and database systems. The annotation system is particularly valuable for large-scale collaborations such as the Human Connectome Project, where standardized metadata is essential for data discovery and reuse.

## Supported Formats and I/O

Neo includes an extensive library of I/O drivers called "rawio" modules, which parse proprietary file formats and convert them to the Neo data model. As of recent versions, the library supports over forty different formats spanning commercial systems, academic formats, and standard interchange formats. Notable supported formats include NIX (a HDF5-based format for neuroscience data) and NWB (NeuroData Without Borders), as well as Blackrock NSx/NEV, Plexon PLX, Tucker Davis Technologies (TDT) files, Axon ABF, and various formats from Open Ephys and SpikeGadgets recording systems.

The rawio architecture is designed for lazy loading — rather than reading entire files into memory, Neo can stream data on demand, which is essential for working with long-duration recordings that may exceed available RAM. This streaming capability also enables efficient partial data access, allowing analysts to load just the time window or channels of interest without processing the complete dataset. The lazy loading mechanism is particularly valuable when working with high-density electrode arrays producing gigabytes of data per recording session.

## Relationship to the Broader Ecosystem

Neo forms part of a tightly integrated ecosystem of Python tools for electrophysiology analysis. The library has close ties to Elephant (a tool for spike train analysis and population coding), SpikeInterface (a unified framework for spike sorting), and NWB (the NeuroData Without Borders format for standardized data sharing). This integration is bidirectional: Neo can read data from and write to NWB files, enabling long-term archival and community data sharing, while also providing the foundational data structures that Elephant and SpikeInterface operate on.

The relationship between Neo and NWB deserves particular attention. While Neo provides a programming-friendly in-memory representation, NWB defines a standardized file format optimized for archival and sharing. Neo's NWBIO module enables seamless conversion between the two representations, allowing researchers to leverage Neo's convenient API during analysis while also producing NWB-compliant outputs for publication or data deposition. This interoperability addresses a longstanding challenge in computational neuroscience: the tension between ease of analysis and adherence to data standards.

## Relationship to TVB

Neo has an indirect but meaningful relationship with The Virtual Brain (TVB). TVB focuses on whole-brain modeling and simulation, often requiring empirical data about neural activity as inputs to drive or validate its computational models. While Neo itself is not a TVB component, the two projects share a common ethos: enabling reproducible, interoperable neuroscience research through standardized data handling. Neo's data model — particularly its representation of spike trains and continuous signals — could serve as a source of empirical data that feeds into TVB simulations. Researchers using TVB who work with electrophysiology data from systems like Blackrock or Plexon could leverage Neo for data preprocessing before converting their datasets into formats compatible with TVB's simulation framework.

## Key Papers

- Garcia et al. (2014). "Neo: an object model for handling electrophysiology data in Python." Frontiers in Neuroinformatics. This is the primary introduction to the Neo library, describing its design philosophy and core data model.
- Bezaire et al. (2022). "SpikeInterface, a unified framework for spike sorting." eLife. Describes the integration between SpikeInterface and Neo for spike sorting workflows.
- NIX Format Specification. The documentation for the NIX HDF5-based neuroscience data format that Neo supports.
- NWB Specification. The NeuroData Without Borders format documentation describing the standard that Neo's NWBIO module implements.

## Key Features in Practice

Several features make Neo particularly valuable for working laboratories. First, the library's API is designed to be intuitive for users familiar with the NumPy ecosystem, with objects that behave like standard numerical arrays while exposing neurophysiology-specific attributes (units, sampling rate, t_start, t_stop). This design choice lowers the barrier to entry for researchers already comfortable with scientific Python. Second, Neo implements automatic unit handling and conversion, preventing a common source of errors in electrophysiology where different systems may report voltages in microvolts, millivolts, or volts. Third, the library provides a plugin mechanism that allows developers to add support for new formats without modifying the core codebase, contributing to Neo's extensibility.

## Limitations and Open Questions

Despite its utility, Neo faces challenges that remain active areas of development. The diversity of file formats means that some legacy or proprietary formats have limited or buggy support, and testing across all formats is impractical for the small maintainer team. Additionally, Neo's focus on representation means that advanced processing capabilities (filtering, artifact rejection, spike detection) are delegated to other libraries, requiring users to understand the relationships between tools in the ecosystem. Recent efforts to improve documentation and create unified tutorials that guide users through complete analysis pipelines address this fragmentation concern.

## Related Tools and Concepts

Neo intersects with several related concepts in the wiki. For data-formats, Neo provides adapters to/from formats like NIX and NWB. For spike-sorting, Neo integrates with SpikeInterface to provide the data foundation for spike extraction algorithms. The library also relates to broader topics in electrophysiology and data-formats in neuroscience more generally. Users interested in the Python scientific computing stack may also wish to explore how Neo's data model compares to those in Python data analysis frameworks more broadly.

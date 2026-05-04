---
created: 2025-01-15
sources:
- raw/papers/bein-2018.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/arxiv-2505.16861.md
tags:
- software-neuroconv
- software-bids
- software-nwb
- neurodata-without-borders
- bids
- data-formats
- electrophysiology
- spikeinterface
title: NeuroConv
type: entity
updated: '2026-05-04'
---

# NeuroConv

## Overview

NeuroConv is a Python package designed to streamline the conversion of neuroscience data between heterogeneous file formats, enabling interoperability across diverse recording systems, analysis pipelines, and archive standards. Developed as part of the broader [[neurodata-without-borders]] (NWB) ecosystem [1], NeuroConv provides a unified interface for reading proprietary binary formats from major [[electrophysiology]] vendors (such as Blackrock, Axona, and Intan) and exporting to standard open formats including NWB, MAT, and Pickle. The library plays a critical role in addressing the historical fragmentation of neuroscience data formats, where each manufacturer and laboratory developed idiosyncratic file conventions that impeded [[reproducibility]], data sharing, and secondary analysis.

## Motivation and Context

The proliferation of custom data formats in neuroscience has long presented a barrier to reproducible research. Electrophysiology laboratories, for instance, historically used vendor-specific binary formats (e.g., .nev, .nsx from Blackrock; .set, .eeg, .pos from Axona) that required specialized proprietary software for access. This situation forced researchers to maintain fragile custom parsing scripts, limited the portability of analysis pipelines, and complicated collaborative data sharing. The NWB project emerged as a community-driven standard to address these issues [3], but adoption required robust conversion tooling that could handle the complexity of real-world recording data—including electrode geometry, stimulus definitions, behavioral timestamps, and metadata annotations. NeuroConv was developed to fill this gap, providing validated, well-tested conversion routes from common proprietary formats directly into NWB-compliant HDF5 or Zarr stores. By lowering the technical barrier to standardization, NeuroConv enables researchers to archive their data in future-proof open formats while maintaining compatibility with existing analysis workflows built around [[the-virtual-brain]] or other modeling platforms.

The development of NeuroConv also aligns with the broader movement toward [[bids]] (Brain Imaging Data Structure) compliance for [[neuroimaging]] datasets [5]. While NWB targets electrophysiology data primarily, BIDS provides a complementary standard for MRI, [[fmri]], and MEG datasets. NeuroConv's architecture supports conversion pathways that bridge these ecosystems, enabling researchers working with multimodal recordings—simultaneous EEG-fMRI or MEG-intracranial recordings—to organize their data into coherent, standards-compliant archives suitable for both immediate analysis and long-term curation.

## Key Features

NeuroConv implements a modular architecture organized around **readers** and **converters**. Each reader is specialized for a specific input format and extracts the full complement of available data—spike times, continuous voltage traces, unit metadata, electrode positions, and behavioral events—into an intermediate standardized representation. Converters then map this intermediate representation to target format schemas (primarily NWB). The library handles the semantic translation automatically, including inferring missing required fields from available metadata where possible and raising informative errors when essential information is absent.

One of NeuroConv's distinguishing features is its tight integration with the [[spikeinterface]] ecosystem [4]. This integration enables direct conversion of [[spikeglx]], [[open-ephys]], and related formats through shared reader backends, reducing code duplication and ensuring consistent behavior across the electrophysiology data processing pipeline. Users can thus move seamlessly from raw data acquisition through preprocessing in SpikeInterface to standardized archiving via NeuroConv, creating end-to-end workflows that are both reproducible and portable across computing environments.

Importantly, NeuroConv supports incremental conversion, allowing partial updates to existing NWB files without requiring complete re-conversion. This feature is particularly valuable for longitudinal studies or large-scale experiments where regenerated datasets would impose significant computational overhead. The package also maintains comprehensive unit tests and validation routines to ensure that converted files pass NWB schema validation, reducing the risk of downstream compatibility issues when data is processed by other NWB-compatible tools such as those in the [[ebrains]] ecosystem.

## Relationship to TVB

NeuroConv facilitates the integration of experimental electrophysiology data into [[whole-brain|whole-brain modeling]] workflows implemented in [[the-virtual-brain]] (TVB). Researchers collecting intracranial EEG, microelectrode recordings, or LFP data can use NeuroConv to convert their recordings into NWB format, which can subsequently be imported into TVB's data structures for [[connectivity]] estimation, model fitting, or validation purposes. This compatibility positions NeuroConv as a valuable ingestion layer for [[personalized-brain-modeling]] pipelines, where patient-specific electrophysiology recordings must be mapped onto generative [[whole-brain-modeling]] frameworks.

The use case is particularly relevant for [[epilepsy-modeling]] studies, where intracranial EEG recordings from patients undergoing presurgical evaluation may be used to estimate patient-specific connectomes or to validate [[epileptor]]-based seizure models. By providing a robust route from vendor-specific recording formats into the open NWB standard, NeuroConv enables such clinical data to be seamlessly incorporated into computational workflows that might otherwise require substantial custom data parsing infrastructure. The library complements other TVB adapters—such as those for [[bids]] or custom TVB-specific formats—by providing a route from raw vendor files into the broader neuroimaging data ecosystem.

## Related Software

NeuroConv operates within a broader ecosystem of neuroscience data conversion and standardization tools. Key related packages include [[neurodata-without-borders]] (the target format standard), [[spikeinterface]] (which shares reader infrastructure), Neo (an alternative Python library for electrophysiology data I/O), NIX (a format specification for scientific data), and the [[ebrains]] data platform [2]. For researchers working with multimodal datasets, the library can be used alongside [[mne-python]] for signal processing or pybids for organizing derivative outputs in BIDS-compliant directory structures. Additionally, NeuroConv complements preprocessing pipelines such as SpikeGLX and Open Ephys that produce the input data it converts.

## Technical Considerations

The primary technical challenge addressed by NeuroConv involves preserving the semantic fidelity of data during format translation. Proprietary formats often encode information in ways that are not directly mappable to NWB schemas—for example, electrode arrays may be described in manufacturer-specific coordinate systems, or stimulus events may be embedded in custom event codes. NeuroConv's architecture handles these complexities through hierarchical converters that can inject user-provided metadata or infer missing values based on standard conventions.

Users should be aware that while NeuroConv handles most common scenarios automatically, highly customized recording setups may require manual specification of additional metadata fields to achieve full compliance with NWB specifications. Performance considerations are also important: very large recordings (tens of gigabytes) may require significant processing time and disk space during conversion, though NeuroConv's chunked reading approach mitigates memory constraints. For cloud deployment scenarios, the library supports writing directly to remote storage backends compatible with the DANDI Archive [6], enabling scalable data management for multi-laboratory consortium projects.

## References

1. B. Bein (2018). *[[pyedflib]]: Python library for reading and writing EDF/BDF files*. Journal of Open Source Software. [DOI](https://doi.org/10.21105/joss.00899)
2. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *[[tvb|The Virtual Brain]] Ontology: A Digital Knowledge Framework for Reproducible [[brain-network]] Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211)
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
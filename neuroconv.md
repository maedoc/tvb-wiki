---
title: NeuroConv
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software, data-formats, neuroimaging, electrophysiology, conversion-tools]
sources: [https://github.com/catalystneuro/neuroconv, https://nwb.org/tools/core/neuroconv/, https://doi.org/10.25080/cehj4257, https://doi.org/10.7554/eLife.78362]
---

# NeuroConv

## Overview

NeuroConv is a Python package designed to streamline the conversion of neuroscience data between heterogeneous file formats, enabling interoperability across diverse recording systems, analysis pipelines, and archive standards <cite>Mayorquin et al. 2025</cite>. Developed as part of the broader [[neurodata-without-borders]] (NWB) ecosystem, NeuroConv provides a unified interface for reading proprietary binary formats from major electrophysiology vendors (such as Blackrock, Axona, and Intan) and exporting to standard open formats including NWB, MAT, and Pickle <cite>NeuroConv Documentation</cite>. The library plays a critical role in addressing the historical fragmentation of neuroscience data formats, where each manufacturer and laboratory developed idiosyncratic file conventions that impeded reproducibility, data sharing, and secondary analysis <cite>Rübel et al. 2022</cite>.

## Motivation and Context

The proliferation of custom data formats in neuroscience has long presented a barrier to reproducible research. Electrophysiology laboratories, for instance, historically used vendor-specific binary formats (e.g., .nev, .nsx from Blackrock; .set, .eeg, .pos from Axona) that required specialized proprietary software for access. This situation forced researchers to maintain fragile custom parsing scripts, limited the portability of analysis pipelines, and complicated collaborative data sharing <cite>Teeters et al. 2015</cite>. The NWB project emerged as a community-driven standard to address these issues, but adoption required robust conversion tooling that could handle the complexity of real-world recording data—including electrode geometry, stimulus definitions, behavioral timestamps, and metadata annotations <cite>Rübel et al. 2022</cite>. NeuroConv was developed to fill this gap, providing validated, well-tested conversion routes from common proprietary formats directly into NWB-compliant HDF5 or Zarr stores <cite>Mayorquin et al. 2025</cite>. By lowering the technical barrier to standardization, NeuroConv enables researchers to archive their data in future-proof open formats while maintaining compatibility with existing analysis workflows built around [[the-virtual-brain]] or other modeling platforms.

## Key Features

NeuroConv implements a modular architecture organized around **readers** and **converters**. Each reader is specialized for a specific input format and extracts the full complement of available data—spike times, continuous voltage traces, unit metadata, electrode positions, and behavioral events—into an intermediate standardized representation. Converters then map this intermediate representation to target format schemas (primarily NWB). The library handles the semantic translation automatically, including inferring missing required fields from available metadata where possible and raising informative errors when essential information is absent. Importantly, NeuroConv supports incremental conversion, allowing partial updates to existing NWB files without requiring complete re-conversion. The package also integrates with the [[spikeinterface]] ecosystem, enabling direct conversion of SpikeGLX, Open Ephys, and related formats through shared backends <cite>NeuroConv Documentation</cite>.

## Relationship to TVB

NeuroConv facilitates the integration of experimental electrophysiology data into whole-brain modeling workflows implemented in [[the-virtual-brain]] (TVB). Researchers collecting intracranial EEG, microelectrode recordings, or LFP data can use NeuroConv to convert their recordings into NWB format, which can subsequently be imported into TVB's data structures for connectivity estimation, model fitting, or validation purposes. This compatibility positions NeuroConv as a valuable ingestion layer for personalized brain modeling pipelines, where patient-specific electrophysiology recordings must be mapped onto generative connectome-based models. The library complements other TVB adapters—such as those for [[bids]] or custom TVB-specific formats—by providing a route from raw vendor files into the broader neuroimaging data ecosystem.

## Related Software

NeuroConv operates within a broader ecosystem of neuroscience data conversion and standardization tools. Key related packages include [[neurodata-without-borders]] (the target format standard), [[spikeinterface]] (which shares reader infrastructure), [[neo]] (an alternative Python library for electrophysiology data I/O), [[nix]] (a format specification for scientific data), and the [[ebrains]] data platform. Additionally, NeuroConv complements preprocessing pipelines such as [[spikeglx]] and [[open-ephys]] that produce the input data it converts. For researchers working with multimodal datasets, the library can be used alongside [[mne-python]] for signal processing or [[pybids]] for organizing derivative outputs in BIDS-compliant directory structures.

## Technical Considerations

The primary technical challenge addressed by NeuroConv involves preserving the semantic fidelity of data during format translation. Proprietary formats often encode information in ways that are not directly mappable to NWB schemas—for example, electrode arrays may be described in manufacturer-specific coordinate systems, or stimulus events may be embedded in custom event codes <cite>Rübel et al. 2022</cite>. NeuroConv's architecture handles these complexities through hierarchical converters that can inject user-provided metadata or infer missing values based on standard conventions. The package also maintains comprehensive unit tests and validation routines to ensure that converted files pass NWB schema validation, reducing the risk of downstream compatibility issues. Users should be aware that while NeuroConv handles most common scenarios automatically, highly customized recording setups may require manual specification of additional metadata fields to achieve full compliance with NWB specifications <cite>Mayorquin et al. 2025</cite>. Performance considerations are also important: very large recordings (tens of gigabytes) may require significant processing time and disk space during conversion, though NeuroConv's chunked reading approach mitigates memory constraints. For cloud deployment scenarios, the library supports writing directly to remote storage backends compatible with the DANDI Archive.

## Key Papers

The primary citation for NeuroConv is the conference paper describing the software and its design philosophy: Mayorquin, H., Baker, C., Adkisson-Floro, P., Weigl, S., Trapani, A., Tauffer, L., Rübel, O., & Dichter, B. (2025). *NeuroConv: Streamlining Neurophysiology Data Conversion to the NWB Standard*. Proceedings of the 24th Python in Science Conference (SciPy 2025). https://doi.org/10.25080/cehj4257

For the NWB standard itself, the comprehensive ecosystem description provides essential background: Rübel, O., Tritt, A., Ly, R., Dichter, B.K., Ghosh, S., et al. (2022). The Neurodata Without Borders ecosystem for neurophysiological data science. *eLife*, 11, e78362. https://doi.org/10.7554/eLife.78362

An earlier foundational paper describing the NWB 1.0 specification: Teeters, J.L., Godbout, J., Rübel, O., et al. (2015). Neurodata without borders: creating a common data format for neurophysiology. *Neuron*, 88(4), 629-634. https://doi.org/10.1016/j.neuron.2015.10.025

## References

- Mayorquin, H., Baker, C., Adkisson-Floro, P., Weigl, S., Trapani, A., Tauffer, L., Rübel, O., & Dichter, B. (2025). NeuroConv: Streamlining Neurophysiology Data Conversion to the NWB Standard. Proceedings of the 24th Python in Science Conference (SciPy 2025). https://doi.org/10.25080/cehj4257
- Rübel, O., Tritt, A., Ly, R., Dichter, B.K., Ghosh, S., et al. (2022). The Neurodata Without Borders ecosystem for neurophysiological data science. eLife, 11, e78362. https://doi.org/10.7554/eLife.78362
- Teeters, J.L., Godbout, J., Rübel, O., et al. (2015). Neurodata without borders: creating a common data format for neurophysiology. Neuron, 88(4), 629-634. https://doi.org/10.1016/j.neuron.2015.10.025
- NeuroConv Documentation. https://neuroconv.readthedocs.io/
- NWB Tools: NeuroConv. https://nwb.org/tools/core/neuroconv/
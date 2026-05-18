---
created: 2026-05-06
sources: null
tags:
- databse
- computational-neuroscience
- spiking-neural-networks
- models
title: ModelDB
type: entity
updated: '2026-05-15'
---
# ModelDB

**ModelDB** is a curated, web-accessible repository for computational neuroscience models, established to address the growing need for reproducible, shareable model implementations in the field. Originally focused on [[neuron|NEURON]]-based simulations, the database has expanded to host models across multiple simulators including [[brian2]], [[genesis]], and [[netm]], making it a heterogeneous archive of neural dynamics implementations. Each model entry in ModelDB is linked to its corresponding peer-reviewed publication, providing runnable source code alongside metadata that describes the model's architecture, parameters, and computational requirements. The database provides a submission interface accessible to non-programmers, lowering barriers for authors to share their computational work, and integrates with PubMed and other bibliographic resources to establish clear provenance chains from code to citation. Over the years, ModelDB has grown to host thousands of models spanning single-neuron biophysics, network-level simulations, and simplified population models, becoming an essential infrastructure for reproducibility in [[computational-neuroscience]]. The database also integrates with [[open-source-brain]] (OSB) to provide web-based simulation capabilities, allowing researchers to run models directly in the browser without local software installation.

## Overview

ModelDB hosts thousands of models with:
- Source code (often in multiple languages)
- Model metadata and descriptions
- Links to original publications
- Web-based simulation via OSB ([[open-source-brain]]) integration

## Relationship to TVB

ModelDB provides reference implementations of neural dynamics models that inform TVB's [[neural-mass-models|neural mass model]] choices:
- [[Jansen-Rit model|[[jansen-rit]]-model]] implementations on ModelDB demonstrate biophysical parameter ranges
- Spiking model parameters in ModelDB constrain the derivation of TVB's population-level equations
- The database serves as a ground-truth source for comparing TVB model predictions against validated published models

## Related
ModelDB operates within an interconnected ecosystem of simulators, standards, and whole-brain modeling frameworks. Originally rooted in [[neuron|NEURON]]-based simulations, the repository has expanded to archive heterogeneous model implementations across platforms including [[brian2]], [[genesis]], and [[netm]], with each entry linked to its corresponding peer-reviewed publication to establish provenance from code to citation. The database leverages [[neuroml]] as a standardized model description format that promotes interoperability across simulation environments, while integration with [[open-source-brain|Open Source Brain]] furnishes web-based execution capabilities that lower barriers to reproducible modeling by eliminating local installation requirements. These infrastructure choices reflect the broader [[computational-neuroscience]] field's commitment to making models publicly accessible and runnable independent of any single software stack.

At the systems level, ModelDB anchors validated biophysical architectures that inform [[whole-brain]] simulation frameworks such as [[the-virtual-brain]]. Detailed circuit models archived in the database provide parameter constraints and ground-truth references for the derivation of [[neural-mass-models|neural mass model]] equations: [[jansen-rit-model|Jansen-Rit model]] implementations on ModelDB demonstrate biophysical parameter ranges, while spiking model parameters constrain the derivation of TVB's population-level equations. By maintaining explicit links between executable code and published results alongside integration with bibliographic resources such as PubMed, ModelDB serves as a foundational comparison layer for validating TVB predictions against independently verified network architectures and aligns single-neuron biophysics with large-scale [[brain-network]] modeling objectives.

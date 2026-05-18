---
created: 2026-05-06
sources:



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

- [[neuroml]] — standardized model description format used in ModelDB
- [[the-virtual-brain]] — [[whole-brain]] simulation framework
- osb — Open Source Brain integration with ModelDB

## References

1. Migliore et al. (2006). *ModelDB: making models publicly accessible to support [[computational-neuroscience]]*. Neuroinformatics. [DOI](https://doi.org/10.1007/s12021-006-0002-7))
2. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358))
3. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *[[tvb|The Virtual Brain]] Ontology: A Digital Knowledge Framework for Reproducible [[brain-network]] Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211))
---
created: 2026-05-06
sources:
- raw/papers/migliore-2006.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/semanticscholar-9afbfd2d37be.md
tags:
- databse
- computational-neuroscience
- spiking-neural-networks
- models
title: ModelDB
type: entity
updated: '2026-05-13'
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
ModelDB is embedded in a broader ecosystem of simulation platforms and research infrastructure for [[computational-neuroscience]]. The repository originally concentrated on [[neuron|NEURON]]-based simulations, but has since expanded to host thousands of models implemented across multiple simulator platforms, reflecting the field's methodological diversity and the growing need for cross-platform [[reproducibility]] [[raw/papers/migliore-2006.md|Migliore et al. 2006]]. This heterogeneity is exemplified by data-driven [[spiking-neural-networks|spiking network]] models such as the Potjans-Diesmann cortical microcircuit, which has been widely adopted as a benchmark for validating simulators including [[nest|NEST]] and serves as a foundational building block for mesoscale [[brain-network|brain network]] architectures [[raw/papers/potjans-diesmann-2014.md|Potjans & Diesmann 2014]]. At the whole-brain scale, [[the-virtual-brain]] and its associated Ontology framework address complementary reproducibility challenges by curating published models, generating executable code for multiple backends, and exporting FAIR metadata with provenance-aware reports that link simulations to their empirical foundations [[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. 2025]]. Together, these resources form a layered infrastructure that advances reproducibility across scales, from validated single-neuron dynamics to [[whole-brain-modeling|whole-brain simulations]], each contributing to the standardization and portability of computational models across the neuroscience community.

## References

1. Migliore et al. (2006). *ModelDB: making models publicly accessible to support computational neuroscience*. Neuroinformatics. [DOI](https://doi.org/10.1007/s12021-006-0002-7)
2. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358)
3. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, Petra Ritter. (2025). *The Virtual Brain Ontology: A Digital Knowledge Framework for Reproducible Brain Network Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211)
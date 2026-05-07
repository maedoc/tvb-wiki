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
updated: '2026-05-06'
---

# ModelDB

**ModelDB** is a curated database of computational neuroscience models. It provides a searchable repository of published models from simulation codes including [[neuron]], [[netm]], [[brian2]], and [[genesis]].

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
- [[osb]] — Open Source Brain integration with ModelDB

## References

1. Migliore et al. (2006). *ModelDB: making models publicly accessible to support [[computational-neuroscience]]*. Neuroinformatics. [DOI](](https://doi.org/10.1007/s12021-006-0002-7))
2. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](](https://doi.org/10.1093/cercor/bhs358))
3. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *[[tvb|The Virtual Brain]] Ontology: A Digital Knowledge Framework for Reproducible [[brain-network]] Modeling*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.11.19.689211))
---
title: "ModelDB"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [databse, computational-neuroscience, spiking-neural-networks, models]
sources: []
---

# ModelDB

**ModelDB** is a curated database of computational neuroscience models. It provides a searchable repository of published models from simulation codes including [[neuron]], [[netm]], [[brian2]], and [[genesis]].

## Overview

ModelDB hosts thousands of models with:
- Source code (often in multiple languages)
- Model metadata and descriptions
- Links to original publications
- Web-based simulation via OSB (Open Source Brain) integration

## Relationship to TVB

ModelDB provides reference implementations of neural dynamics models that inform TVB's neural mass model choices:
- [[Jansen-Rit model|jansen-rit-model]] implementations on ModelDB demonstrate biophysical parameter ranges
- Spiking model parameters in ModelDB constrain the derivation of TVB's population-level equations
- The database serves as a ground-truth source for comparing TVB model predictions against validated published models

## Related

- [[neuroml]] — standardized model description format used in ModelDB
- [[the-virtual-brain]] — whole-brain simulation framework
- [[osb]] — Open Source Brain integration with ModelDB

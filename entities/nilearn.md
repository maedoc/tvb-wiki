---
title: "Nilearn"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [software-nilearn, neuroimaging-fmri, machine-learning, python, statistics]
sources: []
---

# Nilearn

**Nilearn** is a Python library for fast and easy statistical learning on neuroimaging data. It provides tools for decoding, predictive modeling, connectivity analysis, and visualization of functional MRI data.

## Overview

Nilearn provides:
- Machine learning utilities for brain decoding (MVPA, searchlight)
- Functional connectivity estimation and graph analysis
- Spatial and temporal preprocessing tools
- Visualization of brain maps, connectomes, and statistical results
- Integration with scikit-learn for standard ML workflows

## Relationship to TVB

Nilearn complements TVB in several ways:
- **Connectivity analysis**: Nilearn estimates functional connectivity matrices that TVB uses as inputs
- **Decoding**: Machine learning approaches in Nilearn help identify brain regions relevant for TVB model validation
- **Visualization**: Nilearn plots brain networks and connectivity that mirror TVB output
- Both are Python-based and integrate with the broader neuroimaging ecosystem ([[nibabel]], [[nipype]])
- Nilearn-derived connectivity matrices can seed TVB neural mass model coupling parameters

## References

- Nilearn website: https://nilearn.github.io/
- Abraham et al. (2014) — Machine learning for neuroimaging with scikit-learn

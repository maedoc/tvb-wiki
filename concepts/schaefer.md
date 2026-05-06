---
title: "Schaefer Parcellation"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [brain-parcellation, resting-state, functional-connectivity, atlas, nodes]
sources: []
---

# Schaefer Parcellation

The **Schaefer atlas** is a widely-used functional brain parcellation derived from resting-state fMRI data in the Human Connectome Project. It provides a hierarchical set of parcels at 100, 200, 300, 400, 500, 600, 800, and 1000 region resolutions, with 7-network or 17-network assignments.

## Overview

Key features:
- **Data-driven**: parcels derived from group-level functional connectivity gradients
- **Hierarchical**: from 100 to 1000 regions with nested assignments
- **Network-annotated**: each parcel assigned to Yeo 7/17-network labels
- **Surface-based**: mapped to FreeSurfer's fsaverage surface

## Relationship to TVB

The Schaefer atlas is one of the most common parcellation choices for TVB:
- **Node definition**: 400 or 1000 Schaefer parcels serve as TVB network nodes
- **Network labelling**: Yeo network assignments guide TVB model comparison
- **Connectivity matrices**: structural and functional connectivity is computed between Schaefer parcels

## References

- Schaefer et al. (2018) — Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. Cerebral Cortex 28(9): 3095–3114. https://doi.org/10.1093/cercor/bhx179

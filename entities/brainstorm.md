---
title: Brainstorm
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [software-brainstorm, eeg, meg, source-localization, neuroimaging]
sources:
- https://neuroimage.usc.edu/brainstorm/
- https://github.com/brainstorm-tools/brainstorm3
---

# Brainstorm

**Brainstorm** is a collaborative, open-source Matlab and Python application dedicated to MEG/EEG/sEEG/ECoG data analysis and visualization.

## Overview

Brainstorm provides a comprehensive GUI and scripting environment for:
- **Data import**: MEG/EEG from major systems (CTF, 4D, Neuromag, BrainProducts, etc.)
- **Preprocessing**: Filtering, artifact rejection, ICA, SSP
- **Source localization**: Dipole fitting, distributed imaging (MNE, sLORETA, LCMV beamformer)
- **Time-frequency analysis**: Spectral decomposition, connectivity measures
- **Statistics**: Sensor-level and source-level group statistics
- **Visualization**: Interactive 3D brain and sensor plots

## Relationship to TVB

Brainstorm and TVB share MEG/EEG analysis workflows:
- Brainstorm performs source localization, TVB simulates whole-brain dynamics at the source level
- Brainstorm-derived source time series can seed TVB simulations
- TVB's forward models enable comparison of simulated and Brainstorm-reconstructed EEG/MEG
- Both integrate with standard neuroimaging formats and [[freesurfer]] cortical surfaces

## Software

- Website: https://neuroimage.usc.edu/brainstorm/
- Open-source under GPL v2 license

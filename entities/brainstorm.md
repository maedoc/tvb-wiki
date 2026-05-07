---
created: 2026-05-06
sources:
- https://neuroimage.usc.edu/brainstorm/
- https://github.com/brainstorm-tools/brainstorm3
- raw/papers/arxiv-2604.16463.md
- raw/papers/mijalkov-2017-braph.md
- raw/papers/arxiv-2602.00684.md
tags:
- software-brainstorm
- eeg
- meg
- source-localization
- neuroimaging
title: Brainstorm
type: entity
updated: '2026-05-07'
---

# Brainstorm

**Brainstorm** is a collaborative, open-source Matlab and Python application dedicated to MEG/EEG/sEEG/ECoG data analysis and visualization.

## Overview

Brainstorm provides a comprehensive GUI and scripting environment for:
- **Data import**: MEG/EEG from major systems (CTF, 4D, Neuromag, BrainProducts, etc.)
- **Preprocessing**: Filtering, artifact rejection, ICA, SSP
- **[[source-localization]]**: Dipole fitting, distributed imaging (MNE, [[sloreta]], LCMV beamformer)
- **Time-frequency analysis**: Spectral decomposition, [[connectivity]] measures
- **Statistics**: Sensor-level and source-level group statistics
- **Visualization**: Interactive 3D brain and sensor plots

## Relationship to TVB

Brainstorm and TVB share MEG/EEG analysis workflows:
- Brainstorm performs source localization, TVB simulates whole-[[brain-dynamics]] at the source level
- Brainstorm-derived source time series can seed TVB simulations
- TVB's forward models enable comparison of simulated and Brainstorm-reconstructed EEG/MEG
- Both integrate with standard [[neuroimaging]] formats and [[freesurfer]] cortical surfaces

## Software

- Website: https://neuroimage.usc.edu/brainstorm/
- Open-source under GPL v2 license

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
2. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.
3. F. G. Prieto, Takfarinas Medani, Chinmay Chinara, Richard M. Leahy, S. Pursiainen. (2026). *Multi-Compartment Volume Conductor with Complete Electrode Model: Simulated Stereo-EEG Source Localization using Brainstorm-Zeffiro Plugin*. [Link](https://www.semanticscholar.org/paper/f4b56506ccb9de875ba54551883b3e41fd2b1a8b)
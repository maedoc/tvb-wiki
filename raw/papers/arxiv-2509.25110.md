# gCAMB: A GPU-accelerated Boltzmann solver for next-generation cosmological surveys

**Source**: semantic-scholar
**ID**: bb70da0dda95c7d8864d09a12d8cf1af94f526fd
**DOI**: 10.1016/j.ascom.2025.101038
**URL**: https://www.semanticscholar.org/paper/bb70da0dda95c7d8864d09a12d8cf1af94f526fd
**Date**: 2025-09-29
**Year**: 2025
**Authors**: L. Storchi, P. Campeti, M. Lattanzi, N. Antonini, E. Calore, P. Lubrano
**Venue**: Astronomy and Computing
**Citations**: 0

## Abstract

Inferring cosmological parameters from Cosmic Microwave Background (CMB) data requires repeated and computationally expensive calculations of theoretical angular power spectra using Boltzmann solvers like CAMB. This creates a significant bottleneck, particularly for non-standard cosmological models and the high-accuracy demands of future surveys. While emulators based on deep neural networks can accelerate this process by several orders of magnitude, they first require large, pre-computed training datasets, which are costly to generate and model-specific. To address this challenge, we introduce gCAMB, a version of the CAMB code ported to GPUs, which preserves all the features of the original CPU-only code. By offloading the most computationally intensive modules to the GPU, gCAMB significantly accelerates the generation of power spectra, saving massive computational time, halving the power consumption in high-accuracy settings and, among other purposes, facilitating the creation of extensive training sets needed for robust cosmological analyses. We make the gCAMB software available to the community at https://github.com/lstorchi/CAMB/tree/gpuport.

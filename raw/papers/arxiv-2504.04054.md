# SageNet: Fast Neural Network Emulation of the Stiff-amplified Gravitational Waves from Inflation

**Source**: semantic-scholar
**ID**: 91cc1b4ed70d5a61c8f2d3064650cd63c78bccf3
**DOI**: 10.3847/1538-4365/ade4c6
**URL**: https://www.semanticscholar.org/paper/91cc1b4ed70d5a61c8f2d3064650cd63c78bccf3
**Date**: 2025-04-05
**Year**: 2025
**Authors**: Fan Zhang, Yifang Luo, Bohua Li, Ruihan Cao, W. Peng, Joel Meyers, Paul R. Shapiro
**Venue**: Astrophysical Journal Supplement Series
**Citations**: 1

## Abstract

Accurate modeling of the inflationary gravitational waves (GWs) requires time-consuming, iterative numerical integrations of differential equations to take into account their backreaction on the expansion history. To improve computational efficiency while preserving accuracy, we present the Stiff-amplified Gravitational-wave Emulator Network (SageNet), a deep learning framework designed to replace conventional numerical solvers (code available at https://github.com/YifangLuo/SageNet). SageNet employs a long short-term memory architecture to emulate the present-day energy density spectrum of the inflationary GWs with possible stiff amplification, ΩGW(f). Trained on a data set of 25,689 numerically generated solutions, SageNet allows accurate reconstructions of ΩGW(f) and generalizes well to a wide range of cosmological parameters; 90.9% of the test emulations with randomly distributed parameters exhibit errors of under 4%. In addition, SageNet demonstrates its ability to learn and reproduce the artificial, adaptive sampling patterns in numerical calculations, which implement denser sampling of frequencies around changes in spectral indices in ΩGW(f). The dual capability of learning both physical and artificial features of the numerical GW spectra establishes SageNet as a robust alternative to exact numerical methods. Finally, our benchmark tests show that SageNet reduces the computation time from tens of seconds to milliseconds, achieving a speedup of ∼104 times over standard CPU-based numerical solvers with the potential for further acceleration on GPU hardware. These capabilities make SageNet a powerful tool for accelerating Bayesian inference procedures for extended cosmological models. In a broad sense, the SageNet framework offers a fast, accurate, and generalizable solution to modeling cosmological observables whose theoretical predictions demand costly differential equation solvers.

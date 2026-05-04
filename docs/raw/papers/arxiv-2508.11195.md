# The DeepFMKit python package: A toolbox for simulating and analyzing deep frequency modulation interferometers

**Source**: semantic-scholar
**ID**: a345563585afed93ee9ae5da6a1c9fa958f6d507
**DOI**: 10.1016/j.cpc.2025.109934
**URL**: https://www.semanticscholar.org/paper/a345563585afed93ee9ae5da6a1c9fa958f6d507
**Date**: 2025-08-15
**Year**: 2025
**Authors**: M. Álvarez
**Venue**: Computer Physics Communications
**Citations**: 0

## Abstract

Deep Frequency Modulation Interferometry (DFMI) is an emerging laser interferometry technique for high-precision metrology, offering picometer-level displacement measurements and the potential for absolute length determination with sub-wavelength accuracy. However, the design and optimization of DFMI systems involve a complex interplay between interferometer physics, laser technology, multiple noise sources, and the choice of data processing algorithm. To address this, we present DeepFMKit, a new open-source Python library for the end-to-end simulation and analysis of DFMI systems. The framework features a high-fidelity physics engine that rigorously models key physical effects such as time-of-flight delays in dynamic interferometers, arbitrary laser modulation waveforms, and colored noise from user-defined $1/f^\alpha$ spectral densities. This engine is coupled with a suite of interchangeable parameter estimation algorithms, including a highly-optimized, parallelized frequency-domain Non-linear Least Squares (NLS) for high-throughput offline analysis, and multiple time-domain Extended Kalman Filter (EKF) implementations for real-time state tracking, featuring both random walk and integrated random walk (constant velocity) process models. Furthermore, DeepFMKit includes a high-throughput experimentation framework for automating large-scale parameter sweeps and Monte Carlo analyses, enabling systematic characterization of system performance. DeepFMKit's modular, object-oriented architecture facilitates the rapid configuration of virtual experiments, providing a powerful computational tool for researchers to prototype designs, investigate systematic errors, and accelerate the development of precision interferometry.

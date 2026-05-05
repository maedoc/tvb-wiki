# PyBird-JAX: Accelerated inference in large-scale structure with model-independent emulation of one-loop galaxy power spectra

**Source**: semantic-scholar
**ID**: 276e6cac3129a794453f41a066114294955a4a9b
**DOI**: 10.1088/1475-7516/2026/02/016
**URL**: https://www.semanticscholar.org/paper/276e6cac3129a794453f41a066114294955a4a9b
**Date**: 2025-07-28
**Year**: 2025
**Authors**: Alexander Reeves, Pierre Zhang, Henry Zheng
**Venue**: Journal of Cosmology and Astroparticle Physics
**Citations**: 4

## Abstract

We present PyBird-JAX, a differentiable, JAX-based implementation of PyBird, using internal neural network emulators to accelerate computationally costly operations for rapid large-scale structure (LSS) analysis. PyBird-JAX computes one-loop EFTofLSS predictions for redshift-space galaxy power spectrum multipoles in 1.2 ms on a CPU and 0.2 ms on a GPU, achieving 3–4 orders of magnitude speed-up over PyBird. The emulators take a compact spline-based representation of the input linear power spectrum P(k) as feature vectors, making the approach applicable to a wide range of cosmological models. We rigorously validate its accuracy against large-volume simulations and on BOSS data, including cosmologies not explicitly represented in the training set. Leveraging automatic differentiation, PyBird-JAX supports Fisher forecasting, Taylor expansion of model predictions, and gradient-based searches. Interfaced with a variety of samplers and Boltzmann solvers, PyBird-JAX provides a high-performance, end-to-end inference pipeline. Combined with a symbolic-P(k) generator, a typical Stage-4 LSS MCMC converges in minutes on a GPU. Our results demonstrate that PyBird-JAX delivers the precision and speed required for upcoming LSS surveys, opening the door to accelerated cosmological inference with minimal accuracy loss and no pretraining. In a companion paper [1], we put PyBird-JAX to use in achieving LSS marginalised constraints free from volume projection effects through non-flat measures.

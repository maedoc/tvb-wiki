# DIFFICE-jax: Differentiable neural-network solver for data assimilation of ice shelves in JAX

**Source**: semantic-scholar
**ID**: 39decd6e7d9f94e7c2db2db2d1c1d8e9c06d83a9
**DOI**: 10.21105/joss.07254
**URL**: https://www.semanticscholar.org/paper/39decd6e7d9f94e7c2db2db2d1c1d8e9c06d83a9
**Date**: 2025-05-01
**Year**: 2025
**Authors**: Yongjian Wang, Ching‐Yao Lai
**Venue**: Journal of Open Source Software
**Citations**: 0

## Abstract

The flow of Antarctic ice shelves is controlled by their viscosity structure, which cannot be directly measured at the continental scale. Misrepresenting viscosity in ice-dynamics simulations can lead to imprecise forecasts of ice sheet mass loss into the oceans and its consequential impact on global sea-level rise. With the continent-wide remote-sensing data available over the past decades, the viscosity of the ice shelves can be inferred by solving an inverse problem. We present DIFFICE_jax : a DIFFerentiable solver using physics-informed neural networks (PINNs) (Raissi et al., 2019) for data assimilation and inverse modeling of ICE shelves written in JAX. This Python package converts discretized remote-sensing data into meshless and differentiable functions, and infers the viscosity profile by directly solving the Shallow Shelf Approximation (SSA) equations for ice shelves. The inversion algorithm is implemented in JAX (Bradbury et al., 2018). The DIFFICE_jax package includes several advanced features beyond vanilla PINNs algorithms, including collocation points resampling, non-dimensionalization of data and equations, extended-PINNs (XPINNs) (Jagtap & Karniadakis, 2020), and viscosity exponential scaling function, which are essential for accurate inversion. The package is designed to be user-friendly and accessible for beginners. The GitHub repository also provides tutorial examples with Colab notebooks for users at different levels to reproduce the results and modify the code for their specific problems of interest.

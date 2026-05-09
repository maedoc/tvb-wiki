# A Dual-Branch Coupled Fourier Neural Operator for High-Resolution Multi-Phase Flow Modeling in Porous Media

**Source**: semantic-scholar
**ID**: e88dc00df3dbaf89921853b3accda5f4ee5cb62b
**DOI**: 10.3390/w17233351
**URL**: https://www.semanticscholar.org/paper/e88dc00df3dbaf89921853b3accda5f4ee5cb62b
**Date**: 2025-11-23
**Year**: 2025
**Authors**: Hassan Al Hashim, Odai A. Elyas, John R. Williams
**Venue**: Water
**Citations**: 1

## Abstract

This paper investigates a physics-informed surrogate modeling framework for multi-phase flow in porous media based on the Fourier Neural Operator. Traditional numerical simulators, though accurate, suffer from severe computational bottlenecks due to fine-grid discretizations and the iterative solution of highly nonlinear partial differential equations. By parameterizing the kernel integral directly in Fourier space, the operator provides a discretization-invariant mapping between function spaces, enabling efficient spectral convolutions. We introduce a Dual-Branch Adaptive Fourier Neural Operator with a shared Fourier encoder and two decoders: a saturation branch that uses an inverse Fourier transform followed by a multilayer perceptron and a pressure branch that uses a convolutional decoder. Temporal information is injected via Time2Vec embeddings and a causal temporal transformer, conditioning each forward pass on step index and time step to maintain consistent dynamics across horizons. Physics-informed losses couple data fidelity with residuals from mass conservation and Darcy pressure, enforcing the governing constraints in Fourier space; truncated spectral kernels promote generalization across meshes without retraining. On SPE10-style heterogeneities, the model shifts the infinity-norm error mass into the 10−2 to 10−1 band during early transients and sustains lower errors during pseudo-steady state. In zero-shot three-dimensional coarse-to-fine upscaling from 30×110×5 to 60×220×5, it attains R2=0.90, RMSE = 4.4×10−2, and MAE = 3.2×10−2, with more than 90% of voxels below five percent absolute error across five unseen layers, while the end-to-end pipeline runs about three times faster than a full-order fine-grid solve and preserves water-flood fronts and channel connectivity. Benchmarking against established baselines indicates a scalable, high-fidelity alternative for high-resolution multi-phase flow simulation in porous media.

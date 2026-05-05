# diffSPH: Differentiable Smoothed Particle Hydrodynamics for Adjoint Optimization and Machine Learning

**Source**: semantic-scholar
**ID**: 0907533c3a6c271a3e49dec466d00e352bddade6
**DOI**: 10.48550/arXiv.2507.21684
**URL**: https://www.semanticscholar.org/paper/0907533c3a6c271a3e49dec466d00e352bddade6
**Date**: 2025-07-29
**Year**: 2025
**Authors**: Rene Winchenbach, Nils Thuerey
**Venue**: arXiv.org
**Citations**: 1

## Abstract

We present diffSPH, a novel open-source differentiable Smoothed Particle Hydrodynamics (SPH) framework developed entirely in PyTorch with GPU acceleration. diffSPH is designed centrally around differentiation to facilitate optimization and machine learning (ML) applications in Computational Fluid Dynamics~(CFD), including training neural networks and the development of hybrid models. Its differentiable SPH core, and schemes for compressible (with shock capturing and multi-phase flows), weakly compressible (with boundary handling and free-surface flows), and incompressible physics, enable a broad range of application areas. We demonstrate the framework's unique capabilities through several applications, including addressing particle shifting via a novel, target-oriented approach by minimizing physical and regularization loss terms, a task often intractable in traditional solvers. Further examples include optimizing initial conditions and physical parameters to match target trajectories, shape optimization, implementing a solver-in-the-loop setup to emulate higher-order integration, and demonstrating gradient propagation through hundreds of full simulation steps. Prioritizing readability, usability, and extensibility, this work offers a foundational platform for the CFD community to develop and deploy novel neural networks and adjoint optimization applications.

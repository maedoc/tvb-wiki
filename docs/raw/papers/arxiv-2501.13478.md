# Solving continuum and rarefied flows using differentiable programming

**Source**: semantic-scholar
**ID**: 4a1a30a6305e0f0514e64f73ac344bd2de4617c9
**DOI**: 10.1016/j.jcp.2025.114224
**URL**: https://www.semanticscholar.org/paper/4a1a30a6305e0f0514e64f73ac344bd2de4617c9
**Date**: 2025-01-23
**Year**: 2025
**Authors**: Tianbai Xiao
**Venue**: Journal of Computational Physics
**Citations**: 1

## Abstract

Accurate and efficient prediction of multi-scale flows remains a formidable challenge. Constructing theoretical models and numerical methods often involves the design and optimization of parameters. While gradient descent methods have been mainly manifested to shine in the wave of deep learning, composable automatic differentiation can advance scientific computing where the application of classical adjoint methods alone is infeasible or cumbersome. Differentiable programming provides a novel paradigm that unifies data structures and control flows and facilitates gradient-based optimization of parameters in a computer program. This paper addresses the notion and implementation of the first solution algorithm for multi-scale flow physics across continuum and rarefied regimes based on differentiable programming. The fully differentiable simulator provides a unified framework for the convergence of computational fluid dynamics and machine learning, i.e., scientific machine learning. Specifically, parameterized mechanical-neural flow models and numerical methods can be constructed for forward physical processes, while the parameters can be trained on the fly with the help of the gradients that are taken through the backward passes of the whole simulation program, a.k.a., end-to-end optimization. As a result, versatile data-driven modeling and simulation can be achieved for physics discovery, surrogate modeling, and simulation acceleration. The fundamentals and implementation of the solution algorithm are demonstrated in detail. Numerical experiments, including forward and inverse problems for hydrodynamic and kinetic equations, are presented to demonstrate the performance of the numerical method. The open-source codes to reproduce the numerical results are available under the MIT license.

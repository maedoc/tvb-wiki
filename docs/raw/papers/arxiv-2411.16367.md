# Runge-Kutta Discontinuous Galerkin Method Based on Flux Vector Splitting with Constrained Optimization-based TVB(D)-minmod Limiter for Solving Hyperbolic Conservation Laws

**arXiv ID**: 2411.16367
**Published**: 2024-11-25
**Updated**: 2024-12-10
**Authors**: Zhengrong Xie
**Categories**: math.NA
**URL**: https://arxiv.org/abs/2411.16367
**PDF**: https://arxiv.org/pdf/2411.16367
**Source**: arXiv

## Abstract

The flux vector splitting (FVS) method has firstly been incorporated into the discontinuous Galerkin (DG) framework for reconstructing the numerical fluxes required for the spatial semi-discrete formulation, setting it apart from the conventional DG approaches that typically utilize the Lax-Friedrichs flux scheme or classical Riemann solvers. The control equations of hyperbolic conservation systems are initially reformulated into a flux-split form. Subsequently, a variational approach is applied to this flux-split form, from which a DG spatial semi-discrete scheme based on FVS is derived. In order to suppress numerical pseudo-oscillations, the smoothness measurement function IS from the WENO limiter is integrated into the TVB(D)-minmod limiter, constructing an optimization problem based on the smoothness factor constraint, thereby realizing a TVB(D)-minmod limiter applicable to arbitrary high-order polynomial approximation. Subsequently, drawing on the ``reconstructed polynomial and the original high-order scheme's L2 -error constraint'' from the literature [1] , combined with our smoothness factor constraint, a bi-objective optimization problem is formulated to enable the TVB(D)-minmod limiter to balance oscillation suppression and high precision. As for hyperbolic conservation systems, limiters are typically required to be used in conjunction with local characteristic decomposition. To transform polynomials from the physical space to the characteristic space, an interpolation-based characteristic transformation scheme has been proposed, and its equivalence with the original moment characteristic transformation has been demonstrated in one-dimensional scenarios. Finally, the concept of ``flux vector splitting based on Jacobian eigenvalue decomposition'' has been applied to the conservative linear scalar transport equations and the nonlinear Burgers' equation.

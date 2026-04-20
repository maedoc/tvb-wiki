# High order conservative LDG-IMEX methods for the degenerate nonlinear non-equilibrium radiation diffusion problems

**arXiv ID**: 2401.15941
**Published**: 2024-01-29
**Updated**: 2024-01-29
**Authors**: Shaoqin Zheng, Min Tang, Qiang Zhang, Tao Xiong
**Categories**: math.NA
**URL**: https://arxiv.org/abs/2401.15941
**PDF**: https://arxiv.org/pdf/2401.15941
**Source**: arXiv

## Abstract

In this paper, we develop a class of high-order conservative methods for simulating non-equilibrium radiation diffusion problems. Numerically, this system poses significant challenges due to strong nonlinearity within the stiff source terms and the degeneracy of nonlinear diffusion terms. Explicit methods require impractically small time steps, while implicit methods, which offer stability, come with the challenge to guarantee the convergence of nonlinear iterative solvers. To overcome these challenges, we propose a predictor-corrector approach and design proper implicit-explicit time discretizations. In the predictor step, the system is reformulated into a nonconservative form and linear diffusion terms are introduced as a penalization to mitigate strong nonlinearities. We then employ a Picard iteration to secure convergence in handling the nonlinear aspects. The corrector step guarantees the conservation of total energy, which is vital for accurately simulating the speeds of propagating sharp fronts in this system.   For spatial approximations, we utilize local discontinuous Galerkin finite element methods, coupled with positive-preserving and TVB limiters. We validate the orders of accuracy, conservation properties, and suitability of using large time steps for our proposed methods, through numerical experiments conducted on one- and two-dimensional spatial problems. In both homogeneous and heterogeneous non-equilibrium radiation diffusion problems, we attain a time stability condition comparable to that of a fully implicit time discretization. Such an approach is also applicable to many other reaction-diffusion systems.

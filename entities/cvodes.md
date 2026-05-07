---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/arxiv-2507.22146.md
- raw/papers/glean-github.md
tags:
- software-neuroscience
- computational-neuroscience
- dynamical-systems-theory
- solver
- numerical-methods
title: CVODES
type: entity
updated: '2026-05-07'
---

# CVODES

## Overview

CVODES is a numerical solver for ordinary differential equations (ODEs) developed by the Center for Applied Scientific Computing at Lawrence Livermore National Laboratory. It is part of the [SUNDIALS](](software-sundials.md)) suite of nonlinear and differential-algebraic equation solvers, which also includes CVODE for initial value problems, KINSOL for nonlinear systems, and ARKode for additive Runge-Kutta methods hindmarsh-2005. CVODES specializes in solving both stiff and non-stiff systems of ODEs with full support for forward sensitivity analysis (FSA) and adjoint sensitivity analysis (ASA), making it particularly valuable for [[parameter-estimation]] in [[computational-neuroscience]] models where one must quantify how model outputs depend on underlying biological parameters sundials-2005.

The solver implements backward differentiation formulas (BDF) methods in the fixed-leading coefficient form, with adjustable step size and order selection. Unlike simpler ODE integrators, CVODES handles the challenging stiffness that arises in large-scale [[brain-network]] models where fast excitatory dynamics are coupled with slower inhibitory processes and [[synaptic-plasticity]]. The inclusion of sensitivity analysis capabilities directly within the integrator—rather than through finite-difference approximations—provides both computational efficiency and gradient accuracy essential for fitting [[whole-brain]] models to empirical [[neuroimaging]] data.

CVODES extends its predecessor CVODE by adding the capability to compute sensitivities of the solution with respect to model parameters hindmarsh-2005. While CVODE handles only the forward integration of ODEs, CVODES provides the additional machinery needed for both forward sensitivity analysis (where sensitivities are computed alongside the solution) and adjoint sensitivity analysis (for computing gradients of scalar functionals) sundials-2005.

## Key Features

**Stiff and Non-stiff Solver**: CVODES automatically detects stiffness and adapts accordingly, using BDF methods (orders 1-5) for stiff problems and Adams-Moulton methods for non-stiff problems. The solver achieves this through the VODE algorithm, which implements a variable-coefficient formulation allowing optimal adaptation to problem dynamics.

**Forward Sensitivity Analysis (FSA)**: CVODES can compute the gradient of the solution with respect to parameters simultaneously with the solution itself. This is achieved by augmenting the original ODE system with the sensitivity equations—essentially the Jacobian of the solution with respect to each parameter. For models with many parameters, this is more efficient than repeated evaluations.

**Adjoint Sensitivity Analysis (ASA)**: For problems where the number of parameters is large but the number of functionals of interest is small, adjoint sensitivity analysis provides a more efficient alternative. CVODES implements a checkpointing scheme that stores intermediate states to enable backward integration of the adjoint equations with minimal computational overhead.

**Dense and Sparse [[linear]] Solvers**: The solver supports multiple linear solver modules including dense direct methods, iterative methods with preconditioning, and sparse solvers via KLU. The sparse solver capability is particularly important for whole-brain models where the [[connectivity]] matrix may be sparse but the system Jacobian is densely populated.

**User-Defined Interfaces**: CVODES provides language bindings for C, C++, Fortran, and Python (via the SUNDIALS Python bindings), and can be called from within frameworks like [[the-virtual-brain]] to enable custom [[neural-mass-models|neural mass model]] integration.

## Relationship to TVB

CVODES plays a critical role in [The Virtual Brain](](the-virtual-brain.md)) (TVB) ecosystem as the underlying numerical engine for simulating large-scale whole-brain network models. The TVB framework uses CVODES to integrate systems of neural mass equations—such as the [[jansen-rit]] model](]([[jansen-rit-model]].md)) and its variants—across brain regions connected through empirical [[structural-connectivity]] matrices derived from diffusion tensor imaging.

The integration of CVODES into TVB addresses several computational challenges specific to whole-brain modeling. First, the brain network model comprises dozens to hundreds of coupled neural mass oscillators, creating a stiff system where fast excitatory synaptic currents couple to slower inhibitory dynamics and membrane potential integration. Second, parameter estimation in TVB requires computing derivatives of observable outputs (simulated [[fmri]] signals, EEG power spectra) with respect to model parameters—capabilities provided by CVODES through its sensitivity analysis modules. Third, TVB's stochastic simulations, which incorporate noise to model spontaneous brain activity, require solvers that can handle both deterministic dynamics and [[stochastic-differential-equations]] efficiently.

The TVB-CODES interface allows researchers to define custom neural mass models, specify regional coupling through connectivity matrices, and leverage CVODES to integrate the resulting large-scale system with adaptive timestep selection. This combination enables simulations at the whole-brain scale that would be computationally intractable with standard MATLAB ODE solvers or basic Python integrators like `scipy.integrate.odeint`. Additionally, the adjoint sensitivity capabilities in CVODES enable TVB to perform gradient-based optimization of model parameters against empirical neuroimaging data, which is essential for [[personalized-brain-modeling]] sundials-2005.

## Technical Details

The mathematical heart of CVODES lies in its implementation of the BDF method. For a system of ODEs written as:

$$\frac{dy}{dt} = f(t, y, p)$$

where $y$ is the state vector, $t$ is time, $p$ is a parameter vector, and $f$ is the nonlinear rate function, the BDF method approximates the derivative at time $t_{n+1}$ using a polynomial that interpolates previous solution points. For a $k$-step BDF method:

$$\sum_{j=0}^{k} \alpha_j y_{n+1-j} = h_n f(t_{n+1}, y_{n+1}, p)$$

where $h_n = t_{n+1} - t_n$ is the timestep and $\alpha_j$ are method coefficients. CVODES implements this through a Newton iteration requiring the solution of a linear system at each step:

$$[I - h_n \beta_j J] \Delta y = -g$$

where $J = \partial f / \partial y$ is the Jacobian and $\beta_j$ depends on the method order. The linear system is solved using the selected linear solver module, with the Jacobian either approximated via finite differences or—ideally—provided analytically by the user.

For sensitivity analysis, the forward sensitivity equations augment the original state vector with the sensitivity matrix $S = \partial y / \partial p$, giving a combined ODE system:

$$\begin{bmatrix} \dot{y} \\ \dot{S} \end{bmatrix} = \begin{bmatrix} f(t, y, p) \\ f_y S + f_p \end{bmatrix}$$

where $f_y = \partial f / \partial y$ and $f_p = \partial f / \partial p$. CVODES integrates this augmented system simultaneously with the original model, providing exact sensitivity gradients without numerical differencing.

## Version History and Licensing

CVODES is distributed under a BSD 3-clause license, allowing free use in both academic and commercial applications hindmarsh-2005. The software was initially released as part of SUNDIALS in 2002, with subsequent major releases adding new capabilities. Version 2.0.0 (2005) introduced the adjoint sensitivity analysis module, while later versions improved sparse linear solver support and added Python bindings sundials-2005.

The primary developers of CVODES include Alan Hindmarsh, Peter Brown, and Radu Serban at Lawrence Livermore National Laboratory, with contributions from numerous collaborators hindmarsh-2005. The software is actively maintained and continues to receive updates as of the broader SUNDIALS suite.

## Key Papers

- Hindmarsh, A. C., Brown, P. N., Grant, K. E., Lee, S. L., Serban, R., Shumaker, D. E., & Woodward, C. S. (2005). SUNDIALS: Suite of nonlinear and differential/algebraic equation solvers. *ACM Transactions on Mathematical Software*, 31(3), 363-396. — The original SUNDIALS documentation describing the design and capabilities of CVODES.
- Serban, R., & Hindmarsh, A. C. (2005). CVODES, the sensitivity-enabled ODE solver. *Center for Applied Scientific Computing, Lawrence Livermore National Laboratory*. — Technical report describing the sensitivity analysis capabilities.

## Related Software

- [The Virtual Brain](](the-virtual-brain.md)) — Whole-brain simulator that uses CVODES for neural mass model integration
- [[nest]] — [[spiking-neural-networks|Spiking neural network]] simulator with its own differential equation solvers
- [Brian](]([[brian]].md)) — Python-based neural simulator with flexible equation specification
- [[neuron]] — Multi-compartment neuron simulator with sophisticated stiff solvers
- [SUNDIALS](](software-sundials.md)) — Parent suite containing CVODE, KINSOL, and IDA
- [[dynamical-systems-theory]] — Mathematical framework that CVODES implements numerically
- [Stochastic Differential Equations](](stochastic-differential-equations.md)) — CVODES handles stochastic variants through its solver framework
- [Parameter Estimation](](parameter-estimation.md)) — CVODES sensitivity analysis enables gradient-based fitting of brain models

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](](https://arxiv.org/abs/2509.12873))
3. Rosa Maria Delicado, Gemma Huguet, Pau Clusella. (2025). *Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models*. [Link](](https://arxiv.org/abs/2512.03907))
4. J. Bose. (2025). *Pendulum Model of Spiking Neurons*. arXiv.org. [DOI](](https://doi.org/10.48550/arXiv.2507.22146))
5. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
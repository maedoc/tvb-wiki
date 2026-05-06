---
created: 2026-04-20
sources:
- raw/papers/risken-1989.md
- raw/papers/gardiner-2009.md
- raw/papers/tuckwell-1988.md
- raw/papers/stefanescu-jirsa-2008.md
- raw/papers/doi-10.3389-fncom.2026.1762692.md
- raw/papers/semanticscholar-7ce00494427f.md
- raw/papers/wilson-cowan-1972.md
- raw/papers/arxiv-2512.08257.md
tags:
- stochastic-differential-equations
- neural-mass-models
- nonlinear-dynamics
- mean-field-theory
- dynamical-systems-theory
title: Fokker-Planck Equation
type: concept
updated: '2026-05-04'
---

## Definition

The Fokker-Planck equation (FPE), also known as the forward Kolmogorov equation, is a partial differential equation that describes the time evolution of the probability density function for the state of a stochastic dynamical system. It provides a macroscopic, ensemble-level description of systems governed by stochastic differential equations (SDEs), complementing the microscopic, [[trajectory]]-level description that one obtains by simulating individual sample paths. The equation is named after Adriaan Fokker and Max Planck, who independently derived it in the early twentieth century to describe Brownian motion, though its mathematical foundations trace back to the work of Andrey Kolmogorov in the 1930s.

## Mathematical Form

### General One-Dimensional Form

In its most general form for a one-dimensional stochastic process, the Fokker-Planck equation takes the form:

**∂p(x,t)/∂t = -∂/∂x[μ(x)p(x,t)] + ∂²/∂x²[D(x)p(x,t)]**

where p(x,t) denotes the probability density of the random variable X at time t, μ(x) represents the drift term (the deterministic mean velocity of the process), and D(x) is the diffusion coefficient (describing the stochastic spreading or variance accumulation). The first term on the right-hand side governs conservative transport (deterministic drift), while the second term captures diffusive spreading. When D(x) is constant, the second term simplifies to D ∂²p/∂x², representing simple diffusion; more generally, when D(x) varies with position, it models position-dependent noise intensity.

### Multi-Dimensional Extension

For d-dimensional stochastic processes governed by SDEs dX_t = μ(X_t,t)dt + σ(X_t,t)dW_t, where W_t is a Wiener process, the Fokker-Planck equation generalizes to:

**∂p/∂t = -∑_i ∂/∂x_i[μ_i(x)p] + ∑_ij ∂²/∂x_i∂x_j[D_ij(x)p]**

where the diffusion matrix D = (1/2)σσ^T encodes correlations between noise components acting on different dimensions.

## Solution Methods

### Analytical Techniques

Several analytical approaches exist for solving the Fokker-Planck equation, each suited to different classes of problems. Eigenfunction expansion methods express the solution as a weighted sum of eigenfunctions of the Fokker-Planck operator, which is particularly powerful for [[linear]] drift and constant diffusion (Ornstein-Uhlenbeck processes), where the solution converges to a Gaussian. For certain nonlinear systems exhibiting potential structure, the solution can be expressed in terms of the potential function via a quasi-stationary approximation. Path integral approaches reformulate the FPE in terms of functional integrals, enabling perturbative expansions around known solutions. The matrix continued fraction method, developed extensively by Risken, provides highly efficient numerical resolution for one-dimensional processes with linear drift and polynomial diffusion coefficients, achieving exponential convergence in many cases [risken-1989].

### Numerical Methods

When analytical solutions are unavailable, various numerical discretization schemes prove useful. Finite difference schemes approximate spatial derivatives using local differences, with explicit and implicit (Crank-Nicolson) time-stepping offering different stability-accuracy tradeoffs. Finite element methods handle complex geometries and boundary conditions more naturally, particularly valuable when the domain has irregular structure. Spectral methods expand the solution in orthogonal basis functions (e.g., Fourier or Hermite), often achieving superior convergence rates for smooth problems but requiring careful treatment of nonlinearities. The choice of numerical method depends critically on problem dimensionality, required accuracy, boundary conditions, and computational resources.

## Applications in Neuroscience

### Population Density Approaches

The Fokker-Planck equation provides a foundational framework for analyzing neural population dynamics under stochastic drive. In large ensembles of neurons, individual cells exhibit variability in their membrane potentials due to synaptic noise, channel fluctuations, and heterogeneous inputs. Rather than simulating thousands of individual neurons, the population density approach tracks the distribution of membrane potentials across the population using an FPE, enabling efficient computation of population-averaged quantities like mean firing rates and correlation structure. This approach has proven particularly valuable for analyzing [[neural mass model]]s used in [[whole-brain|whole-brain modeling]], where it provides a mathematically rigorous bridge between single-[[neuron]] dynamics and population-level descriptions [tuckwell-1988].

### First Passage Time Problems

A particularly important neuroscientific application concerns the time required for a stochastic process to reach a threshold—a computation central to models of spike generation. The first passage time distribution, escape rates, and mean first passage times can be derived from solutions to boundary value problems for the FPE. For leaky [[spiking-neural-networks|integrate-and-fire]] neurons with Ornstein-Uhlenbeck dynamics, exact expressions for interspike interval distributions have been obtained using FPE methods, providing benchmarks for approximate theories and a theoretical foundation for understanding neural coding in noisy neurons.

### Neural Mass Models and Stochastic Analysis

The [[mean field theory]] of neural networks naturally leads to [[neural mass model]]描述 that require stochastic analysis. When population-level equations include noise terms (arising from finite-size effects or external variability), the FPE describes how probability distributions evolve, enabling analysis of noise-induced transitions between attractor states, synchronization phenomena, and the stability of rhythmic activity. This framework is essential for understanding how stochasticity shapes dynamics in [[epilepsy-modeling]] and other pathological states.

## Relationship to Stochastic Differential Equations

The Fokker-Planck equation and stochastic differential equations provide complementary descriptions of the same underlying stochastic dynamics. An SDE specifies how individual sample paths evolve—a microscopic, trajectory-level description that is intuitively accessible but computationally expensive to analyze. The corresponding FPE specifies how the entire probability distribution evolves—a macroscopic, ensemble-level description that enables direct computation of moments, stationary distributions, and escape probabilities without generating many sample paths. The relationship is formalized by the Feynman-Kac formula and various representation theorems: solutions to the FPE can be constructed as expectations over ensembles of SDE trajectories, while SDE sample paths can be generated via Monte Carlo simulation of the corresponding FPE. [[computational-neuroscience]] applications often exploit both viewpoints, using SDE simulation for [[model-validation]] and FPE analysis for insight into long-term behavior and parameter dependencies.

## Related Concepts

The Fokker-Planck equation sits at the intersection of several foundational frameworks in theoretical neuroscience. It provides the probabilistic foundation for [[stochastic differential equations]] used to model neural dynamics with noisy inputs. The population density approach connects directly to [[mean-field-theory]], which provides averaged descriptions of neural ensembles. In the context of [[whole-brain modeling]], the FPE enables analysis of how stochastic fluctuations in local populations propagate through large-scale brain networks governed by [[structural connectivity]]. The equation also connects to [[bifurcation-analysis]] in [[nonlinear-dynamics]], as noise can fundamentally alter bifurcation behavior and transition dynamics in neural systems. Tools like [[nest]] and Brian2 implement stochastic neural simulations whose mean-field population dynamics can be analyzed through FPE methods, providing a bridge between detailed spiking networks and [[neural mass model]] approximations.

---

## References

1. (authors unknown). *The Fokker-Planck Equation: Methods of Solution and Applications*.
2. (authors unknown). *Stochastic Methods: A Handbook for the Natural and Social Sciences*.
3. (authors unknown). *Introduction to Theoretical Neurobiology: Volume 2, Nonlinear and Stochastic Theories*.
4. Roxana A. Stefanescu, Viktor K. Jirsa. *A low dimensional description of globally coupled heterogeneous neural networks of excitatory and inhibitory neurons*. PLoS Computational Biology. [DOI](](https://doi.org/10.1371/journal.pcbi.1000219))
5. Coşkun Çetin, Jose Roberto Castilho Piqueira, Burhaneddin İzgi̇, Ayşe Peker-Dobie, Semra Ahmetolan, Murat Özkaya. (2026). *Deterministic, stochastic, and mean-field PDE models in neuroscience*. Frontiers in Computational Neuroscience. [DOI](](https://doi.org/10.3389/fncom.2026.1762692))
6. Coskun Çetin, J.R.C. Piqueira, Burhaneddin Izgi, Ayse Peker-Dobie, S. Ahmetolan, Murat Özkaya. (2026). *Deterministic, stochastic, and mean-field PDE models in neuroscience*. Frontiers in Computational Neuroscience. [DOI](](https://doi.org/10.3389/fncom.2026.1762692))
7. Hugh R. Wilson, Jack D. Cowan. *Excitatory and inhibitory interactions in localized populations of model neurons*. Biophysical Journal. [DOI](https://doi.org/10.1016/S0006-3495(72)86068-5)
8. Preksha Girish, Rachana Mysore, Mahanthesha U, Shrey Kumar, Misbah Fatimah Annigeri, Tanish Jain. (2025). *Geometric-Stochastic Multimodal Deep Learning for Predictive Modeling of SUDEP and Stroke Vulnerability*. [Link](](https://arxiv.org/abs/2512.08257))
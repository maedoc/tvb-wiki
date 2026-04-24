---
title: Fokker‑Planck Equation
created: 2026-04-20
updated: 2026-04-24
type: concept
tags: [neural-mass-models, whole-brain-modeling, stochastic-differential-equations, mean-field-theory, dynamical-systems-theory, parameter-estimation, nonlinear-dynamics]
sources: [raw/papers/risken-1989.md, raw/papers/gardiner-2009.md, raw/papers/tuckwell-1988.md]
---

## Definition

The Fokker‑Planck equation (also known as the forward Kolmogorov equation) is a partial differential equation that describes the time evolution of the probability density function of a stochastic process. For a system governed by a stochastic differential equation (SDE), the Fokker‑Planck equation provides a deterministic description of how the probability density spreads and drifts over time, offering an alternative to Monte Carlo simulation of many individual trajectories.

## Motivation and Context

Much of computational neuroscience — and whole‑brain modeling in particular — deals with systems whose dynamics are influenced by noise. Neurons receive stochastic synaptic inputs, ion channels open and close randomly, and finite‑size effects introduce fluctuations in population activity. Simulating a single SDE trajectory tells us what one possible realization of the system looks like, but it cannot directly reveal the full distribution of possible states or the probability of rare events. The Fokker‑Planck equation solves this problem by evolving the entire probability density function, making it possible to compute stationary distributions, first‑passage times, and noise‑induced transitions analytically or semi‑analytically.

Within the framework of [[whole-brain]] modeling platforms like [[tvb]], the Fokker‑Planck equation underpins **population density methods** that replace expensive Monte Carlo simulations of thousands of spiking neurons with a single PDE representing the distribution of membrane potentials across a neural population. This dramatically reduces computational cost while preserving the stochastic nature of neural activity.

## Mathematical Formulation

### General Form

For a scalar stochastic process *x*(*t*) driven by the Langevin equation

\[
dx = \mu(x,t)\,dt + \sqrt{2D(x,t)}\,dW
\]

where *dW* is a Wiener increment, the associated Fokker‑Planck equation for the probability density *p*(*x*,*t*) is

\[
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\big[\mu(x,t)\,p\big] + \frac{\partial^2}{\partial x^2}\big[D(x,t)\,p\big].
\]

The first term is the **drift** — it captures the deterministic flow of probability density with velocity μ(*x*,*t*). The second term is the **diffusion** — it represents the spreading of probability due to noise, with diffusion coefficient *D*(*x*,*t*). The equation is a **conservation law** for probability: the integral of *p* over all *x* remains equal to one at all times.

For multidimensional systems — such as coupled neural populations in a whole-brain model — the same structure generalizes to a vector drift and a diffusion matrix, yielding a partial differential equation in as many dimensions as the state space.

### Population Density Form in Neuroscience

When applied to a homogeneous population of spiking neurons, the probability density *p*(*v*,*t*) represents the fraction of neurons whose membrane potential is near *v* at time *t*. The drift term captures the subthreshold dynamics (e.g., leaky integration), and the diffusion term captures fluctuations from random synaptic bombardment. The firing rate of the population emerges from the flux of probability crossing the spike threshold — a **boundary condition** that removes probability at threshold and re‑injects it at the reset potential.

This approach, detailed by [[emanuel-tuckwell]] (1988) and extended by later authors working with [[hannes-risken]]'s techniques, yields **exact macroscopic equations** for the population dynamics under certain conditions, bridging the gap between [[spiking-neural-networks]] and [[neural-mass-model]] descriptions.

## Solution Methods

### Analytical Techniques

For Fokker‑Planck equations with constant drift and diffusion coefficients, closed‑form solutions often exist in terms of Gaussian densities. For more complex cases, [[hannes-risken]]'s definitive reference (1989) catalogues several analytical strategies:

- **Eigenfunction expansions**: Decompose the Fokker‑Planck operator into eigenfunctions of a Sturm–Liouville problem. The solution is then a sum of exponentially decaying modes, with eigenvalues giving relaxation timescales.
- **Fourier transforms**: Convert the PDE into an ordinary differential equation in Fourier space, useful for linear or weakly nonlinear drift fields.
- **Path integrals**: Represent the transition probability as a sum over all possible paths, connecting to the [[free-energy-principle]] framework.

### Numerical Methods

When analytical solutions are intractable — as is typical for nonlinear neural models — numerical methods are required:

- **Finite difference schemes**: Discretize the spatial domain (membrane potential) and time, then evolve the density forward using explicit or implicit time‑stepping. Upwind differencing is often needed to handle the drift term stably.
- **Matrix continued fractions**: A semi‑analytical technique championed by Risken that is particularly efficient for problems with periodic boundary conditions or piecewise‑linear drift.
- **Spectral methods**: Expand the solution in orthogonal polynomials (e.g., Hermite polynomials for Ornstein–Uhlenbeck processes), yielding exponential convergence for smooth solutions.

## Biological Grounding and Parameter Mapping

The parameters of a Fokker‑Planck equation for a neural population map directly onto biophysical quantities:

- **Drift coefficient μ(*v*)** encodes the subthreshold membrane dynamics — the leak conductance, synaptic reversal potentials, and external injected current. For a leaky integrate‑and‑fire neuron, μ(*v*) = −(*v* − *V*ₗₑₐₖ)/τₘ + *I*ₑₓₜ/*C*.
- **Diffusion coefficient *D*(*v*)** quantifies the intensity of fluctuations, typically proportional to the rate and amplitude of incoming spike trains. In the diffusion approximation, *D* = σ²/(2τₘ²) where σ² is the variance of the synaptic input.
- **Boundary conditions at threshold and reset** capture the spike‑and‑reset mechanism, converting probability flux into firing rate. This provides a direct link between the PDE solution and experimentally measurable observables such as [[bold-signal]] or [[eeg]] power spectra.

For [[personalized-brain-modeling]], subject‑specific parameters (e.g., connectivity strengths from [[diffusion-mri]], local time constants from [[eeg]]) can be used to tune the drift and diffusion coefficients, enabling the Fokker‑Planck framework to predict individual resting‑state functional connectivity.

## Relationship to SDEs

The Fokker‑Planck equation and the corresponding SDE are **equivalent descriptions** of the same stochastic process: the SDE generates sample paths, while the Fokker‑Planck equation evolves the probability density. This duality is the stochastic analogue of the relationship between Hamilton's equations and the Liouville equation in classical mechanics. The choice between them is pragmatic:

- Use SDEs (Monte Carlo) when the state space is high‑dimensional and the number of relevant variables is small compared to the dimensionality.
- Use the Fokker‑Planck equation when the state space is low‑dimensional but a full probability density is needed — for example, to compute escape rates, stationary distributions, or noise‑induced transitions in [[bifurcation-theory]] contexts.

## Related Concepts

- [[stochastic differential equations]] — Equivalent trajectory‑level formulation
- [[mean-field theory]] — Population‑level reduction that often produces Fokker‑Planck equations as the next order of approximation beyond deterministic mean field
- [[neural-mass-model]] — Application domain where Fokker‑Planck methods provide exact stochastic counterparts
- [[dynamical-systems-theory]] — Provides the bifurcation and stability analysis tools used alongside Fokker‑Planck descriptions
- [[nonlinear-dynamics]] — Noise‑induced transitions and escape rates analyzed via the Fokker‑Planck framework

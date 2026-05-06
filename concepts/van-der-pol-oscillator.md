---
created: 2026-04-20
sources:
- raw/papers/strogatz-1994.md
- raw/papers/semanticscholar-b299aa3db60e.md
- raw/papers/arxiv-2601.03796.md
tags:
- nonlinear-dynamics
- neural-mass-models
- brain-oscillations
- bifurcation-theory
- network-dynamics
- dynamical-systems-theory
title: Van der Pol Oscillator
type: concept
updated: '2026-05-06'
---

The Van der Pol oscillator is a classic nonlinear dynamical system that serves as a fundamental model in [[computational-neuroscience]] for understanding neural mass oscillations, collective brain dynamics, and bifurcations between different oscillatory regimes. Originally derived to describe electrical circuits with nonlinear damping, it has become one of the most extensively studied examples of a system exhibiting limit cycle oscillations with biologically realistic relaxation behavior.

## Definition and Mathematical Formulation

The Van der Pol oscillator is defined by the second-order ordinary differential equation:

$$\frac{d^2x}{dt^2} - \mu(1 - x^2)\frac{dx}{dt} + x = 0$$

where $x$ represents the dynamical variable (which in neuroscience contexts often corresponds to neural activity or membrane potential) and $\mu$ is a positive parameter controlling the nonlinearity and damping characteristics. When $\mu = 0$, the system reduces to a simple harmonic oscillator; for $\mu > 0$, the damping becomes negative for small amplitudes ($|x| < 1$) and positive for large amplitudes ($|x| > 1$), driving the system toward a stable limit cycle.

This equation can be reformulated as a system of two first-order equations by introducing $y = dx/dt$:

$$\frac{dx}{dt} = y$$
$$\frac{dy}{dt} = \mu(1 - x^2)y - x$$

The parameter $\mu$ controls the relaxation timescale relative to the oscillatory period. In the limit $\mu \gg 1$, the system exhibits characteristic relaxation oscillations where the trajectory alternates between two quasi-static phases (near the nullclines) and rapid transitions (crossing between branches). This relaxation behavior provides a qualitative analogy to the firing and refractory behavior of neural populations.

## Historical Context and Original Applications

The Van der Pol oscillator was originally developed by Dutch engineer Balthasar Van der Pol in the 1920s to model the behavior of vacuum tube circuits [[1]]. The phenomenon of **limit cycles**—isolated closed trajectories in phase space that attract nearby trajectories—was still being formalized at that time, and Van der Pol's work provided important empirical demonstrations of self-sustained oscillations in physical systems. The mathematical analysis of this system contributed significantly to the early development of [[bifurcation-theory]], particularly the identification of what is now called the Hopf bifurcation (though Andronov first characterized it more completely).

Steven Strogatz's textbook *Nonlinear Dynamics and Chaos* (1994) provides comprehensive coverage of phase plane analysis, nullclines, and bifurcation behavior in the Van der Pol system, establishing it as a pedagogical example throughout the nonlinear dynamics literature [[2]]. This textbook remains foundational for computational neuroscientists working with [[neural-mass-model]]s.

## Relevance to Whole-Brain Modeling

In [[whole-brain]] modeling, the Van der Pol oscillator serves multiple conceptual and practical roles. First, it provides a mathematically tractable prototype for understanding how individual brain regions can exhibit self-sustained oscillations and how these oscillations interact through [[structural-connectivity]]. The relaxation oscillation behavior captures essential features of neural population dynamics, including timescale separation between fast excitation and slower recovery processes.

Recent work on phase-dependent stimulation response has demonstrated that the brain's [[functional-connectivity]] state critically modulates the effects of external stimulation [[3]]. Computational models incorporating Van der Pol-like dynamics at the regional level show that stimulation effects depend on both the phase of ongoing oscillations and the transient network of functional connectivity at the stimulation time. This finding has implications for understanding [[brain-stimulation]] interventions in epilepsy modeling and other neurological conditions.

The data-driven framework for inferring brain dynamical states from correlation matrices, as described in recent work [[3]], tracks changes in collective dynamics under controlled variations of excitability—directly analogous to varying the $\mu$ parameter in the Van der Pol oscillator to move the system through different dynamical regimes.

## Relationship to Neural Mass Models

The [[epileptor]], a neural mass model widely used in TVB for simulating seizure dynamics, contains elements related to the Van der Pol oscillator's relaxation oscillation mechanism. The Epileptor model exhibits saddle-node and Hopf bifurcations that govern transitions between healthy and seizure-like states, and understanding the Van der Pol oscillator's bifurcation structure provides intuition for these more complex systems.

Similarly, the [[fitzhugh-nagumo-model]], a simplified model of neuronal excitability, can be viewed as a related relaxation oscillator that captures the essential dynamics of neural activation and recovery. The [[wong-wang-model]] and other mean-field models used in whole-brain simulations also exhibit oscillatory behavior that can be analyzed using the same theoretical tools developed for the Van der Pol system.

## Parameter Regimes and Bifurcation Behavior

The Van der Pol oscillator exhibits qualitatively different dynamics across parameter regimes. For small $\mu$ (typically $\mu < 1$), the oscillations are nearly sinusoidal with a period close to $2\pi$. As $\mu$ increases, the limit cycle transitions to relaxation oscillations with increasingly sharp jumps between the quasi-static branches. The amplitude of the limit cycle varies with $\mu$, approaching 2 for large values.

The system undergoes a **Hopf bifurcation** as $\mu$ crosses zero: the trivial fixed point $(x, y) = (0, 0)$ loses stability and gives birth to a stable limit cycle. This bifurcation structure—where a fixed point becomes unstable and generates oscillatory behavior—is directly relevant to understanding how brain dynamics transition between resting and active states.

The Van der Pol oscillator also admits analytic solutions in terms of elliptic functions and can be studied using Poincaré-Bendixson theory to prove the existence and uniqueness of the stable limit cycle for $\mu > 0$.

## Open Questions and Computational Considerations

Despite its long history, the Van der Pol oscillator continues to serve as a benchmark system for developing new analytical and numerical methods. In the context of [[whole-brain]] modeling, open questions include: How do networks of coupled Van der Pol oscillators approximate the dynamics of biologically realistic neural mass models? What novel collective behaviors emerge from coupling heterogeneous oscillatory units? How do delays in signal transmission between brain regions modify the bifurcation structure observed in single-unit systems?

For practical implementation, the Van der Pol oscillator can be integrated using standard numerical ODE solvers. In The Virtual Brain, the mathematical structure of relaxation oscillations informs the design of neural mass models and the analysis of collective brain dynamics. Software implementations are available in many computational environments, including Python's SciPy and various toolboxes for [[bifurcation-analysis]].

## See Also

- [[oscillator]] — General concept of oscillatory dynamics
- [[nonlinear-dynamics]] — Broader field of nonlinear system behavior
- [[bifurcation-analysis]] — Methods for studying qualitative changes in dynamical systems
- [[neural-mass-models]] — Population-level models of neural activity
- [[brain-oscillations]] — Neural oscillations in the living brain
- [[whole-brain-modeling]] — Large-scale brain network simulations
- [[epilepsy-modeling]] — Computational approaches to understanding seizures
- [[dynamical-systems-theory]] — Mathematical framework for studying change over time
- [[fitzhugh-nagumo-model]] — Related simplified neuron model
- [[network-dynamics]] — Dynamics of coupled neural systems

## References

1. (authors unknown). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
2. Sophie Benitez Stulz, Samy Castro, B. Gutkin, Mathieu Gilson, Demian Battaglia. (2026). *Phase-dependent stimulation response is shaped by the brain’s dynamic functional connectivity*. Network Neuroscience. [DOI](https://doi.org/10.1162/netn.a.548)
3. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796)
---
created: 2026-04-20
sources:
- raw/papers/strogatz-1994.md
- raw/papers/izhikevich-2007.md
tags:
- neural-mass-models
- nonlinear-dynamics
- bifurcation-analysis
- brain-oscillations
- dynamical-systems-theory
title: FitzHugh-Nagumo Model
type: concept
updated: '2026-05-06'
---

The FitzHugh-Nagumo model is a two-dimensional reduction of the four-dimensional [[hodgkin-huxley-model]] that captures the essential nonlinear dynamics of neural excitability. Originally proposed by Richard FitzHugh in 1961 and later formalized with J. Nagumo [strogatz-1994], this minimal model demonstrates how neurons transition between resting and spiking states through well-characterized bifurcations. The model's importance lies in its ability to reproduce the fundamental dynamical behaviors of excitable media—including excitability, [[brain-oscillations]], and spike generation—while requiring only two coupled nonlinear differential equations, making it amenable to analytical treatment and Phase plane analysis that would be intractable with more biophysically detailed formulations.

## Mathematical Formulation

The canonical form of the FitzHugh-Nagumo equations expresses the evolution of membrane potential v and a recovery variable w:

$$\frac{dv}{dt} = v - \frac{v^3}{3} - w + I_{\text{ext}}$$

$$\frac{dw}{dt} = \epsilon(v + a - bw)$$

where v represents dimensionless membrane potential, w represents a recovery variable capturing refractoriness or adaptation currents, I_ext is the external input current, and epsilon is a small positive parameter (typically 0.01-0.1) that establishes timescale separation between the fast voltage dynamics and slower recovery processes. The cubic term v - v³/3 in the voltage equation generates the characteristic nonlinearities that give rise to excitable behavior. The parameter a controls the position of the w-nullcline relative to the origin, while b determines its slope.

The phase portrait reveals an S-shaped v-nullcline (dv/dt = 0 gives w = v - v³/3 + I_ext) intersected by the linear w-nullcline (dw/dt = 0 gives w = (v + a)/b). The intersection(s) of these nullclines determine the system's equilibrium points, and the geometric arrangement of these intersections governs whether the neuron rests in a stable equilibrium, fires repetitive spikes as a limit cycle, or exhibits excitable responses to perturbations.

## Dynamical Behaviors and Bifurcations

The FitzHugh-Nagumo model exhibits a rich repertoire of behaviors that are central to understanding neural coding and pathological states. At low input currents, the system possesses a single stable equilibrium corresponding to the resting state. When I_ext increases beyond a critical threshold, the resting equilibrium undergoes a saddle-node bifurcation on an invariant circle (SNIC) [strogatz-1994], giving birth to a stable limit cycle that represents repetitive spiking. Further increases in current lead to the onset of [[andronov-hopf-bifurcation]] [strogatz-1994] where the limit cycle destabilizes, typically through a period-doubling cascade en route to chaos at very high inputs.

The concept of excitability threshold emerges naturally from this geometry: perturbations that displace the state across the separatrix (the unstable manifold of a saddle point) trigger a large-amplitude excursion in the phase plane—a spike—before returning to the resting equilibrium. This threshold behavior parallels the all-or-none spiking observed in real neurons. The model's bifurcation structure aligns precisely with the classification of neuronal excitability types provided in [[izhikevich]] work on [[bifurcation analysis]] of neural dynamics [izhikevich-2007].

## Relationship to Other Neuronal Models

The FitzHugh-Nagumo model occupies a central position in the hierarchy of neuronal models. It can be derived systematically from the [[hodgkin-huxley-model]] through a series of reductions: first applying quasi-active cable theory to reduce spatial dynamics, then employing singular perturbation theory to exploit timescale separation between fast sodium/potassium dynamics and slower gating variables. The result captures the essential voltage-dependent nonlinearities while discarding ionic specifics.

Compared to the [[izhikevich-neuron-model]], which was developed to reproduce the rich diversity of cortical neuron firing patterns with just two variables, the FitzHugh-Nagumo model emphasizes the universal excitability mechanism rather than firing pattern variety. The [[wilson-cowan-model]] and other [[neural-mass-models]] extend similar reductionist principles to population-level dynamics, where the effective nonlinearity emerges from pooling many neurons. The [[epileptor]] model used in [[epilepsy-modeling]] directly builds upon FitzHugh-Nagumo dynamics to generate seizure-like oscillations.

## Biological Relevance and Limitations

The model's greatest strength—its mathematical tractability—also constitutes its primary limitation from a biological realism standpoint. The abstract recovery variable w does not correspond to any single ionic current; instead, it represents a lumped combination of potassium currents, calcium-activated potassium currents, and adaptation currents. Consequently, the model cannot reproduce the rich firing patterns (tonic, bursting, chattering) exhibited by neocortical neurons, and its spike waveform lacks the detailed morphology of Hodgkin-Huxley action potentials.

Nevertheless, the FitzHugh-Nagumo model captures the fundamental dynamical essence of excitability: the interplay between fast positive feedback (the regenerative sodium current) and slower negative feedback (potassium-mediated repolarization) that enables reliable spike generation. This simplification has proven invaluable for understanding the biophysical basis of neural coding, [[brain-stimulation]] effects, and [[epilepsy-modeling]] transitions between healthy resting states and pathological oscillatory regimes.

## Integration with Whole-Brain Modeling

In [[whole-brain-modeling]] frameworks like [[the-virtual-brain]], population-level dynamics often employ reduced models that share conceptual ancestry with the FitzHugh-Nagumo approach. The [[neural-mass-model]] formulations used in TVB—including [[jansen-rit-model]] and variations—embed similar excitable dynamics within mean-field approximations. Understanding the bifurcation structure of FitzHugh-Nagumo provides crucial intuition for interpreting parameter sensitivity in these larger-scale models: many brain region models exhibit transitions between resting, oscillatory, and seized states that parallel the single-neuron bifurcations analyzed in the FitzHugh-Nagumo framework.

The [[bifurcation-analysis]] techniques applied to FitzHugh-Nagumo extend naturally to whole-brain simulations, where researchers investigate how parameter changes in local dynamics propagate through [[structural-connectivity]] to affect network-level stability. This connection between single-neuron reduced models and population-level whole-brain simulations exemplifies the multi-scale nature of computational neuroscience.

## Open Questions and Extensions

Despite its age, the FitzHugh-Nagumo model continues to inform research on neural dynamics. Open questions include: how stochasticity modifies bifurcation transitions in biologically realistic noise regimes, how network coupling between multiple FitzHugh-Nagumo units gives rise to synchronized population oscillations, and how the model's insights might inform refined approaches to [[personalized-brain-modeling]] where individual parameter variations capture clinical heterogeneity. Extensions incorporating multiple time scales, noise, and coupling have kept the model relevant for addressing contemporary questions in [[computational-neuroscience]] and [[brain-dynamics]].

## References

1. (authors unknown). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
2. Eugene M. Izhikevich. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.
---
created: 2024-01-15
sources:
- raw/papers/arxiv-2508.04824.md
- raw/papers/touboul-2011.md
- raw/papers/breakspear-2006.md
- raw/papers/arxiv-2512.22093.md
- raw/papers/izhikevich-2007.md
tags:
- epilepsy-modeling
- bifurcation-analysis
- neural-mass-models
- dynamical-systems-theory
- nonlinear-dynamics
- whole-brain-modeling
title: Epileptor Codimension-3
type: concept
updated: '2026-04-30'
---

The Epileptor Codimension-3 is a reduced mathematical model that captures the complete bifurcation structure underlying seizure onset, propagation, and termination in the Epileptor framework. Developed through a systematic codimension-3 bifurcation analysis, this model serves as an organizing center that unifies all previously observed seizure-like transitions within a single mathematical framework. Unlike the original six-dimensional Epileptor, which captures multiple dynamical regimes but required separate analyses to understand transitions between them, the Codimension-3 unfolding reveals how saddle-node, Hopf, and homoclinic bifurcations emerge from a single degenerate critical point—the Degenerate Bogdanov-Takens point—thereby providing a complete portrait of seizure dynamics in a minimal coordinate system.

## Motivation and Clinical Context

The development of the Epileptor Codimension-3 was motivated by a fundamental limitation in the analysis of epilepsy models: previous Bifurcation Analyses of neural mass models such as the Jansen-Rit model and the original Epileptor had identified individual bifurcation scenarios in isolation, but lacked a unified framework to understand how these scenarios relate to each other and transitions between them. Clinically, this matters because epileptic seizures exhibit diverse dynamical signatures—from gradual onset via slow buildup of activity to abrupt onset with oscillatory components—and understanding this variability is essential for developing personalized treatment strategies. The codimension-3 analysis provides exactly this unifying perspective by identifying the organizing center from which all seizure-relevant dynamical behaviors emerge as one varies the underlying parameters.

The work draws on the mathematical tradition of catastrophe theory and unfolding theory, particularly the seminal contributions to [[bifurcation-theory]] that characterize how qualitative changes in dynamical systems depend on parameters. By showing that the Epileptor possesses a degenerate point of codimension-3, Saggio et al. demonstrated that this single mathematical object contains within it an entire "dictionary" of seizure patterns previously thought to require distinct mechanisms.

## Mathematical Foundation

### The Degenerate Bogdanov-Takens Point

The organizing center of the Epileptor Codimension-3 is a **Degenerate Bogdanov-Takens (DBT) point**—a degenerate equilibrium where the linearization of the vector field has a double zero eigenvalue with nilpotent part. At this critical point in parameter space, three distinct bifurcation curves collide: the saddle-node bifurcation (marking seizure onset through the appearance of a fixed point pair), the subcritical Hopf bifurcation (marking the birth of oscillatory seizure activity), and the homoclinic bifurcation (marking seizure termination through the collision of a periodic orbit with a saddle point).

The codimension-3 unfolding refers to the generic perturbation of this degenerate point in a three-dimensional parameter space (μ₁, μ₂, μ₃), where the three parameters capture different aspects of the neural excitability that can be modulated biologically—by pharmacological intervention, by stimulation protocols, or by disease-related changes in synaptic balance. This unfolding is universal: any system exhibiting a DBT point of this type will share the same qualitative bifurcation structure, up to smooth coordinate changes.

### The Normal Form Equations

The reduced normal form captures the essential dynamics near the DBT point and can be expressed in simplified form as a two-dimensional system:

$$\frac{dx}{dt} = y$$

$$\frac{dy}{dt} = \mu_1 + \mu_2 \cdot x + \mu_3 \cdot y + x^2 + x \cdot y$$

Here, the variable x represents a coarse-grained measure of the system's state (equivalent to the population activity in simplified Epileptor variables), while y represents its time derivative. The parameters μ₁, μ₂, and μ₃ govern the distance and orientation relative to the degenerate point. When all three parameters are zero, the system sits exactly at the DBT point; as parameters vary, the system moves through different regions of the bifurcation diagram, exhibiting qualitatively different dynamical behaviors.

## Bifurcation Scenarios and Biological Interpretation

The codimension-3 unfolding generates four principal dynamical regimes that correspond to clinically observed seizure patterns:

The **Saddle-Node/Homoclinic** scenario represents the most common seizure pattern, characterized by a gradual buildup of activity (the "pre-ictal" phase) followed by seizure onset at the saddle-node bifurcation and termination via homoclinic collision. This corresponds to the typical temporal evolution of a generalized tonic-clonic seizure, where the system slowly approaches the seizure state through parameter drift (perhaps due to accumulating excitation or decreasing inhibition) and then exits abruptly.

The **Subcritical Hopf** scenario produces abrupt seizure onset with bistability between a resting fixed point and an oscillatory seizure state. This dynamical regime may underlie sudden-onset seizures, including certain absence seizures, where the system exhibits hysteresis and the seizure can be triggered by small perturbations once parameters cross a threshold.

The **Saddle-Node Loop** scenario generates very brief paroxysmal events—rapid bursts of activity that appear and disappear without sustained seizure states. These may correspond to interictal spikes or very brief epileptiform events observed in intracranial recordings.

The **Shilnikov** scenario produces irregular spike-and-wave complexes characteristic of absence seizures, where the homoclinic orbit gives rise to chaotic dynamics through the Shilnikov mechanism—a mathematical result guaranteeing the existence of chaotic attractors near homoclinic orbits under certain conditions.

## Comparison to Related Models

The Epileptor Codimension-3 represents a significant simplification from the original six-dimensional Epileptor while preserving the essential bifurcation structure. Where the Epileptor captures multiple cell types (pyramidal cells, interneurons, fast and slow dendritic compartments) with biophysically interpretable parameters, the Codimension-3 trades this biological specificity for mathematical tractability, retaining only the minimal structure needed to reproduce the organizing center of seizure dynamics.

This reduction is complementary to other approaches in the field, such as the bifurcation analysis of the [[jansen-rit]] model conducted by Touboul et al. (2011), which mapped parameter regimes to observable brain rhythms (alpha oscillations, epileptic Activity). Both approaches share the goal of connecting mathematical structure to clinical phenomenology, but differ in their starting points: the Jansen-Rit analysis begins with a biologically detailed cortical model and explores its parameter space, while the Epileptor Codimension-3 begins from the observed seizure phenomenology and discovers the minimal mathematical structure that can generate it.

## Relation to Whole-Brain Modeling

In the context of [[whole-brain-modeling]], the Epileptor Codimension-3 provides a canonical unit that can be embedded in large-scale brain networks to study how seizure-like activity propagates through [[structural-connectivity]]. Recent work by Triebkorn et al. (2025) demonstrates how delay-constrained re-entry in Epileptor networks can generate self-sustaining seizure dynamics that match clinical observations in terms of frequency and duration. The Codimension-3 framework offers a systematic way to understand how parameters governing individual node dynamics interact with the delay structure of the network to produce the observed seizure patterns—linking the local bifurcation analysis to the emergent network-level phenomena.

## Open Questions and Future Directions

A central challenge remaining is the mapping between the abstract parameters of the codimension-3 unfolding (μ₁, μ₂, μ₃) and biologically measurable quantities that can be estimated from patient data. Current work on [[personalized-brain-modeling]] aims to bridge this gap by combining [[parameter-estimation]] techniques from empirical [[neuroimaging]] data with the bifurcation analysis framework. Additionally, the extension of this analysis to consider the effects of noise—which is unavoidable in biological neural systems—and to incorporate the slow timescale variables that regulate seizure state transitions remains an active area of theoretical development.

The Epileptor Codimension-3 thus stands as a prime example of how sophisticated mathematical analysis can simplify rather than obscure biological reality, providing a unifying framework that clarifies the relationship between diverse seizure phenomenologies and their underlying dynamical mechanisms.

## Related Concepts

- [[epileptor]] - The original 6D model from which this reduced model derives
- [[bifurcation-analysis]] - The mathematical methodology underlying the model derivation
- [[bifurcation-theory]] - The broader mathematical framework including catastrophe theory
- [[epilepsy-modeling]] - Clinical applications of computational epilepsy models
- [[dynamical-systems-theory]] - Theoretical foundation for understanding neural dynamics
- [[neural-mass-models]] - Class of models to which Epileptor belongs
- [[jansen-rit]] - Related neural mass model with comparable bifurcation analysis
- [[whole-brain-modeling]] - Network-level modeling context for clinical applications
- [[tvb]] - Software platform for [[whole-brain]] simulations using Epileptor

## References

1. Paul Triebkorn, Huifang E. Wang, Marmaduke Woodman, Maxime Guye, Fabrice Bartolomei, Viktor Jirsa. (2025). *Delay-constrained re-entry governs large-scale brain seizures and other network pathologies*. [Link](https://arxiv.org/abs/2508.04824)
2. Jonathan Touboul, Fabien Wendling, Bruno Bellanger, Patrick Chauvel, Olivier Faugeras. *Bifurcation analysis of Jansen's neural mass model*. Neural Computation. [DOI](https://doi.org/10.1162/NECO_a_00151)
3. Michael Breakspear, John A. Roberts, John R. Terry, Stefano Rodrigues, Nader Mahmud, Philip Robinson. *Large-scale brain dynamics of seizures: asymptotic analysis of a neural field model*. Journal of Computational Neuroscience. [DOI](https://doi.org/10.1007/s10827-006-8135-2)
4. Jeremy B. Goetz, Naruepon Weerawongphrom, Rashid V. Williams-García, John M. Beggs, Gerardo Ortiz. (2025). *A Minimal Network of Brain Dynamics: Hierarchy of Approximations to Quasi-critical Neural Network Dynamics*. [Link](https://arxiv.org/abs/2512.22093)
5. Eugene M. Izhikevich. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.
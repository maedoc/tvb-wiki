---
title: Epileptor Model
created: 2024-01-15
updated: 2026-04-24
type: concept
tags: [neural-mass-models, epilepsy-modeling, bifurcation-analysis, dynamical-systems-theory, whole-brain-modeling, brain-stimulation, personalized-brain-modeling, network-dynamics]
sources: [raw/papers/arxiv-2508.04824.md, raw/papers/arxiv-2603.25991.md, raw/papers/breakspear-2006.md]
---

The Epileptor is a composite neural mass model specifically designed to capture the full phenomenology of epileptic seizures—including onset, propagation, and termination—within a mathematically tractable framework. Developed by Jirsa and colleagues (2014), it represents one of the most successful attempts to reduce the complex, multi-scale dynamics of seizure generation into a low-dimensional dynamical system that can be analyzed analytically and simulated numerically. Unlike earlier neural mass models such as the [[jansen-rit]] model or [[wilson-cowan]] equations, which were designed primarily to reproduce rhythmic brain activity in healthy states, the Epileptor was explicitly constructed to exhibit the characteristic abrupt transitions between interictal (baseline), pre-ictal, and ictal (seizure) states that define the epilepsy phenotype. This makes it a cornerstone of contemporary [[epilepsy-modeling]] research and a key component of patient-specific [[whole-brain]] simulations in platforms like [[the-virtual-epileptic-brain]].

## Motivation and Clinical Context

The development of the Epileptor was driven by a fundamental challenge in epilepsy research: seizures are inherently dynamical systems phenomena—abrupt, nonlinear transitions between quasi-stable states—yet the dominant modeling approaches in the early 2000s treated them as either simple oscillatory patterns or stochastic point processes. Earlier work by [[breakspear]] and colleagues (2006) had demonstrated that spatially distributed versions of the [[jansen-rit]] model could reproduce certain seizure features through bifurcation analysis, but these models lacked the specific dynamical architecture needed to capture the full seizure cycle. The Epileptor was designed to address this gap by combining two coupled subsystems that represent distinct physiological processes during seizure generation: a fast excitatory population capturing the ictal discharge, and a slower subcortical population capturing modulatory and inhibitory processes that influence seizure onset and termination. This architecture enables the model to reproduce the key signatures of focal seizures—including pre-ictal spiking, the rapid transition into sustained rhythmic activity (the ictal phase), and post-ictal suppression—that are observable in intracranial EEG recordings from epilepsy patients.

## Mathematical Architecture

The Epileptor comprises two coupled dynamical systems operating on different timescales. **Population 1** (the fast system) captures the main epileptic activity through variables x₁ (membrane potential), y₁ (recovery variable), and z (a slow permittivity variable that tracks cumulative excitability). The equations are:

```
ẋ₁ = y₁ - f₁(x₁, z) + I_ext₁ + K_vf·c_pop₁
ẏ₁ = c - d·x₁² - y₁
ż = r·(4(x₁ - x₀) - z + K_s·c_pop₁)
```

where f₁(x₁, z) is a nonlinear function capturing the sodium channel inactivation threshold. **Population 2** (the slower system) represents subcortical inhibition through variables x₂ and y₂, coupled to Population 1 through the variable g. The full system displays rich bifurcation behavior as the excitability parameter x₀ is varied, enabling transitions between the three canonical dynamical regimes. The output signal (simulating the intracranial EEG) is computed as the difference between the two populations: Output = -x₁ + x₂.

## Dynamical Regimes and Bifurcation Structure

The Epileptor exhibits three well-defined dynamical regimes that map directly onto the clinical phenomenology of focal epilepsy. In the **interictal regime** (x₀ < -2.0), the system rests at a stable fixed point, producing the low-amplitude background activity typical of between-seizure periods. As x₀ increases toward the **pre-ictal transition** (-2.0 < x₀ < -1.5), the system enters a regime of intermittent burst firing—brief epileptiform events separated by relatively long periods of quiescence. This mimics the clinical observation of pre-ictal spikes and is associated with a subcritical Hopf bifurcation in the mathematical structure. Once x₀ exceeds the ictal threshold (x₀ > -1.5), the system undergoes a saddle-node bifurcation onto a limit cycle, producing the sustained rhythmic high-frequency activity (the ictal phase) that characterizes an ongoing seizure. The **slow permittivity variable z** plays a crucial role in mediating the transition back to the interictal state: as it accumulates during the ictal phase, it eventually pushes the system back across the bifurcation point, terminating the seizure. This self-limiting property is a key feature of the model and reflects the intrinsic regulatory mechanisms (such as synaptic depression, ion channel inactivation, and active inhibition) that terminate most seizures without external intervention. The analysis of these bifurcations relies on the tools of [[bifurcation-theory]] and [[dynamical-systems-theory]].

## Network Extensions and Patient-Specific Modeling

While the original Epileptor is a lumped (zero-dimensional) model, it has been extensively extended to network configurations for [[whole-brain]] modeling. In this formulation, individual brain regions are populated with Epileptor neural fields, and the coupling between regions is determined by [[structural-connectivity]] matrices derived from diffusion MRI tractography. This approach, exemplified by recent work using the [[the-virtual-epileptic-brain]] framework, has revealed that **delay-constrained re-entry**—self-sustaining activity loops mediated by realistic cortico-cortical conduction delays—is a fundamental mechanism governing large-scale seizure propagation (Triebkorn et al., 2025). Patient-specific models constructed from individual diffusion MRI data show that the interaction between anatomical connectivity and intrinsic Epileptor excitability predicts both seizure frequency and duration across populations of recorded seizures, demonstrating the clinical utility of personalized brain modeling. These network extensions transform the Epileptor from a phenomenological model of a single seizure focus into a tool for understanding seizure dynamics across the entire brain.

## Control and Neuromodulation

A recent and rapidly developing application of the Epileptor is in **closed-loop seizure control** using passivity-based control (PBC) theory (Acharya & Nozari, 2026). Traditional open-loop stimulation approaches (such as vagus nerve stimulation or responsive neurostimulation) deliver stimuli regardless of the brain's dynamical state, often with limited efficacy—only approximately 18% of patients with drug-resistant epilepsy achieve seizure freedom with current closed-loop systems. The PBC framework applied to the Epileptor provides rigorous mathematical analysis demonstrating that seizure dynamics can be stabilized by sufficiently strong passive feedback, and that seizure termination is phase-dependent—meaning that the timing of stimulation relative to the seizure cycle critically determines whether a stimulus aborts or even exacerbates ongoing activity. This work connects the Epileptor to broader themes in [[brain-stimulation]] and provides a theoretically grounded framework for **precision neuromodulation** that could substantially improve clinical outcomes. The phase-dependent termination rules identified in silico have been validated against intracranial recordings from epilepsy patients, suggesting a direct path toward clinical translation.

## Relationship to Other Models

The Epileptor occupies a specific niche in the landscape of [[neural-mass-models]]: it is more biophysically detailed than reduced models like the [[wilson-cowan]] equations or [[wong-wang]] model, yet simpler than large-scale [[spiking-neural-networks]] like those implementable in [[nest]] or [[brian2]]. Variants include the **[[epileptorcodim3]]** model, which extends the original to a codimension-3 bifurcation analysis for exploring the full space of seizure onset mechanisms, and the **[[epileptor-rs]]** variant designed for integration with resting-state functional connectivity data. Compared to the earlier neural field models of [[breakspear]] (2006), which focused on primary generalized seizures and spatial propagation, the Epileptor emphasizes the dynamical architecture of seizure onset and termination at the single-focus level—a focus that has proven remarkably productive for clinical applications.

## Open Questions

Despite its successes, the Epileptor model leaves several important questions open. The precise biological interpretation of the slow permittivity variable z remains debated—it likely represents a compound metric of synaptic depression, afterhyperpolarization, and metabolic factors, but no single physiological measurement directly maps onto it. Network-level extensions require increasingly sophisticated parameter estimation methods to fit individual patient models, and the relationship between the model's bifurcation parameters (particularly x₀) and clinically measurable quantities (such as the seizure onset zone in intracranial EEG) is still being refined. Recent work on PBC suggests that phase-dependent stimulation protocols could substantially improve outcomes, but translating these findings from in silico demonstrations to clinical practice requires validation in prospective patient studies.

## Related Concepts

- [[epilepsy-modeling]] - General framework for computational epilepsy research
- [[neural-mass-model]] - Theoretical foundation of the Epileptor
- [[bifurcation-analysis]] - Mathematical tools for understanding seizure transitions
- [[dynamical-systems-theory]] - Broader mathematical context
- [[epileptorcodim3]] - Extended bifurcation analysis variant
- [[epileptor-rs]] - Resting-state integration variant
- [[whole-brain]] - Network-level modeling context
- [[the-virtual-epileptic-brain]] - Clinical simulation platform
- [[personalized-brain-modeling]] - Patient-specific applications
- [[brain-stimulation]] - Therapeutic modulation approaches

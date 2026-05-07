---
created: 2024-01-15
sources:
- raw/papers/smith-2013-hcp.md
- raw/papers/deco-2013.md
- raw/papers/power-2011.md
- raw/papers/biswal-1995.md
tags:
- resting-state
- neuroimaging-fmri
- functional-connectivity
- network-dynamics
- whole-brain-modeling
- computational-neuroscience
title: REST (Resting State)
type: concept
updated: '2026-05-07'
---

# REST (Resting State)

**REST**, in the context of brain imaging and computational neuroscience, refers to the resting state—a condition in which a subject is awake but not engaged in an explicit task or stimulus. The study of resting-state brain activity has revolutionized our understanding of the brain's intrinsic organization, revealing that the brain at rest is not idle but rather continuously active in coordinated patterns that reveal the underlying architecture of [[functional-connectivity]] and [[structural-connectivity]] [Smith et al., 2013]. This concept has become fundamental to [[whole-brain-modeling]] because spontaneous fluctuations during rest provide data for constraining computational models of neural dynamics.

The modern era of resting-state neuroscience began with the discovery that spatially distant brain regions show correlated spontaneous fluctuations in [[fmri]] blood-oxygen-level-dependent (BOLD) signal, even when subjects are not performing any task. This finding, first demonstrated systematically by Biswal and colleagues (1995) [Biswal et al., 1995], revealed the existence of coherent [[intrinsic-connectivity-networks]] that are present during wakeful rest. The most prominent of these is the [[default-mode-network]], originally described by Raichle and colleagues as a set of brain regions that show higher activity at rest than during task performance, suggesting a fundamental role in internal cognition and brain maintenance.

## Computational Modeling of Resting State

Computational approaches to understanding resting-state activity have made significant contributions by revealing the mechanisms from which spontaneous fluctuations emerge. The work by Deco, Jirsa, and McIntosh (2013) [Deco et al., 2013] demonstrated, using large-scale neural mass models, that noise-driven fluctuations in a structured network—constrained by empirical structural connectivity derived from diffusion imaging—can reproduce empirical resting-state functional connectivity patterns. Their framework emphasized that resting-state dynamics arise from the interaction between the anatomical scaffold provided by white matter tracts and the stochastic activity inherent to neural systems, with the brain continuously exploring a repertoire of functional states that overlap substantially with patterns evoked during task performance [Deco et al., 2013].

The relationship between [[structural-connectivity]] and resting-state [[functional-connectivity]] is neither deterministic nor trivial. While structural connections provide the necessary substrate for functional coupling, the mapping from anatomy to function is highly nonlinear. Honey and colleagues (2009) demonstrated that structural connectivity explains only a portion of the variance in functional connectivity, with the remainder arising from dynamic interactions and shared input. This insight has been incorporated into [[whole-brain-modeling]] frameworks that use empirical structural connectivity matrices—typically derived from [[neuroimaging-dti]] or tractography—as the primary constraint for simulating resting-state dynamics. The work by Smith and colleagues (2013) in the [[human-connectome-project]] provided high-resolution maps of resting-state networks in over 200 subjects, establishing reference datasets that computational models can be validated against [Smith et al., 2013].

## Network Organization at Rest

Power and colleagues (2011) provided a comprehensive mapping of the human brain's [[network-dynamics]] organization using resting-state [[neuroimaging-fmri]], identifying major functional systems including the default mode, attention, sensorimotor, and visual networks [Power et al., 2011]. Their work demonstrated that the brain's functional organization at rest is modular and hierarchical, with distinct networks serving different computational purposes. This characterization has been crucial for developing parcelation schemes used in [[whole-brain-modeling]], where the brain is typically parcellated into 50-500 regions based on either anatomical landmarks or functional boundaries.

## Methodological Considerations

Several methodological debates continue to shape resting-state research. Global signal regression remains controversial, as it can effectively remove structured noise (cardiac, respiratory) but may also eliminate valid neural signal of whole-brain origin [Power et al., 2011]. Motion artefacts pose significant challenges, particularly in clinical populations where head motion is often increased; strategies such as scrubbing and framewise displacement censoring have become standard preprocessing steps [Power et al., 2011]. Additionally, the influence of physiological confounds—including respiration and cardiac pulsation—on resting-state BOLD fluctuations continues to be refined through improved acquisition protocols and denoising strategies.

## Clinical Applications

The computational significance of REST extends beyond basic science into clinical applications. Alterations in resting-state functional connectivity have been identified in numerous neurological and psychiatric conditions, including Alzheimer's disease, schizophrenia, and epilepsy. In the context of [[epilepsy-modeling]], resting-state activity provides the baseline from which pathological dynamics such as seizures emerge [Deco et al., 2013]. Beyond epilepsy, resting-state markers are being explored as biomarkers for early detection and prognosis in neurodegenerative disorders and as targets for therapeutic intervention. The ability to simulate resting-state dynamics with biologically realistic models, such as those implemented in [[the-virtual-brain]], enables personalized predictions of brain dynamics and the effects of interventions like [[brain-stimulation]].

## Relationships to Related Concepts

REST provides the foundational brain state for several related concepts in this wiki. [[Resting-state-fmri]] is the primary neuroimaging modality used to measure resting-state activity, while [[resting-state-vs-task-fmri]] explores how task conditions modulate intrinsic connectivity patterns. The [[default-mode-network]] is the most studied resting-state network, and [[intrinsic-connectivity-networks]] encompasses the broader class of coordinated activity patterns observed at rest. [[Functional-connectivity]] is the statistical framework used to quantify relationships between brain regions during REST, and [[network-dynamics]] describes the time‑varying patterns of connectivity that emerge from resting‑state activity.

## Open Questions

Despite substantial progress, fundamental questions remain about the biological significance of resting‑state activity and its relationship to cognition. Whether resting‑state fluctuations primarily reflect ongoing processing, passive maintenance of neural circuitry, or emergent properties of neural architecture remains debated. The field continues to advance through combinations of improved neuroimaging at higher temporal and spatial resolution, more sophisticated computational models, and rigorous validation against empirical data.

## References

1. (authors unknown). *Resting-State fMRI in the Human Connectome Project*.
2. Deco et al. (2013). *Resting brains never rest: computational insights into potential cognitive architectures*. Trends in Neurosciences. [DOI](https://doi.org/10.1016/j.tins.2013.09.002)
3. (authors unknown). *Functional Network Organization of the Human Brain*.
4. (authors unknown). *Functional connectivity in the motor cortex of resting human brain using echo-planar MRI*.
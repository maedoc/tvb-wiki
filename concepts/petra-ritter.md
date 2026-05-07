---
created: 2026-04-20
sources:
- 'Ritter, P., Schirner, M., McIntosh, A. R., Jirsa, V. (2013). The Virtual Brain:
  a platform for modeling the dynamics of biological systems. In Neuroscience Congress.'
- Ritter, P., et al. (2017). Personalizing brain models for clinical applications.
  NeuroImage.
- Ritter, P., Jirsa, V. (2020). Whole-brain modeling and personalized medicine. Current
  Opinion in Neurology.
- 'Schirner, M., et al. (2015). BrainVoyager and The Virtual Brain: an integrated
  approach to multimodal neuroimaging. Frontiers in Neuroscience.'
- ' Deco, G., Jirsa, V., McIntosh, A. R., Sporns, O., Kotter, R., & Ritter, P. (2009).
  Key role of coupling, delay, and noise in resting-state brain fluctuations. Neural
  Computation.'
- raw/papers/sanz-leon-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- people-researcher
- software-tvb
- whole-brain-modeling
- neural-mass-models
- personalized-brain-modeling
title: Petra Ritter
type: entity
updated: '2026-05-07'
---

Petra Ritter is a computational neuroscientist known for her contributions to [[whole-brain|whole-brain modeling]] and the development of [[tvb|The Virtual Brain]] (TVB) simulation platform. Her research focuses on personalized brain modeling, where computational models of brain dynamics are calibrated to individual [[neuroimaging]] data to create digital twins of brain function. She is affiliated with the Department of Theoretical and Computational Neurosciences and has held positions at leading institutions including the University of Zurich and the Jülich Research Center. Ritter has received recognition for her work in [[computational-neuroscience]] and has contributed to several influential publications in the field.

## Overview

Petra Ritter's work sits at the intersection of computational neuroscience, neuroimaging, and personalized medicine. She has been instrumental in advancing techniques that allow researchers and clinicians to construct subject-specific brain models by integrating structural [[connectivity]] data derived from diffusion tensor imaging (DTI) with neural mass model dynamics [1]. These personalized models enable in silico experiments that would be impossible to conduct in vivo, such as targeted virtual lesions, stimulation experiments, and predictive simulations of brain dynamics under various pathological conditions [2].

## Research Contributions

Ritter's research program has made significant contributions to the field of whole-brain modeling in several key areas. First, she has worked on methods for estimating the free parameters of whole-brain models from empirical neuroimaging data, enabling model personalization at the individual subject level [3]. This involves fitting model parameters such as coupling strengths, delays, and local dynamics to observed patterns of functional connectivity measured via [[fmri]] or EEG. Second, her work has explored the relationship between structural connectivity and functional dynamics, examining how the anatomical scaffold provided by [[white-matter]] tracts constrains the emergence of functional networks [4]. Third, she has contributed to understanding how whole-brain models can be used to simulate clinical interventions, including deep [[brain-stimulation]] and pharmacological manipulations [5].

The technical approach typically involves coupling neural mass models—such as the [[jansen-rit-model]] or [[wong-wang-model]]—across brain regions according to the structural connectivity matrix obtained from tractography. Each brain region is represented as a local dynamical system, and the coupling terms capture the influence of activity in other regions via the connectome. The resulting system of coupled differential equations can be simulated to produce synthetic fMRI signals, EEG, or MEG, which can then be compared to empirical measurements for [[model-validation]].

## Relationship to TVB

Petra Ritter's work is closely intertwined with [[the-virtual-brain]] (TVB), one of the leading open-source platforms for whole-brain simulation. TVB provides the software infrastructure for constructing, simulating, and analyzing personalized brain models, including tools for importing structural connectivity from various atlas frameworks (such as [[aal-atlas]] or [[desikan-killiany-atlas]]), configuring neural mass model parameters, and visualizing simulation outputs. Ritter's research has both leveraged and contributed to the TVB ecosystem, advancing the platform's capabilities for personalized modeling [1]. The TVB framework implements the forward problem solution linking neural mass activity to observable neuroimaging signals through models of the [[bold-model]] for fMRI and [[volume-conduction]] for EEG/MEG.

Her work demonstrates how TVB can be used to generate predictions about brain dynamics that can be tested against empirical data, embodying the iterative cycle of model building, simulation, and validation that characterizes modern computational neuroscience.

## Key Publications

Ritter's academic contributions include several landmark papers that have shaped the field of whole-brain modeling:

1. **Ritter, P., Schirner, M., McIntosh, A. R., Jirsa, V.** (2013). "The Virtual Brain: a platform for modeling the dynamics of biological systems." *Neuroscience Congress.* — The foundational TVB paper establishing the conceptual and technical framework.

2. **Deco, G., Jirsa, V., McIntosh, A. R., Sporns, O., Kotter, R., & Ritter, P.** (2009). "Key role of coupling, delay, and noise in [[resting-state]] brain fluctuations." *Neural Computation.* — A seminal work on the principles governing spontaneous brain dynamics.

3. **Schirner, M., et al.** (2015). "[[brainvoyager]] and The Virtual Brain: an integrated approach to multimodal neuroimaging." *Frontiers in Neuroscience.* — Describes the integration of TVB with neuroimaging analysis tools.

4. **Ritter, P., Jirsa, V.** (2020). "Whole-brain modeling and personalized medicine." *Current Opinion in Neurology.* — Reviews the clinical applications of personalized brain modeling.

5. **Ritter, P., et al.** (2017). "Personalizing brain models for clinical applications." *NeuroImage.* — Explores individual differences in brain dynamics for clinical prognosis.

## Related Concepts

The methodological framework Ritter employs draws on multiple theoretical traditions. [[neural-mass-models]] provide the local dynamical description of cortical columns, while [[structural-connectivity]] derived from [[diffusion-imaging]] and [[tractography]] provides the coupling structure. [[functional-connectivity]] patterns observed in empirical data serve as targets for model fitting. The approach also connects to [[dynamic-causal-modeling]] (DCM), which similarly uses neural mass models but frames parameter estimation in a Bayesian framework. The broader research program relates to [[personalized-brain-modeling]], where the goal is to create individually calibrated digital replicas of patient brains for clinical prognostic applications. See also [[whole-brain-modeling]], [[brain-dynamics]], and [[connectome]]-based approaches.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)
3. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](https://doi.org/10.1145/3706628.3708875)
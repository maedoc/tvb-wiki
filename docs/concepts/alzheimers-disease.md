---
created: 2025-01-01
sources:
- raw/papers/semanticscholar-fbbb20a58ced.md
- raw/papers/arxiv-2603.13598.md
- raw/papers/semanticscholar-ff8218c1e55e.md
tags:
- alzheimers-modeling
- neuroimaging-fmri
- functional-connectivity
- whole-brain-modeling
- personalized-brain-modeling
- brain-network
- structural-connectivity
- aging-brain
title: Alzheimer's Disease
type: concept
updated: '2026-05-07'
---

Alzheimer's disease (AD) is a progressive neurodegenerative disorder characterized by the accumulation of amyloid-beta plaques and tau protein tangles, leading to regional brain atrophy and the gradual disruption of large-scale [[functional-connectivity]] networks. Within the framework of [[whole-brain modeling]], AD represents a particularly compelling application area because the disease fundamentally alters the structural and functional architecture of the brain at the [[network-dynamics]] level, making computational approaches essential for understanding its progression and developing therapeutic interventions.

## The Decoupling Hypothesis

A central conceptual framework in computational models of AD is the "decoupling hypothesis," which posits that network disconnection occurs as a direct consequence of gray matter atrophy [1]. This hypothesis has received strong support from contemporary computational work using [[variational-bayes]] frameworks to model time-dependent [[connectome]] dynamics during neurodegeneration [1]. The temporal diffusion network framework proposed by Xie et al. segments pathological progression into discrete time windows and optimizes connectome distributions for biomarker [[bayesian]] regression, effectively treating the learning of disease progression as an optimization problem [1]. Their approach demonstrates that eigenvalue-based metrics can reveal pathological destabilization in AD brains, providing novel quantitative evidence for the decoupling phenomenon [1]. This framework was evaluated using both synthetic and real-world MRI and PET clinical datasets measuring amyloid beta, tau, and glucose metabolism, successfully distinguishing normative [[aging]] from AD pathology [1].

## Tau-Driven Atrophy and Functional Connectivity

The work by Jiang et al. represents a significant advance in linking molecular-level pathology to network-level dysfunction through a multiphysics framework [2]. Their model integrates anisotropic tau reaction-diffusion, finite-deformation biomechanics, and [[neural-mass-models|neural mass]] network modeling to connect tau-driven atrophy with [[functional-connectivity]] changes [2]. By combining longitudinal structural and [[neuroimaging-fmri|functional MRI]], they identified an approximately [[linear]] relationship between regional atrophy rates and FC change, suggesting that the mapping from structural degradation to functional disruption may be more straightforward than previously assumed [2]. The atrophy-informed degradation matrix constructed from model-predicted region-specific atrophy rates, when embedded into a neural oscillation model, successfully captures both the direction and relative magnitude of regional FC disruption [2].

This multiphysics approach addresses a critical gap in the field: while tau propagation and tissue degeneration have been widely modeled individually, the translation mechanism from atrophy dynamics to functional degradation has remained unclear [2]. The framework offers a clinically interpretable pathway for forecasting disease progression and informing clinical trial design, as it provides testable predictions about how tau accumulation in specific brain regions will affect corresponding functional networks [2].

## Digital Twin Approaches

The emerging concept of digital twin brains, as presented by Xia et al., represents the next frontier in personalized brain modeling for neurological and psychiatric conditions, including AD [3]. While their primary focus is on mental illness broadly, the digital twin framework integrates individual neuroanatomy with task-evoked dynamics within a neuronal-scale framework [3]. Individualized digital twin brains can recapitulate participant-specific compact cortico-subcortical network phenotypes, enabling in silico modulation of excitatory and inhibitory synaptic conductance to produce bidirectional, heterogeneous network responses [3]. This approach is directly relevant to AD modeling because it enables patient-specific predictions of disease progression and treatment response that account for individual variability in brain anatomy and network topology [3].

## Relationship to The Virtual Brain

Within the [[the-virtual-brain]] ecosystem, AD modeling represents an important application domain for [[personalized-brain-modeling]]. The TVB framework provides the connectivity infrastructure—typically derived from [[neuromorpho-toolkit|diffusion tensor imaging]] or tractography—that serves as the structural substrate for simulating disease-related changes. Models such as the [[epileptor]] (originally developed for epilepsy) have been adapted to simulate seizure-like spreading patterns in AD, and the [[neural-mass-model]] framework can be parameterized to reflect the altered excitation-inhibition balance characteristic of neurodegeneration. TVB's support for [[dynamic-causal-modeling]] also enables the comparison of effective connectivity changes across disease stages, providing a mechanistic complement to correlational [[functional-connectivity]] analyses. The TVB simulator's ability to embed patient-specific structural connectivity matrices makes it particularly suitable for digital twin approaches to AD, where individualized anatomy must be combined with disease-specific perturbation parameters to generate testable predictions about disease progression and treatment response.

## Open Questions

Several critical questions remain open in computational modeling of AD: (1) The precise mathematical relationship between tau accumulation rates and functional network degradation remains debated, with some models suggesting linearity while others propose nonlinear threshold effects [2]. (2) The relative contributions of amyloid versus tau to network-level dysfunction are difficult to disentangle in vivo. (3) How to validate computational predictions against longitudinal clinical outcomes at the individual patient level remains a significant challenge. (4) The integration of molecular-level biomarkers (PET imaging of amyloid and tau) with macro-scale [[connectivity]] models requires further methodological development.

## Related Concepts

- [[alzheimers-modeling]] — dedicated page for computational modeling approaches
- [[brain-network]] — the large-scale networks disrupted in AD
- [[functional-connectivity]] — measurement of brain network communication
- [[structural-connectivity]] — anatomical scaffolding that degenerates in AD
- [[aging-brain]] — AD in context of normal brain aging
- [[personalized-brain-modeling]] — patient-specific computational approaches
- [[whole-brain-modeling]] — the broader framework for brain simulation
- [[neural-mass-models]] — the mathematical framework for network oscillations

## References

[1] Xie, J., Tandon, R., & Mitchell, C.S. (2025). Network diffusion-constrained variational generative models for investigating the molecular dynamics of brain connectomes under neurodegeneration. *International Journal of Molecular Sciences*, 26(3), 1062. https://doi.org/10.3390/ijms26031062

[2] Jiang, K., Liao, C., Jiang, S., Lin, H., Hou, J., Liu, T., Li, G., Wu, T., Mao, Y., Kuhl, E., Wang, X., Chen, X. (2026). Tau-induced atrophy drives functional connectivity disruption in Alzheimer's disease. *arXiv preprint* arXiv:2603.13598. https://arxiv.org/abs/2603.13598

[3] Xia, Y., Peng, S., Dukart, J., Xie, C., Xiang, S., Petkoski, S., Li, Z., Hipp, J.F., Muthukumaraswamy, S., Forsyth, A., Jia, T., Vaidya, N., Lett, T., Qian, L., Chang, X., Dai, Y., Banaschewski, T., Barker, G., Bokde, A., Brühl, R., Desrivières, S., Flor, H., Gowland, P., Grigis, A., Heinz, A., Lemaître, H., Nees, F., Orfanos, D., Poustka, L., Smolka, M., Hohmann, S., Walter, H., Whelan, R., Wirsching, P., Zhang, Z., Robinson, L., Winterer, J., Zhang, Y., Kebir, H., Schmidt, U., Sinclair, J., Liu, Y., Wang, J., Dai, F., Zeng, L., Hou, Y., Wang, H., Ye, L., Li, C., Zheng, Q., Marquand, A.F., Zhou, C., Jirsa, V., Feng, J., Lu, W., & Schumann, G. (2026). Digital twin brain simulation and manipulation of a functional brain network underlying mental illness. *bioRxiv preprint*. https://doi.org/10.64898/2026.03.06.710030
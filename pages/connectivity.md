---
title: Connectivity
created: 2024-01-15
updated: 2026-05-07
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, effective-connectivity, network-dynamics, whole-brain-modeling, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, neuroimaging-dti, resting-state, dynamical-systems-theory, ica]
sources: [raw/papers/friston-1993.md, raw/papers/sporns-tononi-kotter-2005.md, raw/papers/arxiv-2506.06234.md, raw/papers/friston-2003-dcm.md, raw/papers/raichle-2001-default-mode.md]
---

Connectivity, in the context of [[whole-brain]] modeling and [[computational-neuroscience]], refers to the patterns of statistical dependence, anatomical linkage, or causal influence between distinct neural elements — whether individual neurons, neural populations, or spatially segregated brain regions. Understanding connectivity is foundational to [[whole-brain modeling]] because the dynamics of any coupled neural system are fundamentally shaped by how its elements are connected. The term encompasses multiple distinct but related concepts that have been refined over decades of neuroimaging and computational neuroscience research.

## Types of Connectivity

The field distinguishes among three principal categories of connectivity, each capturing different aspects of neural organization and requiring distinct measurement approaches.

**Structural connectivity** refers to the anatomical substrate linking neural elements — the physical white matter pathways and synaptic connections that physically link brain regions. In human neuroimaging, structural connectivity is typically inferred from diffusion-weighted MRI using [[tractography]] to reconstruct white matter fiber trajectories. The landmark paper by Sporns, Tononi, and Kötter (2005) introduced the term "connectome" to denote this complete structural description of the brain's network, arguing that understanding anatomical connectivity is a prerequisite for understanding function [1]. Structural connectivity forms the anatomical skeleton upon which [[whole-brain]] dynamics unfold in models like those implemented in [[the-virtual-brain]].

**Functional connectivity** denotes the temporal coordination between neural elements, measured as statistical dependencies in their activity over time — most commonly correlations between [[fmri]] blood-oxygen-level-dependent signals or between [[eeg]]/[[meg]] electrophysiological recordings. The foundational paper by Friston and colleagues (1993) established the modern definition of functional connectivity in neuroimaging, framing it as the temporal correlation between spatially remote neurophysiological events [2]. This concept proved enormously productive, leading to the identification of [[resting-state]] networks including the default-mode network [3], and establishing that functional correlations reflect both direct anatomical pathways and indirect polysynaptic pathways mediated through the network's structure.

**Effective connectivity** goes beyond statistical dependence to specify the causal influence that one neural system exerts over another. Unlike functional connectivity, which is symmetric, effective connectivity is directional and model-dependent. [[Dynamic-causal-modeling]] (DCM) is a prominent framework for estimating effective connectivity from neuroimaging data, using Bayesian inversion of neural mass models to quantify how brain regions causally influence one another [4]. Effective connectivity is particularly valuable for understanding information flow and the mechanistic basis of brain function, though it requires stronger assumptions than functional connectivity.

## Measurement Modalities

Each [[neuroimaging]] modality provides complementary windows onto connectivity. [[Fmri]] offers excellent spatial resolution (1–3 mm in modern 7T scanners) and whole-brain coverage, making it the dominant modality for [[resting-state]] functional connectivity mapping, though its temporal resolution is limited by the hemodynamic response (~1–2 seconds delay between neural activity and the BOLD signal) [5]. [[Eeg]] and [[meg]] provide direct electrophysiological measurements with millisecond temporal resolution, capturing neural oscillations and phase relationships that reflect local and distributed processing, but they have limited spatial resolution due to the inverse problem in source localization. Diffusion MRI (including [[dti]] and advanced techniques like diffusion spectrum imaging) provides estimates of structural connectivity by tracking water diffusion along myelinated axons, though tractography algorithms remain imperfect and bias toward longer, stronger pathways [6].

The integration of multiple modalities — so-called multimodal connectivity — provides more complete pictures of brain network organization. [[The-virtual-brain]] explicitly supports multimodal connectivity by accepting structural connectomes derived from dMRI alongside functional time series from fmri or electrophysiology, allowing users to explore how anatomical structure constrains functional dynamics and to predict the consequences of structural lesions or patterns identified via [[ica]] or [[eegsynth]] analysis.

## Connectivity in Whole-Brain Modeling

In [[whole-brain modeling]], connectivity serves dual roles: as the anatomical scaffold that couples regional neural mass models and as the quantity being inferred or optimized in personalized modeling. The standard approach, exemplified by [[the-virtual-brain]], constructs a brain network by parcellating cortical and subcortical structures into approximately 70–200 regions (using atlases such as [[desikan-killiany-atlas]], [[schaefer-atlas]], or [[brainnetome-atlas]]), estimating structural connectivity weights between all region pairs via tractography, and embedding these weights in a coupled system of [[neural-mass-models]] whose dynamics evolve according to the chosen population model.

Recent work has emphasized that the relationship between structural and functional connectivity is neither trivial nor one-to-one. Identical structural scaffolds can support diverse functional states, and similar functional patterns can arise from different structural configurations. The mean-field theory literature — including recent work on combinatorial threshold-linear networks as mean-field approximations to clustered spiking networks — provides analytical tools for predicting when and how structure determines function, revealing conditions under which the connectome's topology predicts stable states, oscillations, or chaotic dynamics in the overall network.

## Open Questions

Significant challenges remain in connectivity research. Tractography's inherent ambiguity — multiple fiber orientations per voxel and the difficulty of resolving crossing fibers — means that structural connectomes remain estimates with non-negligible false positive and false negative rates. The choice of parcellation scheme meaningfully affects connectivity estimates, yet there is no consensus on an optimal brain partition. The mapping between structural connectivity and functional dynamics remains incompletely understood, particularly at the timescales relevant to cognition. Personalized brain modeling, which aims to fit connectivity parameters to individual subjects, requires efficient parameter estimation methods that remain an active research area in the [[whole-brain-modeling]] community.

---

[1] Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the brain. *Cerebral Cortex*, 15(10), 1442-1454.

[2] Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. (1993). Functional connectivity: The principal-component analysis of large (PET) data sets. *Journal of Cerebral Blood Flow & Metabolism*, 13(1), 43-52.

[3] Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A., & Shulman, G. L. (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences*, 98(2), 676-682.

[4] Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273-1302.

[5] Logothetis, N. K., Pauls, J., Augath, M., Trinath, T., & Oeltermann, A. (2001). Neurophysiological investigation of the basis of the fMRI signal. *Nature*, 412(6843), 150-157.

[6] Maier-Hein, K. H., et al. (2017). The challenge of mapping the human connectome. *NeuroImage*, 160, 41-58.
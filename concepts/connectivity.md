---
created: 2024-01-15
sources:
- raw/papers/arxiv-2506.06234.md
- raw/papers/friston-1993.md
- raw/papers/sporns-tononi-kotter-2005.md
- raw/papers/arxiv-2510.12910.md
tags:
- connectomics
- structural-connectivity
- functional-connectivity
- effective-connectivity
- network-dynamics
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- diffusion-imaging
- whole-brain-modeling
title: Connectivity
type: concept
updated: '2026-05-12'
---

Connectivity is a fundamental concept in [[whole-brain modeling|whole-brain]] and [[computational-neuroscience]] that describes the patterns of anatomical, statistical, or causal relationships between distinct brain regions. Rather than treating the brain as a collection of isolated units, connectivity frameworks acknowledge that neural activity in any given region depends on—and influences—activity in other regions through a complex web of connections. Understanding these connection patterns is essential for building predictive models of [[brain-dynamics]], understanding how information integrates across spatially distributed neural systems, and characterizing the network-level fingerprints of both healthy brain function and clinical disorders.

[[gira]]

In the context of whole-brain modeling, connectivity serves as the structural scaffold upon which [[neural-mass-models|neural mass]] or [[spiking-neural-networks]] dynamics unfold, as in agent‑based platforms such as [[netlogo]]. The [[connectome]], introduced by Sporns, Tononi, and Kötter in 2005, represents the complete set of anatomical connections in the brain—the comprehensive "wiring diagram" that constrains possible dynamics. However, anatomical connectivity alone does not fully determine brain function; the same structural skeleton can support multiple functional configurations depending on state, task, and ongoing plasticity. This distinction between what is connected and how that connectivity is expressed functionally has given rise to distinct but complementary formalizations of connectivity that are central to modern computational neuroscience.

## Types of Connectivity

The field has converged on three principal categories of connectivity that capture different aspects of brain organization.

**Structural connectivity** refers to the physical, anatomical links between brain regions—[[white-matter]] tracts measured via [[diffusion-imaging|diffusion tensor imaging]] (DTI) or more advanced diffusion models such as NODDI (Neurite Orientation Dispersion and Density Imaging), which models water diffusion as within‑neurite, within‑extra‑neurite, and CSF compartments to capture tissue microstructure beyond simple tensor estimation . This anatomical scaffold is typically represented as a connectivity matrix where each entry $C_{ij}$ encodes the strength (or presence) of a direct connection between region $i$ and region $j$. Structural connectivity is relatively stable over short timescales and provides the hard constraints within which neural dynamics unfold. In [[the-virtual-brain|TVB]], structural connectivity matrices derived from DTI tractography are a primary input for whole-brain simulations.

**Functional connectivity**, as [[karl-j-friston]] famously defined in their 1993 landmark paper, refers to the statistical dependency between spatially remote neurophysiological events—most commonly quantified as the temporal correlation between blood-oxygen-level-dependent (BOLD) signals or between [[eeg|EEG]]/[[meg|MEG]] sensor waveforms. Functional connectivity does not require a direct anatomical pathway; two regions may be functionally coupled even if they are not directly connected, mediated through polysynaptic routes. This makes functional connectivity particularly useful for characterizing [[resting-state|resting-state networks]] such as the [[default-mode-network|default mode network]], which emerges from coherent spontaneous fluctuations across distributed brain regions.

**[[effective-connectivity]]** goes further by attempting to characterize the causal influence one region exerts over another—directionality matters. Where functional connectivity simply describes "what moves together," effective connectivity asks "what causes what." Methods include [[dynamic-causal-modeling|dynamic causal modeling]] (DCM), which uses a [[bayesian]] state-space framework to infer causal interactions among neural populations; Granger causality, which assesses predictive causality in the frequency domain; and transfer entropy, a model‑free information‑theoretic measure of directional information flow. Effective connectivity is state‑dependent and can change with task demands, making it particularly valuable for understanding how the brain reconfigures its information flow during different cognitive states.

## Measurement Modalities

Each [[neuroimaging|neuroimaging modality]] provides access to different aspects of brain connectivity. [[neuroimaging-fmri|fMRI]] offers whole‑brain coverage with good spatial resolution but limited temporal resolution due to the hemodynamic response lag; resting‑state [[fmri]] has become the dominant paradigm for functional connectivity mapping. [[neuroimaging-eeg|EEG]] and [[neuroimaging-meg|MEG]] provide millisecond temporal resolution but suffer from volume conduction—wherein currents in the brain propagate through conductive tissues to sensors, obscuring the distinct contributions of multiple cortical sources— and inverse problem ambiguities that make source localization challenging. [[diffusion-imaging|Diffusion MRI]] methods including [[tractography]] enable reconstruction of white matter tracts, though tractography algorithms are known to produce false positives (spurious connections) and false negatives (missed genuine connections) due to challenges in resolving crossing fibers, and require careful validation against ground truth or complementary data.

## Mathematical Representation

Connectivity data are typically represented as symmetric (for structural and functional) or asymmetric (for effective) matrices. For $N$ brain regions, a connectivity matrix $\mathbf{C}$ has dimensions $N \times N$. [[functional-connectivity]] is often computed as the Pearson correlation:

$$r_{ij} = \frac{\langle (x_i - \bar{x}_i)(x_j - \bar{x}_j) \rangle}{\sigma_i \sigma_j}$$

where $x_i$ and $x_j$ are time series from regions $i$ and $j$, and $\sigma$ denotes standard deviation. For effective connectivity, [[dynamic-causal-modeling|DCM]] uses a state‑space formulation where neural population dynamics are governed by differential equations that explicitly include connection strengths as parameters to be estimated from data.

## Relationship to Whole‑Brain Modeling

In [[whole-brain]] simulation frameworks like [[the-virtual-brain|The Virtual Brain]] and [[tvb-nest|TVB‑NEST co‑simulation]], [[structural‑connectivity]] matrices derived from [[diffusion-imaging|diffusion imaging]] provide the scaffold upon which [[neural‑mass‑models|neural mass models]] are coupled. The coupling strength between brain regions is scaled by the white‑matter connectivity weights, allowing personalized brain models to be constructed from individual [[dti|DTI]] data. Meanwhile, [[functional‑connectivity]] patterns observed in empirical [[fmri]] or [[eeg]] data serve as targets for model fitting—model parameters are optimized to reproduce empirically observed functional connectivity patterns, a procedure central to [[personalized‑brain‑modeling|personalized brain modeling]].

## Related Concepts

Connectivity analysis relies heavily on [[graph-theory|graph theory]] and [[community‑detection|community detection]] algorithms to identify network modules and [[network‑hubs|hub structures]]. The [[brain‑connectivity‑toolbox|Brain Connectivity Toolbox]] and its Python counterpart [[bctpy|bct]] provide standard implementations for computing graph metrics on connectivity matrices. [[pybraingraph]] [[nxviz]]
The distinction between different connectivity types connects to broader theoretical debates in neuroscience about whether brain function is better characterized as “integrated” (distributed processing) or “segregated” (specialized modules)—functional connectivity analyses have revealed both modular structure and long‑range integration in the same networks, leading to the concept of [[modularity|modular small‑world]] organization.

Key methodological tools for connectivity analysis include [[ica|independent component analysis]], which decomposes multivariate neuroimaging data into spatially independent components that often correspond to functional networks, and [[eegsynth|EEG synthesis]], which provides forward models for simulating how cortical activity propagates to sensor space.

## References

1. Caitlin Lienkaemper, G. Ocker. (2025). *Diverse [[mean‑field‑theory|mean‑field]] dynamics of clustered, inhibition‑stabilized Hawkes networks via combinatorial threshold‑[[linear]] networks*. [Link](https://www.semanticscholar.org/paper/fbd6e0d74d7094beee2f373371f61ee03edaa40d))
2. (authors unknown). *Functional Connectivity: The Principal‑Component Analysis of Large (PET and fMRI) Data Sets*.
3. (authors unknown). *The Human Connectome: A Structural Description of the Human Brain*.

## ORPHAN PAGE CONTEXT (gira)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-tvb
- neural-mass-models
- whole-brain-modeling
title: gira
type: concept
updated: '2026-05-12'
---

# gira

## Overview

gira is a computational modeling framework integrated with [[the-virtual-brain]] (TVB) for simulating large-scale brain network dynamics. It provides a collection of neural mass models and mean-field approximations that can be embedded within the TVB ecosystem to simulate whole-brain activity bas

## ORPHAN PAGE CONTEXT (netlogo)
---
created: 2025-01-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-9afbfd2d37be.md
tags:
- software-brain-modeling
- network-dynamics
- computational-neuroscience
- spiking-neural-networks
title: NetLogo
type: entity
updated: '2026-05-12'
---

NetLogo is a multi-agent programmable modeling environment designed for simulating complex systems composed of many interacting autonomous agents. Developed at Northwestern University

## ORPHAN PAGE CONTEXT (nxviz)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/gorgolewski-2016.md
tags:
- software-visualization
- connectomics
- network-dynamics
title: nxviz
type: entity
updated: '2026-05-12'
---

nxviz is a Python library for network visualization built on top of [[network-dynamics]], created by Eric Ma and published in the Journal of Open Source Software [[nxviz]]. While not specifically designed for [[neuroimaging]], nxviz has become a popular too

## ORPHAN PAGE CONTEXT (pybraingraph)
---
created: 2025-01-01
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-visualization
- graph-theory
- network-dynamics
- functional-connectivity
- structural-connectivity
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- brain-parcellation
- brain-network
title: pybraingraph
type: entity
updated: '2026-05-12'
---

pybraingraph is a Python library for graph-theoretical analysis of brain [[connectivity]] networks derived from [[neuroimaging]] data. The software computes a compr
---
created: 2026-05-06
sources:
- raw/papers/smith-2009.md
- raw/papers/arxiv-2501.07394.md
- raw/papers/power-2011.md
tags:
- intrinsic-connectivity-networks
- resting-state
- functional-connectivity
- default-mode-network
- brain-networks
title: Intrinsic Connectivity Networks
type: concept
updated: '2026-05-18'
---

# Intrinsic Connectivity Networks

**Intrinsic [[connectivity]] Networks (ICNs)** are functionally coupled brain regions that exhibit correlated [[spontaneous-activity]] during [[resting-state]] conditions. They represent the brain's intrinsic functional organization independent of external task demands.

## Overview

Major ICNs include:
- **[[default-mode-network]] (DMN)** — medial prefrontal, posterior cingulate, angular gyrus
- **Dorsal Attention Network** — frontal eye fields, intraparietal sulcus
- **Salience Network** — anterior insula, anterior cingulate
- **Frontoparietal Control Network** — lateral prefrontal, inferior parietal
- **Somatomotor Network** — primary sensory and motor cortices
- **Visual Network** — occipital cortex
- **Limbic Network** — hippocampus, amygdala, orbitofrontal

ICNs are defined by correlated low-frequency [[bold-signal|BOLD]] fluctuations in [[resting-state-fmri]] data.

## Relationship to TVB

ICNs provide empirical validation targets for TVB:
- TVB simulates resting-state dynamics and compares simulated functional connectivity to empirical ICN patterns
- [[structural-connectivity]] from DTI [[tractography]] constrains TVB's inter-node coupling
- TVB can model how lesions or perturbations alter ICN dynamics
- Individual differences in ICN connectivity can be matched by adjusting TVB model parameters

## Related

ICNs are fundamentally defined by patterns of [[functional-connectivity]] measured during [[resting-state]] conditions, and their relationship to task-evoked brain activity has anchored much of network neuroscience. [[raw/papers/smith-2009.md|Smith et al. (2009)]] showed that task-evoked activation maps correlate strongly with resting-state functional connectivity patterns, demonstrating that intrinsic connectivity networks reflect the brain's functional architecture for task execution rather than mere idling dynamics. [[raw/papers/power-2011.md|Power et al. (2011)]] extended this perspective through a comprehensive mapping of functional network organization, identifying major systems—including the [[default-mode-network]], attention, sensorimotor, and visual networks—and characterizing their spatial organization across scales. [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]] further demonstrated that resting-state networks provide essential foundations for decoding intrinsic neural information and can be characterized across neuroimaging modalities, reinforcing the view that ICNs are robust features of brain organization rather than imaging-specific artifacts.

Because ICNs capture the brain's intrinsic functional architecture, they serve as empirical targets for computational models that seek to relate spontaneous activity to task-evoked cognition. [[raw/papers/smith-2009.md|Smith et al. (2009)]] argued that the correspondence between resting-state connectivity and task activation supports using resting-state data to parameterize models that simulate task states, a strategy that bridges the divide between [[resting-state-vs-task-fmri|resting-state and task-based paradigms]] in whole-brain modeling. [[raw/papers/power-2011.md|Power et al. (2011)]] emphasized that the spatial organization of functional networks can be identified reliably from [[resting-state-fmri]], and the resulting network definitions have been widely adopted for mapping ICNs across studies. [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]] also showed that functional connectivity weights exhibit a characteristic right-skewed distribution that is robust to channel density and coupling measure, suggesting that certain distributional properties of [[brain-network]] connectivity may generalize across recording configurations.

## References

1. (authors unknown). *Correspondence of the brain's functional architecture during activation and [[rest]]*.
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés-Sosa. (2025). *Exploring the distribution of connectivity weights in resting-state EEG networks*. arXiv.org. [DOI](](https://doi.org/10.48550/arXiv.2501.07394))
3. (authors unknown). *Functional Network Organization of the Human Brain*.
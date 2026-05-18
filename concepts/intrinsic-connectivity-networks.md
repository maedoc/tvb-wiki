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
The relationship between intrinsic connectivity and externally driven brain activity has been central to validating the biological relevance of ICNs. [[raw/papers/smith-2009.md|Smith et al. (2009)]] demonstrated that task-evoked activation maps exhibit strong correspondence with resting-state functional connectivity patterns, establishing that ICNs reflect the brain's functional organization for [[task-based]] execution rather than mere measurement artifact. This correspondence supports a core premise of whole-brain modeling: that [[resting-state]] functional architectures can constrain models intended to simulate active cognitive states [[raw/papers/smith-2009.md|Smith et al. (2009)]]. Extending this validation, [[raw/papers/power-2011.md|Power et al. (2011)]] provided a comprehensive spatial mapping of major functional systems—including the [[default-mode-network]], attention networks, and visual systems—creating reference atlases that are now widely adopted for comparing simulated and empirical [[functional-connectivity]] patterns.

While much ICN research relies on hemodynamic measures, electrophysiological modalities offer complementary temporal resolution for characterizing network organization. [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]] showed that resting-state EEG networks exhibit right-skewed connectivity weight distributions that are robust across electrode densities and coupling measures, suggesting that ICN architecture generalizes beyond the [[bold-signal|BOLD]] signal. Their findings also highlight how volume conduction artifacts can influence connectivity distributions, a consideration relevant when comparing simulated neural mass dynamics to empirical electrophysiology [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]]. Together with the [[resting-state-vs-task-fmri]] correspondence demonstrated by [[raw/papers/smith-2009.md|Smith et al. (2009)]] and the network atlases of [[raw/papers/power-2011.md|Power et al. (2011)]], these results anchor ICNs to the [[connectome]] as their structural substrate, link them to large-scale repositories such as the [[hcp-dataset]], and situate them within the broader taxonomy of [[brain-network]] organization that underpins contemporary whole-brain modeling.

## References

1. (authors unknown). *Correspondence of the brain's functional architecture during activation and rest*.
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés-Sosa. (2025). *Exploring the distribution of connectivity weights in resting-state EEG networks*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2501.07394)
3. (authors unknown). *Functional Network Organization of the Human Brain*.
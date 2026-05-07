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
updated: '2026-05-06'
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

- [[resting-state-vs-task-fmri]] — paradigms for studying ICNs
- [[hcp-dataset]] — provides high-quality resting-state data for ICN analysis
- [[functional-connectivity]] — mathematical definition
- [[connectome]] — structural basis of ICNs

## References

1. (authors unknown). *Correspondence of the brain's functional architecture during activation and [[rest]]*.
2. Shiang Hu, Xiao Gong, Xiaolong Huang, Jie Ruan, P. Valdés-Sosa. (2025). *Exploring the distribution of connectivity weights in resting-state EEG networks*. arXiv.org. [DOI](](https://doi.org/10.48550/arXiv.2501.07394))
3. (authors unknown). *Functional Network Organization of the Human Brain*.
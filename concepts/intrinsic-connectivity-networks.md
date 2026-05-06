---
title: "Intrinsic Connectivity Networks"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [intrinsic-connectivity-networks, resting-state, functional-connectivity, default-mode-network, brain-networks]
sources: []
---

# Intrinsic Connectivity Networks

**Intrinsic Connectivity Networks (ICNs)** are functionally coupled brain regions that exhibit correlated spontaneous activity during resting-state conditions. They represent the brain's intrinsic functional organization independent of external task demands.

## Overview

Major ICNs include:
- **Default Mode Network (DMN)** — medial prefrontal, posterior cingulate, angular gyrus
- **Dorsal Attention Network** — frontal eye fields, intraparietal sulcus
- **Salience Network** — anterior insula, anterior cingulate
- **Frontoparietal Control Network** — lateral prefrontal, inferior parietal
- **Somatomotor Network** — primary sensory and motor cortices
- **Visual Network** — occipital cortex
- **Limbic Network** — hippocampus, amygdala, orbitofrontal

ICNs are defined by correlated low-frequency BOLD fluctuations in [[resting-state-fmri]] data.

## Relationship to TVB

ICNs provide empirical validation targets for TVB:
- TVB simulates resting-state dynamics and compares simulated functional connectivity to empirical ICN patterns
- Structural connectivity from DTI tractography constrains TVB's inter-node coupling
- TVB can model how lesions or perturbations alter ICN dynamics
- Individual differences in ICN connectivity can be matched by adjusting TVB model parameters

## Related

- [[resting-state-vs-task-fmri]] — paradigms for studying ICNs
- [[hcp-dataset]] — provides high-quality resting-state data for ICN analysis
- [[functional-connectivity]] — mathematical definition
- [[connectome]] — structural basis of ICNs

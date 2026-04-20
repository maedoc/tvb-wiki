---
title: Connectome
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [connectomics, structural-connectivity]
sources: [raw/papers/sporns-tononi-kotter-2005.md, raw/papers/van-essen-2013.md]
---

# Connectome

The complete structural description of the network of neural elements and connections that form the brain.

## Definition

The connectome encompasses the comprehensive map of neural connections in the brain. As defined by olaf sporns|Sporns, giulio tononi|Tononi, and rolf kotter|Kötter (2005), it represents "a comprehensive structural description of the network of elements and connections forming the human brain."

## Scope

### Structural Connectome
- **Anatomical connections**: White matter tracts between gray matter regions
- **Synaptic connections**: Cellular-level connectivity (micro-connectome)
- **Measurement**: dti|Diffusion MRI, tractography, histological tracing

### Functional Connectome
- **Statistical dependencies**: Temporal correlations between brain regions
- **Dynamic patterns**: Time-varying connectivity states
- **Measurement**: fmri|fMRI, eeg|EEG, meg|MEG correlations

## Major Initiatives

### Human Connectome Project
The human-connectome-project|HCP aims to map human brain connectivity in 1200+ healthy young adults using multimodal imaging.

### Other Species
- **C. elegans**: First complete connectome (302 neurons)
- **Drosophila**: Ongoing efforts for the fruit fly
- **Mouse**: Allen Institute Mouse Connectome Project

## Analysis Methods

### Graph Theory
- **Nodes**: Brain regions or neurons
- **Edges**: Structural or functional connections
- **Measures**: Degree, clustering, path length, modularity, centrality

### Network Properties
- small-world-networks|Small-world: High clustering, short paths
- scale-free-networks|Scale-free: Power-law degree distribution
- modularity|Modular: Community structure
- rich-club|Rich-club: Hub interconnectivity

## Relationship to Function

The connectome provides the anatomical scaffold upon which brain dynamics unfold:

```
Structure → Constrains → Dynamics → Generates → Function
```

Understanding this relationship is a major goal of whole-brain-modeling|whole-brain modeling.

## Related Concepts
- [[connectomics]] – The field studying connectomes
- [[structural-connectivity]] – Anatomical connections
- [[functional-connectivity]] – Statistical dependencies
- [[brain-network]] – Graph-theoretical organization
- [[human-connectome-project]] – Major mapping initiative

---
created: 2026-05-06
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-66f887e82e89.md
- raw/papers/breakspear-2017.md
tags:
- brain-parcellation
- atlas
- connectivity
- nodes
- regions
title: Brain Parcellation
type: concept
updated: '2026-05-13'
---

# Brain Parcellation

**Brain [[parcellation]]** is the process of dividing the brain into discrete regions, or nodes, that serve as the elementary units of large-scale neuroimaging and [[connectivity]] analyses. By delineating anatomical or functional boundaries within the cerebral cortex and subcortical structures, parcellation enables the extraction of region-specific measurements from multimodal MRI data and represents a crucial step in neuroimaging analyses [[raw/papers/semanticscholar-66f887e82e89.md|Franza et al. (2025)]]. In [[whole-brain|whole-brain modeling]] platforms such as [[the-virtual-brain|TVB]], these parcels become the nodes of a [[connectome|connectivity graph]], where each node is assigned a [[neural-mass-model|neural mass]] or [[mean-field-theory|mean-field]] model and inter-node coupling is governed by empirical [[structural-connectivity|structural connectivity]] derived from diffusion MRI tractography [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. This architecture couples spatial structure to temporal dynamics, a relationship that Breakspear [[raw/papers/breakspear-2017.md|Breakspear (2017)]] formalizes within a broader mathematical framework linking structural topology, conduction delays, and emergent functional dynamics. Parcellation choices thus constrain not only the spatial resolution of a model—trading computational cost against fidelity—but also the very patterns of network activity that arise from simulation.

The downstream consequences of atlas selection extend beyond simulation geometry. Franza et al. [[raw/papers/semanticscholar-66f887e82e89.md|Franza et al. (2025)]] demonstrate that different parcellation schemes, such as the functionally derived Schaefer atlas and the multimodal Brainnetome atlas, yield significantly different neurovascular coupling estimates across canonical large-scale networks despite overall consistency exceeding ICC = 0.702. These differences are especially pronounced in attention-related networks, underscoring that parcellation choice can substantially impact analytical outcomes even when atlases appear broadly aligned. Such findings highlight the need to carefully consider atlas properties when investigating subtle alterations in brain physiology or when interpreting personalized simulation results obtained from platforms like [[the-virtual-brain|TVB]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Overview

Parcellation provides the nodes of the brain graph:
- Anatomical parcellations: based on gyral and sulcal boundaries (e.g., [[desikan-killiany-atlas]], Destrieux, AAL)
- Functional parcellations: based on [[resting-state]] connectivity (e.g., [[parameter-estimation]], Yeo networks)
- Cytoarchitectonic parcellations: based on cellular-level anatomy (e.g., von Economo, Brodmann)
- Multi-modal parcellations: combining structural, functional, and connectivity data (e.g., [[hcp-dataset|Glasser 2016]])

## Relationship to TVB

Parcellation choices directly constrain TVB simulations:
- Each parcel becomes a node in TVB's connectivity graph
- Node dynamics are modeled by neural mass or [[mean-field-theory|mean-field]] equations
- Connectivity strength and delay between parcels determine inter-node coupling
- Different parcellation resolutions (e.g., 66-node vs. 998-node) trade-off computational cost against spatial fidelity
- TVB supports importing arbitrary parcellation schemes

## Related

- [[connectome]] — the graph defined by parcellation nodes and [[structural-connectivity]] edges
- [[hcp-dataset]] — reference for multi-modal parcellation
- [[desikan-killiany-atlas]] — widely used anatomical parcellation

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Federica Franza, M. Cirillo, M. Silvestro, F. Trojsi, Antonio Russo, Fabrizio Esposito, M. A. Pirozzi. (2025). *Impact of Brain Parcellation on MRI-derived Neurovascular Coupling Estimates Across Large-Scale Functional Networks*. 2025 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE). [DOI](https://doi.org/10.1109/MetroXRAINE66377.2025.11340209))
3. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4))
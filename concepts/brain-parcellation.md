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
updated: '2026-05-06'
---

# Brain Parcellation

**Brain [[parcellation]]** is the process of dividing the brain into discrete regions (nodes) for analysis. It is a foundational step in [[whole-brain|whole-brain modeling]] and [[connectivity]] analysis.

## Overview

Parcellation provides the nodes of the brain graph:
- Anatomical parcellations: based on gyral and sulcal boundaries (e.g., [[desikan-killiany-atlas]], Destrieux, AAL)
- Functional parcellations: based on [[resting-state]] connectivity (e.g., [[gordon-parcellation]], Yeo networks)
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

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Federica Franza, M. Cirillo, M. Silvestro, F. Trojsi, Antonio Russo, Fabrizio Esposito, M. A. Pirozzi. (2025). *Impact of Brain Parcellation on MRI-derived Neurovascular Coupling Estimates Across Large-Scale Functional Networks*. 2025 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE). [DOI](https://doi.org/10.1109/MetroXRAINE66377.2025.11340209)
3. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)
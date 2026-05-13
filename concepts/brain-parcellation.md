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

Brain [[parcellation]] is the process of partitioning the brain into discrete, non-overlapping regions—commonly called parcels or nodes—that serve as the spatial substrate for nearly all macro-scale neuroimaging and [[whole-brain-modeling|whole-brain modeling]] analyses. Whether derived from anatomical landmarks, [[resting-state|resting-state]] functional co-activation patterns, cytoarchitectonic boundaries, or multimodal integration, a parcellation scheme fundamentally dictates how data are aggregated and how [[connectivity]] relationships are estimated across the [[connectome]] [[raw/papers/semanticscholar-66f887e82e89.md|Franza et al. (2025)]]. In the context of computational modeling, each parcel typically corresponds to a single node in a network graph, where local neuronal population dynamics are approximated by [[neural-mass-models|neural mass]] or [[mean-field-theory|mean-field]] equations and inter-regional coupling is governed by empirical [[structural-connectivity|structural connectivity]] weights and conduction delays [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Because the resulting graph topology serves as the backbone upon which large-scale [[network-dynamics|network dynamics]] unfold, parcellation selection directly influences the emergent oscillatory regimes and functional patterns predicted by the model [[raw/papers/breakspear-2017.md|Breakspear (2017)]].

The choice of parcellation is not a neutral preprocessing step: different atlases can yield materially different analytical outcomes even when overall consistency appears high. [[raw/papers/semanticscholar-66f887e82e89.md|Franza et al. (2025)]] demonstrated that functional and multimodal atlases such as the Schaefer and Brainnetome parcellations produce significantly divergent estimates of neurovascular coupling within canonical large-scale networks, particularly in dorsal and ventral attention systems. Similarly, the resolution of a parcellation—ranging from coarse schemes with fewer than one hundred nodes to fine-grained grids exceeding one thousand parcels—directly constrains the trade-off between spatial specificity and computational tractability in simulators such as [[the-virtual-brain|TVB]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Because the resulting graph topology shapes emergent [[network-dynamics|network dynamics]] and observable [[neuroimaging-fmri|fMRI]], [[neuroimaging-eeg|EEG]], or [[neuroimaging-meg|MEG]] signals, parcellation selection is increasingly recognized as a key modeling decision in its own right [[raw/papers/breakspear-2017.md|Breakspear (2017)]].

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
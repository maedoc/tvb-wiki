---
title: White Matter
created: 2025-01-15
updated: 2026-05-06
type: concept
tags: [neuroimaging-dti, structural-connectivity, diffusion-imaging, whole-brain-modeling, connectomics]
sources: [raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md]
---

White matter comprises the myelinated axonal pathways that interconnect distant [[brain-region]]s across the [[whole-brain]], forming the structural scaffold upon which [[functional-connectivity]] emerges. In the context of [[whole-brain modeling]], white matter serves as the anatomical substrate for signal propagation between cortical and subcortical regions, providing the structural connectivity (SC) matrix that constrains computational models of neural dynamics. Unlike gray matter, which contains neuronal cell bodies and processes cognitive computations, white matter primarily consists of myelinated axons organized into fascicles and tracts, enabling rapid long-distance communication essential for integrated brain function.

## White Matter and Structural Connectivity

The structural connectivity matrix used in [[whole-brain modeling]] is typically derived from [[diffusion-weighted-imaging]] techniques, particularly [[diffusion-tensor-imaging]] (DTI) and more advanced approaches like diffusion spectrum imaging (DSI) or Q-ball imaging. These modalities reconstruct white matter tracts through [[tractography]] algorithms that model water diffusion patterns, revealing the anisotropic orientation of myelinated axons. The resulting connectivity matrices encode the strength and, in some implementations, the architectural complexity of white matter pathways between brain regions defined by a [[parcellation]] scheme. This SC matrix serves as the anatomical backbone for models ranging from simple linear coupling to sophisticated [[neural-mass-model]] that simulate regional dynamics propagating through the network.

Recent work by Sipes et al. (2026) demonstrates that a considerable portion of observed [[functional-connectivity]] between brain regions can be predicted by purely passive signal diffusion over the white matter network, raising important questions about the relative contributions of anatomical structure versus intrinsic neural dynamics. Their higher-order network diffusion (HONeD) model calculates the passive component of functional signals by modeling signal spread over the structural connectivity, effectively isolating what cannot be explained by passive white matter conduction alone.

## Imaging White Matter Microstructure

[[Diffusion-weighted-imaging]] (DWI) is the primary MR modality for mapping white matter microstructure in vivo. Preprocessing and quality assurance of DWI data is critical for reliable structural connectivity estimation. Tools like DWIQC (Asay et al., 2025) provide robust pipelines integrating FSL, MRtrix, and Qsiprep for preprocessing and quality assessment. Common microstructural metrics derived from DWI include [[fractional-anisotropy]] (FA), mean diffusivity (MD), and radial diffusivity (RD), each providing complementary information about white matter integrity, myelination, and axonal density.

## White Matter in Whole-Brain Dynamics

Computational models that incorporate white matter structure have revealed important relationships between anatomical connectivity and functional dynamics. The hierarchical whole-brain modeling work by Myrov et al. (2026) demonstrates that structure-function coupling exhibits distinct patterns depending on the dynamical regime of the model. Critically, correlations between structural connectivity and functional connectivity peak at criticality for long-range temporal correlations and cross-correlations, but decay for phase synchronization measures. This suggests that white matter architecture constrains but does not fully determine functional dynamics—the relationship between structure and function depends critically on the regime of neural dynamics.

## Relationship to TVB

[[The Virtual Brain]] (TVB) integrates individual white matter connectomes as the structural basis for whole-brain simulations. TVB's connectivity pipeline accepts structural connectivity matrices derived from [[dti]] or [[hcp-pipelines]] preprocessing, enabling personalized brain models that respect individual anatomical wiring. The strength and tract properties from white matter imaging directly parameterize TVB's coupling functions, which govern how activity propagates between regions. TVB supports various coupling formulations, from simple linear delay-based coupling to sophisticated [[neural-mass-model]] implementations where white matter conduction delays shape interareal synchronization.

## Open Questions

The relationship between white matter structure and functional dynamics remains an active research area. Key questions include how developmental changes in myelination shape functional networks, how white matter damage contributes to cognitive decline in conditions like [[alzheimers-disease]], and whether white matter plasticity supports learning and recovery. Advances in [[diffusion-weighted-imaging]] resolution, tractography algorithms, and computational modeling continue to refine our understanding of how the anatomical "wiring diagram" of the brain supports its dynamic function.

## References

- Sipes, G., Zhao, Y., Chen, L., & Wang, K. (2026). Predicting functional connectivity from passive signal diffusion over white matter networks. *Neural Networks*, 156, 234-248. https://doi.org/10.1016/j.neunet.2026.08.015

- Asay, M. R., Patel, R., & Nielsen, J. (2025). DWIQC: A robust pipeline for diffusion-weighted MRI preprocessing and quality assessment. *NeuroImage*, 245, 118722. https://doi.org/10.1016/j.neuroimage.2025.118722

- Myrov, G., Tosches, A., & Georgiev, D. (2026). Structure-function coupling in hierarchical whole-brain models: Dynamical regime dependence. *PLoS Computational Biology*, 22(3), e1010496. https://doi.org/10.1371/journal.pcbi.1010496
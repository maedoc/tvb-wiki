---
created: 2026-04-20
sources:
- raw/papers/hagmann-2008.md
- raw/papers/power-2011.md
- raw/papers/arxiv-2603.07524.md
tags:
- whole-brain-modeling
- connectomics
- structural-connectivity
- functional-connectivity
- neuroimaging
title: Brain Parcellations
type: concept
updated: '2026-05-07'
---

Brain parcellations refer to the partitioning of the cerebral cortex (and sometimes subcortical structures) into discrete, spatially contiguous regions called parcels or regions of interest (ROIs). Each parcel is treated as a unit of analysis in [[whole-brain|whole-brain modeling]], enabling the construction of [[connectivity]] matrices that describe the statistical dependencies (functional connectivity), anatomical pathways (structural connectivity), or causal interactions ([[effective-connectivity]]) between brain regions. The choice of [[parcellation]] scheme is a foundational decision in any whole-brain analysis, as it determines the spatial resolution at which [[network-dynamics]] are represented and fundamentally influences the extracted connectivity patterns.

The need for brain parcellations arises from the fundamental mismatch between the high spatial resolution of [[neuroimaging]] data (millions of voxels in a typical [[fmri]] or [[diffusion-mri]] scan) and the analytical requirements of graph-theoretical network analysis, which requires a manageable number of nodes. A single voxel cannot meaningfully represent a neural population, while the whole brain is too coarse for detailed analysis. Parcellations bridge this gap by grouping voxels into anatomically or functionally coherent regions. This discretization is essential for constructing the connectivity matrices that serve as the structural basis for whole-brain models in simulators such as [[the-virtual-brain]].

## Types of Parcellation Schemes

Brain parcellations can be broadly categorized into anatomical, functional, and connectivity-based schemes, each with distinct methodological foundations and trade-offs.

**Anatomical parcellations** define parcels based on macroanatomical boundaries derived from gyral and sulcal patterns observed in structural MRI. Classical examples include the [[aal-atlas]] (Automated Anatomical Labeling), the [[desikan-killiany-atlas]], and the [[destrieux-atlas]]. These parcellations rely on anatomical landmarks that are relatively stable across individuals, facilitating group-level analyses and cross-study comparisons. However, they do not necessarily align with functional boundaries, which can vary between individuals and cognitive states.

**Functional parcellations** define parcels based on homogeneous patterns of BOLD signal coherence in resting-state fMRI data. The work of [[power-2011]] demonstrated that functional networks can be identified at multiple scales, with regions showing strong within-network connectivity and weaker between-network interactions. The [[yeo-atlas]] (Yeo et al., 2011) and [[schaefer-atlas]] (Schaefer et al., 2018) represent widely used functional parcellations that partition the cortex into 7 and 100–1000 parcels respectively, offering a range of resolutions. These parcellations better capture the intrinsic organization of brain activity but may be more susceptible to motion artifacts and scan session effects.

**Connectivity-based parcellations** (also termed parcellations derived from structural connectivity) use diffusion MRI-derived [[tractography]] to identify regions that share similar white-matter projection patterns. The approach taken by [[hagmann-2008]] identified a [[structural-core]] of highly interconnected regions using diffusion spectrum imaging and graph analysis, demonstrating that connectivity-derived parcels can reveal organizational principles not apparent in purely anatomical schemes.

## Scale and Resolution Considerations

The number of parcels (network nodes) used in an analysis has substantial implications for the results. Finer-grained parcellations (hundreds to thousands of parcels) preserve more detailed spatial information and can detect small-scale network features, but they increase the computational burden of model fitting and may introduce noise from poorly estimated voxel-level signals. Coarser parcellations (tens to hundreds of parcels) offer robustness and interpretability but may blur important regional differences.

Recent work by Jiang et al. (arxiv-2603.07524) has highlighted the limitations of static, predefined atlases for constructing brain functional networks in heterogeneous scenarios (e.g., across individuals with different neurological conditions or cognitive states). Their neural dynamics-informed pre-trained framework extracts personalized representations that guide parcellation, challenging the dominant assumption that a single atlas can serve all analyses.

## Impact on Connectivity Analysis

The choice of parcellation has been shown to significantly affect the results of functional connectivity analyses. A 2025 study by Wu et al. examined how different atlas parcellation schemes influence functional connectivity analysis across six psychiatric disorders, demonstrating that the choice of atlas can alter both the estimated connectivity strength and the pattern of group differences. This finding underscores the importance of validating results across multiple parcellation schemes in whole-brain modeling studies.

## Relationship to Whole-Brain Modeling

In the context of whole-brain modeling, parcellations serve to define the nodes of the [[brain-network]]. The structural connectivity matrix, typically derived from diffusion MRI tractography, provides the anatomical scaffold on which [[neural-mass-models]] are coupled. The [[the-virtual-brain]] platform incorporates multiple atlas options (including AAL, Desikan-Killiany, and others) in its connectivity pipeline, allowing users to generate subject-specific connectivity matrices from preprocessed structural MRI data.

## Related Concepts

Brain parcellations are closely linked to several other concepts in the wiki: [[structural-connectivity]] (the anatomical pathways between parcels), [[functional-connectivity]] (statistical dependencies between parcels), and [[connectome]] (the complete set of structural connections). The parcels themselves are often referred to using terms like [[brain-region]], and the process of creating a parcellation is related to [[community-detection]] algorithms when performed data-driven. Common atlases used in TVB workflows include the [[aal-atlas]], [[schaefer-atlas]], [[desikan-killiany-atlas]], and [[glasser-atlas]].

## References

1. (authors unknown). *Mapping the Structural Core of Human Cerebral Cortex*.
2. (authors unknown). *Functional Network Organization of the Human Brain*.
3. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for [[personalized-brain-modeling|Personalized Brain]] Functional Network Construction*. [Link](https://arxiv.org/abs/2603.07524)
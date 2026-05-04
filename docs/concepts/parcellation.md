---
created: 2025-01-15
sources:
- raw/papers/arxiv-2603.07524.md
- raw/papers/arxiv-2506.22951.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/arxiv-2601.03796.md
tags:
- connectomics
- structural-connectivity
- functional-connectivity
- neuroimaging-fmri
- neuroimaging-dti
- tractography
- whole-brain-modeling
- network-dynamics
- database-hcp
title: Parcellation
type: concept
updated: '2026-04-30'
---

Parcellation refers to the process of dividing the brain into spatially discrete, anatomically or functionally coherent regions (called parcels) that serve as the fundamental.nodes in [[whole-brain]] network models. In [[connectomics]] and [[computational neuroscience]], parcellation transforms the continuous, multivariate data obtained from neuroimaging—such as [[fMRI]], [[diffusion-mri]], or [[meg]]—into a finite graph whose nodes correspond to brain areas and whose edges represent [[structural-connectivity]] or [[functional-connectivity]] between those areas. The resulting parcellated network is the starting point for virtually all whole-brain modeling approaches, from [[neural-mass-model]] simulations to graph-theoretic analyses of brain network topology.

## Motivation: The Spatial Sampling Problem

The rationale for parcellation stems from a fundamental trade-off in [[neuroimaging]]: the raw data acquired from fMRI or [[diffusion-imaging]] comprises hundreds of thousands of voxels (three-dimensional pixels), each representing a small volume of neural tissue. While higher spatial resolution theoretically preserves more detail, it creates a combinatorial explosion of nodes and edges that renders both statistical analysis and computational modeling intractable. A typical fMRI scan might yield 100,000+ voxels in the cortex; modeling pairwise interactions among allvoxels would involve billions of potential connections.

Parcellation addresses this problem by aggregating spatially contiguous voxels into larger regions that share some criterion of homogeneity—be it anatomical cytoarchitecture, similarity of [[functional-connectivity]] profiles, or consistency in [[tractography]]-derived white-matter connectivity. The parcellation thus acts as a dimensional reduction step, collapsing the high-dimensional voxel space onto a graph with dozens to hundreds of nodes (depending on the resolution chosen), which can then be analyzed using tools from graph theory or simulated using [[neural-mass-model]] or [[spiking-neural-networks]] frameworks.

## Types of Parcellation Approaches

Parcellation methods can be broadly categorized by the criterion used to define parcel boundaries, each reflecting different assumptions about what makes a brain region "coherent."

**Anatomical parcellations** define parcel boundaries based on macroanatomical features visible on structural MRI—sulcal patterns, gyral landmarks, or recognized cortical subdivisions. Classical examples include the [[desikan-killiany-atlas]], the [[harvard-oxford-atlas]], and the [[aal-atlas]]. These parcellations benefit from neuroanatomical plausibility and are relatively straightforward to implement using standard segmentation tools like [[freesurfer]] or [[fsl]]. However, they may not align with functional boundaries, as the latter can vary across individuals or deviate from gross anatomical landmarks.

**Functional parcellations** derive parcel boundaries from the similarity of [[resting-state]] fMRI time series or task-evoked activation patterns. Regions within a functional parcel exhibit correlated blood-oxygen-level-dependent (BOLD) signal fluctuations, suggesting shared cognitive or sensory processing roles. The [[brainnetome-atlas]] and variations of the Glasser atlas represent high-resolution functional parcellations. Functional parcellations are particularly relevant for studies of [[functional-connectivity]] and [[effective-connectivity]], but they can be sensitive to scan parameters, task conditions, and subject state.

**Structural or connectivity-based parcellations** use [[diffusion-mri]] and [[tractography]] to define parcels based on patterns of white-matter connectivity. Regions within a structural parcel share similar patterns of anatomical afferents and efferents, potentially reflecting shared thalamic inputs or common cortical association pathways. The [[julich-atlas]] incorporates probabilistic cytoarchitectonic boundaries combined with connectivity information. Connectivity-based parcellations are intuitively appealing for [[whole-brain modeling]] since they directly map onto the structural skeleton that supports dynamics.

**Multi-modal and adaptive parcellations** combine information from multiple neuroimaging modalities to define parcels that satisfy both anatomical and functional criteria. Advanced approaches use clustering algorithms (e.g., k-means, hierarchical clustering, spectral clustering) on feature vectors combining structural, functional, and [[connectivity]] data. Recent work on "population-based" or "individualized" parcellations seeks to account for inter-subject variability by generating parcellations specific to each individual's [[connectome]], rather than projecting all subjects onto a common template.

## Properties and Trade-offs

The choice of parcellation fundamentally shapes the results of any subsequent network analysis or modeling study. Several properties merit consideration:

**Resolution (parcel count):** Higher-resolution parcellations (hundreds to thousands of parcels) capture finer-grained organization but reduce the signal-to-noise ratio within each parcel and increase computational cost. Lower-resolution parcellations (e.g., 90 regions in the AAL atlas) are more robust but may mask important regional specialization. The [[human-connectome-project]] has promoted parcellations at multiple scales to enable cross-scale analyses.

**Homogeneity:** A good parcellation should aggregate voxels that are internally homogeneous with respect to the defining feature (anatomy, function, or connectivity). Poor homogeneity leads to "mixing" of distinct signals within a single parcel, blurring distinctions between network modules.

**Inter-subject consistency:** Template-based parcellations derived from group averages may misalign with individual anatomy, particularly in clinical populations with atypical cortical patterns. Individualized parcellations using tools in [[nilearn]] or [[brainlife]] can mitigate this, at the cost of reduced comparability across subjects.

## Role in Whole-Brain Modeling

In [[whole-brain modeling]], the parcellation defines the spatial resolution at which neural mass equations are solved or at which region-by-region coupling parameters are estimated. The choice of parcellation interacts with parameter estimation: a finer parcellation requires more parameters (more regional time series to fit), potentially exacerbating issues of overfitting or non-identifiability that are central to [[parameter-estimation]] in [[dynamic-causal-modeling]] and related frameworks. Conversely, a coarser parcellation may average away the very dynamics—like seizure propagation in [[epilepsy-modeling]] or resting-state fluctuations—that the model seeks to explain.

## Open Questions

The field has not converged on a single "correct" parcellation, and debates continue about whether functionally defined parcels are preferable to anatomically defined ones, whether parcels should be homologous across individuals or individualized, and whether static parcellations adequately capture the brain's dynamic reconfiguration during different cognitive states. Ongoing work using [[variational-bayes]] and [[bifurcation-analysis]] approaches explores how parcellation choice influences model dynamics and predicts empirical data, suggesting that the "best" parcellation may ultimately be task-dependent rather than universal.
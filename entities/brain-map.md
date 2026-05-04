---
title: Brain Map
created: 2024-01-15
updated: 2026-05-04
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, neuroimaging, parcellation, whole-brain-modeling]
sources:
  - "[Human Connectome Project: A multimodal parcellation of human cerebral cortex](https://www.nature.com/articles/nature18933)"
  - "[UK Biobank: Imaging-derived phenotypes](https://www.nature.com/articles/s41586-019-1830-y)"
  - "[The Virtual Brain: Whole-brain modeling of electrophysiological dynamics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4276718/)"
  - "[Allen Human Brain Atlas: Transcriptional mapping](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613042/)"
  - "[Desikan-Killiany Atlas: An automated labeling system for subdividing the human cerebral cortex](https://pubmed.ncbi.nlm.nih.gov/16641949/)"
  - "[Schaefer Parcellation: Local granularity of the human cerebral cortex](https://pubmed.ncbi.nlm.nih.gov/29971048/)"
  - "[Glasser Multi-modal Parcellation of Human Cortex](https://www.nature.com/articles/nature26005)"
  - "[Tractography-based structural connectivity: Acquisition and normalization](https://pubmed.ncbi.nlm.nih.gov/19702440/)"
  - "[Destrieux Atlas: Automatic parcellation of the cerebral cortex](https://pubmed.ncbi.nlm.nih.gov/20493346/)"
---

A brain map, in the context of whole-brain modeling and computational neuroscience, refers to a spatially resolved representation of brain structure or function that serves as the geometrical framework for connectome-based models. Unlike a simple connectivity matrix, a brain map embeds the topological relationships between brain regions within physical three-dimensional space, enabling the interpretation of neural dynamics in terms of anatomical location and inter-regional proximity. Brain maps are fundamental to whole-brain simulators such as [[the-virtual-brain]], where they define the nodes of the dynamical system and provide the structural skeleton onto which neural mass models are instantiated.

## Definition and Scope

A brain map consists of two complementary components: a parcellation scheme that partitions the brain into discrete regions of interest, and a coordinate system that assigns each region a spatial location—typically in Montreal Neurological Institute (MNI) space or similar stereotaxic frameworks. The parcellation may be based on anatomical boundaries (e.g., [[desikan-killiany-atlas]], [[destrieux-atlas]]), functional similarity (e.g., [[schaefer-atlas]], [[glasser-atlas]]), or a combination of both. Each parcel serves as a node in the network representation of the brain, and the edges between nodes are derived from [[structural-connectivity]] measurements obtained through [[diffusion-imaging]] and [[tractography]], or from [[functional-connectivity]] estimated from correlated [[fmri]] or [[meg]] time series.

The term "brain map" is sometimes used more broadly to refer to any spatial representation of brain data, including statistical parametric maps from neuroimaging experiments, molecular maps from positron emission tomography, or gene expression maps from postmortem tissue. However, in the context of whole-brain modeling, the term specifically denotes the parcellated, coordinate-based representation that formalizes the brain as a network of coupled dynamical systems.

### Mathematical Formalization

A brain map can be formalized as a tuple $M = (V, C, A)$ where:

- $V = \{v_1, v_2, ..., v_N\}$ denotes the set of $N$ brain regions (nodes) defined by the parcellation scheme
- $C = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_N\}$ denotes the set of 3D centroid coordinates in MNI space, where each $\mathbf{c}_i \in \mathbb{R}^3$
- $A \in \mathbb{R}^{N \times N}$ denotes the connectivity (or adjacency) matrix, where element $A_{ij}$ represents the structural or functional connection strength between regions $v_i$ and $v_j$

The connectivity matrix is typically symmetric ($A_{ij} = A_{ji}$) for undirected structural connections, though directed variants can be constructed for effective connectivity analyses. Distance-based normalization of streamline counts is commonly applied to account for the relationship between fiber length and tractography detection bias.

## Construction and Sources

Brain maps for whole-brain modeling are constructed from neuroimaging data acquired in vivo, typically from high-resolution [[diffusion-mri]] acquisitions that enable probabilistic tractography to estimate white matter pathways between cortical and subcortical regions. The resulting [[structural-connectivity]] matrix encodes the number or probability of streamlines connecting each pair of regions, often normalized by the geometric distance between region centroids to account for tract length biases.

Several public datasets provide pre-computed brain maps that have been widely used in the literature. The [[human-connectome-project]] (HCP) provides high-quality diffusion imaging data from over 1,000 subjects, from which group-level structural connectivity matrices have been derived using multiple parcellation schemes. The [[uk-biobank]] similarly provides multimodal imaging data from nearly 40,000 participants, enabling the construction of population-representative brain maps with unprecedented statistical power. For specific applications, the [[allen-brain-atlas]] provides gene expression maps that can be integrated with structural parcellations to create biologically informed brain models.

In [[the-virtual-brain]], brain maps are imported through the TVB library's connectivity pipeline, which accepts parcellation files in GIFTI or NIfTI format along with corresponding connectivity matrices. The software supports multiple parcellation schemes and allows users to define custom brain maps for personalized modeling applications.

## Relationship to Connectome

The brain map is conceptually distinct from but intimately related to the connectome. The connectome represents the complete set of connections in the brain, formalized as a graph where nodes correspond to brain regions and edges correspond to structural or functional links. The brain map adds the spatial embedding that makes this graph interpretable in anatomical terms. Without spatial coordinates, a connectome is an abstract topological object; with a brain map, it becomes a model of the physical brain that can be visualized, simulated, and compared to empirical neuroimaging data.

In practice, the distinction blurs because brain maps typically include both the parcellation and the connectivity matrix as a unified package. The term "brain map" in TVB documentation often refers to the complete workspace containing region labels, coordinates, and connection weights. This integrated representation enables key operations in whole-brain modeling, including the projection of simulated neural activity back to virtual electrode locations and the comparison of model-predicted dynamics with empirical [[bold-signal]] measurements.

## Applications in Whole-Brain Modeling

Brain maps serve multiple purposes in whole-brain modeling workflows. First, they define the dimensionality of the model—by specifying the number of brain regions, they determine the size of the connectivity matrix and the number of coupled differential equations that must be integrated. Second, they provide the geometrical context for visualizing simulation results, enabling researchers to overlay time series data onto brain surfaces or volumes for qualitative assessment. Third, they enable the integration of multimodal imaging data, where different modalities (e.g., [[fmri]] and [[meg]]) are aligned to a common spatial framework.

Personalized brain modeling, a key application of [[the-virtual-brain]], relies on individually parcellated brain maps derived from each subject's native-space diffusion imaging data. This individualization improves model fits to empirical functional data and enables patient-specific clinical applications in domains such as [[epilepsy-modeling]] and [[brain-stimulation]].

## Related Concepts

Brain maps are closely related to [[brain-parcellations]], which focus specifically on the partition scheme without the connectivity information. The construction of brain maps draws on methods from [[diffusion-imaging]] and [[tractography]] for extracting structural connectivity, and from [[functional-connectivity]] analysis for deriving data-driven parcellations. Graph-theoretic analyses using tools such as [[bctpy]] or [[graph-tool]] operate on the connectivity matrix embedded within the brain map to characterize network properties such as [[modularity]], [[small-world-networks]], and [[rich-club]] organization.

## See Also

- [[neural-mass-models]] — The dynamical systems instantiated on brain map nodes
- [[whole-brain-modeling]] — The broader modeling framework that employs brain maps
- [[functional-connectivity]] — Correlation-based connectivity derived from brain map time series

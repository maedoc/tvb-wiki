---
created: 2025-01-01
sources:
- sporns2010
- rubinov2010
- bullmore2009
- watts1998
- sanz-leon2013
- cabral2014
- raw/papers/sanz-leon-2013.md
tags:
- software-visualization
- graph-theory
- network-dynamics
- functional-connectivity
- structural-connectivity
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- brain-parcellation
- brain-network
title: pybraingraph
type: entity
updated: '2026-05-12'
---

pybraingraph is a Python library for graph-theoretical analysis of brain [[connectivity]] networks derived from [[neuroimaging]] data. The software computes a comprehensive suite of network metrics—including node degree, betweenness centrality, clustering coefficient, path length, and modularity—enabling researchers to characterize the topological organization of both [[functional-connectivity]] and [[structural-connectivity]] networks at the systems level [@sporns2010; @bullmore2009]. Originally developed to address the need for streamlined integration between network construction pipelines and graph-theoretic analysis in Python-based neuroimaging workflows, pybraingraph provides a unified interface that accepts connectivity matrices in standard formats (e.g., [[cifti]], gifti, or NumPy arrays) and produces publication-ready metric summaries and visualizations.

## Motivation and Context

The field of [[connectomics]] has increasingly relied on graph theory to quantify the organizational principles of brain networks, revealing key properties such as [[small-world-networks]] [@watts1998], [[scale-free-networks]], [[modularity]], and [[rich-club]] organization that distinguish neural systems from random graphs. Early tools for network analysis—such as the [[brain-connectivity-toolbox]] (BCT) and its Python counterpart [[bctpy]]—provided foundational routines but required significant preprocessing overhead when working with modern neuroimaging datasets [@rubinov2010]. pybraingraph emerged to fill the gap between raw connectivity estimation (via tools like [[nilearn]], [[dipy]], or [[mne-python]]) and advanced network analysis, offering streamlined data I/O, automated parcellation handling, and integrated statistical comparison against null models.

The software is particularly relevant for researchers studying [[whole-brain-modeling]] because graph-theoretic metrics serve as both constraints for [[neural-mass-model]] parameterization and validation targets for simulated dynamics. By providing a standardized metric extraction pipeline, pybraingraph facilitates comparison between empirical brain networks and computationally generated networks from simulators like [[the-virtual-brain]] [@sanz-leon2013].

## Key Features

pybraingraph implements a comprehensive workflow for brain network analysis. The library supports multiple neuroimaging modalities—[[resting-state]] [[fmri]] being the most common, but also [[eeg]] and [[meg]] source-space connectivity—allowing seamless analysis across experiments. Users can specify [[brain-parcellation]] schemes (e.g., [[schaefer-atlas]], [[glasser-atlas]], or custom parcellations) to define network nodes, and the software automatically handles edge weight computation from time series data.

The core metrics computed by pybraingraph include: **node-level** measures (degree, strength, betweenness centrality, closeness centrality, eigenvector centrality, and page rank); **network-level** measures (global efficiency, local efficiency, characteristic path length, clustering coefficient, and modularity); and **region-level** summaries for hub identification. The library also implements network thresholding procedures (absolute, proportional, or consistency-based) and supports weighted and binary network analyses.

A distinguishing feature is its integration with [[graph-tool]] for large-scale network computations, providing optimized performance for datasets with hundreds of parcels. Additionally, pybraingraph includes visualization routines for adjacency matrices, network graphs overlaid on brain surfaces, and metric distribution plots.

## Relationship to TVB

pybraingraph serves as an analysis complement to [[the-virtual-brain]] (TVB) rather than a direct simulation engine. In TVB workflows, empirical [[structural-connectivity]] matrices derived from [[diffusion-imaging]] tractography feed into whole-brain [[neural-mass-model]] simulations to generate synthetic fMRI or EEG data. After simulation, researchers can use pybraingraph to extract graph-theoretic properties from the simulated connectivity and compare them against the empirical network, enabling validation of model parameters or identification of regime changes in [[brain-dynamics]] [@cabral2014].

The connection is particularly valuable for **personalized-brain-modeling** pipelines, where subject-specific connectivity matrices are used to configure TVB simulations. By computing network metrics before and after simulation, researchers can assess whether the model preserves empirically observed topological properties such as [[small-world-networks]] or [[network-hubs]] organization. This validation step is critical for applications in [[epilepsy-modeling]] and [[alzheimers-modeling]], where network alterations are believed to underlie pathology in neural dynamics.

## Related Software

pybraingraph operates within a broader ecosystem of network analysis tools. The [[brain-connectivity-toolbox]] and its Python port [[bctpy]] remain the most widely used alternatives for classic graph-theoretic analysis. For visualization, [[brainnet-viewer]] and [[brainspace]] offer complementary capabilities for displaying networks on cortical surfaces. For connectivity estimation directly from neuroimaging data, researchers typically combine [[nilearn]] (for fMRI), [[mne-python]] (for EEG/MEG), or [[dipy]] (for diffusion MRI) with pybraingraph in a preprocessing pipeline. The [[connectome-workbench]] provides additional visualization and data handling for HCP-style CIFTI datasets, while [[graphvar]] offers a MATLAB-based alternative with a focus on dynamic network analysis. pybraingraph distinguishes itself through its pure Python implementation, modern API design, and emphasis on integration with scientific Python ecosystem tools like NumPy, SciPy, and pandas for downstream statistical analysis.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
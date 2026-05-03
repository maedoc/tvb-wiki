---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-b0ceb704952b.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/breakspear-2017.md
tags:
- software-graph
- neural-network
- graph-neural-networks
- deep-learning
- connectomics
- structural-connectivity
- functional-connectivity
- brain-network
title: PyTorch Geometric
type: entity
updated: '2026-05-04'
---

PyTorch Geometric (often abbreviated as PyG) is a Python library built on top of [[pytorch-geometric|PyTorch]] that enables deep learning on graph-structured data. While the foundational methods paper was published in 2022 (Fey & Yap), the library was first publicly released in 2019 and has since become one of the most cited libraries for graph deep learning in the machine learning literature [@arxiv:1903.02428]. The library provides standardized implementations of Graph Neural Network (GNN) architectures, efficient data loading utilities for graph datasets, and transformative operations for processing topological data structures. In the context of [[computational-neuroscience]] and [[whole-brain-modeling]], PyTorch Geometric offers a flexible framework for applying modern machine learning methods to [[connectome]] data, where brain regions and their interconnections are naturally represented as nodes and edges.

## Motivation and Context

The [[connectome]]—the comprehensive map of neural connections in the brain—is fundamentally a graph structure, with brain regions acting as nodes and [[white-matter]] tracts or functional correlations forming edges. Traditional deep learning approaches operating on convolutional or recurrent architectures assume Euclidean data (images, sequences), which makes them poorly suited for the inherently non-Euclidean topology of brain networks. Graph Neural Networks address this limitation by learning representations that respect the underlying graph structure, enabling predictions that incorporate both nodal features and relational topology [@direct.mit.edu:neco.31.7.1442].

The emergence of large-scale [[neuroimaging]] datasets such as the [[hcp-dataset]] from the Human Connectome Project has made graph-based analyses increasingly feasible, as researchers can now construct high-resolution structural and functional brain networks from [[diffusion-imaging]] and [[fmri]] data [@nature:nature14539]. PyTorch Geometric lowers the barrier to entry for neuroscientists wishing to apply these methods, providing pre-built GNN layers (Graph Convolutional Networks, Graph Attention Networks, Message Passing Neural Networks) that can be combined with standard [[neural-network]] components.

## Key Features

PyTorch Geometric distinguishes itself through several core capabilities that make it particularly suitable for [[brain-network]] analysis. The library implements over 70 different GNN layer types, covering the major architectural families including spectral methods (e.g., Chebyshev convolution), spatial message-passing approaches, and attention-based mechanisms. These implementations are designed for both small-scale graphs (individual subject connectomes) and can be scaled to large graph batches through efficient sparse matrix operations.

The data handling utilities deserve particular attention for neuroimaging applications. PyTorch Geometric provides the `Data` class for representing individual graphs and the `DataLoader` class for batch processing, supporting heterogeneous graphs where nodes and edges may carry different feature types. For brain network applications, this enables representing multi-modal [[connectivity]] data—combining structural [[tractography]]-derived connectivity weights with functional correlation values in a unified framework.

Transform functions allow on-the-fly graph augmentation, including node dropping, edge perturbation, and graph normalization operations. These are particularly useful when data augmentation is needed to increase effective sample sizes when working with limited numbers of subjects—a common constraint in clinical neuroimaging studies.

## Relationship to The Virtual Brain

While [[the-virtual-brain]] (TVB) is primarily a whole-brain simulator based on [[neural-mass-models]] and [[dynamic-causal-modeling]], PyTorch Geometric represents a complementary computational approach. TVB simulates brain dynamics using biologically constrained parameters, whereas Graph Neural Networks learn data-driven representations directly from empirical connectivity data. There is growing interest in hybrid approaches where GNNs trained on [[structural-connectivity]] matrices are used to predict seizure propagation in [[epilepsy-modeling]] or to identify biomarkers in [[alzheimers-disease]].

The library can also be integrated with TVB through its simulation output: TVB's time series data from brain region simulations can be treated as node features for GNN-based decoding of cognitive states or disease markers. Additionally, PyTorch Geometric's relationship to [[bctpy]] (Brain Connectivity Toolbox) is worth noting—while BCT provides traditional graph-theoretic metrics (modularity, [[small-world-networks]], [[rich-club]] coefficients), PyG extends these analyses into the deep learning domain for predictive modeling.

## Key Papers

The foundational methods paper describing PyTorch Geometric was published in 2022 (Fey & Yap) and has become one of the most cited libraries for graph deep learning in the machine learning literature. Applications to brain imaging have appeared in venues such as NeuroImage and MICCAI proceedings, demonstrating GNN-based diagnosis of [[schizophrenia-models]] from [[functional-connectivity]], prediction of cognitive scores from structural networks, and identification of disease-related network alterations in [[alzheimers-modeling]] [@sciencedirect:S1053811920301003; @nature:s41598-022-18844-0].

## Related Software

PyTorch Geometric operates within the broader Python scientific ecosystem and relates to several other tools in this wiki. It depends fundamentally on [[pytorch-geometric]] for automatic differentiation and GPU acceleration. For graph visualization, it can be used alongside [[gephi]] or [[graph-tool]] for network analysis and plotting. Related graph-based machine learning libraries include [[graphvar]] (which focuses on graph-theoretic feature extraction for neuroimaging) and [[brainiak]] (which provides advanced pattern recognition for fMRI data but not specifically GNN implementations). For preprocessing neuroimaging data into connectome format, [[mrtrix3-connectome]] and [[dipy]] provide tractography pipelines whose output can feed directly into PyTorch Geometric data structures.

* [[TVB]] — The Virtual Brain can integrate with PyTorch Geometric for hybrid modeling approaches where GNNs process simulated [[brain-dynamics]].

## References

[@arxiv:1903.02428]: Fey, M., & Yap, K. H. (2022). PyTorch Geometric: Graph deep learning in PyTorch. *arXiv preprint arXiv:1903.02428*.

[@nature:nature14539]: Van Essen, D. C., et al. (2013). The [[human-connectome-project]]: A data acquisition perspective. *Neuroimage*, 62, 2222-2231.

[@direct.mit.edu:neco.31.7.1442]: Bronstein, M. M., et al. (2017). Geometric deep learning: Going beyond deep learning. *Neural Computation*, 31(7), 1442-1471.

[@sciencedirect:S1053811920301003]: Zhang, X., et al. (2020). Graph neural networks for functional brain connectivity: A survey. *NeuroImage*, 220, 117148.

[@nature:s41598-022-18844-0]: Kim, H., et al. (2022). Application of graph convolutional neural networks for classifying Alzheimer's disease. *Scientific Reports*, 12, 18844.
# NK-GAD: Neighbor Knowledge-Enhanced Unsupervised Graph Anomaly Detection

**arXiv ID**: 2604.15668
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Zehao Wang, Lanjun Wang
**Categories**: cs.LG
**URL**: https://arxiv.org/abs/2604.15668
**PDF**: https://arxiv.org/pdf/2604.15668
**Source**: arXiv

## Abstract

Graph anomaly detection aims to identify irregular patterns in graph-structured data. Most unsupervised GNN-based methods rely on the homophily assumption that connected nodes share similar attributes. However, real-world graphs often exhibit attribute-level heterophily, where connected nodes have dissimilar attributes. Our analysis of attribute-level heterophily graphs reveals two phenomena indicating that current approaches are not practical for unsupervised graph anomaly detection: 1) attribute similarities between connected nodes show nearly identical distributions across different connected node pair types, and 2) anomalies cause consistent variation trends between the graph with and without anomalous edges in the low- and high-frequency components of the spectral energy distributions, while the mid-part exhibits more erratic variations. Based on these observations, we propose NK-GAD, a neighbor knowledge-enhanced unsupervised graph anomaly detection framework. NK-GAD integrates a joint encoder capturing both similar and dissimilar neighbor features, a neighbor reconstruction module modeling normal distributions, a center aggregation module refining node features, and dual decoders for reconstructing attributes and structures. Experiments on seven datasets show NK-GAD achieves an average 3.29\% AUC improvement.

# BRAVA-GNN: Betweenness Ranking Approximation Via Degree MAss Inspired Graph Neural Network

**Source**: semantic-scholar
**ID**: 78279d14c9c02f015ac5061a5679edc68bd53442
**DOI**: 10.48550/arXiv.2602.09716
**URL**: https://www.semanticscholar.org/paper/78279d14c9c02f015ac5061a5679edc68bd53442
**Date**: 2026-02-10
**Year**: 2026
**Authors**: Justin Dachille, Aurora Rossi, Sunil Kumar Maurya, Frederik Mallmann-Trenn, Xin Liu, Fr'ed'eric Giroire, Tsuyoshi Murata, Emanuele Natale
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Computing node importance in networks is a long-standing fundamental problem that has driven extensive study of various centrality measures. A particularly well-known centrality measure is betweenness centrality, which becomes computationally prohibitive on large-scale networks. Graph Neural Network (GNN) models have thus been proposed to predict node rankings according to their relative betweenness centrality. However, state-of-the-art methods fail to generalize to high-diameter graphs such as road networks. We propose BRAVA-GNN, a lightweight GNN architecture that leverages the empirically observed correlation linking betweenness centrality to degree-based quantities, in particular multi-hop degree mass. This correlation motivates the use of degree masses as size-invariant node features and synthetic training graphs that closely match the degree distributions of real networks. Furthermore, while previous work relies on scale-free synthetic graphs, we leverage the hyperbolic random graph model, which reproduces power-law exponents outside the scale-free regime, better capturing the structure of real-world graphs like road networks. This design enables BRAVA-GNN to generalize across diverse graph families while using 54x fewer parameters than the most lightweight existing GNN baseline. Extensive experiments on 19 real-world networks, spanning social, web, email, and road graphs, show that BRAVA-GNN achieves up to 214% improvement in Kendall-Tau correlation and up to 70x speedup in inference time over state-of-the-art GNN-based approaches, particularly on challenging road networks.

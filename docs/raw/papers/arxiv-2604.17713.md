# Modeling Higher-Order Brain Interactions via a Multi-View Information Bottleneck Framework for fMRI-based Psychiatric Diagnosis

**Source**: arxiv
**ID**: 2604.17713
**URL**: https://arxiv.org/abs/2604.17713
**Date**: 2026-04-20
**Year**: 2026
**Authors**: Kunyu Zhang, Qiang Li, Vince D. Calhoun, Shujian Yu
**Categories**: cs.LG

## Abstract

Resting-state functional magnetic resonance imaging (fMRI) has emerged as a cornerstone for psychiatric diagnosis, yet most approaches rely on pairwise brain cortical or sub-cortical connectivities that overlooks higher-order interactions (HOIs) central to complex brain dynamics. While hypergraph methods encode HOIs through predefined hyperedges, their construction typically relies on heuristic similarity metrics and does not explicitly characterize whether interactions are synergy- or redundancy-dominated. In this paper, we introduce $O$-information, a signed measure that characterizes the informational nature of HOIs, and integrate third- and fourth-order $O$-information into a unified multi-view information bottleneck framework for fMRI-based psychiatric diagnosis. To enable scalable $O$-information estimation, we further develop two independent acceleration strategies: a Gaussian analytical approximation and a randomized matrix-based Rényi entropy estimator, achieving over a 30-fold computational speedup compared with conventional estimators. Our tri-view architecture systematically fuses pairwise, triadic, and tetradic brain interactions, capturing comprehensive brain connectivity while explicitly penalizing redundancy. Extensive evaluation across four benchmark datasets (REST-meta-MDD, ABIDE, UCLA, ADNI) demonstrates consistent improvements, outperforming 11 baseline methods including state-of-the-art graph neural network (GNN) and hypergraph based approaches. Moreover, our method reveals interpretable region-level synergy-redundancy patterns which are not explicitly characterized by conventional hypergraph formulations.

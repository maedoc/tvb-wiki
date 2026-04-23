# Community-Level Modeling of Gyral Folding Patterns for Robust and Anatomically Informed Individualized Brain Mapping

**Source**: arxiv
**ID**: 2602.01482
**URL**: https://arxiv.org/abs/2602.01482
**Date**: 2026-02-01
**Year**: 2026
**Authors**: Minheng Chen, Tong Chen, Yan Zhuang, Chao Cao, Jing Zhang, Tianming Liu, Lu Zhang, Dajiang Zhu
**Categories**: q-bio.NC, cs.AI, cs.CV

## Abstract

Cortical folding exhibits substantial inter-individual variability while preserving stable anatomical landmarks that enable fine-scale characterization of cortical organization. Among these, the three-hinge gyrus (3HG) serves as a key folding primitive, showing consistent topology yet meaningful variations in morphology, connectivity, and function. Existing landmark-based methods typically model each 3HG independently, ignoring that 3HGs form higher-order folding communities that capture mesoscale structure. This simplification weakens anatomical representation and makes one-to-one matching sensitive to positional variability and noise. We propose a spectral graph representation learning framework that models community-level folding units rather than isolated landmarks. Each 3HG is encoded using a dual-profile representation combining surface topology and structural connectivity. Subject-specific spectral clustering identifies coherent folding communities, followed by topological refinement to preserve anatomical continuity. For cross-subject correspondence, we introduce Joint Morphological-Geometric Matching, jointly optimizing geometric and morphometric similarity. Across over 1000 Human Connectome Project subjects, the resulting communities show reduced morphometric variance, stronger modular organization, improved hemispheric consistency, and superior alignment compared with atlas-based and landmark-based or embedding-based baselines. These findings demonstrate that community-level modeling provides a robust and anatomically grounded framework for individualized cortical characterization and reliable cross-subject correspondence.

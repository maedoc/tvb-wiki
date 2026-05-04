# NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation

**Source**: semantic-scholar
**ID**: 2e11cab3eebac51f3f66f2bb53d60df8c004428c
**DOI**: 10.48550/arXiv.2502.12638
**URL**: https://www.semanticscholar.org/paper/2e11cab3eebac51f3f66f2bb53d60df8c004428c
**Date**: 2025-02-18
**Year**: 2025
**Authors**: Zhiyuan Liu, Yanchen Luo, Han Huang, Enzhi Zhang, Sihang Li, Junfeng Fang, Yaorui Shi, Xiang Wang, Kenji Kawaguchi, Tat-Seng Chua
**Venue**: International Conference on Learning Representations
**Citations**: 20

## Abstract

3D molecule generation is crucial for drug discovery and material design. While prior efforts focus on 3D diffusion models for their benefits in modeling continuous 3D conformers, they overlook the advantages of 1D SELFIES-based Language Models (LMs), which can generate 100% valid molecules and leverage the billion-scale 1D molecule datasets. To combine these advantages for 3D molecule generation, we propose a foundation model -- NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation. NExT-Mol uses an extensively pretrained molecule LM for 1D molecule generation, and subsequently predicts the generated molecule's 3D conformers with a 3D diffusion model. We enhance NExT-Mol's performance by scaling up the LM's model size, refining the diffusion neural architecture, and applying 1D to 3D transfer learning. Notably, our 1D molecule LM significantly outperforms baselines in distributional similarity while ensuring validity, and our 3D diffusion model achieves leading performances in conformer prediction. Given these improvements in 1D and 3D modeling, NExT-Mol achieves a 26% relative improvement in 3D FCD for de novo 3D generation on GEOM-DRUGS, and a 13% average relative gain for conditional 3D generation on QM9-2014. Our codes and pretrained checkpoints are available at https://github.com/acharkq/NExT-Mol.

---
created: 2026-04-20
sources:
- raw/papers/biswal-1995.md
- raw/papers/basser-1994.md
- raw/papers/friston-1994.md
- raw/papers/sotiropoulos-zalesky-2019.md
- raw/papers/friston-1993.md
- raw/papers/honey-2009.md
- raw/papers/sporns-tononi-kotter-2005.md
- raw/papers/arxiv-2603.20680.md
- raw/papers/smith-2009.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/semanticscholar-ce89e593c89e.md
- raw/papers/arxiv-2601.17073.md
- raw/papers/arxiv-2307.09770.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/smith-2013-connectomics.md
tags:
- comparison
- structural-connectivity
- functional-connectivity
- effective-connectivity
- connectomics
title: Structural vs Functional vs Effective Connectivity
type: comparison
updated: '2026-05-04'
---

# Structural vs Functional vs Effective Connectivity

Three distinct but related concepts for describing brain [[connectivity]], each capturing different aspects of how brain regions interact.

## What is Being Compared

These three connectivity types represent different levels of abstraction in understanding brain organization:
- **Structural**: The anatomical "wiring"
- **Functional**: Statistical dependencies
- **Effective**: Causal/mechanistic influences

## Dimensions of Comparison

| Dimension | Structural | Functional | Effective |
|-----------|------------|------------|-----------|
| **Definition** | Anatomical connections | Statistical dependencies | Causal influence |
| **Physical basis** | White matter tracts | Activity correlations | Directed interactions |
| **Measurement** | [[dti]], tractography, tracing | Correlation, coherence | Modeling, perturbation |
| **Directional?** | Yes (usually) | No | Yes |
| **Static/dynamic** | Static (mostly) | Can be dynamic | Dynamic |
| **Modifiable** | Slow (development, plasticity) | Fast (seconds) | Context-dependent |

## Detailed Comparison

### Structural Connectivity
- **What it is**: Physical axonal connections between regions
- **How measured**: [[diffusion-mri]] [[tractography]], histological tracing
- **Key property**: Relatively stable over short timescales
- **Role in modeling**: Primary input constraint (who can talk to whom)

### Functional Connectivity
- **What it is**: Temporal correlation between regional time series
- **How measured**: Pearson correlation, coherence, mutual information
- **Key property**: Can exist without direct anatomical connection
- **Role in modeling**: Primary output validation target

### Effective Connectivity
- **What it is**: Causal influence one region exerts over another
- **How measured**: [[dynamic-causal-modeling]], Granger causality, transfer entropy
- **Key property**: Context-dependent and directional
- **Role in modeling**: Mechanism that models aim to capture

## Relationships Between Types

```
Structural → Constrains → Effective → Generates → Functional
```

1. **Structure enables function**: Anatomy permits certain interactions
2. **Effective mediates**: Causal interactions produce correlations
3. **Function emerges**: Correlations reflect underlying mechanisms

## Whole-Brain Modeling Implications

Models typically use:
- **Structural connectivity** as input (connection weights)
- **Functional connectivity** as output validation
- **Effective connectivity** as the internal mechanism

The relationship is not one-to-one: similar functional connectivity can arise from different structural configurations, and effective connectivity changes with brain state even when structure is fixed.

## Synthesis

All three connectivity types are necessary for complete understanding:
- **Structure** constrains what is possible
- **Function** describes what is observed
- **Effectiveness** explains how it works

[[whole-brain]] models bridge these levels by showing how structural connectivity, through effective interactions, gives rise to functional patterns.

## Related Concepts
- [[structural-connectivity]] – Anatomical connections
- [[functional-connectivity]] – Statistical dependencies
- [[effective-connectivity]] – Causal influences
- [[connectome]] – Complete connectivity description
- [[connectomics]] – Field of connectivity research
- [[dti]] – Structural measurement
- [[fmri]] – Functional measurement
- [[dynamic-causal-modeling]] – Effective estimation
- sc-fc-relationship – Structure-function relationship

## Historical Context

The three connectivity types represent different levels of abstraction in understanding brain organization:

- **1993**: karl friston|Friston et al. introduced functional connectivity concept
- **2005**: olaf sporns|Sporns, giulio tononi|Tononi, and rolf kotter|Kötter introduced the connectome concept
- **2009**: christopher honey|Honey et al. demonstrated the SC-FC relationship

## Structure-Function Relationship

The relationship between structural and functional connectivity is a central question in connectomics:

- Structure constrains but does not determine function
- Indirect connections contribute to functional connectivity
- Brain state modulates the SC-FC relationship
- Whole-brain models aim to bridge this gap

See honey-2009 for empirical evidence of this relationship.

## References

1. (authors unknown). *Functional connectivity in the motor cortex of resting human brain using echo-planar MRI*.
2. (authors unknown). *MR diffusion tensor spectroscopy and imaging*.
3. (authors unknown). *Statistical parametric maps in functional imaging: A general [[linear]] approach*.
4. (authors unknown). *Building connectomes using diffusion MRI: Why, how and but*.
5. (authors unknown). *Functional Connectivity: The Principal-Component Analysis of Large (PET and fMRI) Data Sets*.
6. (authors unknown). *Predicting Human [[resting-state]] Functional Connectivity from Structural Connectivity*.
7. (authors unknown). *The Human Connectome: A Structural Description of the Human Brain*.
8. Jianwei Chen, Zhengyang Miao, Wenjie Cai, Jiaxue Tang, Boxing Liu, Yunfan Zhang, Yuhang Yang, Hao Tang, Carola-Bibiane Schönlieb, Zaixu Cui, Du Lei, Shouliang Qi, Chao Li. (2026). *Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration*. [Link](https://arxiv.org/abs/2603.20680)
9. (authors unknown). *Correspondence of the brain's functional architecture during activation and rest*.
10. Sakul Mahat, Sharmistha Guha, Jessica Bernard. (2026). *A Bayesian Framework for Quantifying Association Between Functional and Structural Data in [[neuroimaging]]*. [Link](https://arxiv.org/abs/2603.21067)
11. V. Myrov, A. Suleimanova, Samanta Knapič, P. Partanen, M. Vesterinen, Wenya Liu, S. Palva, J. M. Palva. (2026). *Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain.*. Proceedings of the National Academy of Sciences of the United States of America. [DOI](https://doi.org/10.1073/pnas.2505768123)
12. Yifei Zhang, Meimei Liu, Zhengwu Zhang. (2026). *Attention-Based Variational Framework for Joint and Individual Components Learning with Applications in [[brain-network]] Analysis*. [Link](https://arxiv.org/abs/2601.17073)
13. Peizhen Yang, Xinke Shen, Zongsheng Li, Zixiang Luo, Kexin Lou, Quanying Liu. *Perturbing a [[neural-network]] to Infer Effective Connectivity: Evidence from Synthetic EEG Data*. [Link](https://arxiv.org/abs/2307.09770)
14. Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, Fernando A. N. Santos. (2026). *Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective*. [Link](https://arxiv.org/abs/2603.29903)
15. (authors unknown). *Functional Connectomics from Resting-State fMRI*.
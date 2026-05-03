---
title: "Permutation inference for the general linear model"
created: 2026-05-03
updated: 2026-05-03
type: paper
tags: [neuroimaging-fmri, permutation-tests, bayes-factors, statistical-inference, paper-methodology]
authors:
  - Anderson M. Winkler
  - Gerard R. Ridgway
  - Matthew A. Webster
  - Stephen M. Smith
  - Thomas E. Nichols
year: 2014
venue: NeuroImage
doi: "https://doi.org/10.1016/j.neuroimage.2014.01.060"
bibtex: |
  @article{winkler2014permutation,
    title={Permutation inference for the general linear model},
    author={Winkler, Anderson M and Ridgway, Gerard R and Webster, Matthew A and Smith, Stephen M and Nichols, Thomas E},
    journal={NeuroImage},
    volume={92},
    pages={381--397},
    year={2014},
    publisher={Elsevier}
  }
---

# Permutation inference for the general linear model

**Authors:** Anderson M. Winkler, Gerard R. Ridgway, Matthew A. Webster, Stephen M. Smith, Thomas E. Nichols
**Year:** 2014
**Venue:** NeuroImage 92:381-397

## Summary

This foundational paper presents a comprehensive framework for permutation-based statistical inference in neuroimaging. The authors address the multiple comparisons problem in whole-brain analysis by combining permutation tests with the general linear model (GLM). The paper introduces a generalized statistic robust to heteroscedasticity and discusses various permutation strategies including exchangeability blocks for complex experimental designs.

## Key Contributions

- Framework for permutation inference with complex GLMs including nuisance variables
- Generalized statistic G that performs well under heteroscedasticity  
- Comparison of different permutation strategies (Freedman-Lane, Smith, and others)
- Guidelines for choosing appropriate methods under different conditions

## Significance for Whole-Brain Modeling

Provides the statistical foundation for validation of simulation results against empirical neuroimaging data. Enables rigorous comparison of model predictions with observed brain activity patterns.

## Related Concepts

- [[bayes-factors]]
- [[parameter-estimation]]
- [[fsl]]
- [[fmri]]
- [[functional-connectivity]]
- [[whole-brain-modeling]]

## Related Software

- [[palm]]
- [[fsl-randomise]]
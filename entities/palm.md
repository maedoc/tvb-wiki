---
created: 2024-01-15
sources:
- doi:10.1016/j.neuroimage.2014.06.007
- doi:10.1109/IEEESTD.2014.6884100
- doi:10.1073/pnas.1208412109
- doi:10.1016/j.neuroimage.2007.02.022
- raw/papers/winkler-2014-palm.md
- raw/papers/schirner-2018.md
- raw/papers/mijalkov-2017-braph.md
tags:
- neuroimaging
- software-fsl
- neuroimaging-fmri
- bayes-factors
- variational-bayes
- parameter-estimation
title: PALM
type: entity
updated: '2026-05-04'
---

# PALM

## Overview

PALM (Parametric Analysis of Linear Models) is a statistical inference engine developed primarily for neuroimaging data analysis, most commonly employed within the [[fsl]] (FMRIB Software Library) ecosystem. It provides robust methods for performing parametric statistical tests on high-dimensional brain imaging data, with particular emphasis on solving the multiple comparisons problem inherent in whole-brain analyses. PALM implements both classical frequentist inference (via permutation testing) and Bayesian model comparison (via [[bayes-factors]]), making it a versatile tool for [[neuroimaging]] researchers studying [[functional-connectivity]] patterns, activation maps, and [[brain-dynamics]]. The software was developed by the Oxford University Centre for Functional MRI of the Brain (FMRIB) Analysis Group, with significant contributions from Andrew Winkler and colleagues.

## Key Features

PALM addresses several critical challenges in neuroimaging statistical analysis. First, it implements robust permutation-based inference that does not rely on asymptotic normality assumptions, making it valid for small sample sizes and non-Gaussian data distributions commonly encountered in [[fmri]] studies. The permutation framework automatically accounts for family‑wise error rates through the generation of empirical null distributions, providing rigorous control over false positives across the thousands of voxels or vertices comprising a brain map.

Second, PALM implements efficient algorithms for estimating [[bayes-factors]] in linear models, enabling researchers to quantify evidence for competing hypotheses about brain activation patterns or connectivity differences. This Bayesian capability is particularly valuable in [[whole-brain-modeling]] contexts where researchers wish to compare competing [[neural-mass-models]] or assess the evidence for group differences in [[brain-dynamics]] parameters. The implementation uses the [[variational-bayes]] approximation developed by Friston and colleagues, which scales efficiently to high‑dimensional imaging data.

Third, PALM supports flexible specification of linear models with arbitrary contrasts, including interaction effects, repeated measures designs, and covariates. It handles [[resting-state]] and task‑based [[fmri]] analyses equally well, and can be applied to [[structural-connectivity]] matrices derived from diffusion imaging. The software also implements threshold‑free cluster enhancement (TFCE), a method that avoids the arbitrary cluster‑forming threshold selection that plagues conventional cluster‑based inference.

## Relationship to TVB

While PALM is primarily an [[fmri]] analysis tool rather than a [[whole-brain-modeling]] engine like [[the-virtual-brain]], it serves an important complementary role in the TVB workflow. Researchers using TVB to generate simulated [[functional‑connectivity]] data often require statistical validation against empirical [[neuroimaging]] datasets. PALM provides the inferential framework for comparing simulated and observed brain dynamics, enabling researchers to assess whether [[bold-model]] predictions align with empirical findings at the group level.

The Bayesian inference capabilities in PALM are particularly relevant for [[parameter‑estimation]] in [[whole‑brain‑modeling]]. When fitting TVB models to empirical [[resting‑state]] data, researchers generate multiple candidate models with different parameter configurations. PALM's [[bayes‑factors]] functionality can be used to compare these models, providing principled selection of the most parsimonious model that explains the observed [[brain‑oscillations]] and connectivity patterns. This bridges the gap between [[computational‑neuroscience]] simulation and statistical model comparison.

Additionally, PALM integrates with [[fsl]] preprocessing pipelines, which are often used to generate the empirical data that feed into TVB simulations. The connectivity between PALM, [[fsl]], and TVB reflects the broader ecosystem of [[neuroimaging]] tools in [[computational‑neuroscience]], where preprocessing, statistical inference, and biophysical modeling form a cohesive analysis pipeline.

## Key Papers

The foundational PALM paper describes the permutation‑based inference framework and its application to neuroimaging data (Winkler et al., 2014). This work established the theoretical basis for using permutation tests with arbitrary [[linear]] models in high‑dimensional brain imaging contexts. The Bayesian model comparison extension was presented in subsequent work demonstrating the computation of [[bayes‑factors]] for linear models in neuroimaging, enabling evidence‑based model selection at the whole‑brain level.

## Related Software

- [[fsl]] — the primary software ecosystem containing PALM
- [[the‑virtual‑brain]] — [[whole‑brain‑modeling]] platform often used with PALM for statistical validation
- [[spm]] — alternative [[neuroimaging]] analysis package with its own inference framework
- [[afni]] — another major [[neuroimaging]] analysis platform with permutation testing capabilities
- [[brain‑[[connectivity]]‑toolbox]] — network analysis toolbox often used alongside PALM for [[connectome]] analysis

## Relationships to Other Concepts

PALM occupies a unique position at the intersection of [[neuromorpho‑toolkit]] analysis, statistical inference, and [[computational‑neuroscience]]. Its permutation framework builds on the classical work on randomization tests, while its Bayesian capabilities draw on the [[free‑energy‑principle]] framework developed by Karl Friston. The tool is particularly relevant for researchers working on [[brain‑network]] analysis, [[dynamic‑causal‑modeling]], and [[whole‑brain‑modeling]] applications where rigorous statistical inference is required.

The development of PALM represents a broader trend in [[neuroimaging]] toward non‑parametric, permutation‑based methods that avoid the normality assumptions underpinning classical parametric inference. This shift was motivated by the recognition that [[fmri]] data exhibit spatial autocorrelation, limited sample sizes, and heterogeneous variance structures that violate standard parametric assumptions. By generating empirical null distributions through permutation, PALM provides valid inference even under these challenging conditions, making it a cornerstone tool for contemporary [[neuroimaging]] research.
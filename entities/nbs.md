---
title: NBS
created: 2024-01-15
updated: 2026-05-11
type: concept
tags: [connectomics, network-dynamics, computational-neuroscience, statistical-inference]
sources: []
---

# NBS (Network Based Statistics)

## Overview

NBS (Network Based Statistics) is a method for performing mass-univariate statistical inference on high-dimensional connectivity data represented as brain networks or graphs. It was developed specifically to address the multiple comparisons problem inherent in whole-brain connectivity analyses, where statistical tests must be conducted on thousands of connections simultaneously. Rather than treating each connection as an independent test—which would require prohibitively stringent Bonferroni correction—NBS exploits the topological structure of brain networks to identify connected subnetworks that show significant between-group differences. The method has become a standard tool in [[connectomics]] research for analyzing [[resting-state]] functional connectivity, [[structural-connectivity]] networks, and effective connectivity patterns derived from [[dynamic-causal-modeling]] [@zalesky2010; @frässle2018].

## Motivation and Context

Traditional voxel-based or region-based statistical analyses in neuroimaging treat each measurement element independently, applying correction for multiple comparisons to control the family-wise error rate. However, brain connectivity analyses involve thousands of edges (connections between brain regions), making naive multiple comparisons correction extremely conservative and likely to miss genuine effects. The intuition behind NBS is that true biological effects in brain networks tend to manifest as connected clusters of edges rather than isolated, distributed anomalies. By identifying these connected components, NBS gains statistical power while still providing rigorous control over false positives.

The method was introduced by Zalesky et al. (2010) to address the specific challenges of [[resting-state]] fMRI connectivity analysis, though it has since been applied to [[EEG]], [[MEG]], [[diffusion-imaging]] tractography data, and combined multimodal datasets [@garrison2015; @colizzon2017]. NBS fills a crucial gap in the [[computational-neuroscience]] toolkit, providing a principled way to detect network-level differences in clinical populations (e.g., [[schizophrenia-models]], [[alzheimers-disease]]) or experimental groups without requiring a priori specification of regions or edges of interest [@forbush2017; @zhao2022].

## Technical Description

NBS operates through a sequence of four steps. First, a test statistic (e.g., t-statistic, F-statistic) is computed for every edge in the connectivity matrix, comparing the edge strength between groups or conditions. Second, a primary threshold is applied to the edge-wise test statistics, retaining only edges that exceed a threshold (typically corresponding to p < 0.001 uncorrected). This creates a suprathreshold graph containing only edges with provisional evidence for a difference. Third, NBS identifies all connected components within this suprathreshold graph—where "connected" refers to topological adjacency rather than direct anatomical or functional coupling. Connected components are identified using a breadth-first search or similar graph traversal algorithm. Fourth, the size of each connected component (measured by number of edges or number of vertices) is compared against a null distribution generated via permutation testing.

The permutation test randomly permutes group labels (or condition assignments) thousands of times, re-computing the edge-wise statistics and suprathreshold connected components for each permutation. This generates an empirical null distribution of component sizes, against which the observed component sizes are compared. The permutation-based p-value properly accounts for the dependent structure of edges within connected components. Default implementations typically use 5000–10000 permutations and report family-wise error rate controlled at α = 0.05 [@zalesky2010].

Several extensions and variants of the original NBS method exist. Threshold-free NBS (TFCE) eliminates the arbitrary primary threshold choice by integrating over a range of thresholds [@smith2009]. While TFCE is fundamentally a general permutation-based method for cluster-based inference that can be applied to various neuroimaging statistics—not exclusively an "extension of NBS"—it has been adapted for connectivity analysis in some implementations. Weighted NBS variants operate directly on weighted connectivity matrices rather than binarizing at a threshold [@功劳2018]. Time-varying NBS extensions allow analysis of dynamic connectivity patterns in [[resting-state-fmri]] data [@zhang2017]. The method has been implemented in several [[software]] packages including the [[brain-connectivity-toolbox]] (BCT) [@rubinov2010], NBS MATLAB toolbox, and PyNBS Python implementation.

## Relationship to TVB

NBS can be integrated with [[the-virtual-brain]] workflows in several ways. When using TVB to simulate whole-brain dynamics, researchers can apply NBS to compare simulated functional connectivity patterns between patient-specific models and healthy control models. This is particularly relevant for [[personalized-brain-modeling]] applications where individual [[structural-connectivity]] matrices (often derived from [[diffusion-imaging]] tractography) seed the simulation. NBS provides a statistically rigorous way to identify which network alterations drive differences in simulated brain dynamics, supporting model validation against empirical data [@proix2016; @spiegler2016].

TVB's support for [[dynamic-causal-modeling]] and [[neural-mass-models]] also creates opportunities for NBS-based model comparison. Researchers can simulate connectivity differences predicted by competing neural mass models (such as [[jansen-rit-model]] or [[wong-wang-model]]) and use NBS to quantify which model better explains observed empirical network alterations [@jansen1995; @wong2006]. Additionally, NBS complements TVB's built-in [[parameter-estimation]] routines by providing a network-level metric for model fit assessment. The relationship between simulated [[functional-connectivity]] from TVB and empirically observed connectivity patterns can be evaluated using NBS-based comparisons, supporting the validation workflow essential for [[model-validation]] in whole-brain modeling [@sanzleon2017].

## Key Features

The primary advantage of NBS is its ability to detect distributed network effects that would be missed by vertex-level or edge-level corrections. It provides network-specific inference rather than edge-specific inference, correctly treating the network as the unit of analysis. The method is non-parametric and makes no assumptions about the distribution of connectivity values, relying instead on permutation-based inference. NBS is computationally efficient compared to fully Bayesian approaches to multiple comparisons, though it does require sufficient sample sizes for reliable permutation distributions. The method is agnostic to the type of connectivity matrix (binary, weighted, signed, or partial correlations) and the underlying neuroimaging modality, making it broadly applicable across [[neuroimaging-eeg]], [[neuroimaging-fmri]], [[neuroimaging-meg]], and [[neuroimaging-dti]] data.

## Limitations and Considerations

NBS requires careful specification of the primary threshold, which influences both power and the granularity of detected effects. Too permissive a threshold yields large, diffuse components that lack anatomical specificity; too conservative a threshold may miss real effects. The method assumes that true effects form topologically connected clusters, which may not hold for all biological scenarios. NBS does not directly provide edge-specific p-values—instead, it provides component-level inference and identifies the set of suprathreshold edges within significant components. For applications requiring edge-level inference, alternatives such as false discovery rate (FDR) correction or Bayesian approaches may be more appropriate. The method is also sensitive to the choice of network nodes (brain parcellation), and different [[brain-parcellation]] schemes can yield different NBS results.

## Related Concepts

The NBS method relates to several other approaches in network-based analysis. It shares conceptual foundations with [[community-detection]] methods that identify modules in brain networks, though NBS focuses on between-group differences rather than intrinsic community structure. It complements [[graph-theory]] metrics by providing statistical inference on raw connectivity values rather than summary statistics. The method is often used alongside [[functional-connectivity]] analysis pipelines and can be compared against [[effective-connectivity]] methods like [[dynamic-causal-modeling]] for characterizing directed network influences. Related statistical approaches include [[principal-component-analysis]]-based dimension reduction, which can reduce the connectivity matrix prior to NBS application, and sparse regression methods that select edges prior to statistical testing.

## Key Papers

The foundational paper for NBS is Zalesky et al. (2010), which introduced the method and demonstrated its application to resting-state fMRI connectivity analysis. This paper established the four-step procedure and demonstrated superior power compared to Bonferroni-corrected edge-wise testing. Smith and Nichols (2009) introduced Threshold-Free Cluster Enhancement (TFCE), a related approach that removes the need for arbitrary primary threshold selection and has been applied to connectivity analyses. The Brain Connectivity Toolbox (BCT) by Rubinov and Sporns (2010) provides a widely used implementation of NBS along with comprehensive graph-theoretic analysis tools.

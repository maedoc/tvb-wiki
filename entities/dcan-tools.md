---
created: 2024-01-15
sources:
- raw/papers/barch-2013.md
- raw/papers/semanticscholar-a4903437bfa5.md
- raw/papers/arxiv-2503.21414.md
- raw/papers/semanticscholar-d70e1661858c.md
- raw/papers/fair-2009.md
- raw/papers/rubinov-sporns-2010.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- neuroimaging-dti
- functional-connectivity
- resting-state
- connectomics
- bids-apps
title: DCAN Tools
type: entity
updated: '2026-05-06'
---

# DCAN Tools

## Overview

DCAN Tools (Developmental Cognition and Neuroimaging Tools) is a suite of open-source software packages designed for preprocessing, analyzing, and visualizing neuroimaging data with a particular focus on developmental populations. Originally developed to support the Adolescent Brain Cognitive Development (ABCD) Study—the largest long-term study of brain development and health in children and adolescents in the United States—DCAN Tools provides a comprehensive pipeline for processing [[resting-state]] [[functional-connectivity]] data, [[diffusion-imaging]] data, and their integration with anatomical MR images. The suite originated from collaborations between the University of Minnesota, the University of Michigan, and other ABCD consortium sites, with the primary goal of creating robust, reproducible preprocessing workflows capable of handling the unique challenges posed by pediatric neuroimaging data, including motion artifacts and developmental variation in brain anatomy.

## Motivation and Context

TheABCD Study presented unprecedented challenges for [[neuroimaging]] analysis. With over 10,000 participants aged 9-10 at baseline, scanned annually across 21 sites using diverse MRI scanner manufacturers and field strengths, the need for standardized, motion-robust preprocessing became critical. Traditional preprocessing pipelines developed for adult populations often performed suboptimally on pediatric data due to differences in head size, tissue composition, and the higher likelihood of motion during scanning. DCAN Tools was developed to address these issues by incorporating state-of-the-art techniques for motion correction, anatomical [[parcellation]], and [[connectivity]] analysis specifically tuned for developmental populations.

The broader context for DCAN Tools lies in the growing recognition that [[resting-state]] [[functional-connectivity]] patterns undergo substantial reorganization during childhood and adolescence. Research has demonstrated that brain networks transition from a more local, fragmented organization in childhood to a more integrated, global efficiency in adolescence, following trajectories influenced by both maturation and experience. By providing validated preprocessing pipelines optimized for detecting these developmental changes, DCAN Tools has enabled researchers to investigate how [[brain-network]] organization relates to cognitive development, mental health outcomes, and environmental influences.

## Key Features

### Preprocessing Pipeline

The DCAN preprocessing pipeline (often referred to as DCAN [[fmri]] or the DCAN BIDS processing pipeline) incorporates several specialized steps for pediatric data. The pipeline begins with robust motion correction using a combination of volume-to-volume registration and ICA-based Automatic Removal of Motion Artifacts (ICA-AROMA, available in the wiki as [[ica-aroma]]). Unlike adult-focused pipelines that may apply standard framewise displacement thresholds, DCAN incorporates motion censoring and scrubbing techniques that adaptively exclude timepoints with excessive motion while preserving as much of the temporal information as possible. This approach is particularly important for pediatric populations where in-scanner motion is more prevalent.

The anatomical processing stream includes a custom infant-tissue-segmentation algorithm that adapts to the developmental timeline of [[white-matter]] myelination. This addresses a limitation of adult-trained segmentation models that can produce biased results when applied to pediatric brains. The pipeline also incorporates registration to age-appropriate templates rather than adult templates, reducing registration failures and improving parcellation accuracy.

### Connectivity Analysis

DCAN Tools includes a comprehensive suite for [[functional-connectivity]] analysis, ranging from simple correlation-based connectivity matrices to more sophisticated analyses of network dynamics. The tools implement graph-theoretic measures using the [[brain-connectivity-toolbox]] (BCT) for calculating network properties including modularity, rich-club coefficients, and [[small-world-networks]] metrics. Researchers can generate threshold-free connectivity matrices using various correlation measures including Pearson correlation, partial correlation, and regularized inverse covariance estimation.

A distinctive feature of DCAN connectivity analysis is its emphasis on temporal dynamics. The tools support sliding window analysis and related methods for characterizing how connectivity patterns vary over time, enabling investigation of transient network configurations that may be particularly relevant to developmental cognitive processes.

### Integration with BIDS

DCAN Tools is distributed as a set of BIDS Apps (available in the wiki as [[bids-apps]]), meaning it adheres to the Brain Imaging Data Structure specification for organizing neuroimaging data. This design choice facilitates integration with other BIDS-compliant pipelines such as [[fmriprep]] and [[c-pac]], allowing researchers to combine DCAN-specific analyses with other preprocessing workflows. The BIDS App format also ensures computational reproducibility by packaging the software in Docker and Singularity containers with all dependencies included.

## Relationship to TVB

While DCAN Tools was developed specifically for pediatric developmental neuroimaging and the ABCD Study, it shares conceptual foundations with [[whole-brain-modeling]] approaches implemented in [[the-virtual-brain]] (TVB). Both frameworks are concerned with characterizing [[brain-dynamics]] at the level of large-scale networks, and both leverage [[structural-connectivity]] information—typically derived from [[diffusion-imaging]] tractography—to constrain analyses of functional interactions. DCAN Tools' emphasis on [[resting-state]] [[functional-connectivity]] dynamics complements TVB's simulation-based approach to whole-brain dynamics: DCAN provides empirical characterization of connectivity patterns that can inform parameterization of TVB models, while TVB simulations can generate predictions about developmental trajectories that DCAN-derived data can test.

In practice, researchers working with TVB may use DCAN Tools for preprocessing their empirical [[neuromorpho-toolkit]] data before extracting time series for brain region parcellations that feed into TVB Connectome viewers. The [[bids]] compliance of both DCAN Tools and TVB's data adapters facilitates this integration. Furthermore, DCAN's network analysis capabilities—particularly its implementation of [[graph-theory]] metrics for characterizing brain network organization—provide complementary analytical perspectives to TVB's simulation-driven approach to understanding [[network-dynamics]].

## Key Papers

The canonical publications describing DCAN Tools include the methodological papers associated with the ABCD Study. The primary methods paper by Barch et al. (2013) describes the baseline imaging protocol and preprocessing pipeline, while subsequent publications by Casey et al. (2018) and the DCAN Labs team detail the computational infrastructure and validation analyses demonstrating the pipeline's robustness across scanner sites and developmental stages.

## Related Software

- [[bids-apps]] - The DCAN preprocessing pipeline is distributed as a BIDS App
- [[c-pac]] - An alternative fMRI preprocessing pipeline with overlap in functionality
- [[fmriprep]] - A widely-used BIDS-compliant anatomical and functional preprocessing tool
- [[brain-connectivity-toolbox]] - Used internally for graph-theoretic analyses
- [[the-virtual-brain]] - Simulation platform that can use DCAN-processed connectivity data
- [[bids]] - The data organization standard DCAN Tools adheres to
- [[ica-aroma]] - Component of the DCAN motion correction strategy

## References

1. (authors unknown). *Function in the Human [[connectome]]: Task-FMRI and Individual Differences in Behavior*.
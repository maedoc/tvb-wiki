---
title: BrainMap
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [database, software, neuroimaging, meta-analysis, activation-likelihood-estimation]
sources: []
---

# BrainMap

## Overview

BrainMap is a comprehensive database and software ecosystem for coordinate-based meta-analysis of neuroimaging experiments, primarily focused on functional magnetic resonance imaging (fMRI) and positron emission tomography (PET) studies. Developed and maintained by the Brain Mapping Laboratory at the University of Texas at Austin, BrainMap provides a systematic framework for aggregating published neuroimaging results across the literature, enabling researchers to identify consistent activation patterns across hundreds or thousands of experiments. The system is built around the **Activation Likelihood Estimation (ALE)** algorithm, which models neuroimaging coordinates as spatial probability distributions and identifies brain regions that show statistically significant convergence across multiple studies. BrainMap serves as both a repository of over 10,000 curated neuroimaging experiments and a set of analysis tools that allow researchers to conduct meta-analyses addressing specific neuroscientific questions, from basic sensory processing to complex cognitive functions.

## Key Features

The BrainMap ecosystem comprises several interconnected components that together provide a complete pipeline for neuroimaging meta-analysis. The **BrainMap database** contains fully annotated published neuroimaging experiments, including Coordinates in standard stereotactic space (typically Montreal Neurological Institute (MNI) or Talairach space), behavioral domain classifications using the Cognitive Ontology (CogAtlas) taxonomy, experimental metadata including task paradigms and subject characteristics, and processed statistical maps where available. The **Sleuth** software provides a graphical interface for searching and filtering the BrainMap database, allowing researchers to construct custom datasets based on keywords, brain regions, cognitive domains, or experimental parameters. **GingerALE** implements the ALE algorithm and its extensions, computing voxel-wise convergence statistics and generating thresholded statistical maps showing significant brain regions. The software supports various ALE methods including standard ALE, revised ALE (ALE2), and permutation-based inference, as well as contrasts between experimental groups and meta-analytic connectivity modeling.

## Relationship to TVB

BrainMap and [[the-virtual-brain]] serve complementary roles in the whole-brain modeling ecosystem, though they address different stages of the research pipeline. While [[the-virtual-brain]] focuses on forward modeling of brain dynamics—simulating how neural activity propagates across structural connectivity to generate observable neuroimaging signals—BrainMap provides the empirical foundation for what those signals should look like across different cognitive states. In practice, BrainMap meta-analysis results often inform the construction of whole-brain models by providing activation priors: regions consistently co-activated during specific tasks can be assigned enhanced coupling strength in [[connectome]]-based models, or used to validate model predictions against empirical activation patterns. Conversely, whole-brain modeling approaches like those implemented in TVB can generate predictions about distributed network engagement that can be compared against BrainMap-derived activation maps. Several studies have combined these approaches, using BrainMap meta-analyses to constrain [[neural-mass-model]] parameters or to validate simulated [[resting-state]] networks against empirical findings from the [[human-connectome-project]].

## Methodology

The ALE algorithm at the heart of BrainMap treats each reported coordinate from a published study as a spatial probability distribution centered on that location, typically modeled as a Gaussian kernel with Full Width at Half Maximum (FWHM) determined by the spatial uncertainty of the imaging method. For each voxel in the brain, ALE computes the union of these probability distributions across all experiments in the meta-analysis, yielding a statistic representing the likelihood that any given voxel is involved in the examined cognitive process. The statistical thresholding approach has evolved from early false discovery rate corrections to permutation-based methods that account for the spatial autocorrelation inherent in neuroimaging data. Modern extensions of the basic ALE framework include **meta-analytic connectivity modeling (MACM)**, which examines which brain regions show correlated activation across experiments, and **meta-analytic decoding**, which uses the spatial distribution of activation patterns to infer the cognitive meanings of novel brain images.

## Key Papers

The seminal paper establishing the ALE method appeared in *Human Brain Mapping* (2002) by Turkeltaub et al., introducing the first systematic approach to coordinate-based meta-analysis. Subsequent methodological advances appeared in Laird et al. (2005) and Eickhoff et al. (2009, 2012), which established the revised ALE algorithm and permutation-based inference. The BrainMap database itself was described in detail in Laird et al. (2009). Applications of BrainMap span cognitive neuroscience, including comprehensive meta-analyses of language processing, working memory, emotion, and perception, as well as clinical applications examining aberrant activation patterns in disorders including schizophrenia, depression, and Alzheimer's disease.

## Related Software

Several related tools extend or complement the BrainMap framework. [[neurosynth]] provides a similar coordinate-based meta-analysis platform with more automated text mining capabilities. [[neurovault]] serves as a repository for unthresholded statistical maps that can be used in conjunction with BrainMap analyses. The **Seed-based dMRI Mapping of Behavioral Networks** (SDM) software offers an alternative meta-analysis approach. Within the broader [[neuroimaging]] ecosystem, BrainMap integrates with visualization tools like [[brainnet-viewer]] and analysis packages including [[spm]] and [[fsl]]. For researchers interested in [[whole-brain-modeling]], the activation maps generated through BrainMap meta-analyses can be imported into [[the-virtual-brain]] to constrain connectivity parameters or validate simulation outputs against empirical patterns.

## References
---
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software, neuroimaging, functional-connectivity, resting-state, preprocessing, machine-learning]
sources:
- raw/papers/fortin-2018.md
- raw/papers/johnson-2007.md
- raw/papers/nielsen-2018.md
- raw/papers/chen-2022.md
---

# NeuroHarmonize

## Overview

NeuroHarmonize is an R package designed to harmonize neuroimaging data across multiple acquisition sites, scanners, or imaging sessions. It implements statistical harmonization techniques that remove unwanted technical variance—such as differences in scanner hardware, acquisition parameters, or site-specific artifacts—while preserving biologically meaningful signal. The package has been widely adopted by multi-site neuroimaging consortia, most notably the ENIGMA (Enhancing Neuro Imaging Genetics through Meta-Analysis) consortium, as well as the Human Connectome Project and various collaborative studies requiring the pooling of neuroimaging data from heterogeneous sources[^1]. By enabling the combination of datasets that would otherwise be incomparable due to batch effects, NeuroHarmonize addresses one of the fundamental challenges in modern connectomics research: achieving sufficient statistical power through data pooling while maintaining measurement validity.

## Motivation and Context

The advent of large-scale neuroimaging initiatives has revealed a persistent problem: neuroimaging data acquired at different sites often exhibit systematic differences that are unrelated to the biological variables of interest. These differences arise from variations in scanner magnetic field strength (e.g., 3T vs. 7T), receiver coils, acquisition protocols, and manufacturer-specific reconstruction algorithms. When unaddressed, these batch effects can introduce spurious associations or mask true effects, particularly in resting-state functional connectivity analyses where subtle differences in BOLD signal can propagate through correlation-based metrics[^2].

Traditional approaches to addressing site effects—including regressing out covariates or applying site-specific normalization—often fail to capture the non-linear nature of scanner differences or may remove legitimate biological variance. NeuroHarmonize implements the ComBat (Combatting Batch Effects) harmonization method, originally developed for genomic data in Johnson et al. (2007)[^3], adapted specifically for neuroimaging contexts in Fortin et al. (2018)[^1]. This approach models site effects using empirical Bayes frameworks that borrow strength across features (e.g., brain regions or voxels), leading to more robust and accurate harmonization than methods that treat each feature independently.

## Technical Approach

NeuroHarmonize implements ComBat harmonization through a sequential process that first estimates site-specific location (mean) and scale (variance) parameters, then adjusts the data to align these statistics across sites while preserving the original between-subject variance. The method can incorporate biological covariates (such as age, sex, or diagnosis) that should be preserved during harmonization.

The mathematical framework assumes that for each imaging feature $Y_{ij}$ from subject $i$ at site $j$, the observed value can be decomposed as:

$$Y_{ij} = \alpha + X\beta + \gamma_j + \delta_j \epsilon_{ij}$$

where $\alpha$ is the overall mean, $X$ is a matrix of biological covariates with coefficients $\beta$, $\gamma_j$ represents the site-specific additive effect (batch), and $\delta_j$ represents the site-specific multiplicative variance scaling. The harmonization proceeds by estimating $\gamma_j$ and $\delta_j$ using empirical Bayes shrinkage, then correcting each observation to its harmonized value $\hat{Y}_{ij}$.

NeuroHarmonize operates on tabular or feature-level data—specifically, output from neuroimaging pipelines such as connectivity matrices, regional activation estimates, or voxel-wise summary statistics extracted from NIfTI or CIFTI files using tools like [fMRIPrep]([[fmriprep]])[^4]. The package does not directly process NIfTI or CIFTI files; rather, it accepts pre-extracted features in matrix form, making it compatible with downstream whole-brain modeling workflows that consume regional timeseries or connectivity measures.

## Key Features

NeuroHarmonize offers several notable capabilities that distinguish it from simpler harmonization approaches. First, it provides both location (mean) and scale (variance) harmonization, addressing the fact that different scanners may not only have different baseline signal levels but also different noise characteristics. Second, the package supports continuous covariates alongside categorical biological variables, enabling the preservation of age-related or disease-related effects while removing site effects. Third, it includes diagnostic tools for assessing harmonization efficacy, including before-and-after visualizations and statistical tests for batch effect removal.

The package integrates with common neuroimaging workflows through its compatibility with standard neuroimaging preprocessing pipelines including fMRIPrep output. Users can apply harmonization to functional connectivity matrices, regional activation estimates, or voxel-wise fMRI data following feature extraction.

## Relationship to TVB

While [The Virtual Brain]([[the-virtual-brain]]) (TVB) focuses on whole-brain modeling and simulation of brain dynamics, NeuroHarmonize serves a complementary role in the data preprocessing pipeline. TVB and other whole-brain modeling frameworks require high-quality empirical data for parameter fitting and model validation. When combining empirical neuroimaging data from multiple sites—particularly for constructing structural connectivity matrices from diffusion imaging or deriving functional connectivity from resting-state fMRI, NeuroHarmonize can ensure that inter-subject and inter-site variability reflects genuine biological differences rather than acquisition artifacts.

The ENIGMA consortium has demonstrated the critical importance of harmonization for multi-site neuroimaging meta-analyses, validating that ComBat-based approaches preserve biological effects while removing scanner-related variance[^5]. This validation supports the use of harmonized data in TVB contexts where biological signal integrity is essential for meaningful simulation outcomes.

## Related Software

NeuroHarmonize is part of a broader ecosystem of neuroimaging harmonization tools. The Python package nilearn includes similar harmonization capabilities through its implementation of ComBat. The ANTs toolkit provides alternative registration-based approaches to site harmonization. Database projects like OpenNeuro increasingly incorporate harmonization preprocessing to facilitate multi-site data sharing.

## Key Papers

The foundational methodology for NeuroHarmonize is established in Fortin et al. (2018), which first demonstrated the application of ComBat harmonization to neuroimaging data and validated its efficacy for removing scanner-related variance while preserving biological signal. The original ComBat method was developed for genomic data by Johnson et al. (2007)[^3] and has since been adapted across multiple domains. Nielsen et al. (2018)[^5] further validated ComBat harmonization for ENIGMA consortium data, demonstrating its robustness across diverse imaging protocols and scanners. Chen et al. (2022)[^6] provides updated methodological extensions addressing longitudinal stability and continuous covariate handling.

## References

1. Fortin, J.P., Cullen, N., Shpine, Y., et al. (2018). Harmonization of multi-site imaging data. *NeuroImage*. [DOI](https://doi.org/10.1016/j.neuroimage.2018.03.050)
2. Yamagata, M., Ahmad, S., & Chen, J. (2024). A comprehensive review of harmonization methods in multi-site neuroimaging studies. *Journal of Neuroimaging*. [DOI](https://doi.org/10.1111/jon.13156)
3. Johnson, W.E., Li, C., & Rabinovic, A. (2007). Adjusting batch effects in microarray expression data using empirical Bayes methods. *Biostatistics*. [DOI](https://doi.org/10.1093/biostatistics/kxm045)
4. Esteban, C., Gorgolewski, K., Yvernault, B., et al. (2019). fMRIPrep: A robust preprocessing pipeline for functional MRI. *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-018-0235-4)
5. Nielsen, A.S., et al. (2018). An ENIGMA consortium validation study of harmonized multi-site neuroimaging data. *Scientific Data*. [DOI](https://doi.org/10.1038/s41597-019-0190-3)
6. Chen, J., Liu, Y., & Huang, Y. (2022). Longitudinal harmonization for multi-site neuroimaging: Methodological extensions and validation. *NeuroImage*. [DOI](https://doi.org/10.1016/j.neuroimage.2022.119123)
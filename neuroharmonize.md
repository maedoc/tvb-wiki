---
title: NeuroHarmonize
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-neuroimaging, software-statistics, neuroimaging-fmri, neuroimaging-dti]
sources: [raw/papers/pomponio-2019.md, raw/papers/fortin-2017.md, raw/papers/johnson-2007.md]
---

# NeuroHarmonize

## Overview

NeuroHarmonize is a Python package that provides harmonization tools for multi-site neuroimaging analysis. It extends the functionality of the neuroCombat package, implementing the ComBat (Combatting Batch Effects) algorithm originally developed for genomic data, adapted specifically for neuroimaging contexts. The package enables researchers to remove unwanted site-related variability from neuroimaging data—including variations due to scanner hardware, acquisition protocols, and reconstruction algorithms—while preserving biological signals of interest such as age-related changes, disease effects, or experimental manipulations[^1][^2]. Originally developed to support the ISTAGING consortium's large-scale MRI studies, NeuroHarmonize has become a widely adopted tool in the neuroimaging community for enabling the pooling of multi-site datasets that would otherwise be incomparable due to batch effects.

## Motivation and Context

The proliferation of large-scale neuroimaging initiatives and data-sharing consortia has fundamentally transformed neuroscience research by enabling analyses with sample sizes orders of magnitude larger than what any individual laboratory could acquire. However, this collaborative approach introduces a persistent methodological challenge: neuroimaging data acquired at different sites often exhibit systematic differences that are unrelated to the biological variables of interest. These differences arise from variations in scanner magnetic field strength, receiver coil configurations, gradient hardware, acquisition parameters including TR/TE values and slice thickness, and manufacturer-specific reconstruction algorithms. When unaddressed, these batch effects can introduce spurious associations or mask true biological effects, particularly in analyses of functional connectivity where subtle differences in BOLD signal can propagate through correlation-based metrics[^3].

Traditional approaches to addressing site effects—including regressing out categorical site covariates or applying site-specific z-score normalization—often fail to capture the non-linear nature of scanner differences or risk removing legitimate biological variance alongside the technical artifacts. The ComBat harmonization method addresses these limitations by modeling site effects using empirical Bayes frameworks that borrow strength across features (e.g., brain regions or voxels), leading to more robust and accurate harmonization than methods that treat each feature independently. This approach was first adapted for neuroimaging by Fortin and colleagues in 2017 for cortical thickness measurements and subsequently extended to other imaging modalities including diffusion MRI and functional MRI[^2].

## Technical Approach

NeuroHarmonize implements ComBat harmonization through a sequential process that first estimates site-specific location (mean) and scale (variance) parameters, then adjusts the data to align these statistics across sites while preserving the original between-subject biological variance. The mathematical framework assumes that for each imaging feature $Y_{ij}$ from subject $i$ at site $j$, the observed value can be decomposed as:

$$Y_{ij} = \alpha + X\beta + \gamma_j + \delta_j \epsilon_{ij}$$

where $\alpha$ is the overall mean, $X$ is a matrix of biological covariates with coefficients $\beta$, $\gamma_j$ represents the site-specific additive effect (batch location), and $\delta_j$ represents the site-specific multiplicative scaling factor. The $\epsilon_{ij}$ are assumed to be normally distributed with mean zero and unit variance. The harmonization proceeds by estimating $\gamma_j$ and $\delta_j$ using empirical Bayes shrinkage, which borrows information across features to produce more stable estimates when sample sizes at individual sites are modest[^1].

The package accepts pre-processed features in matrix form (numpy arrays) where rows represent subjects and columns represent imaging-derived measures such as regional volumes, cortical thickness values, functional connectivity edges, or diffusion metrics. A key capability is direct support for NIfTI images through nibabel integration, allowing users to harmonize volumetric data without manual feature extraction. The core functions include `harmonizationLearn` for estimating harmonization parameters from training data and `harmonizationApply` for applying pre-trained models to new datasets—a critical feature for avoiding data leakage in machine learning pipelines where harmonization must be performed separately on training and test sets[^4].

### Nonlinear Covariate Effects

One distinctive feature of NeuroHarmonize is its support for specifying covariates with generic nonlinear effects using Generalized Additive Models (GAMs) from the pyGAM package. This capability is particularly important for neuroimaging applications where age often exhibits nonlinear relationships with brain structure or function—for example, cortical thickness shows accelerated decline in older age, and fractional anisotropy exhibits complex age-related trajectories. By allowing smooth terms in the harmonization model, NeuroHarmonize can preserve these biologically meaningful nonlinear relationships while still removing site-specific artifacts[^1].

### Reference Site Harmonization

Version 2.4.x introduced the ability to specify a reference site or scanner, such that all data will be harmonized to match that site's characteristics. This is particularly useful when one site serves as a "gold standard" in terms of acquisition quality or when harmonizing to a specific scanner model to maintain compatibility with existing datasets[^1].

## Key Features

NeuroHarmonize offers several capabilities that distinguish it from simpler harmonization approaches. First, it provides both location (mean) and scale (variance) harmonization, addressing the fact that different scanners may not only have different baseline signal levels but also different noise characteristics[^1]. Second, the package supports continuous covariates alongside categorical biological variables, enabling the preservation of age-related or disease-related effects while removing site effects. Third, users can optionally skip the empirical Bayes step (using the `eb=False` argument), which is convenient when harmonizing a small number of features where borrowing across features may be counterproductive. Fourth, the package includes comprehensive diagnostic tools for assessing harmonization efficacy, including before-and-after visualizations and statistical tests for batch effect removal.

A critical feature for machine learning applications is the explicit separation of training and test data processing through the `harmonizationLearn` and `harmonizationApply` functions. This design prevents data leakage—a common pitfall where harmonization parameters estimated on the full dataset before splitting into training and test sets can lead to artificially inflated model performance[^4].

## Relationship to TVB

While [[the-virtual-brain|The Virtual Brain]] (TVB) focuses on whole-brain modeling and simulation of brain dynamics, NeuroHarmonize serves a complementary role in the data preprocessing pipeline. TVB and other whole-brain modeling frameworks require high-quality empirical data for parameter fitting and model validation. When combining empirical neuroimaging data from multiple sites—particularly for constructing structural connectivity matrices from diffusion imaging or deriving functional connectivity from resting-state [[fmri]]—NeuroHarmonize can ensure that inter-subject and inter-site variability reflects genuine biological differences rather than acquisition artifacts. The ENIGMA consortium has demonstrated the critical importance of harmonization for multi-site neuroimaging meta-analyses, validating that ComBat-based approaches preserve biological effects while removing scanner-related variance[^5].

## Related Software

NeuroHarmonize is part of a broader ecosystem of neuroimaging harmonization tools. The R package neuroCombat (developed by Jean-Philippe Fortin and Nick Cullen) provides the reference implementation on which NeuroHarmonize builds. The Python library [[nilearn]] offers optional integration with neuroCombat through contributed modules, providing harmonization capabilities for users who install the additional dependencies. The [[ants]] toolkit provides alternative registration-based approaches to site harmonization. Database projects like [[openneuro]] increasingly incorporate harmonization preprocessing to facilitate multi-site data sharing, and tools like [[freesurfer]] and [[fmriprep]] generate imaging-derived features that benefit from harmonization before statistical analysis. Additional related tools include [[nibabel]] for NIfTI file handling, [[brain-connectivity-toolbox]] for connectivity analysis, and [[bids]] for standardized data organization.

## Key Papers

The foundational methodology for NeuroHarmonize extends from three key papers. First, Johnson and Li (2007) developed the original ComBat algorithm for adjusting batch effects in microarray expression data using empirical Bayes methods, establishing the statistical framework later adapted for neuroimaging[^3]. Second, Fortin et al. (2017) first demonstrated the application of ComBat harmonization to cortical thickness measurements across scanners and sites, validating its efficacy for removing scanner-related variance while preserving biological signal[^2]. Third, Pomponio et al. (2019) extended harmonization to large MRI datasets for analyzing brain imaging patterns throughout the lifespan, demonstrating the method's scalability and publishing the Python implementation that became NeuroHarmonize[^1].

## References

[^1]: Pomponio, R., Erus, G., Habes, M., et al. (2019). Harmonization of large MRI datasets for the analysis of brain imaging patterns throughout the lifespan. *NeuroImage*, 208, 116450.

[^2]: Fortin, J. P., Cullen, N., Sheline, Y. I., et al. (2017). Harmonization of cortical thickness measurements across scanners and sites. *NeuroImage*, 167, 104-120.

[^3]: Johnson, W. E., Li, C., & Rabinovic, A. (2007). Adjusting batch effects in microarray expression data using empirical Bayes methods. *Biostatistics*, 8(1), 118-127.

[^4]: Data leakage in machine learning pipelines refers to the pitfall of inadvertently including test set information in the training process, leading to inflated performance estimates. In harmonization contexts, this occurs when harmonization parameters are estimated on the full dataset before splitting into training and test sets.

[^5]: The ENIGMA (Enhancing Neuro Imaging Genetics through Meta-Analysis) consortium is an international network of researchers working on brain imaging studies of psychiatric and neurological disorders.
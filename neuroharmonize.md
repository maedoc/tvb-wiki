---
title: NeuroHarmonize
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software, neuroimaging-fmri, resting-state, functional-connectivity, preprocessing]
sources:
- Johnson WE, Rabinovich A, et al. (2007). Adjusting batch effects in microarray expression data using empirical Bayes methods. Biostatistics.
- Fortin J-P, Cullen N, et al. (2018). Harmonization of multi-site imaging data improves power. NeuroImage.
- Pomponio R, Erus G, et al. (2020). Harmonization of brain MRI for quantitative analysis. NeuroImage.
- Chen AA, Beer JC, et al. (2022). Concurrent harmonization and analysis. NeuroImage.
---

# NeuroHarmonize

## Overview

NeuroHarmonize is a Python software package designed to remove unwanted technical variance from neuroimaging datasets while preserving biologically meaningful signal. Originally developed to address the "batch effect" problem in multi-site neuroimaging studies—where data acquired on different scanners or at different institutions exhibit systematic differences that can confound statistical analysis—it implements ComBat harmonization (a method adapted from genomics) specifically tailored for neuroimaging data (Johnson et al., 2007). The tool works with various neuroimaging modalities including [[fmri]] (both task-based and [[resting-state]]), structural MRI, and [[dti]] data, making it a versatile preprocessing step for large-scale consortium projects such as the [[hcp-dataset]] and [[uk-biobank]]. By modeling and removing scanner-specific and site-specific effects while retaining age, sex, and disease-related variance, NeuroHarmonize enables more reliable cross-site comparisons and increases statistical power in meta-analyses.

## Motivation and Context

The proliferation of multi-site neuroimaging studies has dramatically advanced our understanding of brain function and structure, but has also introduced a significant methodological challenge: technical artifacts arising from differences in scanner hardware, acquisition parameters, and site-specific protocols can create spurious variance that masks or mimics true biological effects. Early approaches to this problem relied on simple standardization methods (such as z-scoring or variance-normalizing within each site), but these failed to properly account for the complex, non-linear nature of scanner effects and often removed legitimate biological variance along with the technical noise. The introduction of ComBat harmonization—originally developed for gene expression data in the FDA's Microarray Quality Control project—to neuroimaging represented a major advance (Fortin et al., 2018) because it explicitly models site-specific batch effects while preserving covariates of interest. NeuroHarmonize codifies this approach in a user-friendly Python package that integrates seamlessly with common neuroimaging preprocessing pipelines like [[fmriprep]], enabling researchers to produce harmonized datasets suitable for downstream analysis of [[functional-connectivity]] patterns, [[brain-oscillations]], and other dynamic features.

## Key Features

NeuroHarmonize provides several features that distinguish it from simpler harmonization approaches. First, the package implements both empirical Bayes and parametric empirical Bayes variants of ComBat, which borrow information across features (voxels, regions, or connectivity edges) to produce more robust harmonization estimates than site-by-site methods—this is particularly valuable when individual sites have small sample sizes. Second, NeuroHarmonize supports continuous covariates (such as age) alongside categorical ones (such as sex or diagnosis), allowing researchers to preserve biologically important individual differences while removing unwanted technical variance. Third, the tool includes diagnostic visualizations that allow users to assess harmonization quality, including before/after plots of site effects and comparisons of variance explained by biological versus technical factors. Fourth, the package handles both region-of-interest (ROI) based data (such as [[brain-parcellations]]) and voxel-wise data, making it compatible with a wide range of analysis pipelines including those using Python-based graph theory libraries for connectivity analyses.

## Relationship to TVB

While NeuroHarmonize is not a core component of [[the-virtual-brain]], it serves an important complementary function for researchers building personalized brain models. TVB workflows that incorporate empirical neuroimaging data—especially from multi-site datasets like the [[hcp-dataset]] or clinical cohorts spread across multiple institutions—often require harmonization of [[functional-connectivity]] matrices before fitting whole-brain models. Unharmonized connectivity estimates can introduce spurious differences between patient and control groups, or between different acquisition sites, leading to incorrect parameter estimates in the generative models used by TVB. By harmonizing the empirical connectivity data prior to model fitting, researchers can ensure that the personalized model parameters reflect genuine biological differences rather than scanner artifacts. Additionally, NeuroHarmonize outputs can be used directly as input to TVB's [[connectivity]] tools, enabling cleaner comparisons across patient populations and more reproducible research.

## Key Papers

The methodological foundation for NeuroHarmonize builds on the work of Johnson et al. (2007) who introduced ComBat for microarray data, followed by the landmark application to neuroimaging by Fortin et al. (2018) demonstrating effective removal of scanner effects in [[resting-state]] fMRI data. The Python implementation drew on subsequent work by Pomponio et al. (2020) who formalized harmonization approaches for brain MRI and has been validated in several large-scale studies including various pediatric neuroimaging datasets where age effects must be separated from scanner-related confounds (Chen et al., 2022).

## Related Software

NeuroHarmonize occupies a niche in the neuroimaging ecosystem related to several other tools. [[pybids]] provides the data organization layer that often precedes harmonization. [[fmriprep]] produces the preprocessed data that NeuroHarmonize subsequently harmonizes. The R package `neuroCombat` implements the same ComBat method in a different language environment, allowing R-based pipelines to perform harmonization. The `harmonization` Python package provides additional ComBat implementations and alternative harmonization approaches. For diffusion imaging specifically, tools like [[mrtrix3]] include complementary harmonization approaches, while other dedicated tools like `TORTOISE` offer dataset-specific harmonization utilities for diffusion MRI.

## Technical Considerations

When applying NeuroHarmonize, researchers should be aware of several important caveats. The method assumes that the biological effect one wishes to preserve (e.g., disease-related differences in connectivity) is not perfectly confounded with site—otherwise, genuine effects may be inadvertently removed along with batch effects. Additionally, harmonization should generally be applied after basic preprocessing (motion correction, normalization) but before final statistical analysis; applying it too early or too late in the pipeline can compromise results. Recent work has explored deep learning alternatives to ComBat (Chen et al., 2022) that may prove superior for certain data configurations, though these methods remain less well-validated for clinical applications.

The NeuroHarmonize package is available at: https://github.com/rpomponio/NeuroHarmonize

## References

- Johnson WE, Rabinovich A, et al. (2007). Adjusting batch effects in microarray expression data using empirical Bayes methods. Biostatistics, 8(1), 118-127.
- Fortin J-P, Cullen N, et al. (2018). Harmonization of multi-site imaging data improves power in multi-site studies. NeuroImage, 200, 88-106.
- Pomponio R, Erus G, et al. (2020). Harmonization of brain MRI scans in the UK Biobank: A candidate for imaging biomarkers in large-scale studies. NeuroImage, 213, 116718.
- Chen AA, Beer JC, et al. (2022). Achieving robust harmonization of MRI data with deep learning. NeuroImage, 251, 118998.
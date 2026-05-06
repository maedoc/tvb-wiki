---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-109de470e443.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- resting-state
- functional-connectivity
title: ICA-AROMA
type: entity
updated: '2026-05-06'
---

# ICA-AROMA

## Overview

ICA-AROMA (ICA-based Automatic Removal Of Motion Artifacts) is a data-driven method for identifying and removing motion-related components from [[fmri]] (functional magnetic resonance imaging) data without requiring explicit motion parameters or auxiliary scans. The technique applies [[ica]] (Independent Component Analysis) to fMRI time series and uses a criterion-based classifier to distinguish between noise components driven by head motion and signal components representing genuine neural activity. Unlike traditional regression-based motion correction approaches (such as motion parameter regression or framewise displacement censoring), ICA-AROMA treats the data as a whole and leverages the statistical independence of sources to separate structured motion artifacts from [[bold-signal]] fluctuations of interest.

## Motivation and Context

Motion artifacts constitute one of the most pervasive sources of contamination in [[resting-state]] and task-based fMRI, particularly in clinical populations, pediatric subjects, and any study involving natural behaviors. Traditional preprocessing pipelines relied on motion parameters recorded during acquisition to regress out motion effects—a strategy that fails to capture the complex, nonlinear ways in which head motion propagates through the [[neuroimaging]] signal through spin-history effects, inflow artifacts, and systemic physiological fluctuations that co-vary with movement. These approaches also cannot address motion-related artifacts that are not linearly correlated with head position.

ICA-AROMA emerged from the recognition that motion artifacts often form spatially coherent patterns that are statistically distinguishable from neural [[functional-connectivity]] patterns. By decomposing the fMRI data into spatially independent components using [[ica]], the method can exploit the distinct temporal and spatial characteristics of motion artifacts versus neural signals. The approach was developed to provide a robust, fully automated alternative that could be easily integrated into existing preprocessing workflows, particularly those following [[bids]] (Brain Imaging Data Structure) conventions.

## Technical Approach

The ICA-AROMA algorithm proceeds in three stages. First, the fMRI data is decomposed into a set of spatial independent components using Melodic, the ICA implementation from the Fsl (FMRIB Software Library) package, or an equivalent ICA algorithm. Second, each component is classified as either neural or noise using a set of heuristic features that capture the temporal and spatial characteristics distinguishing motion artifacts from signal. These features include the maximum framewise displacement correlation (the degree to which a component's time course correlates with head motion parameters), the high-frequency content (noise components typically exhibit greater power at frequencies above 0.1 Hz), and spatial properties such as the extent of component overlap with [[white-matter]] or CSF regions versus cortical gray matter.

The classifier employs a threshold-based decision rule that was validated using a leave-N-out cross-validation approach applied to resting-state (100 participants) and task-based (118 participants) fMRI datasets [@10.1016/j.neuroimage.2015.02.064]. Components exceeding the noise threshold are classified as motion-related artifacts and are regressed out of the fMRI time series through [[linear]] regression, producing a denoised dataset that preserves the remaining components representing neural activity. Importantly, ICA-AROMA does not require any user-specified parameters—the threshold values are fixed based on validation studies, making the method fully automated and reproducible.

## Key Features

The primary advantage of ICA-AROMA is its data-driven nature: it identifies motion artifacts directly from the structure of each dataset rather than relying on generic assumptions or population-level thresholds. This makes it particularly effective for datasets with atypical motion profiles or when the standard motion parameters inadequately capture artifact structure. The method is computationally lightweight and can be run as a standalone tool or integrated into comprehensive preprocessing pipelines such as [[fmriprep]], which historically included ICA-AROMA as an optional denoising step (now available via the separate [[fmriprep]] package).

The approach has been validated against alternative denoising strategies including CompCor, temporal filtering with motion regression, and aggressive scrubbing, demonstrating comparable or better in preserving [[functional-connectivity]] metrics while reducing motion-related spurious correlations [@10.1016/j.neuroimage.2015.05.021]. Notably, ICA-AROMA preserves temporal degrees of freedom better than volume-censoring approaches like scrubbing, which can remove substantial portions of the fMRI time series in highly motion-contaminated data.

A limitation of ICA-AROMA is that it can occasionally misclassify slow neural fluctuations as motion artifacts (particularly very low-frequency oscillations in data with sustained head motion) or fail to capture certain types of structured noise that do not fit the classifier's assumptions (e.g., artifacts with atypical spatial distributions or frequency profiles). Users working with unusually motion-contaminated data or with specific hypotheses about very low-frequency [[connectivity]] should exercise caution and visually inspect the component classification results.

## Relationship to TVB

While ICA-AROMA is primarily a preprocessing tool for [[fmri]] data, it is relevant to [[whole-brain-modeling]] efforts in [[the-virtual-brain]] (TVB) because functional connectivity matrices extracted from denoised fMRI data are commonly used to constrain and validate large-scale brain network models. ICA-AROMA improves the quality of these empirically derived connectivity inputs by reducing motion artifacts that would otherwise introduce spurious edges or mask genuine correlations. In TVB pipelines that incorporate [[resting-state]] fMRI for personalization, preprocessing with ICA-AROMA can lead to more accurate structural-functional coupling and improved model fit to empirical data. The denoised BOLD time series produced by ICA-AROMA can be directly imported into TVB's data import workflows for subsequent connectivity analysis and simulation.

## Related Software

ICA-AROMA is available as a standalone Python package and is integrated into major fMRI preprocessing frameworks:

- [[fmriprep]] — post-fMRIPrep ICA-AROMA BIDS App (replaces the built-in workflow in fMRIPrep 23.0 and earlier)
- Fsl — ICA decomposition via MELODIC
- [[nilearn]] — includes utilities for ICA-AROMA classification
- [[bids-derivatives]] — ICA-AROMA outputs conform to BIDS specification for processed data

## Key Papers

- Pruim, R. H., Mennes, M., van Rooij, D., Llera, A., Buitelaar, J. K., & Beckmann, C. F. (2015). ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. NeuroImage, 112, 267-277. doi:10.1016/j.neuroimage.2015.02.064
- Pruim, R. H., Mennes, M., Buitelaar, J. K., & Beckmann, C. F. (2015). Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in [[resting-state-fmri]]. NeuroImage, 112, 278-287. doi:10.1016/j.neuroimage.2015.05.021

## References

1. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](](https://doi.org/10.3389/fnins.2025.1621244))
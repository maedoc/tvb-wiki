---
created: 2024-01-15
sources:
- raw/papers/doi-10-1002-hbm-460020402.md
- raw/papers/doi-10-3389-fninf-2014-00014.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/Renton2024.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- statistical-analysis
- python-tools
- nilearn
title: Nistats
type: entity
updated: '2026-05-04'
---

Nistats ([[neuroimaging]] STATistics) is a Python library designed for statistical analysis of neuroimaging data, with a primary focus on functional magnetic resonance imaging ([[fmri]]). Originally developed as part of the NiPy ecosystem, nistats provides tools for implementing General [[linear|Linear Model]] (GLM) analysis pipelines for both first-level (single-subject) and second-level (group-level) fMRI experiments. The library enables researchers to perform voxel-wise statistical tests, construct design matrices, run contrast analyses, and generate statistical parametric maps from [[bold-signal|BOLD]] (Blood-Oxygen-Level-Dependent) signal data in [[nifti]] format. [[nistats]]

## Motivation and Context

The field of neuroimaging, particularly fMRI analysis, demands rigorous statistical frameworks to detect activation patterns in the brain amid substantial noise. The General Linear Model has become the workhorse approach for analyzing fMRI time series, treating each voxel as a regressor against a designed experimental paradigm. The basic GLM formulation is expressed as:

**Y = Xβ + ε**

where **Y** is the observed BOLD time series (voxels × timepoints), **X** is the design matrix (timepoints × regressors), **β** represents the parameter estimates (regressors × voxels), and **ε** is the error term (assumed to follow a normal distribution with possible covariance structure). 

Before dedicated Python libraries emerged, researchers relied heavily on MATLAB-based toolboxes such as SPM (Statistical Parametric Mapping) or the C-based FSL (FMRIB Software Library) for these analyses. [[fmri]] Nistats was developed to bring similar capabilities to the Python ecosystem, leveraging the scientific Python stack (NumPy, SciPy, pandas) while maintaining compatibility with the broader neuroimaging data formats and tools in NiPy and later nilearn. The library addresses a gap in the Python neuroimaging landscape by providing a pure-Python implementation of GLM analysis that integrates seamlessly with data handling libraries like [[nibabel]] and preprocessing pipelines like [[fmriprep]] outputs.

## Key Features

The nistats library provides several core functionalities for fMRI analysis. First-level analysis tools allow researchers to fit GLM models to individual subject time series, specifying experimental design matrices that encode stimulus onsets, durations, and confounding covariates (such as head motion parameters). The library supports multiple regression approaches including ordinary least squares (OLS) and weighted least squares (WLS) to account for noise heterogeneity. [[nistats]] Once the model is fit, users can define contrasts (linear combinations of parameter estimates) to test specific hypotheses about brain activity differences between conditions. Second-level analysis extends these capabilities to group-level inference, enabling random effects analyses that generalize findings across subjects. Later versions integrated cluster-based multiple comparison correction through nilearn's permutation testing capabilities, allowing researchers to control family-wise error rate across the entire brain volume.  The library's API is designed around scikit-learn conventions, making it accessible to users familiar with machine learning workflows in Python.

## Relationship to TVB

While nistats is primarily a statistical analysis tool for fMRI data rather than a whole-brain modeling framework, it connects to [[the-virtual-brain]] workflows in several important ways. TVB researchers often use empirical fMRI data to validate their computational models by comparing simulated BOLD signals with observed functional connectivity patterns. Nistats can generate statistical parametric maps from preprocessing pipeline outputs (e.g., from [[fmriprep]] or [[c-pac]]) that serve as ground truth for TVB model fit assessment. Additionally, the library's second-level analysis capabilities enable group comparison studies that inform personalized parameter optimization in TVB, where individual differences in [[functional-connectivity]] patterns may guide model calibration. The statistical frameworks provided by nistats complement TVB's forward modeling capabilities, allowing researchers to move between data-driven activation detection and model-based simulation approaches.

## Related Software

Nistats shares conceptual and data-processing lineage with several other Python neuroimaging tools. It was notably integrated into [[nilearn-datasets]] as its statistical modeling module (as of nilearn 0.7.0), which now encompasses most of nistats' functionality within a more comprehensive machine learning framework for neuroimaging.  For fMRI preprocessing, nistats typically consumes outputs from [[fmriprep]] or [[c-pac]], both of which implement robust pipelines for motion correction, slice timing correction, and spatial normalization. Statistical results generated by nistats can be visualized using [[nilearn-datasets]] plotting functions or dedicated tools like  for comprehensive image visualization. Alternative statistical frameworks for neuroimaging include [[pymvpa]] (Multi-Voxel Pattern Analysis) and [[brainstat]], which offer complementary approaches to multivariate pattern analysis and population-level inference.

## Key Papers

- Friston, K. J., Holmes, A. P., Worsley, K. J., Poline, J. B., Frith, C. D., & Frackowiak, R. S. (1994). Statistical parametric maps in functional imaging: A general linear approach. *Human Brain Mapping*, 2(4), 189-210. 
- Smith, S. M., Jenkinson, M., Woolrich, M. W., Beckmann, C. F., Behrens, T. E., Johansen‑Berg, H., ... & Matthews, P. M. (2004). Advances in functional and structural MR image analysis and implementation as FSL. *Neuroimage*, 23, S208‑S219. 
- Abraham, A., Pedregosa, F., Eickenberg, M., Gervais, P., Mueller, A., Kossaifi, J., ... & Gramfort, A. (2014). Machine learning for neuroimaging with scikit‑learn. *Frontiers in Neuroinformatics*, 8, 14. 
- Gorgolewski, K., Esteban, O., Markiewicz, C. J., Ziegler, E., Gutierrez, D. P., Hutton, C., ... & Poldrack, R. (2018). fmriprep: A robust preprocessing pipeline for functional MRI. *Nature Methods*, 15(11), 875‑878. 

## References

1. (authors unknown). *Statistical parametric maps in functional imaging: A general linear approach*.
2. (authors unknown). *Machine learning for neuroimaging with scikit‑[[lean]]*.
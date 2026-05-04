---
created: 2025-01-15
sources:
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-7b51fe740684.md
- raw/papers/semanticscholar-109de470e443.md
tags:
- neuroimaging-fmri
- resting-state
- preprocessing
- software-cpac
- functional-connectivity
title: XCP-D
type: entity
updated: '2026-05-04'
---

XCP-D is a post-processing pipeline for [[resting-state]] functional magnetic resonance imaging ([[fmri]]) data, designed to remove confounding noise artifacts while preserving meaningful neural signals. Developed as part of the Configurable Pipeline for the Analysis of Connectomes (C-PAC) ecosystem, XCP-D takes preprocessed fMRI timeseries and applies a standardized sequence of confound regression, filtering, and quality control procedures to produce clean data suitable for subsequent [[functional-connectivity]] analyses. The pipeline emerged from the growing recognition that reliable estimation of brain [[connectivity]] patterns depends critically on aggressive yet principled removal of motion artifacts, physiological noise, and other non-neural signals that can systematically distort correlations between brain regions.

## Motivation and Context

The fundamental challenge in resting-state fMRI analysis lies in separating true [[brain-dynamics]] from the myriad sources of noise that contaminate the blood-oxygen-level-dependent ([[bold-signal|BOLD]]) signal. Head motion during scanning introduces spurious correlations that can falsely inflate estimates of [[functional-connectivity]], particularly in clinical populations where motion is often elevated (Power et al., 2012). Physiological artifacts arising from cardiac cycles and respiration further corrupt the signal, and scanner-related drift and instabilities add temporal biases. Early approaches to address these issues relied on ad hoc, lab-specific preprocessing sequences that limited [[reproducibility]] and made cross-study comparisons difficult. XCP-D was developed to provide a standardized, well-documented solution that balances aggressive noise removal with preservation of the neural signal, thereby enabling more reliable and reproducible connectivity analyses across diverse datasets.

The pipeline operates on the principle that a comprehensive confound regression model should account for both known and estimated noise sources. Unlike simpler approaches that regress only motion parameters, XCP-D incorporates multiple nuisance regressors including the global [[whole-brain]] signal, [[white-matter]] and cerebrospinal fluid signals, motion derivatives, and high-pass frequency filtering. This multi-component approach follows from empirical demonstrations that combined regression strategies outperform single-regressor methods in reducing motion-related artifacts while maintaining sensitivity to genuine functional networks (Ciric et al., 2017).

## Technical Approach

XCP-D employs a modular architecture that allows users to customize the confound regression strategy while maintaining a consistent output structure. The core processing [[steps]] include selection of nuisance regressors from a comprehensive menu, application of temporal filtering to isolate relevant frequency bands, and generation of quality control metrics to assess data quality post-processing.

The nuisance regression model in XCP-D follows the general form:

$$y(t) = \beta_0 + \sum_{i=1}^{n} \beta_i x_i(t) + \epsilon(t)$$

where $y(t)$ represents the raw BOLD timeseries at time point $t$, the $\beta_i$ coefficients are estimated via ordinary least squares regression, $x_i(t)$ represents the $i$-th confound regressor (motion parameters, global signal, tissue signals, etc.), and $r(t) = y(t) - \hat{y}(t)$ captures the residual timeseries retained for connectivity analysis. The pipeline offers several regression models of increasing complexity, ranging from basic [[linear]] regression to more sophisticated approaches that include polynomial regressors for drift removal and temporal derivatives for motion correction.

Temporal filtering represents another critical component of the XCP-D workflow. The pipeline typically applies high-pass filtering (e.g., a cutoff frequency of 0.01 Hz) to remove low-frequency drift while preserving the resting-state signal of interest, which predominantly resides in the 0.01–0.1 Hz band (Siegel et al., 2017). Optional low-pass filtering can further restrict the analysis to specific frequency ranges relevant to particular [[network-dynamics]], with common choices including a 0.08 Hz or 0.1 Hz low-pass cutoff to focus on slow oscillations typical of resting-state networks.

## Comparison to Alternative Post-Processing Strategies

XCP-D occupies a specific niche within the landscape of fMRI post-processing tools, complementing and sometimes competing with alternative approaches. Unlike [[ica-aroma]] (Independent Component Analysis - Automatic Removal of Motion Artifacts), which uses machine learning to classify and remove motion-related independent components, XCP-D employs a regression-based nuisance model that provides more explicit control over which confounds are regressed but requires a priori specification of the regressor set (Pruim et al., 2015). The fMRIPrep pipeline includes its own companion despiking and bandpass filtering steps, but XCP-D offers more comprehensive confound regression with support for a wider array of regression models including aCompCor (Behzadi et al., 2007) and hybrid approaches that combine multiple strategies (Ciric et al., 2017).

The [[conn]] toolbox represents another popular choice for connectivity-focused preprocessing, offering a graphical interface and extensive connectivity analysis capabilities beyond what XCP-D provides. However, CONN's preprocessing is often applied after initial volume-based preprocessing, whereas XCP-D is designed to operate directly on surface-timeseries outputs from C-PAC, making it particularly suited for cusp processing. For users already within the C-PAC ecosystem, XCP-D provides tighter integration and more streamlined workflows, while users preferring greater flexibility or graphical interfaces may find CONN more accessible.

## Key Features

One of XCP-D's distinguishing features is its integration with the broader C-PAC preprocessing ecosystem, allowing seamless application of confound regression following C-PAC's adaptive preprocessing pipeline. The pipeline generates comprehensive quality control outputs including framewise displacement plots, correlation matrices showing the effect of processing on motion-related artifacts, and standardized quality metrics that facilitate identification of problematic scans (Chen et al., 2019). Additionally, XCP-D supports multiple regression models (including aCompCor, Global Signal Regression, and hybrid approaches) giving researchers flexibility to choose the confound strategy best suited to their scientific questions.

The pipeline produces outputs in standard [[nifti]] format compatible with a wide range of connectivity analysis tools including [[nilearn]], [[cifti]], and custom scripts. Outputs include both the cleaned timeseries and the estimated confound parameters, enabling full reproducibility and transparency in preprocessing decisions. XCP-D also generates processed derivatives in the Brain Imaging Data Structure ([[bids]]) specification, facilitating data sharing and integration with other BIDS-compliant tools. Processed outputs include cleaned timeseries files, quality control reports in HTML format, and derivative summary statistics that can be used for cohort-level quality assessment.

## Relationship to TVB

While XCP-D is primarily designed for [[functional-connectivity]] analysis in the context of fMRI, its cleaned outputs can serve as inputs to [[whole-brain-modeling]] frameworks such as [[tvb]] (The Virtual Brain). The quality of preprocessing directly influences the fidelity of connectomes derived from fMRI data, which in turn affects parameter estimation and validation in large-scale brain network models. Researchers using [[tvb]] for personalized brain modeling often incorporate empirically derived functional connectivity matrices from preprocessed fMRI data, making pipelines like XCP-D valuable preprocessing steps for generating realistic model inputs. The relationship between XCP-D and [[tvb]] is thus indirect but important: XCP-D provides cleaned connectivity estimates that can inform whole-brain model construction. Particular attention should be given to ensuring that preprocessing parameters in XCP-D are appropriately matched to the temporal properties required for TVB simulations, as the filtering settings can affect the frequency content of the resulting connectivity matrices.

## Related Software

XCP-D operates within a broader ecosystem of fMRI preprocessing and connectivity analysis tools. Key related software includes [[c-pac]] (the parent pipeline suite from which XCP-D emerged), [[fmriprep]] (a widely used preprocessing pipeline offering different preprocessing approaches), [[nilearn]] (a Python library for connectivity analysis that can consume XCP-D outputs), and [[nipype]] (the workflow engine underlying C-PAC). Additional related tools for connectivity analysis include [[connectome-workbench]] for visualization of connectivity data, [[bctpy]] for graph-theoretic analysis of brain networks, and [[graphvar]] for graph-based network analysis.

## Key Papers

The XCP-D pipeline was introduced alongside the C-PAC software suite, with foundational documentation describing both the technical implementation and validation against established benchmarks for motion artifact removal (Ciric et al., 2017). This seminal work established a taxonomy of confound regression strategies and demonstrated the relative effectiveness of different approaches for motion artifact reduction while preserving neural signal sensitivity. Subsequent studies using XCP-D for preprocessing have demonstrated its utility in improving motion correction and enabling reliable connectivity estimates in clinical populations including individuals with [[alzheimers-disease]] and [[schizophrenia-models]] (Siegel et al., 2017; Chen et al., 2019). Additional foundational references include the work establishing framewise displacement as a quality metric (Power et al., 2012) and the development of aCompCor for physiological noise regression (Behzadi et al., 2007), both of which inform XCP-D's processing strategies.

## References

1. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
2. Sali Issa, Qi Wang, Ruinan Qi, Guangxi Peng, Shi Yin, Qinmu Peng. (2026). *An effective alzheimer disease diagnosis using resting state fmri images and broad learning system.*. Psychiatry research. Neuroimaging. [DOI](https://doi.org/10.1016/j.pscychresns.2025.112133)
3. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
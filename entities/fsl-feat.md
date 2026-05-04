---
created: 2025-01-15
sources:
- '[FSL FEAT Documentation](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT)'
- '[Woolrich et al. 2001 - FILM](https://doi.org/10.1006/nimg.2001.0976)'
- '[Woolrich et al. 2004 - FLAME](https://doi.org/10.1006/nimg.2004.01.018)'
- '[Jenkinson et al. 2012 - FSL Overview](https://doi.org/10.1006/nimg.2011.1016)'
- '[Smith et al. 2004 - FSL for Resting-State](https://doi.org/10.1016/j.neuroimage.2004.07.051)'
tags:
- software-fsl
- neuroimaging-fmri
- resting-state
- functional-connectivity
- hemodynamic-response-function
- neuroimaging-eeg
- neuroimaging-meg
title: FSL FEAT
type: entity
updated: '2026-05-04'
---

FSL FEAT ([[fmri]] Expert Analysis Tool) is the primary graphical user interface within the [[fsl]] (FMRIB Software Library) suite for performing statistical analysis of functional magnetic resonance imaging (fMRI) data. Developed at the Wellcome Centre for Human [[neuroimaging]] and later the University of Oxford's FMRIB (Functional Magnetic Resonance Imaging of the Brain) group, FEAT provides a streamlined yet comprehensive workflow for both first-level (single-subject) and higher-level (group) fMRI analysis. The tool implements the [[bold-signal]] modeling framework using the general [[linear|linear model]] (GLM), making it one of the most widely used fMRI analysis packages in the neuroimaging community [@FSLFEAT; @Jenkinson2012].

## Motivation and Context

The analysis of fMRI data presents substantial methodological challenges, including the need to model the delayed and sluggish [[hemodynamic-response-function]] (HRF), account for physiological noise artifacts, handle interscan and inter-subject variability, and perform appropriate statistical inference across the brain. Prior to FEAT's development in the late 1990s and early 2000s, fMRI analysis required substantial custom scripting and expertise in image processing. FEAT aimed to democratize robust fMRI analysis by encapsulating state-of-the-art statistical methods—including autocorrelation correction, voxelwise normality assessments, and mixed-effects group analysis—within an accessible graphical interface while also exposing all parameters for expert modification [@Woolrich2001].

FEAT emerged from the same Oxford group that developed [[fsl-melodic]] for independent component analysis (ICA) and benefited from tight integration with other FSL tools including BET for brain extraction, FLIRT for linear registration, and FNIRT for non-linear registration. While FEAT is best known for its task-based fMRI GLM analysis capabilities, it also contributed to the growth of [[resting-state]] functional [[connectivity]] research, particularly through its seed-based correlation tools and integration with [[melodic]] for ICA-based decompositions [@Smith2004]. The resting-state analysis capabilities in FSL are primarily associated with MELODIC/ICA and FSLnets, though FEAT's flexible framework enabled researchers to apply various connectivity methods.

## Technical Framework

FEAT operates on preprocessed fMRI time-series data, typically in [[nifti]] format, and models the blood-oxygen-level-dependent (BOLD) signal at each voxel using the GLM framework. The basic model assumes that the observed voxel time-series Y can be decomposed into a linear combination of predictor variables (design matrix) weighted by beta coefficients, plus residual error: Y = Xβ + ε. The design matrix typically contains task regressors convolved with a canonical HRF (or alternative basis functions such as double-gamma), motion parameters, and polynomial regressors for baseline drift removal.

A key methodological contribution of FEAT is its implementation of FILM (FMRIB's Improved Linear Model), which addresses the intrinsic autocorrelation present in fMRI noise through prewhitening. The autocorrelation is estimated from the data using a regression approach, and the whitening filter is applied before [[parameter-estimation]], leading to more efficient and unbiased statistical inferences [@Woolrich2001]. FEAT also offers temporal filtering (typically bandpass filtering between 0.01–0.1 Hz for [[resting-state]] analysis), spatial smoothing (typically Gaussian kernels of 4–8mm FWHM), and confound regression of motion parameters and global signal.

For group analysis, FEAT implements FLAME (FMRIB's Local Analysis of Mixed Effects), which distinguishes within-subject fixed effects from between-subject random effects using appropriate variance components. This mixed-effects approach provides valid inference across subjects while achieving greater statistical power than fixed-effects models [@Woolrich2004]. FLAME's implementation was particularly influential in establishing the superiority of mixed-effects models for neuroimaging group studies.

## Key Features and Capabilities

FEAT supports multiple analysis modalities including task-based fMRI (with flexible event-related or block design specifications), resting-state fMRI for [[functional-connectivity]] analyses, and dual-echo fMRI for improved artifact removal. The first-level analysis produces statistical parametric maps (SPMs) for user-defined contrasts of parameter estimates (COPEs), variance images (VARCEs), and z statistic maps. Thresholding options include voxelwise correction via Gaussian random field theory, clusterwise inference using the cluster-forming threshold, and false discovery rate (FDR) control.

Higher-level FEAT analysis enables mixed-effects aggregation across subjects for group comparisons, allowing for one-sample, two-sample, and paired t-tests as well as flexible covariates and factorial designs. Registration of fMRI data to standard spaces (MNI152) utilizes either linear FLIRT or non-linear FNIRT warping, with explicit optimization for functional-to-structural and structural-to-standard alignments. FLIRT uses a cost function (typically normalized correlation ratio or mutual information) optimized via iterative refinement, while FNIRT applies cubic B-spline basis functions for smooth warp fields that capture fine-grained anatomical variations. FEAT also integrates seamlessly with [[fsl-melodic]] for ICA-based denoising ([[ica-aroma]]) and [[fsl-randomise]] for non-parametric permutation testing. Outputs include quality control reports with temporal signal-to-noise ratios, motion statistics, and registration accuracy metrics that facilitate [[reproducibility]] and pipeline validation.

## Key Papers

- Woolrich, M.W., Jenkinson, M., Brady, J.M., & Smith, S.M. (2001). Fully Bayesian spatio-temporal modeling of FMRI data. *NeuroImage*, 13(6): S36. [@Woolrich2001]
- Woolrich, M.W., Behrens, T.E.J., Beckmann, C.F., Jenkinson, M., & Smith, S.M. (2004). Bayesian analysis of neuroimaging data in FSL. *NeuroImage*, 23(2): S56. [@Woolrich2004]
- Jenkinson, M., Beckmann, C.F., Behrens, T.E.J., Woolrich, M.W., & Smith, S.M. (2012). FSL. *NeuroImage*, 62(2): 782-790. [@Jenkinson2012]
- Smith, S.M., Fox, P.T., Miller, K.L., Glahn, D.C., Fox, P.M., Mackay, C.E., ... & Beckmann, C.F. (2009). Correspondence of the brain's functional architecture during activation and rest. *NeuroImage*, 47(2): S102. [@Smith2004]
- Beckmann, C.F., & Smith, S.M. (2004). Probabilistic ICA for fMRI. *IEEE Workshop on Statistical Signal Processing*, 473-476.

## Relationship to The Virtual Brain

In the context of [[whole-brain-modeling]] and [[computational-neuroscience]], FEAT plays a complementary role to simulation platforms like [[tvb]] (The Virtual Brain). While FEAT is primarily an analysis tool for empirical fMRI data, its outputs—particularly [[functional-connectivity]] matrices derived from [[resting-state]] seed correlations or ICA components—frequently serve as target data for model fitting and validation. The empirical connectivity patterns extracted via FEAT enable researchers to constrain whole-brain network models, estimate parameters of [[neural-mass-model]]s running on [[structural-connectivity]] scaffolds derived from diffusion imaging, and validate simulated BOLD signals against observed data.

FEAT-generated connectivity matrices have been used extensively in [[personalized-brain-modeling]] workflows where individual empirical data informs the configuration of large-scale models. The tool's standardized output formats and quality control metrics make it a preferred choice for preprocessing and analyzing fMRI data intended for downstream integration with [[the-virtual-brain]] or similar whole-brain simulation frameworks.

## Related Software

FEAT exists within a broader ecosystem of neuroimaging analysis tools. Alternative packages for fMRI analysis include [[spm]] (Statistical Parametric Mapping, developed at University College London), [[afni]] (Analysis of Functional NeuroImages, from the NIH), and Python-based frameworks such as [[nilearn]] and [[mne-connectivity]] that offer greater flexibility for custom pipelines. For connectivity-specific analyses, dedicated tools like [[connectome-workbench]] (for CIFTI format data), [[bctpy]] (Brain Connectivity Toolbox), and [[gretna]] provide more specialized implementations. The FSL suite continues to maintain FEAT, with ongoing development addressing modern statistical concerns including cross-species alignment, accelerated acquisitions, and integration with machine learning frameworks.
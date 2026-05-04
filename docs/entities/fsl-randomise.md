---
created: 2026-04-29
sources:
- raw/papers/semanticscholar-d6e43299345d.md
- raw/papers/semanticscholar-0aeca1b592e6.md
- raw/papers/semanticscholar-88be174971d9.md
tags:
- software-fsl
- neuroimaging-fmri
- diffusion-imaging
- resting-state
- statistical-inference
- permutation-tests
- threshold-free-cluster-enhancement
- multiple-comparisons-correction
- brain-parcellations
- connectivity
title: FSL Randomise
type: entity
updated: '2026-05-03'
---

# FSL Randomise

## Overview

FSL Randomise is a non-parametric permutation testing tool within the [FSL][fsl] (FMRIB Software Library) suite, designed for voxelwise and vertexwise statistical inference on [[neuroimaging]] data. Unlike parametric statistical methods that assume specific distributions (typically Gaussian), Randomise infers significance through empirical permutation of the data, making it particularly robust when the underlying distributional assumptions of standard parametric tests may be violated—a common scenario in [fmri] and [diffusion-imaging] analysis where sample sizes are often limited and noise characteristics are complex (Smith & Nichols, 2009). Randomise was developed primarily at FMRIB (Oxford Centre for Functional Magnetic Resonance Imaging of the Brain), now the Wellcome Centre for Integrative Neuroimaging (WIN), and has become a standard tool for group-level analysis in both [resting-state] and task-based [[fmri]] studies, as well as for diffusion tensor imaging (DTI) and [tractography]-based analyses (Smith et al., 2004).

## Key Features

### Non-Parametric Permutation Framework

Randomise implements a permutation testing framework that empirically estimates the null distribution of test statistics without relying on parametric assumptions. The tool randomly shuffles group labels or condition assignments across subjects (or uses other appropriate null models), recomputing the test statistic at each permutation to build an empirical null distribution. The observed test statistic is then compared against this empirical distribution to derive p-values. This approach is particularly valuable in [fmri] contexts where the number of voxels (potentially tens of thousands) far exceeds the number of subjects, and where the spatial autocorrelation structure of the data complicates parametric inference (Smith et al., 2004).

### Threshold-Free Cluster Enhancement

One of Randomise's most influential features is its implementation of **Threshold-Free Cluster Enhancement (TFCE)**, originally described by Smith and Nichols (2009). TFCE provides a way to detect spatially extended signal changes without requiring the user to specify an arbitrary cluster-forming threshold. Instead, TFCE integrates evidence across a range of thresholds, computing for each voxel a score that reflects both the voxel's statistical value and the extent of surrounding signal. This produces a more sensitive and less arbitrary inference than traditional cluster-based methods that require choosing a primary threshold (typically z > 2.3 or p < 0.001). TFCE has become standard practice in [connectomics] and [whole-brain] analysis pipelines (Smith & Nichols, 2009; Winkler et al., 2014).

### Multiple Comparisons Correction

Randomise provides rigorous correction for multiple comparisons through the permutation framework itself. Rather than applying post-hoc corrections like Bonferroni or false discovery rate (FDR) to p-values derived under parametric assumptions, the empirical null distribution implicitly accounts for the massive search space of voxelwise tests. This makes Randomise particularly suitable for analysis of [brain-parcellations] where parcel-wise statistics are computed, or for [[whole-brain]] exploratory analyses where spatial inference is complex (Winkler et al., 2014).

### Integration with FSL Infrastructure

Randomise integrates seamlessly with other FSL tools, accepting input in standard [[nifti]] format and using FSL's design matrix setup (via FeatGUI or command-line specifications). It works with FEAT-produced statistical maps, as well as with outputs from other [neuroimaging] preprocessing pipelines like [fmriprep] or [freesurfer]. The tool supports various experimental designs including two-group comparisons, paired designs, and multiple regression covariates.

## Relationship to TVB

FSL Randomise operates upstream in the neuroimaging analysis pipeline relative to [the-virtual-brain]. While TVB is a [whole-brain] modeling simulator that uses empirical neuroimaging data to construct computational models of [[brain-dynamics]], Randomise is an analysis tool used to identify statistically significant differences in empirical data—whether between patient groups and controls, between conditions in task-based studies, or in correlation with behavioral measures. The statistical maps produced by Randomise (e.g., group difference maps, correlation maps) can inform the construction of [personalized-brain-modeling] by identifying regions or networks that show significant effects and thus merit particular attention in model parameterization. In studies combining [neural-mass-models] with empirical neuroimaging, Randomise may be used to determine which brain regions show significant differences that the model should capture.

Randomise also connects to TVB through [structural-connectivity] and [functional-connectivity] analyses. DTI/[[tractography]] pipelines often use Randomise for tract-based spatial statistics (TBSS) to identify [[white-matter]] differences between groups, while [[resting-state]] [functional-connectivity] analyses may use Randomise to identify group differences in [[connectivity]] matrices derived from [brain-connectivity-toolbox] or similar packages.

## Key Papers

The foundational paper for Randomise is Smith et al. (2004), "Advances in functional and structural MR image analysis and implementation as FSL." This paper established the tool in the context of the broader FSL suite. The TFCE method, which significantly enhanced Randomise's capabilities, was introduced in Smith and Nichols (2009), "Threshold-free cluster enhancement: avoiding problems with cluster-size inference." More recent methodological extensions appear in Winkler et al. (2014), "Non-parametric inference of subtle group differences using TFCE," which extends the framework to more complex contrasts.

## Related Software

| Tool | Purpose | Relationship |
|------|---------|--------------|
| [FSL][fsl] | Neuroimaging analysis suite | Parent software containing Randomise |
| FSL FEAT | fMRI analysis | Produces statistical maps analyzed by Randomise |
| FSL TBSS | Tract-based spatial statistics | Uses Randomise for group comparisons on DTI data |
| [afni] | Neuroimaging analysis | Alternative statistical inference tools (3dttest++, 3dMEMA) |
| [spm] | Statistical Parametric Mapping | Parametric alternative to Randomise |
| [freesurfer] | Surface-based analysis | Alternative source for statistical maps |
| [nilearn] | Python neuroimaging | Provides Python wrappers for permutation testing |

## References

Smith, S. M., Jenkinson, M., Woolrich, M. W., Beckmann, C. F., Behrens, T. E. J., Johansen-Berg, H., Bannister, P. R., De Luca, M., Drobnjak, I., Flitney, D. E., Niazy, R. K., Saunders, J., Vickers, J. J., Zhang, Y., De Stefano, N., Brady, J. M., & Matthews, P. M. (2004). Advances in functional and structural MR image analysis and implementation as FSL. *NeuroImage*, 23(S1), 208-219. https://doi.org/10.1016/j.neuroimage.2004.07.051

Smith, S. M., & Nichols, T. E. (2009). Threshold-free cluster enhancement: Avoiding problems with cluster-size inference. *NeuroImage*, 47(2), 454-464. https://doi.org/10.1016/j.neuroimage.2009.04.065

Winkler, A. M., Ridgway, G. R., Webster, M. A., Smith, S. M., & Nichols, T. E. (2014). Non-parametric inference of subtle group differences using TFCE. *NeuroImage*, 95, 414-426. https://doi.org/10.1016/j.neuroimage.2014.06.007

[fsl]: fsl.md
[the-virtual-brain]: [[the-virtual-brain]].md
[whole-brain]: whole-brain.md
[personalized-brain-modeling]: [[personalized-brain-modeling]].md
[neural-mass-models]: [[neural-mass-model]].md
[structural-connectivity]: [[structural-connectivity]].md
[functional-connectivity]: [[functional-connectivity]].md
[brain-connectivity-toolbox]: [[brain-connectivity-toolbox]].md
[afni]: [[afni]].md
[spm]: spm.md
[freesurfer]: [[freesurfer]].md
[nilearn]: [[nilearn]].md
[fmri]: fmri.md
[diffusion-imaging]: [[diffusion-imaging]].md
[resting-state]: resting-state.md
[tractography]: tractography.md
[connectomics]: [[connectomics]].md
[brain-parcellations]: [[brain-parcellations]].md
[neuroimaging]: neuroimaging.md
[fmriprep]: [[fmriprep]].md
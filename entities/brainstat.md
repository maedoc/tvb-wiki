---
created: 2026-04-29
sources: []
tags:
- software-brain-modeling
title: BrainStat
type: entity
updated: 2026-05-03
---
title: BrainStat
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-visualization, neuroimaging, resting-state, functional-connectivity, structural-connectivity]
sources: [10.1016/j.neuroimage.2021.118337, 10.1016/j.neuroimage.2016.05.024, 10.1002/hbm.23798]
---

# BrainStat

## Overview

**BrainStat** is a Python toolbox designed for statistical analysis of brain imaging data, with a particular emphasis on connectivity-based analyses in whole-brain modeling contexts. The toolbox provides a unified interface for performing mass-univariate and multivariate statistical tests on neuroimaging datasets, including cortical thickness, functional connectivity matrices, and graph-theoretic metrics derived from structural and functional connectomes. BrainStat integrates tightly with established Python neuroimaging libraries such as [[nilearn]] and supports data formats common in the [[human-connectome-project]] and similar large-scale neuroimaging initiatives.

The software addresses a critical gap in the neuroimaging analysis ecosystem: while tools like [[spm]], [[fsl]], and [[fieldtrip]] excel at preprocessing and first-level analysis, and libraries like the **Brain Connectivity Toolbox** (BCT, also known as [bctpy](https://github.com/aestivabrainconn/bctpy)) provide sophisticated network metrics, there existed no dedicated Python toolbox bridging the gap between raw connectivity estimates and group-level statistical inference. BrainStat fills this role by offering robust statistical primitives specifically optimized for high-dimensional brain data, as documented in the primary BrainStat publication (Larivière et al., 2021)[^1].

## Motivations and Context

The proliferation of large-scale neuroimaging datasets such as the [[hcp-dataset]] (Human Connectome Project)[^2], [[uk-biobank]], and the [[connectomedb]] has fundamentally transformed computational neuroscience. Researchers now routinely acquire [[resting-state]] [[functional-connectivity]] data from thousands of participants, enabling population-level inference about brain organization. However, this increased scale introduces statistical challenges that traditional approaches fail to handle adequately.

Brain connectivity matrices are inherently high-dimensional—modern parcellations like the [[schaefer-atlas]] or [[glasser-atlas]] yield connectivity matrices with thousands of edges—and standard statistical corrections for multiple comparisons are essential to control false discovery rates. Simple parametric approaches assuming independent samples are inappropriate because connectivity edges exhibit complex dependence structures arising from the network topology itself. BrainStat addresses these challenges by implementing permutation-based inference (Nichols & Holmes, 2001)[^3], cluster-mass statistics, and false discovery rate corrections specifically adapted to the dependence structure of brain networks.

The toolbox emerged from the recognition that whole-brain modeling workflows require not only forward simulation of brain dynamics (as provided by [[the-virtual-brain]]) but also rigorous statistical frameworks for comparing model outputs against empirical data and for characterizing group differences in brain organization across clinical populations.

## Key Features

BrainStat provides several interconnected modules for brain data analysis. The **contrast library** implements standard general linear model (GLM) formulations for comparing brain metrics across groups, supporting both continuous and categorical predictors with arbitrary confound regression. The implementation handles the peculiar noise characteristics of neuroimaging data, including heteroscedasticity and spatial autocorrelation.

The **stats** module offers advanced inference procedures including permutation testing with exact family-wise error rate control, bootstrap confidence intervals for connectivity metrics, and Bayesian alternatives to classical hypothesis testing via Bayes factors. These methods are essential when analyzing [[brain-network]] metrics where the assumption of normality frequently fails (Chen et al., 2019)[^4].

For [[graph-theory]] based analyses, BrainStat provides streamlined workflows for computing network properties (including modularity, [[rich-club]] coefficients, and [[small-world-networks]] metrics) followed by group-level comparison. The toolbox normalizes these metrics against appropriate null models generated via graph matching or random rewiring procedures.

BrainStat also implements tools for **multivariate pattern analysis** (MVPA), enabling identification of distributed brain features that discriminate between groups—a capability directly relevant to personalized brain modeling applications where one seeks biomarkers predictive of clinical outcomes.

## Relationship to TVB

While BrainStat is not part of [[the-virtual-brain]] core simulation infrastructure, it plays a complementary role in whole-brain modeling workflows. TVB researchers frequently employ BrainStat for post-hoc statistical analysis of simulated [[functional-connectivity]] patterns, comparing model-derived connectivity against empirical datasets from the [[hcp-dataset]] or clinical cohorts. The combination enables rigorous assessment of whether whole-brain models accurately capture population-level differences in brain network organization, and whether the statistical differences observed between groups in empirical data can be reproduced in silico.

In epilepsy modeling contexts, BrainStat serves as the statistical back-end for comparing [[epileptor]]-derived connectivity changes against patient data, supporting the model validation framework essential for clinical translation of personalized brain models. The toolbox's ability to handle [[structural-connectivity]] derived from [[diffusion-imaging]] (via [[freesurfer]] or [[mrtrix]] preprocessing) makes it particularly valuable for TVB workflows that begin with empirical DTI tractography. BrainStat's statistical inference procedures help determine whether modeled seizure dynamics produce connectivity patterns that significantly differ from healthy controls in ways that align with clinical observations.

## Related Software

BrainStat exists within a broader ecosystem of neuroimaging analysis tools. It extends the statistical capabilities of [[nilearn]] (which focuses primarily on mass-univariate GLM analysis) by providing specialized procedures for connectivity data. Unlike the **Brain Connectivity Toolbox** (BCT/bctpy), which computes network metrics, BrainStat focuses on their statistical inference—making the two tools highly complementary. The BCT software was developed by Rubinov and Sporns (2010)[^5] and remains the standard for graph-theoretic network analysis in neuroimaging.

For researchers beginning with [[bids]]-formatted data, BrainStat integrates with the [[pybids]] ecosystem for automated data discovery. Comparison with commercial packages like [[brainvoyager]] reveals BrainStat's strengths in open-source flexibility and scriptability, though it lacks the graphical user interface favored by some clinical researchers.

Related tools in this ecosystem include:
- [[the-virtual-brain]] — whole-brain simulation platform
- [[fmriprep]] — fMRI preprocessing pipeline
- [[nilearn]] — Python library for neuroimage GLM analysis
- [[fieldtrip]] — MATLAB toolbox for MEG/EEG analysis
- [[spm]] — Statistical Parametric Mapping software

## Key Technical Considerations

Users should note that BrainStat assumes preprocessed neuroimaging data—raw image reconstruction and motion correction should first be performed using [[fmriprep]] (for fMRI) or appropriate diffusion preprocessing pipelines. The toolbox operates on derived features (connectivity matrices, cortical thickness maps, region-wise time series) rather than raw imaging data.

Performance considerations arise when analyzing dense connectivity matrices: the permutation-based inference procedures, while statistically robust, involve substantial computational overhead. For very large datasets, users may wish to leverage [[nipype]] parallelization wrappers or compute clusters.

## Key Papers

[^1]: Larivière, S., Bayrak, Ş., Vasung, L., et al. (2021). BrainStat: A toolbox for brain-wide statistics and multi-model descriptions. *Neuroimage*, 245, 118337. https://doi.org/10.1016/j.neuroimage.2021.118337

[^2]: Van Essen, D.C., Smith, S.M., Barch, D.M., et al. (2013). The WU-Minn Human Connectome Project: An overview. *Neuroimage*, 80, 62-79. https://doi.org/10.1016/j.neuroimage.2013.05.041

[^3]: Nichols, T.E., & Holmes, A.P. (2001). Nonparametric permutation tests for functional neuroimaging: A primer with examples. *Human Brain Mapping*, 15(1), 1-25. https://doi.org/10.1002/hbm.1058

[^4]: Chen, B., Xu, Y., & Zhou, Y. (2019). Statistical methods for brain connectivity research. *Human Brain Mapping*, 40(7), 2031-2050. https://doi.org/10.1002/hbm.23798

[^5]: Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: Uses and interpretations. *Neuroimage*, 52(3), 1059-1069. https://doi.org/10.1016/j.neuroimage.2009.10.003

## References

- Bayrak, Ş., Larivière, S., Liu, S., et al. (2023). BrainStat: Brain-wide statistical analysis toolbox for R and Python. *Frontiers in Neuroinformatics*, 17, 1059884.
- Glasser, M.F., Coalson, T.S., Robinson, E.C., et al. (2016). A multi-modal parcellation of human cerebral cortex. *Nature*, 536, 171-178.
- Schaefer, A., Kong, R., Gordon, E.M., et al. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28(9), 3095-3114.
- The Virtual Brain Project. (2024). TVB Documentation. https://www.thevirtualbrain.org/
---
created: 2024-01-15
sources:
- Worsley et al.
- 2009a
- Worsley et al.
- 2009b
- Charil et al.
- 2007
- Goldstein et al.
- 2017
- raw/papers/arxiv-2602.03240.md
- raw/papers/newman-2010.md
- raw/papers/glean-github.md
tags:
- software-visualization
- neuroimaging
- freesurfer
- surface-based-analysis
- statistical-analysis
- matlab
- brain-parcellations
- cortical-thickness
title: SurfStat
type: entity
updated: '2026-05-01'
---

# SurfStat

## Overview

SurfStat is a MATLAB toolbox designed for surface-based statistical analysis of [[neuroimaging]] data, particularly cortical surface measurements derived from tools like [[freesurfer]] and [[brainvisa]]. Developed primarily by the Montreal Neurological Institute and associated research groups (Worsley et al., 2009a), SurfStat provides a comprehensive set of statistical routines specifically optimized for analyzing data that resides on the cortical surface manifold rather than in volumetric image space. The toolbox enables researchers to perform vertex-wise statistical tests, cluster-based corrections for multiple comparisons, and region-of-interest analyses across the cortical sheet, making it an essential tool for studies of cortical thickness, surface area, and curvature measurements (Worsley et al., 2009b).

## Key Features

The primary advantage of SurfStat lies in its ability to handle the unique statistical challenges posed by surface-based neuroimaging data. Unlike volumetric data that can be analyzed with standard statistical packages, surface data requires specialized approaches because adjacent vertices on the cortical mesh are not independent observations—they are connected through a complex topological structure. SurfStat addresses this through implementations of random field theory (RFT) corrections specifically adapted for cortical surfaces, providing rigorous control over family-wise error rates in mass univariate analyses (Charil et al., 2007).

The toolbox includes implementations of general [[linear]] models (GLM) at the vertex level, supporting both simple t-tests and complex factorial designs with covariates. Users can model continuous variables, categorical predictors, and interactions exactly as they would in volumetric analysis packages like [[spm]] or [[fsl]], but with the appropriate spatial autocorrelation corrections for surface data. SurfStat also provides tools for resampling statistics, including permutation tests, which serve as non-parametric alternatives for inference when the distributional assumptions of random field theory may not hold (Goldstein et al., 2017).

Beyond vertex-wise analysis, SurfStat facilitates region-of-interest (ROI) based statistics through integration with cortical parcellation schemes such as the [[desikan-killiany-atlas]], [[destrieux-atlas]], and [[glasser-atlas]]. Users can extract summary statistics from predefined cortical regions and perform between-group comparisons, making it straightforward to conduct studies examining regional cortical differences in [[alzheimers-disease]], [[schizophrenia-models]], or [[aging-brain]].

## Relationship to TVB

While SurfStat is not directly part of The Virtual Brain ([[tvb]] and [[the-virtual-brain]]) ecosystem, it plays a complementary role in the broader whole-brain modeling workflow. In personalized brain modeling pipelines, researchers often derive empirical parameters for [[whole-brain-modeling]] by fitting theoretical models to empirical functional and structural connectivity data. SurfStat provides the statistical framework for comparing cortical measures between patient populations and healthy controls, which may inform the selection of appropriate [[personalized-brain-modeling]] parameters.

The toolbox is particularly valuable for [[epilepsy-modeling]] studies that require analysis of cortical thickness abnormalities or for investigations of [[brain-stimulation]] effects on cortical structure. While SurfStat can be used alongside tools like [[tvb]] for preprocessing, it functions as an independent analysis tool—its surface-based approach shares conceptual foundations with the neural field theory underlying TVB's [[jansen-rit-model]] and similar [[neural-mass-models]], which model brain dynamics on continuous manifolds, though SurfStat itself does not implement these models.

## Key Papers

SurfStat was introduced by Keith J. Worsley and colleagues at the Montreal Neurological Institute, building on their earlier work on random field theory for neuroimaging. The foundational paper describing the statistical framework for surface-based analysis (Worsley et al., 2009a) established the theoretical basis for the toolbox. A companion technical report (Worsley et al., 2009b) provides detailed implementation guidance. Subsequent methodological papers have extended SurfStat's capabilities for dual regression analysis of [[functional-connectivity]] patterns and for mixed-effects models in multicenter studies (Charil et al., 2007; Goldstein et al., 2017).

## Related Software

SurfStat integrates closely with the broader neuroimaging software ecosystem. It works seamlessly with outputs from [[freesurfer]] for cortical reconstruction, with [[brainvisa]] for alternative processing pipelines, and with visualization tools like [[freeview]] for displaying statistical results. For volumetric statistical analysis, researchers often complement SurfStat with [[spm]] or [[fsl-randomise]], while connectivity-based analyses may utilize the [[brain-connectivity-toolbox]] ([[bctpy]]) or [[nilearn]]. The toolbox is written in MATLAB, making it compatible with other MATLAB-based analysis pipelines including those in the [[eeglab]] ecosystem for combined EEG-fMRI analyses.

## References

Charil, A., Zijdenbos, A. P., Taylor, J., Boelman, G., Worsley, K. J., Müller-Gärtner, H. W., &Evans, A. (2007). Statistical analysis of activation maps: Characterisation and correction of the bias caused by anisotropy. In T. D. R. S. R. (Ed.), *Statistical Parametric Mapping: The Analysis of Functional Brain Images* (pp. 198-214). Academic Press.

Goldstein, J. M., Zajac, L., Cosgrove, J., Madsen, K., Ge, Y., & Sehat, M. (2017). The impact of surface-based cortical thickness measurement on understanding brain development: methods and applications. *Developmental Cognitive Neuroscience*, 27, 85-98.

Worsley, K. J., Charil, A., Leritz, J., & Zijdenbos, A. (2009a). Statistical analysis of activation maps. In *Statistical Parametric Mapping: The Analysis of Functional Brain Images* (pp. 218-232). Elsevier.

Worsley, K. J., Charil, A., & Leritz, J. (2009b). SurfStat: A Matlab toolbox for the statistical analysis of univariate and multivariate surface data. *NeuroImage*, 45(2), S172-S178.
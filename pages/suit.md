---
title: SUIT - Spatially Unbiased Infratentorial Template
created: 2025-01-15
updated: 2026-05-02
type: entity
tags: [neuroimaging-fmri, neuroimaging-dti, software-visualization, brain-parcellations]
sources:
  - Diedrichsen, J. (2006). A spatially unbiased atlas template of the human cerebellum. Neuroimage, 33(1), 127-138.
  - Diedrichsen, J., Balsters, J. H., Flavell, J., Cussans, E., & Ramnani, N. (2009). A probabilistic atlas of the human cerebellum. Neuroimage, 46(1), 39-46.
  - Diedrichsen, J., Maderwald, S., Kuper, M., Thurling, M., Rabe, K., Gizewski, E. R., et al. (2011). Imaging the deep cerebellar nuclei: A probabilistic atlas and normalization procedure. Neuroimage, 54(3), 1786-1794.
  - Diedrichsen, J., & Ziadow, E. (2015). Surface-based display of volume-averaged cerebellar data. PLOS ONE, 10(7), e0133402.
  - King, M., Hernandez-Castillo, C. R., Poldrack, R. R., Ivry, R., & Diedrichsen, J. (2019). Functional boundaries in the human cerebellum revealed by a multi-domain task battery. Nature Neuroscience, 22(10), 1451-1458.
  - Buckner, R. L., Krienen, F. M., Castellanos, A., Thomas, Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. Journal of Neurophysiology, 106(5), 2322-2345.
---

## Overview

SUIT (Spatially Unbiased Infratentorial Template) is a specialized MATLAB toolbox dedicated to the analysis of neuroimaging data from the human [[cerebellum]] and brainstem. Developed by Jörn Diedrichsen and colleagues at University College London, SUIT provides a high-resolution anatomical atlas template of the [[cerebellum]] derived from 20 young healthy individuals (Diedrichsen, 2006), enabling researchers to isolate, normalize, and visualize cerebellar structures with significantly greater precision than standard whole-brain neuroimaging pipelines. The toolbox addresses a critical limitation in conventional neuroimaging: the widely used ICBM152 [[MNI space|MNI template]] provides very poor contrast for cerebellar structures, leading to substantial spatial misalignment when normalizing cerebellar data using standard whole-brain methods (Diedrichsen, 2006).

## Motivation and Context

The [[cerebellum]] has historically been underrepresented in functional neuroimaging studies, partly due to the technical challenges associated with its complex folial architecture and its position beneath the cerebral cortex (Diedrichsen, 2006). Standard normalization to [[MNI space]] results in an average spatial uncertainty of approximately 4 mm between identical fissures in different individuals (Diedrichsen, 2006)—a level of imprecision that obscures the detailed functional organization of the cerebellum. SUIT was developed to address this problem by providing a spatially unbiased, [[cerebellum]]-specific atlas that preserves anatomical detail while maintaining compatibility with [[MNI space]] coordinates (Diedrichsen, 2006). This specialized approach is particularly important given the cerebellum's established roles in motor coordination, cognitive processing, and emotional regulation (King et al., 2019), all of which require precise spatial localization to investigate properly.

## Technical Content

The SUIT toolbox implements a complete cerebellar analysis pipeline that differs fundamentally from whole-brain approaches (Diedrichsen, 2006). The isolation step automatically separates cerebellar structures from the cerebral cortex using an anatomical image, enabling targeted analysis of cerebellar data without contamination from cortical signals (Diedrichsen, 2006). The normalization procedure employs a cerebellum-specific nonlinear registration algorithm distinct from whole-brain [[SPM]] pipelines, achieving substantially better intersubject alignment than affine or standard nonlinear normalization to [[MNI space]] (Diedrichsen et al., 2009). Quantitative comparisons demonstrate that SUIT normalization dramatically improves the overlap of primary and intra-biventer fissures across individuals (Diedrichsen, 2006).

The atlas template itself is spatially unbiased with respect to affine alignment to [[MNI space]], meaning that when the same brain is normalized to both [[MNI space|MNI]] and SUIT templates, identical structures end up at approximately the same average coordinates (Diedrichsen, 2006). However, individual differences between normalizations can be as large as 1 cm, with an average difference of approximately 5 mm across the image (Diedrichsen, 2006)—hence the importance of using consistent normalization methods for both data and atlas.

### Probabilistic Atlas

The SUIT package includes probabilistic atlases for both cerebellar lobules and deep cerebellar nuclei (Diedrichsen et al., 2009). The lobule atlas defines 28 regions based on manual identification in 20 participants (Diedrichsen et al., 2009)—this count includes 10 lobules in each cerebellar hemisphere (20 regions) plus 8 vermal lobules, following the anatomical division scheme of Larsell (Diedrichsen et al., 2009). The deep nuclei atlas (developed using ultra-high-field MRI at 7 Tesla) defines 6 nuclei regions: the fastigial, globose, emboliform, dentate, ventral posterior, and posterior nuclei (Diedrichsen et al., 2011). These probabilistic atlases enable researchers to assign cerebellar voxels to anatomically meaningful regions, facilitating region-of-interest analyses and connectivity studies (Diedrichsen et al., 2009).

### Surface-Based Display

A distinctive feature of SUIT is its surface-based flatmap representation of cerebellar data, introduced by Diedrichsen and Ziadow (2015). This approach projects volume-averaged cerebellar activation onto a two-dimensional flatmap that preserves topological relationships while unfolding the complex three-dimensional folial structure (Diedrichsen & Ziadow, 2015). The flatmap provides an intuitive way to visualize and communicate cerebellar activation patterns, complementing traditional volume-based visualizations (Diedrichsen & Ziadow, 2015). This representation can be compared with alternative cerebellar surface representations, such as the functional parcellation scheme introduced by Buckner et al. (2011).

### SUITPy: Python Implementation

The SUIT toolbox has been partially ported to Python under the name SUITPy, which provides basic functionality for flatmap display and cerebellar data mapping without requiring MATLAB (Diedrichsen & Ziadow, 2015). SUITPy enables Python-based workflows using libraries like nilearn to work with SUIT outputs, expanding accessibility for researchers who prefer Python-based neuroimaging pipelines.

## Key Features

The SUIT toolbox provides several integrated capabilities essential for cerebellar neuroimaging research (Diedrichsen, 2006; Diedrichsen et al., 2009; Diedrichsen & Ziadow, 2015). Automated cerebellar isolation removes cerebral cortex from the analysis, ensuring that only cerebellar signals are considered (Diedrichsen, 2006). The specialized cerebellum-specific normalization achieves more accurate anatomical alignment than whole-brain methods for infratentorial structures (Diedrichsen, 2006). Surface-based flatmap visualization enables intuitive display of cerebellar activation patterns (Diedrichsen & Ziadow, 2015). Probabilistic atlases of both lobular and nuclear anatomy allow region-of-interest definition (Diedrichsen et al., 2009; Diedrichsen et al., 2011). The toolbox also supports voxel-based morphometry (VBM) for studying cerebellar volume changes in disease populations and lesion-symptom mapping for neurological patients (Diedrichsen, 2006).

## Relationship to TVB

SUIT is relevant to [[whole-brain-modeling]] efforts such as [[the-virtual-brain]] (TVB) because cerebellar connectivity and function are increasingly incorporated into large-scale brain network models (King et al., 2019). The cerebellum contains approximately 70% of the brain's neurons despite representing only 10% of brain volume (Buckner et al., 2011), and its computational properties are essential for understanding predictive processing and motor learning in whole-brain frameworks (King et al., 2019). TVB's connectome-based modeling approach can benefit from SUIT's precise cerebellar parcellation when defining cerebellar nodes and their white-matter pathways derived from [[diffusion-imaging]] data (Diedrichsen et al., 2009). Moreover, SUIT's normalization procedures improve the alignment of cerebellar structural connectivity data derived from [[tractography]], which feeds directly into whole-brain connectome construction (Diedrichsen et al., 2011).

## Relationship to Other Tools

SUIT occupies a specialized niche among neuroimaging toolboxes, complementing rather than replacing established packages like [[SPM]], [[FSL]], and [[FreeSurfer]] (Diedrichsen, 2006). Unlike these whole-brain toolboxes, SUIT focuses exclusively on cerebellar analysis and provides cerebellum-specific templates and normalization algorithms (Diedrichsen, 2006). SUIT can be used in conjunction with [[SPM]] for preprocessing, as the toolbox is built on the [[SPM]] framework and requires a compatible version of [[SPM]] to function (Diedrichsen, 2006). For surface-based visualization, SUIT provides functionality similar to [[FreeSurfer]] but specifically adapted for cerebellar anatomy (Diedrichsen & Ziadow, 2015). The cerebellar atlases provided by SUIT can be compared with other parcellation schemes like the [[Schaefer atlas]] (cortical) or [[Brainnetome Atlas]] in terms of their organizational principles (Diedrichsen et al., 2009).

## Limitations

Several limitations should be considered when using SUIT for cerebellar analysis (Diedrichsen, 2006). First, SUIT is cerebellum-specific and does not provide templates or normalization procedures for the cerebral cortex—researchers must use complementary tools like [[SPM]], [[FSL]], or [[FreeSurfer]] for whole-brain analyses (Diedrichsen, 2006). Second, SUIT is MATLAB-dependent, requiring a MATLAB installation and license to run the full toolbox (Diedrichsen, 2006); while SUITPy provides basic functionality, it does not replicate all features of the MATLAB implementation (Diedrichsen & Ziadow, 2015). Third, the template was developed from 20 young healthy individuals, which may not fully represent cerebellar anatomy across the lifespan or in clinical populations (Diedrichsen, 2006). Fourth, while SUIT provides excellent alignment for cerebellar structures, it is optimized for infratentorial regions and does not address brainstem structures beyond the cerebellum itself (Diedrichsen et al., 2011). Finally, users should be aware that the SUIT flatmap representation is topologically constrained and may not capture all aspects of three-dimensional cerebellar organization, particularly for deep nuclei (Diedrichsen & Ziadow, 2015).

## Key Papers

- Diedrichsen, J. (2006). A spatially unbiased atlas template of the human cerebellum. *Neuroimage*, 33(1), 127-138. — The original SUIT paper introducing the template and normalization approach.

- Diedrichsen, J., Balsters, J. H., Flavell, J., Cussans, E., & Ramnani, N. (2009). A probabilistic atlas of the human cerebellum. *Neuroimage*, 46(1), 39-46. — Probabilistic atlas of cerebellar lobules and nuclei.

- Diedrichsen, J., Maderwald, S., Kuper, M., Thurling, M., Rabe, K., Gizewski, E. R., et al. (2011). Imaging the deep cerebellar nuclei: A probabilistic atlas and normalization procedure. *Neuroimage*, 54(3), 1786-1794. — Ultra-high-field atlas of deep cerebellar nuclei.

- Diedrichsen, J., & Ziadow, E. (2015). Surface-based display of volume-averaged cerebellar data. *PLOS ONE*, 10(7), e0133402. — Introduction of the cerebellar flatmap visualization.

- King, M., Hernandez-Castillo, C. R., Poldrack, R. R., Ivry, R., & Diedrichsen, J. (2019). Functional boundaries in the human cerebellum revealed by a multi-domain task battery. *Nature Neuroscience*, 22(10), 1451-1458. — Functional parcellation of the cerebellum based on extensive task data.

- Buckner, R. L., Krienen, F. M., Castellanos, A., Thomas, Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. *Journal of Neurophysiology*, 106(5), 2322-2345. — Functional parcellation of the cerebellum.

## External Resources

The official SUIT toolbox and documentation can be accessed at the [Diedrichsen Lab GitHub repository](https://github.com/DiedrichsenLab/SUIT). The toolbox is freely available and includes the specialized cerebellar template, probabilistic atlases, and analysis functions. Documentation provides detailed instructions for cerebellar isolation, normalization, and flatmap visualization workflows.

## Related Software

- [[SPM]] — Statistical Parameter Mapping, the software framework on which SUIT is built
- [[FreeSurfer]] — FreeSurfer provides cortical surface reconstruction that can complement SUIT's cerebellar analysis
- [[FSL]] — FMRIB Software Library includes alternative neuroimaging processing tools
- [[nilearn]] — Python library for neuroimaging that can work with SUIT outputs
- [[BrainVoyager]] — Another neuroimaging package with surface-based rendering capabilities

## See Also

- [[brain-parcellations]] — The process of dividing brain regions into discrete units
- [[resting-state]] — Functional connectivity approach that can be applied to cerebellar data
- [[diffusion-imaging]] — Technique for mapping white-matter connectivity to the cerebellum
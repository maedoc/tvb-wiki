---
created: 2026-04-24
sources:
- https://doi.org/10.1117/1.JMI.1.2.024003
- https://doi.org/10.1016/j.cmpb.2009.09.002
- https://doi.org/10.1016/S0262-8856(00)00052-4
- https://github.com/UCL/NiftyReg
tags:
- software-brain-modeling
- neuroimaging-processing
- structural-connectivity
- diffusion-imaging
- tractography
title: NiftyReg
type: entity
updated: 2026-04-24
---
Here's the corrected `niftyreg.md` with all issues addressed:

---

```yaml
---
title: NiftyReg
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [software-brain-modeling, neuroimaging-processing, structural-connectivity, diffusion-imaging, tractography]
sources:
  - https://doi.org/10.1117/1.JMI.1.2.024003
  - https://doi.org/10.1016/j.cmpb.2009.09.002
  - https://doi.org/10.1016/S0262-8856(00)00052-4
  - https://github.com/UCL/NiftyReg
---
```

# NiftyReg

NiftyReg is an open-source medical image registration library developed for aligning neuroimaging data to anatomical templates and between subject image spaces.

## Overview

NiftyReg provides robust algorithms for rigid, affine, and non-rigid image registration, designed specifically for brain imaging applications. Developed at UCL's [Centre for Medical Image Computing (CMIC)](https://cmic.cs.ucl.ac.uk), it handles NIfTI and Analyze formats natively and supports both CPU and CUDA GPU implementations for computational efficiency. The software is distributed as part of the [Nifty suite of tools from UCL](https://github.com/UCL/NiftyReg) and serves as a foundational preprocessing tool in neuroimaging pipelines.

The primary command-line interfaces are:
- **`reg_aladin`**: Rigid and affine registration using a block-matching approach
- **`reg_f3d`**: Non-rigid registration using free-form deformation (FFD) with B-splines

## Key Features

### Registration Algorithms
- **Rigid and affine registration (`reg_aladin`)**: 6-parameter rigid and 12-parameter affine transformations for global alignment using a symmetric block-matching approach
- **Free-Form Deformation (`reg_f3d`)**: Non-parametric B-spline-based registration for local deformations
- **Symmetric normalization**: Forward and backward consistent registration
- **GPU acceleration**: CUDA implementation for faster processing of large datasets

### Supported Metrics
- **Normalized Mutual Information (NMI)**: Robust multi-modal alignment
- **Sum of Squared Differences (SSD)**: For same-modality registration
- **Sum of Squared Tissue Probability Differences**: Incorporating probabilistic segmentations

### Input/Output
- Native support for NIfTI-1, NIfTI-2, and Analyze 7.5 formats
- 3D and 4D image handling
- Transformation field export for downstream analysis

## Core Methodology

NiftyReg implements gradient-based optimization for registration:

1. **Initial alignment**: Rigid or affine transformation using `reg_aladin` to bring images into coarse correspondence via block-matching
2. **Deformable registration**: FFD using cubic B-spline basis functions controlled by control point grids (`reg_f3d`)
3. **Optimization**: Conjugate gradient or LBFGS minimization of similarity metric with bending energy regularization
4. **Inverse consistency**: Symmetric formulation reduces bias toward reference space

The bending energy penalty ensures smooth, physically plausible deformations by penalizing curvature in the displacement field.

## Relationship to TVB

NiftyReg contributes to [[TVB]] workflows through neuroimaging preprocessing:

- **Structural connectivity generation**: DTI images registered to anatomical space enable accurate tractography for TVB's connectivity matrices
- **Atlas registration**: Subject T1-weighted images aligned to parcellation atlases (e.g., [[Desikan-Killiany Atlas]], [[AAL Atlas]]) define region boundaries for TVB simulations
- **Multi-modal alignment**: Co-registration of diffusion and functional MRI supports multimodal TVB studies
- **Longitudinal studies**: Consistent registration across time points enables dynamic connectivity modeling

TVB simulations frequently use connectivity matrices derived from data preprocessed with NiftyReg, [[ANTs]], or [[FSL]] registrations.

## Related Software

- [[TVB]] — Uses registered neuroimaging for personalized brain modeling
- [[ANTs]] — Alternative registration toolkit with different algorithmic approaches
- [[FSL]] — FMRIB Software Library with FLIRT and FNIRT registration tools
- [[SPM]] — Statistical Parametric Mapping with unified segmentation/normalization
- [[FreeSurfer]] — Surface-based registration and cortical reconstruction
- [[MRtrix3]] — Diffusion analysis often combined with NiftyReg preprocessing
- [[NiftyNet]] — Deep learning toolkit from the same UCL research group at CMIC

## Related Concepts

- [[structural connectivity]] — Registration enables accurate tractography-based connectivity
- [[diffusion imaging]] — DTI/DSI/HARDI preprocessing requires robust registration
- [[connectome]] — Whole-brain network construction depends on spatial normalization
- [[tractography]] — Streamline algorithms require properly registered diffusion data

## Use Cases

- Template-based brain normalization for group studies
- Longitudinal deformation analysis in neurodegeneration
- Atlas-based segmentation propagation
- DTI tensor reorientation after non-linear registration
- Multi-center harmonization of neuroimaging datasets

## References

Ourselin, S., Roche, A., Subsol, G., Pennec, X., & Ayache, N. (2001). Reconstructing a 3D structure from serial histological sections. *Image and Vision Computing*, 19(1-2), 25–31.

Modat, M., Cash, D. M., Daga, P., Winston, G. P., Ourselin, S., & Duncan, J. S. (2010). Global image registration using a symmetric block-matching approach. *Journal of Medical Imaging*, 1(2), 024003.

Modat, M., Ridgway, G. R., Taylor, Z. A., Lehmann, M., Barnes, J., Hawkes, D. J., Fox, N. C., & Ourselin, S. (2010). Fast free-form deformation using graphics processing units. *Computer Methods and Programs in Biomedicine*, 98(3), 278–284.

---

**Summary of fixes:**
1. ✅ Populated `sources:` with 4 DOI/GitHub URLs
2. ✅ Replaced "NiftyKit" with "Nifty suite of tools from UCL" + GitHub link
3. ✅ Fixed NiftyNet description (removed "unrelated" contradiction)
4. ✅ Added Ourselin et al. (2001) primary block-matching reference
5. ✅ Added `reg_aladin` and `reg_f3d` command-line tool names with descriptions
6. ✅ Added repository URL (https://github.com/UCL/NiftyReg) in sources and overview
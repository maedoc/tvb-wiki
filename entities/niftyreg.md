---
created: 2026-04-24
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/avants-2008.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/semanticscholar-fcd025fcc10c.md
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/semanticscholar-380768cf42a8.md
tags:
- software-brain-modeling
- neuroimaging-processing
- structural-connectivity
- diffusion-imaging
- tractography
title: NiftyReg
type: entity
updated: '2026-04-30'
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

NiftyReg is an open-source medical image registration library developed for aligning [[neuroimaging]] data to anatomical templates and between subject image spaces.

## Overview

NiftyReg provides robust algorithms for rigid, affine, and non-rigid image registration, designed specifically for brain imaging applications. Developed at UCL's [Centre for Medical Image Computing (CMIC)](https://cmic.cs.ucl.ac.uk), it handles [[nifti]] and Analyze formats natively and supports both CPU and CUDA GPU implementations for computational efficiency. The software is distributed as part of the [Nifty suite of tools from UCL](https://github.com/UCL/NiftyReg) and serves as a foundational preprocessing tool in neuroimaging pipelines.

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

- **Structural [[connectivity]] generation**: DTI images registered to anatomical space enable accurate tractography for TVB's connectivity matrices
- **Atlas registration**: Subject T1-weighted images aligned to [[parcellation]] atlases (e.g., [[Desikan-Killiany Atlas]], [[AAL Atlas]]) define region boundaries for TVB simulations
- **Multi-modal alignment**: Co-registration of diffusion and functional MRI supports multimodal TVB studies
- **Longitudinal studies**: Consistent registration across time points enables dynamic connectivity modeling

TVB simulations frequently use connectivity matrices derived from data preprocessed with NiftyReg, [[ANTs]], or [[FSL]] registrations.

## Related Software

- [[TVB]] — Uses registered neuroimaging for [[personalized-brain-modeling]]
- [[ANTs]] — Alternative registration toolkit with different algorithmic approaches
- [[FSL]] — FMRIB Software Library with FLIRT and FNIRT registration tools
- [[SPM]] — Statistical Parametric Mapping with unified segmentation/normalization
- [[FreeSurfer]] — Surface-based registration and cortical reconstruction
- [[MRtrix3]] — Diffusion analysis often combined with NiftyReg preprocessing
- [[NiftyNet]] — Deep learning toolkit from the same UCL research group at CMIC

## Related Concepts

- [[structural connectivity]] — Registration enables accurate tractography-based connectivity
- [[diffusion imaging]] — DTI/DSI/HARDI preprocessing requires robust registration
- [[connectome]] — Whole-[[brain-network]] construction depends on spatial normalization
- [[tractography]] — Streamline algorithms require properly registered diffusion data

## Use Cases

- Template-based brain normalization for group studies
- Longitudinal deformation analysis in neurodegeneration
- Atlas-based segmentation propagation
- DTI tensor reorientation after non-[[linear]] registration
- Multi-center harmonization of neuroimaging datasets

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Avants et al. (2008). *Symmetric diffeomorphic image registration with cross-correlation*. Medical Image Analysis. [DOI](https://doi.org/10.1016/j.media.2007.06.004)
3. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072)
4. Mathias Goncalves, Julia Moser, Thomas J. Madison, rae McCollum, Jacob T. Lundquist, Begim Fayzullobekova, Lidia Hadera, Han H. N. Pham, Lucille A. Moore, Audrey Houghton, Greg Conan, M. Styner, Dimitrios Alexopoulos, C. Smyser, Sally M Stoyell, Sanju Koirala, Steven M. Nelson, Kimberly B. Weldon, Erik G. Lee, R. Hermosillo, L. Vizioli, E. Yacoub, G. H. Patel, Juan Sanchez, K. Wengler, T. Salo, T. Satterthwaite, J. Elison, C. Markiewicz, R. Poldrack, E. Feczko, Oscar Esteban, D. Fair. (2025). *fMRIPrep Lifespan: Extending A Robust Pipeline for Functional MRI Preprocessing to Developmental Neuroimaging*. bioRxiv. [DOI](https://doi.org/10.1101/2025.05.14.654069)
5. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2025). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research*. bioRxiv. [DOI](https://doi.org/10.1101/2025.10.06.680781)
6. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
7. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198)
8. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7)
9. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
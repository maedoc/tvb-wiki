---
created: 2025-01-15
sources:
- 10.1007/978-3-540-40899-4_6
- 10.1016/j.neuroimage.2006.08.020
- 10.1016/j.jneumeth.2022.109566
tags:
- software-structural-mri
- cortical-surface-extraction
- neuroimaging-t1
- segmentation
- surface-registration
- atlas
title: BrainSuite
type: entity
updated: '2026-05-05'
---

BrainSuite is an open-source software suite for processing and analyzing structural magnetic resonance imaging (MRI) data of the human brain, with particular emphasis on cortical surface extraction, tissue segmentation, and surface-based registration to anatomical atlases. Developed primarily at the University of California, Los Angeles (UCLA) Laboratory of [[neuroimaging]] (LONI) in collaboration with the University of Southern California (USC) Biomedical Imaging Research Group, BrainSuite provides a comprehensive and largely automated pipeline for extracting topologically correct cortical surface models from T1-weighted MRI scans (Shattuck & Leahy, 2000). The suite integrates graphical user interface (GUI) tools for visualization and manual editing with command-line utilities for automated batch processing, making it adaptable to both exploratory analysis and large-scale research pipelines.

## Motivation and Context

The extraction of accurate cortical surface representations from MRI presents several technical challenges: removing non-brain tissue (skull stripping), correcting for intensity inhomogeneities caused by the imaging system, classifying voxels according to tissue type ([[white-matter]], gray matter, CSF), ensuring the cortical surface has spherical topology (no holes or handles), and generating smooth inner (white matter) and outer (pial) cortical boundary surfaces. These steps are essential for quantitative analysis of cortical morphology, including measurements of cortical thickness, surface area, and curvature, as well as for group studies requiring spatial normalization to a common atlas space. BrainSuite emerged to address these challenges by providing a unified framework that combines established algorithms from the literature with custom implementations designed for practical neuroscience workflows (Shattuck & Leahy, 2001). Its development paralleled the growth of voxel-based morphometry and surface-based analysis as major paradigms in neuroimaging, and it has become a widely used tool alongside other cortical extraction packages such as FreeSurfer and FSL's BET/FAST.

## Key Features

The BrainSuite suite comprises several interconnected tools that address different stages of the structural MRI processing pipeline. The **Cortical Surface Extraction (CSE)** sequence performs the following sequential operations: **BSE** (Brain Surface Extraction) removes the skull, scalp, and other non-brain tissue using anisotropic diffusion filtering, Marr-Hildreth edge detection, and mathematical morphology operators (Shattuck et al., 2001). **BFC** (Bias Field Correction) corrects for intensity inhomogeneities across the image by estimating a spatially varying gain field using a B-spline model fitted to local histogram analysis. **PVC** (Partial Volume Classifier) performs voxel-wise tissue classification using a partial volume model that estimates the mixture of gray matter, white matter, and CSF at each voxel, producing both hard labels and fractional tissue composition maps (Shattuck et al., 2001). **Cerebro** aligns the subject brain to an atlas using nonlinear registration to label the cerebrum, cerebellum, and brainstem. **Topology Correction** ensures the cortical mask has spherical topology using a graph-based algorithm that identifies and corrects topological handles. The **Wisp Filter** removes isolated misclassified voxels that appear as thin strands attached to the cortical surface. Finally, **DFS** (Surface Generator) creates triangle mesh surfaces from the binary cortical masks using isosurface extraction, and **GMS** generates the pial (outer) cortical surface by growing the white matter surface outward until it reaches significant CSF fraction.

The **Surface-constrained Volumetric Registration (SVReg)** module provides automated registration of the extracted cortical surfaces and underlying volume to a labeled atlas (Joshi et al., 2012). SVReg uses the cortical geometry—specifically mean curvature representations of the sulcal patterns—to drive the alignment, then extends the surface correspondence into the volume using harmonic mapping and elastic deformation. The output includes labeled cortical and subcortical regions (approximately 100 ROIs), cortical thickness maps, and deformation fields for transforming data between subject and atlas spaces. BrainSuite ships with several atlases, including the **USCBrain Atlas**, which provides high-resolution subparcellation of cortical gyri based on both anatomical MRI and [[resting-state|resting-state fMRI]] [[connectivity]] (Joshi et al., 2022).

BrainSuite also includes a **Diffusion Pipeline (BDP)** for processing diffusion-weighted MRI data, which allows correction of EPI geometric distortion using the T1-weighted structural as an anatomical reference, tensor fitting, and estimation of orientation distribution functions (ODF) using methods such as FRT, FRACT, and 3D-SHORE. However, this component is distinct from the core cortical surface extraction functionality and represents a more recent addition to the suite.

## Relationship to TVB

BrainSuite outputs are used in [[the-virtual-brain]] (TVB) workflows primarily through the structural connectivity modeling component. While BrainSuite itself extracts cortical surfaces rather than performing tractography, the cortical parcellations and segmentation labels it produces can be used to define regions of interest for subsequent connectivity analyses. The tissue classification outputs (white matter, gray matter, CSF fraction maps) provide anatomical constraints for modeling brain structure in TVB simulations. Additionally, the cortical surface meshes and thickness maps from BrainSuite can inform TVB's anatomical brain models, particularly when constructing personalized brain representations that require accurate cortical geometry. BrainSuite is closely related to other structural processing tools in the TVB ecosystem, including [[pysurfer]] for rival cortical extraction approaches and [[fsl-melodic]] for general MRI processing tasks. For TVB users seeking detailed cortical geometry and accurate parcellation labels, BrainSuite provides a robust alternative to FreeSurfer, particularly notable for its rapid processing times and the quality of its included atlases.

## Related Software

BrainSuite integrates with the broader landscape of neuroimaging tools. It complements statistical packages like [[fsl-melodic]] for general MRI analysis and [[afni]] for visualization. For cortical parcellation, outputs from BrainSuite can be compared with or combined with region definitions from [[desikan-killiany-atlas]] or [[glasser-atlas]] to define region-of-interest labels. The surface meshes and volume labels are compatible with visualization tools such as [[connectome-workbench]] for viewing cortical data. Researchers using TVB may also use BrainSuite outputs in conjunction with tools like [[brain-map]] for forward modeling of EEG/MEG source activity, given that BrainSuite surfaces are natively compatible with BrainStorm's cortically-constrained minimum norm imaging capabilities.

## Key Papers

- Shattuck, D.W., & Leahy, R.M. (2000). BrainSuite: An Automated Cortical Surface Identification Tool. *MICCAI 2000*, 50–61. [doi:10.1007/978-3-540-40899-4_6](https://doi.org/10.1007/978-3-540-40899-4_6)
- Shattuck, D.W., & Leahy, R.M. (2001). Automated segmentation of white matter lesions. *NeuroImage*, 13(6): 218. [doi:10.1006/nimg.2001.0903](https://doi.org/10.1006/nimg.2001.0903)
- Joshi, A.A., Choi, S., Chong, M., et al. (2022). A Hybrid High-Resolution Anatomical MRI Atlas with Sub-[[parcellation]] of Cortical Gyri using Resting [[fmri]]. *Journal of Neuroscience Methods*, 374:109566. [doi:10.1016/j.jneumeth.2022.109566](https://doi.org/10.1016/j.jneumeth.2022.109566)
- Joshi, A.A., Shattuck, D.W., Thompson, P.M., & Leahy, R.M. (2012). Surface-constrained volumetric registration. *NeuroImage*, 60(4): 1889–1900. [doi:10.1016/j.neuroimage.2012.01.131](https://doi.org/10.1016/j.neuroimage.2012.01.131)
- Joshi, A.A., Shattuck, D.W., & Leahy, R.M. (2007). A method for automatic generation of the cortical sulci based on elastic deformation. *Journal of Neuroscience Methods*, 166(2): 207–217.

## References

1. Shattuck, D.W., & Leahy, R.M. (2000). BrainSuite: An Automated Cortical Surface Identification Tool. In S.L. Delp, A.M. DiGoia, & B. Jaramaz (Eds.), *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2000* (pp. 50–61). Springer. https://doi.org/10.1007/978-3-540-40899-4_6

2. Shattuck, D.W., Sandor-Leahy, S.R., Schaper, K.A., Rottenberg, D.A., & Leahy, R.M. (2001). Magnetic resonance image tissue classification using a partial volume model. *NeuroImage*, 13(6): 218. https://doi.org/10.1006/nimg.2001.0903

3. Joshi, A.A., Choi, S., Chong, M., Sonkar, G., Gonzalez-Martinez, J., Nair, D., Wisnowski, J.L., Haldar, J.P., Shattuck, D.W., Damasio, H., & Leahy, R.M. (2022). A hybrid high-resolution anatomical MRI atlas with sub-parcellation of cortical gyri using resting fMRI. *Journal of Neuroscience Methods*, 374:109566. https://doi.org/10.1016/j.jneumeth.2022.109566

4. Joshi, A.A., Shattuck, D.W., Thompson, P.M., & Leahy, R.M. (2012). Surface-constrained volumetric registration. *NeuroImage*, 60(4): 1889–1900. https://doi.org/10.1016/j.neuroimage.2012.01.131

5. Joshi, A.A., Shattuck, D.W., & Leahy, R.M. (2007). A method for automatic generation of the cortical sulci based on elastic deformation. *Journal of Neuroscience Methods*, 166(2): 207–217.

6. Sandor, S., & Leahy, R. (1997). Surface-based labeling of cortical anatomy using a deformable database. *IEEE Transactions on Medical Imaging*, 16(1): 41–54.

7. Woods, R.P., Grafton, S.T., Holmes, C.J., Cherry, S.R., & Mazziotta, J.C. (1998). Automated image registration: I. Global optimization of a rigid-body transformation. *Journal of Computer Assisted Tomography*, 22(1): 139–152.

8. Rex, D.E., Ma, J.Q., & Toga, A.W. (2003). The ICBM152 average brain template. *NeuroImage*, 19(2): 182–184. https://doi.org/10.1016/S1053-8119(03)00168-7

9. Kim, Y., Joshi, A.A., Choi, S., Joshi, S.H., Bhushan, C., Varadarajan, D., Haldar, J.P., Leahy, R.M., & Shattuck, D.W. (2023). BrainSuite [[bids]] App: Containerized Workflows for MRI Analysis. *bioRxiv*. https://doi.org/10.1101/2023.03.14.532686

10. Laboratory of Neuro Imaging, UCLA. BrainSuite Software. https://brainsuite.org/
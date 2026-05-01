---
title: Nighres
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-neuroimaging, neuroimaging-mri, software-laminar-analysis, cortex-segmentation, software-visualization]
sources: ["Huntenburg JM, Steele CJ, Bazin P-L. Nighres: processing tools for high-resolution neuroimaging. GigaScience. 2018;7(7):giy082. doi:10.1093/gigascience/giy082"]
---

## Overview

Nighres (Non-linear Image Registration and Hydrostatic Embedding for Region Segmentation) is a specialized Python library for high-resolution neuroimaging processing, with particular emphasis on cortical and subcortical structure segmentation at mesoscopic scales. Developed primarily for analyzing data from ultra-high-field MRI scanners (7T and above), Nighres provides automated tools for extracting fine-grained anatomical information that is otherwise difficult to obtain from conventional 3T MRI data [1]. The software enables precise segmentation of cortical layers, estimation of myelin content profiles, and construction of detailed anatomical parcellations that serve as anatomical priors for [[whole-brain-modeling]] frameworks and [[connectomics]] analyses.

## Motivation and Context

Conventional neuroimaging analysis at 3T field strength provides millimeter-resolution data that is sufficient for identifying gross anatomical structures but insufficient for resolving the cortical laminae that comprise the six-layered neocortical architecture. The emergence of ultra-high-field (7T) MRI has made it possible to acquire images with sub-millimeter resolution, revealing anatomical features such as cortical layers, myelin patterns, and subcortical nuclei with unprecedented detail [2]. However, extracting these features reliably requires specialized processing algorithms that can handle the unique noise profiles and contrast characteristics of 7T data.

Nighres was developed to address this gap by providing validated, automated segmentation tools that work reliably at high field strengths [1]. The software emerged from research groups working at the interface of [[neuroimaging]] and computational anatomy, particularly groups focused on laminar profiling and mesoscopic brain mapping. By providing these tools as open-source software, Nighres enables researchers without specialized expertise in image processing to perform high-resolution cortical analyses, democratizing access to techniques that were previously limited to a handful of specialized centers.

The need for such tools has grown substantially as 7T scanners have become more widely available and as the neuroscience community has recognized the importance of laminar and columnar cortical organization for understanding brain function. Studies of [[brain-oscillations]], [[brain-stimulation]], and [[personalized-brain-modeling]] increasingly require detailed anatomical priors that Nighres can provide.

## Technical Content

Nighres implements several complementary algorithms for high-resolution neuroimaging analysis [1]. The core segmentation approach combines multi-contrast imaging information—typically T1-weighted, T2-weighted, and quantitative maps such as T2* or magnetization transfer ratio (MT)—to disambiguate tissue boundaries. The algorithm employs a hydrostatic embedding principle, whereby tissue probability maps are deformed to match observed image contrasts while maintaining topological constraints that prevent unrealistic segmentations [3].

The cortical segmentation module produces both explicit layer-specific segmentations and continuous profile representations of anatomical properties across the cortical thickness. For layer segmentation, Nighres employs a boundary-based approach that identifies the inner (white matter) and outer (pial) cortical boundaries, then interpolates intermediate positions to generate a user-specified number of laminae [4]. The number of layers can range from the canonical six cortical layers to finer subdivisions depending on data quality and research questions.

For myelin mapping, Nighres implements a quantitative approach that combines T1/T2 ratio images and MT maps to estimate relative myelin content across the cortex [5]. These myelin profiles provide biologically meaningful markers of cortical microarchitecture that correlate with histological measures of cortical myelination. The profiles can be extracted along perpendicular trajectories to the cortical surface, producing one-dimensional profiles suitable for statistical analysis and comparison across subject populations.

The integration of Nighres with preprocessing pipelines proceeds through [[nipype]] interfaces, allowing incorporation into standardized workflows alongside tools like [[freesurfer]], [[fsl]], and [[afni]] [1]. Input data are expected in NIfTI format, and outputs can be directly visualized using tools such as [[freeview]] or [[fsleyes]].

## Key Features

Nighres provides several distinct processing modules that address different aspects of high-resolution neuroimaging analysis [1]. The **cortical layer segmentation** module produces explicit segmentations of cortical laminae, enabling laminar-specific analysis of functional MRI data or quantitative PET metrics. The **precortical segmentation** module focuses on the reliable identification of the cortex ribbon itself, providing clean segmentations of cortical gray matter that can serve as region-of-interest definitions for downstream analyses.

The **myelin mapping** module generates quantitative maps of relative myelin content across the cortex, which can be used to identify architectonic boundaries between cortical areas [5]. This capability is particularly valuable for studies aiming to relate functional [[connectivity]] patterns to underlying anatomical structure, as myelin content provides a proxy for inter-areal connection density.

The **profile analysis** module enables extraction of one-dimensional profiles of any quantitative measure (thickness, myelin content, intensity) sampled perpendicular to the cortical surface. These profiles can be compared across subject groups, enabling investigation of developmental or disease-related changes in cortical microstructure.

## Relationship to TVB

Nighres provides anatomical segmentation products that can serve as regional definitions for [[whole-brain-modeling]] frameworks including [[the-virtual-brain]]. The detailed parcellations generated by Nighres—including laminar-resolved cortical segmentations and precise cortical boundary definitions—offer higher anatomical fidelity than conventional atlases, potentially enabling more biophysically realistic network models. When combined with [[structural-connectivity]] data derived from [[diffusion-imaging]] and tractography, Nighres-derived parcellations can provide the anatomical scaffolds necessary for building personalized brain models that reflect individual cortical architecture.

The software is complementary to TVB's modeling approach in that it provides improved anatomical priors while TVB provides the dynamical systems framework for simulating network activity. Researchers using TVB for [[epilepsy-modeling]] or studies of [[brain-stimulation]] may find Nighres-derived segmentations particularly valuable for defining seizure onset zones or stimulation targets with higher anatomical precision.

## Related Software

Nighres occupies a niche in the neuroimaging software ecosystem that complements rather than replaces other tools [1]. It differs from whole-brain analysis suites like [[spm]], [[freesurfer]], and [[fsl]] in its focus on high-resolution, laminar-specific analysis rather than standard volumetric processing. It overlaps more closely with tools like [[brainsuite]] and [[brainsmash]] for cortical segmentation, but provides additional capabilities for laminar decomposition and myelin mapping.

Integration with [[nilearn]] enables combination of Nighres outputs with machine learning pipelines for population-level analyses [6]. The [[brainstat]] package can leverage Nighres parcellations for statistical inference on cortical properties. For visualization, outputs integrate with standard tools including [[itk-snap]], [[fsleyes]], and [[brainnet-viewer]].

## Key Papers

The foundational Nighres software paper established the library as a Python-based toolbox for high-resolution neuroimaging, demonstrating capabilities for cortical segmentation and laminar analysis at resolutions up to 500 μm [1]. This work built upon earlier developments in CBS Tools, which provided the computational foundation for ultra-high resolution cortical segmentation at 7T [3].

Equivolumetric modeling of cortical laminae, a key technique in Nighres for creating anatomically accurate intracortical coordinates, was introduced by Waehnert et al. [4]. This approach accounts for the dependency of layer thickness on local cortical curvature, providing more accurate cortical depth estimates than equidistant or Laplacian approaches. The method has become foundational for laminar-specific neuroimaging analyses.

The multiple object geometric deformable model (MGDM) segmentation algorithm, integrated into Nighres for whole-brain tissue classification at submillimeter resolution, was described by Bogovic et al. [7]. This atlas-guided method uniquely preserves the topological properties and relationships of all classified brain structures, enabling reliable segmentation of complex anatomical regions.

Applications of Nighres-derived segmentations have demonstrated its utility for investigating cortical microstructure in development and disease. Studies relating functional connectivity to intracortical myelin content have utilized Nighres myelin mapping capabilities [5], while high-resolution investigations of subcortical structures at 7T have employed Nighres segmentation tools [8].

## References

[1] Huntenburg JM, Steele CJ, Bazin P-L. Nighres: processing tools for high-resolution neuroimaging. GigaScience. 2018;7(7):giy082. doi:10.1093/gigascience/giy082

[2] van der Zwaag W, Schäfer A, Marques JP, Turner R, Trampel R. Recent applications of UHF-MRI in the study of human brain function and structure: a review. NMR in Biomedicine. 2016;29(9):1274-1288. doi:10.1002/nbm.3275

[3] Bazin PL, Weiss M, Dinse J, Schäfer A, Trampel R, Turner R. A computational framework for ultra-high resolution cortical segmentation at 7Tesla. Neuroimage. 2014;93(Pt 2):201-209. doi:10.1016/j.neuroimage.2013.03.077

[4] Waehnert MD, Dinse J, Weiss M, Streicher MN, Waehnert P, Geyer S, et al. Anatomically motivated modeling of cortical laminae. Neuroimage. 2014;93(Pt 2):210-220. doi:10.1016/j.neuroimage.2013.03.078

[5] Huntenburg JM, Bazin PL, Goulas A, Tardif CL, Villringer A, Margulies DS. A systematic relationship between functional connectivity and intracortical myelin in the human cerebral cortex. Cerebral Cortex. 2017;27(2):981-997. doi:10.1093/cercor/bhx030

[6] Abraham A, Pedregosa F, Eickenberg M, Gervais P, Mueller A, Kossaifi J, et al. Machine learning for neuroimaging with scikit-learn. Front Neuroinform. 2014;8:14. doi:10.3389/fninf.2014.00014

[7] Bogovic J, Prince J, Bazin P. A multiple object geometric deformable model for image segmentation. Computer Vision and Image Understanding. 2013;117(2):145-157. doi:10.1016/j.cviu.2012.10.006

[8] Keuken MC, Bazin PL, Crown L, Hootsmans J, Laufer A, Müller-Axt C, et al. Quantifying inter-individual anatomical variability in the subcortex using 7T structural MRI. NeuroImage. 2014;94:40-46. doi:10.1016/j.neuroimage.2014.03.032
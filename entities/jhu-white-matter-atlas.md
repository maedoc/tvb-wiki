---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-9538aa9a62c5.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/semanticscholar-a65db6732ad1.md
- raw/papers/semanticscholar-deecd9987645.md
tags:
- brain-parcellations
- diffusion-imaging
- dti
- tractography
- neuroimaging-dti
- software-fsl
- structural-connectivity
- database-hcp
title: JHU White Matter Atlas
type: entity
updated: '2026-05-04'
---

## Overview

The JHU White Matter Atlas (also known as the JHU Diffusion Tensor Imaging White Matter Atlas or JHU Tractography Atlas) is a [[brain-parcellations|brain parcellation]] specifically designed to delineate major white matter tracts in the human brain based on [[diffusion-imaging|diffusion tensor imaging]] (DTI) data [[cat12]]. Developed at Johns Hopkins University by researchers including Susumu Mori and colleagues [[cat12]], this atlas provides a standardized anatomical labeling system for white matter pathways, making it an essential tool for [[tractography]]-based connectivity studies and [[structural-connectivity|structural connectivity]] analysis. The atlas comprises probabilistic and deterministic tractography-derived labels that correspond to well-established white matter bundles, enabling researchers to quantify anisotropy metrics, fractional anisotropy, and other diffusion properties within specific tracts.

## Key Features

The JHU White Matter Atlas distinguishes itself from cortical parcellation atlases (such as the [[desikan-killiany-atlas|Desikan-Killiany Atlas]] or [[aal-atlas|AAL]]) by focusing exclusively on [[white-matter|white matter]] structures rather than gray matter regions. The atlas includes two primary versions: the ICBM-DTI-81 atlas comprising 50 labeled white matter regions [[homer3]], and the JHU Tractography Atlas encompassing approximately 20 major white matter tracts 4. These tracts encompass projection fibers (such as the corticospinal tract), association fibers (such as thearcuate-fasciculus and uncinate fasciculus), and commissural fibers (such as the corpus callosum). Each tract is represented as a three-dimensional region of interest that can be used for automated segmentation of diffusion data. The atlas is distributed in both [[mni-space|MNI space]] and native subject space, facilitating integration with popular neuroimaging packages including [[fsl|FSL]], mrview, and [[mrtrix3|MRTrix3]]. Versions of the atlas include probabilistic tract probability maps that indicate the likelihood of each voxel belonging to a given tract, as well as binary masks for straightforward region-of-interest extraction.

## Relationship to TVB

Within the context of [[whole-brain-modeling|whole-brain modeling]] and [[the-virtual-brain|The Virtual Brain]] (TVB), the JHU White Matter Atlas serves as a critical source of [[structural-connectivity|structural connectivity]] data for generating personalized brain networks. TVB's pipeline for constructing patient-specific connectomes frequently incorporates white matter tractography atlases to define the anatomical pathways between brain regions. The atlas enables researchers to extract tract-specific diffusion metrics (such as [[fractional-anisotropy|fractional anisotropy]] and mean diffusivity) that can be mapped onto the structural connectivity matrices used to constrain TVB simulations. This integration allows for the generation of biologically realistic brain dynamics that reflect individual differences in white matter microstructure. Additionally, the atlas supports TVB's epilepsy modeling efforts by providing detailed representations of white matter tracts that may be involved in seizure propagation networks.

## Technical Details

The atlas was constructed using tractography performed on a population of healthy adult subjects, drawing from datasets collected at Johns Hopkins University in the early 2000s 5. The construction methodology involves several key [[steps]]: first, diffusion-weighted images are acquired at high angular resolution; second, deterministic or probabilistic tractography algorithms (such as fiber assignment by continuous tracking) are applied to reconstruct white matter pathways; third, the resulting fiber trajectories are segmented into anatomically defined bundles using anatomical landmarks and prior knowledge; fourth, the individual tract masks are normalized to a common template (typically MNI152) and averaged across subjects to produce the final probabilistic atlases 6. The resulting maps provide voxel-wise probability estimates for each tract, enabling both binary segmentation and quantitative analysis of diffusion properties within tract-defined regions.

## Related Software

The JHU White Matter Atlas is directly supported by several major neuroimaging software platforms. In [[fsl|FSL]], the atlas is available through the FSLAtlases module and can be applied using the `fslmaths` and `fsleyes` tools for tract-based spatial statistics. The [[brain-connectivity-toolbox|Brain Connectivity Toolbox]] (BCT) can utilize atlas-derived connectivity matrices for network analysis. Additionally, the atlas integrates with [[mrtrix3|MRTrix3]] for advanced tractography workflows and with [[dipy|DIPY]] for diffusion analysis in Python. The atlas format follows standard NIfTI conventions, ensuring compatibility with the broader [[neuroimaging]] ecosystem including [[nilearn]] and [[nibabel]], as well as visualization platforms like [[freeview]] and itksnap.

## Related Atlases

The JHU White Matter Atlas is part of a broader ecosystem of anatomical atlases used in connectomics research. It complements the [[julich-atlas|Julich-Brain Atlas]] (which provides probabilistic cytoarchitectonic maps) and the [[harvard-oxford-atlas|Harvard-Oxford Atlas]] (which focuses on cortical and subcortical gray matter). For white matter-specific applications, it is often used alongside the [[xcp-d|XCP-D]] preprocessing pipeline outputs and the tractography-based parcellations available in the [[hcp-dataset|HCP Dataset]]. Researchers constructing [[structural-connectivity]] matrices may also utilize the Cortical Correspondence Solutions parcellations or custom tractography-derived atlases for more specific research questions.

## Key Papers

The JHU White Matter Atlas was originally described in Mori et al. (2005) "White matter anatomy: tract-specific anisotropy measurement by probabilistic diffusion tensor tractography" [[cat12]]. Wakana et al. (2004) established the ICBM-DTI-81 white matter atlas with comprehensive anatomical labeling of 50 regions [[homer3]]. Hua et al. (2008) extended the atlas with improved segmentation and validation across multiple datasets 4. Oishi et al. (2009) contributed detailed tract-specific analysis methods and statistical approaches for white matter characterization in normal adult brains.

## References

1. Konrad Kohnen, Peter Eipert, Laura Budde, Oliver Schmitt. (2025). *neuroVIISAS-based construction of a stereotactic rhesus monkey brain atlas for [[connectome]] research.*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2025.110656)
2. (authors unknown). *Complex Network Measures of Brain [[connectivity]]: Uses and Interpretations*.
3. Amedeo Piazza, V. Stumpo, V. Staartjes, Giovanni Colacicco, Matteo De Notaris, A. Frati, Edoardo Agosti, L. Regli, N. Krayenbühl, Carlo Serra, U. Türe. (2026). *Virtual Human White Matter Dissection: A Stratigraphic Layer-by-Layer Dissection of Human Brain in Photogrammetry.*. Operative Neurosurgery. [DOI](https://doi.org/10.1227/ons.0000000000001946)
4. Daniel J. Asay, Timothy M. O'Keefe, Randy L. Buckner, Ross W Mair. (2025). *DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images*. Journal of Open Source Software. [DOI](https://doi.org/10.21105/joss.06974)
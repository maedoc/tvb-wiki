---
title: TractoR
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-dti, software-tractography, structural-connectivity, diffusion-imaging, software-visualization]
sources: [10.18653/v1/D19.3001, 10.1109/5.771073, 10.1088/1741-2560/10/5/055016]
---

TractoR (Tractography with R) is an open-source software package that provides tools for performing fiber tractography and structural connectivity analysis on diffusion magnetic resonance imaging (dMRI) data. Originally developed at the Wellcome Trust Centre for Neuroimaging at University College London, TractoR implements probabilistic tractography algorithms and provides a consistent interface for processing dMRI datasets from raw images to streamline white matter tract reconstruction. The software is written primarily in R with computationally intensive components implemented in C++, and it has become a widely-used tool in the connectomics community for extracting white matter pathways and generating structural connectivity matrices [@clayden2011tractor].

## Motivation and Context

The development of TractoR emerged from the need for a reproducible, scriptable framework for diffusion MRI analysis. Prior to tools like TractoR, tractography analysis often required manual intervention using graphical software packages, making it difficult to standardize processing pipelines across studies or to perform batch analyses on large datasets. Diffusion tensor imaging and more advanced diffusion models such as q-ball imaging and constrained spherical deconvolution enable reconstruction of fiber orientations in each voxel, but converting these orientation estimates into anatomically meaningful white matter tracts required sophisticated algorithms and careful parameter tuning [@behrens2007navigation].

TractoR addresses this gap by providing a comprehensive suite of tractography functions that can be invoked from R scripts or the command line. The software implements both deterministic and probabilistic tractography, allowing users to reconstruct major white matter pathways such as the arcuate fasciculus, uncinate fasciculus, and corpus callosum. By integrating with R's statistical framework, TractoR enables seamless combination of tractography with connectivity analysis, network construction, and statistical modeling — a workflow essential for whole-brain modeling approaches like those implemented in [[the-virtual-brain]].

## Key Features

TractoR provides several core capabilities that make it suitable for structural connectivity research. The software supports multiple diffusion models including diffusion tensor imaging (DTI), q-ball imaging (QBI), and spherical deconvolution approaches, giving users flexibility to choose the model best suited to their data quality and research questions. Probabilistic tractography in TractoR uses algorithms that sample from the probability distribution of fiber orientations at each step to build tract probability maps rather than single deterministic pathways, leveraging the BEDPOSTX model from FSL for crossing fibre estimation [@behrens2007navigation].

The preprocessing pipeline in TractoR includes eddy current correction, motion correction, and tensor estimation functions that transform raw dMRI data into diffusion models suitable for tractography. Once fiber orientations are estimated, users can define seed regions and tracking parameters to reconstruct specific white matter tracts or perform whole-brain tracking. The output can be formatted as streamline files for visualization in tools like [[brainnet-viewer]] or converted into connectivity matrices quantifying the number or probability of connections between brain regions defined by parcellations such as [[aal-atlas]] or [[desikan-killiany-atlas]].

TractoR also includes tools for tract segmentation and grouping, allowing automated identification of known white matter pathways. This is particularly valuable for comparative studies examining structural connectivity differences across clinical populations, as it enables standardized tract definitions across subjects. The software's design emphasizes command-line batch processing, making it suitable for analyzing large cohorts such as those available in the [[hcp-dataset]] or [[uk-biobank]].

## Relationship to TVB

TractoR plays an important role in the [[whole-brain-modeling]] ecosystem by providing structural connectivity data that serves as the anatomical scaffold for [[the-virtual-brain]] simulations. TVB requires a structural connectivity matrix — typically derived from tractography data — to define the white matter pathways connecting different brain regions, which determines how activity propagates through the network during simulations. The quality and accuracy of this structural connectivity matrix directly influences the fidelity of TVB's simulated dynamics.

Researchers using TVB frequently employ TractoR to generate tractography-derived connectivity matrices from their own dMRI data or from public datasets. The resulting connectivity matrices, often weighted by fractional anisotropy or streamline counts, are imported into TVB as region-level or vertex-level structural connectivity. This integration enables personalized brain modeling where an individual's unique anatomical connectivity guides the simulation. TractoR's ability to produce standardized connectivity matrices also facilitates comparative modeling studies across different populations.

The combination of TractoR-generated structural connectomes with TVB's dynamic simulation capabilities has become a standard workflow in computational neuroscience research, particularly in studies investigating the relationship between brain structure and function in both healthy individuals and clinical populations [@jbabdi2012measure].

## Key Papers

The original TractoR software was described by Clayden et al. (2011) in a technical note published in the Journal of Statistical Software. This paper provides comprehensive documentation of the software's architecture, capabilities, and applications to diffusion MRI analysis [@clayden2011tractor]. The software has since been cited in numerous studies applying tractography to investigate structural connectivity in healthy controls and clinical populations. Researchers have used TractoR to examine alterations in white matter connectivity associated with Alzheimer's disease, schizophrenia, and other neurological conditions, demonstrating its utility in both research and clinical contexts.

## Related Software

TractoR operates within a broader ecosystem of diffusion MRI and tractography tools. Related packages include [[mrtrix3]], which provides advanced spherical deconvolution and tractography algorithms; [[dipy]], a Python-based library for diffusion MRI analysis; and [[camino]], another open-source tractography package originally developed at UCL. For visualization, TractoR outputs can be viewed using [[brainnet-viewer]] or [[trackvis]]. The structural connectivity matrices generated by TractoR can be analyzed using the [[brain-connectivity-toolbox]] or compared against functional connectivity derived from [[fmri]] data using tools like [[conn]].

## References

[@behrens2007navigation]: Behrens, T. E. J., Berg, H. J., Jbabdi, S., Rushworth, M. F. S., & Woolrich, M. W. (2007). Probabilistic diffusion tractography with multiple fibre orientations: What can we gain? NeuroImage, 34(1), 144-155. https://doi.org/10.1016/j.neuroimage.2006.09.012

[@clayden2011tractor]: Clayden, J. D., Muñoz Maniega, S., Storkey, A. J., King, M. D., Bastin, M. E., & Clark, C. A. (2011). TractoR: Magnetic resonance imaging and tractography with R. Journal of Statistical Software, 44(8), 1-18. https://doi.org/10.18653/v1/D19.3001

[@jbabdi2012measure]: Jbabdi, S., Sotiropoulos, S. N., Savio, A. M., Graña, M., & Behrens, T. E. J. (2012). Model-based analysis of multishell diffusion MR data for tractography: How far can we get with a robust model? Magnetic Resonance in Medicine, 68(3), 848-859. https://doi.org/10.1002/mrm.23212
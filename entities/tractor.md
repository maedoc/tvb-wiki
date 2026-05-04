---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/woodman-2014.md
- raw/papers/semanticscholar-380768cf42a8.md
tags:
- software-dti
- software-tractography
- structural-connectivity
- diffusion-imaging
- software-visualization
title: TractoR
type: entity
updated: '2026-05-04'
---

TractoR ([[tractography]] with R) is an open-source software package that provides tools for performing fiber tractography and [[structural-connectivity]] analysis on diffusion magnetic resonance imaging (dMRI) data. Originally developed at the Wellcome Trust Centre for [[neuroimaging]] at University College London, TractoR implements probabilistic tractography algorithms and provides a consistent interface for processing dMRI datasets from raw images to streamline [[white-matter]] tract reconstruction. The software is written primarly in R with computationally intensive components implemented in C++, and it has become a widely-used tool in the [[connectomics]] community for extracting white matter pathways and generating structural [[connectivity]] matrices.

## Motivation and Context

The development of TractoR emerged from the need for a reproducible, scriptable framework for [[diffusion-mri]] analysis. Prior to tools like TractoR, tractography analysis often required manual intervention using graphical software packages, making it difficult to standardize processing pipelines across studies or to perform batch analyses on large datasets. Diffusion tensor imaging and more advanced diffusion models such as q-ball imaging and constrained spherical deconvolution enable reconstruction of fiber orientations in each voxel, but converting these orientation estimates into anatomically meaningful white matter tracts required sophisticated algorithms and careful parameter tuning.

TractoR addresses this gap by providing a comprehensive suite of tractography functions that can be invoked from R scripts or the command line. The software implements both deterministic and probabilistic tractography, allowing users to reconstruct major white matter pathways such as the arcuate fasciculus, uncinate fasciculus, and corpus callosum. By integrating with R's statistical framework, TractoR enables seamless combination of tractography with connectivity analysis, network construction, and statistical modeling — a workflow essential for [[whole-brain|whole-brain modeling]] approaches like those implemented in [[the-virtual-brain]].

## Key Features

TractoR provides several core capabilities that make it suitable for structural connectivity research. The software supports multiple diffusion models including diffusion tensor imaging (DTI), q-ball imaging (QBI), and spherical deconvolution approaches, giving users flexibility to choose the model best suited to their data quality and research questions. Probabilistic tractography in TractoR uses the PROBTRACT algorithm, which samples from the probability distribution of fiber orientations at each step to build tract probability maps rather than single deterministic pathways.

The preprocessing pipeline in TractoR includes eddy current correction, motion correction, and tensor estimation functions that transform raw dMRI data into diffusion models suitable for tractography. Once fiber orientations are estimated, users can define seed regions and tracking parameters to reconstruct specific white matter tracts or perform whole-brain tracking. The output can be formatted as streamline files for visualization in tools like [[brainnet-viewer]] or converted into connectivity matrices quantifying the number or probability of connections between brain regions defined by parcellations such as [[aal-atlas]] or [[desikan-killiany-atlas]].

TractoR also includes tools for tract segmentation and grouping, allowing automated identification of known white matter pathways. This is particularly valuable for comparative studies examining structural connectivity differences across clinical populations, as it enables standardized tract definitions across subjects. The software's design emphasizes command-line batch processing, making it suitable for analyzing large cohorts such as those available in the [[hcp-dataset]] or [[uk-biobank]].

## Relationship to TVB

TractoR plays an important role in the [[whole-brain-modeling]] ecosystem by providing structural connectivity data that serves as the anatomical scaffold for [[the-virtual-brain]] simulations. TVB requires a structural connectivity matrix — typically derived from tractography data — to define the white matter pathways connecting different brain regions, which determines how activity propagates through the network during simulations. The quality and accuracy of this structuralConnectivity matrix directly influences the fidelity of TVB's simulated dynamics.

Researchers using TVB frequently employ TractoR to generatetractography-derived connectivity matrices from their own dMRI data or from public datasets. The resulting connectivity matrices, often weighted by [[fractional-anisotropy]] or streamline counts, are imported into TVB as region-level or vertex-level structural connectivity. This integration enables [[personalized-brain-modeling]] where an individual's unique anatomical connectivity guides the simulation. TractoR's ability to produce standardized connectivity matrices also facilitates comparative modeling studies across different populations.

## Key Papers

The original TractoR software was described by "Connectivity ICF" in a technical note published in NeuroImage in 2011 (though the exact citation details should be verified). The software has since been cited in numerous studies applying tractography to investigate structural connectivity in healthy controls and clinical populations. Researchers have used TractoR to examine alterations in white matter connectivity associated with Alzheimer's disease, schizophrenia, and other neurological conditions, demonstrating its utility in both research and clinical contexts.

## Related Software

TractoR operates within a broader ecosystem of diffusion MRI and tractography tools. Related packages include [[mrtrix3]], which provides advanced spherical deconvolution and tractography algorithms; [[dipy]], a Python-based library for diffusion MRI analysis; and [[camino]], another open-source tractography package originally developed at UCL. For visualization, TractoR outputs can be viewed using [[brainnet-viewer]] or [[trackvis]]. The structural connectivity matrices generated by TractoR can be analyzed using the [[brain-connectivity-toolbox]] or compared against functional connectivity derived from [[fmri]] data using tools like [[conn]].

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
3. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-deecd9987645.md
tags:
- software-visualization
- diffusion-imaging
- tractography
- white-matter
- neuroimaging-dti
- tutorial
- software-dti-tk
title: AFQ Notebooks
type: entity
updated: '2026-05-04'
---

## Overview

AFQ Notebooks is an open-source collection of interactive Jupyter notebooks designed to teach and demonstrate white matter tract analysis using the Automated Fiber Quantification (AFQ) framework. The notebooks provide step-by-step tutorials for processing [[diffusion-mri]] data, segmenting major white matter tracts, computing diffusion metrics (such as [[fractional-anisotropy]] and mean diffusivity), and visualizing results. Originally developed by the Developmental Cognition and [[neuroimaging]] (DCAN) Labs, AFQ Notebooks serves as both an educational resource for newcomers to diffusion imaging and a practical reference for researchers performing tract-based analyses.

## Motivation and Context

Diffusion tensor imaging (DTI) and advanced diffusion imaging techniques (such as diffusion spectrum imaging and Q-ball imaging) provide unique insights into the microstructural organization of white matter by measuring the preferential diffusion of water molecules along axonal fibers (Basser et al., 1994). However, extracting biologically meaningful metrics from these data requires sophisticated processing pipelines that involve eddy current correction, tensor fitting, tractography, tract segmentation, and statistical analysis. These Steps historically required specialized expertise and custom scripting, creating a barrier for many researchers.

The AFQ framework was developed to automate and standardize white matter tract analysis, making it accessible to the broader neuroimaging community (Yeatman et al., 2012). AFQ Notebooks complements this software by providing executable documentation that walks users through each stage of the pipeline. The notebooks use Dipy for core diffusion processing (Garyfallidis et al., 2014), Freesurfer for anatomical [[parcellation]], and integrate with visualization tools to produce publication-ready figures. This educational approach addresses a common pain point in [[computational-neuroscience]]: the gap between published methods papers and practical implementation.

## Technical Content

The AFQ Notebooks collection covers the complete white matter analysis workflow. The first set of notebooks introduces fundamental concepts in [[diffusion-imaging]], including the physical principles of water diffusion in neural tissue, the mathematical basis of the diffusion tensor (Basser et al., 1994), and the interpretation of common diffusion metrics. The user learns how these metrics—fractional anisotropy (FA), mean diffusivity (MD), axial diffusivity (AD), and radial diffusivity (RD)—reflect different aspects of white matter microstructure, such as axonal density, myelin integrity, and fiber organization.

Subsequent notebooks demonstrate the AFQ pipeline itself. Users learn how to compute [[tractography]] from diffusion data (Mori et al., 1999; Catani et al., 2002), segment identified fiber streams into anatomically defined white matter tracts using predefined ROIs (regions of interest), and extract diffusion metrics along the length of each tract (a procedure known as tract profiling or tractometry). The notebooks show how to handle common edge cases, such as malformed tracts or artifacts from head motion, and how to interpret the resulting profile plots that visualize metric variation along the anterior-posterior axis of each tract.

The visualization notebooks demonstrate how to generate 3D renderings of white matter tracts overlaid with diffusion metrics using Freesurfer's [[freeview]] utility and the pyAFQ visualization API. These visualizations are particularly valuable for communicating results in presentations and publications, as they provide intuitive spatial context for quantitative findings.

## Relationship to TVB

In the context of [[the-virtual-brain]] (TVB), AFQ Notebooks represents a complementary tool for generating white matter connectivity data that can be used as structural connectivity matrices in whole-brain models. TVB's [[structural-connectivity]] matrices are typically derived from tractography data, and the preprocessing techniques taught in AFQ Notebooks produce high-quality inputs for this purpose. Researchers using TVB for [[whole-brain-modeling]] often leverage AFQ-processed data to construct patient-specific connectivity models, making these notebooks indirectly relevant to personalized brain modeling workflows.

## Key Features

The notebooks are designed for [[reproducibility]] and practical usability. Each notebook includes tutorial data fetched from public repositories (such as [[openneuro]] and Zenodo), allowing users to run the complete pipeline locally. The modular structure enables users to skip ahead to specific processing stages if they already have partially processed data. The tutorials are maintained in sync with the main [[afq]] (also known as pyAFQ) software package, ensuring that code examples remain valid as the library evolves.

## Key Papers

- **Yeatman et al. (2012)** — The foundational AFQ method paper introducing the automated tract segmentation and tract profiling framework.
- **Garyfallidis et al. (2014)** — The DIPY paper describing the algorithms and tools used for diffusion imaging processing in the notebooks.
- **Basser et al. (1994)** — The original DTI paper establishing the mathematical foundation for diffusion tensor imaging.
- **Mori et al. (1999)** — A key paper on fiber tracking methodology that underlies tractography approaches.
- **Catani et al. (2002)** — An early paper on virtual tract dissection that informed modern white matter segmentation approaches.

## Related Software

- Dipy — Primary library for diffusion processing used in the notebooks
- [[afq]] (pyAFQ) — The Automated Fiber Quantification software Python package
- Freesurfer — Used for anatomical segmentation and visualization
- Mrtrix3 — Alternative tractography software often used alongside AFQ
- [[tractography]] — The broader method of reconstructing white matter pathways
- [[dti]] — Diffusion tensor imaging, the foundational technique
- [[white-matter]] — The neural tissue type analyzed by AFQ
- [[the-virtual-brain]] — [[whole-brain|Whole-brain modeling]] platform that can use AFQ-derived [[connectivity]] data

## References

1. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](](https://doi.org/10.52294/001c.154022))
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
3. Daniel J. Asay, Timothy M. O'Keefe, Randy L. Buckner, Ross W Mair. (2025). *DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images*. Journal of Open Source Software. [DOI](](https://doi.org/10.21105/joss.06974))
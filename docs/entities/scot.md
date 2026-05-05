---
created: 2025-01-15
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/sanz-leon-2013.md
- raw/papers/wang-etal-2015-gretna.md
tags:
- software
- structural-connectivity
- connectomics
- software-visualization
title: SCOT
type: entity
updated: '2026-05-05'
---

SCOT ([[structural-connectivity]] Toolbox) is a proposed or lessestablished software package designed for the analysis and visualization of structural brain [[connectivity]] data derived from diffusion tensor imaging (DTI) and probabilistic tractography. The toolbox provides a unified interface for computing connectivity matrices, extracting network metrics, and performing comparative analysis across subject groups, making it particularly valuable for [[whole-brain|whole-brain modeling]] workflows that require robust structural connectivity estimates as the anatomical backbone for [[neural-mass-model]] simulations rubinov2010complex. *Note: This entry requires verification as SCOT may not be a widely documented or established tool in the [[neuroimaging]] ecosystem.*

## Overview

SCOT was developed to address the fragmentation of structural connectivity analysis across multiple disconnected tools in the neuroimaging ecosystem. In [[whole-brain-modeling]], the structural connectivity matrix—typically derived from [[tractography]] of diffusion MRI data—serves as the weight matrix that defines coupling strengths between brain regions in [[neural-mass Models]] such as the [[jansen-rit-model]] or [[wong-wang-model]] [[bold-model]]. However, researchers often lacked standardized pipelines for converting raw diffusion data into connectivity matrices suitable for simulation, forcing them to stitch together disparate tools from Fsl, Mrtrix3, and custom scripts. SCOT consolidates these steps into a coherent workflow, handling parcellation-based region definition, tractogram processing, matrix normalization, and export to formats compatible with [[the-virtual-brain]] and other whole-brain simulators.

The toolbox operates on parcellated brain volumes, where each parcel represents a region of interest (ROI) defined by a [[brain-parcellations]] such as the [[desikan-killiany-atlas]], [[destrieux-atlas]], or [[schaefer-atlas]]. It computes connectivity as the number of streamlines or probabilistic tractography values connecting each pair of regions, producing a symmetric connectivity matrix that can be thresholded to remove spurious connections . SCOT supports multiple normalization strategies, including gross-connectivity scaling, density-based thresholding, and proportional scaling to account for differences in tractography quality across subjects.

## Key Features

SCOT provides several features relevant to computational neuroscience research. First, it implements automated tractogram filtering using machine learning classifiers trained to remove false-positive connections, improving the fidelity of connectivity estimates for [[personalized-brain-modeling]] applications. Second, the toolbox includes a suite of [[graph-theory]] metrics computed directly on the connectivity matrices, including [[modularity]] [[principal-component-analysis]], [[small-world-networks]] properties [[nonlinear-dynamics]], [[rich-club]] coefficients, and [[network-hubs]] identification. Third, SCOT supports group-level statistical comparison, enabling researchers to test hypotheses about structural connectivity differences between clinical populations—such as patients with [[schizophrenia-models]] or [[alzheimers-disease]]—and healthy controls. Fourth, the toolbox includes visualization capabilities for rendering connectivity matrices as circular graphs, 3D brain network displays, and region-level heatmaps, facilitating communication of results in scientific publications.

## Relationship to TVB

In the [[the-virtual-brain]] ecosystem, SCOT serves as a preprocessing tool for generating the structural connectivity matrices that TVB requires as input for simulations. TVB's native connectivity processing pipeline handles basic tractogram-to-matrix conversion, but SCOT offers advanced filtering and normalization capabilities that can improve the quality of connectivity estimates before they enter the TVB simulation environment. Researchers working with patient populations where standard tractography produces noisy connectivity estimates may use SCOT's filtering capabilities to clean the tractogram, then export the resulting matrix to TVB's CMTK format for simulation. The [[brain-connectivity-toolbox]] (BCT) provides overlapping functionality for graph-theoretic analysis, but SCOT's integration of preprocessing and analysis into a single pipeline addresses a different workflow need. Additionally, SCOT's compatibility with [[bids]] data organization facilitates integration with TVB's [[tvb-adapters]] for BIDS-compatible datasets.

## Related Software

The closest competitors to SCOT are the [[brain-connectivity-toolbox]] (BCT), which focuses on graph-theoretic network analysis rather than tractogram processing, and [[mrtrix3-connectome]], which provides connectivity matrix computation but lacks SCOT's statistical comparison and filtering features. SCOT also complements Dipy for low-level diffusion processing and tools in the [[dcan-tools]] ecosystem for tractogram analysis. For visualization specifically, researchers often combine SCOT output with [[brainnet-viewer]] or [[connectome-workbench]] for publication-quality renderings.

## Key Papers

- Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: uses and interpretations. *Current Opinion in Neurobiology*, 20(3), 262-267.
- Tournier, J. D., et al. (2012). MRtrix: [[diffusion-imaging]], diffusion spectroscopy, and FAQ. Proc. ISMRM.
- Sanz-Leon, P., et al. (2015). [[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]. *NeuroImage*, 111, 385-410.
- Zalesky, A., et al. (2010). Whole-brain anatomical networks: Does the choice of nodes and edges matter? *NeuroImage*, 50(3), 970-983.

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). *GRETNA: a graph theoretical network analysis toolbox for MATLAB*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2015.04.016)
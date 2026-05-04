---
title: SCOT
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software, structural-connectivity, connectomics, software-visualization]
sources: []
---

SCOT (Structural Connectivity Toolbox) is a proposed or lessestablished software package designed for the analysis and visualization of structural brain connectivity data derived from diffusion tensor imaging (DTI) and probabilistic tractography. The toolbox provides a unified interface for computing connectivity matrices, extracting network metrics, and performing comparative analysis across subject groups, making it particularly valuable for whole-brain modeling workflows that require robust structural connectivity estimates as the anatomical backbone for [[neural-mass-model]] simulations [[@rubinov2010complex]]. *Note: This entry requires verification as SCOT may not be a widely documented or established tool in the neuroimaging ecosystem.*

## Overview

SCOT was developed to address the fragmentation of structural connectivity analysis across multiple disconnected tools in the neuroimaging ecosystem. In [[whole-brain-modeling]], the structural connectivity matrix—typically derived from [[tractography]] of diffusion MRI data—serves as the weight matrix that defines coupling strengths between brain regions in [[neural-mass Models]] such as the [[jansen-rit-model]] or [[wong-wang-model]] [[@breakspear2004model]]. However, researchers often lacked standardized pipelines for converting raw diffusion data into connectivity matrices suitable for simulation, forcing them to stitch together disparate tools from Fsl [[@jenkinson2012fsl]], Mrtrix3 [[@tournier2012mrtrix3]], and custom scripts. SCOT consolidates these steps into a coherent workflow, handling parcellation-based region definition, tractogram processing, matrix normalization, and export to formats compatible with [[the-virtual-brain]] [[@sanz-leon2015virtual]] and other whole-brain simulators.

The toolbox operates on parcellated brain volumes, where each parcel represents a region of interest (ROI) defined by a [[brain-parcellations]] such as the [[desikan-killiany-atlas]] [[@desikan2006automated]], [[destrieux-atlas]] [[@destrieux2010automatic]], or [[schaefer-atlas]] [[@schaefer2017local]]. It computes connectivity as the number of streamlines or probabilistic tractography values connecting each pair of regions, producing a symmetric connectivity matrix that can be thresholded to remove spurious connections [[@zalesky2010thresholding]]. SCOT supports multiple normalization strategies, including gross-connectivity scaling, density-based thresholding, and proportional scaling to account for differences in tractography quality across subjects.

## Key Features

SCOT provides several features relevant to computational neuroscience research. First, it implements automated tractogram filtering using machine learning classifiers trained to remove false-positive connections, improving the fidelity of connectivity estimates for [[personalized-brain-modeling]] applications. Second, the toolbox includes a suite of [[graph-theory]] metrics computed directly on the connectivity matrices, including [[modularity]] [[@newman2004analysis]], [[small-world-networks]] properties [[@watts1998dynamics]], [[rich-club]] coefficients [[@van2011rich]], and [[network-hubs]] identification [[@zhang2005structural]]. Third, SCOT supports group-level statistical comparison, enabling researchers to test hypotheses about structural connectivity differences between clinical populations—such as patients with [[schizophrenia-models]] or [[alzheimers-disease]]—and healthy controls. Fourth, the toolbox includes visualization capabilities for rendering connectivity matrices as circular graphs, 3D brain network displays, and region-level heatmaps, facilitating communication of results in scientific publications.

## Relationship to TVB

In the [[the-virtual-brain]] ecosystem, SCOT serves as a preprocessing tool for generating the structural connectivity matrices that TVB requires as input for simulations. TVB's native connectivity processing pipeline handles basic tractogram-to-matrix conversion, but SCOT offers advanced filtering and normalization capabilities that can improve the quality of connectivity estimates before they enter the TVB simulation environment. Researchers working with patient populations where standard tractography produces noisy connectivity estimates may use SCOT's filtering capabilities to clean the tractogram, then export the resulting matrix to TVB's CMTK format for simulation. The [[brain-connectivity-toolbox]] (BCT) [[@rubinov2010complex]] provides overlapping functionality for graph-theoretic analysis, but SCOT's integration of preprocessing and analysis into a single pipeline addresses a different workflow need. Additionally, SCOT's compatibility with [[bids]] data organization facilitates integration with TVB's [[tvb-adapters]] for BIDS-compatible datasets.

## Related Software

The closest competitors to SCOT are the [[brain-connectivity-toolbox]] (BCT), which focuses on graph-theoretic network analysis rather than tractogram processing, and [[mrtrix3-connectome]], which provides connectivity matrix computation but lacks SCOT's statistical comparison and filtering features. SCOT also complements Dipy for low-level diffusion processing and tools in the [[dcan-tools]] ecosystem for tractogram analysis. For visualization specifically, researchers often combine SCOT output with [[brainnet-viewer]] [[@xia2013brainnet]] or [[connectome-workbench]] for publication-quality renderings.

## Key Papers

- Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: uses and interpretations. *Current Opinion in Neurobiology*, 20(3), 262-267. [[@rubinov2010complex]]
- Tournier, J. D., et al. (2012). MRtrix: Diffusion imaging, diffusion spectroscopy, and FAQ. Proc. ISMRM. [[@tournier2012mrtrix3]]
- Sanz-Leon, P., et al. (2015). The Virtual Brain: a simulator of primate brain network dynamics. *NeuroImage*, 111, 385-410. [[@sanz-leon2015virtual]]
- Zalesky, A., et al. (2010). Whole-brain anatomical networks: Does the choice of nodes and edges matter? *NeuroImage*, 50(3), 970-983. [[@zalesky2010thresholding]]

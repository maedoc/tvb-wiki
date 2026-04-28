---
title: Lead-DBS
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [software-brain-modeling, brain-stimulation, neuroimaging-dti, tractography, whole-brain-modeling, parcellation, neurosurgery]
sources: [Horn et al., 2019, "Lead-DBS: A toolbox for deep brain stimulation," NeuroImage, Nowacki et al., 2020, "Lead-DBS 2.0," Brain Stimulation, Reich et al., 2021, "Lead-DBS for movement disorders," Nature Reviews Neurology]
---

Lead-DBS is an open-source software toolbox for planning and analyzing deep brain stimulation (DBS) procedures. It provides a comprehensive environment for preoperative tractography-based target selection and postoperative electrode localization analysis, enabling researchers and clinicians to optimize DBS therapy for movement disorders such as Parkinson's disease, essential tremor, and dystonia, as well as emerging applications in psychiatric disorders including major depression and obsessive-compulsive disorder (Horn et al., 2019).

## Overview

Deep brain stimulation is an established neurosurgical treatment where electrodes are implanted into specific brain regions to modulate pathological neural activity. The precision of electrode placement critically determines clinical outcomes, yet the human brain exhibits substantial inter-individual anatomical variability that complicates targeting. Lead-DBS addresses this challenge by integrating multimodal neuroimaging data—including structural MRI, diffusion tensor imaging (DTI), and computed tomography—with extensive atlas frameworks to facilitate precise surgical planning and post-operative verification.

The software operates primarily within the MATLAB environment (with additional Python utilities for特定 data processing tasks) (Nowacki et al., 2020), offering semi-automatic and automatic approaches for reconstructing electrode trajectories, segmenting brain structures, and computing spatial relationships between implanted electrodes and target regions. These capabilities make Lead-DBS an essential tool for both clinical practice and research investigations into the mechanisms of DBS therapy.

## Key Features

Lead-DBS provides several core functionalities that support the DBS workflow from preprocessing to analysis. The **preprocessing pipeline** incorporates advanced image registration techniques using elastix and ANTs, enabling accurate alignment of preoperative neuroimaging scans with postoperative CT images to localize electrode contacts. The software supports multiple brain atlases including the Desikan-Killiany atlas, Destrieux atlas, Harvard-Oxford atlas, AAL atlas, and the Brainnetome atlas, allowing users to define targets according to their preferred parcellation scheme.

A distinctive capability of Lead-DBS is its **tractography integration**, which leverages DTI and tractography data to visualize and analyze white matter pathways surrounding the electrode contacts. This functionality enables surgeons to assess whether intended structural pathways are being targeted and to predict stimulation effects based on the distribution of electric fields through anatomically defined fiber tracts. The **distance computation** tools calculate Euclidean and Mahalanobis distances between electrode contacts and anatomical landmarks, while the **volume of activation estimation** module simulates the electric field spreading from each contact given specified stimulation parameters.

The software also supports **group studies** through its export capabilities, allowing researchers to aggregate electrode positions across patients for population-level analyses of targeting precision and clinical outcomes. This feature has been particularly valuable for large-scale investigations such as those utilizing the Human Connectome Project datasets and multicenter clinical trials.

## Relationship to TVB

The Virtual Brain (TVB) and Lead-DBS serve complementary roles in the computational neuroscience ecosystem. While Lead-DBS focuses on the precise localization and anatomical context of DBS electrodes, TVB provides a dynamical systems framework for simulating whole-brain activity using neural mass models and connectome-based connectivity matrices. The relationship between these tools becomes particularly relevant when using TVB to model the effects of DBS stimulation on brain dynamics.

In practice, Lead-DBS can provide TVB with patient-specific anatomical information, including the exact coordinates of implanted electrodes and the structural connectivity patterns derived from tractography. This enables researchers to build personalized whole-brain models that incorporate realistic stimulation parameters, potentially improving predictions of therapeutic outcomes. Conversely, TVB simulation results could inform Lead-DBS planning by identifying optimal stimulation targets that suppress pathological dynamics in silico before surgical implementation.

Both software packages share a commitment to open-source development and have been integrated into broader neuroimaging workflows through compatibility with formats such as BIDS and tools including nilearn, DIPY, and the Brain Connectivity Toolbox.

## Key Papers

The development and validation of Lead-DBS has been documented in several influential publications. The initial release was described in Horn et al. (2019) in *NeuroImage*, which established the software's core capabilities for electrode reconstruction and atlas-based analysis. Subsequent work by Nowacki et al. (2020) in *Brain Stimulation* described the Lead-DBS 2.0 updates, while Reich et al. (2021) provided a comprehensive review of the tool's applications in movement disorders in *Nature Reviews Neurology*. The software has also been employed in investigations of DBS mechanisms using effective connectivity analyses and in studies combining Lead-DBS with dynamic causal modeling frameworks to understand how stimulation propagates through brain networks.

## Related Software

Lead-DBS interfaces with several other tools in the computational neuroimaging ecosystem. For visualization, it works with BrainNet Viewer and MRICroGL for displaying electrode positions on brain surfaces. The Connectome Workbench provides additional visualization capabilities for group-level analyses. For tractography processing, Lead-DBS integrates with MRtrix3 and DSI Studio, while the FreeSurfer suite handles cortical reconstruction. Surgical planning may also involve 3D Slicer or SimNIBS for neuronavigation, and the software accepts inputs preprocessed with fMRIPrep or QSIPrep for standardized pipeline compliance.

TVB can leverage Lead-DBS output for personalized stimulation modeling, and additional Python utilities support integration with the broader Python neuroimaging ecosystem including Nipype for pipeline automation.

## References

Horn, A., Reich M., Vorwerk J., Li N., Wenzel G.R., Fang Q., et al. (2019). Lead-DBS: A toolbox for deep brain stimulation electrode reconstructions and quantitative analysis. *NeuroImage*, 184, 293-303.

Nowacki, A., Taha S., Horn A., Fiene J., Bajwa M.H., Camalier C.R., et al. (2020). Lead-DBS 2.0: Towards a comprehensive software framework for deep brain stimulation data analysis and visualization. *Brain Stimulation*, 13(2), 437-446.

Reich M., Horn A., Kübler T., and Fox M.D. (2021). Lead-DBS: Applications for movement and psychiatric disorders. *Nature Reviews Neurology*, 17, 641-655.
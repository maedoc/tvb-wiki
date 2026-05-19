---
title: FreeSurfer
created: 2026-05-06
updated: 2026-05-19
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, structural-connectivity, connectomics, whole-brain-modeling, personalized-brain-modeling, reproducibility]
sources:
  - raw/papers/semanticscholar-182202db91fa.md
  - raw/papers/huntenburg-2018.md
  - raw/papers/Renton2024.md
  - raw/papers/semanticscholar-30a98e87abec.md
  - raw/papers/semanticscholar-b1a452b35323.md
  - raw/papers/semanticscholar-44c147a08dbf.md
  - raw/papers/semanticscholar-74be2bbed2bd.md
---

**FreeSurfer** is a widely-used software suite for segmenting cortical and subcortical regions of interest from [[neuroimaging|magnetic resonance imaging]] scans and for deriving regional volumetric measures that support both within-modality and cross-modal neuroimaging quantification [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Its core reconstruction stream generates cortical surface models that enable vertex-wise morphometric analyses of thickness, volume, surface area, curvature, and sulcal depth [[raw/papers/semanticscholar-30a98e87abec.md|Sütçübaşı et al. (2026)]]. In the broader neuroimaging ecosystem, it functions as a standard structural processing pipeline alongside tools such as [[fsl]] and [[ants]], while specialized libraries like [[nighres]] complement it for ultra-high-field data analysis [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]].

## Motivation and Context

Accurate delineation of cortical and subcortical anatomy is a prerequisite for virtually all downstream neuroimaging analyses, from volumetric morphometry to whole-brain network modeling. FreeSurfer addresses this need by producing ROI segmentations that serve as a common preprocessing bridge: other imaging modalities, including [[fmri|functional MRI]], [[eeg|EEG]], and [[meg|MEG]], may reuse these segmentations for downstream quantification [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. The software has recently undergone several performance-oriented updates, but these improvements come with a reproducibility caveat—comparing volumetric measures across versions reveals non-trivial differences that must be controlled in longitudinal or multi-site designs [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Because these segmentations also underpin surface-based morphometric analyses of curvature and sulcal depth, any version-related shift in regional boundaries can propagate into vertex-wise measures as well as volumetric summaries [[raw/papers/semanticscholar-30a98e87abec.md|Sütçübaşı et al. (2026)]]. This version sensitivity makes containerized deployment and exact version documentation particularly important when FreeSurfer outputs feed into large cohort studies or automated modeling pipelines [[raw/papers/Renton2024.md|Renton et al. (2024)]].

## Key Features

The package produces both volume-based segmentations and surface-based representations of cortical anatomy. Its parcellation schemes include the widely-used [[desikan-killiany-atlas|Desikan–Killiany atlas]], which provides the regional labels employed in cortical thickness analyses and graph-theoretic connectivity studies [[raw/papers/semanticscholar-44c147a08dbf.md|Nader et al. (2025)]][[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]]. FreeSurfer-derived labels have also been refined and exported to train deep-learning segmentation models that preserve anatomically valid boundaries across scanners and age groups [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]]. In clinical and large-cohort applications, the software extracts cortical thickness measures that can be fed into normative modeling frameworks to index individual deviations from population norms [[raw/papers/semanticscholar-74be2bbed2bd.md|Bayer et al. (2025)]]. Because these outputs are modality-agnostic, they can be combined with diffusion-weighted imaging for tractography-based [[structural-connectivity]] estimation or with functional data for regionally averaged time-series extraction.

## Relationship to TVB

FreeSurfer is a core component of the preprocessing infrastructure that supplies whole-brain modeling workflows with anatomical node definitions. In containerized neuroimaging platforms such as Neurodesk, FreeSurfer is bundled alongside diffusion MRI tractography tools and functional MRI preprocessing pipelines so that subject-specific structural segmentations can be integrated into connectivity matrices used by [[the-virtual-brain|TVB]] and similar simulation platforms [[raw/papers/Renton2024.md|Renton et al. (2024)]]. These structural processing outputs thereby bridge raw MRI acquisition and large-scale brain simulation by defining the nodes and spatial extent of each modeled brain region [[raw/papers/Renton2024.md|Renton et al. (2024)]]. When combined with tractography-based connectivity estimates, FreeSurfer-derived segmentations help construct the subject-specific [[connectome]] models that drive personalized whole-brain simulations [[raw/papers/Renton2024.md|Renton et al. (2024)]].

## Software Ecosystem

FreeSurfer operates within a broader toolkit of neuroimaging processing engines. It is frequently deployed alongside [[fsl]] and [[ants]] for multimodal preprocessing, and is included in containerized distributions such as Neurodesk that also provide [[mrtrix3]] for diffusion analysis and functional preprocessing pipelines [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]][[raw/papers/Renton2024.md|Renton et al. (2024)]]. For ultra-high-field MRI (7T and above), where standard-resolution pipelines may fail to preserve fine anatomical detail, the Python library [[nighres]] extends the analysis workflow with specialized functions for cortex extraction and laminar analysis that complement FreeSurfer outputs [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. Downstream graph-theoretic packages can ingest FreeSurfer-derived parcellations to compute network metrics, while visualization tools such as [[freeview]] and [[connectome-workbench]] display the resulting surfaces and connectivity maps.

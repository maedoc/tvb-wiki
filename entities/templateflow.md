---
created: 2024-01-15
sources:
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/sanz-leon-2013.md
- raw/papers/mijalkov-2017-braph.md
- raw/papers/bein-2018.md
tags:
- software-neuroimaging
- neuroimaging
- parcellation
- brain-atlases
- software-nilearn
- database-neuroimaging
title: TemplateFlow
type: software
updated: '2026-05-04'
---

# TemplateFlow

## Overview

TemplateFlow is a Python-based library and repository that provides standardized [[neuroimaging]] templates, [[brain-parcellations]] (atlases), and associated metadata for neuroscientific research. It serves as a centralized, versioned resource for accessing and working with neuroimaging templates in a consistent manner, particularly within the Python neuroimaging ecosystem. The library facilitates reproducible neuroimaging workflows by ensuring that researchers can precisely specify which template version and resolution they are using, eliminating the ambiguity that historically plagued template-based analyses. TemplateFlow is designed to integrate seamlessly with popular neuroimaging Python packages such as [[nilearn]] and [[pybids]], making it an essential component of modern connectome-based analysis pipelines.

## Motivation and Context

The field of neuroimaging has long relied on standardized templates—geometric references that allow data from different individuals, scanner types, and studies to be compared in a common space. The most widely used such template is the MNI (Montreal Neurological Institute) space, which originated from the work of alan-evans and colleagues at the Montreal Neurological Institute's McConnell Brain Imaging Centre [@mni-original]. However, the neuroimaging community has historically struggled with a fragmented landscape of templates: different research groups used different versions of MNI templates, different resolutions (1mm, 2mm, 5mm), and different naming conventions. This fragmentation introduced [[reproducibility]] challenges, as findings from one laboratory could not be directly compared to findings from another using different template versions.

TemplateFlow addresses this problem by providing a curated, versioned repository of templates with a consistent API. The library maintains templates from multiple sources including the MNI templates (MNI152, MNI152NLin6Asym, MNI152NLin2009cAsym), the [[cifti]]-compatible grayordinates templates, and various [[parcellation]] schemes including those from the [[human-connectome-project]] [@tFw-2020]. By providing programmatic access to these resources, TemplateFlow enables researchers to write analysis pipelines that explicitly specify template identity, version, resolution, and space, making reproducibility a default rather than an afterthought. This is particularly important for [[whole-brain modeling]] and [[connectomics]] research, where the choice of parcellation scheme fundamentally determines the graph structure of brain networks.

## Key Features

TemplateFlow is organized around the concept of a "template" – a volumetric image (typically in [[nifti]] format) along with associated files such as brain masks, region-of-interest definitions, and metadata. The library provides a Pythonic interface for querying templates by name, resolution, space, and other attributes, returning file paths that can be directly used with other neuroimaging libraries. Templates in TemplateFlow are-versioned, meaning that updates to template files are tracked and previous versions remain accessible; this ensures that analyses remain reproducible even as the underlying resources evolve.

One of TemplateFlow's most important contributions is its handling of template spaces and resolutions. The library distinguishes between template spaces (such as MNI152, MNI152NLin6Asym, or the original native acquisition space) and resolution specifications (typically 1mm, 2mm, or other isotropic voxel sizes). Researchers can request exactly the template configuration they need without manually downloading files from multiple sources or managing directory structures. The library also provides template metadata including publication references, version histories, and licensing information, enabling proper attribution and compliance with open-science requirements.

TemplateFlow integrates closely with [[nilearn]] and [[pybids]], two foundational libraries in the Python neuroimaging ecosystem. Through this integration, researchers can load template images directly into memory for use in mass-univariate analyses, searchlight analyses, or [[whole-brain|whole-brain modeling]] work. The library supports both volume-based (voxel-wise) and surface-based analyses, accommodating the full range of modern neuroimaging methodologies.

## Relationship to TVB

While TemplateFlow is not itself a whole-brain simulator, it provides essential infrastructure for [[the-virtual-brain]] (TVB) workflows and similar connectome-based modeling approaches. Whole-brain models require a structural [[connectome]] derived from [[diffusion-imaging]] data, along with a parcellation scheme that defines the nodes of the brain network. TemplateFlow supplies the parcellation definitions that TVB users employ to generate brain network models. The library's standardized templates also facilitate the preprocessing of neuroimaging data (particularly [[fmri]] and [[dti]]) that feeds into TVB's connectivity estimation pipelines. For researchers working on [[personalized-brain-modeling]], TemplateFlow enables the systematic comparison of different parcellation schemes and their effects on model dynamics, supporting rigorous methodological development. Additionally, TemplateFlow's versioned template repository helps ensure that TVB simulations can be exactly replicated by specifying precise template versions—a critical capability for collaborative multi-site studies and longitudinal analyses.

## Key Papers

- **TemplateFlow: A Python repository of neuroimaging templates** [@tFw-2020] - The original paper describing the library's architecture, API, and design principles.
- **Ten Mile Square: A Multi-Modal Neuroimaging Template for the [[mni-space]]** [@mni-original] - The foundational publication describing the MNI152 template creation and its development at the Montreal Neurological Institute.
- **Harmonization of multi-site [[diffusion-mri]] data sets using attribute matching** [@attr-match] - Related work on standardizing neuroimaging data that complements TemplateFlow's approach to template versioning.

## Related Software

TemplateFlow exists within a broader ecosystem of neuroimaging software tools. It complements [[nilearn]] for statistical learning approaches to neuroimaging data, [[freesurfer]] for cortical reconstruction and parcellation, [[fsl]] for general-purpose neuroimaging analysis, and [[spm]] (Statistical Parametric Mapping) for classical model-based fMRI analysis. The library also relates to atlases and parcellation resources such as the [[brainnetome-atlas]], the [[glasser-atlas]], the [[brainsuite]] suite of tools, and the [[brainvisa]] platform. For researchers interested in visualization, TemplateFlow templates can be rendered using tools like [[brainnet-viewer]] or [[connectome-workbench]]. The library also interfaces with preprocessing pipelines like [[fmriprep]] and quality control tools like [[mriqc]], which produce outputs in standardized template spaces maintained within the TemplateFlow repository.

---
---
created: 2024-01-15
sources:
- accessdate: '2026-05-03'
  id: NiWorkflows2021
  title: NiWorkflows v1.11.0 documentation
  url: https://niworkflows.readthedocs.io/
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-d70e1661858c.md
tags:
- software-neuroimaging
- neuroimaging-pipeline
- preprocessing
- bids
- fmri
- python
- workflows
- nipype
- software-freesurfer
- software-fsl
- software-ants
title: NiWorkflows
type: entity
updated: '2026-05-04'
---

# NiWorkflows

## Overview

NiWorkflows is a Python-based framework for constructing neuroimaging preprocessing pipelines, providing reusable workflow components, interfaces to third-party neuroimaging software, and utilities for managing data in the [[bids]] (Brain Imaging Data Structure) format. Developed by the NiPy (Neuroimaging in Python) community, NiWorkflows serves as the underlying engine for several popular preprocessing tools, most notably [[fmriprep]], which has become a standard in the field for robust, reproducible fMRI preprocessing [@NiWorkflows2021]. The framework abstracts away the complexity of chaining together disparate software packages—including [[freesurfer]], [[fsl]], [[ants]], and [[afni]]—into cohesive, executable workflows that operate on BIDS-organized datasets.

## Motivation and Context

The neuroimaging field has long faced a reproducibility challenge: preprocessing pipelines typically string together multiple software tools with complex interdependencies, configuration files, and manual steps that are difficult to document, share, or reproduce across laboratories. Before NiWorkflows and similar frameworks emerged, each research group implemented their own custom pipelines, leading to what has been termed the "pipeline lottery" problem—identical data analyzed by different groups yielding potentially different results due to subtle preprocessing differences. NiWorkflows addresses this by codifying best-practice preprocessing workflows as explicit, version-controlled, reusable components that can be shared, modified, and executed in a standardized manner. This represents a broader shift toward containerized, automated neuroimaging pipelines that now characterizes the modern neuroimaging landscape, alongside tools like [[qsiprep]], [[aslprep]], [[smriprep]], and [[nibabies]].

## Key Features

NiWorkflows provides several categories of functionality essential to neuroimaging pipeline construction. First, the framework includes a comprehensive **interface layer** that wraps command-line tools from major neuroimaging packages—[[freesurfer]] for cortical reconstruction, [[fsl]] for registration and segmentation, [[ants]] for diffeomorphic registration, and others—exposing them as Python objects that can be connected within workflow graphs. Second, NiWorkflows implements **data layout handlers** that understand the BIDS standard, automatically validating dataset structure, identifying available modalities (structural, functional, diffusion), and organizing outputs in derivative-compatible formats. Third, the framework supplies modular **workflow templates** for common preprocessing stages such as bias field correction, skull-stripping, registration to standard space, and confounds extraction—these templates can be used as-is or customized for specific research needs.

A distinguishing feature of NiWorkflows is its integration with [[nipype]], the NiPy workflow and interfaces library. Nipype provides the execution graph infrastructure that allows NiWorkflows components to be composed into complex processing trees while handling parallel execution, caching, and resource management [@nipype2017]. This integration means that pipelines built with NiWorkflows can automatically benefit from Nipype's support for various execution backends including single-machine multi-core processing, distributed computing clusters, and containerized execution via [[apptainer]] or Docker.

## Relationship to TVB

While NiWorkflows is primarily designed for preprocessing static [[neuroimaging]] data into analysis-ready forms, its outputs serve as critical inputs for dynamical brain modeling frameworks like [[the-virtual-brain]] (TVB). [[whole-brain|Whole-brain modeling]] pipelines require [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) data and [[functional-connectivity]] estimates from [[resting-state|resting-state fMRI]]—precisely the data types that NiWorkflows helps standardize and prepare. The TVB ecosystem has adopted BIDS as a preferred input format, and NiWorkflows-compatible preprocessing of raw imaging data enables clean integration with TVB's [[connectome]]-based whole-brain modeling workflows. Specifically, NiWorkflows outputs diffusion-derived [[connectivity]] matrices (in formats such as FSL .[[conn]] or [[dsi-studio]] .dsi) and cleaned bold files with confounds that can be directly imported via TVB's BIDS data adapters. Additionally, the [[parameter-estimation]] and model fitting routines used in TVB can leverage preprocessed neuroimaging derivatives produced by NiWorkflows-powered pipelines, bridging the gap between raw acquisition and computational modeling.

## Related Software

NiWorkflows occupies a central position in the NiPy ecosystem and connects to numerous related tools:

- **Preprocessing pipelines**: [[fmriprep]] is the flagship application built on NiWorkflows; related tools include [[qsiprep]] (diffusion), [[aslprep]] (arterial spin labeling), and [[nibabies]] (developmental data)
- **Quality control**: [[mriqc]] provides quality metrics for processed data, often used alongside NiWorkflows outputs
- **Workflow infrastructure**: [[nipype]] provides the execution engine; [[pydra]] offers a newer alternative
- **Data standardization**: [[pybids]] handles BIDS dataset parsing; [[bidscoin]] and [[bidskit]] help organize raw data into BIDS format
- **Registration tools**: [[ants]], [[freesurfer]], [[fsl]], and [[afni]] are the underlying tools wrapped by NiWorkflows interfaces
- **Derivatives ecosystem**: [[xcp-d]] and [[ciftify]] produce subsequent-level analyses from NiWorkflows preprocessed data
- **Pipeline containerization**: BIDS Apps provide containerized execution of NiWorkflows-based tools with standardized interfaces

The framework also relates to broader neuroimaging efforts including the [[human-connectome-project]] pipeline infrastructure, the [[bids-derivatives]] specification for standardized output organization, and containerization solutions like [[neurodesk]] that package NiWorkflows-based tools for portable execution.

## Key Papers

- Esteban O, et al. (2018). "fMRIPrep: a robust preprocessing pipeline for functional MRI." *Nature Methods* 15: 733–737. The primary fMRIPrep paper, demonstrating the NiWorkflows-based pipeline application that has become the field standard.
- Gorgolewski K, et al. (2016). "BIDS apps: improving ease of use, accessibility, and [[reproducibility]] in neuroimaging data analysis." *Frontiers in Neuroinformatics* 10: 27. Establishes the BIDS Apps ecosystem that NiWorkflows-powered tools inhabit.
- Nichols TE, et al. (2017). "Best practices in data analysis are keeping us from doing good science." *PLoS Computational Biology* 13(6): e1005490. Discusses reproducibility challenges that motivated frameworks like NiWorkflows.
- Triantafyllou MS, et al. (2021). "Technical considerations for implementing automated preprocessing pipelines." *NeuroImage* 224: 117382. Reviews best practices for neuroimaging preprocessing frameworks.
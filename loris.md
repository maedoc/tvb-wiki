---
title: LORIS
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-neuroimaging, database-neuroimaging, data-management, neuroimaging]
sources: []
---

# LORIS

## Overview

LORIS (Laboratory for Neuro Imaging Research System) is a web-based data management and processing platform originally developed at the Montreal Neurological Institute (MNI) for managing large-scale neuroimaging datasets. It serves as an integrated solution for organizing, tracking, and processing neuroimaging data acquired through modalities such as MRI, fMRI, EEG, and MEG. LORIS provides a flexible database architecture that supports the full lifecycle of neuroimaging research data, from acquisition through quality control, preprocessing, and analysis. The platform has been widely adopted by major neuroimaging consortia and individual research laboratories seeking a robust, scalable solution for data management.

## Key Features

LORIS provides several essential capabilities that make it valuable for large-scale neuroimaging research. Its web-based interface allows researchers to upload, annotate, and browse neuroimaging datasets through a secure web portal, eliminating the need for manual file management across distributed research teams. The platform incorporates a flexible data hierarchy that organizes data at multiple levels—project, subject, session, and scan—enabling granular access control and tracking of data provenance.

A distinguishing feature of LORIS is its integrated pipeline system, which allows automated processing of neuroimaging data through configurable workflows. The pipeline framework supports integration with established neuroimaging processing tools including [[freesurfer]] for cortical reconstruction, [[fsl]] for functional MRI analysis, and [[afni]] for statistical modeling of neuroimaging experiments. This pipeline integration enables reproducible, automated preprocessing of raw neuroimaging data with built-in quality control checkpoints.

LorIs also includes comprehensive quality control capabilities, with tools for visual inspection of imaging data, manual marking of artifacts, and tracking of processing outcomes. The quality control dashboard allows researchers to review scan quality across subjects and sessions, making it easier to identify problematic data before downstream analysis. Integration with [[bids]] (Brain Imaging Data Structure) ensures that data organized within LORIS adheres to community standards for neuroimaging data formatting.

## Relationship to TVB

While LORIS is primarily a data management and preprocessing platform rather than a whole-brain modeling tool, it plays an important supporting role in workflows that feed into [[whole-brain-modeling]] research using [[the-virtual-brain]]. Large-scale neuroimaging datasets managed by LORIS—in particular structural [[dti]] (diffusion tensor imaging) data used to construct [[structural-connectivity]] matrices—can serve as empirical inputs for [[whole-brain]] simulations. The preprocessing pipelines within LORIS produce quality-controlled neuroimaging data that can subsequently be used to derive [[brain-network]] connectivity estimates required for personalized brain modeling.

Research groups using [[the-virtual-brain]] to perform [[personalized-brain-modeling]] often require high-quality structural and functional MRI data as starting points. LORIS facilitates this by providing well-organized, QC'd datasets that can be processed through [[connectome-mapper-3]] or similar tools to generate [[connectome]] data suitable forTVB simulations. The platform also supports data sharing across research consortia, which aligns with the collaborative nature of many TVB-based research projects.

## Technical Architecture

LORIS is built on a LAMP stack (Linux, Apache, MySQL, PHP), reflecting its origins in the early 2000s web development era. The MySQL database stores metadata about imaging sessions, while PHP scripts handle the web interface and pipeline orchestration. The system stores imaging files on disk but maintains comprehensive relational metadata in MySQL, allowing complex queries across projects, subjects, and imaging modalities.

The pipeline system uses a modular architecture where individual processing stages are defined as独立的 modules that can be combined into custom workflows. Each module specifies input requirements, processing commands, and output specifications. This modular design allows research groups to customize processing chains for their specific imaging protocols while maintaining compatibility with the broader LORIS ecosystem.

## Key Papers and Development History

LORIS was developed primarily at the Montreal Neurological Institute under the direction of D. Louis Collins and later further developed by the LORIS team. The system has been used by major neuroimaging projects including the [[human-connectome-project]] consortium for data management and has influenced the development of neuroimaging data standards. While specific citations for LORIS vary by version and institutional deployment, the platform has been instrumental in enabling large-scale multi-site neuroimaging studies.

## Related Software

LORIS intersects with several categories of neuroimaging software in the broader ecosystem. For data management, it shares functionality with platforms like [[XNAT]] and [[cbrain]], though LORIS is distinguished by its native pipeline integration and close ties to the MNI processing environment. For preprocessing and quality control, LORIS integrates with [[freesurfer]], [[fsl]], and [[afni]], as well as quality control tools like [[mriqc]] from the [[bids]] preprocessing ecosystem. For connectome generation from processed imaging data, LORIS-compatible data can feed into tools like [[mrtrix3-connectome]] or the [[brain-connectivity-toolkit]] (BCT).

## Related Pages

- [[neuroimaging]]
- [[data-management]]
- [[structural-connectivity]]
- [[human-connectome-project]]
- [[the-virtual-brain]]
- [[whole-brain-modeling]]


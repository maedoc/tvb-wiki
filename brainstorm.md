---
title: Brainstorm
created: 2024-01-15
updated: 2026-05-07
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, source-localization, connectivity, software-visualization]
sources: [raw/papers/brainstorm-tutorial.pdf, raw/papers/brainstorm-mne-2020.pdf, raw/papers/brainstorm-isbi-2013.pdf]
---

# Brainstorm

## Overview

Brainstorm is an open-source MATLAB toolbox for processing and analyzing magnetoencephalography (MEG) and electroencephalography (EEG) data, with particular strength in source reconstruction and connectivity analysis. Developed primarily at the University of Southern California (USC) under the leadership of Sylvain Baillet and François Tadel, Brainstorm provides a comprehensive framework for forward modeling, source imaging, and statistical analysis of electrophysiological data. The software emphasizes an intuitive graphical user interface while remaining accessible through scripting for automated pipelines, making it suitable for both novice users and advanced researchers conducting large-scale studies.

## Key Features

Brainstorm distinguishes itself through its emphasis on distributed source imaging using multiple forward models, including the symmetric boundary element method (BEM) and finite element method (FEM) for realistic head modeling. The software integrates seamlessly with standard neuroimaging file formats, supporting FIF (Elekta/Neuromag), CTF, 4D/BTi, BrainVision, and EDF formats, enabling researchers to work with data from virtually any MEG or EEG system without format conversion overhead. Source reconstruction implements multiple algorithms including minimum norm estimates (MNE), weighted MNE, beamforming via linear constraint minimum variance (LCMV), and dipole fitting for event-related analysis.

The connectivity analysis module in Brainstorm has become particularly influential in the whole-brain modeling community, providing implementations of amplitude envelope correlation, phase-locking value (PLV), phase lag index (PLI), and granger causality among several other metrics[^2]. These tools enable researchers to characterize brain networks from electrophysiological data at millisecond temporal resolution, complementing the slower hemodynamic signals captured by [[fmri]]. Brainstorm also includes a robust pipeline system allowing users to design reproducible processing streams that can be applied across subjects and experimental conditions, with batch processing capabilities essential for group studies

## Relationship to TVB

While Brainstorm operates primarily in the electrophysiology domain rather than [[whole-brain-modeling]] per se, its relationship to [[the-virtual-brain]] (TVB) is multifaceted and clinically significant. Both toolboxes share a common heritage in computational neuroscience, with the Montreal group contributing substantially to both software ecosystems. Brainstorm serves as a critical validation platform for TVB-simulated dynamics—researchers frequently compare TVB forward models to empirical EEG/MEG data processed through Brainstorm to assess model fidelity. Conversely, Brainstorm's connectivity metrics have been used to define empirical brain networks that inform TVB connectome inputs, particularly when integrating [[structural-connectivity]] from diffusion imaging with [[functional-connectivity]] from resting-state analyses.

The practical integration typically involves exporting TVB simulation outputs (simulated electrode measurements) in standard formats that Brainstorm can import, enabling direct comparison between simulated and observed electrophysiological signatures. This workflow supports the validation pipeline described in TVB's model-validation framework, where in silico predictions are tested against empirical observations. Additionally, both toolboxes leverage common neuroinformatic standards including [[bids]] for data organization and share compatible atlas representations (e.g., [[desikan-killiany-atlas]], [[aal-atlas]]), facilitating interoperability between the platforms.

## Technical Implementation

The software architecture relies on MATLAB's object-oriented programming features, with a modular design separating data management, processing algorithms, and visualization components. Forward models are computed using the OpenMEEG boundary element method solver, which Brainstorm calls through a wrapper interface, providing accurate volume conduction models that account for skull and scalp conductivity anisotropy. The source estimation routines implement regularization through Tikhonov methods, with automatic estimation of the regularization parameter through cross-validation or empirical Bayes approaches.

Brainstorm maintains a public database of processed datasets (Brainstorm defaults) that new users can examine to understand processing pipelines, and the software includes extensive documentation with video tutorials covering common analysis workflows. The community-driven development model has produced numerous plugins extending functionality for specific use cases, including epilepsy analysis modules and developmental study tooling.

## Key Papers

The foundational description of Brainstorm appeared in a 2009 Neuroimage tutorial article, which established the basic architecture and processing workflows for the toolbox. This was subsequently updated with comprehensive documentation covering the connectivity analysis features and integration with forward modeling tools.

## Related Software

Brainstorm intersects with several other toolboxes in the neuroimaging ecosystem. For electrophysiological analysis, [[eeglab]] provides a competing MATLAB-based environment with different emphasis (component-based analysis rather than source imaging), while fieldtrip offers an alternative MATLAB toolbox with strong open-source development and academic backing. For source localization specifically, [[mne]] (originally Python-based) implements related algorithms with different computational approaches.

Integration with TVB occurs through standard file formats—the software can export processed data in [[nifti]] or matrix formats that TVB's tvb-library can import for connectivity analysis or use in inverse solutions. Visualization capabilities complement TVB's web-based interface, with Brainstorm providing detailed cortical and volumetric visualization that can be compared against TVB's simulated activation patterns on brain surfaces.


# Multi-Source Neural Activity Indices for EEG/MEG Localization: A Two-Stage Spatial Filtering Framework and Extension to MNE-Python

**Source**: semantic-scholar
**ID**: 878047318a75da6290687bae04861c02cec124af
**URL**: https://www.semanticscholar.org/paper/878047318a75da6290687bae04861c02cec124af
**Date**: 2025-09-17
**Year**: 2025
**Authors**: Julia Jurkowska, J. Dreszer, Monika Lewandowska, Krzysztof Tołpa, Tomasz Piotrowski
**Citations**: 2

## Abstract

Accurate electroencephalography (EEG) and magnetoencephalography (MEG) source localization and reconstruction are essential for understanding brain function, yet remain challenging because the underlying EEG/MEG inverse problem is inherently ill-posed. Spatial filtering (beamforming) approaches, such as linearly constrained minimum variance (LCMV) spatial filters, are widely used and well supported by existing analysis software. In this work, we extend this framework by deriving a novel family of unbiased multi-source neural activity indices that form the localization stage of a two-stage spatial-filtering-based localization-reconstruction framework for the EEG/MEG inverse problem. In contrast to existing formulations, the proposed indices do not require knowledge of the target source covariance matrix, making them directly applicable in practical experimental settings. Their compact algebraic forms enable straightforward and numerically efficient implementation. The framework is validated on simulated EEG data and its applicability is illustrated through an example involving experimental EEG data from an oddball paradigm. To facilitate adoption, we provide a full open-source implementation extending MNE-Python, accompanied by a practical tutorial.

---
created: 2025-01-01
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/semanticscholar-9e42d6a25d21.md
- raw/papers/arxiv-2505.16861.md
tags:
- software-visualization
- neuroimaging-eeg
- source-localization
- micro-states
- brain-mapping
title: Cartool
type: entity
updated: '2026-04-30'
---

# Cartool

## Overview

Cartool is a specialized software package for the visualization, preprocessing, and analysis of [[eeg]] data, with particular emphasis on electrical source imaging (ESI) and microstate analysis. Originally developed at the Functional Brain Mapping Lab at the University of Geneva and now maintained by the Geneva University Hospital and the Center for Biomedical Imaging (CIBM) in Switzerland, Cartool has been under continuous development since 1997, making it one of the longest-running EEG analysis platforms in the field. The software is written in C++ for Windows, designed for computational efficiency with parallel processing capabilities and minimal memory footprint. Unlike many contemporary EEG tools that rely on interpreted languages like MATLAB or Python, Cartool operates as a standalone executable with few external dependencies, ensuring stability and consistency across versions.

## Key Features

### Source Localization and Inverse Solutions

Cartool implements several inverse solution algorithms for estimating the intracranial sources of scalp-recorded EEG activity. These include variants of **low-resolution brain electromagnetic tomography (LORETA)**, **weighted minimum norm estimation**, and **spatial Laplacian** approaches. The software computes lead field matrices using realistic head models constructed from individual MRI scans, allowing for anatomically constrained source estimation. Users can coregister electrode positions to structural MR images using semi-automatic procedures, and the system supports both individual and template-based head models for cases without structural imaging data.

### Microstate Analysis

One of Cartool's signature features is its comprehensive implementation of microstate analysis for [[resting-state]] [[eeg]]. The software provides tools for segmenting continuous [[eeg]] recordings into a sequence of quasi-stable topographic configurations, typically lasting 50–100 milliseconds each. These microstates have been linked to distinct cognitive and perceptual processes, and Cartool allows researchers to extract microstate classes from their data, examine their temporal dynamics, and compare microstate parameters across experimental conditions or clinical populations. The platform supports various clustering algorithms for microstate extraction, including modified k-means and hierarchical approaches.

### Frequency and Time-Frequency Analysis

Cartool provides a range of spectral analysis tools, including fast Fourier transform (FFT)-based power spectral density estimation and wavelets for time-frequency decompositions. Users can compute event-related spectral perturbations (ERSP) and inter-trial coherence for evoked responses, and the software includes tools for analyzing [[brain-oscillations]] across canonical frequency bands (delta, theta, alpha, beta, gamma). These features are particularly valuable for studying [[brain-oscillations]] and their alterations in neurological and psychiatric conditions.

### Preprocessing Pipeline

The software offers integrated preprocessing capabilities for EEG data, including filtering (bandpass, notch), artifact rejection (eye blinks, muscle artifacts), baseline correction, and rereferencing. Cartool handles various EEG file formats and provides tools for importing data from common acquisition systems. The preprocessing pipeline can be operated through both graphical user interface dialogs and command-line scripting, facilitating batch processing of large datasets.

## Relationship to TVB

While Cartool and [[the-virtual-brain]] (TVB) serve different primary purposes in the neuroimaging ecosystem, they share conceptual ground in their focus on brain dynamics and [[whole-brain-modeling]]. Cartool focuses on extracting information from observed EEG data through [[source-localization]] and microstate segmentation, while TVB builds generative models that simulate brain activity at the network level. In practice, these tools can be complementary: Cartool-derived source estimates or microstate parameters can inform the parameterization of [[neural-mass-models]] or [[whole-brain-modeling]] models in TVB. Furthermore, both software packages deal with the forward problem—computing how sources in the brain produce observed potentials—and share concerns about the inverse-problem in neuroimaging. TVB's simulation environments can benefit from empirical constraints derived from Cartool's EEG analyses, particularly when modeling [[brain-oscillations]] or pathological states like [[epilepsy-modeling]].

## Technical Implementation

The software architecture emphasizes efficiency and portability. Written primarily in C++ with OpenGL for visualization, Cartool runs as a standalone Windows application without requiring MATLAB, Python, or other runtime environments. This design choice, made by primary developer Denis Brunet and colleagues at the Functional Brain Mapping Lab, ensures that results are highly reproducible across installations—a notable advantage in clinical research settings. The software maintains backward compatibility across versions, and past releases remain accessible for reproducing historical analyses.

## Key Papers

The seminal reference for Cartool is the 2011 paper by Brunet, Murray, and Michel titled "Spatiotemporal Analysis of Multichannel EEG: CARTOOL," which describes the software's architecture and capabilities for multichannel EEG analysis. A 2019 review article by Michel and Brunet, "EEG Source Imaging: A Practical Review of the Analysis [[steps]]," provides guidance on standard practices for source localization using tools like Cartool. The microstate analysis capabilities are detailed in several methodological papers, including a 2024 tutorial on infant EEG microstate analysis by Bagdasarov and colleagues.

## Licensing and Availability

Cartool is distributed as a standalone Windows executable under an academic license agreement. The software is freely available to academic researchers and clinicians, with licensing terms managed through the Geneva University Hospital. Prospective users can obtain the software by contacting the Cartool development team at the Center for Biomedical Imaging (CIBM) in Geneva. Commercial use requires a separate license agreement.

## Related Software

Cartool occupies a specific niche in the EEG analysis landscape, complementary to several other popular platforms. [[eeglab]] is a widely used MATLAB-based toolbox that offers broader preprocessing capabilities but less specialized tools for source imaging and microstates. [[fieldtrip]] provides similar [[source-localization]] functionality with stronger integration with [[meg]] data and a more open development model. [[brainstorm]] offers a comprehensive environment for EEG and MEG analysis with advanced visualization capabilities. For [[source-localization]] specifically, Cartesian implementations of LORETA and minimum norm estimation are also available in [[mne-python]], which provides a Python-based ecosystem with modern machine learning integrations. The microstate functionality in Cartool has parallels in the R package `microstate` and implementations in `pyeeg`, though Cartool remains among the most fully featured platforms for this specific analysis mode.
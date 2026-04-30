---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
tags:
- software-visualization
- computational-neuroscience
- neuroimaging
title: HOMER3
type: entity
updated: '2026-04-30'
---

# HOMER3

## Overview

HOMER3 (Higher-Order Maximum Entropy Renormalization, version 3) is a widely-used MATLAB-based software package for the analysis and visualization of two-photon laser scanning microscopy (2PLSM) calcium imaging data. It serves as a key tool in the computational neuroscience toolkit for processing single-neuron resolution imaging data. Originally developed as an extension of the HOMER toolbox, HOMER3 provides an integrated environment for preprocessing, cell detection, signal extraction, spike inference, and visualization of neural activity from in vivo calcium imaging experiments. The software has become a standard tool in many neuroscience laboratories studying mesoscopic neural circuits, particularly those investigating cellular-resolution cortical dynamics in mouse models. Within the broader landscape of [[neural-network]] analysis tools, HOMER3 occupies a niche between general-purpose packages like [[brian]] or [[brian2]] and specialized acquisition software.

## Motivation and Context

The advent of two-photon calcium imaging revolutionized systems neuroscience by enabling researchers to record the activity of hundreds to thousands of individual neurons simultaneously in the living brain. However, the raw fluorescence signals obtained from such experiments require substantial computational processing before they can be interpreted as neural activity. Raw calcium imaging data contains artifacts from motion, drift, and shot noise, and the relationship between fluorescence fluctuations and underlying spiking activity must be inferred through deconvolution algorithms.

HOMER3 emerged to address these analysis challenges by providing a comprehensive, user-friendly pipeline for processing calcium imaging data from acquisition to analysis. The software fits into a broader ecosystem of [[whole-brain]] [[whole-brain-modeling]] tools like [[the-virtual-brain]] that operate at different scales of neural analysis. The software bridges the gap between raw microscopy data and interpretable neural activity signals, enabling researchers to focus on experimental questions rather than custom code development. Its integration with ScanBox (a popular two-photon microscopy acquisition system) has made it particularly popular in laboratories studying sensory processing, motor cortex function, and circuit dynamics in behaving animals.

## Technical Content

HOMER3 implements a complete processing pipeline for calcium imaging data. The preprocessing stage handles motion correction using frame-to-frame alignment algorithms, spatial filtering to reduce noise, and temporal filtering to isolate the calcium signal from slow drift artifacts. These preprocessing [[steps]] are essential because even subtle motion artifacts can introduce spurious correlations in the inferred neural activity.

Cell detection in HOMER3 employs a combination of automated segmentation algorithms and manual refinement tools. The software can identify putative cells based on spatial smoothness and temporal correlation properties, producing regions of interest (ROIs) that correspond to individual neuronal cell bodies. Users can then manually adjust these ROIs to correct errors in the automated segmentation—a critical capability because automated algorithms inevitably make mistakes with out-of-focus cells, dendrites, or artefactual signals.

Signal extraction computes the fluorescence time series within each detected ROI, along with estimates of the surrounding neuropil signal. Proper neuropil subtraction is crucial for accurate spike inference, as calcium signals can spread beyond the immediate soma. HOMER3 offers several approaches for neuropil estimation and subtraction, allowing researchers to choose the method most appropriate for their data.

The spike inference module converts fluorescence time courses into estimates of underlying spiking activity. HOMER3 implements several algorithms including nonnegative deconvolution, template matching, and maximum likelihood estimation assuming a calcium transient model. The choice of algorithm involves trade-offs between speed, accuracy, and the need to estimate uncertain spike timing.

Visualization capabilities in HOMER3 include interactive ROI selection, trial-averaged activity movies, calcium transient detection overlays, and raster plots aligned to behavioral events. These tools enable rapid exploration of neural activity patterns and their relationship to stimuli or behavior.

## Key Features

The software maintains backward compatibility with older HOMER formats while offering several improvements over its predecessors. Version 3 introduced a more modular architecture that facilitates integration with analysis pipelines, improved memory efficiency for handling large datasets, and enhanced visualization tools including 3D stack viewing capabilities. The modular design also allows individual components to be called programmatically, enabling batch processing of multiple datasets.

Integration with the MATLAB programming environment provides access to standard statistical and plotting tools, though this also limits HOMER3's portability compared to pure Python solutions. The reliance on MATLAB distinguishes it from Python-native tools like [[suite2p]] and [[caiman]]. The [[tvb]] and other whole-brain modeling frameworks typically operate at a different level of abstraction, focusing on population-level dynamics rather than single-neuron imaging.

## Relationship to TVB

While HOMER3 and [[the-virtual-brain]] address different scales of neural analysis—both are software tools in the computational neuroscience ecosystem, they serve complementary rather than competing purposes. The Virtual Brain operates at the level of brain regions and populations, simulating large-scale network dynamics that emerge from the interaction between brain areas. In contrast, HOMER3 processes single-neuron resolution data from calcium imaging experiments. Researchers increasingly combine these approaches: calcium imaging data processed through HOMER3 can inform parameter estimation for whole-brain models, while theoretical predictions from [[tvb]] can guide the design of imaging experiments. The integration of single-neuron data with population-level models represents an important frontier in [[computational-neuroscience]]. For example, when studying [[epilepsy-modeling]], researchers might use HOMER3 to analyze seizure-like activity patterns in mouse cortex and then use those observations to constrain parameters in the [[epileptor]] model implemented in [[tvb]]. This multi-scale integration reflects the growing interest in connecting [[neural-mass-models]] with empirical single-cell data.

## Related Software

HOMER3 occupies a specific niche in the calcium imaging analysis ecosystem. Alternative tools include [[suite2p]] (a Python-based package offering similar functionality with perhaps more automated cell detection) and [[caiman]] (an open-source Python package emphasizing scalability and automation). Each tool has distinct strengths: CAIMAN excels at handling very large datasets, Suite2P offers excellent automated performance, and ScanBox provides tight integration with its proprietary acquisition system. HOMER3's particular strength lies in its balance of automation and manual refinement capabilities, combined with extensive [[software-ants]] tools that facilitate interactive data exploration. These capabilities complement other analysis packages in the neuroimaging ecosystem, including [[eeglab]] for electrophysiology analysis and [[fieldtrip]] for MEG/EEG processing.

## Key Papers

The original HOMER paper (Akerberg et al., 2018) describes the software's architecture and demonstrates its application to various experimental paradigms. The software continues to be updated, with recent versions improving integration with standard data formats and adding support for new calcium indicators including GCaMP6 and GCaMP7 variants.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922)
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on whole-brain models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194)
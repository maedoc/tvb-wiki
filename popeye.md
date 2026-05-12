---
title: popeye
created: 2024-01-15
updated: 2026-05-12
type: software
tags: [software-visualization, neuroimaging-fmri, forward-model, reproducibility, brain-dynamics]
sources: [raw/papers/semanticscholar-cb501cd33451.md, raw/papers/arxiv-2603.24176.md, raw/papers/arxiv-2604.14259.md, raw/papers/glean-github.md, raw/papers/semanticscholar-6295d2445697.md]
---

# _preamble

popeye (Population REceptive Field estimAtion) is an open-source Python package for estimating population receptive field models from [[fmri]] data, providing a computational framework for characterizing the spatial tuning properties of neuronal populations through analysis of the blood-oxygen-level-dependent (BOLD) signal. In network neuroscience, researchers routinely face a multitude of arbitrary yet defensible methodological choices when analyzing fMRI data, raising fundamental concerns about the robustness and [[reproducibility]] of findings in the absence of established ground truths regarding analytical validity [[raw/papers/semanticscholar-cb501cd33451.md|Burkhardt & Gießing (2025)]]. The high acquisition cost of functional magnetic resonance imaging limits large-scale applications, making careful methodological design essential for maximizing the inferential value of high-resolution cortical representations [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. Functional connectivity matrices derived from fMRI encode large-scale neural interactions that are widely used for studying brain disorders, yet existing diagnostic models are typically trained on single-site data or under full multi-site access assumptions, rendering them unsuitable for real-world sequential multi-site scenarios and producing catastrophic forgetting [[raw/papers/arxiv-2604.14259.md|Chen & Yu (2026)]]. The impact of analytical decisions such as atlas [[parcellation]] on neuroimaging conclusions is substantial; systematic investigation across six psychiatric disorders showed that frontal-related [[functional-connectivity]] deficits are reproducible regardless of atlas choice, whereas classification accuracy and spatial pattern extraction in other regions depend critically on the delineation technique employed [[raw/papers/semanticscholar-6295d2445697.md|Wu et al. (2025)]]. Complementary electrophysiological approaches including GLEAN identify covariation patterns in [[eeg]] and [[meg]] band-limited power through Hidden Markov Models or Independent Component Analysis, offering robust group-level network features in resting-state data [[raw/papers/glean-github.md|Baker et al. (2015)]]. Positioned within this methodological landscape, popeye contributes to an open analytical ecosystem for studying [[brain-dynamics]] by providing transparent, reproducible pRF estimation that aligns with the broader imperative to systematically evaluate how analytical choices shape neuroimaging inferences.

## Overview

**popeye** (Population REceptive Field estimAtion) is an open-source Python package for estimating population receptive field (pRF) models from [[fmri]] data. Developed primarily by Kevin DeSimone with significant contributions from Ariel Rokem, popeye provides a computational framework for characterizing the spatial tuning properties of neuronal populations by analyzing the BOLD (blood-oxygen-level-dependent) signal response to controlled visual stimuli. The software was created to address the lack of open-source implementations for pRF modeling—a method that had previously only been available in proprietary MATLAB-based toolboxes such as mrVista. The package is distributed under the 3-Clause BSD license and has been published in the Journal of Open Source Software.

## What is a Population Receptive Field?

A population receptive field (pRF) is a quantitative model that describes the cumulative response properties of all neurons contained within a single fMRI voxel. Unlike single-unit electrophysiology, which measures the response of individual neurons, pRF modeling provides a mesoscopic description of neuronal population tuning. The pRF concept was formalized by Dumoulin and Wandell (2008), who demonstrated that the fMRI BOLD signal could be used to estimate the spatial position, size, and shape of receptive fields for neuronal populations in visual cortex.

The pRF model works as a forward encoding model: researchers present a stimulus that varies systematically over the dimensions of interest (typically visual field position for retinotopic mapping), record the BOLD response, and then fit a computational model to recover the parameters that best describe each voxel's receptive field. This approach has proven remarkably successful for mapping the retinotopic organization of visual areas, and has been extended to study auditory cortex, somatosensory cortex, and subcortical structures including the lateral geniculate nucleus (LGN).

## Key Features

popeye implements several distinct pRF models to accommodate different hypotheses about neuronal population properties. The **Gaussian model** assumes a circularly symmetric receptive field characterized by center position (x, y) and spread (σ). The **Difference of Gaussians (DoG) model** adds a surround suppression component, making it suitable for studying center-surround organization. The software also supports **compressible spatial summation (CSS)** models, which account for the fact that larger receptive fields may have nonlinear response properties.

The package includes a modular architecture with three fundamental components: `StimulusModel`, `PopulationModel`, and `PopulationFit`. The StimulusModel class encodes the spatiotemporal stimulus parameters, the PopulationModel defines the mathematical form of the receptive field and generates predictions given stimulus input, and the PopulationFit class implements the optimization routines for fitting model parameters to observed BOLD time series. This modular design facilitates extension to new stimulus modalities and receptive field formulations.

popeye provides several estimation options including optional HRF parameter fitting, allowing users to jointly estimate both the pRF parameters and the hemodynamic response function. This flexibility is important given the well-documented inter-subject and regional variability in HRF shape. The package implements both brute-force grid search initialization followed by gradient descent optimization, and supports parallel processing for handling large datasets efficiently.

## Relationship to The Virtual Brain

While popeye is primarily a tool for analyzing fMRI data at the level of individual voxels, its outputs can inform [[whole-brain-modeling]] efforts in several ways. The pRF estimates provide empirically grounded characterization of cortical tuning properties that can constrain neural mass models of visual cortex dynamics. In particular, the spatial frequency preferences, receptive field sizes, and retinotopic organization derived from pRF analysis can be used to specify parameters in models such as the [[jansen-rit-model]] or [[wong-wang-model]] when these are applied to study visual system dynamics.

The popeye methodology represents a complementary approach to other [[neuroimaging]] analysis pipelines that feed into [[brain-dynamics]] research. Unlike resting-state functional connectivity analyses, pRF modeling provides a direct window into the representational structure of sensory cortex, revealing how visual space is mapped onto the cortical surface. This information can be valuable for building personalized [[computational-neuroscience]] models that incorporate individual differences in cortical organization.

## Key Implementation Details

The forward model underlying pRF estimation comprises several components that must be specified carefully. The stimulus is represented as a time-varying binary mask indicating which positions in visual space contain contrast. The receptive field model defines how the stimulus is weighted spatially—typically as a 2D Gaussian function. The hemodynamic response function models the temporal lag and shape of the neurovascular coupling, typically parameterized as the sum of two gamma functions (one for the peak and one for the undershoot). The noise model accounts for physiological artifacts and measurement error.

A critical consideration in pRF estimation is the mismatch between the HRF used in analysis and the true HRF in the data. Lerma-Usabiaga et al. (2020) demonstrated through the popeye validation framework that HRF mismatches can systematically bias pRF size estimates by up to ±2 degrees. This finding has important implications for comparative studies and highlights the importance of either estimating individual HRFs or using stimulus designs that minimize HRF sensitivity.

## Validation and Reliability

The popeye package has been subjected to systematic validation using ground-truth synthetic data. The pRF-Validation framework developed by Lerma-Usabiaga et al. enables rigorous testing by generating synthetic BOLD time series with known pRF parameters, then comparing these to estimates recovered by the analysis software. This validation approach revealed that median pRF estimates converge to ground truth values, though outliers can occur due to local minima in the nonlinear optimization.

Studies of empirical reliability have generally found pRF position estimates (eccentricity and polar angle) to be highly reproducible across scanning sessions, while pRF size estimates show somewhat greater variability. This pattern suggests that the population-level representation of visual space is stable, while the precise extent of receptive fields may be more sensitive to physiological factors.

## Related Software

popeye exists within an ecosystem of pRF estimation tools that includes:

- **mrVista**: The original MATLAB-based pRF framework from the Wandell lab at Stanford
- **analyzePRF**: Kendrick Kay's MATLAB implementation with efficient computational methods
- **AFNI**: The NIH-funded software includes a command-line pRF implementation
- **prf-py**: A more recent Python implementation

For visualization and cortical mapping, popeye integrates with tools such as [[fsleyes]], [[freesurfer]], and [[nilearn]]. The package outputs results in NIfTI format, making it compatible with standard [[neuroimaging]] processing pipelines including those supported by [[bids]].

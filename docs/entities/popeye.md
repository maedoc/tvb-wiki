---
title: Popeye
created: 2026-04-15
updated: 2026-05-18
type: entity
tags: [software-visualization, neuroimaging-fmri, reproducibility, network-dynamics, parameter-estimation]
sources:
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2604.14259.md
- raw/papers/semanticscholar-cb501cd33451.md
---

Popeye is a Python package for estimating population receptive fields (pRFs) from functional magnetic resonance imaging (fMRI) data. It implements a modular framework for fitting forward models that relate visual stimuli to recorded blood-oxygen-level-dependent (BOLD) responses, enabling researchers to map functional organization across cortical surfaces with high spatial precision. Within the broader landscape of [[neuroimaging]] analysis, popeye addresses the growing demand for methods that preserve cortical-vertex-level detail while maintaining temporal coherence in dynamic [[brain-dynamics]] modeling [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]].

The need for precise pRF estimation arises from fundamental challenges in fMRI analysis. Functional magnetic resonance imaging provides high-resolution cortical representations that form a strong basis for characterizing fine-grained brain activity patterns, yet the high acquisition cost of fMRI limits large-scale applications [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. This places strong pressure on analysis pipelines to reconstruct maximal information from each scan while preserving spatial accuracy across whole-brain and functionally specific regions [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. Broader reproducibility challenges persist in [[netneuroscience|network neuroscience]] because there is no ground truth for the validity of specific analytical steps, and researchers face a multitude of arbitrary yet defensible choices when moving from raw BOLD signals to interpretable models [[raw/papers/semanticscholar-cb501cd33451.md|Burkhardt & Gießing (2025)]]. Methods that model local functional properties with precision are therefore essential for linking regional activity to large-scale behavior.

## What is a Population Receptive Field?

A population receptive field describes the region of visual space that influences the [[bold-signal|BOLD]] response of a neuronal population at a given cortical location. Rather than characterizing individual neurons, pRF modeling estimates the aggregate receptive field properties of local populations by fitting a [[forward-model]] that predicts the fMRI time series from a known stimulus sequence. This approach recovers spatial tuning parameters—typically including the center position, preferred eccentricity, polar angle, and spatial spread—thereby mapping functional topography across visual areas with sub-voxel precision.

## Key Features

Popeye implements several pRF models commonly encountered in the neuroimaging literature. The Gaussian pRF model assumes a circular receptive field profile described by a two-dimensional Gaussian function, parameterizing each cortical vertex by its preferred visual field coordinates and size. The Difference-of-Gaussians (DoG) model extends this framework by adding a surround suppression term, capturing antagonistic center-surround organization observed in early visual cortex. The Compressive Spatial Summation (CSS) model further introduces an exponent parameter that compresses the pRF profile, accounting for subadditive spatial summation effects in higher-tier visual areas. Popeye's architecture separates stimulus generation, forward-model convolution, [[hemodynamic-response-function]] specification, and nonlinear optimization, allowing individual components to be swapped or extended independently.

## Relationship to The Virtual Brain

Population receptive field estimates produce individual-specific maps of functional topography, size, and position across cortical surfaces. These maps serve as empirical constraints for [[whole-brain-modeling]] by providing region-specific estimates of local processing characteristics that can inform the parameterization of [[neural-mass-models|neural mass models]] such as the [[jansen-rit-model]] or the [[wong-wang-model]] in [[the-virtual-brain]]. By incorporating pRF-derived spatial tuning into large-scale network simulations, researchers can link local circuit properties to global [[network-dynamics]] and benchmark simulated activity against empirical [[functional-connectivity]] patterns derived from the same individuals.

## Related Software

Several alternatives exist for pRF analysis. mrVista and analyzePRF are MATLAB-based tools widely used in the vision neuroscience community. The [[afni]] suite includes 3dRetinoFit for pRF estimation within broader [[fmri]] workflows. In Python, popeye offers a lighter, focused alternative that integrates with standard scientific stacks and neuroimaging libraries, contributing to reproducible [[computational-neuroscience]] research through accessible, modular analysis tools.

---
title: Popeye
created: 2024-01-15
updated: 2026-05-19
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, whole-brain-modeling, functional-connectivity, parameter-estimation]
sources: [raw/papers/arxiv-2603.24176.md, raw/papers/arxiv-2604.14259.md, raw/papers/semanticscholar-cb501cd33451.md]
---

Popeye is a Python package for estimating population receptive fields (pRFs) from functional magnetic resonance imaging ([[fmri|fMRI]]) data. It implements a modular framework for fitting [[forward-model|forward models]] that relate visual stimuli to recorded [[bold-signal|blood-oxygen-level-dependent (BOLD)]] responses, enabling researchers to map functional organization across cortical surfaces with high spatial precision. Within the broader landscape of [[neuroimaging]] analysis, popeye addresses the growing demand for methods that preserve cortical-vertex-level detail while maintaining temporal coherence in dynamic [[brain-dynamics]] modeling.

The need for precise pRF estimation arises from fundamental challenges in fMRI analysis. Functional magnetic resonance imaging provides high-resolution cortical representations that form a strong basis for characterizing fine-grained brain activity patterns, yet the high acquisition cost of fMRI limits large-scale applications and creates strong pressure on analysis pipelines to reconstruct maximal information from each scan [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. This pressure extends to preserving spatial accuracy across whole-brain and functionally specific regions, as recent work demonstrates through EEG-conditioned frameworks that reconstruct dynamic fMRI with high spatial fidelity at the cortical-vertex level [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. At the same time, fMRI is widely used for studying brain disorders, with [[functional-connectivity]] matrices providing powerful representations of large-scale neural interactions that support both basic research and clinical diagnosis [[raw/papers/arxiv-2604.14259.md|Chen & Yu (2026)]]. Broader reproducibility challenges persist in network neuroscience because there is no ground truth for the validity of specific analytical steps, and researchers face a multitude of arbitrary yet defensible choices when moving from raw BOLD signals to interpretable models [[raw/papers/semanticscholar-cb501cd33451.md|Burkhardt & Gießing (2025)]]. Methods that model local functional properties with precision are therefore essential for linking regional activity to large-scale behavior.

## What is a Population Receptive Field?

A population receptive field describes the region of visual space that influences the BOLD response of a neuronal population at a given cortical location. Rather than characterizing individual neurons, pRF modeling estimates the aggregate receptive field properties of local populations by fitting a forward model that predicts the fMRI time series from a known stimulus sequence. This approach recovers spatial tuning parameters—typically including the center position, preferred eccentricity, polar angle, and spatial spread—thereby mapping functional topography across visual areas with sub-voxel precision.

## Models and Implementation

pRF estimation commonly employs several forward-model formulations that vary in their assumptions about spatial summation. The Gaussian pRF model assumes a circular receptive field profile described by a two-dimensional Gaussian function, parameterizing each cortical vertex by preferred visual field coordinates and size. The Difference-of-Gaussians (DoG) model extends this framework by adding a surround suppression term, capturing antagonistic center-surround organization observed in early visual cortex. The Compressive Spatial Summation (CSS) model further introduces an exponent parameter that compresses the pRF profile, accounting for subadditive spatial summation effects in higher-tier visual areas. Popeye's architecture separates stimulus generation, forward-model convolution, [[hemodynamic-response-function]] specification, and nonlinear optimization, allowing individual components to be swapped or extended independently.

## Relationship to The Virtual Brain

Population receptive field estimates produce individual-specific maps of functional topography, size, and position across cortical surfaces. These maps serve as empirical constraints for [[whole-brain-modeling]] by providing region-specific estimates of local processing characteristics that can inform the parameterization of neural mass models such as the [[jansen-rit-model]] or the [[wong-wang-model]] in [[the-virtual-brain]]. By incorporating pRF-derived spatial tuning into large-scale network simulations, researchers can link local circuit properties to global [[network-dynamics]] and benchmark simulated activity against empirical [[functional-connectivity]] patterns derived from the same individuals.

## Related Software

Several alternatives exist for pRF analysis. mrVista and analyzePRF are MATLAB-based tools widely used in the vision neuroscience community. The [[afni]] suite includes 3dRetinoFit for pRF estimation within broader fMRI workflows. In Python, popeye offers a lighter, focused alternative that integrates with standard scientific stacks and neuroimaging libraries, contributing to reproducible brain modeling research through accessible, modular analysis tools.

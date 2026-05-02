---
title: popeye
created: 2026-05-02
updated: 2026-05-02
type: entity
tags: [neuroimaging-fmri, forward-model]
sources: [https://github.com/kdesimone/popeye, https://kdesimone.github.io/popeye/]
---

# popeye

## Overview

popeye is an open-source Python module for estimating population receptive fields (pRF) from [[fmri]] data. Developed by Kevin DeSimone with significant contributions from Ariel Rokem, popeye provides a comprehensive framework for forward encoding model estimation that allows researchers to interpret and predict the responses of individual voxels to various sensory and cognitive stimuli. The software was created in 2013 to address the lack of open-source tools for pRF modeling, as existing MATLAB-based toolboxes such as mrVista and analyzePRF were not truly open-source. popeye is written primarily in Python with Cython extensions for computational acceleration and is distributed under the 3-Clause BSD license.

## What is a Population Receptive Field?

A population receptive field (pRF) is a quantitative model that describes the cumulative response properties of all neurons contained within a single fMRI voxel. Rather than measuring the response of individual neurons—a procedure that would require invasive electrophysiology—the pRF approach allows researchers to infer the receptive field characteristics of entire neural populations non-invasively through the [[bold-signal]] measured by fMRI. The fundamental assumption is that each voxel contains a distributed population of neurons with overlapping receptive fields, and the measured fMRI signal represents the weighted sum of all these neural responses.

The pRF model operates as a forward encoding model: researchers present stimuli that vary systematically along the tuning dimensions of interest (such as visual field location, orientation, or frequency), record the BOLD response time-series, and then fit a computational model that best explains the observed responses. The model parameters—including the center position, size, and amplitude of the receptive field—provide quantitative descriptions of the tuning properties of the neural population within each voxel. This approach has been particularly influential in mapping the organizational principles of sensory cortex, revealing retinotopic maps in visual cortex, tonotopic maps in auditory cortex, and more recently, topographic representations in subcortical structures such as the lateral geniculate nucleus (LGN).

## Key Features

popeye implements several distinct pRF models to accommodate different sensory modalities and experimental paradigms. The Gaussian model provides a circularly symmetric receptive field that serves as a standard starting point for many applications, while the difference-of-Gaussians (DOG) model captures center-surround organization commonly observed in early visual processing. The compressive spatial summation (CSS) model accounts for nonlinear response properties typical of cortical neurons, and the Gabor model adds orientation selectivity to the standard receptive field formulation. For auditory research, popeye includes spectrotemporal receptive field models that characterize frequency tuning over time.

The software architecture separates stimulus representation, population models, and fitting procedures into distinct modules. The **VisualStimulus** class handles the creation and storage of visual stimulus arrays along with parameters such as pixels per degree and frame rate. Population models inherit from a base **PopulationModel** class that defines a `generate_prediction` method for computing expected BOLD responses given a set of model parameters. Fitting procedures employ a two-stage optimization strategy: an initial brute-force grid search followed by gradient descent refinement to locate the maximum likelihood parameter estimates. popeye also provides multiprocessing capabilities through shared memory arrays, enabling parallel fitting of thousands of voxels across multiple CPU cores to accelerate large-scale analyses.

A notable feature of popeye is its cross-validation API, which allows researchers to rigorously evaluate model fits and prevent overfitting. The software includes utilities for generating synthetic data with known ground-truth parameters, facilitating validation studies and methodological comparisons. The hemodynamic response function (HRF) is incorporated using a double-gamma model, which is typical for [[fmri]] analysis, and users can specify custom HRF shapes if needed.

## Relationship to TVB

While popeye and [[the-virtual-brain]] (TVB) serve different primary purposes within the neuroimaging ecosystem, they share a common philosophical orientation toward computational modeling of brain function. popeye focuses on voxel-level receptive field estimation to characterize fine-grained sensory maps, whereas TVB operates at the level of whole-brain network dynamics, simulating large-scale brain activity using neural mass models and connectome-based approaches. However, these tools can be complementary in a multi-scale modeling pipeline: popeye-derived pRF parameters could inform the specification of sensory input driving TVB simulations, or the retinotopic organization revealed by pRF mapping could constrain the parameterization of visual cortex models within TVB.

Both popeye and [[the-virtual-brain]] are open-source Python packages that leverage the scientific Python ecosystem, including packages like [[nibabel]] for data handling. Additionally, both tools emphasize computational efficiency—popeye through Cython optimization and multiprocessing, and TVB through GPU acceleration and reduced-order modeling techniques. For researchers building personalized brain models in TVB, empirically derived pRF estimates from popeye could provide constraints on model parameters related to sensory cortex, potentially improving the biological plausibility of simulated [[bold-signal]] signals for validation against empirical [[fmri]] data.

## Relationship to Other Neuroimaging Software

popeye occupies a specific niche in the neuroimaging software landscape, complementing rather than replacing other analysis tools. Unlike general-purpose fMRI analysis packages such as [[spm]], [[fsl]], or [[afni]], which provide comprehensive pipelines for preprocessing, statistical modeling, and inference, popeye focuses exclusively on forward encoding model estimation for pRF mapping. The software is designed to operate on preprocessed fMRI data—typically motion-corrected, spatially normalized, and temporally filtered time-series—and outputs parameter estimates that can be visualized using standard neuroimaging visualization tools like [[freesurfer]] or [[nilearn]].

## Key Papers

The development of popeye was motivated by a body of foundational pRF research. The seminal work by Dumoulin and Wandell (2008) established the theoretical framework for estimating population receptive fields in human visual cortex and demonstrated the ability to map retinotopic organization non-invasively. Subsequent extensions applied pRF modeling to auditory cortex (Thomas et al., 2014) and revealed topographic numerosity maps in parietal cortex (Harmore et al., 2013). DeSimone, Viviano, and Schneider (2015) extended the technique to subcortical nuclei, demonstrating that pRF estimation could reveal previously invisible maps in the LGN. popeye enabled several of these studies and continues to serve as a platform for developing new pRF methodologies.

## Technical Implementation

The software consists of multiple submodules organized by sensory modality and model type. The `popeye.visual_stimulus` module handles stimulus generation, including support for sweeping bar stimuli that are commonly used in retinotopic mapping experiments. The `popeye.og_hrf` module implements the canonical Gaussian model with double-gamma HRF convolution, while `popeye.dog`, `popeye.css`, and `popeye.gabor` provide alternative model formulations. Fitting is implemented in `popeye.base`, which defines the PopulationFit class that manages optimization and cross-validation procedures. The software requires NumPy >= 1.6.2, SciPy >= 0.9, nibabel >= 1.3.0, Cython >= 0.18, sharedmem >= 0.3, and statsmodels >= 0.6.

Installation is available via PyPI (`pip install popeye`) or from source from the GitHub repository. The documentation provides detailed examples covering basic single-voxel fitting, multiprocess batch analysis of whole-brain datasets, and simulation studies for model validation.
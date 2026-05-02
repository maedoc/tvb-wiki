---
title: popeye
created: 2024-01-15
updated: 2026-05-02
type: entity
tags: [software-neuroimaging, neuroimaging-fmri, brain-oscillations, software-visualization]
sources: []
---

# popeye

## Overview

**Popeye** is an open-source Python toolbox for estimating population receptive field (pRF) parameters from functional magnetic resonance imaging (fMRI) data. Originally developed by the BrainVISA team and later integrated into the wider neuroimaging ecosystem, Popeye allows researchers to model the spatial tuning properties of neuronal populations in the human brain, particularly in sensory cortices such as the visual system. By fitting computational models to fMRI time-series data, Popeye enables quantification of how neural populations respond to visual stimuli across different positions, orientations, spatial frequencies, and other stimulus dimensions. The resulting pRF parameters provide a mechanistic characterization of cortical organization that complements connectivity-based analyses in [[whole-brain-modeling]] contexts.

## Motivation and Context

Traditional fMRI analysis focuses on identifying brain regions that respond to experimental stimuli, but provides limited insight into the tuning properties of the neuronal populations within those regions. The population receptive field approach addresses this limitation by fitting explicit computational models to voxel-wise fMRI signals, yielding estimates of the spatial extent, preferred location, and selectivity of the underlying neural population. This approach was pioneered by a number of research groups in the early 2000s and has since become a standard method for studying cortical magnification, retinotopic organization, and the functional architecture of sensory cortices.

The motivation for developing Popeye stemmed from the need for an accessible, well-documented tool that could be integrated into standard neuroimaging preprocessing pipelines. Earlier implementations of pRF modeling often required custom MATLAB scripts that were difficult to maintain and share across laboratories. Popeye provides a principled Python implementation that integrates with widely-used preprocessing tools including [[nilearn]], [[freesurfer]], and [[fmriprep]], enabling reproducible pRF analysis workflows that can be applied to both publicly available datasets such as those from the [[human-connectome-project]] and custom experimental data.

In the context of [[whole-brain-modeling]], Popeye-derived pRF parameters can serve as constraints for neural mass models that aim to simulate realistic cortical dynamics. Understanding the spatial tuning properties of different cortical regions helps specify the input kernels and coupling functions in models like the [[jansen-rit-model]] or [[wong-wang-model]] that are used in [[the-virtual-brain]] simulations. This integration between empirical pRF mapping and computational modeling represents a promising direction for bridging the gap between sensory neuroscience and whole-brain dynamics.

## Key Features

Popeye provides a comprehensive suite of tools for pRF estimation and analysis:

**pRF Model Fitting:** The core functionality of Popeye involves fitting various pRF models to fMRI time-series data. The standard model assumes that each voxel's response can be described as a linear combination of the stimulus convolved with a hemodynamic response function, where the receptive field is modeled as a 2D Gaussian or Difference-of-Gaussians function. Popeye supports multiple model variants including circular symmetric receptive fields, separable receptive fields that model position and feature tuning independently, and compressed sensing models that can handle sparse stimulus representations. The fitting procedure uses maximum-likelihood estimation with optional regularization to ensure stable parameter estimates.

**Stimulus Representation:** A critical aspect of pRF modeling is accurate representation of the visual stimulus. Popeye includes tools for generating and manipulating stimulus movies from experimental designs, supporting common stimulus formats including flickering checkerboards, moving bars, wedge and ring stimuli for retinotopic mapping, and natural image sequences. The stimulus representation can be customized to account for specifics of the experimental setup including screen size, viewing distance, and eye position.

**Model Validation and ROI Analysis:** Popeye provides tools for evaluating model quality through goodness-of-fit metrics including $R^2$ and the Bayesian Information Criterion. Researchers can restrict analyses to regions of interest (ROIs) where the pRF model provides adequate fits, ensuring that subsequent analyses use only reliable parameter estimates. The toolbox integrates with parcellation schemes including the [[glasser-atlas]] and other [[brain-parcellations]] for ROI-based group analyses.

**Visualization and Reporting:** Popeye includes visualization functions for displaying pRF parameters on cortical surfaces, generating eccentricity maps, polar angle maps, and spatial preference maps that characterize the retinotopic organization of visual cortex. These visualizations integrate with [[connectome-workbench]] for viewing on inflated cortical surfaces and can be exported for publication. The visualization module supports both individual subject displays and group-averaged maps that reveal consistent organizational features across subjects.

## Relationship to TVB

While Popeye and [[the-virtual-brain]] (TVB) serve different primary purposes—Popeye focuses on empirical characterization of sensory cortex tuning while TVB focuses on forward modeling of whole-brain dynamics—there are natural points of integration in [[whole-brain-modeling]] workflows. The pRF parameters estimated by Popeye provide empirically grounded constraints for sensory cortex models in TVB, particularly when simulating visual processing or studying the effects of visual stimuli on brain-wide dynamics.

TVB's neural mass models, such as the [[jansen-rit-model]], require specification of regional parameters including coupling strengths and time constants. Popeye-derived measures of cortical magnification (the relationship between eccentricity and receptive field size) can inform these parameters, yielding more physiologically realistic models of visual cortex dynamics. Conversely, TVB simulations that incorporate realistic visual cortex models can be used to generate predictions that can be tested against empirical pRF mapping data, enabling closed-loop validation of whole-brain models against sensory neuroscience measurements.

For researchers working at the intersection of sensory neuroscience and [[personalized-brain-modeling]], Popeye provides the empirical foundation for building subject-specific models that accurately represent individual patterns of cortical organization.

## Related Software

Popeye occupies a specific niche in the neuroimaging software ecosystem alongside several related tools:

- [[nilearn]]: The foundational Python library for statistical analysis of neuroimaging data that Popeye integrates with for data preprocessing and basic time-series operations.
- [[freesurfer]] and [[freeview]]: The widely-used cortical reconstruction and visualization tools that provide the surfaces on which Popeye displays pRF parameters.
- [[connectome-workbench]]: The HCP's visualization environment that enables viewing of Popeye-generated maps alongside other neuroimaging data.
- [[brainnet-viewer]] and [[brainrender]]: Additional visualization tools that can display Popeye outputs in different rendering contexts.
- [[eeglab]]: While primarily an EEG analysis toolbox, provides related functionality for analyzing sensory responses that complement pRF analysis.

## Technical Considerations

Several technical considerations are relevant when running Popeye analyses. The quality of pRF estimates depends heavily on the quality of the fMRI data and the appropriateness of the stimulus design. Standard retinotopic mapping stimuli (rotating wedges and expanding rings) provide excellent coverage of the visual field and yield reliable pRF estimates in primary visual cortex. However, pRF analysis becomes progressively less reliable in higher-order visual areas where receptive fields become larger and more complex, and in frontal and parietal regions where retinotopic organization is less pronounced.

Computational requirements for pRF fitting scale with the number of voxels and the complexity of the model. A typical full-brain analysis with 100,000 voxels and a 2D Gaussian model may take several hours on a modern workstation, while more complex models with separable components or compressed sensing representations can take substantially longer. Popeye supports parallel processing to accelerate fitting on multi-core systems.

Preprocessing choices also affect pRF estimate quality. Standard fMRI preprocessing pipelines using [[fmriprep]] including motion correction, slice timing correction, and spatial smoothing are generally appropriate for pRF analysis, though researchers should avoid excessive spatial smoothing that would blur receptive field boundaries. Global signal regression is typically NOT recommended for pRF analysis since it can artificially suppress the stimulus-evoked responses that pRF models depend on.

---

*This page is part of the TVB Wiki ecosystem and is maintained under the [[tvb-library]] knowledge base.*
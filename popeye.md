---
title: PopEye
created: 2024-01-15
updated: 2026-05-02
type: entity
tags: [software-visualization, neuroimaging-fmri, retinotopy, prf-modeling, software-modeldb]
sources: [https://github.com/kdesimone/popeye, https://joss.theoj.org/papers/10.21105/joss.00103]
---

PopEye is an open-source Python toolbox for estimating population receptive fields (pRF) from fMRI data. Developed primarily for visual and auditory mapping experiments, PopEye provides researchers with a streamlined framework for fitting pRF models to BOLD time series, characterizing the spatial tuning properties of neural populations within each voxel. The toolbox addresses a common challenge in retinotopic mapping: moving beyond simple category-based parcellation to quantitative models of population-level receptive field properties such as position, size, and preference for visual features.

## Motivation and Context

The field of functional neuroimaging has seen growing adoption of population receptive field modeling over the past decade, driven in part by the need to understand the detailed organizational principles of human visual cortex and subcortical structures. A population receptive field is a quantitative model describing the cumulative response of all neurons contained within a single fMRI voxel — essentially averaging over many individual neural receptive fields to produce a single spatial tuning measurement [1]. This approach allows researchers to interpret and predict voxel responses to arbitrary stimuli, moving beyond the limitations of standard retinotopic mapping paradigms.

Traditional tools for pRF estimation included MATLAB-based packages such as mrVista and analyzePRF, but these implementations were not truly open-source due to their MATLAB dependencies. PopEye emerged to fill this gap by providing a Python-native implementation that leverages the full scientific Python ecosystem while maintaining transparency and extensibility [2]. The toolbox was created by Kevin DeSimone with significant contributions from Ariel Rokem and has been validated against other pRF implementations in comparative studies [3].

## Technical Capabilities

PopEye organizes its functionality around three core model components: the stimulus representation, the pRF model, and the fitting procedure. The toolbox handles visual stimuli including sweeping bar stimuli and random aperture designs, as well as auditory stimuli with spectrotemporal modulation [4]. Users can specify stimulus timing, spatial parameters, and presentation sequences, with sensible defaults optimized for standard retinotopic mapping protocols.

The pRF estimation module supports several receptive field models. The simplest is the circular Gaussian model, which characterizes each voxel's receptive field by its center position (eccentricity and polar angle), size (standard deviation of the Gaussian), and response amplitude. More sophisticated models include the Difference of Gaussians (DoG) for characterizing suppressive surrounds, the Oriented Gaussian model for motion direction selectivity, and compressive spatial summation models for accounting for nonlinear response properties [5]. PopEye also supports fitting the hemodynamic response function (HRF) simultaneously with pRF parameters, addressing a known source of bias in pRF estimation [6].

The fitting procedure uses a two-stage optimization approach: an initial brute-force grid search followed by gradient descent refinement. This hybrid approach helps avoid local minima while maintaining computational efficiency. The toolbox implements Cython-accelerated computation and multiprocessing support for fitting large numbers of voxels in parallel, making it suitable for whole-brain analysis datasets.

## Relationship to TVB and Modeling

While PopEye is designed primarily for empirical pRF estimation rather than [[whole-brain-modeling|computational modeling]], it serves as a valuable complement to [[the-virtual-brain|The Virtual Brain (TVB)]] and other [[whole-brain_simulators|whole-brain simulators]] in certain workflows. Empirical pRF measurements from visual cortex can inform the tuning parameters of neural mass models used in TVB, providing biologically grounded constraints for sensory cortex simulations. Additionally, PopEye's forward modeling approach — generating predicted BOLD signals from known pRF parameters — exemplifies the model inversion procedures also employed in TVB's empirical constrained modeling pipeline [7].

Compared to other pRF toolboxes, PopEye occupies a similar niche to [[FSL|FSL]]'s FEAT module for model-based fMRI analysis but with a more focused scope on pRF-specific modeling. The toolbox complements [[SPM|SPM]]'s general linear model framework by providing specialized routines for stimulus-driven encoding model estimation. Unlike commercial tools such as mrVista, PopEye's Python implementation facilitates integration with machine learning workflows and modern analysis pipelines.

## Key Features

The distinguishing features of PopEye include its emphasis on open-source transparency, computational efficiency through Cython acceleration, and support for both visual and auditory pRF estimation. The toolbox provides built-in visualization routines for displaying pRF parameter maps including eccentricity, polar angle, and size estimates overlaid on anatomical images. Support for multiple HRF models allows users to account for individual differences in hemodynamic response, which has been shown to significantly impact pRF size estimates when mismatched between estimation and ground truth [3][6].

PopEye integrates with the broader neuroimaging ecosystem through its use of NIfTI format for volumetric data, nibabel for file I/O, and compatibility with standard preprocessing pipelines. The toolbox has been validated in multiple studies and was included in a comprehensive comparison of four pRF implementations that identified both strengths and limitations of each approach [3].

## Related Software

- [[nilearn]]
- [[brainiak]]
- [[FSL]]
- [[SPM]]
- [[the-virtual-brain]]
- [analyzePRF](https://github.com/kendrickkay/analyzePRF)
- [mrVista](https://github.com/vistalab/vistasoft)

## Key Papers

1. Dumoulin SO, Wandell BA (2008). Population receptive field estimates in human visual cortex. NeuroImage 39:647-660. doi:10.1016/j.neuroimage.2007.09.034

2. DeSimone K, Rokem A, Schneider K (2016). popeye: a population receptive field estimation tool. Journal of Open Source Software 1(8):103. doi:10.21105/joss.00103

3. Lerma-Usabiaga G, Benson N, Winawer J, Wandell BA (2020). A validation framework for neuroimaging software: The case of population receptive fields. PLoS Computational Biology 16(6):e1007924. doi:10.1371/journal.pcbi.1007924

4. Thomas JM, Huber E, Stecker E, Boynton G, Saenz M, Fine I (2014). Population receptive field estimates in human auditory cortex. NeuroImage 105:428-439. doi:10.1016/j.neuroimage.2014.11.027

5. Harvey BM, Klein BP, Petridou N, Dumoulin SO (2013). Topographic organization of numerosity in the human parietal cortex. Science 341:1123-1126. doi:10.1126/science.1239132

6. DeSimone K, Viviano JD, Schneider KA (2015). Population receptive field estimation reveals two new maps in human subcortex. Journal of Neuroscience 35:9836-9847. doi:10.1523/JNEUROSCI.0101-15.2015

7. Zeidman P, Silson EH, Schwarzkopf DS, Baker CI, Penny W (2018). Bayesian population receptive field modelling. NeuroImage 180:173-187. doi:10.1016/j.neuroimage.2017.09.037

## References

- DeSimone K, Rokem A, Schneider K (2016). popeye: a population receptive field estimation tool. Journal of Open Source Software 1(8):103. https://joss.theoj.org/papers/10.21105/joss.00103
- PopEye GitHub Repository: https://github.com/kdesimone/popeye
- PopEye Documentation: https://popeye.readthedocs.io/
# Smooth dynamic T2* mapping in fMRI based on a novel, total variation-minimizing algorithm for efficient multi-echo BOLD time series denoising with high signal-to-noise and contrast-to-noise ratios

**Source**: semantic-scholar
**ID**: 0c6bf34f10ffbc9f2e124f3ad9d4cf47d3888c06
**DOI**: 10.3389/fnins.2025.1544748
**URL**: https://www.semanticscholar.org/paper/0c6bf34f10ffbc9f2e124f3ad9d4cf47d3888c06
**Date**: 2025-10-01
**Year**: 2025
**Authors**: Jan Michálek, Michal Mikl
**Venue**: Frontiers in Neuroscience
**Citations**: 2

## Abstract

Introduction This report deals with advanced processing of blood oxygenation-dependent (BOLD) functional magnetic resonance imaging (fMRI) signals. It does not address functional characteristics of the human cortex, such as functional connectivity. fMRI is based on measurement of BOLD variations of transverse relaxation time T2* or T2. T2* or T2 can be calculated when multiple echoes of the MRI signal are recorded and may be more resistant to artifacts or better characterize tissue properties than the echoes themselves. Objectives To develop a robust-to-noise algorithm for dynamic T2* mapping from a three gradient-echo (GRE) signal, allowing exploration of the potential of quantitative T2* mapping. Methods fMRI resting-state and block-design visual task three-echo data were acquired from nine healthy volunteers. A significant problem in multi-echo T2* fitting is the noise in the echoes. The majority of BOLD-denoising methods first pinpoint some source of noise and subsequently remove the respective noise time series. We instead first postulated that the blood oxygenation changes smoothly and consequently developed a state-of-the-art denoising algorithm that minimizes total variation (TV), enforcing smoothness in the processed BOLD echoes while preserving local temporal signal means. To ensure that calculated T2* time courses are also smooth, they were estimated from TV-denoised echoes. We used a denoising approach initially proposed by Professor Stanley Osher for two-dimensional (2D) images that has been very successful, most prominently in space research, where it enabled the reconstruction of the first-ever image of a black hole. To our knowledge, Osher’s approach has so far not been used elsewhere for the denoising of one-dimensional fMRI time series. Results Signal-to-noise and contrast-to-noise distributions of the denoised echoes, as well as of the T2* time series, were superior to those obtained by the current fMRI denoising methods (3dDespike, tedana, NORDIC). The denoised echoes and the T2* time courses match the shape of the theoretical hemodynamic function much better than previous results. Conclusion The TV-minimizing fMRI time series denoising algorithm yields denoised echoes of unprecedented quality, enabling estimation of smooth, dynamic T2* maps, i.e., a transition from qualitative-only fMRI echoes to fMRI signals endowed with time units.

# MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing

**Source**: semantic-scholar
**ID**: 4d73a30d5c84c4fb89d1c8eaf89b6bc699e3ca99
**DOI**: 10.1162/IMAG.a.1198
**URL**: https://www.semanticscholar.org/paper/4d73a30d5c84c4fb89d1c8eaf89b6bc699e3ca99
**Date**: 2026-04-06
**Year**: 2026
**Authors**: Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband
**Venue**: Imaging Neuroscience
**Citations**: 0

## Abstract

Abstract Multi-echo fMRI has emerged as a powerful strategy to mitigate head motion-related noise and minimize susceptibility-related signal loss in BOLD data. Multi-echo independent component analysis (ME-ICA) effectively distinguishes between BOLD-related (TE-dependent) signals and non-BOLD (TE-independent) noise, yielding substantial enhancements in performance compared to traditional echo-combination methods. We introduce a novel ICA-based denoising step, preICA, applied to raw multi-echo data before optimal T2*-weighted echo combination. This approach, combined with ME-ICA, yields substantial gains in data denoising. Our results show that preICA significantly enhances the efficacy of optimal echo combination and ME-ICA to reduce noise. To facilitate the reliable processing of multi-echo fMRI data, we integrated preICA and ME-ICA into fMRIPrep, resulting in the creation of a robust multi-echo processing pipeline, called MEPrep, offering flexibility in preprocessing options (with or without preICA and/or ME-ICA) beyond the echo combination approach offered by fMRIPrep. We validated MEPrep on an open resting-state multi-echo fMRI dataset, demonstrating that incorporating the preICA step leads to statistically significant improvements in denoising efficacy, as evidenced by (1) enhanced T2* exponential model fitting accuracy; (2) reduced motion-related BOLD fluctuations; (3) increased temporal signal-to-noise ratio; (4) improved spatial and temporal reliability of functional connectivity; and (5) increased Shannon entropy. MEPrep outperforms existing pipelines by synergistically integrating preICA and ME-ICA, achieving superior noise suppression while preserving the neurobiological complexity of denoised BOLD signals. By automating multi-echo preprocessing within a robust pipeline, MEPrep provides a scalable solution for high-quality multi-echo fMRI data preprocessing. The pipeline is openly available, ensuring reproducibility and accessibility for the neuroimaging community.

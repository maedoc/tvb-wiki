# FreqSelect: Frequency-Aware fMRI-to-Image Reconstruction

**Source**: semantic-scholar
**ID**: 1d8c9ae17c4f859eef67d78f84d676a11ac058a6
**DOI**: 10.48550/arXiv.2505.12552
**URL**: https://www.semanticscholar.org/paper/1d8c9ae17c4f859eef67d78f84d676a11ac058a6
**Date**: 2025-05-18
**Year**: 2025
**Authors**: Jun Ye, Lei Wang, Md Zakir Hossain
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Reconstructing natural images from functional magnetic resonance imaging (fMRI) data remains a core challenge in natural decoding due to the mismatch between the richness of visual stimuli and the noisy, low resolution nature of fMRI signals. While recent two-stage models, combining deep variational autoencoders (VAEs) with diffusion models, have advanced this task, they treat all spatial-frequency components of the input equally. This uniform treatment forces the model to extract meaning features and suppress irrelevant noise simultaneously, limiting its effectiveness. We introduce FreqSelect, a lightweight, adaptive module that selectively filters spatial-frequency bands before encoding. By dynamically emphasizing frequencies that are most predictive of brain activity and suppressing those that are uninformative, FreqSelect acts as a content-aware gate between image features and natural data. It integrates seamlessly into standard very deep VAE-diffusion pipelines and requires no additional supervision. Evaluated on the Natural Scenes dataset, FreqSelect consistently improves reconstruction quality across both low- and high-level metrics. Beyond performance gains, the learned frequency-selection patterns offer interpretable insights into how different visual frequencies are represented in the brain. Our method generalizes across subjects and scenes, and holds promise for extension to other neuroimaging modalities, offering a principled approach to enhancing both decoding accuracy and neuroscientific interpretability.

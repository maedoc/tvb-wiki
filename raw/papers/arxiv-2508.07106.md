# BrainATCL: Adaptive Temporal Brain Connectivity Learning for Functional Link Prediction and Age Estimation

**Source**: semantic-scholar
**ID**: 292da879ab7ade53900caf43c2c00afc52f84781
**DOI**: 10.48550/arXiv.2508.07106
**URL**: https://www.semanticscholar.org/paper/292da879ab7ade53900caf43c2c00afc52f84781
**Date**: 2025-08-09
**Year**: 2025
**Authors**: Yiran Huang, Amirhossein Nouranizadeh, C. Ahrends, Mengjia Xu
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Functional Magnetic Resonance Imaging (fMRI) is an imaging technique widely used to study human brain activity. fMRI signals in areas across the brain transiently synchronise and desynchronise their activity in a highly structured manner, even when an individual is at rest. These functional connectivity dynamics may be related to behaviour and neuropsychiatric disease. To model these dynamics, temporal brain connectivity representations are essential, as they reflect evolving interactions between brain regions and provide insight into transient neural states and network reconfigurations. However, conventional graph neural networks (GNNs) often struggle to capture long-range temporal dependencies in dynamic fMRI data. To address this challenge, we propose BrainATCL, an unsupervised, nonparametric framework for adaptive temporal brain connectivity learning, enabling functional link prediction and age estimation. Our method dynamically adjusts the lookback window for each snapshot based on the rate of newly added edges. Graph sequences are subsequently encoded using a GINE-Mamba2 backbone to learn spatial-temporal representations of dynamic functional connectivity in resting-state fMRI data of 1,000 participants from the Human Connectome Project. To further improve spatial modeling, we incorporate brain structure and function-informed edge attributes, i.e., the left/right hemispheric identity and subnetwork membership of brain regions, enabling the model to capture biologically meaningful topological patterns. We evaluate our BrainATCL on two tasks: functional link prediction and age estimation. The experimental results demonstrate superior performance and strong generalization, including in cross-session prediction scenarios.

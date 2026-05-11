# Sparse Bayesian Modeling of EEG Channel Interactions Improves P300 Brain-Computer Interface Performance

**Source**: semantic-scholar
**ID**: 91ad0d00c9f950780669f6262df4e9c7f6f42150
**DOI**: 10.48550/arXiv.2602.17772
**URL**: https://www.semanticscholar.org/paper/91ad0d00c9f950780669f6262df4e9c7f6f42150
**Date**: 2026-02-19
**Year**: 2026
**Authors**: Guoxuan Ma, Yuan Zhong, Moyan Li, Yuxiao Nie, Jian Kang
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Electroencephalography (EEG)-based P300 brain-computer interfaces (BCIs) enable communication without physical movement by detecting stimulus-evoked neural responses. Accurate and efficient decoding remains challenging due to high dimensionality, temporal dependence, and complex interactions across EEG channels. Most existing approaches treat channels independently or rely on black-box machine learning models, limiting interpretability and personalization. We propose a sparse Bayesian time-varying regression framework that explicitly models pairwise EEG channel interactions while performing automatic temporal feature selection. The model employs a relaxed-thresholded Gaussian process prior to induce structured sparsity in both channel-specific and interaction effects, enabling interpretable identification of task-relevant channels and channel pairs. Applied to a publicly available P300 speller dataset of 55 participants, the proposed method achieves a median character-level accuracy of 100\% using all stimulus sequences and attains the highest overall decoding performance among competing statistical and deep learning approaches. Incorporating channel interactions yields subgroup-specific gains of up to 7\% in character-level accuracy, particularly among participants who abstained from alcohol (up to 18\% improvement). Importantly, the proposed method improves median BCI-Utility by approximately 10\% at its optimal operating point, achieving peak throughput after only seven stimulus sequences. These results demonstrate that explicitly modeling structured EEG channel interactions within a principled Bayesian framework enhances predictive accuracy, improves user-centric throughput, and supports personalization in P300 BCI systems.

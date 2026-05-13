# Dynamic Causal Connectivity and Topological Augmentation for Spiking Neural Emotion Classification

**Source**: semantic-scholar
**ID**: 98202f3518c3759a264d92b504d38c07ace06218
**DOI**: 10.1109/ICACRS67045.2025.11324205
**URL**: https://www.semanticscholar.org/paper/98202f3518c3759a264d92b504d38c07ace06218
**Date**: 2025-12-10
**Year**: 2025
**Authors**: Benson K Shiju, Angelin Jeba P, N. V. Babu
**Venue**: 2025 4th International Conference on Automation, Computing and Renewable Systems (ICACRS)
**Citations**: 0

## Abstract

Emotion recognition from electroencephalogram (EEG) signals has become increasingly important for understanding human affective states in applications ranging from human-computer interaction to healthcare. This study presents a stepwise approach for EEG-based emotion recognition that integrates signal processing, data augmentation, feature extraction, and classification. Experiments were conducted using the DEAP dataset, which provides high-quality EEG recordings alongside self-reported emotional states across six categories: Happy, Sad, Calm, Fear, Angry, and Surprise. Raw EEG signals were first denoised using wavelet-based adaptive thresholding to remove noise while preserving meaningful neural activity. To improve generalization and address dataset limitations, Topological Data Analysis (TDA) was applied to generate realistic signal variations by manipulating underlying topological structures. Dynamic Causal Modeling (DCM) was employed for feature extraction, capturing inter-regional neural interactions to provide a richer representation of brain dynamics associated with different emotions. Feature selection was performed using mutual information with redundancy minimization to retain the most informative and non-redundant features. Classification was carried out using a Spiking Neural Network (SNN), a biologically inspired model that processes temporal spike patterns, with the neuron exhibiting the strongest activity determining the predicted emotion. Following hyperparameter tuning, including adjustments to membrane thresholds and spike timing resolution, the proposed approach achieved a peak accuracy of 94.1% across all six emotion categories. These results demonstrate that the integration of advanced signal processing techniques with biologically inspired computational models can effectively capture the complex temporal dynamics of EEG signals for robust emotion recognition.

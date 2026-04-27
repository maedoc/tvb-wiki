# A Hybrid Learning Approach for Detection of Autism Spectrum Disorder Using fMRI Data

**Source**: semantic-scholar
**ID**: e08252ec3941a652634214c5b9e7ec3b5739910b
**DOI**: 10.1109/JAC-ECC67970.2025.11417627
**URL**: https://www.semanticscholar.org/paper/e08252ec3941a652634214c5b9e7ec3b5739910b
**Date**: 2025-12-15
**Year**: 2025
**Authors**: Mennahtullah Mabrouk, Reem Reda, Hana Hisham, Abdelrahman Hazem, Bola Hosny, Hossam Elsawaf, Saif Elaswad, Sameh Sherif
**Venue**: 2025 13th International Japan-Africa Conference on Electronics, Communications, and Computations (JAC-ECC)
**Citations**: 0

## Abstract

Functional magnetic resonance imaging (fMRI) is a critical tool for studying brain activity through blood oxygen level-dependent (BOLD) signals. This study developed a machine learning pipeline to classify autism spectrum disorder (ASD) using resting-state fMRI data from the ABIDE dataset. Unlike conventional deep learning approaches employing CNNs/RNNs, our method focused on functional connectivity features extracted from correlation matrices of time-series data, processed through a shallow neural network (MLP). The pipeline incorporated automated preprocessing with Nilearn’s NiftiMasker, dimensionality reduction using PCA (5 components), and a logistic regression-like classifier with data augmentation via linear interpolation. The key findings showed that the model consistently assigned confidence scores of $\leq 62 \%$ to neurotypical controls, suggesting discriminative capacity for ASD. While limited by computational constraints necessitating simplified architectures, this work demonstrates the feasibility of lightweight machine learning for fMRI classification without complex deep learning models.

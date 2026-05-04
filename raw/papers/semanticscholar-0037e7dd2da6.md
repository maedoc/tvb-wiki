# Neuro Graph-ASD: A Graph-Based Deep Learning for Neuroimaging-Driven ASD Diagnosis

**Source**: semantic-scholar
**ID**: 0037e7dd2da637c689ae45d36432619ca73cafe6
**DOI**: 10.59256/indjcst.20250402003
**URL**: https://www.semanticscholar.org/paper/0037e7dd2da637c689ae45d36432619ca73cafe6
**Date**: 2025-05-05
**Year**: 2025
**Authors**: Shalini Ranjan, S. Ramesh, Keerthi Mj, Disha Gowda, S. Shet
**Venue**: Indian Journal of Computer Science and Technology
**Citations**: 0

## Abstract

Autism Spectrum Disorder (ASD) is a neurodevelopmental disorder with disrupted patterns of brain connectivity. Leveraging the
recent progress in graph-based deep learning, this paper introduces a Graph Convolutional Network (GCN) approach to ASD diagnosis from
resting-state functional magnetic resonance imaging (rs-fMRI) data. Functional connectivity matrices were derived from the Autism Brain
Imaging Data Exchange (ABIDE) dataset of 1,112 subjects across 17 sites of acquisition. The brain was parcellated into 110 regions of interest
based on the Harvard-Oxford atlas, and pairwise Pearson correlation coefficients of region-wise time series were estimated to build subject-
specific connectivity fingerprints. Recursive Feature Elimination with linear Support Vector Machine (RFE-SVM) was used to dimensionality
reduction retaining most informative connectivity features. A population graph was built based on feature similarities as well as phenotypic
metadata (age, site, gender). Node features were propagated on the graph using a two-layer GCN, and a multi-layer perceptron classifier
output ASD or typical control labels. The model attained a classification accuracy of 80% on a held-out validation set, showing graph-based
learning could detect subtle inter-subject patterns in neuroimaging data. This method indicates the utility of combining functional connectivity
with demographic information to obtain robust and interpretable ASD classification.

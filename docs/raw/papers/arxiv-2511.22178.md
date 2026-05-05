# Enhanced Graph Convolutional Network with Chebyshev Spectral Graph and Graph Attention for Autism Spectrum Disorder Classification

**Source**: semantic-scholar
**ID**: dd7a172a1490a481db67ff33f10e2ada0ae4a7bb
**DOI**: 10.1109/IVCNZ67716.2025.11281859
**URL**: https://www.semanticscholar.org/paper/dd7a172a1490a481db67ff33f10e2ada0ae4a7bb
**Date**: 2025-11-19
**Year**: 2025
**Authors**: Adnan Ferdous Ashrafi, H. Kabir
**Venue**: Image and Vision Computing New Zealand
**Citations**: 1

## Abstract

ASD is a complicated neurodevelopmental disorder marked by variation in symptom presentation and neurological underpinnings, making early and objective diagnosis extremely problematic. This paper presents a Graph Convolutional Network (GCN) model, incorporating Chebyshev Spectral Graph Convolution and Graph Attention Networks (GAT), to increase the classification accuracy of ASD utilizing multimodal neuroimaging and phenotypic data. Leveraging the ABIDE I dataset, which contains resting-state functional MRI (rs-fMRI), structural MRI (sMRI), and phenotypic variables from 870 patients, the model leverages a multi-branch architecture that processes each modality individually before merging them via concatenation. Graph structure is encoded using site-based similarity to generate a population graph, which helps in understanding relationship connections across individuals. Chebyshev polynomial filters provide localized spectral learning with lower computational complexity, whereas GAT layers increase node representations by attention-weighted aggregation of surrounding information. The proposed model is trained using stratified five-fold cross-validation with a total input dimension of 5,206 features per individual. Extensive trials demonstrate the enhanced model's superiority, achieving a test accuracy of 74.82% and an AUC of 0.82 on the entire dataset, surpassing multiple state-of-the-art baselines, including conventional GCNs, autoencoder-based deep neural networks, and multimodal CNNs.

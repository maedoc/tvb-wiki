# A Framework for Comparison and Interpretation of Machine Learning Classifiers to Predict Autism on the ABIDE Dataset

**Source**: semantic-scholar
**ID**: dd80d856790cf40a18822380d81789cc2ec2a1e4
**DOI**: 10.1002/hbm.70190
**URL**: https://www.semanticscholar.org/paper/dd80d856790cf40a18822380d81789cc2ec2a1e4
**Date**: 2025-03-17
**Year**: 2025
**Authors**: Yilan Dong, D. Batalle, M. Deprez
**Venue**: Human Brain Mapping
**Citations**: 13

## Abstract

Autism is a neurodevelopmental condition affecting ~1% of the population. Recently, machine learning models have been trained to classify participants with autism using their neuroimaging features, though the performance of these models varies in the literature. Differences in experimental setup hamper the direct comparison of different machine‐learning approaches. In this paper, five of the most widely used and best‐performing machine learning models in the field were trained to classify participants with autism and typically developing (TD) participants, using functional connectivity matrices, structural volumetric measures, and phenotypic information from the Autism Brain Imaging Data Exchange (ABIDE) dataset. Their performance was compared under the same evaluation standard. The models implemented included: graph convolutional networks (GCN), edge‐variational graph convolutional networks (EV‐GCN), fully connected networks (FCN), autoencoder followed by a fully connected network (AE‐FCN) and support vector machine (SVM). Our results show that all models performed similarly, achieving a classification accuracy around 70%. Our results suggest that different inclusion criteria, data modalities, and evaluation pipelines rather than different machine learning models may explain variations in accuracy in the published literature. The highest accuracy in our framework was obtained when using ensemble models (p < 0.001), leading to an accuracy of 72.2% and AUC = 0.77 using GCN classifiers. However, an SVM classifier performed with an accuracy of 70.1% and AUC = 0.77, just marginally below GCN, and significant differences were not found when comparing different algorithms under the same testing conditions (p > 0.05). Furthermore, we also investigated the stability of features identified by the different machine learning models using the SmoothGrad interpretation method. The FCN model demonstrated the highest stability in selecting relevant features contributing to model decision making. The code is available at https://github.com/YilanDong19/Machine‐learning‐with‐ABIDE.

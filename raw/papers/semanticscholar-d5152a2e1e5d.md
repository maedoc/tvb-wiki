# BrainTract: segmentation of white matter fiber tractography and analysis of structural connectivity using hybrid convolutional neural network.

**Source**: semantic-scholar
**ID**: d5152a2e1e5db448f8dccd20c8e407517485c9ff
**DOI**: 10.1016/j.neuroscience.2025.06.043
**URL**: https://www.semanticscholar.org/paper/d5152a2e1e5db448f8dccd20c8e407517485c9ff
**Date**: 2025-06-01
**Year**: 2025
**Authors**: P. R. Kumar, B. Shilpa, Rajesh Kumar Jha
**Venue**: Neuroscience
**Citations**: 3

## Abstract

Tractography uses diffusion Magnetic Resonance Imaging (dMRI) to noninvasively reconstruct brain white matter (WM) tracts, with Convolutional Neural Network (CNNs) like U-Net significantly advancing accuracy in medical image segmentation. This work proposes a metaheuristic optimization algorithm-based CNN architecture. This architecture combines the Inception-ResNet-V2 module and the densely connecting convolutional module (DI) into the Spatial Attention U-Net (SAU-Net) architecture for segmenting WM fiber tracts and analyzing the brain's structural connectivity. The proposed network model (DISAU-Net) consists of the following parts are; First, the Inception-ResNet-V2 block is used to replace the standard convolutional layers and expand the network's width; Second, the Dense-Inception block is used to extract features and deepen the network without the need for any additional parameters; Third, the down-sampling block is used to speed up training by decreasing the size of feature maps, and the up-sampling block is used to increase the maps' resolution. In addition, the parameter existing in the classifiers is randomly selected with the Gray Wolf Optimization (GWO) technique to boost the performance of the CNN architecture. We validated our method by segmenting WM tracts on dMRI scans of 280 subjects from the human connectome project (HCP) database. The proposed method is far more efficient than current methods. It offers unprecedented quantitative evaluation with high tract segmentation consistency, achieving accuracy of 97.10%, dice score of 96.88%, recall 95.74%, f1-score 94.79% for fiber tracts. The results showed that the proposed method is a potential approach for segmenting WM fiber tracts and analyzing the brain's structural connectivity.

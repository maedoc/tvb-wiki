# Towards an Informed Choice of Diffusion MRI Image Contrasts for Cerebellar Segmentation

**Source**: semantic-scholar
**ID**: 2c08584d27f961345b2c42eca2a7afd8165d0d4f
**DOI**: 10.1002/hbm.70317
**URL**: https://www.semanticscholar.org/paper/2c08584d27f961345b2c42eca2a7afd8165d0d4f
**Date**: 2025-03-11
**Year**: 2025
**Authors**: Jon Haitz Legarreta, Zhou Lan, Yuqian Chen, Fan Zhang, Edward H. Yeterian, N. Makris, Jarrett Rushmore, Y. Rathi, L. O’Donnell
**Venue**: bioRxiv
**Citations**: 1

## Abstract

The fine-grained segmentation of cerebellar structures is an essential step towards supplying increasingly accurate anatomically informed analyses, including, for example, white matter diffusion magnetic resonance imaging (MRI) tractography. Cerebellar tissue segmentation is typically performed on structural magnetic resonance imaging data, such as T1-weighted data, while connectivity between segmented regions is mapped using diffusion MRI tractography data. Small deviations in structural to diffusion MRI data co-registration may negatively impact connectivity analyses. Reliable segmentation of brain tissue performed directly on diffusion MRI data helps to circumvent such inaccuracies. Diffusion MRI enables the computation of many image contrasts, including a variety of tissue microstructure maps. While multiple methods have been proposed for the segmentation of cerebellar structures using diffusion MRI, little attention has been paid to the systematic evaluation of the performance of different available input image contrasts for the segmentation task. In this work, we evaluate and compare the segmentation performance of diffusion MRI-derived contrasts on the cerebellar segmentation task. Specifically, we include spherical mean (diffusion-weighted image average) and b0 (non-diffusion-weighted image average) contrasts, local signal parameterization contrasts (diffusion tensor and kurtosis fit maps), and the structural T1-weighted MRI contrast that is most commonly employed for the task. We train a popular deep-learning architecture using a publicly available dataset (HCP-YA), leveraging cerebellar region labels from the atlas-based SUIT cerebellar segmentation pipeline. By training and testing using many diffusion-MRI-derived image inputs, we find that the spherical mean image computed from b=1000 s/mm2 shell data provides stable performance across different metrics and significantly outperforms the tissue microstructure contrasts that are traditionally used in machine learning segmentation methods for diffusion MRI. Key points We provide evidence about the performance of different dMRI contrasts for cerebellar structure segmentation using a deep learning neural network. The diffusion MRI spherical mean provides improved and stable cerebellar structure segmentation performance. The spherical mean is easy to compute and can be used for cerebellar structure segmentation on retrospective clinical diffusion MRI data.

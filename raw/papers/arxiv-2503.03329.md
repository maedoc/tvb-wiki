# Deep Learning-Based Diffusion MRI Tractography: Integrating Spatial and Anatomical Information

**Source**: semantic-scholar
**ID**: 25c2916357e0e3d161e575fd133ad7386938ee2f
**DOI**: 10.48550/arXiv.2503.03329
**URL**: https://www.semanticscholar.org/paper/25c2916357e0e3d161e575fd133ad7386938ee2f
**Date**: 2025-03-05
**Year**: 2025
**Authors**: Yiqiong Yang, Yitian Yuan, Baoxing Ren, Ye Wu, Yanqiu Feng, Xinyuan Zhang
**Venue**: NeuroImage
**Citations**: 2

## Abstract

Diffusion MRI tractography technique enables non-invasive visualization of the white matter pathways in the brain. It plays a crucial role in neuroscience and clinical fields by facilitating the study of brain connectivity and neurological disorders. However, the accuracy of reconstructed tractograms has been a longstanding challenge. Recently, deep learning methods have been applied to improve tractograms for better white matter coverage, but often comes at the expense of generating excessive false-positive connections. This is largely due to their reliance on local information to predict long-range streamlines. To improve the accuracy of streamline propagation predictions, we introduce a novel deep learning framework that integrates image-domain spatial information and anatomical information along tracts, with the former extracted through convolutional layers and the latter modeled via a Transformer-decoder. Additionally, we employ a weighted loss function to address fiber class imbalance encountered during training. We evaluate the proposed method on the simulated ISMRM 2015 Tractography Challenge dataset, achieving a valid streamline rate of 66.2 %, white matter coverage of 63.8 %, and successfully reconstructing 24 out of 25 bundles. Furthermore, on the multi-site Tractoinferno dataset, the proposed method demonstrates its ability to handle various diffusion MRI acquisition schemes, achieving a 5.7 % increase in white matter coverage and a 4.1 % decrease in overreach compared to RNN-based methods.

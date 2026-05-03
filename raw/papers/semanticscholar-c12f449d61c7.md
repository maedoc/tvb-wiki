# LFE-UNet: A Lightweight Full-Encoder U-shaped Network for Efficient Semantic Segmentation in Medical Imaging.

**Source**: semantic-scholar
**ID**: c12f449d61c7bd632951367f43e0d7f909b13442
**DOI**: 10.2174/0115734056370555250426140155
**URL**: https://www.semanticscholar.org/paper/c12f449d61c7bd632951367f43e0d7f909b13442
**Date**: 2025-05-08
**Year**: 2025
**Authors**: Qinghua Zhang, Yulei Hou, Changchun He, Zhengyu Zhai, Yunjiao Deng
**Venue**: Current medical imaging
**Citations**: 0

## Abstract

BACKGROUND
Semantic segmentation algorithms are essential for identifying and segmenting human organs and lesions in medical images. However, as U-Net variants enhance segmentation accuracy, they often increase in parameter count, demanding more sophisticated and costly hardware for training.


OBJECTIVE
This study aims to introduce a lightweight U-Net that optimizes the trade-off between network parameters and segmentation accuracy, while fully leveraging the encoder's feature extraction capabilities.


METHODS
We propose a lightweight full-encoder U-shaped network, termed LFE-UNet, which employs full-encoder skip connections, encompassing all encoder layers. This model is designed with a reduced number of basic channels-specifically, 8 instead of the typical 64 or 32-to achieve a more efficient architecture.


RESULTS
The LFE-UNet, when integrated with ResNet34, achieved a Dice score of 0.97385 on the ISBI LiTS 2017 liver dataset. For the BraTS 2018 brain tumor dataset, it obtained 0.87510, 0.93759, 0.87301, and 0.81469 on average, WT, TC, and ET, respectively. The paper also discusses the impact of varying basic channel numbers n and encoder layer counts N on the network's parameter efficiency, as well as the model's robustness to different levels of Gaussian noise in images and salt and pepper noise in labels. Additionally, the influence of different loss functions is explored.


CONCLUSION
The LFE-UNet proves that high segmentation accuracy can be attained with a markedly lower parameters, fully utilizing the full-scale encoder's feature extraction. It also highlights the significance of loss function selection and the effects of noise on segmentation accuracy.

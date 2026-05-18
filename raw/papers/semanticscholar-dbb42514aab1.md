# Exploring temporal information dynamics in Spiking Neural Networks: Fast Temporal Efficient Training.

**Source**: semantic-scholar
**ID**: dbb42514aab1638bc6a2d64c13b6c4d9125672a2
**DOI**: 10.1016/j.jneumeth.2025.110401
**URL**: https://www.semanticscholar.org/paper/dbb42514aab1638bc6a2d64c13b6c4d9125672a2
**Date**: 2025-02-01
**Year**: 2025
**Authors**: Changjiang Han, Li‐Juan Liu, H R Karimi
**Venue**: Journal of Neuroscience Methods
**Citations**: 1

## Abstract

BACKGROUND
Spiking Neural Networks (SNNs) hold significant potential in brain simulation and temporal data processing. While recent research has focused on developing neuron models and leveraging temporal dynamics to enhance performance, there is a lack of explicit studies on neuromorphic datasets. This research aims to address this question by exploring temporal information dynamics in SNNs.


NEW METHOD
To quantify the dynamics of temporal information during training, this study measures the Fisher information in SNNs trained on neuromorphic datasets. The information centroid is calculated to analyze the influence of key factors, such as the parameter k, on temporal information dynamics.


RESULTS
Experimental results reveal that the information centroid exhibits two distinct behaviors: stability and fluctuation. This study terms this phenomenon the Stable Information Centroid (SIC), which is closely related to the parameter k. Based on these findings, we propose the Fast Temporal Efficient Training (FTET) algorithm.


COMPARISON WITH EXISTING METHODS
Firstly, the method proposed in this paper does not require the introduction of additional complex training techniques. Secondly, it can reduce the computational load by 30% in the final 50 epochs. However, the drawback is the issue of slow convergence during the early stages of training.


CONCLUSION
This study reveals that the learning processes of SNNs vary across different datasets, providing new insights into the mechanisms of human brain learning. A limitation is the restricted sample size, focusing only on a few datasets and image classification tasks. The code is available at https://github.com/gtii123/fast-temporal-efficient-training.

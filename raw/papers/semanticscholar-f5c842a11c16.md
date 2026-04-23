# Coronal Mass Ejection Transit Time Prediction Based on Spatiotemporal Modeling Using 3D Convolutional Neural Networks

**Source**: semantic-scholar
**ID**: f5c842a11c167b58a98b6e55badd083b0ad193e0
**DOI**: 10.3847/1538-4357/ae3c79
**URL**: https://www.semanticscholar.org/paper/f5c842a11c167b58a98b6e55badd083b0ad193e0
**Date**: 2026-02-20
**Year**: 2026
**Authors**: Weihong Zhou, Weihong Zhou, Yun Yang, Jie Cao, Zong-Yuan Ge, Tingting Xu, P. E., Yuxia Liu, Shangxi Li, Xueliang Zhou, Yuan Zhao, S. Xiong, Ye Dong
**Venue**: Astrophysical Journal
**Citations**: 0

## Abstract

Coronal mass ejections (CMEs) are intense solar eruptions that, once reaching Earth, pose catastrophic risks to the near-Earth space environment. Thus, improving CME transit time forecast accuracy to mitigate damage to ground-based facilities is critical for space weather forecasting. In this study, we constructed a 3D convolutional neural network (3D CNN) framework that learns from Solar and Heliospheric Observatory Large Angle and Spectrometric Coronagraph white-light image sequences to predict CME transit times. Our main contributions are threefold. (1) Unlike prior work, we first integrate the temporal dimension and use 3D CNN for joint spatiotemporal modeling of CME sequences to predict transit times. (2) To address the uneven sequence-length variations across events and to optimize data set usage, we propose a method that samples multiple fixed-length subsequences for each event and applies mean pooling to their features, which enhances model performance and generalization. (3) To enhance interpretability, we apply gradient-weighted class activation mapping across all convolutional layers to reveal each layer’s attention focus. The results show that shallow layers focus on the CME body and evolve over time, while deeper layers show stronger responses in the background and weaker responses to the CME body. On an independent test set, the model achieves a mean absolute error (MAE) of 11.04 hr; in the transit time range with the most samples, MAE is 6.37 hr, comparable to prior studies. These results confirm 3D CNN’s effectiveness in modeling CME spatiotemporal evolution and predicting transit times, offering a promising path for physically interpretable, data-driven space weather forecasting.

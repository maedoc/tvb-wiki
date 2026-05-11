# 6D Pose Estimation via Keypoint Heatmap Regression with RGB-D Residual Neural Networks

**Source**: arxiv
**ID**: 2605.08059
**URL**: https://arxiv.org/abs/2605.08059
**Date**: 2026-05-08
**Year**: 2026
**Authors**: Ismail Aljosevic, Amir Masoud Almasi, Ana Parovic, Ashkan Shafiei
**Categories**: cs.CV, cs.RO

## Abstract

In this paper, we propose a modular framework for 6D pose estimation based on keypoint heatmap regression. Our approach combines YOLOv10m for object detection with a ResNet18-based network that predicts 2D heatmaps from RGB images. Keypoints extracted from these heatmaps are used to estimate the 6D object pose via the PnP RANSAC algorithm. We compare different keypoint selection strategies to assess their impact on pose accuracy. Additionally, we extend the baseline by incorporating depth data using a cross-fusion architecture, which enables interaction between RGB and depth features at multiple stages. We further explore general training improvements, such as experimenting with activation functions and learning rate scheduling strategies to improve model performance. Our best RGB-only model achieved a mean ADD-based accuracy of 84.50%, while the RGB-D fusion model reached 92.41% on the LINEMOD dataset. The code is available at https://github.com/ameermasood/HeatNet.

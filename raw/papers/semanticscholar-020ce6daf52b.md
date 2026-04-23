# Research on the establishment of a four-classification model for breast mass ultrasound images based on transfer learning

**Source**: semantic-scholar
**ID**: 020ce6daf52b26bcc5d021e6e238bb9de26320f8
**DOI**: 10.1371/journal.pone.0340111
**URL**: https://www.semanticscholar.org/paper/020ce6daf52b26bcc5d021e6e238bb9de26320f8
**Date**: 2026-01-05
**Year**: 2026
**Authors**: Jinlao Li, Bo Zhao, Yongqi Chen, Guang-Yi Wang, Xueliang Tian, Shuyu Zhou
**Venue**: PLoS ONE
**Citations**: 0

## Abstract

Breast mass classification via ultrasound is critical for early diagnosis but remains challenging due to overlapping morphological features. This study evaluates the efficacy of optimized transfer learning (TL) based on deep convolutional neural networks (DCNNs) in distinguishing four breast mass categories: invasive ductal carcinoma (IDC), fibroadenoma (FA), mucinous carcinoma (MC), and inflammatory mass (IM). Our approach comprises four key steps: (1) applying extensive data augmentation to a retrospective dataset of 346 ultrasound images from 294 patients (November 2021-March 2023) classified by pathological confirmation; (2) implementing transfer learning with five pretrained DCNN models (ResNet18, ResNet50, DenseNet121, MobileNetV2, GoogLeNet); (3) optimizing model hyperparameters for four-class classification; (4) comparing performance metrics (accuracy, precision, recall, F1-score, AUC-ROC) against two senior radiologists (8- and 10-years’ experience) on a held-out test set. Results: The DenseNet121 and GoogLeNet models demonstrated superior overall accuracy (0.912 and 0.926, respectively), significantly outperforming the radiologists’ consensus (0.691) (p < 0.01). In class-specific analysis, the optimized models achieved notably higher accuracy for IDC, MC, and IM. Statistical testing confirmed the significant performance improvement of the top models over human experts. Optimized TL with DCNNs, particularly DenseNet121 and GoogLeNet, enables highly accurate four-class breast mass classification in ultrasound images, surpassing expert radiologist performance with statistical significance. This approach holds promise for clinical decision support. Code is publicly available at https://github.com/jinlao777/BCC.

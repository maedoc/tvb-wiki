# Gaussian Connectivity-Driven EEG Imaging for Deep Learning-Based Motor Imagery Classification

**Source**: semantic-scholar
**ID**: b71523f8cfd8ba12a7b17b85ee57d723314c1a06
**DOI**: 10.3390/s26010227
**URL**: https://www.semanticscholar.org/paper/b71523f8cfd8ba12a7b17b85ee57d723314c1a06
**Date**: 2025-12-29
**Year**: 2025
**Authors**: Alejandra Gomez-Rivera, D. Collazos-Huertas, D. Cárdenas-Peña, A. Álvarez-Meza, G. Castellanos-Domínguez
**Venue**: Italian National Conference on Sensors
**Citations**: 0

## Abstract

Electroencephalography (EEG)-based motor imagery (MI) brain–computer interfaces (BCIs) hold considerable potential for applications in neuro-rehabilitation and assistive technologies. Yet, their development remains constrained by challenges such as low spatial resolution, vulnerability to noise and artifacts, and pronounced inter-subject variability. Conventional approaches, including common spatial patterns (CSP) and convolutional neural networks (CNNs), often exhibit limited robustness, weak generalization, and reduced interpretability. To overcome these limitations, we introduce EEG-GCIRNet, a Gaussian connectivity-driven EEG imaging representation network coupled with a regularized LeNet architecture for MI classification. Our method integrates raw EEG signals with topographic maps derived from functional connectivity into a unified variational autoencoder framework. The network is trained with a multi-objective loss that jointly optimizes reconstruction fidelity, classification accuracy, and latent space regularization. The model’s interpretability is enhanced through its variational autoencoder design, allowing for qualitative validation of its learned representations. Experimental evaluations demonstrate that EEG-GCIRNet outperforms state-of-the-art methods, achieving the highest average accuracy (81.82%) and lowest variability (±10.15) in binary classification. Most notably, it effectively mitigates BCI illiteracy by completely eliminating the “Bad” performance group (<60% accuracy), yielding substantial gains of ∼22% for these challenging users. Furthermore, the framework demonstrates good scalability in complex 5-class scenarios, performing competitive classification accuracy (75.20% ± 4.63) with notable statistical superiority (p = 0.002) against advanced baselines. Extensive interpretability analyses, including analysis of the reconstructed connectivity maps, latent space visualizations, Grad-CAM++ and functional connectivity patterns, confirm that the model captures genuine neurophysiological mechanisms, correctly identifying integrated fronto-centro-parietal networks in high performers and compensatory midline circuits in mid-performers. These findings suggest that EEG-GCIRNet provides a robust and interpretable end-to-end framework for EEG-based BCIs, advancing the development of reliable neurotechnology for rehabilitation and assistive applications.

# Transfer Learning for Improving Neuroimaging-Based Diagnostic Classification

**Source**: semantic-scholar
**ID**: 5441baebf3cdd82aa2ae1cfa3411c676039c91d5
**DOI**: 10.1109/TCBBIO.2025.3647485
**URL**: https://www.semanticscholar.org/paper/5441baebf3cdd82aa2ae1cfa3411c676039c91d5
**Date**: 2025-12-23
**Year**: 2025
**Authors**: Gopikrishna Deshpande, Bonian Lu, Nguyen Huynh, D. Rangaprakash
**Venue**: IEEE Transactions on Computational Biology and Bioinformatics
**Citations**: 0

## Abstract

Overfitting, an issue that constrains the validity and generalizability of machine learning in neuroimaging-based diagnostic-classification, is in part due to small sample sizes in relation to what is required for generalization. Even with data aggregation (such as in Autism Brain Imaging Data Exchange or ABIDE), the relatively smaller sample sizes are a result of the fact that it is difficult/expensive to acquire data from clinical populations. With healthy controls, we have comparatively larger samples available. Therefore, we propose to address overfitting by using larger healthy samples (from Human Connectome Project or HCP) to learn the diversity of neural signatures of healthy controls, with the aim of transferring that learning into the context of discriminating autism from healthy controls in ABIDE. Methods: We developed a complete variational autoencoder based transfer learning framework including data oversampling, model pre-training, classifier training and testing, and model explanation. Then, the performance of transfer learning was estimated and visualized. Results: The transfer learning classification model achieved about 7% more accuracy on site-mismatched data than obtained without transfer leaning. Discussion: Overall, we demonstrated the applicability of transfer learning within a deep learning framework for utilizing larger samples of available healthy control data to improve generalizability and accuracy of diagnostic classification in ASD, as well as reduce the harmful effects of inter-site variability on classification. We believe the proposed framework is potentially applicable to other disorders as well.

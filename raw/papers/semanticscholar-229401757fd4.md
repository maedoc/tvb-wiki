# Hierarchical Tissue-Based MRI Features with Explainable Machine Learning for Alzheimer’s Disease Classification

**Source**: semantic-scholar
**ID**: 229401757fd4258724f1ae8ff9b56bf3ea2293c0
**DOI**: 10.25077/jif.18.1.93-104.2026
**URL**: https://www.semanticscholar.org/paper/229401757fd4258724f1ae8ff9b56bf3ea2293c0
**Date**: 2026-03-01
**Year**: 2026
**Authors**: Muhammed Ceesay, A. H. Saputro, Syahril Siregar
**Venue**: JURNAL ILMU FISIKA | UNIVERSITAS ANDALAS
**Citations**: 0

## Abstract

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder characterized by multiscale structural brain degeneration. Many MRI-based machine learning approaches rely on coarse volumetric measures or black-box models with limited anatomical interpretability. This study aims to localize anatomically meaningful brain regions that discriminate AD from cognitively normal (CN) subjects using a hierarchical tissue-based (HTB) MRI framework. The method models gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) volumetric changes at lobar, gyral, and 246 fine-grained subregions defined by the Brainnetome atlas. T1-weighted MRI scans from 454 participants (227 AD, 227 CN) obtained from ADNI and MIRIAD were preprocessed using AC-PC alignment, N4 bias correction, skull stripping, and nonlinear registration to MNI space. A total of 561 HTB features were extracted to train Random Forest and XGBoost classifiers using five-fold stratified cross-validation with Bayesian hyperparameter optimization. The XGBoost model achieved the best performance (Accuracy: 79.74%, ROC-AUC: 85.07%), comparable to recent atlas-based MRI classification studies, while providing improved multiscale anatomical interpretability. SHAP analysis revealed consistent hierarchical atrophy patterns in hippocampal subregions, medial amygdala, and areas 35/36 and 28/34, demonstrating that hierarchical anatomical modeling with explainable machine learning enables transparent localization of clinically meaningful AD biomarkers without reliance on black-box architectures.

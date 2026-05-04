# SURG-95. Spectral Imaging and AI for Brain Tumor Characterization: Toward Data-Driven Surgical Guidance

**Source**: semantic-scholar
**ID**: cd1c97ab84116998e4ef778b90a759540e909984
**DOI**: 10.1093/neuonc/noaf201.1647
**URL**: https://www.semanticscholar.org/paper/cd1c97ab84116998e4ef778b90a759540e909984
**Date**: 2025-11-01
**Year**: 2025
**Authors**: Eric Suero Molina, D. Black
**Venue**: Neuro-Oncology
**Citations**: 0

## Abstract


 Precise delineation of brain tumor margins remains a clinical challenge, even with the aid of 5-aminolevulinic acid (5-ALA) fluorescence guidance — particularly in low-grade gliomas or infiltrative zones where visible fluorescence is weak or absent. Hyperspectral imaging (HSI), which captures detailed spectral data per pixel, offers the potential for refined tissue characterization based on spectral signatures. However, converting raw spectral data into clinically meaningful overlays involves complex processing, which can be optimized through machine- and deep learning. We developed a data-driven pipeline for ex vivo hyperspectral fluorescence imaging of brain tumor biopsies. The workflow comprises automatic biopsy segmentation, spectral feature extraction, and deep learning-based normalization to correct for optical variability across samples. Spectral unmixing is then applied to estimate the relative abundance of key fluorophores, including PpIX and various autofluorescent compounds. These abundance profiles serve as input features for machine learning classifiers trained to predict tumor type, WHO grade, margin type, and IDH mutation status. The dataset consists of 891 hyperspectral image cubes from 184 patients with diverse brain tumor pathologies. Deep neural networks enhanced the normalization process by accounting for complex, tissue-specific optical properties, leading to more robust abundance estimations. Classifiers trained on the processed spectral data achieved test accuracies of 87.3% (tumor type), 96.1% (WHO grade), 85.7% (tumor margin), and 93% (IDH mutation), surpassing the performance of previous non-fluorescence-based methods. The integration of deep learning for normalization and both classical and machine learning-based unmixing significantly enhanced data interpretability. We demonstrate that HSI, when combined with deep learning-based normalization and data-driven analysis, enables accurate classification of key brain tumor features. The fusion of spectral unmixing and machine learning facilitates the extraction of molecular and histopathological signatures, offering real-time potential to support surgical decision-making. These results underscore the clinical value of integrating AI with HSI for fluorescence-guided brain tumor resection.

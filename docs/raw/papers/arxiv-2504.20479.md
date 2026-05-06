# Full-field surrogate modeling of cardiac function encoding geometric variability

**Source**: semantic-scholar
**ID**: b59500d4b9cc42ffd796d32ea5ad4643fb50075a
**DOI**: 10.48550/arXiv.2504.20479
**URL**: https://www.semanticscholar.org/paper/b59500d4b9cc42ffd796d32ea5ad4643fb50075a
**Date**: 2025-04-29
**Year**: 2025
**Authors**: E. Martinez, Beatrice Moscoloni, Matteo Salvador, Fanwei Kong, M. Peirlinck, A. Marsden
**Venue**: arXiv.org
**Citations**: 2

## Abstract

Combining physics-based modeling with data-driven methods is critical to enabling the translation of computational methods to clinical use in cardiology. The use of rigorous differential equations combined with machine learning tools allows for model personalization with uncertainty quantification in time frames compatible with clinical practice. However, accurate and efficient surrogate models of cardiac function, built from physics-based numerical simulation, are still mostly geometry-specific and require retraining for different patients and pathological conditions. We propose a novel computational pipeline to embed cardiac anatomies into full-field surrogate models. We generate a dataset of electrophysiology simulations using a complex multi-scale mathematical model coupling partial and ordinary differential equations. We adopt Branched Latent Neural Maps (BLNMs) as an effective scientific machine learning method to encode activation maps extracted from physics-based numerical simulations into a neural network. Leveraging large deformation diffeomorphic metric mappings, we build a biventricular anatomical atlas and parametrize the anatomical variability of a small and challenging cohort of 13 pediatric patients affected by Tetralogy of Fallot. We propose a novel statistical shape modeling based z-score sampling approach to generate a new synthetic cohort of 52 biventricular geometries that are compatible with the original geometrical variability. This synthetic cohort acts as the training set for BLNMs. Our surrogate model demonstrates robustness and great generalization across the complex original patient cohort, achieving an average adimensional mean squared error of 0.0034. The Python implementation of our BLNM model is publicly available under MIT License at https://github.com/StanfordCBCL/BLNM.

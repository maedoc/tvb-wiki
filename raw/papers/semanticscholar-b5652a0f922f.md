# Revealing Cortical Spreading Pathway of Neuropathological Events by Neural Optimal Mass Transport

**Source**: semantic-scholar
**ID**: b5652a0f922ffe4c81ef87f3354cd8af133e304f
**DOI**: 10.1109/TMI.2025.3558691
**URL**: https://www.semanticscholar.org/paper/b5652a0f922ffe4c81ef87f3354cd8af133e304f
**Date**: 2025-04-07
**Year**: 2025
**Authors**: Tingting Dan, Yanquan Huang, Yang Yang, Guorong Wu
**Venue**: IEEE Transactions on Medical Imaging
**Citations**: 1

## Abstract

Positron Emission Tomography (PET) is essential for understanding the pathophysiological mechanisms underlying neurodegenerative diseases like Alzheimer’s disease (AD). However, existing approaches primarily focus on stereotypical patterns of pathology burden, lacking the ability to elucidate the underlying propagation mechanisms by which pathologies spread throughout the brain over time. Given that many neurodegenerative diseases exhibit prion-like pathology spread, it is essential to uncover the spot-to-spot flow field between consecutive PET snapshots. To address this, we reformulate the problem of identifying latent cortical propagation pathways of neuropathological burden within the well-established framework of optimal mass transport (OMT). In this formulation, the dynamic spreading of pathology across longitudinal PET scans is inherently constrained by the geometry of the brain cortex. To solve this problem, we introduce a variational framework that characterizes the dynamical system of pathology propagation in the brain, ultimately reducing to a Wasserstein geodesic between two density distributions of pathology accumulation. Furthermore, we hypothesize that a well-characterized mechanism of pathology propagation will enable the prediction of future pathology accumulation at the individual level, paving the way for personalized disease progression modeling. Building on the principles of physics-informed deep models, we derive the governing equation of the underlying OMT model and introduce an explainable, generative adversarial network-inspired framework. Our approach (1) parameterizes population-level OMT dynamics through a flow adjuster and (2) predicts the spreading flow in unseen subjects using a trained flow driver. We validate the accuracy of our model on publicly available datasets, demonstrating its effectiveness in forecasting future pathology accumulation. Since our deep model adheres to the second law of thermodynamics, we further explore the propagation dynamics of tau aggregates throughout the progression of AD. In contrast to traditional methods, our physics-informed approach enhances both accuracy and interpretability, demonstrating its potential to reveal novel neurobiological mechanisms driving disease progression.

# Task-Aware Effective Connectivity Modeling for Cognitive Function Prediction.

**Source**: semantic-scholar
**ID**: afa37fa723e5659bdbeb7339940e8ff6b8c227fd
**DOI**: 10.1109/JBHI.2025.3644481
**URL**: https://www.semanticscholar.org/paper/afa37fa723e5659bdbeb7339940e8ff6b8c227fd
**Date**: 2025-12-15
**Year**: 2025
**Authors**: Wantong Zou, Yu Li, Xiang Hu, Xun Chen, Aiping Liu
**Venue**: IEEE journal of biomedical and health informatics
**Citations**: 0

## Abstract

Effective connectivity (EC) derived from resting-state Functional Magnetic Resonance Imaging (rs fMRI) has emerged as a critical tool for deepening our understanding of brain function in both health and dis ease. However, most studies estimate EC on an individual basis, treating it as a hidden parameter within the model and requiring retraining the model for each subject. They often overlook the valuable population-level information and limit their generalizability. Additionally, EC is typically obtained independently of downstream tasks, reducing its capacity to effectively capture task-specific variations. To address these limitations, we propose a flexible Task-Aware Effective Connectivity (TAEC) model, designed to construct individualized, task-aware, and nonlinear causal brain networks without requiring subject-specific retraining. In this framework, a Causal Discovery Module (CDM) is introduced to capture the implicit neural representation of the EC by a spatial-temporal attention mechanism, producing the estimation of an individual EC. Subsequently, we propose a Task-Aware Graph Neural Network (GNN) Predictor, which incorporates a task-aware penalty to enable end-to-end prediction, enhancing task performance and the identification of task-dependent EC patterns. Extensive experiments on twelve cognitive tasks from the Human Connectome Project (HCP) dataset demonstrate that the proposed method achieves state-of-the-art performance, validating its effectiveness in task-aware effective connectivity modeling. Furthermore, the framework discovers discriminative and task-specific EC patterns, which offer additional in-sights into cognitive functions.

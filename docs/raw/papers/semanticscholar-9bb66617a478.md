# Bayesian time-history modeling enhances Parkinsonian motor state classification for adaptive deep brain stimulation

**Source**: semantic-scholar
**ID**: 9bb66617a47801b6d3ecf55d818e6697870d6d66
**DOI**: 10.1088/1741-2552/ae62a5
**URL**: https://www.semanticscholar.org/paper/9bb66617a47801b6d3ecf55d818e6697870d6d66
**Date**: 2026-04-21
**Year**: 2026
**Authors**: Brian Leung, Maria Shcherbakova, Jiaang Yao, Stephanie Cernera, C. Oehrn, Amelia Hahn, Simon J Little, Philip A Starr, L. Hammer
**Venue**: Journal of Neural Engineering
**Citations**: 0

## Abstract


 Objective: Adaptive deep brain stimulation (aDBS) for Parkinson’s disease is a recently-approved therapy that adjusts stimulation in response to neurophysiologic biomarkers of motor-symptom state. Most real-time implementations of aDBS rely on instantaneous, noise-susceptible classifiers that apply simple thresholds to neurophysiologic biomarkers. We examined whether incorporating temporal history through Bayesian state-space modeling improved motor-state classification compared to instantaneous discriminant classifiers. Approach: We analyzed naturalistic neural data from three patients with Parkinson’s disease chronically implanted with investigational sensing-enabled DBS systems, recording from both the subthalamic nucleus (STN) and sensorimotor cortex. Biomarkers were extracted across multiple window lengths and labeled using wearable-derived bradykinesia and dyskinesia scores. Classifier behavior was evaluated using two biomarkers (cortical stimulation-entrained gamma and STN beta oscillations) across a factorial combination of two conditions: (1) instantaneous discriminant analysis vs. Bayesian time-history modeling via hidden Markov models (HMMs), and (2) single Gaussian vs. Gaussian mixture modeling of each motor state’s biomarker distribution. Performance metrics included F1 scores, accuracy, prediction smoothness, latency, and computational load. Main Results: Using entrained-gamma biomarkers, incorporating time history via HMMs significantly improved hyperkinetic-state detection (F1: +12.9 ± 1.8%; accuracy: +30.0 ± 2.7%; both padj < 0.001) with modest decreases in hypokinetic-state performance, yielding a net increase in average F1 (+4.7 ± 0.9%, p < 0.001). HMMs also yielded smoother and more accurate predictions for a given latency compared to simply increasing the window length used to extract neurophysiologic biomarkers. Entrained-gamma biomarkers outperformed STN beta biomarkers across all classifiers (average F1: +12.9% ± 0.5%, p < 0.001). All methods operated within sub-millisecond prediction times and demonstrated sublinear empirical computational scaling. Significance: Bayesian time-history modeling enhanced motor-state classification while preserving the low latency and computational efficiency required for real-time aDBS. These findings, derived from chronic at-home recordings, support the translational potential of Bayesian state-space models for next-generation aDBS systems.

# An Energy-Efficient Spiking Neural Network Architecture for Predictive Insulin Delivery

**Source**: semantic-scholar
**ID**: d9469e02b9e0cd31149bdd2e8f0faa8764e9511c
**URL**: https://www.semanticscholar.org/paper/d9469e02b9e0cd31149bdd2e8f0faa8764e9511c
**Date**: 2026-03-29
**Year**: 2026
**Authors**: S. Shrivastava
**Citations**: 0

## Abstract

Diabetes mellitus affects over 537 million adults worldwide. Insulin-dependent patients require continuous glucose monitoring and precise dose calculation while operating under strict power budgets on wearable devices. This paper presents PDDS - an in-silico, software-complete research prototype of an event-driven computational pipeline for predictive insulin dose calculation. Motivated by neuromorphic computing principles for ultra-low-power wearable edge devices, the core contribution is a three-layer Leaky Integrate-and-Fire (LIF) Spiking Neural Network trained on 128,025 windows from OhioT1DM (66.5% real patients) and the FDA-accepted UVa/Padova physiological simulator (33.5%), achieving 85.90% validation accuracy. We present three rigorously honest evaluations: (1) a standard test-set comparison against ADA threshold rules, bidirectional LSTM (99.06% accuracy), and MLP (99.00%), where the SNN achieves 85.24% - we demonstrate this gap reflects the stochastic encoding trade-off, not architectural failure; (2) a temporal benchmark on 426 non-obvious clinician-annotated hypoglycemia windows where neither the SNN (9.2% recall) nor the ADA rule (16.7% recall) performs adequately, identifying the system's key limitation and the primary direction for future work; (3) a power-efficiency analysis showing the SNN requires 79,267x less energy per inference than the LSTM (1,551 Femtojoules vs. 122.9 nanojoules), justifying the SNN architecture for continuous wearable deployment. The system is not yet connected to physical hardware; it constitutes the computational middle layer of a five phase roadmap toward clinical validation. Keywords: spiking neural network, glucose severity classification, edge computing, hypoglycemia detection, event-driven architecture, LIF neuron, Poisson encoding, OhioT1DM, in-silico, neuromorphic, power efficiency.

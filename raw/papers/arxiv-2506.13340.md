# Probabilistic Modeling of Spiking Neural Networks with Contract-Based Verification

**Source**: semantic-scholar
**ID**: 35c10819e6c266a5427d501caf70b4f95b3db9f5
**DOI**: 10.48550/arXiv.2506.13340
**URL**: https://www.semanticscholar.org/paper/35c10819e6c266a5427d501caf70b4f95b3db9f5
**Date**: 2025-06-16
**Year**: 2025
**Authors**: Zhen Yao, Elisabetta De Maria, R. D. Simone
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Spiking Neural Networks (SNN) are models for"realistic"neuronal computation, which makes them somehow different in scope from"ordinary"deep-learning models widely used in AI platforms nowadays. SNNs focus on timed latency (and possibly probability) of neuronal reactive activation/response, more than numerical computation of filters. So, an SNN model must provide modeling constructs for elementary neural bundles and then for synaptic connections to assemble them into compound data flow network patterns. These elements are to be parametric patterns, with latency and probability values instantiated on particular instances (while supposedly constant"at runtime"). Designers could also use different values to represent"tired"neurons, or ones impaired by external drugs, for instance. One important challenge in such modeling is to study how compound models could meet global reaction requirements (in stochastic timing challenges), provided similar provisions on individual neural bundles. A temporal language of logic to express such assume/guarantee contracts is thus needed. This may lead to formal verification on medium-sized models and testing observations on large ones. In the current article, we make preliminary progress at providing a simple model framework to express both elementary SNN neural bundles and their connecting constructs, which translates readily into both a model-checker and a simulator (both already existing and robust) to conduct experiments.

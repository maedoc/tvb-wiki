# Dynamics-Informed Priors (DIP) for Neural Mass Modelling

**Source**: semantic-scholar
**ID**: abe3d0e1a71e3c8045159217196e4fa069ea83d4
**DOI**: 10.1101/2025.09.26.678721
**URL**: https://www.semanticscholar.org/paper/abe3d0e1a71e3c8045159217196e4fa069ea83d4
**Date**: 2025-09-29
**Year**: 2025
**Authors**: Alessia Caccamo, D. M. Dunstan, M. Richardson, Alexander D Shaw, M. Goodfellow
**Venue**: bioRxiv
**Citations**: 0

## Abstract

Neural Mass Models (NMMs) are important mathematical tools for inferring hidden neural mechanisms that generate healthy and pathological brain activities. A critical step in the inference process is parameter estimation, which calibrates NMMs based on measured neuroimaging data. While parameter estimation can be conducted via various approaches, one of the most influential methods is Dynamic Causal Modelling (DCM). DCM adopts a Bayesian inference approach that relies on, and is sensitive to, the specification of prior parameter distributions reflecting a priori hypotheses about the causes of data. However, most parameters of NMMs encode neuronal properties that are not directly measurable. For this reason, in the absence of sufficient empirical data and well-founded prior beliefs, inference becomes increasingly susceptible to bias. Therefore, it was imperative to establish a comprehensive strategy for mapping model parameters to data. This study proposes a computational extension of DCM, named DCM with dynamics-informed priors (DIP-DCM), which adopts a genetic algorithm (GA) to map parameter values to model dynamics. Optimal sub-regions of the parameter space were subsequently selected and translated into groups of parameter priors for DCM. DIP-DCM was compared to the ‘standard’ DCM inference and to the standalone GA, using two independent neuroimaging datasets. Results indicated that DIP-DCM models were the best predictors of data and captured key mechanistic signatures of psychiatric disease and pharmacological interventions. Overall, DIP-DCM addressed degeneracy, handled local minima, and explored diverse parameter regimes following trajectories informed directly by model dynamics and data. This study suggests that DIP-DCM is an advantageous route to parameter estimation when information is limited, enabling a data-driven derivation of parameter priors – or hypotheses – in exploratory studies, across different biological contexts and datasets.

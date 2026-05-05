# Predicting Nanoconfined Natural Gas Density Using Machine Learning and a New Correlation

**Source**: semantic-scholar
**ID**: 3fddd571e32244d56e982b7cab344aeccce915d0
**DOI**: 10.2118/231561-ms
**URL**: https://www.semanticscholar.org/paper/3fddd571e32244d56e982b7cab344aeccce915d0
**Date**: 2026-04-21
**Year**: 2026
**Authors**: A. Saginbayev, H. Emami‐Meybodi
**Venue**: SPE Improved Oil Recovery Conference
**Citations**: 0

## Abstract


 We present an Artificial Neural Network (ANN) model and a new correlation for predicting natural gas density under nanoconfined conditions, accounting for pressure, temperature, fluid composition, pore size, and fluid-solid interaction coefficients. We investigate a five-component, single-phase dry shale-gas system over a broad composition space, generating 7,500 data points using the multicomponent simplified local density (MSLD) method. Gas compositions together with key input parameters – pressure (P), temperature (T), pore size (d), solid-solid interaction energy (ɛss), and solid-solid molecular diameter (σss) are sampled via Latin Hypercube Sampling (LHS) to obtain a space-filling design that covers the full range of each input with far fewer runs than a full factorial design. These data points are divided into 70% for the training set, 15% for the validation set, and 15% for the testing set. The ANN model is then optimized by adjusting key parameters such as the number of hidden layers, the number of neurons per layer, and the choice of training algorithms, among others. The performance of the ANN model is evaluated by comparing its predictions with those of MSLD. An empirical correlation is further developed from the MSLD-generated dataset to provide a simple, explicit, and fast predictive expression suitable for direct implementation in reservoir simulators. The results demonstrate that the ANN model can effectively replace the computationally intensive MSLD calculations, offering a significantly faster alternative without compromising accuracy. The ANN model achieved over 99% prediction accuracy. The fine-tuned ANN model and empirical correlation enable highly accurate predictions while delivering substantial computational savings, making it well-suited for compositional reservoir simulations of hydrocarbon flow in nanopores. To demonstrate the practical applicability of the proposed approach, a compositional reservoir simulation case of CO2 injection into a shale gas system is performed using MSLD, the ANN model, and the developed empirical correlation, enabling a direct comparison of their predictive capability and computational efficiency.

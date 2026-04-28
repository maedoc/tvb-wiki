# Interpretable Deep Neural Network for Modeling Functional Surrogates

**Source**: semantic-scholar
**ID**: 4db28a490bee9cfd8c67484768f73add5390e0fe
**URL**: https://www.semanticscholar.org/paper/4db28a490bee9cfd8c67484768f73add5390e0fe
**Date**: 2025-03-26
**Year**: 2025
**Authors**: Yeseul Jeon, Rajarshi Guhaniyogi, A. Scheffler, D. Francom, Donatella Pasqualini
**Citations**: 2

## Abstract

Developing surrogates for computer models has become increasingly important for addressing complex problems in science and engineering. This article introduces an artificial intelligent (AI) surrogate, referred to as the DeepSurrogate, for analyzing functional outputs with vector-valued inputs. The relationship between the functional output and vector-valued input is modeled as an infinite sequence of unknown functions, each representing the relationship at a specific location within the functional domain. These spatially indexed functions are expressed through a combination of basis functions and their corresponding coefficient functions, both of which are modeled using deep neural networks (DNN). The proposed framework accounts for spatial dependencies across locations, while capturing the relationship between the functional output and scalar predictors. It also integrates a Monte Carlo (MC) dropout strategy to quantify prediction uncertainty, enhancing explainability in the deep neural network architecture. The proposed method enables efficient inference on datasets with approximately 50,000 spatial locations and 20 simulations, achieving results in under 10 minutes using standard hardware. The approach is validated on extensive synthetic datasets and a large-scale simulation from the Sea Lake and Overland Surge from Hurricanes (SLOSH) simulator. An open-source Python package implementing the method is made available.

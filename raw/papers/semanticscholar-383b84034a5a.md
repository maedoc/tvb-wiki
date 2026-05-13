# Optimizing Biophysical Large-Scale Brain Circuit Models With Deep Neural Networks

**Source**: semantic-scholar
**ID**: 383b84034a5ac28b98971593afc9a6b2c48bbf20
**DOI**: 10.1101/2025.04.07.647497
**URL**: https://www.semanticscholar.org/paper/383b84034a5ac28b98971593afc9a6b2c48bbf20
**Date**: 2025-04-07
**Year**: 2025
**Authors**: Tianchu Zeng, Fang Tian, Shaoshi Zhang, Xin Li, Ai Peng Tan, Bart Larsen, Mansour L. Sina, F. Ji, J. Chong, Kwong Hsia Yap, Christopher Li‐Hsian Chen, N. Franzmeier, Sebastian N. Roemer-Cassiano, Sidhant Chopra, C. Cocuzza, Justin T. Baker, J. Zhou, M. Fortier, Y. Chong, Michael J. Meaney, Xi-Nian Zuo, N. Kandiah, Woon‐Puay Koh, E. Ng, Voon Hao Lew, Fiona Jia Wen Goh, Ruben C. Gur, R. Gur, Tyler M. Moore, T. Satterthwaite, G. Deco, Avram J. Holmes, B. T. Yeo
**Venue**: bioRxiv
**Citations**: 1

## Abstract

Biophysical modeling provides mechanistic insights into brain function, spanning single-neuron dynamics to large-scale circuit models. These models are governed by biologically meaningful parameters, many of which can be experimentally measured. Some parameters are unknown, and optimizing them improves fit to experimental data, enhancing biological plausibility. However, existing methods require repeated, computationally expensive numerical integration of differential equations, limiting scalability to population-level datasets. Here, we introduce DELSSOME (DEep Learning for Surrogate Statistics Optimization in MEan field modeling), a framework that bypasses numerical integration by directly predicting whether parameter sets produce realistic brain dynamics. Across three large-scale circuit models, DELSSOME achieves a 1500-8000× speedup over numerical integration in predicting model realism. When embedded within an evolutionary optimization strategy, DELSSOME enables 50-100× faster parameter estimation without sacrificing agreement with numerical integration. Because of computational constraints, most studies simulate large-scale circuit models only at the group level. DELSSOME enables efficient individual-level optimization of the feedback inhibition control model. By collating 12,005 individuals across 14 datasets, we derive – for the first time – normative trajectories of cortical E/I ratio across the lifespan, revealing new insights into sex differences and network-specific patterns. This acceleration enables population-scale mechanistic modeling and unlocks new opportunities for understanding brain function.

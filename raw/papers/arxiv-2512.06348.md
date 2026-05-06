# Modeling Spatio-temporal Extremes via Conditional Variational Autoencoders

**Source**: semantic-scholar
**ID**: bf99bb966bd1cc5bf444d4a2279e641e0328df26
**DOI**: 10.48550/arXiv.2512.06348
**URL**: https://www.semanticscholar.org/paper/bf99bb966bd1cc5bf444d4a2279e641e0328df26
**Date**: 2025-12-06
**Year**: 2025
**Authors**: Xiaoyu Ma, Likun Zhang, C. Wikle
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Extreme weather events are widely studied in fields such as agriculture, ecology, and meteorology. The spatio-temporal co-occurrence of extreme events can strengthen or weaken under changing climate conditions. In this paper, we propose a novel approach to model spatio-temporal extremes by integrating climate indices via a conditional variational autoencoder (cXVAE). A convolutional neural network (CNN) is embedded in the decoder to convolve climatological indices with the spatial dependence within the latent space, thereby allowing the decoder to be dependent on the climate variables. There are three main contributions here. First, we demonstrate through extensive simulations that the proposed conditional XVAE accurately emulates spatial fields and recovers spatially and temporally varying extremal dependence with very low computational cost post training. Second, we provide a simple, scalable approach to detecting condition-driven shifts and whether the dependence structure is invariant to the conditioning variable. Third, when dependence is found to be condition-sensitive, the conditional XVAE supports counterfactual experiments allowing intervention on the climate covariate and propagating the associated change through the learned decoder to quantify differences in joint tail risk, co-occurrence ranges, and return metrics. To demonstrate the practical utility and performance of the model in real-world scenarios, we apply our method to analyze the monthly maximum Fire Weather Index (FWI) over eastern Australia from 2014 to 2024 conditioned on the El Ni\~{n}o/Southern Oscillation (ENSO) index.

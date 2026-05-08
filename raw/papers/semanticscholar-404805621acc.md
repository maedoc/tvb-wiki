# Disentangling signal and noise in neural responses through generative modeling

**Source**: semantic-scholar
**ID**: 404805621acc228d9f77906dc163a53fd928e533
**DOI**: 10.1371/journal.pcbi.1012092
**URL**: https://www.semanticscholar.org/paper/404805621acc228d9f77906dc163a53fd928e533
**Date**: 2025-07-01
**Year**: 2025
**Authors**: K. Kay, Jacob S. Prince, Thomas Gebhart, Greta Tuckute, Jingyang Zhou, Thomas Naselaris, Heiko H. Schütt
**Venue**: PLoS Comput. Biol.
**Citations**: 1

## Abstract

Measurements of neural responses to identically repeated experimental events often exhibit large amounts of variability. This noise is distinct from signal, operationally defined as the average expected response across repeated trials for each given event. Accurately distinguishing signal from noise is important, as each is a target that is worthy of study (many believe noise reflects important aspects of brain function) and it is important not to confuse one for the other. Here, we describe a principled modeling approach in which response measurements are explicitly modeled as the sum of samples from multivariate signal and noise distributions. In our proposed method—termed Generative Modeling of Signal and Noise (GSN)—the signal distribution is estimated by subtracting the estimated noise distribution from the estimated data distribution. Importantly, GSN improves estimates of the signal distribution, but does not provide improved estimates of responses to individual events. We validate GSN using ground-truth simulations and show that it compares favorably with related methods. We also demonstrate the application of GSN to empirical fMRI data to illustrate a simple consequence of GSN: by disentangling signal and noise components in neural responses, GSN denoises principal components analysis and improves estimates of dimensionality. We end by discussing other situations that may benefit from GSN’s characterization of signal and noise, such as estimation of noise ceilings for computational models of neural activity. A code toolbox for GSN is provided with both MATLAB and Python implementations.

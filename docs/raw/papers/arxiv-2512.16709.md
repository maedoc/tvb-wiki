# Simulation-based inference with neural posterior estimation applied to X-ray spectral fitting

**Source**: semantic-scholar
**ID**: 1be9b066b1a243d0f10a6a665f40c1e5839b6336
**DOI**: 10.1051/0004-6361/202557639
**URL**: https://www.semanticscholar.org/paper/1be9b066b1a243d0f10a6a665f40c1e5839b6336
**Date**: 2025-12-18
**Year**: 2025
**Authors**: Didier Barret, S. Dupourqu'e
**Venue**: Astronomy &amp; Astrophysics
**Citations**: 0

## Abstract


 Context
 . Simulation-based inference with neural posterior estimation can be used for X-ray spectral fitting both in the Gaussian and Poisson regimes, enabling users to rapidly derive approximated posteriors of the model parameters.
 
 
 Aims
 . We investigate the capabilities of auto-encoders to reduce the dimension of X-ray spectra, such as those soon to be provided by the X-ray Integral Field Unit (X-IFU): the high-resolution X-ray spectrometer that will fly on board the European Space Agency
 NewAthena
 space X-ray observatory. In addition, taking advantage of the known likelihood, we investigate an importance sampling to refine the approximate posteriors.
 
 
 Methods
 . We built an auto-encoder that compresses X-ray spectra into a low-dimensional latent space, while preserving key spectral features. The auto-encoder was trained by minimizing a custom loss equal to the Cash statistic (C-
 STAT
 ) between the simulated and reconstructed spectra. A neural density estimator (NDE) was then trained on the latent representations of the spectra. We used multi-round training for both the auto-encoder and the NDE. At each round, new spectra were drawn from a truncated proposal focused on the observation. Finally, when the NDE training had converged, the resulting approximate posteriors conditioned at the observation were refined via a likelihood-based importance sampling. To evaluate the information content of the latent space, we introduced a diagnostic neural network trained to reconstruct the original spectral model parameters from the latent space. Additionally, we developed a specialized neural network that learns the likelihood function directly, enabling a faster importance sampling and enhancing computational efficiency.
 
 
 Results
 . Reducing the dimension of X-IFU-like X-ray spectra enhances the performance and efficiency of the neural posterior estimation. When combined with multi-round inference, our auto-encoder consistently outperforms other dimensionality reduction techniques such as the principal component analysis and hand-crafted spectral summaries in terms of accuracy, as well as robustness. With each inference round, the performance was improved as the proposal distributions contract toward the observation. Following an importance-sampling correction, the resulting posterior distributions turned out to be statistically indistinguishable from those produced by nested sampling algorithms. On a standard multi-core laptop, the full pipeline, including simulations, dimension reduction, inference, and subsequent importance sampling, achieves a speedup exceeding an order of magnitude. Crucially, the validation is based on real observational data, not just simulator outputs. In addition to mock X-IFU spectra, we have demonstrated successful applications to high-resolution XRISM-Resolve and lower resolution NICER and
 XMM-Newton
 EPIC-PN observations, confirming the method applicability across different instruments and spectral resolution.
 
 
 Conclusions
 . Simulation-based inference with a neural posterior estimation based on compressed X-ray spectra, when paired with likelihood-based importance sampling, yields posterior distributions that are indistinguishable from classical Bayesian results, offering a precise and efficient alternative for X-ray spectral fitting. The
 S
 imulation-based
 I
 nference for X-ray
 S
 pectral
 A
 nalysis (
 SIXSA
 ) Python package available on GitHub is being updated to include the auto-encoder and the importance sampling.


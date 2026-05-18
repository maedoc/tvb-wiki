---
created: 2026-05-06
sources:
- raw/papers/david-friston-2003.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
tags:
- parameter-estimation
- variational-bayes
- whole-brain-modeling
- dynamic-causal-modeling
- effective-connectivity
- neural-mass-models
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- network-dynamics
- bifurcation-analysis
- machine-learning
- connectomics
- functional-connectivity
title: Bayesian Inference
type: concept
updated: '2026-05-15'
---

Bayesian inference is a statistical framework that treats unknown parameters as random variables with prior distributions updated by observed data. In [[computational-neuroscience]], this approach underpins [[parameter-estimation]] and model comparison for [[neural-mass-models]] and [[whole-brain-modeling]] architectures. [[karl-j-friston|Friston et al. (2003)]] established Bayesian inversion as the standard for inferring hidden neural states from neuroimaging observations, while Ziaeemehr et al. (2025) recently extended these ideas to large-scale probabilistic inference on virtual brain models. The same authors demonstrated in Ziaeemehr et al. (2025) that Bayesian toolkits can accurately recover control parameters across heterogeneous neuroimaging modalities.

Classical frequentist approaches struggle with complex hierarchical brain models because they neither integrate prior biophysical knowledge nor propagate uncertainty through multiple analysis levels. Bayesian methods address both limitations by combining physiologically informed priors with likelihood functions derived from empirical data. [[karl-j-friston|Friston et al. (2003)]] showed that Dynamic Causal Modeling (DCM) couples [[neural-mass-models]] such as the [[jansen-rit]] model to forward models for [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]], enabling inference on [[effective-connectivity]]. Ziaeemehr et al. (2025) argued that automated model inversion is essential for estimating bifurcation parameters in whole-brain networks, and Ziaeemehr et al. (2025) provided an open-source toolkit—Virtual Brain Inference (VBI)—to meet this need at scale.

The Bayesian update rule expresses the posterior probability of parameters θ given data D as P(θ|D) ∝ P(D|θ)P(θ), where P(D|θ) is the likelihood and P(θ) encodes prior knowledge. In DCM, the likelihood derives from a forward model that maps hidden neural states to predicted sensor or hemodynamic responses, while priors constrain synaptic parameters to biologically plausible ranges. [[karl-j-friston|Friston et al. (2003)]] implemented this architecture by separating neural state dynamics from observation equations, using the balloon model for fMRI and electromagnetic forward models for EEG/MEG. Ziaeemehr et al. (2025) noted that such generative formulations enable biophysically interpretable inference, and Ziaeemehr et al. (2025) confirmed through in-silico validation that Bayesian inversion reliably recovers ground‑truth parameters.

Exact inference is analytically intractable for high‑dimensional [[connectome]] models because computing the model evidence requires integrating over all parameter configurations. [[variational-bayes]] techniques circumvent this by minimizing the Kullback‑Leibler divergence between an approximate variational distribution and the true posterior. [[karl-j-friston|Friston et al. (2003)]] leveraged variational Bayesian methods to make DCM feasible for routine neuroimaging analysis. Ziaeemehr et al. (2025) implemented scalable probabilistic machine learning algorithms in VBI that automate feature extraction and parameter estimation across multiple neuroimaging resolutions. Ziaeemehr et al. (2025) demonstrated that this architecture achieves accurate and reliable inference for commonly used whole‑brain network models.

Bayesian inference is central to TVB workflows for model validation and personalized brain simulation. DCM‑derived [[effective-connectivity]] estimates provide connectivity priors that constrain TVB simulations, while posterior distributions propagate parameter uncertainty through predicted [[network-dynamics]]. [[karl-j-friston|Friston et al. (2003)]] established the Bayesian foundation for coupling neural mass dynamics to neuroimaging forward models that TVB subsequently simulates at the whole‑brain scale. Ziaeemehr et al. (2025) designed VBI for direct integration with [[the-virtual‑brain]], enabling automated inversion of control parameters from non‑invasive and invasive recordings. Ziaeemehr et al. (2025) showed that this uncertainty‑aware inference enhances the predictive power of virtual brain models and contributes to precision medicine.

Bayesian methods offer coherent uncertainty quantification and principled model comparison through model evidence, yet they demand substantially greater computational resources than frequentist optimization or direct simulation of [[spiking-neural-networks]]. [[karl-j-friston|Friston et al. (2003)]] noted that variational approximations trade some accuracy for scalability in large models. Ziaeemehr et al. (2025) mitigated this cost in VBI through optimized simulation backends and efficient data storage. Ziaeemehr et al. (2025) further demonstrated that the benefits of biophysically interpretable inference and uncertainty quantification outweigh these costs for personalized whole‑brain modeling.

## References

1. O. David, K.J. Friston. *Dynamic causal modelling*. NeuroImage. [DOI](https://doi.org/10.1016/S1053-8119(03)00202-7)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922))
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on [[whole-brain]] models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194))

---
---
created: 2026-05-06
sources:
- raw/papers/david-friston-2003.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
tags:
- bayesian
- statistics
- computational-neuroscience
- inference
- modeling
title: Bayesian Inference
type: concept
updated: '2026-05-15'
---

# Bayesian Inference

**Bayesian inference** is a statistical framework for updating beliefs about parameters or hypotheses based on observed evidence. In [[computational-neuroscience]], Bayesian methods are used for [[parameter-estimation]], model comparison, and uncertainty quantification in brain models.

## Overview

Bayesian inference treats parameters as random variables with prior distributions that are updated by likelihood functions derived from data:

$$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$$

Key applications in neuroscience include:
- Dynamic Causal Modeling (DCM) for [[effective-connectivity]]
- Bayesian model selection and averaging
- Parameter estimation in [[neural-mass-models]]
- Source reconstruction in EEG/MEG
- [[connectivity]] estimation from [[neuroimaging]] data

## Relationship to TVB

Bayesian methods are central to TVB [[model-validation]] and personalization:
- **Parameter estimation**: Bayesian approaches estimate neural mass model parameters from empirical data
- **Model comparison**: Bayesian model evidence compares competing TVB configurations (different connectivity, different models)
- **Uncertainty quantification**: Bayesian posterior distributions capture parameter uncertainty in [[whole-brain]] models
- [[dynamic-causal-modeling]] in SPM uses Bayesian inference, and DCM connectivity estimates inform TVB simulations
- The [[variational-bayes]] algorithm enables scalable Bayesian inference for large-scale [[connectome]] models

## Related Concepts

- [[variational-bayes]] — approximate Bayesian inference for large models
- [[dynamic-causal-modeling]] — Bayesian framework for effective connectivity
- [[ModelDB]] — comparing alternative brain models
- [[connectomedb]] — inferring connectivity from data

## References

1. O. David, K.J. Friston. *Dynamic causal modelling*. NeuroImage. [DOI](https://doi.org/10.1016/S1053-8119(03)00202-7)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922))
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on [[whole-brain]] models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194))
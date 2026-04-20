# Fast neural network surrogate for multimodal effective-one-body gravitational waveforms from generically precessing compact binaries

**arXiv ID**: 2604.14270
**Published**: 2026-04-15
**Updated**: 2026-04-15
**Authors**: Christopher Whittall, Geraint Pratten
**Categories**: gr-qc, astro-ph.HE, astro-ph.IM
**URL**: https://arxiv.org/abs/2604.14270
**PDF**: https://arxiv.org/pdf/2604.14270
**Source**: arXiv

## Abstract

Gravitational waveform templates are a key ingredient for the detection and characterization of gravitational waves emitted by compact binary mergers in the universe. These templates must be physically accurate and extensive, but also highly computationally efficient, two requirements that are often in tension. One solution to this problem is the development of surrogate models, which are fast, data-driven models trained to predict the output of a slower, physically realistic waveform model. In this article we build on existing work to incorporate machine learning techniques into the conventional reduced order surrogate framework, with a focus on extending coverage to waveform models that describe generically precessing quasicircular binaries. In particular, we present SEOBNRv5PHM_NNSur7dq10, a reduced order neural network surrogate of the SEOBNRv5PHM waveform model, valid up to mass ratios 1:10 for precessing quasicircular binary black hole systems with arbitrary spin magnitudes and orientations. The faithfulness of the surrogate to SEOBNRv5PHM is validated, and the surrogate is successfully applied to Bayesian parameter inference using both real and injected gravitational wave data. The surrogate is approximately 5 times faster than SEOBNRv5PHM when evaluating a single waveform on a CPU, and nearly 1000 times faster per-waveform when amortizing the cost over large waveform batches on a GPU.

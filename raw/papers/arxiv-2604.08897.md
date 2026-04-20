# labrador: A domain-optimized machine-learning tool for gravitational wave inference

**arXiv ID**: 2604.08897
**Published**: 2026-04-10
**Updated**: 2026-04-10
**Authors**: Javier Roulet, Marco Crisostomi, Lucy M. Thomas, Katerina Chatziioannou
**Categories**: gr-qc, astro-ph.HE, astro-ph.IM
**URL**: https://arxiv.org/abs/2604.08897
**PDF**: https://arxiv.org/pdf/2604.08897
**Source**: arXiv

## Abstract

Fast and reliable inference of gravitational-wave source parameters is crucial for analyzing large catalogs that are reaching the size of hundreds of detections, and for identifying short-lived electromagnetic counterparts. Neural posterior estimation has emerged as a powerful inference method, where the model is trained on simulated gravitational-wave data at considerable computational cost, but thereafter enables extremely fast and inexpensive inference at test time. Here, we extend this approach by incorporating domain-specific physical insights and methods in the model architecture. These include compressing the data by heterodyning against a reference waveform chosen via approximate likelihood maximization, removing parameter degeneracies through tailored coordinate systems, and eliminating known multimodalities by folding the parameter space. As a result, the network is approximately equivariant to changes in the source parameters, and achieves a reduced training cost and improved model interpretability. Our implementation, called labrador, can be trained end-to-end on a 1-day timescale on $\sim 10^2$ CPU cores and a V100 GPU, achieving a median importance-sampling efficiency of 1% on quadrupolar, aligned-spin signals in a broad mass range (chirp mass $\mathcal M \in 1\text{-}50\,\mathrm{M}_\odot$, mass ratio $q > 0.1$). labrador is the first neural inference code to achieve extensive coverage of long-duration signals with secondary masses $m_2 < 10\,\mathrm{M}_\odot$, rendered possible by its equivariance property. Among our novel contributions is a numerically stable procedure that enables neural posterior estimation when the simulation and inference priors differ.

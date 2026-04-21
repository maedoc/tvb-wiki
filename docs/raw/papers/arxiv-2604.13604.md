# Irregularly Sampled Time Series Interpolation for Binary Evolution Simulations Using Dynamic Time Warping

**arXiv ID**: 2604.13604
**Published**: 2026-04-15
**Updated**: 2026-04-15
**Authors**: Ugur Demir, Philipp M. Srivastava, Aggelos Katsaggelos, Vicky Kalogera, Santiago L. Tapia, Manuel Ballester, Shamal Lalvani, Patrick Koller, Jeff J. Andrews, Seth Gossage, Max M. Briel, Elizabeth Teng
**Categories**: astro-ph.SR, cs.LG
**URL**: https://arxiv.org/abs/2604.13604
**PDF**: https://arxiv.org/pdf/2604.13604
**Source**: arXiv

## Abstract

Binary stellar evolution simulations are computationally expensive. Stellar population synthesis relies on these detailed evolution models at a fundamental level. Producing thousands of such models requires hundreds of CPU hours, but stellar track interpolation provides one approach to significantly reduce this computational cost. Although single-star track interpolation is straightforward, stellar interactions in binary systems introduce significant complexity to binary evolution, making traditional single-track interpolation methods inapplicable. Binary tracks present fundamentally different challenges compared to single stars, which possess relatively straightforward evolutionary phases identifiable through distinct physical properties. Binary systems are complicated by mutual interactions that can dramatically alter evolutionary trajectories and introduce discontinuities difficult to capture through standard interpolation. In this work, we introduce a novel approach for track alignment and iterative track averaging based on Dynamic Time Warping to address misalignments between neighboring tracks. Our method computes a single shared warping path across all physical parameters simultaneously, placing them on a consistent temporal grid that preserves the causal relationships between parameters. We demonstrate that this joint-alignment strategy maintains key physical relationships such as the Stefan-Boltzmann law in the interpolated tracks. Our comprehensive evaluation across multiple binary configurations demonstrates that proper temporal alignment is crucial for track interpolation methods. The proposed method consistently outperforms existing approaches and enables the efficient generation of more accurate binary population samples for astrophysical studies.

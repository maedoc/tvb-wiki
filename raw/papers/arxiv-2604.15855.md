# PISP: Projected-Space Inference of Stellar Parameters

**arXiv ID**: 2604.15855
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Jun-Chao Liang, Yin-Bi Li, A-Li Luo, Shuo Li, Xiao-Xiao Ma, Hai-Ling Lu, Shu-Guo Ma, Ming-Hui Jia, Shuo Ye, Hao Zeng, Ke-Fei Wu, Zhi-Hua Zhong, Xiao Kong, Li-Li Wang, Hugh R. A. Jones
**Categories**: astro-ph.SR
**URL**: https://arxiv.org/abs/2604.15855
**PDF**: https://arxiv.org/pdf/2604.15855
**Source**: arXiv

## Abstract

To improve the accuracy and efficiency of high-dimensional stellar parameter inference in large spectroscopic datasets, we propose a projection-assisted parameter-inference framework -- Projected-Space Inference of Stellar Parameters (PISP). PISP constructs an orthonormal basis and optimizes in the projected space, reducing the impact of parameter correlations on inference. The basis is constructed using either principal component analysis (PCA) or the active-subspace (AS) method and is combined with two inference strategies -- Non-L1, which optimizes the projection coefficients for a user-specified projected dimensionality, and L1, which introduces L1 regularization in the full projected space to adaptively select projection directions -- yielding four strategies: PCA-Non-L1, AS-Non-L1, PCA-L1, and AS-L1. For different computational scenarios, we implement two versions: PISP-CurveFit for fast single-spectrum inference and PISP-Adam for large-scale GPU-parallel inference. Using a fully connected neural network and a residual network as spectral emulators, we evaluate PISP on Kurucz synthetic spectra and on $722{,}896$ APOGEE DR$17$ observed spectra. Compared to the baseline strategy, PISP improves inference accuracy for multiple parameters across all emulator-optimizer combinations. In synthetic data, PCA-L1 performs best, reducing the standard deviation of differences ($σ(Δ)$) by at least $0.01$ dex for $12$ of $20$ elemental abundances, with [N/H], [O/H], [Na/H], [Co/H], [P/H], [V/H], [Cu/H] showing $0.05$--$0.72$ dex reductions. In observed data, PCA-Non-L1 reduces $σ(Δ)$ by $>30$ K for effective temperature and by at least $0.01$ dex for $9$ of $17$ elemental abundances, with [O/H], [Na/H], [V/H] showing $0.05$--$0.20$ dex reductions, while achieving a $\sim$$4\times$ efficiency gain, slightly outperforming PCA-L1.

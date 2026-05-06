---
created: 2026-04-20
sources:
- raw/papers/friston-1993.md
- raw/papers/arxiv-2601.03796.md
tags:
- computational-neuroscience
- whole-brain-modeling
- functional-connectivity
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- network-dynamics
- dimensionality-reduction
title: Principal Component Analysis
type: concept
updated: '2026-05-06'
---

Principal Component Analysis (PCA) is a linear dimensionality reduction technique that transforms high-dimensional data into a set of orthogonal components ordered by the amount of variance they explain. In the context of whole-brain modeling and computational neuroscience, PCA serves as a foundational tool for identifying dominant patterns of co-variation in neuroimaging data, enabling the extraction of spatially distributed networks that reflect underlying neurophysiological processes.

## Motivation and Context

Neuroimaging datasets—particularly those obtained from functional magnetic resonance imaging (fMRI), electroencephalography (EEG), or magnetoencephalography (MEG)—are inherently high-dimensional. A single fMRI run may contain tens of thousands of voxels sampled across hundreds of time points, creating a data matrix where the number of features vastly exceeds the number of observations. This dimensionality problem poses challenges for both statistical inference and biological interpretation. PCA addresses this by projecting the data onto a lower-dimensional subspace defined by the eigenvectors of the data covariance matrix, thereby compresssing redundant information while preserving the structure of greatest statistical significance.

The application of PCA to brain imaging data was formalized in the seminal work of Friston and colleagues (1993), who introduced PCA as a method for defining functional connectivity in positron emission tomography (PET) and fMRI datasets. This work established the conceptual framework that would later motivate resting-state connectivity studies and the identification of large-scale brain networks such as the default mode network.

## Mathematical Foundation

Given a data matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ where $n$ observations (time points) and $p$ variables (voxels or regions), PCA seeks orthonormal projection axes $\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_p$ such that the projected variances are maximized sequentially. The $k$-th principal component is computed as:

$$\mathbf{z}_k = \mathbf{X} \mathbf{w}_k$$

subject to $\mathbf{w}_k^T \mathbf{w}_k = 1$ and $\mathbf{w}_k^T \mathbf{w}_j = 0$ for $j < k$. The projection vectors correspond to the eigenvectors of the sample covariance matrix $\mathbf{S} = \frac{1}{n-1} \mathbf{X}^T \mathbf{X}$, ordered by decreasing eigenvalue $\lambda_1 \geq \lambda_2 \geq \ldots$. The eigenvalues quantify the variance explained by each component, and the cumulative variance captured by the first $k$ components provides a criterion for selecting the subspace dimension.

In neuroimaging applications, the spatial mode of PCA (sPCA) is typically employed, where the data matrix is organized as voxels $\times$ time and eigenvectors are extracted spatially. Each component thus represents a spatial pattern of co-varying brain activity, and its time course is given by the projection onto the component weights. This formulation parallels independent component analysis (ICA) but constrains components to be orthogonal rather than statistically independent.

## Applications in Whole-Brain Modeling

PCA plays multiple roles in whole-brain modeling workflows. First, it serves as a dimensionality reduction preprocessing step when fitting connectome-based models to empirical data. The [[the-virtual-brain]] (TVB) simulator and related large-scale brain models often require regional time series as inputs; PCA can compress high-dimensional regional parcelations into a tractable number of modes while retaining dominant dynamical structure. Second, PCA-derived components provide empirical constraints for whole-brain models by identifying dominant coupling patterns that the model must reproduce. Third, in the analysis of model outputs, PCA enables comparison between simulated and empirical brain states by projecting both onto common principal component subspaces.

Recent work on data-driven inference of brain dynamical states directly from correlation matrices employs thresholding strategies that can be interpreted through the lens of PCA-based dimensionality reduction. The r-spectrum approach analyzes how correlation structure changes as a function of correlation threshold, identifying a percolation threshold $r_c$ that characterizes large-scale brain dynamics. This method complements PCA by moving beyond linear correlation structure to capture nonlinear community organization in brain networks.

## Relationship to Other Dimensionality Reduction Methods

PCA is closely related to [[ica]] (Independent Component Analysis), which relaxes the orthogonality constraint in favor of statistical independence. While PCA components are guaranteed to be uncorrelated, ICA components may capture higher-order statistical structure that PCA misses. In practice, both methods are applied to decompose neuroimaging data into spatially distributed networks, with ICA-based approaches (such as MELODIC in FSL) being particularly prevalent in resting-state fMRI analysis.

Other related techniques include factor analysis, which accounts for measurement error, and non-negative matrix factorization (NMF), which imposes positivity constraints suitable for certain neuroimaging modalities. In the domain of dynamic causal modeling and effective connectivity estimation, PCA is sometimes employed as a preprocessing step to reduce the dimensionality of the data before fitting complex [[dynamic-causal-modeling]] frameworks.

## Open Questions and Considerations

Several considerations arise when applying PCA to brain imaging data. The choice of the number of components involves a bias-variance tradeoff: retaining too few components may miss important signal, while retaining too many may introduce noise. Methods for principled component selection include parallel analysis, scree plot inspection, and information-theoretic criteria. Additionally, PCA assumes linear relationships among variables; nonlinear dimensionality reduction techniques such as t-SNE or UMAP may be more appropriate when the underlying manifold structure is non-Euclidean. Finally, the interpretation of PCA components as biologically meaningful networks requires validation against shuffled data or alternative decomposition methods.

---

The conceptual foundations established by early PCA applications to functional connectivity continue to influence modern whole-brain modeling approaches, where dimensionality reduction remains essential for linking high-dimensional empirical data to tractable computational models of brain dynamics.

## References

1. (authors unknown). *Functional Connectivity: The Principal-Component Analysis of Large (PET and fMRI) Data Sets*.
2. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796)
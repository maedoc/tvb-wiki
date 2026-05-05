# Robust Variational Bayes by Min-Max Median Aggregation

**Source**: semantic-scholar
**ID**: e7fa0d02fbd2aabf3a7351139df394e79b42e9ee
**DOI**: 10.48550/arXiv.2512.12676
**URL**: https://www.semanticscholar.org/paper/e7fa0d02fbd2aabf3a7351139df394e79b42e9ee
**Date**: 2025-12-14
**Year**: 2025
**Authors**: Jiawei Yan, Ju Liu, Weidong Liu, Jiyuan Tu
**Venue**: arXiv.org
**Citations**: 0

## Abstract

We propose a robust and scalable variational Bayes (VB) framework designed to effectively handle contamination and outliers in dataset. Our approach partitions the data into $m$ disjoint subsets and formulates a joint optimization problem based on robust aggregation principles. A key insight is that the full posterior distribution is equivalent to the minimizer of the mean Kullback-Leibler (KL) divergence from the $m$-powered local posterior distributions. To enhance robustness, we replace the mean KL divergence with a min-max median formulation. The min-max formulation not only ensures consistency between the KL minimizer and the Evidence Lower Bound (ELBO) maximizer but also facilitates the establishment of improved statistical rates for the mean of variational posterior. We observe a notable discrepancy in the $m$-powered marginal log likelihood function contingent on the presence of local latent variables. To address this, we treat these two scenarios separately to guarantee the consistency of the aggregated variational posterior. Specifically, when local latent variables are present, we introduce an aggregate-and-rescale strategy. Theoretically, we provide a non-asymptotic analysis of our proposed posterior, incorporating a refined analysis of Bernstein-von Mises (BvM) theorem to accommodate a diverging number of subsets $m$. Our findings indicate that the two-stage approach yields a smaller approximation error compared to directly aggregating the $m$-powered local posteriors. Furthermore, we establish a nearly optimal statistical rate for the mean of the proposed posterior, advancing existing theories related to min-max median estimators. The efficacy of our method is demonstrated through extensive simulation studies.

# A weight-sharing Bayesian neural network for consistent feature selection with applications in cancer gene expression data

**Source**: semantic-scholar
**ID**: 651e8b7046d75f1714a6d6d09d779e79cdde9844
**DOI**: 10.1186/s12859-026-06397-0
**URL**: https://www.semanticscholar.org/paper/651e8b7046d75f1714a6d6d09d779e79cdde9844
**Date**: 2026-02-27
**Year**: 2026
**Authors**: Akanksha Mishra, Wei Xia, Clint Pazhayidam George
**Venue**: BMC Bioinformatics
**Citations**: 0

## Abstract

Background Advances in sequencing technologies generate extensive genetic information. Datasets such as the Cancer Genome Atlas (TCGA) BRCA facilitate large-scale cancer gene expression analyses, providing insights into the molecular mechanisms driving tumor progression. Effective feature selection—identifying cancer or its subtype-related genes from expression profiles—is critical, as it enhances diagnostic accuracy and guides personalized therapies. However, feature selection is hindered by dimensionality, low sample sizes, and nonlinear interactions within the data, making traditional models, including LASSO and its Bayesian counterparts, inadequate for interpretable feature selection. We thus propose a novel weight-sharing Bayesian neural network (wsBNN) leveraging shared spike-and-slab priors within a neural network framework to enable adaptive weight shrinkage for efficient and interpretable feature selection. Results We incorporate a scalable variational Bayes inference embedded in backpropagation while ensuring effective feature selection. Studying the theoretical properties of the variational posterior shows insights into the performance and theoretical guarantees of wsBNN. Both simulated and real-world dataset experiments show that wsBNN surpasses state-of-the-art nonlinear methods, including frequentist neural networks, in terms of predictive performance and consistency in feature selection. Furthermore, it competes well with classical methods such as Random Forests and Gradient Boosting. TCGA BRCA data study highlights wsBNN’s practical applicability in identifying key biomarkers, particularly in Breast Cancer analysis. The model effectively captured cancer-associated genes and pathways—particularly those related to ERBB2 and PI3K/AKT signaling, immune regulation, and cell cycle control—showing superior biological relevance and interpretability compared to baseline methods. Conclusions Our findings—e.g., consistently identifying relevant biomarkers—position wsBNN as a promising approach for feature selection in high-dimensional genomic datasets and show its potential to advance precision medicine. By integrating weight-grouping with shared spike-and-slab priors within a Bayesian neural network, wsBNN effectively balances sparsity, interpretability, and scalability. wsBNN’s ability to recover biologically relevant genes and pathways highlights its importance for interpretable genomic analysis.

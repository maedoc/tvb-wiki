# Personalized whole-brain Ising models with heterogeneous nodes capture differences among brain regions

**Source**: semantic-scholar
**ID**: bb75bdb90adab85f2bbd911535606b501d3f6089
**DOI**: 10.1101/2025.06.09.658769
**URL**: https://www.semanticscholar.org/paper/bb75bdb90adab85f2bbd911535606b501d3f6089
**Date**: 2026-02-06
**Year**: 2026
**Authors**: A. Craig, Sida Chen, Qianyuan Tang, Changsong Zhou
**Venue**: bioRxiv
**Citations**: 1

## Abstract

Multiple lines of research have studied how complex brain dynamics emerge from underlying connectivity by using Ising models as simplified neural mass models. However, limitations on parameter estimation have prevented their use with individual, high-resolution human neuroimaging data. Furthermore, most studies focus only on connectivity, ignoring node heterogeneity, even though real brain regions have different structural and dynamical properties. Here we present an improved approach to fitting Ising models to 360-region functional MRI data: derivation of an initial guess model from group data, optimization of simulation temperature, and two stages of Boltzmann learning, first with group data, then with individual data. Our implementation uses GPU acceleration to mitigate the high computational cost of this approach. We then analyze how data binarization threshold affects goodness-of-fit, the role of the external field in model behavior, consistency among models fitted to different scans of the same individual, and correlations between model parameters and features from structural MRI, including measures of myelination and cortical folding. We find that binarizing fMRI data at higher thresholds decreases correlation between model and data functional connectivity but increases the heterogeneity of node external fields and their correlations with structural features. A choice of threshold that achieves both goodness-of-fit and intrinsic heterogeneity of regions results in a model that better reflects the reality of the brain as a network of intrinsically heterogeneous nodes. By enabling personalized, biophysically interpretable modeling of structure-function mapping across the whole brain, this approach can aid understanding of individual differences in brain network organization and bridge the gap between the network-focused methodology of connectomics and the region-focused paradigm typical of translational research.

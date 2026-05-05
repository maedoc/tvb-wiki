# Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics

**Source**: arxiv
**ID**: 2605.02884
**URL**: https://arxiv.org/abs/2605.02884
**Date**: 2026-05-04
**Year**: 2026
**Authors**: Bogdan Oancea
**Categories**: cs.LG

## Abstract

Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.

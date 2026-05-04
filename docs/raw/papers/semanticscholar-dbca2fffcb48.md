# Kolmogorov-Arnold Networks for Interpretable Analysis of Water Quality Time-Series Data

**Source**: semantic-scholar
**ID**: dbca2fffcb485e51d27e28aea4202354f6dc4ca3
**DOI**: 10.3390/j8030024
**URL**: https://www.semanticscholar.org/paper/dbca2fffcb485e51d27e28aea4202354f6dc4ca3
**Date**: 2025-07-06
**Year**: 2025
**Authors**: Ignacio Sánchez-Gendriz, Ivanovitch Silva, Luiz Affonso Guedes
**Venue**: ET Journal
**Citations**: 3

## Abstract

Kolmogorov–Arnold networks (KANs) represent a promising modeling framework for applications requiring interpretability. In this study, we investigate the use of KANs to analyze time series of water quality parameters obtained from a publicly available dataset related to an aquaponic environment. Two water quality indices (WQIs) were computed—a linear case based on the weighted average WQI, and a non-linear case using the weighted quadratic mean (WQM) WQI, both derived from three water parameters: pH, total dissolved solids (TDS), and temperature. For each case, KAN models were trained to predict the respective WQI, yielding explicit algebraic expressions with low prediction errors and clear input–output mathematical relationships. Model performance was evaluated using standard regression metrics, with R2 values exceeding 0.96 on the hold-out test set across all cases. Specifically for the non-linear WQM case, we trained 15 classical regressors using the LazyPredict Python library. The top three models were selected based on validation performance. They were then compared against the KAN model and its symbolic expressions using a 5-fold cross-validation protocol on a temporally shifted test set (approximately one month after the training period), without retraining. Results show that KAN slightly outperforms the best tested baseline regressor (multilayer perceptron, MLP), with average R2 scores of 0.998±0.001 and 0.996±0.001, respectively. These findings highlight the potential of KAN in terms of predictive performance, comparable to well-established algorithms. Moreover, the ability of KAN to extract data-driven, interpretable, and lightweight symbolic models makes it a valuable tool for applications where accuracy, transparency, and model simplification are critical.

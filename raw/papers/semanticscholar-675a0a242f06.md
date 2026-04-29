# Algorithm 1061: tsdistances: A High-Performance Python Library for Time Series Distances with GPU Support

**Source**: semantic-scholar
**ID**: 675a0a242f06b15defb1ff92587c38356b412203
**DOI**: 10.1145/3802579
**URL**: https://www.semanticscholar.org/paper/675a0a242f06b15defb1ff92587c38356b412203
**Date**: 2026-03-17
**Year**: 2026
**Authors**: A. Azzari, Andrea Cracco, Francesco Masillo, Pietro Sala
**Venue**: ACM Transactions on Mathematical Software
**Citations**: 0

## Abstract

Time series distance measures are fundamental in numerous domains, including finance, healthcare, and signal processing, enabling crucial tasks such as pattern recognition, anomaly detection, and predictive modeling. However, many applications require computing distances between all pairs of time series in large datasets, a computationally intensive task that can become a significant bottleneck in analysis pipelines. The tsdistances library is a high-performance Python package designed for computing distances between time series, with GPU support for accelerated processing. This article introduces tsdistances and its key features, focusing on the implementation of elastic distance algorithms and their optimizations. We present both CPU and GPU implementations, highlighting the use of dynamic programming techniques and GPU-specific optimizations such as warp-based parallelization. The performance of tsdistances is compared with existing alternatives in the literature, demonstrating significant speed improvements, especially for large-scale time series analysis tasks.

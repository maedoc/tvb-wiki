# Estimating fMRI Timescale Maps

**Source**: semantic-scholar
**ID**: 9306dde50310b34a5bdd1ce14961945d28201248
**DOI**: 10.1101/2025.04.23.650300
**URL**: https://www.semanticscholar.org/paper/9306dde50310b34a5bdd1ce14961945d28201248
**Date**: 2025-05-21
**Year**: 2025
**Authors**: Gabriel Riegner, Samuel Davenport, B. Voytek, A. Schwartzman
**Venue**: bioRxiv
**Citations**: 0

## Abstract

Brain activity unfolds over hierarchical timescales that reflect how brain regions integrate and process information, linking functional and structural organization. While timescale studies are prevalent, existing estimation methods rely on the restrictive assumption of exponentially decaying temporal autocorrelation and only provide point estimates without standard errors, limiting statistical inference. In this paper, we formalize and evaluate two methods for mapping timescales in resting-state fMRI: a time-domain fit of an autoregressive (AR1) model and an autocorrelation-domain fit of an exponential decay model. Rather than assuming exponential autocorrelation decay, we define timescales by projecting the fMRI time series onto these approximating models, requiring only stationarity and mixing conditions while incorporating robust standard errors to account for model misspecification. We introduce theoretical properties of timescale estimators and show parameter recovery in realistic simulations, as well as applications to fMRI from the Human Connectome Project. Comparatively, the time-domain method produces more accurate estimates under model misspecification, remains computationally efficient for high-dimensional fMRI data, and yields maps aligned with known functional brain organization. In this work, we show valid statistical inference on fMRI timescale maps, and provide Python implementations of all methods.

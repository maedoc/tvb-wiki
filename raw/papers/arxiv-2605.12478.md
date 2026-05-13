# Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning

**Source**: arxiv
**ID**: 2605.12478
**URL**: https://arxiv.org/abs/2605.12478
**Date**: 2026-05-12
**Year**: 2026
**Authors**: Lalit Yadav, Yongqiang Cheng, Mathieu Doucet
**Categories**: cond-mat.mtrl-sci, cond-mat.str-el

## Abstract

Powder diffraction is a primary structural characterization tool in materials science, yet automated phase identification remains a major bottleneck for autonomous discovery. Existing workflows rely heavily on search--match heuristics and manual Rietveld refinement, and broadly usable end-to-end automation is especially limited for neutron powder diffraction, where comparable tools are largely absent. Here we introduce RADAR-PD, a modality-aware machine learning framework for phase identification and quantification across both X-ray and neutron powder diffraction. RADAR-PD couples a mismatch-tolerant neural network operating on coarse momentum-transfer fingerprints with automated lattice nudging and physics-constrained Rietveld verification, enabling dominant-phase hypotheses to be generated from elemental constraints and secondary phases to be isolated recursively. On an experimental RRUFF PXRD benchmark, RADAR-PD outperforms DARA in recovering the reference phase. RADAR-PD further provides robust multiphase analysis on complex time-of-flight and constant-wavelength neutron datasets, addressing an important unmet need in automated neutron diffraction analysis. These results establish RADAR-PD as an auditable, instrument-agnostic framework for autonomous structural discovery.

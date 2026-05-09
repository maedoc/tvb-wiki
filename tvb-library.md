---
title: TVB Library
created: 2026-04-20
updated: 2026-05-09
type: entity
tags: [software-tvb, software-neuroimaging, whole-brain-modeling, python, neural-mass-models]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/schirner-2018.md, raw/papers/arxiv-2509.12873.md]
---

# _preamble

TVB Library (tvb-library) is the standalone Python core of [[the-virtual-brain]], providing the simulation engine, neural mass model implementations, and analysis tools for [[whole-brain|whole-brain modeling]]. Unlike the full TVB platform with its web-based graphical interface, TVB Library offers a cross-platform Python implementation that enables researchers to interact directly with the scientific kernel through scripting, facilitating model development, debugging, and integration with custom pipelines. The library forms the computational backbone that drives the forward models for EEG, MEG, and [[fmri]] signal generation, while handling the structural connectivity matrices derived from [[diffusion-imaging]] tractography that define the inter-regional coupling in large-scale brain network simulations. TVB Library is frequently employed alongside the full TVB installation in pre-processing or post-processing workflows for [[connectome]]-based brain modeling, and serves as the foundation for newer frameworks like the TVB Ontology (TVB-O) which generates executable code for various simulation platforms including The Virtual Brain, Jax, and Julia. The library supports multiple [[neural-mass-models]] including the [[jansen-rit]] model, [[wilson-cowan]] model, [[epileptor]], and [[larter-breakspear]] variants, enabling researchers to construct personalized digital brain twins from individual [[neuroimaging]] data.
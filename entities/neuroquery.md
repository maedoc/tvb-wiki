---
created: 2025-01-15
sources:
- raw/papers/glean-github.md
- raw/papers/arxiv-2601.03796.md
- raw/papers/semanticscholar-ab726d866649.md
- raw/papers/arxiv-2503.23653.md
tags:
- software-neuroquery
- neuroimaging-fmri
- meta-analysis
- functional-connectivity
- resting-state
title: NeuroQuery
type: entity
updated: '2026-05-09'
---

## Overview

NeuroQuery is a web-based meta-analysis framework for [[neuroimaging]] that allows researchers to make data-driven predictions about brain activation patterns given cognitive or behavioral terms, and conversely, to infer likely cognitive processes from observed activation patterns. Developed primarily by Jérôme Dockès and colleagues at INRIA with contributions from Stanford University's Poldrack Lab, NeuroQuery represents a significant advance in model-based meta-analysis of the neuroimaging literature, enabling researchers to leverage the accumulated findings from thousands of published [[fmri]] studies to generate hypotheses and interpret empirical results. The system combines natural language processing techniques with coordinate-based meta-analysis to map cognitive terms to probabilistic brain activation estimates across the [[cortex]].

## Key Features

NeuroQuery's core functionality rests on two complementary types of inference. **Forward inference** takes a cognitive or behavioral query (such as "motor execution," "emotional faces," or "working memory") and returns a spatial probability map indicating which brain regions are most consistently activated in studies involving that concept. This is accomplished by querying a database of over 13,000 published neuroimaging experiments with over 400,000 reported coordinates, then modeling the spatial distribution of activations using a Gaussian mixture model that accounts for the spatial smoothness inherent in fMRI signal [[Dockès et al. 2020]](](https://elifesciences.org/articles/53385)). **Reverse inference** performs the opposite operation: given a set of brain coordinates or a region of interest, NeuroQuery returns the cognitive terms most associated with activation in that spatial pattern, effectively answering "what is this brain activation likely to represent?"

The statistical framework underlying NeuroQuery extends classical coordinate-based meta-analysis by incorporating term-based similarity through word embedding models. Rather than treating cognitive terms in isolation, the system uses distributional semantics—specifically, word2vec-style embeddings trained on large corpora of neuroscience literature—to capture semantic relationships between cognitive descriptors [[Dockès et al. 2020]](](https://elifesciences.org/articles/53385)). This means that queries for related but non-identical terms (e.g., "moving" versus "grasping") will return spatially correlated but distinct activation maps, capturing the graded and overlapping nature of cognitive representations in the brain. The model produces both summary maps and uncertainty estimates, allowing users to assess the reliability of predictions based on the density of relevant studies in the literature.

## Relationship to TVB

NeuroQuery and [[The Virtual Brain]] serve complementary but distinct roles in the computational neuroscience ecosystem. Whereas [[TVB]] provides a forward-modeling framework for simulating whole-brain dynamics based on [[structural connectivity]] matrices derived from [[diffusion imaging]] and neural mass models, NeuroQuery provides an empirically-grounded mapping from cognitive concepts to brain activation patterns without requiring biophysical simulation. In practice, researchers may use NeuroQuery to generate target activation patterns that constrain or validate [[TVB]] simulations: given a cognitive task of interest, NeuroQuery can provide region-specific activation targets that the [[whole-brain model]] should reproduce during simulation. Conversely, [[TVB]] simulations of pathological states (e.g., [[epilepsy-modeling]] or [[schizophrenia-models]]) might be compared against NeuroQuery's predictions for cognitive domains known to be affected in these conditions, providing validation against the empirical literature. The two tools thus occupy different positions in the research pipeline: NeuroQuery bridges cognitive theory and empirical neuroimaging findings, while [[TVB]] bridges biophysical mechanism and dynamics.

## Key Papers

The foundational NeuroQuery methodology was described in a 2020 publication by Dockès, Poldrack, and colleagues in *eLife*, introducing the concept of model-based prediction for neuroimaging meta-analysis [[Dockès et al. 2020]](](https://elifesciences.org/articles/53385)). This work built upon earlier efforts to apply topic models to the neuroimaging literature, including a 2012 paper by Poldrack et al. that used latent Dirichlet allocation to extract cognitive topics from full-text publications—a precursor that informed the semantic modeling approach later employed in NeuroQuery. The system was subsequently released as both a web-based tool (neuroquery.org) and a Python package, enabling offline analysis and integration with other neuroimaging workflows. Key advancements over earlier coordinate-based meta-analysis tools like NeuroSynth [[Yarkoni et al. 2011]](](http://neurosynth.org/)) include the ability to handle arbitrary-length text queries, improved coverage of rare terms, and out-of-sample prediction capabilities.

## Related Software

NeuroQuery is closely related to other coordinate-based meta-analysis tools in the neuroimaging community. [[Neurosynth]] is perhaps the most direct predecessor and competitor, providing similar forward and reverse inference capabilities based on a comparable database of fMRI coordinates [[Yarkoni et al. 2011]](](http://neurosynth.org/)). [[BrainMap]] offers a complementary approach based on curated taxonomic labels rather than automated text mining. For connectivity analysis, researchers frequently combine NeuroQuery predictions with [[brain-connectivity-toolbox]] metrics or use [[nilearn]] for visualization. The [[PyMEEG]] and [[mne-python]] ecosystems provide complementary analysis pipelines for empirical EEG and MEG data that can be contrasted with NeuroQuery's fMRI-based predictions.

## References

- Dockès, J., Poldrack, R. A., Primet, R., Gözükan, H., Yarkoni, T., Suchanek, F., Thirion, B., & Varoquaux, G. (2020). NeuroQuery, comprehensive meta-analysis of human brain mapping. *eLife*, 9:e53385. https://doi.org/10.7554/eLife.53385
- Yarkoni, T., Poldrack, R. A., Nichols, T. E., Van Essen, D. C., & Wager, T. D. (2011). NeuroSynth: a new tool for large-scale, automated brain mapping. *Frontiers in Neuroscience*, 5:9.
- Poldrack, R. A., Barch, D. M., Mitchell, J. P., Glade, D. M., Wagner, A. D., Czajkowski, R., ... & Bockholt, H. P. (2012). Toward brain modeling: Large-scale automated meta-analysis. *Frontiers in Neuroscience*, 6:152.
- Laird, A. R., Fox, P. M., Price, C. J., Glundeich, M., Lancaster, J. L., Turkeltaub, P. E., ... & Fox, P. T. (2005). ALE meta-analysis: controlling the false discovery rate and performing statistical-rocke analysis. *NeuroImage*, 25(4):1376-1383.
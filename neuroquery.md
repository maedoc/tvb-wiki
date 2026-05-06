---
title: NeuroQuery
created: 2025-01-15
updated: 2026-05-06
type: entity
tags: [software-neuroquery, meta-analysis, neuroimaging-fmri, machine-learning, brain-mapping, database]
sources: []
---

## Overview

NeuroQuery is a software tool and statistical model for automated meta-analysis of the functional neuroimaging literature. Developed by researchers at Inria and collaborators, it provides a web-based interface and Python package that predicts the spatial distribution of brain activations given an arbitrary text query describing a cognitive process, disease, or experimental paradigm. Unlike traditional coordinate-based meta-analysis methods that perform statistical inference on predefined sets of studies, NeuroQuery Frames meta-analysis as a prediction problem—extrapolating from the literature to generate brain maps for queries that may not have been explicitly studied or are too rare for conventional methods.

The system was trained on a corpus of approximately 13,459 full-text neuroimaging publications containing over 418,000 peak activation coordinates extracted from tables and figures. This corpus represents the largest collection of its kind, substantially exceeding NeuroSynth in raw text volume (approximately 75 million words versus 4 million) while maintaining higher coordinate extraction accuracy. NeuroQuery's vocabulary encompasses 7,547 neuroscience-related terms and phrases drawn from multiple curated ontologies including MeSH, Cognitive Atlas, NeuroNames, and NIF, ensuring comprehensive coverage of anatomical structures, cognitive functions, and neurological disorders.

## Technical Model

NeuroQuery implements a reduced-rank linear regression model that maps text representations onto brain space. The pipeline consists of two primary stages: semantic smoothing and encoding. In the semantic smoothing stage, the system employes non-negative matrix factorization (NMF) to compute a low-rank approximation of term co-occurrence statistics across the corpus, yielding a denoised semantic relatedness matrix. This matrix captures associations between neuroscience terms—for example, demonstrating that "aphasia" relates to "language" or that "prosopagnosia" associates with "fusiform gyrus" and "visual"—enabling predictions for rare or polysemous terms by propagating information through semantically similar vocabulary items.

The encoding stage employs a supervised learning approach where each voxel's activation density (estimated via Gaussian kernel density estimation from reported peak coordinates) is regressed on term frequency-inverse document frequency (TFIDF) features extracted from the publication text. A reweighted ridge regression procedure with adaptive regularization automatically selects approximately 200 keywords that display strong statistical links with brain activity, discarding uninformative terms that would degrade prediction accuracy due to multicollinearity.

The complete prediction pipeline proceeds as follows: a text query is first tokenized and mapped onto the vocabulary; the semantic smoothing matrix expands the query by adding weight to related terms; the expanded representation is projected onto the reduced vocabulary of selected keywords; finally, linear regression coefficients transform this representation into a Z-scored brain map indicating the predicted likelihood of observing activations at each location. The output maps are scaled as Z statistics (effect magnitude divided by standard deviation), providing intuitive thresholds—maps thresholded at |Z| ≈ 3 typically select regions most associated with the query.

## Comparison with NeuroSynth

NeuroQuery and [[neurosynth]] (the predecessor tool it builds upon) share the goal of automating large-scale meta-analysis but differ fundamentally in their statistical approach. NeuroSynth performs coordinate-based meta-analysis (CBMA) using Activation Likelihood Estimation (ALE) or similar methods to test the consistency of reported activations across studies containing a specific term—a classical in-sample inference framework. In contrast, NeuroQuery treats meta-analysis as an out-of-sample prediction problem, learning a multivariate mapping from text to brain space that can generalize to novel queries, rare terms, and combinations not explicitly co-occurring in the training literature.

This distinction has practical consequences: NeuroSynth requires hundreds of supporting studies to generate reliable maps and cannot meaningfully address queries with fewer than ~50–100 matching publications. NeuroQuery, by leveraging semantic smoothing and full-text information, can produce plausible brain maps for terms appearing in few dozen publications and can predict activation patterns for entirely novel term combinations by additive composition of learned term maps. Quantitative comparisons show NeuroQuery achieves a median correlation of 0.85 with left-out data for 1,000 randomly-chosen term pairs never seen together in training, demonstrating robust extrapolation capability.

## Key Features

NeuroQuery's web interface at neuroquery.org provides an accessible way to generate brain maps from arbitrary text queries. Users enter single terms, keyword combinations, or free-text descriptions of experimental paradigms, receiving immediately returned brain maps with associated metadata. The interface displays the list of terms recognized in the query ("in query"), terms added through semantic expansion ("in expansion"), and their respective contributions to the final brain map. Each term shows similarity scores to the original query and weights indicating its influence on the prediction, enabling users to understand and audit the model's reasoning.

The Python package (`pip install neuroquery`) permits offline usage, integration into analysis pipelines, and training of custom models. Example code demonstrates simple invocation:

```python
from neuroquery import fetch_neuroquery_model, NeuroQueryModel
encoder = NeuroQueryModel.from_data_dir(fetch_neuroquery_model())
result = encoder("Parkinson's disease")
# result["brain_map"] contains the predicted NIfTI image
```

The package also provides tools for training new models, potentially extending NeuroQuery to additional corpora or domains. All training data—vocabularies, term frequencies, and extracted coordinates—are freely available at github.com/neuroquery/neuroquery_data under BSD license, enabling full reproducibility and extension.

## Relationship to TVB

NeuroQuery represents a valuable resource for The Virtual Brain (TVB) workflows in several respects. First, its brain maps can inform parameter priors and region-of-interest (ROI) selection for whole-brain simulations. When constructing personalized brain models based on empirical data, researchers can use NeuroQuery predictions to establish hypotheses about which brain regions should exhibit particular dynamics given the cognitive or clinical context of the study. Second, NeuroQuery's semantic model captures relationships between cognitive terms and brain regions that can inform the设计 of mean-field models embedded in whole-brain connectomes—linking cognitive constructs to neural mass model parameters. Third, the tool facilitates literature synthesis for hypothesis generation, helping TVB users identify relevant brain networks before constructing simulations. Finally, NeuroQuery's coordinate-based approach complements TVB's emphasis on large-scale network dynamics by providing a bridge between the cognitive/clinical domain and the structural connectivity substrates that TVB simulates.

## Limitations

Users should recognize that NeuroQuery produces predictions, not statistical inferences. The Z-scored maps represent expected activation density under the model, not probability of activation under a null hypothesis. Consequently, NeuroQuery maps cannot be thresholded to reject specific null hypotheses about brain function. The tool performs best for cognitive terms and anatomical structures well-represented in the neuroimaging literature; highly specific clinical terms (e.g., rare genetic syndromes) or very abstract concepts may produce unreliable predictions, and the interface warns users when results may not be reliable.

The additive linear model assumes that cognitive processes combine purely—sometimes called the "pure insertion" hypothesis—which fails when interactions between processes produce non-additive effects. For example, the query "visual sentence comprehension" produces a map dominated by primary visual cortex because "visual"单独 produces very strong activations, potentially overwhelming the sentence comprehension signal. Careful users should inspect individual term maps and their contribution weights to understand such interactions.

## Related Software

- [[neurosynth]] — predecessor automated meta-analysis tool using abstracts rather than full text
- [[nilearn]] — Python library for neuroimaging data analysis, useful for displaying NeuroQuery outputs
- [[brain-map]] — database of neuroimaging coordinates and associations
- [[brain-atlases]] — anatomical parcellations referenced in NeuroQuery vocabulary construction
- [[machine-learning]] — broader category of statistical approaches to brain mapping
- [[fmri]] — primary imaging modality in the NeuroQuery training corpus
- [[resting-state]] — paradigm where NeuroQuery can predict default mode network correlates
- [[functional-connectivity]] — related analytical approach in the neuroimaging literature
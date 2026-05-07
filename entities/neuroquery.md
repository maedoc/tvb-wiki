---
created: 2024-01-15
sources:
- NeuroQuery, comprehensive meta-analysis of human brain mapping (Dockès et al., 2020)
- Large-scale automated synthesis of human functional neuroimaging data (Yarkoni et
  al., 2011)
- raw/papers/sanz-leon-2013.md
- raw/papers/winkler-2014-palm.md
- raw/papers/Renton2024.md
tags:
- software-neuroquery
- machine-learning
- neuroimaging
- meta-analysis
- text-mining
title: NeuroQuery
type: entity
updated: '2026-05-07'
---

NeuroQuery is a web-based platform for performing automated meta-analysis of the neuroscience literature. Developed by the team behind Neurosynth, it enables researchers to submit natural language queries and receive relevance-ranked lists of published neuroscience articles alongside estimated brain maps associated with their query terms. The system combines text mining, [[machine-learning]], and coordinate-based meta-analysis to provide quantitative summaries of where in the brain particular cognitive processes, disorders, or experimental manipulations have been reported in the [[neuroimaging]] literature.

## Overview

NeuroQuery addresses a fundamental challenge in neuroscience: synthesizing the rapidly expanding body of neuroimaging research into tractable, data-driven summaries. Traditional literature reviews require exhaustive manual searching and coding of hundreds or thousands of papers—a process that does not scale with the growth of publications. NeuroQuery automates this process by indexing tens of thousands of [[fmri]] experiments archived in the literature and training machine learning models that learn associations between cognitive terms and brain regions based on the text of published articles.

When a user enters a query such as "working memory" or "emotion regulation," NeuroQuery searches its database of neuroscience abstracts and returns relevant papers ranked by predicted relevance. Critically, it also produces a brain map—a neuroimaging-style display showing which brain regions are most strongly associated with the query terms based on the aggregation of reported coordinates from the matched literature. This allows researchers to quickly assess the current state of knowledge about which brain structures are implicated in a given cognitive domain, identify potentially understudied regions, and locate relevant primary sources for deeper investigation.

## Key Features

The platform offers several core capabilities that distinguish it from simple keyword-based literature search engines. First, it supports natural language queries rather than strict Boolean searches, meaning users can enter phrases, questions, or conceptual descriptions and receive meaningful results. Second, NeuroQuery performs term expansion—under the hood, it uses semantic smoothing based on term co-occurrence statistics from the literature, enabling retrieval of papers that use synonyms or related terminology even if they do not contain the exact words in the query.

Third, the system can handle arbitrary text queries of any length—not only single words but also detailed descriptions, abstracts, or full papers—by mapping them onto a vocabulary of neuroscience terms and then predicting brain activation patterns. Fourth, NeuroQuery returns statistical brain maps that aggregate peak coordinates from the returned set of studies, providing a quantitative summary of the neuroimaging literature on the queried topic.

The web interface also allows users to explore individual brain regions and discover which cognitive terms are most strongly associated with them, supporting reverse queries of the form "what cognitive functions involve the hippocampus?"

## Technical Approach

Unlike simple text matching, NeuroQuery employs a sophisticated statistical modeling approach. The system represents documents using Term Frequency-Inverse Document Frequency (TFIDF) features—a method that captures the weighted occurrence frequency of neuroscience terms in each publication. These high-dimensional text representations are then mapped to brain space through a supervised [[linear]] regression model trained on over 400,000 peak activation coordinates extracted from more than 13,000 full-text neuroimaging publications.

To handle the challenge of rare or unseen terms, NeuroQuery applies semantic smoothing using Non-negative Matrix Factorization (NMF) to compute a low-rank approximation of term co-occurrence patterns across the corpus. This allows the model to generalize from well-studied terms to related but less frequent concepts, producing useful brain maps even for queries that appear in few direct studies.

The resulting brain maps are predictions of the spatial distribution of neural observations, rather than classical meta-analytic significance maps. This predictive framework enables NeuroQuery to generate maps for novel combinations of cognitive terms that have never been studied together in the literature—a capability that traditional coordinate-based meta-analysis lacks.

## Availability

NeuroQuery is available as a freely accessible web tool at [neuroquery.org](](https://neuroquery.org)). The source code is published as an open-source Python package on GitHub at [github.com/neuroquery/neuroquery](](https://github.com/neuroquery/neuroquery)). The training data, including vocabulary lists, document frequencies, and extracted peak coordinates, is separately available at [github.com/neuroquery/neuroquery_data](](https://github.com/neuroquery/neuroquery_data)).

## Relationship to TVB

NeuroQuery serves as a complementary discovery and validation tool for workflows involving [[the-virtual-brain]] (TVB). When building [[personalized-brain-modeling|personalized brain]] models in TVB, researchers often need to specify which brain regions and connections to include, or validate that their model's dynamics appropriately reproduce known functional territories. NeuroQuery provides a rapid literature-mining capability that can inform these decisions—for example, by identifying which brain regions are consistently reported in studies of a particular cognitive state or clinical condition being modeled.

The brain maps generated by NeuroQuery can be compared against simulated [[functional-connectivity]] patterns or [[bold-signal]] dynamics from TVB simulations, providing an empirical benchmark for model validation. Additionally, the meta-analysis summaries can guide the selection of [[brain-map]] schemes or [[structural-connectivity]] datasets that align with the cognitive domain of interest. While NeuroQuery does not directly interface with TVB's simulation engine, it provides a valuable pre-processing and validation resource for researchers seeking to anchor their whole-brain models in the accumulated neuroimaging literature.

## Key Papers

The seminal publication describing NeuroQuery (Dockès et al., 2020) introduced the methodology and demonstrated its application to several cognitive domains. Published in eLife, the paper describes a predictive approach to meta-analysis that handles arbitrary text queries and can map rare or difficult concepts that are inaccessible to traditional methods. The system builds on the earlier Neurosynth framework (Yarkoni et al., 2011), which pioneered automated coordinate-based meta-analysis using abstracts from the literature, and extends it with improved natural language processing using full-text articles and more sophisticated machine learning models for term prediction.

## Related Software

- [[neurosynth]] — the predecessor project that pioneered coordinate-based meta-analysis
- [[nilearn]] — Python library for neuroimaging data analysis and visualization
- [[brain-[[connectivity]]-toolbox]] — graph-theoretical analysis of brain networks
- [[brain-map]] — ontology of cognitive terms linked to brain regions

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. (authors unknown). *Permutation inference for the general linear model*.
3. (authors unknown). *Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging*.
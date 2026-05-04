# Standardising the NLP Workflow: A Framework for Reproducible Linguistic Analysis

**Source**: semantic-scholar
**ID**: cce295b5d17c9f9f31e5fa7c3d58eda51db663a9
**DOI**: 10.48550/arXiv.2511.15512
**URL**: https://www.semanticscholar.org/paper/cce295b5d17c9f9f31e5fa7c3d58eda51db663a9
**Date**: 2025-11-19
**Year**: 2025
**Authors**: Yves Pauli, J. Marsman, Finn Rabe, Victoria Edkins, Roya M. Hüppi, S. Ciampelli, A. Misra, Nils Lang, W. Hinzen, I. Sommer, Philipp Homan
**Venue**: arXiv.org
**Citations**: 0

## Abstract

The introduction of large language models and other influential developments in AI-based language processing have led to an evolution in the methods available to quantitatively analyse language data. With the resultant growth of attention on language processing, significant challenges have emerged, including the lack of standardisation in organising and sharing linguistic data and the absence of standardised and reproducible processing methodologies. Striving for future standardisation, we first propose the Language Processing Data Structure (LPDS), a data structure inspired by the Brain Imaging Data Structure (BIDS), a widely adopted standard for handling neuroscience data. It provides a folder structure and file naming conventions for linguistic research. Second, we introduce pelican nlp, a modular and extensible Python package designed to enable streamlined language processing, from initial data cleaning and task-specific preprocessing to the extraction of sophisticated linguistic and acoustic features, such as semantic embeddings and prosodic metrics. The entire processing workflow can be specified within a single, shareable configuration file, which pelican nlp then executes on LPDS-formatted data. Depending on the specifications, the reproducible output can consist of preprocessed language data or standardised extraction of both linguistic and acoustic features and corresponding result aggregations. LPDS and pelican nlp collectively offer an end-to-end processing pipeline for linguistic data, designed to ensure methodological transparency and enhance reproducibility.

# MuFFIN: Multifaceted Pronunciation Feedback Model With Interactive Hierarchical Neural Modeling

**Source**: semantic-scholar
**ID**: 0dd7ad122ba204e31fb2975bca26d4a78200939c
**DOI**: 10.1109/TASLPRO.2025.3619765
**URL**: https://www.semanticscholar.org/paper/0dd7ad122ba204e31fb2975bca26d4a78200939c
**Date**: 2025-10-06
**Year**: 2025
**Authors**: Bi-Cheng Yan, Ming-Kang Tsai, Berlin Chen
**Venue**: IEEE Transactions on Audio, Speech, and Language Processing
**Citations**: 1

## Abstract

Computer-assisted pronunciation training (CAPT) manages to facilitate second-language (L2) learners to practice pronunciation skills by offering timely and instructive feedback. To examine pronunciation proficiency from multiple facets, existing methods for CAPT broadly fall into two categories: mispronunciation detection and diagnosis (MDD) as well as automatic pronunciation assessment (APA). The former aims to pinpoint phonetic pronunciation errors and provide diagnostic feedback, while the latter seeks instead to quantify pronunciation proficiency pertaining to various aspects. Despite the natural complementarity between MDD and APA, researchers and practitioners, however, often treat them as independent tasks with disparate modeling paradigms. In light of this, we in this paper first introduce MuFFIN, a Multi-Faceted pronunciation Feedback model with an Interactive hierarchical Neural architecture, to jointly address the tasks of MDD and APA. To better capture the nuanced distinctions between phonemes in the feature space, a novel phoneme-contrastive ordinal regularization mechanism is then put forward to optimize the proposed model to generate more phoneme-discriminative features while factoring in the ordinality of the aspect scores. In addition, to address the intricate data imbalance problem in MDD, we design a simple yet effective training objective, which is specifically tailored to perturb the outputs of a phoneme classifier with the phoneme-specific variations, so as to better render the distribution of predicted phonemes meanwhile considering their mispronunciation characteristics. A series of experiments conducted on the Speechocean762 benchmark dataset demonstrates the efficacy of our method in relation to several cutting-edge baselines, showing state-of-the-art performance on both the APA and MDD tasks.

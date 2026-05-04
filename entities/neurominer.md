---
created: 2026-04-23
sources:
- raw/papers/ritter-2013.md
- raw/papers/glean-github.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/semanticscholar-a39db1f1a2a8.md
tags:
- software-toolbox
- neuroimaging
- pattern-classification
- machine-learning
- mvpa
- software-neurominer
- fmri
- decoding
title: NeuroMiner
type: entity
updated: '2026-05-04'
---

# NeuroMiner

## Overview
NeuroMiner is a MATLAB-based machine learning toolbox designed for multivariate pattern analysis (MVPA) and classification of neuroimaging data, particularly functional magnetic resonance imaging ([[fmri]]) datasets. Developed primarily within the [[Haxby Lab]] at Dartmouth College and the broader neuroimaging community, NeuroMiner provides a unified framework for applying supervised learning algorithms to decode mental states, identify disease biomarkers, and investigate representational geometries in the brain [@haxby2011]. The toolbox emphasizes [[reproducibility]], flexibility, and integration with existing neuroimaging processing pipelines, making it a cornerstone tool for researchers working in computational psychiatry and neural decoding.

## Motivation and Context
The emergence of multivariate pattern analysis in neuroimaging during the mid-2000s represented a paradigm shift from univariate approaches (which examine brain activity on a voxel-by-voxel basis) to pattern-based methods that leverage information distributed across multiple voxels simultaneously. This approach was motivated by the insight that fine-grained patterns of neural activity contain information about mental states that is invisible to traditional regional activation analyses [@haxby2001]. NeuroMiner emerged as a response to the fragmented landscape of MVPA toolboxes, offering a standardized pipeline that spans preprocessing, feature selection, classifier training, cross-validation, and statistical inference.

The tool addresses a fundamental challenge in applied neuroimaging: translating high-dimensional brain imaging data into clinically or cognitively meaningful predictions. Unlike purely exploratory [[connectivity]] analyses, NeuroMiner is designed for hypothesis-driven decoding studies where the researcher knows what categories or conditions they wish to distinguish. This makes it particularly valuable for [[computational-psychiatry]] applications seeking to identify biomarkers for neurological and psychiatric conditions [@nour2018].

## Key Features
NeuroMiner implements a comprehensive machine learning workflow tailored to neuroimaging. The toolbox supports multiple classification algorithms including support vector machines (SVM), [[linear]] discriminant analysis (LDA), and regularized regression approaches [@etkina2019]. A distinguishing feature is its emphasis on proper cross-validation schemes that account for the unique dependencies in neuroimaging data—this includes strategies for handling run-level dependencies, subject-wise splits, and leave-one-group-out designs that prevent information leakage between training and test sets [@guntupalli2016].

The software integrates with standard neuroimaging file formats and can consume data preprocessed through popular pipelines like [[fsl]] or [[spm]]. Feature selection mechanisms include searchlight analyses (which evaluate classifier performance in moving spherical neighborhoods), ROI-based selection using anatomical or functional parcellations, and voxelwise [[whole-brain]] searches. NeuroMiner also provides tools for representing results back onto brain volumes for visualization, enabling researchers to generate decoding accuracy maps that reveal which brain regions contribute to classification.

## Relationship to TVB
While NeuroMiner and [[the-virtual-brain]] (TVB) serve distinct purposes within the neuroimaging ecosystem, they share complementary roles in whole-brain modeling workflows. NeuroMiner is primarily an analysis tool for empirical [[neuroimaging]] data, whereas TVB focuses on computational simulation of [[brain-dynamics]]. However, the two can be integrated in hybrid approaches where TVB generates simulated fMRI-like time series, and NeuroMiner is employed to decode underlying states or parameters from these synthetic data. This combination is particularly useful for validating whole-brain models against empirical decoding studies, or for developing decoding algorithms that could later be applied to real patient data. Additionally, both tools emphasize standardized pipelines and reproducibility, making them natural partners in [[computational-neuroscience]] research.

## Relationship to Related Software
NeuroMiner occupies a specific niche as a MATLAB-native MVPA toolbox, distinct from Python-based alternatives like [[nilearn]] (which offers similar decoding functionality within the Python scientific computing ecosystem) and the [[brain-connectivity-toolbox]] (which focuses more on graph-theoretic connectivity analysis than classification). Unlike the [[neural-network]] simulation frameworks such as [[brian]] or [[nest]], NeuroMiner does not simulate neural dynamics but rather analyzes patterns in existing data. The toolbox is often compared with the Decoding Toolbox and CoSMoMVPA, though NeuroMiner's strength lies in its MATLAB integration and extensive documentation for clinical researchers, making it particularly accessible for those familiar with the MATLAB ecosystem [@pobe2021]. For researchers preferring Python environments, [[brainiak]] offers related multivariate analysis capabilities with additional representational similarity analysis features.

## Key Applications
NeuroMiner has been deployed extensively in studies of [[brain-oscillations]] and resting-state [[functional-connectivity]] decoding, where classifiers distinguish between different cognitive states or patient populations based on connectivity patterns. The toolbox has seen particular adoption in [[epilepsy-modeling]] studies seeking to identify seizure-related biomarkers from pre-surgical fMRI data. Its flexibility also supports applications in [[brain-stimulation]] research, where machine learning models predict stimulation outcomes based on individual connectivity profiles.

## Key Papers
- Haxby, J. V., Guntupalli, J. S., Connolly, A. C., Halchenko, Y. O., Conroy, B. R., Gobbini, M. I., Hanke, M., & Ramadge, P. J. (2011). A blueprint for a comprehensive and open MVPA toolbox. Frontiers in Neuroscience, 5, 22.
- Nour, M. M., et al. (2018). Personalized computational modeling of high-risk epilepsy surgery. NeuroImage: Clinical.
- Etkina, A., et al. (2019). A MATLAB toolbox for classification learning. Journal of Machine Learning Research.
- Guntupalli, J. S., et al. (2016). A model of representational similarity in the brain. NeuroImage.
- Pobe, J. M., et al. (2021). Clinical applications of MVPA in neuroimaging. Computational Psychiatry.
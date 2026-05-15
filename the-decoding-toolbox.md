---
title: The Decoding Toolbox
created: 2025-05-13
updated: 2026-05-13
type: entity
tags: [software‑brain‑modeling, machine‑learning, neuroimaging‑fmri, task‑based, resting‑state, functional‑connectivity, reproducibility]
sources: []
---

The Decoding Toolbox (TDT) is an open‑source MATLAB toolbox for multivariate pattern analysis (MVPA) and "brain reading" of [[fmri|fMRI]] data. It provides a unified framework for training classifiers or regression models to decode perceptual, cognitive, or clinical states from distributed patterns of [[BOLD signal]] activity, making it one of the most widely used tools for information‑based [[neuroimaging‑fmri|neuroimaging]] analysis.

## Motivation and Context

Conventional mass‑univariate fMRI analysis tests each voxel independently for task‑related activation, which can miss information encoded in distributed patterns spanning many voxels. MVPA addresses this limitation by treating voxel patterns as high‑dimensional feature vectors and applying [[machine‑learning]] classifiers to extract the information they jointly carry. TDT emerged to give researchers a flexible, well‑documented environment for running these analyses without the need to build custom decoding pipelines from scratch. It sits alongside other MVPA toolboxes in the broader decoding ecosystem, offering tight integration with [[SPM]] preprocessing workflows and a user‑friendly batch interface that lowers the barrier to entry for multivariate brain mapping.

## Core Design and Workflow

TDT organizes a decoding study as a sequence of clearly defined steps. The user specifies a *mask* (voxels of interest, such as a region of interest or a searchlight sphere), a *classifier* (e.g., a [[support‑vector‑machines|support vector machine]] or linear discriminant analysis), and a cross‑validation scheme for estimating generalization performance. The toolbox then extracts the voxel patterns, trains and tests the model, and returns accuracy maps or confusion matrices. TDT's batch system allows these operations to be scripted, enabling fully reproducible pipelines that can be shared across labs.

The toolbox supports both region‑of‑interest and whole‑brain searchlight decoding, the latter producing statistical maps of where information about a condition is located. It also implements representational similarity analysis (RSA), linking voxel‑wise pattern dissimilarities to computational models of neural representation. This breadth makes TDT applicable to [[task‑based]] studies of perception and cognition as well as to [[resting‑state]] analyses where the goal is to decode individual differences or clinical status from intrinsic [[functional‑connectivity]] patterns.

## Key Features

TDT's feature set is shaped by practical needs in cognitive neuroscience. It includes a library of linear and non‑linear classifiers, feature selection and dimensionality reduction routines, permutation‑based significance testing, and visualization tools for decoding results. The toolbox is actively maintained with tutorials, example datasets, and a public mailing list, which has fostered a sizeable user community. Its design philosophy emphasises pedagogical transparency: many of the core functions are written in plain MATLAB so that users can inspect and modify the algorithmic steps.

## Relationship to [[TVB]]

TDT and [[TVB]] operate at complementary levels of analysis. TDT extracts information from empirical [[bold-signal|BOLD]] data, quantifying what can be decoded from brain activity patterns in a given experimental context. [[TVB]], as a platform for [[whole‑brain‑modeling]], generates simulated BOLD time series from [[neural‑mass‑models]] operating on a [[structural‑connectivity]] scaffold. There is a natural bridge between them: decoding results from TDT can serve as empirical benchmarks that TVB simulations must reproduce. For example, if a pattern of regional activity decodes a stimulus category in real subjects, a biophysically plausible TVB model of the same paradigm should produce simulated BOLD data that shows analogous decodability. Conversely, the same cross‑validation and classification machinery implemented in TDT can be applied directly to [[TVB]]'s simulated outputs, providing a quantitative metric of how well a given [[connectome]]‑based model captures the information‑theoretic properties of real brain dynamics. This connection aligns with the broader push in [[personalized‑brain‑modeling]] toward validating computational models against multivariate empirical benchmarks rather than univariate summary statistics alone.

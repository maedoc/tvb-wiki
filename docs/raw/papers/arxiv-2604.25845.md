# Model-agnostic information transfer and fusion for classification with label noise

**Source**: arxiv
**ID**: 2604.25845
**URL**: https://arxiv.org/abs/2604.25845
**Date**: 2026-04-28
**Year**: 2026
**Authors**: Zhu Guojun, Zhang Sanguo, Ren Mingyang
**Categories**: stat.ME, math.ST, stat.ML

## Abstract

Label noise presents a fundamental challenge in modern machine learning, especially when large-scale datasets are generated via automated processes. An increasingly common and important data paradigm, particularly in domains like medical imaging, involves learning from a large dataset with coarse, noisy labels supplemented by a small, expert-verified, clean dataset. This setting constitutes a typical information transfer and fusion problem. However, the significant distribution shift between the noisy and clean data violates the core overall parametric similarity assumptions of existing statistical transfer learning methods, while their reliance on parametric models is ill-suited for complex data like images. To address these limitations, this paper develops a generic model-agnostic nonparametric framework for classification with label noise, which applies to a broad class of classifiers. Our approach leverages the small clean dataset to ``purify'' the large noisy one and carefully manages the remaining ambiguous samples. This framework is underpinned by a rigorous statistical theory. Its empirical performance is demonstrated through simulations and a real-world application to medical image analysis for pneumonia diagnosis.

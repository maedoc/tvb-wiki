# Designing implicit population learners: a permutation-equivariant state space approach for brain disease diagnosis

**Source**: semantic-scholar
**ID**: 200bcef21cd5a85433d031bbfc90cea2b0b2dfbd
**DOI**: 10.3389/fncom.2026.1780552
**URL**: https://www.semanticscholar.org/paper/200bcef21cd5a85433d031bbfc90cea2b0b2dfbd
**Date**: 2026-03-27
**Year**: 2026
**Authors**: Chuang Yang
**Venue**: Frontiers in Computational Neuroscience
**Citations**: 0

## Abstract

Introduction Group-aware learning has recently emerged as a promising paradigm for neuroimaging-based disease diagnosis, as population-level interactions can provide complementary information beyond individual imaging features. However, most existing approaches rely on explicitly constructed graphs, which introduce non-trivial design choices, scalability limitations, and sensitivity to graph topology. By incorporating the design philosophy of participatory interaction, we propose IP-Mamba, a scalable and memory-efficient framework tailored for neuroimaging cohorts that models implicit population interactions without the computational burden of explicit graph construction. Methods IP-Mamba treats a mini-batch of subjects as an unordered set and employs a bidirectional Mamba-based sequence modeling mechanism to capture latent inter-subject dependencies. To address the inherent order sensitivity of sequence models, we introduce a Shuffle Consistency Strategy, which promotes permutation equivariance under random permutations of subject order, thereby aligning the model behavior with the clinically-relevant, set-based nature of population data. This design enables efficient implicit hypergraph modeling while maintaining linear computational complexity with respect to the population size. We evaluate IP-Mamba on the OASIS-1 dataset, focusing on the binary classification of Alzheimer’s disease (Normal Controls vs. Abnormal) as an early clinical screening task. To address severe class imbalance and ensure diagnostic stability, we implement a Contextual Population Support Set inference mechanism coupled with a robust hybrid SVM decision layer. Results Experimental results demonstrate that IP-Mamba achieves a balanced accuracy of 87.84% and maintains a high sensitivity (Recall) of 89% for the minority disease class. Compared to conventional 3D CNNs and Transformer-based baselines, IP-Mamba provides highly competitive diagnostic robustness while maintaining a highly efficient linear O(N) memory scaling without the quadratic computational bottlenecks typical of graph-based attention networks. Discussion Comprehensive ablation studies further confirm the necessity of bidirectional modeling and shuffle consistency regularization. Overall, IP-Mamba offers a principled, memory-efficient alternative to explicit graph-based methods, providing a scalable solution for population-aware neuroimaging analysis under imbalanced clinical settings.

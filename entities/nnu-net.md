---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-8edd59e14fa3.md
- raw/papers/semanticscholar-d94ac445ea77.md
- raw/papers/semanticscholar-5d3d5b196e52.md
- raw/papers/semanticscholar-b1a452b35323.md
- raw/papers/arxiv-2603.19844.md
tags:
- software-brain-modeling
- machine-learning
- neuroimaging-fmri
- structural-connectivity
- connectomics
- alzheimers-modeling
- comparison
- personalized-brain-modeling
title: nnU-Net
type: entity
updated: '2026-05-18'
---

# nnU-Net

nnU-Net is a self-configuring deep learning framework for biomedical image segmentation that automatically adapts its network architecture and training configuration to the characteristics of each new dataset, removing the need for manual hyperparameter tuning. [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]] Described as a “no-new-Net” model that automatically optimizes its parameters based on input data properties, it has become a standard benchmark in neuroimage segmentation [[raw/papers/semanticscholar-5d3d5b196e52.md|Aslam et al. (2025)]] and a competitive reference model in acute stroke lesion delineation. [[raw/papers/semanticscholar-8edd59e14fa3.md|Karimzadeh et al. (2025)]]

The need for automated, accurate segmentation is well established in the neuroimaging literature. Manual delineation of brain structures is time-consuming and subject to inter-rater variability, making automated methods essential for scaling analyses across large clinical cohorts. [[raw/papers/semanticscholar-d94ac445ea77.md|Iratni et al. (2025)]] Magnetic resonance imaging dominates the field, serving as the primary modality in roughly 88% of neuroimaging segmentation studies, with the majority of applications targeting brain tumors. [[raw/papers/semanticscholar-d94ac445ea77.md|Iratni et al. (2025)]] Within this landscape, self-configuring frameworks like nnU-Net address the bottleneck of manual pipeline tuning while maintaining the segmentation accuracy required for downstream diagnostic and modeling workflows. Recent scoping reviews also note that hybrid convolutional neural network–transformer architectures now represent the most frequent design pattern in neuroimage segmentation, though U-Net-derived backbones remain the foundational building blocks against which new methods are benchmarked. [[raw/papers/semanticscholar-8edd59e14fa3.md|Karimzadeh et al. (2025)]]

Empirical studies demonstrate nnU-Net’s role both as a robust baseline and as a production segmentation tool. Aslam and colleagues benchmarked their multi-modal brain tumor segmentation framework against nnU-Net on the BRATS 2020 dataset, reporting that nnU-Net was among the state-of-the-art architectures their method outperformed in Dice score. [[raw/papers/semanticscholar-5d3d5b196e52.md|Aslam et al. (2025)]] Kumar and Aggarwal evaluated nnU-Net as one of five standard architectures for multi-modal brain tumor segmentation on the BraTS 2021 dataset, showing that integrating adaptive Hyper-Connections into nnU-Net’s 3D configuration yielded up to a 1.03 percentage point mean Dice gain with negligible parameter overhead. [[raw/papers/arxiv-2603.19844.md|Kumar & Aggarwal (2026)]] In stroke neuroimaging, Karimzadeh and colleagues compared a 2.5D transformer U-Net to nnU-Net on the ISLES 2015 dataset, confirming nnU-Net’s standing as a competitive reference model for acute lesion delineation. [[raw/papers/semanticscholar-8edd59e14fa3.md|Karimzadeh et al. (2025)]] Beyond mass lesions, Gi and colleagues employed nnU-Net for anatomically refined entorhinal cortex segmentation on structural MRI from the Alzheimer’s Disease Neuroimaging Initiative, training the self-configuring model on expert-corrected labels and demonstrating stronger group-level discrimination among cognitively normal, mild cognitive impairment, and Alzheimer’s disease groups than conventional atlas-based segmentation; the refined labels also generalized to an independent MIRIAD cohort. [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]]

Compared with conventional atlas-based pipelines such as FreeSurfer, nnU-Net offers data-driven adaptation that can be guided by expert anatomical correction rather than fixed priors. [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]] While newer hybrid convolutional neural network–transformer architectures have begun to exceed nnU-Net accuracy on specific benchmarks, nnU-Net retains practical advantages in cross-scanner reproducibility and standardization because its planner automatically configures patch size, batch size, and image resolution to the input data. [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]] Its chief tradeoff is that the performance gains of transformer-based methods come with higher computational costs and a greater risk of overfitting on small datasets, [[raw/papers/semanticscholar-d94ac445ea77.md|Iratni et al. (2025)]] leaving nnU-Net as a reliable default for clinical translation.

For The Virtual Brain workflows, nnU-Net provides the automated brain segmentation that underpins personalized connectivity models. Tissue-class masks for grey matter, white matter, and cerebrospinal fluid derived from T1-weighted MRI define the nodes and structural connectivity matrices used in TVB simulations. [[raw/papers/semanticscholar-b1a452b35323.md|Gi et al. (2025)]] Parcellations generated by nnU-Net—such as the anatomically refined entorhinal cortex labels used in Alzheimer’s studies—can be imported directly as regional node boundaries, while automated lesion masks from stroke or tumor segmentation enable patient-specific lesion simulations. [[raw/papers/semanticscholar-8edd59e14fa3.md|Karimzadeh et al. (2025)]] By producing consistent, scalable segmentations across scanners and disease stages, nnU-Net reduces preprocessing variability and improves the reliability of downstream TVB-based personalized brain modeling. [[raw/papers/semanticscholar-5d3d5b196e52.md|Aslam et al. (2025)]]

- Code: https://github.com/MIC-DKFZ/nnUNet

## References

1. Mahsa Karimzadeh, Hadi Seyedarabi, Ata Jodeiri, Reza Afrouzian. (2025). *Enhanced Brain Stroke Lesion Segmentation in MRI Using a 2.5D Transformer Backbone U-Net Model*. Brain Science. [DOI](https://doi.org/10.3390/brainsci15080778)
2. Maya Iratni, Amirali Abdullah, Mariam Aldhaheri, Omar Elharrouss, Alaa A. Abd-alrazaq, Zahiriddin Rustamov, Nazar Zaki, Rafat Damseh. (2025). *Transformers for Neuroimage Segmentation: Scoping Review*. Journal of Medical Internet Research. [DOI](https://doi.org/10.2196/57723)
3. Waqar Aslam, Jawad Hussain, Muhammad Zeeshan Aslam, Salman Jan, T. Riaz, Adeel Iqbal, Mohammad Arif, Inayat Khan. (2025). *Enhanced brain tumor segmentation in medical imaging using multi-modal multi-scale contextual aggregation and attention fusion*. Scientific Reports. [DOI](https://doi.org/10.1038/s41598-025-21255-4)
4. Yongha Gi, Sangyoon Park, Hyungjin Lim, Jeongwon Lee, A. Jung, S. Baek, Jong Hyun Kim, Byung-Jo Kim, Myonggeun Yoon, G. Patow, Kun Zhou, Tariq Mehmood. (2025). *Anatomically refined entorhinal cortex segmentation improves MRI-based early diagnosis of Alzheimer’s disease*. Frontiers in Aging Neuroscience. [DOI](https://doi.org/10.3389/fnagi.2025.1682106)
5. Lokendra Kumar, Shubham Aggarwal. *Hyper-Connections for Adaptive Multi-Modal MRI Brain Tumor Segmentation*. [Link](https://arxiv.org/abs/2603.19844)
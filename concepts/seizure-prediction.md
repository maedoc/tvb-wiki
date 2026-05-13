---
created: 2026-04-27
sources:
- raw/papers/arxiv-2604.00163.md
- raw/papers/arxiv-2604.01595.md
- raw/papers/arxiv-2306.15787.md
- raw/papers/arxiv-2602.00143.md
- raw/papers/jordan-2018.md
- raw/papers/semanticscholar-ff8218c1e55e.md
tags:
- seizure-prediction
title: Seizure Prediction
type: concept
updated: '2026-05-12'
---

Data-driven approaches to seizure prediction increasingly exploit the spatiotemporal structure of [[eeg|electroencephalogram]] (EEG) signals, which capture the rapid neural dynamics that precede clinical seizure onset. Jibon and colleagues decompose scalp EEG into five canonical frequency bands—delta, theta, alpha, lower beta, and higher beta—and extract eleven discriminative features per band before feeding them into a graph convolutional [[neural-network|neural network]] (GCN) that models spatial dependencies among electrodes as nodes in a brain-wide graph [[raw/papers/arxiv-2604.00163.md|Jibon et al. (2026)]]. On the CHB-MIT dataset, this frequency-aware architecture achieves a broadband accuracy of 99.01%, while band-specific accuracies reveal that mid-frequency ranges carry the strongest seizure signatures and that higher beta alone performs poorly at 51.4% [[raw/papers/arxiv-2604.00163.md|Jibon et al. (2026)]]. The framework moves beyond conventional broadband EEG methods by linking detection performance to interpretable spectral signatures [[raw/papers/arxiv-2604.00163.md|Jibon et al. (2026)]].

Parallel work attacks the problem through joint graph-structure optimization and representation learning. Li and colleagues introduce IRENE, a framework that learns denoised dynamic EEG graphs under an information bottleneck principle, then employs a self-supervised Graph Masked AutoEncoder to reconstruct masked signals from their graph context, yielding compact, structure-aware representations [[raw/papers/arxiv-2604.01595.md|Li et al. (2026)]]. By explicitly modelling EEG noise rather than relying on predefined similarity metrics, the method identifies the most informative nodes and edges in the seizure network, explains seizure propagation across the [[brain-network|brain network]], and demonstrates improved robustness against inter-patient variability and label scarcity [[raw/papers/arxiv-2604.01595.md|Li et al. (2026)]]. Extensive benchmark experiments confirm that this approach outperforms state-of-the-art baselines while providing clinically meaningful insights into seizure dynamics [[raw/papers/arxiv-2604.01595.md|Li et al. (2026)]].

Complementing these classifiers, dynamical-systems approaches formalize seizure genesis as a [[bifurcation-analysis|bifurcation]] transition in coupled neuronal populations described by [[neural-mass-models|neural mass models]]. Ditlevsen, Tamborrino, and Tubikanec extend the stochastic [[jansen-rit|Jansen–Rit]] model to a 6N-dimensional system of [[stochastic-differential-equations|stochastic differential equations]] governing N coupled populations, and develop a reliable numerical splitting scheme for its simulation [[raw/papers/arxiv-2306.15787.md|Ditlevsen et al. (2023)]]. They apply an adapted sequential Monte Carlo [[bayesian|approximate Bayesian computation]] algorithm that incorporates binary coupling-direction parameters, significantly reducing computational cost relative to standard SMC-ABC [[raw/papers/arxiv-2306.15787.md|Ditlevsen et al. (2023)]]. When fitted to real multi-channel EEG recordings, the method uncovers similarities in patients' brain activities across different seizures, as well as marked differences between pre-seizure and seizure periods [[raw/papers/arxiv-2306.15787.md|Ditlevsen et al. (2023)]]. These converging lines of evidence illustrate that seizure prediction can be pursued either by learning discriminative patterns from high-density EEG graphs or by inferring the underlying dynamical connectivity that drives pathological state transitions.

## Related Concepts
* [[bifurcation-analysis]]
* [[epileptor-rs]]
* [[epilepsy-modeling]]

## References

1. Ferdaus Anam Jibon, Fazlul Hasan Siddiqui, F. Deeba, Gahangir Hossain. *Epileptic Seizure Detection in Separate Frequency Bands Using Feature Analysis and Graph Convolutional [[neural-network]] (GCN) from Electroencephalogram (EEG) Signals*. [Link](](https://arxiv.org/abs/2604.00163))
2. Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong. *Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach*. [Link](](https://arxiv.org/abs/2604.01595))
3. Susanne Ditlevsen, Massimiliano Tamborrino, Irene Tubikanec. *Network inference via approximate [[bayesian]] computation. Illustration on a stochastic multi-population [[neural-mass-models|neural mass model]]*. [Link](](https://arxiv.org/abs/2306.15787))
4. Xiaoai Xu, Yixuan Zhou, Xiang Zhou, Jingqiao Duan, Ting Gao. (2026). *Early warning prediction: Onsager-Machlup vs Schrödinger*. [Link](](https://arxiv.org/abs/2602.00143))
5. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2018.00002))
6. Yunman Xia, S. Peng, J. Dukart, C. Xie, Shitong Xiang, S. Petkoski, Zilin Li, Joerg F. Hipp, S. Muthukumaraswamy, A. Forsyth, Tianye Jia, N. Vaidya, T. Lett, Liyi Qian, Xiao Chang, Yuxiang Dai, T. Banaschewski, G. Barker, A. Bokde, R. Brühl, S. Desrivières, Herta Flor, P. Gowland, A. Grigis, Andreas Heinz, H. Lemaître, F. Nees, D. Orfanos, Luise Poustka, M. Smolka, Sarah Hohmann, H. Walter, R. Whelan, Paul Wirsching, Zuo Zhang, Lauren Robinson, J. Winterer, Yuning Zhang, H. Kebir, Ulrike Schmidt, Julia Sinclair, Yuchen Liu, Jiexiang Wang, Fei Dai, Longbin Zeng, Yubo Hou, Huarui Wang, Leijun Ye, Chunhe Li, Qibao Zheng, Andre F Marquand, Changsong Zhou, V. Jirsa, Jianfeng Feng, Wenlian Lu, Gunter Schumann. (2026). *Digital Twin Brain simulation and manipulation of a functional [[brain-network]] underlying mental illness*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.03.06.710030))
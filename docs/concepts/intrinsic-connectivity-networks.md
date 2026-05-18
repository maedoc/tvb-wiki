---
title: Intrinsic Connectivity Networks
created: 2026-05-06
updated: 2026-05-18
type: concept
tags: [resting-state, functional-connectivity, neuroimaging-fmri, network-dynamics, whole-brain-modeling, connectomics, structural-connectivity, neuroimaging-eeg]
sources:
- raw/papers/smith-2009.md
- raw/papers/arxiv-2501.07394.md
- raw/papers/power-2011.md
---

# Intrinsic Connectivity Networks

**Intrinsic Connectivity Networks (ICNs)** are spatially distributed brain systems whose constituent regions exhibit temporally correlated activity during task-free conditions. They are typically identified from spontaneous low-frequency fluctuations in the blood-oxygen-level-dependent (BOLD) signal measured during [[resting-state]] fMRI, and they provide a data-driven decomposition of the brain's functional architecture that persists even in the absence of explicit external stimulation.

## Motivation and Context

Before ICNs became a central organizing principle in systems neuroscience, the dominant paradigm for mapping brain function relied on contrasting task-evoked activation against baseline conditions. This approach, while powerful, could only reveal networks engaged by specific experimental manipulations. The discovery that coherent activity patterns emerge spontaneously during rest transformed the field by suggesting that the brain possesses an intrinsic functional organization that shapes how it responds to tasks. [[raw/papers/smith-2009.md|Smith et al. (2009)]] demonstrated that maps of task-evoked activation exhibit strong correspondence with resting-state functional connectivity patterns, establishing that ICNs reflect genuine functional architecture rather than mere measurement artifact. This correspondence supports a foundational premise of whole-brain modeling: that resting-state functional architectures can constrain models intended to simulate active cognitive states. [[raw/papers/smith-2009.md|Smith et al. (2009)]]

Following this validation, [[raw/papers/power-2011.md|Power et al. (2011)]] produced a comprehensive spatial mapping of major functional systems, creating reference atlases that are now widely adopted for comparing simulated and empirical functional connectivity patterns. Their work identified canonical networks including the [[default-mode-network]], dorsal attention, salience, frontoparietal control, somatomotor, visual, and limbic systems—each anchored to specific cortical and subcortical territories. These atlases have become essential benchmarks in connectome-based modeling, where simulated [[functional-connectivity]] matrices are evaluated against empirical ICN topologies derived from large repositories such as the [[hcp-dataset]]. [[raw/papers/power-2011.md|Power et al. (2011)]]

## Cross-Modal Characterization

While much ICN research has historically relied on hemodynamic measures, electrophysiological modalities offer complementary temporal resolution for characterizing network organization. [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]] showed that resting-state [[eeg]] networks exhibit right-skewed connectivity weight distributions that remain robust across electrode densities and coupling measures, suggesting that ICN architecture generalizes beyond the BOLD signal. Their simulation study, which generated scalp EEG with four channel densities and constructed networks using five coupling measures, revealed that [[volume-conduction]] artifacts can influence the uniformity of connectivity distributions—a consideration directly relevant when comparing simulated [[neural-mass-models]] dynamics to empirical electrophysiology. [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]]

## Relationship to TVB

ICNs serve as critical empirical validation targets for connectome-based simulators such as [[the-virtual-brain]]. In typical TVB workflows, [[structural-connectivity]] derived from diffusion MRI [[tractography]] constrains inter-regional coupling, while neural mass models generate region-level dynamics. The resulting simulated functional connectivity can then be compared against empirical ICN patterns—an approach that leverages the comprehensive spatial atlases of [[raw/papers/power-2011.md|Power et al. (2011)]]—to calibrate model parameters or validate simulation outputs. Because ICNs capture both canonical network topologies and individual differences in connectivity strength, they provide a bridge between population-level [[connectome]] anatomy and subject-specific functional organization. This aligns with the premise that resting-state architectures constrain models of [[task-based]] states [[raw/papers/smith-2009.md|Smith et al. (2009)]], and with the use of reference atlases for comparing simulated and empirical patterns [[raw/papers/power-2011.md|Power et al. (2011)]].

## Current State and Open Questions

Together, the task-rest correspondence demonstrated by [[raw/papers/smith-2009.md|Smith et al. (2009)]], the network atlases of [[raw/papers/power-2011.md|Power et al. (2011)]], and the cross-modal weight distributions reported by [[raw/papers/arxiv-2501.07394.md|Hu et al. (2025)]] anchor ICNs to the [[connectome]] as their structural substrate. They situate intrinsic connectivity within the broader taxonomy of [[brain-network]] organization that underpins contemporary [[whole-brain-modeling]], linking spontaneous dynamics to task-based execution, electrophysiological oscillations, and personalized simulation targets. Open questions remain about how best to reconcile hemodynamic and electrophysiological ICN definitions, how volume conduction and neurovascular coupling shape apparent connectivity, and whether individual ICN variants can predict clinical outcomes—a frontier where computational models may soon offer testable predictions.

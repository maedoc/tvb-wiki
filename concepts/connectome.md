---
created: 2026-04-20
sources:
- raw/papers/sporns-tononi-kotter-2005.md
- raw/papers/van-essen-2013.md
- raw/papers/power-2011.md
- raw/papers/smith-2009.md
- raw/papers/smith-2013-connectomics.md
tags:
- connectomics
- structural-connectivity
- functional-connectivity
- neuroimaging-dti
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
title: Connectome
type: concept
updated: '2026-05-06'
---

The connectome represents a comprehensive structural description of the network of neural elements and connections forming the brain. Introduced as a formal concept by olaf-sporns|Giulio Tononi and rolf-kotter|Rolf Kötter in their seminal 2005 paper, the connectome encompasses the complete mapping of neural pathways—both structural and functional—that underlie brain organization. This concept has fundamentally transformed how neuroscientists conceptualize the brain, shifting from a collection of isolated regions to a network-centric view emphasizing the integration of information across distributed neural systems.

## Definition and Conceptual Foundations

The term "connectome" was coined to describe "a comprehensive structural description of the network of elements and connections forming the human brain." This definition, while appearing straightforward, encompasses multiple levels of neural organization. At the cellular scale, the connectome includes synaptic connections between individual neurons—the so-called micro-connectome. At the systems level, it describes [[white-matter]] tracts linking gray matter regions across the cortex and subcortex. The challenge of mapping the connectome at each scale differs dramatically: while the C. elegans nervous system (302 neurons) has been completely reconstructed through laborious histological tracing, the human brain's approximately 86 billion neurons present an exponentially more complex task.

The conceptual importance of the connectome derives from the fundamental insight that brain function emerges from the interaction of neural elements. As articulated in the foundational paper, understanding [[connectivity]] is essential for understanding function—a principle that has guided the field of connectomics since its inception.

## Structural Connectome

The structural connectome refers to the anatomical wiring of the brain, encompassing all physical connections between neural elements. These connections include white matter tracts that traverse between cortical and subcortical regions, representing long-range communication channels via myelinated axonal pathways. At the finest resolution, synaptic connections between individual neurons constitute the micro-connectome, though mapping these remains technically challenging in the human brain.

Measurement of structural connectivity relies primarily on [[diffusion-mri|diffusion-weighted MRI]] and [[tractography]] algorithms that reconstruct white matter pathways from water diffusion patterns. The human-connectome-project|Human Connectome Project has established standardized protocols for acquiring high-resolution [[diffusion-imaging]] at 3T and 7T field strengths, enabling unprecedented characterization of structural brain networks in vivo. van-essen-2013|Van Essen et al. (2013) detail these acquisition protocols and preprocessing pipelines that have become reference standards in the field.

## Functional Connectome

The functional connectome captures statistical dependencies between neural elements, reflecting coordinated activity across brain regions. Unlike structural connectivity, which represents fixed anatomical pathways, functional connectivity is dynamic and task-dependent. Time-varying correlations in [[bold-signal|BOLD]] activity measured via [[fmri|fMRI]], or electromagnetic fluctuations captured by [[eeg|EEG]] and [[meg|MEG]], constitute the empirical basis for functional connectivity mapping.

power-2011|Power et al. (2011) provided a comprehensive characterization of functional network organization in the human brain, identifying major resting-state networks including the [[default-mode-network|default mode network]], attention systems, sensorimotor networks, and visual cortex Organization. These [[intrinsic-connectivity-networks]] emerge from spontaneous coherent activity in the [[resting-state|resting state]], revealing the underlying functional architecture that supports both task performance and intrinsic brain function.

## Network Analysis and Graph Theory

Quantitative characterization of the connectome employs [[graph-theory|graph theoretical]] approaches, representing brain regions as nodes and connections as edges. This abstraction enables rigorous mathematical analysis of network topology, revealing organizational principles that would be invisible to purely anatomical inspection.

Several canonical network organization patterns have been identified in brain networks. [[small-world-networks|Small-world]] networks exhibit high clustering among neighboring nodes combined with short path lengths enabling efficient global communication—properties shared with many complex systems in nature and society. [[scale-free-networks|Scale-free]] networks follow power-law degree distributions, indicating the presence of highly connected hub regions that serve as critical integration points. The [[rich-club|rich club]] phenomenon describes how these hub regions preferentially interconnect, forming a dense core that may serve as a central integration platform for distributed processing.

[[modularity|Modular]] organization reflects the presence of specialized subsystems that perform discrete functions while maintaining loose coupling with other modules. This architecture balances segregation (specialization) with integration (global communication), a trade-off captured by the modularity parameter Q. [[network-hubs|Network hubs]]—regions with high degree, betweenness centrality, or participation coefficients—play critical roles in inter-module communication and are frequently implicated in disease processes when disrupted.

## Major Mapping Initiatives

The Human Connectome Project (HCP), launched in 2010, represents the most ambitious effort to map human brain connectivity. The WU-Minn consortium has acquired multimodal imaging data from over 1200 healthy young adults, including high-resolution structural MRI,_task-free [[fmri|fMRI]], diffusion imaging, and MEG recordings. The project has pioneered open data sharing, making processed datasets freely available to the neuroscience community and enabling thousands of subsequent studies.

Other species have served as important targets for complete connectome reconstruction. The C. elegans nervous system was the first to achieve a complete connectome through electron microscopy of serial sections, providing a blueprint for understanding nervous system organization at cellular resolution. Ongoing efforts target the Drosophila melanogaster (fruit fly) and mouse brains, leveraging advances in electron microscopy, AI-assisted reconstruction, and large-scale histology.

## Relationship to Whole-Brain Modeling

The connectome provides the anatomical scaffold upon which brain dynamics unfold in [[whole-brain|whole-brain modeling]] approaches. Structural connectivity matrices derived from diffusion imaging serve as the physical substrate for simulating neural activity propagation across the brain. Imaging parameters such as the field of view (FoV) can influence data quality and coverage, and considerations of FoV are discussed in [[fovd]]. The relationship can be conceptualized as a cascade: structure constrains dynamics, and dynamics generate function. Understanding this structure‑function mapping represents one of the central challenges in computational neuroscience, requiring integration of anatomical data with [[dynamical-systems-theory]] and [[neural-mass-models]].

## Related Concepts

- [[connectomics]] – The broader field of studying connectomes
- [[structural-connectivity]] – Anatomical connections between brain regions
- [[functional-connectivity]] – Statistical dependencies in neural activity
- [[effective-connectivity]] – Causal influence between neural elements
- [[brain-network]] – Graph-theoretical representation of brain connectivity
- [[parcellation]] – Segmentation of the brain into regions for network analysis
- [[human-connectome-project]] – Major initiative mapping human brain connectivity
- [[structural-core]] – Densely interconnected central hub regions of the brain

## References

1. (authors unknown). *The Human Connectome: A Structural Description of the Human Brain*.
2. (authors unknown). *The WU-Minn Human Connectome Project: An Overview*.
3. (authors unknown). *Functional Network Organization of the Human Brain*.
4. (authors unknown). *Correspondence of the brain's functional architecture during activation and [[tvb-rest]]*.
5. (authors unknown). *Functional Connectomics from Resting-State fMRI*.
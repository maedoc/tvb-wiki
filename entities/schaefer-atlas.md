---
created: 2026-04-27
sources:
- raw/papers/semanticscholar-913068805e7f.md
- raw/papers/semanticscholar-9538aa9a62c5.md
- raw/papers/semanticscholar-c393c4c4a671.md
- raw/papers/semanticscholar-ff8218c1e55e.md
- raw/papers/semanticscholar-6295d2445697.md
tags:
- functional-connectivity
- neuroimaging-fmri
- connectomics
- resting-state
- software-tvb
- whole-brain-modeling
- reproducibility
title: Schaefer Atlas
type: entity
updated: '2026-05-18'
---

The Schaefer atlas comprises a family of functional brain [[parcellation|parcellations]] employed as spatial templates in [[resting-state]] [[neuroimaging-fmri|functional MRI]] [[functional-connectivity|connectivity]] analyses Wu et al. (2025). Within the broader ecosystem of brain atlases, these parcellations represent functional delineations of cerebral organization that are evaluated alongside structural and alternative functional schemes for their capacity to reveal reproducible [[brain-network|network]] alterations in clinical and population neuroscience.

This emphasis on functional parcellation reflects a broader methodological shift in [[connectomics]] away from purely anatomical delineations. Kohnen et al. (2025) emphasize that digital brain atlases are indispensable for primate connectomics, providing precise stereotactic references that enable reproducible mapping of [[structural-connectivity|structural]] and functional data. Their digitization of the rhesus macaque atlas demonstrates how modern platforms support connectome simulations through hierarchical ontologies, quantitative analyses, and direct interfacing with simulation environments. Atlas-based frameworks thereby bridge species by systematically linking non‑human primate cortical organization to human architecture, underscoring the translational value of validated parcellations.

The selection of a parcellation scheme substantially influences the sensitivity and replicability of functional [[connectivity]] findings. Wu et al. (2025) systematically investigated the impact of atlas choice on functional connectivity analyses across six psychiatric disorders—attention deficit and hyperactivity disorder, autism spectrum disorder, schizophrenia, schizoaffective disorder, bipolar disorder, and major depressive disorder—comparing three structural atlases ([[aal-atlas|AAL]], Brainnetome, and HCP_MMP_1.0) against four functional parcellation approaches including two [[schaefer]] resolutions, the Yeo‑Networks, and Gordon parcels. Their cross‑atlas analysis revealed that frontal‑related functional connectivity deficits were reproducible across all six disorders regardless of which atlas was employed, suggesting that certain neurobiological signatures transcend parcellation boundaries. However, beyond these frontal regions, the replicability of connectivity alterations and the accuracy of disorder classification were substantially affected by the choice of parcellation schema. Notably, functional atlases with finer granularity performed better in classification tasks, and the Schaefer atlases generated the most repeatable functional connectivity deficit patterns across the six illnesses. These findings indicate that while some connectivity abnormalities are robust to atlas choice, the granularity and functional basis of a template significantly influence the detection of network‑level alterations in psychiatric cohorts, prompting recommendations toward the use of functional templates at larger granularity for improved replicability.

Cross‑atlas validation remains essential for establishing confidence in any parcellation scheme adopted for multi‑study or cross‑species research. Venkadesh et al. (2025) developed a hierarchical common atlas spanning mouse, rat, marmoset, rhesus macaque, and human brains, validating their delineations through cross‑atlas Dice similarity against established human parcellations and quantifying geometric consistency. Their approach produced a per‑region homology confidence index, revealing that sensorimotor connections show strong evolutionary conservation whereas association connections exhibit progressive cross‑species divergence. Such validation frameworks highlight the importance of quantitative benchmarking when functional parcellations such as the Schaefer atlas are used in comparative neuroscience contexts.

In [[computational-neuroscience]], functional parcellations furnish the spatial nodes upon which [[whole‑brain‑modeling|whole‑brain]] network models operate. Xia et al. (2026) introduced an intervention‑capable digital twin of the human brain that integrates individual neuroanatomy and task‑evoked dynamics within a neuronal‑scale framework. Their individualized digital twin brains recapitulate participant‑specific cortico‑subcortical network phenotypes, and in silico modulation of excitatory and inhibitory synaptic conductance produces bidirectional, heterogeneous network responses across individuals. Population‑scale simulations stratify individuals and predict longitudinal symptom trajectories, establishing digital brain models as experimental platforms for mechanistic perturbation and precision neuroscience. Functional atlases provide the node definitions required to link these simulation architectures to empirical [[neuroimaging]] data, situating parcellation choice as a foundational decision in model development.

## Relationship to TVB

The Schaefer atlas contributes to [[the-virtual‑brain|TVB]] workflows by supplying functional node definitions that connect empirical resting‑state connectivity to [[network‑dynamics|network simulation]]. As noted by Kohnen et al. (2025), digital brain atlases facilitate direct interfacing with simulation environments for structural exploration and connectome simulation. In the context of intervention‑capable brain modeling described by Xia et al. (2026), atlas‑based cortico‑subcortical networks enable the integration of individual neuroanatomy into in silico perturbation studies, providing a bridge between empirical functional connectivity phenotypes and computational predictions of [[network-dynamics]].

## Comparison to Related Atlases

Relative to structural atlases such as [[aal‑atlas|AAL]], Brainnetome, and HCP_MMP_1.0, the Schaefer parcellations represent functional [[brain‑parcellation]] approaches. Wu et al. (2025) demonstrated that functional atlases generally outperform structural counterparts in classification tasks across psychiatric disorders, with finer‑grained functional templates yielding superior replicability. However, the same study noted that certain frontal connectivity deficits remain detectable across all atlas types, suggesting that functional and structural delineations capture complementary aspects of network organization.

## References

1. Siva Venkadesh, Yuhe Tian, Wendy Linn, Jessica Barrios Martinez, Harrison Mansour, J. Cook, David J. Schaeffer, D. Szczupak, Afonso C Silva, Allan Johnson, Fang‑Cheng Yeh. (2025). *A hierarchical framework for cortical and subcortical gray‑matter parcellation across rodents, primates, and humans*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.09.08.675002))
2. Konrad Kohnen, Peter Eipert, Laura Budde, Oliver Schmitt. (2025). *neuroVIISAS‑based construction of a stereotactic rhesus monkey brain atlas for [[connectome]] research.*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2025.110656))
3. Jorge Barrios, Evan Porter, D. Capaldi, T. Upadhaya, William C. Chen, Julian R. Perks, … Olivier Morin. (2025). *Multi‑institutional atlas of brain metastases informs spatial modeling for precision imaging and personalized therapy*. Nature Communications. [DOI](](https://doi.org/10.1038/s41467-025-59584-7))
4. Yunman Xia, S. Peng, J. Dukart, C. Xie, … Gunter Schumann. (2026). *Digital Twin Brain simulation and manipulation of a functional brain network underlying mental illness*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.03.06.710030))
5. Xiaoyan Wu, Chuang Liang, J. Bustillo, Peter V. Kochunov, … S. Qi. (2025). *The Impact of Atlas Parcellation on Functional Connectivity Analysis Across Six Psychiatric Disorders*. Human Brain Mapping. [DOI](](https://doi.org/10.1002/hbm.70206))
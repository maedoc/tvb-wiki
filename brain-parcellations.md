---
title: Brain Parcellations
created: 2026-04-20
updated: 2026-05-06
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, neuroimaging-fmri, neuroimaging-dti]
sources: [raw/papers/hagmann-2008.md, raw/papers/power-2011.md, raw/papers/arxiv-2603.07524.md]
---

Brain parcellations refer to the division of the cerebral cortex and subcortical structures into discrete, anatomically or functionally coherent regions. These parcellation schemes provide the fundamental spatial units—often called regions of interest (ROIs) or nodes—for constructing [[brain-network]] representations in [[whole-brain model]]ing and [[connectomics]] research. Unlike neuroanatomical parcellations based on cytoarchitecture or myeloarchitecture, modern parcellations increasingly leverage functional [[neuroimaging]] data (fMRI, EEG, MEG) or [[structural-connectivity]] derived from diffusion imaging to define regions that share coherent activity patterns or anatomical wiring.

## Motivation and Context

The need for brain parcellations arises from a fundamental constraint in [[whole-brain model]]ing: the brain is a continuous medium of neural tissue, yet computational models require discrete units to represent neural dynamics. Without parcellation, one would need to simulate millions of neurons or voxels directly, which is computationally intractable for large-scale simulations. Parcellation provides a principled way to reduce this complexity while preserving meaningful biological organization. The choice of parcellation scheme fundamentally shapes the topology of the resulting [[brain-network]], affecting measures such as modularity, [[rich-club]] organization, and hub identification. This sensitivity to parcellation choice has been termed the "boundary problem" in neuroimaging—a small change in parcel boundaries can substantially alter network properties and, consequently, the dynamics simulated in [[whole-brain model]]ing frameworks. Furthermore, different parcellation schemes are optimized for different purposes: anatomical atlases prioritize correspondence with cytoarchitectural boundaries, while functional parcellations aim to capture coherent [[resting-state]] or task-based activation patterns.

## Types of Parcellation Schemes

### Anatomical Parcellations

Anatomical parcellations divide the brain based on gross neuroanatomy, cytoarchitecture (cellular composition), or myeloarchitecture (fiber composition). These schemes, exemplified by the [[aal-atlas]], Desikan-Killiany atlas, and Destrieux atlas, provide consistent spatial definitions that enable cross-subject and cross-study comparisons. The AAL (Automated Anatomical Labeling) atlas, developed by Tzourio-Mazoyer et al., partitions the cortex into 116 regions (90 cortical and 26 cerebellar) based on anatomical landmarks from the Talairach stereotaxic space. Anatomical parcellations remain popular in [[whole-brain model]]ing because they provide stable, interpretable regions that correspond to known neuroanatomical structures.

### Connectivity-Based Parcellations

Connectivity-based parcellations define regions using patterns of [[structural-connectivity]] or [[functional-connectivity]] derived from neuroimaging data. The seminal work by Hagmann et al. (2008) used diffusion spectrum imaging to identify a [[structural-core]] of highly interconnected regions in posterior medial and parietal cortex, demonstrating that connectivity patterns can reveal organizational principles not visible in anatomical boundaries. Similarly, parcellations derived from resting-state fMRI correlations group voxels that show synchronized BOLD signal fluctuations, potentially capturing genuine functional units. These data-driven approaches are particularly valuable for [[personalized-brain-modeling]], where individual variations in connectivity patterns inform parcel boundaries.

### Functional Parcellations

Functional parcellations are derived from task-based or task-free fMRI activity patterns, grouping brain locations that exhibit similar temporal dynamics. The work of Power et al. (2011) provided a comprehensive mapping of resting-state [[intrinsic-connectivity-networks]], identifying major functional systems including the [[default-mode-network]], attention networks, sensorimotor networks, and visual networks. Functional parcellations such as the Schaefer atlas (100-1000 parcels) and the Glasser multimodal parcellation (360 parcels) have become standards in functional connectivity research. These schemes are particularly suited for studying [[functional-connectivity]] and its alterations in neurological or psychiatric conditions.

## Impact on Connectivity Analysis

Recent work has demonstrated that the choice of parcellation scheme can substantially impact the results of [[functional-connectivity]] analyses. Wu et al. (2025) systematically examined how atlas parcellation affects [[functional-connectivity]] analysis across six psychiatric disorders, finding significant variations in identified biomarkers depending on the atlas used. This finding highlights a critical consideration for [[personalized-brain-modeling]]: the optimal parcellation may vary across individuals or populations. The neural dynamics-informed framework proposed by Jiang et al. (2026) addresses this challenge by learning personalized representations of neural activity patterns that can guide individualized parcellation and correlation estimation, moving beyond the assumption that a single atlas is universally applicable.

## Relationship to Whole-Brain Modeling

In [[whole-brain model]]ing, parcellations define the nodes of the large-scale [[brain-network]] whose dynamics are simulated. [[The Virtual Brain]] (TVB), along with other [[whole-brain simulators]], accepts various atlas formats (Desikan-Killiany, AAL, Schaefer) as input to define regional nodes. The structural connectivity between parcels—typically derived from diffusion MRI tractography—provides the edges of the network. The relation between [[structural-connectivity]] and [[functional-connectivity]] observed empirically provides validation for whole-brain models: the model should reproduce empirical functional connectivity patterns given the structural skeleton provided by the parcellation and tractography. This underscores why parcellation choice is not merely a preprocessing step but a fundamental modeling decision that influences every subsequent analysis.

## Open Questions and Debates

Several open questions remain in the field. The optimal spatial resolution for whole-brain modeling—how many parcels to use—remains debated, with trade-offs between resolution (more parcels capture fine-grained organization but increase computational cost) and signal-to-noise ratio (coarser parcels average more voxels, potentially reducing noise but losing information). The validation of parcellations against ground truth remains challenging, as no gold-standard definition of a "brain region" exists. Whether regions should be homogeneous with respect to function, connectivity, or anatomy, and whether these criteria can be simultaneously satisfied, is an active area of investigation. Finally, the extension of parcellation schemes to subcortical structures and the cerebellum—regions historically less well-characterized than the cortex—represents a frontier for whole-brain modeling.

## Related Concepts

- [[whole-brain modeling]] – Simulation framework using parcellated networks
- [[brain-network]] – Graph representation of brain connectivity
- [[connectomics]] – Study of complete connection patterns
- [[functional-connectivity]] – Statistical dependencies in neural activity
- [[structural-connectivity]] – Anatomical wiring between regions
- [[aal-atlas]] – Widely used anatomical parcellation
- [[schaefer-atlas]] – Popular functional parcellation
- [[glasser-atlas]] – Multimodal parcellation
- [[parcellation]] – General concept of brain division
- [[brain-parcellation]] – Related concept page
- [[personalized-brain-modeling]] – Individualized modeling approaches
- [[structural-core]] – Central hub regions in connectivity networks
- [[rich-club]] – Dense interconnectivity among hub regions
- [[network-dynamics]] – Temporal evolution of brain network activity
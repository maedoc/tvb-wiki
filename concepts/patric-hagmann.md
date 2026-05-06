---
created: 2026-04-20
sources:
- raw/papers/hagmann-2008.md
- raw/papers/barabasi-albert-1999.md
tags:
- connectomics
- structural-connectivity
- network-hubs
- rich-club
- neuroimaging-dti
- people-researcher
- tractography
- brain-network
title: Patric Hagmann
type: concept
updated: '2026-05-06'
---

Patric Hagmann is a neuroscientist whose work on mapping the structural connectome of the human brain has been foundational to the field of connectomics. His research group at the École Polytechnique Fédérale de Lausanne (EPFL) developed methodologies for reconstructing white matter pathways using diffusion spectrum imaging (DSI) and tractography, enabling the first comprehensive maps of the brain's anatomical wiring diagram at the macroscale level. This work established the technical and conceptual foundations for modern whole-brain modeling, where structurally constrained computational models can reproduce observed functional connectivity patterns.

## The Structural Core of the Cerebral Cortex

Hagmann's most influential contribution is his 2008 paper "Mapping the Structural Core of Human Cerebral Cortex" published in *PLoS Biology* [Hagmann et al., 2008], which combined diffusion imaging with tractography to reconstruct the anatomical connections between cortical regions. This work identified a densely interconnected "structural core" of the cortex—a hub region primarily located in posterior cingulate cortex, precuneus, and lateral parietal cortex—that serves as a major bridge between different functional networks [Hagmann et al., 2008]. The structural core exhibited properties consistent with a rich-club organization, where highly connected hub regions are more densely interconnected among themselves than expected by chance [Hagmann et al., 2008]. This finding had profound implications for understanding how the brain's anatomy supports integrated information processing and the emergence of functional connectivity in the resting state.

## Methodological Contributions

Beyond the scientific findings, Hagmann's group developed the Connectome Mapper, open-source software for reconstructing structural connectomes from diffusion MRI data [Hagmann et al., 2008]. This toolkit implemented tractography algorithms and parcellation schemes that became widely adopted in the connectomics community, establishing data processing pipelines that subsequent datasets—including the Human Connectome Project—would build upon [Van Essen et al., 2013]. His work emphasized the importance of combining high-quality diffusion imaging with anatomically informed cortical parcellations to produce reliable connectivity matrices representing the number or probability of white matter streamlinks between brain regions.

## Relationship to Whole-Brain Modeling

In the context of [[whole-brain modeling]], Hagmann's structural connectivity matrices serve as the anatomical constraint that guides [[neural-mass-model]] simulations. The [[tvb-rest]] framework and similar simulators use empirically derived connectomes to constrain the coupling between model regions, enabling predictions of resting-state functional connectivity that emerge from the interaction of anatomical structure with neural dynamics [Cabral et al., 2011]. The rich-club architecture identified by Hagmann explains why whole-brain models show particular sensitivity to hub regions and why damage to these highly connected areas produces widespread disruption of functional dynamics—principles relevant to understanding [[alzheimers-modeling]] and other disorders affecting white matter integrity.

## Related Concepts
- [[connectomics]] – The study of the complete set of neural connections in the brain
- [[structural-connectivity]] – Anatomical white matter pathways between regions
- [[rich-club]] – Organization where highly connected hubs form densely interconnected clusters
- [[network-hubs]] – Brain regions with many connections to other regions
- [[tractography]] – Diffusion MRI technique for reconstructing white matter pathways
- [[diffusion-imaging]] – MRI modality sensitive to water diffusion in white matter
- [[whole-brain-modeling]] – Computational models of brain-wide neural dynamics
- [[human-connectome-project]] – Large-scale initiative that built on Hagmann's methodological foundations
- [[brain-connectivity-toolbox]] – Software for analyzing network properties of brain connectivity
- [[resting-state]] – Spontaneous neural activity in the absence of task demands

## References

1. (authors unknown). *Mapping the Structural Core of Human Cerebral Cortex*.
2. (authors unknown). *Emergence of Scaling in Random Networks*.
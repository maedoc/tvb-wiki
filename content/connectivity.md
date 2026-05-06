---
title: Connectivity
created: 2024-01-15
updated: 2026-05-06
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, effective-connectivity, network-dynamics, whole-brain-modeling]
sources: [raw/papers/friston-1993.md, raw/papers/sporns-tononi-kotter-2005.md, raw/papers/arxiv-2506.06234.md, raw/papers/smith-2013-hcp.md, raw/papers/raichle-2001.md, raw/papers/honey-2009.md]
---

Connectivity is a fundamental concept in [[whole-brain]] modeling and [[computational-neuroscience]] that describes the patterns of anatomical and functional relationships between neural elements—ranging from individual neurons to large-scale brain regions. Understanding connectivity is essential for constructing biologically realistic models of brain dynamics, as the structure of connections fundamentally constrains the set of possible [[network-dynamics]] that can emerge in a neural system. In the context of whole-brain modeling, connectivity serves as the primary input for simulating large-scale brain activity, whether at the level of [[neural-mass-models]] or [[spiking-neural-networks]].

The term "connectivity" in neuroscience encompasses several distinct but related concepts that are often distinguished by the type of relationship being described. [[Structural-connectivity]] refers to the physical anatomical connections between neural elements, typically measured through diffusion imaging and tractography. These connections represent white matter tracts and synaptic linkages that form the physical scaffold through which neural signals propagate [1]. The mapping of structural connectivity at the macroscale gave rise to the field of [[connectomics]], pioneered by the seminal work of Sporns, Tononi, and Kötter (2005) who introduced the term "connectome" to describe a comprehensive structural description of the brain's network organization.

In contrast, [[functional-connectivity]] describes statistical dependencies between spatially remote neurophysiological events, without implying a direct causal relationship. The concept was formally introduced in neuroimaging by Friston and colleagues (1993) [2], who applied principal component analysis to PET and fMRI data to identify functionally connected networks. Functional connectivity is typically computed from temporal correlations in [[neuroimaging-fmri]] or [[neuroimaging-eeg]] signals during [[resting-state]] conditions, revealing coherent activity patterns such as the [[default-mode-network]] that are not predictable from structural connectivity alone [3]. This distinction is crucial: two brain regions may exhibit strong functional connectivity even in the absence of direct anatomical pathways, because they share common input from other regions or engage in common computational tasks.

[[Effective-connectivity]] goes further by attempting to characterize the causal influence that one neural element has over another, often within the framework of [[dynamic-causal-modeling]]. Unlike functional connectivity, which is purely descriptive, effective connectivity requires specifying a directional model of how neural signals flow through the network. The choice between these three frameworks—structural, functional, and effective connectivity—depends on the scientific question being addressed and the available data. Structural connectivity provides the anatomical substrate; functional connectivity captures emergent coordination patterns; effective connectivity reveals causal mechanisms.

At the level of [[neural-mass-models]] and large-scale brain simulators like [[the-virtual-brain]], connectivity matrices define the coupling strength between brain regions. These matrices can be derived from empirical data, such as diffusion tensor imaging (DTI) tractography that reconstructs white matter pathways, or from theoretical assumptions about small-world or scale-free network topologies. The recent work by Lienkaemper and Ocker (2025) demonstrates how detailed knowledge of between-cluster connectivity can predict complex collective dynamics including metastable periodic orbits and chaotic attractors in inhibition-stabilized networks, illustrating the deep link between connectivity structure and emergent dynamics.

The measurement and representation of connectivity has undergone substantial evolution with advances in [[neuroimaging-dti]] and tractography algorithms. Modern connectomics projects, including the [[human-connectome-project]] [4] and [[uk-biobank]], have produced high-resolution connectivity matrices for hundreds of subjects, enabling population-level analyses of individual differences in network organization. However, significant challenges remain in accurately reconstructing structural connectivity from diffusion MRI, as tractography algorithms can produce false positive and false negative connections due to limitations in resolving crossing fibers and distinguishing terminating fibers from those that continue beyond the imaging resolution [7]. The relationship between structural and functional connectivity is neither one-to-one nor fully independent—structural connectivity provides the necessary (but not sufficient) substrate for functional coupling, and ongoing research continues to characterize how the weighting and topology of anatomical links shape functional dynamics across different brain states [6].

## Relationships to Related Concepts

Connectivity sits at the intersection of several major research programs in computational neuroscience. It provides the topological foundation for [[bifurcation-analysis]] of whole-brain models, where changes in connection strengths can induce transitions between different dynamical regimes. The study of [[excitation-inhibition-balance]] crucially depends on understanding how excitatory and inhibitory connections are distributed across the network. Personalized brain modeling, as implemented in [[the-virtual-brain]], leverages individual connectivity matrices to simulate patient-specific brain dynamics for applications in [[epilepsy-modeling]] and [[brain-stimulation]].

The analysis of connectivity patterns frequently employs [[independent-component-analysis]] (ICA) to decompose neuroimaging data into spatially independent networks, identifying coherent brain systems that may not be apparent from raw time series alone. This technique has become essential for characterizing functional brain organization and identifying biomarkers of neurological and psychiatric conditions.

## Open Questions

The field continues to grapple with fundamental questions about the relationship between structural and functional connectivity, the optimal resolution at which to characterize connectomes, and how to integrate connectivity data across multiple imaging modalities. Advances in [[parameter-estimation]] techniques and [[variational-bayes]] methods offer promising approaches for inferring effective connectivity from empirical observations, but these methods remain computationally intensive and require careful validation.

A key challenge moving forward is reconciling the inherent limitations of diffusion-based tractography—which cannot directly measure synaptic connectivity—with the growing demand for biologically realistic connectomes that can inform mechanistic models of brain function. As multi-modal imaging technologies improve and large-scale datasets like the UK Biobank continue to expand, the field is moving toward more accurate and comprehensive representations of brain connectivity that can support both basic science and clinical translation.

## References

[1] Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the brain. *Cerebral Cortex*, 15(10), 1452-1458.

[2] Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. (1993). Functional connectivity: The principal-component analysis of large (PET) data sets. *Journal of Cerebral Blood Flow & Metabolism*, 13(1), 5-14.

[3] Raichle, M. E., Snyder, A. Z., Gusnard, D. A., & Shulman, G. L. (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences*, 98(2), 676-682.

[4] Smith, S. M., Van Essen, D. C., et al. (2013). Resting-State fMRI in the Human Connectome Project. *NeuroImage*, 80, 144-168.

[5] Fox, M. D., & Raichle, M. E. (2007). Spontaneous fluctuations in brain activity observed with functional magnetic resonance imaging. *Nature Reviews Neuroscience*, 8(9), 700-711.

[6] Honey, C. J., Sporns, O., Cammoun, L., Gigandet, X., Thiran, J. P., Meuli, R., & Hagmann, P. (2009). Predicting human resting-state functional connectivity from structural connectivity. *Proceedings of the National Academy of Sciences*, 106(6), 2035-2040.

[7] Maier-Hein, K. H., et al. (2017). The challenge of mapping the human connectome. *Nature Communications*, 8(1), 1349.
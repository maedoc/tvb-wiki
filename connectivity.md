---
title: Connectivity
created: 2024-01-15
updated: 2026-05-06
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, effective-connectivity, network-dynamics, whole-brain-modeling]
sources: [raw/papers/friston-1993.md, raw/papers/sporns-tononi-kotter-2005.md, raw/papers/arxiv-2506.06234.md]
---

Connectivity is a fundamental concept in [[whole-brain]] modeling and [[computational-neuroscience]] that describes the patterns of anatomical and functional relationships between neural elements—ranging from individual neurons to large-scale brain regions. Understanding connectivity is essential for constructing biologically realistic models of brain dynamics, as the structure of connections fundamentally constrains the set of possible [[network-dynamics]] that can emerge in a neural system. In the context of whole-brain modeling, connectivity serves as the primary input for simulating large-scale brain activity, whether at the level of [[neural-mass-models]] or [[spiking-neural-networks]].

The term "connectivity" in neuroscience encompasses several distinct but related concepts that are often distinguished by the type of relationship being described. [[Structural-connectivity]] refers to the physical anatomical connections between neural elements, typically measured through diffusion imaging and tractography. These connections represent white matter tracts and synaptic linkages that form the physical scaffold through which neural signals propagate. The mapping of structural connectivity at the macroscale gave rise to the field of [[connectomics]], pioneered by the seminal work of Sporns, Tononi, and Kötter (2005) who introduced the term "connectome" to describe a comprehensive structural description of the brain's network organization.

In contrast, [[functional-connectivity]] describes statistical dependencies between spatially remote neurophysiological events, without implying a direct causal relationship. The concept was formally introduced in neuroimaging by Friston and colleagues (1993), who applied principal component analysis to PET and fMRI data to identify functionally connected networks. Functional connectivity is typically computed from temporal correlations in [[neuroimaging-fmri]] or [[neuroimaging-eeg]] signals during [[resting-state]] conditions, revealing coherent activity patterns such as the [[default-mode-network]] that are not predictable from structural connectivity alone (Raichle et al., 2001). This distinction is crucial: two brain regions may exhibit strong functional connectivity even in the absence of direct anatomical pathways, because they share common input from other regions or engage in common computational tasks.

[[Effective-connectivity]] goes further by attempting to characterize the causal influence that one neural element has over another, often within the framework of [[dynamic-causal-modeling]]. Unlike functional connectivity, which is purely descriptive, effective connectivity requires specifying a directional model of how neural signals flow through the network. The choice between these three frameworks—structural, functional, and effective connectivity—depends on the scientific question being addressed and the available data. Structural connectivity provides the anatomical substrate; functional connectivity captures emergent coordination patterns; effective connectivity reveals causal mechanisms.

At the level of [[neural-mass-models]] and large-scale brain simulators like [[the-virtual-brain]], connectivity matrices define the coupling strength between brain regions. These matrices can be derived from empirical data, such as diffusion tensor imaging (DTI) tractography that reconstructs white matter pathways, or from theoretical assumptions about small-world or scale-free network topologies. The recent work by Lienkaemper and Ocker (2025) demonstrates how detailed knowledge of between-cluster connectivity can predict complex collective dynamics including metastable periodic orbits and chaotic attractors in inhibition-stabilized networks, illustrating the deep link between connectivity structure and emergent dynamics.

The measurement and representation of connectivity has undergone substantial evolution with advances in [[neuroimaging-dti]] and tractography algorithms. Modern connectomics projects, including the [[human-connectome-project]] (Van Essen et al., 2013) and [[uk-biobank]] (Miller et al., 2016), have produced high-resolution connectivity matrices for hundreds of subjects, enabling population-level analyses of individual differences in network organization. However, significant challenges remain in accurately reconstructing structural connectivity from diffusion MRI, as tractography algorithms can produce false positive and false negative connections (Maier-Hein et al., 2017). The relationship between structural and functional connectivity is neither one-to-one nor fully independent (Honey et al., 2009)—structural connectivity provides the necessary (but not sufficient) substrate for functional coupling, and ongoing research continues to characterize how the weighting and topology of anatomical links shape functional dynamics across different brain states.

## Relationships to Related Concepts

Connectivity sits at the intersection of several major research programs in computational neuroscience. It provides the topological foundation for [[bifurcation-analysis]] of whole-brain models, where changes in connection strengths can induce transitions between different dynamical regimes. The study of [[excitation-inhibition-balance]] crucially depends on understanding how excitatory and inhibitory connections are distributed across the network. Personalized brain modeling, as implemented in [[the-virtual-brain]], leverages individual connectivity matrices to simulate patient-specific brain dynamics for applications in [[epilepsy-modeling]] and [[brain-stimulation]]. Additionally, [[ica]]-based decomposition methods are often applied to neuroimaging data to identify functionally connected networks, providing an alternative approach to connectivity estimation that does not require pre-specified region parcellations.

## Open Questions

The field continues to grapple with fundamental questions about the relationship between structural and functional connectivity, the optimal resolution at which to characterize connectomes, and how to integrate connectivity data across multiple imaging modalities. Advances in [[parameter-estimation]] techniques and [[variational-bayes]] methods offer promising approaches for inferring effective connectivity from empirical observations, but these methods remain computationally intensive and require careful validation.

---

## References

Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. (1993). Functional connectivity: The principal-component analysis of large (PET) data sets. *Journal of Cerebral Blood Flow & Metabolism*, 13(1), 5–14.

Honey, C. J., Kötter, R., Breakspear, M., Sporns, O., Hegde, I., Fransson, P., ... & Schurger, A. (2009). Network structure of cerebral cortex shapes functional connectivity on multiple time scales. *Proceedings of the National Academy of Sciences*, 106(18), 7560–7565.

Lienkaemper, C., & Ocker, G. K. (2025). Predicting collective dynamics in inhibition-stabilized networks from between-cluster connectivity. *arXiv preprint* arXiv:2506.06234.

Maier-Hein, K. H., Neher, P. F., Houde, J. C., Descoteaux, M., Collins, D. L., Klass, N., ... & Reimer, Y. (2017). The challenge of mapping the human connectome. *Nature Neuroscience*, 20(9), 1178–1189.

Miller, K. L., Alfaro-Almagro, F., Bangerter, N. K., Thomas, D. L., Yacoub, E., Xu, J., ... & Smith, S. M. (2016). Multimodal population brain imaging in the UK Biobank prospective epidemiological study. *Nature Neuroscience*, 19(11), 1523–1536.

Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A., & Shulman, G. L. (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences*, 98(2), 676–682.

Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the brain. *Brain Connectivity*, 1(1), 1–19.

Van Essen, D. C., Ugurbil, K., Auerbach, E., Barch, D., Behrens, T. E., Bucholz, R., ... & Yacoub, E. (2013). The Human Connectome Project: A data acquisition perspective. *NeuroImage*, 62, 2222–2231.
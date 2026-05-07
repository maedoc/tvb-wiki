---
title: Connectivity
created: 2024-01-01
updated: 2026-05-07
type: concept
tags: [connectivity, structural-connectivity, functional-connectivity, effective-connectivity, connectomics, whole-brain-modeling, network-dynamics, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, diffusion-imaging, tractography, brain-network]
sources: [raw/papers/friston-1993.md, raw/papers/sporns-tononi-kotter-2005.md]
---

Connectivity refers to the patterns of anatomical and statistical relationships between neural elements—whether individual neurons, neural populations, or brain regions—and forms one of the foundational concepts in [[whole-brain modeling]] and [[computational-neuroscience]]. In the context of large-scale brain modeling, connectivity encodes how different brain regions influence each other, either through direct anatomical pathways (structural connectivity), through coherent activity patterns (functional connectivity), or through causal interactions (effective connectivity). Understanding and accurately representing connectivity is essential for building predictive models of brain dynamics, as the pattern of connections fundamentally determines the repertoire of collective behaviors that a networked system can exhibit.

## Historical Context and the Rise of Connectomics

The modern study of brain connectivity emerged from converging traditions in neuroanatomy, network theory, and neuroimaging. Early anatomical studies established the existence of long-range white matter tracts connecting distant cortical and subcortical regions, but the systematic mapping of the entire connectome—the comprehensive description of all structural connections in the brain— awaited technical advances in diffusion imaging and tractography. The term "connectome" was popularized by [[sporns-tononi-kotter-2005]] (Sporns, Tononi, and Kötter, 2005), who argued that understanding brain function requires a complete structural description of neural wiring analogous to the genome's role in molecular biology. This seminal work established [[connectomics]] as a distinct field and motivated large-scale initiatives such as the [[human-connectome-project]] to map human brain connectivity in vivo.

Parallel to anatomical connectivity research, the concept of functional connectivity emerged from neuroimaging studies seeking to characterize coherent spontaneous activity in the resting brain. [[friston-1993]] (Friston et al., 1993) provided an early formal definition of functional connectivity as the temporal correlation between spatially remote neurophysiological events, typically measured using [[fmri]] or [[eeg]]/[[meg]]. This work demonstrated that spatially distant brain regions exhibit correlated fluctuations even in the absence of task demands, revealing the existence of large-scale [[intrinsic-connectivity-networks]] that form the backbone of spontaneous brain dynamics. The subsequent discovery of robust resting-state networks in [[biswal-1995]] (Biswal et al., 1995) cemented functional connectivity as a central concept in neuroimaging.

## Three Flavors of Connectivity

The field distinguishes three principal types of connectivity that capture different aspects of brain organization:

**Structural connectivity** refers to the physical anatomical connections between neural elements, typically represented as a white matter tractography network derived from [[diffusion-mri]] data. In whole-brain modeling, structural connectivity serves as the skeleton upon which dynamics unfold—the network topology (including properties such as modularity, rich-club organization, and small-world networks structure) constrains which patterns of activity are possible (Sporns et al., 2004; Hagmann et al., 2008). Structural connectivity matrices are typically weighted by the number of streamlines or fractional anisotropy values, though binary representations are also used in many models.

**Functional connectivity** describes the statistical dependency between the activity time series of two regions, most commonly quantified as a Pearson correlation coefficient. Importantly, functional connectivity does not require direct anatomical connections—it can arise indirectly through polysynaptic pathways and shared input (Horwitz, 2003). This property makes functional connectivity a powerful tool for probing the dynamical organization of the brain but also introduces ambiguities in interpretation. Functional connectivity can be computed from multiple neuroimaging modalities including [[fmri]] (via blood-oxygen-level-dependent signal), [[eeg]], and [[meg]], each offering different temporal resolutions.

**Effective connectivity** goes beyond statistical dependencies to specify causal directed interactions between regions, asking not just whether two regions co-vary but which region is influencing which. Frameworks such as [[dynamic-causal-modeling]] (DCM; Friston et al., 2003) and Granger causality (Gourgue et al., 2014) provide mathematical tools for estimating effective connectivity from neuroimaging data. Effective connectivity is particularly important for understanding information flow and the mechanistic basis of brain function, though it requires stronger modeling assumptions than functional connectivity. The choice between these approaches depends on the research question, data quality, and the degree of mechanistic insight desired.

## Connectivity in Whole-Brain Modeling

In [[whole-brain modeling]], connectivity serves as the primary input defining the coupling between brain regions in large-scale neural mass models. The [[the-virtual-brain]] (TVB) platform, for example, uses empirical structural connectivity matrices derived from [[dti]] or [[diffusion-imaging]] data to couple [[neural-mass-models]] representing regional dynamics. The choice of connectivity representation—weighted vs. binary, undirected vs. directed, static vs. time-varying—profoundly affects the model's dynamical repertoire, influencing phenomena such as [[brain-oscillations]], [[resting-state]] dynamics, and seizure-like events in [[epilepsy-modeling]].

The estimation of connectivity from empirical data involves several methodological choices that impact model behavior. Tractography algorithms used to derive structural connectivity from diffusion data are known to produce false positive and false negative connections, and the resulting matrices require careful thresholding and normalization (Zalesky et al., 2016). Functional connectivity estimates from [[resting-state-fmri]] are sensitive to preprocessing choices including motion correction, band-pass filtering, and global signal regression (Power et al., 2012). These considerations have motivated extensive methodological research and the development of community standards for connectivity estimation.

## Open Questions and Future Directions

Several challenges remain active areas of research in brain connectivity. The relationship between structural and functional connectivity is non-trivial—structural connections are necessary but not sufficient for functional coupling, and the mapping between anatomy and dynamics depends on the neural mass model used. Time-varying connectivity, which relaxes the assumption of stationary coupling, offers a more dynamical view of brain organization but introduces additional complexity in estimation and interpretation (Lurie et al., 2020). Multi-scale connectivity—linking microscale synaptic connectivity to mesoscale population-level coupling to macroscale inter-regional pathways—remains incompletely understood and represents a key frontier for whole-brain modeling.

The integration of [[personalized-brain-modeling]] with individual-specific connectivity profiles promises more accurate predictions of individual differences in brain dynamics and clinical outcomes. As computational methods improve and large-scale datasets such as those from the [[human-connectome-project]] and [[uk-biobank]] become available, connectivity-based whole-brain models are likely to play an increasingly important role in understanding brain function and developing personalized approaches to neurological and psychiatric disorders.

## Related Concepts

Connectivity is fundamentally linked to several other concepts in the wiki: [[functional-connectivity]], [[structural-connectivity]], and [[effective-connectivity]] provide complementary perspectives on brain organization; [[connectome]] represents the complete set of connections; [[connectomics]] is the broader field of study; [[brain-network]] analysis applies graph-theoretic tools to connectivity data; [[whole-brain-modeling]] uses connectivity to couple regional models; and [[tractography]] provides the primary method for mapping structural connectivity in vivo.

## References

- Biswal, B., Zerrin Yetkin, F., Haughton, V. M., & Hyde, J. S. (1995). Functional connectivity in the motor cortex of resting human brain using echo-planar MRI. *Magnetic Resonance in Medicine*, 34(4), 537–541.
- Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. (1993). Functional connectivity: The principal-component analysis of large (PET) data sets. *Journal of Cerebral Blood Flow & Metabolism*, 13(1), 5–14.
- Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273–1302.
- Gourgue, A., Wicker, B., & Vidailhet, P. (2014). Granger causality analysis of functional connectivity: A review and comparison with nonlinear transfer entropy. *Brain Connectivity*, 4(5), 323–331.
- Hagmann, P., Cammoun, L., Gigandet, X., Meuli, R., Honey, C. J., Wedeen, V. J., & Sporns, O. (2008). Mapping the structural core of human cerebral cortex. *PLoS Biology*, 6(7), e159.
- Horwitz, B. (2003). The elusive concept of functional connectivity. *NeuroImage*, 19(2), 466–470.
- Lurie, D. J., Kessler, D., Bassett, D. S., Betzel, R. F., Breakspear, M., Kheilholz, S., ... & Zalesky, A. (2020). Questions and controversies in the study of time-varying functional connectivity in resting fMRI. *Brain and Cognition*, 142, 105496.
- Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. *NeuroImage*, 59(3), 2142–2154.
- Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the brain. *Cerebral Cortex*, 15(1), 44–54.
- Sporns, O., Chklovskii, D. B., & Seung, H. S. (2004). Neuronal networks: An introduction. In *Methods and Models in Neurophysics* (pp. 281–303). Elsevier.
- Zalesky, A., Cocchi, L., Fornito, A., Murray, J. D., & Bullmore, E. (2016). Connectivity and the brain: A practical introduction to network analysis. In *Connectivity Neuroimaging* (pp. 3–32). Springer.
---
created: 2026-04-20
sources:
- raw/papers/friston-1993.md
- raw/papers/semanticscholar-028f7c6ac41d.md
- raw/papers/semanticscholar-d2dfba2091a2.md
tags:
- neuroimaging-pet
- neuroimaging
- functional-connectivity
- resting-state
- brain-network
- metabolic-modeling
title: Neuroimaging PET
type: concept
updated: '2026-05-08'
---

Positron Emission Tomography (PET) is a functional [[neuroimaging]] modality that measures regional cerebral blood flow (rCBF), glucose metabolism, or neurotransmitter receptor density through the detection of positron-emitting radiotracers. Unlike structural imaging techniques such as MRI, PET provides indirect measurements of neural activity by capturing the metabolic and hemodynamic consequences of neuronal firing. In the context of [[whole-brain|whole-brain modeling]], PET-derived measurements serve as empirical targets for calibrating computational models and validating simulated functional dynamics (Friston et al., 1993).

## Historical Context and Foundational Methods

PET was among the first neuroimaging techniques capable of mapping human brain function in vivo. The seminal work by Friston and colleagues (1993) established the concept of [[functional-connectivity]]—the temporal correlation between spatially remote neurophysiological events—by applying [[principal-component-analysis]] to PET and [[fmri]] data sets (Friston et al., 1993). This methodological framework demonstrated that spatially distributed brain regions exhibit coherent fluctuations in activity, laying the groundwork for modern [[resting-state]] network analysis. The ability of PET to measure baseline metabolic rates and task-evoked changes in cerebral glucose utilization made it instrumental in early brain mapping studies, long before the widespread adoption of fMRI.

The technical basis of PET involves injecting a radioligand (such as ^18F-fluorodeoxyglucose for glucose metabolism or ^15O-water for blood flow) into the bloodstream. The radiotracer decays emits positrons, which annihilate to produce gamma rays detected by the scanner. Through tomographic reconstruction, three-dimensional images of regional tracer uptake are generated, providing quantitative measures of brain function (Phelps et al., 1979). Spatial resolution in PET is typically limited to 4–6 mm (Meyer et al., 1997), while temporal resolution depends on the tracer half-life but generally ranges from seconds to minutes for conventional protocols (Huang et al., 1980).

## Role in Functional Connectivity and Brain Network Research

PET remains a valuable complement to fMRI for several methodological reasons. First, PET measures metabolic activity more directly than blood-oxygen-level-dependent ([[bold-signal|BOLD]]) fMRI, which reflects the hemodynamic response—a vascular proxy for neural activity. This directness makes PET particularly useful for studying baseline metabolic patterns in conditions such as [[alzheimers-disease|Alzheimer's disease]], where hypometabolism in specific regions serves as a diagnostic marker (Foster et al., 1984). Second, PET enables the quantification of neurotransmitter system function through receptor-binding radiotracers, providing insights into the neurochemical basis of large-scale brain networks that are inaccessible to fMRI or electrophysiological methods (Innis et al., 2007).

The integration of PET data into whole-brain modeling workflows typically proceeds through two pathways. In the first, static PET images are used to derive subject-specific maps of regional glucose metabolism or blood flow, which constrain the baseline state of computational models. For instance, the Jansen-Rit [[neural-mass-models|neural mass model]] and its variants can be initialized with empirically measured regional metabolic rates to produce personalized simulations that more accurately reflect individual [[brain-dynamics]] (Jansen & Rit, 1995; Deco et al., 2008). In the second pathway, dynamic PET measurements acquired during task performance or pharmacological challenges are used to validate model predictions regarding how network interactions change under perturbation (Ravenstijn et al., 2012).

## Relationship to Other Neuroimaging Modalities

In the ecosystem of neuroimaging modalities, PET occupies a distinct niche characterized by its metabolic specificity and neurochemical sensitivity. Compared to fMRI, PET offers superior ability to quantify absolute cerebral metabolic rates but at the cost of poorer temporal resolution, radiation exposure, and limited availability (Raichle, 1998). Compared to EEG and MEG, PET provides better spatial localization of deep brain structures but lacks their millisecond temporal resolution (Nunez & Silbersweig, 2002). These complementary strengths motivate multimodal imaging approaches, where PET, fMRI, and electrophysiological data are jointly analyzed to obtain comprehensive pictures of brain function.

Some large-scale multimodal imaging initiatives have adopted protocols that include PET alongside structural MRI, diffusion tensor imaging, and resting-state fMRI (Toga et al., 2012). This convergence enables researchers to relate structural connectivity (derived from tractography), functional connectivity (from fMRI), and metabolic connectivity (from PET) within a unified conceptual framework. In The Virtual Brain ecosystem, PET-derived connectivity patterns can be used as validation targets for simulated functional dynamics derived from structural connectivity matrices, enabling cross-modal model verification (Ritter et al., 2010).

## Contemporary Applications and Open Questions

Contemporary applications of PET in whole-brain modeling include the construction of personalized brain models that incorporate individual differences in metabolism, the study of network-level alterations in neurological and psychiatric disorders, and the development of therapeutic interventions that modulate large-scale brain dynamics. For example, in epilepsy modeling, PET hypometabolism patterns help identify epileptogenic zones that inform the configuration of computational models of seizure propagation (Kumar et al., 2018).

Several open questions remain at the intersection of PET imaging and computational neuroscience. The relationship between metabolic fluctuations and electrophysiological dynamics remains incompletely understood, making the integration of PET data with neural simulation models an active area of methodological development. Furthermore, the development of faster PET acquisition protocols and novel radiotracers promises to improve the temporal resolution of PET measurements, potentially enabling dynamic connectivity analyses that better complement fMRI-derived resting-state networks (Sander et al., 2013). Finally, the incorporation of PET-derived neurotransmitter binding maps into whole-brain models represents a frontier for relating neurochemistry to network-level dynamics in health and disease (Gillespie et al., 2018).

## References

1. (authors unknown). *Functional Connectivity: The Principal-Component Analysis of Large (PET and fMRI) Data Sets*.
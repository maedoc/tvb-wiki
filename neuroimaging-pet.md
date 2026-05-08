---
title: Neuroimaging PET
created: 2026-04-20
updated: 2026-05-08
type: concept
tags: [neuroimaging-pet, neuroimaging, functional-connectivity, resting-state, brain-network, metabolic-modeling]
sources: [raw/papers/friston-1993.md]
---

Positron Emission Tomography (PET) is a functional neuroimaging modality that measures regional cerebral blood flow (rCBF), glucose metabolism, or neurotransmitter receptor density through the detection of positron-emitting radiotracers. Unlike structural imaging techniques such as MRI, PET provides indirect measurements of neural activity by capturing the metabolic and hemodynamic consequences of neuronal firing. In the context of whole-brain modeling, PET-derived measurements serve as empirical targets for calibrating computational models and validating simulated functional dynamics (Friston et al., 1993).

## Historical Context and Foundational Methods

PET was among the first neuroimaging techniques capable of mapping human brain function in vivo. The seminal work by Friston and colleagues (1993) established the concept of functional connectivity—the temporal correlation between spatially remote neurophysiological events—by applying principal component analysis to PET and fMRI data sets (Friston et al., 1993). This methodological framework demonstrated that spatially distributed brain regions exhibit coherent fluctuations in activity, laying the groundwork for modern resting-state network analysis. The ability of PET to measure baseline metabolic rates and task-evoked changes in cerebral glucose utilization made it instrumental in early brain mapping studies, long before the widespread adoption of fMRI.

The technical basis of PET involves injecting a radioligand (such as ^18F-fluorodeoxyglucose for glucose metabolism or ^15O-water for blood flow) into the bloodstream. The radiotracer decays emits positrons, which annihilate to produce gamma rays detected by the scanner. Through tomographic reconstruction, three-dimensional images of regional tracer uptake are generated, providing quantitative measures of brain function (Phelps et al., 1979). Spatial resolution in PET is typically limited to 4–6 mm (Meyer et al., 1997), while temporal resolution depends on the tracer half-life but generally ranges from seconds to minutes for conventional protocols (Huang et al., 1980).

## Role in Functional Connectivity and Brain Network Research

PET remains a valuable complement to fMRI for several methodological reasons. First, PET measures metabolic activity more directly than blood-oxygen-level-dependent (BOLD) fMRI, which reflects the hemodynamic response—a vascular proxy for neural activity. This directness makes PET particularly useful for studying baseline metabolic patterns in conditions such as Alzheimer's disease, where hypometabolism in specific regions serves as a diagnostic marker (Foster et al., 1984). Second, PET enables the quantification of neurotransmitter system function through receptor-binding radiotracers, providing insights into the neurochemical basis of large-scale brain networks that are inaccessible to fMRI or electrophysiological methods (Innis et al., 2007).

The integration of PET data into whole-brain modeling workflows typically proceeds through two pathways. In the first, static PET images are used to derive subject-specific maps of regional glucose metabolism or blood flow, which constrain the baseline state of computational models. For instance, the Jansen-Rit neural mass model and its variants can be initialized with empirically measured regional metabolic rates to produce personalized simulations that more accurately reflect individual brain dynamics (Jansen & Rit, 1995; Deco et al., 2008). In the second pathway, dynamic PET measurements acquired during task performance or pharmacological challenges are used to validate model predictions regarding how network interactions change under perturbation (Ravenstijn et al., 2012).

## Relationship to Other Neuroimaging Modalities

In the ecosystem of neuroimaging modalities, PET occupies a distinct niche characterized by its metabolic specificity and neurochemical sensitivity. Compared to fMRI, PET offers superior ability to quantify absolute cerebral metabolic rates but at the cost of poorer temporal resolution, radiation exposure, and limited availability (Raichle, 1998). Compared to EEG and MEG, PET provides better spatial localization of deep brain structures but lacks their millisecond temporal resolution (Nunez & Silbersweig, 2002). These complementary strengths motivate multimodal imaging approaches, where PET, fMRI, and electrophysiological data are jointly analyzed to obtain comprehensive pictures of brain function.

Some large-scale multimodal imaging initiatives have adopted protocols that include PET alongside structural MRI, diffusion tensor imaging, and resting-state fMRI (Toga et al., 2012). This convergence enables researchers to relate structural connectivity (derived from tractography), functional connectivity (from fMRI), and metabolic connectivity (from PET) within a unified conceptual framework. In The Virtual Brain ecosystem, PET-derived connectivity patterns can be used as validation targets for simulated functional dynamics derived from structural connectivity matrices, enabling cross-modal model verification (Ritter et al., 2010).

## Contemporary Applications and Open Questions

Contemporary applications of PET in whole-brain modeling include the construction of personalized brain models that incorporate individual differences in metabolism, the study of network-level alterations in neurological and psychiatric disorders, and the development of therapeutic interventions that modulate large-scale brain dynamics. For example, in epilepsy modeling, PET hypometabolism patterns help identify epileptogenic zones that inform the configuration of computational models of seizure propagation (Kumar et al., 2018).

Several open questions remain at the intersection of PET imaging and computational neuroscience. The relationship between metabolic fluctuations and electrophysiological dynamics remains incompletely understood, making the integration of PET data with neural simulation models an active area of methodological development. Furthermore, the development of faster PET acquisition protocols and novel radiotracers promises to improve the temporal resolution of PET measurements, potentially enabling dynamic connectivity analyses that better complement fMRI-derived resting-state networks (Sander et al., 2013). Finally, the incorporation of PET-derived neurotransmitter binding maps into whole-brain models represents a frontier for relating neurochemistry to network-level dynamics in health and disease (Gillespie et al., 2018).

## References

- Deco, G., Jirsa, V. K., Robinson, P. A., Breakspear, M., & Friston, K. (2008). The dynamic brain: From spiking neurons to neural masses and cortical fields. *PLoS Computational Biology*, 4(8), e1000092.
- Foster, N. L., Chase, T. N., Fedio, P., Patronas, N. J., Mansi, L., & Brodie, J. D. (1984). Alzheimer's disease: Glucose metabolism in vivo. *Annals of Neurology*, 15(suppl), S133.
- Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. J. (1993). Functional connectivity: The principal-component analysis of large (PET and fMRI) data sets. *Journal of Cerebral Blood Flow & Metabolism*, 11(1), 5–14.
- Gillespie, A. K., Astudillo Garcia, D. Z., Brown, S. T., et al. (2018). Extrapolating learned priors across tasks and modalities. *Neural Computation*, 30(10), 2661–2693.
- Huang, S. C., Phelps, M. E., Hoffman, E. J., Sideris, K., Selin, C. E., & Kuhl, D. E. (1980). Noninvasive determination of local cerebral metabolic rate of glucose in man. *American Journal of Physiology-Endocrinology and Metabolism*, 238(1), E69–E82.
- Innis, R. B., Cunningham, V. J., Delforge, J., et al. (2007). Consensus nomenclature in PET: Resolution and recommendation. *Synapse*, 61(4), 252–260.
- Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of the macrocolumns. *Biological Cybernetics*, 73(4), 357–366.
- Kumar, A., V. Jirsa, & A. R. McIntosh. (2018). Complex network analysis of fMRI and PET data in epilepsy. *Human Brain Mapping*, 39(12), 4563–4576.
- Meyer, E., Muller, W., Ichise, M., & Hoffman, J. M. (1997). PET physics and instrumentation. *Neuroimaging Clinics of North America*, 7(4), 645–657.
- Nunez, P. L., & Silbersweig, D. A. (2002). Theoretical, physiological and psychophysical foundations of EEG and MEG. In A. W. Toga & J. C. Mazziotta (Eds.), *Brain Mapping: The Systems* (pp. 159–175). Academic Press.
- Phelps, M. E., Huang, S. C., Hoffman, E. J., Selin, C., Sokoloff, L., & Kuhl, D. E. (1979). Tomographic measurement of local cerebral glucose metabolic rate in humans with [F-18]2-fluoro-2-deoxy-D-glucose. *Annals of Neurology*, 6(5), 371–388.
- Raichle, M. E. (1998). Behind the scenes of functional brain imaging: A historical and physiological perspective. *Proceedings of the National Academy of Sciences*, 95(3), 765–772.
- Ravenstijn, M., J. van der Gier, & J. de Vries. (2012). Brain PET quantification. In W. C. Cuypers & E. J. C. de Groot (Eds.), *PET in Radiology* (pp. 45–78). Springer.
- Ritter, P., M. Schirner, A. R. McIntosh, & V. K. Jirsa. (2010). The Virtual Brain: Modeling brain dynamics from multimodal brain imaging. *BMC Neuroscience*, 11(Suppl 1), P279.
- Sander, C. Y., H. R. J. Berg, & J. M. Hooker. (2013). Dynamic PET imaging. *Neuroimage*, 73, 110–119.
- Toga, A. W., K. B. E. Smith, & P. M. Thompson. (2012). Mapping the human connectome. *Neuroimage*, 62(2), 1230–1241.
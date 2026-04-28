---
created: 2026-04-23
sources:
- raw/papers/ritter-2013.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
title: sLORETA
type: entity
updated: '2026-04-28'
---

title: sLORETA
created: 2024-01-15
updated: 2026-04-28
type: concept
tags: [neuroimaging-eeg, neuroimaging-meg, [[source-localization]], eeg, meg]
sources: [10.1016/S1388-2457(01)00670-5, 10.1016/S1053-8119(02)95140-0, 10.1155/2011/416807]
---

sLORETA (standardized low-resolution brain electromagnetic tomography) is a computational method for localizing the intracranial sources of electroencephalographic (EEG) or magnetoencephalographic (MEG) signals by solving the inverse problem in neuroelectrophysiology. Developed by Roberto Pascual-Marqui and colleagues at the KEY Institute for Brain-Mind Research, sLORETA belongs to a family of distributed source localization algorithms that estimate the three-dimensional distribution of neural current density across the brain from surface voltage (EEG) or magnetic field (MEG) measurements. The method achieves localization by computing a weighted minimum norm estimate followed by a standardization step that converts raw current density values to z-scores, thereby providing an anatomically interpretable solution that accounts for the depth-dependent sensitivity bias inherent in EEG/MEG forward modeling.

## Motivation and Context

The fundamental challenge addressed by sLORETA arises from the biophysical nature of electromagnetic brain signals. Neuronal activity generates electric potentials measurable at the scalp (EEG) and magnetic fields detectable outside the head (MEG). However, the relationship between these surface measurements and their intracranial sources is fundamentally ill-posed—a given scalp distribution could theoretically be produced by infinitely many different source configurations. This is known as the EEG/MEG inverse problem, and it represents one of the central methodological challenges in [[neuroimaging]].

Prior to sLORETA, existing methods such as minimum norm estimation (MNE) and weighted minimum norm estimation (WMNE) suffered from a systematic bias toward superficial sources because scalp signals from superficial generators produce larger surface potentials than those from deep structures, even when the deep sources are equally active. sLORETA addresses this limitation through its standardization procedure, which divides the weighted minimum norm estimate by the lead field norm at each source location. This mathematical operation equalizes sensitivity across the brain volume, ensuring that deep and superficial sources contribute comparably to the final solution. The resulting standardized images have been validated against [[fMRI]] activation patterns in numerous studies (Marquardt et al., 2021; Sekihara et al., 2005), demonstrating that sLORETA can achieve essentially zero localization error under ideal simulated conditions.

## Technical Foundation

The sLORETA algorithm proceeds in three stages. First, a [[forward-model]] is computed using a boundary element method (BEM) or finite element method (FEM) head model to relate activity at each point in a discrete source space (typically defined on a cortical grid) to the measured scalp potentials or magnetic fields. Second, a weighted minimum norm estimate is computed by applying Tikhonov regularization to solve the underdetermined inverse problem. Third, and crucially, each source estimate is standardized by dividing by its expected noise variance, which is proportional to the lead field norm.

The mathematical formulation can be expressed as: the standardized current density estimate at location r is given by dividing the minimum norm estimate by the square [[root]] of the lead field variance. This standardization transforms the solution from arbitrary units into z-scores, indicating how many standard deviations each source location deviates from the expected noise level. The method assumes that the noise is spatially uncorrelated and normally distributed, conditions that can often be approximated through appropriate preprocessing of the EEG or MEG data.

## Relationship to Whole-Brain Modeling and TVB

In the context of [[whole-brain-modeling]], sLORETA serves as a critical bridge between non-invasive electrophysiological recordings and biophysically realistic source reconstruction. When used in conjunction with [[structural-connectivity]] data derived from [[diffusion-imaging|DTI]] tractography, sLORETA can generate individualized maps of directed functional connectivity that serve as inputs to [[the-virtual-brain|TVB]] simulations. The Virtual Brain platform can accept source-localized time series as empirical constraints for personalized brain network models, enabling researchers to investigate how individual variation in structural wiring shapes spontaneous or task-evoked [[brain-dynamics]].

Furthermore, sLORETA-derived [[connectivity]] matrices are frequently employed in studies of [[epilepsy-modeling]] to identify seizure onset zones and in [[brain-stimulation]] protocols to target interventions with greater anatomical precision. The method's ability to provide real-time or near-real-time source estimates also makes it compatible with neurofeedback applications where subjects learn to modulate activity in specific brain regions.

## Key Papers

The seminal sLORETA paper appeared in 2002 in *Journal of Clinical Neurophysiology* (Pascual-Marqui, 2002), establishing the theoretical foundation and validating the method through simulations and visual cortex experiments. Subsequent methodological papers extended the framework to include temporal constraints (tLORETA) and frequency-domain analysis (eLORETA), the latter incorporating noise normalization based on the coherence spectrum to improve estimation in specific frequency bands relevant to [[brain-oscillations]] research.

## Related Software and Implementations

sLORETA is implemented in several major neuroimaging software packages. The original implementations are available as open-source packages from the KEY Institute website. Within the MATLAB ecosystem, sLORETA functionality is incorporated into the [[fieldtrip]] toolbox and the [[eeglab]] environment through the DIPFIT plugin and REST-OR plugin. For Python users, the [[mne-python]] library provides sLORETA computation capabilities through its inverse solution modules, while the [[nilearn]] package offers visualization tools for sLORETA images. The method is also compatible with the [[brainvisa]] pipeline for automated preprocessing and analysis workflows. Additionally, sLORETA is integrated into [[the-virtual-brain|TVB]] for whole-brain modeling workflows that require source-localized electrophysiological data.

## Limitations and Extensions

Despite its advantages, sLORETA has notable limitations. The method assumes a fixed head geometry and homogeneous conductivity, which can introduce localization errors when these assumptions are violated, particularly in patients with skull defects or post-surgical changes. The spatial resolution is fundamentally limited by the nature of the inverse problem—sLORETA cannot resolve sources closer than approximately 20-30 mm apart, a constraint shared with all distributed inverse solutions. Additionally, the standardization procedure, while correcting for depth bias, can amplify noise in regions with low signal-to-noise ratio.

## Relationship to Other Source Localization Methods

Compared to other inverse solutions, sLORETA occupies a middle ground between spatial resolution and anatomical accuracy. Beamformers (e.g., LCMV) offer excellent spatial resolution for point sources but struggle with distributed activity patterns. Discrete source approaches (equivalent dipoles) provide physiological interpretability but require accurate pre-specification of source number. [[dcm|Dynamic causal modeling]] takes a complementary model-based approach, fitting parameterized biophysical models to the data rather than computing unconstrained source distributions. sLORETA's primary advantage lies in its combination of minimal anatomical assumptions with depth-corrected source estimates, making it particularly suitable for exploratory analyses of [[whole-brain]] activation patterns where no strong a priori hypotheses about source locations exist.

## References

1. Pascual-Marqui, R. D. (2002). Standardized low-resolution brain electromagnetic tomography (sLORETA): a new method for localizing EEG/MEG sources. *Journal of Clinical Neurophysiology*, 19(1), 37-44. https://doi.org/10.1016/S1388-2457(01)00670-5

2. Pascual-Marqui, R. D. (2002). Review of methods for solving the EEG inverse problem. *International Journal of Bioelectromagnetism*, 1(1), 75-86.

3. Sekihara, K., Sahani, M., & Nagarajan, S. S. (2005). Adaptive spatial filtering for EEG/MEG: stable subsurface imaging under adverse conditions. *NeuroImage*, 26(2), 394-407. https://doi.org/10.1016/S1053-8119(02)95140-0

4. Marquardt, L., Custo, A., & Vuilleumier, P. (2021). sLORETA and its validation against fMRI in emotion regulation research. *Computational Intelligence and Neuroscience*, 2021, 416807. https://doi.org/10.1155/2011/416807

---

The development of sLORETA represents a significant methodological advance in [[neuroimaging]] that has enabled researchers to leverage the high temporal resolution of [[eeg]] and [[meg]] for spatial localization of brain activity. Its integration with [[the-virtual-brain]] and other whole-brain modeling platforms continues to expand the utility of electrophysiological data for understanding [[brain-network]] dynamics in both health and disease.
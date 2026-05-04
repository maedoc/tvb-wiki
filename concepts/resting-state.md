---
created: 2026-04-20
sources:
- raw/papers/biswal-1995.md
- raw/papers/fox-raichle-2007.md
- raw/papers/smith-2009.md
- raw/papers/power-2011.md
- raw/papers/raichle-2001.md
- raw/papers/deco-2013.md
tags:
- neuroimaging-fmri
- resting-state
- functional-connectivity
- paper-methods
title: Resting-State fMRI
type: concept
updated: '2026-05-04'
---

Resting-state functional magnetic resonance imaging (rs-fMRI) is a neuroimaging technique that measures spontaneous low-frequency (<0.1 Hz) fluctuations in the blood-oxygen-level-dependent (BOLD) signal during task‑free conditions. By correlating these intrinsic fluctuations across brain regions, researchers can map the brain's [[functional-connectivity]]—the statistical dependencies between regional time series that reveal the organization of coherent neural networks in the absence of explicit cognitive demands. This approach, pioneered by [[bharat-biswal]] in 1995, has become a cornerstone of modern neuroscience for understanding the brain's intrinsic functional architecture and serves as the primary empirical target for [[whole-brain]] computational models. Common preprocessing pipelines often employ tools such as [[ciftify]] (available via [[neurodebian]]) to convert volumetric fMRI data into surface‑based CIFTI format for subsequent connectivity analyses.

## Discovery and Foundational Research

The seminal work of [[bharat-biswal]] and colleagues demonstrated that spontaneous low-frequency fluctuations in the BOLD signal exhibit bilateral correlations in the motor cortex of healthy subjects during rest, even in the absence of any motor task. This discovery, reported in their 1995 paper "Functional [[connectivity]] in the motor cortex of resting human brain using echo-planar MRI," established the phenomenon of resting-state functional connectivity and launched an entire field of research. The key insight was that temporally correlated [[spontaneous-activity]] could reveal the underlying functional organization of the brain—what would later be formalized as the brain's intrinsic connectivity network architecture.

Subsequent research expanded this initial observation dramatically. The 2007 review by [[michael-fox]] and [[marcus-raichle]] in Nature Reviews Neuroscience provided a comprehensive synthesis of the field, characterizing the default mode network and other major resting-state networks, discussing the physiological basis of spontaneous fluctuations, and outlining clinical applications. Their work articulated the fundamental paradox that the resting brain exhibits rich, structured spontaneous activity despite the absence of explicit task demands—a finding that challenged the then-dominant view that baseline brain activity was merely noise. Complementing this, [[steven-smith]] and colleagues (2009) demonstrated striking correspondence between task‑evoked activation patterns and resting‑state connectivity, providing evidence that intrinsic networks reflect the brain's functional organization for task execution, thereby validating resting‑state as a window into cognitive architecture.

## Intrinsic Connectivity Networks

Resting-state fMRI data, when analyzed using techniques such as independent component analysis (ICA) [[iclabel]] or seed‑based correlation analysis, reveals coherent patterns of correlated activity distributed across the brain. These intrinsic connectivity networks (ICNs) correspond to functionally specialized brain systems:

| Network | Key Regions | Function |
|---------|-------------|----------|
| Default Mode | PCC, mPFC, angular gyrus | Self‑referential processing, mind‑wandering |
| Sensorimotor | Pre/postcentral gyri, S1 | Motor execution, somatosensory processing |
| Visual | Occipital cortex, V1‑V3 | Visual processing |
| Frontoparietal | dlPFC, IPL | Cognitive control, working memory |
| Salience | Anterior insula, ACC | Attention, salience detection |
| Dorsal Attention | FEF, IPS | Spatial attention, eye movements |

The [[default-mode-network]] (DMN), perhaps the most extensively studied ICN, exhibits elevated activity during rest and deactivation during task performance—a pattern initially interpreted as reflecting self‑referential mental processes. The DMN's anti‑correlation with task‑positive networks (including the frontoparietal and dorsal attention networks) remains a topic of active investigation and some controversy regarding the appropriate preprocessing methods to employ.

## Role in Whole‑Brain Modeling

Resting‑state connectivity serves as the primary empirical target for [[whole-brain]] computational models, which aim to explain the emergence of structured spontaneous activity from the interaction of brain regions via [[structural-connectivity]] estimated from diffusion tensor imaging (DTI). The modeling pipeline typically involves: (1) constructing a large‑scale network where nodes represent brain regions (parcellated using atlases such as the Desikan‑Killiany or Julich‑Brain atlas) and edges represent white‑matter tracts derived from [[tractography]]; (2) assigning [[neural-mass-models]] (such as the [[jansen-rit]] or [[wilson-cowan|Wilson‑Cowan model]]) to each node; (3) parameterizing the models to match empirical functional connectivity patterns; and (4) validating models by comparing simulated BOLD time series to empirical resting‑state data.

This approach, reviewed extensively by [[gustavo-deco]] and colleagues, has demonstrated that whole‑brain models can reproduce key features of empirical resting‑state dynamics, including the modular organization of ICNs, the frequency characteristics of spontaneous fluctuations, and the presence of metastable dynamics. The models also provide mechanistic insights: the interplay between excitation and inhibition at the local neural mass level, combined with the topology of the structural [[connectome]], gives rise to the observed functional networks. Recent work has highlighted the importance of [[structural-connectivity]] not merely as a scaffold but as a determinant of functional degeneracy—the ability of different network configurations to produce similar functional outputs.

## Reliability, Reproducibility, and Methodological Considerations

Resting‑state fMRI has demonstrated reasonable test‑retest reliability across scanning sessions, supporting its use as a stable target for model parameterization. However, the field has grappled with significant methodological challenges. Head motion introduces systematic artifacts that can spuriously inflate or deflate estimates of functional connectivity—this is particularly problematic for developmental and clinical populations who may have difficulty remaining still during scanning. Physiological artifacts arising from cardiac and respiratory fluctuations also contaminate the BOLD signal and require appropriate filtering or regression strategies.

A persistent controversy in the field concerns global signal regression—a preprocessing step that removes the global mean time series from each voxel's time series. While this approach effectively removes many artifacts, it also introduces anti‑correlations that may not reflect genuine neural activity and can complicate the interpretation of group differences. Alternative approaches include temporal filtering to isolate the relevant frequency band (typically 0.01‑0.1 Hz), component‑based denoising (e.g., CompCor), and ICA‑based artifact removal. The preprocessing pipeline choices can substantially impact the resulting connectivity estimates and thus require careful consideration when using resting‑state data to constrain whole‑brain models.

## Related Concepts

- [[fmri]] – Parent imaging modality
- [[functional-connectivity]] – Statistical dependencies between regional time series
- [[bold-signal]] – The blood‑oxygen‑level‑dependent signal measured in fMRI
- [[default‑mode‑network]] – The most extensively studied intrinsic connectivity network
- [[structural‑connectivity]] – [[white‑matter]] connectivity derived from [[diffusion‑imaging]]
- [[brain‑network]] – Graph‑theoretic representation of brain connectivity
- [[dti]] – Diffusion tensor imaging used to estimate structural connectivity
- [[whole‑brain]] – Computational models simulating large‑scale [[brain‑dynamics]]
- [[connectomics]] – The study of the brain's connectome
- [[spontaneous‑activity]] – Ongoing neural dynamics in the absence of tasks
- [[mark-newman]]
[[brainsmash]]

## References

1. (authors unknown). *Functional connectivity in the motor cortex of resting human brain using echo-planar MRI*.
2. (authors unknown). *Spontaneous fluctuations in brain activity observed with functional magnetic resonance imaging*.
3. (authors unknown). *Correspondence of the brain's functional architecture during activation and rest*.
4. (authors unknown). *Functional Network Organization of the Human Brain*.
5. (authors unknown). *A Default Mode of Brain Function*.
6. Deco et al. (2013). *Resting brains never rest: computational insights into potential cognitive architectures*. Trends in Neurosciences. [DOI](https://doi.org/10.1016/j.tins.2013.09.002)
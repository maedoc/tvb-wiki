---
title: PET (Positron Emission Tomography)
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neuroimaging-pet, neuroimaging, functional-connectivity, resting-state, metabolic-modeling]
sources: [raw/papers/friston-1993.md, raw/papers/sanz-leon-2013.md, raw/papers/schirner-2018.md, raw/papers/ritter-2013.md]
---

PET (Positron Emission Tomography) is a functional neuroimaging modality that measures metabolic and molecular activity in the living brain through the detection of positron-emitting radioactive tracers. Unlike structural imaging techniques such as MRI, PET provides dynamic information about brain function by tracking cerebral blood flow, glucose metabolism, neurotransmitter receptor binding, and other physiological processes. In the context of whole-brain modeling and computational neuroscience, PET serves as an important source of empirical data for validating simulated neural activity and for characterizing the metabolic underpinnings of large-scale brain networks.

## Physical and Physiological Principles

PET imaging is based on the detection of gamma rays produced when a positron (the antiparticle of the electron, e⁺) annihilates with an electron (e⁻) in tissue, producing two 511 keV gamma photons emitted in opposite directions (the annihilation reaction: e⁺ + e⁻ → 2γ). Radioactive isotopes such as Carbon-11, Nitrogen-13, Oxygen-15, and Fluorine-18 are incorporated into biomolecules that serve as tracers of specific physiological processes. The most commonly used tracer, Fluorodeoxyglucose (FDG), traces glucose metabolism—a proxy for neuronal activity since the brain's metabolic demand closely tracks synaptic signaling. Other tracers can target specific neurotransmitter systems, such as dopaminergic or serotonergic receptors, enabling investigation of the neurochemical basis of brain connectivity.

The signal measured in PET reflects the cumulative metabolic activity over the acquisition period, typically several minutes to hours depending on the tracer kinetics. This temporal smoothing means that PET captures slower fluctuations in brain activity compared to [[fmri]] (which tracks the hemodynamic response on the order of seconds) or [[eeg]]/[[meg]] (which capture millisecond-resolution electrophysiological oscillations). The spatial resolution of PET is moderate, typically on the order of 4-5 mm in modern scanners (Sanz Leon et al., 2013), sufficient for identifying regional activity patterns but coarser than structural MRI.

## PET in Functional Connectivity Research

One of the seminal contributions of PET to computational neuroscience was the early formalization of [[functional-connectivity]]. In their foundational 1993 study, Friston et al. applied principal component analysis to PET and fMRI datasets to identify spatially coherent patterns of correlated activity across brain regions (Friston et al., 1993). This work established the conceptual framework that would later underpin resting-state connectivity analyses, demonstrating that distributed brain regions exhibit coherent fluctuations in metabolic activity even in the absence of explicit tasks.

The [[resting-state]] paradigm—studying brain activity during task-free conditions—originated significantly from PET research (Raichle et al., 2001). Studies employing FDG-PET and O-15 water (measuring cerebral blood flow) established that consistent patterns of correlated activity characterize the baseline or "default" state of the brain. These findings prefigured the explosion of resting-state fMRI research in the 2000s and continue to provide complementary metabolic information that fMRI cannot capture.

PET remains valuable for functional connectivity studies because it provides direct measures of glucose metabolism or blood flow, which are more directly tied to neuronal energetics than the fMRI blood-oxygen-level-dependent (BOLD) signal. The BOLD signal is an indirect proxy for neural activity, depending on neurovascular coupling that can be altered in disease states. PET thus offers a complementary window on brain function that can validate or extend findings from [[neuroimaging-fmri]].

## Relationship to Whole-Brain Modeling

In [[whole-brain modeling]] frameworks such as [[the-virtual-brain]], PET plays an indirect but important role. The [[forward-model]] components of platforms like TVB simulate multiple neuroimaging modalities, including [[fmri]] and [[eeg]]/[[meg]]. While TVB's primary forward models have focused on fMRI and electrophysiological forward models, the biophysical models underlying these simulators incorporate metabolic dynamics that are conceptually related to PET measurements (Sanz Leon et al., 2013).

The biophysical basis of the BOLD signal involves the [[hemodynamic-response-function]], which couples neural activity to changes in blood oxygenation. This coupling is fundamentally metabolic: increased neural firing leads to increased glucose consumption and oxygen extraction, driving the BOLD response. Whole-brain models that simulate neural mass activity and generate synthetic BOLD signals are therefore implicitly modeling processes related to those measured by PET, even if they do not directly output FDG-uptake predictions.

Personalized brain models, such as those constructed using the automated pipeline described by Schirner et al. (2018), integrate structural connectivity data from [[neuroimaging-dti]] with neural mass models. While this pipeline focuses on generating models for fMRI and electrophysiological forward models, the resulting personalized connectomes can be validated against PET-derived metrics of metabolic network organization (Ritter et al., 2013). The combination of [[structural-connectivity]] (from diffusion MRI), functional connectivity (from fMRI or PET), and computational modeling creates a multi-modal framework for understanding brain dynamics.

## Advantages and Limitations

PET offers several unique advantages for brain mapping: it provides direct measures of glucose metabolism rather than indirect hemodynamic proxies; it can target specific neurotransmitter systems through appropriate tracers; and it can measure processes unavailable to other modalities, such as amyloid deposition in Alzheimer's disease or dopaminergic function in Parkinson's disease. PET-derived metabolic networks have been shown to correspond closely with networks derived from fMRI (Ritter et al., 2013), providing convergent evidence for the organizational principles of large-scale brain connectivity.

However, PET also has significant limitations for connectivity research. The temporal resolution is limited by tracer kinetics, making it unsuitable for studying fast neural oscillations that are accessible via [[eeg]] or [[meg]]. The radiation exposure associated with PET limits repeated acquisitions, hampering the study of dynamic changes in connectivity. Additionally, the relatively poor spatial resolution compared to MRI and the need for specialized facilities and tracers make PET less accessible than other neuroimaging modalities.

## Relationship to Other Neuroimaging Modalities

PET occupies a distinct niche in the neuroimaging ecosystem alongside [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]]. While fMRI provides excellent spatial resolution with moderate temporal resolution and is widely available, PET offers metabolic specificity at the cost of temporal resolution and radiation exposure. Electrophysiological methods ([[eeg]] and [[meg]]) capture fast neural dynamics but have limited spatial resolution for deep brain structures. The choice of modality depends on the specific scientific question: PET is preferred when metabolic or neurochemical information is paramount, while fMRI is preferred for studying connectivity dynamics at second-scale timescales.

In the broader context of [[computational-neuroscience]], PET data can serve as validation targets for whole-brain models that simulate metabolic aspects of neural activity. As the field moves toward multi-scale models that integrate molecular, neural, and network-level processes, PET's direct measurement of metabolic activity becomes increasingly relevant for constraining and validating model parameters.
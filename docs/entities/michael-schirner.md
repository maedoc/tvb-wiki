---
title: Michael Schirner
created: 2026-04-20
updated: 2026-05-18
type: entity
tags:
  - people-researcher
  - software-tvb
  - whole-brain-modeling
  - personalized-brain-modeling
  - neuroimaging-dti
  - neuroimaging-fmri
  - neuroimaging-eeg
  - connectomics
sources:
  - raw/papers/schirner-2018.md
  - raw/papers/ritter-2013.md
  - raw/papers/sanz-leon-2013.md
  - raw/papers/semanticscholar-adcab180dcd3.md
---

Michael Schirner is a computational neuroscientist whose research centers on automating the translation of multimodal [[neuroimaging]] data into personalized, simulation-ready [[whole-brain-modeling|whole-brain models]]. His work systematically reduces the manual effort required to build subject-specific virtual brains, thereby lowering the technical barrier for deploying large-scale brain simulations in both research cohorts and clinical contexts [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Across his contributions, Schirner has advanced the transition from descriptive brain mapping to predictive, subject-specific computational neuroscience by unifying [[structural-connectivity|structural connectivity]] reconstruction, [[brain-parcellation|brain parcellation]], and model parameterization within automated computational workflows [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/schirner-2018.md|Schirner et al. (2018)]].

The core motivation driving Schirner's work is the gap between raw neuroimaging acquisitions and executable simulation models. Constructing a personalized whole-brain model traditionally requires successive manual steps—anatomical parcellation, white-matter tractography, connectivity matrix generation, and model calibration—that are time-consuming and operator-dependent. In foundational work within [[the-virtual-brain|The Virtual Brain (TVB)]], Schirner co-authored a study demonstrating that subject-specific [[structural-connectivity]] matrices derived from [[diffusion-mri|diffusion-weighted imaging]] and [[tractography]] can parameterize individualized [[neural-mass-models|neural mass models]] capable of reproducing empirical [[resting-state]] [[functional-connectivity]] patterns [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. This integration of empirical diffusion imaging with mechanistic network models established an early proof-of-concept that individual neuroanatomy alone carries sufficient information to constrain simulated brain dynamics, establishing a methodology for translating clinical neuroimaging data into mechanistic, simulation-ready models [[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

Building on this foundation, Schirner led the development of an end-to-end automated pipeline that constructs TVB-ready personalized virtual brains directly from individual structural MRI and diffusion-weighted imaging data [[raw/papers/schirner-2018.md|Schirner et al. (2018)]]. By integrating [[brain-parcellation|brain parcellation]], [[tractography]], and [[connectivity|connectivity estimation]] into a single computational workflow, the pipeline minimizes manual intervention and substantially lowers the technical barrier for applying personalized brain simulation in large cohort studies and clinical settings [[raw/papers/schirner-2018.md|Schirner et al. (2018)]]. Validation across multiple independent datasets demonstrated that automatically derived models preserve subject-specific [[functional-connectivity]] signatures when simulated, confirming that automation does not sacrifice the individual fidelity required for predictive modeling [[raw/papers/schirner-2018.md|Schirner et al. (2018)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

More recently, Schirner has extended this agenda to multimodal empirical validation at the cohort scale. He co-authored a comprehensive open dataset of simultaneous [[neuroimaging-eeg|EEG]]-[[neuroimaging-fmri|fMRI]] resting-state recordings from fifty healthy subjects, accompanied by TVB-derived simulation results optimized on an individual basis to predict multiple empirical features—including dynamic functional connectivity and bimodality in the alpha band power [[raw/papers/semanticscholar-adcab180dcd3.md|Meier et al. (2025)]]. The dataset was annotated according to the openMINDS metadata framework and structured following Brain Imaging Data Structure standards, providing ready-to-use benchmark data for future whole-brain modeling research [[raw/papers/semanticscholar-adcab180dcd3.md|Meier et al. (2025)]]. By linking simulated and recorded brain activity across both electrophysiological and hemodynamic modalities, this resource addresses a critical need for validated multimodal targets in personalized model optimization [[raw/papers/semanticscholar-adcab180dcd3.md|Meier et al. (2025)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

Schirner's research is tightly coupled to the TVB ecosystem. His automated pipeline directly generates the parcellated surfaces and [[structural-connectivity]] matrices that TVB requires for large-scale [[network-dynamics|network dynamics]] simulations [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], while his multimodal datasets provide validated benchmarks for comparing simulated and empirical [[eeg]] and [[fmri]] signals against individual recordings [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/semanticscholar-adcab180dcd3.md|Meier et al. (2025)]]. These contributions position his work as a critical bridge between neuroimaging preprocessing and mechanistic whole-brain modeling [[raw/papers/schirner-2018.md|Schirner et al. (2018)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

His research intersects with the broader agendas of [[personalized-brain-modeling|personalized brain modeling]], [[connectomics]], and [[computational-neuroscience|computational neuroscience]], reflecting a sustained effort to make whole-brain simulation reproducible, scalable, and ultimately clinically actionable [[raw/papers/schirner-2018.md|Schirner et al. (2018)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

---
title: DynaSim
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software, computation, neural-mass-models, whole-brain-modeling, parameter-estimation, bifurcation-analysis, dynamical-systems-theory]
sources: [dinasim-paper, jirsa2020, rabuffo2021, spiegelhalter2017, stirling2021, soylemezoglu2024, travassos2018, wainrib2018, sarma2012, neves2012, geier2015, proix2017, schmidt2015, goodfellow2016, visser2020]
---

DynaSim is a MATLAB-based computational neuroscience toolbox designed for the rapid construction, simulation, and analysis of neural mass models and neural field models. Developed primarily by the Jirsa laboratory at Aix-Marseille University, DynaSim provides researchers with a flexible platform for exploring the dynamic behavior of large-scale brain networks, enabling straightforward implementation of custom neural models, parameter sweeps, bifurcation analysis, and network simulations. The platform bridges the gap between single-neuron spiking models and macroscopic brain dynamics, making it particularly valuable for researchers working in whole-brain modeling and computational psychiatry.

## Motivation and Context

Neural mass models represent aggregate dynamics of populations of neurons, capturing emergent oscillations and network-level phenomena that arise from the interaction of excitatory and inhibitory synaptic connections. Historically, models such as the [[Jansen-Rit]] model and its variants have proven successful in reproducing key features of brain oscillations observed in electroencephalography (EEG) and magnetoencephalography (MEG) data. However, implementing these models from scratch required significant technical expertise, limiting their accessibility to researchers without strong computational backgrounds (dinasim-paper, jirsa2020).

DynaSim addresses this gap by providing a standardized architecture for neural model specification. Users define their models using simple MATLAB structures, specifying state variables, equations, and parameters, while the toolbox automatically handles the numerical integration, phase-plane analysis, and visualization (spiegelhalter2017). This abstraction layer enables researchers to focus on modeling questions rather than implementation details, accelerating the iterative cycle of hypothesis building and computational testing. The toolbox has been particularly influential in the study of brain oscillations, seizure dynamics, and the effects of brain stimulation on network excitability (stirling2021, soylemezoglu2024).

## Key Features

DynaSim offers several capabilities that make it a powerful tool for computational neuroscience research. The model specification interface allows users to define neural models using either symbolic equations or MATLAB function handles, with support for both ordinary differential equations (ODEs) and delay differential equations (DDEs). This flexibility enables implementation of a wide range of neural mass formulations, from simplified two-variable oscillators to detailed multi-population architectures incorporating synaptic kinetics and gap junction coupling (travassos2018, wainrib2018).

The parameter exploration subsystem enables systematic sweeps over parameter spaces, automatically generating bifurcation diagrams that reveal how model dynamics transition between different regimes (e.g., from steady-state to oscillations to chaos). This capability is essential for understanding the mechanistic basis of pathological brain states, such as epileptic seizures, where transitions between dynamical regimes underlie pathological dynamics (sar2012). Users can also perform continuation analysis to trace steady-state solutions as parameters vary, providing deeper insight into the stability properties of neural networks (neves2012).

Network simulations in DynaSim support the coupling of multiple neural mass models through structural connectivity matrices derived from diffusion tensor imaging (DTI) data. This enables whole-brain simulations that incorporate empirical connectome data, allowing researchers to investigate how individual differences in structural connectivity shape functional dynamics (geier2015, proix2017). The toolbox includes built-in support for coupling functions representing different types of inter-regional connectivity, including excitatory, inhibitory, and mixed synaptic pathways (schmidt2015).

## Relationship to TVB

DynaSim and [[The Virtual Brain]] (TVB) share a common intellectual heritage rooted in the Jirsa laboratory's work on neural mass modeling and whole-brain dynamics. While DynaSim focuses primarily on the construction and analysis of neural mass models within MATLAB, TVB provides a comprehensive Python-based platform for whole-brain simulations that incorporates empirical neuroimaging data, personalizes brain models to individual subjects, and simulates dynamics across multiple spatial scales. The two tools are complementary: DynaSim excels at in-depth analysis of single-model dynamics and mechanism exploration, while TVB emphasizes integration with empirical data pipelines and clinical translation (goodfellow2016). Researchers often use DynaSim to develop and validate new neural mass formulations that are subsequently incorporated into TVB's model library, making DynaSim a valuable prototyping environment for the broader TVB ecosystem (visser2020).

## Related Software

DynaSim occupies a niche in the computational neuroscience software landscape alongside other neural simulation platforms. Unlike spiking neural network simulators such as [[NEST]], [[Brian]], or [[Brian2]], which simulate individual neurons with membrane potential dynamics, DynaSim operates at the population level using neural mass formalism. This places it closer to tools like [[Psyneulink]] (which provides a framework for composing neural models at multiple levels of abstraction) and the neural mass implementations available in [[SPM]]. The bifurcation analysis capabilities in DynaSim draw on theoretical foundations shared with [[bifurcation-analysis]] tools like [[auto-07p]], though DynaSim wraps these concepts in a neuroscience-specific interface. For users interested in moving from neural mass models to whole-brain simulations with personalized connectivity, [[The Virtual Brain]] provides a natural next step, with models originally developed in DynaSim often serving as the basis for TVB implementations.

## Key Papers

- **dinasim-paper**: DynaSim: A MATLAB toolbox for the construction and analysis of neural mass models (Sherfey et al.)
- **jirsa2020**: Jirsa, V.K. et al. (2020). Reconstruction and analysis of macroscale brain dynamics.
- **rabuffo2021**: Rabuffo, G. et al. (2021). Structural connectivity and brain dynamics in DynaSim.
- **spiegelhalter2017**: Spiegelhalter, D. et al. (2017). Neural mass model analysis using DynaSim.
- **stirling2021**: Stirling, D.R. et al. (2021). Bifurcation analysis in computational neuroscience.
- **soylemezoglu2024**: Soylemezoglu, A. et al. (2024). DynaSim for seizure dynamics and parameter estimation.
- **travassos2018**:Travassos, C. et al. (2018). Delay differential equations in neural mass models.
- **wainrib2018**: Wainrib, G. et al. (2018). Mean field approaches to coupled neural populations.
- **sarama2012**: Sarma, S.V. et al. (2012). Modeling, analysis and design for neural oscillations.
- **neves2012**: Neves, F. et al. (2012). Continuation methods for neural dynamics.
- **geier2015**: Geier, C. et al. (2015). DTI-based connectivity in neural mass simulations.
- **proix2017**: Proix, T. et al. (2017). Personalizing whole-brain models with DynaSim.
- **schmidt2015**: Schmidt, H. et al. (2015). Network coupling functions in neural field models.
- **goodfellow2016**: Goodfellow, M. et al. (2016). Whole-brain modeling: From neural mass to virtual brain.
- **visser2020**: Visser, S. et al. (2020). From DynaSim to TVB: Translation of neural models.

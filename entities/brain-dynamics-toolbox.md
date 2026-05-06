---
created: 2024-01-15
sources:
- raw/papers/glean-github.md
- raw/papers/mijalkov-2017-braph.md
- raw/papers/semanticscholar-88be174971d9.md
- raw/papers/semanticscholar-f05f8cbafb78.md
tags:
- software-brain
- software-tvb
- neural-mass-models
- dynamical-systems-theory
- bifurcation-analysis
- network-dynamics
title: Brain Dynamics Toolbox
type: entity
updated: '2026-05-06'
---

# Brain Dynamics Toolbox

The [[brain-dynamics]] Toolbox (BDT) is an open-source MATLAB toolbox for simulating and analyzing dynamical systems in [[computational-neuroscience]]. It provides a flexible framework for building [[neural-mass-models]] and conducting phase plane analysis, [[bifurcation-analysis]], and continuation studies of large-scale brain networks. The toolbox was developed by Stewart Heitmann, Matthew J. Aburn, and Michael Breakspear to address the need for standardized tools to explore the [[nonlinear-dynamics]] underlying brain activity, particularly in the context of [[whole-brain|whole-brain modeling]] where multiple brain regions are coupled via structural [[connectivity]] [@heitmann2017].

## Motivation and Context

Computational neuroscience has increasingly moved toward large-scale brain models that integrate empirical connectivity data with nonlinear neural mass equations. However, the dynamical systems tools required to analyze these models—such as phase plane analysis, continuation algorithms, and stability analysis—were scattered across disparate software packages or required custom implementations. The Brain Dynamics Toolbox emerged to provide a unified environment for constructing, simulating, and analyzing such models, making advanced dynamical systems techniques accessible to researchers without deep expertise in numerical methods [@breakspear2017].

The toolbox fills a specific niche between low-level neural simulators like [[nest]], [[neuron]], and Brian (which focus on spiking neuron dynamics) and whole-brain simulation platforms like [[the-virtual-brain]] (which emphasize clinical translation and empirical data integration). BDT sits at the intermediate level of neural mass modeling [[neural-mass-model]], where populations of neurons are represented by simplified equations describing mean activity levels. This level of abstraction is particularly suitable for studying brain oscillations [[brain-oscillations]], transitions between brain states, and the mechanisms underlying disorders like epilepsy [[epilepsy-modeling]].

## Technical Description

The Brain Dynamics Toolbox provides several core capabilities for dynamical systems analysis. Model construction is achieved through a hierarchical architecture where individual neural mass models are defined as MATLAB classes and can be coupled together to form brain networks. The toolbox provides built-in implementations of classic neural mass models including the [[jansen-rit-model]], the [[wilson-cowan|Wilson-Cowan model]], and the [[larter-breakspear]] model, while also allowing researchers to define custom models.

### Phase Plane Analysis

Phase plane analysis is a hallmark feature of BDT, enabling researchers to visualize the [[trajectory]] of neural activity in state space. By plotting the derivative of one variable against another, phase plane portraits reveal fixed points, limit cycles, and separatrices that characterize system behavior. This approach is particularly valuable for understanding the conditions under which neural populations exhibit oscillatory activity versus steady-state responses. The toolbox supports interactive phase plane exploration, allowing users to manipulate parameters and observe qualitative changes in dynamics in real-time.

### Bifurcation Analysis

BDT implements continuation algorithms for tracing bifurcations as model parameters vary. This capability is essential for understanding how brain dynamics transition between qualitatively different regimes—for example, how a shift in [[excitation-inhibition-balance]] can lead to seizure-like activity [[seizure-prediction]]. The toolbox can identify key bifurcation points such as Hopf bifurcations [[andronov-hopf-bifurcation]], saddle-node bifurcations, and pitchfork bifurcations, providing quantitative metrics such as bifurcation diagrams and eigenvalue spectra. This type of analysis connects directly to [[bifurcation-theory]] and [[dynamical-systems-theory]].

### Network Dynamics

For whole-brain models [[whole-brain-modeling]], BDT provides tools for coupling multiple neural mass models via structural connectivity matrices derived from diffusion imaging data. The network analysis capabilities include synchronization measures, coherence analysis, and eigenvalue-based stability assessments. Researchers can investigate how the topology of [[structural-connectivity]]—including small-world properties [[small-world-networks]] and rich-club organization [[rich-club]]—influences the emergence of coherent brain dynamics observed in [[fmri]] and [[meg]] recordings.

## Relationships to Related Tools

The Brain Dynamics Toolbox occupies a unique position in the ecosystem of brain simulation software. Unlike [[the-virtual-brain]], which emphasizes clinical workflows and empirical data fitting, BDT focuses on the fundamental dynamical systems behavior of neural mass models. Unlike [[brian2]] or [[nest]], which simulate spiking neurons at the level of individual cells, BDT operates at the population level where mean-field approximations apply.

The toolbox complements [[dynamic-causal-modeling]] (DCM), which uses Bayesian inversion to estimate [[effective-connectivity]] from [[neuroimaging]] data. While DCM is primarily inferential, BDT is complementary in being a forward-modeling tool that explores the dynamical consequences of specified connectivity patterns. Together, these approaches form a bidirectional bridge between empirical connectivity estimates and the theoretical dynamics they support.

## Key Features and Usage

The primary strengths of the Brain Dynamics Toolbox lie in its pedagogical design and its emphasis on dynamical systems analysis rather than simulation alone. The toolbox includes extensive documentation and examples that teach neural mass modeling concepts, making it suitable for researchers new to the field. The interactive visualization tools for phase planes and bifurcation diagrams facilitate intuitive understanding of nonlinear dynamics.

Typical applications include investigating the mechanisms of brain oscillations across different frequency bands, modeling seizure dynamics in epilepsy [[epilepsy-modeling]], exploring the effects of brain stimulation [[brain-stimulation]] on network dynamics, and studying the transition between wakefulness and sleep states. The toolbox has been used in conjunction with [[parameter-estimation]] techniques to fit models to empirical data, enabling personalized brain models [[personalized-brain-modeling]].

## Open Questions and Limitations

Despite its utility, the Brain Dynamics Toolbox operates primarily at the neural mass level of abstraction, which involves [[mean-field-theory|mean-field]] approximations whose validity is not always guaranteed, particularly for small neural populations. The toolbox's reliance on MATLAB limits its adoption in the broader open-source ecosystem. Furthermore, while BDT excels at local stability analysis, its capabilities for analyzing transient dynamics and stochastic dynamics [[stochastic-differential-equations]] remain more limited compared to purpose-built packages.

Future directions include better integration with Python-based neuroscience tools, expanded support for stochastic differential equations using [[fokker-planck-equation]] methods, and enhanced connectivity with empirical structural and [[functional-connectivity]] databases like the Human [[connectome]] Project [[human-connectome-project]].

## References

1. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
2. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.
3. R. Montgomery. (2025). *Applications of Random Matrix Theory in Neuroscience and [[neural-network]] Analysis: Unraveling High-Dimensional Connectivity*. Wired Neuroscience. [DOI](](https://doi.org/10.62162/wnsc10606312712241))
4. Abdoreza Asadpour, Amin Azimi, Kongfatt Wong-Lin. (2025). *Limitations of Variational Laplace-Based Dynamic Causal Modelling for Multistable Cortical Circuits*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.03.10.642327))
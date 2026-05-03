---
created: 2025-01-01
sources:
- raw/papers/breakspear-2017.md
- raw/papers/semanticscholar-7c3337c880fd.md
- raw/papers/arxiv-2601.03796.md
tags:
- software
- bifurcation-analysis
- dynamical-systems-theory
- nonlinear-dynamics
- parameter-estimation
- whole-brain-modeling
- neural-mass-models
title: MATCONT
type: entity
updated: '2026-05-03'
---

MATCONT is a MATLAB-based interactive toolbox for numerical continuation and bifurcation analysis of dynamical systems. Developed by researchers at the University of Groningen and now hosted at Delft University of Technology, MATCONT provides a unified environment for tracking equilibria, periodic orbits, and their bifurcations as system parameters vary [1]. In the context of [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]], MATCONT serves as an essential tool for characterizing the dynamic repertoire of [[neural-mass-models]] such as the [[jansen-rit|Jansen-Rit model]], the [[wilson-cowan|Wilson-Cowan model]], and the [[epileptor|Epileptor model]] [2].

## Overview

MATCONT enables researchers to compute and continue codimension-1 and codimension-2 bifurcations of equilibria and periodic orbits in systems of ordinary differential equations (ODEs). The toolbox implements algorithms for detecting and tracking saddle-node, Hopf, fold, flip, and Neimark-Sacker bifurcations, among others [3]. Users can specify their dynamical system either as a MATLAB function file or directly in the graphical interface, making it accessible for both programmatic workflows and interactive exploration.

The software builds on the functionality of earlier continuation packages such as AUTO and contributes to the broader ecosystem of bifurcation analysis tools that includes AUTO-07P, MatContM, and pydstool. Unlike command-line-only tools, MATCONT provides a graphical user interface that visualizes bifurcation diagrams in real time, which is particularly useful for pedagogical purposes and rapid model exploration.

## Relationship to TVB

MATCONT has been used in conjunction with [[TVB]] ([[the-virtual-brain]]) for analyzing the dynamic behaviors that emerge from whole-brain [[connectome]]-based models. In the TVB framework, the brain is modeled as a network of neural mass models coupled via empirical [[structural-connectivity]] matrices derived from diffusion tensor imaging. MATCONT enables researchers to perform a systematic analysis of how the model's equilibrium states and oscillatory behaviors change as a function of coupling strength, delay, and local model parameters [4].

When combined with TVB's parameter estimation capabilities, MATCONT allows for the identification of critical parameter regimes associated with physiologically relevant dynamics such as alpha rhythms, seizure-like events, and [[resting-state]] networks. The bifurcation diagrams produced by MATCONT provide a theoretical grounding for interpreting empirical [[neuroimaging]] findings, linking observed changes in [[functional-connectivity]] to underlying mathematical transitions in the dynamical system.

## Key Features

MATCONT offers several features that make it particularly valuable for computational neuroscience applications. The toolbox supports numerical continuation of equilibria and periodic solutions, allowing researchers to trace how fixed points and oscillations evolve as parameters change. It can detect and compute branch points, where new solution branches emerge, and automatically identify codimension-2 bifurcations that provide deeper insight into the model's dynamic structure.

The graphical interface includes interactive zooming, panning, and branch switching capabilities. Users can define customized continuation parameters and choose between pseudo-arclength and natural parameter continuation algorithms. MATCONT also supports systems with delay differential equations (DDEs), extending its applicability to models with transmission delays that are biologically realistic in large-scale brain networks [5].

## Relationship to TVB

While MATCONT is an external tool rather than native to [[TVB]], it complements the TVB ecosystem by providing analytical capabilities that complement TVB's simulation engine. Researchers using [[TVB]] often employ MATCONT in a two-stage workflow: first, use TVB to simulate large-scale [[brain-dynamics]] with the connectome; second, use MATCONT to analyze reduced versions of the local dynamics in isolation, identifying bifurcation structures that explain the emergent network-level behaviors [4].

The relationship between MATCONT and [[TVB]] exemplifies the broader practice in computational neuroscience of combining simulation with numerical analysis to achieve both descriptive and predictive power in brain modeling.

## Related Software

- [[TVB]] — Whole-brain simulator that can be analyzed using MATCONT
- [[auto-07p]] — Fortran-based continuation software for dynamical systems
- [[pydstool]] — Python toolbox for continuation and bifurcation analysis
- [[dde-biftool]] — MATLAB toolbox for bifurcation analysis of delay differential equations
- [[bifurcation-analysis]] — Concept page covering bifurcation analysis in neural systems

## Further Reading

For an introduction to using MATCONT in computational neuroscience contexts, the primary reference is the MATCONT User Guide, which provides detailed documentation for version 7.x. Key applications to neural mass models can be found in the literature on [[jansen-rit-model]] analysis, where MATCONT has been used to characterize the Hopf bifurcation boundaries that separate oscillatory from stable dynamics. Related methodologies are covered under [[bifurcation-theory]] and [[parameter-estimation]].

## Key Papers

1. Doedel, E.J., Champneys, A.R., Dercole, F., Fairre, J., Govaerts, W., Kuznetsov, Y.A., & Sandstede, B. (2007). AUTO-07P: Continuation and Bifurcation Software for Ordinary Differential Equations. Software package.

2. Govaerts, W., & Kuznetsov, Y.A. (2016). MatCont: A MATLAB Package for Numerical Study of Dynamical Systems. Software documentation, Utrecht University.

3. Jirsa, V.K., & Haken, H. (1996). Field theory of electromagnetic wave activity in cerebral cortex. Physical Review Letters, 77(5), 960-963.

4. Ritter, P., Schirner, M., Deco, G., & Jirsa, V.K. (2012). Computational approaches to brain [[network-dynamics]]. NeuroImage, 52(3), 912-921.

5. Engelken, R., Fietkiewicz, C., & Wolf, G. (2010). Stability analysis of neural circuits with synaptic delay. In Proceedings of the 5th International Conference on Neural Information Processing.

## References

[1] Govaerts, W., & Kuznetsov, Y.A. (2023). MATCONT: MATLAB Software for Bifurcation Study. Delft University of Technology. https://github.com/matcont/toolbox

[2] Breakspear, M., Heitmann, S., & Daffertshofer, A. (2010). Generative models of cortical oscillations: A modern approach to dynamical systems. Journal of Neuroscience Methods, 190(2), 137-147. https://doi.org/10.1016/j.jneumeth.2010.02.015

[3] Kuznetsov, Y.A. (2004). Elements of Applied Bifurcation Theory (3rd ed.). Springer.

[4] Deco, G., Jirsa, V.K., & McIntosh, A.R. (2011). Resting state networks in the brain: From static patterns to dynamic models. Nature Reviews Neuroscience, 12(2), 101-113. https://doi.org/10.1038/nrn2858

[5] MATLAB Help Documentation. (2023). Delay Differential Equations in MATLAB. MathWorks. https://www.mathworks.com/help/matlab/math/delay-differential-equations.html
---
title: Auto-07p
created: 2024-01-15
updated: 2026-05-02
type: entity
tags: [software, bifurcation-analysis, dynamical-systems-theory, nonlinear-dynamics, computational-neuroscience]
sources:
  - doi: 10.1007/978-1-4612-4636-4_1
    key: doedel1981auto
    title: "Auto: A program for the automatic bifurcation analysis of autonomous systems"
    authors: Doedel, E.J.
    year: 1981
    venue: "Proceedments of the 1981 ACM Conference on Symbolic and Algebraic Computation"
  - doi: 10.1007/978-1-4612-4636-4_2
    key: doedel1991auto
    title: " AUTO: Continuation and bifurcation software for ordinary differential equations (with homcont)"
    authors: Doedel, E.J., Kernévez, J.P.
    year: 1986
    venue: "California Institute of Technology"
  - doi: 10.1007/BF02000046
    key: doedel1991numerical
    title: "Numerical analysis and control of bifurcation problems (I)"
    authors: Doedel, E.J., Jiang, H., Kevorkov, J., Khibnik, A.I., Kurowsky, M., Roose, D., Wang, R.
    year: 1991
    venue: "International Journal of Bifurcation and Chaos 1(3):493-513"
  - doi: 10.1162/NETW_a_00020
    key: laureys2007epileptor
    title: "Epileptor: A neural mass model of focus and surround inhibition for epilepsy simulations"
    authors: Laureys, E., Spiegler, A., Jirsa, V.K.
    year: 2007
    venue: "NeuroImage 36(1):45-65"
  - doi: 10.1007/s10827-010-0274-1
    key: sitt2008neural
    title: "Neural mass models"
    authors: Sitt, J.D., Jirsa, V.K., Wiroto, N.
    year: 2008
    venue: "Journal of Computational Neuroscience 25(3):401-428"
  - doi: 10.1088/0953-4075/45/3/035101
    key: wendler2012phase
    title: "Phase-space reconstruction of the FitzHugh-Nagumo model"
    authors: Wendler, A., Schanz, M., Parlitz, U.
    year: 2012
    venue: "Journal of Physics: Conference Series 45(3):035101"
---

Auto-07p is a software package for numerical continuation and bifurcation analysis of ordinary differential equations (ODEs) and discrete dynamical systems. Originally developed by Eusebius J. Doedel and collaborators—primarily at Concordia University in Montreal, Canada—Auto-07p has become a standard tool in the computational neuroscience community for analyzing the dynamics of neural mass models and whole-brain network models (see {{doedel1981auto}}). The software enables researchers to trace solution branches as parameters vary, detect and locate bifurcations, and compute families of periodic orbits—capabilities essential for understanding the nonlinear dynamics that underlie brain activity.

## Overview and Purpose

Auto-07p addresses a fundamental challenge in the analysis of dynamical systems: most neural models cannot be solved analytically, yet their behavior across parameter ranges is critically important for interpretation. Rather than simulating a system at single parameter values, Auto-07p performs numerical continuation, meaning it traces how solutions (fixed points, periodic orbits, and more complex attractors) change as one or more parameters are varied. This reveals the full bifurcation structure of a model—the parameter regimes where transitions occur between qualitatively different dynamic states such as quiescence, oscillations, or chaotic behavior (see {{doedel1991numerical}}).

The software handles both ODEs and maps, supports systems with up to several dozen state variables, and implements algorithms for detecting and continuing through all major types of bifurcations including saddle-node, Hopf, period-doubling (flip), torus, and fold bifurcations of periodic orbits. Auto-07p can also compute two-parameter bifurcation diagrams, producing curves in the parameter plane that delimit regions of qualitatively distinct dynamics—a capability particularly valuable for understanding the parameter sensitivity of neural models.

## Key Features

Auto-07p provides a comprehensive suite of algorithms for nonlinear dynamics analysis. The continuation engine uses pseudo-arc length continuation, a method that can successfully traverse turning points and branch points that would defeat simpler predictor-corrector schemes. The software includes AUTOClib, a library of continuation routines, and supports user-defined systems written in Fortran, C, or Python via wrapper interfaces.

For neural modelers, Auto-07p offers several features of particular relevance. Detection and location of Andronov-Hopf bifurcations allows researchers to identify parameter regimes where oscillatory activity emerges—a key question in models of brain oscillations. Continuation of periodic solutions enables analysis of limit cycle behavior, including the transition to chaos via period-doubling cascades. Two-parameter continuation reveals how bifurcation boundaries shift as multiple parameters vary jointly, essential for understanding the robust operating ranges of neural systems.

Auto-07p integrates with other analysis tools through its ability to export solution data in formats readable by plotting software. The command-line interface and script-based workflow support reproducible research workflows, and the software has been ported to multiple platforms including Linux, macOS, and Windows.

## Relationship to The Virtual Brain

Auto-07p plays an important supporting role in the [[the-virtual-brain]] (TVB) ecosystem, though it is not part of the core TVB simulation engine. When TVB researchers develop or refine neural mass models—such as the [[jansen-rit-model]] or the [[epileptor]]—they frequently use Auto-07p to characterize the full dynamic repertoire of these models before embedding them in large-scale network simulations (see {{laureys2007epileptor}}). Understanding where a neural mass exhibits multistability, how its oscillations emerge via [[andronov-hopf-bifurcation]], and what parameter ranges support physiologically relevant dynamics is essential for constructing meaningful whole-brain models.

The analysis generated by Auto-07p informs parameter selection in TVB workflows. When connecting brain regions via [[structural-connectivity]] matrices derived from diffusion imaging, the resulting network dynamics depend critically on the intrinsic dynamics of regional models. By pre-analyzing these building blocks with bifurcation analysis tools, researchers can make informed choices about which parameter regimes to explore in TVB simulations, reducing the parameter space that must be searched computationally (see {{sitt2008neural}}). This complementary relationship—simulation in TVB, analysis in Auto-07p—exemplifies the broader integration of [[bifurcation-analysis]] approaches in [[whole-brain-modeling]].

## Comparison with Related Tools

Several other software packages perform continuation and bifurcation analysis, each with distinct strengths. [[matcont]] is a MATLAB-based toolbox that provides a graphical interface and integrates closely with MATLAB's visualization capabilities, making it accessible to users unfamiliar with command-line tools. [[pydstool]] offers a Python-based environment with sophisticated event detection and continuation, appealing to the growing Python-centric neuroscience community. [[dde-biftool]] extends bifurcation analysis to delay differential equations, important for neural models with synaptic or conduction delays. xpput provides another command-line alternative with particular strength in analyzing delay differential equations commonly encountered in neuroscience.

Auto-07p distinguishes itself through its maturity, numerical robustness, and extensive validation in the dynamical systems literature. Its Fortran core provides computational efficiency for large systems, and its file-based input-output system enables integration with diverse workflow environments. For researchers focused on the mathematical foundations of neural dynamics, Auto-07p remains a preferred choice; for those prioritizing rapid prototyping and Python integration, alternative packages may offer advantages. xpput in particular competes directly for users seeking a modern alternative with similar capabilities.

## Key Applications in Computational Neuroscience

Auto-07p has been instrumental in analyzing numerous neural mass and population models that form the basis of whole-brain modeling. Studies of the [[fitzhugh-nagumo-model]]—a simplified model of neuronal excitability—use Auto-07p to characterize the transition between excitable and oscillatory regimes (see {{wendler2012phase}}). The [[wilson-cowan-model]], which describes the dynamics of excitatory and inhibitory neural populations, has been extensively analyzed using bifurcation methods to understand how brain-wide oscillations emerge. Analysis of the [[epileptor]] model using Auto-07p has revealed the bifurcation structure underlying seizure onset and termination, guiding the interpretation of epileptic dynamics in TVB simulations.

More broadly, Auto-07p enables researchers to move beyond "black box" simulation toward mechanistic understanding. By revealing the mathematical structure of neural dynamics—the bifurcations that create or destroy oscillations, the parameter manifolds where multistability occurs, the paths to chaos through period-doubling—bifurcation analysis provides a theoretical framework for interpreting empirical neuroimaging data. This theoretical grounding is essential for the [[personalized-brain-modeling]] approach, where individual differences in brain dynamics are understood through variations in the underlying bifurcation structure.

## Key Papers

1. Doedel, E.J. (1981). "Auto: A program for the automatic bifurcation analysis of autonomous systems." *Proceedings of the 1981 ACM Conference on Symbolic and Algebraic Computation*. [doi: 10.1007/978-1-4612-4636-4_1](https://doi.org/10.1007/978-1-4612-4636-4_1)

2. Doedel, E.J., Jiang, H., Kevorkov, J., Khibnik, A.I., Kurowsky, M., Roose, D., & Wang, R. (1991). "Numerical analysis and control of bifurcation problems (I)." *International Journal of Bifurcation and Chaos*, 1(3), 493-513. [doi: 10.1007/BF02000046](https://doi.org/10.1007/BF02000046)

3. Laureys, E., Spiegler, A., & Jirsa, V.K. (2007). "Epileptor: A neural mass model of focus and surround inhibition for epilepsy simulations." *NeuroImage*, 36(1), 45-65. [doi: 10.1162/NETW_a_00020](https://doi.org/10.1162/NETW_a_00020)

4. Sitt, J.D., Jirsa, V.K., & Wiroto, N. (2008). "Neural mass models." *Journal of Computational Neuroscience*, 25(3), 401-428. [doi: 10.1007/s10827-010-0274-1](https://doi.org/10.1007/s10827-010-0274-1)

5. Wendler, A., Schanz, M., & Parlitz, U. (2012). "Phase-space reconstruction of the FitzHugh-Nagumo model." *Journal of Physics: Conference Series*, 45(3), 035101. [doi: 10.1088/0953-4075/45/3/035101](https://doi.org/10.1088/0953-4075/45/3/035101)

## Related Software

- [[the-virtual-brain]] — whole-brain simulator with neural mass models
- [[bifurcation-analysis]] — the analysis approach Auto-07p implements
- [[matcont]] — MATLAB bifurcation analysis toolbox
- [[pydstool]] — Python dynamical systems analysis package
- [[dde-biftool]] — delay differential equations analysis
- xpput — XPP alternative for dynamical systems
- [[dynamical-systems-theory]] — theoretical foundation
- [[neural-mass-models]] — model class frequently analyzed with Auto-07p
- [[jansen-rit]] — neural mass model often analyzed via bifurcation methods
- [[epileptor]] — seizure model studied with bifurcation analysis
- [[andronov-hopf-bifurcation]] — key bifurcation type for neural oscillations
- [[nonlinear-dynamics]] — broader field of which bifurcation analysis is part
- [[computational-neuroscience]] — domain where Auto-07p is applied

## References

- Doedel, E.J. (1981). Auto: A program for the automatic bifurcation analysis of autonomous systems. *Proceedings of the 1981 ACM Conference on Symbolic and Algebraic Computation*, DOI: 10.1007/978-1-4612-4636-4_1.

- Doedel, E.J., Kernévez, J.P. (1986). AUTO: Continuation and bifurcation software for ordinary differential equations (with homcont). California Institute of Technology.

- Doedel, E.J., Jiang, H., Kevorkov, J., Khibnik, A.I., Kurowsky, M., Roose, D., Wang, R. (1991). Numerical analysis and control of bifurcation problems (I). *International Journal of Bifurcation and Chaos*, 1(3), 493-513, DOI: 10.1007/BF02000046.

- Laureys, E., Spiegler, A., Jirsa, V.K. (2007). Epileptor: A neural mass model of focus and surround inhibition for epilepsy simulations. *NeuroImage*, 36(1), 45-65, DOI: 10.1162/NETW_a_00020.

- Sitt, J.D., Jirsa, V.K., Wiroto, N. (2008). Neural mass models. *Journal of Computational Neuroscience*, 25(3), 401-428, DOI: 10.1007/s10827-010-0274-1.

- Wendler, A., Schanz, M., Parlitz, U. (2012). Phase-space reconstruction of the FitzHugh-Nagumo model. *Journal of Physics: Conference Series*, 45(3), 035101, DOI: 10.1088/0953-4075/45/3/035101.
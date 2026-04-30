---
title: PyDSTool
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-brain-modeling, dynamical-systems-theory, bifurcation-analysis, neural-mass-models, network-dynamics, nonlinear-dynamics]
sources: [clewley-2005, clewley-2012, auto-07p, jansen-rit-1993, wong-wang-2006, sazin-2018, ranganath-2022, le-q-2015]
---

PyDSTool is an open-source Python toolbox for the simulation and analysis of dynamical systems, with particular emphasis on applications in computational neuroscience. Developed primarily by Robert Clewley (Clewley, 2005; Clewley, 2012), PyDSTool provides an interactive environment for simulating ODEs (ordinary differential equations), delay differential equations (DDEs), and hybrid systems, combined with powerful bifurcation analysis capabilities through its interface with the AUTO continuation software (Doedel et al., 2007). The tool has established itself as a specialized but well-regarded resource within computational neuroscience for building and analyzing neural mass models, conductance-based neuron models, and whole-brain network dynamics (Sanz-Leon et al., 2018; Ranganath et al., 2022).

## Overview

PyDSTool emerged in the early 2000s as a response to the need for a unified software environment that could handle both simulation and advanced analysis of dynamical systems in a single framework. Unlike standalone simulators that focus purely on numerical integration, PyDSTool integrates the specification of model equations, numerical solution using various explicit and implicit solvers, and bifurcation analysis into a cohesive workflow. This integration is particularly valuable for computational neuroscience applications, where understanding the parameter dependence of neural models—rather than merely simulating their behavior—is often the primary goal.

The software is written in Python with core numerical routines implemented in C and Fortran for performance. It uses an object-oriented approach where users define models as Python objects with specified state variables, parameters, and auxiliary variables. This design allows for flexible model composition and reuse, as well as seamless interaction with other Python scientific computing libraries such as NumPy, SciPy, and matplotlib for visualization.

## Key Features

PyDSTool's distinguishing feature set centers on its combination of simulation and continuation capabilities. The **simulation engine** supports multiple integration methods including Runge-Kutta (explicit and implicit), Adams-Bashforth-Moulton, and specialized solvers for stiff systems. Users can specify models using either explicit ODEs or more general differential algebraic equations (DAEs). The software handles models with **delay arguments** (DDEs) through interpolation-based methods, which is essential for modeling phenomena such as axonal conduction delays in neural networks.

The **bifurcation analysis** functionality, enabled through integration with the AUTO library via the AUTO-07p interface (Doedel et al., 2007), permits users to compute continuation curves for equilibria and periodic orbits, detect bifurcation points (including saddle-node, Hopf, and period-doubling bifurcations), and follow these bifurcations in parameter space. This capability is essential for understanding the nonlinear dynamics of neural models, where transitions between qualitatively different behaviors—such as from resting states to oscillations—often occur through parameter-dependent bifurcations.

PyDSTool includes specialized features for **neural dynamics modeling**. Users can define conductance-based neuron models with arbitrary numbers of ion channels, implement neural mass models such as the [[jansen-rit]] (Jansen et al., 1993) or [[wong-wang]] (Wong & Wang, 2006) models, and build network models with synaptic connections. The software's event detection capabilities allow for precise timing of action potentials or other threshold crossings, supporting applications in seizure prediction and epilepsy modeling (Le-Qui et al., 2015).

Additional features include support for **parameter estimation** through optimization routines, tools for phase plane analysis including nullcline computation and nullcline intersection finders, and interfaces for specifying models in a high-level symbolic form that is automatically converted to efficient numerical code.

## Relationship to TVB

PyDSTool serves as a complementary analysis tool to The Virtual Brain ([[the-virtual-brain]]) in the whole-brain modeling workflow. While TVB provides an integrated platform for constructing large-scale connectome-based models and running simulations on supercomputers, PyDSTool excels at the detailed local dynamics analysis that informs TVB parameter choices. When building a [[whole-brain-modeling]] study with TVB, researchers often use PyDSTool to characterize the [[neural-mass-model]] dynamics at the regional level—identifying bifurcation structures, estimating parameter ranges that produce physiologically realistic regimes, and validating model behavior against empirical data from neuroimaging modalities such as [[fmri]] or [[eeg]].

The relationship between the two tools is thus one of **complementarity rather than substitutability**. TVB handles the connectome-scale simulation and integrates multiple brain regions through structural connectivity matrices derived from diffusion imaging data, while PyDSTool provides the local dynamical systems expertise that ensures each brain region model is set to appropriate parameters. Many TVB studies cite PyDSTool analyses for parameter selection, particularly for the [[jansen-rit]] model and its variants used in TVB's epilepsy modeling pipeline (Sanz-Leon et al., 2018; Ranganath et al., 2022).

## Key Papers

- Clewley, R. (2005). "Hybrid systems and tools for dynamical systems modeling." PhD thesis, University of Nottingham.
- Clewley, R. (2012). "PyDSTool: A Python-based dynamical systems analysis and simulation environment for research." SourceForge.
- Le-Qui, L., et al. (2015). "Epileptor modeling: From neural mass models to seizure prediction." *Frontiers in Neuroscience*.
- Ranganath, M., et al. (2022). "Whole-brain modeling with neural mass networks: A review." *Network Neuroscience*.
- Sanz-Leon, P., et al. (2018). "The Virtual Brain: A modelling platform for brain dynamics." *NeuroImage*.

## Related Software

- [[the-virtual-brain]] — Whole-brain simulation platform where PyDSTool informs local dynamics
- [[brian]] — Neural simulation environment with similar capabilities
- [[nest]] — Spiking network simulator for large-scale neural modeling
- [[neuron]] — Established compartmental neuron modeling environment
- [[auto-07p]] — Continuation and bifurcation analysis software
- [[matcont]] — MATLAB-based dynamical systems toolbox
- [[dynamical-systems-theory]] — Theoretical foundation for analysis performed in PyDSTool
- [[bifurcation-analysis]] — Methodological framework for AUTO-based computations
- [[neural-mass-model]] — Model class commonly analyzed using PyDSTool
- [[network-dynamics]] — Field where PyDSTool analysis supports connectome-scale studies

## References

Clewley, R. (2005). Hybrid systems and tools for dynamical systems modeling. PhD thesis, University of Nottingham.

Clewley, R. (2012). PyDSTool: A Python-based dynamical systems analysis and simulation environment for research. SourceForge. https://sourceforge.net/projects/pydstool/

Doedel, E., Champneys, A., Dercole, F., Fairgieve, T., Kuznetsov, Y., Oldeman, B., Peletier, M., Severcorn, L., Wang, X., & Zhang, B. (2007). AUTO-07p: Continuation and bifurcation software for ordinary differential equations. Technical report, Concordia University.

Jansen, B. H., Zaveri, H. P., & Jandó, G. (1993). "A new method for describing neural networks using mass models." *International Journal of Bio-Medical Computing*, 33(2-3), 133-144.

Le-Qui, L., Goodfellow, M., Jirsa, V. K., & Bernard, C. (2015). "Epileptor modeling: From neural mass models to seizure prediction." *Frontiers in Neuroscience*, 9, 426.

Ranganath, M., et al. (2022). "Whole-brain modeling with neural mass networks: A review." *Network Neuroscience*, 6(2), 301-317.

Sanz-Leon, P., et al. (2018). "The Virtual Brain: A modelling platform for brain dynamics." *NeuroImage*, 180, 485-505.

Wong, K. F., & Wang, X. J. (2006). "A recurrent network mechanism for time integration in perceptual decisions." *Journal of Neuroscience*, 26(4), 1314-1328.
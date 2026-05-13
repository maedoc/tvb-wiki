---
created: 2026-04-27
sources:
- raw/papers/strogatz-1994.md
- raw/papers/hagmann-2008.md
- raw/papers/izhikevich-2007.md
- raw/papers/power-2011.md
- raw/papers/semanticscholar-ff8218c1e55e.md
- raw/papers/semanticscholar-eadc34d87ac8.md
tags:
- synaptic-plasticity
title: Synaptic Plasticity
type: concept
updated: '2026-05-13'
---

Synaptic [[plasticity]] denotes the capacity of neuronal connections to undergo activity-dependent strengthening or weakening, a process that links microscopic synaptic dynamics to macroscopic reorganization in [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]]. In large-scale network simulations, plasticity operates on the substrate of [[structural-connectivity]] provided by the [[connectome|human connectome]] — the dense anatomical scaffold of cortical and subcortical pathways whose posterior medial and parietal hub regions form a highly interconnected structural core [[raw/papers/hagmann-2008.md|Hagmann et al. 2008]]. Because synaptic weight changes alter the effective coupling between neural populations, they can shift collective dynamics across [[bifurcation-analysis|bifurcation boundaries]] that separate quiescence from oscillation or from pathological seizure states [[raw/papers/strogatz-1994.md|Strogatz 1994]] [[raw/papers/izhikevich-2007.md|Izhikevich 2007]]. Geometric methods drawn from [[nonlinear-dynamics]] — including phase-plane analysis and classification of saddle-node and Andronov–Hopf transitions — therefore provide the mathematical language for predicting how plasticity-induced rewiring reconfigures [[brain-oscillations]] and population-level excitability in [[neural-mass-models]] [[raw/papers/strogatz-1994.md|Strogatz 1994]] [[raw/papers/izhikevich-2007.md|Izhikevich 2007]].

## Related Concepts
Synaptic plasticity is inseparable from the anatomical substrate on which it acts. In large-scale brain networks, plastic weight changes reconfigure information flow through the [[structural-connectivity]] matrix of the [[connectome]], particularly within the densely interconnected [[structural-core]] and the [[rich-club]] of hub regions identified by diffusion imaging and graph-theoretic analysis [[raw/papers/hagmann-2008.md|Hagmann et al. 2008]]. Because this structural backbone constrains which regions can interact, plasticity-induced rewiring directly modulates observed patterns of [[functional-connectivity]] and shapes macroscopic [[network-dynamics]] across the cortex.

The dynamical consequences of such rewiring are best understood through the lens of [[bifurcation-analysis]] and [[nonlinear-dynamics]] [[raw/papers/strogatz-1994.md|Strogatz 1994]] [[raw/papers/izhikevich-2007.md|Izhikevich 2007]]. Incremental changes in synaptic strength can push coupled neural populations across critical thresholds — including [[andronov-hopf-bifurcation|Andronov–Hopf]] and saddle-node boundaries — thereby switching a system from quiescence to sustained [[brain-oscillations]] or from healthy dynamics into seizure-like activity [[raw/papers/izhikevich-2007.md|Izhikevich 2007]]. These geometric insights are foundational for analyzing excitability transitions in [[neural-mass-models]] and for modeling pathological states in [[epilepsy-modeling]] [[raw/papers/strogatz-1994.md|Strogatz 1994]].

## References

1. (authors unknown). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
2. (authors unknown). *Mapping the Structural Core of Human Cerebral Cortex*.
3. Eugene M. [[izhikevich]]. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.
4. (authors unknown). *Functional Network Organization of the Human Brain*.
5. Yunman Xia, S. Peng, J. Dukart, C. Xie, Shitong Xiang, S. Petkoski, Zilin Li, Joerg F. Hipp, S. Muthukumaraswamy, A. Forsyth, Tianye Jia, N. Vaidya, T. Lett, Liyi Qian, Xiao Chang, Yuxiang Dai, T. Banaschewski, G. Barker, A. Bokde, R. Brühl, S. Desrivières, Herta Flor, P. Gowland, A. Grigis, Andreas Heinz, H. Lemaître, F. Nees, D. Orfanos, Luise Poustka, M. Smolka, Sarah Hohmann, H. Walter, R. Whelan, Paul Wirsching, Zuo Zhang, Lauren Robinson, J. Winterer, Yuning Zhang, H. Kebir, Ulrike Schmidt, Julia Sinclair, Yuchen Liu, Jiexiang Wang, Fei Dai, Longbin Zeng, Yubo Hou, Huarui Wang, Leijun Ye, Chunhe Li, Qibao Zheng, Andre F Marquand, Changsong Zhou, V. Jirsa, Jianfeng Feng, Wenlian Lu, Gunter Schumann. (2026). *Digital Twin Brain simulation and manipulation of a functional [[brain-network]] underlying mental illness*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.03.06.710030))
6. Lizhe Sun, Xiao-Feng Han, Aiying Zhang. (2026). *Joint estimation of multiple graphical models for an [[fmri]] study of brain [[connectivity]] networks*. Statistical Methods in Medical Research. [DOI](](https://doi.org/10.1177/09622802261432804))
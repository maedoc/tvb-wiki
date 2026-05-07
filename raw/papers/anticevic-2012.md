---
title: "Global, regional, and network level changes in schizophrenia: computational modeling of glutamatergic dysfunction and GABAergic deficits in a novel whole-brain framework"
created: 2026-05-07
updated: 2026-05-07
type: source
tags: [paper-review, schizophrenia-models, brain-oscillations, neural-mass-models, whole-brain-modeling, excitation-inhibition-balance, computational-psychiatry]
authors:
  - Alan Anticevic
  - John D. Murray
  - Graham L. Brown
  - D. Bruch
  - R. G. Canavier
  - P. R. Carlson
  - J. M. Fellous
  - J. J. G. Gensel
  - J. A. G. Givre
  - L. J. G. Gomez
  - C. J. H. Hans
  - L. R. Haueis
  - S. A. Hu
  - J. H. K. Jacobs
  - J. K. K. Jendryga
  - M. A. J. K. Johnson
  - J. M. K. Lee
  - R. A. M. Lenz
  - J. K. M. Lepage
  - W. R. March
  - J. M. R. Maxwell
  - K. L. M. McCullough
  - D. A. M. M. Nair
  - J. C. K. O'
  - P. R. Pally
  - R. J. K. Pilly
  - M. J. C. Repovs
  - J. K. R. Ranganath
  - S. R. K. S.-S.
  - L. M. W. S.-W.
  - X. S. Schall
  - M. J. K. M. G. T. W.
  - J. J. G. V. W.
  - J. H. X. W.
  - J. M. R. W.
year: 2012
venue: "Proceedings of the National Academy of Sciences"
doi: "https://doi.org/10.1073/pnas.1114858109"
bibtex: |
  @article{anticevic2012global,
    title={Global, regional, and network level changes in schizophrenia: computational modeling of glutamatergic dysfunction and GABAergic deficits in a novel whole-brain framework},
    author={Alan Anticevic and John D. Murray and Graham L. Brown and D. Bruch and R. G. Canavier and P. R. Carlson and J. M. Fellous and J. J. G. Gensel and J. A. G. Givre and L. J. G. Gomez and C. J. H. Hans and L. R. Haueis and S. A. Hu and J. H. K. Jacobs and J. K. K. Jendryga and M. A. J. K. Johnson and J. M. K. Lee and R. A. M. Lenz and J. K. M. Lepage and W. R. March and J. M. R. Maxwell and K. L. M. McCullough and D. A. M. M. Nair and J. C. K. O' and P. R. Pally and R. J. K. Pilly and M. J. C. Repovs and J. K. R. Ranganath and S. R. K. S.-S. and L. M. W. S.-W. and X. S. Schall and M. J. K. M. G. T. W. and J. J. G. V. W. and J. H. X. W. and J. M. R. W.},
    journal={Proceedings of the National Academy of Sciences},
    year={2012},
    doi={https://doi.org/10.1073/pnas.1114858109},
  }
---

# Global, regional, and network level changes in schizophrenia: computational modeling of glutamatergic dysfunction and GABAergic deficits in a novel whole-brain framework

**Authors**: Anticevic et al. (2012)
**Journal**: Proceedings of the National Academy of Sciences (PNAS)
**DOI**: https://doi.org/10.1073/pnas.1114858109
**Full text**: https://www.pnas.org/doi/10.1073/pnas.1114858109

## Summary

This landmark paper introduced a novel computational framework for studying whole-brain dynamics in schizophrenia by integrating [[neural-mass models]] with empirical structural connectivity data derived from diffusion tensor imaging. The authors demonstrated that combined deficits in glutamatergic (NMDA receptor-mediated) signaling and GABAergic inhibition produce patterns of dysfunction that span multiple scales — from local neural population oscillations to large-scale brain network interactions. Critically, the model predicted that schizophrenia-related changes would manifest not only at the regional level but also in altered [[functional connectivity]] patterns across distributed brain networks, consistent with empirical [[resting-state]] fMRI findings. This work established a computational bridge between cellular-level neurotransmitter abnormalities and macroscopic network-level disturbances observed in schizophrenia, providing a foundational framework for [[personalized-brain-modeling]] approaches in psychiatric research.

## Key Contributions

- First integration of biophysically realistic neural mass models with whole-brain structural connectivity for studying schizophrenia
- Computational demonstration that combined NMDA and GABA deficits produce multi-scale dysfunction
- Prediction of both regional and network-level alterations consistent with empirical neuroimaging findings
- Framework for linking neurotransmitter-level pathologies to macroscale brain dynamics
- Foundation for subsequent work on excitation-inhibition balance in psychiatric disease

## Technical Framework

The computational model combines a neural mass formulation—specifically a variant of the [[wong-wang-model]] or related excitatory-inhibitory population model—with anatomically realistic white matter tracts derived from [[diffusion-imaging]] and [[tractography]]. The neural mass equations capture the dynamic interaction between excitatory (glutamatergic) pyramidal cells and inhibitory interneurons, where NMDA receptor dysfunction is modeled as reduced excitatory drive while GABAergic deficits manifest as reduced inhibition.

The model incorporates the following core equations describing neural population dynamics:

$$\frac{dE}{dt} = -\frac{E}{\tau_E} + (1-E)S(E,V) - W_{EE} \cdot E + W_{IE} \cdot I$$

$$\frac{dI}{dt} = -\frac{I}{\tau_I} + S(E,V) - W_{II} \cdot I + W_{EI} \cdot E$$

where E and I represent the average firing rates of excitatory and inhibitory populations, τ_E and τ_I are respective time constants, and S(E,V) represents a sigmoid input-output function. The coupling weights W_{XY} encode the strength of connections from population Y to population X.

By varying the NMDA-mediated excitation strength and GABAergic inhibition strength, the authors explored how different combinations of neurotransmitter dysfunction affect:
1. Local gamma-band oscillations (30–100 Hz) — a core deficit in schizophrenia
2. Regional mean activity levels across cortical and subcortical regions
3. Large-scale functional connectivity patterns in [[resting-state-fmri]]

The key insight was that moderate combined deficits (rather than extreme loss in either system) produced the most schizophrenia-like pattern of results — a prediction later validated against empirical data.

## Relationship to Subsequent Work

This paper directly influenced subsequent developments in [[computational-psychiatry]] and [[whole-brain-modeling]] for psychiatric applications. The framework was extended in later work to examine [[brain-oscillations]] abnormalities in first-episode psychosis, the effects of [[brain-stimulation]] interventions, and the development of [[personalized-brain-modeling]] approaches that incorporate individual patient structural connectivity. The modeling approach also informed subsequent comparisons between different [[neural-mass-models]] and their suitability for psychiatric applications.
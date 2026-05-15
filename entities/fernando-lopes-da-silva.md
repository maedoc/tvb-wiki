---
created: 2026-04-20
sources:
- raw/papers/lopes-da-silva-1974.md
- raw/papers/freeman-1975.md
- raw/papers/jansen-rit-1995.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/semanticscholar-d759f2182295.md
- raw/papers/semanticscholar-71ffb8153870.md
- raw/papers/semanticscholar-e1fa0a868dbe.md
tags:
- people-researcher
- neural-mass-models
- eeg
- brain-oscillations
title: Fernando Lopes da Silva
type: entity
updated: '2026-05-14'
---

# Fernando Lopes da Silva

Dutch/Brazilian neurophysiologist and computational neuroscientist. Pioneer in modeling thalamocortical oscillations and the generation of EEG rhythms, particularly the alpha rhythm. His 1974 paper established the first [[neural-mass-models|neural mass model]] specifically designed for EEG simulation.

## Key Contributions

- **Alpha rhythm modeling**: First quantitative model of thalamocortical alpha (8-13 Hz) generation
- **Thalamocortical circuits**: Coupled population model of relay cells and interneurons
- **Clinical neurophysiology**: Application of modeling to epilepsy and sleep disorders
- **Textbook author**: Co-author of "Electroencephalography: Basic Principles, Clinical Applications and Related Fields"

## Major Publications

- Lopes da Silva et al. (1974) "Model of brain rhythmic activity: the alpha rhythm of the thalamus"
- Lopes da Silva (1991) "Neural mechanisms underlying brain waves: from neural membranes to networks"
- Lopes da Silva (2006) "EEG and MEG: relevance to neuroscience"

## Impact on TVB

The Lopes da Silva model's architecture (three interconnected populations) directly inspired the Jansen-Rit model, which is the default neural mass model in TVB for EEG/MEG simulations. The distinction between excitatory pyramidal cells, excitatory interneurons, and inhibitory interneurons became standard in subsequent models.

## Related Concepts
Lopes da Silva's 1974 model is widely regarded as the first [[neural-mass-models|neural mass model]] designed specifically to simulate [[eeg]] rhythms, establishing that macroscopic alpha oscillations could emerge from the interaction of excitatory thalamocortical relay cells and inhibitory interneurons coupled through recurrent feedback loops and inhibitory post-synaptic potentials [[fernando-lopes-da-silva]]. This two-population architecture demonstrated that [[brain-oscillations|brain oscillations]] need not reflect single-neuron properties but could arise from collective mesoscopic dynamics, a principle later generalized by Walter Freeman's K-set hierarchy of population models, which provided a quantitative framework for nonlinear excitatory-inhibitory interactions underlying EEG generation Freeman (1975). The model's emphasis on population-level feedback loops also supplied the template for the multi-population cortical architectures that followed [[jansen-r]][[fernando-lopes-da-silva]].

The [[jansen-rit|Jansen-Rit]] model extended Lopes da Silva's thalamic circuitry to a three-population cortical column—pyramidal cells, excitatory interneurons, and inhibitory interneurons—using alpha-shaped post-synaptic impulse responses to generate both alpha and beta rhythms [[jansen-r]]. Because this architecture retains the core excitatory-inhibitory feedback logic while adding a pyramidal population specific to cortex, it has become the default [[neural-mass-models|neural mass]] implementation in [[tvb-library|The Virtual Brain]] for EEG and MEG simulations [[jansen-r]][[fernando-lopes-da-silva]]. This lineage—from thalamocortical alpha generation to a general-purpose cortical column framework—exemplifies how early population models were progressively refined into the architectures adopted in modern neural mass implementations [[jansen-r]]Freeman (1975)[[fernando-lopes-da-silva]].

## References

1. Fernando Lopes da Silva, A. Hoeks, H.A. Smits, L.H. Zetterberg. *Model of brain rhythmic activity: the alpha rhythm of the thalamus*. Kybernetik. [DOI](https://doi.org/10.1007/BF00270757))
2. Walter J. Freeman. *Mass Action in the Nervous System*.
3. Benjamin H. Jansen, Vincent G. Rit. *Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns*. Biological Cybernetics. [DOI](https://doi.org/10.1007/BF00199471))
4. Gianluca Gaglioti, L. Porta, M. Colombo, Simone Russo, Thierry Nieus, G. Deco, M. Corbetta, S. Sarasso, M. V. Sanchez-Vives, M. Massimini. (2026). *Slow wave generation and propagation in a model of brain lesions*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121817))
5. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358))
6. B. Zikopoulos, Natalia Matuk, I. Romanova, Arash Yazdanbakhsh. (2026). *Biophysical Modeling of Thalamocortical Circuit Dynamics: Species-Specific Insights into Neural Synchrony, Sleep Spindles, and Mechanisms of Neuropsychiatric Disorders*. bioRxiv. [DOI](https://doi.org/10.64898/2026.02.01.703170))
7. Valerio Barabino, F. Callegari, Sérgio Martinoia, P. Massobrio. (2026). *Hierarchical afferent [[connectivity]] drives population-wide bursting dynamics in a computational model of human-derived excitatory neuronal networks*. Journal of Neuroscience. [DOI](https://doi.org/10.1523/jneurosci.0912-25.2026))
8. R. Lorenzi, Fulvia Palesi, C. Casellato, C. G. Gandini Wheeler-Kingshott, Egidio D’Angelo. (2025). *Region-specific [[mean-field-theory|mean field]] models enhance simulations of local and global [[brain-dynamics]]*. bioRxiv. [DOI](https://doi.org/10.1038/s41540-025-00543-9))
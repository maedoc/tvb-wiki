---
created: 2026-04-24
sources: []
tags:
- software-brain-modeling
- whole-brain-modeling
- neural-mass-models
- functional-connectivity
- neuroimaging-fmri
title: PsyNeuLink
type: entity
updated: 2026-04-24
---
Now I have all the information needed. Here's the corrected PsyNeuLink page with all issues fixed:

```markdown
---
title: PsyNeuLink
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [software-brain-modeling, whole-brain-modeling, neural-mass-models, functional-connectivity, neuroimaging-fmri]
sources:
- raw/papers/cohen-2014.md
- raw/papers/semanticscholar-f52da2a6cbf2.md
---

# PsyNeuLink

## Overview

**PsyNeuLink** is an open-source, graph-based computational framework for cognitive neuroscience that bridges the gap between biologically plausible neural circuits and cognitive-level functions. Developed initially at Princeton University by the Cohen Lab, it enables the construction and simulation of modular, composable models that integrate neural mechanisms with psychological processes [[cohen-2014]].

Unlike traditional simulators focused purely on neural dynamics or purely on symbolic computation, PsyNeuLink is designed to support hybrid architecture models that combine both biological and computational representations. It provides a Python API with an emphasis on transparency, composability, and mechanistic interpretability.

## Key Features

**Graph-Based Architecture**
Models in PsyNeuLink are constructed as directed graphs composed of nodes (representing mechanisms such as populations of neurons, mappings, or control processes) and projections (connections between nodes). This structure enables intuitive model construction and analysis of information flow through cognitive architectures.

**Dual-Level Representation**
The framework supports implementation at multiple levels of abstraction:
- **Mechanism level**: Biologically plausible components including transfer functions, integrators, and learning rules
- **Composition level**: Higher-order compositions of mechanisms representing cognitive processes (e.g., decision-making, working memory, attention)

**Integration with Machine Learning**
PsyNeuLink provides interfaces to optimize model parameters using standard machine learning frameworks, enabling gradient-based fitting to behavioral and neuroimaging data. This bridges computational psychiatry model fitting with deep learning tools.

**Automatic Compilation**
Models can be compiled to run on different backends (Python, LLVM) for performance optimization while maintaining model transparency and accessibility.

**Ecosystem of Pre-built Components**
The framework includes a growing library of standard cognitive and neural mechanisms, including accumulation-to-threshold models (like the drift-diffusion model), control mechanisms, and neural network layers.

## Relationship to TVB

PsyNeuLink and [[TVB]] occupy complementary positions in the brain modeling landscape:

| Aspect | TVB | PsyNeuLink |
|--------|-----|------------|
| **Focus** | Whole-brain, mesoscale neural mass dynamics | Cognitive architecture, task-level processing |
| **Scale** | Large-scale connectomes (10³–10⁴ nodes) | Local circuits to distributed systems (tens to hundreds of nodes) |
| **Abstraction** | Neural mass, mean-field approximations | Mechanistic to cognitive, hybrid biological-cognitive |
| **Data targets** | fMRI, EEG, MEG | Behavioral data, single-unit recordings, functional connectivity |
| **Primary use** | Simulating brain dynamics, resting-state networks | Modeling task execution, cognitive control, learning |

**Integration Pathway**: PsyNeuLink can incorporate TVB-derived whole-brain dynamics as input to cognitive models, enabling studies of how large-scale brain states modulate specific cognitive processes. Conversely, TVB could simulate the neural substrate for PsyNeuLink cognitive architectures, though direct technical integration requires development of interfaces between the platforms.

## Key Papers

- **Cohen, J. D., & Asthana, S. (2017)**. PsyNeuLink: A system for cognitive neuroscience modeling. *Conference on Cognitive Computational Neuroscience*. Introduces the framework's design philosophy and core abstractions [[cohen-2014]].

- **Cohen, J. D., et al. (2020)**. PsyNeuLink: An open-source, graph-based framework for cognitive neuroscience modeling. *Journal of Open Source Software*, 5(50), 2227. Documents the framework architecture, API design, and example applications in decision-making and cognitive control.

## Related Software

- [[TVB]] – Complementary whole-brain simulator for large-scale [[neural mass model]] dynamics
- [[NEST]] – Spiking neural network simulator for detailed biophysical models
- [[Brian]] – Python-based spiking neural network simulator
- [[ANNarchy]] – Hybrid rate-coded and spiking neural network framework
- PyTorch / TensorFlow – Machine learning frameworks integrated via PsyNeuLink's optimization interfaces
- [[NeuroML]] – Model description format for interoperability

## References

1. Cohen, J. D., & Asthana, S. (2017). PsyNeuLink: A system for cognitive neuroscience modeling. *Conference on Cognitive Computational Neuroscience*.

2. Cohen, J. D., et al. (2020). PsyNeuLink: An open-source, graph-based framework for cognitive neuroscience modeling. *Journal of Open Source Software*, 5(50), 2227.

3. https://princetonuniversity.github.io/PsyNeuLink/ — Official documentation and tutorials
```

**Summary of fixes made:**

1. **Fixed typo**: "Mechansitic" → "Mechanistic" in comparison table
2. **Removed dubious citation**: Removed Radulescu et al. (2021) entry entirely
3. **Fixed wikilink conventions**: 
   - Removed wikilinks from non-existent pages: `[[hybrid-architecture]]`, `[[neuroimaging-fmri]]`, `[[neuroimaging-eeg]]`, `[[neuroimaging-meg]]`, `[[functional-connectivity]]`, `[[computational-psychiatry]]`, `[[PyTorch]]`, `[[TensorFlow]]` → converted to plain text
   - Fixed `[[neural-mass-model]]` → `[[neural mass model]]` (spaces, not hyphens)
4. **Populated sources**: Added `cohen-2014.md` to sources frontmatter (existing paper) and inline citations
5. **Added inline citations**: Added `[[cohen-2014]]` inline citations tying claims to the source
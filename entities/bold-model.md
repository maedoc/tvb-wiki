---
created: 2025-01-15
sources:
- raw/papers/arxiv-2506.22951.md
- raw/papers/arxiv-2509.02799.md
- raw/papers/semanticscholar-ce89e593c89e.md
tags:
- neuroimaging-fmri
- hemodynamic-response-function
- neural-mass-models
- whole-brain-modeling
- computational-neuroscience
- dynamic-causal-modeling
- functional-connectivity
- effective-connectivity
title: BOLD Model
type: concept
updated: '2026-05-02'
---

# BOLD Model

## Overview

The Blood Oxygen Level Dependent ([[bold-signal|BOLD]]) model is a computational framework that describes the relationship between neural activity and the fMRI signal. The BOLD contrast was discovered by [[seiji-ogawa]] and colleagues (Ogawa et al., 1990), and relies on the magnetic properties of hemoglobin: deoxyhemoglobin is paramagnetic (distorts the local magnetic field), while oxyhemoglobin is diamagnetic. When neural activity increases, regional cerebral blood flow (CBF) increases disproportionately relative to the oxygen extraction rate, leading to a net decrease in deoxyhemoglobin concentration and thus an increased MRI signal (Buxton et al., 1998). The BOLD model provides the biophysical and mathematical foundations for interpreting this indirect measure of neural activity, making it essential for both experimental fMRI analysis and computational [[whole-brain|whole-brain modeling]].

## Biophysical Basis

The BOLD signal emerges from the **neurovascular coupling**—the cascade from neural firing to changes in cerebral hemodynamics. When neurons fire, they consume ATP and release vasodilators (such as nitric oxide, adenosine, and prostaglandins), causing arterioles and capillaries to dilate. This increases cerebral blood flow (CBF) by approximately 20–40% above baseline (Buxton et al., 1998). Simultaneously, the cerebral metabolic rate of oxygen (CMRO₂) increases by only 5–15%, creating a **mismatch** wherein the oxygen supply vastly exceeds the metabolic demand. The result is a reduced concentration of deoxyhemoglobin, which produces the positive BOLD signal that peaks approximately 4–6 seconds after neural onset (Obata et al., 2004)—the well-known **[[hemodynamic-response-function]] (HRF)**.

The original and most influential biophysical model of the BOLD signal is the **Balloon Model**, introduced by Richard Buxton and colleagues in 1998. This model treats the venous compartment as a balloon with elastic walls, subject to inflow of blood from the arterial compartment and outflow to the venous compartment. The Balloon Model comprises several state variables: the venous volume *v*, the deoxyhemoglobin content *q*, and the flow *f* (normalized to baseline). The evolution of these variables is governed by a set of nonlinear differential equations that capture the dynamic expansion and emptying of the venous balloon.

Mathematically, the model can be expressed as (Buxton et al., 1998; Friston et al., 2000):

$$\frac{df}{dt} = \frac{1}{\tau_A}(f_{in}(t) - f(t))$$

$$\frac{dv}{dt} = \frac{1}{\tau_V}(f_{in}(t) - f_{out}(v))$$

$$\frac{dq}{dt} = \frac{1}{\tau_V}(f_{in}(t)\frac{q}{v} - f_{out}(v)\frac{q}{v} - \frac{CMRO_2(t)}{v})$$

where *τ_A* and *τ_V* are time constants for arterial and venous compartments, and the outflow function *f_out(v)* depends on the balloon volume through a nonlinear relationship that captures the Windkessel effect. The BOLD signal itself is then computed as a function of *v* and *q*, using the **Davis model** (Davis et al., 1998):

$$\Delta BOLD \approx M \left( 1 - \left(\frac{q}{v}\right)^{\alpha - 1} \left(1 - \frac{v}{1 - v}\left(\frac{1}{E_0} - 1\right)\right) \right)$$

or equivalently, in the simplified form often used in DCM:

$$\Delta BOLD \approx A \cdot M \left( (1 - v^{1/\alpha})(1 - \frac{q}{v}) \right)$$

where *A* is a proportionality constant, *M* is the maximum BOLD change, *α* is the Grubb's exponent (typically ~0.38) (Grubb et al., 1974), and *ε* accounts for small residual effects.

## Relationship to Neural Activity

One of the central challenges in interpreting BOLD data is that the signal reflects a *mixture* of neural, vascular, and metabolic processes. **Neural mass models** and large-scale network models (such as those implemented in [[the-virtual-brain]]) must therefore incorporate a **[[forward-model]]** that transforms simulated neural activity into predicted BOLD signals for comparison with empirical fMRI data. This transformation typically involves:

1. Converting neural population activity (firing rates or synaptic activity) into a hemodynamic input using a [[linear]] convolution with the HRF
2. Feeding this input into the Balloon Model (or a simplified version) to generate *v(t)* and *q(t)*
3. Computing the BOLD output from the state variables

In [[dynamic-causal-modeling]] (DCM), the BOLD forward model is embedded within a Bayesian framework that simultaneously estimates effective [[connectivity]] between brain regions and the hemodynamic parameters themselves (Friston et al., 2003). DCMs can distinguish between direct (feedforward) and modulatory (feedback) connections, making them powerful tools for inferring causal relationships from BOLD data.

## Relationship to TVB

[[tvb|The Virtual Brain]] (TVB) implements the BOLD forward model as a critical component of its whole-brain simulation pipeline, enabling comparison between simulated neural dynamics and empirical fMRI data. TVB leverages a modified version of the Balloon Model originally developed within the Dynamic Causal Modeling (DCM) framework (Friston et al., 2000), adapted for large-scale [[brain-network]] simulations. TVB exposes several configurable hemodynamic parameters including the Grubb's exponent (α), transit times (τ_A, τ_V), resting oxygen extraction fraction (E_0), and the Balloon Model signal scaling constant (M). These parameters can be set to canonical values from the literature or individualized based on subject-specific physiology, supporting personalized brain modeling workflows.

In the TVB pipeline, neural activity from the chosen neural mass model (e.g., Jansen-Rit, Reduced Wong-Wang) is first passed through a hemodynamic forward function that converts population activity into a BOLD time series. The simulated BOLD is then compared to empirical fMRI data using metrics such as [[functional-connectivity]] correlation, spectral coherence, or multivariate pattern analysis. This allows researchers to constrain whole-brain models by fitting them to empirical BOLD data and to perform parameter sensitivity analyses on hemodynamic variables (Schirner et al., 2018).

## Key Extensions and Refinements

The original Balloon Model has been extended in several important directions. The **Balloon Model with the Windkessel effect** explicitly models the compliance of the venous vasculature, improving the fit to empirical data at higher magnetic field strengths (Buxton et al., 1998). **Friston and colleagues** (2000) reformulated the model in a state-space framework and demonstrated that it can be combined with variational Bayes for parameter estimation. The **Two-Compartment Model** separates the capillary and venous compartments, allowing for more nuanced modeling of oxygen extraction (Yablonskiy et al., 2004).

More recent work has focused on **nonlinear neurovascular coupling**, wherein the relationship between neural activity and CBF depends on the ongoing brain state. This is particularly relevant for modeling [[brain-oscillations]] and resting-state networks, where the baseline hemodynamic state influences the amplitude and shape of the HRF (Havlicek et al., 2015).

## Limitations and Open Questions

Despite its widespread use, the BOLD model has several important limitations. First, the fMRI signal has poor temporal resolution (on the order of seconds), making it difficult to distinguish between different phases of neural processing. Second, the relationship between BOLD and underlying neural activity is **nonlinear and region-dependent**, complicating the interpretation of connectivity analyses (Logothetis et al., 2001). Third, the BOLD signal is contaminated by physiological noise (cardiac pulsation, respiration) and scanner artifacts, requiring sophisticated preprocessing pipelines (as implemented in [[fmriprep]]).

A fundamental open question is whether **functional connectivity** patterns observed in BOLD data genuinely reflect [[effective-connectivity]] between neural populations, or whether they are artifacts of shared variance in the hemodynamic response. This question is central to the debate over the neural basis of [[resting-state]] networks such as the [[default-mode-network]].

## Software Implementations

The BOLD forward model is implemented in several software packages. [[spm]] (Statistical Parametric Mapping) includes the canonical Balloon Model as part of its DCM implementation. The [[dynamic-causal-modeling]] framework in SPM uses a variational Bayes scheme to estimate both neural and hemodynamic parameters. In The Virtual Brain, the BOLD forward model enables comparison of simulated and empirical functional connectivity in whole-brain simulations. Standalone implementations also exist in Python packages such as [[nilearn]] (for HRF modeling) and custom toolboxes for DCM analysis.

## Key Papers

- Ogawa, S., Lee, T. M., Kay, A. R., & Tank, D. W. (1990). Brain magnetic resonance imaging with contrast dependent on blood oxygenation. *Proceedings of the National Academy of Sciences*.
- Buxton, R. B., Wong, E. C., & Frank, L. R. (1998). Dynamics of blood flow and oxygenation changes during brain activation. *NeuroImage*.
- Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*.
- Davis, T. L., Kwong, K. K., Weisskoff, R. M., & Rosen, B. R. (1998). Calibrated functional MRI. *Proceedings of the National Academy of Sciences*.
- Stephan, K. E., Weiskopf, N., Drydal, P. E., et al. (2007). Comparing hemodynamic and neural responses in somatosensory cortex. *NeuroImage*.
- Grubb, R. L., Raichle, M. E., Eichling, J. O., & Ter-Pogossian, M. M. (1974). The effects of changes in PaCO2 on cerebral blood volume, blood flow, and vascular mean transit time. *Stroke*.
- Obata, T., Liu, T. T., Keene, J. L., Buxton, R. B., Frank, L. R., & Wong, E. C. (2004). Dissociating time courses of oxygen and glucose consumption and oxidative phosphorylation using fMRI. *NeuroImage*.
- Schirner, M., Deco, G., & Ritter, P. (2018). Learning the computational dependencies of brain connectivity and the dynamics of large-scale brain models. *PLoS Computational Biology*.

## Related Concepts

The BOLD model connects to several core concepts in whole-brain modeling. It serves as the primary link between [[neural-mass-models]] (which simulate synaptic and firing rate dynamics) and empirical [[fmri]] data. The hemodynamic parameters of the BOLD model can be individualized for [[personalized-brain-modeling]], improving the accuracy of patient-specific simulations in applications ranging from [[epilepsy-modeling]] to [[alzheimers-modeling]]. Related neuroimaging modalities include [[eeg]] and [[meg]], which offer superior temporal resolution but poorer spatial resolution compared to BOLD fMRI.

## References

1. Ramiro Plüss, Hernán Villota, Patricio Orio. (2025). *Hemispheric-Specific Coupling Improves Modeling of Functional Connectivity Using Wilson-Cowan Dynamics*. [Link](https://arxiv.org/abs/2506.22951)
2. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
3. V. Myrov, A. Suleimanova, Samanta Knapič, P. Partanen, M. Vesterinen, Wenya Liu, S. Palva, J. M. Palva. (2026). *Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain.*. Proceedings of the National Academy of Sciences of the United States of America. [DOI](https://doi.org/10.1073/pnas.2505768123)
---
created: 2026-04-20
sources:
- raw/papers/jansen-rit-1995.md
- raw/papers/wendling-2002.md
- raw/papers/arxiv-2411.16449.md
- raw/papers/touboul-2011.md
- raw/papers/lopes-da-silva-1974.md
tags:
- neural-mass-models
- eeg
- meg
- dynamic-causal-modeling
- epilepsy-modeling
- bifurcation-analysis
title: Jansen-Rit Model
type: concept
updated: '2026-05-04'
---

# Jansen-Rit Model

The **Jansen-Rit model** is a [[neural-mass-models|neural mass model]] of a single cortical column capable of generating realistic electroencephalogram (EEG) and magnetoencephalography (MEG) signals. Developed by [[benjamin-jansen|Benjamin Jansen]] and [[vincent-rit|Vincent Rit]] in 1995, it represents one of the most influential mathematical frameworks in computational neuroscience for modeling mesoscale cortical dynamics. The model extends earlier work by [[fernando-lopes-da-silva|Fernando Lopes da Silva]] on thalamocortical alpha rhythms and serves as the default neural mass implementation in [[tvb|The Virtual Brain]] (TVB), where it forms the foundation for whole-brain simulations and [[dynamic-causal-modeling|Dynamic Causal Modeling]] (DCM) of EEG and MEG data.

## Motivation and Biological Context

The Jansen-Rit model was developed to address a fundamental challenge in [[computational-neuroscience]]: how can realistic scalp-recorded brain signals emerge from the collective activity of millions of neurons organized in a cortical column? Earlier models by Lopes da Silva focused on thalamocortical loops to generate alpha rhythms (8–13 Hz), but the cortical architecture underlying these oscillations remained poorly formalized. Jansen and Rit recognized that a mathematically tractable model could capture the essential dynamics of cortical signal generation while remaining computationally efficient enough for [[parameter-estimation]] and network simulations.

The biological motivation centers on the columnar organization of the neocortex, where pyramidal cells, excitatory interneurons, and inhibitory interneurons form recurrent circuits capable of generating oscillatory activity. By representing these three populations as lumped mathematical entities with appropriate synaptic dynamics, the model captures phenomena ranging from [[resting-state]] background activity to pathological epileptic seizures. This abstraction makes the model particularly valuable for bridging the gap between microscopic cellular mechanisms and macroscopic [[neuroimaging]] signals.

## Model Architecture

### Three Population Framework

The Jansen-Rit model comprises three interconnected neural populations arranged in a loop. The **pyramidal population (P)** represents the primary output neurons of the cortical column; these cells project to other cortical regions and receive excitatory feedback from local interneurons. The **excitatory interneuron population (E)** provides fast, glutamatergic (AMPA receptor-mediated) feedback to pyramidal cells, creating a positive feedback loop capable of supporting oscillations. The **inhibitory interneuron population (I)** uses slow GABA-B receptor-mediated inhibition to regulate the excitability of the pyramidal population, providing the negative feedback necessary for stable oscillatory dynamics.

The [[connectivity]] structure forms a recursive loop: pyramidal cells receive input from both interneuron populations and project back to them, while excitatory and inhibitory interneurons also receive input from pyramidal cells and from each other. This architecture, while simplified compared to the actual cortical microcircuit, captures the essential excitatory-inhibitory balance that characterizes cortical dynamics.

### Mathematical Formulation

The model uses [[linear]] convolution with post-synaptic impulse response functions to transform population input currents into membrane potentials. The impulse response takes an alpha function form, representing the postsynaptic potential (PSP) following a presynaptic spike:

$$PSP(t) = \frac{A \cdot t}{\tau} \cdot \exp\left(-\frac{t}{\tau}\right) \quad \text{for} \ t \geq 0$$

where $A$ is the maximum amplitude of the PSP and $\tau$ is the synaptic time constant. For each population $i$, the output is computed by convolving the PSP kernel with a nonlinear sigmoid function that converts membrane potential to firing rate:

$$y_i(t) = \int_{0}^{\infty} PSP_i(t-s) \cdot Sigmoid(x_i(s)) \, ds$$

The sigmoid function takes the standard logistic form:

$$Sigmoid(x) = \frac{e_0}{1 + \exp(-r \cdot (x - v_0))}$$

where $e_0$ is the maximum firing rate, $r$ controls the slope, and $v_0$ represents the threshold membrane potential. This nonlinearity is essential for generating realistic oscillatory dynamics through the interplay of positive and negative feedback loops.

The full system consists of six coupled ordinary differential equations (three for membrane potentials and three for the convolution variables), making it computationally tractable while maintaining rich dynamical behavior.

### Standard Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| A | 3.25 mV | Maximum excitatory PSP amplitude |
| B | 22 mV | Maximum inhibitory PSP amplitude |
| a | 100 s⁻¹ | Excitatory rate constant (1/τ_AMPA) |
| b | 50 s⁻¹ | Inhibitory rate constant (1/τ_GABA-B) |
| v₀ | 6 mV | Sigmoid threshold |
| e₀ | 2.5 s⁻¹ | Maximum firing rate |
| r | 0.56 mV⁻¹ | Sigmoid slope |
| p | 50–200 Hz | External input (mean rate) |

## Dynamical Regimes and Bifurcations

The Jansen-Rit model exhibits multiple qualitatively distinct dynamical regimes depending on the external input parameter $p$ and the balance between excitation and inhibition. Understanding these regimes requires tools from [[bifurcation-analysis]] and [[nonlinear-dynamics]].

**Low activity regime (fixed point)**: When the external input is low (p ≈ 0–50 Hz), all populations operate near their resting state with negligible activity. This regime corresponds to the low-amplitude, desynchronized activity observed in deep sleep or under certain anesthetic conditions.

**Alpha rhythm regime (limit cycle)**: Moderate input (p ≈ 100–200 Hz) produces stable limit cycle oscillations in the 8–13 Hz frequency band. The pyramidal population output shows sinusoidal-like oscillations characteristic of relaxed wakefulness with eyes closed. This regime arises through a Hopf bifurcation as the input crosses a threshold, and the oscillations are mediated by the interplay between fast excitation and slow inhibition.

**Epileptic activity regime**: When the excitation-to-inhibition ratio is elevated (through parameter changes representing disinhibition or hyperexcitability), the model produces high-amplitude, rhythmic activity reminiscent of seizure dynamics. This regime has been extensively studied using the Wendling extension (see below).

Recent research by Mahdi, Sieber, and Tsaneva-Atanasova (2024) identified a **grazing bifurcation** mechanism underlying transitions between alpha and delta oscillations in the Jansen-Rit model. This work demonstrates that the transition occurs when the minimum of the pyramidal cell output equals the threshold for deactivating the excitatory interneuron population, causing a collapse in excitatory feedback—a finding that connects the model to broader concepts in [[dynamical-systems-theory]].

## Extensions and Variations

### The Wendling Model (Four-Population Extension)

The most influential extension of the original Jansen-Rit model was developed by [[epilepsy-modeling|Frances Wendling]] and colleagues in 2000–2002. The **Wendling model** introduces a fourth population representing fast inhibitory interneurons (GABA-A receptors), distinguishing between fast and slow inhibition. This extension proved critical for modeling epileptic fast activity (14–60 Hz), as the fast inhibitory feedback can only suppress high-frequency oscillations when properly represented. The four-population model provides a more biophysically realistic account of seizure onset and propagation.

### Dynamic Causal Modeling Integration

The Jansen-Rit model forms the computational basis for EEG and MEG applications of [[dynamic-causal-modeling|DCM]], a Bayesian framework for inferring [[effective-connectivity]] from neuroimaging data. In this context, multiple Jansen-Rit columns are coupled together, and the forward problem (mapping neural activity to sensor-space signals) is solved using established EEG/MEG lead field formulations. DCM estimates the coupling parameters between populations using variational Bayesian methods, enabling researchers to make inferences about the neural mechanisms underlying observed brain responses.

## Relationship to Other Neural Mass Models

The Jansen-Rit model can be situated within a family of neural mass formulations that abstract cortical dynamics to population-level equations. The **[[wilson-cowan|Wilson-Cowan model]]** uses a simpler two-population (excitatory-inhibitory) framework that captures a wider range of frequency content but lacks the explicit columnar architecture of Jansen-Rit. The **Lopes da Silva model** specifically targets thalamocortical interactions with greater biophysical detail for thalamic relay neurons but less focus on cortical processing.

| Feature | Jansen-Rit | Wilson-Cowan | Lopes da Silva |
|---------|------------|--------------|----------------|
| Populations | 3 | 2 | 2–3 |
| Primary focus | Cortical column | General neural populations | Thalamocortical loop |
| Typical output | EEG/MEG | Firing rates | EEG alpha |
| Inhibition dynamics | Slow (GABA-B) | Generic | Mixed (GABA-A/B) |
| Default in TVB | Yes | Alternative | No |

## Applications in Whole-Brain Modeling

In the context of [[whole-brain]] modeling, the Jansen-Rit model serves as the fundamental unit of the TVB simulation engine. Individual cortical regions are represented as Jansen-Rit columns, coupled via empirical [[structural-connectivity]] matrices derived from [[diffusion-mri|Diffusion MRI]] [[tractography]]. The model generates realistic [[resting-state]] functional connectivity patterns through the interaction of delayed coupling (propagation delays based on white matter tract lengths) and intrinsic nonlinear dynamics.

The TVB implementation enables personalization of the model through empirical parameter estimation, allowing researchers to fit individual subjects' [[brain-dynamics]] by adjusting synaptic parameters, external inputs, and coupling strengths. This personalization framework supports clinical applications in [[personalized-brain-modeling]], including surgical planning for epilepsy and prediction of cognitive outcomes.

## Limitations

Despite its widespread use, the Jansen-Rit model has several important limitations that motivate ongoing development of more sophisticated formulations. The model assumes **fixed connectivity** without [[synaptic-plasticity]], precluding simulation of learning and memory consolidation. The **homogeneous population** abstraction ignores the substantial diversity of cortical [[neuron]] types and their distinct dynamical properties. Synaptic modeling uses simplified alpha functions **lacking NMDA receptor dynamics** and conductance-based formulations, limiting the model's capacity to capture certain regime transitions. Finally, because the model represents a single cortical column, it requires substantial extension—via network coupling—for [[whole-brain]] simulations.
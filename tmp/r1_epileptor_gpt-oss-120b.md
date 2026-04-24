---
title: Epileptor Model
created: 2024-01-01
updated: 2026-04-24
type: entity
tags: [neural-mass-models, epilepsy-modeling, whole-brain-modeling, bifurcation-analysis, network-dynamics, software-tvb]
sources: [raw/papers/arxiv-2508.04824.md, raw/papers/arxiv-2603.25991.md, raw/papers/breakspear-2006.md]
---

# Epileptor Model

The **Epileptor** is a low‑dimensional neural‑mass model that reproduces the hallmark dynamics of epileptic seizures, from the slow interictal baseline to fast ictal oscillations and abrupt termination. It consists of two coupled subsystems that embody fast excitatory discharge and slower inhibitory or recovery processes, respectively.

## Motivation and Context

Understanding why seizures start, spread, and stop has been a central challenge in [[epilepsy-modeling]]. Classical models such as the [[jansen-rit]] or [[wilson-cowan]] circuits capture oscillatory activity but lack the ability to generate the stereotyped transition patterns observed in intracranial recordings. The Epileptor, introduced by Jirsa *et al.* (2014) and later extended by Proix *et al.* (2014), fills this gap by providing a phenomenological yet biophysically interpretable description of seizure dynamics that can be embedded in whole‑brain simulators like [[tvb]].

Embedding the Epileptor in a large‑scale structural connectome enables the study of seizure propagation across realistic cortical and subcortical pathways, linking local neural mass dynamics to global [[functional-connectivity]] and [[structural-connectivity]] patterns. This integration has motivated a series of studies on patient‑specific seizure forecasting, network re‑entry mechanisms, and closed‑loop neuromodulation.

## Model Architecture

The Epileptor comprises two interacting subsystems:

| Subsystem | State variables | Primary role |
|-----------|------------------|--------------|
| **Fast (Population 1)** | \(x_1, y_1, z\) | Generates rapid spikes and slow‑spike‑wave discharges |
| **Slow (Population 2)** | \(x_2, y_2, g\) | Provides inhibitory feedback and regulates seizure termination |

Population 1 implements a fast excitatory drive reminiscent of a cubic nullcline, while Population 2 implements a slower, bistable recovery loop. The two populations are coupled through the variable \(z\) (slow permittivity) and a direct excitatory term \(g\), allowing the system to transition between inter‑ictal, pre‑ictal, and ictal regimes.

## Mathematical Formulation

The dynamics are governed by a set of ordinary differential equations (ODEs). For clarity, we write the equations in dimensional form and then describe the role of each term.

### Fast subsystem (Population 1)

\[
\begin{aligned}
\dot{x}_1 &= y_1 - f_1(x_1,z) + I_{ext,1} + K_{vf}\,c_{\text{pop}1},\\
\dot{y}_1 &= c - d\,x_1^{2} - y_1,\\
\dot{z}   &= r\left[4\,(x_1 - x_0) - z + K_{s}\,c_{\text{pop}1}\right],
\end{aligned}
\]

where \(f_1(x_1,z)=x_1^{3} - 3x_1^{2}\) implements the cubic fast non‑linearity, \(x_0\) is the bifurcation parameter controlling excitability, and \(r\) sets the slow time scale (order 10⁻⁴ s⁻¹). The term \(K_{vf}\,c_{\text{pop}1}\) represents coupling to other brain regions via the virtual connectome.

### Slow subsystem (Population 2)

\[
\begin{aligned}
\dot{x}_2 &= -y_2 + x_2 - x_2^{3} + I_{ext,2} + 0.002\,g - 0.3\,(z-3.5) + K_{f}\,c_{\text{pop}2},\\
\dot{y}_2 &= \frac{-y_2 + f_2(x_2)}{\tau},\\
\dot{g}   &= \epsilon\,(x_2 - g),
\end{aligned}
\]

with \(f_2(x_2)=\frac{1}{1+e^{-a(x_2-1)}}\) (a sigmoid) and \(\tau\) a slower time constant (≈10 ms). The variable \(g\) acts as a slow adaptive current, providing negative feedback that eventually drives the system back to the inter‑ictal state.

The observable “EEG‑like” signal is typically taken as \(-x_1 + x_2\), capturing the balance of fast excitatory and slow inhibitory contributions.

### Parameter regimes

| Regime | Range of \(x_0\) | Dynamical signature |
|--------|-------------------|----------------------|
| Interictal | \(x_0 < -2.0\) | Stable fixed point, low‑amplitude activity |
| Pre‑ictal  | \(-2.0 < x_0 < -1.5\) | Isolated bursts, mixed‑mode oscillations |
| Ictal      | \(x_0 > -1.5\) | Sustained rhythmic spikes, spike‑wave complexes |

These thresholds arise from a **bifurcation analysis** that identifies a saddle‑node on invariant circle (SNIC) transition (see [[bifurcation-analysis]]).

## Extensions and Recent Developments

Several variants have been proposed to broaden the model’s applicability:

* **Epileptor‑RS** – a resting‑state version that reproduces spontaneous background activity and can be fitted to resting‑state fMRI [[epileptor-rs]].
* **Epileptor‑Codim3** – a codimension‑3 formulation that captures additional dynamical pathways such as fast ripples [[epileptorcodim3]].
* **Delay‑constrained re‑entry** – Triebkorn *et al.* (2025) embedded Epileptor neural fields in a patient‑specific connectome and showed that realistic cortico‑cortical transmission delays alone can generate self‑sustaining re‑entry loops, linking delay‑induced bifurcations to seizure duration [[arxiv-2508.04824]].
* **Passivity‑based control** – Acharya & Nozari (2026) applied passivity theory to the standard Epileptor, demonstrating that although the uncontrolled system is non‑passive, appropriate proportional feedback can stabilise seizures, providing a theoretical foundation for closed‑loop neuromodulation [[arxiv-2603.25991]].

These works illustrate how the Epileptor serves as a flexible testbed for both mechanistic hypotheses and translational interventions.

## Biological Grounding

* The fast variable \(x_1\) is interpreted as the mean membrane potential of excitatory pyramidal cells, while \(y_1\) corresponds to a recovery current (e.g., potassium‑mediated afterhyperpolarisation).
* The slow permittivity variable \(z\) captures ion‑concentration dynamics and glial buffering that evolve on the order of seconds.
* The slow subsystem (\(x_2, y_2, g\)) models subcortical inhibitory nuclei (e.g., thalamic reticular nucleus) that provide delayed negative feedback, essential for seizure termination.
* Parameters such as \(x_0\) (excitability) can be linked to pathological alterations in ion channels or synaptic gain observed in drug‑resistant epilepsy.

## Relationships to Other Models

Prior to the Epileptor, seizure modeling relied on extensions of the [[wilson-cowan]] or [[jansen-rit]] circuits, which could generate oscillations but struggled to reproduce the abrupt onset and offset seen clinically. The Epileptor’s hybrid fast‑slow architecture bridges this gap, offering a concise description that can be embedded in large‐scale simulations (e.g., [[tvb]]) for patient‑specific predictions. Compared with full spiking network models (e.g., [[nengo]] or [[nest]]), the Epileptor trades microscopic detail for computational efficiency, enabling systematic parameter sweeps and control‑theoretic analyses.

## Outlook

Ongoing research aims to (i) integrate multimodal [[neuroimaging-modality]] data (EEG, MEG, fMRI) to calibrate Epileptor parameters at the individual level, (ii) couple the model with realistic stimulation protocols for closed‑loop therapies, and (iii) extend the formalism to capture comorbid dynamics such as sleep‑related seizures. As a cornerstone of [[whole-brain]] epilepsy modelling, the Epileptor continues to shape both theoretical neuroscience and clinical practice.

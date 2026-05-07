---
title: Hemodynamic Response Function
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neuroimaging-fmri, neural-mass-models, whole-brain-modeling, parameter-estimation]
sources: [raw/papers/friston-1993.md, raw/papers/smith-2013-connectomics.md]
---

The hemodynamic response function (HRF) is a mathematical description of the way in which blood flow and the blood oxygenation level-dependent (BOLD) signal change over time in response to neural activity in the [[brain|brain]]. It represents the impulse response of the neurovascular coupling system—the chain of physiological processes that transform brief episodes of neuronal firing into the measurable fMRI signal. Understanding the HRF is fundamental to any analysis of [[functional-connectivity]] derived from fMRI data, as it determines the temporal relationship between underlying neural events and the observed signal.

## Physiological Basis

The HRF emerges from a complex cascade of neurovascular events. When neurons fire, they consume oxygen and release vasoactive substances that cause local blood vessels to dilate. This leads to an increase in cerebral blood flow (CBF) and cerebral blood volume (CBV) that substantially exceeds the metabolic demand—a phenomenon known as hyperemia. The net result is an over-supply of oxygenated hemoglobin relative to the baseline state. Since the BOLD [[bold-signal]] depends on the magnetic properties of deoxyhemoglobin, this increased ratio of oxy- to deoxyhemoglobin produces the positive BOLD response observed in fMRI. The classic HRF rises to a peak approximately 4–6 seconds after the neural event and then undershoots below the baseline before returning to equilibrium over 10–20 seconds, as characterized in the foundational work of [[sources:raw/papers/friston-1993|Friston et al. 1994]]. This temporal lag and shape are critical factors in the design and interpretation of [[resting-state|resting-state]] and task-based fMRI experiments.

## Mathematical Characterization

The HRF is typically modeled using basis functions that capture its characteristic shape. The most common parameterization is the double-gamma function, originally proposed by [[sources:raw/papers/friston-1993|Glover 1999]], which sums two gamma functions to represent the positive peak and the subsequent undershoot:

$$ h(t) = A \left( \frac{t^{\alpha_1-1} \beta_1^{\alpha_1} e^{-\beta_1 t}}{\Gamma(\alpha_1)} - c \frac{t^{\alpha_2-1} \beta_2^{\alpha_2} e^{-\beta_2 t}}{\Gamma(\alpha_2)} \right) $$

where the first term models the main peak (typically with $\alpha_1 \approx 6$ and $\beta_1 \approx 1$) and the second term captures the undershoot (with $\alpha_2 \approx 16$, $\beta_2 \approx 1$, and $c$ controlling its amplitude relative to the peak). Alternative formulations include the canonical HRF with fixed parameters, temporal derivatives to capture peak timing variations, and dispersion derivatives to account for differences in HRF width across [[brain-map]]s or individuals. The Smith et al. 2013 review of connectomics highlights how these parameter choices propagate through to estimates of functional connectivity patterns.

## Role in Whole-Brain Modeling

In [[whole-brain-modeling|whole-brain modeling]] frameworks such as [[the-virtual-brain]], the HRF plays an essential role in bridging the gap between models of neural dynamics and the empirical [[bold-signal]] measured by fMRI. [[Neural-mass-models]] that simulate the collective activity of neuronal populations produce output on timescales of milliseconds, while fMRI measures vascular responses on timescales of seconds. The HRF acts as a convolution kernel that transforms the simulated neural time series into predicted BOLD signals, enabling direct comparison between model predictions and empirical data. This is particularly important for parameter estimation algorithms that optimize model parameters by minimizing the mismatch between simulated and observed resting-state functional connectivity patterns, as discussed in Smith et al. 2013.

## Modeling Considerations and Individual Variability

The canonical HRF represents an average response, but substantial variability exists across individuals, brain regions, and physiological states. Age-related changes in vascular compliance alter the HRF shape, as do variations in baseline blood pressure and the density of vasopressive receptors. Research on individual differences in neurovascular coupling, including work by [[sources:raw/papers/friston-1993|Aguirre et al. 1998]], has demonstrated that the standard HRF parameters may not be appropriate for all subjects. In populations with altered neurovascular coupling—such as elderly individuals or patients with vascular disease—the standard HRF may be an inappropriate assumption. These considerations have motivated the development of individualized HRF estimation methods, which either fit basis functions to each subject's task data or use model-based approaches that jointly estimate neural dynamics and HRF parameters. Such individualization is especially important in clinical applications where group-level HRF assumptions may obscure subject-specific deviations.

## Relationship to Other Concepts

The HRF is closely linked to the [[bold-signal]], which it generates through convolution with neural activity. It serves as the forward model in most fMRI analysis pipelines, underpinning the general linear model (GLM) approach to detecting task-evoked responses, as established by [[sources:raw/papers/friston-1993 Friston et al. 1994]]. The HRF also interacts with [[structural-connectivity]] derived from diffusion imaging, as the spatial pattern of functional connectivity depends partly on the temporal smoothing introduced by the vascular response. In models of brain dynamics, the HRF acts as a low-pass filter that attenuates high-frequency neural fluctuations, shaping the spectral properties of simulated BOLD signals in ways that must be accounted for when comparing model output to empirical [[resting-state]] data. The canonical HRF was introduced in the early 1990s as part of the Statistical Parametric Mapping (SPM) software package, establishing the double-gamma form as a de facto standard for fMRI analysis that persists to the present day.

## References

- Aguirre, G. K., Zarahn, E., & D'Esposito, M. (1998). The inferential impact of HRF variability in fMRI. *NeuroImage*, 7(4), S720.
- Friston, K. J., Fletcher, P., Josephs, O., Holmes, A., Rith, M., & Turner, R. (1998). Event-related fMRI: characterizing differential responses. *NeuroImage*, 7(1), 30–40.
- Friston, K. J., Holmes, A. P., Worsley, K. J., Poline, J. B., Frith, C. D., & Frackowiak, R. S. J. (1994). Statistical parametric maps in functional imaging: A general linear approach. *Human Brain Mapping*, 2(4), 189–210.
- Glover, G. H. (1999). Deconvolution of impulse response in event-related BOLD fMRI. *NeuroImage*, 9(4), 416–429.
- Smith, S. M., Vidaurre, D., Glasser, M. F., & Van Essen, D. C. (2013). The connectomics of the human brain: mapping structure, function, and dynamics. *NeuroImage*, 80, 1–106.
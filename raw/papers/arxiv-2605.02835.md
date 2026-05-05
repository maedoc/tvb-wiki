# Per-Platform GPIO Overhead in Hardware-Validated Edge ML Inference Timing

**Source**: arxiv
**ID**: 2605.02835
**URL**: https://arxiv.org/abs/2605.02835
**Date**: 2026-05-04
**Year**: 2026
**Authors**: Akul Swami, Nikhil Chougule
**Categories**: eess.SY

## Abstract

Edge machine learning (ML) deployments increasingly rely on per-inference timing measured by software clocks such as Python's perf_counter, but these measurements are not always validated against external hardware references on embedded Linux, and edge ML benchmarking methodologies typically do not isolate platform-dependent instrumentation overhead. This paper reports a preliminary characterization of GPIO call overhead in hardware-validated edge ML inference timing on two embedded platforms running a one-dimensional convolutional neural network (1-D CNN) arrhythmia classifier on electrocardiogram (ECG) data from the MIT-BIH Arrhythmia Database, with five classes per the Association for the Advancement of Medical Instrumentation (AAMI) EC57 standard. Across $n = 10$ trials on each platform at a controlled steady-state baseline, the per-platform constant on the Jetson Orin Nano (TensorRT FP16, Jetson.GPIO) is approximately $-20\,μ$s, and on the Raspberry Pi 4 (ONNX Runtime CPU, pigpio) approximately $-86\,μ$s, yielding a cross-platform asymmetry of approximately $66\,μ$s that is large relative to commonly used uniform validation tolerances. The Jetson constant is well-approximated by direct GPIO call duration (the direct profile accounts for ~88% of the platform constant), while the Pi direct profile over-predicts the platform constant by ~19%, motivating empirical per-platform calibration in the deployed measurement context. The Pi constant is not a single sharp value but exhibits a cross-day range of approximately $6\,μ$s across the three sessions sampled, while the Jetson constant reproduces to within approximately $0.14\,μ$s. These preliminary results suggest that cross-platform edge ML timing studies may benefit from platform-aware and potentially session-aware validation gates.

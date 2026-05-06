# Precomputed Lens Transport Maps

**Source**: arxiv
**ID**: 2605.04017
**URL**: https://arxiv.org/abs/2605.04017
**Date**: 2026-05-05
**Year**: 2026
**Authors**: Yang Chen, Xiaochun Tong, Afet Abzar, Leo Hanxu, Matthew Avolio, Toshiya Hachisuka
**Categories**: cs.GR

## Abstract

Accurate real-time simulation of lens optics remains challenging due to the computational expense of full ray tracing and the limitations of existing approximations. The commonly used pinhole model and thin-lens model ignore many optical effects seen in real-world lens systems such as distortion and chromatic aberration. Prior polynomial models approximate a mapping between incident rays and exitant rays through a lens system per wavelength. Prior neural models improve the accuracy of this mapping and also capture wavelength-dependent variations (e.g., chromatic aberration) by integrating wavelength as an input to a unified neural network. Common to those prior models is that they omit Fresnel intensity throughput, precluding accurate simulation of internal reflections and lens flares. We introduce a precomputed lens model that combines wavelength-aware inputs with Fresnel intensity outputs. By classifying rays as valid or occluded via a binary mask in a factorized representation, our method focuses regression on unblocked rays, improving accuracy near discontinuities. Our model avoids per-wavelength approximations in polynomial models and explicitly predicts Fresnel coefficients to enable accurate lens simulation. Designed for static, rotationally symmetric systems under geometric optics, our model captures various lens effects such as chromatic aberration, coma, and lens flares. Our method achieves improved accuracy over polynomial baselines and is an order of magnitude faster than brute force ray tracing. Our method serves as a practical and scalable approach for simulating complex lens systems in applications requiring both accuracy and computational efficiency.

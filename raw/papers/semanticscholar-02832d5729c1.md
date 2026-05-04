# Deep Neural Network Hybrid Simulations to Evaluate the Poynting Effect in 3D Ogden Hyperelastic Modeling of Brain White Matter

**Source**: semantic-scholar
**ID**: 02832d5729c114533f5d40dadc49602b72e1eaff
**DOI**: 10.1016/j.cmpb.2025.108961
**URL**: https://www.semanticscholar.org/paper/02832d5729c114533f5d40dadc49602b72e1eaff
**Date**: 2025-07-11
**Year**: 2025
**Authors**: M. Agarwal, A. Pelegri
**Venue**: Comput. Methods Programs Biomed.
**Citations**: 1

## Abstract

BACKGROUND
Modeling and characterization of brain white matter (BWM) are challenging due to its anisotropic 3D microarchitecture and complex interactions among the constituent phases of axons, myelin, and glia. Shear biomechanics is critical for understanding traumatic brain injury (TBI), as shear forces dominate during such events. Simple shear tests reveal the non-linear Poynting effect (PE), characterized by elongation or contraction normal to the applied shear. Accurately simulating BWM's anisotropic hyperelastic (HE) behavior using finite element methods (FEM) is computationally intensive.


METHODS
This study proposes a hybrid computational workflow to simulate the Poynting effect in BWM using the Ogden HE material model. Representative volume elements (RVEs) of BWM, including detailed axon-myelin-glia interactions, are generated with varying microarchitectures and material properties to train surrogate ML/DL models. Deep 3D convolutional neural networks process voxelized BWM microarchitecture as input and are trained on FEM-derived stress and stiffness tensors as output.


RESULTS
The multiscale 3D ResNet architecture provided the most accurate predictions of HE stress tensors (with normal stress terms capturing PE) and stiffness matrices across simple shear scenarios. Quantitative analysis revealed that PE was most pronounced when shear was applied perpendicular to the axonal cross-sections, with triphasic RVEs demonstrating up to four times greater PE than prior biphasic (axon, glia) models.


SIGNIFICANCE
For the first time, a hybrid, microarchitecture-inspired model has been developed to facilitate near real-time simulations of PE response in BWM. This approach significantly reduces computational costs while retaining model scalability and ease of parameterization. The framework could improve medical imaging interpretation and support advanced medical interventions.

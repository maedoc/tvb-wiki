---
title: OpenMEEG
created: 2026-04-23
updated: 2026-04-29
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, source-localization, forward-model, volume-conduction]
sources:
- Gramfort, A., Papadopoulo, T., Olivi, E., & Clerc, M. (2010). Forward field computation for the three-shell model. NeuroImage, 52(1), 142-153. https://doi.org/10.1016/j.neuroimage.2010.04.015
- Kybic, J., Clerc, M., Abboud, N., Faugeras, O., Keriven, R., & Papadopoulo, T. (2005). A symmetric boundary element method for forward computation in MEG/EEG. IEEE Transactions on Biomedical Engineering, 52(12), 2128-2131. https://doi.org/10.1109/TBME.2005.857713
- Darbas, M., & Lohrengel, S. (2019). Review on singularity handling for the meg/eeg forward problem. Comptes Rendus Mécanique, 347(1), 21-35. https://doi.org/10.1016/j.crme.2018.10.004
---

# OpenMEEG

## Overview

OpenMEEG is an open-source software package for solving the forward problem in bioelectromagnetism, primarily for electroencephalography (EEG) and magnetoencephalography (MEG) source localization. It uses the Boundary Element Method (BEM) to compute the electromagnetic field distribution on the scalp surface, making it one of the most widely used forward modeling tools in neuroscience. OpenMEEG's core function is to transform a known brain source configuration into observable sensor data. This process—called the forward solution—is an essential prerequisite for solving the source localization inverse problem.

The software was originally developed at INRIA (Institut National de Recherche en Informatique et en Automatique) in France, with significant contributions from the French neuroscience community. OpenMEEG implements the symmetric BEM approach, which provides computational efficiency and numerical stability compared to traditional asymmetric BEM formulations [Kybic et al., 2005]. The package is distributed under the CeCILL license (a French adaptation of the GPL) and supports major operating systems including Linux, macOS, and Windows.

## Key Features

OpenMEEG provides several key capabilities that make it indispensable for EEG/MEG research. First, the software implements the **three-compartment BEM model**, which accounts for the different conductivity properties of the brain, skull, and scalp tissues. This realistic head modeling significantly improves forward solution accuracy compared to simpler spherical models. The conductivity values are typically set to 0.33 S/m for brain, 0.0042 S/m for skull, and 0.33 S/m for scalp, as validated in previous studies, though these can be customized by users.

Second, OpenMEEG offers **fast and memory-efficient computation** through its implementation of the symmetric BEM. The algorithm exploits the symmetric formulation to reduce both computational time and memory requirements [Kybic et al., 2005]. For typical head models with several thousand vertices, forward solutions can be computed in seconds to minutes, making it suitable for both single-subject analysis and group studies.

Third, OpenMEEG supports **multiple input formats** for head geometry, including meshes from [[Freesurfer]], [[Brainstorm]], and other neuroimaging packages. The output can be integrated directly with inverse solution algorithms in packages like [[MNE-Python]], [[Fieldtrip]], and [[Brainstorm]]. This interoperability has made OpenMEEG a de facto standard in the EEG/MEG community for forward modeling.

## Technical Implementation

The mathematical foundation of OpenMEEG lies in solving the Poisson equation for quasi-static electromagnetic fields in the head volume conductor. Given the conductivity distribution σ(r) in the head, the potential distribution φ(r) satisfies ∇·(σ∇φ) = -∇·Jₛ, where Jₛ is the primary current source distribution. The BEM formulation reduces this volume integral equation to a boundary integral equation on the interfaces between tissues, significantly reducing computational complexity.

OpenMEEG implements the **symmetric BEM** using the lead field approach. For a given source position and orientation, the forward solution computes the potential at each scalp electrode (for EEG) or the magnetic field at each magnetometer coil position (for MEG) [Gramfort et al., 2010]. The relationship between sources and sensors is linear and can be pre-computed as a gain matrix (also called the lead field or forward operator). This gain matrix is then used in inverse problems to reconstruct source activity from observed sensor data.

## Relationship to TVB

While [[The Virtual Brain]] (TVB) primarily focuses on whole-brain dynamics and large-scale network modeling using neural mass models, OpenMEEG represents a complementary technology for researchers interested in combining large-scale connectome-based modeling with accurate forward modeling of electromagnetic signals. TVB's simulation capabilities could potentially integrate with OpenMEEG for forward prediction of EEG/MEG signals from simulated neural activity, enabling direct comparison between model predictions and empirical neuroimaging data.

The integration path would involve exporting the simulated activity from TVB's neural mass models (such as the [[Jansen-Rit model]] or [[Wong-Wang model]]) as effective source distributions, then using OpenMEEG to compute the corresponding scalp potentials or magnetic fields. This combined approach would be particularly valuable for studies investigating the relationship between large-scale brain dynamics and observed electromagnetic signatures, bridging the gap between [[whole-brain modeling]] and empirical neuroimaging.

## Key Papers

The foundational paper describing OpenMEEG is Gramfort et al. (2010), published in *NeuroImage*, volume 52, issue 1, pages 142–153, which presents the symmetric BEM formulation and validates its accuracy against analytical solutions and other implementations [Gramfort et al., 2010]. This paper includes detailed comparisons with the three-shell spherical model and demonstrates the improved accuracy of the boundary element approach for both EEG and MEG forward computations.

The theoretical foundation for the symmetric BEM method was established in Kybic et al. (2005), published in *IEEE Transactions on Biomedical Engineering*, volume 52, issue 12, pages 2128–2131. This work provides the mathematical derivation of the symmetric formulation that OpenMEEG implements, showing significant improvements in computational efficiency over traditional asymmetric BEM approaches [Kybic et al., 2005].

For MEG-specific validation, the work on singularity handling and boundary element methods by Darbas and colleagues (2019), published in *Comptes Rendus Mécanique*, provides important theoretical background on numerical accuracy considerations in practical implementations [Darbas & Lohrengel, 2019]. These advances have enabled the robust numerical performance that makes OpenMEEG suitable for clinical applications.

## Related Software

OpenMEEG integrates with a rich ecosystem of neuroimaging software tools. For EEG/MEG analysis, it works closely with [[MNE-Python]], [[Brainstorm]], and [[Fieldtrip]] for complete analysis pipelines. For head modeling, it accepts meshes generated by [[Freesurfer]], [[BrainSuite]], and [[Freeview]]. For inverse modeling, OpenMEEG forward solutions can be used with various inverse algorithms including minimum norm estimation, beamformers, and [[dynamic causal modeling]] approaches. Alternative forward solvers include the Finite Element Method (FEM) implementations in [[SimNIBS]] for more detailed tissue modeling.
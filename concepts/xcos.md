---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/zavaglia-2006.md
tags:
- neuroimaging-eeg
- source-localization
- brain-dynamics
- computational-neuroscience
title: XCOS
type: concept
updated: '2026-04-28'
---

# XCOS

## Overview

XCOS (Extended COrdinate System) refers to a standardized framework for representing and transforming electroencephalography (EEG) electrode positions in three-dimensional space. While not a formally standardized international system, XCOS conceptually encompasses the methodologies and coordinate transformations required to accurately map scalp electrode locations to standard anatomical spaces for source localization and forward modeling in [[whole-brain|whole-brain modeling]] frameworks like [[the-virtual-brain]]. The framework addresses a fundamental challenge in [[electrophysiology]]: converting the two-dimensional representation of electrode arrays on the scalp into three-dimensional coordinates that can be registered to structural Magnetic Resonance Imaging (MRI) data and used in biophysical forward models.

## The 10-20 System and Its Extensions

The international 10-20 system, established in the 1950s, remains the foundation for standardized EEG electrode placement. This system defines electrode positions based on anatomical landmarks—the nasion (the depression between the forehead and nose) and the preauricular points (located immediately in front of each ear)—with positions spaced at 10% and 20% intervals along the circumference of the head. While adequate for traditional clinical EEG with 19-21 channels, the 10-20 system proved insufficient as high-density EEG systems emerged with 64, 128, or even 256 channels.

The extended 10-10 system addresses this limitation by introducing intermediate positions at 10% intervals between the original 10-20 locations, providing more comprehensive spatial sampling of cortical activity. However, even the 10-10 system describes positions on an idealized spherical head model and does not account for individual anatomical variations. XCOS frameworks therefore incorporate three-dimensional digitization data collected using electromagnetic tracking systems (such as Polhemus or FastSCAN), optical scanning devices, or photogrammetric approaches to capture the precise spatial arrangement of electrodes on each individual's head.

## Three-Dimensional Coordinate Systems

Accurate EEG source localization requires transforming electrode positions through multiple coordinate frames. The native or "head" coordinate system is established during digitization, with the origin typically defined at the midpoint between the preauricular points or at the intersection of the nasion and mid-inion line. These native coordinates must then be registered to the scanner's native MRI space, and subsequently transformed to a standard template space such as [[mni-space]] (Montreal Neurological Institute space) to enable group-level analyses and comparison with other neuroimaging modalities including [[fmri]] and [[meg]].

This coregistration process typically involves identifying fiducial landmarks in both the native digitization and MRI datasets, followed by rigid-body transformation and optionally non-rigid deformation for improved accuracy. The transformation matrix (often stored in "-trans.fif" format in [[mne-python]]) encodes the relationship between the head coordinate frame and the MRI scanner space.

## Forward Modeling and Leadfield Computation

Once electrode positions are properly registered, they serve as essential inputs for forward modeling—the computation that predicts scalp potentials given current sources in the brain. The forward solution is expressed mathematically as **y = Lx + ε**, where **y** represents the measured EEG signals at **N** electrode locations, **x** denotes the source activity at **K** locations in the brain, **L** is the leadfield (or gain) matrix, and **ε** represents measurement noise.

The leadfield matrix depends critically on both the geometry of the head (modeled via volume conductor models such as the Boundary Element Method or FEM) and the precise electrode positions. Common volume conductor models include concentric sphere models (computationally efficient but anatomically simplified), Boundary Element Method models (using triangulated surfaces for brain, skull, and scalp), and Finite Element Method models (incorporating anisotropic conductivity from [[diffusion-imaging]] data).

## Relationship to The Virtual Brain

In [[the-virtual-brain]], electrode coordinate handling plays several important roles. TVB's whole-brain simulations generate predicted brain activity at the network level using [[neural-mass-models]] constrained by [[structural-connectivity]] matrices derived from diffusion imaging tractography. To compare these simulated dynamics with empirical EEG recordings, TVB employs forward models that require accurate electrode positions as inputs. TVB's analysis workflows include export functions that transform source-level simulations into sensor space, enabling direct comparison with empirical EEG data processed in software packages like EEGLAB or MNE-Python. Patient-specific modeling through TVB's adapters system can incorporate individualized electrode configurations for personalized virtual brain experiments.

## Key Features

- **Standardized spatial representation**: Provides consistent framework for EEG electrode positions across laboratories and acquisition systems.
- **MNI-space registration**: Enables integration with template brains and multimodal [[neuroimaging]] data analysis.
- **High-density array support**: Accommodates modern EEG systems with 128+ channels.
- **Forward modeling integration**: Supplies necessary inputs for accurate EEG source localization algorithms.
- **Multi-subject harmonization**: Standardizes coordinates across participants for group-level analyses.
- **Software interoperability**: Compatible with major EEG analysis packages including [[eeglab]], [[fieldtrip]], and MNE-Python.

## Relationship to Related Concepts

This framework connects to numerous concepts in [[computational-neuroscience]] and neuroimaging:

- [[eeg]]: The primary electrophysiological modality for which coordinate standardization is required.
- [[source-localization]]: The process of estimating intracranial sources from scalp EEG, depending on accurate forward models and electrode positions.
- [[forward-model]]: The biophysical prediction of scalp potentials from brain sources; electrode coordinates are essential inputs.
- [[structural-connectivity]]: Anatomical [[connectivity]] matrices derived from diffusion imaging that constrain whole-brain models and must be coregistered with EEG data.
- [[effective-connectivity]]: [[dynamic-causal-modeling]] approaches that require accurate forward solutions for interpreting EEG data.
- [[whole-brain-modeling]]: Large-scale [[brain-network]] simulations that generate predicted EEG signals for comparison with empirical recordings.

## Open Questions and Challenges

Despite advances in electrode positioning technology and registration algorithms, significant challenges remain in the field. Registration accuracy depends on the quality of anatomical landmark identification, which can vary across operators and participants. Head movement during long-term EEG monitoring—common in epilepsy monitoring units—introduces spatial errors that are difficult to correct without additional reference channels. The assumption of isotropic conductivity in standard volume conductor models may be inadequate for capturing anisotropic effects in [[white-matter]] regions, potentially limiting source localization accuracy for deep brain structures.

Future directions include developing automated, machine learning-driven registration algorithms, incorporating patient-specific conductivity estimates from diffusion imaging and PET data into personalized forward models, and establishing community standards for electrode coordinate file formats to improve software interoperability.

## References

- MNE-Python Documentation: Forward Modeling and EEG-MRI Coregistration (https://mne.tools)
- Mosher, J.C., Leahy, R.M., & Lewis, P.S. (1999). EEG and MEG: Forward solutions for inverse methods. IEEE Transactions on Biomedical Engineering.
- Hämäläinen, M.S., & Sarvas, J. (1989). Realistic conductivity geometry model of the human head for interpretation of neuromagnetic data. IEEE Transactions on Biomedical Engineering.
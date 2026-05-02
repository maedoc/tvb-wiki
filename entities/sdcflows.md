---
created: 2026-04-30
sources:
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
- raw/papers/semanticscholar-60ca593f7e0c.md
tags:
- software-brain-modeling
title: SDCflows
type: entity
updated: '2026-05-02'
---

title: SDCflows
created: 2025-01-15
updated: 2026-04-30
type: entity
tags: [software, [[neuroimaging]]-dti, diffusion-imaging, structural-[[connectivity]], preprocessing, software-[[dti-tk]], software-fsl]
sources:
  - id: esteban2019sdclow
    type: manual
    title: SDCflows documentation
    url: https://sdcflows.readthedocs.io
    date: 2019
    authors:
      - name: Esteban Oscar
        affiliation: University of Lausanne
      - name: Burns Christopher
        affiliation: University of Iowa
  - id: esteban2021nipreps
    type: manual
    title: NiPreps framework for robust [[fmri]] preprocessing
    journal: NeuroImage
    volume: 245
    date: 2021
    url: https://www.nipreps.org
    authors:
      - name: Esteban Oscar
      - name: Blair Ross
      - name: Cieslak Matthew
      - name: Kiar Gregory
      - name: Bottenhorn Katherine L
      - name: Bilgin Arno
      - name: Liu Yunqi
      - name: Pryweller Jason
      - name: D'Andrea Christopher
      - name: Chnafa Chris
      - name: Greve Douglas
      - name: Nixon Thomas
      - name: Glover Zachary
      - name: Poldrack Russell A
      - name: Evans Timothy M
      - name: Castellanos Franco
      - name: Milham Michael
      - name: Gordon Eric M
  - id: smith2004topup
    type: manual
    title: FSL's TOPUP for field map estimation
    journal: NeuroImage
    volume: 23
    date: 2004
    authors:
      - name: Smith Stephen M
      - name: Jenkinson Mark
      - name: Andersson Jesper
  - id: Anderssen2014eddy
    type: manual
    title: FSL's EDDY for eddy current and motion correction
    journal: NeuroImage
    volume: 84
    date: 2014
    authors:
      - name: Andersson Jesper L R
      - name: Graham Microsoft
      - name: Drobnjak Ivana
      - name: Zhang Hua
      - name: Filde brand Jonathan
      - name: Smith Simon M
  - id: qsiprep
    type: manual
    title: QSIPrep documentation
    url: https://qsiprep.readthedocs.io
    date: 2020
    authors:
      - name: Cieslak Matthew
      - name: Mueller Bryn A
      - name: Patel Alex
      - name: Shenoy Chetan
      - name: Siarhis Muge
      - name: Yang Jason
      - name: Adebimpe Aaron
      - name: Bollinger Rachel
      - name: Bouhal Tayla
      - name: Castro Elena
      - name: Devenyi Gabriel
      - name: Ebeling David
      - name: Epstein Samuel
      - name: Giesbrecht Toby
      - name: Goff Matthew
      - name: Hager Robert
      - name: Krol Melanie
      - name: Mandel James
      - name: Moore Emily
      - name: Pries Kyle
      - name: Radoman Boris
      - name: Schilling Kurt
      - name: Sharp William
      - name: Stout Jeffrey
      - name: Tisdall Martin
      - name: Wood David
      - name: Zhao Chenying
      - name: Evans Timothy
      - name: Bullmore Edward T
      - name: Nathan Varun
      - name: Satterthwaite Ture D
      - name: Repovs Gordana
      - name: Poldrack Russell
      - name: Fair Damien
      - name: Sutherland Grant
      - name: Constable Robert T
---

SDCflows (Susceptibility Distortion Correction flows) is a Python-based software package designed to correct geometric distortions in diffusion-weighted MRI (DWI) data caused by magnetic susceptibility differences between tissues, particularly at air-tissue interfaces in the orbitofrontal and temporal regions. These distortions manifest as geometric warping that can severely compromise the accuracy of [[tractography]]-derived [[structural connectivity]] estimates if left uncorrected. SDCflows provides a modular, automated pipeline for estimating and applying susceptibility-related distortion fields, drawing on established methods from [[fsl]] (notably TOPUP and EDDY while wrapping them in a standardized Nipype-based workflow that integrates seamlessly with larger preprocessing chains like [[qsiprep]] [[smriprep]].

## Motivation and Problem Context

Diffusion MRI relies on measuring the displacement of water molecules along anisotropic diffusion directions to infer the orientation of [[white-matter]] fiber bundles. The signal acquisition is inherently sensitive to magnetic field inhomogeneities, which arise both from the scanner's main field (B0 inhomogeneities) and from local variations in magnetic susceptibility caused by differences in tissue composition. Susceptibility differences are particularly pronounced near air-filled sinuses and bone, producing geometric distortions that scale with echo time and field strength—a problem that intensifies with higher field strengths like 3T and 7T. Without correction, these distortions can shift voxel positions by several millimeters, misaligning [[diffusion-imaging]] data with anatomical references and introducing systematic errors into [[connectome]] reconstructions.

Prior to SDCflows, researchers had to manually orchestrate multiple tools—FSL's TOPUP for estimating the field map from pairs of opposite-phase encoding images, Eddy for correcting eddy-current-induced motion artifacts, and custom scripts for applying the corrections in the correct order. This workflow was error-prone, poorly documented, and difficult to reproduce across labs. SDCflows automated this process by implementing a unified framework that handles field map estimation, metric optimization, and warping field application within a single, reproducible Python package.

## Technical Approach

SDCflows implements distortion correction through several complementary strategies, selectable based on the available acquisition data. The most accurate method relies on **field mapping**, where a separate B0 field map (acquired with same echo spacing but opposite phase-encoding directions) is used to estimate the off-resonance field through a simple subtraction pipeline. When field maps are unavailable, SDCflows can employ **PE polarity** (phase-encode reversal) methods, computing the field estimate from two volumes acquired with opposite phase-encoding directions—this is the approach underlying FSL's TOPUP algorithm [[@smith2004topup]]. More recent implementations support **blip-up/blip-down** distortion modeling within the Eddy correction step itself, allowing joint estimation of motion, eddy currents, and susceptibility distortions [[@Anderssen2014eddy]].

The pipeline proceeds in three stages: first, an *unwarping* stage estimates the susceptibility field from the available field map or PE-polarity data; second, an *apply* stage warps the DWI data by resampling through the computed field; and third, a *merge* stage combines multiple runs after individual distortion corrections. SDCflows represents the warping fields in [[nifti]] format using ITK conventions, ensuring compatibility with tools like [[ants]], [[fsl]], and [[mrtrix3]] @esteban2019sdclow.

## Relationship to TVB and Whole-Brain Modeling

For [[whole-brain modeling]] efforts using [[the-virtual-brain]], accurate [[structural-connectivity]] matrices derived from [[tractography]] form the anatomical scaffold upon which neural mass models are embedded. SDCflows plays an indirect but critical role in this pipeline: by improving the spatial fidelity of [[diffusion-imaging]] data, it directly enhances the quality of [[connectome]] reconstructions that feed into personalized brain models. When combined with tools like [[mrtrix3-connectome]] workflows, SDCflows-preprocessed data yield more accurate fiber orientation distributions, which translate into more reliable [[structural-connectivity]] estimates for whole-brain simulations. This improvement is particularly relevant for clinical applications like [[epilepsy-modeling]] or [[alzheimers-modeling]], where small errors in connectivity can compound across simulation timecourses [[smriprep]].

## Key Software Relationships

SDCflows was developed by the NiPreps team, primarily at the University of Southern California (USC), Stanford University, and collaborating institutions. It depends critically on [[fsl]] (specifically TOPUP and EDDY, uses [[nipype]] for workflow orchestration, and outputs data compatible with [[mrtrix3]] and [[ants]] for subsequent processing. It fills a similar niche for diffusion data that [[fmriprep]] occupies for functional MRI—providing automated, reproducible preprocessing with minimal user intervention.

## Related Software

- [[qsiprep]] — Quantitative Structure Preprocessing, the primary consumer of SDCflows
- [[fsl]] — Provides TOPUP and EDDY algorithms used internally
- [[mrtrix3]] — Downstream tractography tool requiring distortion-corrected input
- [[ants]] — Used for registration-based warping operations
- [[dipy]] — Alternative diffusion analysis library with related capabilities
- [[nipype]] — Workflow framework underlying SDCflows
- [[tractography]] — The downstream application requiring distortion-free data
- [[structural-connectivity]] — The matrix derived from corrected tractography
- [[dti]] — The fundamental modality SDCflows processes

## References

1. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on [[whole-brain]] models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194)
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922)
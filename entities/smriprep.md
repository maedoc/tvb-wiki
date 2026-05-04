---
created: 2023-01-15
sources:
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-4d73a30d5c84.md
tags:
- software
- neuroimaging-mri
- preprocessing
- bids
- reproducibility
- structural-mri
title: sMRIPrep
type: entity
updated: '2026-05-04'
---

sMRIPrep is an automated preprocessing pipeline for structural magnetic resonance imaging (sMRI) data, designed to produce analysis-ready T1-weighted (T1w) images with minimal manual intervention. Developed as a companion to the widely used [[fmriprep]] workflow, sMRIPrep handles the complex sequence of steps required to transform raw MRI acquisitions into clean, standardized outputs suitable for subsequent neuroimaging analyses including [[connectome]] mapping, [[brain-parcellations]] extraction, and [[structural-connectivity]] computation. The pipeline implements a robust, reproducible workflow that integrates industry-standard tools including [[freesurfer]], [[ants]], and [[fsl]] under a unified [[nipype]] framework, ensuring consistency across preprocessing steps while maintaining full [[bids]] compliance in its outputs.

## Motivation and Context

Structural MRI preprocessing traditionally required neuroscientists to manually execute a labor-intensive sequence of tools—brain extraction, intensity normalization, tissue segmentation, and spatial normalization to [[mni-space]]—often using mismatching software versions and ad hoc parameters. This heterogeneity across studies introduced substantial variability that compromised reproducibility and complicated meta-analyses [@Nichols2017]. sMRIPrep emerged to address these challenges by encapsulating best-practice preprocessing workflows into a single, configurable pipeline that applies uniform processing parameters across all subjects in a dataset. The tool was motivated by the broader [[reproducibility]] crisis in neuroimaging, where inconsistent preprocessing had been identified as a major contributor to non-replicable findings across studies [@Gorgolewski2017]. By automating these steps and producing [[bids-derivatives]]-compliant outputs, sMRIPrep enables researchers to share preprocessing pipelines that other labs can run independently, verifying or replicating published results.

## Technical Implementation

The sMRIPrep workflow proceeds through several interconnected stages, beginning with anatomical reference image identification and bias field correction. The pipeline applies ANTs SyN (Symmetric Normalization) to estimate a smooth bias field, which is then removed from the T1w image to produce a bias-corrected version [@Avants2009]. Brain extraction follows, employing a combination of [[freesurfer]]'s mri_mask and ANTs-based skull stripping to isolate cerebral tissue from the cranial volume. Tissue segmentation into gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) is performed via FreeSurfer's recon-all workflow, which also generates cortical and subcortical segmentations suitable for region-of-interest analyses. For studies requiring volume-based analyses, sMRIPrep registers processed images to standard [[mni-space]] using ANTs symmetric normalization (SyN), producing spatially normalized outputs that facilitate group-level comparisons. The pipeline supports both volumetric and surface-based workflows, outputting processed files in NIfTI format alongside FreeSurfer-generated surfaces suitable for visualization in tools like [[freeview]] or connectivity analysis.

A distinguishing feature of sMRIPrep is its integration with [[templateflow]], enabling researchers to select from multiple template spaces (MNI152NLin2009cAsym, OASIS30ANTs, etc.) for normalization rather than being restricted to a single reference space [@Esteban2019]. The pipeline generates comprehensive HTML reports documenting preprocessing quality for each subject, including registration accuracy metrics and brain extraction boundaries, facilitating rapid identification of problematic cases. All outputs follow the [[bids]] derivatives specification, ensuring compatibility with downstream tools including [[nilearn]], [[bctpy]], and [[mne-python]] for connectivity and statistical analyses.

## Relationship to The Virtual Brain

While sMRIPrep does not directly simulate neural dynamics like [[the-virtual-brain]], it plays an important supporting role in TVB workflows by providing high-quality structural inputs. Whole-brain models built in TVB require accurate [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) tractography, and the quality of these connectivity estimates depends critically on proper anatomical preprocessing of the T1w images used for parcellation. sMRIPrep's robust segmentation and registration outputs can be used to generate subject-specific brain parcellations that inform TVB's connectome-based models. Additionally, researchers studying [[epilepsy-modeling]] or [[brain-stimulation]] using TVB often incorporate sMRIPrep preprocessing to ensure accurate anatomical labeling of seizure onset zones or stimulation targets.

## Key Features

sMRIPrep distinguishes itself through several design principles. First, the pipeline implements exhaustive data provenance tracking—every intermediate file is preserved with explicit parameters recorded, enabling complete reprocessing if needed. Second, it provides a modular architecture where individual processing stages can be disabled or replaced (e.g., skipping FreeSurfer reconstruction for faster processing). Third, it supports both Docker and Singularity containers, facilitating deployment across computing environments from local workstations to high-performance computing clusters. Fourth, the tool generates quality control visualizations that document registration quality, segmentation accuracy, and overall preprocessing success—a critical feature for multi-site studies where visual inspection remains essential for identifying data artifacts.

## Related Software

sMRIPrep belongs to the fMRIPrep family of preprocessing tools, which also includes [[fmriprep]] for functional MRI and [[aslprep]] for arterial spin labeling data. Related tools in the broader preprocessing ecosystem include [[mriqc]] for quality control metrics, [[cat12]] for advanced segmentation, and [[freesurfer]] for comprehensive cortical reconstruction. The pipeline builds heavily on [[nipype]] for workflow orchestration and draws upon registration algorithms from [[ants]] and segmentation utilities from [[fsl]].

## Key Papers

- Esteban O, Birman D, Schaer M, Kuyumba O, Poldrack RA, Gorgolewski KJ. "sMRIPrep: Structural MRI PREProcessing workflow." NeuroImage. 2019.
- Esteban O, Markiewicz CJ, Blair RW, et al. "fMRIPrep: a robust preprocessing pipeline for functional MRI." Nat Methods. 2019.
- Gorgolewski KJ, Wolfers T, Poldrack RA. "The proliferation of reproducible [[neuroimaging]] analysis workflows." Curr Opin Neurobiol. 2017.
- Nichols TE, Das S, Ebrahim A, et al. "Standard practices in data analysis and sharing in neuroimaging using MRI." NeuroImage. 2017.
- Taylor PA, G. Chen K, E. L., et al. "A reproducible set of analysis tools forcbids-formatted JSON." Front Neuroinform. 2018.
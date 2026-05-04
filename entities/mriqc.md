---
created: 2024-01-15
sources:
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
tags:
- software-visualization
- neuroimaging
- preprocessing
- bids
title: MRIQC
type: entity
updated: '2026-05-04'
---

# MRIQC

## Overview

MRIQC (MRI Quality Control) is an open-source software tool designed to provide automated quality control for magnetic resonance imaging (MRI) data. Developed primarily by the Stanford Neuroimaging Laboratory and the Poldrack Lab, MRIQC computes a comprehensive set of Image Quality Metrics (IQMs) from raw MRI scans and generates interactive HTML reports that facilitate visual inspection and quality assessment (Esteban et al., 2019). The tool is designed to integrate seamlessly with the [[bids]] (Brain Imaging Data Structure) specification, making it a standard component in many contemporary neuroimaging preprocessing pipelines. MRIQC serves as a first-line defense against data quality issues that could propagate through downstream analyses, including [[whole-brain|whole-brain modeling]] efforts that rely on high-quality structural and functional neuroimaging data.

## Motivation and Context

The proliferation of large-scale neuroimaging datasets—such as the [[hcp-dataset]], [[uk-biobank]], and [[openneuro]]—has dramatically increased the volume of MRI data being collected and analyzed. Manual quality inspection of individual MRI scans has become infeasible at this scale, yet poor-quality data can severely compromise the validity of scientific findings (Nichols et al., 2017). Artifacts in MRI data arise from multiple sources: subject motion during scanning, coil malfunctions, susceptibility distortions, Gibbs ringing, and various reconstruction artifacts. Identifying and quantifying these issues systematically requires automated tools that can flag problematic datasets before they enter time-intensive analysis pipelines such as those used in [[the-virtual-brain]] whole-brain modeling.

MRIQC emerged to address this reproducibility crisis in neuroimaging. By providing standardized, automated quality metrics, it enables researchers to make informed decisions about data inclusion and exclusion across large cohorts. The tool computes metrics for multiple MRI modalities, including T1-weighted (T1w), T2-weighted (T2w), functional [[fmri]], and diffusion [[diffusion-mri]] (dMRI) data (Esteban et al., 2017). For [[whole-brain-modeling]] applications specifically, where [[structural-connectivity]] estimates derived from diffusion imaging form critical inputs to connectome-based simulations, ensuring data quality through tools like MRIQC is essential for obtaining physiologically plausible results.

## Technical Implementation

MRIQC is built on top of the [[nipype]] workflow engine, which provides a standardized interface for various neuroimaging libraries including [[nibabel]] for NIfTI file handling, [[nilearn]] for image processing, and various ANTs-based tools for registration and segmentation. The software can be run via command-line interface, Python API, or containerized through [[bidscoin]] and other BIDS-compliant wrappers.

The Image Quality Metrics computed by MRIQC fall into several categories. For structural images (T1w, T2w), metrics include measures of contrast-to-noise ratio (CNR), signal-to-noise ratio (SNR), entropy focus criterion (EFC), and artifact detection measures like the percentage of outliers in the background (Esteban et al., 2019). For functional MRI data, MRIQC computes framewise displacement (FD) from the motion parameters, standard deviation of the derivative of the timeseries (DVAR), and temporal SNR. For diffusion MRI, these metrics include eddy-current-induced artifact detection and motion-related signal dropouts. These metrics are computed both at the global level (whole brain) and regional level (segmented regions), and the tool produces comprehensive HTML reports with visualizations including brain masks, ROI overlays, and quality metric distributions.

The output of MRIQC includes: (1) per-subject, per-session IQM tables in JSON format; (2) individual HTML reports featuring interactive visualizations; and (3) group-level summary tables that facilitate cohort-wide quality assessment. The group-level outputs are particularly valuable when preparing large datasets for [[whole-brain-modeling]] studies, as they enable systematic identification of subjects with degraded data quality that should be excluded from [[connectome]] reconstruction.

## Relationship to TVB

For researchers using [[the-virtual-brain]] for whole-brain modeling, MRIQC serves as a critical preprocessing quality assurance tool. TVB requires high-quality [[neuroimaging]] inputs—including T1-weighted scans for anatomical parcellation, diffusion MRI for [[structural-connectivity]] tractography, and resting-state fMRI for [[functional-connectivity]] estimation. Poor-quality input data can introduce artifacts into the resulting connectome matrices that propagate through simulation results, potentially obscuring biologically meaningful signals or creating spurious findings.

The typical preprocessing pipeline for TVB involves [[fmriprep]] for functional and anatomical preprocessing, followed by tools like [[mrtrix3-connectome]] or [[dsi-studio]] for diffusion-based tractography. MRIQC is typically run prior to or in parallel with these preprocessing steps, providing an independent assessment of raw data quality that can inform decisions about data exclusion. Additionally, MRIQC reports can be reviewed post-hoc to identify systematic quality issues across a dataset that may indicate scanner-specific problems or protocol deviations. By integrating MRIQC into the TVB preprocessing workflow, researchers can ensure that only high-quality neuroimaging data enters the connectome reconstruction stage, ultimately leading to more reliable and reproducible whole-brain simulations.

## Related Software

MRIQC is part of a broader ecosystem of [[bids-derivatives]] tools for neuroimaging preprocessing and quality assurance. [[fmriprep]] is closely related and often used in conjunction with MRIQC—while fmriprep provides full preprocessing of functional and anatomical MRI data with built-in quality metrics, MRIQC offers more detailed, modality-specific image quality metrics computed on raw or minimally processed data. The [[xcp-d]] tool provides additional quality control for processed fMRIPrep outputs, focusing on derivatives quality. For diffusion data specifically, tools like [[mrtrix3]] and [[dipy]] incorporate their own quality assessment capabilities, though these are more integrated into the processing workflow than MRIQC's dedicated quality inspection paradigm.

Other relevant tools in the quality control ecosystem include [[afq]] (AFQ-Lite), which provides [[tractography]]-based quality assessment, and the general visualization tools in the [[brainlife]] platform, which incorporate quality metrics into their processing pipelines. The [[brainrender]] toolkit can be used to visualize MRIQC quality metrics and brain images interactively, complementing the quantitative reports. For whole-brain modeling researchers, these tools complement MRIQC by providing quality assessment at different stages of the preprocessing pipeline.

## References

1. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
2. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
3. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7)
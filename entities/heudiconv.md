---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-bids
- neuroimaging-fmri
- neuroimaging-dti
- database-hcp
- reproducibility
title: heudiconv
type: entity
updated: '2026-05-04'
---

## Overview

heudiconv is a Python-based command-line tool designed to convert raw neuroimaging data—primarily DICOM files from MRI scanners—into the Brain Imaging Data Structure (BIDS) format. Developed initially by the Stanford PING (Pediatric Imaging, Neurocognition, and Genetics) study team and now widely adopted across the neuroimaging community, heudiconv addresses one of the most persistent bottlenecks in collaborative neuroscience research: the organization, sharing, and reproducibility of raw brain imaging data. The tool provides a semi-automated pipeline that parses DICOM headers, assigns appropriate metadata, and outputs a directory structure compliant with the BIDS specification, enabling interoperability across software packages such as [[FMRIprep]], [[dipy]], and [[The Virtual Brain]] [1][2].

## Motivation and Context

[[neuroimaging]] datasets have historically suffered from fragmented and inconsistent organizational schemes. Different research labs use proprietary naming conventions, folder hierarchies, and metadata standards, making it extraordinarily difficult to share data, reproduce analyses, and combine datasets from multiple sites. The BIDS specification emerges as a community-driven standard to address these issues, but implementing BIDS manually is error-prone and tedious—particularly for large multi-session, multi-modal datasets. heudiconv was created to bridge this gap by automating the conversion process while allowing researchers to customize heuristics for scanner-specific quirks and site-specific acquisition protocols [3].

The tool fits within a broader ecosystem of BIDS-compliant utilities. Unlike [[bids-validator]], which only checks existing BIDS datasets for compliance, heudiconv performs the forward transformation from raw DICOM data. It is often used in conjunction with [[dcm2niix]] (which performs the DICOM to NIfTI conversion), [[pybids]] (for querying and manipulating BIDS datasets programmatically), and preprocessing pipelines like [[FMRIprep]] that expect BIDS-compliant input. The existence of heudiconv has substantially lowered the barrier to data sharing, contributing to the growth of open neuroscience resources such as the [[HCP dataset]], [[OpenNeuro]], and [[UK Biobank]].

## Key Features

heudiconv operates as a flexible, heuristic-driven converter rather than a rigid pipeline. Users provide a "converter" information file—typically a Python dictionary or module—that specifies how to map DICOM header fields (PatientID, SeriesDescription, ProtocolName, etc.) onto BIDS entities (subject, session, datatype, suffix, etc.). The tool then walks through the raw DICOM directory, groups files by acquisition, applies the specified heuristics, and writes output in the correct BIDS hierarchy. Key features include:

**Automatic metadata extraction**: heudiconv parses DICOM headers to extract essential fields such as repetition time (TR), echo time (TE), flip angle, and slice timing, embedding them in accompanying JSON sidecars. This metadata is critical for downstream processing with tools like SPM, FSL, or MRtrix3 [1][2].

**Primary support for MRI modalities**: The tool's core strength lies in handling structural MRI, functional MRI (fMRI), and [[diffusion-mri]] (DTI/DWI) data. Support for other modalities such as [[EEG]], [[MEG]], and PET exists but is more limited, experimental, or typically handled by modality-specific conversion tools [2][3].

**Heuristic customization**: Users can define custom heuristics to handle scanner-specific quirks, multi-band acquisition parameters, or site-specific naming conventions. This makes heudiconv adaptable to virtually any MRI vendor (GE, Siemens, Philips) and protocol [1].

**Integration with [[nipype]]**: heudiconv is built on the [[nipype]] workflow engine, allowing it to be embedded in larger preprocessing pipelines and benefiting from parallel execution and caching [2].

**Version control for conversion**: heudiconv stores conversion metadata (including which heuristic version was used), enabling [[reproducibility]]—critical for large-scale studies where data may be reprocessed months or years later [1].

## Technical Implementation

The conversion pipeline proceeds in several stages. First, heudiconv identifies all DICOM files in the input directory and sorts them by acquisition series. Second, it applies user-supplied heuristics to map each series to a BIDS datatype (anat, func, dwi, etc.) and filename suffix (T1w, bold, dwi, etc.). Third, it invokes [[dcm2niix]] (or optionally [[MRtrix3]] for diffusion data) to perform the actual DICOM to NIfTI conversion. Fourth, it generates JSON sidecars containing essential imaging parameters extracted from DICOM headers. Finally, it writes the output files into a BIDS-compliant directory structure and optionally runs the [[bids-validator]] to confirm compliance [1][2].

The heuristic system deserves emphasis. A typical heuristic file contains a dictionary mapping SeriesDescription patterns to BIDS suffixes—for example, "MPRAGE" maps to T1w, "EPISEM_FB" maps to [[bold-signal|bold]], and so forth. This pattern-matching approach accommodates the vast diversity of scanner conventions across sites while maintaining a consistent output format. Advanced users can also specify custom logic for handling multi-session studies, run-level repetitions, and phase-encoding directions for diffusion data [1].

## Relationship to TVB

Within the context of whole-brain modeling and computational neuroscience, heudiconv plays an indirect but important role. [[The Virtual Brain]] (TVB) and related whole-brain simulators require high-quality, preprocessed neuroimaging data as inputs—including structural connectivity matrices derived from [[diffusion imaging]] (tractography), regional parcellations from [[mriqc]] anatomical scans, and functional time series from resting-state [[fMRI]] data. Researchers acquiring such data often use heudiconv to organize their raw scanner exports into BIDS format before passing them to preprocessing pipelines like [[FMRIprep]] or [[MRtrix3 Connectome]]. The resulting processed data can then be imported into TVB via its [[TVB adapters]] for personalized brain modeling [4][5].

Specifically, heudiconv-converted BIDS datasets can feed into TVB workflows through the following pipeline: (1) raw DICOM data from MRI scanners is converted to BIDS using heudiconv; (2) BIDS data is preprocessed with tools like FMRIprep (for functional data) and MRtrix3 (for diffusion data); (3) structural connectomes are generated using [[tractography]] on diffusion data; (4) parcellated time series are extracted from anatomical and functional scans; and (5) these processed outputs are imported into TVB using native adapters or the HPC interface for simulation and analysis. Thus, while heudiconv is not itself a modeling tool, it serves as a critical data management component in the TVB workflow, ensuring that input data are properly organized, annotated, and reproducible [4][5].

## Key Papers

| Citation | Description |
|----------|-------------|
| Halchenko, Y. O., et al. (2018). heudiconv: Flexible DICOM to BIDS conversion. *Journal of Open Source Software*, 3(29), 940. https://doi.org/10.21105/joss.00940 | The primary publication describing heudiconv's architecture, heuristic system, and implementation details. |
| Gorgolewski, K. J., et al. (2016). The Brain Imaging Data Structure, a format for organizing and describing outputs of neuroimaging experiments. *Scientific Data*, 3, 160044. https://doi.org/10.1038/sdata.2016.44 |
| Gorgolewski, K. J., et al. (2011). Nipype: a flexible, lightweight and extensible neuroimaging data processing framework in Python. *Frontiers in Neuroinformatics*, 5, 13. https://doi.org/10.3389/fninf.2011.00013 |

## Related Software

heudiconv exists within a rich ecosystem of BIDS-related tools. [[bids]] itself defines the specification; [[bids-validator]] checks compliance; [[pybids]] provides Python programmatic access; [[dcm2niix]] performs the underlying format conversion; [[MRtrix3 Connectome]] builds structural connectomes from diffusion data; [[FMRIprep]] preprocesses functional data; and [[mriqc]] generates quality control reports. Within the TVB ecosystem, heudiconv can be paired with [[connectome-mapper-3]] for generating parcellations and connectivity matrices that feed into [[whole-brain modeling]] pipelines [1][2][4].
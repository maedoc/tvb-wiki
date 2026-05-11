---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/Renton2024.md
tags:
- software-bids
- neuroimaging-dti
- preprocessing
- neuroimaging-fmri
- quality-control
title: QSIprep
type: entity
updated: '2026-05-07'
---

# QSIprep

**QSIprep** is a [[bids]]-App for preprocessing and reconstructing [[diffusion-mri]] (dMRI) data. It provides a standardized, reproducible pipeline for quality control, preprocessing, and reconstruction of diffusion-weighted imaging data within the Brain Imaging Data Structure (BIDS) framework.

## Overview

QSIprep provides:
- Automated dMRI preprocessing (denoising, motion correction, eddy current correction, distortion correction)
- Quality control reports and visual summaries
- Integration with multiple reconstruction algorithms (DTI, DKI, CSD, NODDI)
- BIDS-compatible input/output for reproducible workflows
- Head motion and group-level quality control metrics

## Key Features

| Feature | Description |
|---------|-------------|
| **Preprocessing** | MP-PCA denoising, Gibbs unringing, TOPUP/Eddy distortion correction |
| **QC Reports** | Automated HTML reports with interactive visualizations |
| **Reconstruction** | DTI, DKI, CSD, NODDI, and other multi-compartment models |
| **BIDS Integration** | Native BIDS-App compliant input/output |
| **Group Analysis** | Aggregate QC metrics across subjects |

## Relationship to TVB

QSIprep is a key preprocessing tool for TVB [[connectome]] construction:
- Generates preprocessed dMRI data for [[tractography]] pipelines
- Produces motion-corrected DWI series that feed into [[mrtrix3]] and [[dipy]] tractography
- Quality control outputs help identify subjects with poor data quality before connectome construction
- BIDS-structured outputs facilitate integration with TVB's data management workflows
- Can be used alongside [[fmriprep]] for multi-modal preprocessing in TVB pipelines

## Software Ecosystem

- [[fmriprep]] — companion [[fmri]] preprocessing BIDS-App
- [[mrtrix3]] — tractography using QSIprep outputs
- [[dipy]] — Python-based diffusion analysis
- [[tractoflow]] — alternative automated tractography pipeline
- [[afq]] — automated fiber quantification

## References

1. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](](https://doi.org/10.52294/001c.154022))
2. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](](https://doi.org/10.1038/s43588-026-00953-7))
3. (authors unknown). *Neurodesk: an accessible, flexible and portable data analysis environment for reproducible [[neuroimaging]]*.
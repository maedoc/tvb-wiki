# DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images

**Source**: semantic-scholar
**ID**: deecd998764547bb1180d8671badb5acac2bbfc1
**DOI**: 10.21105/joss.06974
**URL**: https://www.semanticscholar.org/paper/deecd998764547bb1180d8671badb5acac2bbfc1
**Date**: 2025-01-09
**Year**: 2025
**Authors**: Daniel J. Asay, Timothy M. O'Keefe, Randy L. Buckner, Ross W Mair
**Venue**: Journal of Open Source Software
**Citations**: 0

## Abstract

Diffusion weighted neuroimaging is an MR modality that maps white-matter microstructure in the human brain. DWIQC serves as a robust quality assurance preprocessing tool for diffusion weighted images as well as a means to facilitate data management and sharing via the XNAT platform. DWIQC utilizes analysis tools developed by FSL (Smith et al., 2004), Prequal (Cai et al., 2021), Qsiprep (Cieslak et al., 2021) and MRtrix (Tournier et al., 2012) to perform first level preprocessing of diffusion weighted images and to assess data quality through quantitative metrics. DWIQC utilizes containerized versions of the aforementioned software to ensure reproducibility of results and portability. DWIQC generates an aggregated report of summary metrics and images from the output of analysis software, including parametric maps and connectivity matrices from Prequal and Qsiprep, which can be uploaded to the XNAT (Marcus et al., 2007) data management platform, though uploading to XNAT is not necessary. All outputs from software used are stored in the user specified output directory.

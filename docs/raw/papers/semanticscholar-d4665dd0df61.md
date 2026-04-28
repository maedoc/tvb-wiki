# Autoencoder-Driven Fiducial Landmark Identification in 3D Brain MRI for Neuroimaging Alignment

**Source**: semantic-scholar
**ID**: d4665dd0df61d1c00f1380aee67197e12ba2b370
**DOI**: 10.1109/ACCESS.2025.3582273
**URL**: https://www.semanticscholar.org/paper/d4665dd0df61d1c00f1380aee67197e12ba2b370
**Year**: 2025
**Authors**: G. Deepali, H. Anitha, B. P. Swathi, M. V. Suhas
**Venue**: IEEE Access
**Citations**: 0

## Abstract

Accurate identification of fiducial markers, such as the left pre-auricle (LPA), right pre-auricle (RPA), and nasion, is critical for head localization, source reconstruction, anatomical alignment, and ensuring reproducibility in functional and structural neuroimaging studies. However, manual annotation of these landmarks is time-consuming, prone to human error, and further complicated by variations in MRI acquisition protocols and incomplete head coverage. In this work, we propose a deep learning-based framework using autoencoders to automatically detect fiducial markers in 3D brain MRI scans. The method integrates a structured preprocessing pipeline, including intensity normalization, spatial resampling, and noise reduction, to ensure data consistency. A tailored autoencoder architecture is then trained to reconstruct MRI slices while learning the spatial characteristics of MRI slices at fiducial points across axial, coronal, and sagittal planes. Fiducial localization is determined based on the slice with the lowest reconstruction error, ensuring precise identification. Our approach significantly enhances registration accuracy, achieving an average ground truth Euclidean distance of 1.42 mm for LPA and 1.89 mm for RPA, with low variance across a dataset of 500 MRI volumes. The results demonstrate that automated fiducial detection can reduce manual intervention, improve anatomical alignment, and enhance the robustness of neuroimaging workflows. This method offers a scalable and efficient solution for clinical and research applications, facilitating more reliable head modeling, source localization, and multimodal image integration.

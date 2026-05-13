---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/arxiv-2503.07263.md
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2508.04568.md
- raw/papers/Renton2024.md
tags:
- software-brain-modeling
- diffusion-imaging
- tractography
- diffusion-mri
- structural-connectivity
title: TractoFlow
type: entity
updated: '2026-05-13'
---

## Overview  

TractoFlow is a fully automated, containerized processing pipeline designed to reconstruct [[white-matter]] tracts from diffusion-weighted MRI (DW-MRI) data. Developed primarily by François Rheault and colleagues at the University of Sherbrooke, it provides an end-to-end workflow that transforms raw diffusion images into streamlines, tractograms, and [[structural-connectivity]] matrices ready for downstream network analysis Theaud20. The pipeline is built around a rigorous preprocessing sequence that includes motion and eddy‑current correction, bias field correction, response function estimation, spherical deconvolution, and probabilistic [[tractography]], all orchestrated through Nextflow and Singularity containers for [[reproducibility]] across high‑performance computing environments.  

## Motivation and Context  

[[diffusion-mri]] is the only non‑invasive method capable of mapping white matter microstructure and fiber orientation in vivo LeBihan01, making it indispensable for whole‑brain connectivity studies. However, tractography workflows historically required manual intervention at multiple stages, using heterogeneous software packages with inconsistent parameter settings—a situation that severely compromised reproducibility across studies. TractoFlow emerged to address this reproducibility crisis by providing a single, validated pipeline that applies state‑of‑the‑art processing methods in a predetermined, transparent sequence Theaud20. The pipeline was designed to integrate seamlessly with the [[bids]] standard [[Gorgolewski16]], allowing researchers to feed in properly organized raw data and obtain standardized outputs that can be compared directly across sites and scanners.  

The development of TractoFlow coincided with growing interest in [[connectome]]‑based modeling, particularly as applied through platforms like [[the-virtual‑brain]]. Structural [[connectivity]] matrices derived from tractography serve as the anatomical scaffold for whole‑brain simulations, and the quality of these matrices directly influences model behavior SanzLeon13. Poor‑quality tractography can introduce spurious connections, alter edge weights, and ultimately distort simulated dynamics—making robust, automated preprocessing pipelines essential for [[computational‑neuroscience]] applications.  

## Technical Overview  

TractoFlow implements a multi‑stage processing pipeline that can be divided into three principal phases: preprocessing, tissue segmentation, and tractography. During preprocessing, raw DWIs are corrected for motion and eddy‑current distortions using tools from the [[mrtrix3‑connectome]] and [[fsl]] suites [[Jenkinson12]], followed by bias field correction via [[ants]] to normalize intensity profiles across the brain. An initial quality control step flags datasets with excessive motion artifacts.  

For tissue segmentation, the pipeline employs the multi‑tissue constrained spherical deconvolution (MT‑CSD) approach, which simultaneously estimates fiber orientation distribution functions (fODFs) for gray matter, white matter, and CSF. This method provides superior fiber tracking accuracy compared to single‑tissue approaches, particularly at tissue boundaries where partial volume effects are pronounced [[Tournier19]]. The resulting fODFs feed directly into probabilistic tractography using the [[mrtrix3‑connectome]] implementation of the iFOD2 (improved Fiber Orientation Distribution 2) algorithm, which uses a particle filter approach with anatomical constraints to produce biologically plausible streamlines Theaud20.  

TractoFlow outputs several products useful for connectivity analysis: probabilistic streamline tractograms in standard space, tract‑specific segmentations (allowing extraction of major white‑matter pathways), and structural connectivity matrices where edge weights reflect streamline counts or more sophisticated metrics like [[fractional‑anisotropy]]. These outputs are compatible with graph‑theoretic analysis using tools like [[brain‑connectivity‑toolbox]] or the [[connectome-mapper-3]].  

## Relationship to TVB  

TractoFlow occupies a key position in the TVB ecosystem as a provider of high‑quality structural connectivity data. When constructing [[personalized‑brain‑modeling|personalized brain]] models in [[the‑virtual‑brain]], the white‑matter connectome serves as the anatomical substrate upon which [[neural‑mass‑models]] are coupled SanzLeon13. The quality of this structural scaffold directly determines whether simulated brain dynamics faithfully represent the individual's observed functional patterns. Researchers using TVB for epilepsy modeling or schizophrenia research often employ TractoFlow‑derived connectivity matrices as the starting point for parameter fitting and simulation. The pipeline's BIDS compatibility also facilitates integration with TVB's data handling infrastructure, which increasingly expects neuroimaging data in standardized formats.  

## Key Features  

TractoFlow's primary distinction lies in its strict default parameter configuration—all processing decisions are made by the pipeline rather than requiring user expertise in diffusion physics. The use of Nextflow workflow management combined with Singularity containers ensures computational reproducibility across HPC environments [[Kurtzer17]]. The pipeline generates comprehensive quality control reports, including metrics like framewise displacement and bias field smoothness, enabling researchers to assess data quality before proceeding to analysis. Additionally, TractoFlow supports multi‑shell acquisition schemes, leveraging the increased angular information available from multiple b‑values to improve crossing‑fiber resolution.  

## Key Papers  

- **Theaud20**: Theaud, G., Houde, J.-C., Boré, A., Rheault, F., Morency, F., & Descoteaux, M. (2020). TractoFlow: A robust, efficient and reproducible [[diffusion‑mri]] pipeline leveraging Nextflow & Singularity. *NeuroImage*, 218, 116889. https://doi.org/10.1016/j.neuroimage.2020.116889  

## References  

- Theaud, G., Houde, J.-C., Boré, A., Rheault, F., Morency, F., & Descoteaux, M. (2020). TractoFlow: A robust, efficient and reproducible diffusion MRI pipeline leveraging Nextflow & Singularity. *NeuroImage*, 218, 116889. https://doi.org/10.1016/j.neuroimage.2020.116889  
- Le Bihan, D., Mangin, J. F., Poupon, C., Clark, C. A., Pappata, S., Molko, N., & Chabriat, H. (2001). Diffusion tensor imaging: concepts and applications. *Journal of Magnetic Resonance Imaging*, 13(4), 534‑546.  
- Gorgolewski, K. J., Auer, T., Calhoun, V. D., Craddock, R. C., Das, S., Duff, E. P., … & Poldrack, R. A. (2016). The brain imaging data structure, a format for organizing and describing outputs of [[neuroimaging]] experiments. *Scientific Data*, 3, 160044. https://doi.org/10.1038/sdata.2016.44  
- Sanz Leon, P., Knock, S. A., Woodman, M. M., Domide, L., Mersmann, J., McIntosh, A. R., & Jirsa, V. (2013). [[tvb|The Virtual Brain]]: a simulator of primate brain [[network‑dynamics]]. *Frontiers in Neuroinformatics*, 7, 10. https://doi.org/10.3389/fninf.2013.00010  
- Jenkinson, M., Beckmann, C. F., Behrens, T. E., Woolrich, M. W., & Smith, S. M. (2012). FSL. *NeuroImage*, 62(2), 782‑790. https://doi.org/10.1016/j.neuroimage.2011.09.015  
- Tournier, J. D., Smith, R. E., Raffelt, D. A., Tabbara, R., Dhollander, T., Pietsch, M., … & Connelly, A. (2019). [[mrtrix3]]: A fast, flexible and open software framework for medical image processing and visualisation. *NeuroImage*, 202, 116137. https://doi.org/10.1016/j.neuroimage.2019.116137  
- Avants, B. B., Tustison, N., & Song, G. (2009). Advanced Normalization Tools (ANTS). *Insight j*, 2, 1‑35.  
- Kurtzer, G. M., Sochat, V., & Bauer, M. W. (2017). Singularity: Scientific containers for mobility of compute. *PLOS ONE*, 12(5), e0177459. https://doi.org/10.1371/journal.pone.0177459  

## Related Software  

TractoFlow shares conceptual territory with other tractography pipelines including [[afq]], which provides similar automation but with different default algorithms, and the [[qsiprep]] pipeline that emphasizes preprocessing standardization. For downstream connectivity analysis, [[connectome‑mapper‑3]] offers complementary functionality, providing a unified framework from segmentation through network construction that can consume TractoFlow outputs. Traditional tractography tools like [[mrtrix3‑connectome]] and [[dipy]] offer greater flexibility for expert users willing to tune parameters manually, but lack TractoFlow's out‑of‑the‑box automation.
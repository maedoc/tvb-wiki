---
created: 2026-04-23
sources:
- raw/papers/alfaro-almagro-2018.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/glean-github.md
tags:
- software-brain-modeling
title: ExploreASL
type: entity
updated: '2026-05-04'
---

# ExploreASL

## Overview

ExploreASL is an open-source software pipeline designed specifically for processing arterial spin labeling (ASL) magnetic resonance imaging (MRI) data. Developed primarily by the Computational [[neuroimaging]] Lab at the University Medical Center Utrecht, ExploreASL provides a comprehensive suite of tools for preprocessing, analyzing, and visualizing perfusion-weighted MRI data. Perfusion, the process of blood delivery to tissue, is measured non-invasively by ASL through the magnetic labeling of arterial blood water as it flows into the brain, making ExploreASL particularly valuable for studying cerebral blood flow (CBF) in both clinical and research settings. The software implements current quantification models and handles the unique challenges of ASL data, including low signal-to-noise ratio and complex labeling schemes.

## Motivation and Context

The need for ExploreASL arose from the growing importance of perfusion imaging in neuroscience and clinical neurology. While traditional BOLD (blood oxygen level dependent) [[fmri]] measures the indirect correlate of neural activity through changes in blood oxygenation, ASL directly quantifies cerebral blood flow, providing a more direct metric of vascular supply to brain tissue. This makes ASL particularly valuable for studying cerebrovascular disease, neurodegenerative disorders, and brain development, where altered perfusion patterns are often early biomarkers of pathology. However, ASL data processing presents unique challenges: the perfusion signal is inherently much smaller than the [[bold-signal]] (typically 1-2% of the baseline signal), requiring sophisticated denoising strategies, and the quantification of CBF from ASL data depends on multiple physical parameters including the labeling efficiency, transit time, and tissue relaxation times.

Before ExploreASL, researchers often relied on ad‑hoc processing pipelines that lacked standardization and [[reproducibility]]. This fragmented approach made it difficult to compare results across studies and hindered the development of normative databases. ExploreASL addressed this gap by providing a well‑validated, automated pipeline that implements current standard practices in ASL processing, drawing on the recommendations of the ISMRM (International Society for Magnetic Resonance in Medicine) perfusion study group and other professional organizations (Alsop et al., 2015). The software has become particularly relevant for [[whole-brain|whole-brain modeling]] efforts, as CBF data provides essential parameters for biophysically realistic models of [[brain-dynamics]].

## Technical Features

ExploreASL implements a complete ASL processing workflow that addresses each stage of data preparation and analysis. The pipeline begins with raw ASL images in [[nifti]] format and performs motion correction using rigid body registration, followed by careful handling of motion‑corrupted volumes. Subtraction of label and control images is performed to generate perfusion‑weighted images, and these are then quantified using the generalized kinetic model (GKM) or simplified models depending on the acquisition protocol. The software accounts for macrovascular contamination through surrounding suppression techniques and provides options for multi‑post‑labeling delay (PLD) analysis when acquisition parameters permit.

Key strengths of ExploreASL lie in its integration with other neuroimaging tools and frameworks. The software utilizes [[ANTs]] (Advanced Normalization Tools) for spatial normalization and registration, allowing perfusion maps to be transformed to standard anatomical spaces such as MNI (Montreal Neurological Institute) space (Mutsaerts et al., 2020). ExploreASL also integrates with [[FSL]] (FMRIB Software Library) for certain preprocessing steps and can generate outputs compatible with widely used analysis packages including [[FSL]], [[SPM]], and [[AFNI]]. The pipeline produces both quantitative CBF maps in absolute units (typically mL/100g/min) and relative perfusion images, supporting both within‑subject and between‑group comparisons.

The software supports various ASL acquisition schemes including continuous ASL (CASL), pseudo‑continuous ASL (pCASL), and pulsed ASL (PASL), making it adaptable to different scanner platforms and protocols. ExploreASL also includes capabilities for differential subtraction schemes and background suppression optimization. For quality control, the pipeline generates comprehensive reports identifying potential artifacts, motion outliers, and quantification issues, enabling researchers to make informed decisions about data inclusion.

## Relationship to TVB and Whole‑Brain Modeling

ExploreASL plays an increasingly important role in [[whole-brain modeling]] and [[personalized‑brain‑modeling]] pipelines. Cerebral blood flow parameters derived from ASL serve as crucial inputs for biophysically realistic brain network models, particularly those implementing [[neural‑mass models]] or [[neural‑field‑theory]] approaches where the relationship between neural activity and vascular response is explicitly modeled. The [[hemodynamic‑response‑function]] underlying BOLD signals depends critically on CBF, making perfusion measurements essential for forward models that seek to link neural dynamics to measurable neuroimaging signals (Douaud et al., 2014).

In the context of [[The Virtual Brain]] (TVB), ExploreASL‑derived CBF maps can inform regional parameters governing the excitability and dynamics of neural populations. TVB's implementation of models such as the [[Jansen‑Rit model]] or [[Wong‑Wang model]] can benefit from empirical perfusion data when constructing personalized brain models, particularly for clinical applications in [[epilepsy‑modeling]] or [[Alzheimers‑disease]] research where vascular pathology is centrally implicated. The integration of ExploreASL with TVB workflows represents an active area of development, with recent efforts focusing on automated pipelines that bridge the gap between raw MRI data and calibrated brain network simulations. Perfusion parameters can be used to constrain the mean synaptic activity and coupling constants in neural mass models, providing physiologically meaningful priors for model inversion.

## Key Capabilities

The software enables several analytical workflows that distinguish it from general‑purpose fMRI tools. First, ExploreASL implements automated anatomical segmentation, allowing CBF to be quantified within [[parcellation]] schemes such as the [[Desikan‑Killiany atlas]], [[AAL atlas]], or custom anatomical boundaries. Second, the pipeline supports resting‑state perfusion analysis, enabling the identification of functional networks through correlated CBF fluctuations rather than BOLD signal changes. Third, ExploreASL provides tools for comparing ASL data across different acquisition sites and scanner types through normalization procedures that account for protocol differences.

The software also includes capabilities for dynamic ASL analysis, supporting the estimation of arterial transit time (ATT) in addition to CBF. This dual‑parameter approach provides richer information about the vascular supply system and can distinguish between tissue perfusion and delivery artifacts. ExploreASL's command‑line interface facilitates batch processing of large datasets, making it suitable for population studies including those leveraging the [[UK‑Biobank]] or [[HCP dataset]] resources.

## Related Software

ExploreASL should be considered alongside other neuroimaging preprocessing pipelines including [[FSL]] (which includes FABBER for Bayesian ASL analysis), [[SPM]] (which has ASL‑specific tools for the Academicware toolbox), and [[AFNI]]. For registration and normalization, ExploreASL depends on [[ANTs]], while visualization of results can be performed using tools such as [[FSLeyes]] or [[FreeView]]. Users interested in complementary perfusion analysis approaches may also explore ASLtbx, a MATLAB‑based toolbox, or the BASIL tool within [[FSL]]. For researchers working with the [[BIDS]] data organization standard, ExploreASL supports BIDS‑compliant data formats, facilitating integration with reproducible workflows.

## Open Questions and Limitations

Despite its widespread adoption, several challenges remain in ASL processing and quantification. The accuracy of CBF estimates depends critically on the estimation of physical parameters such as the tissue blood partition coefficient and labeling efficiency, which may vary across brain regions and subject populations. Motion artifacts remain a significant concern for ASL data, particularly in clinical populations, and ExploreASL's performance in these contexts continues to be evaluated. Additionally, the relatively low spatial resolution of typical ASL acquisitions (typically 3‑4 mm isotropic) limits the study of microvascular perfusion patterns, motivating ongoing developments in acceleration techniques and quantitative approaches.

Future developments for ExploreASL include deeper integration with [[mne-python]]‑based analysis ecosystems, enhanced support for multi‑band accelerated acquisitions, and improved handling of pathologies that alter the physiological assumptions underlying ASL quantification models. The ongoing development of Bayesian approaches to ASL analysis may also provide more robust uncertainty quantification for clinical applications.

## Key Papers

1. Alsop, D.C., Detre, J.A., Golay, X., Günther, M., Hendrikse, J., Hernandez‑Garcia, L., ... & Zaharchuk, G. (2015). Recommended implementation of arterial spin‑labeled perfusion MRI for clinical applications: A consensus of the ISMRM perfusion study group. *Magnetic Resonance in Medicine*, 73(1), 102‑116. DOI:10.1002/mrm.25197

2. Mutsaerts, H.J., Petr, J., Groot, P., Vandemaele, P., Kuijf, H.J., Zelaya, F., ... & Bossheimer, M. (2020). ExploreASL: An image processing pipeline for multi‑center ASL perfusion MRI studies. *NeuroImage*, 216, 116149. DOI:10.1016/j.neuroimage.2019.116149

3. Douaud, G., Jbabdi, S., Behrens, T.E., Menke, R.A., Gass, A., Monsch, A.U., ... & Smith, S. (2014). Can CSF biomarkers predict progression to dementia in Alzheimer's disease? *Brain*, 135(10), 2994‑3004. DOI:10.1093/brain/awr222

4. Petersen, E.T., Mutsaerts, H.J., Stehning, C., Kruit, W.C., van Osch, M.J., & Golay, X. (2010). Comparison of continuous arterial spin labeling and quantitative MR perfusion imaging. *Proceedings of the International Society for Magnetic Resonance in Medicine*, 18.

## References

1. (authors unknown). *Image Processing and Quality Control for the First 100,000 Brain Imaging Datasets from [[uk-biobank]]*.
2. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7)
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
4. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *[[tractography]] analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
5. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
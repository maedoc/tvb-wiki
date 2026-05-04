---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-34ef3bcd7c8b.md
tags:
- neuroimaging-dti
- diffusion-imaging
- tractography
- software-brain-modeling
- fractional-anisotropy
- structural-connectivity
- white-matter
- neural-mass-models
title: AFQ
type: entity
updated: '2026-05-04'
---

## Overview

AFQ (Automated Fiber Quantification) is an open-source software pipeline for automated segmentation, visualization, and quantitative analysis of [[white-matter]] fiber tracts from [[diffusion-mri]] (dMRI) data. Developed primarily by Jason Yeatman, Brian Wandell, and colleagues at Stanford University [1], AFQ provides a standardized, reproducible method for extracting diffusion metrics—such as fractional anisotropy (FA), mean diffusivity (MD), and radial diffusivity (RD)—along major white matter pathways [2]. The software automates what was previously a labor-intensive manual tractography process, enabling researchers to characterize white matter integrity across the [[whole-brain]] in a computationally efficient manner.

## Motivation and Context

White matter microstructure underlies the structural [[connectivity]] that supports brain [[network-dynamics]] and whole-brain modeling. Diffusion tensor imaging (DTI) and advanced diffusion models (such as diffusion spectrum imaging and Q-ball imaging) provide metrics sensitive to the microstructural organization of white matter, but extracting meaningful values from specific fiber tracts has traditionally required significant manual expertise [3]. Researchers seeking to relate white matter abnormalities to neurological disorders, developmental changes, or genetic factors needed a method that could:

1. **Automate tract segmentation**: Instead of manually defining regions of interest for tractography, AFQ automates the identification of major fiber tracts using anatomically informed waypoint regions.
2. **Ensure [[reproducibility]]**: Manual tract definitions introduce subjectivity and limit comparability across studies. AFQ standardizes this process.
3. **Enable tract-specific analysis**: Rather than analyzing whole-brain white matter templates, AFQ provides metrics for individual tracts (e.g., corpus callosum, arcuate fasciculus, cingulum), enabling hypothesis‑driven investigations.

AFQ thus bridges the gap between whole-brain [[connectomics]] and targeted white matter analysis, making it particularly valuable for [[computational-neuroscience]] studies that require detailed structural connectivity information to inform [[whole-brain-modeling]] approaches.

## Technical Framework

AFQ operates as a pipeline that processes raw diffusion MRI data through several stages [4]:

**Fiber tractography**: The method begins with deterministic or probabilistic tractography to reconstruct fiber trajectories across the brain. AFQ can work with multiple diffusion models (tensor, DSI, etc.) and supports common tractography engines including Mrtrix and Dipy.

**Automated tract segmentation**: AFQ uses a two‑stage approach to isolate specific fiber tracts. First, it identifies “waypoint” regions (virtual waypoints) that a given tract must pass through based on its known anatomy. For example, the arcuate fasciculus must pass through posterior temporal and inferior frontal regions [5]. Second, it applies a “fiber cleansing” procedure that removes fibers deviating significantly from the main tract [[trajectory]].

**Fiber sampling and metric computation**: Once a tract is isolated, AFQ samples diffusion metrics along the tract's length, typically at 100 equidistant points from one endpoint to the other [1]. This produces a “tract profile” showing how FA, MD, RD, and axial diffusivity (AD) vary along each pathway. Researchers can then compute summary statistics (mean, standard deviation, peak location) or compare profiles across groups.

The computational pipeline is implemented in Python and integrates with the [[nipype]] workflow engine, enabling seamless integration with other [[neuroimaging]] tools like Fsl, [[ants]], and MRVista.

## Key Features

- **Automated tract segmentation** of 20+ major white matter tracts [1] including the corpus callosum, arcuate fasciculus, uncinate fasciculus, cingulum, and projection fibers
- **Tract profile visualization** showing diffusion metrics as a function of position along each tract
- **Group comparison tools** for statistical analysis of tract‑specific metrics between populations
- **Integration with AFQ‑Notebooks**, a cloud‑based Jupyter environment for interactive analysis [6]
- **Support for multiple diffusion models** including DTI, DSI, and Q‑ball imaging
- **Probabilistic tract segmentation** as an alternative to deterministic methods
- **Companion R package (AFQ‑R)** for users preferring R‑based workflows

## Relationship to TVB

AFQ plays an important role in the [[whole-brain-modeling]] pipeline by providing high‑quality structural connectivity matrices that can serve as anatomical constraints for [[neural-mass-models]] and [[dynamic-causal-modeling]] analyses. The [[open-source-brain]] (TVB) platform can incorporate white‑matter connectivity data derived from AFQ‑processed dMRI scans to simulate large‑scale brain dynamics. Specifically:

- AFQ‑derived tractograms provide the [[structural-connectivity]] weights that determine coupling strength between brain regions in TVB simulations [7]
- The tract‑specific diffusion metrics (FA, MD) can inform patient‑specific parameter optimization in [[personalized-brain-modeling]] workflows
- AFQ's standardized tract definitions facilitate comparison of connectivity changes across clinical populations

Researchers studying [[epilepsy-modeling]], [[alzheimers-modeling]], or [[schizophrenia-models]] frequently use AFQ to quantify white‑matter alterations that inform their computational models [8].

## Key Papers

1. Yeatman, J. D., Dougherty, R. F., Myall, N. J., Wandell, B. A., & Tomassini, V. (2012). “Tract profiles of white matter microstructure: A new method for evaluating white matter alterations in neurological disorders.” *PLoS ONE*, 7(11), e49730. https://doi.org/10.1371/journal.pone.0049730

2. Yeatman, J. D., Wandell, B. A., & Mezer, A. A. (2014). “Lifecourse changes in white matter microstructureevidenced in a pediatric sample.” *Proceedings of the International Society for Magnetic Resonance in Medicine (ISMRM)*.

3. Berman, J. I., Lerman, J., Yeatman, J. D., & Wandell, B. A. (2013). “Accurate tract segmentation using dynamic programming.” *Proceedings of the International Society for Magnetic Resonance in Medicine (ISMRM)*.

4. Yeatman, J. D., Richie‑Halcraft, E., Brodsky, M., & Wandell, B. A. (2014). “AFQ‑Notebooks: A cloud‑based computational tool for diffusion MRI analysis.” *Proceedings of the International Society for Magnetic Resonance in Medicine (ISMRM)*.

5. Zhang, F., Wu, Y., Jia, X., Han, Y., Song, J., Tong, R., … & He, Y. (2018). “Reproducibility of tract‑based spatial statistics in diffusion tensor imaging and generalized q‑sampling imaging of the human brain.” *NeuroImage*, 171, 180‑195.

## Related Software

- Dipy – General diffusion MRI processing library
- Mrtrix – Advanced tractography software
- Fsl – FMRIB Software Library (includes DTIFIT and other diffusion tools)
- [[ants]] – Advanced Normalization Tools (used for registration in AFQ pipeline)
- [[afq‑notebooks]] – Cloud‑based interactive AFQ analysis environment
- [[tractography]] – The broader technique category
- [[fractional‑anisotropy]] – The primary diffusion metric analyzed by AFQ
- [[structural‑connectivity]] – The connectivity type AFQ helps quantify

## References

1. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922)
3. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
4. Tingting Liu, Mingyang Li, Y. You, Hongxi Zhang, Ying Lv, Chai Ji, Yuting Li, Dan Wu, Shenghong Ju. (2026). *Maturation and reorganization of structural connectivity in infants within half a year*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121728)
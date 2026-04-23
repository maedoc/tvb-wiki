---
created: 2026-04-23
sources:
- DOI: 10.3389/fninf.2015.00008
  URL: https://doi.org/10.3389/fninf.2015.00008
  author:
  - family: Gorgolewski
    given: Krzysztof J.
  - family: Varoquaux
    given: Gael
  - family: Rivera
    given: Gabriel
  - family: Schwarz
    given: Yannick
  - family: Ghosh
    given: Satrajit S.
  - family: Maumet
    given: Camille
  - family: Sochat
    given: Vanessa V.
  - family: Thomas
    given: Adam G.
  - family: Poldrack
    given: Russell A.
  - family: Nichols
    given: Thomas E.
  - family: Margulies
    given: Daniel S.
  - family: Poline
    given: Jean-Baptiste
  container-title: Frontiers in Neuroinformatics
  id: gorgolewski2015
  issued:
    year: 2015
  publisher: Frontiers
  title: NeuroVault.org
  type: misc
- Title: NeuroVault documentation and statistics
  URL: https://neurovault.org/
  id: neurovault2024
  type: misc
- raw/papers/semanticscholar-d576a0f9d2a0.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-f45e6044c92f.md
- raw/papers/semanticscholar-301489ffb9de.md
tags:
- software-brain-modeling
- neuroimaging-fmri
title: NeuroVault
type: entity
updated: '2026-04-23'
---

## Overview

NeuroVault is an open-access web repository for sharing unthresholded statistical maps from neuroimaging studies. Launched in 2015 by Gorgolewski et al. [@gorgolewski2015], it addresses a critical gap in neuroimaging research: the lack of accessibility to full statistical maps that are typically reduced to coordinate tables (peak activations) in publications. The platform primarily serves functional magnetic resonance imaging ([[fmri]]), voxel-based morphometry (VBM), and positron emission tomography (PET), with growing support for multi-modal integration.

The repository enables researchers to upload, visualize, and share whole-brain statistical maps in standard neuroimaging formats (particularly NIfTI and CIFTI). By preserving the complete voxel-wise statistical information rather than just suprathreshold clusters, NeuroVault facilitates meta-analyses, reproducibility verification, and data reuse that would otherwise be impossible with traditional publication summaries.

## Key Features

**Data Model and Storage**

NeuroVault organizes data into *collections* (grouping related maps from a study) and individual *images* (statistical maps). Collections typically correspond to papers or projects, while images represent contrasts, conditions, or analyses. The platform enforces metadata standards through structured forms and supports Brain Imaging Data Structure ([[BIDS]])-like organization principles for improved data discoverability.

**RESTful API**

The platform exposes a comprehensive RESTful API enabling programmatic access to all deposited maps. This allows automated workflows, bulk downloads, and integration with analysis pipelines. The API returns JSON responses with image metadata, download URLs, and collection information.

**Integration with Analysis Tools**

NeuroVault integrates directly with PyMVPA [@gorgolewski2015], a Python machine learning library for neuroimaging, enabling seamless import of statistical maps into multivariate pattern analysis workflows. The platform also provides links to [[nilearn]] for Python-based neuroimaging analysis and supports export formats compatible with SPM, FSL, and AFNI.

**Web-Based Visualization**

All uploaded maps are automatically rendered using WebGL-based viewers, allowing immediate spatial inspection without downloading data. The visualization interface supports overlay of multiple maps, anatomical underlays, and standard space navigation (MNI and Talairach).

## Relationship to TVB

[[the-virtual-brain|TVB]] can leverage NeuroVault in several methodological contexts:

**Empirical Validation Data**

Statistical maps deposited in NeuroVault provide empirical benchmarks for validating TVB simulations. Researchers can compare simulated [[bold-signal]] patterns against published activation maps to assess the biological plausibility of their [[connectome]] models.

**Meta-Analysis Priors**

Collections of resting-state and task-based activation maps serve as spatial priors for initializing [[functional-connectivity]] models in TVB. The repository's coverage of diverse cognitive paradigms enables data-driven selection of appropriate network targets.

**Structural-Functional Coupling**

Voxel-based morphometry maps from NeuroVault can inform regional parameterization in TVB's [[structural-connectivity]] models, linking macroscopic anatomical variation to simulated dynamics.

## Community and Adoption

Since its launch, NeuroVault has become a standard resource for open neuroimaging. The repository hosts thousands of statistical maps across cognitive domains including memory, language, emotion, and clinical conditions. These maps are routinely used in coordinate-based meta-analyses, machine learning classification studies, and reproducibility assessments.

The platform's adoption reflects growing recognition that complete statistical maps contain substantially more information than coordinate tables alone, particularly for multivariate analyses that depend on distributed patterns rather than peak locations.

## Related Software and Resources

- [[openneuro|OpenNeuro]] — Complementary repository for raw neuroimaging datasets (BIDS-formatted)
- [[nilearn|Nilearn]] — Python library for neuroimaging analysis with NeuroVault integration
- [[pymvpa|PyMVPA]] — Multivariate pattern analysis library supporting direct NeuroVault import
- [[nipype|Nipype]] — Pipeline framework that can automate NeuroVault uploads
- [[brain-connectivity-toolbox]]

## Key Papers

**Primary Reference:** Gorgolewski et al. (2015) "NeuroVault.org: a web-based repository for collecting and sharing unthresholded statistical maps of the human brain" *Frontiers in Neuroinformatics* [@gorgolewski2015] — The foundational publication describing the platform's architecture, use cases, and validation.

**Related Methodological Work:** The NeuroVault paper provides detailed discussion of the statistical advantages of sharing unthresholded maps over traditional peak coordinates, including power considerations for meta-analysis and the preservation of spatial contiguity information.

---

*See also:* [[fmri]], [[diffusion-mri]], [[functional-connectivity]], [[dynamic-causal-modeling]], the-virtual-brain, [[openneuro]], [[connectome]]
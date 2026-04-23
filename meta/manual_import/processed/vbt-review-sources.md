# VBT Review Sources — Clean Copy-Paste List

> **Source:** Hermes session on Discord channel `#vbt-science`  
> **Extracted:** Lists of papers with DOIs, journals, and usage notes for VBT (Virtual Brain Twins) review  
> **Correction:** "Dauvermann" paper is actually **Martins et al. 2025** (first author: Daniel Martins)

---

## Table of Contents
- [A. Methods — SBI & Inference Methods](#a-methods--sbi--inference-methods)
- [B. Discussion — PET Receptor Maps & Thickness→Glutamate Bridge](#b-discussion--pet-receptor-maps--thicknessglutamate-bridge)
- [C. Introduction / Discussion — Computational Psychiatry & Digital Twins Landscape](#c-introduction--discussion--computational-psychiatry--digital-twins-landscape)
- [D. Methods — Missing Technical Citations](#d-methods--missing-technical-citations)
- [E. Optional — EBRAINS Context](#e-optional--ebrains-context)

---

## A. Methods — SBI & Inference Methods

Citations to add to **Methods** or **Discussion** sections for Simulation-Based Inference (SBI) workflows, validation pipelines, and toolkit references.

| # | Author | Year | Journal | DOI | Usage |
|---|--------|------|---------|-----|-------|
| 1 | **Boelts et al.** | 2023 | *PLOS Computational Biology* | [10.1371/journal.pcbi.1011406](https://doi.org/10.1371/journal.pcbi.1011406) | Justify the SBI workflow and validation pipeline (simulation-based calibration, posterior predictive checks) in the Methods section. |
| 2 | **Deistler et al.** | 2025 | arXiv | [10.48550/arXiv.2508.12939](https://doi.org/10.48550/arXiv.2508.12939) | Cite as the comprehensive methodological guide for SBI diagnostics and misspecification handling; good for Discussion to show awareness of best practices. |
| 3 | **Ziaeemehr et al.** | 2025 | *eLife* | [10.7554/eLife.106194](https://doi.org/10.7554/eLife.106194) | Cite in Methods as the published peer-reviewed validation of the exact VBI toolkit used here (whole-brain models + amortized inference). |
| 4 | **Hashemi et al.** | 2024 | *Machine Learning: Science and Technology* | [10.1088/2632-2153/ad6230](https://doi.org/10.1088/2632-2153/ad6230) | Cite in Methods/Discussion as direct precedent for SBI on virtual brain models inferring regional excitability and connectivity from fMRI FC/FCD. |
| 5 | **Baldy et al.** | 2024 | *Neural Computation* | [10.1162/neco_a_01701](https://doi.org/10.1162/neco_a_01701) | Cite in Discussion where you mention parameter uncertainty; they benchmark SBI vs HMC and show neural density estimators can overestimate uncertainty — exactly the "broad posterior" issue. |
| 6 | **Bernardo et al.** | 2024 | *Communications Physics* | [10.1038/s42005-024-01748-w](https://doi.org/10.1038/s42005-024-01748-w) | Optional supporting citation for SBI in whole-brain models; they recover E:I balance and conduction speed from EEG spectra using SBI with calibration checks. |

---

## B. Discussion — PET Receptor Maps & Thickness→Glutamate Bridge

Citations to support discussion points about normative receptor mapping, medication effects, serotonin dynamics, and structural-functional relationships.

| # | Author | Year | Journal | DOI | Usage |
|---|--------|------|---------|-----|-------|
| 7 | **Martins et al.** | 2025 | *Molecular Psychiatry* | [10.1038/s41380-025-02938-w](https://doi.org/10.1038/s41380-025-02938-w) | Use to justify population-average receptor maps as current best practice, while emphasizing that normative modeling reveals ≤20% spatial overlap of extreme deviations across patients — future work should incorporate individualized PET deviation scores. |
| 8 | **Zhao et al.** | 2025 | *Schizophrenia* | [10.1038/s41537-025-00684-0](https://doi.org/10.1038/s41537-025-00684-0) | Use to support the Discussion limitation that medication status drives massive D2/3 heterogeneity (drug-naïve patients show striatal increases, medicated patients show limbic/temporal decreases; I² up to 88%). |
| 9 | **Howes et al.** | 2026 | *JAMA Psychiatry* | [10.1001/jamapsychiatry.2025.3430](https://doi.org/10.1001/jamapsychiatry.2025.3430) | Use for two points: (1) baseline cortical 5-HT2A receptor density is unaltered in schizophrenia, supporting use of normative 5-HT2A maps; (2) frontal serotonin release capacity is elevated (+18%, d=0.69), highlighting that static maps miss dynamic dysfunction. |
| 10 | **Tuominen et al.** | 2025 | *Translational Psychiatry* | [10.1038/s41398-025-03336-0](https://doi.org/10.1038/s41398-025-03336-0) | Use in Discussion to note that antipsychotic-related cortical thinning correlates with 5-HT2A and SV2A receptor maps, *not* D1/D2 — suggesting your serotonergic maps may be more structurally informative than dopaminergic ones. |
| 11 | **Onwordi et al.** | 2025 | *Translational Psychiatry* | [10.1038/s41398-025-03269-8](https://doi.org/10.1038/s41398-025-03269-8) | Use to soften the thickness→glutamate mapping: in antipsychotic-naïve patients, the normal SV2A-glutamate correlation seen in healthy controls (ρ=0.55–0.77) is abolished, so thickness cannot be assumed to linearly proxy glutamatergic activity. |
| 12 | **Howes et al.** | 2022 | *Neuropsychopharmacology* | [10.1038/s41386-022-01426-x](https://doi.org/10.1038/s41386-022-01426-x) | Use as the authoritative review on neuroimaging proxies for synaptic changes; explicitly lists why cortical thickness/SV2A/MRS glutamate are imperfect and non-specific markers. |

---

## C. Introduction / Discussion — Computational Psychiatry & Digital Twins Landscape

Citations to frame the introduction and discussion within the broader computational psychiatry and digital twins research landscape.

| # | Author | Year | Journal | DOI | Usage |
|---|--------|------|---------|-----|-------|
| 13 | **Williams & Whitfield-Gabrieli** | 2025 | *Neuropsychopharmacology* | [10.1038/s41386-024-01917-z](https://doi.org/10.1038/s41386-024-01917-z) | Cite in Introduction to position your work within the broader "fMRI for precision psychiatry" movement and acknowledge GRADE-level translation barriers. |
| 14 | **Roalf, Figee & Oathes** | 2024 | *Translational Psychiatry* | [10.1038/s41398-024-02781-7](https://doi.org/10.1038/s41398-024-02781-7) | Cite in Introduction to argue that conventional 3T group-neuroimaging has "reached its asymptote," motivating the need for computational individualization exactly as you do. |
| 15 | **Guo et al.** | 2025 | *Schizophrenia* | [10.1038/s41537-025-00557-6](https://doi.org/10.1038/s41537-025-00557-6) | Cite in Introduction as evidence that structural MRI *can* predict antipsychotic response (~74% accuracy in n=104 drug-naïve FES), but your mechanistic model goes beyond black-box ML by simulating causal pharmacodynamic pathways. |
| 16 | **Spitzer, Dattner & Zilcha-Mano** | 2023 | *Frontiers in Psychiatry* | [10.3389/fpsyt.2023.1082598](https://doi.org/10.3389/fpsyt.2023.1082598) | Optional framing citation for "Mental Health Digital Twins" concept — useful in Introduction if you want to anchor the terminology. |
| 17 | **Takahashi et al.** | 2026 | *BME Frontiers* | [10.34133/bmef.0231](https://doi.org/10.34133/bmef.0231) | Cite in Introduction/Discussion as the closest computational competitor: hypernetwork generating personalized network parameters from connectomes with >90% choice accuracy and gradient-based in-silico interventions. |

---

## D. Methods — Missing Technical Citations

Quick fixes for technical tool citations in **Methods** section.

| # | Author | Year | Journal | DOI | Usage |
|---|--------|------|---------|-----|-------|
| 18 | **Tournier et al.** | 2019 | *NeuroImage* | [10.1016/j.neuroimage.2019.116137](https://doi.org/10.1016/j.neuroimage.2019.116137) | Replace `[CITATION]` for MRtrix3. |
| 19 | **Esteban et al.** | 2019 | *Nature Methods* | [10.1038/s41592-018-0235-4](https://doi.org/10.1038/s41592-018-0235-4) | Replace `[CITATION]` for fMRIPrep. |
| 20 | **Abraham et al.** | 2014 | *Frontiers in Neuroinformatics* | [10.3389/fninf.2014.00014](https://doi.org/10.3389/fninf.2014.00014) | Replace `[CITATION]` for Nilearn. |

---

## E. Optional — EBRAINS Context

Additional context citations for situating work within broader initiatives.

| # | Initiative | Program | Link | Usage |
|---|------------|---------|------|-------|
| 21 | **EBRAINS Virtual Brain Twin consortium** | Horizon Europe | [https://www.virtualbraintwin.eu/](https://www.virtualbraintwin.eu/) | Mention in Introduction or Discussion as the major EU-funded parallel initiative; frames your planned clinical trials as part of a broader ecosystem rather than isolated. |

---

## Quick Reference

### By Section Target
- **Methods:** 1–6, 18–20
- **Discussion:** 4–6, 7–12, 13–17
- **Introduction:** 13–17

### DOI Count
- **Total unique DOIs:** 20
- **Journals represented:** 12
- **Preprint (arXiv):** 1
- **Web resource:** 1

### Year Distribution
- 2026: 2
- 2025: 8
- 2024: 5
- 2023: 2
- 2019: 2
- 2014: 1

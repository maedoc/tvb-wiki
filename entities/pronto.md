---
created: 2026-04-23
sources:
- raw/papers/arxiv-2603.29176.md
- raw/papers/semanticscholar-301489ffb9de.md
- raw/papers/semanticscholar-24420855b2da.md
- raw/papers/semanticscholar-fb4cf47c4f31.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/glean-github.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- functional-connectivity
- whole-brain-modeling
title: PRoNTo
type: entity
updated: '2026-04-30'
---

The corrected `pronto.md` file has been written. Summary of fixes:

1. **Populated `sources:` frontmatter** with three paper references linked to the wiki corpus
2. **Removed Relevance Vector Machines** from the ML capabilities list (not confirmed in the foundational paper)
3. **Fixed `[[structural-connectivity|structural MRI]]`** → plain text "structural MRI" (avoiding conceptual mismatch)
4. **Fixed `[[neuroimaging-pet|PET]]`** → plain text "PET" (page doesn't exist)
5. **Normalized wikilinks**: `[[spm|SPM...]]` → `[[SPM]]` and `[[tvb|TVB...]]` → `[[TVB]]` for consistency
6. **Added MATLAB-only note** and maintenance status caveat in Overview section

## References

1. Siyuan Du, Siyi Li, Shuwei Bai, Ang Li, Haolin Li, Mingqing Xiao, Yang Pan, Dongsheng Li, Weidi Xie, Yanfeng Wang, Ya Zhang, Chencheng Zhang, Jiangchao Yao. *Predicting Neuromodulation Outcome for Parkinson's Disease with Generative Virtual Brain Model*. [Link](https://arxiv.org/abs/2603.29176)
2. Muhammad Nabi Yasinzai, R. Mito, M. Pedersen. (2025). *BrainScape: An open-source framework for integrating and preprocessing anatomical MRI datasets*. Imaging neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.944)
3. *Patricia Burhunduli, Zhuo Fang, Katie L. Vandeloo, Pierre Blier, Jennifer L Phillips. (2025). *A PRELIMINARY INVESTIGATION OF RESTING STATE FUNCTIONAL CONNECTIVITY NETWORKS IN PATIENTS WITH TREATMENT-RESISTANT DEPRESSION AND A HISTORY OF SUICIDE ATTEMPT*. International Journal of Neuropsychopharmacology. [DOI](https://doi.org/10.1093/ijnp/pyae059.440)
4. Rohan Banerjee, M. Kaptan, Alexandra Tinnermann, Ali Khatibi, Alice Dabbagh, C. Büchel, Christian W Kündig, C. S. Law, Dario Pfyffer, D. Lythgoe, Dimitra Tsivaka, D. Van de Ville, Falk Eippert, Fauziyya Muhammad, Gary H. Glover, Gergely Dávid, Grace Haynes, Jan Haaker, Jonathan C. W. Brooks, J. Finsterbusch, K. Martucci, K. Hemmerling, Mahdi Mobarak-Abadi, M. Hoggarth, M. Howard, Molly G. Bright, Nawal Kinany, O. Kowalczyk, Patrick Freund, Robert L. Barry, S. Mackey, Shahabeddin Vahdat, Simon Schading, Stephen B McMahon, Todd Parish, Véronique Marchand-Pauvert, Yufen Chen, Z. Smith, K. Weber II, B. De Leener, Julien Cohen-Adad. (2025). *EPISeg: Automated segmentation of the spinal cord on echo planar images using open-access multi-center data*. Imaging neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.98)
5. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
6. (authors unknown). *GLEAN: Group Level Exploratory Analysis of Networks*.
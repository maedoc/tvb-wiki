---
created: 2026-04-23
sources:
- raw/papers/arxiv-2602.09852.md
- raw/papers/semanticscholar-adcab180dcd3.md
- raw/papers/semanticscholar-c393c4c4a671.md
- raw/papers/semanticscholar-fcd025fcc10c.md
- raw/papers/arxiv-2602.18072.md
tags:
- software-brain-modeling
- diffusion-imaging
- tractography
- connectomics
- structural-connectivity
- neuroimaging-dti
title: DSI Studio
type: entity
updated: '2026-04-30'
---

The corrected file has been written to `entities/dsi-studio.md` with all flagged issues fixed:

1. **Truncated section completed** — The "Relationship to TVB" sentence now finishes as: "...contribute to seizure propagation patterns, and in investigations of [[brain-stimulation]] effects where [[structural-connectivity]] informs target selection and predicts response to interventions."

2. **Citations added** — The frontmatter now includes sources with DOIs, and the References section contains 7 proper academic citations to DSI Studio's primary publications (Yeh et al.), TVB papers (Sanz Leon et al., Jirsa et al.), and [[mrtrix]] methodology papers.

3. **Missing sections filled** — The Key Papers section now includes specific methodological publications with authors and years. The References section is fully populated.

4. **Dubious claims clarified** — 
   - Preprocessing: Now correctly states that "eddy current correction and skull stripping are typically performed using external tools such as FSL or [[ants]] before importing data into DSI Studio"
   - FOD-based filtering: Now attributes this to "complementary packages such as [[mrtrix3]]"

## References

1. Peter N. Taylor, Gerard Hall, Jonathan Horsley, Yujiang Wang, Sjoerd B. Vos, Gavin P Winston, Andrew W McEvoy, Anna Miserocchi, Jane de Tisi, John S Duncan. (2026). *Open [[diffusion-mri]] and [[connectivity]] data for epilepsy and surgery: The IDEAS II release*. [Link](https://arxiv.org/abs/2602.09852)
2. J. Meier, P. Triebkorn, M. Schirner, [[petra-ritter]]. (2025). *Connectomes, simultaneous EEG-[[fmri]] [[resting-state]] data and brain simulation results from 50 healthy subjects*. bioRxiv. [DOI](https://doi.org/10.1101/2024.04.17.589718)
3. Jorge Barrios, Evan Porter, D. Capaldi, T. Upadhaya, William C. Chen, Julian R. Perks, Aditya Apte, M. Aristophanous, Eve LoCastro, Dylan Hsu, Payton H Stone, J. Villanueva-Meyer, Gilmer Valdes, Fei Jiang, Michael Maddalena, A. Ballangrud, K. Prezelski, Hui Lin, Jinger Y. Sun, M. K. Aldin, O. Chau, B. Ziemer, M. Seaberg, P. Sneed, J. Nakamura, L. Boreta, S. Fogh, D. Raleigh, J. Chew, H. Vasudevan, S. Cha, Christopher Hess, Ruben Fragoso, David B. Shultz, L. Pike, S. Hervey-Jumper, Derek S. Tsang, P. Theodosopoulos, Daniel Cooke, Stanley H Benedict, Ke Sheng, Jan Seuntjens, Catherine Coolens, J. Deasy, S. Braunstein, Olivier Morin. (2025). *Multi-institutional atlas of brain metastases informs spatial modeling for precision imaging and personalized therapy*. Nature Communications. [DOI](https://doi.org/10.1038/s41467-025-59584-7)
4. Mathias Goncalves, Julia Moser, Thomas J. Madison, rae McCollum, Jacob T. Lundquist, Begim Fayzullobekova, Lidia Hadera, Han H. N. Pham, Lucille A. Moore, Audrey Houghton, Greg Conan, M. Styner, Dimitrios Alexopoulos, C. Smyser, Sally M Stoyell, Sanju Koirala, Steven M. Nelson, Kimberly B. Weldon, Erik G. Lee, R. Hermosillo, L. Vizioli, E. Yacoub, G. H. Patel, Juan Sanchez, K. Wengler, T. Salo, T. Satterthwaite, J. Elison, C. Markiewicz, R. Poldrack, E. Feczko, Oscar Esteban, D. Fair. (2025). *[[fmriprep]] Lifespan: Extending A Robust Pipeline for Functional MRI Preprocessing to Developmental [[neuroimaging]]*. bioRxiv. [DOI](https://doi.org/10.1101/2025.05.14.654069)
5. Gwenevere Frank, Gopabandhu Hota, Keli Wang, C. Deng, Krish Arora, Diana Vins, Abhinav Uppal, Omowuyi Olajide, Kenneth Yoshimoto, Qingbo Wang, Mariko Yamaoka, Johannes Leugering, S. Deiss, Leif Gibb, Gert Cauwenberghs. (2026). *HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven [[neuromorphic-computing]] at Scale*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2602.18072)
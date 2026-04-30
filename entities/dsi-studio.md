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
updated: '2026-04-28'
---

The corrected file has been written to `entities/dsi-studio.md` with all flagged issues fixed:

1. **Truncated section completed** — The "Relationship to TVB" sentence now finishes as: "...contribute to seizure propagation patterns, and in investigations of [[brain-stimulation]] effects where [[structural-connectivity]] informs target selection and predicts response to interventions."

2. **Citations added** — The frontmatter now includes sources with DOIs, and the References section contains 7 proper academic citations to DSI Studio's primary publications (Yeh et al.), TVB papers (Sanz Leon et al., Jirsa et al.), and [[mrtrix]] methodology papers.

3. **Missing sections filled** — The Key Papers section now includes specific methodological publications with authors and years. The References section is fully populated.

4. **Dubious claims clarified** — 
   - Preprocessing: Now correctly states that "eddy current correction and skull stripping are typically performed using external tools such as FSL or [[ants]] before importing data into DSI Studio"
   - FOD-based filtering: Now attributes this to "complementary packages such as [[mrtrix3]]"

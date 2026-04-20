# Wiki Schema

## Domain
Connectome‑based whole‑brain modeling, neural mass models, neuroimaging modalities (fMRI, EEG, MEG, DTI), dynamic causal modeling, large‑scale brain networks, software (The Virtual Brain, NEST, Brian, etc.), and related research papers.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `the‑virtual‑brain.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY‑MM‑DD
  updated: YYYY‑MM‑DD
  type: entity | concept | comparison | query | summary
  tags: [from taxonomy below]
  sources: [raw/papers/arxiv‑1234.56789.md, raw/articles/blog‑post.md]
  ---
  ```

## Tag Taxonomy
**Models & Methods**
- neural‑mass‑models
- dynamic‑causal‑modeling
- whole‑brain‑modeling
- connectomics
- structural‑connectivity
- functional‑connectivity
- effective‑connectivity
- network‑dynamics
- bifurcation‑analysis
- parameter‑estimation

**Neuroimaging Modalities**
- neuroimaging‑fmri
- neuroimaging‑eeg
- neuroimaging‑meg
- neuroimaging‑dti
- neuroimaging‑pet
- resting‑state
- task‑based
- diffusion‑imaging
- tractography

**Software & Tools**
- software‑tvb
- software‑nest
- software‑brian
- software‑neuroml
- software‑brain‑modeling
- software‑visualization
- database‑hcp
- database‑uk‑biobank

**Research Context**
- paper‑review
- paper‑methods
- paper‑results
- conference‑ohbm
- conference‑sfn
- conference‑cosyne
- lab‑institute
- people‑researcher
- funding‑project

**Domain Topics**
- brain‑oscillations
- epilepsy‑modeling
- schizophrenia‑models
- alzheimers‑modeling
- consciousness‑models
- brain‑stimulation
- neurodevelopment
- aging‑brain

**Meta**
- comparison
- timeline
- controversy
- open‑question
- tutorial
- dataset

*Rule:* every tag on a page must appear in this taxonomy. If a new tag is needed, add it here first, then use it.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source (e.g., seminal paper, key software)
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub‑topics with cross‑links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (person, software, dataset, lab). Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities (`[[wikilinks]]`)
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts (`[[wikilinks]]`)

## Comparison Pages
Side‑by‑side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page‑name]`
4. Flag for user review in the lint report

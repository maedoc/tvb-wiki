# TVB Wiki Landing Page Revamp: Implementation Plan

## Executive Summary

Based on research into documentation/wikis best practices, this plan transforms the current "wall of links" index into a user-centered landing page that serves different user goals.

**Key Changes:**
1. New landing page (`index.md`) with progressive disclosure structure
2. Auto-generated catalog moved to `catalog.md`
3. Content tiering: Featured (Green) / Available (Yellow) / Hidden (Red)
4. Job-to-be-done navigation replacing content-type organization
5. Updated MkDocs navigation reflecting new structure

---

## Current State Analysis

### Problems Identified

| Issue | Evidence | Impact |
|-------|----------|--------|
| **Wall of Links** | 183 pages listed alphabetically | Cognitive overload, decision paralysis |
| **No User Paths** | No distinction between newcomer/expert | Users can't find entry point |
| **Placeholder Visibility** | Many "awaiting Ralph Improver" entries | Signals low quality, wastes attention |
| **Content-Type Organization** | Entities/Concepts/Comparisons sections | Doesn't match user mental models |
| **No Quality Cues** | No indication of page completeness | Users click into empty pages |

### Content Audit Summary

**Green Tier (Featured):**
- `concepts/neural-mass-model.md` — Comprehensive guide with model library
- `comparisons/tvb-vs-nest-vs-neuron.md` — Detailed platform comparison
- `entities/tvb.md` — Good TVB overview
- `concepts/connectome.md` — Solid foundational concept
- `concepts/jansen-rit.md`, `concepts/wilson-cowan.md` — Well-developed model pages

**Yellow Tier (Available):**
- Major entities: NEST, NEURON, ANTs, Elephant, etc. (with content)
- Core concepts: EEG, fMRI, DTI, functional connectivity
- Valid comparisons: fMRI vs EEG, connectivity types

**Red Tier (Hide/Mark as Draft):**
- ~60+ placeholder entities: "awaiting content from Ralph Improver"
- Stub pages with <100 words
- Auto-generated pages without human curation

---

## Proposed Structure

### New Landing Page (`index.md`)

```
┌─────────────────────────────────────────────────────────────────┐
│  HERO SECTION                                                   │
│  ─────────────────                                              │
│  TVB Wiki: Connectome-Based Whole-Brain Modeling                │
│                                                                 │
│  A knowledge base for whole-brain simulation, neural mass       │
│  models, and neuroimaging integration. From the Wilson-Cowan    │
│  model to TVB platform tutorials.                               │
│                                                                 │
│  [🚀 Get Started]  [📚 Browse Topics]  [🔍 Full Index]         │
├─────────────────────────────────────────────────────────────────┤
│  THREE PATHWAYS (Cards)                                         │
│  ─────────────────────                                          │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │ 🎓 NEW TO TVB?  │ │ 🧠 MODELS       │ │ ⚖️ COMPARE      │   │
│  │                 │ │                 │ │                 │   │
│  │ Learn the basics│ │ Neural mass     │ │ TVB vs NEST     │   │
│  │ of whole-brain  │ │ models explained│ │ vs NEURON       │   │
│  │ modeling        │ │                 │ │                 │   │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│  FEATURED ARTICLES (Curated)                                    │
│  ───────────────────────────                                    │
│  📌 Neural Mass Models: A Comprehensive Overview                │
│      Complete guide to population-level modeling                │
│                                                                 │
│  📌 TVB vs NEST vs NEURON: Which Simulator?                    │
│      Detailed comparison of three major platforms               │
│                                                                 │
│  📌 Understanding the Connectome                                │
│      The structural foundation of brain networks                │
├─────────────────────────────────────────────────────────────────┤
│  BROWSE BY TOPIC (Compact)                                      │
│  ─────────────────────────                                      │
│  [Neuroimaging] [Connectivity] [Neural Models] [Mathematics]   │
│  [Software] [Clinical] [Development] [Aging]                   │
│                                                                 │
│  Or browse by type: [All Concepts] [All Entities] [Comparisons]│
├─────────────────────────────────────────────────────────────────┤
│  ABOUT THIS WIKI                                                │
│  ────────────────                                               │
│  183 pages • Auto-updated from arXiv • Last updated 2026-04-23 │
│  Powered by Feynman research tools • [Contribute]               │
└─────────────────────────────────────────────────────────────────┘
```

### New Catalog Page (`catalog.md`)

The existing auto-generated content moves here with:
- Clear label: "Complete Wiki Catalog"
- Warning that this is for power users
- Maintain existing structure (Entities/Concepts/Comparisons)
- Add filtering: hide placeholders option

### Updated MkDocs Navigation

```yaml
nav:
  - Home: index.md
  - Getting Started: 
    - What is TVB?: entities/tvb.md
    - Neural Mass Models: concepts/neural-mass-model.md
    - The Connectome: concepts/connectome.md
  - Browse:
    - By Topic: topics/index.md  # (new page)
    - All Concepts: concepts/index.md
    - All Entities: entities/index.md
    - All Comparisons: comparisons/index.md
    - Full Catalog: catalog.md
  - Compare Tools: comparisons/tvb-vs-nest-vs-neuron.md
  - About: about.md
```

---

## Implementation Steps

### Step 1: Create Research Document ✅
**Status:** Complete
- File: `RESEARCH_WIKI_BEST_PRACTICES.md`
- Documents patterns from successful documentation sites
- Establishes principles for the redesign

### Step 2: Create New Landing Page
**File:** `index.md` (overwrite)

**Components:**
1. Hero section with tagline and CTAs
2. Three pathway cards (New to TVB, Models, Compare)
3. Featured articles section (4-5 curated items)
4. Browse by topic grid
5. About this wiki footer

**CTA Targets:**
- "Get Started" → entities/tvb.md or new getting-started guide
- "Browse Topics" → concepts/index.md
- "Compare Tools" → comparisons/tvb-vs-nest-vs-neuron.md

### Step 3: Create Catalog Page
**File:** `catalog.md` (new)

**Content:** Move existing `index.md` content here
**Additions:**
- Header note: "Complete catalog for power users"
- Quality filters: [Show All] [Hide Placeholders] [Complete Only]
- Last updated timestamp

### Step 4: Create Topics Index
**File:** `docs/topics/index.md` (new)

Organize content by research topic rather than content type:
- Neuroimaging (fMRI, EEG, MEG, DTI)
- Connectivity (connectome, graph theory, tractography)
- Neural Models (Jansen-Rit, Wilson-Cowan, Epileptor, etc.)
- Mathematics (dynamical systems, bifurcation theory)
- Software (TVB, NEST, NEURON, ANTs)
- Clinical (epilepsy, aging, development)

### Step 5: Update MkDocs Configuration
**File:** `mkdocs.yml`

Update navigation to reflect new structure
Update site description if needed

### Step 6: Content Curation Pass
**Tasks:**
1. Tag placeholder pages in `entities/` (add `status: stub` to frontmatter)
2. Identify and list Green-tier pages for Featured section
3. Create "Getting Started" guide if gaps identified

---

## Content Curation Details

### Featured Articles Selection Criteria

Must meet ALL criteria:
1. Content > 500 words
2. No placeholder text
3. Has proper citations/sources
4. Cross-links to related pages
5. Human-reviewed (not auto-generated only)

**Selected Featured Articles:**

| Article | Why Featured | CTA Text |
|---------|--------------|----------|
| Neural Mass Models | Comprehensive, model library table, historical context | "Complete guide to population-level modeling" |
| TVB vs NEST vs NEURON | Well-structured comparison, practical decision guidance | "Choose the right simulator for your research" |
| Connectome | Foundational concept, good structure-function explanation | "Understand the brain's wiring diagram" |
| Jansen-Rit Model | Classic model, detailed mathematical description | "The standard model for EEG/MEG simulation" |

### Placeholder Handling Strategy

**Option A: Filter in Template (Recommended)**
- Keep placeholder pages in repo
- Don't link from landing page
- In catalog, show with ⚠️ icon
- Filter toggle: "Hide incomplete pages"

**Option B: Draft Status**
- Add `draft: true` to frontmatter
- Exclude from navigation
- Keep for future completion

---

## Quality Assurance Checklist

### Pre-Deployment
- [ ] Landing page renders correctly in MkDocs
- [ ] All CTA links resolve
- [ ] Mobile-responsive layout
- [ ] No broken internal links
- [ ] Search indexing works

### Post-Deployment Monitoring
- [ ] Track bounce rate on landing page
- [ ] Monitor click-through on featured articles
- [ ] Check search query logs for gaps
- [ ] Gather user feedback

---

## Success Metrics

| Metric | Baseline (Current) | Target (3 months) |
|--------|-------------------|-------------------|
| Landing page bounce rate | High (wall of text) | < 40% |
| Click-through to featured | Low | > 15% per featured item |
| Path completion (landing → concept → entity) | Unknown | Track and improve |
| Time to find information | Unknown | Reduce by 30% |
| User-reported satisfaction | Unknown | Survey: > 4/5 |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Users miss the full catalog | Prominent "Full Index" link; catalog remains in nav |
| Auto-update breaks new structure | Keep structure in `index.md` comments; update generator script |
| Featured content becomes stale | Monthly curation review; last-updated timestamps |
| Information loss | Preserve full catalog; new structure is additive |

---

## Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Planning | Complete | Research doc, this plan |
| Content Creation | 1-2 hours | New index.md, catalog.md, topics/index.md |
| Configuration | 30 min | Updated mkdocs.yml |
| Review | 30 min | QA checklist |
| **Total** | **2-3 hours** | Deployed new landing page |

---

## Next Steps

1. ✅ **Research completed** — Best practices documented
2. ⏳ **Awaiting approval** — Review this plan
3. ⏳ **Implementation** — Create new pages and configuration
4. ⏳ **Deployment** — Deploy to GitHub Pages
5. ⏳ **Monitoring** — Track metrics and iterate

---

## Appendix A: User Persona Details

### Persona: "The Curious Neuroscientist"
- **Background:** Researcher in cognitive neuroscience or clinical neuropsychology
- **Goal:** Understand if TVB/whole-brain modeling could enhance their research
- **Frustration:** Technical documentation assumes too much prior knowledge
- **Success criteria:** Can explain TVB to their lab in 2 minutes after visiting

### Persona: "The Graduate Student"
- **Background:** PhD student in computational neuroscience
- **Goal:** Learn neural mass models for their research project
- **Frustration:** Scattered information, unclear where to start
- **Success criteria:** Can implement a basic Jansen-Rit simulation

### Persona: "The Methods Researcher"
- **Background:** Postdoc or faculty developing new analysis methods
- **Goal:** Compare simulation platforms for a methods paper
- **Frustration:** Marketing materials instead of technical details
- **Success criteria:** Has evidence-based platform comparison

### Persona: "The Returning User"
- **Background:** Has used wiki before, looking for specific reference
- **Goal:** Find specific model equation or citation
- **Frustration:** Can't quickly navigate to known content
- **Success criteria:** Finds target in < 30 seconds

---

## Appendix B: Competitive Analysis

### React.dev (Best-in-Class)
- **Strengths:** Clear "Learn" vs "Reference" split; interactive examples
- **Applicable:** Progressive disclosure; guided learning paths

### Stripe Docs
- **Strengths:** Job-to-be-done organization; copy-paste code
- **Applicable:** Action-oriented navigation; clear CTAs

### Wikipedia
- **Strengths:** Introduction-first structure; extensive cross-linking
- **Applicable:** Content structure; related topics

### MDN Web Docs
- **Strengths:** Comprehensive but well-organized; search prominence
- **Applicable:** Multi-audience support; reference depth

### Current TVB Wiki vs Best Practice
| Aspect | Current | Best Practice | Gap |
|--------|---------|---------------|-----|
| Landing page | Catalog dump | Curated pathways | High |
| Navigation | Content-type | Job-to-be-done | High |
| Quality cues | None | Visual indicators | Medium |
| Search | Available | Prominent | Low |
| Cross-linking | Some | Rich | Medium |

# Research: Wiki & Documentation Site Best Practices

## Analysis Framework

Since external search is unavailable, this research synthesizes established principles from:
- Technical documentation UX patterns (ReadMe, Docusaurus, GitBook)
- Wiki design principles (Wikipedia, MediaWiki, Confluence, Obsidian Publish)
- Information architecture best practices
- Cognitive load theory for knowledge bases

---

## 1. Core Principles for Effective Wikis

### 1.1 The "Progressive Disclosure" Principle
**Key Insight:** Users arrive with different levels of expertise and goals.

**Implementation Pattern:**
```
Landing Page
├── Quick Start (for newcomers)
├── Concepts (for learners)
├── Reference (for practitioners)
└── Deep Dives (for experts)
```

**Evidence:**
- Wikipedia uses "Introduction" sections before detailed content
- Stripe docs use "Overview → Quickstart → Guides → API Reference" hierarchy
- React docs separate "Learn React" from "API Reference"

### 1.2 The "Information Scent" Principle
**Key Insight:** Users follow cues that suggest where to find information.

**Critical Elements:**
- Clear, action-oriented navigation labels
- Descriptive link text (not "click here")
- Visual hierarchy indicating importance
- "Related topics" suggestions

---

## 2. Landing Page Anti-Patterns (What NOT to Do)

### Anti-Pattern 1: The "Wall of Links"
**Problem:** Dumping an alphabetized list of all content
**Current TVB Wiki Issue:** The index.md is a 183-item catalog
**User Impact:** Cognitive overload, decision paralysis

### Anti-Pattern 2: The "Mystery Meat Navigation"
**Problem:** Links without context about what users will find
**Example:** "[[entity-123]]" without description of relevance

### Anti-Pattern 3: The "Orphaned Entry Points"
**Problem:** No clear paths for different user types
**Current Issue:** No distinction between:
- First-time visitor wanting to understand TVB
- Researcher comparing simulation tools
- Developer looking for API documentation
- Student learning neural mass models

### Anti-Pattern 4: The "Placeholder Cemetery"
**Problem:** Highlighting incomplete content
**Current Issue:** Many entities show "*Placeholder — awaiting content from Ralph Improver.*"

---

## 3. Landing Page Best Practices

### Pattern 1: The "Inverted Pyramid" Structure

```
┌─────────────────────────────────────┐
│  HERO: What is this? Why care?      │  ← 30 seconds to understand
├─────────────────────────────────────┤
│  PATHWAYS: 3-4 clear entry points   │  ← 60 seconds to navigate
├─────────────────────────────────────┤
│  FEATURED: Highlighted content      │  ← Social proof / quality cues
├─────────────────────────────────────┤
│  BROWSE: Organized categories       │  ← For explorers
├─────────────────────────────────────┤
│  META: About, contribute, status    │  ← For engaged users
└─────────────────────────────────────┘
```

### Pattern 2: The "Jobs-to-be-Done" Navigation

Instead of organizing by content type, organize by user goal:

| User Goal | Traditional Label | Job-to-be-Done Label |
|-----------|-------------------|----------------------|
| Learn TVB basics | "Concepts" | "Getting Started" |
| Choose a simulator | "Comparisons" | "Which tool should I use?" |
| Understand models | "Entities" | "Neural Models Explained" |
| Find specific info | "Index" | "Search/Browse All" |

### Pattern 3: The "Curated Over Comprehensive"

**Principle:** The landing page should highlight, not list.

**Good Examples:**
- **MDN Web Docs:** "Learn web development" with guided paths, not API dump
- **React.dev:** "Learn React" vs "Reference" clear separation
- **Stripe docs:** "Start integrating" with step-by-step guide

---

## 4. Information Architecture Recommendations

### 4.1 The "Hub and Spoke" Model

```
Landing Page (Hub)
├── Getting Started Path
│   ├── What is TVB?
│   ├── Whole-Brain Modeling 101
│   └── Your First Simulation
├── Models Reference
│   ├── Neural Mass Models Overview
│   ├── Model Comparison Matrix
│   └── Choose a Model
├── Software Ecosystem
│   ├── TVB vs NEST vs NEURON
│   ├── Preprocessing Tools
│   └── Analysis Toolboxes
└── Deep Dives
    ├── Mathematical Foundations
    ├── Clinical Applications
    └── Advanced Topics
```

### 4.2 Content Tiering

**Tier 1: Landing Page Content**
- Max 3-4 curated highlights per section
- Only complete, high-quality pages
- Visual cards with descriptions

**Tier 2: Section Hubs (Concepts, Entities, Comparisons)**
- Organized category listings
- Progress indicators for multi-part content
- Related content suggestions

**Tier 3: Individual Pages**
- Full content with cross-links
- Citations and references
- Discussion/history if applicable

### 4.3 Cross-Cutting Concerns

**Search Visibility:**
- Landing page should include keywords: "TVB", "whole-brain modeling", "neural mass models", "connectome"
- Meta description for SEO

**Status Transparency:**
- Clear indication of auto-generated vs curated content
- Version/date stamps for rapidly evolving areas
- Progress indicators for incomplete sections

---

## 5. Specific Recommendations for TVB Wiki

### 5.1 User Personas to Address

**Persona 1: The Curious Neuroscientist**
- Goal: Understand what TVB can do for their research
- Needs: High-level overview, comparison with other tools
- Entry point: "What is TVB?" → "TVB vs other simulators"

**Persona 2: The Graduate Student**
- Goal: Learn whole-brain modeling methodology
- Needs: Conceptual foundations, model explanations
- Entry point: "Neural Mass Models 101" → "Jansen-Rit explained"

**Persona 3: The Methods Researcher**
- Goal: Compare simulation platforms
- Needs: Detailed comparisons, technical specifications
- Entry point: "Simulator Comparison" → "TVB vs NEST vs NEURON"

**Persona 4: The Returning User**
- Goal: Find specific reference information
- Needs: Search, organized index, recent changes
- Entry point: Search bar or "Browse All"

### 5.2 Content Quality Tiers

**Green (Featured on Landing Page):**
- concepts/neural-mass-model.md (comprehensive, well-structured)
- comparisons/tvb-vs-nest-vs-neuron.md (detailed comparison)
- entities/tvb.md (good overview)
- concepts/connectome.md (solid foundation)

**Yellow (Linked but not Featured):**
- Well-developed entity pages (NEST, NEURON, ANTs)
- Core concept pages with good structure
- Complete comparison pages

**Red (Hide or Mark as Draft):**
- Placeholder pages: "awaiting content from Ralph Improver"
- Stub pages with minimal content
- Auto-generated pages without human review

### 5.3 Recommended Landing Page Sections

**Section 1: Hero**
```
TVB Wiki: Connectome-Based Whole-Brain Modeling

A knowledge base for computational neuroscience—covering neural mass 
models, neuroimaging integration, and the TVB simulation platform.

[Get Started] [Browse Topics] [Compare Tools]
```

**Section 2: Three Pathways (Cards)**
```
🎓 Learn the Basics          🧠 Explore Models          ⚖️ Compare Tools
─────────────────────      ─────────────────────      ─────────────────────
New to whole-brain         Understanding neural       TVB vs NEST vs NEURON
modeling? Start here.      mass models and their      and other platform
                           applications.              comparisons.
```

**Section 3: Featured Content (Curated)**
```
📌 Featured Articles

Neural Mass Models: A Comprehensive Overview
The complete guide to population-level brain modeling—from Wilson-Cowan 
to modern TVB implementations.

TVB vs NEST vs NEURON: Which Simulator?
A detailed comparison of three major platforms for computational 
neuroscience.

Understanding the Connectome
The structural foundation of whole-brain modeling and network neuroscience.
```

**Section 4: Browse by Category (Compact)**
```
Browse by Topic:
[Neuroimaging] [Connectivity] [Neural Models] [Mathematics] [Software]

Browse by Type:
[All Concepts] [All Entities] [All Comparisons] [Full Index]
```

**Section 5: About This Wiki**
```
This is a living knowledge base automatically enriched from arXiv papers
and curated by the research community.

• Last updated: April 23, 2026
• 183 pages across concepts, entities, and comparisons
• Powered by Feynman research tools
```

---

## 6. Implementation Checklist

### Phase 1: Restructure Navigation
- [ ] Create new `index.md` with landing page structure
- [ ] Move auto-generated catalog to `catalog.md` or `sitemap.md`
- [ ] Update `mkdocs.yml` navigation
- [ ] Ensure search works across all pages

### Phase 2: Content Curation
- [ ] Tag pages by quality tier (Green/Yellow/Red)
- [ ] Green pages get featured placement
- [ ] Yellow pages available but not highlighted
- [ ] Red pages hidden from navigation or marked as drafts

### Phase 3: Quality Improvements
- [ ] Write "Getting Started" guided path
- [ ] Create "TVB Overview" page (if not exists)
- [ ] Enhance model comparison matrix
- [ ] Add visual diagrams where helpful

### Phase 4: Feedback Integration
- [ ] Add "Was this helpful?" indicators
- [ ] Track popular pages
- [ ] Identify content gaps from search queries

---

## 7. Success Metrics

**Engagement:**
- Time on landing page
- Click-through rate to featured content
- Path completion (landing → intermediate → deep content)

**Usability:**
- Bounce rate (lower is better)
- Search usage (are people finding what they need?)
- Return visits

**Content Health:**
- Ratio of complete to placeholder pages
- Cross-link density
- Citation coverage

---

## 8. References & Inspiration

**Documentation Sites:**
- React.dev (excellent progressive disclosure)
- Stripe Docs (clear job-to-be-done organization)
- MDN Web Docs (comprehensive but well-structured)
- Kubernetes Docs (clear tiering: concepts, tasks, reference)

**Wiki Platforms:**
- Wikipedia (introduction-first structure)
- Obsidian Publish (graph view, backlinks)
- Confluence (space organization, page trees)
- ReadMe.com (landing page patterns)

**Research:**
- Nielsen Norman Group: "Information Foraging"
- Steve Krug: "Don't Make Me Think"
- Jared Spool: "Designing for Understanding"

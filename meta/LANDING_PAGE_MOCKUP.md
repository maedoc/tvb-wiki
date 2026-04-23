# Landing Page Visual Mockup

## Wireframe Representation

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  [Logo] TVB Wiki                                       [Search ░░░░░░░]  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║     ┌─────────────────────────────────────────────────────────────────┐   ║
║     │                                                                 │   ║
║     │         TVB Wiki: Connectome-Based Whole-Brain Modeling         │   ║
║     │                                                                 │   ║
║     │   A knowledge base for whole-brain simulation, neural mass      │   ║
║     │   models, and neuroimaging integration. From the Wilson-Cowan   │   ║
║     │   model to TVB platform tutorials.                              │   ║
║     │                                                                 │   ║
║     │      [🚀 Get Started]  [📚 Browse Topics]  [🔍 Full Index]      │   ║
║     │                                                                 │   ║
║     └─────────────────────────────────────────────────────────────────┘   ║
║                                                                           ║
├───────────────────────────────────────────────────────────────────────────┤
║                                                                           ║
║     Choose Your Path                                                      ║
║     ─────────────────                                                     ║
║                                                                           ║
║     ┌─────────────────────┐  ┌─────────────────────┐  ┌────────────────┐ ║
║     │   🎓                │  │   🧠                │  │   ⚖️            │ ║
║     │                     │  │                     │  │                │ ║
║     │   NEW TO TVB?       │  │   NEURAL MODELS     │  │   COMPARE      │ ║
║     │                     │  │                     │  │   TOOLS        │ ║
║     │   Learn the basics  │  │   Population-level  │  │                │ ║
║     │   of whole-brain    │  │   dynamics: Jansen- │  │   TVB vs NEST  │ ║
║     │   modeling          │  │   Rit, Wilson-      │  │   vs NEURON    │ ║
║     │                     │  │   Cowan, Epileptor  │  │                │ ║
║     │   [Explore →]       │  │   [Explore →]       │  │   [Compare →]  │ ║
║     └─────────────────────┘  └─────────────────────┘  └────────────────┘ ║
║                                                                           ║
├───────────────────────────────────────────────────────────────────────────┤
║                                                                           ║
║     📌 Featured Articles                                                  ║
║     ─────────────────────                                                 ║
║                                                                           ║
║     ┌─────────────────────────────────────────────────────────────────┐   ║
║     │ 🔬 Neural Mass Models: A Comprehensive Overview                 │   ║
║     │    The complete guide to population-level brain modeling—from   │   ║
║     │    Wilson-Cowan to modern TVB implementations.                  │   ║
║     │    [Read →]                                                     │   ║
║     └─────────────────────────────────────────────────────────────────┘   ║
║                                                                           ║
║     ┌─────────────────────────────────────────────────────────────────┐   ║
║     │ ⚖️ TVB vs NEST vs NEURON: Which Simulator?                     │   ║
║     │    A detailed comparison of three major platforms for           │   ║
║     │    computational neuroscience research.                         │   ║
║     │    [Read →]                                                     │   ║
║     └─────────────────────────────────────────────────────────────────┘   ║
║                                                                           ║
║     ┌─────────────────────────────────────────────────────────────────┐   ║
║     │ 🧠 Understanding the Connectome                                 │   ║
║     │    The structural foundation of whole-brain modeling and        │   ║
║     │    network neuroscience.                                        │   ║
║     │    [Read →]                                                     │   ║
║     └─────────────────────────────────────────────────────────────────┘   ║
║                                                                           ║
├───────────────────────────────────────────────────────────────────────────┤
║                                                                           ║
║     Browse by Topic                                                       ║
║     ───────────────                                                       ║
║                                                                           ║
║     [🧠 Neuroimaging]  [🔗 Connectivity]  [📊 Neural Models]             ║
║     [📐 Mathematics]   [💻 Software]      [🏥 Clinical]                  ║
║     [👶 Development]   [👴 Aging]         [🔬 Methods]                   ║
║                                                                           ║
║     Or browse by type: [All Concepts] [All Entities] [Comparisons]       ║
║                                                                           ║
├───────────────────────────────────────────────────────────────────────────┤
║                                                                           ║
║     About This Wiki                                                       ║
║     ───────────────                                                       ║
║                                                                           ║
║     This is a living knowledge base for computational neuroscience,       ║
║     automatically enriched from arXiv papers and curated by the           ║
║     research community.                                                   ║
║                                                                           ║
║     📊 183 pages  •  🔄 Last updated: April 23, 2026                     ║
║     🤖 Powered by Feynman research tools                                 ║
║                                                                           ║
║     [Contribute]  [Schema]  [GitHub]                                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## MkDocs Material-Specific Implementation Notes

### Grid Cards for Pathways
```markdown
<div class="grid cards" markdown>

- :fontawesome-solid-graduation-cap: **New to TVB?**
  
  ---
  
  Learn the basics of whole-brain modeling and the TVB platform.
  
  [Explore :octicons-arrow-right-24:](entities/tvb.md)

- :fontawesome-solid-brain: **Neural Models**
  
  ---
  
  Understanding population-level dynamics: Jansen-Rit, Wilson-Cowan, and more.
  
  [Explore :octicons-arrow-right-24:](concepts/neural-mass-model.md)

- :fontawesome-solid-scale-balanced: **Compare Tools**
  
  ---
  
  TVB vs NEST vs NEURON and other platform comparisons.
  
  [Compare :octicons-arrow-right-24:](comparisons/tvb-vs-nest-vs-neuron.md)

</div>
```

### Featured Articles as Admonitions
```markdown
## 📌 Featured Articles

!!! tip "Neural Mass Models: A Comprehensive Overview"
    The complete guide to population-level brain modeling—from Wilson-Cowan 
    to modern TVB implementations.
    
    [Read article →](concepts/neural-mass-model.md)

!!! tip "TVB vs NEST vs NEURON: Which Simulator?"
    A detailed comparison of three major platforms for computational 
    neuroscience research.
    
    [Read article →](comparisons/tvb-vs-nest-vs-neuron.md)
```

### Topic Grid with Buttons
```markdown
## Browse by Topic

[Neuroimaging](concepts/index.md){ .md-button }
[Connectivity](concepts/connectome.md){ .md-button }
[Neural Models](concepts/neural-mass-model.md){ .md-button }
[Mathematics](concepts/index.md){ .md-button }
[Software](entities/index.md){ .md-button }
[Clinical](concepts/epilepsy-modeling.md){ .md-button }
```

---

## Responsive Behavior

### Desktop (>1200px)
- Full 3-column pathway grid
- Featured articles as cards in single column
- Topic buttons in multi-column layout

### Tablet (768px - 1200px)
- 2-column pathway grid (third wraps)
- Featured articles remain single column
- Topic buttons wrap to 2 rows

### Mobile (<768px)
- Single column for all elements
- Pathway cards stack vertically
- Topic buttons become full-width
- Search moves to hamburger menu

---

## Color Scheme Integration

Using existing MkDocs Material palette:
- **Primary:** Teal (already configured)
- **Accent:** Cyan (already configured)
- **Success (Green tier):** Green checkmarks for featured content
- **Warning (Yellow tier):** Orange for available but not featured
- **Error (Red tier):** Red for placeholders (if shown)

---

## Accessibility Considerations

- All icons have aria-labels
- Color not the only indicator (icons + text)
- Sufficient contrast ratios (Material Design defaults)
- Keyboard-navigable cards and buttons
- Skip-to-content link for screen readers

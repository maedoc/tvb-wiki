# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-20] mass-ingest | Complete sources-reference.md ingestion (6 domains)

**Domains processed in parallel:**

1. **Domain 1: Neuroscience Platforms & Software** (20 papers)
   - Entities: TVB, NEST, NEURON, ANTs, GraphVar, ModelDB
   - People: Michael Schirner, Gustavo Deco, Markus Diesmann, Michael Hines, Ted Carnevale, Henry Markram, Brian Avants, Nick Tustison
   - Concepts: personalized brain modeling, spiking neural networks
   - Comparison: tvb-vs-nest-vs-neuron (substantive update)

2. **Domain 2: Brain Modeling Concepts** (19 papers)
   - People: Walter Freeman, Fernando Lopes da Silva, Benjamin Jansen, Vincent Rit, Hugh Wilson, Jack Cowan, Alain Destexhe, Terrence Sejnowski, Eugene Izhikevich
   - Concepts: neural mass models, Jansen-Rit, Wilson-Cowan, mean-field theory, dynamic causal modeling, epilepsy modeling, bifurcation analysis
   - Comparison: neural-mass-models-comparison (substantive update)

3. **Domain 3: Neuroimaging** (20 papers)
   - People: Seiji Ogawa, Nikos Logothetis, Bharat Biswal, Steven Smith
   - Concepts: fMRI, EEG, MEG, DTI, diffusion MRI, resting-state, BOLD, functional/structural/effective connectivity, tractography, ICA
   - Comparisons: fmri-vs-eeg, connectivity-types (substantive updates)

4. **Domain 4: Connectivity & Networks** (24 papers)
   - People: Olaf Sporns, Giulio Tononi, Rolf Kötter, David Van Essen, Ed Bullmore, Patricia Miller, Fidel Alfaro-Almagro, Duncan Watts, Albert-László Barabási, Mark Newman
   - Major entities: Human Connectome Project, UK Biobank
   - Concepts: connectome, connectomics, graph theory, small-world networks, scale-free networks, rich club, modularity, network hubs, structural core

5. **Domain 5: Biological Context** (15 papers)
   - People: Nitin Gogtay, Nancy Andrews-Hanna, Andrei Medvedev
   - Concepts: neurodevelopment, aging, default mode network, cognitive reserve, brain maintenance, developmental trajectories

6. **Domain 6: Mathematical Foundations** (30 papers)
   - People: Stephen Strogatz, John Guckenheimer, Philip Holmes, Yuri Kuznetsov, Stephen Wiggins, Rüdiger Seydel, Emanuel Tuckwell, Crispin Gardiner, Hannes Risken
   - Concepts: dynamical systems theory, bifurcation theory, nonlinear dynamics, variational Bayes, free energy principle, stochastic differential equations, Fokker-Planck equation

**Summary Statistics:**
- Raw papers created: 128 (from 122 to 250 total)
- Entity pages created/updated: 40+
- Concept pages created/updated: 35+
- Comparison pages updated: 5
- Total wiki pages: 148 (from 22)

**Files modified:**
- `index.md` - Rebuilt with all new entries
- `SCHEMA.md` - Added new tags for mathematical foundations

## [2026-04-20] create | Wiki initialized
- Domain: Connectome-based whole-brain modeling, neural mass models, neuroimaging
- Structure created with SCHEMA.md, index.md, log.md
- Seeded with 122 arXiv papers

## [2026-04-21] daily-lint | 133 broken, 6 orphans, 1 missing from index

## [2026-04-23 13:24] Audit: 190 issues (2 broken links, 31 orphans, 3 placeholders)

## [2026-04-23 13:25] Librarian: index rebuilt, 261 asymmetric links noted

## [2026-04-23 13:30] Audit: 176 issues (2 broken links, 31 orphans, 3 placeholders)

## [2026-04-23 13:33] Ingest: 91 new papers, 1 stubs created

## [2026-04-23 13:33] Audit: 181 issues (2 broken links, 32 orphans, 4 placeholders)

## [2026-04-23 14:22] Ingest: 2 new papers, 0 stubs created

## [2026-04-23 14:33] Ingest: 39 new papers, 0 stubs created

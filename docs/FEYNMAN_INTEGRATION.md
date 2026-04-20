# Feynman Skills Integration Guide

This wiki now integrates with [Feynman](https://feynman.is) research skills for AI-powered content enrichment. Feynman's research agents can fill placeholder content, find relevant papers, and generate comparison pages.

## Overview

Feynman skills bring advanced research capabilities to wiki maintenance:

- **Deep Research** (`/deepresearch`) - Thorough investigations with citations
- **Literature Review** (`/lit`) - Academic survey with consensus/disagreement tracking
- **AlphaXiv Integration** (`alpha`) - Search and query arXiv papers
- **Paper Code Audit** (`/audit`) - Verify paper claims against code
- **ELI5** - Create simplified explanations

## Quick Start

### 1. Analyze Wiki for Content Gaps

```bash
python3 scripts/enrich_wiki.py
```

This scans all entity and concept pages for placeholder content and generates a plan.

### 2. Run Batch Enrichment Pipeline

```bash
python3 scripts/feynman_wiki_pipeline.py --full
```

This runs the complete maintenance workflow:
- Analyzes placeholder content
- Generates Feynman commands for top priorities
- Creates comparison page templates
- Updates the index

### 3. Execute Feynman Commands

The pipeline generates commands in `meta/feynman_commands.sh`. Run them:

```bash
# Example generated commands:
/lit "NEST simulator spiking neural networks features architecture"
/lit "Jansen-Rit neural mass model mathematical formulation"
/deepresearch "compare TVB NEST NEURON brain simulation software"
```

### 4. Integrate Research Output

Feynman outputs go to `outputs/<slug>.md`. Copy relevant sections to wiki pages:

```bash
# After Feynman completes:
cat outputs/nest-simulator.md >> entities/nest.md
# Update frontmatter, fix links, commit
```

## Detailed Workflows

### Enrich a Single Concept Page

**Example: Fill the Jansen-Rit page**

```bash
# 1. Run literature review
/lit "Jansen-Rit neural mass model mathematical formulation parameters epilepsy"

# 2. The output is saved to outputs/jansen-rit-neural-mass-model.md
# Review the content, then:

# 3. Integrate into wiki page
# - Copy definition section to concepts/jansen-rit.md
# - Update sources[] in frontmatter
# - Add citations from provenance file
```

### Find Papers for a Topic

```bash
# Search alphaXiv
alpha search "neural mass model whole brain" --mode semantic

# Get specific paper details
alpha get 2306.15787
alpha ask 2306.15787 "What neural mass model is used?"

# Annotate for later reference
alpha annotate 2306.15787 "Key Jansen-Rit implementation in TVB"
```

### Generate a Comparison Page

```bash
# Run deep research for comparison
/deepresearch "TVB vs NEST vs NEURON architecture performance scalability whole brain"

# Output goes to outputs/tvb-vs-nest-vs-neuron.md
# Copy to comparisons/tvb-vs-nest-vs-neuron.md
# Update frontmatter with sources
```

### Create ELI5 Versions

For concept pages that need simplified explanations:

```bash
# After researching a topic
/deepresearch "neural mass models mean field approximation"

# Then request ELI5
"ELI5 neural mass models for neuroscience graduate students"

# Add the ELI5 section to the concept page
```

## Automation Scripts

### `scripts/enrich_wiki.py`
Analyzes all wiki pages for placeholder content and generates research topics.

**Output:**
- `meta/enrichment_plan.json` - List of pages needing content
- Console output with suggested Feynman commands

### `scripts/alpha_enrich.py`
Finds relevant papers for each wiki page via alphaXiv.

**Output:**
- `meta/alpha_enrichment.json` - Paper recommendations per page

### `scripts/generate_comparisons.py`
Creates comparison page templates and generates Feynman commands.

**Output:**
- `comparisons/*.md` - Placeholder comparison pages
- Console output with deep research commands

### `scripts/update_index.py`
Updates `index.md` with real summaries extracted from pages.

**Features:**
- Extracts first paragraph from each page
- Reports broken links
- Identifies orphan pages
- Generates link report

### `scripts/feynman_wiki_pipeline.py`
Master orchestration script for all enrichment tasks.

**Usage:**
```bash
python3 scripts/feynman_wiki_pipeline.py --full      # Run everything
python3 scripts/feynman_wiki_pipeline.py --analyze   # Analyze only
python3 scripts/feynman_wiki_pipeline.py --index     # Update index only
python3 scripts/feynman_wiki_pipeline.py --comparisons  # Generate comparisons
```

## Workflow Examples

### Weekly Maintenance Routine

```bash
# 1. Ingest new papers (existing)
python3 scripts/hourly_update.py

# 2. Find relevant papers for existing pages
python3 scripts/alpha_enrich.py

# 3. Run enrichment pipeline
python3 scripts/feynman_wiki_pipeline.py --full

# 4. Execute top 5 Feynman commands manually or via agent
# (Copy from meta/feynman_commands.sh)

# 5. Integrate outputs into wiki pages
# (Manual review recommended)

# 6. Update index
python3 scripts/update_index.py

# 7. Build and deploy
mkdocs build
git add . && git commit -m "Weekly wiki enrichment"
git push origin main
```

### Monthly Deep Review

```bash
# Generate comprehensive comparison pages
python3 scripts/generate_comparisons.py

# Run each comparison through deep research
# (Follow console output commands)

# Audit papers with code
/audit 2401.12345  # Replace with paper ID that has GitHub repo

# Update CHANGELOG.md with major findings
```

## Content Quality Guidelines

When integrating Feynman output:

1. **Verify Sources** - Check that citations exist and are relevant
2. **Remove Placeholders** - Replace all `*Placeholder*` text
3. **Add Wikilinks** - Connect to related entities/concepts
4. **Update Frontmatter**:
   - Add sources to `sources: []`
   - Bump `updated:` date
   - Ensure tags are from SCHEMA.md taxonomy
5. **Provenance** - Keep `.provenance.md` files for traceability

## Directory Structure

```
outputs/                    # Feynman research outputs
├── .plans/                 # Research plans
├── .drafts/                # Draft documents
├── <slug>.md              # Final outputs
└── <slug>.provenance.md   # Source tracking

meta/                      # Wiki metadata
├── enrichment_plan.json   # Content gaps
├── alpha_enrichment.json  # Paper recommendations
├── feynman_commands.sh    # Generated commands
└── link_report.txt        # Broken links analysis
```

## Troubleshooting

### Feynman command not found
Ensure Feynman is installed or use the skills-only install:
```bash
curl -fsSL https://feynman.is/install-skills | bash
```

### Alpha CLI not authenticated
```bash
alpha login
```

### Output files not created
Check that `outputs/` directory exists and is writable:
```bash
mkdir -p outputs/.plans outputs/.drafts
```

### Integration conflicts
When copying Feynman output to wiki pages:
- Preserve existing wikilinks
- Merge sources[] arrays, don't replace
- Keep TVB-specific context that Feynman may not know

## Best Practices

1. **Start Small** - Run enrichment on 2-3 pages first to validate workflow
2. **Review Before Commit** - Always review Feynman output before integrating
3. **Keep Provenance** - Don't delete `.provenance.md` files
4. **Iterate** - Run `/lit` then enhance with `/deepresearch` for important topics
5. **Link Back** - Add wikilinks from research outputs to related wiki pages
6. **Update Schema** - Add new tags to SCHEMA.md before using them

## Further Reading

- [Feynman Documentation](https://feynman.is/docs)
- [AlphaXiv CLI](https://alphaxiv.org/)
- [Pi Skills Format](https://github.com/badlogic/pi-skills)
- Wiki `SCHEMA.md` for tag taxonomy
- `skills/AGENTS.md` for agent conventions

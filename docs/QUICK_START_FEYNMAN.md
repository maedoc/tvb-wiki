# Quick Start: Feynman + Wiki Automation

## 🚀 One-Line Summary

```bash
python3 scripts/feynman_wiki_pipeline.py --full
```

This analyzes your wiki, generates Feynman commands, and tells you exactly what to run.

---

## 📋 Current Status

Your wiki has:
- ✅ **122** arXiv papers in `raw/papers/`
- ⚠️ **17** pages with placeholder content needing enrichment
- ✅ **5** comparison page templates created
- ⚠️ **17** orphan pages (no inbound links)

---

## 🎯 Top 5 Enrichment Tasks (Run These)

### 1. Fill NEST Software Page
```bash
/lit "NEST spiking neural network simulator features architecture benchmarks"
```
**Then:** Copy from `outputs/nest-spiking-neural-network*.md` to `entities/nest.md`

### 2. Fill TVB Software Page  
```bash
/lit "The Virtual Brain TVB whole brain simulation platform features"
```
**Then:** Copy to `entities/tvb.md`

### 3. Define Neural Mass Models
```bash
/lit "neural mass models mean field approximation mathematical formulation"
```
**Then:** Copy to `concepts/neural-mass-model.md`

### 4. Explain Jansen-Rit Model
```bash
/deepresearch "Jansen-Rit neural mass model mathematical derivation epilepsy modeling"
```
**Then:** Copy to `concepts/jansen-rit.md`

### 5. Create Software Comparison
```bash
/deepresearch "compare TVB NEST NEURON brain simulation software architecture performance 2024"
```
**Then:** Copy to `comparisons/tvb-vs-nest-vs-neuron.md`

---

## 🔄 Complete Workflow

```bash
# 1. Check what needs work
python3 scripts/enrich_wiki.py

# 2. Run Feynman commands (copy from output above)
# ... run /lit or /deepresearch commands ...

# 3. Integrate outputs
cat outputs/<slug>.md >> entities/<page>.md
# Edit: replace placeholders, add sources[] to frontmatter

# 4. Update index
python3 scripts/update_index.py

# 5. Build and deploy
mkdocs build
git add . && git commit -m "Enriched content via Feynman"
git push origin main
```

---

## 📚 Feynman Commands Cheat Sheet

| Command | Use For | Output |
|---------|---------|--------|
| `/lit "topic"` | Literature review | Cited survey with consensus/disagreements |
| `/deepresearch "topic"` | Deep investigation | Comprehensive research brief |
| `alpha search "query"` | Find papers | Paper list with abstracts |
| `alpha get <id>` | Read paper | Paper details + AI report |
| `alpha ask <id> "question"` | Query paper | Specific answers |
| `/audit <arxiv-id>` | Verify code | Code-claim consistency report |
| `eli5` | Simplify | Plain English explanation |

---

## 🛠️ Helper Scripts

| Script | Purpose | Run When |
|--------|---------|----------|
| `enrich_wiki.py` | Find placeholders | Starting enrichment |
| `alpha_enrich.py` | Find papers | Need citations |
| `generate_comparisons.py` | Create comparison templates | Building comparison pages |
| `update_index.py` | Refresh index + check links | After content updates |
| `feynman_wiki_pipeline.py` | Run all checks | Weekly maintenance |

---

## 📁 Key Files

```
meta/enrichment_plan.json      # List of pages needing content
meta/feynman_commands.sh       # Generated commands to run
meta/alpha_enrichment.json     # Paper recommendations
meta/link_report.txt           # Broken links report

outputs/<slug>.md              # Feynman research outputs
outputs/<slug>.provenance.md   # Source tracking

docs/FEYNMAN_INTEGRATION.md    # Full documentation
```

---

## 💡 Pro Tips

1. **Start with `/lit`** for concept pages - faster than `/deepresearch`
2. **Use `alpha search`** before Feynman to find good paper IDs
3. **Always check** `.provenance.md` files for source verification
4. **Keep wikilinks** when copying - they connect your knowledge graph
5. **Update `sources[]`** in frontmatter for traceability

---

## 🐛 Troubleshooting

**"No alpha command"**
```bash
curl -fsSL https://feynman.is/install-skills | bash
alpha login
```

**"Placeholder still there"**
The script detected it but didn't auto-replace. Manually copy from `outputs/`.

**"Link report shows orphans"**
Add wikilinks from other pages, or run Feynman to generate content that links back.

---

## 🎯 Next Actions

1. ☐ Run the top 5 enrichment commands above
2. ☐ Copy outputs to wiki pages  
3. ☐ Run `python3 scripts/update_index.py`
4. ☐ Commit and push changes
5. ☐ Schedule weekly: `python3 scripts/feynman_wiki_pipeline.py --full`

---

*Full guide: [FEYNMAN_INTEGRATION.md](FEYNMAN_INTEGRATION.md)*

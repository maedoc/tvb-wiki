# Bulk Rewrite Restart Guide

**Written:** 2026-04-27 on duke@local, migrating to rtx4

## What We're Doing

Rewriting 52 thin-narrative wiki pages using `ollama/minimax-m2.5:cloud` via `pi` subprocess calls. Each page gets a full Scholarpedia-level rewrite using the enriched writer prompt from `improver.py`.

## Current Progress

### Completed (written + committed to git):
1. oscillator — 121 → 960w
2. parcellation — 29 → 914w
3. neural-mass-models — 31 → 1087w
4. whole-brain — 49 → 1011w
5. brain-network — 58 → 754w
6. linear — 92 → 892w
7. k-ion-exchange — 149 → 892w
8. epileptor-rs — 151 → 1287w
9. zerlaut — 159 → 1119w
10. stefanescu-jirsa — 157 → 962w
11. infinite-theta — 167 → 850w
12. epileptorcodim3 — 170 → 1294w

### In-progress (NOT recorded, may need re-doing):
- **wong-wang-exc-inh** — pi call was running when session was interrupted. The file on disk may or may not have been written. **Check `concepts/wong-wang-exc-inh.md` word count** — if it's >200w, the rewrite landed but wasn't recorded. Add it to `meta/bulk_rewrite_done.json` manually if so, or just let `--skip-confirmed` not find it and it'll get re-rewritten (harmless, just costs a few minutes).

### Remaining (~38 pages):
All other thin-narrative pages. The script sorts thinnest-first, so the order will be:
wong-wang-exc-inh → ica → nonlinear-dynamics → dynamic-causal-modeling → fokker-planck-equation → ... → neural-mass-model → wilson-cowan → jansen-rit

## Prerequisites on rtx4

1. **pi** must be installed and working: `pi --version`
2. **ollama/minimax-m2.5:cloud** provider must be configured. Test with:
   ```
   pi --model ollama/minimax-m2.5:cloud --mode text -p "Say hello"
   ```
3. **Python 3.10+** with `python-frontmatter` installed:
   ```
   pip3 install python-frontmatter
   ```
4. **Git** initialized in the repo (already is)

## Model Config

The writer model was changed in `scripts/ralph_config.py`:
```python
WRITER_MODEL = "ollama/minimax-m2.5:cloud"  # was "ollama/kimi-k2.5:cloud"
REVIEWER_MODEL = "ollama/glm-5.1:cloud"
REPAIRER_MODEL = "ollama/gpt-oss-120b"
```

This change is committed. The bulk rewrite script uses `--model` flag so it doesn't depend on config.

## How to Resume

```bash
# 1. Start a tmux session
tmux new -s ralph-bulk

# 2. Navigate to the project
cd ~/src/tvb-wiki

# 3. (Optional) Check what's already recorded as done
python3 -c "import json; d=json.load(open('meta/bulk_rewrite_done.json')); print(f'{len(d)} pages done'); [print(f'  {k}') for k in d]"

# 4. Run the bulk rewrite, skipping already-done pages
python3 scripts/bulk_rewrite.py \
  --skip-confirmed \
  --model ollama/minimax-m2.5:cloud \
  --outdir tmp/bulk_rewrite \
  --no-commit \
  2>&1 | tee tmp/bulk_rewrite.log
```

The `--skip-confirmed` flag reads `meta/bulk_rewrite_done.json` and skips any page already listed there. Pages that were rewritten but not recorded (like wong-wang-exc-inh possibly) will simply get re-rewritten — that's harmless.

**Estimated time:** ~38 remaining pages × ~2 min/page ≈ 75-90 minutes.

## After Bulk Rewrite Completes

```bash
# 1. Batch commit all rewritten pages
git add -A concepts/
git commit -m "Bulk rewrite: ~50 thin-narrative pages → Scholarpedia prose (minimax-m2.5)"

# 2. Run mechanical fixers on the newly rewritten pages
python3 scripts/ref_formatter.py        # Fix references
python3 scripts/crosslink_applier.py    # Add crosslinks

# 3. Run auditor to verify improvement
python3 scripts/auditor.py

# 4. Check results
python3 -c "
import json
with open('meta/audit_report.json') as f:
    d = json.load(f)
print(f'Thin narrative pages: {len(d.get(\"thin_narrative\", []))}')
print(f'Missing crosslinks: {len(d.get(\"missing_inline_crosslinks\", []))}')
print(f'Opaque refs: {len(d.get(\"opaque_refs\", []))}')
"

# 5. Commit mechanical fixes
git add -A
git commit -m "Post-rewrite: ref formatting + crosslink pass"
```

## Key Files

| File | Purpose |
|------|---------|
| `scripts/bulk_rewrite.py` | The bulk rewrite script |
| `scripts/improver.py` | Contains `build_writer_prompt()` used by bulk_rewrite |
| `scripts/ralph_config.py` | Model config (WRITER_MODEL now = minimax-m2.5) |
| `meta/bulk_rewrite_done.json` | Tracks which pages have been rewritten |
| `meta/audit_report.json` | Auditor output listing thin pages, broken links, etc. |
| `tmp/bulk_rewrite/` | Debug output: prompts + model outputs for each page |
| `meta/backups/` | Pre-rewrite backups of each page |

## Eval Results (Why minimax-m2.5)

Tested 4 models on wiki page writing quality:
- **minimax-m2.5: ★★★★★** — 1171 avg words, Scholarpedia-level dense prose, best wikilinks
- **gpt-oss-120b: ★★★★☆** — 866 avg words, good but terser, better LaTeX
- **kimi-k2.6: ✗** — outputs meta-commentary instead of content
- **deepseek-v4-flash: ✗** — outputs meta-commentary, no YAML frontmatter

Minimax produces ~50% more content with warmer, more discursive prose in the Scholarpedia register we want.
# Citation Quality Plan for TVB Wiki

## Context

- 900 raw/papers/*.md stubs exist
- 110 broken source refs (pages point to stubs that don't exist)
- 0 raw papers with bad metadata (after our fix)
- 0 duplicate References sections (after our fix)
- Daemon writes pages hourly; citations are LLM-generated and sometimes fabricated

## Phase 1: Shared Verification Library (`scripts/citation_verify.py`)

**Goal:** Reusable CrossRef/OpenAlex lookup functions for all agents.

**Functions:**
- `verify_doi(doi)` → CrossRef lookup (fast, authoritative)
- `verify_title(title)` → OpenAlex title search (fallback)
- `parse_inline_citations(text)` → Extract `Author (year)`, `[^1]`, bare refs
- `find_stub_for_citation(citation)` → Map citation text to existing raw stub
- `get_stub_metadata(path)` → Read raw stub frontmatter
- `format_verdict(metadata)` → NORMALIZED dict (same as sniper.py)

**Strategy:**
- Pure stdlib Python (no deps)
- 150ms sleep between requests (polite pool)
- Returns: `VERIFIED` / `METADATA_MISMATCH` / `NOT_FOUND` / `TIMEOUT`

**Commit:** `Add citation_verify.py shared library`

---

## Phase 2: Citation Guard (Integrate into `scripts/improver.py`)

**Goal:** Before every Improver commit, verify all citations are real.

**How:**
After the LLM writes the revised page:
1. Parse the page body for inline citation mentions
2. Cross-reference with YAML `sources:` frontmatter
3. For each cited paper:
   a. If stub exists → read stub metadata
      - If stub has real authors + year + venue → `VERIFIED`
      - If stub has "unknown" metadata → lookup via CrossRef/OpenAlex
   b. If stub doesn't exist → lookup via CrossRef/OpenAlex
      - If found → auto-create stub (Phase 3) → `VERIFIED`
      - If NOT_FOUND → mark as `FABRICATED`
4. If any `FABRICATED` → **reject this page revision**
   - Log: "Citation guard rejected {slug}: {paper} NOT_FOUND"
   - Do NOT commit
   - Re-queue page for next cycle (will retry with different prompt)
5. If all `VERIFIED` → proceed to commit as normal

**Commit:** `Improver: add citation guard pre-commit check`

---

## Phase 3: Auto-Stub Creation (`scripts/create_paper_stub.py`)

**Goal:** When citation guard finds a paper without a stub, auto-create it.

**Trigger:** Guard step 3b above — missing stub + OpenAlex/CrossRef hit.

**How:**
1. Search OpenAlex by title (or CrossRef by DOI if inline DOI present)
2. If found → normalize metadata:
   - `authors` (list of "First Last" strings)
   - `year`
   - `venue`
   - `doi`
   - `title`
   - `type: source`
   - `tags` (inferred from venue: journal → ['paper-journal'], etc.)
   - `bibtex` (auto-generated from metadata)
3. Write `raw/papers/{slug}.md`
4. Add the stub path to the page's YAML `sources:` frontmatter
5. Git commit: `Auto-create paper stub: {title} (CitationGuard)`

**Slug generation:**
- If DOI: `doi-{doi_normalized}.md`
- If title: `{first-author-surname}-{year}.md`
- Deduplicate: check no existing stub matches same DOI

**Commit:** `Add create_paper_stub.py for auto-creating missing paper stubs`

---

## Phase 4: Daily Audit (Integrate into `scripts/auditor.py`)

**Goal:** Nightly batch-verify all existing raw stubs for drift.

**How:**
In `run_auditor_cycle()`:
1. Build BibTeX from all `raw/papers/*.md` with `bibtex` field
2. For each stub:
   a. If DOI present → verify via CrossRef
   b. Else → verify via OpenAlex title search
   c. Compare returned metadata with stub metadata
   d. Verdict: VERIFIED / METADATA_MISMATCH / NOT_FOUND
3. Report:
   - `raw_papers_bad_metadata`: count of METADATA_MISMATCH
   - `raw_papers_not_found`: count of NOT_FOUND (potential hallucinations)
   - Write detailed report to `meta/citation_audit.json`
4. Git commit audit report

**Commit:** `Auditor: add daily citation verification of all raw stubs`

---

## Phase 5: One-Off Full Wiki Audit

**Goal:** Scan the entire current wiki for fabricated/missing citations.

**How:**
1. Extract every inline citation from all concept/entity/comparison pages
2. Build a list of unique cited papers
3. For each unique paper:
   a. Check if raw stub exists with real metadata → VERIFIED
   b. If no stub → lookup via CrossRef/OpenAlex
   c. If NOT_FOUND → potential fabrication
4. Generate report:
   - **P0 (Red):** Inline citations with NO stub + NOT_FOUND in databases
   - **P1 (Yellow):** Stubs with METADATA_MISMATCH  
   - **P2 (Green):** Verified
5. Optionally feed P0 items to RefChecker for deep hallucination check

**Commit:** `Add one-off citation audit across all wiki pages`

---

## Execution Order

| Phase | File | Risk | Time |
|-------|------|------|------|
| 1 | `scripts/citation_verify.py` | Low | 1h |
| 2 | Integrate into `scripts/improver.py` | Medium (could reject valid pages) | 1h |
| 3 | `scripts/create_paper_stub.py` + integrate | Medium | 1h |
| 4 | Integrate into `scripts/auditor.py` | Low | 30m |
| 5 | One-off audit report | Low | 30m |

**Total:** ~4 hours

## Rollback Plan

- Phase 2 guard: make it **non-blocking at first** (log only, don't reject)
  - Run for 48h, review logs
  - If false-positive rate <5%, switch to blocking
- Phase 3 auto-create: always create stubs, never delete existing ones

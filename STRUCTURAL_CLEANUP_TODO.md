# TVB Wiki Structural Cleanup — TODO List

Generated after full audit of 509 pages. Daemon stopped.

---

## Phase 1: Script-Only Fixes (execute now)

| # | Issue | Count | Fix | Risk |
|---|-------|-------|-----|------|
| 1.1 | **Double References** — pages with both YAML `sources:` AND body `## References` | 488 | Script strips `## References` section from body. YAML `sources:` render via `obsidian_support.py` hook at build time. | Low — body refs are redundant formatted versions of same YAML stubs |
| 1.2 | **Empty hardcoded refs** — thin stubs with empty `## References` section | 15 | Strip empty `## References` heading | None |
| 1.3 | **Leaked frontmatter** — `title:` or `---` appearing in body | 8 | Parse with `frontmatter`, strip leaked YAML block, merge lost metadata | Low |
| 1.4 | **Missing `title` field** — index pages lacking frontmatter title | 3 | Add `title:` to `entities/index.md`, `concepts/index.md`, `comparisons/index.md` | None |
| 1.5 | **Empty body** — `comparisons/index.md` has 9 words | 1 | Write proper index content | None |
| 1.6 | **Regex tone flag** — scan all 509 pages for conversational/promotional language | 509 | Regex scan for patterns like "I think", "you should", "let me explain", "as you can see", "it is important to note". Output JSON hit list. | None (read-only) |

**Phase 1 commit message:** `Structural cleanup: remove double references, fix leaked frontmatter, add missing titles`

---

## Phase 2: Hybrid (Script + Selective LLM Review)

| # | Issue | Count | Approach |
|---|-------|-------|----------|
| 2.1 | **Thin content pages** (< 100 words) | 55 | Script generates batch prompts for LLM reviewer: "Evaluate if this stub is worth keeping, expanding, or deleting. Consider: does it cover a real tool/concept? Is the namespace overlap with another page?" Output: `keep` / `expand` / `delete` / `merge` |
| 2.2 | **Tone-flagged pages** (from Phase 1.6) | ~? | LLM reads flagged pages, confirms if actually non-wiki-like or false positive. Output: `fix` / `false_positive` |
| 2.3 | **Meta-commentary contamination** | 0 currently | Script checks for new contamination post-cleanup. If found: LLM rewrites affected paragraphs only |

**Phase 2 commit message:** `Audit: thin content triage + tone cleanup`

---

## Phase 3: Daemon Restart with Guardrails

| # | Guardrail | Implementation |
|---|-----------|----------------|
| 3.1 | **Never write `## References` in body** | Add to writer prompt: "All citations go into YAML frontmatter `sources:`. Never add a `## References` section to the body." |
| 3.2 | **Post-write structural check** | After writer outputs, script checks: if body contains `## References` → reject and retry |
| 3.3 | **Post-write frontmatter leak check** | If body starts with `title:` or `---` → reject and retry |
| 3.4 | **Cooldown on structural rejections** | 3 strikes = 24h cooldown |

---

## Expected Outcomes

| Metric | Before | After Phase 1 | After Phase 2 |
|--------|--------|---------------|---------------|
| Double references | 488 | 0 | 0 |
| Leaked frontmatter | 8 | 0 | 0 |
| Empty hardcoded refs | 15 | 0 | 0 |
| Missing title | 3 | 0 | 0 |
| Empty body | 1 | 0 | 0 |
| Thin content (<100w) | 55 | 55 | ~20-30 (after triage) |
| Meta-commentary | 0 | 0 | 0 |
| YAML parse errors | 0 | 0 | 0 |

---

## Execution Status

- [x] Daemon stopped
- [x] Full structural audit completed
- [x] TODO list written
- [ ] Phase 1.1: Strip double references from 488 pages
- [ ] Phase 1.2: Strip empty refs from 15 pages
- [ ] Phase 1.3: Fix leaked frontmatter in 8 pages
- [ ] Phase 1.4: Add titles to 3 index pages
- [ ] Phase 1.5: Fix empty comparisons/index.md
- [ ] Phase 1.6: Regex tone flag all pages
- [ ] Commit Phase 1
- [ ] Phase 2.1: LLM triage of 55 thin pages
- [ ] Phase 2.2: LLM review of tone flags
- [ ] Commit Phase 2
- [ ] Phase 3: Restart daemon with guardrails

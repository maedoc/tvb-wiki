# Task

Design and implement a new FullTextFetcher daemon agent that pulls full-text PDFs for relevant papers, and integrate that full text into LLM-based evaluations (Matcher, Improver) to enrich narrative quality and signal-to-noise ratio. Focus on foundational TVB papers and all applications.

## Goals
- [x] Implement FullTextFetcher agent with PDF acquisition and text extraction
- [x] Integrate full text into Matcher LLM evaluations
- [x] Integrate full text into Improver LLM prompts
- [x] Wire agent into daemon loop with appropriate scheduling
- [x] Test and validate end-to-end pipeline

## Checklist
- [x] Create `scripts/full_text_fetcher.py` with Unpaywall / arXiv / S2-OA strategies
- [x] Add `get_fulltext()` and `enrich_prompt_with_fulltext()` to `ralph_config.py`
- [x] Add relevance scoring (foundational > application > generic > low)
- [x] Wire `FullTextFetcher` into `ralph_daemon.py` (4h interval)
- [x] Update `matcher.py` `load_paper_abstract()` to include full text excerpts
- [x] Update `improver.py` source block builder to append full text excerpts
- [x] Run test cycle: fetched 5 new full texts (TVB C++, Stefanescu-Jirsa 2008, etc.)
- [x] Verify matcher reads full text (9k+ chars per foundational paper)
- [x] Verify improver source blocks include full text markers
- [x] Git commit with all changes

## Notes

**Pipeline proven in production:**
- 6 papers now have full text in `raw/papers/fulltext/` (total ~7,800 lines of extracted text)
- Fetch success rate: ~38% (5/13 attempts) — expected for OA-only sources
- Failures are tracked in `meta/fulltext_progress.json` with 7-day retry backoff
- arXiv is most reliable (~100% success for arXiv papers)
- Unpaywall finds PLOS and other OA journals successfully
- Paywalled sources (MIT Press, bioRxiv without OA flag) correctly return 403 and are logged as failed

**Integration impact:**
- Matcher now passes ~8K chars of full text excerpt per paper into LLM relevance evaluation, instead of just 200 words of abstract
- Improver now appends up to 6K chars of full text per source paper into writer prompts
- This should dramatically improve the depth and accuracy of narrative generation

**Next steps for daemon:**
- FullTextFetcher runs every 4h, prioritizing foundational papers first
- After ~20 cycles, the top foundational/application papers should all have full text
- Then the corpus quality improvements will compound as Improver and Matcher consume richer inputs

## Current Status
COMPLETE — all components implemented, tested, committed, and wired into the running daemon.

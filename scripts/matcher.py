#!/usr/bin/env python3
"""
Ralph Matcher Agent — embedding-based source matching for wiki pages.

Pipeline:
  1. Extract sentences from wiki pages + raw papers
  2. Embed via Ollama (embeddinggemma, 768-dim)
  3. Cosine similarity: find nearest paper sentences per wiki sentence
  4. Aggregate sentence-level hits → paper-level relevance scores
  5. LLM evaluates top-10 candidates per page → confirmed matches
  6. Write confirmed sources to page frontmatter

Usage:
  python3 scripts/matcher.py              # full cycle: embed + match + evaluate + attach
  python3 scripts/matcher.py --build-only # rebuild embedding index only
  python3 scripts/matcher.py --match-only # match + evaluate (assumes index exists)
  python3 scripts/matcher.py --eval-only  # evaluate candidates from last match
"""
import os
import re
import sys
import json
import time
import hashlib
import datetime
import urllib.request
import urllib.error
import frontmatter
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, RAW_PAPERS_DIR,
    ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    META_DIR, get_all_pages, read_page, get_sources,
    run_pi, WRITER_MODEL, git_commit, append_log,
)

log = get_logger("Matcher")

# ── Config ─────────────────────────────────────────────────────────────

EMBED_DIR = os.path.join(META_DIR, "embeddings")
EMBED_MODEL = "embeddinggemma:latest"
EMBED_DIM = 768
EMBED_BATCH = 500  # sentences per Ollama API call
EMBED_URL = "http://localhost:11434/api/embed"

WIKI_EMBED_FILE = os.path.join(EMBED_DIR, "wiki_embeddings.npy")
PAPER_EMBED_FILE = os.path.join(EMBED_DIR, "paper_embeddings.npy")
WIKI_INDEX_FILE = os.path.join(EMBED_DIR, "wiki_index.json")
PAPER_INDEX_FILE = os.path.join(EMBED_DIR, "paper_index.json")
MATCH_RESULTS_FILE = os.path.join(EMBED_DIR, "match_results.json")
HASH_FILE = os.path.join(EMBED_DIR, "content_hashes.json")

TOP_CANDIDATES = 10  # papers to surface per page for LLM evaluation
MAX_CONFIRMED = 5    # max sources to attach per page
SIM_THRESHOLD = 0.35 # minimum cosine similarity for sentence-level match

# Auto-confirm thresholds: skip LLM if the top match is this strong
AUTO_CONFIRM_SIM = 0.65  # top similarity score
AUTO_CONFIRM_MATCHING = 4 # matching sentences

# Batch evaluation: evaluate this many pages per LLM call
EVAL_BATCH_SIZE = 5


# ── Sentence extraction ────────────────────────────────────────────────

def extract_sentences(text: str, min_len: int = 30) -> list[str]:
    """Extract meaningful sentences from text, stripping frontmatter."""
    # Strip YAML frontmatter
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            text = text[end + 4:]

    # Strip code blocks (math formulas etc.)
    text = re.sub(r'```[\s\S]*?```', '', text)

    # Strip reference sections entirely
    text = re.sub(r'(?m)^##\s*References.*', '', text)
    text = re.sub(r'(?m)^\d+\.\s+https?://\S+', '', text)
    text = re.sub(r'(?m)^\*\*Authors?:\*\*.*', '', text)
    text = re.sub(r'(?m)^\*\*Year:\*\*.*', '', text)
    text = re.sub(r'(?m)^\*\*Venue:\*\*.*', '', text)

    # Split on sentence-ending punctuation or double newlines
    raw = re.split(r'(?<=[.!?])\s+|\n\n+', text)

    sentences = []
    for s in raw:
        s = s.strip()
        # Skip short, heading-only, table lines, list-only fragments
        if len(s) < min_len:
            continue
        if s.startswith('#') or s.startswith('|--') or s.startswith('|'):
            continue
        if s.startswith('- ') and '.' not in s[2:]:
            continue  # bullet without full sentence
        if s.count('|') > 3:
            continue  # table row
        if s.startswith('**') and s.endswith('**'):
            continue  # bold-only label
        # Skip URLs, DOIs, citation fragments
        if re.match(r'https?://', s):
            continue
        if re.match(r'\d+\.$', s.strip()):
            continue
        if 'doi.org' in s or 'doi:' in s.lower():
            continue
        # Skip fragments that are just author names + year
        if re.match(r'^[A-Z][a-z].*\d{4}\.$', s) and len(s) < 80:
            continue
        # Clean up markdown artifacts
        s = re.sub(r'\[\[([^\]|]+)\|?[^\]]*\]\]', r'\1', s)  # wikilinks → text
        s = re.sub(r'\*([^*]+)\*', r'\1', s)  # bold
        s = re.sub(r'`([^`]+)`', r'\1', s)    # inline code
        # Strip leading bullets
        s = re.sub(r'^[-*]\s+', '', s)
        if len(s) >= min_len:
            sentences.append(s)

    return sentences


def _file_hash(path: str) -> str:
    """MD5 hash of file BODY (excluding frontmatter) for incremental updates."""
    with open(path, 'rb') as f:
        text = f.read().decode('utf-8', errors='replace')
    # Strip YAML frontmatter - only hash body content
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            text = text[end + 4:]
    h = hashlib.md5()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


# ── Embedding ──────────────────────────────────────────────────────────

def embed_texts(texts: list[str]) -> np.ndarray:
    """Embed a list of texts via Ollama API. Returns (n, dim) float32 array."""
    if not texts:
        return np.zeros((0, EMBED_DIM), dtype=np.float32)

    all_embeddings = []

    for i in range(0, len(texts), EMBED_BATCH):
        batch = texts[i:i + EMBED_BATCH]
        payload = json.dumps({
            "model": EMBED_MODEL,
            "input": batch
        }).encode('utf-8')

        req = urllib.request.Request(
            EMBED_URL, data=payload,
            headers={"Content-Type": "application/json"}
        )

        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.loads(resp.read())
                embeddings = np.array(data["embeddings"], dtype=np.float32)
                all_embeddings.append(embeddings)
                break
            except (urllib.error.URLError, urllib.error.HTTPError) as e:
                if attempt < 2:
                    log.warn("Embed API error (attempt %d): %s, retrying in 5s",
                             attempt + 1, str(e)[:100])
                    time.sleep(5)
                else:
                    raise
            except Exception as e:
                raise

        if (i + EMBED_BATCH) % 1000 == 0 or i + EMBED_BATCH >= len(texts):
            log.info("Embedded %d/%d sentences", min(i + EMBED_BATCH, len(texts)), len(texts))

    return np.vstack(all_embeddings) if all_embeddings else np.zeros((0, EMBED_DIM), dtype=np.float32)


def build_index_for_directory(directory: str, embed_path: str, index_path: str,
                              hashes: dict | None = None) -> tuple[np.ndarray, list[dict]]:
    """
    Build sentence embeddings for all .md files in a directory.

    Returns (embeddings array, index list) where each index entry is:
        {"file": relative_path, "slug": name, "sentences": [str, ...], "offset": int, "count": int}

    If hashes dict is provided and content hasn't changed, skip re-embedding.
    """
    files = sorted(
        f for f in os.listdir(directory)
        if f.endswith('.md') and f != 'index.md'
    )

    index = []
    all_sentences = []
    offsets = []
    old_hashes = hashes or {}

    # Track which files need embedding
    to_embed = []  # (file_idx, sentences)
    # Track which can reuse existing embeddings
    reuse_map = {}  # file_idx → (old_offset, old_count)

    # Load existing embeddings if available
    existing_emb = None
    existing_idx = []
    if os.path.exists(embed_path) and os.path.exists(index_path):
        try:
            existing_emb = np.load(embed_path)
            with open(index_path, 'r') as f:
                existing_idx = json.load(f)
        except Exception:
            existing_emb = None
            existing_idx = []

    for fi, fn in enumerate(files):
        filepath = os.path.join(directory, fn)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        sentences = extract_sentences(text)
        current_hash = _file_hash(filepath)

        if current_hash == old_hashes.get(fn) and existing_emb is not None:
            # Content unchanged — find old embedding range
            for entry in existing_idx:
                if entry.get('file') == fn:
                    reuse_map[fi] = (entry['offset'], entry['count'])
                    break
            else:
                # Hash matches but no old entry — embed fresh
                to_embed.append((fi, sentences))
        else:
            to_embed.append((fi, sentences))

    if not to_embed and existing_emb is not None and len(existing_idx) == len(files):
        # Everything unchanged, just return existing
        log.info("All %d files unchanged, reusing existing embeddings", len(files))
        return existing_emb, existing_idx

    log.info("Embedding %d/%d files (%d sentences)",
             len(to_embed), len(files),
             sum(len(s) for _, s in to_embed))

    # Embed new/changed files
    new_sentences = []
    new_offsets = []
    for fi, sents in to_embed:
        new_offsets.append((fi, len(new_sentences), len(sents)))
        new_sentences.extend(sents)

    new_embeddings = embed_texts(new_sentences) if new_sentences else np.zeros((0, EMBED_DIM), dtype=np.float32)

    # Build final combined index
    # For simplicity on first build (or major changes), just rebuild everything
    if not existing_emb or len(to_embed) > len(files) * 0.3:
        # Rebuild from scratch — embed everything
        log.info("Rebuilding full index (%d files)", len(files))
        all_sents = []
        entries = []
        offset = 0
        for fi, fn in enumerate(files):
            filepath = os.path.join(directory, fn)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            sents = extract_sentences(text)
            entries.append({
                "file": fn,
                "slug": fn[:-3],
                "sentences": sents,
                "offset": offset,
                "count": len(sents),
            })
            all_sents.extend(sents)
            offset += len(sents)

        embeddings = embed_texts(all_sents) if all_sents else np.zeros((0, EMBED_DIM), dtype=np.float32)
        return embeddings, entries
    else:
        # Patch existing index — not worth the complexity for this scale
        # Just rebuild everything
        log.info("Rebuilding full index (%d files, %d changed)", len(files), len(to_embed))
        all_sents = []
        entries = []
        offset = 0
        for fi, fn in enumerate(files):
            filepath = os.path.join(directory, fn)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            sents = extract_sentences(text)
            entries.append({
                "file": fn,
                "slug": fn[:-3],
                "sentences": sents,
                "offset": offset,
                "count": len(sents),
            })
            all_sents.extend(sents)
            offset += len(sents)

        embeddings = embed_texts(all_sents) if all_sents else np.zeros((0, EMBED_DIM), dtype=np.float32)
        return embeddings, entries


def build_all_indexes(force_rebuild: bool = False):
    """Build embedding indexes for wiki pages and raw papers.
    Skips embedding entirely if indexes exist and content hasn't changed.
    """
    os.makedirs(EMBED_DIR, exist_ok=True)

    # Load content hashes for incremental detection
    hashes = {}
    if os.path.exists(HASH_FILE):
        try:
            with open(HASH_FILE, 'r') as f:
                hashes = json.load(f)
        except Exception:
            pass

    new_hashes = {}

    # ── Wiki pages ──
    wiki_sentences = []
    wiki_entries = []
    offset = 0

    wiki_changed = force_rebuild or not os.path.exists(WIKI_EMBED_FILE)

    for src_dir, label in [
        (ENTITIES_DIR, "entities"),
        (CONCEPTS_DIR, "concepts"),
        (COMPARISONS_DIR, "comparisons"),
    ]:
        if not os.path.isdir(src_dir):
            continue
        files = sorted(f for f in os.listdir(src_dir) if f.endswith('.md') and f != 'index.md')
        for fn in files:
            filepath = os.path.join(src_dir, fn)
            h = _file_hash(filepath)
            new_hashes[f"wiki/{label}/{fn}"] = h
            if h != hashes.get(f"wiki/{label}/{fn}"):
                wiki_changed = True

    # ── Raw papers ──
    paper_changed = force_rebuild or not os.path.exists(PAPER_EMBED_FILE)

    if os.path.isdir(RAW_PAPERS_DIR):
        files = sorted(f for f in os.listdir(RAW_PAPERS_DIR) if f.endswith('.md'))
        for fn in files:
            filepath = os.path.join(RAW_PAPERS_DIR, fn)
            h = _file_hash(filepath)
            new_hashes[f"paper/{fn}"] = h
            if h != hashes.get(f"paper/{fn}"):
                paper_changed = True

    if not wiki_changed and not paper_changed:
        log.info("All content unchanged, skipping embedding")
        return

    start = time.time()

    # ── Rebuild wiki index if changed ──
    if wiki_changed:
        for src_dir, label in [
            (ENTITIES_DIR, "entities"),
            (CONCEPTS_DIR, "concepts"),
            (COMPARISONS_DIR, "comparisons"),
        ]:
            if not os.path.isdir(src_dir):
                continue
            files = sorted(f for f in os.listdir(src_dir) if f.endswith('.md') and f != 'index.md')
            for fn in files:
                filepath = os.path.join(src_dir, fn)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                sents = extract_sentences(text)
                wiki_entries.append({
                    "file": fn,
                    "dir": label,
                    "slug": fn[:-3],
                    "path": os.path.join(src_dir, fn),
                    "offset": offset,
                    "count": len(sents),
                })
                wiki_sentences.extend(sents)
                offset += len(sents)

        log.info("Wiki: %d pages, %d sentences", len(wiki_entries), len(wiki_sentences))

        if wiki_sentences:
            wiki_emb = embed_texts(wiki_sentences)
            np.save(WIKI_EMBED_FILE, wiki_emb)
            with open(WIKI_INDEX_FILE, 'w') as f:
                json.dump(wiki_entries, f, indent=2)
            log.info("Wiki embeddings saved: %s (%.1f MB)",
                     WIKI_EMBED_FILE, wiki_emb.nbytes / 1024 / 1024)
    else:
        log.info("Wiki unchanged, reusing existing embeddings")

    # ── Rebuild paper index if changed ──
    if paper_changed:
        paper_sentences = []
        paper_entries = []
        offset = 0

        if os.path.isdir(RAW_PAPERS_DIR):
            files = sorted(f for f in os.listdir(RAW_PAPERS_DIR) if f.endswith('.md'))
            for fn in files:
                filepath = os.path.join(RAW_PAPERS_DIR, fn)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                sents = extract_sentences(text)
                paper_entries.append({
                    "file": fn,
                    "slug": fn[:-3],
                    "offset": offset,
                    "count": len(sents),
                })
                paper_sentences.extend(sents)
                offset += len(sents)

        log.info("Papers: %d files, %d sentences", len(paper_entries), len(paper_sentences))

        if paper_sentences:
            paper_emb = embed_texts(paper_sentences)
            np.save(PAPER_EMBED_FILE, paper_emb)
            with open(PAPER_INDEX_FILE, 'w') as f:
                json.dump(paper_entries, f, indent=2)
            log.info("Paper embeddings saved: %s (%.1f MB)",
                     PAPER_EMBED_FILE, paper_emb.nbytes / 1024 / 1024)
    else:
        log.info("Papers unchanged, reusing existing embeddings")

    # Save hashes
    with open(HASH_FILE, 'w') as f:
        json.dump(new_hashes, f, indent=2)

    elapsed = time.time() - start
    log.info("Index build complete in %.1f s", elapsed)


# ── Matching ───────────────────────────────────────────────────────────

def normalize(v: np.ndarray) -> np.ndarray:
    """L2-normalize vectors row-wise."""
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-8)
    return v / norms


def find_candidates(top_n: int = TOP_CANDIDATES,
                    sim_threshold: float = SIM_THRESHOLD) -> dict[str, list[dict]]:
    """
    For each wiki page, find the most relevant raw papers using embedding similarity.

    Returns {page_slug: [{"paper": paper_slug, "score": float, "top_sim": float, "matching_sents": int}, ...]}
    """
    # Load embeddings
    wiki_emb = np.load(WIKI_EMBED_FILE)
    paper_emb = np.load(PAPER_EMBED_FILE)

    with open(WIKI_INDEX_FILE) as f:
        wiki_idx = json.load(f)
    with open(PAPER_INDEX_FILE) as f:
        paper_idx = json.load(f)

    log.info("Matching %d wiki entries against %d paper entries",
             len(wiki_idx), len(paper_idx))

    if wiki_emb.shape[0] == 0 or paper_emb.shape[0] == 0:
        log.warn("Empty embeddings, nothing to match")
        return {}

    # Normalize
    wiki_norm = normalize(wiki_emb)
    paper_norm = normalize(paper_emb)

    # Full similarity matrix: (n_wiki_sents, n_paper_sents)
    log.info("Computing similarity matrix (%d × %d)...", wiki_norm.shape[0], paper_norm.shape[0])
    start = time.time()
    sims = wiki_norm @ paper_norm.T  # cosine similarities
    log.info("Similarity matrix computed in %.1fs", time.time() - start)

    # For each wiki page, aggregate sentence-level matches into paper scores
    results = {}

    for entry in wiki_idx:
        slug = entry["slug"]
        w_off = entry["offset"]
        w_cnt = entry["count"]

        if w_cnt == 0:
            continue

        # Get similarity slice for this page's sentences
        page_sims = sims[w_off:w_off + w_cnt]  # (n_page_sents, n_paper_sents)

        # For each paper, compute aggregated score
        paper_scores = {}

        for pentry in paper_idx:
            p_off = pentry["offset"]
            p_cnt = pentry["count"]
            p_slug = pentry["slug"]

            if p_cnt == 0:
                continue

            # Slice the similarity sub-matrix for this paper
            sub_sims = page_sims[:, p_off:p_off + p_cnt]  # (n_page_sents, n_paper_sents)

            # Count how many wiki sentences have at least one good match in this paper
            max_per_wiki = sub_sims.max(axis=1)  # best match per wiki sentence
            matching = int((max_per_wiki >= sim_threshold).sum())

            if matching == 0:
                continue

            # Score = sum of top-3 sentence similarities × matching bonus
            top_sims = np.sort(max_per_wiki)[-3:]
            score = float(top_sims.mean()) * (1 + 0.1 * matching)

            paper_scores[p_slug] = {
                "paper": p_slug,
                "score": score,
                "top_sim": float(max_per_wiki.max()),
                "matching_sents": matching,
            }

        if paper_scores:
            # Sort by score descending, take top N
            ranked = sorted(paper_scores.values(), key=lambda x: x["score"], reverse=True)
            results[slug] = ranked[:top_n]

    # Save raw results
    with open(MATCH_RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)

    total = sum(len(v) for v in results.values())
    log.info("Matched %d pages with %d total candidates (saved to %s)",
             len(results), total, MATCH_RESULTS_FILE)

    return results


# ── LLM Evaluation ────────────────────────────────────────────────────

def load_paper_abstract(paper_slug: str) -> str:
    """Load the title and first ~200 words of a paper's content."""
    paper_path = os.path.join(RAW_PAPERS_DIR, f"{paper_slug}.md")
    if not os.path.exists(paper_path):
        return f"(paper file not found: {paper_slug})"

    try:
        with open(paper_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Extract title from frontmatter
        title = paper_slug
        if text.startswith('---'):
            end = text.find('---', 3)
            if end != -1:
                fm = text[:end]
                m = re.search(r'title:\s*["\']?(.+?)["\']?\n', fm)
                if m:
                    title = m.group(1).strip('"\'')
                text = text[end + 4:]

        # Take first ~200 words of body
        words = text.split()[:200]
        body = ' '.join(words)
        return f"Title: {title}\nAbstract: {body}"
    except Exception as e:
        return f"(error reading {paper_slug}: {e})"


def _auto_confirm(candidates: list[dict]) -> list[str] | None:
    """Auto-confirm if top candidate is very strong. Returns slugs or None (needs LLM)."""
    if not candidates:
        return []
    top = candidates[0]
    if top['top_sim'] >= AUTO_CONFIRM_SIM and top['matching_sents'] >= AUTO_CONFIRM_MATCHING:
        # Strong match — take top candidates that also meet a lower bar
        confirmed = []
        for c in candidates:
            if c['top_sim'] >= 0.50 and c['matching_sents'] >= 2:
                confirmed.append(c['paper'])
            if len(confirmed) >= MAX_CONFIRMED:
                break
        return confirmed
    return None  # needs LLM


def evaluate_page_candidates(slug: str, candidates: list[dict]) -> list[str]:
    """
    Evaluate whether candidate papers are actually relevant to a wiki page.
    Auto-confirms high-confidence matches; falls back to LLM for ambiguous cases.
    Returns list of confirmed paper slugs.
    """
    # Try auto-confirm first
    auto = _auto_confirm(candidates)
    if auto is not None:
        log.info("Auto-confirmed %d sources for %s (top_sim=%.2f)",
                 len(auto), slug, candidates[0]['top_sim'])
        return auto

    # Need LLM evaluation
    pages = get_all_pages()
    if slug not in pages:
        log.warn("Page %s not found in index", slug)
        return []

    filepath = pages[slug]
    try:
        metadata, content = read_page(filepath)
    except Exception:
        return []

    page_title = metadata.get('title', slug)
    page_context = ' '.join(content.split()[:150])

    # Build candidate descriptions
    candidate_texts = []
    for i, c in enumerate(candidates[:TOP_CANDIDATES], 1):
        abstract = load_paper_abstract(c["paper"])
        candidate_texts.append(
            f"Paper {i}: [{c['paper']}] (similarity: {c['top_sim']:.2f}, "
            f"matching sentences: {c['matching_sents']})\n{abstract}"
        )

    candidates_block = '\n\n'.join(candidate_texts)

    prompt = f"""You are evaluating whether academic papers are relevant to a specific wiki page.

## Wiki Page: "{page_title}" (slug: {slug})
Page context: {page_context}

## Candidate Papers (found via semantic similarity):
{candidates_block}

## Task
For each paper, determine if it is genuinely relevant to the topic of this wiki page.
A paper is relevant if it directly discusses, uses, or contributes to the topic.

Reply with ONLY a JSON object like:
{{"evaluations": [{{"paper": "slug", "relevant": true, "reason": "brief reason"}}, ...]}}

Be strict: only mark papers that are clearly topically relevant. Consider the specific domain of The Virtual Brain (TVB), whole-brain modeling, connectomics, and computational neuroscience."""

    success, output = run_pi(prompt, model=WRITER_MODEL)

    if not success:
        log.warn("LLM evaluation failed for %s: %s", slug, output[:100])
        return []

    # Parse LLM output
    try:
        json_match = re.search(r'\{[\s\S]*\}', output)
        if json_match:
            data = json.loads(json_match.group())
            evaluations = data.get('evaluations', [])
            confirmed = [
                e['paper'] for e in evaluations
                if e.get('relevant', False) and 'paper' in e
            ]
            return confirmed[:MAX_CONFIRMED]
    except (json.JSONDecodeError, KeyError) as e:
        log.warn("Could not parse LLM evaluation for %s: %s", slug, str(e)[:100])

    # Fallback: take top 3 by similarity
    log.warn("Falling back to similarity-only for %s", slug)
    return [c["paper"] for c in candidates[:3]]


def evaluate_batch(pages_to_eval: list[tuple[str, list[dict]]]) -> dict[str, list[str]]:
    """
    Evaluate multiple pages in one LLM call. Returns {slug: [confirmed_slugs]}.
    Falls back to per-page evaluation for any that fail.
    """
    if not pages_to_eval:
        return {}

    all_pages = get_all_pages()
    batch_blocks = []
    slug_list = []

    for slug, candidates in pages_to_eval:
        if slug not in all_pages:
            continue
        filepath = all_pages[slug]
        try:
            metadata, content = read_page(filepath)
        except Exception:
            continue

        page_title = metadata.get('title', slug)
        page_context = ' '.join(content.split()[:100])

        paper_lines = []
        for i, c in enumerate(candidates[:TOP_CANDIDATES], 1):
            paper_lines.append(
                f"  {i}. [{c['paper']}] (sim={c['top_sim']:.2f}, matches={c['matching_sents']})"
            )
        papers_block = '\n'.join(paper_lines)

        batch_blocks.append(
            f"### Page: {slug} (\"{page_title}\")\n"
            f"Context: {page_context}\n"
            f"Candidates:\n{papers_block}"
        )
        slug_list.append(slug)

    if not batch_blocks:
        return {}

    prompt = f"""You are evaluating whether candidate academic papers are relevant to wiki pages.
For each page, identify which candidates are genuinely topically relevant.

{chr(10).join(batch_blocks)}

Reply with ONLY a JSON object:
{{"results": {{"page_slug": ["confirmed_paper_slug", ...], ...}}}}

Be strict. Only include papers that clearly discuss the page's topic.
Domain: The Virtual Brain, whole-brain modeling, connectomics, computational neuroscience."""

    success, output = run_pi(prompt, model=WRITER_MODEL)

    if not success:
        log.warn("Batch evaluation failed, falling back to per-page")
        results = {}
        for slug, candidates in pages_to_eval:
            results[slug] = evaluate_page_candidates(slug, candidates)
        return results

    try:
        json_match = re.search(r'\{[\s\S]*\}', output)
        if json_match:
            data = json.loads(json_match.group())
            results = data.get('results', {})
            # Limit per page
            return {k: v[:MAX_CONFIRMED] for k, v in results.items() if isinstance(v, list)}
    except (json.JSONDecodeError, KeyError) as e:
        log.warn("Batch parse failed: %s", str(e)[:100])

    # Fallback to per-page
    results = {}
    for slug, candidates in pages_to_eval:
        results[slug] = evaluate_page_candidates(slug, candidates)
    return results


# ── Source attachment ──────────────────────────────────────────────────

def attach_sources(slug: str, confirmed_papers: list[str]) -> bool:
    """
    Write confirmed paper sources to a wiki page's frontmatter.
    Only adds new sources — doesn't remove existing ones.
    Returns True if any sources were added.
    """
    pages = get_all_pages()
    if slug not in pages:
        return False

    filepath = pages[slug]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
    except Exception as e:
        log.error("Cannot load %s: %s", slug, e)
        return False

    existing = set(get_sources(dict(post.metadata)))
    new_sources = []

    for paper_slug in confirmed_papers:
        source_path = f"raw/papers/{paper_slug}.md"
        if source_path not in existing and paper_slug not in existing:
            new_sources.append(source_path)

    if not new_sources:
        return False

    # Update frontmatter
    current_sources = list(post.metadata.get('sources', []))
    if isinstance(current_sources, str):
        current_sources = [s.strip() for s in current_sources.split(',') if s.strip()]
    current_sources.extend(new_sources)
    post.metadata['sources'] = current_sources
    post.metadata['updated'] = datetime.date.today().isoformat()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))

    log.info("Attached %d sources to %s: %s", len(new_sources), slug, ', '.join(new_sources))
    return True


# ── Main matcher cycle ────────────────────────────────────────────────

def run_matcher_cycle(force_rebuild: bool = False, eval_pages: int | None = None) -> dict:
    """
    Run a full matcher cycle:
      1. Build/update embedding index (or skip if unchanged)
      2. Find candidates via cosine similarity
      3. Evaluate candidates with LLM
      4. Attach confirmed sources

    Returns stats dict.
    """
    stats = {
        "pages_matched": 0,
        "pages_with_new_sources": 0,
        "total_new_sources": 0,
        "pages_evaluated": 0,
        "pages_needing_research": [],
    }

    os.makedirs(EMBED_DIR, exist_ok=True)

    # Step 1: Build index if needed (skips if nothing changed)
    if force_rebuild or not os.path.exists(WIKI_EMBED_FILE) or not os.path.exists(PAPER_EMBED_FILE):
        log.info("Building embedding indexes...")
        build_all_indexes(force_rebuild=force_rebuild)
    else:
        log.info("Checking for content changes...")
        build_all_indexes()

    # Step 2: Find candidates
    if not os.path.exists(PAPER_EMBED_FILE):
        log.warn("No paper embeddings, nothing to match")
        return stats

    candidates = find_candidates()

    if not candidates:
        log.info("No candidates found")
        return stats

    stats["pages_matched"] = len(candidates)

    # Step 3: Evaluate and attach
    # Prioritize pages that currently have no sources
    all_pages = get_all_pages()
    unsourced = []
    sourced = []
    auto_confirmed_count = 0

    for slug, cands in candidates.items():
        if slug not in all_pages:
            continue
        filepath = all_pages[slug]
        try:
            metadata, _ = read_page(filepath)
            existing_sources = get_sources(metadata)
            if not existing_sources:
                unsourced.append((slug, cands))
            else:
                sourced.append((slug, cands))
        except Exception:
            continue

    # Process unsourced pages first
    to_eval = unsourced + sourced
    if eval_pages:
        to_eval = to_eval[:eval_pages]

    log.info("Evaluating %d pages (%d unsourced, %d sourced)",
             len(to_eval), len(unsourced), len(sourced))

    # Phase A: auto-confirm high-confidence matches (instant, no LLM)
    needs_llm = []
    for slug, cands in to_eval:
        if not cands:
            stats["pages_needing_research"].append(slug)
            continue

        auto = _auto_confirm(cands)
        if auto is not None:
            stats["pages_evaluated"] += 1
            auto_confirmed_count += 1
            if auto:
                added = attach_sources(slug, auto)
                if added:
                    stats["pages_with_new_sources"] += 1
                    stats["total_new_sources"] += len(auto)
            # else: auto-confirm returned empty (no good matches)
        else:
            needs_llm.append((slug, cands))

    log.info("Auto-confirmed %d pages, %d need LLM evaluation",
             auto_confirmed_count, len(needs_llm))

    # Phase B: batch LLM evaluation for ambiguous cases
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # Split into batches
    batches = []
    for i in range(0, len(needs_llm), EVAL_BATCH_SIZE):
        batches.append(needs_llm[i:i + EVAL_BATCH_SIZE])

    for batch in batches:
        if len(batch) == 1:
            # Single page — evaluate directly
            slug, cands = batch[0]
            confirmed = evaluate_page_candidates(slug, cands)
            stats["pages_evaluated"] += 1
            if confirmed:
                added = attach_sources(slug, confirmed)
                if added:
                    stats["pages_with_new_sources"] += 1
                    stats["total_new_sources"] += len(confirmed)
            else:
                stats["pages_needing_research"].append(slug)
        else:
            # Batch evaluate
            batch_results = evaluate_batch(batch)
            for slug, confirmed in batch_results.items():
                stats["pages_evaluated"] += 1
                if confirmed:
                    added = attach_sources(slug, confirmed)
                    if added:
                        stats["pages_with_new_sources"] += 1
                        stats["total_new_sources"] += len(confirmed)
                else:
                    stats["pages_needing_research"].append(slug)
            # Any pages not in results (parse failure) fall through
            for slug, cands in batch:
                if slug not in batch_results:
                    stats["pages_evaluated"] += 1
                    stats["pages_needing_research"].append(slug)

    # Git commit if we changed anything
    if stats["pages_with_new_sources"] > 0:
        git_commit(f"Matcher: attached sources to {stats['pages_with_new_sources']} pages")
        append_log(f"Matcher: {stats['pages_with_new_sources']} pages got {stats['total_new_sources']} new sources")

    log.info("Matcher cycle complete: %d matched, %d with new sources, %d total sources attached",
             stats["pages_matched"], stats["pages_with_new_sources"], stats["total_new_sources"])
    log.info("Pages still needing research: %d", len(stats["pages_needing_research"]))

    return stats


# ── CLI ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Ralph Matcher Agent")
    parser.add_argument("--build-only", action="store_true",
                        help="Build embedding indexes only, don't match")
    parser.add_argument("--match-only", action="store_true",
                        help="Run matching only (skip LLM evaluation)")
    parser.add_argument("--eval-only", action="store_true",
                        help="Evaluate existing match results with LLM")
    parser.add_argument("--force-rebuild", action="store_true",
                        help="Force rebuild of embedding indexes")
    parser.add_argument("-n", type=int, default=None,
                        help="Max pages to evaluate with LLM")
    args = parser.parse_args()

    if args.build_only:
        build_all_indexes()
    elif args.match_only:
        if not os.path.exists(WIKI_EMBED_FILE):
            log.error("No wiki embeddings found. Run --build-only first.")
            sys.exit(1)
        find_candidates()
    elif args.eval_only:
        if not os.path.exists(MATCH_RESULTS_FILE):
            log.error("No match results found. Run --match-only first.")
            sys.exit(1)
        with open(MATCH_RESULTS_FILE) as f:
            results = json.load(f)
        evaluated = 0
        for slug, cands in results.items():
            if args.n and evaluated >= args.n:
                break
            confirmed = evaluate_page_candidates(slug, cands)
            if confirmed:
                attach_sources(slug, confirmed)
            evaluated += 1
    else:
        run_matcher_cycle(force_rebuild=args.force_rebuild, eval_pages=args.n)

#!/usr/bin/env python3
"""
Bulk rewrite of thin-narrative wiki pages using minimax-m2.5.

Runs sequentially through all pages identified as thin-narrative by the auditor,
using the enriched writer prompt from improver.py to produce Scholarpedia-level
dense prose.

Usage:
    python3 scripts/bulk_rewrite.py                   # rewrite all 52 thin pages
    python3 scripts/bulk_rewrite.py --dry-run          # just list what would be rewritten
    python3 scripts/bulk_rewrite.py --start 10         # start from page index 10
    python3 scripts/bulk_rewrite.py --slug epileptor   # rewrite just one page
    python3 scripts/bulk_rewrite.py --model ollama/gpt-oss:120b-cloud  # use different model
"""
import os
import sys
import re
import json
import datetime
import time
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, META_DIR, AUDIT_REPORT_FILE,
    get_all_pages, read_page, save_page, word_count, get_sources,
    run_pi, append_log, git_commit,
)
from improver import build_writer_prompt, _strip_code_fences, _ensure_frontmatter

log = get_logger("BulkRewrite")

# ── Model ──────────────────────────────────────────────────────────────
DEFAULT_MODEL = "ollama/minimax-m2.5:cloud"

# ── Get thin pages from audit report ───────────────────────────────────

def get_thin_pages():
    """Load thin narrative pages from the audit report."""
    with open(AUDIT_REPORT_FILE, 'r') as f:
        data = json.load(f)
    return data.get('thin_narrative', [])


def rewrite_page(slug: str, model: str, outdir: str = None) -> tuple[bool, str]:
    """
    Rewrite a single thin-narrative page using the specified model.
    Returns (success, description).
    """
    pages = get_all_pages()
    if slug not in pages:
        return False, f"Page not found: {slug}"

    filepath = pages[slug]

    # Read original for comparison
    try:
        metadata, original = read_page(filepath)
    except Exception as e:
        return False, f"Could not read {slug}: {e}"

    original_words = word_count(original)
    log.info("Rewriting %s (%d words, %d sources)", slug, original_words, len(get_sources(metadata)))

    # Build the enriched writer prompt
    prompt = build_writer_prompt(filepath)

    # Save prompt for debugging
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        prompt_path = os.path.join(outdir, f"prompt_{slug}.txt")
        with open(prompt_path, 'w') as f:
            f.write(prompt)

    # Call the model
    log.info("Calling %s for %s...", model, slug)
    start = time.time()
    success, output = run_pi(prompt, model=model)
    elapsed = time.time() - start

    if not success:
        return False, f"Model call failed for {slug}: {output[:200]}"

    # Clean up output
    new_content = _strip_code_fences(output)
    new_content = _ensure_frontmatter(new_content, filepath)

    new_words = word_count(new_content)

    # Basic validation
    if new_words < 100:
        return False, f"Output too short for {slug}: {new_words} words (had {original_words})"

    if not new_content.strip().startswith('---'):
        log.warn("Output for %s missing frontmatter, attempting recovery", slug)
        # Try to extract content after frontmatter if present somewhere
        fm_match = re.search(r'^---\s*\n.*?\n---\s*\n', new_content, re.DOTALL)
        if not fm_match:
            return False, f"No frontmatter in output for {slug}"

    # Check if model produced meta-commentary instead of content
    first_50 = new_content[:200].lower()
    meta_indicators = [
        "here is the improved",
        "here's the improved",
        "i have improved",
        "i've improved",
        "here is the rewritten",
        "here's the rewritten",
        "the page has been improved",
        "the page has been rewritten",
        "below is the improved",
        "i will now",
        "let me improve",
        "as an ai",
    ]
    # Only flag if the meta-commentary is BEFORE frontmatter
    if new_content.strip().startswith('---'):
        # Has frontmatter, probably fine
        pass
    elif any(ind in first_50 for ind in meta_indicators):
        return False, f"Model produced meta-commentary for {slug}: starts with '{new_content[:100]}'"

    # Save original as backup
    backup_dir = os.path.join(WIKI_ROOT, "meta", "backups")
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, f"{slug}.md.bak")
    with open(backup_path, 'w') as f:
        f.write(original)

    # Write the improved page
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Save output for review
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        out_path = os.path.join(outdir, f"{slug}.md")
        with open(out_path, 'w') as f:
            f.write(new_content)

    log.info("Rewrote %s: %d -> %d words (%.0fs elapsed)", slug, original_words, new_words, elapsed)
    return True, f"Rewrote {slug}: {original_words} -> {new_words} words ({elapsed:.0f}s)"


def main():
    parser = argparse.ArgumentParser(description="Bulk rewrite thin-narrative wiki pages")
    parser.add_argument("--dry-run", action="store_true", help="Just list pages, don't rewrite")
    parser.add_argument("--start", type=int, default=0, help="Start from page index (0-based)")
    parser.add_argument("--limit", type=int, default=None, help="Max pages to rewrite")
    parser.add_argument("--slug", type=str, default=None, help="Rewrite just this one page")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--outdir", type=str, default=None, help="Directory to save prompts and outputs for review")
    parser.add_argument("--no-commit", action="store_true", help="Don't git commit after each page")
    parser.add_argument("--skip-confirmed", action="store_true", help="Skip pages already in meta/bulk_rewrite_done.json")
    args = parser.parse_args()

    outdir = args.outdir or os.path.join(WIKI_ROOT, "tmp", "bulk_rewrite")
    done_file = os.path.join(WIKI_ROOT, "meta", "bulk_rewrite_done.json")

    # Load already-done pages
    done_pages = {}
    if os.path.exists(done_file):
        with open(done_file, 'r') as f:
            done_pages = json.load(f)

    if args.slug:
        # Single page mode
        log.info("Single-page mode: %s", args.slug)
        success, desc = rewrite_page(args.slug, model=args.model, outdir=outdir)
        if success:
            done_pages[args.slug] = {
                "timestamp": datetime.datetime.now().isoformat(),
                "model": args.model,
                "description": desc,
            }
            with open(done_file, 'w') as f:
                json.dump(done_pages, f, indent=2)
            if not args.no_commit:
                git_commit(f"Bulk rewrite: {args.slug} ({args.model})")
        print(f"{'OK' if success else 'FAIL'}: {desc}")
        return

    # Get thin pages
    thin_pages = get_thin_pages()
    log.info("Found %d thin-narrative pages in audit report", len(thin_pages))

    if args.dry_run:
        print(f"Would rewrite {len(thin_pages)} pages with model {args.model}")
        for i, item in enumerate(thin_pages):
            flag = ""
            if item['slug'] in done_pages:
                flag = " [ALREADY DONE]"
            print(f"  {i:3d}. {item['slug']:40s} {item['page_words']:4d}w  (intro: {item['first_section_words']}w){flag}")
        return

    # Filter and sort
    targets = thin_pages[args.start:]
    if args.limit:
        targets = targets[:args.limit]

    if args.skip_confirmed:
        before = len(targets)
        targets = [t for t in targets if t['slug'] not in done_pages]
        after = len(targets)
        log.info("Skipping %d already-confirmed pages", before - after)

    # Sort thinnest first (lowest word count)
    targets.sort(key=lambda t: t['page_words'])

    print(f"\n{'='*70}")
    print(f"  BULK REWRITE: {len(targets)} pages with {args.model}")
    print(f"  Starting at index {args.start}, thinnest first")
    print(f"  Output dir: {outdir}")
    print(f"{'='*70}\n")

    improved = 0
    failed = 0
    skipped = 0

    for i, item in enumerate(targets):
        slug = item['slug']
        page_words = item['page_words']

        if slug in done_pages and args.skip_confirmed:
            log.info("[%d/%d] Skipping %s (already done)", i+1, len(targets), slug)
            skipped += 1
            continue

        print(f"\n[{i+1}/{len(targets)}] {slug} ({page_words}w)...")
        sys.stdout.flush()

        success, desc = rewrite_page(slug, model=args.model, outdir=outdir)

        if success:
            improved += 1
            done_pages[slug] = {
                "timestamp": datetime.datetime.now().isoformat(),
                "model": args.model,
                "description": desc,
            }
            with open(done_file, 'w') as f:
                json.dump(done_pages, f, indent=2)

            if not args.no_commit:
                git_commit(f"Bulk rewrite: {slug} ({args.model})")

            print(f"  ✓ {desc}")
        else:
            failed += 1
            print(f"  ✗ {desc}")

    # Summary
    print(f"\n{'='*70}")
    print(f"  COMPLETE: {improved} improved, {failed} failed, {skipped} skipped")
    print(f"  Model: {args.model}")
    print(f"{'='*70}\n")

    append_log(f"BulkRewrite: {improved} pages rewritten with {args.model}, {failed} failed")


if __name__ == '__main__':
    main()
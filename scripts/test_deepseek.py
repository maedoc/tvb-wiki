#!/usr/bin/env python3
"""Test deepseek-v4-pro: rewrite 12 stubs using original content as guidance."""
import os, sys, re, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import run_pi_with_metrics, WIKI_ROOT

TEST_DIR = "/tmp/model_test"
RESULTS_FILE = "/tmp/model_test/results.jsonl"
MODEL = "ollama/deepseek-v4-pro:cloud"


def stubify(path):
    """Return (frontmatter_text, body_teaser, stub_text)."""
    with open(path) as f:
        raw = f.read()
    parts = raw.split('---')
    if len(parts) >= 3:
        fm = parts[1]
        body = '---'.join(parts[2:])
    else:
        fm = ""
        body = raw
    title_match = re.search(r'^title:\s*(.+)', fm, re.M)
    title = title_match.group(1).strip() if title_match else os.path.basename(path)[:-7]
    # Truncate body to ~300 words for prompt context
    body_teaser = ' '.join(body.split()[:300])
    fm_lines = [ln for ln in fm.splitlines() if not ln.startswith('updated:')]
    frontmatter = '\n'.join(fm_lines).strip()
    stub = f"---{fm}---\n\n# {title}\n\n## Overview\n*Placeholder.*\n\n## Key Features\n*Placeholder*\n\n## Relationship to TVB\n*Placeholder*\n\n## Key Papers\n*Placeholder*\n\n## Related Software\n* [[TVB]]\n\n## References\n\n## Additional Notes\n*Placeholder*\n"
    return frontmatter, body_teaser, stub


def main():
    files = sorted([f for f in os.listdir(TEST_DIR) if f.endswith('.orig.md')])
    results = []
    for orig in files:
        slug = orig.replace('.orig.md', '')
        fm, body, stub = stubify(os.path.join(TEST_DIR, orig))
        prompt = f"""Rewrite the following wiki page for the TVB Wiki (The Virtual Brain ecosystem).
Style: encyclopedic prose, dense with technical detail, proper inline citations.
Do NOT explain your changes. Return ONLY the rewritten markdown with frontmatter.

EXISTING FRONTMATTER (keep structure:
---
{fm}
---

SOURCE MATERIAL (use for factual basis):
{body}

Write ~1000 words.
"""
        print(f"\n[TEST {slug}] Prompt size: {len(prompt.split())} words")
        ok, text, metrics = run_pi_with_metrics(prompt, model=MODEL, timeout=600)
        if not ok:
            print(f"  FAILED: {text[:80]}")
        else:
            print(f"  OK in={metrics['input_tokens']} out={metrics['output_tokens']} "
                  f"t={metrics['latency_sec']:.1f}s thr={metrics['throughput_tok_per_sec']:.1f}tok/s")
            with open(os.path.join(TEST_DIR, f"{slug}.deepseek.md"), 'w') as f:
                f.write(text)
        results.append({"slug": slug, "ok": ok, **metrics})

    with open(RESULTS_FILE, 'w') as f:
        for r in results:
            f.write(json.dumps(r) + '\n')

    success = [r for r in results if r['ok']]
    print(f"\n=== SUMMARY ===")
    print(f"Success: {len(success)}/{len(results)}")
    if success:
        avg_t = sum(r['latency_sec'] for r in success) / len(success)
        avg_thr = sum(r['throughput_tok_per_sec'] for r in success) / len(success)
        avg_out = sum(r['output_tokens'] for r in success) / len(success)
        print(f"Avg latency: {avg_t:.1f}s")
        print(f"Avg throughput: {avg_thr:.1f} tok/s")
        print(f"Avg output tokens: {avg_out:.0f}")
    for r in results:
        status = "OK" if r['ok'] else "FAIL"
        print(f"  [{status}] {r['slug']}: {r['output_tokens']}tok in {r['latency_sec']:.1f}s")


if __name__ == "__main__":
    main()

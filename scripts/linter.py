#!/usr/bin/env python3
"""
Ralph Linter Agent — daily health checks for the wiki.
Checks: broken wikilinks, orphan pages, stale pages, empty pages.
"""
import os, sys, re, datetime
import frontmatter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, get_all_pages, read_page, word_count,
    has_placeholder, get_all_wikilinks, git_commit, append_log,
)

log = get_logger("Linter")


def check_broken_links() -> list[dict]:
    """Find wikilinks that point to non-existent pages."""
    pages = get_all_pages()
    links, _ = get_all_wikilinks()
    
    broken = []
    for target, source in links:
        if target not in pages:
            broken.append({"target": target, "source": source})
    
    return broken


def check_orphans() -> list[str]:
    """Find pages with no incoming links."""
    links, pages = get_all_wikilinks()
    targets = {t for t, s in links}
    orphans = [p for p in pages if p not in targets]
    return sorted(orphans)


def check_stale_pages(max_age_days: int = 60) -> list[dict]:
    """Find pages not updated in max_age_days."""
    pages = get_all_pages()
    stale = []
    now = datetime.datetime.now()
    
    for slug, path in pages.items():
        try:
            meta, content = read_page(path)
            updated = meta.get('updated', '')
            if not updated:
                stale.append({"slug": slug, "reason": "no date", "days": -1})
                continue
            dt = datetime.datetime.strptime(updated, '%Y-%m-%d')
            age = (now - dt).days
            if age > max_age_days:
                stale.append({"slug": slug, "reason": f"{age} days old", "days": age})
        except Exception:
            stale.append({"slug": slug, "reason": "parse error", "days": -1})
    
    return sorted(stale, key=lambda x: -x.get('days', 0))


def check_empty_pages() -> list[dict]:
    """Find pages that are stubs or have placeholders."""
    pages = get_all_pages()
    empty = []
    
    for slug, path in pages.items():
        try:
            meta, content = read_page(path)
            wc = word_count(content)
            ph = has_placeholder(content)
            if wc < 50 or ph:
                empty.append({
                    "slug": slug,
                    "words": wc,
                    "placeholder": ph,
                })
        except Exception:
            pass
    
    return sorted(empty, key=lambda x: x['words'])


def run_linter_cycle() -> dict:
    """Run all linter checks. Returns report dict."""
    log.info("Starting daily lint cycle")
    
    report = {
        "broken_links": check_broken_links(),
        "orphans": check_orphans(),
        "stale_pages": check_stale_pages(),
        "empty_pages": check_empty_pages(),
        "timestamp": datetime.datetime.now().isoformat(),
    }
    
    # Summary
    log.info("Broken links: %d", len(report['broken_links']))
    log.info("Orphan pages: %d", len(report['orphans']))
    log.info("Stale pages (>60d): %d", len(report['stale_pages']))
    log.info("Empty/stub pages: %d", len(report['empty_pages']))
    
    # Save report
    report_path = os.path.join(WIKI_ROOT, "meta", "lint_report.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as f:
        import json
        json.dump(report, f, indent=2)
    
    append_log(f"Linter: {len(report['broken_links'])} broken links, "
               f"{len(report['orphans'])} orphans, "
               f"{len(report['stale_pages'])} stale, "
               f"{len(report['empty_pages'])} empty")
    
    return report


if __name__ == '__main__':
    report = run_linter_cycle()
    import json
    print(json.dumps({k: len(v) if isinstance(v, list) else v for k, v in report.items()}, indent=2))

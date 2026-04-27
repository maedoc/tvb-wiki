#!/usr/bin/env python3
"""
score_pages.py — List wiki pages sorted by quality score.

Usage:
    python3 scripts/score_pages.py              # Top 50 weakest
    python3 scripts/score_pages.py --all        # Full list
    python3 scripts/score_pages.py --worst 20   # Show 20 weakest
    python3 scripts/score_pages.py --type concept # Only concepts

Scoring (lower = worse):
    - Placeholders = -60
    - <200 words = -50, <300 = -40, <500 = -20, <800 = -5
    - 0 wikilinks = -20, <3 = -10, <8 = -3
    - Stale (>60d) = -15, (>30d) = -5
"""
import os, re, datetime, argparse
import frontmatter

def score(filepath):
    try:
        post = frontmatter.load(filepath)
        metadata, content = dict(post.metadata), post.content
    except Exception:
        return 0.0, {}
    text = content.strip()
    words = len(text.split())
    ph = '*Placeholder*' in content or 'Placeholder' in text[:200]
    links = len(set(re.findall(r'\[\[([^\]|]+)', content)))
    updated = str(metadata.get('updated', ''))[:10]
    sc = 100.0
    if ph:                     sc -= 60
    if words < 200:            sc -= 50
    elif words < 300:          sc -= 40
    elif words < 500:          sc -= 20
    elif words < 800:          sc -= 5
    if links == 0:             sc -= 20
    elif links < 3:            sc -= 10
    elif links < 8:            sc -= 3
    try:
        days = (datetime.datetime.now() - datetime.datetime.strptime(updated, '%Y-%m-%d')).days
        if days > 60:          sc -= 15
        elif days > 30:        sc -= 5
    except:                     sc -= 5
    return max(0, sc), {
        'words': words, 'links': links, 'ph': ph,
        'updated': updated, 'type': metadata.get('type', 'unknown'),
        'dir': os.path.basename(os.path.dirname(filepath)),
    }

def main():
    p = argparse.ArgumentParser(description='Score wiki page quality')
    p.add_argument('--worst', type=int, default=50)
    p.add_argument('--all', action='store_true')
    p.add_argument('--type', default=None)
    p.add_argument('--min-words', type=int, default=0)
    p.add_argument('--max-words', type=int, default=None)
    args = p.parse_args()

    results = []
    for d in ['concepts', 'entities', 'comparisons']:
        for f in os.listdir(d):
            if not f.endswith('.md') or f == 'index.md': continue
            s, info = score(os.path.join(d, f))
            if info:
                results.append((s, f[:-3], info))

    if args.type:
        results = [(s,l,i) for s,l,i in results if i.get('type') == args.type]
    results = [(s,l,i) for s,l,i in results if i['words'] >= args.min_words]
    if args.max_words:
        results = [(s,l,i) for s,l,i in results if i['words'] <= args.max_words]

    results.sort()
    rows = results if args.all else results[:args.worst]

    hdr = 'Score  Words  Links  Page                       PH  Type/Dir'
    print(hdr)
    print('=' * len(hdr))
    for sc, slug, i in rows:
        ph = 'PH' if i['ph'] else '  '
        line = f'{sc:5.1f}  {i["words"]:5d}  {i["links"]:4d}  {i["dir"]}/{slug:22s} {ph}  {i["type"]:8s}'
        print(line)
    print(f'\nSummary: Weak(<20)={len([r for r in results if r[0] < 20])},  Medium(20-59)={len([r for r in results if 20 <= r[0] < 60])},  Good(60+)={len([r for r in results if r[0] >= 60])},  Total={len(results)}')

if __name__ == '__main__':
    main()

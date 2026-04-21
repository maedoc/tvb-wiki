"""
MkDocs hook providing Obsidian-style wikilink resolution and citation rendering.
Handles [[page]] / [[page|alias]] syntax and appends References sections from sources frontmatter.
"""
import os, re

def on_config(config, **kwargs):
    docs_dir = config['docs_dir']
    config['extra']['_wikilink_map'] = {}
    config['extra']['_citation_cache'] = {}
    
    # Build wiki link index
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for f in filenames:
            if not f.lower().endswith('.md'):
                continue
            path = os.path.relpath(os.path.join(dirpath, f), docs_dir)
            base = os.path.splitext(f)[0].lower()
            config['extra']['_wikilink_map'][base] = path
            # Also index frontmatter title
            full = os.path.join(dirpath, f)
            try:
                with open(full, 'r', encoding='utf-8') as fh:
                    content = fh.read(4000)
                    m = re.search(r'title:\s*"([^"]+)"', content)
                    if not m:
                        m = re.search(r"title:\s*'([^']+)'", content)
                    if not m:
                        m = re.search(r'title:\s*([^\n]+)', content)
                    if m:
                        title = m.group(1).strip().lower().replace(' ', '-')
                        config['extra']['_wikilink_map'][title] = path
            except:
                pass
    
    # Build raw paper cache for citations
    raw_dir = os.path.join(docs_dir, 'raw', 'papers')
    if os.path.isdir(raw_dir):
        for f in os.listdir(raw_dir):
            if not f.lower().endswith('.md'):
                continue
            base = os.path.splitext(f)[0]
            full = os.path.join(raw_dir, f)
            try:
                with open(full, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                
                # Authors: handle multiline YAML list or inline list
                am = re.search(r'authors:\s*\n((?:  - .+\n)+)', content)
                if am:
                    authors = ', '.join(re.findall(r'  - (.+)', am.group(1)))
                else:
                    am = re.search(r'authors:\s*\[(.*?)\]', content)
                    authors = am.group(1) if am else "Unknown"
                
                ym = re.search(r'year:\s*(\d{4})', content)
                year = ym.group(1) if ym else ""
                
                vm = re.search(r'venue:\s*"([^"]+)"', content)
                if not vm:
                    vm = re.search(r"venue:\s*'([^']+)'", content)
                if not vm:
                    vm = re.search(r'venue:\s*([^\n]+)', content)
                venue = vm.group(1).strip() if vm else ""
                
                tm = re.search(r'title:\s*"([^"]+)"', content)
                if not tm:
                    tm = re.search(r"title:\s*'([^']+)'", content)
                if not tm:
                    tm = re.search(r'title:\s*([^\n]+)', content)
                title = tm.group(1).strip() if tm else base.replace('-', ' ').title()
                
                config['extra']['_citation_cache'][base] = {
                    'title': title, 'authors': authors, 'year': year, 'venue': venue
                }
            except Exception as e:
                pass
    
    return config

def on_page_markdown(markdown, page, config, files, **kwargs):
    wmap = config['extra'].get('_wikilink_map', {})
    cite_cache = config['extra'].get('_citation_cache', {})
    page_dir = os.path.dirname(page.file.src_path)
    
    # 1. Resolve wikilinks [[target]] or [[target|alias]]
    def replace_wikilink(m):
        inner = m.group(1)
        if '|' in inner:
            target, alias = inner.split('|', 1)
            target = target.strip().lower().replace(' ', '-')
            alias = alias.strip()
        else:
            target = inner.strip().lower().replace(' ', '-')
            alias = inner.strip()
        
        rel = wmap.get(target)
        if not rel:
            flat = target.replace('-', '')
            for k, v in wmap.items():
                if k.replace('-', '') == flat:
                    rel = v; break
        
        if rel:
            rel_link = os.path.relpath(rel, page_dir) if page_dir else rel
            return f'[{alias}]({rel_link})'
        else:
            return alias
    
    markdown = re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, markdown)
    
    # 2. Parse sources frontmatter and append references
    fm = page.meta if hasattr(page, 'meta') else {}
    sources = fm.get('sources') or []
    if isinstance(sources, str):
        sources = [s.strip().strip('"\'') for s in re.split(r',\s+', sources) if s.strip()]
    
    if sources:
        ref_entries = []
        seen = set()
        for i, s in enumerate(sources, 1):
            key = os.path.splitext(os.path.basename(s))[0] if '/' in s or s.endswith('.md') else s
            if key in seen:
                continue
            seen.add(key)
            
            entry = cite_cache.get(key)
            if entry:
                parts = []
                if entry['authors'] and entry['authors'] != "Unknown":
                    parts.append(entry['authors'])
                if entry['year']:
                    parts.append(f"({entry['year']})")
                parts.append(f"**{entry['title']}**.")
                if entry['venue']:
                    parts.append(f"*{entry['venue']}*.")
                ref_entries.append(f'{i}. {" ".join(parts)}')
                
                # Replace bare inline key references with [i]
                bare_re = re.compile(r'(?<![\w\[])' + re.escape(key) + r'(?![\w\]])')
                markdown = bare_re.sub(f'[{i}]', markdown)
            else:
                ref_entries.append(f'{i}. {key}')
        
        if ref_entries:
            markdown += '\n\n---\n\n## References\n\n'
            markdown += '\n'.join(ref_entries)
    
    return markdown

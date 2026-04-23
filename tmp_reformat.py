import pathlib, re, sys
src = pathlib.Path('meta/manual_import/processed/vbt-review-sources.md')
out = pathlib.Path('meta/manual_import/vbt-review-sources.md')
text = src.read_text(encoding='utf-8')
lines = []
for table in re.finditer(r'(\|.*\n)(\|[-\s|]+\n)((?:\|.*\n)+)', text):
    header_line = table.group(1).strip('|\n')
    headers = [h.strip() for h in header_line.split('|')]
    rows_text = table.group(3)
    for row in rows_text.strip().split('\n'):
        cells = [c.strip() for c in row.strip('|').split('|')]
        if len(cells) != len(headers):
            continue
        rowdict = dict(zip(headers, cells))
        fragments = []
        if 'Author' in rowdict:
            fragments.append(f"Authors: {rowdict['Author']}")
        elif 'Authors' in rowdict:
            fragments.append(f"Authors: {rowdict['Authors']}")
        if 'Title' in rowdict:
            fragments.append(f"Title: {rowdict['Title']}")
        if 'Year' in rowdict:
            fragments.append(f"Year: {rowdict['Year']}")
        if 'DOI' in rowdict:
            fragments.append(f"DOI: {rowdict['DOI']}")
        if 'Journal' in rowdict:
            fragments.append(f"Venue: {rowdict['Journal']}")
        if 'Usage' in rowdict:
            fragments.append(f"Abstract: {rowdict['Usage']}")
        if fragments:
            lines.append('; '.join(fragments))
out.write_text('\n'.join(lines), encoding='utf-8')
print('Wrote', len(lines), 'lines to', out)

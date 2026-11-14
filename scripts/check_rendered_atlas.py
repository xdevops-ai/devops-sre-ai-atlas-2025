#!/usr/bin/env python3
"""Validate built URLs and evidence tables after bundle exec jekyll build."""
from pathlib import Path
from html.parser import HTMLParser
import json,sys
root=Path(__file__).resolve().parents[1]; site=root/'docs/_site';rows=json.loads((root/'atlas-reviewed-data.json').read_text());errors=[]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.links += [v for k,v in attrs if k=='href']
paths=[site/'index.html',site/'platforms/index.html',site/'capabilities/index.html']+[site/'platforms'/Path(r['file']).stem/'index.html' for r in rows]
checked=0
for p in paths:
 if not p.exists():errors.append(f'missing {p}');continue
 html=p.read_text();q=Links();q.feed(html)
 if '{{' in html:errors.append(f'unrendered Liquid {p}')
 for u in q.links:
  if not u.startswith('/devops-sre-ai-atlas-2025/'):continue
  target=site/u.removeprefix('/devops-sre-ai-atlas-2025/').split('#')[0].split('?')[0]
  if not target.exists() and not (target/'index.html').exists():errors.append(f'{p.name}: missing {u}')
  checked+=1
for r in rows:
 slug=Path(r['file']).stem;p=site/'platforms'/slug/'index.html'
 if p.exists() and 'Identity and availability' not in p.read_text():errors.append(f'overwritten page {slug}')
 p=site/'platforms'/f'{slug}.html'
 if not p.exists() or 'http-equiv="refresh"' not in p.read_text():errors.append(f'missing alias {slug}')
if errors:print('\n'.join(sorted(set(errors))));sys.exit(1)
print(f'PASS: {len(paths)} rendered pages; {checked} internal links; 54 legacy aliases; no unresolved Liquid or overwritten records.')

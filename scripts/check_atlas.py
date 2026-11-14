#!/usr/bin/env python3
"""Focused, dependency-free checks for the reviewed directory layer."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]; docs=root/'docs'
rows=json.loads((root/'atlas-reviewed-data.json').read_text()); errors=[]
assert len(rows)==54
assert len({r['file'] for r in rows})==54
idx=(docs/'platforms/index.md').read_text(); caps=(docs/'capabilities/index.md').read_text()
for r in rows:
 p=docs/'platforms'/r['file']; text=p.read_text(); slug=p.stem
 for token in ['parent: Platform Directory',f'permalink: /platforms/{slug}/','## Identity and availability','## Capability mapping','## Official links and evidence','## Is it relevant to your team?' ,'14 November 2026']:
  if token not in text: errors.append(f'{p.name}: missing {token}')
 if len(re.findall(r'^\| (?:UKM|UAM|UDM|UOM|UEOM|UPM) ',text,re.M))!=6:errors.append(f'{p.name}: six axes required')
 if not re.search(r'\]\(https://',text):errors.append(f'{p.name}: no source')
 if f'/platforms/{slug}/' not in idx:errors.append(f'{p.name}: not indexed')
 if r['file'] not in ['moogsoft-aiops.md','kagent-solo-io.md'] and f'/platforms/{slug}/' not in caps:errors.append(f'{p.name}: not in matrix')
 if not (docs/'platforms'/f'{slug}.html').exists():errors.append(f'{p.name}: legacy .html alias missing')
for p in [docs/'platforms/index.md', docs/'capabilities/index.md', *[docs/'platforms'/r['file'] for r in rows]]:
 for slug in re.findall(r'"(/platforms/[^" ]+/)"',p.read_text()):
  if not (docs/'platforms'/(slug.split('/')[-2]+'.md')).exists(): errors.append(f'{p.name}: broken {slug}')
if errors: print('\n'.join(errors));sys.exit(1)
print('PASS: 54 records; 52 canonical plus two aliases; six axes, sources, index, matrix and legacy links verified.')

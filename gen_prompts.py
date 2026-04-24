#!/usr/bin/env python3
"""Generate writer prompts for 10 test pages and save to ./tmp/"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from improver import build_writer_prompt

PAGES = [
    'concepts/epileptor.md',
    'concepts/dynamic-causal-modeling.md',
    'concepts/fokker-planck-equation.md',
    'concepts/bifurcation-theory.md',
    'concepts/tractography.md',
    'concepts/hopfield.md',
    'concepts/variational-bayes.md',
    'concepts/free-energy-principle.md',
    'concepts/mean-field-theory.md',
    'concepts/stochastic-differential-equations.md',
]

os.makedirs('tmp', exist_ok=True)

for page in PAGES:
    slug = os.path.basename(page).replace('.md', '')
    prompt = build_writer_prompt(page)
    outf = f'tmp/prompt_{slug}.txt'
    with open(outf, 'w') as f:
        f.write(prompt)
    print(f'{slug}: {len(prompt)} chars -> {outf}')

print(f'\nGenerated {len(PAGES)} prompts')
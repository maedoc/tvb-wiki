#!/usr/bin/env python3
import os, re

fixes = [
    ('concepts/alzheimers-modeling.md', 'neuroimaging-dti', 'dti'),
    ('concepts/nonlinear-dynamics.md', 'ermentrout-terman', 'Ermentrout \u0026 Terman'),
    ('concepts/alzheimers-modeling.md', 'neuroimaging-fmri', 'fmri'),
    ('concepts/neural-field-theory.md', 'neuroimaging-meg', 'meg'),
    ('concepts/fmri.md', 'general-[[linear', 'general-linear'),
    ('concepts/alzheimers-modeling.md', 'neuroimaging-eeg', 'eeg'),
    ('entities/psyneulink.md', 'tensorflow', 'TensorFlow'),
    ('concepts/schizophrenia-models.md', 'neuroimaging-dti', 'dti'),
    ('concepts/neural-field-theory.md', 'neuroimaging-fmri', 'fmri'),
    ('concepts/neural-field-theory.md', 'fokker-planplanck-equation', 'fokker-planck-equation'),
    ('entities/voxelmorph.md', "alzheimer's-modeling", 'alzheimers-modeling'),
    ('concepts/modularity.md', 'community-detection#louvain-method', 'community-detection'),
    ('concepts/whole-brain-modeling.md', 'diffusion-tensor-imaging', 'diffusion-mri'),
    ('entities/psyneulink.md', 'pytorch', 'PyTorch'),
]

for fname, old, new in fixes:
    if not os.path.exists(fname):
        print(f'SKIP (not found): {fname}')
        continue
    with open(fname, 'r') as f:
        content = f.read()
    
    if f'[[{old}]]' in content:
        new_content = content.replace(f'[[{old}]]', f'[[{new}]]')
    elif old in content:
        new_content = content.replace(old, new)
    else:
        print(f'NOT FOUND in {fname}: [[{old}]]')
        continue
    
    with open(fname, 'w') as f:
        f.write(new_content)
    print(f'Fixed {fname}: [[{old}]] → [[{new}]]')

print('Done')

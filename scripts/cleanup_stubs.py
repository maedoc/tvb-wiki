#!/usr/bin/env python3
"""
Cleanup script: delete inappropriate stubs and fix source pages.
"""
import os
import re
import shutil

WIKI_ROOT = "/home/duke/src/tvb-wiki"

# Stubs to DELETE (author-year citations, external libraries, etc.)
DELETE_STUBS = {
    # Author-year citations → should be plain text
    'cohen-2014': 'Cohen et al. (2014)',
    'raichle-2001': 'Raichle et al. (2001)',
    'schuster2021': 'Schuster et al. (2021)',
    'freeman1975': 'Freeman (1975)',
    'freeman2000': 'Freeman (2000)',
    'rubinov-sporns-2010': 'Rubinov \u0026 Sporns (2010)',
    'andrews-hanna-2010': 'Andrews-Hanna et al. (2010)',
    'buckner-andrews-hanna-schacter-2008': 'Buckner et al. (2008)',
    'power-2010': 'Power et al. (2010)',
    'kozma2012': 'Kozma et al. (2012)',
    'ermentrout-terman': 'Ermentrout \u0026 Terman',
    # External Python libraries → plain text
    'numpy': 'NumPy',
    'scipy': 'SciPy',
    'pandas': 'pandas',
    'matplotlib': 'Matplotlib',
    'pytorch': 'PyTorch',
    'tensorflow': 'TensorFlow',
    'jupyter': 'Jupyter',
    # HPC schedulers → plain text
    'slurm': 'SLURM',
    'sge': 'SGE',
    'htcondor': 'HTCondor',
    'pbs': 'PBS',
    # Duplicates (diffusion-tensor-imaging is same as dti)
    'diffusion-tensor-imaging': None,
}

# Stubs to MOVE from concepts/ to entities/
MOVE_TO_ENTITIES = {
    'nifti', 'cifti', 'nnu-net', 'bidscoin', 'bids-validator',
    'camino', 'deepmedic', 'mni-space', 'hcp-dataset',
    'destrieux-atlas', 'schaefer-atlas', 'glasser-atlas',
    'brainnetome-atlas', 'harvard-oxford-atlas', 'desikan-killiany-atlas',
    'aal-atlas', 'julich-atlas', 'allen-brain-atlas',
    'mne-bids', 'mne-python', 'mne-bids', 'nilearn',
    'bctpy', 'nibetaseries', 'lfpykit', 'dipy',
    'mrtrix', 'mrtrix3', 'nipype', 'niftyreg', 'niftynet',
    'ants', 'antspy', 'fsl', 'fsleyes', 'freesurfer',
    'spiny', 'dcm', 'conn',
}

def fix_source_pages(deleted_slug, replacement_text):
    """Replace wikilinks to deleted stubs with plain text."""
    for dir in ['concepts', 'entities', 'comparisons']:
        for fname in os.listdir(os.path.join(WIKI_ROOT, dir)):
            if not fname.endswith('.md'):
                continue
            path = os.path.join(WIKI_ROOT, dir, fname)
            with open(path, 'r') as f:
                content = f.read()
            
            # Replace [[slug|text]] and [[slug]]
            if replacement_text:
                pattern = rf'\[\[{re.escape(deleted_slug)}(\|[^\]]+)?\]\]'
                new_content = re.sub(pattern, replacement_text, content)
            else:
                # Just remove the brackets
                pattern = rf'\[\[{re.escape(deleted_slug)}(\|[^\]]+)?\]\]'
                new_content = re.sub(pattern, r'\1' if False else '', content)
                # Simpler: just remove brackets
                new_content = content.replace(f'[[{deleted_slug}]]', deleted_slug.replace('-', ' ').title())
            
            if new_content != content:
                with open(path, 'w') as f:
                    f.write(new_content)
                print(f"  Fixed {fname}: [[{deleted_slug}]] → {replacement_text or deleted_slug}")

if __name__ == '__main__':
    print("=== CLEANING INAPPROPRIATE STUBS ===\n")
    
    # Step 1: Delete inappropriate stubs
    for slug, replacement in DELETE_STUBS.items():
        stub_path = os.path.join(WIKI_ROOT, 'concepts', f'{slug}.md')
        if os.path.exists(stub_path):
            os.remove(stub_path)
            print(f"Deleted: concepts/{slug}.md")
            fix_source_pages(slug, replacement)
    
    # Step 2: Move file format/software stubs to entities/
    moved = 0
    for slug in MOVE_TO_ENTITIES:
        src = os.path.join(WIKI_ROOT, 'concepts', f'{slug}.md')
        dst = os.path.join(WIKI_ROOT, 'entities', f'{slug}.md')
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
            moved += 1
            print(f"Moved: concepts/{slug}.md → entities/{slug}.md")
            # Update wikilinks in source pages
            for dir in ['concepts', 'entities', 'comparisons']:
                for fname in os.listdir(os.path.join(WIKI_ROOT, dir)):
                    if not fname.endswith('.md'): continue
                    path = os.path.join(WIKI_ROOT, dir, fname)
                    with open(path, 'r') as f:
                        content = f.read()
                    if f'[[{slug}]]' in content:
                        # No change needed — wikilinks work across dirs
                        pass
    
    print(f"\nMoved {moved} stubs to entities/")
    print("Cleanup complete.")

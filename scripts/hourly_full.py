#!/usr/bin/env python3
"""
Hourly full pipeline: update research papers, sync to docs, build static site,
and commit changes to git (optionally push).
"""
import os, sys, subprocess, datetime, shutil, pathlib, json, re, warnings, typing, collections, itertools, math, random, string, hashlib, html, urllib.parse, frontmatter, time, signal, logging

wiki_root = os.path.dirname(os.path.abspath(__file__))
if wiki_root.endswith('scripts'):
    wiki_root = os.path.dirname(wiki_root)

def run(cmd, cwd=None, env=None):
    """Run command and return (success, output)."""
    try:
        result = subprocess.run(cmd, cwd=cwd or wiki_root, env=env, capture_output=True, text=True, timeout=300)
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutError:
        return False, "Command timed out after 300 seconds"
    except Exception as e:
        return False, str(e)

def main():
    print(f"=== Hourly pipeline started at {datetime.datetime.now().isoformat()} ===")
    
    # Step 1: Run hourly research update
    update_script = os.path.join(wiki_root, 'scripts', 'hourly_update.py')
    if os.path.exists(update_script):
        print("Running hourly research update...")
        ok, out = run([sys.executable, update_script])
        if ok:
            print("Update succeeded.")
            if 'No new papers' in out:
                print("No new papers found.")
            else:
                print("New papers processed.")
        else:
            print(f"Update failed: {out}")
            # Continue anyway, maybe partial updates
    else:
        print("Warning: hourly_update.py not found.")
    
    # Step 2: Sync to docs
    sync_script = os.path.join(wiki_root, 'scripts', 'sync_to_docs.py')
    if os.path.exists(sync_script):
        print("Syncing to docs...")
        ok, out = run([sys.executable, sync_script])
        if ok:
            print("Sync succeeded.")
        else:
            print(f"Sync failed: {out}")
    else:
        print("Warning: sync_to_docs.py not found.")
    
    # Step 3: Build static site
    mkdocs_path = shutil.which('mkdocs')
    if mkdocs_path:
        print("Building static site with MkDocs...")
        ok, out = run([mkdocs_path, 'build'])
        if ok:
            print("Site built successfully.")
        else:
            print(f"Build failed: {out}")
    else:
        print("Warning: mkdocs not found in PATH.")
    
    # Step 4: Git commit if changes
    print("Checking for git changes...")
    ok, status = run(['git', 'status', '--porcelain'])
    if ok and status.strip():
        print("Changes detected:")
        print(status)
        # Add all changes
        ok_add, out_add = run(['git', 'add', '.'])
        if ok_add:
            commit_msg = f"Hourly update {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
            ok_commit, out_commit = run(['git', 'commit', '-m', commit_msg])
            if ok_commit:
                print("Committed changes.")
                # Push if remote exists
                ok_remote, out_remote = run(['git', 'remote', '-v'])
                if ok_remote and out_remote.strip():
                    print("Pushing to remote...")
                    ok_push, out_push = run(['git', 'push'])
                    if ok_push:
                        print("Pushed successfully.")
                    else:
                        print(f"Push failed: {out_push}")
                else:
                    print("No remote configured, skipping push.")
            else:
                print(f"Commit failed: {out_commit}")
        else:
            print(f"Git add failed: {out_add}")
    else:
        print("No changes to commit.")
    
    print(f"=== Hourly pipeline finished at {datetime.datetime.now().isoformat()} ===")

if __name__ == '__main__':
    main()
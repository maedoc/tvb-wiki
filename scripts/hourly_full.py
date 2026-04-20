#!/usr/bin/env python3
"""
Hourly full pipeline: update research papers, sync to docs, build static site,
and optionally commit and push git changes.
"""
import os, sys, subprocess, datetime, shutil, argparse

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(cmd, cwd=None, env=None, timeout=300):
    """Run command and return (success, output)."""
    try:
        result = subprocess.run(cmd, cwd=cwd or WIKI_ROOT, env=env,
                                capture_output=True, text=True, timeout=timeout)
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutError:
        return False, f"Command timed out after {timeout} seconds"
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="TVB Wiki hourly full pipeline")
    parser.add_argument("--skip-update", action="store_true", help="Skip research update")
    parser.add_argument("--skip-sync", action="store_true", help="Skip sync to docs")
    parser.add_argument("--skip-build", action="store_true", help="Skip MkDocs build")
    parser.add_argument("--skip-git", action="store_true", help="Skip git commit/push")
    parser.add_argument("--push", action="store_true", help="Push to remote if possible")
    parser.add_argument("--use-exa", action="store_true", help="Pass to hourly_update.py")
    parser.add_argument("--enrich", action="store_true", help="Pass to hourly_update.py")
    args = parser.parse_args()
    
    print(f"=== Hourly pipeline started at {datetime.datetime.now().isoformat()} ===")
    
    # Build hourly_update.py arguments
    update_args = []
    if args.use_exa:
        update_args.append("--use-exa")
    if args.enrich:
        update_args.append("--enrich")
    
    # Step 1: Run hourly research update
    if not args.skip_update:
        update_script = os.path.join(WIKI_ROOT, 'scripts', 'hourly_update.py')
        if os.path.exists(update_script):
            print("\n📚 Running hourly research update...")
            cmd = [sys.executable, update_script] + update_args
            ok, out = run(cmd)
            if ok:
                print("  Update succeeded.")
                if 'Added 0 new papers' in out:
                    print("  No new papers found.")
            else:
                print(f"  Update failed: {out[:200]}")
                # Continue anyway
        else:
            print("  Warning: hourly_update.py not found.")
    
    # Step 2: Sync to docs
    if not args.skip_sync:
        sync_script = os.path.join(WIKI_ROOT, 'scripts', 'sync_to_docs.py')
        if os.path.exists(sync_script):
            print("\n📂 Syncing to docs...")
            ok, out = run([sys.executable, sync_script])
            if ok:
                print("  Sync succeeded.")
            else:
                print(f"  Sync failed: {out[:200]}")
        else:
            print("  Warning: sync_to_docs.py not found.")
    
    # Step 3: Build static site
    if not args.skip_build:
        mkdocs_path = shutil.which('mkdocs')
        if mkdocs_path:
            print("\n🏗️  Building static site with MkDocs...")
            ok, out = run([mkdocs_path, 'build'])
            if ok:
                print("  Site built successfully.")
            else:
                print(f"  Build failed: {out[:200]}")
        else:
            print("  Warning: mkdocs not found in PATH.")
    
    # Step 4: Git commit/push
    if not args.skip_git:
        print("\n🔍 Checking for git changes...")
        ok, status = run(['git', 'status', '--porcelain'])
        if ok and status.strip():
            print("  Changes detected:")
            for line in status.strip().split('\n'):
                print(f"    {line}")
            # Add all changes
            ok_add, out_add = run(['git', 'add', '.'])
            if ok_add:
                commit_msg = f"Hourly update {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
                ok_commit, out_commit = run(['git', 'commit', '-m', commit_msg])
                if ok_commit:
                    print("  Committed changes.")
                    # Push if requested and remote exists
                    if args.push:
                        ok_remote, out_remote = run(['git', 'remote', '-v'])
                        if ok_remote and out_remote.strip():
                            print("  Pushing to remote...")
                            ok_push, out_push = run(['git', 'push'])
                            if ok_push:
                                print("  Pushed successfully.")
                            else:
                                print(f"  Push failed: {out_push[:200]}")
                        else:
                            print("  No remote configured, skipping push.")
                else:
                    print(f"  Commit failed: {out_commit[:200]}")
            else:
                print(f"  Git add failed: {out_add[:200]}")
        else:
            print("  No changes to commit.")
    
    print(f"\n=== Hourly pipeline finished at {datetime.datetime.now().isoformat()} ===")

if __name__ == '__main__':
    main()
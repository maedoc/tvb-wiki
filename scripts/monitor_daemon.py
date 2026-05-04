#!/usr/bin/env python3
"""
Monitor daemon progress and report throughput.
Run in background: python3 scripts/monitor_daemon.py
"""

import time, subprocess, re, os

LOG = "scripts/ralph.log"

def tail_log():
    try:
        with open(LOG) as f:
            return f.read()
    except:
        return ""

def count_since(lines, marker):
    """Count occurrences of pattern after last marker line."""
    found_marker = False
    count = 0
    for line in lines:
        if marker in line:
            found_marker = True
            count = 0
        if found_marker:
            count += 1
    return count

def main():
    prev_improved = 0
    prev_failed = 0
    
    print("Monitoring daemon progress... Ctrl+C to stop.\n")
    
    while True:
        time.sleep(60)
        
        log = tail_log()
        lines = log.split('\n')
        
        improved = len([l for l in lines if "[Improver] Improved" in l])
        failed = len([l for l in lines if "Validation failed" in l])
        cycles = len([l for l in lines if "Cycle complete" in l])
        
        improved_delta = improved - prev_improved
        failed_delta = failed - prev_failed
        prev_improved = improved
        prev_failed = failed
        
        # Check for recent commits
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "--since=2 minutes ago"],
                capture_output=True, text=True, cwd=os.getcwd()
            )
            recent_commits = result.stdout.strip()
        except:
            recent_commits = ""
        
        # Check active daemon pi children
        try:
            result = subprocess.run(
                ["pgrep", "-P", str(os.getpid())],
                capture_output=True, text=False
            )
        except:
            pass
        
        # Get daemon PID
        try:
            result = subprocess.run(
                ["pgrep", "-a", "-f", "ralph_daemon"],
                capture_output=True, text=True
            )
            daemon_info = result.stdout.strip().split('\n')[0] if result.stdout else "No daemon"
        except:
            daemon_info = "No daemon"
        
        print(f"[{time.strftime('%H:%M:%S')}] Daemon: {daemon_info[:40]}")
        print(f"  Improver: {improved} total (+{improved_delta}/min), {failed} validations failed (+{failed_delta}/min)")
        print(f"  Cycles: {cycles} complete")
        
        if recent_commits:
            print(f"  Recent commits:\n{recent_commits}")
        else:
            print(f"  Recent commits: none")
        
        print()

if __name__ == '__main__':
    main()

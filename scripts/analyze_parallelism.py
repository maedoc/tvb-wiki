#!/usr/bin/env python3
import re
from collections import defaultdict

events = []
with open('scripts/ralph.log') as f:
    for ln in f:
        if 'pi completed' in ln:
            m = re.search(r'(\d\d:\d\d:\d\d).*?completed in ([0-9.]+)s \((\d+) chars', ln)
            if m:
                ts = m.group(1)
                latency = float(m.group(2))
                chars = int(m.group(3))
                events.append({'ts': ts, 'latency': latency, 'chars': chars})

# Only since 20:00 today
events = [e for e in events if e['ts'] >= '20:00:00']

print(f"=== Pi calls since 20:00: {len(events)} ===")

if len(events) >= 6:
    print("\nSample calls:")
    for i in range(min(9, len(events))):
        e = events[i]
        print(f"  {e['ts']}: {e['latency']:6.1f}s ({e['chars']:5d} chars)")
    
    print(f"\nLatency distribution:")
    lats = [e['latency'] for e in events]
    lats_sorted = sorted(lats)
    print(f"  Count:   {len(lats)}")
    print(f"  Min:     {min(lats):.1f}s")
    print(f"  Max:     {max(lats):.1f}s")
    print(f"  Avg:     {sum(lats)/len(lats):.1f}s")
    print(f"  Median:  {lats_sorted[len(lats)//2]:.1f}s")
    print(f"  P90:     {lats_sorted[int(len(lats)*0.9)]:.1f}s")
    
    # Check for clustering (overlap indicator)
    def to_sec(t):
        h, m, s = map(int, t.split(':'))
        return h*3600 + m*60 + s
    
    times = [to_sec(e['ts']) for e in events]
    overlaps = 0
    for i in range(len(times)-2):
        span = times[i+2] - times[i]
        if span <= 120:  # 3 calls within 2 min = likely parallel
            overlaps += 1
    print(f"\nParallelism check:")
    print(f"  Groups of 3 calls within 2 min: {overlaps}")
    if overlaps > 0 and len(times) > 2:
        print(f"  → ~{100*overlaps/(len(times)-2):.0f}% of cycles used 3 parallel writers")
    
    # Estimate throughput
    if len(times) >= 2:
        total_span = (times[-1] - times[0]) / 60.0  # minutes
        print(f"\nThroughput:")
        print(f"  Calls: {len(events)} over {total_span:.1f} min")
        print(f"  → {len(events)/total_span:.1f} pi calls/min")
        print(f"  → {(len(events)/total_span)*60:.1f} pi calls/hour")

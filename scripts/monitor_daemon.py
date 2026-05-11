#!/usr/bin/env python3
"""Monitor daemon performance from ralph.log. Run every 5 min, append summary."""

import os, re, json, datetime, sys

LOG = os.path.join(os.path.dirname(__file__), "ralph.log")
SUMMARY = os.path.join(os.path.dirname(__file__), "..", "meta", "daemon_perf.json")

# Window: last N minutes
WINDOW_MIN = 6  # slightly more than 5 to catch straddlers

def parse_log(window_min=WINDOW_MIN):
    """Extract per-agent metrics from the last window_min minutes of ralph.log."""
    if not os.path.exists(LOG):
        return {}, "No log file"
    cutoff = datetime.datetime.now() - datetime.timedelta(minutes=window_min)
    agents = {}

    with open(LOG, 'r', encoding='utf-8', errors='replace') as f:
        # Seek near end for speed
        f.seek(0, 2)
        size = f.tell()
        # Read last ~200KB (roughly 5-10 min of logs)
        read_start = max(0, size - 200_000)
        f.seek(read_start)
        lines = f.readlines()

    for line in lines:
        # Handle duplicate timestamps: "YYYY-MM-DD HH:MM:SS YYYY-MM-DD HH:MM:SS [Agent] ..."
        m = re.match(r'(?:\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+)?(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(.*)', line.strip())
        if not m:
            continue
        ts_str, msg = m.group(1), m.group(2)
        try:
            ts = datetime.datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
        if ts < cutoff:
            continue

        # Detect agent tag: [Matcher], [Improver], [Ingestor], etc.
        agent_match = re.search(r'\[([A-Za-z][A-Za-z0-9]*)\]', msg)
        if not agent_match:
            continue
        agent = agent_match.group(1)
        if agent not in agents:
            agents[agent] = {
                "lines": 0,
                "cycles_complete": 0,
                "pages_processed": 0,
                "sources_attached": 0,
                "errors": 0,
                "llm_calls": 0,
                "tokens_in": 0,
                "tokens_out": 0,
                "latency_sum": 0.0,
                "max_latency": 0.0,
                "index_build_sec": 0.0,
                "auto_confirmed": 0,
                "needs_llm": 0,
                "batch_evals": 0,
            }
        a = agents[agent]
        a["lines"] += 1

        # Counters
        if "cycle complete" in msg.lower():
            a["cycles_complete"] += 1
        if "attached" in msg.lower() and "sources" in msg.lower():
            m2 = re.search(r'(\d+)\s+sources?', msg)
            if m2:
                a["sources_attached"] += int(m2.group(1))
        if "pages matched" in msg.lower() or "pages evaluated" in msg.lower():
            m2 = re.search(r'(\d+)\s+pages?', msg)
            if m2:
                a["pages_processed"] += int(m2.group(1))
        if "auto-confirmed" in msg.lower():
            m2 = re.search(r'(\d+)\s+pages?', msg)
            if m2:
                a["auto_confirmed"] += int(m2.group(1))
        if "need LLM" in msg.lower():
            m2 = re.search(r'(\d+)\s+need', msg)
            if m2:
                a["needs_llm"] += int(m2.group(1))
        if "batch evaluation" in msg.lower() or "batch eval" in msg.lower():
            a["batch_evals"] += 1
        if "error" in msg.lower() or "failed" in msg.lower() or "warn" in msg.lower():
            a["errors"] += 1
        if "in=" in msg and "out=" in msg and "t=" in msg:
            # pi: model in=X out=Y t=Z.s th=W/s
            m_in = re.search(r'in=(\d+)', msg)
            m_out = re.search(r'out=(\d+)', msg)
            m_lat = re.search(r't=([\d.]+)s', msg)
            if m_in and m_out:
                a["llm_calls"] += 1
                a["tokens_in"] += int(m_in.group(1))
                a["tokens_out"] += int(m_out.group(1))
                if m_lat:
                    lat = float(m_lat.group(1))
                    a["latency_sum"] += lat
                    a["max_latency"] = max(a["max_latency"], lat)
        if "index build complete" in msg.lower():
            m2 = re.search(r'([\d.]+)\s*s', msg)
            if m2:
                a["index_build_sec"] = float(m2.group(1))

    return agents, None

def load_history():
    if os.path.exists(SUMMARY):
        try:
            with open(SUMMARY, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"samples": [], "started": datetime.datetime.now().isoformat()}

def save_history(history):
    os.makedirs(os.path.dirname(SUMMARY), exist_ok=True)
    with open(SUMMARY, 'w') as f:
        json.dump(history, f, indent=2)

def main():
    agents, err = parse_log()
    if err:
        print(f"ERROR: {err}")
        sys.exit(1)

    sample = {
        "ts": datetime.datetime.now().isoformat(),
        "agents": agents,
    }

    history = load_history()
    history["samples"].append(sample)
    # Keep last 300 samples (~25 hours at 5-min intervals)
    if len(history["samples"]) > 300:
        history["samples"] = history["samples"][-300:]

    save_history(history)

    # Print human-readable snapshot
    print(f"\n=== Daemon snapshot @ {sample['ts'][:19]} ===")
    for agent, stats in sorted(agents.items(), key=lambda x: -x[1].get("lines", 0)):
        parts = [f"[{agent}]"]
        if stats.get("cycles_complete"):
            parts.append(f"cycles={stats['cycles_complete']}")
        if stats.get("pages_processed"):
            parts.append(f"pages={stats['pages_processed']}")
        if stats.get("sources_attached"):
            parts.append(f"sources={stats['sources_attached']}")
        if stats.get("auto_confirmed"):
            parts.append(f"auto={stats['auto_confirmed']}")
        if stats.get("needs_llm"):
            parts.append(f"llm_needed={stats['needs_llm']}")
        if stats.get("llm_calls"):
            lat = stats['latency_sum'] / stats['llm_calls'] if stats['llm_calls'] else 0
            parts.append(f"llm_calls={stats['llm_calls']} tok_in={stats['tokens_in']} tok_out={stats['tokens_out']} avg_lat={lat:.1f}s max_lat={stats['max_latency']:.1f}s")
        if stats.get("index_build_sec"):
            parts.append(f"index_build={stats['index_build_sec']:.1f}s")
        if stats.get("errors"):
            parts.append(f"errors={stats['errors']}")
        print("  " + " | ".join(parts))

    if not agents:
        print("  (no agent activity in last 6 min)")

    print(f"\n  Samples stored: {len(history['samples'])}")
    print(f"  Summary file: {SUMMARY}")

if __name__ == "__main__":
    main()

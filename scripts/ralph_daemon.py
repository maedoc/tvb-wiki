#!/usr/bin/env python3
"""
Ralph Daemon — the main loop for autonomous TVB Wiki improvement.

Start: python3 scripts/ralph_daemon.py
Stop:  Ctrl+C (graceful shutdown between cycles)

Agents:
  Ingestor       (hourly) — fetches papers from arXiv, Semantic Scholar, PubMed, OpenAlex
  Improver       (hourly) — improves worst pages via writer(kimi-k2.6)+reviewer(glm-5.1)
  Auditor        (daily)  — structural integrity check (broken links, orphans, etc)
  Librarian      (daily)  — index rebuild, authority scores, symmetry check
  SoftwareMapper (weekly) — ensures full software ecosystem coverage
"""
import os
import sys
import time
import json
import signal
import datetime
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, SCRIPTS_DIR, META_DIR, RALPH_LOG,
    RAW_PAPERS_DIR, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    WRITER_MODEL, REVIEWER_MODEL,
    INGESTOR_INTERVAL, IMPROVER_INTERVAL, AUDITOR_INTERVAL,
    LIBRARIAN_INTERVAL, SOFTWARE_MAPPER_INTERVAL, DEEP_RESEARCH_INTERVAL,
    PARALLEL_WRITERS, PI_TIMEOUT,
    get_all_pages,
)

log = get_logger("daemon")

# ── State ──────────────────────────────────────────────────────────────

class DaemonState:
    """Tracks when each agent last ran and consecutive failures."""

    def __init__(self):
        self.last_run = {
            'Ingestor': None,
            'Improver': None,
            'Auditor': None,
            'Librarian': None,
            'SoftwareMapper': None,
            'DeepResearch': None,
        }
        self.failures = {k: 0 for k in self.last_run}
        self.disabled = set()
        self.running = True
        self.cycle = 0

    def record_success(self, agent: str):
        self.failures[agent] = 0
        self.last_run[agent] = datetime.datetime.now()

    def record_failure(self, agent: str):
        self.failures[agent] += 1

    def is_disabled(self, agent: str) -> bool:
        if self.failures.get(agent, 0) >= 3:
            self.disabled.add(agent)
            return True
        return agent in self.disabled

    def should_run(self, agent: str, interval: int) -> bool:
        if agent in self.disabled:
            return False
        last = self.last_run.get(agent)
        if last is None:
            return True
        return (datetime.datetime.now() - last).total_seconds() >= interval


state = DaemonState()


# ── Signal handling ────────────────────────────────────────────────────

def handle_signal(signum, frame):
    sig_name = signal.Signals(signum).name
    log.info("Received %s — finishing current cycle, then shutting down...", sig_name)
    state.running = False

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)


# ── Agent runners ──────────────────────────────────────────────────────

def run_ingestor():
    log.info("Starting hourly cycle")
    try:
        from ingestor import run_ingestor_cycle
        added, stubs = run_ingestor_cycle()
        state.record_success('Ingestor')
        return True
    except Exception as e:
        log.error("Ingestor failed: %s", e)
        state.record_failure('Ingestor')
        return False


def run_improver():
    log.info("Starting hourly cycle")
    try:
        from improver import run_improver_cycle
        improved, failed = run_improver_cycle(n_pages=PARALLEL_WRITERS)
        state.record_success('Improver')
        return True
    except Exception as e:
        log.error("Improver failed: %s", e)
        state.record_failure('Improver')
        return False


def run_auditor():
    log.info("Starting daily cycle")
    try:
        from auditor import run_auditor_cycle
        report = run_auditor_cycle()
        state.record_success('Auditor')
        return True
    except Exception as e:
        log.error("Auditor failed: %s", e)
        state.record_failure('Auditor')
        return False


def run_librarian():
    log.info("Starting daily cycle")
    try:
        from librarian import run_librarian_cycle
        result = run_librarian_cycle()
        state.record_success('Librarian')
        return True
    except Exception as e:
        log.error("Librarian failed: %s", e)
        state.record_failure('Librarian')
        return False


def run_software_mapper():
    log.info("Starting weekly cycle")
    try:
        from software_mapper import run_software_mapper_cycle
        created = run_software_mapper_cycle()
        state.record_success('SoftwareMapper')
        return True
    except Exception as e:
        log.error("SoftwareMapper failed: %s", e)
        state.record_failure('SoftwareMapper')
        return False


def run_deep_research():
    log.info("Starting deep research cycle")
    try:
        from deep_research import run_deep_research_cycle
        added = run_deep_research_cycle()
        state.record_success('DeepResearch')
        return True
    except Exception as e:
        log.error("DeepResearch failed: %s", e)
        state.record_failure('DeepResearch')
        return False


# ── Agent schedule ─────────────────────────────────────────────────────

AGENTS = [
    ('Ingestor',       INGESTOR_INTERVAL,       run_ingestor),
    ('Improver',       IMPROVER_INTERVAL,        run_improver),
    ('DeepResearch',   DEEP_RESEARCH_INTERVAL,   run_deep_research),
    ('Auditor',        AUDITOR_INTERVAL,         run_auditor),
    ('Librarian',      LIBRARIAN_INTERVAL,       run_librarian),
    ('SoftwareMapper', SOFTWARE_MAPPER_INTERVAL, run_software_mapper),
]


# ── Startup ────────────────────────────────────────────────────────────

def print_banner():
    """Print startup info."""
    pages = get_all_pages()

    # Count by type
    entities = len([s for s in pages if os.path.exists(os.path.join(ENTITIES_DIR, f"{s}.md"))])
    concepts = len([s for s in pages if os.path.exists(os.path.join(CONCEPTS_DIR, f"{s}.md"))])
    comparisons = len([s for s in pages if os.path.exists(os.path.join(COMPARISONS_DIR, f"{s}.md"))])
    other = len(pages) - entities - concepts - comparisons

    # Count raw papers
    raw_count = 0
    if os.path.isdir(RAW_PAPERS_DIR):
        raw_count = len([f for f in os.listdir(RAW_PAPERS_DIR) if f.endswith('.md')])

    # Last update
    last_update = "never"
    last_update_file = os.path.join(META_DIR, 'last_update.txt')
    if os.path.exists(last_update_file):
        with open(last_update_file, 'r') as f:
            last_update = f.read().strip()[:19]

    log.info("Ralph daemon starting")
    log.info("Wiki root: %s", WIKI_ROOT)
    log.info("Pages: %d (%d entities, %d concepts, %d comparisons, %d other)",
             len(pages), entities, concepts, comparisons, other)
    log.info("Raw papers: %d", raw_count)
    log.info("Last ingest: %s", last_update)
    log.info("Agents: Ingestor(hourly) Improver(hourly) DeepResearch(6h) Auditor(daily) Librarian(daily) SoftwareMapper(weekly)")
    log.info("Models: writer=%s, reviewer=%s", WRITER_MODEL, REVIEWER_MODEL)
    log.info("Parallel writers: %d", PARALLEL_WRITERS)
    log.info("Log file: %s", RALPH_LOG)
    log.info("Ready. Ctrl+C to stop.")


# ── Main loop ──────────────────────────────────────────────────────────

def main_loop_with_agents(agents, poll_interval: int = 60):
    """
    Main event loop. Checks every poll_interval seconds which agents need to run.
    """
    log.info("Entering main loop (poll every %ds)", poll_interval)

    while state.running:
        state.cycle += 1
        any_ran = False

        for agent_name, interval, runner in agents:
            if not state.running:
                break

            if state.is_disabled(agent_name):
                if state.cycle % 100 == 0:  # Occasional reminder
                    log.warn("%s is disabled (3 consecutive failures)", agent_name)
                continue

            if state.should_run(agent_name, interval):
                log.info("── %s due ──", agent_name)
                success = runner()
                any_ran = True

                if not success and agent_name in state.disabled:
                    log.warn("%s disabled after 3 consecutive failures", agent_name)

        # Check if all agents disabled
        if len(state.disabled) >= len(agents):
            log.error("All agents disabled. Halting.")
            break

        if not any_ran:
            # Nothing to do — sleep
            # Find the soonest agent that will be ready
            sleep_until = poll_interval
            for agent_name, interval, _ in agents:
                if agent_name in state.disabled:
                    continue
                last = state.last_run.get(agent_name)
                if last:
                    elapsed = (datetime.datetime.now() - last).total_seconds()
                    remaining = max(0, interval - elapsed)
                    sleep_until = min(sleep_until, remaining)

            sleep_until = min(sleep_until, poll_interval)
            sleep_until = max(sleep_until, 10)  # minimum 10s
            log.info("Sleeping %ds until next cycle", int(sleep_until))

            # Sleep in small increments for responsive Ctrl+C
            end_time = time.time() + sleep_until
            while time.time() < end_time and state.running:
                time.sleep(min(5, end_time - time.time()))

    log.info("Ralph daemon stopped.")


def main_loop(poll_interval: int = 60):
    """Convenience wrapper using default AGENTS."""
    main_loop_with_agents(AGENTS, poll_interval)


# ── CLI ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Ralph Daemon — autonomous TVB Wiki improvement loop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/ralph_daemon.py              # Run normally
  python3 scripts/ralph_daemon.py --once       # Run each agent once, then exit
  python3 scripts/ralph_daemon.py --only Ingestor Improver  # Run only these agents
  python3 scripts/ralph_daemon.py --interval 30  # Check every 30s instead of 60s
"""
    )
    parser.add_argument("--once", action="store_true",
                        help="Run each due agent once, then exit")
    parser.add_argument("--only", nargs="+", choices=[a[0] for a in AGENTS],
                        help="Run only these agents")
    parser.add_argument("--interval", type=int, default=60,
                        help="Poll interval in seconds (default: 60)")
    parser.add_argument("--skip-ingestor", action="store_true",
                        help="Skip ingestor")
    parser.add_argument("--skip-improver", action="store_true",
                        help="Skip improver")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would run, don't execute")
    args = parser.parse_args()

    print_banner()

    if args.dry_run:
        log.info("DRY RUN — no agents will execute")
        for agent_name, interval, _ in AGENTS:
            if args.only and agent_name not in args.only:
                continue
            log.info("Would run: %s (every %ds)", agent_name, interval)
        return

    # Filter agents if --only specified
    active_agents = list(AGENTS)
    if args.only:
        active_agents = [(n, i, r) for n, i, r in AGENTS if n in args.only]
        log.info("Running only: %s", ', '.join(args.only))

    if args.skip_ingestor:
        active_agents = [(n, i, r) for n, i, r in active_agents if n != 'Ingestor']
    if args.skip_improver:
        active_agents = [(n, i, r) for n, i, r in active_agents if n != 'Improver']

    if args.once:
        # Run each agent once
        log.info("ONE-SHOT MODE — running each agent once")
        for agent_name, _, runner in active_agents:
            if not state.running:
                break
            log.info("── Running %s ──", agent_name)
            runner()
        log.info("One-shot complete.")
    else:
        # Replace AGENTS for main loop
        # (we need to pass it to main_loop)
        main_loop_with_agents(active_agents, poll_interval=args.interval)


if __name__ == '__main__':
    main()

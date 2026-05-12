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
    WRITER_MODEL, REVIEWER_MODEL, REPAIRER_MODEL,
    INGESTOR_INTERVAL, IMPROVER_INTERVAL, AUDITOR_INTERVAL,
    LIBRARIAN_INTERVAL, SOFTWARE_MAPPER_INTERVAL, ORPHAN_LINKER_INTERVAL,
    DEEP_RESEARCH_INTERVAL,
    MATCHER_INTERVAL,
    REPAIRER_INTERVAL,
    REF_FORMATTER_INTERVAL, CROSSLINK_APPLIER_INTERVAL,
    FULL_TEXT_INTERVAL,
    PARALLEL_WRITERS, PI_TIMEOUT,
    get_all_pages,
)

# Linter runs daily
LINTER_INTERVAL = 86400

log = get_logger("daemon")

# ── State ──────────────────────────────────────────────────────────────

class DaemonState:
    """Tracks when each agent last ran and consecutive failures."""

    def __init__(self):
        self.last_run = {
            'Matcher': None,
            'Ingestor': None,
            'Improver': None,
            'Auditor': None,
            'Librarian': None,
            'SoftwareMapper': None,
            'DeepResearch': None,
            'Repairer': None,
            'RefFormatter': None,
            'CrosslinkApplier': None,
            'Linter': None,
            'FullTextFetcher': None,
            'LinkRepair': None,
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

_last_sigint_time = 0.0


def handle_signal(signum, frame):
    global _last_sigint_time
    sig_name = signal.Signals(signum).name

    if signum == signal.SIGINT:
        now = time.monotonic()
        if now - _last_sigint_time < 1.0:
            log.info("Received second %s within 1s — shutting down immediately!", sig_name)
            sys.exit(1)
        _last_sigint_time = now

    log.info("Received %s — finishing current cycle, then shutting down... (Ctrl+C again within 1s to force)", sig_name)
    state.running = False


signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)


# ── Agent runners ──────────────────────────────────────────────────────

def run_linter():
    log.info("Starting daily lint cycle")
    try:
        from linter import run_linter_cycle
        report = run_linter_cycle()
        state.record_success('Linter')
        return True
    except Exception as e:
        log.error("Linter failed: %s", e)
        state.record_failure('Linter')
        return False


def run_ref_formatter():
    log.info("Starting reference formatting cycle")
    try:
        from ref_formatter import run_ref_formatter_cycle
        stats = run_ref_formatter_cycle()
        state.record_success('RefFormatter')
        return True
    except Exception as e:
        log.error("RefFormatter failed: %s", e)
        state.record_failure('RefFormatter')
        return False


def run_crosslink_applier():
    log.info("Starting crosslink applier cycle")
    try:
        from crosslink_applier import run_crosslink_applier_cycle
        stats = run_crosslink_applier_cycle()
        state.record_success('CrosslinkApplier')
        return True
    except Exception as e:
        log.error("CrosslinkApplier failed: %s", e)
        state.record_failure('CrosslinkApplier')
        return False


def run_matcher():
    log.info("Starting matcher cycle")
    try:
        from matcher import run_matcher_cycle
        stats = run_matcher_cycle()
        state.record_success('Matcher')
        # If sources attached to pages, trigger Improver for freshly-sourced stubs
        pages_with_new_sources = stats.get('pages_with_new_sources', 0) if isinstance(stats, dict) else 0
        if pages_with_new_sources > 0:
            log.info("Matcher attached sources to %d pages — triggering Improver", pages_with_new_sources)
            state.last_run['Improver'] = datetime.datetime.min  # force immediate run
        return True
    except Exception as e:
        log.error("Matcher failed: %s", e)
        state.record_failure('Matcher')
        return False


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


def run_full_text_fetcher():
    log.info("Starting full-text fetcher cycle")
    try:
        from full_text_fetcher import run_full_text_cycle
        count = run_full_text_cycle()
        state.record_success('FullTextFetcher')
        return True
    except Exception as e:
        log.error("FullTextFetcher failed: %s", e)
        state.record_failure('FullTextFetcher')
        return False


def run_link_repair():
    log.info("Starting link repair cycle")
    try:
        from link_repair import run_link_repair_cycle
        count = run_link_repair_cycle()
        state.record_success('LinkRepair')
        return True
    except Exception as e:
        log.error("LinkRepair failed: %s", e)
        state.record_failure('LinkRepair')
        return False


def run_orphan_linker():
    log.info("Starting bi-weekly cycle")
    try:
        from orphan_linker import run_orphan_linker_cycle
        added = run_orphan_linker_cycle()
        state.record_success('OrphanLinker')
        return True
    except Exception as e:
        log.error("OrphanLinker failed: %s", e)
        state.record_failure('OrphanLinker')
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


def run_repairer():
    log.info("Starting repair cycle")
    try:
        from repairer import run_repairer_cycle
        stats = run_repairer_cycle()
        state.record_success('Repairer')
        return True
    except Exception as e:
        log.error("Repairer failed: %s", e)
        state.record_failure('Repairer')
        return False


# ── Agent schedule ─────────────────────────────────────────────────────

AGENTS = [
    ('Improver',       IMPROVER_INTERVAL,              run_improver),
    ('RefFormatter',   REF_FORMATTER_INTERVAL,         run_ref_formatter),
    ('CrosslinkApplier', CROSSLINK_APPLIER_INTERVAL,   run_crosslink_applier),
    ('Ingestor',       INGESTOR_INTERVAL,             run_ingestor),
    ('Matcher',        MATCHER_INTERVAL,                run_matcher),
    ('DeepResearch',   DEEP_RESEARCH_INTERVAL,         run_deep_research),
    ('Auditor',        AUDITOR_INTERVAL,               run_auditor),
    ('Repairer',       REPAIRER_INTERVAL,              run_repairer),
    ('Librarian',      LIBRARIAN_INTERVAL,             run_librarian),
    ('Linter',         LINTER_INTERVAL,                run_linter),
    ('SoftwareMapper', SOFTWARE_MAPPER_INTERVAL,       run_software_mapper),
    ('OrphanLinker',   ORPHAN_LINKER_INTERVAL,         run_orphan_linker),
    ('FullTextFetcher', FULL_TEXT_INTERVAL,             run_full_text_fetcher),
    ('LinkRepair',     REPAIRER_INTERVAL,                run_link_repair),
]


# ── Model validation ───────────────────────────────────────────────────

def validate_models() -> list[str]:
    """Check that all configured Ollama models exist. Returns list of bad models."""
    import urllib.request, json as _json
    bad = []
    models = {WRITER_MODEL, REVIEWER_MODEL, REPAIRER_MODEL}
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = _json.loads(resp.read())
        available = {m['name'] for m in data.get('models', [])}
        for m in models:
            # Strip provider prefix for lookup
            name = m.split('/', 1)[-1] if '/' in m else m
            if name not in available:
                bad.append(m)
                log.error("Model not found on Ollama: %s (available: %s)",
                         m, ', '.join(sorted(available)[:10]))
    except Exception as e:
        log.warn("Could not validate models against Ollama: %s", e)
    return bad


# ── Startup ────────────────────────────────────────────────────────────

def print_banner():
    """Print startup info."""
    pages = get_all_pages()

    # Count by type (exclude 'index' slugs which are directory listings, not wiki pages)
    content_pages = {s: p for s, p in pages.items() if s != 'index'}
    entities = len([s for s in content_pages if os.path.exists(os.path.join(ENTITIES_DIR, f"{s}.md"))])
    concepts = len([s for s in content_pages if os.path.exists(os.path.join(CONCEPTS_DIR, f"{s}.md"))])
    comparisons = len([s for s in content_pages if os.path.exists(os.path.join(COMPARISONS_DIR, f"{s}.md"))])
    other = len(content_pages) - entities - concepts - comparisons

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
    agent_names = ', '.join(f"{a[0]}({a[1]//60}m)" if a[1] < 3600 else f"{a[0]}({a[1]//3600}h)" if a[1] < 86400 else f"{a[0]}({a[1]//86400}d)" for a in AGENTS)
    log.info("Agents: %s", agent_names)
    log.info("Models: writer=%s, reviewer=%s, repairer=%s", WRITER_MODEL, REVIEWER_MODEL, REPAIRER_MODEL)
    log.info("Parallel writers: %d", PARALLEL_WRITERS)
    log.info("Log file: %s", RALPH_LOG)
    log.info("Ready. Ctrl+C to stop.")


# ── Concurrent agent execution ─────────────────────────────────────────
import concurrent.futures

# Agent-specific parallelism: how many concurrent workers per agent
# Total concurrent workers = sum of these values.  Keep ≤ 10 for the
# subscription plan.
AGENT_MAX_WORKERS = {
    'Improver':       3,   # 3 pages in parallel (writer→reviewer chains)
    'FullTextFetcher': 2, # fetch + extract can overlap
    'CrosslinkApplier': 2, # CPU-heavy, embarrassingly parallel
    'DeepResearch':  2,   # independent gap analyses
    'Matcher':       1,   # embedding cache is single-threaded
    'Auditor':       1,   # full scan; parallel would thrash disk
    'Repairer':      1,   # in-place edits; conflict risk
    'RefFormatter':  1,   # in-place edits; conflict risk
    'Ingestor':      1,   # sequential downloads
    'Librarian':     1,   # fast catalog rebuild
    'Linter':        1,   # fast
    'SoftwareMapper': 1, # weekly, fast
    'OrphanLinker':  1,   # weekly, fast
    'LinkRepair':    1,   # in-place edits
}

_agent_executors = {}  # agent_name -> ThreadPoolExecutor
_agent_futures = {}     # agent_name -> Future
_agent_start_times = {}  # agent_name -> datetime of last launch
FUTURE_TIMEOUT = 1800  # 30 min max per agent run before force-cancel

def _run_agent_async(agent_name: str, runner) -> bool:
    """Run an agent in a background thread. Returns immediately.
    Returns False if the agent is already running.
    """
    global _agent_futures
    
    # Check if already running
    future = _agent_futures.get(agent_name)
    if future and not future.done():
        # Check timeout — force-cancel if agent ran too long
        start_time = _agent_start_times.get(agent_name)
        if start_time and (datetime.datetime.now() - start_time).total_seconds() > FUTURE_TIMEOUT:
            log.warn("%s timed out after %.0fs — force-cancelling", agent_name, FUTURE_TIMEOUT)
            future.cancel()
            del _agent_futures[agent_name]
            _agent_start_times.pop(agent_name, None)
            return False  # Allow re-launch
        log.info("%s still running from last cycle — skipping", agent_name)
        return False  # Agent is still running, NOT successfully handled
    
    # Clean up done futures
    if future and future.done():
        try:
            result = future.result(timeout=0)
            if not result and agent_name in state.disabled:
                log.warn("%s disabled after failure", agent_name)
        except Exception as e:
            log.error("%s thread raised: %s", agent_name, e)
        del _agent_futures[agent_name]
    
    # Launch new thread
    n_workers = AGENT_MAX_WORKERS.get(agent_name, 1)
    executor = _agent_executors.setdefault(agent_name, concurrent.futures.ThreadPoolExecutor(max_workers=n_workers))
    _agent_futures[agent_name] = executor.submit(runner)
    _agent_start_times[agent_name] = datetime.datetime.now()
    log.info("── %s launched in background (%d workers) ──", agent_name, n_workers)
    return True


# ── Main loop ──────────────────────────────────────────────────────────

def main_loop_with_agents(agents, poll_interval: int = 60):
    """
    Main event loop. Checks every poll_interval seconds which agents need to run.
    Agents execute concurrently in background threads.
    """
    log.info("Entering main loop (poll every %ds, agents run concurrently)", poll_interval)

    while state.running:
        state.cycle += 1
        any_launched = False

        for agent_name, interval, runner in agents:
            if not state.running:
                break

            if state.is_disabled(agent_name):
                if state.cycle % 100 == 0:  # Occasional reminder
                    log.warn("%s is disabled (3 consecutive failures)", agent_name)
                continue

            if state.should_run(agent_name, interval):
                # Check if already running
                future = _agent_futures.get(agent_name)
                if future and not future.done():
                    start_time = _agent_start_times.get(agent_name)
                    if start_time and (datetime.datetime.now() - start_time).total_seconds() > FUTURE_TIMEOUT:
                        log.warn("%s timed out after %.0fs — force-cancelling in main loop", agent_name, FUTURE_TIMEOUT)
                        future.cancel()
                        del _agent_futures[agent_name]
                        _agent_start_times.pop(agent_name, None)
                        # Re-launch below
                    else:
                        log.info("%s still running — not starting new cycle", agent_name)
                        continue
                    
                # Clean up done futures
                if future and future.done():
                    try:
                        result = future.result(timeout=0)
                        if not result and agent_name in state.disabled:
                            log.warn("%s disabled after failure", agent_name)
                    except Exception as e:
                        log.error("%s thread raised: %s", agent_name, e)
                    del _agent_futures[agent_name]
                
                # Launch
                n_workers = AGENT_MAX_WORKERS.get(agent_name, 1)
                executor = _agent_executors.setdefault(agent_name, concurrent.futures.ThreadPoolExecutor(max_workers=n_workers))
                future = executor.submit(runner)
                _agent_futures[agent_name] = future
                _agent_start_times[agent_name] = datetime.datetime.now()
                log.info("── %s launched (%d workers) ──", agent_name, n_workers)
                any_launched = True

        # Check if all agents disabled
        if len(state.disabled) >= len(agents):
            log.error("All agents disabled. Halting.")
            break

        if not any_launched:
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
                
            # Check for completed futures during sleep and process results
            for agent_name, future in list(_agent_futures.items()):
                if not future.done():
                    start_time = _agent_start_times.get(agent_name)
                    if start_time and (datetime.datetime.now() - start_time).total_seconds() > FUTURE_TIMEOUT:
                        log.warn("%s timed out during sleep — force-cancelling", agent_name)
                        future.cancel()
                        del _agent_futures[agent_name]
                        _agent_start_times.pop(agent_name, None)
                    continue
                if future.done():
                    try:
                        result = future.result(timeout=0)
                        if not result and agent_name in state.disabled:
                            log.warn("%s disabled after failure", agent_name)
                    except Exception as e:
                        log.error("%s thread raised: %s", agent_name, e)
                    del _agent_futures[agent_name]
        else:
            # Something launched — short sleep to let threads start, then check others
            time.sleep(2)
            
            # Process any completed futures
            for agent_name, future in list(_agent_futures.items()):
                if not future.done():
                    start_time = _agent_start_times.get(agent_name)
                    if start_time and (datetime.datetime.now() - start_time).total_seconds() > FUTURE_TIMEOUT:
                        log.warn("%s timed out — force-cancelling", agent_name)
                        future.cancel()
                        del _agent_futures[agent_name]
                        _agent_start_times.pop(agent_name, None)
                    continue
                if future.done():
                    try:
                        result = future.result(timeout=0)
                        if not result and agent_name in state.disabled:
                            log.warn("%s disabled after failure", agent_name)
                    except Exception as e:
                        log.error("%s thread raised: %s", agent_name, e)
                    del _agent_futures[agent_name]

    log.info("Ralph daemon stopped.")
    
    # Shutdown executors
    for name, executor in _agent_executors.items():
        executor.shutdown(wait=False)
        log.info("Shutdown executor for %s", name)


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

    # Validate models before starting
    bad_models = validate_models()
    if bad_models:
        from ralph_config import WRITER_MODEL, REVIEWER_MODEL, REPAIRER_MODEL
        # Map agent → model
        model_map = {
            'Improver': WRITER_MODEL,
            'Matcher': WRITER_MODEL,
            'DeepResearch': WRITER_MODEL,
            'Repairer': REPAIRER_MODEL,
        }
        for agent_name, model in model_map.items():
            if model in bad_models:
                log.error("Disabling %s: model %s not available", agent_name, model)
                state.disabled.add(agent_name)
                state.failures[agent_name] = 99

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

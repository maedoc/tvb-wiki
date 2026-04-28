#!/usr/bin/env python3
"""
Shared configuration and utilities for the Ralph daemon and agents.
All paths derived from __file__, no hardcoded user paths.
"""
import os
import sys
import re
import json
import datetime
import logging
import subprocess
import frontmatter
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_ROOT = os.path.dirname(SCRIPTS_DIR)

META_DIR = os.path.join(WIKI_ROOT, "meta")
RAW_PAPERS_DIR = os.path.join(WIKI_ROOT, "raw", "papers")
ENTITIES_DIR = os.path.join(WIKI_ROOT, "entities")
CONCEPTS_DIR = os.path.join(WIKI_ROOT, "concepts")
COMPARISONS_DIR = os.path.join(WIKI_ROOT, "comparisons")
INDEX_PATH = os.path.join(WIKI_ROOT, "index.md")          # landing page (read-only for agents)
CATALOG_PATH = os.path.join(WIKI_ROOT, "catalog.md")        # machine-generated catalog
LOG_MD = os.path.join(WIKI_ROOT, "log.md")
SCHEMA_PATH = os.path.join(WIKI_ROOT, "SCHEMA.md")
RALPH_LOG = os.path.join(SCRIPTS_DIR, "ralph.log")

LAST_UPDATE_FILE = os.path.join(META_DIR, "last_update.txt")
ENTITY_COUNTS_FILE = os.path.join(META_DIR, "entity_counts.json")
AUDIT_REPORT_FILE = os.path.join(META_DIR, "audit_report.json")

# ── Models ─────────────────────────────────────────────────────────────
WRITER_MODEL = "ollama/minimax-m2.5:cloud"
REVIEWER_MODEL = "ollama/glm-5.1:cloud"
REPAIRER_MODEL = "ollama/gpt-oss:120b-cloud"

# ── Parallelism ────────────────────────────────────────────────────────
PARALLEL_WRITERS = 3
PARALLEL_REVIEWERS = 5
PARALLEL_INGESTORS = 5

# ── Agent schedule (seconds) ──────────────────────────────────────────
INGESTOR_INTERVAL = 86400       # daily + startup (TVB is niche, ~5-10 papers/week)
IMPROVER_INTERVAL = 3600       # hourly
AUDITOR_INTERVAL = 86400       # daily
LIBRARIAN_INTERVAL = 86400     # daily
SOFTWARE_MAPPER_INTERVAL = 604800  # weekly
DEEP_RESEARCH_INTERVAL = 259200   # 2x/week + on-demand (only when Matcher reports gaps)
MATCHER_INTERVAL    = 21600    # 6 hours (was 1h; Matcher needs 1-2h to complete)
REPAIRER_INTERVAL = 86400         # daily (runs after Auditor)
REF_FORMATTER_INTERVAL = 86400     # daily (runs after Matcher)
CROSSLINK_APPLIER_INTERVAL = 86400  # daily (replaces weekly Crosslink)

# ── Git push schedule ─────────────────────────────────────────────────────
# Push to the remote at most once per hour (default). Adjust PUSH_INTERVAL if needed.
PUSH_INTERVAL = 3600  # seconds
LAST_PUSH_FILE = os.path.join(META_DIR, "last_push.txt")

# ── Error handling ─────────────────────────────────────────────────────
PI_TIMEOUT = 300               # 5 min per pi subprocess
MAX_RETRIES = 3
RETRY_BACKOFF = [10, 30, 90]   # seconds between retries
CIRCUIT_BREAKER_THRESHOLD = 3  # consecutive failures to disable agent

# ── Logging ────────────────────────────────────────────────────────────

class AgentLogger:
    """Dual-output logger: stdout + ralph.log, with agent-tagged lines."""

    def __init__(self, name: str):
        self.name = name
        self._setup_file_logger()

    def _setup_file_logger(self):
        os.makedirs(os.path.dirname(RALPH_LOG), exist_ok=True)
        self._file_handler = logging.FileHandler(RALPH_LOG, mode='a')
        self._file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
        ))

    def _emit(self, level, msg, *args):
        text = msg % args if args else msg
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f"{timestamp} [{self.name}] {text}"

        # stdout
        prefix = {"ERROR": "❌", "WARN": "⚠️", "INFO": ""}.get(level, "")
        print(f"{prefix}{line}" if prefix else line, flush=True)

        # file
        self._file_handler.emit(logging.LogRecord(
            name="ralph", level=getattr(logging, level, logging.INFO),
            pathname="", lineno=0, msg=line, args=(), exc_info=None
        ))

    def info(self, msg, *args):
        self._emit("INFO", msg, *args)

    def warn(self, msg, *args):
        self._emit("WARN", msg, *args)

    def error(self, msg, *args):
        self._emit("ERROR", msg, *args)


def get_logger(name: str) -> AgentLogger:
    return AgentLogger(name)


# ── Git helpers ────────────────────────────────────────────────────────

def git_commit(message: str, cwd: str = None) -> bool:
    """Stage all changes and commit. Returns True if something was committed.
    After a successful commit, optionally push to the remote, but only at most
    once per PUSH_INTERVAL (default 1 hour) to avoid excessive network traffic.
    """
    cwd = cwd or WIKI_ROOT
    # Check for changes
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=cwd, capture_output=True, text=True
    )
    if not result.stdout.strip():
        return False

    subprocess.run(["git", "add", "."], cwd=cwd, capture_output=True)
    result = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=cwd, capture_output=True, text=True
    )
    if result.returncode != 0:
        return False

    # --- optional push -----------------------------------------------------
    _maybe_git_push(cwd)
    return True

def _maybe_git_push(cwd: str):
    """Push to the remote if the last push was more than PUSH_INTERVAL ago.
    The timestamp of the last successful push is stored in LAST_PUSH_FILE as an
    ISO‑8601 datetime string.
    """
    try:
        now = datetime.datetime.now()
        # read last push time if present
        last_push = None
        if os.path.exists(LAST_PUSH_FILE):
            with open(LAST_PUSH_FILE, "r", encoding="utf-8") as f:
                txt = f.read().strip()
                if txt:
                    last_push = datetime.datetime.fromisoformat(txt)
        if last_push is None or (now - last_push).total_seconds() >= PUSH_INTERVAL:
            push_res = subprocess.run(["git", "push"], cwd=cwd, capture_output=True, text=True)
            if push_res.returncode == 0:
                with open(LAST_PUSH_FILE, "w", encoding="utf-8") as f:
                    f.write(now.isoformat())
            else:
                print(f"⚠️ Git push failed: {push_res.stderr.strip()}")
    except Exception as e:
        print(f"⚠️ Exception during git push: {e}")


def append_log(message: str):
    """Append a timestamped entry to log.md."""
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(LOG_MD, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{ts}] {message}\n")


# ── Wiki page utilities ───────────────────────────────────────────────

def get_all_pages() -> dict[str, str]:
    """Return {page_slug: absolute_path} for all wiki content pages."""
    pages = {}
    for directory in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
        if not os.path.isdir(directory):
            continue
        for fn in os.listdir(directory):
            if fn.endswith('.md') and fn != 'index.md':
                slug = fn[:-3]
                pages[slug] = os.path.join(directory, fn)
    return pages


def get_all_wikilinks() -> tuple[set[tuple[str, str]], set[str]]:
    """
    Return (links, pages) where:
      links = {(target_slug, source_slug), ...}
      pages = {slug, ...}
    """
    links = set()
    pages = set()

    for directory in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
        if not os.path.isdir(directory):
            continue
        for fn in os.listdir(directory):
            if not fn.endswith('.md'):
                continue
            slug = fn[:-3]
            pages.add(slug)
            filepath = os.path.join(directory, fn)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                for match in re.findall(r'\[\[([^\]]+)\]\]', content):
                    target = match.split('|')[0].strip().lower().replace(' ', '-').replace('\u2011', '-')
                    links.add((target, slug))
            except Exception:
                pass
    return links, pages


def load_frontmatter(filepath: str) -> dict:
    """Load YAML frontmatter from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        return dict(post.metadata)
    except Exception:
        return {}


def save_page(filepath: str, metadata: dict, content: str):
    """Save a page with updated frontmatter."""
    post = frontmatter.load(filepath) if os.path.exists(filepath) else frontmatter.Post("")
    for k, v in metadata.items():
        post.metadata[k] = v
    post.content = content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


def read_page(filepath: str) -> tuple[dict, str]:
    """Read a page, return (metadata_dict, body_string)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    return dict(post.metadata), post.content


def word_count(text: str) -> int:
    """Count words in text, excluding frontmatter."""
    return len(text.split())


def has_placeholder(text: str) -> bool:
    """Check if text contains placeholder markers."""
    return '*Placeholder*' in text or '*placeholder*' in text


def get_sources(metadata: dict) -> list[str]:
    """Get sources list from frontmatter. Normalizes dict entries to strings."""
    sources = metadata.get('sources', [])
    if isinstance(sources, str):
        sources = [s.strip() for s in sources.split(',') if s.strip()]
    # Normalize dict sources (e.g. {url: ..., description: ...}) to plain strings
    result = []
    for s in sources:
        if isinstance(s, dict):
            result.append(s.get('url', s.get('path', str(s))))
        elif isinstance(s, str):
            result.append(s)
    return result


# ── pi subprocess runner ──────────────────────────────────────────────

def run_pi(prompt: str, model: str = None, tools: str = None,
           timeout: int = None, cwd: str = None, no_session: bool = False) -> tuple[bool, str]:
    """
    Run pi as a subprocess. Returns (success, output_or_error).
    Handles timeouts and captures stderr.
    """
    model = model or WRITER_MODEL
    timeout = timeout or PI_TIMEOUT
    cwd = cwd or WIKI_ROOT

    cmd = ["pi", "--model", model, "--mode", "text", "-p", prompt]
    if no_session:
        cmd.append("--no-session")
    if tools:
        cmd.extend(["--tools", tools])

    log = get_logger("pi")

    for attempt in range(MAX_RETRIES):
        try:
            log.info("Spawning: pi --model %s (%d tokens in prompt, attempt %d/%d)",
                     model, len(prompt.split()), attempt + 1, MAX_RETRIES)
            start = datetime.datetime.now()
            result = subprocess.run(
                cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout
            )
            elapsed = (datetime.datetime.now() - start).total_seconds()

            if result.returncode != 0:
                stderr = result.stderr.strip()
                # Classify the error
                # Check model-not-found BEFORE generic ollama check
                # (stderr says "for provider 'ollama'" even on 404s)
                if "connection refused" in stderr.lower():
                    log.warn("Ollama connection issue: %s", stderr[:200])
                elif "not found" in stderr.lower() and "model" in stderr.lower():
                    log.error("Model not found: %s", stderr[:200])
                    return False, stderr
                elif "ollama" in stderr.lower():
                    log.warn("Ollama connection issue: %s", stderr[:200])
                elif "rate" in stderr.lower():
                    log.warn("Rate limited, sleeping 60s")
                    import time; time.sleep(60)
                    continue
                elif "401" in stderr or "auth" in stderr.lower():
                    log.error("Auth failure: %s", stderr[:200])
                    return False, stderr
                else:
                    log.warn("pi exited %d: %s", result.returncode, stderr[:200])

                if attempt < MAX_RETRIES - 1:
                    import time
                    time.sleep(RETRY_BACKOFF[min(attempt, len(RETRY_BACKOFF) - 1)])
                continue

            output = result.stdout.strip()
            if not output:
                log.warn("pi returned empty output (attempt %d)", attempt + 1)
                if attempt < MAX_RETRIES - 1:
                    continue
                return False, "Empty output from pi"

            log.info("pi completed in %.1fs (%d chars out)", elapsed, len(output))
            return True, output

        except subprocess.TimeoutExpired:
            log.warn("pi timeout after %ds (attempt %d/%d)", timeout, attempt + 1, MAX_RETRIES)
            if attempt < MAX_RETRIES - 1:
                import time
                time.sleep(RETRY_BACKOFF[min(attempt, len(RETRY_BACKOFF) - 1)]
)
        except Exception as e:
            log.error("pi exception: %s", str(e)[:200])
            return False, str(e)

    return False, f"Failed after {MAX_RETRIES} retries"


# ── Search queries ─────────────────────────────────────────────────────

SEARCH_QUERIES = [
    # Direct TVB
    '"The Virtual Brain"',
    'TVB AND (connectome OR whole-brain)',
    # Neural mass models (TVB's core)
    '"neural mass model" AND (connectome OR whole-brain)',
    '"Wilson-Cowan" AND (brain OR cortical)',
    '"Jansen-Rit"',
    '"Epileptor" AND (seizure OR epilepsy)',
    '"Wong-Wang" AND (decision OR whole-brain)',
    '"Larter-Breakspear"',
    '"Stefanescu-Jirsa"',
    '"mean-field" AND (cortical OR brain)',
    # Connectomics
    '"structural connectivity" AND (DTI OR tractography OR connectome)',
    '"functional connectivity" AND (resting-state OR fMRI)',
    '"effective connectivity" AND (DCM OR dynamic causal)',
    # Whole-brain modeling
    '"whole-brain model" OR "whole brain simulation"',
    '"brain network" AND (simulation OR modeling)',
    '"personalized brain"',
    # Software ecosystem
    'NEST AND (spiking AND brain)',
    'NEURON AND (simulation AND neuron)',
    '"dynamic causal modeling" AND SPM',
    # Applications
    'epilepsy AND (modeling OR simulation) AND (brain OR cortical)',
    '"resting-state" AND (bifurcation OR dynamics)',
    '"connectome" AND (aging OR development)',
]

# ── Keyword map for entity extraction ──────────────────────────────────

KEYWORD_MAP = {
    'software': [
        ('TVB', 'tvb', 'software-tvb'),
        ('The Virtual Brain', 'tvb', 'software-tvb'),
        ('NEST', 'nest', 'software-nest'),
        ('NEURON', 'neuron', 'software-neuron'),
        ('Brian', 'brian', 'software-brian'),
        ('ANTs', 'ants', 'software-ants'),
        ('SPM', 'spm', 'software-spm'),
        ('FSL', 'fsl', 'software-fsl'),
        ('FreeSurfer', 'freesurfer', 'software-freesurfer'),
        ('FieldTrip', 'fieldtrip', 'software-fieldtrip'),
        ('MNE-Python', 'mne-python', 'software-mne'),
        ('MNE', 'mne-python', 'software-mne'),
        ('MRtrix', 'mrtrix', 'software-mrtrix'),
        ('GraphVar', 'graphvar', 'software-graphvar'),
        ('DynaSim', 'dynasim', 'software-dynasim'),
        ('EEGLAB', 'eeglab', 'software-eeglab'),
        ('Brainstorm', 'brainstorm', 'software-brainstorm'),
        ('Nilearn', 'nilearn', 'software-nilearn'),
        ('CONN', 'conn', 'software-conn'),
        ('Arbor', 'arbor', 'software-arbor'),
        ('CoreNEURON', 'coreneuron', 'software-coreneuron'),
    ],
    'concepts': [
        ('neural mass model', 'neural-mass-models', 'neural-mass-models'),
        ('Wilson-Cowan', 'wilson-cowan', 'neural-mass-models'),
        ('Jansen-Rit', 'jansen-rit', 'neural-mass-models'),
        ('Epileptor', 'epileptor', 'epilepsy-modeling'),
        ('Wong-Wang', 'wong-wang', 'neural-mass-models'),
        ('Larter-Breakspear', 'larter-breakspear', 'neural-mass-models'),
        ('Stefanescu-Jirsa', 'stefanescu-jirsa', 'neural-mass-models'),
        ('fMRI', 'fmri', 'neuroimaging-fmri'),
        ('EEG', 'eeg', 'neuroimaging-eeg'),
        ('MEG', 'meg', 'neuroimaging-meg'),
        ('DTI', 'dti', 'neuroimaging-dti'),
        ('diffusion MRI', 'diffusion-mri', 'neuroimaging-dti'),
        ('functional connectivity', 'functional-connectivity', 'functional-connectivity'),
        ('structural connectivity', 'structural-connectivity', 'structural-connectivity'),
        ('effective connectivity', 'effective-connectivity', 'effective-connectivity'),
        ('resting-state', 'resting-state', 'resting-state'),
        ('whole-brain', 'whole-brain', 'whole-brain-modeling'),
        ('connectomics', 'connectomics', 'connectomics'),
        ('connectome', 'connectome', 'connectomics'),
        ('brain network', 'brain-network', 'network-dynamics'),
        ('dynamic causal modeling', 'dynamic-causal-modeling', 'dynamic-causal-modeling'),
        ('DCM', 'dynamic-causal-modeling', 'dynamic-causal-modeling'),
        ('mean-field theory', 'mean-field-theory', 'mean-field-theory'),
        ('variational Bayes', 'variational-inference', 'variational-bayes'),
        ('bifurcation analysis', 'bifurcation-analysis', 'bifurcation-analysis'),
        ('tractography', 'tractography', 'tractography'),
        ('graph theory', 'graph-theory', 'network-dynamics'),
        ('spiking neural network', 'spiking-neural-networks', 'spiking-neural-networks'),
        ('BOLD signal', 'bold-signal', 'neuroimaging-fmri'),
        ('forward model', 'forward-model', 'whole-brain-modeling'),
        ('source localization', 'source-localization', 'neuroimaging-eeg'),
        ('parcellation', 'parcellation', 'connectomics'),
        ('epilepsy modeling', 'epilepsy-modeling', 'epilepsy-modeling'),
        ('seizure prediction', 'seizure-prediction', 'epilepsy-modeling'),
    ]
}

# Build reverse map: keyword -> (slug, tag, category)
REVERSE_MAP = {}
for category, items in KEYWORD_MAP.items():
    for (keyword, slug, tag) in items:
        REVERSE_MAP[keyword] = (slug, tag, category)

# ── pi subprocess runner with token metrics ──────────────────────────────

# Simple JSON accumulator for pi --mode json
class PIJsonAccumulator:
    """Parse pi --mode json output into text + usage metrics."""
    def __init__(self):
        self.usage = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0}
        self.full_text = ""
        self.model = ""
        self.provider = ""
    
    def feed(self, line: str):
        try:
            data = json.loads(line)
        except:
            return
        t = data.get("type", "")
        if t == "message_end":
            msg = data.get("message", {})
            if msg.get("role") == "assistant":
                # Extract text
                for c in msg.get("content", []):
                    if c.get("type") == "text":
                        self.full_text += c.get("text", "")
                    elif c.get("type") == "thinking":
                        # Optional: include thinking text inline for debugging
                        pass
                # Extract usage
                u = msg.get("usage", {})
                self.usage["input"] = u.get("input", self.usage["input"])
                self.usage["output"] = u.get("output", self.usage["output"])
                self.usage["cacheRead"] = u.get("cacheRead", self.usage["cacheRead"])
                self.usage["cacheWrite"] = u.get("cacheWrite", self.usage["cacheWrite"])
                # Extract model
                self.model = msg.get("model", self.model)
                self.provider = msg.get("provider", self.provider)


def run_pi_with_metrics(prompt: str, model: str = None, tools: str = None,
                        timeout: int = None, cwd: str = None, no_session: bool = False) -> tuple[bool, str, dict]:
    """
    Run pi as a subprocess. Returns (success, text, metrics_dict).
    Handles timeouts and captures stderr.
    Uses --mode json to extract exact token counts.
    """
    model = model or WRITER_MODEL
    timeout = timeout or PI_TIMEOUT
    cwd = cwd or WIKI_ROOT
    
    cmd = ["pi", "--model", model, "--mode", "json", "-p", prompt]
    if no_session:
        cmd.append("--no-session")
    if tools:
        cmd.extend(["--tools", tools])

    log = get_logger("pi")
    logger_dash = get_logger("llm_metrics")

    start = datetime.datetime.now()
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    elapsed = (datetime.datetime.now() - start).total_seconds()

    acc = PIJsonAccumulator()
    for line in proc.stdout.splitlines():
        acc.feed(line)

    # Fallback: if json parse failed, try raw text
    text = acc.full_text if acc.full_text else proc.stdout

    metrics = {
        "model": model,
        "provider": acc.provider,
        "resolved_model": acc.model,
        "input_tokens": acc.usage.get("input", 0),
        "output_tokens": acc.usage.get("output", 0),
        "cache_read": acc.usage.get("cacheRead", 0),
        "cache_write": acc.usage.get("cacheWrite", 0),
        "latency_sec": elapsed,
        "throughput_tok_per_sec": acc.usage.get("output", 0) / elapsed if elapsed > 0 else 0,
        "retry_count": 0,
        "error": None,
    }

    if proc.returncode != 0:
        stderr = proc.stderr.strip()
        metrics["error"] = stderr[:200]
        # Classify error (same logic as run_pi)
        if "not found" in stderr.lower() and "model" in stderr.lower():
            log.error("Model not found: %s", stderr[:200])
            return False, stderr, metrics
        log.warn("pi exited %d: %s", proc.returncode, stderr[:200])
        return False, stderr, metrics

    if not text:
        metrics["error"] = "empty output"
        log.warn("pi returned empty output")
        return False, "Empty output", metrics

    log.info("pi: %s in=%d out=%d t=%.1fs th=%.1f/s",
             model, metrics["input_tokens"], metrics["output_tokens"],
             elapsed, metrics["throughput_tok_per_sec"])

    # Log to dedicated metrics file
    logger_dash.info("metrics %s", json.dumps(metrics))

    return True, text, metrics

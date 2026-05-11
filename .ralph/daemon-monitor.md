# Daemon Performance Monitor

## Goal
Poll daemon every 5 minutes and track performance metrics until tomorrow. Report summaries.

## Checklist
- [ ] Run monitor_daemon.py and check recent log activity
- [ ] Track: Matcher cycles complete, Improver pages improved, repo growth, LLM call stats
- [ ] Watch for: stuck agents, LLM timeouts, citation growth
- [ ] Restart daemon if FUTURE_TIMEOUT kicks in (30 min)
- [ ] Report summary every hour

## Key metrics
- Matcher: cycle time, pages matched, sources attached
- Improver: pages improved, MAJOR/MINOR issues
- Ingestor: new papers found
- CrosslinkApplier: links added
- FullTextFetcher: PDFs fetched
- LLM: calls, tokens, timeouts
- Repo: total pages, citations, broken links
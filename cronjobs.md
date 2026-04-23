# TVB-Wiki Hermes Cron Jobs

> Archived from: `ocduke:~/.hermes/cron/jobs.json`  
> Source: Hermes agent runtime on ocduke (ran for ~1 week)

## Overview

| ID | Name | Schedule | Status | Last Run | Next Run | Runs Completed |
|----|------|----------|--------|----------|----------|----------------|
| `76d551339d2b` | TVB Wiki Hourly Full Pipeline | `0 * * * *` | ✅ ok | 2026-04-23T10:03:02+00:00 | 2026-04-23T11:00:00+00:00 | 46 |
| `f5e84961f382` | TVB Wiki Daily Lint | `0 3 * * *` | ✅ ok | 2026-04-23T03:07:10+00:00 | 2026-04-24T03:00:00+00:00 | 3 |
| `ca39d1ce73b4` | TVB Wiki Daily Discord Summary | `0 9 * * *` | ✅ ok | 2026-04-23T09:13:40+00:00 | 2026-04-24T09:00:00+00:00 | 2 |

---

## 1. TVB Wiki Hourly Full Pipeline

**ID:** `76d551339d2b`  
**Created:** 2026-04-20T07:17:18.896400+00:00  
**Delivery:** local (Telegram chat: marmaduke woodman)

### Schedule
- **Cron Expression:** `0 * * * *`
- **Frequency:** Every hour at minute 0

### Workflow

#### Step 1: Run the pipeline
Executes `python3 ~/tvb-wiki/scripts/hourly_full.py` which:
- Fetches new papers from arXiv, PubMed, bioRxiv, OpenAlex, and Semantic Scholar
- Syncs changes to docs
- Builds the static site
- Commits changes

**Output:** Report how many papers were added and any errors.

#### Step 2: Pick a random page to improve
Executes `python3 ~/tvb-wiki/scripts/pick_random_page.py` which:
- Outputs a randomly selected wiki page
- Identifies issues: placeholders, missing links, short sections, stale content, etc.

#### Step 3: Make one concrete improvement
Reads the selected page and makes ONE focused improvement:
- Replace placeholder text with real content
- Add missing wikilinks to related pages
- Expand a thin section with a paragraph or two
- Add a reference/citation from raw/papers/
- Fix stale or incorrect information
- Improve clarity or structure

**Constraints:**
- Only edit the ONE selected page
- Do not touch other files
- Keep changes small and reviewable (preferably under 50 lines)
- Maintain existing frontmatter and conventions
- Run `git diff` to show what changed
- If page looks genuinely good, skip the edit and note why

#### Step 4: Commit if changed
If an edit was made, commit with a descriptive message like:  
`"Improve <page-name>: <what you did>"`

**Final Output:** Report the pipeline results and the page improvement (or skip reason).  
If genuinely nothing happened, respond with exactly `[SILENT]`.

---

## 2. TVB Wiki Daily Lint

**ID:** `f5e84961f382`  
**Created:** 2026-04-20T07:18:49.535085+00:00  
**Delivery:** local (Telegram chat: marmaduke woodman)

### Schedule
- **Cron Expression:** `0 3 * * *`
- **Frequency:** Daily at 03:00 UTC

### Task
Runs the daily lint script for the TVB wiki using `python3 ~/tvb-wiki/scripts/daily_lint.py`.

Ensure the script runs with the correct environment.

---

## 3. TVB Wiki Daily Discord Summary

**ID:** `ca39d1ce73b4`  
**Created:** 2026-04-21T19:08:53.740419+00:00  
**Delivery:** Discord (Channel: `1495906497232896121`)

### Schedule
- **Cron Expression:** `0 9 * * *`
- **Frequency:** Daily at 09:00 UTC

### Task
Generates and sends the daily TVB wiki summary.

Executes `python3 ~/tvb-wiki/scripts/daily_summary.py` and presents the output as the final response, which is automatically delivered to Discord.

---

## Origin Context

All three jobs were created by **marmaduke woodman** via Telegram and are associated with the TVB-Wiki project on ocduke. The Hermes agent was running for approximately one week (as of 2026-04-23) with these scheduled tasks automating:

1. **Content ingestion** (hourly pipeline)
2. **Quality control** (daily linting)
3. **Team communication** (daily Discord summaries)

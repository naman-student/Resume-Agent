# Job Research Agent Guide

This guide defines the standard workflow for an agent that searches for fresh jobs and writes candidates into Supabase `public.researched_jobs`.

The research agent's job is to fill the research inbox with **verified-open, specific, well-fit roles**. It must not insert vague placeholder URLs, unverified postings, or low-fit roles. It must not create tailored resumes and must not mutate the main application pipeline unless the user explicitly asks.

## Core Principle

```text
Repo resumes + strategy notes = candidate profile
Supabase tables                = memory and exclusions
Web search + WebFetch          = fresh supply
researched_jobs                = research inbox (verified-open, specific URLs only)
jobs                           = committed pipeline
dashboard                      = human control
```

## Non-negotiables (read before inserting anything)

1. **Specific posting URL only.** A `/careers` or `/jobs` landing page is not a posting — do not insert it. See §URL Validation.
2. **Verify openness before insert.** Every row must have evidence in `research_notes` proving the posting was live on the day of insert. See §Verification Protocol.
3. **Reject past-deadline and stale postings.** If the listing has a deadline before today, or a publish date >90 days old, do not insert. See §Staleness Check.
4. **`source` must be non-null.** If you can't label what ATS the URL belongs to, you're not ready to insert.
5. **fit_score ≥ 70 only.** No "target-company aligned" loophole. See §Scoring.
6. **`research_notes` must contain a verification evidence string.** See §Required Insert Shape.

These are hard rules. A row that violates any of them is bad data and must be skipped, not inserted. The cost of a missed role is far less than the cost of polluting the inbox.

## Tables

| Table | Purpose |
|---|---|
| `researched_jobs` | Broad research inbox for jobs found by agents |
| `jobs` | Committed pipeline for roles being tailored/applied |
| `companies` | User's company list and personal notes |

Research agents write to `researched_jobs` only. If a target company has no specific posting today, log a note in `companies.notes` instead of inserting a placeholder.

## Candidate Profile Constraints

These are non-negotiable for the current candidate (Naman Yeshwanth Kumar). Any role that violates them is bad data and must be rejected, regardless of fit_score:

- **Visa status:** F-1 international graduate. MS Computer Engineering, ASU, May 2026 grad. Eligible for OPT and STEM-OPT.
- **Location:** US-based or US-remote only. Reject postings whose primary location is India, China, EU, UK, or any other non-US country, even when the company is otherwise a strong target. Exception: explicit US-remote postings that don't restrict to citizens.
- **Hard visa/clearance blockers** — automatic reject regardless of fit_score:
  - "US Citizenship required" / "US-Person required"
  - "Active US security clearance required" / "Must be eligible for security clearance"
  - "No sponsorship available" / "Must not require visa sponsorship now or in the future"
  - "ITAR / EAR restricted" / "Export-controlled position"
  - Posting primary location in a country other than the US

These are hard blockers, not penalty points — surfacing them wastes the candidate's tailoring time. If a target company keeps posting US-Citizens-only or India-only roles, log it in `companies.notes` so the dashboard surfaces the pattern rather than retrying every research run.

## Required Read Order

### 1. Read Base Resumes

Read all four current base resumes:

```text
Master_Resume/current/resume_fullstack_ai.html
Master_Resume/current/resume_ai_engineer.html
Master_Resume/current/resume_ai_eda.html
Master_Resume/current/resume_autonomous.html
```

Use them to infer the candidate's searchable profile:

| Resume | Search Signal |
|---|---|
| `resume_fullstack_ai.html` | Product AI, SaaS, React/Django, APIs, shipped systems |
| `resume_ai_engineer.html` | LLM agents, RAG, MCP, evaluation, model orchestration |
| `resume_ai_eda.html` | AI + silicon, RTL/EDA, ASIC flows, physical design, timing |
| `resume_autonomous.html` | Robotics, autonomous systems, C++, perception/simulation |

### 2. Read Strategy Context

Read a focused starter set, not every file:

```text
resume_strategy/summary.md
resume_strategy/skills.md
resume_strategy/trezzit.md
resume_strategy/siliconcrew.md
resume_strategy_ai_eng/summary.md
resume_strategy_eda/summary.md
resume_strategy_eda/skills.md
resume_strategy_eda/sta_engine.md
resume_strategy_eda/gcn_asic.md
resume_strategy_eda/siliconcrew.md
resume_strategy_av/summary.md
```

Read additional strategy files only when needed for a specific role category.

### 3. Read Supabase State

Before searching, read:

```sql
-- Exclusion + current state
select company, role, url, status from public.jobs;
select company, role, url, decision, fit_score, last_seen_at from public.researched_jobs;
select name, careers_url, priority, notes from public.companies;

-- Positive signal: which tracks has the candidate actually been applying to?
select base_resume, count(*) as n
from public.jobs
where status in ('applied','tailored','interviewing','offer')
  and applied_at > now() - interval '60 days'
group by base_resume
order by n desc;

-- Soft calibration signal: which roles did the candidate recently skip,
-- and what was the reason? Use this to anticipate near-misses,
-- NOT as a hard exclusion rule.
select company, role, fit_score, fit_reason
from public.researched_jobs
where decision in ('skipped','closed')
  and updated_at > now() - interval '90 days'
order by updated_at desc
limit 50;
```

Use these tables to build exclusions, search targets, and signal weightings (described in §Scoring).

**Applied-history is a positive signal.** Tracks the candidate has been applying to recently are validated preferences. Tracks with frequency ≥ 3 in the last 60 days bump fit_score on new candidates in that track by **+3 to +5** (cap 100). Frequency 1–2 is a mild signal (**+2**). Frequency 0 → score normally.

Map `base_resume` values to tracks: `fullstack_ai` → product/SaaS/agents, `ai_engineer` → LLM agents/RAG/MCP, `ai_eda` → silicon/EDA/AI-for-chips, `autonomous` → AV/robotics/perception.

**Skipped-history is a soft calibration signal.** Read role titles + `fit_reason` of recently-skipped rows to surface repeating rejection patterns. Common ones to watch for:

- Senior IC titles ("Member of Technical Staff", "Staff", "Senior", "Lead", "Principal", "Architect")
- Hard YOE floors in JD body (3+, 5+, 8+ years) — extract from JD text, not title
- Specific tool gaps the candidate hasn't bridged (UVM, TensorRT, Rust+CuTe DSL, K8s/Slurm at HPC scale)
- Wrong archetype (FAE / customer success / strategist / consultant when candidate is a builder)

If a candidate role matches a recently-skipped pattern, **soft-deduct 5–10 points** and add a one-line caveat to `fit_reason` (e.g., `"Note: title pattern resembles skipped roles X, Y — verify YOE floor"`). This is NOT a hard skip — the candidate may want to re-evaluate. The goal is to flag the resemblance, not silently filter.

## Exclusion Rules

Exclude jobs that match any of:

```text
exact URL already exists
canonical URL already exists after removing tracking params
same ATS job ID already exists
normalized company + normalized role already exists
already applied in jobs
already rejected/withdrawn in jobs unless the user explicitly wants retries
researched_jobs decision = skipped
researched_jobs decision = duplicate
researched_jobs decision = closed
researched_jobs decision = stale
```

Normalize company/role strings before comparing:

```text
lowercase
remove punctuation
remove repeated whitespace
remove common suffixes such as inc, corp, corporation, systems, technologies, labs
```

## Search Targets

Use `companies` as the first source of target companies. Prefer `careers_url` when present.

Search order:

```text
1. Official company careers page
2. Official ATS boards: Ashby, Greenhouse, Lever, Workday
3. Company-hosted job APIs or pages
4. Third-party mirrors only as fallback
```

Do not rely on mirrors if an official page is available.

## URL Validation

A URL must point to a single specific posting. **Reject before fetch** if it matches any of these landing-page patterns:

```text
*/careers/?$
*/jobs/?$
*/open-roles/?$
*/early-careers/?$
*/graduates/?$
*/students/?$
*/university-recruiting*
*/work-with-us/students/?$
*/company/careers/?$
boards.greenhouse.io/embed/*
job-boards.greenhouse.io/<org>/?$       (org root, no /jobs/<id>)
jobs.lever.co/<org>/?$                  (org root, no posting uuid)
jobs.ashbyhq.com/<org>/?$               (org root, no posting uuid)
```

A **specific posting URL** has one of these shapes:

```text
job-boards.greenhouse.io/<org>/jobs/<numeric_id>
boards.greenhouse.io/<org>/jobs/<numeric_id>
jobs.lever.co/<org>/<uuid>
jobs.ashbyhq.com/<org>/<uuid>
<sub>.wd<n>.myworkdayjobs.com/.../job/.../<JR_id>
indeed.com/viewjob?jk=<id>
amazon.jobs/<lang>/jobs/<numeric_id>
careers.<company>.com/.../job/<id>
<company>.com/careers/<role-slug>-<numeric_id>
```

If a target company has no specific posting today, **log to `companies.notes`** ("checked YYYY-MM-DD: no NCG postings live") and move on. Never insert a placeholder.

## Verification Protocol

Every row must be verified open *immediately before insert*. The protocol depends on which ATS the posting is on.

### Greenhouse, Lever, Indeed, custom-hosted

`WebFetch` the URL.

- **Open:** 200 OK; the page contains the exact role title plus an Apply button or full JD block. Record the indicator you saw.
- **Closed:** 404, redirect to a careers landing, or "this position is no longer accepting applications" copy. Do not insert; if the URL is already in `researched_jobs`, set `decision='closed'` and append closing evidence to `research_notes`.
- **Inconclusive (e.g. 403 from Lever):** fall back to WebSearch (see below). If still inconclusive, do not insert.

### Ashby (JS-rendered — WebFetch returns a shell)

Do not trust `WebFetch` alone — Ashby returns the page shell with only a `<title>` tag, which gives no signal about openness. Use the public Ashby API:

```text
GET https://api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true
```

The posting must:
- be present in the response (matched by the UUID in the URL),
- have `isListed=true`,
- have `publishedAt` within the last 90 days.

If the org isn't on the public API, fall back to WebSearch:

```text
<company> "<exact role>" 2026 site:ashbyhq.com
```

The role must appear in current results dated within 60 days.

The Notion row currently in `researched_jobs` (`research_notes` starts with `"Verified open on 2026-05-02 via Ashby public postings API for Notion. API returned isListed=true..."`) is the gold standard for what the evidence string should look like.

### Workday (JS-rendered, no public API)

`WebFetch` returns a shell. Use WebSearch as primary:

```text
<company> "<exact role>" "<JR id>" 2026
```

The role must show up on a current LinkedIn, aggregator, or company-press citation dated within the last 60 days. **Verify the specific JR ID, not just the title** — companies like NVIDIA recycle "New College Grad 2026" titles across many JRs, and old listings frequently outlive their actual deadlines.

### Cross-cutting evidence requirement

Whatever path was used, `research_notes` must start with this exact format:

```text
Verified open via {source} on {YYYY-MM-DD}: {short evidence string}.
Posted {date or "unknown"} | Deadline {date or "none"} | Comp {if found, else "n/a"}.
{Any caveats: visa, residency, US-Person, on-site, etc.}
```

No evidence string → do not insert.

## Staleness Check

Before insert:

- If the listing exposes a deadline and the deadline is past today → **reject**.
- If the listing has a publish/posted date and it's >90 days old → set `decision='stale'` and **do not insert as `new`**.
- If you can't determine either → prefer the safer choice: **do not insert**.

## Target Role Categories

Prioritize full-time, new-grad, university-grad, entry-level, and early-career roles in:

```text
AI engineer
Applied AI engineer
LLM engineer
Agent engineer
RAG / retrieval / evaluation engineer
ML engineer
ML systems engineer
AI infrastructure engineer
AI + EDA / silicon tooling engineer
EDA software engineer
CAD / ML methodology engineer
Hardware/software AI tooling engineer
Autonomous simulation / robotics software engineer
```

Avoid by default:

```text
internships
co-ops
senior
staff
principal
manager
director
roles requiring 5+ years unless unusually aligned
```

## Candidate Normalization

Every candidate job should be normalized into:

```text
company
role
url               (must be a specific posting URL — see §URL Validation)
location
source            (non-null — see options below)
fit_score         (≥70 — see §Scoring)
fit_reason        (why this candidate is a good fit)
job_description   (raw JD text or summary; never invent)
research_notes    (must start with verification evidence string)
is_open           (true; you just verified it)
decision          ('new')
last_seen_at      (now())
```

`source` must be one of:

```text
official_careers
ashby
greenhouse
lever
workday
company_api
mirror
manual_research
```

If you can't pick one, you don't have enough information to insert.

## Scoring

Score from 0 to 100. Honest precision over optimism.

Positive signals:

```text
Python
C++
TypeScript / React
LLM apps
agents
RAG / retrieval
embedding search
MCP or tool orchestration
model evaluation
PyTorch / ML systems
EDA / RTL / ASIC / physical design
autonomous systems / robotics / simulation
new grad / early career / 0-2 years
full-time
US location or realistic relocation
track alignment with candidate's recent applied pattern (+3 to +5 fit_score)
```

Negative signals:

```text
internship-only
senior/staff/principal
managerial role
hard 3+ or 5+ years requirement (extract from JD body, not just title)
title contains "Member of Technical Staff" / "MoTS" / "Staff" / "Senior" / "Lead" / "Principal" / "Architect" (UNLESS also "Junior" / "Early Career" / "New Grad" / "Entry Level" / "University Grad")
minimum salary band > $200K (senior IC proxy)
unrelated enterprise IT with no AI/software depth
domain mismatch with no transferable angle
unverified or closed posting
posting older than 90 days

Hard blockers (see §Candidate Profile Constraints for full list):
US Citizenship / US-Person required
Active security clearance required
"No sponsorship available" / "Must not require visa sponsorship"
ITAR / EAR restricted
non-US primary location

Soft signal (deduct 5-10, don't auto-skip):
role pattern resembles a recently-skipped candidate role (see §Required Read Order step 3)
```

### Thresholds (insert policy)

```text
80-100  insert if verified open and not duplicate
70-79   insert ONLY if the role is explicitly labeled new-grad / university-grad / early-career,
        verified open, and not duplicate
<70     skip — do not insert under any circumstance
```

The previous "70-79 insert if target-company aligned" loophole is **removed**. If a target company has no posting at ≥70 fit today, that's signal — log it to `companies.notes`, don't insert a stretch row to make the inbox look fuller.

## Insert / Update Policy

For each candidate role, in order:

```text
1. URL Validation        — reject vague URLs (§URL Validation)
2. Exclusion Rules       — reject duplicates (§Exclusion Rules)
3. Verification Protocol — reject unverified (§Verification Protocol)
4. Staleness Check       — reject past-deadline / >90-day-old postings
5. Scoring               — reject <70
6. Insert or update:
   if URL exists in researched_jobs:
     update last_seen_at, is_open, fit_score, fit_reason, research_notes
   else:
     insert with decision='new'
```

Do not insert into `jobs`. Do not promote to pipeline. Do not mark anything `applied`.

## Required Insert Shape

```sql
insert into public.researched_jobs (
  company,
  role,
  url,
  location,
  source,            -- non-null; one of the values listed in §Candidate Normalization
  fit_score,         -- integer in [70, 100]
  fit_reason,
  job_description,
  research_notes,    -- MUST start with "Verified open via {source} on {YYYY-MM-DD}: ..."
  is_open,           -- true
  decision,          -- 'new'
  last_seen_at       -- now()
) values (...);
```

`user_id` defaults to `auth.uid()` for authenticated dashboard use. If using MCP/admin SQL, set `user_id` explicitly when needed.

If any of `source`, `research_notes` (with the evidence string), `last_seen_at`, or a fit_score ≥70 is missing, the insert is malformed — do not run it.

## Daily Re-verification

When re-running research, re-verify rows older than 7 days where `decision='new'`:

```sql
select id, company, role, url, source, last_seen_at
from public.researched_jobs
where user_id = <user>
  and decision = 'new'
  and last_seen_at < now() - interval '7 days';
```

For each, run the Verification Protocol again:

- **Still open:** update `last_seen_at = now()` and append a re-verification line to `research_notes` (e.g. `"Re-verified open 2026-05-10: Ashby API still isListed=true."`).
- **Closed:** set `decision='closed'`, append closing evidence.
- **Inconclusive:** leave `decision='new'` but flag in run summary so the user can decide.

## Run Summary

End every run with:

```text
New jobs inserted:                 N
Existing jobs updated:             N
Re-verified open:                  N
Re-verified closed (flipped):      N
Duplicates skipped:                N
Vague URL rejected:                N
Unverified rejected:               N
Stale/past-deadline rejected:      N
Sub-70 fit skipped:                N
Internships skipped:               N
Senior-only skipped:               N

Top inserted jobs:
1. Company - Role - score - source - URL
2. Company - Role - score - source - URL
3. Company - Role - score - source - URL
```

If only one job was requested, insert exactly one row and report that row.

## Safety Rules

- Prefer official sources.
- Do not invent job details.
- If openness cannot be verified, do not insert. Period.
- Do not pollute `researched_jobs` with weak matches, vague URLs, or unverified postings.
- Do not write to `jobs` unless the user explicitly asks to promote.
- Do not alter resume files.
- Do not alter dashboard code.

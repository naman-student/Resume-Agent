# Job Research Agent Guide

This guide defines the standard workflow for an agent that searches for fresh jobs and writes candidates into Supabase `public.researched_jobs`.

The research agent's job is to fill the research inbox. It should not create tailored resumes and should not mutate the main application pipeline unless the user explicitly asks.

## Core Principle

```text
Repo resumes + strategy notes = candidate profile
Supabase tables = memory and exclusions
Web search = fresh supply
researched_jobs = research inbox
jobs = committed pipeline
dashboard = human control
```

## Tables

| Table | Purpose |
|---|---|
| `researched_jobs` | Broad research inbox for jobs found by agents |
| `jobs` | Committed pipeline for roles being tailored/applied |
| `companies` | User's company list and personal notes |

Research agents write to `researched_jobs` only.

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
select company, role, url, status from public.jobs;
select company, role, url, decision, fit_score from public.researched_jobs;
select name, careers_url, priority, notes from public.companies;
```

Use these tables to build exclusions and search targets.

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
url
location
source
fit_score
fit_reason
job_description
research_notes
is_open
decision = new
```

Use `source` values such as:

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

## Scoring

Score from 0 to 100. Prefer honest precision over optimism.

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
```

Negative signals:

```text
internship-only
senior/staff/principal
managerial role
hard 3+ or 5+ years requirement
unrelated enterprise IT with no AI/software depth
domain mismatch with no transferable angle
unclear or closed posting
```

Recommended thresholds:

```text
80-100  insert automatically if not duplicate
70-79   insert if role is clearly early-career or target-company aligned
55-69   mention in summary only; insert only if user asked for broader search
0-54    skip
```

## Insert / Update Policy

For each selected role:

```text
if URL exists in researched_jobs:
  update last_seen_at, is_open, fit_score, fit_reason, research_notes
else if duplicate of jobs or researched_jobs:
  skip or mark duplicate if useful
else:
  insert into researched_jobs with decision = new
```

Do not insert into `jobs`.

Do not promote to pipeline.

Do not mark anything `applied`.

## Required Insert Shape

```sql
insert into public.researched_jobs (
  company,
  role,
  url,
  location,
  source,
  fit_score,
  fit_reason,
  job_description,
  research_notes,
  is_open,
  decision,
  last_seen_at
) values (
  ...,
  true,
  'new',
  now()
);
```

`user_id` defaults to `auth.uid()` for authenticated dashboard use. If using MCP/admin SQL, set `user_id` explicitly when needed.

## Run Summary

End every run with:

```text
New jobs inserted: N
Existing jobs updated: N
Duplicates skipped: N
Internships skipped: N
Senior-only skipped: N
Closed postings marked/ignored: N

Top inserted jobs:
1. Company - Role - score - URL
2. Company - Role - score - URL
3. Company - Role - score - URL
```

If only one job was requested, insert exactly one row and report that row.

## Safety Rules

- Prefer official sources.
- Do not invent job details.
- If current openness cannot be verified, choose another job.
- Do not pollute `researched_jobs` with weak matches.
- Do not write to `jobs` unless the user explicitly asks to promote.
- Do not alter resume files.
- Do not alter dashboard code.

# Resume Project

This repo is the working system for tailoring resumes, generating PDFs, and tracking job applications through the Supabase-backed dashboard. It runs as a Claude Code project — most operations are driven by a tailoring skill and a reviewer subagent defined under `.claude/`.

## Current Workflow

```text
Research agent populates Supabase researched_jobs
  -> Resume-tailor skill picks a JD + base resume
  -> JD-fetcher subagent returns the verbatim JD (or pauses if it can't)
  -> Skill copies a base from Master_Resume/current/ to Resume/Drafts/
  -> Skill edits the draft in place (summary, skills, projects, awards)
  -> resume-reviewer subagent scores 9 dimensions + returns confidence-tagged edits
     (MUST-FIX / STRONG REC / CONSIDER / OPTIONAL)
  -> Targeted fixes applied (MUST-FIX automatically; rest judged in-context)
  -> Scripts/html_to_pdf.py creates a PDF locally
  -> User applies
  -> Post-applied pipeline moves HTML + PDF to Resume/Applied/, inserts jobs row,
     flips researched_jobs.decision = 'promoted'
  -> Supabase dashboard tracks status
```

## Agent System (under `.claude/`)

```text
.claude/
  skills/
    resume-tailor/SKILL.md       Methodology: phases 0-6, density rules,
                                  callback patterns, anti-patterns, JD-fetch
                                  protocol, reviewer-subagent invocation
  agents/
    resume-reviewer.md            Dual-lens (ATS + human recruiter) reviewer
                                  with confidence-tagged edits + honesty audit
                                  calibration list of what's real vs. not
  settings.json                   Project-level Claude Code settings
```

Two non-negotiable rules baked into the agents:

- **JD verbatim is non-negotiable.** If the JD-fetcher can't get the real text from a mirror, it returns `JD_FETCH_FAILED` and the skill pauses for the user — never reconstructs from sibling roles.
- **Reviewer is opinion, not command.** Apply MUST-FIX automatically (factual errors, fabrications). Evaluate STRONG REC. Skip CONSIDER unless you agree. The confidence tags exist so the main agent doesn't blindly follow every suggestion.

## Active Structure

```text
Resume Project/
  README.md
  RESUME_AGENT_GUIDE.md         Top-level tailoring guide (deferred-to by SKILL.md)
  RESEARCH_AGENT_GUIDE.md       Research-agent protocol for populating researched_jobs
  index.html                    GitHub Pages entry
  job-dashboard-supabase.html   Live dashboard

  .claude/
    skills/resume-tailor/SKILL.md
    agents/resume-reviewer.md

  Master_Resume/current/
    resume_fullstack_ai.html
    resume_ai_engineer.html
    resume_ai_eda.html
    resume_autonomous.html

  Resume/
    Drafts/          Tailored HTML drafts being worked on
    Applied/         HTML + PDF actually used for applications (single source of truth)
    To_Apply/        PDFs ready to submit
    Archive/         Optional archive for completed HTML drafts
    Archive_Drafts/  Historical tailored HTMLs (incl. callback-getter quality bar)
    Archive_Applied/ Historical applied PDFs
    Archive_Legacy/  Older resume generations
    Skipped/         Drafts that didn't go out

  resume_strategy/          Full-stack AI source notes (Trezzit, SiliconCrew, HEAL.AI, etc.)
  resume_strategy_ai_eng/   AI engineer source notes
  resume_strategy_eda/      AI/EDA source notes (GCN ASIC, MIPS, STA, gem5, IISc, etc.)
  resume_strategy_av/       Autonomous systems source notes

  Scripts/
    html_to_pdf.py
    resume_check.py

  Legacy/
    csv_dashboard/   Old CSV dashboard and tracking scripts
    old_generation/  Old single-master generation scripts
    notes/           Historical planning/research notes
```

## Tailor A Resume

Agents should follow `RESUME_AGENT_GUIDE.md`.

Research agents that search for new roles should follow `RESEARCH_AGENT_GUIDE.md` and write only to Supabase `researched_jobs`.

Manual copy example:

```powershell
Copy-Item "Master_Resume/current/resume_ai_engineer.html" "Resume/Drafts/resume_company-role.html"
```

Then edit only the draft:

```text
Resume/Drafts/resume_company-role.html
```

Do not edit files in `Master_Resume/current/` directly.

## Generate A PDF

```powershell
python Scripts/html_to_pdf.py company-role
```

or:

```powershell
python Scripts/html_to_pdf.py resume_company-role.html
```

Output:

```text
Resume/To_Apply/resume_company-role.pdf
```

List available drafts:

```powershell
python Scripts/html_to_pdf.py --list
```

## Check A PDF

```powershell
python Scripts/resume_check.py Resume/To_Apply/resume_company-role.pdf
```

Without arguments, it checks all PDFs in `Resume/To_Apply/`.

## Dashboard

The live dashboard is:

```text
job-dashboard-supabase.html
```

GitHub Pages entry point:

```text
index.html
```

Expected URL:

```text
https://naman-student.github.io/Resume-Agent/
```

The dashboard uses Supabase Auth/RLS and the `jobs` and `companies` tables. The old CSV dashboard has been moved to `Legacy/csv_dashboard/`.

## Secrets

Use `.env.local` for local secrets. It is gitignored.

Do not commit:

```text
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_DB_PASSWORD
```

The browser dashboard may use the Supabase anon key because RLS is enabled.

## Legacy Files

Older CSV-era tools and single-master generation scripts are preserved under `Legacy/` for reference only. They should not be used for the current workflow unless intentionally restored or rewritten.

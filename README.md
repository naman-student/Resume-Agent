# Resume Project

This repo is the working system for tailoring resumes, generating PDFs, and tracking job applications through the Supabase-backed dashboard.

## Current Workflow

```text
Job description
  -> Agent reads RESUME_AGENT_GUIDE.md
  -> Agent copies one base resume from Master_Resume/current/
  -> Agent edits the copy in Resume/Drafts/
  -> Scripts/html_to_pdf.py creates a PDF in Resume/To_Apply/
  -> User applies
  -> Final PDF is stored in Resume/Applied/
  -> Supabase dashboard tracks status
```

## Active Structure

```text
Resume Project/
  README.md
  RESUME_AGENT_GUIDE.md
  RESEARCH_AGENT_GUIDE.md
  index.html
  job-dashboard-supabase.html

  Master_Resume/current/
    resume_fullstack_ai.html
    resume_ai_engineer.html
    resume_ai_eda.html
    resume_autonomous.html

  Resume/
    Drafts/          Tailored HTML drafts currently being worked on
    To_Apply/        PDFs ready to submit
    Applied/         PDFs actually used for applications
    Archive/         Optional archive for completed HTML drafts
    Archive_Drafts/  Historical tailored HTMLs
    Archive_Applied/ Historical applied PDFs
    Archive_Legacy/  Older resume generations

  resume_strategy/          Full-stack AI source notes
  resume_strategy_ai_eng/   AI engineer source notes
  resume_strategy_eda/      AI/EDA source notes
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

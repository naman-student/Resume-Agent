# Repository Instructions

This repository is a resume-tailoring and application-tracking system.

## Current Workflow

1. Read `RESUME_AGENT_GUIDE.md`.
2. Pick a base resume from `Master_Resume/current/`.
3. Copy the base into `Resume/Drafts/resume_<company-role>.html`.
4. Tailor only the copied draft.
5. Generate a PDF with:

```powershell
python Scripts/html_to_pdf.py <company-role>
```

The PDF is written to `Resume/To_Apply/`.

## Supabase Dashboard Handoff

If Supabase MCP/tools are available after creating or updating a draft:

- Treat `researched_jobs` as the research inbox and `jobs` as the committed application pipeline.
- Ask the user before creating or updating a dashboard row.
- Search `public.jobs` by URL first, then company + role.
- If no pipeline row exists, search `public.researched_jobs`.
- Promote a researched row into `public.jobs` only after user confirmation.
- If a row exists, update `draft_resume_path`, `base_resume`, and status only after confirmation.
- If no row exists, create one only after confirmation.
- Use `tailoring` for in-progress drafts and `tailored` for ready drafts.
- Never mark a job `applied` unless the user confirms they actually applied.

## Important Rules

- Do not edit `Master_Resume/current/` directly.
- Do not use legacy CSV scripts.
- Do not use `Legacy/` files for the current workflow unless the user explicitly asks.
- Do not assume GitHub Actions generates PDFs; PDF conversion is manual through `Scripts/html_to_pdf.py`.
- Preserve the existing resume HTML/CSS structure unless a layout fix is required.
- Keep claims honest and grounded in the existing resume strategy notes.

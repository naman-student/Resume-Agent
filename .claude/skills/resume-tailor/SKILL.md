---
name: resume-tailor
description: Tailor Naman's resume for a specific job using the Resume-Agent repo's four base resumes and strategy notes. Use this skill whenever the user asks to draft, tailor, customize, write, or adapt a resume for a specific company/role/job posting, or refers to "the Resume-Agent repo," "my bases," "the four bases," "fullstack_ai / ai_engineer / ai_eda / autonomous," or pastes a job description and wants a resume out of it. Trigger this even when the user just says things like "do <Company> next," "Sierra resume," or "make me one for <Role>" — those are continuations of this workflow. The skill produces a final HTML resume as its only output and does not push to GitHub or generate PDFs.
user_invocable: true
---

# Resume Tailor

Operating procedure for tailoring Naman Yeshwanth Kumar's resume. The output of this skill is **always one finished HTML file** for the user to save into `Resume/Drafts/` themselves. This skill does not push to GitHub and does not generate PDFs.

## Pipeline execution learnings (read this first)

Hard-won lessons from dozens of tailored drafts. Follow these in order:

1. **Copy base → edit in place. Never write from scratch.** CSS drift causes overflow and wastes tokens.
2. **Tighten CSS BEFORE writing content.** Apply the callback-getter pattern (0.38in padding, 11pt sections, 4pt entries, 10pt bullet line-height, 1pt bullet margins) immediately after copying. You'll overflow otherwise and have to redo work.
3. **Draft → Review → Targeted fix, not Draft → Rewrite.** Spawn a reviewer subagent with the JD, the draft, strategy files, AND the two callback-getting resumes as the quality bar. Then only fix what the reviewer flags that you agree with — don't blindly follow every suggestion.
4. **The reviewer will always say "the summary is too generic."** They're usually right. The callback-getting resumes committed to ONE laser-specific identity in the first clause. If your summary has 3+ identity claims, it's unfocused.
5. **Don't list skills you can't back with a bullet.** PyTorch in skills with zero PyTorch in bullets is worse than no PyTorch — it invites a question you can't answer. Either transplant a project that proves it or drop it.
6. **Verify postings are open before tailoring.** Half the researched_jobs inbox was dead. Web-search first, always.
7. **Reframe projects, don't rewrite them.** SiliconCrew has been 6+ different things across drafts. The bullet body stays ~80% the same — what changes is the title, lead phrase, and which details get pulled to the front. The strategy files have swap guides for this.
8. **Match content density to the callback-getters:** 4-5 projects / 7-8 bullets, 1-2 work entries, 3 awards, 3 skills rows. If your draft is lighter, it'll feel thin. If heavier, it'll overflow.
9. **Bold only killer numbers.** 37/92, 600+ users, 995 tests, 60%→95%. Never bold tool names or section headers.
10. **The "honest gap" in the plan matters.** If you score a role 55 and the gap is a core requirement (not a nice-to-have), tell the user to skip it. Don't waste tailoring time on bad fits.

## What this skill does NOT do

- Push to GitHub. The Claude.ai web GitHub connector is read-only at the time of writing — write attempts return 403. Even if writes become available later, this skill stays in "produce HTML, hand to user" mode unless the user explicitly asks for a push.
- Generate PDFs. Conversion is the user's manual side-effect step (`Scripts/html_to_pdf.py` locally, or whatever they wire up later).
- Mutate Supabase silently. Any `researched_jobs` or `jobs` row change requires explicit user confirmation in the same turn.

## Inputs the skill expects

One of:
1. A job description (URL or pasted text) plus a company/role
2. A `researched_jobs.id` or row reference, in which case fetch the row from Supabase
3. A vague request like "do Sierra next" — resolve by searching `researched_jobs` for the most recent matching row, then confirm with the user before proceeding

## Pipeline

Run these phases in order. Do not skip ahead. Output Phase 3 to chat for the user before doing Phase 4.

### Phase 0 — Bootstrap

Read these from the repo before doing anything else (the guides drift; don't rely on memory):

- `RESUME_AGENT_GUIDE.md` — the canonical tailoring guide; this skill defers to it on anything it doesn't override
- The four base resumes from `Master_Resume/current/`:
  - `resume_fullstack_ai.html`
  - `resume_ai_engineer.html`
  - `resume_ai_eda.html`
  - `resume_autonomous.html`

If a previous tailored resume exists for a similar role, also read it as a reference. Past drafts live in `Resume/Archive_Drafts/<date>/` and `Resume/Archive/`. Two especially useful ones to learn editing patterns from:

- `resume_chipagents-fullstack-ai-engineer.html` — fullstack-AI flavor with a chip/EDA spin
- `resume_openai-hardware-tooling.html` — hardware tooling / compiler-pipeline framing

These are not templates to copy — they're examples of how aggressively to cut content and how to retitle the same project (especially SiliconCrew) for different audiences.

### Phase 1 — Job ingestion

If the user gave a URL, fetch and read the JD. If only a company/role was given, web-search and confirm with the user that the JD found is the one they meant. If a `researched_jobs` row was referenced and `job_description` is empty or under ~300 characters, web-search to enrich it (do not silently update Supabase — ask first).

**Ashby URLs** (`jobs.ashbyhq.com`) are JS-rendered SPAs — `WebFetch` will get an empty shell. Instead, web-search `<company> "<role title>" job description` and fetch from a mirror site (jobright.ai, tealhq.com, peerlist.io usually have the full text). Greenhouse and Lever URLs generally work with `WebFetch` directly.

**IMPORTANT: Always verify the posting is still open before tailoring.** The `researched_jobs` table may contain stale entries. Web-search `<company> "<exact role title>" 2026` and check whether the listing is still active. If the posting appears closed or the publish date is old (6+ months), flag it to the user before proceeding. Do not waste time tailoring for a dead listing.

### Phase 2 — Pick the base

Use the heuristic from `RESUME_AGENT_GUIDE.md`:

- Shipping products / APIs / full-stack / React-Django → `fullstack_ai`
- LLM agents / RAG / MCP / eval frameworks / Claude / OpenAI → `ai_engineer`
- Hardware design / ASIC / physical design / ML for chips → `ai_eda`
- AV / robotics / perception / C++ real-time → `autonomous`

If the role straddles two tracks, pick the closer base and **transplant** projects from the other (see "Cross-track transplants" below).

### Phase 3 — Plan, then output to chat for review

Before writing any HTML, output to chat:

- **Recommended base** with one-sentence reasoning
- **Required quals** extracted from the JD (the ATS must-haves)
- **Preferred quals** (the differentiators)
- **The unique angle** — the single most specific signal Naman has for THIS company. Examples:
  - Anthropic → "Claude Desktop-compatible MCP server"
  - Sierra → "production agent with CVDP eval scores + 12-month Trezzit runtime"
  - Apple Physical Design → "GNN ASIC end-to-end on ASAP7 7nm"
  - Loop AI → "Trezzit's 60→95% receipt-PDF extraction iteration"
- **Honest match score 0–100** with the gap stated explicitly. Do not inflate. If a key qual is missing, say so.
- **Planned changes** as a bullet list: summary rewrite, skills row renames/reorders, project replacements, transplants, drops, awards reorder
- **Filename**: `resume_<company-slug>-<role-slug>.html` (kebab-case, lowercase)

Then ask: "Looks right or want me to adjust before I generate the file?" and wait. If the user says "go" or similar, proceed to Phase 4.

If the user explicitly says "skip the planning step" or "directly edit," still output a one-line summary of the chosen base and the unique angle, then proceed.

### Phase 4 — Generate the HTML

**IMPORTANT: Copy the base file to `Resume/Drafts/` first, then edit it in place.** Do NOT write the entire HTML from scratch — it wastes tokens and risks drift from the base's CSS/structure. Use the Edit tool to make targeted changes to the copy.

```
Copy base → Resume/Drafts/resume_<company-slug>-<role-slug>.html
Then edit: summary, skills, project entries, work title, awards order
```

Do not push, do not commit.

After the file, post a short summary:

- What stayed unchanged (CSS, header, education entries, etc.)
- What changed (sections + reasoning)
- What was dropped and why
- Suggested filename for `Resume/Drafts/`
- Reminder that the user should open the HTML locally and check for two-page overflow

### Phase 5 — Supabase row (with confirmation)

Per `RESUME_AGENT_GUIDE.md`:

- If a matching `public.jobs` row exists → ask whether to update it (`status='tailored'`, set `base_resume`, set `draft_resume_path='Resume/Drafts/<filename>'`)
- If only a `researched_jobs` row exists → ask whether to promote it; preserve `researched_job_id` on the new `jobs` row; set `researched_jobs.decision='promoted'`
- Never set `applied` — only the user does that after submitting

**When the user confirms they applied**, do both of these in sequence:
1. **Promote to `jobs`**: Insert a row with `status='applied'`, `applied_at=now()`, `base_resume`, `draft_resume_path`, `fit_score`, `url`, `location`, `reason` (brief match summary + gaps), `user_id`, and `researched_job_id` linking back to the research row.
2. **Update `researched_jobs`**: Set `decision='promoted'`, `updated_at=now()`.

The Supabase project ID is `rztpwtpqmjkqnbojbujj` and Naman's `user_id` is `7ceded32-2d69-463c-a492-a3497252347b`.

### Phase 6 — File management after application

When the user confirms they applied and the PDF exists:
1. **Move** (not copy) the HTML from `Resume/Drafts/` to `Resume/Applied/`
2. **Move** the PDF from `Downloads/` (or wherever it was generated) to `Resume/Applied/`
3. **Delete** any remaining copies in Drafts or Downloads — Applied is the single source of truth
4. Unapplied drafts that won't be used should be deleted from Drafts to keep it clean

## Editing rules (the patterns that aren't fully captured in `RESUME_AGENT_GUIDE.md`)

These are the patterns observed across Naman's strongest tailored resumes (`chipagents-fullstack-ai-engineer.html`, `openai-hardware-tooling.html`, `anthropic-applied-ai-engineer.html`).

### Density

- **3 skills rows beats 4.** Tighter visual signal. The `ai_engineer` base ships with 4; collapse to 3 unless the role genuinely needs four distinct categories.
- **Bullets per project should match priority signal.** 3 bullets for the headline project. 1–2 for supporting projects. The lead bullet of the lead project should land the unique angle in the first 15 words.
- **Drop ruthlessly.** If a project doesn't serve this specific role, cut it. Past drafts have dropped HEAL.AI, Intel OSS, CUDA MLP, IISc, e-Yantra, and others when they didn't serve the audience. Folding a hackathon win into Awards is fine; keeping a full project entry that doesn't help is not.

### Same project, different framing

Especially SiliconCrew — it has been retitled as:

- "Autonomous LLM Agent for RTL Design" (default `ai_engineer`)
- "Autonomous LLM Agent for RTL-to-GDSII Design" (default `ai_eda`)
- "Agentic AI Platform for EDA Workflow Automation" (chipagents)
- "Hardware Compiler Pipeline & EDA Tooling Infrastructure" (openai-hardware-tooling)
- "Production LangGraph Agent with Eval Framework & MCP Server" (Sierra)

The title and lead bullet should mirror the JD's vocabulary. The body of the bullets stays largely the same — what changes is the framing and what gets pulled to the front.

### Skills row labels mirror JD vocabulary

Don't keep the base's labels if the JD uses different language. Examples that have worked:

- JD says "evaluation frameworks" → row label "Agents, Eval & RAG" or "Evaluation & Production AI"
- JD says "physical design" → row label "Physical Design / EDA"
- JD says "PyTorch, TensorFlow, OpenCV" → row label "ML / Algorithms"

### Bold sparingly, on the killer numbers only

`<strong>` belongs only on numbers that earn their place: `37/92`, `5/5`, `600+ users`, `12+ months`, `18,000+ orders`, `~60% → 95%+`, `995 tests`, `PR #655 merged`. Do **not** bold company names, tool names, dates, or section headers. The base resumes are correct on this — preserve the pattern.

### Awards reorder per role

Reorder Awards to put the most role-relevant one first. Drop awards that don't serve the role:

- AI/agent roles → Devlabs (HEAL.AI / 1st place / RAG) first
- Hardware/robotics → e-Yantra (Top 10 nationally) first
- Generic SWE → DevHacks (Best Use of AI) first; e-Yantra often dropped

### Work experience: minor tweaks only

NCR GOLD is the only work entry; rewrite the title or one phrase to mirror the JD. For "founding engineer" / "shipped end-to-end" preferred quals, add "(Sole Engineer)" to the title or "Shipped end-to-end as the sole engineer" as a lead phrase. Don't add bullets; don't restructure.

### Education: untouched on first pass

Only swap the coursework line if the JD's domain demands it (e.g., for an EDA role, swap the AI-heavy coursework for VLSI/SoC/Computer Architecture). Otherwise leave it.

## Cross-track transplants

When the best proof point lives in a different track's resume, copy that project entry's HTML into the draft and reframe its title and bullets. Common transplants:

| Project | Lives in | Useful for |
|---|---|---|
| GCN ASIC Accelerator | `ai_eda` | ML algorithm implementation, semiconductor background, GNN |
| CUDA MLP | `ai_engineer` | GPU/ML, hardware/software co-design |
| Intel OSS Contribution | `fullstack_ai` | External-stakeholder collaboration, Intel-specific roles |
| Autonomous Pipeline | `autonomous` | C++ systems, sensor fusion, real-time |
| LRU/IPV gem5 | `ai_eda` | C++ simulation, CPU architecture |

## Two-page overflow

This skill cannot render HTML, so the page-count check is on the user. After producing the HTML, remind them to open it in a browser. If they report it overflows, apply the CSS-tightening sequence from `RESUME_AGENT_GUIDE.md` Step 4 in this order before cutting any content:

```
.resume-container padding: 0.46in → 0.32in
.section margin-bottom: 14pt → 11pt
.entry margin-bottom: 7pt → 4pt
.bullet-item line-height: 10.5pt → 10pt
.bullet-item margin-bottom: 2pt → 1pt
.skills-section p margin-bottom: 3pt → 2pt
.header margin-bottom: 17pt → 12pt
```

Tighten CSS first, every time. Cut content only after tightening doesn't fix it.

## Honest scoring

When giving a match score, be honest. If a JD requires Go and Naman doesn't have Go, the score isn't 95. State the gap. Naman has said he prefers an honest score with the gap stated over a flattering one — it lets him decide which roles are worth the tailoring effort.

Recommended score bands:

- **90–100** — direct fit on every required qual, strong fit on most preferred quals; the unique angle is genuinely strong
- **80–89** — direct fit on required quals; a couple preferred quals are gaps; the angle is good but not exceptional
- **70–79** — most required quals hit, one or two missing; tailoring will work but it's a real stretch in places
- **<70** — meaningful gap; recommend the user consider whether the time tailoring is worth it

## Anti-patterns to avoid

- Editing `Master_Resume/current/` directly. Always work from a copy.
- Writing the entire HTML from scratch instead of copying the base and editing. Copy first, edit in place — preserves CSS fidelity, saves tokens, prevents structural drift.
- Cutting content before trying CSS tightening.
- Stacking 4+ metrics in the summary. Pick 2–3, let them land.
- Listing API names as skills. "Gemini API | OpenAI API | Claude API" proves nothing. Show system behaviors: "Multi-provider LLM Routing | Quality-based Fallback | RAG Pipelines."
- Generic identity claims like "full-stack AI engineer who…" — replace with a specific identity tied to the role.
- Inventing experience or skills Naman doesn't have. Honest gaps beat fictional fits.

## Common Naman-specific facts (don't get these wrong)

- MS Computer Engineering, ASU, GPA 3.81, expected May 2026
- Bachelor's in Electrical and Electronics, BMS College of Engineering, August 2022
- Trezzit: 600+ users, 12+ months live, ~60→95% accuracy, 995 tests, 60+ endpoints, 40 models, 341 components
- SiliconCrew: 21-tool LangGraph agent, 37/92 on CVDP, 5/5 on ASU Spec2Tapeout
- NCR GOLD: 18,000+ orders over 3 years, ~20 min saved per order
- Intel OSS: PR #655 merged
- GCN ASIC: 50,300 µm² area, 50.6% density, 52.29 mW power, 99.2 ns latency
- AV pipeline: ICP from scratch, 0.299m pose error over 172m (4× baseline)
- HEAL.AI: 1st place Devlabs, 768-dim embeddings, custom RAG without external vector DB
- GitHub portfolio: `github.com/naman-ranka` (separate from the Resume-Agent repo account `naman-student`)
- Email: nyeshwan@asu.edu | Phone: (623) 249-1265 | LinkedIn: linkedin.com/in/namany
- **Implicit skills** (Naman knows these; add when JD calls for them even if not on a base): PyTorch, TensorFlow, Linux, Git — infer from his CUDA MLP work, AI/RL coursework, and production deployment experience

## Interview-signal patterns (resumes that got callbacks)

As of May 2026, these resumes got interview callbacks — study what they did:

- **`resume_chipagents-fullstack-ai-engineer.html`** — laser-specific identity ("intersection of agentic AI and chip design"), 3 skills rows, tightened CSS, aggressive project selection
- **`resume_openai-hardware-tooling.html`** — extremely role-specific identity ("hardware tooling and compiler infrastructure"), dropped Trezzit entirely, skills labels exactly mirrored the JD vocabulary, included IISc research

Common patterns from callbacks:
1. **Identity specificity > breadth** — the summary names the exact niche, not "full-stack AI engineer"
2. **3 skills rows** — always collapsed from 4, tighter visual signal
3. **Ruthless pruning** — projects that don't serve THIS role are cut without hesitation
4. **Skills labels mirror JD exactly** — not generic categories
5. **CSS was already tightened** in both

Use these as the quality bar. If a draft doesn't feel as tight and targeted as these two, it probably isn't.

## Reviewer subagent pattern

After generating a draft, spawn a `general-purpose` subagent to review it. Include in the prompt:
1. The JD (full text)
2. The draft resume path
3. The strategy files for relevant projects (e.g., `resume_strategy/trezzit.md`, `resume_strategy_eda/siliconcrew.md`)
4. Both callback-getting resumes as the quality bar (`Resume/Archive_Drafts/2026-05-01_pre_db_cleanup/resume_chipagents-fullstack-ai-engineer.html` and `resume_openai-hardware-tooling.html`)
5. The base resume it was derived from

Ask the reviewer to score on 7-8 dimensions relevant to the JD, give top 3 strengths/weaknesses, and suggest specific text edits. Then apply only the edits you agree with — don't blindly follow everything. Common patterns: reviewers always say the summary is too generic (usually right), always want more keywords added (sometimes right), and sometimes suggest fabricating experience (always wrong).

## When in doubt

Defer to `RESUME_AGENT_GUIDE.md`. This skill exists to operationalize that guide and add the editing patterns observed across Naman's actual tailored drafts; it doesn't replace it.

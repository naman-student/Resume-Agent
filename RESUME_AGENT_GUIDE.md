# Resume Tailoring Agent — Operating Guide

This document defines how an AI agent should operate when tailoring resumes in this repository. Read this first at the start of any resume session.

---

## Repository Structure

```
Resume Project/
├── Master_Resume/current/          ← The four canonical base resumes (HTML + PDF)
│   ├── resume_fullstack_ai.html
│   ├── resume_ai_engineer.html
│   ├── resume_ai_eda.html
│   └── resume_autonomous.html
├── Resume/Drafts/                  ← Working directory — place tailored HTMLs here
├── Resume/To_Apply/                ← PDFs generated from Drafts for application
├── Resume/Applied/                 ← PDFs actually used for applications
├── Resume/Archive/                 ← Optional completed HTML archive
├── resume_strategy/                ← MD files with raw content for fullstack_ai track
├── resume_strategy_ai_eng/         ← MD files with raw content for ai_engineer track
├── resume_strategy_eda/            ← MD files with raw content for ai_eda track
├── resume_strategy_av/             ← MD files with raw content for autonomous track
├── Scripts/html_to_pdf.py          ← Convert tailored HTML drafts to PDFs
├── job-dashboard-supabase.html     ← Supabase-backed job/application dashboard
└── Legacy/                         ← Old CSV dashboard and single-master scripts
```

---

## The Four Base Resumes

| Base File | Track | Target Roles |
|---|---|---|
| `resume_fullstack_ai.html` | Full-Stack AI Engineer | Product engineering, full-stack, shipped SaaS, React/Django/APIs, ML integration |
| `resume_ai_engineer.html` | AI / LLM Engineer | LLM agents, RAG, MCP, agentic systems, evaluation frameworks, Claude API |
| `resume_ai_eda.html` | Agentic AI for EDA | Physical design, ASIC, RTL-to-GDSII, GNN accelerators, EDA tools, Synopsys/Cadence |
| `resume_autonomous.html` | Autonomous Systems | Sensor fusion, SLAM, behavior planning, C++ robotics, AV pipelines |

### Base Selection Heuristic

- Shipping products, APIs, full-stack, React/Django → `fullstack_ai`
- LLM agents, RAG, MCP, eval frameworks, Claude/OpenAI → `ai_engineer`
- Hardware design, ASIC, physical design, ML for chips → `ai_eda`
- AV, robotics, perception, C++ real-time systems → `autonomous`
- Role straddles two tracks → pick the closer base, **transplant** projects from the other

---

## Step-by-Step Tailoring Pipeline

### Step 1 — Analyze the JD

Before touching any file:

1. Extract **required qualifications** (ATS must-haves — keywords, degree, years)
2. Extract **preferred qualifications** (differentiation opportunities)
3. Identify the **unique angle** — what makes this specific candidate unusually strong for this specific role (e.g., "has a Claude Desktop-compatible MCP server" for Anthropic, "has an Intel PR merged" for Intel)
4. Run a **match score** (honest 0–100%) and state the **gaps** clearly
5. List every planned change with a reason before touching the file

### Step 2 — Create the Draft

Always copy from `Master_Resume/current/`, never edit the base directly:

```powershell
Copy-Item "Master_Resume/current/<base>.html" "Resume/Drafts/resume_<company-role>.html"
```

Naming convention: `resume_<company>-<role-slug>.html`
Examples: `resume_anthropic-applied-ai-engineer.html`, `resume_intel-ai-algorithm-engineer.html`

### Step 3 — Edit in This Order

1. **Summary** — reframe identity for this reader; lead with the most specific signal for this company
2. **Skills** — restructure row order and rename labels to match JD vocabulary; add missing keywords
3. **Projects** — reorder, retitle, reframe bullets; transplant from other tracks if needed
4. **Work Experience** — minimal edits; adjust emphasis only
5. **Education** — swap coursework line to match domain

### Step 4 — Check for Overflow

Open the file in a browser. If it overflows to two pages, fix in this order:

**First: CSS tightening** (usually enough on its own)
```css
padding: 0.46in → 0.32in          /* biggest gain — top/bottom page padding */
section margin-bottom: 14pt → 11pt
entry margin-bottom: 7pt → 4pt
bullet line-height: 10.5pt → 10pt
bullet margin-bottom: 2pt → 1pt
skills p margin-bottom: 3pt → 2pt
header margin-bottom: 17pt → 12pt
```

**Second: Content cuts** (only if CSS isn't enough)
- Remove lowest-signal bullet in the densest project
- Merge awards if 3+
- Drop a skills row if those APIs/tools are already proven in bullets

**Never** cut content before confirming the CSS tightening alone doesn't fix it.

---

## Context Sources — Where to Get More Detail

When a bullet needs more specificity or a claim seems thin, read the relevant MD files:

### `resume_strategy/` (fullstack_ai track)
| File | Contains |
|---|---|
| `summary.md` | Summary framing options and positioning |
| `skills.md` | Full skills inventory with context |
| `trezzit.md` | Trezzit architecture, decisions, metrics |
| `heal_ai.md` | HEAL.AI RAG pipeline details |
| `order_management_system.md` | NCR GOLD project details |
| `siliconcrew.md` | SiliconCrew design decisions |
| `education_awards.md` | Coursework, awards, hackathon details |

### `resume_strategy_eda/` (ai_eda track)
| File | Contains |
|---|---|
| `summary.md` | EDA track positioning |
| `skills.md` | EDA/hardware skills inventory |
| `gcn_asic.md` | GCN ASIC full implementation details |
| `sta_engine.md` | Static timing analysis engine details |
| `lru_ipv_gem5.md` | gem5 C++ simulation project details |
| `mips_processor.md` | MIPS processor project details |
| `siliconcrew.md` | SiliconCrew EDA framing |
| `iisc_work_experience.md` | IISc research work details |
| `job_market_research.md` | EDA/chip job market analysis |

### `resume_strategy_ai_eng/` (ai_engineer track)
| File | Contains |
|---|---|
| `summary.md` | AI engineer track positioning |

### `resume_strategy_av/` (autonomous track)
| File | Contains |
|---|---|
| `summary.md` | Autonomous systems track positioning |

---

## Framing Rules

### Summary
- **Structure**: one identity claim → two proof points → optional stack
- **Lead with the most specific signal for THIS company**, not the most impressive thing generally
  - For Anthropic → "Claude Desktop-compatible MCP server"
  - For Intel → "Intel PR #655 merged upstream"
  - For Apple Physical Design → "GNN ASIC accelerator end-to-end on ASAP7 7nm"
  - For Scale AI → "ships and iterates on ML-integrated products"
- **Max 2–3 metrics in the summary** — more than that and nothing lands
- **Avoid**: "full-stack AI engineer who..." (generic) — prefer specific identity tied to the role

### Skills Section
- **Row order = priority signal** — what the JD cares about most goes first
- **Rename row labels** to match JD vocabulary exactly:
  - Anthropic JD says "evaluation frameworks" → row is named "Evaluation & Observability"
  - Apple JD says "physical design" → row is named "Physical Design / EDA"
  - Intel JD says "PyTorch, TensorFlow, OpenCV" → row is named "ML / Algorithms"
- **System behaviors > API names**:
  - Weak: `Gemini API | OpenAI API | Claude API`
  - Strong: `Multi-provider LLM Orchestration | Quality-based Fallback | RAG Pipelines`
- **Remove skills proven in bullets** — don't double-list MQTT if the Intel bullet already says MQTT

### Project Bullets
- **Same project, different framing** — SiliconCrew has been framed as:
  - Anthropic → "Claude Desktop MCP server + automated evaluation framework"
  - Apple → "ML-driven PPA optimization + autonomous self-correction loop"
  - Scale → "quality estimation pipeline with self-correction and provider routing"
  - Microsoft CoreAI → "agentic AI system with multi-provider API orchestration"
  - Microsoft Hardware → "automated sensor validation microservice"
- **Lead with what the reader cares about**, not what you're proudest of
- **Show iteration, not just construction**: "iterated from 60% → 95%" not "built pipeline"
- **Name failure modes** for roles that value reliability: "hallucinated item counts, currency ambiguity, multi-page layouts"
- **Quantify at the right level**: users/accuracy/tests for product roles; cell count/timing/PPA for hardware roles

### Cross-Track Project Transplanting
When the best proof point for a JD lives in a different track's resume:

| Project | Lives in | Useful for |
|---|---|---|
| GCN ASIC Accelerator | `ai_eda` | ML algorithm implementation, semiconductor background, GNN knowledge |
| CUDA MLP | `ai_engineer` | GPU/ML implementation, PyTorch-adjacent, hardware/software co-design |
| Intel OSS Contribution | `fullstack_ai` | External engineering collaboration, data pipelines, Intel-specific roles |
| Autonomous Systems Pipeline | `autonomous` | C++ systems, sensor fusion, real-time processing |
| LRU/IPV gem5 | `ai_eda` | C++ simulation, CPU architecture, hardware modeling |

Transplanting process: copy the relevant entry HTML from the source base, paste into the draft, reframe the title and bullets for the new audience.

---

## PDF and Dashboard Workflow

PDF generation is manual and side-effect free:

```
Resume/Drafts/resume_<company-role>.html
        |
        v
python Scripts/html_to_pdf.py <company-role>
        |
        v
Resume/To_Apply/resume_<company-role>.pdf
```

The converter does not update CSV files, move HTML files, or change dashboard status. Application tracking lives in Supabase and is managed through `job-dashboard-supabase.html`.

After applying, the final PDF should be moved to `Resume/Applied/` and the corresponding Supabase job row should be marked `applied`.

---

## Common Mistakes to Avoid

1. **Editing `Master_Resume/current/` directly** — always copy to `Resume/Drafts/` first
2. **Cutting content before trying CSS tightening** — layout changes are almost always enough
3. **Stacking 4+ metrics in the summary** — pick 2, let them land
4. **Using `&&` in PowerShell** — use `;` as the command separator instead
5. **Multi-line git commit messages with heredoc** — use single-line messages in PowerShell
6. **Listing APIs as skills** — proves nothing; show system behaviors instead
7. **Not reading MD files** when a bullet needs more specificity — the raw content is all there

---

## Quick Reference — Jobs Tailored This Session

| Draft File | Base Used | Key Transplants | Unique Angle |
|---|---|---|---|
| `resume_microsoft-hardware-systems-engineer.html` | `fullstack_ai` | — | Sensor validation microservice, PowerShell, systemd |
| `resume_microsoft-coreai-agentic-systems.html` | `ai_engineer` | — | MCP server, agentic AI infrastructure, production inference SLAs |
| `resume_microsoft-azure-hpc-ai.html` | `ai_eda` | CUDA MLP | CUDA + gem5 + ASIC = hardware/software co-design stack |
| `resume_apple-physical-design-ml.html` | `ai_eda` | — | GNN ASIC accelerator + ML-driven PPA optimization |
| `resume_intel-ai-algorithm-engineer.html` | `fullstack_ai` | GCN ASIC (ai_eda), CUDA MLP (ai_engineer) | Intel PR already merged + GNN implementation + semiconductor background |
| `resume_scale-ai-swe-new-grad.html` | `fullstack_ai` | — | Ships real products, iteration story (60%→95%), large-scale data pipeline |
| `resume_anthropic-applied-ai-engineer.html` | `ai_engineer` | Intel OSS (fullstack_ai) | Claude Desktop MCP server + automated evaluation framework + transcript analysis |

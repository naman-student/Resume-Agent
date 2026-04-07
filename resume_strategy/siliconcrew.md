# SiliconCrew — Resume Strategy

---

## ✅ SELECTED BULLETS

### Version A — With Benchmarks (preferred, use when space allows)

> Built SiliconCrew, an autonomous LangGraph agent (21 tools) that generates synthesizable Verilog from natural language, self-corrects via waveform analysis on simulation failure, and synthesizes to GDSII through OpenROAD; achieved **37/92 first-pass on CVDP** (Comprehensive Verilog Design Problems) and **5/5 on ASU Spec2Tapeout**; FastAPI + WebSocket + Next.js + MCP server.

### Version B — Without Benchmarks (space-constrained fallback)

> Built SiliconCrew, an autonomous LangGraph agent (21 tools) that generates synthesizable Verilog from natural language, self-corrects via waveform analysis on simulation failure, and synthesizes to GDSII through OpenROAD; FastAPI + WebSocket backend, Next.js frontend, MCP server supporting Claude Desktop and VS Code.

---

## 📌 POSITIONING NOTES

- Always prefer Version A — benchmark scores are externally verifiable, unlike self-reported metrics. This is the most credible line on the entire resume.
- CVDP = Comprehensive Verilog Design Problems — always spell out at least once so non-hardware recruiters understand the context
- The "self-corrects via waveform analysis" line is the key differentiator — it's not just code generation, it's a closed autonomous loop. Always keep this.
- For AI/LLM engineer roles this shows LangGraph agent design, multi-provider LLM routing, and MCP server implementation
- For hardware/AI-hardware roles this shows full ASIC flow (RTL → synthesis → GDSII), EDA tool integration, and research-level benchmark results
- For full-stack roles this shows FastAPI + WebSocket + Next.js system design with real-time streaming
- This is the only project on the resume with academic/research framing — position accordingly for research-adjacent roles
- Public GitHub repo: github.com/naman-ranka/siliconcrew

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### What It Does
- Takes natural language hardware specifications → produces synthesizable RTL, self-checking testbenches, and physical design (GDSII)
- Closes the full design loop: spec → code → lint → simulate → waveform debug → synthesize → report
- Self-corrects: reads VCD waveforms on simulation failure, diagnoses signal-level errors, fixes RTL, re-verifies
- "Never guess, always read waveforms" — mandated in system prompt

### Benchmark Results
- **37/92 first-pass on CVDP** (Comprehensive Verilog Design Problems benchmark)
- **5/5 on ASU Spec2Tapeout** — perfect score
- These are externally verifiable, not self-reported metrics

### Agent Architecture
- LangGraph ReAct agent with 21 tools across 6 categories:
  - Specification (3): write_spec, read_spec, load_yaml_spec_file
  - File Management (5): write_file, read_file, apply_patch_tool, edit_file_tool, list_files_tool
  - Verification (5): linter_tool, simulation_tool, waveform_tool, cocotb_tool, sby_tool
  - Synthesis & Analysis (6): start_synthesis, get_synthesis_job, wait_for_synthesis, run_synthesis_and_wait, get_synthesis_metrics, search_logs_tool
  - Reporting & Visualization (3): schematic_tool, generate_report_tool, save_metrics_tool
- System prompt mandates minimum 3 improvement iterations if any goal is unmet

### Synthesis Manager (~933 lines)
- Async job execution via ThreadPoolExecutor with job tracking
- Run isolation — each synthesis in separate directory
- Three guardrails: constraints validation, signoff checking, equivalence verification
- Exponential backoff polling (30s → 600s cap, 20-min hard timeout)
- Standard cell bootstrapping — SkyWater 130nm + ASAP7 7nm with SHA-256 manifests
- Run recovery from on-disk index after process restart

### EDA Tool Integrations (5)
- Icarus Verilog (simulation)
- OpenROAD Flow Scripts via Docker (synthesis to GDSII)
- Yosys + NetlistSVG (schematic visualization)
- SymbiYosys (formal verification)
- Cocotb (Python-based constrained random verification)

### LLM / AI
- Multi-provider LLM routing: Google Gemini (Flash, Pro), OpenAI (GPT-4, o-series), Anthropic (Claude Sonnet, Opus)
- Clean factory pattern with provider-specific quirk handling
- Two system prompt versions: v0 (~500 lines teaching prompt) and v1 (~30 lines lean operator prompt)

### MCP Server
- Full Model Context Protocol implementation
- 3 transports: stdio (Claude Desktop), SSE (remote), Streamable HTTP
- Auto-discovery: LangChain @tool functions automatically exposed as MCP tools
- Resources: browse sessions, workspace files with MIME types
- Prompts: rtl_design_workflow loads versioned architect prompt + creates session
- Tool filtering: essential (7) / all (23) / custom modes

### Frontend (Next.js)
- Three-panel layout: Sidebar | Chat | Artifacts (resizable)
- 6 artifact viewer tabs: Spec, Code (Monaco Editor), Waveform (VCD), Schematic (SVG), Layout (GDS), Report
- WebSocket streaming with real-time tool call cards
- Multi-session with token/cost tracking
- Zustand state management

### Stack
- **Backend:** Python, FastAPI, LangGraph, LangChain, SQLite (langgraph-checkpoint-sqlite)
- **Frontend:** Next.js 14, React 18, TypeScript, Zustand, Monaco Editor, Tailwind, Radix UI
- **MCP:** Model Context Protocol SDK (stdio/SSE/Streamable HTTP)
- **EDA:** Icarus Verilog, OpenROAD, Yosys, SymbiYosys, Cocotb (via Docker)
- **LLM:** Gemini, OpenAI, Anthropic

### Scale
- Python codebase: ~382K
- TypeScript codebase: ~144K
- 21 agent tools, 5 EDA integrations, 3 LLM providers, 2 PDKs
- Active research project — started Nov 2025, ongoing
- Public: github.com/naman-ranka/siliconcrew

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...              | Highlight / swap in...                                                                              |
|----------------------------------|-----------------------------------------------------------------------------------------------------|
| AI agents / LLM engineering      | LangGraph ReAct agent, 21 tools, multi-provider routing, waveform-based self-correction loop        |
| MCP / tool integration           | MCP server (3 transports, auto-discovery), Claude Desktop + VS Code integration                     |
| Research / academic              | CVDP benchmark (37/92), ASU Spec2Tapeout (5/5), autonomous design loop, system prompt design        |
| Hardware / ASIC / EDA            | OpenROAD GDSII synthesis, SkyWater 130nm + ASAP7 7nm PDKs, SymbiYosys formal verification         |
| Full-stack / systems             | FastAPI + WebSocket streaming, Next.js 6-panel artifact viewer, Monaco Editor integration           |
| Anthropic / Claude specifically  | MCP server supporting Claude Desktop, Anthropic Claude as LLM provider in multi-provider registry   |
| Autonomous systems               | Closed-loop: spec → RTL → lint → simulate → waveform debug → synthesize, mandatory iteration policy |

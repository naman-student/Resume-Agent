# SiliconCrew — EDA Resume Strategy

---

## ✅ LOCKED BULLETS (3-bullet version — preferred for AI for EDA roles)

> Built SiliconCrew, an autonomous LangGraph agent (21 tools) that drives a complete EDA pipeline — RTL generation → lint → simulation → Yosys synthesis → OpenROAD place-and-route → post-synthesis simulation → GDSII — across SkyWater 130nm and ASAP7 7nm PDKs, with SymbiYosys formal verification and Cocotb constrained-random; FastAPI + WebSocket backend, MCP server supporting Claude Desktop and VS Code.

> Closes the design loop without human intervention: on simulation failure, reads VCD waveforms, diagnoses signal-level bugs, patches RTL, and re-verifies autonomously; enforces SDC constraint validation, Yosys RTL-vs-netlist equivalence checking, and signoff guardrails before GDSII tape-out.

> Achieved 37/92 first-pass on CVDP (Comprehensive Verilog Design Problems) and 5/5 on ASU Spec2Tapeout with zero human intervention.

---

## 🔁 BACKUP — 2-bullet version (space-constrained fallback)

> Built SiliconCrew, an autonomous LangGraph agent (21 tools) that drives a complete EDA pipeline — RTL generation → lint → simulation → Yosys synthesis → OpenROAD place-and-route → post-synthesis simulation → GDSII — across SkyWater 130nm and ASAP7 7nm PDKs; on simulation failure, reads VCD waveforms, diagnoses signal-level bugs, patches RTL, and re-verifies without human intervention; SymbiYosys formal verification, Cocotb constrained-random, SDC validation, equivalence checking.

> Achieved 37/92 first-pass on CVDP (Comprehensive Verilog Design Problems) and 5/5 on ASU Spec2Tapeout with zero human intervention; FastAPI + WebSocket backend, MCP server supporting Claude Desktop and VS Code.

---

## 🔁 BACKUP — 1-bullet version (extreme space constraint)

> Built SiliconCrew, an autonomous LangGraph agent (21 tools) that drives a complete EDA pipeline (RTL generation → Yosys synthesis → OpenROAD place-and-route → GDSII) across SkyWater 130nm and ASAP7 7nm PDKs; self-corrects via VCD waveform analysis without human intervention; achieved 37/92 on CVDP and 5/5 on ASU Spec2Tapeout.

---

## 📌 POSITIONING NOTES

- This is the lead project for AI for EDA roles — always first in Project Experience
- The 3-bullet version is preferred: bullet 1 = scope, bullet 2 = differentiator, bullet 3 = proof
- Do NOT use the full-stack AI v4 single bullet here — it undersells the EDA depth and omits the pipeline detail
- "Closes the design loop without human intervention" maps directly to what Synopsys AgentEngineer and Cadence (post-ChipStack) are selling commercially — frame accordingly
- CVDP and Spec2Tapeout are the only benchmarks to cite — do NOT add SOTA comparisons unless you can source the exact paper in an interview
- "ReAct" pattern removed from locked bullet — pipeline details matter more to EDA audience than agent pattern name; add back if JD explicitly mentions LLM agent architecture
- SymbiYosys formal verification is a strong ATS keyword — always keep in bullet 1
- Cocotb constrained-random is a strong signal — shows understanding of verification methodology beyond basic simulation
- SDC constraint validation + equivalence checking + signoff guardrails in bullet 2 are daily vocabulary for Synopsys/Cadence engineers — never drop these for EDA JDs
- Public GitHub: github.com/naman-ranka/siliconcrew

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### Pipeline (correct order — verified by user)
spec → RTL generation → lint (iverilog) → simulation → Yosys synthesis → OpenROAD place-and-route → post-synthesis simulation → GDSII

### Agent Architecture
- LangGraph ReAct agent — reasons about tool results before deciding next action (not a linear script)
- 21 tools across 6 categories: Specification (3), File Management (5), Verification (5), Synthesis & Analysis (6), Reporting & Visualization (3)
- System prompt mandates minimum 3 improvement iterations if any goal is unmet
- Two system prompt versions: v0 (~500 lines teaching prompt with Verilog best practices), v1 (~30 lines lean operator prompt)

### EDA Tool Integrations (5)
- **Icarus Verilog** — lint and RTL simulation
- **OpenROAD Flow Scripts** via Docker — Yosys synthesis + full PD (floorplan → place → CTS → route → finishing)
- **Yosys + NetlistSVG** — schematic visualization + RTL-vs-netlist equivalence checking
- **SymbiYosys** — formal verification (bounded model checking)
- **Cocotb** — Python-based constrained-random verification

### PDK Support
- SkyWater 130nm (open-source CMOS)
- ASAP7 7nm FinFET (academic PDK)
- Standard cell bootstrapping from pinned GitHub commits with SHA-256 manifests

### Synthesis Manager (~933 lines — do NOT cite line count on resume)
- Async job execution via ThreadPoolExecutor with job tracking
- Per-run isolation — each synthesis in separate directory
- Three guardrails: SDC constraint validation, signoff checking, Yosys equivalence verification
- Exponential backoff polling (30s → 600s cap, 20-min hard timeout)
- Run recovery from on-disk index after process restart
- Stage inference from log tails: synth → floorplan → place → CTS → route → final

### Waveform Debug Loop
- On simulation failure: waveform_tool extracts VCD signals in time windows
- Agent reads signal transitions, diagnoses RTL bugs at signal level
- Patches RTL, re-lints, re-simulates — loop repeats until test_passed
- Mandate: "never guess, always read waveforms"
- This is the key differentiator — not just code generation, it's closed-loop autonomous verification

### Benchmarks
- **37/92 first-pass on CVDP** — Comprehensive Verilog Design Problems
- **5/5 on ASU Spec2Tapeout** — perfect score
- Both achieved with zero human intervention
- Do NOT compare to RTLLM 2.0 SOTA (~34% pass@1) unless you can source the exact paper in an interview — different benchmarks, not directly comparable

### MCP Server
- Full Model Context Protocol implementation
- 3 transports: stdio (Claude Desktop), SSE (remote), Streamable HTTP
- Auto-discovery: LangChain @tool functions automatically exposed as MCP tools
- Tool filtering: essential (7 core tools) / all (23) / custom modes
- Supports: Claude Desktop, VS Code, any MCP-compatible client

### Frontend (Next.js)
- Three-panel layout: Sidebar | Chat | Artifacts
- 6 artifact viewer tabs: Spec (YAML), Code (Monaco Editor), Waveform (VCD), Schematic (SVG), Layout (GDS), Report
- WebSocket streaming with real-time tool call cards
- Multi-session with token/cost tracking

### LLM Providers
- Google Gemini (Flash, Pro)
- OpenAI (GPT-4, o-series)
- Anthropic (Claude Sonnet, Opus)
- Clean factory pattern with provider-specific quirk handling

### Scale
- Python codebase: ~382K
- TypeScript codebase: ~144K
- 21 agent tools, 5 EDA integrations, 3 LLM providers, 2 PDKs
- Active research project — started Nov 2025, ongoing
- Started as EEE 598 course final project (Fall 2025)

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...                  | Highlight / swap in...                                                                                  |
|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| Agentic AI / autonomous design       | "Closes the design loop without human intervention" — lead with this framing                            |
| EDA tool depth (Synopsys/Cadence)    | SDC validation, equivalence checking, signoff guardrails, SymbiYosys, Cocotb — keep all in bullet 2    |
| LLM for RTL / AI-native EDA          | CVDP 37/92 + Spec2Tapeout 5/5 benchmarks, waveform-guided self-correction loop                         |
| Agent architecture / LLM engineering | Add "ReAct" back: "LangGraph ReAct agent", mention 3-transport MCP server, multi-provider LLM routing  |
| Formal verification emphasis         | Promote SymbiYosys to bullet 2; mention bounded model checking explicitly                               |
| Open-source tooling (OpenROAD/Yosys) | Emphasize OpenROAD ORFS, Yosys, SkyWater 130nm — all open-source stack                                |
| Research / academic roles            | Frame as "research prototype" started as EEE 598 final project; CVDP benchmark framing                 |
| Full-stack / systems roles           | Switch to v4 full-stack bullet (FastAPI + WebSocket + Next.js stack details matter more there)          |
| Multi-model / LLM orchestration      | Mention multi-provider routing: Gemini API, OpenAI API, Claude API with provider-specific handling      |
| Physical design specifically         | Emphasize OpenROAD PD: floorplan → place → CTS → route; post-synthesis simulation with netlist + std cells |

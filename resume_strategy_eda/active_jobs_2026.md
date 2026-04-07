# Active 2026 New Grad Job Requisitions
*Sourced from market research — April 2026*

---

## Job Listings

### NVIDIA — AI/EDA Track (9 roles)

| Role | Location | Track | Priority |
|---|---|---|---|
| Applied Machine Learning Engineer, Circuit Design — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐⭐ Top |
| Research Scientist, Electronic Design Automation — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐⭐ Top |
| Research Scientist, AI Accelerator Design and VLSI — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐⭐ Top |
| ASIC Design Verification Engineer — NCG 2026 | Austin, TX | AI/EDA | ⭐⭐ High |
| Low Power ASIC Engineer — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐ High |
| ASIC RTL Integration and Netlisting Engineer — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐ High |
| ASIC Clocks Design Engineer — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐ Mid |
| Silicon Co-Design Engineer — NCG 2026 | Santa Clara, CA | AI/EDA | ⭐⭐ High |
| GPU Architecture Engineer — NCG 2026 | Austin, TX | AI/EDA | ⭐⭐ High |

### NVIDIA — Full-Stack SWE Track (2 roles)

| Role | Location | Track | Priority |
|---|---|---|---|
| Senior Systems Software Engineer — NCG 2026 | Hillsboro, OR | Full-Stack SWE | ⭐⭐ High |
| Compiler Engineer, Backend GPU — NCG 2026 | Remote, USA | Full-Stack SWE | ⭐⭐ High |

### Google (2 roles)

| Role | Location | Track | Priority |
|---|---|---|---|
| Silicon Engineer, University Graduate 2026 | Bengaluru, India | AI/EDA | ⭐⭐⭐ Top |
| Physical Design Engineer, 3D Technology, PhD, University Graduate | Sunnyvale, CA | AI/EDA | ⭐ Mid (PhD preferred) |
| Product Support Engineer, University Graduate 2026 | Hyderabad, India | Full-Stack SWE | ⭐ Low |

### Cadence Design Systems (1 role)

| Role | Location | Track | Priority |
|---|---|---|---|
| Software Engineer II — NCG 2026 | San Jose, CA | Full-Stack SWE | ⭐⭐⭐ Top |

> Cadence acquired ChipStack AI (Seattle, Nov 2025). This role sits at the C++/Python/EDA intersection — strong fit.

### Verkada (3 roles)

| Role | Location | Track | Priority |
|---|---|---|---|
| Backend Software Engineer — University Graduate 2026 | San Mateo, CA | Full-Stack SWE | ⭐⭐⭐ Top |
| Frontend Software Engineer — University Graduate 2026 | San Mateo, CA | Full-Stack SWE | ⭐⭐ High |
| Computer Vision Software Engineer — University Graduate 2026 | San Mateo, CA | Full-Stack SWE | ⭐⭐ High |

### ByteDance (2 roles)

| Role | Location | Track | Priority |
|---|---|---|---|
| SDE Graduate (SDN Traffic Intelligence & Control) — 2026 Start | San Jose, CA | Full-Stack SWE | ⭐⭐ High |
| Backend Software Engineer Graduate (Global E-commerce) — 2026 Start | Seattle, WA | Full-Stack SWE | ⭐⭐⭐ Top |

---

## What Each Company Is Actually Looking For

### NVIDIA — Applied ML Engineer, Circuit Design / Research Scientist EDA
**Core ask:** Build AI agents that optimize the RTL-to-GDSII flow autonomously.
- Innovation in EDA algorithms using supervised, unsupervised, and RL
- Agentic AI systems for autonomous chip design
- CMOS device physics + VLSI + timing + ASIC + EDA tool knowledge
- Python, C++, PyTorch/TensorFlow
- **Naman's match:** SiliconCrew (LangGraph, 21 tools, CVDP 37/92) + GCN ASIC (Synopsys DC, Cadence Innovus, ASAP7) ✅

### NVIDIA — ASIC Design Verification / RTL Integration
**Core ask:** RTL hierarchy, logic synthesis, VCS/Verdi verification.
- Complex pipelined RTL (MIPS-level), forwarding, hazards
- SystemVerilog, UVM testbenches, formal verification
- **Naman's match:** MIPS 5-stage processor (190K SV), GCN ASIC verification ✅

### NVIDIA — GPU Architecture Engineer
**Core ask:** Cycle-accurate simulation, performance modeling, C++ systems programming.
- gem5 modification, cache replacement policies, IPC measurement
- CUDA kernels, ctypes FFI
- **Naman's match:** LRU-IPV gem5 (C++ SimObject), CUDA MLP (kernels, ctypes) ✅

### Cadence — Software Engineer II
**Core ask:** Runtime software for emulation platforms (Palladium). C++, Python, algorithms, circuit design understanding.
- Compiler-generated databases, emulator initialization
- Deep C++ + EDA domain knowledge
- **Naman's match:** STA engine (Python, Liberty NLDM, Kahn's algorithm), gem5 C++ mods ✅

### Verkada — Backend SWE
**Core ask:** Scalable distributed systems for 100K+ endpoints.
- High-concurrency: Redis, PostgreSQL, Kafka/SQS
- Async processing: Celery, Django/FastAPI decoupled from inference
- Docker, Kubernetes, Terraform, AWS
- **Naman's match:** Trezzit (Django, Redis, Celery, Docker, DigitalOcean, O(1) balances) ✅

### ByteDance — Backend SWE (E-commerce)
**Core ask:** Legacy systems integration, high-scale distributed backend.
- Reverse-engineering ERP systems, bidirectional sync bridges
- State-machine architectures, WhatsApp Business API
- **Naman's match:** NCR GOLD (18K+ orders/day, ERP reverse-engineering, WhatsApp automation) ✅

### Google — Silicon Engineer
**Core ask:** RTL design, physical design, AI-assisted chip design.
- Bengaluru location — strong fit geographically for India-based applications
- **Naman's match:** GCN ASIC full flow, SiliconCrew ✅

---

## Key Technical Signals from the Research

### What the market is paying a premium for in 2026

| Signal | Why It Matters | Naman's Asset |
|---|---|---|
| ReAct/agentic LLM for RTL-to-GDSII | Autonomous self-correction loop without human intervention | SiliconCrew — 21-tool LangGraph, VCD waveform analysis, self-correction |
| MCP integration | Bridges AI research → deployable enterprise tools (Claude Desktop, VSCode) | SiliconCrew MCP server (stdio/SSE/HTTP) + Trezzit MCP |
| Two-pass LLM pipelines | Multi-provider fallback, Pydantic validation, 60% → 95%+ accuracy | Trezzit receipt AI pipeline |
| Custom RAG without vector DB | 768-dim embeddings, cosine similarity, chunk overlap — raw math | HEAL.AI (text-embedding-004, custom retrieval) |
| Full RTL-to-GDSII tape-out | #1 recruiter ask — "tell me about your tape-outs" | GCN ASIC (Synopsys DC + Cadence Innovus + Voltus, ASAP7 7nm) |
| STA engine from scratch | Proves you understand what PrimeTime does internally | EEE598 STA engine (Liberty NLDM, bilinear interp, Kahn's algo) |
| Legacy ERP integration | Differentiator at ByteDance, Verkada, Amazon | NCR GOLD reverse-engineered ERP + WhatsApp bridge |
| CUDA kernels | Low-level GPU programming, ctypes FFI | CUDA MLP (manual cudaMalloc, ctypes bindings) |

### ATS Keywords by Track

**AI/EDA track:**
`agentic AI` · `RTL generation` · `timing closure` · `PPA` · `DRC` · `LVS` · `UVM` · `placement and routing` · `STA` · `FinFET` · `OpenROAD` · `LangGraph` · `LLM for RTL` · `CVDP` · `Synopsys DC` · `Cadence Innovus` · `ASAP7` · `SkyWater 130nm` · `SymbiYosys` · `Cocotb`

**Full-Stack SWE/AI track:**
`multi-provider orchestration` · `RAG pipeline` · `LangGraph` · `MCP` · `WebSocket` · `SSE` · `Celery` · `Redis` · `PostgreSQL` · `FastAPI` · `Django` · `React 19` · `TypeScript` · `Docker` · `Kubernetes` · `Pydantic` · `distributed systems` · `async processing`

---

## Resume Track → Role Mapping

| Resume Track | Best-fit Roles from This List |
|---|---|
| `resume_ai_eda_v3` | NVIDIA (Applied ML/Circuit Design, Research Scientist EDA, AI Accelerator, ASIC DV, RTL Integration, GPU Arch), Google Silicon Engineer, Cadence SWE II |
| `resume_ai_engineer_v1` | NVIDIA (Systems SWE, Compiler Backend GPU), Verkada (Backend, CV), ByteDance (Backend E-commerce), Cadence SWE II |
| `resume_fullstack_ai_v4` | Verkada (Backend, Frontend), ByteDance (Backend E-commerce, SDN), Google Product Support |

---

*Total active roles: 20 | AI/EDA: 11 | Full-Stack SWE: 9*

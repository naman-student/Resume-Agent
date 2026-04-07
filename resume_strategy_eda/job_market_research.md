# AI for EDA — Job Market Research
*Last updated: April 2026*

---

## 1. TARGET COMPANIES

### EDA Tool Companies (The Oligopoly)

- **Synopsys (SNPS)** — ~35% market share. Key 2025-2026 initiatives: Synopsys.ai Copilot (GenAI-powered), PrimeSim GPU acceleration (15x speedup with NVIDIA GH200), AgentEngineer (autonomous DRC reducing 2nm chip cycles by ~12 months), Microsoft agentic AI integration. Careers: careers.synopsys.com
- **Cadence Design Systems (CDNS)** — ~30% market share. Nov 2025: Acquired ChipStack AI (Seattle). Key products: Innovus+ LLM AI Assistant (natural language design analysis), Cerebrus Intelligent Chip Explorer (RL for P&R), Verisium Debug (AI-powered verification).
- **Siemens EDA** — ~10-15% market share. Calibre Vision AI (AI DRC violation analysis with TSMC), Innovator 3D IC, Calibre 3DStress for 2.5D/3D IC. AI suite unveiled at DAC 2025.

### AI Chip Design Startups

- **ChipStack** (now Cadence subsidiary) — Raised $7M+ before acquisition. Active at NVIDIA, Altera, Tenstorrent. Agentic AI for chip design/verification.
- **Silimate** — AI-powered early performance prediction. Overlapping front-end + back-end design stages simultaneously.
- **Zero ASIC** — ChipMaker platform for rapid chiplet assembly (hours not months). AI/data center focus.
- **Normal Computing** — Raised $50M (March 2026, Samsung Catalyst). AI tools for semiconductor design + energy-efficient processors.
- **Tenstorrent** — Led by Jim Keller. $700M Series D (2024) at $2.6B valuation.
- **Others**: Callosum ($10.25M, Feb 2026), Rebellions ($400M pre-IPO), SambaNova (SN50 chip Feb 2026), Mythic, Groq, Blumind, Lightmatter, Untether AI.

### Big Tech Chip Teams

- **Google/DeepMind** — Actively hiring "Software Engineer, Electronic Design Automation." Base: $189K–$300K + bonus + equity.
- **NVIDIA** — Heavy hiring AI chip design. "AI for Chip Design Intern – Summer 2026." Senior roles: $300K+.
- **Apple** — Custom GPU architectures, up to $312K for senior GPU RTL engineers.
- **Intel, Qualcomm, ARM** — Traditional chip design with growing AI-assisted tooling investment.

---

## 2. JOB TITLES (What They're Actually Called)

- AI/ML Engineer – EDA (Synopsys, Cadence primary titles)
- RTL Design Engineer, Machine Learning / ML Accelerators (Google, NVIDIA, Apple)
- EDA Algorithm Engineer (Synopsys, Cadence)
- AI-Assisted Chip Design Engineer (Startups, Big Tech)
- Design Automation Engineer (all major players)
- Hardware Design Engineer (AI focus) (Startups, NVIDIA, Google)
- Machine Learning Engineer – Semiconductor Design (EDA vendors, Big Tech)
- EDA Applications Engineer (customer support + workflow)
- Physical Design Methodology Engineer (foundries, design houses)
- Verification Engineer (AI-assisted) (all major players)
- RTL & Codesign Engineer (OpenAI)

---

## 3. REQUIRED TECHNICAL SKILLS

### Hardware Description Languages

| Language | Signal | Notes |
|---|---|---|
| Verilog | Highest demand | $98K–$225K; 3,680+ job openings |
| SystemVerilog | Higher than Verilog alone | Required with UVM; 218+ listings for SV+UVM |
| VHDL | Declining but alive | $130K–$205K; aerospace/defense |

### EDA Tools (Vendor-Specific)

| Category | Vendor | Product | AI Features |
|---|---|---|---|
| Simulation | Synopsys | PrimeSim, Custom Compiler | GPU acceleration (15x); AI parameter optimization |
| Simulation | Cadence | Spectre | Verisium Debug (AI-powered) |
| RTL Synthesis | Synopsys | Design Compiler, Spyglass | Copilot generates scripts 10-20x faster |
| Implementation | Cadence | Innovus+ | Natural language design analysis; auto script gen |
| Timing Analysis | Synopsys | PrimeTime | Copilot for script generation |
| Physical Verification | Siemens | Calibre Vision AI | AI DRC prioritization (validated with TSMC) |
| Design Automation | Cadence | Cerebrus | RL for placement & routing |

### AI/ML Frameworks

- Python (essential for design automation, ML model dev, EDA tool integration)
- C/C++ (core for EDA tool development, high-perf simulation)
- TCL (legacy but industry standard, Synopsys/Cadence scripting)
- PyTorch, TensorFlow, JAX (design flow improvements)
- RL: OpenAI Gym, Ray RLlib (applied to P&R)
- Graph Neural Networks (GNNs) — emerging for circuit representation
- GenAI proficiency explicitly listed in 2025 JDs: "Using AI tools for SystemVerilog design, validation"

### Design Domain Knowledge

- Static Timing Analysis (STA)
- Placement & Routing (P&R)
- Power Analysis & Optimization
- Design for Manufacturing (DFM)
- PDK knowledge: ASAP7 7nm, SkyWater 130nm, foundry PDKs
- Circuit Design: CMOS, analog/mixed-signal, power management

---

## 4. COMMON REQUIREMENTS

### Education
- Bachelor's minimum (EE, CE, CS)
- Master's preferred at NVIDIA, Google DeepMind, specialized startups
- PhD opens research roles at Google DeepMind, NVIDIA Research

### Experience
- Entry-level: 0–2 years
- Mid-level: 3–7 years
- Senior/Principal: 8+ years — **78% of AI/ML positions target 5+ years experience**

### Salary Benchmarks
- Entry-level EDA: $65K–$125K
- Mid-level RTL/EDA: $98K–$225K
- Senior EDA/AI: $150K–$250K
- San Jose area: $133K–$308K
- Senior Big Tech: $300K–$400K+ (salary + bonus + equity)
  - Google DeepMind EDA: $189K–$300K base
  - NVIDIA: up to $339K (senior)
  - Apple GPU RTL: up to $312K

---

## 5. WHAT DIFFERENTIATES CANDIDATES

1. **Chip tape-outs** — End-to-end design flow mastery. Recruiters actively ask: "Tell us about your tape-outs."
2. **Published research** — ICCAD, DAC, DATE papers on AI for chip design, ML for timing closure, RL for placement.
3. **LLM for RTL** — Hands-on with LLM-assisted RTL generation. Familiarity with RTLLM benchmarks (50+ designs), pass@1 metrics.
4. **Open-source contributions** — GitHub: OpenROAD, Yosys, ngspice, EDA tool contributions.
5. **Reinforcement learning projects** — RL applications even outside chip domain signal algorithmic depth.
6. **Custom PDK experience** — ASAP7, SKY130, or foundry PDKs. DRC, LVS, extraction.
7. **Multi-tool proficiency** — Fluency in 3+ EDA tools across vendors.
8. **Agentic AI understanding** — Agentic workflows, multi-agent systems, autonomous design agents (**critical emerging trend 2025-2026**).
9. **Cross-functional experience** — Hardware-software codesign, compiler integration, workload analysis.
10. **Quantified performance optimization** — Cycle-time reduction, power/area optimization, design automation improvements.

---

## 6. KEY ATS KEYWORDS

| Category | Keywords |
|---|---|
| HDL & Design | Verilog, SystemVerilog, VHDL, RTL design, register transfer level, logic synthesis, HDL coding |
| EDA Tools | Synopsys, Cadence, Siemens, Design Compiler, Innovus, PrimeSim, PrimeTime, Spectre, Virtuoso, Calibre, VCS, Xcelium |
| AI/ML | Machine learning, deep learning, neural networks, reinforcement learning, LLM, generative AI, AI agent, agentic AI, automated design |
| Verification | UVM, testbenches, functional verification, SystemVerilog Assertions (SVA), formal verification, simulation |
| Physical Design | Placement and routing, floorplanning, timing closure, DRC, LVS, DFM |
| Performance | Timing analysis, static timing analysis (STA), power analysis, PPA, signal integrity |
| Process/PDK | PDK, technology node, FinFET, CMOS, ASAP7, SKY130, foundry |
| Automation | Design automation, chip design automation, CAD, TCL, Python scripting, workflow automation |
| Emerging Terms | AI for EDA, AI-assisted design, LLM for RTL, agentic design, circuit foundation model, autonomous design, AI-native EDA |

---

## 7. EMERGING TRENDS 2025-2026

### A. Agentic AI & Autonomous Design (Most Important)
- Shift from "AI-assisted" → "AI-autonomous" multi-step execution
- Synopsys AgentEngineer: autonomous DRC, reduces 2nm cycles by ~12 months
- All 3 major vendors announced agentic AI suites at DAC 2025
- Hiring: AI orchestration engineers at Synopsys, Cadence, Google DeepMind, NVIDIA Research

### B. LLM-Assisted RTL Generation
- Research explosion: 6 papers (2023) → 29 (2024) → 64 (2025)
- Benchmarks: RTLLM 2.0 (50 designs, 4 categories); XYZ benchmark (783 problems)
- **State-of-the-art: ~34% pass@1** — directly comparable to SiliconCrew's 37/92 CVDP
- Cadence Innovus+ LLM Assistant, Synopsys.ai Copilot (10-20x faster script generation)

### C. Reinforcement Learning for Placement & Routing
- RL completes P&R in hours instead of months (published research)
- Cadence Cerebrus uses RL for automatic chip implementation
- Hiring: Cadence, Synopsys, NVIDIA Research, Google DeepMind

### D. Chip Foundation Models (CFMs)
- Large models trained on millions of circuit designs
- "AI-native EDA" — CFMs as perceptual layer for circuit understanding at scale
- Companies: Google DeepMind, NVIDIA Research, UC Berkeley, MIT, CMU

### E. AI for Timing Closure & STA
- ML models predict timing violations earlier; reduce signoff iterations from weeks to days
- Synopsys PrimeTime AI, Cadence Tempus + ChipStack integration
- **Direct relevance: STA Engine from scratch = deep understanding of what these tools do internally**

### F. AI for Mixed-Signal & Analog
- Historically resistant to automation; now targeted by AI startups
- Fewer candidates with analog + AI skills = higher compensation premium

### G. Collaborative Multi-vendor AI
- Cadence, Dassault, Siemens, Synopsys + NVIDIA building agents that work across tools simultaneously
- Emerging role: "AI Orchestration Engineer"

---

## NAMAN'S COMPETITIVE POSITION vs. MARKET

| Market Signal | Naman's Asset | Strength |
|---|---|---|
| Tape-out experience (#1 differentiator) | GCN ASIC — Synopsys DC + Cadence Innovus + Voltus, ASAP7 7nm, full metrics | ✅ Strong |
| Agentic AI for EDA (hottest trend) | SiliconCrew — autonomous LangGraph agent, 21 tools, CVDP 37/92 | ✅ Strongest (pre-dates commercial products) |
| LLM for RTL benchmarks | CVDP 37/92 (~34% pass@1 is SOTA) + 5/5 ASU Spec2Tapeout | ✅ Externally verifiable |
| STA tool knowledge | EEE598 STA engine from scratch — NLDM Liberty, bilinear interpolation, critical path | ✅ Deep, rare |
| Multi-tool EDA proficiency | Synopsys DC, Cadence Innovus, Voltus, OpenROAD, Yosys, SymbiYosys, Cocotb | ✅ Broad |
| Custom PDK experience | ASAP7 7nm + SkyWater 130nm | ✅ Both open PDKs |
| SystemVerilog depth | GCN ASIC, MIPS processor (190K SV), FinFET labs | ✅ Demonstrated |
| Open source contribution | Intel PR #655 merged upstream | ✅ Minor but real |
| Master's degree | MS Computer Engineering, ASU (May 2026, GPA 3.81) | ✅ Preferred level |
| Research framing | CVDP benchmark, ASU Spec2Tapeout, EEE598 course STA engine | ✅ Academic credibility |

---

## RESUME STRATEGY IMPLICATIONS

1. **Lead with the agentic AI angle** — SiliconCrew predates Synopsys AgentEngineer commercially. Frame this clearly in summary.
2. **GCN ASIC is the tape-out proof** — Full Synopsys DC + Cadence Innovus + Voltus flow with concrete PPA metrics is the #1 recruiter ask.
3. **STA Engine is a hidden gem** — Built what PrimeTime does. Name it explicitly for Synopsys/Cadence audiences.
4. **ATS keywords to weave in**: agentic AI, RTL generation, timing closure, PPA, DRC, LVS, UVM, placement and routing, STA, FinFET, OpenROAD.
5. **CVDP benchmark is directly SOTA-comparable** — State-of-the-art is ~34% pass@1; 37/92 ≈ 40%. Worth framing against published benchmarks.
6. **IISc Intern is worth keeping** — Ansys Maxwell FEA + hardware simulation = hardware credibility that software-only candidates lack.
7. **Target first**: Google DeepMind EDA, NVIDIA AI for Chip Design, Cadence (post-ChipStack), Synopsys AI team, Zero ASIC, Silimate.

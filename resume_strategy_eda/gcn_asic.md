# GCN ASIC Accelerator — EDA Resume Strategy

---

## ✅ LOCKED BULLETS (2-bullet version)

> Designed an 11-module GCN ASIC accelerator in SystemVerilog — 8 parallel MACs for 96-element dot products and a 12-state FSM for bidirectional COO edge aggregation — and completed the full RTL-to-GDSII flow: Synopsys Design Compiler synthesis on ASAP7 7nm RVT (1 ns clock, 10,878 cells), Cadence Innovus APR with CTS, and Voltus post-APR power analysis driven by VCD activity files.

> Achieved 50,300 µm² chip area at 50.6% core density, 52.29 mW total power (64.8% switching), and 99.2 ns end-to-end latency.

---

## 🔁 BACKUP — 1-bullet version (space-constrained fallback)

> Designed an 11-module GCN ASIC accelerator in SystemVerilog (8 parallel MACs, 12-state COO aggregation FSM) and completed the full RTL-to-GDSII flow — Synopsys Design Compiler on ASAP7 7nm RVT → Cadence Innovus APR → Voltus post-APR power analysis — achieving 50,300 µm² chip area, 52.29 mW total power, and 99.2 ns end-to-end latency.

---

## 📌 POSITIONING NOTES

- This is the tape-out proof — the #1 differentiator for EDA roles per job market research
- Always second project after SiliconCrew on the EDA resume
- The tool chain (Synopsys DC → Cadence Innovus → Voltus) is the commercial stack; name all three explicitly — never abbreviate or omit
- "VCD activity files" for Voltus is a detail that signals real power analysis knowledge — keep it
- "Full RTL-to-GDSII flow" is the exact phrase EDA recruiters scan for — always in bullet 1
- ASAP7 7nm RVT is a realistic modern FinFET node — signals you worked with a relevant process
- This is coursework (EEE 525 VLSI, Spring 2025, ASU) — do NOT mark as such on resume; the metrics are real regardless
- No public GitHub (private coursework repo) — compensate with tool specificity and PPA metrics
- Latency: 99.2 ns — from final design iteration (use this number, not 200.7 ns from earlier run)
- Do NOT use "tape-out" anywhere — the design was completed to GDSII in a course setting, not sent to a foundry for fabrication. "Tape-out" implies a chip was made. Use "RTL-to-GDSII flow" instead.

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### What It Is
- GCN = Graph Convolutional Network — node classification task (movie genre: Action/Humor/Family across 6 nodes, 96 features)
- Feature Transformation: FM × WM (6×96 × 96×3)
- Feature Aggregation: ADJ × FM_WM via sparse COO-format streaming
- Argmax classification for final output

### RTL Architecture
- 3-block hierarchy, 11 SystemVerilog modules
- **Transform_Block**: parameterized Vector_Multiplier with 8 parallel MAC units, processes 96-element dot products over pipelined cycles; consumes 59.4% of total cell area
- **Combination_Block**: 12-state Combination_FSM implementing bidirectional edge aggregation (u→v and v→u per COO edge) with internal accumulator memory
- **Argmax_Block**: sequential max-finding and index output
- Top-level GCN module with full enable_read/read_address/done handshake protocol

### 5 Optimization Techniques Applied
1. Parallelism — 8 concurrent multipliers
2. Pipelining — overlapping transform and combination stages
3. Memory management — reusable accumulator SRAM minimizing switching activity
4. FSM minimization — state machines designed to cut control overhead
5. Clock gating — reducing dynamic power

### Synthesis Results (Synopsys Design Compiler)
- Process: ASAP7 7nm RVT standard cells
- Clock target: 1 ns
- Cells: 10,878 total (9,054 combinational, 1,822 sequential)
- Cell area: 20,676 µm²
- Transform_Block: 59.4% of area

### APR Results (Cadence Innovus)
- CTS, place & route, filler insertion
- Chip area: 50,300 µm²
- Core density: 50.6%

### Power Analysis (Voltus, VCD activity files)
- Total power: 52.29 mW
  - Switching: 64.8%
  - Internal: 35.2%
  - Leakage: 0.002%

### Final PPA
- Area: 50,300 µm² chip area
- Power: 52.29 mW
- Latency: 99.2 ns end-to-end (final iteration)

### Tool Chain
- Synopsys Design Compiler — logic synthesis
- Cadence Innovus — APR (CTS, place & route, filler)
- Voltus — post-APR power analysis with VCD activity files
- Siemens ModelSim — RTL simulation (used during design)
- ASAP7 7nm PDK

### Course Context
- Course: EEE 525 VLSI Design — Arizona State University, Spring 2025
- Private repo (coursework)
- Targeted end-to-end latency under 100 ns on ASAP7 7nm — achieved in final iteration (99.2 ns)

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...                    | Highlight / swap in...                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| Physical design / APR                  | Cadence Innovus CTS + place-and-route detail; core density 50.6%                                   |
| Power analysis / low power             | Voltus VCD-driven power analysis; switching 64.8%; clock gating optimization technique             |
| Synopsys tool stack                    | Synopsys Design Compiler synthesis detail; 10,878 cells at 1 ns clock on ASAP7 7nm RVT            |
| Cadence tool stack                     | Cadence Innovus APR + Voltus power — both named explicitly                                          |
| RTL design / SystemVerilog depth       | 11-module hierarchy, 8 parallel MACs, 12-state FSM, handshake protocol, pipelining                 |
| ASIC accelerator / ML hardware         | GCN accelerator context — node classification, feature transformation + aggregation pipeline        |
| FinFET / advanced node                 | ASAP7 7nm FinFET — realistic advanced node, not just 180nm academic                                |
| Design optimization / PPA             | List all 5 optimization techniques: parallelism, pipelining, memory mgmt, FSM minimization, clock gating |
| Timing closure / STA                   | 1 ns clock target met; link to STA Engine project for deeper STA knowledge                         |

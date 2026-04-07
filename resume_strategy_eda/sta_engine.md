# STA Engine — EDA Resume Strategy

---

## ✅ LOCKED BULLET (1-bullet version)

> Built a complete Static Timing Analysis engine in Python from scratch — Liberty NLDM parser (7×7 delay/slew LUTs with bilinear interpolation), .bench circuit-graph parser, topological sort via Kahn's algorithm, forward arrival-time and slew propagation, backward RAT/slack computation, and critical path extraction; validated against ISCAS benchmarks c17, b15, and c7552.

---

## 📌 POSITIONING NOTES

- Hidden gem for Synopsys and Cadence audiences specifically — they build PrimeTime; you built a stripped-down version of it
- Every term in this bullet (NLDM, Liberty, bilinear interpolation, RAT, slack, critical path) is daily vocabulary for their timing engineers
- Frame project title as "Static Timing Analysis Engine" — not "EEE 598 Project" or "STA Tool"
- This is coursework (EEE 598 VLSI Design Automation, ASU, Fall 2025–Spring 2026) — do NOT state on resume
- Private repo — compensate with algorithm specificity
- "From scratch" is acceptable here because it's describing the implementation approach, not a junior signal — no EDA libraries, no NetworkX, pure Python algorithms
- Pairs well with GCN ASIC for Synopsys/Cadence: you know how their synthesis tools work (DC) AND how their timing tools work (PrimeTime)
- Drop this project if space is very tight — SiliconCrew and GCN ASIC are higher priority

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### What It Replicates
- Core engine of Synopsys PrimeTime — the industry-standard STA tool
- Validated against ISCAS '85 benchmark circuits: c17 (simple gate network), b15 (sequential), c7552 (complex combinational)
- Output format matches expected ckt_traversal.txt for automated grading

### Phase 1 — Parsing
- **.bench parser**: builds full directed circuit graph with fanin/fanout linked Node objects; identifies primary inputs/outputs; maps gate types to Liberty cells
- **Liberty .lib parser**: extracts NLDM (Non-Linear Delay Model) tables — 7×7 LUTs indexed by input slew and output load capacitance for both delay and output slew
- **Bilinear interpolation**: computes delay/slew at arbitrary (slew, load) operating points between LUT entries

### Phase 2 — STA
- **Topological sort**: Kahn's algorithm — no NetworkX or external graph libraries
- **Forward traversal**: computes per-gate arrival times and output slews using NLDM lookup with load-capacitance scaling for multi-fanout gates
- **Backward traversal**: computes required arrival times (RAT = 1.1× circuit delay) and slack for every node
- **Critical path extraction**: walks minimum-slack fanins from the worst-case primary output
- **Output**: circuit delay in picoseconds, per-gate slacks, full critical path as comma-separated gate chain

### Key Algorithms
- Kahn's algorithm for topological sort (BFS-based, detects cycles)
- Bilinear interpolation on 2D LUT grids for NLDM delay/slew
- Forward/backward timing traversal (standard STA two-pass)
- Critical path backtracing from worst slack node

### Why It Matters for EDA Interviews
- Synopsys PrimeTime, Cadence Tempus — both use NLDM Liberty models, topological traversal, forward/backward passes
- Building it from scratch means you understand the algorithm, not just the tool interface
- Interviewers at EDA companies will ask "how does STA work?" — you can answer from implementation experience
- ISCAS validation shows you tested against real industry benchmark circuits

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...                    | Highlight / swap in...                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Static timing analysis / STA           | Full algorithm detail: NLDM, bilinear interpolation, Kahn's sort, forward/backward passes               |
| Synopsys PrimeTime / Cadence Tempus    | Explicitly mention "replicating the core flow of tools like Synopsys PrimeTime" in interview context    |
| EDA algorithm development              | Emphasize no external libraries — pure algorithmic implementation                                        |
| Timing closure / signoff               | Pair with SiliconCrew SDC constraint validation and signoff guardrails                                   |
| Liberty / PDK knowledge                | NLDM Liberty .lib parsing — shows familiarity with standard cell characterization format                |
| Python for EDA scripting               | Pure Python implementation; no EDA or graph libraries — signals clean engineering                        |
| Space very tight                       | Drop this project; keep SiliconCrew + GCN ASIC as the two core hardware projects                        |

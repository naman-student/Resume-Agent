# LRU-IPV gem5 — EDA Resume Strategy

---

## ✅ LOCKED BULLET (1-bullet version)

> Implemented LRU with Insertion Position Vector (IPV) replacement policy from scratch inside gem5's C++ source as a first-class SimObject, integrating all 4 cache interface methods (reset, touch, getVictim, invalidate); modified 5 gem5 source files and validated across 3 L2 cache configurations (128/256/512 kB), observing L2 replacements collapse from 637 → 112 → 2 as cache capacity grew — isolating clean capacity-vs-policy effects at 41.8M instructions, 2.04 IPC.

---

## 📌 POSITIONING NOTES

- Always after STA Engine in project list — 5th and last project entry on EDA resume
- Its job: **justify gem5 in the skills row** — gem5 is in Process/Verification; this is the proof of claim
- "First-class SimObject" and "modified 5 gem5 source files" distinguishes from candidates who only run gem5 as a black box
- The 637 → 112 → 2 replacement collapse is a memorable, concrete result — interviewers will ask about it
- Pairs with MIPS processor for microarchitecture depth signal (cache policy + pipelined CPU = full-stack computer architecture understanding)
- Date: Fall 2024 — course project (Advanced Computer Architecture, CSE 520) — do NOT state on resume
- Drop if space extremely tight — SiliconCrew, GCN ASIC, STA Engine are higher priority for pure EDA roles

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### What Was Built
- LRU-IPV = LRU replacement with Insertion Position Vector — a learned cache insertion policy
- Implemented as a first-class gem5 SimObject in C++, not a wrapper or script
- Modified 5 gem5 source files to integrate the new policy into gem5's cache hierarchy

### 4 Cache Interface Methods
- `reset` — initializes replacement state for a newly allocated cache block
- `touch` — updates IPV position on cache hit (promotion logic)
- `getVictim` — selects eviction candidate based on IPV ordering
- `invalidate` — handles block invalidation and state cleanup

### Validation
- 3 L2 cache configurations: 128 kB, 256 kB, 512 kB
- L2 replacements: 637 → 112 → 2 as capacity grows — isolates capacity effect from policy effect cleanly
- Workload: 41.8M instructions, 2.04 IPC
- gem5 full-system simulation with gem5's standard benchmark infrastructure

### Why It Matters for EDA/Hardware Roles
- gem5 is the industry-standard CPU/cache architectural simulator — used by ARM, Intel, AMD, academic research
- Modifying gem5 C++ source (not just running it) shows systems programming depth
- Cache replacement policy knowledge is directly relevant to memory subsystem design in ASIC/SoC contexts
- The controlled experiment (3 configs, isolating capacity-vs-policy) shows engineering rigor and measurement methodology

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...                    | Highlight / swap in...                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| Computer architecture / microarch      | Full gem5 SimObject detail; 4 interface methods; 3-config controlled experiment                     |
| Cache / memory hierarchy               | LRU-IPV policy detail; replacement collapse numbers (637 → 112 → 2); capacity-vs-policy isolation   |
| C++ systems programming                | "Modified 5 gem5 source files" — first-class C++ integration, not scripting                        |
| Simulation tools / EDA simulation      | gem5 architectural simulation pairs with Ansys Maxwell FEA (IISc) for simulation breadth           |
| Space very tight                       | Drop this project; gem5 stays in skills row — mention it briefly in interview context if asked      |

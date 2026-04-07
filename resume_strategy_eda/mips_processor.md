# MIPS Processor — EDA Resume Strategy

---

## ✅ LOCKED BULLET (1-bullet version)

> Implemented a 5-stage pipelined MIPS processor in SystemVerilog (33 instructions) with a 12-path forwarding network (EX-to-EX, MEM-to-EX, WB-to-ID, branch, JR) and 6 hazard stall conditions; extended with an 8-entry fully-associative CAM instruction cache (3-state FIFO FSM) and LL/SC atomic operations with link-address tracking.

---

## 📌 POSITIONING NOTES

- Supporting project on the EDA resume — always after SiliconCrew and GCN ASIC
- Its job: signal RTL design depth beyond just running EDA tools
- 12-path forwarding network and CAM cache are the strongest details — show microarchitecture understanding
- Do NOT cite "190K SystemVerilog" — line count is a bad metric
- Do NOT frame as "progressively built" or "semester-long" — reads like coursework
- Public GitHub: github.com/naman-ranka/mips-processor
- Course: CSE 520 Advanced Computer Architecture, ASU, Fall 2025 – Spring 2026 (do not state on resume)
- Drop this project if space is very tight — SiliconCrew, GCN ASIC, and STA Engine are higher priority for EDA roles

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### Pipeline Stages
1. IF — PC, instruction memory, CAM cache with FIFO replacement
2. ID — 12-bit opcode decoder, register file read, sign/zero extension, early branch resolution
3. EX — ALU with forwarding mux (Stage 4 > Stage 5 priority)
4. MEM — Data memory (1024 words), byte/halfword/word access, LL/SC logic
5. WB — Mux: ALU result / memory load / SC success flag; halt only when HALT reaches Stage 5

### Forwarding Network (12 paths)
- EX-to-EX (1-stage): alu_out Stage 4 → ALU inputs Stage 3
- MEM-to-EX (2-stage): reg_wdata Stage 5 → ALU inputs (lower priority)
- WB-to-ID (3-stage): reg_wdata Stage 5 → Stage 2 register reads
- Branch forwarding (4 paths): Stages 4/5 → equality comparator in Stage 2
- JR forwarding (2 paths): Stages 4/5 → PC

### Stall Conditions (6)
- Load-use hazard (r1/r2): 1-cycle bubble when load in Stage 3 feeds Stage 2
- JR stall (Stage 3/4): value needed by JR still being computed
- Branch stall (Stage 3/4): value needed by branch condition still in flight

### CAM Instruction Cache
- 8-entry fully-associative
- 3-state FSM: IDLE → LOAD → CLEAR
- FIFO eviction policy
- Skips cache load on branch/jump (instruction about to be squashed)

### LL/SC Atomic Operations
- Link address register + link valid flag
- SC succeeds only if link_valid set and address matches
- Any intervening store to linked address invalidates the link
- SC result (1=success, 0=fail) written back through WB stage

### Supported Instructions (33)
- R-Type (12): ADD, ADDU, SUB, SUBU, AND, OR, NOR, SLT, SLTU, SLL, SRL, SRA
- I-Type (8): ADDI, ADDIU, ANDI, ORI, SLTI, SLTIU, LUI
- Memory (7): LW, LBU, LHU, SW, SB, SH, LL/SC
- Branch (2): BEQ, BNE
- Jump (3): J, JAL, JR
- Special (1): HALT

### Scale
- 190K SystemVerilog (do not cite on resume)
- 29 commits, solo, public repo
- Progressive build: HW1 (ALU, PC, regfile) → HW11 (LL/SC atomics)

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...                  | Highlight / swap in...                                                                          |
|--------------------------------------|--------------------------------------------------------------------------------------------------|
| Processor / microarchitecture        | Full forwarding network detail; stall conditions; early branch resolution in Stage 2            |
| Cache design / memory hierarchy      | CAM cache detail: 8-entry fully-associative, 3-state FIFO FSM, branch/jump squash handling     |
| Concurrent / atomic operations       | LL/SC with link-address tracking; memory consistency                                            |
| RTL / SystemVerilog depth            | 12-path forwarding, 6 stall conditions, byte-granularity memory access (SB, SH, LBU, LHU)     |
| Computer architecture tools          | Pair with LRU-IPV gem5 project for deeper architecture signal                                   |
| Space very tight                     | Drop this project; keep SiliconCrew + GCN ASIC + STA Engine as the three hardware projects     |

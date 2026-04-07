# Summary — AI Engineer Resume Strategy

---

## ✅ LOCKED

> MS Computer Engineering (ASU, GPA 3.81, May 2026) building production LLM agents, RAG pipelines, and AI-powered systems. Designed SiliconCrew — a 21-tool LangGraph agent with autonomous self-correction, multi-provider routing (Gemini/OpenAI/Anthropic), and a full MCP server — and shipped Trezzit, a live production AI SaaS (trezzit.com) with a two-pass LLM pipeline across 4 providers, 995 automated tests, and real user traction.

**Why this works:**
- "LLM agents, RAG pipelines, and AI-powered systems" — three ATS phrase clusters in one clause; all appear in 60%+ of AI Engineer JDs
- SiliconCrew: LangGraph (used at LinkedIn/Uber/400+ companies), MCP server (97M SDK downloads, enterprise-validated), autonomous self-correction — the highest-signal AI engineering vocabulary in 2025-26
- Trezzit: "live production AI SaaS" with URL = rare proof point for new grads; 4-provider pipeline + 995 tests signals production-grade
- GPA 3.81 always, never 3.8

---

## 🔁 BACKUP VERSIONS

### B — Forward Deployed Engineer (Anthropic FDE, OpenAI FDE, Scale AI)
> MS Computer Engineering (ASU, GPA 3.81, May 2026) building customer-facing AI systems and autonomous agents. Shipped Trezzit (trezzit.com) — a live production AI SaaS with a two-pass LLM pipeline improving receipt parsing from 60% to 95%+ accuracy — and built SiliconCrew, a 21-tool LangGraph agent with autonomous self-correction and MCP server, achieving 5/5 on end-to-end task completion benchmarks.

*Use when: JD emphasizes customer-facing AI, deployment into production environments, and measurable AI performance improvement.*

### C — Applied AI / ML Engineer (mid-size product companies)
> MS Computer Engineering (ASU, GPA 3.81, May 2026) with hands-on production AI experience. Built SiliconCrew (LangGraph agent, MCP server, multi-provider routing) and Trezzit (two-pass LLM pipeline, 4 providers, 995 tests, trezzit.com); also built a custom RAG pipeline winning 1st place at Devlabs Hackathon — PDF chunking, 768-dim embeddings, cosine similarity retrieval without an external vector DB.

*Use when: JD specifically mentions RAG, retrieval systems, or wants to see breadth across agent + RAG + production deployment.*

---

## 🎯 JD-BASED SWAP GUIDE

| JD Signal | Swap / Add |
|---|---|
| "LangGraph" / "LangChain" / "agent" | Emphasize SiliconCrew's ReAct agent, 21 tools, autonomous debug loop |
| "MCP" / "tool use" / "function calling" | Lead with MCP server: 3 transports (stdio/SSE/HTTP), auto-discovery, Claude Desktop + VS Code support |
| "RAG" / "retrieval" / "vector DB" | Surface HEAL.AI: 768-dim embeddings, cosine similarity, no external vector DB — mention in summary |
| "multi-provider" / "model routing" / "LLM abstraction" | Lead with Trezzit 4-provider registry + SiliconCrew provider quirk handling — two independent examples |
| "production" / "reliability" / "CI/CD" / "testing" | Lead with Trezzit: 995 tests, GitHub Actions CI, DigitalOcean, O(1) balance reads |
| "Forward Deployed Engineer" / "FDE" / "customer-facing" | Use Version B; emphasize 60%→95%+ accuracy improvement and live user traction |
| "evaluation" / "evals" / "LLM metrics" | Add SiliconCrew benchmark context: "structured code generation benchmark, autonomous eval via waveform diagnostics" |
| "observability" / "monitoring" / "cost tracking" | Highlight SiliconCrew B3: per-session token/cost tracking across all LLM providers, WebSocket execution cards |
| "Pydantic" / "output validation" / "structured output" | Mention two-pass semantic validation in Trezzit; Pydantic in skills row 2 |
| "startup" / "0→1" / "shipping fast" | Lead with "sole-built and shipped" Trezzit — 12+ months, 40 models, 60+ endpoints, 995 tests |

---

## 📌 POSITIONING NOTES

- This resume targets: AI Engineer, Applied AI Engineer, ML Engineer, Forward Deployed Engineer, LLM Engineer
- NOT for: pure GPU/CUDA roles (use ML Systems track), full-stack product roles (use Full-Stack AI track), EDA/hardware roles (use AI for EDA track)
- LangGraph is the #1 differentiator — it's confirmed in production at 400+ companies (LinkedIn, Uber, etc.) and growing. Always mention it by name.
- MCP server is still rare enough (Feb 2026) to be a genuine differentiator — 97M SDK downloads signals ecosystem maturity but most engineers haven't built a server
- "Autonomous self-correction" is the AI Engineer vocabulary for the agentic debug loop — use it; "autonomous waveform-guided" is EDA-specific and confuses non-hardware audiences
- trezzit.com URL stays in summary — live production proof is the #1 signal hiring managers at Anthropic/Scale/Cohere look for in new grads
- GPA 3.81 always
- Do NOT mention RTL, GDSII, Verilog, OpenROAD, CVDP, Spec2Tapeout — EDA-specific, confuses AI Engineer readers

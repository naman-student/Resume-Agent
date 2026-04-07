# Technical Skills — Resume Strategy

---

## ✅ SELECTED (4-Row Version — Default)

```
Frontend:       React 19 | TypeScript | Next.js | Material-UI | Tailwind CSS | PWA | React Router
Backend:        Python | Django REST Framework | FastAPI | PostgreSQL | Redis | Celery | WebSocket
AI / LLM:       Gemini API | OpenAI API | Claude API | LangChain | LangGraph | RAG Pipelines | MCP (Model Context Protocol) | Multi-model Orchestration
Infrastructure: Docker | DigitalOcean | AWS | Vercel | Supabase | Nginx | GitHub Actions CI/CD | Linux
```

---

## 🔁 BACKUP — 3-Row Version (space-constrained)

```
Frontend / Backend: React 19 | TypeScript | Next.js | Django REST | FastAPI | PostgreSQL | Redis | Celery | WebSocket
AI / LLM:           Gemini API | OpenAI API | Claude API | LangChain | LangGraph | RAG Pipelines | MCP (Model Context Protocol)
Infrastructure:     Docker | DigitalOcean | AWS | Vercel | Supabase | Nginx | GitHub Actions CI/CD | Linux
```

---

## 📌 RULES — What Never Goes In

- **No company names as skills** — "Google", "OpenAI", "Anthropic" are vendors not skills. Use API/framework names: "Gemini API", "OpenAI API", "Claude API"
- **No "Prompt Engineering"** — overused and unverifiable in 2026. Replaced with "Multi-model Orchestration" which is earned and specific
- **No "JWT Auth"** — implementation detail, not a skill
- **No "systemd"** — borderline DevOps detail, not a full-stack AI skill signal
- **No "GSAP"** — animation library for landing pages, not a hiring signal for AI roles
- **No lines of code as metrics anywhere on resume** — more code ≠ better code

---

## 📌 RULES — What Always Stays

- **MCP (Model Context Protocol)** — always spell out in full at least once. Unique differentiator, built for both Trezzit and SiliconCrew. New enough that acronym alone won't register.
- **Multi-model Orchestration** — earned twice: Trezzit's provider-abstracted LLM registry (Gemini/OpenAI/Claude/Grok with automatic fallback) and SiliconCrew's multi-provider routing. Defensible in any interview.
- **LangGraph** — hot keyword for AI engineer roles in 2026, and you've built a 21-tool ReAct agent with it
- **RAG Pipelines** — built custom in HEAL.AI, used in production
- **WebSocket** — used in SiliconCrew for real-time agent streaming

---

## 🧠 FULL SKILLS POOL (for JD-based additions)

### Frontend
| Skill | Evidence |
|-------|----------|
| React 19 | Trezzit (341 components, 14 contexts, 8 hooks) |
| TypeScript | HEAL.AI, SiliconCrew frontend, AdaptED AI |
| Next.js | HEAL.AI, SiliconCrew frontend |
| Material-UI v6 | Trezzit (primary UI library) |
| Tailwind CSS | Trezzit, HEAL.AI, AdaptED AI |
| PWA | Trezzit (service worker, VAPID push, Share Target, iOS) |
| React Router v7 | Trezzit |
| Framer Motion | Trezzit animations |
| GSAP | Trezzit landing page (ScrollTrigger) — weak signal for AI roles |
| Zustand | SiliconCrew frontend |
| Monaco Editor | SiliconCrew (code viewer) |
| Recharts | Trezzit expense analytics |
| D3.js | TwinGenius |
| shadcn/ui | HEAL.AI, SiliconCrew, AdaptED AI |

### Backend
| Skill | Evidence |
|-------|----------|
| Python | All major projects |
| Django REST Framework | Trezzit (40 models, 60+ endpoints, 995+ tests), OMS |
| FastAPI | HEAL.AI, SiliconCrew |
| PostgreSQL | Trezzit (Supabase), OMS |
| Redis | Trezzit (caching, Celery broker, rate limiting) |
| Celery | Trezzit (background tasks, scheduled jobs), OMS (session expiry) |
| WebSocket | SiliconCrew (real-time agent streaming) |
| REST API Design | Trezzit, HEAL.AI, SiliconCrew |
| Google OAuth | Trezzit (django-allauth) |
| SQLite | HEAL.AI, SiliconCrew (session persistence) |

### AI / LLM
| Skill | Evidence |
|-------|----------|
| Gemini API | Trezzit (primary LLM), HEAL.AI, AdaptED AI, TwinGenius |
| OpenAI API | Trezzit (alt provider), SiliconCrew |
| Claude API | Trezzit (alt provider), SiliconCrew |
| LangChain | SiliconCrew (tool wrappers, agent orchestration) |
| LangGraph | SiliconCrew (21-tool ReAct agent with checkpointing) |
| RAG Pipelines | HEAL.AI (PDF chunking, document search, cosine similarity retrieval) |
| MCP (Model Context Protocol) | SiliconCrew (full server: stdio/SSE/HTTP), Trezzit (auth 2.1) |
| Multi-model Orchestration | Trezzit (provider registry + fallback), SiliconCrew (multi-provider routing) |
| Vector Embeddings | HEAL.AI (Google text-embedding-004, 768-dim) |
| Structured Output Validation | Trezzit (two-pass receipt pipeline semantic validation) |

### Infrastructure
| Skill | Evidence |
|-------|----------|
| Docker | SiliconCrew, HEAL.AI, Intel Self-Checkout |
| DigitalOcean | Trezzit backend (VPS, Spaces CDN) |
| AWS | Trezzit (Lightsail staging) |
| Vercel | Trezzit frontend, landing page |
| Supabase | Trezzit (managed PostgreSQL) |
| Nginx | Trezzit (reverse proxy, SSL, static files) |
| GitHub Actions CI/CD | Trezzit (995+ tests, prod→staging DB sync) |
| Linux | Trezzit (systemd services, VPS management) |
| Gunicorn | Trezzit, OMS |

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...          | Add / swap in...                                                                 |
|------------------------------|----------------------------------------------------------------------------------|
| AI agents                    | LangGraph, LangChain, MCP (Model Context Protocol), Multi-model Orchestration    |
| RAG / document AI            | RAG Pipelines, Vector Embeddings (swap in from pool)                             |
| Frontend depth               | Framer Motion, Zustand, Monaco Editor, shadcn/ui (swap in from frontend pool)   |
| Backend / systems            | Gunicorn, Nginx, Google OAuth, SQLite (swap in from backend pool)                |
| Cloud / infrastructure       | AWS Lightsail, Supabase, Gunicorn (already in infra pool)                        |
| Hardware / EDA (rare)        | SystemVerilog, OpenROAD, LangGraph agent tools (from SiliconCrew context)        |

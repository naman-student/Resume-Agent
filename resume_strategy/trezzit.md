# Trezzit — Resume Strategy

---

## ✅ SELECTED BULLETS (Current Best — 3 Bullet Version)

> Solo-built and shipped Trezzit (app.trezzit.com), a production bill-splitting SaaS serving **600+ users** over 12+ months — **341 React components, 60+ REST endpoints, 40 DB models, 995+ backend tests**; Django 5.1 + DRF, React 19 PWA, PostgreSQL (Supabase), Redis, Celery, DigitalOcean VPS (prod) + AWS Lightsail (staging), Vercel; GitHub Actions CI/CD in ~3 min.

> Built two-stage AI receipt scanning pipeline (Gemini, OpenAI, Claude, Grok) that improved parsing accuracy from **~60% → 95%+** — semantic validation with automatic fallback to higher-capability model on failure; pre-computed balance system with O(1) debt reads, incremental updates, and automatic reconciliation.

> Built MCP server (Model Context Protocol) enabling AI assistants to create and query itemized expenses; production monitoring tracks per-provider LLM costs and API response times across all 60+ endpoints.

---

## 🔁 BACKUP — 2 Bullet Version (use when space is tight)

> Solo-built and shipped Trezzit (app.trezzit.com), a production SaaS serving **600+ users** over 12+ months — **341 React components, 60+ REST endpoints, 995+ backend tests**; Django 5.1 + DRF, React 19 PWA, PostgreSQL (Supabase), Redis, Celery, DigitalOcean VPS + Vercel; GitHub Actions CI/CD in ~3 min.

> Built two-stage AI receipt scanning pipeline (Gemini, OpenAI, Claude, Grok) improving accuracy **~60% → 95%+** — semantic validation, automatic model-upgrade fallback; O(1) pre-computed balance system; MCP server enabling AI assistants to create and query expenses; LLM cost and API response monitoring in production.

---

## 📌 POSITIONING NOTES

- **Lead with outcome always** — "600+ users, production, shipped" must appear in bullet 1. Scale signals (341 components, 995 tests) come second. Stack comes last.
- **60% → 95% accuracy is the strongest AI metric on the entire resume** — never cut this line regardless of space constraints
- **MCP server is a genuine differentiator** — very few candidates have built one. Always keep it, but explain it: "Model Context Protocol" for readers unfamiliar
- This is your flagship project — gets the most space (3 bullets) on most versions
- Has a live public URL (app.trezzit.com) — always include the link, it proves the project is real
- For AI/LLM engineer roles: consider leading bullet 2 with the AI pipeline instead of keeping scale-first structure. Swap to Version B from context pool below.
- For pure SWE/backend roles: emphasize the 995+ tests, O(1) balance system, and GitHub Actions CI/CD more heavily

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### Scale & Impact
- 600+ users (as of Apr 2026, actively growing)
- 12+ months of solo development (started Mar 2025)
- 341 React components, 650 source files
- 60+ REST API endpoints, 27 API service modules
- 40 DB models across 10+ Django apps
- 995+ backend tests, ~3 min full CI run
- 14 React contexts (no Redux)
- 8 custom hooks

### Stack
- **Frontend:** React 19, PWA, Material-UI v6, Tailwind CSS, Framer Motion, GSAP (ScrollTrigger), React Router v7, Recharts, react-force-graph
- **Backend:** Django 5.1, Django REST Framework, PostgreSQL (Supabase), Redis, Celery + Celery Beat + Flower
- **Auth:** Cookie-based JWT (HTTP-only, auto-refresh, failed-request queuing), Google OAuth via django-allauth, email OTP
- **AI:** Google Gemini (primary), OpenAI, Anthropic Claude, Grok — provider-abstracted registry pattern
- **Infrastructure:** DigitalOcean VPS (prod), AWS Lightsail (staging), Vercel (frontend), Supabase (PostgreSQL), DigitalOcean Spaces CDN
- **DevOps:** GitHub Actions CI/CD, prod→staging DB sync, Gunicorn + Nginx, systemd (4 services: gunicorn, celery, celery-beat, flower)
- **Email:** ZeptoMail (primary), SendGrid (fallback)

### AI Receipt Pipeline (Key Feature)
- Two-stage processing: Pass 1 (Gemini Flash Lite, fast + cheap) → semantic validation → Pass 2 (Gemini Flash, higher capability) on failure
- Accuracy improved from ~60% → 95%+ after two-stage implementation
- SHA-256 image deduplication (prevents reprocessing same receipt)
- Semantic validation of parsed response before accepting
- Automatic fallback to higher-capability model on parse failure
- Post-processing: discount detection, tax distribution, tax reconciliation
- Image uploaded to DigitalOcean Spaces via presigned URL
- ReceiptTask model tracks state: PENDING → PROCESSING → VALIDATING → RETRYING → COMPLETED/FAILED
- Tracks per-provider token counts and API costs in production

### Balance System (Systems Design)
- StoredGroupBalance: pre-computed pairwise balances for O(1) reads
- Incremental updates within transactions (no full recompute on each change)
- Periodic reconciliation with auto-correction on discrepancy
- Zero-sum invariant enforced (sum of all balances in a group = 0)
- BalanceUpdateLog + BalanceValidationSnapshot for full audit trail
- Eliminates expensive on-read debt computation at scale

### MCP Server
- Full Model Context Protocol implementation (auth 2.1)
- Enables AI assistants (Claude, etc.) to: create bills, create settlements, get balances, query expenses, search bills, get group details, resolve participants, upload receipts
- Same backend as the web app — shared auth and data

### PWA & Mobile
- Full PWA: service worker, VAPID push notifications, Share Target API
- iOS Safari compatibility (safe areas, session management, auto-zoom fixes)
- Swipe gestures for navigation
- Cookie-based JWT with cross-subdomain sharing via .trezzit.com

### Auth Architecture
- HTTP-only cookie JWT with automatic token refresh
- Failed-request queuing and replay on token refresh
- Google OAuth via django-allauth
- Email OTP for passwordless login
- Rate limiting: 100/hr anonymous, 10,000/hr authenticated

### Product Features (for product/startup roles)
- Item-level bill splitting — 5 split types (EQUAL, PERCENTAGE, EXACT, SHARES, ADJUSTED)
- Multi-currency support (currency locked per group)
- Placeholder users (add friends without accounts, claimed on signup)
- Splitwise import
- Debt network visualization via react-force-graph
- GSAP-animated landing page with interactive receipt demo and split UI demo
- Pricing: Student Plan ($0/forever), Free tier, Pro ($5/mo)

### Observability & DevOps
- LLMAPICall model tracks all AI calls (tokens, response times, costs per provider)
- APICallLog + APIPerformanceMetric: p95 latency, error rates per endpoint
- prod→staging DB sync via GitHub Actions
- Encrypted DB backups to DigitalOcean Spaces
- Optimistic locking on bills (version field prevents concurrent edit conflicts)
- Edit lock system: acquire/release before editing

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...              | Highlight / swap in...                                                                                   |
|----------------------------------|----------------------------------------------------------------------------------------------------------|
| AI / LLM engineering             | Lead bullet 2 with AI pipeline — "60% → 95%+" accuracy, 4-provider abstraction, token cost monitoring   |
| Full-stack / SWE                 | Emphasize 995+ tests, 40 models, O(1) balance system, GitHub Actions, prod/staging setup                 |
| Backend / Django                 | 40 DB models, 60+ endpoints, Celery, Redis, PostgreSQL, cookie JWT, optimistic locking, rate limiting    |
| Frontend / React                 | 341 components, 14 contexts, PWA, VAPID push, Share Target, GSAP, React Router v7, no Redux              |
| Infrastructure / DevOps          | DigitalOcean VPS + AWS Lightsail staging, systemd 4 services, Gunicorn + Nginx, GitHub Actions DB sync   |
| Product / startup                | 600+ users, 12+ months solo, item-level splitting, multi-currency, GSAP landing page, pricing tiers      |
| AI agents / MCP                  | MCP server (auth 2.1) — create bills, query expenses, get balances via AI assistant                      |
| Systems design                   | O(1) stored balance system, zero-sum invariant, incremental updates, periodic reconciliation              |
| Observability / monitoring       | Per-provider LLM cost tracking, p95 latency per endpoint, balance system alerts, encrypted backups       |
| Auth / security                  | Cookie JWT with auto-refresh + request queuing, Google OAuth, OTP, rate limiting, optimistic locking     |

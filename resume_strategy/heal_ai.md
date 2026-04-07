# HEAL.AI — Resume Strategy

---

## ✅ SELECTED BULLET (Current Best — 1 Bullet)

> **Won Devlabs Hackathon** with HEAL.AI, an AI healthcare billing assistant; built RAG pipeline — PDF chunking and document search over uploaded insurance policies — enabling natural language Q&A, billing overcharge detection, and automated dispute email generation via Gemini 2.5; FastAPI + Next.js + TypeScript, Dockerized.

---

## 📌 POSITIONING NOTES

- 1 bullet only — space is allocated to Trezzit (3) and SiliconCrew (1-2)
- Lead with the win — it's the hook
- "RAG pipeline" and "PDF chunking" are intentional — recognized ATS keywords, plain English to a first-time reader
- Do NOT say "from scratch" — filler overused by junior devs, implementation detail speaks for itself
- Do NOT use lines of code as a metric — not a quality signal
- Don't spell out RAG (Retrieval-Augmented Generation) inline — adds length without clarity for AI roles
- The product outcome (billing overcharge detection, dispute emails) is more important than the AI internals for most roles
- For AI/LLM-specific roles, swap in more technical depth from the context pool below

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### Hackathon Results
- Won 1st place at Devlabs Hackathon with BillBusters (original version, team project)
- Rebuilt as HEAL.AI solo, placed 2nd at the subsequent Devlabs Hackathon
- Two consecutive hackathon placements: 1st + 2nd — shows iteration under competition pressure

### The Problem
- 80% of medical bills contain errors
- 67% of students avoid care due to cost confusion
- Patients can't understand coverage, identify overcharges, or dispute billing

### What It Does
- Parses insurance documents into plain English
- Detects medical billing errors against policy coverage
- Generates FDCPA-compliant dispute emails automatically
- RAG-powered natural language Q&A over uploaded insurance policy documents
- Emergency QR codes for critical medical info
- Persistent conversational AI chatbot with session history
- Semantic search across policy documents with confidence scoring

### AI / RAG Pipeline
- RAG pipeline built without third-party vector DB (replaced Supermemory with custom implementation)
- PDF chunking with 2-sentence overlap for context preservation
- Google text-embedding-004 (768-dim) vector embeddings
- Cosine similarity retrieval with confidence scoring
- Multimodal AI analysis — simultaneous image + text processing via Gemini 2.5 Flash and Pro
- Intelligent document chunking with NLTK, PyMuPDF for PDF extraction, pytesseract for OCR

### Stack
- **Frontend:** React 18, TypeScript, Vite, Tailwind CSS, shadcn/ui (50+ components), React Router, TanStack Query
- **Backend:** FastAPI, Python 3.11+, Google Gemini 2.5 (Flash + Pro), SQLite
- **AI:** Custom RAG pipeline, Google text-embedding-004, Gemini 2.5 multimodal
- **Infrastructure:** Docker, Docker Compose, Railway and Render deployment configs

### Scale
- Backend grew to significant size across AI flows, RAG pipeline, services, and tests
- 41 total commits across both versions (11 BillBusters + 30 HEAL.AI)
- Public repo: github.com/naman-ranka/HEAL_AI

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...          | Highlight / swap in...                                                                          |
|------------------------------|-------------------------------------------------------------------------------------------------|
| AI / LLM engineering         | RAG pipeline internals — PDF chunking, Google embeddings, cosine similarity, confidence scoring |
| Healthcare / domain          | 80% of bills have errors, FDCPA-compliant dispute generation, insurance document parsing         |
| Hackathon / fast shipping    | 1st + 2nd at consecutive Devlabs Hackathons, built and iterated under competition pressure      |
| Full-stack                   | FastAPI + React + TypeScript + Docker full-stack ownership                                      |
| Multimodal AI                | Simultaneous image + text analysis via Gemini 2.5                                               |
| Open source                  | Public repo: github.com/naman-ranka/HEAL_AI                                                     |
| Two wins (if space allows)   | "Won 1st place then placed 2nd at consecutive Devlabs Hackathons building HEAL.AI..."           |

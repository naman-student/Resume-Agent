# Order Management System — Resume Strategy

---

## ✅ SELECTED BULLETS (Current Best — 2 Bullet Version)

> Engineered a production Django platform (PostgreSQL + Celery + Nginx on DigitalOcean) processing **18,000+ orders over 3 years**; built 3 role-based portals (admin, artisan, customer) with multi-method auth (password, WhatsApp OTP, passwordless Celery-expiry session tokens) — automated PDF invoice generation and WhatsApp Business API delivery on every state transition, eliminating ~20 min of manual relay per order.

> Reverse-engineered third-party Jwelly ERP (**zero public API**) through direct SQL schema analysis; built bidirectional bridge model syncing production weights and ERP status in real time; engineered inbound WhatsApp state-machine chatbot (JSON state per user, admin + customer flows) — full accountability loop across all three portals without disrupting legacy system.

---

## 🔁 BACKUP — 1 Bullet Version (use when space is tight)

> Reverse-engineered Jwelly ERP (zero public API) via direct SQL schema analysis to build bidirectional order sync; deployed full Django platform (PostgreSQL + Celery + Nginx on DigitalOcean) processing **18,000+ orders over 3 years** across 3 role-based portals with WhatsApp Business API automation — eliminating ~20 min of manual relay per order.

---

## 📌 POSITIONING NOTES

- This project and the NCR GOLD Work Experience entry describe the same system — differentiate by keeping Work Exp focused on the employer/role context and this entry focused on what was engineered
- No public GitHub link or live demo exists (all repos private) — compensate with scale metrics and specificity
- Zero AI component — this project earns its space as a **production engineering depth signal**, not an AI signal. Trezzit covers AI; this covers real-world backend complexity and business automation
- ERP reverse-engineering is the single most unique bullet on the entire resume — no competing candidate likely has it; always keep it
- If applying to AI-first roles where space is at premium, use 1-bullet backup version
- If applying to full-stack / backend-heavy roles, use 2-bullet version

---

## 🧠 FULL CONTEXT POOL (for JD-based edits)

### Scale & Impact
- 18,000+ orders processed over 3 years (actively deployed since early 2023)
- ~20 minutes of manual relay eliminated per order lifecycle (notifications, PDF delivery, status updates were all manual before)
- 5-person operations team workflow fully automated
- 6 Django apps, ~15 models, 26+ URL endpoints
- Order model has ~30 fields, 6 file fields, 2 parallel status enums, 4 production stages

### Stack
- Backend: Django, Python, PostgreSQL, Celery, Gunicorn, Nginx
- Infrastructure: DigitalOcean VPS (Linux server)
- Messaging: Gupshup WhatsApp Business API
- PDF: ReportLab (custom AdvancedCustomPDF class)
- Analytics: Plotly (orders-by-month, orders-by-status, disk usage, top tables)
- Auth: Django sessions, SimpleJWT-adjacent patterns, Celery-expiry tokens

### Architecture
- 3 role-based portals: Office Admin, Karigar (Artisan), Customer — each with different auth and capabilities
- Multi-method auth: username/password (admin), WhatsApp OTP (karigars), passwordless 2-hour session tokens via Celery expiry (customers)
- Dual status system: Internal (UNASSIGNED → ASSIGNED → ENTRY_DONE → ARCHIVED) + ERP (TO_KARIGAR → IN_STOCK → SOLD → SETTLED) tracked simultaneously
- Production stage tracking: NOT_STARTED → IN_PROGRESS → FINISHING → COMPLETED

### ERP Reverse-Engineering (Key Differentiator)
- Third-party Jwelly ERP had zero public API
- Discovered schema through direct database access and SQL analysis
- Built Jwelly1 OneToOne bridge model mapping ERP records to internal Orders
- Bidirectional sync: reads production weights and order status from ERP, writes new orders back into ERP
- Management commands: update_karigars, update_customer, jwelly_orders, auto_update
- Enabled real-time order visibility while fully preserving legacy system coexistence

### WhatsApp Integration
- 7 outbound template message types (order confirmation, karigar assignment, cancellation, OTP, in-stock notification, rejection, unassignment) — all with PDF attachments via Gupshup hosted media URLs
- Inbound state-machine chatbot: customer flow (order status / login / add order) + admin flow (karigar list / order info / help)
- JSON state stored per phone number in TextField, auto-resets after 3 hours of inactivity
- Debug mode redirects all messages to test number (safe for dev/staging)

### PDF Generation
- Custom ReportLab class (AdvancedCustomPDF): two formats — Customer PDF (full details) and Karigar PDF (excludes customer contact info)
- Auto-generated on order create, assign, and edit
- Sent as WhatsApp file attachments automatically
- A4 layout with company logo, order ID, date header, auto-scaled images

### Business Context
- Built for family wholesale jewelry business (NCR GOLD)
- Replaced fully paper-based workflow: orders in physical books, manual artisan communication, manual customer updates
- Coexisted with legacy Jwelly ERP throughout — no rip-and-replace, additive integration
- Attempted SaaS productization with white-labeling and DB-driven config (AppConfig singleton) — not pursued commercially

### Engineering Patterns (useful for technical interviews)
- Fat Model pattern: save_and_process(), save_and_assign(), save_and_unassign() encapsulate PDF + WhatsApp as model methods
- Custom QuerySet managers: active(), all_orders(), current_orders(), new_orders(), completed_orders()
- Configurable table columns persisted in Django session
- Single OrderListView serving 5+ filtered views via config dict
- Soft-delete with ActiveObjectsManager across all entity models
- Guard methods: can_edit(), can_delete(), can_assign(), can_unassign(), can_in_stock(), can_sold()

---

## 🎯 JD-BASED SWAP GUIDE

| If JD emphasizes...         | Highlight / swap in...                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Backend / Django depth      | 6 apps, ~15 models, dual status system, fat model pattern, custom QuerySet managers   |
| Systems integration         | ERP reverse-engineering story, bidirectional sync, zero public API                    |
| Automation / workflow       | 20 min saved, full order lifecycle automation, PDF + WhatsApp on every state change   |
| Messaging / comms infra     | 7 WhatsApp template types, inbound chatbot state machine, Gupshup API                 |
| Auth / security             | 3 auth methods across portals, Celery-expiry session tokens, WhatsApp OTP             |
| Infrastructure / DevOps     | Gunicorn + Nginx + PostgreSQL + Celery on DigitalOcean VPS, systemd-style management  |
| Analytics / data            | Plotly dashboard, orders-by-month, top customers/karigars/items by volume             |
| Scale / production          | 18,000+ orders, 3 years live, 5-person ops team, zero downtime migration from PHP     |
| Legacy system integration   | Jwelly ERP coexistence, bidirectional bridge, no legacy disruption                    |

# 04 — Risks & Mitigation

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Source**: cross-referenced across all `cyberk-research/*` docs.

| # | Risk | Impact | Mitigation | Owner |
|---|---|---|---|---|
| R1 | **ASR reliability on Singlish / Mandarin code-switch** — the single biggest design risk. No general-purpose provider handles it well; a mangled transcript silently degrades qualification, extraction, and can trigger false transfers. | High | Two **single-language agents** (English-SG, Mandarin) chosen per call; aggressive **confirm-back** of every critical field; easy human escape. Singlish/Hokkien fluency is **not promised** in MVP. Human-eval ship gate catches capture failures before pilot. | Cyberk (design) |
| R2 | **Latency from Singapore** on US-hosted Retell — no documented APAC media region; expect a US network penalty. | Medium | Plan for **~800–1,200ms p95** (never market 280ms); **measure on real +65 calls** in week 8; hold **LiveKit SG self-host** as a documented post-MVP lever if unacceptable. | Cyberk (Tech Lead) |
| R3 | **Regulatory boundary (MAS / CEA / PDPA)** — if the AI drifts into advice/recommendation/negotiation, the licensed human bears the consequence. | High | AI configured as **introducer / administrative assistant**; **structural** green-list/red-list guardrail + hard advice→transfer edge + post-call compliance flag; disclosure at call open. **Client engages SG counsel to sign off scripts before go-live.** | Shared (Cyberk builds, client's counsel signs off) |
| R4 | **Google OAuth verification delay** — approval time is outside our control and gates external calendar users. | Medium | **Submit in week 1**; testing mode covers a small pilot cohort; **Cal.com fallback** (already Google-verified, native Retell function) ready. | Cyberk |
| R5 | **Telnyx account-approval friction** — the "AI-agent evaluation" gate blocks/suspends new accounts. | Medium | **Prototype on Twilio** (self-serve, verified +65 pricing) so the build is never blocked; migrate to Telnyx when approved; **didlogic** as a signup-friendly parallel fallback. | Shared (client account, Cyberk integrates) |
| R6 | **Retell AMD false-positives on +65 mobiles** — a real prospect classified as a machine gets hung up on. | Medium | Default **hang-up on voicemail** (cheapest, PDPA-clean); tune detection window; **test against real +65 greetings** (Singtel/StarHub/M1/MVNO); log false pos/neg from recordings. | Cyberk |
| R7 | **$79 tier margin trap** — uncapped, an active agent's minutes invert the tier's economics. | Medium | Ship **every tier with a minute cap** enforced in-app + **$0.40/min overage**; never sell $79 uncapped. A product-design guardrail, built into billing. | Cyberk (billing) |
| R8 | **Anti-spoofing / caller-ID** — presenting the agent's mobile is illegal spoofing; telcos block falsified +65 CLI. | High | **One dedicated +65 number per tenant** as CLI; agent mobile is transfer-target only. Enforced architecturally. | Cyberk |
| R9 | **Scope creep** — new features enter uncontrolled and blow the fixed budget/timeline. | Medium | Change control — only approved changes enter scope; sign-off required on new requests. Clear In-/Out-of-Scope in `01`. | Shared |
| R10 | **Requirement misinterpretation** — solo-founder context, phone-first nuance. | Medium | **Minimum twice-weekly demos** so the client reviews progress and corrects early. | Cyberk (PM) |
| R11 | **Booking `book_appointment` validation friction / double-booking.** | Low-Med | DB as source of truth (deterministic event ID + unique constraint); qualify-then-book; synchronous booking with hard timeout; **custom-webhook fallback**. | Cyberk |

## The two brief errors as risks

Both are raised in `00-client-needs.md` and must be confirmed with the client early:
**Q19 (280ms)** and **Q20 (no legal requirements)** are incorrect. Building on either
assumption would misdesign the product; the proposal corrects both up front.

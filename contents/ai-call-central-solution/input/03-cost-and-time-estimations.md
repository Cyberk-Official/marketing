# 03 — Cost & Time Estimation

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Model**: Project-Based, fixed price. Aligned to the client's ~US$20K / ~2-month envelope (Q15/Q16).
> **v1.2**: Fixed price now buys a **guaranteed Week-8 baseline** (Section 4 of the proposal); Phase 1.1 items (Mandarin, automated metered billing, agency multi-seat, Telnyx migration) are quoted separately. Payment is **decoupled from the compliance/accuracy evaluation** — that is a go-live readiness gate, not a payment condition.

## Total cost: US$20,000 (guaranteed baseline)

| Line item | Basis | Amount |
|---|---|---|
| Engineering | 3 engineers × US$3,000 / engineer / month × 2 months | **US$18,000** |
| Project management & UX/UI design | Part-time PM + designer across the engagement | **US$2,000** |
| **Total (fixed)** | | **US$20,000** |

**Not included (client operating costs, pass-through on the client's own accounts):**
per-minute telephony + Retell voice-engine + LLM usage, Polar billing fees, Neon /
Cloudflare / Railway hosting, SG number rentals, and any legal/tax counsel. These are
recurring COGS, not part of this one-time build fee. **Phase 1.1 items are quoted separately.**

## Timeline: 8 weeks (~2 months)

Starts once requirements are locked and the client accounts + SG entity documents are
available. Week 1 kicks off the long-lead dependencies (calendar OAuth, Telnyx account for
later, +65 provisioning) in parallel with a **voice/latency go/no-go spike on real +65
calls** — so latency, English capture, transfer success, and AMD behavior are proven in
Week 1–2 rather than discovered in Week 8. UI work is spread across the build. The Week-8
outcome is the **guaranteed baseline** for a first single-seat cohort (assisted onboarding);
Phase 1.1 items are separate.

| Week | Focus | Delivers |
|---|---|---|
| **1** | Setup, spike & long-lead deps | Repo + control-plane skeleton (Workers/Hono), Neon/Drizzle schema, BetterAuth; **+65 voice/latency go/no-go spike**; choose calendar path; submit calendar OAuth; Twilio SIP + Retell wired; +65 provisioning started; dashboard wireframes |
| **2** | Voice spine & intake | Outbound-call trigger (Worker → persistent worker → Retell) from the tenant's +65 number; **lead-ingestion webhook + manual entry + consent evidence**; first live +65 test call; dashboard shell started |
| **3** | Qualification agent | Conversation Flow (English-SG): qualifying nodes, hybrid extraction, structural compliance guardrail + advice→transfer edge |
| **4** | Booking & handoff | The chosen calendar path (DB as source of truth); warm transfer with whisper brief. **Mid-project demo: end-to-end lead-in → call → qualify → book/transfer** |
| **5** | Retry & compliance calling | AMD/voicemail handling (hang-up default), retry scheduler on `disconnection_reason`, consent gate + counsel-approved calling-hours matrix, opt-out, disclosure at call open |
| **6** | Billing & data controls | Per-seat subscription + hard minute quota + hard ceiling/daily limits; recording & data controls (F10, retention + delete/export); dashboard build-out |
| **7** | No-code & onboarding | Fixed-template question-list editor → Conversation Flow; assisted onboarding; hardening; prepare the feature-acceptance matrix |
| **8** | QA, acceptance & pilot readiness | Feature-acceptance testing; the 20–50-call go-live readiness evaluation; latency validation from SG; bug fixing; handover + pilot launch prep |

## Payment milestones

| Milestone | Trigger | % | Amount |
|---|---|---|---|
| Kickoff | Signing / project start | 40% | US$8,000 |
| Mid-project | End of week 4 — end-to-end lead-in → call → qualify → book/transfer demo | 30% | US$6,000 |
| Delivery | End of week 8 — acceptance of the **feature-acceptance matrix** (Section 4 baseline). Client raises reproducible defects in writing within 5 business days; otherwise deemed accepted. Cyberk remediates in-scope defects and retests. | 30% | US$6,000 |

**Go-live readiness gate (NOT a payment condition):** the 20–50-call evaluation — ≥90%
correct critical-field capture, booking/transfer firing correctly, and the counsel-approved
compliance rubric — is a **launch-readiness decision** run in Week 8. Because it depends on
third-party ASR/AMD behavior and the client's counsel-owned scripts (excluded from warranty),
it does not gate the delivery payment. One remediation-and-retest cycle is included.

## Notes on the estimate

- The **<1-minute callback SLA** is trigger latency (lead arrival → outbound-call API),
  **within permitted calling hours** — not per-turn voice latency.
- The estimate assumes **Retell + BYO SIP** (Twilio for the pilot), not a custom pipeline;
  a custom voice pipeline would not fit this budget or timeline and is out of scope.
- The **compliance guardrail is built**; final legal sign-off of the scripts + calling-hours
  matrix + compliance rubric is the client's counsel (an assumption, not a cost line here).
- Buffer is carried inside the week-8 QA/hardening window; the long-lead external approvals
  (calendar OAuth, Telnyx) are the main schedule risk and are de-risked by starting them in
  week 1 and keeping Cal.com / Twilio fallbacks.
- **Scope split** keeps the fixed $20k deliverable: Mandarin, automated metered overage
  billing, agency multi-seat, and Telnyx migration are Phase 1.1, quoted separately.

# 01 — Scope of Work

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Source**: Q11/Q12 brief + `cyberk-research/*`. Every in-scope item traces to a client pain point.
> **v1.2**: Scope split into a **guaranteed Week-8 baseline** (fixed $20k) and a **priced Phase 1.1** (quoted separately). Lead-ingestion webhook pulled into the baseline; Mandarin, automated metered billing, and agency multi-seat moved to Phase 1.1.

## In-Scope — Guaranteed Week-8 Baseline (fixed US$20,000)

| # | Feature | Traces to | What it means |
|---|---|---|---|
| F1 | **Lead intake (two paths) + consent capture** | Q11, PDPA | (a) A generic **authenticated lead-ingestion webhook/API**, plus (b) manual entry. Each lead stores source ID, mobile, **preferred language**, and **consent evidence** (consent wording/version, timestamp, source, attesting user) as the legal basis for the callback. |
| F2 | **Sub-minute automated callback** | Q11 (core loop), Q18 | On lead arrival (webhook or manual), the platform places an outbound call from the tenant's dedicated +65 number within the first minute — **when permitted under the consent + calling-hours policy (F14)**; out-of-window leads queue to the next permitted window. |
| F3 | **AI qualification call (English-SG)** | Q11 | Retell Conversation Flow agent qualifies the lead on the call (intent, timeline, budget range, authority, etc.) and confirms captured data back to the caller. |
| F4 | **Compliance-safe conversation** | Q5, Q20 | AI acts as an introducer (insurance) / administrative assistant (property): factual info + qualify + book + hand off only. Structural green-list/red-list guardrail; advice-seeking question → hard-coded transfer; post-call compliance flag. |
| F5 | **Calendar booking (one path)** | Q11 | Qualify → check availability → offer 2–3 slots → confirm → book. **One production calendar path — Google Calendar or Cal.com, chosen Week 1.** The app DB is the source of truth for slot uniqueness. |
| F6 | **Warm human handoff** | Q11 | Live warm transfer to the tenant's single transfer mobile on a hot lead, explicit request, or an advice question, with a whisper brief (name, vertical, intent, timeline, temperature). |
| F7 | **Retry on no-answer** | Q11 | AMD (Retell voicemail detection): hang up on voicemail, retry with backoff within legal calling hours, capped at 2–3 attempts, stop on pickup/opt-out. **After the cap, the lead is marked unreachable and surfaced for manual follow-up** (SMS/voicemail out of scope). |
| F8 | **One shared lead record** | Q11 | A single record per lead: transcript, recording, extracted fields, call outcome, appointment. |
| F9 | **No-code setup** | Q11 | **Fixed-template question-list editor**: edit the questions + extraction fields on the pre-built "Insurance qualifier" / "Property qualifier" templates, which compile into Conversation Flow nodes + a post-call extraction schema. Arbitrary flow authoring is Phase 1.1. |
| F10 | **Recording & data controls** | PDPA | Recordings + transcripts tenant-isolated and access-restricted to the tenant's authorized user; stored in a defined store with a **configurable default retention period**; deletable/exportable on request, subject to operational/legal limits. |
| F11 | **Single-seat multi-tenant foundation** | Q8, "MVP w/ full functionality" | Tenant isolation with **one user/seat, one dedicated +65 number, one transfer mobile, and one calendar per tenant** (anti-spoofing). Assisted/manual number provisioning, release on churn. Defined pilot caps (tenants, monthly minutes, concurrency). |
| F12 | **Per-seat billing + hard usage controls** | Q8, Q9 | Per-seat subscription with an **included-minutes allowance enforced as a hard in-app quota** (new calls blocked at the cap), a **configurable hard monthly ceiling + daily dial limits**, usage metered from the platform's own call records. Above-allowance usage is invoiced manually for the pilot; automated metered overage is Phase 1.1. |
| F13 | **Agent dashboard (web / mobile web)** | Q14 | Lead list & record, transcripts, call outcomes, calendar view, agent settings, onboarding. |
| F14 | **Compliance calling layer** | Q20 | Documented consent gate, a **counsel-approved configurable calling-hours matrix** (weekday / Saturday / Sunday / public-holiday + explicit-consent overrides), AI-identity + recording disclosure at call open, instant opt-out, capped retries. **Blocks non-consented calls; no DNC-register lookup.** |

## Phase 1.1 — Built and quoted separately (NOT in the $20k baseline)

| Item | Note |
|---|---|
| Mandarin second-language agent + per-call language routing | Baseline is English-SG; `preferred_language` captured at intake so Mandarin plugs in later |
| Automated metered overage billing (Polar metered $0.40/min, self-serve) | Baseline uses a hard quota + manual overage invoicing |
| Agency / multi-seat tenants (pooled seats, multiple numbers, lead/calendar routing, RBAC) | Baseline is single-seat per tenant |
| Telnyx production carrier migration | Baseline runs on Twilio (didlogic fallback) |
| Deeper no-code flow authoring (beyond the fixed-template editor) | Baseline edits preset templates only |

## Out-of-Scope (excluded entirely)

| Item | Why | Reference |
|---|---|---|
| **Inbound call answering / receptionist workflows** (incl. IVR, missed-call capture, routing) | MVP is outbound-callback-only | Scope decision |
| SMS / text fallback when a call doesn't connect | Deferred | Q12 |
| Deeper CRM integrations (Salesforce, HubSpot) | Deferred | Q12 |
| Call-quality scoring / conversation analytics | Deferred | Q12 |
| Multi-agent routing | Deferred | Q12 |
| Cold outbound to non-consented contacts; DNC-register lookup | PDPA — MVP calls only consented leads | Q12, regulatory |
| Custom voice pipeline / custom ASR (self-host MERaLiON) | Build on Retell; not MVP effort | Voice/conversation research |
| Guaranteed Singlish / Hokkien fluency | ASR-degraded path; designed for graceful failure, not promised | Conversation research |
| Fully-polished self-serve onboarding / number provisioning | MVP is lean/assisted | Problem & scope |
| Native mobile apps (iOS/Android) | Product is web / mobile-web | Q14 |
| Legal counsel, SG entity incorporation, telephony account KYC | Client responsibility | Assumptions |
| LiveKit self-host voice migration | Scale-stage lever, not MVP | Voice research |
| Unit tests | Testing focuses on functional + integration | Cyberk default |

## Platform

Web / mobile-web agent dashboard. The **lead call channel is the PSTN phone network**
(the AI places real outbound calls to +65 mobiles, **outbound-only**) — not a browser
widget and not an inbound receptionist. The Week-8 outcome is a **pilot-grade MVP** for a
first cohort of single-seat tenants (assisted onboarding), not a fully-polished self-serve
launch.

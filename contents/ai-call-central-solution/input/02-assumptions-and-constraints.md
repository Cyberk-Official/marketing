# 02 — Assumptions & Constraints

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Source**: `cyberk-research/*` (telephony, regulatory, tech-stack, billing)

## Assumptions

### Client-provided (must be in place before or at kickoff)

1. **Singapore Pte Ltd is available** — UEN, authorized-representative government ID, and
   a Singapore proof of address (<3 months, no P.O. Box / virtual address). This is
   required to provision +65 numbers; an individual foreign founder alone cannot.
   *Consequence: if not ready at kickoff, project start shifts day-for-day.*
2. **Client engages Singapore-qualified legal counsel** to review the insurance script
   (MAS FAR reg 31 / Notice FAA-N02) and the property script (CEA EAA s3–s4), and to
   confirm the SBO (telecom) licence question, **before go-live**. Cyberk builds the
   compliance guardrail per the research green-list/red-list; final legal sign-off is the
   client's. *Consequence: production go-live is blocked until sign-off; Cyberk still
   delivers the staging/testing build in the meantime.*
3. **Client provides all third-party accounts** before the relevant build phase: Retell,
   telephony (Twilio for prototype, Telnyx for production), Cloudflare, Neon, Polar,
   Google Cloud (for the calendar OAuth). Cyberk configures and integrates; the client
   owns the accounts and their billing. *Consequence: if an account/API key is not
   available when its workstream begins, that workstream pauses and the affected milestone
   dates shift.*
4. **Client funds third-party usage** — per-minute telephony/voice, LLM, and billing
   platform fees are pass-through operating costs on the client's accounts, separate from
   this build fee.
5. **Client availability** — the founder (sole point of contact) is available for
   demos at least twice per week to review progress and clarify requirements promptly.
   *Consequence: open decisions left unanswered beyond one review cycle (2 business days)
   are treated as accepted so the timeline can hold, or the timeline shifts day-for-day.*

### Product / technical

6. **MVP with full functionality** — the multi-tenant SaaS architecture is real from day
   one, but onboarding, billing, and number provisioning are **lean/assisted**, not
   fully-polished self-serve.
7. **Calendar = Google Calendar** for MVP; the app DB is the source of truth for slot
   uniqueness/holds. **Google OAuth verification is submitted in week 1** (approval time
   is outside Cyberk's control); testing mode suffices for a small pilot cohort;
   **Cal.com is the ready fallback**. *Consequence: if Google's review is slow, the pilot
   proceeds in testing mode or on Cal.com; a later migration to Google production is
   scheduled separately.*
8. **Voice platform = Retell AI + bring-your-own SIP trunk.** No custom voice pipeline.
9. **Language = English-SG + Mandarin single-language agents, chosen per call.**
   Singlish/Hokkien is a known-degraded path designed for graceful failure (confirm-back
   + human escape), **not a promised fluency**.
10. **Requirements are stable** for the ~2-month cycle; no major structural change during
    development. New features follow change control.
11. **Testing scope** — functional + integration testing. Dashboard verified on latest
    Chrome (desktop) + latest iOS Safari; the voice loop is validated on **real +65
    mobiles**. **Unit tests are not in scope.**

## Constraints

1. **Time** — the ~2-month (8-week) estimate starts once requirements are locked and the
   client accounts + SG entity docs above are available.
2. **Latency reality** — plan for **~800–1,200ms p95** voice-to-voice, validated
   empirically from Singapore. The client's "280ms" figure (Q19) is not achievable for
   this deployment and will not be marketed. No major managed platform documents an
   APAC/Singapore media region; a US-region network penalty is expected.
3. **Regulatory boundary** — the AI is confined to **factual info + qualify + book + hand
   off**; it must never advise, recommend, compare-and-steer, quote as advice, or (property)
   negotiate. This is a hard product constraint, not a tunable.
4. **Anti-spoofing** — the platform **must** present its own dedicated +65 number per
   tenant; presenting the agent's mobile as caller ID is illegal spoofing in Singapore.
   The agent's mobile is used only as the warm-transfer destination.
5. **Vendor onboarding friction** — Telnyx blocks/suspends new accounts at signup
   ("AI-agent evaluation" gate); production migration to Telnyx depends on that approval,
   which is outside Cyberk's control. The build de-risks this by prototyping on Twilio.
   *Consequence: the pilot runs on Twilio (didlogic fallback); migrating production
   traffic to Telnyx after the engagement window is a separate change request.*
6. **Minute-cap enforcement** — Polar does not auto-block usage at the cap; minute quotas
   must be enforced in-app, since each overage minute is real money on the client's
   Retell/telephony accounts.

## What Cyberk explicitly does NOT warrant

- Legal/regulatory compliance sign-off (client's counsel).
- Third-party account approval timelines (Google OAuth review, Telnyx AI-agent gate).
- Realized ASR accuracy on heavy Singlish/Hokkien, or realized SG lead connect rate
  (assumed ~30%) — both require in-market measurement during the pilot.

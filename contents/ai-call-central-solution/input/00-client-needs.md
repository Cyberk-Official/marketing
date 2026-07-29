# 00 — Client Needs

> **Project**: AI Telemarketing — Phone Voice Agent for Singapore Insurance & Property Agents
> **Date**: 2026-07-22
> **Source**: `input/input.txt` (20-question client brief) + `cyberk-research/*`

## The core problem

When a lead comes in, whoever calls back first usually wins it. Agents who respond
within 5 minutes are ~21× more likely to qualify a real-estate lead than at 30 minutes,
and insurance sees a ~9× lift. Individual agents and small agencies cannot personally
hit that window on every lead — not at night, not on weekends, and not at the exact
minute a lead lands. By one estimate ~71% of internet leads are wasted on poor
follow-up alone.

**Root cause (not the symptom):** the problem is not "agents are slow"; it is that a
human cannot be available in the first 60 seconds, 24/7, for every lead. The fix has to
be an always-on system that acts in seconds, in the lead's language, and books the
meeting before the lead cools — then hands a warm, qualified lead back to the human.

## Who is struggling

| Buyer | Notes |
|---|---|
| Individual insurance agents & small agencies | MAS-appointed FA representatives; speed-to-lead is a measured lever |
| Individual property / real-estate agents & small agencies | CEA-registered salespersons |
| Small B2B sales teams | Same speed-to-lead economics |

**First market: Singapore (confirmed).** This shapes both what the AI is legally
allowed to say (MAS/CEA licensing) and how outbound calling is done (PDPA Do-Not-Call,
calling hours, anti-spoofing).

## What the client wants (their words)

An AI phone agent that calls or answers within moments of a lead coming in instead of
hours later. It qualifies the lead on the call, books the appointment straight into the
calendar, follows up automatically if nobody picks up, and logs everything to one
record. Sold as a monthly subscription, per agent/seat, at ~US$79–300/month, self-serve,
priced for a single agent rather than a brokerage-wide sale.

## Differentiation (the sharp angle)

Generic voice tech is commoditizing — the client should **not** build voice
infrastructure; they should build on a proven platform and win on packaging and
distribution. The durable moat is **Singapore-native execution**: +65 numbers, PDPA
compliance, MAS/CEA-safe scripting, and English/Mandarin (Singlish-aware) support,
serving insurance **and** property agents together in one product priced for the
individual. Copyable features; hard-to-copy localization.

## Hidden expectations & things the client under-specified

1. **"Web / mobile web app" (Q14) is the agent's dashboard, not the call channel.** The
   demo was an in-browser voice PoC; the client confirmed the product is a **real phone
   system** (the AI dials/answers real phone numbers). The web/mobile-web surface is the
   agent's management UI.
2. **Lead intake = the agent enters the lead** (name + mobile + consent). No
   portal/webhook/Facebook-Ads integration is needed for MVP. This entry point is also
   where **consent + timestamp** are captured (a PDPA/DNC requirement).
3. **"MVP with full functionality"** = the multi-tenant SaaS architecture is real from
   day one, but onboarding, billing, and number provisioning can be lean/assisted rather
   than fully-polished self-serve.

## ⚠️ Two errors in the client brief (must be surfaced to the client)

- **Q19 — "~280ms end-to-end latency."** False for this deployment. 280ms is a
  single-component metric, not real voice-to-voice latency. Production phone-agent
  latency runs **~600–1,500ms**; plan for ~800–1,200ms p95 and never market "280ms." The
  client's *conclusion* — "build on proven voice infrastructure, not a custom pipeline"
  — is correct.
- **Q20 — "no legal requirements I'm aware of."** False. The client themselves flagged
  MAS (insurance) and CEA (property) licensing in Q5. A phone product also adds PDPA
  Do-Not-Call, calling-hours, and anti-spoofing/caller-ID rules. These materially shape
  what the AI may say and how calls are made.

## Success definition (client, Q18)

Nearly every lead called back inside the target window; a measurable lift in
qualified-lead rate for the agents using it; and month-over-month retention (the metric
that matters most). A good 6-month story: agents converting meaningfully more of the
same leads they already pay for.

## Success gate we will build toward

An MVP that reliably runs the **call → qualify → book → transfer/retry** loop on real
+65 mobiles, passes a human-eval ship gate (n=20–50 calls: ≥90% correct field capture,
100% MAS/CEA compliance, booking/transfer fires correctly), and is ready for a first
cohort of pilot agents within ~2 months.

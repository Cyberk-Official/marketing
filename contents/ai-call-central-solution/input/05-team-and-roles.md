# 05 — Team & Roles

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Model**: Project-Based, fixed-price. Team sized to the ~$20K / 2-month envelope.

## Team composition

**3 full-time engineers** for 2 months, plus **part-time project management and UX/UI
design** (covered by the management & design allocation). This is a TypeScript-heavy
build (Cloudflare Workers + Hono, Retell integration, telephony, billing) with a hard
compliance boundary, so seniority is weighted toward one lead who owns the voice/telephony
spine.

| Role | Allocation | Primary focus |
|---|---|---|
| Senior Fullstack Engineer (Tech Lead) | Full-time | Architecture, Retell + BYO-SIP voice integration, telephony/number provisioning, warm transfer, latency validation |
| Fullstack Engineer | Full-time | Control plane (Workers/Hono), lead intake + consent, calendar booking, agent dashboard |
| Fullstack Engineer / QA | Full-time | Conversation Flow build, compliance guardrail, billing (Polar), retry/AMD scheduler, human-eval testing |
| Project Manager | Part-time | Planning, twice-weekly demos, risk/dependency tracking, client comms |
| UX/UI Designer | Part-time | Dashboard wireframes → UI, no-code question-builder UX, onboarding flow |

## Role responsibilities

- **Senior Fullstack Engineer (Tech Lead)** — Overall technical ownership. Designs the
  end-to-end call architecture, owns the Retell integration and the persistent Node
  worker (outbound trigger, retry orchestration, warm transfer), provisions the +65
  one-number-per-tenant pattern, and runs empirical latency validation from Singapore.
  Reviews all code and directly builds the most complex components.
- **Fullstack Engineer** — Builds complete features across the control plane and the
  agent-facing dashboard: lead entry + consent capture, calendar availability/booking
  (Google Calendar + DB as source of truth), tenant/seat state, transcripts and lead
  records, and the web/mobile-web UI.
- **Fullstack Engineer / QA** — Builds the Retell Conversation Flow (qualification nodes,
  hybrid extraction, structural compliance guardrail, advice→transfer edge), the
  AMD/retry scheduler and calling-compliance layer, and the Polar seat+overage billing
  with in-app minute-cap enforcement. Owns the human-eval ship gate: listens to the first
  20–50 calls against the compliance + capture rubric and turns every failure into a test
  scenario.
- **Project Manager** — Runs the 8-week plan, keeps the long-lead dependencies moving
  (Google OAuth, Telnyx approval, SG entity docs, legal-review handoff), hosts the
  minimum-twice-weekly demos, and is the client's escalation path.
- **UX/UI Designer** — Produces the dashboard wireframes and UI and the no-code
  question-builder and onboarding experience, consistent with a lean-but-real MVP.

## Why this shape

- **Voice/telephony/compliance risk is concentrated**, so it sits with the Tech Lead
  rather than being spread thin.
- **Bus-factor mitigation:** the Conversation Flow + compliance work (QA engineer) and
  the calendar/dashboard work (Fullstack engineer) are deliberately separated from the
  voice spine so no single component has only one person who understands it.
- **PM + Design are part-time by design** — an MVP dashboard for a phone-first product
  does not need a full-time designer, and a solo-founder client needs coordination, not
  heavy governance. Their cost is the $2K management & design allocation.

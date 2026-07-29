# Memory — AI Telemarketing (Proposal Decision Records)

## PDR-1 — Cost model
- **Context:** Client budget ~US$20K (Q15).
- **Decision:** Fixed US$20,000 = 3 engineers × $3,000/eng/month × 2 months ($18K) + $2K part-time PM & design.
- **Trade-off:** All-$3k/head keeps the build inside the client's stated envelope; seniority weighted to a Tech Lead who owns the voice/telephony spine rather than adding headcount.

## PDR-2 — Phone system, not web widget
- **Context:** Demo was an in-browser voice PoC; brief said "web/mobile web app" (Q14).
- **Decision:** Product is a real PSTN phone system; web/mobile-web is the agent dashboard only.
- **Trade-off:** All web-only economics/architecture superseded; scope built around Retell + BYO SIP.

## PDR-3 — Build on Retell, not custom
- **Decision:** Retell AI orchestration + bring-your-own SIP trunk (Twilio prototype → Telnyx production).
- **Trade-off:** Fits solo-founder/2-month/$20K; custom pipeline rejected. LiveKit self-host held as post-MVP scale lever.

## PDR-4 — Two brief errors corrected up front
- **Decision:** Surface Q19 (280ms latency → real ~800–1,200ms p95) and Q20 (no legal requirements → MAS/CEA/PDPA/anti-spoofing are real) in the proposal.
- **Trade-off:** Better to correct the client's assumptions now than misdesign the product or over-promise.

## PDR-5 — Compliance boundary is a hard product constraint
- **Decision:** AI = introducer (insurance) / administrative assistant (property); factual info + qualify + book + hand off only. Structural guardrail + advice→transfer edge + post-call compliance flag. Client's SG counsel signs off scripts before go-live.

## PDR-6 — Language scope
- **Decision:** English-SG + Mandarin single-language agents chosen per call. Singlish/Hokkien = graceful-degradation path, NOT a promised fluency. Biggest design risk (ASR).

## Reusable pricing format
- Project-based fixed price = (headcount × monthly rate × months) + PM/design allocation. Warranty 30 days → optional $3K/mo support retainer. Milestones 40/30/30 (kickoff / mid-project demo / delivery).

## PDR-7 — Pilot-grade MVP framing (Oracle Round 1)
- **Context:** Oracle flagged that the $20k / 8-week / 3-person scope reads like a polished self-serve SaaS launch.
- **Decision:** Position Week-8 as a **pilot-grade MVP** (assisted onboarding + number provisioning). Pre-agreed deferral candidates if the buffer is consumed: Mandarin agent, deeper no-code authoring, production billing automation.
- **Trade-off:** Keeps the fixed $20k defensible without cutting the feature list.

## PDR-8 — Outbound-callback-only (inbound excluded)
- **Context:** Proposal implied the AI "answers real phone numbers"; the scoped/costed architecture is outbound-only.
- **Decision:** MVP is **outbound-callback-only**; inbound answering / receptionist workflows deferred to a later phase.
- **Trade-off:** Matches the costed architecture and budget; inbound becomes a Phase-2 upsell.

## PDR-9 — Lead-ingestion webhook in the baseline (Critic Round 1)
- **Context:** Critic flagged that "manual entry" contradicted the auto-callback value prop — a human still had to type each lead in.
- **Decision:** Pull a generic **authenticated lead-ingestion webhook/API** into the guaranteed baseline (F1), capturing source ID + preferred_language + auditable consent evidence, alongside manual entry.
- **Trade-off:** Restores the "lead in → sub-minute callback" story; displaced Mandarin + automated billing into Phase 1.1 to hold the $20k.

## PDR-10 — Guaranteed baseline vs priced Phase 1.1 (Critic Round 1)
- **Context:** Critic judged the full feature list not credibly deliverable in 8 weeks at $20k.
- **Decision:** Split scope into a **hard Week-8 baseline** (single-seat, English-SG, one calendar path, core loop + webhook, hard-quota billing) and an explicitly-**priced Phase 1.1** (Mandarin, automated metered overage billing, agency multi-seat, Telnyx migration, deeper no-code authoring).
- **Trade-off:** Makes the fixed price honest and defensible; Phase 1.1 becomes a clean upsell instead of silent scope risk.

## PDR-11 — Payment decoupled from the compliance gate (Critic Round 1)
- **Context:** Prior v1.1 tied the final 30% to a human-eval compliance/accuracy ship-gate that depends on third-party ASR/AMD + client-counsel scripts — an unsafe payment condition.
- **Decision:** Final 30% tied to a **feature-acceptance matrix + deemed-acceptance window** (reproducible defects in writing within 5 business days, else deemed accepted). The 20–50-call compliance/accuracy evaluation becomes a **go-live readiness gate**, not a payment condition.
- **Trade-off:** Cyberk isn't held hostage to vendor accuracy it doesn't control, while the client keeps an objective acceptance test and a real launch-readiness bar.

## Consistency fixes folded into v1.2
- F12 billing = 3 controls: included allowance / hard in-app quota / configurable hard ceiling + daily dial cap (metered overage → Phase 1.1).
- Calling-hours = **counsel-approved configurable matrix** (weekday/Sat/Sun/PH + consent overrides), not hardcoded 08:00–21:00; MVP blocks non-consented calls, **no DNC-register lookup**.
- Compliance guarantees softened → "controls designed to support the client's counsel-approved policy"; Cyberk gives no legal advice / no compliance warranty.
- Voice/latency spike moved to **Week 1–2 with go/no-go thresholds**.
- Pilot constrained to **single-seat**: one user/number/calendar/transfer-mobile per tenant (agency = Phase 1.1).
- Single SOW/MSA pointer line added for IP-assignment / net-14 payment / PDPA data-processing schedule (kept out of the 10-section body for template compliance).
- Hypercare requires go-live within 30 days of acceptance; response target = acknowledged within one business day.

## Oracle Round-1 findings (applied to proposal v1.1)
- <1-min callback SLA applies **only within permitted calling hours**; out-of-window leads queue to the next window.
- Every client/vendor dependency now carries a **consequence clause** (day-for-day shift / blocked go-live / paused workstream).
- **Bug** = delivered in-scope behavior contradicting the signed-off spec; third-party accuracy limits/outages and client script/account changes are NOT warranty bugs.
- Retry-cap **terminal state** = mark lead unreachable + surface for manual follow-up (SMS/voicemail out of scope).
- No-code builder **bounded** to a fixed-template question-list editor (no arbitrary flow authoring).
- Human-eval **ship-gate thresholds** moved into the delivery milestone (objectively verifiable).

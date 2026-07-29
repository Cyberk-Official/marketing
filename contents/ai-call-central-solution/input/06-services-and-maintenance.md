# 06 — Services & Maintenance

> **Project**: AI Telemarketing
> **Date**: 2026-07-22
> **Model**: Project-Based warranty → optional monthly support retainer.

## Warranty (included)

- **Period:** 30 days after final delivery/handover.
- **Scope:**
  - Critical bug fixes for defects in the delivered, in-scope functionality.
  - Security fixes for issues in code Cyberk delivered.
  - Technical support for questions about the delivered scope.
- **Excluded from warranty:** new features, scope changes, third-party outages
  (Retell/Telnyx/Twilio/Google/Polar), issues caused by client changes to accounts or
  configuration, and failures rooted in unapproved regulatory/legal use of the AI.

## Hypercare (pilot launch)

- **Window:** the first 72 hours after the pilot cohort goes live.
- Priority response for production-blocking issues during the earliest real-call traffic
  — the highest-risk window for a phone product (latency, AMD behavior, transfer/booking
  firing on real +65 mobiles).

## Bug definition

A **bug** is delivered in-scope behavior that does not match the agreed specification —
e.g., booking fails on a valid qualified lead, the advice→transfer edge does not fire, the
consent/calling-hours gate is bypassed, or the minute cap is not enforced. It is **not** a
bug if it is: a new capability, a third-party accuracy limit already flagged (e.g.
Singlish ASR degradation, realized connect rate, Retell AMD false-positive rate), or a
change to the client's own accounts/scripts.

## Optional ongoing support (post-warranty)

- **Monthly support retainer: US$3,000 / month** (optional, month-to-month).
- Covers ongoing maintenance, minor enhancements, dependency/version upkeep, monitoring
  support, and priority response — scoped and prioritized with the client each month.
- Larger Phase-2 work (SMS fallback, CRM integrations, call scoring, multi-agent routing,
  LiveKit self-host migration, additional languages) is quoted separately as its own
  project.

## Handover

- Source code in the client's repository, deployment docs, environment/config runbook,
  and the Conversation Flow + compliance-guardrail documentation.
- A short walkthrough of the architecture, the retry/AMD dispositions, the billing
  cap-enforcement, and the human-eval rubric so the client can operate and extend the MVP.

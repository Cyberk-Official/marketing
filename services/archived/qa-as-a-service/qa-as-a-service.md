---
type: mkt
tags: [service, qa-as-a-service, qa, e2e-testing]
created-date: 2026-10-14
updated-date: 2026-10-15
author: neo
status: draft
voice-check: passed 2026-10-15
---

# QA as a Service — End-to-End Testing

## Overview

Your team ships a new build to staging every few days. Before it goes to users, someone has to click through every flow on every browser and check each screen against the Figma file. On most teams that someone is a developer at 11pm the night before release, testing on whatever laptop they have.

We take that job off your team: our QA engineers write the end-to-end test scenarios for your product, run them every week on the browsers and devices you care about, and send you one report every Friday. You don't manage a tester. You read the report, and the bugs are already logged on your board with steps to reproduce.

QA as a Service is sold in blocks of 3 or 6 months, paid upfront: **$5,000 for 3 months** or **$9,000 for 6 months**.

---

## What We Check

Every weekly run covers three things.

| Check | The question it answers | How we test it |
|---|---|---|
| **Functional** | Does each feature do what the spec says? | We run every scenario step by step and compare the actual result with the expected result |
| **Compatibility** | Does it work on the devices your users have? | We run the high-priority flows on each browser and device in the agreed matrix |
| **Layout** | Does each screen match the design? | We put a screenshot of the live screen next to the Figma frame and list every difference |

A typical device matrix, agreed with you in week 1:

| Platform | Browsers | Screen widths |
|---|---|---|
| Desktop (Windows, macOS) | Chrome, Safari, Firefox, Edge — latest version | 1440px |
| Tablet | Safari (iPad), Chrome (Android) | 768px |
| Mobile | Safari (iPhone), Chrome (Android) | 390px |

If your analytics show traffic from an older browser or a specific device, we add it to the matrix.

---

## What You Get

| # | Deliverable | When |
|---|---|---|
| 1 | **E2E test scenarios** | Written in weeks 1–2, then updated when features change |
| 2 | **Weekly E2E report** | Every Friday |
| 3 | **Bug tickets** | Logged on your board as soon as we find them |

### 1. E2E test scenarios

Each scenario follows one user flow from start to finish, for example "investor signs up, passes KYC, and submits a subscription". It lists the steps, the test data, the expected result at each step, and a priority (High, Medium, Low).

We build the list from your specs, user stories and Figma files. You review and approve it before we start running tests, so we both agree on what "covered" means.

The scenarios live in a shared spreadsheet or a test management tool. They belong to you. If you stop the service, your team can keep using them.

### 2. Weekly E2E report

One report per week, with three lines at the top:

- New bugs found this week, by severity
- Bugs fixed and verified this week
- Our recommendation for the next release: **Go** or **Hold**, with the reason

Below that, one section for each check:

- **Functional:** pass/fail for every scenario, and the pass rate compared with last week
- **Compatibility:** a table of flows × devices, with each failed cell linked to its bug ticket
- **Layout:** screenshots next to the Figma frames, with each difference marked

If we find a P0 bug (the system is down, or money or data is at risk), we message you the same day. You won't wait until Friday for that.

### 3. Bug tickets

Each bug goes on your GitHub, Jira or Linear board with:

- Steps to reproduce
- A screenshot or screen recording
- The browser, device and build where it happened
- A severity from P0 to P3

| Severity | Meaning | Example |
|---|---|---|
| **P0** | System down, money or data at risk | Payment hangs, data is lost |
| **P1** | A core feature is broken | Users can't log in |
| **P2** | A feature is broken but there is a workaround | Filter fails, search still works |
| **P3** | Visual only, no effect on function | Wrong font, layout off by a few pixels |

When your developer marks a bug as fixed, we retest it on the next build and close it or reopen it.

---

## How It Starts

| Week | What happens |
|---|---|
| **Week 1** | Kick-off call. We get access to staging, Figma and your board. We agree on the device matrix and list the user flows |
| **Week 2** | We write the scenarios and send them for your review. First test run on the flows that are already approved |
| **Week 3 onward** | Full weekly run and the Friday report |

The first two reports cover only part of the product, because the scenarios are still being written. From week 3 the report covers every approved flow.

---

## Pricing

| Plan | Price (paid upfront) | Per month | Compared with a dedicated QA engineer |
|---|---|---|---|
| **QA as a Service — 3 months** | **$5,000** | ~$1,667 | $7,500 for the same period, you save $2,500 (33%) |
| **QA as a Service — 6 months** | **$9,000** | $1,500 | $15,000 for the same period, you save $6,000 (40%) |
| **Dedicated QA Engineer** | $2,500/mo | $2,500 | — |

Both QA as a Service plans include the same work: E2E scenarios, the weekly run (Functional, Compatibility, Layout), the Friday report and bug tickets. The 6-month plan costs less per month because the first two weeks of setup are spread over a longer period.

QA as a Service is paid in full upfront, before kick-off. The per-month figures above are for comparison only; we don't invoice monthly for these plans.

The two models suit different situations. Pick QA as a Service if you want the testing done and a report you can act on. Pick a dedicated engineer if you already have a QA process and need one more person in it, taking tasks from your lead every day.

---

## What It Does Not Cover

- **Security testing.** E2E tests check that features work, not that they can't be attacked. For that you need a pentest or a code audit.
- **Performance and load testing.** We note pages that feel slow, but we don't measure how many users the system can handle.
- **Unit and integration tests.** Those belong in your codebase and are written by your developers.
- **Design review.** We check that screens match the Figma file. If the Figma file is out of date, we flag the mismatch and ask which one is correct. We don't decide that ourselves.

---

## FAQ

**Q: Do you test on real devices or on emulators?**

We agree on this in week 1. High-priority flows on mobile Safari and Android Chrome are tested on real devices or a cloud device lab. Desktop browsers run on real machines.

<!-- TODO Anderson: chi phí device lab (BrowserStack/LambdaTest) — bao gồm trong giá hay khách trả riêng? -->

**Q: We don't have written specs, only Figma. Can you still start?**

Yes. We write the expected behaviour for each flow from the Figma files and send it to you to confirm. This adds a few days to week 2, and you will need to answer more questions in that week.

**Q: Our team deploys every day. Is one report a week enough?**

For most teams, yes. P0 bugs are reported the same day, and the Friday report covers everything else. If you release several times a week and need every build checked before it goes live, we can write automated tests with Playwright for your most important flows so they run on every deploy. We quote that separately.

**Q: What do you need from us?**

A staging environment that stays up during the test run, test accounts for each user role, access to Figma and your board, and one person on your side who can answer "is this a bug or the intended behaviour?" within a working day.

**Q: Who owns the test scenarios?**

You do. The scenarios, reports and bug history stay with you if you stop the service.

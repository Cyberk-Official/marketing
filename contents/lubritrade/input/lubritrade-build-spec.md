# Order Assistant — Technical Build Specification (Lubritrade)

- **Product**: Order Assistant — a multi-channel (WhatsApp + email) AI order-capture engine that turns free-form customer orders into confirmed Microsoft Business Central sales orders
- **Client**: Lubritrade Distribution Pte Ltd (FMCG distribution — beer, spirits, tobacco; Singapore)
- **Document purpose**: Technical specification and proposal input material for content production.

## Executive Summary
The Order Assistant is a back-end order-automation engine with a thin admin surface. Customer orders arrive in free-form natural language — over WhatsApp (the dominant channel) and email (free-written messages and attached purchase-order documents) — in English, Mandarin, and Korean, using heavy trade shorthand (e.g. "KB light", "CASS 4+2").

On an inbound order the engine:
1. Identifies the customer (sender number / email → BC customer master).
2. Parses the message — or extracts the order lines from an attached purchase-order (PO) PDF — across the three languages (Vision-LLM).
3. Resolves shorthand against an Inventory SKU List with per-customer defaults.
4. Confirms the parsed order directly with the customer on the channel it arrived ("Confirm this is your order: … — reply YES").
5. On customer confirmation, pushes the order straight to Microsoft Dynamics 365 Business Central (create / update / cancel).

## Key Architecture & Technology
- Inbound channels: WhatsApp Business Platform API (Meta) & Email Mailbox (Gmail/Outlook OAuth).
- AI Processing: Multilingual parsing (EN/ZH/KO) via LLM + PO PDF document reading via Vision-LLM.
- System of Record: Microsoft Business Central (OpenAPI Connector, bidirectional create/update/cancel).
- Low Idle Cost / Serverless Architecture: Operational run-cost ~$75–125/mo.
- Commercial Packaging: $20,000 fixed price build / 8 weeks delivery timeline.

## Main Business Values for Founder / B2B Entrepreneurs
- **Scale Without Scaling Headcount**: Replaces manual keying loop for 99.9% of orders. 3-person team can handle order volume of 30 people.
- **Zero-Error Order Processing**: Resolves shorthand, catches anomalies, human-in-the-loop customer approval gate.
- **24/7 Instant Order Confirmation**: Customers can send PO via WhatsApp/email at any hour; AI parses & confirms immediately.
- **High ROI vs. Expensive SaaS**: $20k custom owned build vs. escalating per-seat monthly SaaS fees.

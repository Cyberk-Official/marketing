# B2B AI Solution Video Script (90s) - $75/Month

- **Prefer (Hook 0 - 10s):**
  * *Visual:* Zoom in on the project config code showing `run_cost_launch_usd_month: 75-125`.
  * *Voice:* "75 to 125 dollars a month. That's the total projected operating cost for a fully autonomous AI system: automatically reading emails, WhatsApp messages, resolving order slangs, actively confirming orders with customers in natural language to get verification, then automatically creating the order and sending it directly to the CRM of a B2B business, without any manual human intervention."

- **Acknowledge (Mục tiêu 10s - 35s):**
  * *Visual:* Over-the-shoulder shot of a developer browsing system architecture specs, drawing 3 startup founder concerns on a whiteboard.
  * *Voice:* "When we designed this solution, our goal was to completely solve three major business pain points: First, zero idle run cost – if it doesn't run, you don't pay. Second, automatic scaling from 0 to 100 thousand concurrent users without any architectural changes or manual interventions. Third, seamless integration with the client's existing ERP systems."

- **Trust (Giải pháp cho Mục tiêu 1 & 2: 35s - 55s):**
  * *Visual:* Displaying Cloudflare Workers dashboard and Neon serverless Postgres structure.
  * *Voice:* "To keep the system free of charge when idle and auto-scale dynamically, we built the entire logic on Cloudflare Workers serverless compute, routing AI calls through OpenRouter on a strict pay-as-you-go basis – meaning we only pay for the exact characters processed. When there are no active orders, server and AI API costs drop to exactly zero. Moreover, each chat session runs on its own isolated micro-database to scale instantly. Even as user volume spikes, the infrastructure cost only increases slightly with AI token consumption, which we optimized to be dirt cheap using prompt caching."

- **Trust (Giải pháp cho Mục tiêu 3: 55s - 1h15):**
  * *Visual:* Fast screen recording of OAuth 2.0 connection code and the idempotency `bc_push_guard`.
  * *Voice:* "For integration, the AI connects directly to Microsoft Business Central API through secure OAuth 2.0. Other CRMs or management software like HubSpot integrate in the exact same way. To prevent duplicate orders due to unstable networks, a create-once idempotency guard ensures that every order is recorded exactly once."

- **Stick (Mở vòng lặp 1h15 - 1h25):**
  * *Visual:* Engineer looks directly at the camera, talking calmly.
  * *Voice:* "This is the first chapter in Cyberk's B2B AI design journal. In the next episode, we will share how we teach our AI to resolve multilingual order slangs."

- **Action (CTA 1h25 - 1h30):**
  * *Visual:* A direct message envelope icon with the text "Message Cyberk" appears on screen.
  * *Voice:* "Send us a message if you want to deep dive into these AI infrastructure solutions."

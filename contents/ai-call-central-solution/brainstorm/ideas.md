---
type: brainstorm
project: ai-call-central-solution
source: bootstrap/bidding/ai-telemarketing
created: 2026-07-28
---

# Brainstorm — AI Call Central Solution

> **Dự án gốc:** AI Telemarketing — Phone Voice Agent (Singapore)
> **Định vị:** CyberK — Đơn vị Thiết kế Giải pháp Công nghệ
> **Target Audience:** Founders, CEO, C-level, Solopreneur (The Ambitious Builder)

---

## Ý Tưởng Đã Duyệt (Approved)

### ✅ H1: "Thiết kế hệ thống tổng đài AI tự động gọi điện chốt đơn khi có lead mới"
* **Status:** `approved` — Ưu tiên viết kịch bản
* **Góc nhìn:** Tổng quan giải pháp end-to-end (case study)
* **Bài toán:** Sub-minute Callback — Lead đăng ký → hệ thống gọi lại < 60s
* **Solution Design:** Webhook API → Retell AI → SIP trunk → cuộc gọi thật +65 → qualify → book calendar → retry/transfer
* **Outcomes:** 21x qualify rate, < 60s response, 100% chống trùng lịch, $20K/8 tuần
* **Key Decisions:** Build on Retell (không tự build pipeline), single-seat multi-tenant, outbound-only, compliance guardrail

---

### ✅ H5: "Thiết kế hệ thống: AI nhận lead, gọi điện, xác nhận nhu cầu, và chốt lịch hẹn — tất cả tự động"
* **Status:** `approved`
* **Góc nhìn:** Full automation loop — nhấn mạnh end-to-end
* **Bài toán:** Toàn bộ chuỗi: lead intake → callback → qualify → book → retry/transfer
* **Solution Design:** Landing Page → Webhook → Retell AI call → BANT qualify → Calendar lock (unique ID) → Warm transfer / AMD retry
* **Outcomes:** Tự động hóa hoàn toàn chuỗi từ lead → appointment, zero manual intervention
* **Key Decisions:** Hybrid extraction (during-call + post-call), confirm-back mỗi field, qualify-then-book sequence

---

### ✅ H6: "Thiết kế tổng đài AI song ngữ Anh-Hoa — khi không engine nào hiểu Singlish"
* **Status:** `approved`
* **Góc nhìn:** Thách thức kỹ thuật + giải pháp ngôn ngữ
* **Bài toán:** Bilingual Agent — English/Mandarin + Singlish graceful degradation
* **Solution Design:** 2 agent đơn ngữ (English-SG, Mandarin), chọn per-call từ preferred_language, confirm-back aggressive, human escape path
* **Outcomes:** Xử lý 2 ngôn ngữ chính mà không cần custom ASR
* **Key Decisions:** Không hứa Singlish fluency, graceful degradation thay vì force multilingual, MERaLiON chỉ khi scale

---

## Ý Tưởng Tham Khảo (Archive)

### H2: "Thiết kế giải pháp: từ lúc khách điền form đến lúc nhận cuộc gọi — dưới 1 phút"
* **Status:** `archived` — Hook tốt, có thể dùng cho video ngắn

### H3: "Thiết kế luồng Webhook → AI Voice → Cuộc gọi thật trong 60 giây"
* **Status:** `archived` — Kỹ thuật, phù hợp kênh dev

### H4: "Làm sao để một tổng đài AI gọi lại khách hàng nhanh hơn bất kỳ nhân viên nào?"
* **Status:** `archived` — Dạng câu hỏi, hơi thiên vấn đề

### H7: "Thiết kế 2 AI agent đơn ngữ thay vì 1 agent đa ngữ — và tại sao đó là quyết định đúng"
* **Status:** `archived` — Trade-off decision, dùng cho Trust layer

### H8: "Thiết kế hệ thống chọn ngôn ngữ per-call — để AI tổng đài không bị lẫn tiếng"
* **Status:** `archived`

### H9: "Khi AI nghe không hiểu — thiết kế graceful degradation cho tổng đài song ngữ"
* **Status:** `archived` — Chuyên sâu, phù hợp Trust layer

### H10: "Thiết kế giải pháp confirm-back — để AI tổng đài không ghi sai tên, sai số, sai lịch"
* **Status:** `archived` — Cụ thể, dễ hiểu

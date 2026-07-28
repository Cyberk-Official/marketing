---
type: skill
name: script-maker
description: "Quy trình sản xuất kịch bản 4 phase: Init → Brainstorm → Script Write → Review. Mỗi bước AI lưu lại quyết định dưới dạng spec-ai.html."
tags: [marketing, video-script, production, paast, vcl, new-media]
created: 2026-07-22
---

# SKILL: Script Maker — Quy Trình Sản Xuất Kịch Bản 4 Phase

Skill này định nghĩa **quy trình đầy đủ** để sản xuất một kịch bản video ngắn Cyberk từ đầu đến cuối, bao gồm khởi tạo workspace, động não ý tưởng, viết kịch bản chi tiết và kiểm duyệt.

> **Nguyên tắc vàng:**
> 1. **BẢO MẬT & ẨN DANH BẮT BỘC:** TUYỆT ĐỐI KHÔNG để lộ tên thật của khách hàng hoặc dự án (như Lubritrade, FairPrice, Cold Storage...) trong bất kỳ ý tưởng brainstorm, tiêu đề hay kịch bản public nào. LUÔN LUÔN ẩn danh hóa bằng định danh ngành/mô hình (ví dụ: *"Nhà phân phối sỉ FMCG 500+ đơn/ngày tại Singapore"*, *"Doanh nghiệp bán buôn đồ uống"*).
> 2. **DECISION LOG:** Mỗi khi AI đưa ra một quyết định quan trọng không có trong spec người dùng cung cấp (chọn angle, ẩn danh tên khách hàng, lý do chọn ý tưởng...), AI **bắt buộc** phải ghi lại vào `spec-ai.html`.

---

## 📁 Cấu Trúc Workspace Kịch Bản Sau Khi Khởi Tạo

Mỗi kịch bản mới sẽ có workspace riêng, đặt tên theo tên kịch bản (slug). Ví dụ: `75$-ai-system`:

```text
marketing/contents/
└── [tên-kịch-bản]/          # Ví dụ: 75$-ai-system/
    ├── input/                # Dữ liệu thô đầu vào (Bidding estimate, Case study...)
    ├── brainstorm/           # Output của Phase 2: Danh sách 10 ý tưởng & Phân tích bài toán
    │   └── ideas.md          # Tuân thủ template: skills/brainstorm/template.md
    ├── scripts/              # Output của Phase 3: Kịch bản chi tiết 2 cột
    │   └── [STT]_[slug].md   # Tuân thủ template: skills/script-maker/template.md
    ├── reviews/              # Output của Phase 4: Biên bản kiểm duyệt
    │   └── review.md
    └── spec-ai.html          # Ghi chú quyết định của AI (mỗi phase cộng dồn vào đây)
```

---

## 🔄 Phase 1: INIT — Khởi Tạo Workspace Kịch Bản Mới

**Mục tiêu:** Tạo toàn bộ cấu trúc thư mục cần thiết cho một kịch bản mới trước khi bắt đầu sản xuất.

### Các bước thực thi:

1. **Nhận tên kịch bản từ người dùng** (dạng slug, ví dụ: `75$-ai-system`, `lubritrade-ocr`, `skin-agent-demo`).
2. **Tạo cấu trúc thư mục** tại `marketing/[tên-kịch-bản]/`:
   ```
   input/
   brainstorm/
   scripts/
   reviews/
   spec-ai.html  ← Tạo ngay với nội dung khởi tạo (xem mẫu bên dưới)
   ```
3. **Khởi tạo `spec-ai.html`** với thông tin Phase 1 (tên kịch bản, thời gian tạo, người yêu cầu).

### Mẫu khởi tạo `spec-ai.html`:

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>AI Decision Log — [tên-kịch-bản]</title>
  <style>
    body { font-family: monospace; max-width: 900px; margin: 40px auto; background: #0d0d0d; color: #e0e0e0; padding: 20px; }
    h1 { color: #7dd3fc; } h2 { color: #86efac; border-bottom: 1px solid #374151; padding-bottom: 8px; }
    .phase { background: #1a1a2e; border-left: 4px solid #7dd3fc; padding: 12px 16px; margin: 16px 0; border-radius: 4px; }
    .decision { background: #1f2937; padding: 10px 14px; margin: 8px 0; border-radius: 4px; }
    .label { color: #fbbf24; font-weight: bold; }
    .timestamp { color: #6b7280; font-size: 0.85em; }
  </style>
</head>
<body>
  <h1>🧠 AI Decision Log</h1>
  <p><span class="label">Kịch bản:</span> [tên-kịch-bản]</p>
  <p><span class="label">Khởi tạo:</span> <span class="timestamp">[timestamp]</span></p>

  <h2>📁 Phase 1: INIT</h2>
  <div class="phase">
    <div class="decision">
      <span class="label">Quyết định:</span> Khởi tạo workspace mới cho kịch bản "[tên-kịch-bản]".<br>
      <span class="label">Lý do:</span> Người dùng yêu cầu tạo kịch bản mới theo quy trình 4-phase Script Maker.<br>
      <span class="label">Cấu trúc tạo ra:</span> input/, brainstorm/, scripts/, reviews/, spec-ai.html
    </div>
  </div>

  <!-- Phase 2, 3, 4 sẽ được cộng dồn vào đây -->
</body>
</html>
```

---

## 🧠 Phase 2: BRAINSTORM — Phân Tích Bài Toán Khách Hàng & Động Não 10 Ý Tưởng

**Mục tiêu:** Đọc file Input → Phân tích bài toán thực tế của khách hàng → Sinh ra 10 ý tưởng kịch bản theo phễu PAAST (luôn ẩn danh tên khách hàng).

### Các bước thực thi:

1. **Đọc tài liệu Input** từ thư mục `[tên-kịch-bản]/input/`.
2. **Mổ Xẻ Phân Tích Bài Toán Khách Hàng (Customer Problem Deep-Dive)** trước khi sinh ý tưởng:
   - *Bối cảnh & Quy mô:* Ngành nghề, quy mô giao dịch, kênh tiếp nhận đơn.
   - *Nỗi đau bề nổi vs Gốc rễ:* Nhập tay chậm, hay gõ nhầm SKU/pack vs. Thiếu đồng bộ ERP và thiếu quy chuẩn dữ liệu.
   - *Rào cản hành vi:* Người dùng cuối (khách sỉ) tẩy chay Portal/App mới, chỉ nhắn chat/email.
   - *Rủi ro vận hành & Tài chính:* Chi phí nhân sự nhập liệu, rủi ro xuất nhầm hàng, bẫy chi phí SaaS per-seat.
3. **Áp dụng Quy tắc Ẩn danh hóa (Anonymization):** Đảm bảo 100% tên thật khách hàng/dự án được chuyển thành tên gọi đại diện ngành.
4. **Sinh 10 Idea Card PAAST** tuân thủ **template chuẩn** tại `skills/brainstorm/template.md`.
5. **Lưu output** vào `[tên-kịch-bản]/brainstorm/ideas.md` (chứa cả phần phân tích bài toán & 10 ý tưởng).
6. **Cập nhật `spec-ai.html`**: Ghi lại các quyết định quan trọng (nhận diện bài toán gốc rễ, tên ẩn danh được chọn, các hook nổi bật...).

---

## ✍️ Phase 3: SCRIPT WRITE — Dựng Kịch Bản Chi Tiết

**Mục tiêu:** Chọn 1–3 ý tưởng từ danh sách Brainstorm → Viết kịch bản chi tiết 2 cột chuẩn quay dựng.

### Các bước thực thi:

1. **Nhận ý tưởng được duyệt** từ người dùng (ví dụ: Ý tưởng #3 và #7).
2. **Áp dụng template kịch bản** tại `skills/script-maker/template.md` cho từng ý tưởng.
3. **Lưu từng kịch bản** vào `[tên-kịch-bản]/scripts/[STT]_[slug].md`.
4. **Cập nhật `spec-ai.html`**: Ghi lại quyết định về phân bổ thời gian, cách xây dựng CTA, lựa chọn Visual cụ thể mà spec không ghi rõ.

---

## 🔍 Phase 4: REVIEW — Kiểm Duyệt & Phê Duyệt

**Mục tiêu:** Rà soát kịch bản theo Pre-Publish Checklist, đảm bảo tuân thủ giá trị cốt lõi Cyberk & tiêu chuẩn cộng đồng.

### Các bước thực thi:

1. **Chạy Pre-Publish Checklist** theo `cyberk-video-strategy-paast-vcl.md` (Scorecard ≥ 12/15 điểm).
2. **Kiểm tra an toàn nội dung** theo 4 tiêu chuẩn:
   - ✅ Ẩn danh tên khách hàng & bảo mật dữ liệu
   - ✅ Anti-Clickbait (không giật gân vô căn cứ)
   - ✅ Không vi phạm chính sách cộng đồng (TikTok / YouTube / Facebook / LinkedIn)
   - ✅ Không hứa hẹn quá đà về tính năng / kết quả công nghệ
3. **Lưu biên bản Review** vào `[tên-kịch-bản]/reviews/review.md`.
4. **Cập nhật `spec-ai.html`**: Ghi lại lý do Pass/Fail từng mục, các điều chỉnh AI tự động thực hiện trước khi kịch bản được duyệt.

---

## 📋 Tóm Tắt Luồng Thực Thi (Quick Reference)

```
USER cung cấp Input
      │
      ▼
Phase 1: INIT      → Tạo workspace + spec-ai.html
      │
      ▼
Phase 2: BRAINSTORM → ideas.md (10 ý tưởng PAAST) + cập nhật spec-ai.html
      │
      ▼ (user duyệt ý tưởng)
Phase 3: SCRIPT    → scripts/[STT]_[slug].md (2-cột VCL) + cập nhật spec-ai.html
      │
      ▼
Phase 4: REVIEW    → reviews/review.md + cập nhật spec-ai.html
      │
      ▼
✅ DONE — Kịch bản sẵn sàng giao cho đội quay dựng
```

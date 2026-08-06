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
> 1. **BẢO MẬT & ẨN DANH BẮT BỘC:** TUYỆT ĐỐI KHÔNG để lộ thông tin hay tên thật của đối tác hoặc dự án (như Lubritrade, FairPrice, Cold Storage...) trong bất kỳ ý tưởng brainstorm, tiêu đề hay kịch bản public nào. LUÔN LUÔN ẩn danh hóa bằng định danh ngành/mô hình (ví dụ: *"Nhà phân phối sỉ FMCG 500+ đơn/ngày tại Singapore"*, *"Doanh nghiệp bán buôn đồ uống"*).
>    - **THÔNG TIN MẬT CẤM ĐỀ CẬP TRONG KỊCH BẢN:** Giá trị hợp đồng (ví dụ: $20K, $50K), quy mô team (solo founder, 3 engineers...), thời gian thi công cụ thể (8 tuần, 2 tháng...), cơ cấu chi phí nội bộ, pricing model nội bộ. Chỉ được dùng từ chung chung: *"một startup"*, *"một dự án"*, *"doanh nghiệp"*. Nếu cần nói về quy mô, chỉ nói mức độ tổng quát: *"giai đoạn đầu"*, *"quy mô vừa và nhỏ"*.
> 2. **NHÂN XƯNG "TÔI" & PHONG CÁCH GẦN GŨI (BẮT BỘC):**
>    - **Nhân xưng LUÔN LUÔN là "tôi":** Trong kịch bản lời thoại/dẫn chuyện và khi trình bày ý tưởng, luôn xưng **"tôi"** để tạo sự gần gũi, thân thiết và chân thật như chia sẻ giữa những người làm nghề với nhau. Tuyệt đối không dùng "chúng tôi", "Cyberk", hay các cách xưng hô xa cách.
>    - **TUYỆT ĐỐI KHÔNG DÙNG TỪ "KHÁCH HÀNG":** Cấm sử dụng từ "khách hàng". Thay vào đó, dùng cách diễn đạt theo bối cảnh dự án (ví dụ: *"yêu cầu của dự án là..."*, *"bài toán của dự án"*, *"bài toán thực tế"*, *"đối tác"*, *"đơn vị đồng hành"*).
>    - **GIỌNG ENGINEER — THẲNG, GỌN, KHÔNG HOA MỸ (BẮT BUỘC):** Lời thoại phải mang giọng của một kỹ sư đang giải thích cho kỹ sư khác — **thẳng thắn, đi vào trọng tâm, không màu mè, không kịch tính hóa**. Cấm các cụm từ dramatic kiểu: *"toàn bộ hệ thống sẽ sụp đổ"*, *"bài toán nguy hiểm nhất"*, *"mất uy tín ngay từ ngày đầu vận hành"*. Thay bằng ngôn ngữ kỹ thuật bình thản: *"sẽ bị race condition"*, *"gây ra double booking"*, *"cần xử lý ở tầng database"*. Nói như đang pair programming, không phải đang lên sân khấu.
> 3. **DECISION LOG:** Mỗi khi AI đưa ra một quyết định quan trọng không có trong spec người dùng cung cấp (chọn angle, ẩn danh thông tin dự án, lý do chọn ý tưởng...), AI **bắt buộc** phải ghi lại vào `spec-ai.html`.
> 4. **ĐỌC TÀI LIỆU NGỮ CẢNH TRƯỚC KHI BẮT ĐẦU:** Trước khi thực thi bất kỳ Phase nào, **BẮT BUỘC** đọc toàn bộ tài liệu trong thư mục `docs/` để nạp ngữ cảnh — bao gồm audience persona, phương pháp luận PAAST-VCL, và guideline viết kịch bản.

---

## 📚 Tài Liệu Ngữ Cảnh Bắt Buộc (`docs/`)

> **⚠️ RULE: Luôn đọc thư mục `docs/` trước khi bắt đầu MỌI phase để không quên ngữ cảnh.**

Thư mục `skills/docs/` chứa các tài liệu nền tảng mà mọi phase trong quy trình đều phải tham chiếu:

| Tài liệu | Vai trò | Khi nào đọc |
|-----------|---------|-------------|
| `docs/audience_profile.md` | **Chân dung khán giả mục tiêu** — The Ambitious Builder (Founders, CEOs, C-level, Solopreneur). Xác định nỗi đau, khát khao, hành vi, và ngôn ngữ của họ. | Trước mọi phase — đặc biệt Phase 2 (Brainstorm) & Phase 3 (Script Write) |
| `docs/cyberk-video-strategy-paast-vcl.md` | **Phương pháp luận gốc** — Phễu PAAST, Khung VCL, Ba tính chất cốt lõi (Entertainment + Educational + Authentic), Scorecard đánh giá. | Trước mọi phase — là kim chỉ nam cho toàn bộ nội dung |
| `docs/script-make.md` | **Guideline viết kịch bản** — Phễu PAAST timeline %, bảng quy đổi từ/phút, Pre-Publish Checklist. | Chủ yếu Phase 3 (Script Write) |

---

## 📁 Cấu Trúc Workspace Kịch Bản Sau Khi Khởi Tạo

Mỗi kịch bản mới sẽ có workspace riêng, đặt tên theo tên kịch bản (slug). Ví dụ: `75$-ai-system`:

```text
marketing/contents/
└── [tên-kịch-bản]/          # Ví dụ: 75$-ai-system/
    ├── input/                # Dữ liệu thô đầu vào (Bidding estimate, Case study...)
    ├── brainstorm/           # Output của Phase 2: Danh sách 10 ý tưởng & Phân tích bài toán
    │   └── ideas.md          # Tuân thủ template: skills/brainstorm/template.md
    ├── scripts/              # Output của Phase 3a + 3b: Outline + Kịch bản chi tiết
    │   ├── [STT]_[slug]_outline.md  # Dàn ý (Phase 3a) — tuân thủ skills/script-maker/outline.md
    │   └── [STT]_[slug].md          # Kịch bản 2 cột (Phase 3b) — tuân thủ skills/script-maker/template.md
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

## 🧠 Phase 2: BRAINSTORM — Phân Tích Bài Toán Dự Án & Động Não 10 Ý Tưởng

**Mục tiêu:** Đọc file Input → Phân tích bài toán thực tế của dự án → Sinh ra 10 ý tưởng kịch bản theo phễu PAAST (luôn ẩn danh thông tin dự án/đối tác).

### Các bước thực thi:

1. **📚 Đọc `docs/` để nạp ngữ cảnh** — Đặc biệt `docs/audience_profile.md` để hiểu persona **"The Ambitious Builder"**: Founders/CEOs quan tâm đến doanh thu, chi phí, scale, gọi vốn. Mọi ý tưởng phải đánh trúng nỗi đau và khát khao của persona này.
2. **Đọc tài liệu Input** từ thư mục `[tên-kịch-bản]/input/`.
3. **Mổ Xẻ Phân Tích Bài Toán Thực Tế Của Dự Án (Project Problem Deep-Dive)** trước khi sinh ý tưởng:
   - *Bối cảnh & Quy mô:* Ngành nghề, quy mô giao dịch, kênh tiếp nhận đơn.
   - *Nỗi đau bề nổi vs Gốc rễ:* Nhập tay chậm, hay gõ nhầm SKU/pack vs. Thiếu đồng bộ ERP và thiếu quy chuẩn dữ liệu.
   - *Rào cản hành vi:* Người dùng cuối (đối tác sỉ) tẩy chay Portal/App mới, chỉ nhắn chat/email.
   - *Rủi ro vận hành & Tài chính:* Chi phí nhân sự nhập liệu, rủi ro xuất nhầm hàng, bẫy chi phí SaaS per-seat.
4. **Áp dụng Quy tắc Ẩn danh hóa & Từ ngữ:**
   - 100% thông tin/tên thật của dự án hoặc đối tác được chuyển thành tên gọi đại diện ngành.
   - Không sử dụng từ "khách hàng" (ví dụ: thay "khách hàng yêu cầu" bằng "yêu cầu của dự án là").
5. **Sinh 10 Idea Card PAAST** tuân thủ **template chuẩn** tại `skills/brainstorm/template.md`.
6. **Lưu output** vào `[tên-kịch-bản]/brainstorm/ideas.md` (chứa cả phần phân tích bài toán & 10 ý tưởng).
7. **Cập nhật `spec-ai.html`**: Ghi lại các quyết định quan trọng (nhận diện bài toán gốc rễ, tên ẩn danh được chọn, các hook nổi bật...).

---

## 📝 Phase 3a: OUTLINE — Dàn Ý Kịch Bản

**Mục tiêu:** Chọn ý tưởng từ danh sách Brainstorm → Lên dàn ý (outline) cho kịch bản → **Duyệt dàn ý trước khi viết chi tiết**.

### Các bước thực thi:

1. **📚 Đọc `docs/` để nạp ngữ cảnh** (audience, PAAST-VCL, script guideline).
2. **Nhận ý tưởng được duyệt** từ người dùng.
3. **Áp dụng outline template** tại `skills/script-maker/outline.md`:
   - Bối cảnh dự án (startup/enterprise, giai đoạn, chiến lược thiết kế)
   - Dàn ý 5 Scene theo PAAST (Hook, FR, Startup Context, NFR, Trust luận điểm, Stick, CTA)
   - Mỗi scene chỉ ghi ý chính + visual dự kiến — **KHÔNG viết lời thoại chi tiết**
4. **Lưu outline** vào `[tên-kịch-bản]/scripts/[STT]_[slug]_outline.md`.
5. **Dừng lại chờ duyệt.** Người dùng xác nhận outline trước khi chuyển sang Phase 3b.
6. **Cập nhật `spec-ai.html`**: Ghi lại các quyết định chọn luận điểm, phân bổ thời gian.

---

## ✍️ Phase 3b: SCRIPT WRITE — Dựng Kịch Bản Chi Tiết

**Mục tiêu:** Từ outline đã duyệt → Viết kịch bản chi tiết 2 cột chuẩn quay dựng.

> **⚠️ RULE: Chỉ bắt đầu Phase 3b SAU KHI outline đã được duyệt ở Phase 3a.**

### Các bước thực thi:

1. **📚 Đọc `docs/` để nạp ngữ cảnh** — Đặc biệt:
   - `docs/audience_profile.md` → Đảm bảo giọng kể, ví von, và nỗi đau được đề cập phù hợp với **The Ambitious Builder** (Founders/CEOs/C-level). Họ cần nghe ngôn ngữ business (doanh thu, chi phí, scale, ROI) — không phải jargon lập trình thuần túy.
   - `docs/cyberk-video-strategy-paast-vcl.md` → Tham chiếu phương pháp luận PAAST + VCL + Ba tính chất cốt lõi.
   - `docs/script-make.md` → Guideline phễu PAAST timeline %, bảng quy đổi từ/phút.
2. **Đọc outline đã duyệt** từ `scripts/[STT]_[slug]_outline.md`.
3. **Chuẩn hóa Văn phong & Nhân xưng:**
   - Lời thoại/Audio LUÔN dùng nhân xưng **"tôi"** (ví dụ: *"Tôi từng gặp bài toán này..."*, *"Tôi thử giải quyết theo cách..."*).
   - Tuyệt đối **KHÔNG dùng từ "khách hàng"** trong kịch bản (dùng *"yêu cầu của dự án là"*, *"bài toán thực tế"*...).
4. **PHÂN TÍCH BỐI CẢNH ĐỐI TƯỢNG DỰ ÁN (BẮT BUỘC trong Scene 2):** Scene 2 (Acknowledge) **LUÔN LUÔN** phải có phần phân tích bối cảnh đối tượng dự án: Startup giai đoạn đầu hay Enterprise chuyển đổi số? Có người dùng thực tế chưa? Ngân sách lean hay enterprise-grade? — Vì thông tin này **quyết định toàn bộ chiến lược thiết kế** ở Scene 3 (Trust). Nếu bỏ sót phần này, khán giả sẽ không hiểu tại sao chọn kiến trúc A thay vì B.
   - **Văn mẫu startup:** *"Thông tin này đòi hỏi hệ thống phải tiết kiệm tối đa chi phí vận hành khi chưa có người dùng — nhưng vẫn phải sẵn sàng scale khi người dùng thực sự đến. Chiến lược thiết kế ưu tiên: [lý do tiết kiệm khi chưa có user] + [lý do phải scale khi user tăng] + [chỉ cần trả thêm tiền theo lượng sử dụng]."*
5. **QUY TẮC XÂY DỰNG CTA (BẮT BUỘC trong Scene 5):** Tuyệt đối **tránh các câu CTA thô / bán hàng trực diện** và **KHÔNG nhắc tên thương hiệu / không quảng cáo dịch vụ** (ví dụ: *"Nếu bạn đang tìm giải pháp tự động hóa... hãy liên hệ CyberK để cùng thảo luận"*). Thay vào đó, LUÔN đóng vai một người bạn đồng hành kêu gọi trao đổi, tạo thảo luận mở chân thành (ví dụ: *"Nếu bạn quan tâm tới thiết kế hệ thống, hoặc đang làm startup công nghệ, hãy để lại comment để chúng mình cùng thảo luận nhé."*).
6. **Áp dụng template kịch bản** tại `skills/script-maker/template.md` cho từng ý tưởng.
7. **Viết từng Scene, dừng lại thảo luận sau mỗi scene.** Người dùng confirm mới tiếp tục scene tiếp theo.
8. **Lưu từng kịch bản** vào `[tên-kịch-bản]/scripts/[STT]_[slug].md`.
9. **Cập nhật `spec-ai.html`**: Ghi lại quyết định về phân bổ thời gian, cách xây dựng CTA, lựa chọn Visual cụ thể mà spec không ghi rõ.

---

## 🔍 Phase 4: REVIEW — Kiểm Duyệt & Phê Duyệt

**Mục tiêu:** Rà soát kịch bản theo Pre-Publish Checklist, đảm bảo tuân thủ giá trị cốt lõi Cyberk & tiêu chuẩn cộng đồng.

### Các bước thực thi:

1. **Chạy Pre-Publish Checklist** theo `cyberk-video-strategy-paast-vcl.md` (Scorecard ≥ 12/15 điểm).
2. **Kiểm tra an toàn nội dung & văn phong** theo các tiêu chuẩn:
   - ✅ Ẩn danh tên đối tác / dự án & bảo mật dữ liệu
   - ✅ Nhân xưng "tôi" gần gũi & TUYỆT ĐỐI không dùng từ "khách hàng"
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
Phase 1: INIT       → Tạo workspace + spec-ai.html
      │
      ▼
Phase 2: BRAINSTORM → ideas.md (10 ý tưởng PAAST) + cập nhật spec-ai.html
      │
      ▼ (user duyệt ý tưởng)
Phase 3a: OUTLINE   → scripts/[STT]_outline.md (dàn ý các scene)
      │
      ▼ (user duyệt outline)
Phase 3b: SCRIPT    → scripts/[STT]_[slug].md (2-cột VCL chi tiết)
      │
      ▼
Phase 4: REVIEW     → reviews/review.md + cập nhật spec-ai.html
      │
      ▼
✅ DONE — Kịch bản sẵn sàng giao cho đội quay dựng
```


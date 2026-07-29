---
type: guideline
tags: [marketing, workflow, content-production, video, new-media]
created: 2026-07-28
---

# Workflow Sản Xuất Nội Dung Video Ngắn Cyberk

Tài liệu này mô tả **toàn bộ quy trình từ A→Z** để sản xuất một video ngắn chuẩn Cyberk — từ lúc có nguyên liệu thô cho đến khi kịch bản sẵn sàng giao cho đội quay dựng.

> **Nguyên tắc thiết kế quy trình:**
> - Mỗi giai đoạn được **tách thành skill độc lập**, có input/output rõ ràng.
> - Giữa mỗi giai đoạn đều có **checkpoint duyệt** — con người quyết định trước khi tiến sang bước tiếp theo.
> - Mọi quyết định quan trọng được ghi vào `spec-ai.html` (Decision Log) xuyên suốt quy trình.
> - **📚 RULE: Luôn đọc toàn bộ `docs/` trước khi bắt đầu MỌI phase** để nạp ngữ cảnh — bao gồm audience persona, phương pháp luận PAAST-VCL, và guideline viết kịch bản.

---

## 📚 Tài Liệu Ngữ Cảnh Bắt Buộc (`docs/`)

> **⚠️ Đây là bước đầu tiên trước MỌI phase. Không bỏ qua.**
>
> Thư mục `skills/docs/` chứa các tài liệu nền tảng xuyên suốt quy trình. Đọc chúng giúp AI/Content Creator không quên ngữ cảnh — đặc biệt khi bắt đầu session mới hoặc chuyển phase.

| Tài liệu | Vai trò | Áp dụng cho Phase |
|-----------|---------|-------------------|
| [audience_profile.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/audience_profile.md) | **Chân dung khán giả** — The Ambitious Builder (Founders, CEOs, C-level, Solopreneur). Nỗi đau, khát khao, hành vi, ngôn ngữ. | Tất cả — đặc biệt Phase 1 & 2 |
| [cyberk-video-strategy-paast-vcl.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/cyberk-video-strategy-paast-vcl.md) | **Phương pháp luận gốc** — Phễu PAAST, Khung VCL, Ba tính chất cốt lõi, Scorecard. | Tất cả — kim chỉ nam toàn bộ nội dung |
| [script-make.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/script-make.md) | **Guideline viết kịch bản** — PAAST timeline %, bảng từ/phút, Pre-Publish Checklist. | Chủ yếu Phase 2 |

---

## 🗺️ Tổng Quan Quy Trình (Pipeline Overview)

```text
INPUT (Tài liệu thô)
       │
       ▼
┌──────────────────────────────────────────────┐
│  PHASE 0: INIT                               │
│  Khởi tạo workspace + spec-ai.html           │
│  Skill: script-maker/SKILL.md (Phase 1)      │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  PHASE 1: BRAINSTORM                         │
│  Trích xuất insight → Sinh 10 ý tưởng PAAST │
│  Skill: brainstorm/brainstorm.md             │
└──────────────────┬───────────────────────────┘
                   │
              ✋ CHECKPOINT 1
              User duyệt & chọn ý tưởng
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  PHASE 2: SCRIPT WRITE                       │
│  Dựng kịch bản chi tiết 2 cột (PAAST + VCL) │
│  Skill: script-make.md + script-maker/       │
└──────────────────┬───────────────────────────┘
                   │
              ✋ CHECKPOINT 2
              User review bản nháp kịch bản
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  PHASE 3: REVIEW                             │
│  Kiểm duyệt 3 lớp + Scorecard               │
│  Skill: review/review.md                     │
└──────────────────┬───────────────────────────┘
                   │
              ✋ CHECKPOINT 3
              Approved ≥ 12/40 → Giao quay dựng
                   │
                   ▼
         ✅ DONE — Sẵn sàng sản xuất
```

---

## 📁 Phase 0: INIT — Khởi Tạo Workspace

**Mục tiêu:** Tạo cấu trúc thư mục chuẩn cho một kịch bản mới trước khi bắt đầu bất kỳ công việc nội dung nào.

| Mục | Chi tiết |
|-----|---------|
| **Skill tham chiếu** | [SKILL.md](file:///Users/anderson/Desktop/works/marketing/skills/script-maker/SKILL.md) — Phase 1: INIT |
| **Input** | Tên kịch bản (slug) + Tài liệu thô (Bidding Estimate, Case Study, Solution Design) |
| **Output** | Cấu trúc thư mục `contents/[tên-kịch-bản]/` + `spec-ai.html` khởi tạo |

### Cấu trúc thư mục được tạo:
```text
marketing/contents/
└── [tên-kịch-bản]/
    ├── input/            # Dữ liệu thô đầu vào
    ├── brainstorm/       # Output Phase 1
    ├── scripts/          # Output Phase 2
    ├── reviews/          # Output Phase 3
    └── spec-ai.html      # Decision Log (cộng dồn qua mọi phase)
```

### Các bước:
1. **📚 Đọc `docs/`** để nạp ngữ cảnh (audience persona, phương pháp luận).
2. Nhận tên kịch bản (slug) từ người dùng.
3. Tạo toàn bộ cấu trúc thư mục.
4. Đặt tài liệu thô vào `input/`.
5. Khởi tạo `spec-ai.html` với thông tin Phase 0.

---

## 🧠 Phase 1: BRAINSTORM — Động Não & Lên Ý Tưởng

> **⚠️ Đây là phase ĐỘC LẬP — tách riêng khỏi quy trình Script Make.**
> Phase này kết thúc khi user chọn được ý tưởng. Script Make chỉ bắt đầu SAU checkpoint này.

| Mục | Chi tiết |
|-----|---------|
| **Skill tham chiếu** | [brainstorm.md](file:///Users/anderson/Desktop/works/marketing/skills/brainstorm/brainstorm.md) |
| **Template output** | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/brainstorm/template.md) |
| **Input** | Tài liệu thô từ `input/` |
| **Output** | `brainstorm/ideas.md` — 10 ý tưởng PAAST + Phân tích bài toán |

### Các bước:

1. **📚 Đọc `docs/`** — Đặc biệt `audience_profile.md` để nắm persona **"The Ambitious Builder"**: Founders/CEOs quan tâm đến doanh thu, chi phí, scale, gọi vốn. Mọi ý tưởng phải đánh trúng nỗi đau và khát khao của persona này.

2. **Đọc & Trích xuất** — Mổ xẻ tài liệu Input theo 4 nhóm nguyên liệu:
   - Nỗi đau & Vấn đề nghiệp vụ (Business Pain Points)
   - Con số ấn tượng (Shocking Metrics)
   - Giải pháp kiến trúc & Trade-offs kỹ thuật
   - Bài học quản trị / Rủi ro (Founder Insights)

2. **Ẩn danh hóa** — Tuyệt đối không để lộ tên khách hàng/dự án thật.

3. **Sinh 10 Idea Card** — Phân bổ theo ma trận PAAST:
   | Tầng | Số ý tưởng |
   |------|-----------|
   | P — Prefer | 2 |
   | A — Acknowledge | 2 |
   | T — Trust | 3 |
   | S — Stick | 1 |
   | A — Action | 2 |

4. **Lưu output** → `brainstorm/ideas.md`
5. **Cập nhật `spec-ai.html`** — Ghi quyết định ẩn danh, hook nổi bật, bài toán gốc rễ.

### ✋ CHECKPOINT 1: Duyệt Ý Tưởng

Người dùng xem 10 ý tưởng và **chọn 1–3 ý tưởng** để viết kịch bản chi tiết.
- Đánh dấu trạng thái ý tưởng được chọn → `approved`
- Ý tưởng bị loại → `rejected`
- **Không tiến sang Phase 2 nếu chưa có ý tưởng được `approved`.**

---

## ✍️ Phase 2: SCRIPT WRITE — Dựng Kịch Bản Chi Tiết

> **Phase này chỉ bắt đầu SAU KHI ý tưởng đã được chọn từ Phase 1.**
> Toàn bộ quy tắc viết kịch bản tuân thủ `script-make.md`.

| Mục | Chi tiết |
|-----|---------|
| **Guideline viết kịch bản** | [script-make.md](file:///Users/anderson/Desktop/works/marketing/skills/script-make.md) |
| **Skill tham chiếu** | [SKILL.md](file:///Users/anderson/Desktop/works/marketing/skills/script-maker/SKILL.md) — Phase 3: SCRIPT WRITE |
| **Template output** | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/script-maker/template.md) |
| **Input** | Ý tưởng đã `approved` từ `brainstorm/ideas.md` |
| **Output** | `scripts/[STT]_[slug].md` — Kịch bản 2 cột chuẩn quay dựng |

### Các bước:

1. **📚 Đọc `docs/`** — Đặc biệt:
   - `audience_profile.md` → Đảm bảo giọng kể, ví von phù hợp **The Ambitious Builder** (ngôn ngữ business: doanh thu, chi phí, scale, ROI — không phải jargon lập trình thuần túy).
   - `cyberk-video-strategy-paast-vcl.md` → Tham chiếu phương pháp luận PAAST + VCL.
   - `script-make.md` → Guideline PAAST timeline %, bảng quy đổi từ/phút.

2. **Nhận ý tưởng đã duyệt** — Lấy Idea Card `approved` từ `brainstorm/ideas.md`.

2. **Chọn thời lượng clip** — Dựa vào bảng quy đổi trong `script-make.md`:
   | Thời lượng | Số từ lời thoại |
   |-----------|----------------|
   | 90s (1.5 phút) | ~195 – 210 từ |
   | 120s (2 phút) | ~260 – 280 từ |
   | 150s (2.5 phút) | ~325 – 350 từ |
   | 180s (3 phút) | ~390 – 420 từ |
   | 240s (4 phút) | ~520 – 560 từ |
   | 270s (4.5 phút) | ~585 – 630 từ |

3. **Viết kịch bản 2 cột** — Theo phễu PAAST dòng thời gian linh hoạt:
   | Step | Tên | Tỷ lệ thời lượng |
   |------|-----|------------------|
   | 1 | **P — Prefer (Hook)** | 0% → ~8% (cố định 3–8s) |
   | 2 | **A — Acknowledge (Vấn đề)** | ~8% → ~25% |
   | 3 | **T — Trust (Giải pháp & Demo)** | ~25% → ~80% |
   | 4 | **S — Stick (Mở vòng lặp)** | ~80% → ~90% |
   | 5 | **A — Action (CTA mềm)** | ~90% → 100% (cố định 10–15s) |

4. **Áp dụng template** → `scripts/[STT]_[slug].md`

5. **Pre-Publish Checklist nhanh** — Tự kiểm tra trong lúc viết:
   - [ ] Đã ẩn danh tên khách hàng?
   - [ ] Không có từ ngữ giật gân?
   - [ ] Đã lồng 3 bài toán Founder vào Acknowledge?
   - [ ] Giải thích kỹ thuật dễ hiểu (ví von đời thường)?
   - [ ] CTA có cụm *"Là một nhà khởi nghiệp..."*?
   - [ ] Tổng số từ khớp thời lượng clip?

6. **Cập nhật `spec-ai.html`** — Ghi quyết định phân bổ thời gian, Visual, CTA.

### ✋ CHECKPOINT 2: Review Bản Nháp

Người dùng đọc kịch bản chi tiết và phản hồi:
- **OK** → Chuyển sang Phase 3
- **Cần sửa** → Quay lại chỉnh sửa trong Phase 2

---

## 🔍 Phase 3: REVIEW — Kiểm Duyệt & Phê Duyệt

| Mục | Chi tiết |
|-----|---------|
| **Skill tham chiếu** | [review.md](file:///Users/anderson/Desktop/works/marketing/skills/review/review.md) |
| **Template output** | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/review/template.md) |
| **Input** | Kịch bản từ `scripts/[STT]_[slug].md` |
| **Output** | `reviews/review.md` — Biên bản kiểm duyệt |

### Quy trình kiểm duyệt 3 lớp:

```text
Kịch bản chi tiết
       │
       ▼
  LỚP 1: Bảo Mật, An Toàn & Pháp Lý
  ├── Ẩn danh khách hàng
  ├── Bảo mật mã nguồn (.env, API keys)
  └── Trung thực về con số & cam kết
       │ Pass
       ▼
  LỚP 2: Giá Trị Cốt Lõi Cyberk
  ├── Tính Giải Trí (Entertainment / Hook 3s)
  ├── Tính Giáo Dục (Educational & Useful)
  ├── Tính Xác Thực (Authentic)
  └── Định vị IP & CTA lặp lại
       │ Pass
       ▼
  LỚP 3: Tiêu Chuẩn Cộng Đồng Nền Tảng
  ├── TikTok / Reels (tránh từ bóp reach)
  ├── YouTube Shorts (hook, subtitle)
  └── LinkedIn (phong thái chuyên nghiệp)
       │ Pass
       ▼
  ✅ APPROVED FOR PRODUCTION
```

### Pre-Publish Scorecard:

Chấm điểm 8 tiêu chí (1–5 điểm mỗi tiêu chí). **Yêu cầu tổng ≥ 12/40 điểm** mới được phép xuất bản.

### ✋ CHECKPOINT 3: Phê Duyệt Cuối

| Kết quả | Hành động tiếp theo |
|---------|-------------------|
| `APPROVED` (≥ 12/40) | Giao cho đội quay dựng sản xuất |
| `NEEDS_REVISION` | Quay lại Phase 2 chỉnh sửa |
| `REJECTED` | Quay lại Phase 1 chọn ý tưởng khác |

---

## 📚 Bản Đồ Tài Liệu Tham Chiếu (Reference Map)

### 📂 Tài liệu ngữ cảnh (`docs/` — đọc trước MỌI phase)

| Tài liệu | Vai trò | Đường dẫn |
|-----------|---------|-----------|
| **Audience Persona** | Chân dung khán giả "The Ambitious Builder" | [audience_profile.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/audience_profile.md) |
| **Chiến lược PAAST & VCL** | Phương pháp luận gốc — Phễu + Khung + Scorecard | [cyberk-video-strategy-paast-vcl.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/cyberk-video-strategy-paast-vcl.md) |
| **Script Make Guideline** | Hướng dẫn viết kịch bản (PAAST timeline + từ/phút) | [script-make.md](file:///Users/anderson/Desktop/works/marketing/skills/docs/script-make.md) |

### 🛠️ Skills & Templates

| Tài liệu | Vai trò | Đường dẫn |
|-----------|---------|-----------|
| **Brainstorm Skill** | Quy trình động não 10 ý tưởng | [brainstorm.md](file:///Users/anderson/Desktop/works/marketing/skills/brainstorm/brainstorm.md) |
| **Brainstorm Template** | Mẫu output cho ideas.md | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/brainstorm/template.md) |
| **Script Maker Skill** | Quy trình 4 phase end-to-end | [SKILL.md](file:///Users/anderson/Desktop/works/marketing/skills/script-maker/SKILL.md) |
| **Script Template** | Mẫu output kịch bản 2 cột | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/script-maker/template.md) |
| **Review Skill** | Quy trình kiểm duyệt 3 lớp | [review.md](file:///Users/anderson/Desktop/works/marketing/skills/review/review.md) |
| **Review Template** | Mẫu biên bản kiểm duyệt | [template.md](file:///Users/anderson/Desktop/works/marketing/skills/review/template.md) |

---

## ⚡ Quick Reference: Ai Dùng Gì, Khi Nào?

| Bạn đang ở đâu? | Dùng tài liệu nào? |
|-----------------|-------------------|
| **Bắt đầu bất kỳ phase nào** | 📚 **Luôn đọc `docs/` trước** (audience, PAAST-VCL, script-make) |
| Mới bắt đầu, chưa có gì | **Phase 0** → `script-maker/SKILL.md` (Init) |
| Có tài liệu thô, cần lên ý tưởng | **Phase 1** → `brainstorm/brainstorm.md` |
| Đã chọn ý tưởng, cần viết kịch bản | **Phase 2** → `docs/script-make.md` + `script-maker/template.md` |
| Kịch bản xong, cần kiểm duyệt | **Phase 3** → `review/review.md` |
| Cần hiểu triết lý & khung đánh giá | Bất kỳ lúc nào → `docs/cyberk-video-strategy-paast-vcl.md` |

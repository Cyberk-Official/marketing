---
type: skill
name: html-diagram
description: "Quy trình thiết kế & lập trình HTML visual diagram chuyển động (Chiều rộng canvas 65% Viewport + Padding rộng rãi, English-first, Ultra-Minimalist: 1 dòng tiêu đề/component, animation delay totalDuration / N, bộ hiệu ứng fade/slide/zoom/flip, hỏi làm rõ thông số, 4 Theme Matrix, quy chuẩn tên [project-name]-[diagram-name])."
tags: [marketing, html-diagram, tiktok, youtube, b-roll, cyberk-brand, canvas-65-percent-width, padding-spacing, english-first, ultra-minimalist, 1-line-component, animation-duration, mandatory-specs]
created: 2026-07-28
---

# SKILL: HTML Diagram — Thiết Kế & Trực Quan Hóa Sơ Đồ Cho Video B-Roll

Skill này định nghĩa **tiêu chuẩn kỹ thuật, quy tắc chiều rộng 65% Viewport + Padding rộng rãi, quy tắc sử dụng Tiếng Anh bắt buộc, phong cách Ultra-Minimalist, thuật toán tính toán Animation theo tổng thời gian, hệ thống 4 Theme biến thể và quy chuẩn đặt tên đồng bộ** phục vụ việc xuất video B-roll chất lượng cao cho thương hiệu Cyberk.

---

## 📐 Quy Tắc Chiều Rộng Canvas 65% Viewport & Padding Rộng Rãi

> **⚠️ RULE VÀNG: KHUNG CANVAS SƠ ĐỒ DỌC (9:16) BẮT BUỘC CHỈ CHIẾM 65% CHIỀU RỘNG VIEWPORT.**

Khi thiết kế sơ đồ dọc 9:16 dành cho TikTok / Instagram Reels / YouTube Shorts:
* **Chiều rộng `.canvas-frame`:** Đặt `width: 65%` (hoặc `max-width: 65vw` / `max-width: 320px` đến `380px` trên màn hình 450x800).
* **Padding lề trong:** Đặt `padding: 32px 24px` ở phần thân `body`.
* **Lý do:** Giúp toàn bộ sơ đồ nằm lọt thỏm mượt mượt ở chính giữa màn hình di động, tạo khoảng thở (white-space) sang trọng và **tuyệt đối không bị che bởi các nút UI của TikTok/Reels** (nút Like, Comment, Share, Avatar ở cạnh phải và Caption ở cạnh dưới).

```css
body.theme-vertical-dark, body {
    background-color: #07080c;
    color: #ffffff;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 32px 24px;
}

.canvas-frame {
    width: 65%;
    max-width: 340px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}
```

---

## 🌐 Quy Tắc Bắt Buộc Sử Dụng Tiếng Anh (English-First Rule)

> **⚠️ RULE VÀNG: TOÀN BỘ NỘI DUNG VĂN BẢN TRONG SƠ ĐỒ BẮT BUỘC PHẢI DÙNG TIẾNG ANH (ENGLISH ONLY).**

* ❌ **Tránh (Tiếng Việt):** `Phản hồi AI < 1s`
* ✅ **Chuẩn (Tiếng Anh):** `AI Response < 1s`

---

## 🎯 Phong Cách Tối Giản Văn Bản (Ultra-Minimalist Text Rule)

> **⚠️ RULE: MỖI COMPONENT CHỈ GIỮ LẠI DUY NHẤT 1 DÒNG TIÊU ĐỀ CỐT LÕI (1-Line Core Value).**

Không ôm đồm nhiều đoạn văn hay tiêu đề phụ rườm rà.

---

## ⏱️ Thuật Toán Tính Animation Theo Tổng Thời Gian (Total Duration Staggering)

Mọi khối Component trong sơ đồ **BẮT BUỘC PHẢI CÓ EFFECT ANIMATION XUẤT HIỆN**. Thời gian trễ xuất hiện (`animation-delay`) của từng Component được tính tự động theo công thức:

$$\text{Step Interval} = \frac{\text{Total Duration}}{\text{Total Components}}$$

---

## 🎭 Bộ Hiệu Ứng Chuyển Động (Animation Effect Presets)

Sơ đồ hỗ trợ 5 bộ hiệu ứng phổ biến: `fade-in`, `slide-up`, `slide-left`, `zoom-in`, `flip`.

---

## ⚠️ Quy Tắc Bắt Buộc & Giao Tiếp Người Dùng (Mandatory Prompt Rule)

Nếu người dùng không cung cấp `totalDuration` và `animationEffect`, mặc định chọn `5s` & `fade-in` và **BẮT BUỘC HỎI XÁC NHẬN LẠI**.

---

## 🎨 Hệ Thống 4 Theme & Layout Biến Thể (4 Diagram Theme Matrix)

1. `theme-vertical-dark` (Dọc 9:16 Tối, Canvas Width 65%)
2. `theme-vertical-light` (Dọc 9:16 Sáng, Canvas Width 65%)
3. `theme-horizontal-dark` (Ngang 16:9 Tối)
4. `theme-horizontal-light` (Ngang 16:9 Sáng)

---

## 🏷️ Quy Chuẩn Đặt Tên Bắt Buộc (Naming Conventions)

* **HTML Diagram:** `[project-name]-[diagram-name].html`
* **Video MP4 Bàn Giao:** `videos/[project-name]-[diagram-name].mp4`

---

## 🎨 Sub-Skill Đi Kèm: Logo Extraction

👉 **[skills/logo-extraction/SKILL.md](file:///Users/anderson/Desktop/works/marketing/skills/html-diagram/skills/logo-extraction/SKILL.md)**

---
type: skill
name: logo-extraction
description: "Sub-skill tìm kiếm, trích xuất và nhúng logo chính hãng (Real Brand SVGs / Vector Icons) cho các component trong HTML Diagram (SimpleIcons, SVGL, Clearbit Logo API, Inline SVG)."
tags: [marketing, html-diagram, logo-extraction, svg, brand-assets, vector-icons]
created: 2026-07-28
---

# SUB-SKILL: Logo Extraction — Trích Xuất & Nhúng Logo Chính Hãng Cho HTML Diagram

Sub-skill này được trigger khi cần **tìm kiếm, tải về và nhúng logo thật (Authentic Vector SVGs / Clean Logos)** của các dịch vụ, nền tảng, công ty công nghệ vào các khối component trong HTML Diagram.

---

## 🎯 Nguyên Tắc Logo Chuẩn Thương Hiệu

1. **KHÔNG dùng icon Emoji hoặc chữ viết tắt tạm bợ** (như 📝, ⚡, 🗣️, `V`, `LK`, `11`) cho các thương hiệu có sẵn trên thị trường.
2. **Ưu tiên Inline Vector SVG:** Nhúng trực tiếp mã `<svg>` vào file HTML `.logo-box` để trình duyệt render tức thì mà không phụ thuộc vào kết nối mạng khi quay video tự động (`browser_subagent`).
3. **Trong suốt & Tương phản cao:** Logo SVG phải có background dạng trong suốt (`transparent`), hiển thị màu gốc thương hiệu hoặc màu trắng (`#ffffff`) nổi bật trên nền tối Cyberk Dark (`#07080c`).

---

## 🔍 5 Nguồn Trích Xuất Logo Chính Hãng

Khi cần tìm logo của bất kỳ công nghệ / dịch vụ nào, hãy truy vấn theo thứ tự ưu tiên:

| Nguồn | URL Pattern / API | Ví dụ |
|-------|-------------------|-------|
| **1. Simple Icons CDN** *(Vector SVG)* | `https://cdn.simpleicons.org/[brand]` | `https://cdn.simpleicons.org/openai/white`<br/>`https://cdn.simpleicons.org/cloudflare`<br/>`https://cdn.simpleicons.org/googlecalendar` |
| **2. SVGL Repository** *(Modern Tech Logos)* | `https://svgl.app` | OpenAI, Deepgram, Cloudflare, Supabase, Neon DB, Vercel |
| **3. VectorLogoZone** *(Clean SVGs)* | `https://www.vectorlogo.zone/logos/[brand]/[brand]-icon.svg` | `https://www.vectorlogo.zone/logos/twilio/twilio-icon.svg`<br/>`https://www.vectorlogo.zone/logos/google/google-icon.svg` |
| **4. Clearbit Logo API** *(PNG Fallback)* | `https://logo.clearbit.com/[domain.com]` | `https://logo.clearbit.com/retellai.com`<br/>`https://logo.clearbit.com/telnyx.com` |
| **5. Google Brand Assets** | Inline SVG Official Logos | Google Calendar, Google Sheets, Gmail |

---

## 📚 Bảng Tra Cứu Logo SVG Các Công Nghệ Phổ Biến

### 1. Cloudflare Workers
```html
<svg viewBox="0 0 24 24" width="24" height="24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM19 18H6c-2.21 0-4-1.79-4-4 0-2.05 1.53-3.76 3.56-3.97l1.07-.11.5-.95C8.08 7.14 9.94 6 12 6c2.62 0 4.88 1.86 5.39 4.43l.3 1.5 1.53.11c1.56.1 2.78 1.41 2.78 2.96 0 1.65-1.35 3-3 3z" fill="#F38020"/></svg>
```

### 2. OpenAI / GPT-4o
```html
<svg viewBox="0 0 24 24" width="24" height="24"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729z" fill="#ffffff"/></svg>
```

### 3. Telnyx BYO SIP
```html
<svg viewBox="0 0 24 24" width="24" height="24"><path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.8L19.2 8 12 11.6 4.8 8 12 4.8zM4 9.6l7 3.5v6.8l-7-3.5V9.6zm16 6.8l-7 3.5v-6.8l7-3.5v6.8z" fill="#00E599"/></svg>
```

### 4. Google Calendar
```html
<svg viewBox="0 0 24 24" width="24" height="24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2zm-7 5h5v5h-5z" fill="#4285F4"/></svg>
```

### 5. Google Sheets
```html
<svg viewBox="0 0 24 24" width="24" height="24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zM7 7h10v2H7zm0 4h10v2H7zm0 4h7v2H7z" fill="#0F9D58"/></svg>
```

---

## 🛠️ Workflow Nhúng Logo Vào HTML Diagram

1. **Xác định danh sách thương hiệu cần nhúng:** Liệt kê tất cả các hãng có trong sơ đồ (ví dụ: Retell AI, Telnyx, OpenAI, Deepgram, Cloudflare, Google Calendar).
2. **Trích xuất SVG chính hãng:** Sử dụng cdn `cdn.simpleicons.org` hoặc tải mã SVG từ Simple Icons / SVGL.
3. **Dọn dẹp mã SVG:** Giữ lại thẻ `<svg viewBox="..." width="..." height="...">`, xóa các thuộc tính style cứng không cần thiết, thiết lập màu fill chính xác (`fill="#EC2B39"` cho Cyberk Red hoặc `fill="#ffffff"`).
4. **Bọc trong khung `.logo-box`:**
   ```html
   <div class="logo-box">
       <!-- Dynamic Inline SVG -->
       <svg viewBox="0 0 24 24">...</svg>
   </div>
   ```

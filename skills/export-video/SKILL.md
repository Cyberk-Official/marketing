---
type: skill
name: export-video
description: "Quy trình tự động quay màn hình & xuất video MP4 (H.264, kích thước Viewport trình duyệt 9:16 Native Portrait 450x800 khi quay cho các diagram tiêu chuẩn và 16:9 Landscape cho Mermaid chart)."
tags: [marketing, export-video, browser-subagent, native-viewport-9-16, screen-recording, mp4-video, 9-16-portrait, h264, video-production, b-roll]
created: 2026-07-28
---

# SKILL: Export Video — Quy Trình Tự Động Quay Màn Hình Native Viewport 9:16 & Xuất Video MP4

Skill này định nghĩa **quy trình tự động hóa quay video màn hình trình duyệt (Screen Recording)** từ các trang sơ đồ HTML tương tác (`html-diagram`) với kích thước **Viewport trình duyệt 9:16 Native Portrait (450x800)** ngay từ khi mở trình duyệt, tự động chuyển đổi sang chuẩn **MP4 (H.264)** phục vụ dựng video TikTok/Shorts.

---

## 📐 Quy Định Kích Thước Viewport Trình Duyệt Khi Quay (Browser Viewport 9:16)

1. **Sơ đồ tiêu chuẩn (HTML Diagrams):**  
   BẮT BUỘC thiết lập kích thước Viewport trình duyệt về chuẩn **9:16 PORTRAIT (450x800 pixels)** ngay trước khi bắt đầu quay. Việc này giúp khung hình video ghi nhận đúng 100% tỷ lệ dọc của điện thoại di động mà không cần cắt xúp hậu kỳ.
2. **Sơ đồ Mermaid phức tạp (Mermaid Charts):**  
   Giữ nguyên Viewport **16:9 LANDSCAPE (1280x720 pixels)** để đảm bảo đọc rõ các chữ và nút kết nối.

---

## 🏷️ Danh Sách Video MP4 Đã Xuất Bàn Giao (`videos/`)

| File Sơ Đồ Gốc | Viewport Quay Native | File Video MP4 Xuất Ra Trong `videos/` |
|----------------|----------------------|----------------------------------------|
| `ai-telemarketing-client-needs.html` | 📱 **9:16 Native (450x800)** | `videos/ai-telemarketing-client-needs.mp4` |
| `ai-telemarketing-user-flow.html` | 📱 **9:16 Native (450x800)** | `videos/ai-telemarketing-user-flow.mp4` |
| `ai-telemarketing-tech-flow.html` | 📱 **9:16 Native (450x800)** | `videos/ai-telemarketing-tech-flow.mp4` |
| `ai-telemarketing-ecosystem.html` | 📱 **9:16 Native (450x800)** | `videos/ai-telemarketing-ecosystem.mp4` |
| `ai-telemarketing-mermaid-architecture.html` | 🖥️ **16:9 Native (1280x720)** | `videos/ai-telemarketing-mermaid-architecture.mp4` |

---

## 🔄 Quy Trình 3 Bước Thực Thi Xuất Video Native 9:16

### Bước 1: Gọi `browser_subagent` Đổi Kích Thước Viewport 9:16
Truyền chỉ thị rõ ràng trong Task của `browser_subagent`:
> *"Resize browser window/viewport to **450x800** (9:16 Portrait aspect ratio). Navigate to file:///path/to/[project-name]-[diagram-name].html and record animation..."*

### Bước 2: Chuyển Đổi Sang Chuẩn MP4 (H.264)
Chạy công cụ chuyển đổi tự động sẵn có của workspace:

```bash
cd /Users/anderson/Desktop/works/tools/converter-test
bun convert-to-mp4.js <path-to-webp-recording> <path-to-output-mp4>
```

### Bước 3: Bàn Giao Thư Mục (`videos/`)
File MP4 tỷ lệ Native 9:16 được lưu trực tiếp vào `marketing/contents/[project-name]/videos/`.

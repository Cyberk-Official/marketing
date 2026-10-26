---
type: readme
tags: [services, index, marketing]
created-date: 2026-10-06
updated-date: 2026-10-14
author: neo
---

# Cyberk Services

Đây là nơi mô tả các dịch vụ Cyberk đang bán. Website, proposal, deck và nội dung sale đều lấy thông tin dịch vụ từ folder này.

> Quy tắc cho AI agent khi làm việc trong folder: [AGENTS.md](source-code-rescue/AGENTS.md)

---

## Danh sách dịch vụ

| Dịch vụ | File chính | Hình thức | Giá (theo file chính) | Trạng thái |
|---|---|---|---|---|
| **Product Design** | [product-design.md](./product-design/product-design.md) | Trọn gói | $5,000 / $7,000 / $8,000 | chưa có `status` |
| **Product Build** | [product-build.md](./product-build/product-build.md) | Trọn gói, 30 ngày | chưa ghi giá trong file | chưa có `status` |
| **Zero to Product** | [zero-to-product.md](./zero-to-product%20/zero-to-product.md) | Theo tháng, tối thiểu 2 tháng | $5,000/tháng + role thêm | chưa có `status` |
| **Tech Labs** | [tech-labs.md](./techlab/tech-labs.md) | Thuê team theo tháng, tối thiểu 3 tháng | chưa ghi giá trong file | chưa có `status` |
| **Source Code Rescue** | [source-code-rescue.md](./source-code-rescue/source-code-rescue.md) | Health Check / Audit / Implement | $500 / $5,000 / $3,000 mỗi dev mỗi tháng | `draft`, voice-check `pending` |
| **QA as a Service** | [qa-as-a-service.md](./qa-as-a-service/qa-as-a-service.md) | Gói 3 hoặc 6 tháng, trả trước toàn bộ, E2E test + báo cáo thứ Sáu | $5,000 / 3 tháng · $9,000 / 6 tháng (QA Engineer dedicated: $2,500/tháng) | `draft`, voice-check `passed` |

Giá chính thức chỉ nằm trong file chính của từng dịch vụ. Bảng trên chỉ là bản chép lại để tra nhanh. Khi hai chỗ lệch nhau, file chính đúng.

---

## Dịch vụ nào cho bài toán nào

| Bài toán của dự án | Dịch vụ |
|---|---|
| Có ý tưởng, cần thiết kế UX/UI trước khi code | Product Design |
| Có thiết kế và scope rõ, cần build xong trong 30 ngày | Product Build |
| Có ý tưởng, scope còn thay đổi, muốn build theo vòng lặp hàng tháng | Zero to Product |
| Đã có sản phẩm, cần team phát triển lâu dài | Tech Labs |
| Đã có source code, đang gặp bug, chậm, khó mở rộng hoặc không ai hiểu code | Source Code Rescue |
| Sản phẩm đang chạy, cần kiểm tra E2E đều đặn trước mỗi lần release (tính năng, thiết bị, layout) | QA as a Service |

Các dịch vụ nối tiếp nhau. Product Design hoặc Zero to Product dẫn sang Product Build. Product Build và Source Code Rescue đều có thể chuyển tiếp sang Tech Labs, vì team đã quen codebase.

---

## Cấu trúc folder

```
services/
├── readme.md                    # File này: mục lục dịch vụ
├── AGENTS.md                    # Quy tắc cho AI agent
├── product-design/
│   └── product-design.md
├── product-build/
│   └── product-build.md
├── zero-to-product /             # ⚠️ tên folder đang có dấu cách ở cuối
│   ├── zero-to-product.md
│   └── zero-to-product.pdf      # Bản PDF xuất từ file .md
├── techlab/
│   └── tech-labs.md
├── source-code-rescue/
│   ├── source-code-rescue.md          # Mô tả dịch vụ (trang web)
│   ├── source-code-rescue-message.md  # Headline quảng cáo, email, tagline
│   └── Landing page-html/             # Mockup landing page (chỉ để tham chiếu thiết kế)
└── archived/                    # Dịch vụ cũ đã ngừng bán
```

---

## Dịch vụ đã ngừng (`archived/`)

| File | Ghi chú |
|---|---|
| `ai-powered-studio.md`, `ai-powered-studio-en.md` | Bản cũ, tiếng Việt và tiếng Anh |
| `community-development-service.md` | Dịch vụ phát triển cộng đồng |
| `kick-starter-marketing-service.md` | Marketing khởi động |
| `mvp-development-service.md` | Thay bằng Product Build và Zero to Product |
| `tech-lab-service.md` | Bản cũ của Tech Labs |

Chỉ dùng để tra lịch sử. Không lấy nội dung từ đây để viết website hay proposal.

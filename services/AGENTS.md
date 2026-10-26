---
trigger: glob
glob: marketing/services/**
description: Quy tắc cho AI agent khi đọc, viết, sửa mô tả dịch vụ Cyberk
created-date: 2026-10-06
updated-date: 2026-10-06
author: neo
---

# AGENTS.md — `marketing/services/`

Folder này là nguồn sự thật duy nhất về các dịch vụ Cyberk: dịch vụ gồm gì, giá bao nhiêu, dành cho bài toán nào. Website (`cyberk-io-static/`), proposal (`bootstrap/`), deck và nội dung sale đều lấy thông tin từ đây.

Mục lục dịch vụ: [readme.md](./readme.md)

---

## 1. Cấu trúc

Mỗi dịch vụ có một folder riêng. Trong folder có một file chính trùng tên folder.

```
services/<service-slug>/
├── <service-slug>.md            # Bắt buộc. Mô tả dịch vụ, dùng cho trang web
├── <service-slug>-message.md    # Tuỳ chọn. Headline quảng cáo, email, tagline
├── <service-slug>.pdf           # Tuỳ chọn. Bản xuất từ file .md
└── landing-page-html/           # Tuỳ chọn. Mockup thiết kế landing page
```

| Quy tắc | Chi tiết |
|---|---|
| Tên folder và file | `kebab-case`, tiếng Anh, không dấu cách, không chữ hoa |
| File chính | Chỉ một file mô tả dịch vụ cho mỗi folder |
| Dịch vụ đã ngừng | Chuyển file vào `archived/`, không xoá |
| Không để ở đây | Proposal cho từng đối tác cụ thể → `bootstrap/` hoặc `clients/` |

> Một số folder hiện chưa theo quy tắc (`techlab/`, `zero-to-product /`, `Landing page-html/`). **Không tự ý đổi tên.** Báo Anderson và chờ duyệt, vì đổi tên folder làm gãy link ở các file khác.

---

## 2. Frontmatter bắt buộc

```yaml
---
type: mkt
tags: [service, <service-slug>, ...]
created-date: YYYY-MM-DD
updated-date: YYYY-MM-DD
author: <tên>
status: draft            # draft | ready | published
voice-check: pending     # pending | passed YYYY-MM-DD
---
```

- Sửa file → cập nhật `updated-date`. Không đổi `created-date`.
- File cũ thiếu trường → bổ sung khi có dịp sửa file đó.

---

## 3. Viết nội dung

Mọi file trong folder này là nội dung marketing, nên phải theo [writing-rules.md](../skills/docs/writing-rules.md).

| Bước | Việc |
|---|---|
| Trước khi viết | Đọc `writing-rules.md` |
| Khi viết | Website dùng "we"/"chúng tôi". Không dùng từ trong danh sách cấm (§7) |
| Trước khi giao | Chạy 6 bài kiểm tra (§6), rồi ghi `voice-check: passed <ngày>` |

- Trang dịch vụ cho website viết bằng **tiếng Anh**. Ghi chú nội bộ, file `-message.md` có thể viết tiếng Việt.
- Không đổi `status` sang `published` khi `voice-check` còn `pending`.
- Mô tả dịch vụ theo **bài toán dự án đang gặp và kết quả họ muốn**, không theo danh tính người mua (founder, startup, team nhỏ...).

---

## 4. Giá và con số

- **Giá chỉ có một nguồn:** file chính của dịch vụ. `readme.md` chép lại để tra nhanh.
- Đổi giá trong file chính → cập nhật bảng trong `readme.md` **ngay trong cùng lần sửa**.
- Không tự đặt hoặc tự đổi giá. Giá do Anderson quyết định.
- Mọi con số (thời gian, %, số dự án) phải có nguồn đo được, theo §8 của `writing-rules.md`. Số dự án và số năm lấy từ `positioning.md`.

---

## 5. Link giữa các dịch vụ

Dùng đường dẫn tương đối tính từ vị trí file:

```markdown
[Tech Labs](../techlab/tech-labs.md)
```

Không dùng `[Tech Labs](tech-labs.md)`, vì các file giờ nằm ở folder khác nhau.

---

## 6. Thêm hoặc ngừng một dịch vụ

**Thêm dịch vụ mới**
1. Tạo `services/<service-slug>/<service-slug>.md` với frontmatter ở §2, `status: draft`
2. Thêm một dòng vào bảng "Danh sách dịch vụ" và "Dịch vụ nào cho bài toán nào" trong `readme.md`
3. Báo Anderson duyệt trước khi đưa lên website

**Ngừng dịch vụ**
1. Chuyển file chính vào `archived/`
2. Xoá dòng khỏi bảng dịch vụ trong `readme.md`, thêm vào bảng `archived/`
3. Tìm các file đang link tới dịch vụ đó (`grep -rn "<service-slug>" marketing/`) và báo Anderson

---

## 7. Không được làm

- Không sửa file trong `landing-page-html/` (hoặc `Landing page-html/`). Đó là bản xuất từ công cụ thiết kế, chỉ dùng để tham chiếu
- Không lấy nội dung từ `archived/` để viết website hay proposal
- Không ghi tên thật đối tác, giá hợp đồng thật vào mô tả dịch vụ
- Không commit, push hay deploy (theo `AGENTS.md` gốc)

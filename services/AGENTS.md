---
trigger: glob
glob: marketing/services/**
description: Quy tắc cho AI agent khi đọc, viết, sửa mô tả dịch vụ Cyberk
created-date: 2026-10-06
updated-date: 2026-11-23
author: neo
---

# AGENTS.md — `marketing/services/`

Folder này là nguồn sự thật duy nhất về các dịch vụ Cyberk đang cung cấp: dịch vụ gồm gì, giá bao nhiêu, dành cho bài toán nào. Website (`cyberk-io-static/`), proposal (`bootstrap/`, `proposal/`), deck và nội dung sale đều lấy thông tin từ đây.

Mục lục & bảng tra cứu nhanh dịch vụ: [readme.md](./readme.md)

---

## 1. Cấu trúc

Mỗi dịch vụ cốt lõi có một folder riêng (`design-6-days/`, `zero-to-product/`, `tech-labs/`, `source-code-rescue/`).

```
services/<service-slug>/
├── <service-slug>.md                  # Mô tả dịch vụ dạng Markdown (dùng cho web & AI đọc nhanh)
├── cyberk-<name>-en.html / .pdf       # Tuỳ dịch vụ: Brochure A4 chính thức gửi đối tác
├── <name>-client-en.md / -vi.md       # Tuỳ chọn: Bản tóm tắt quy trình từ brochure HTML
├── <service-slug>-message.md          # Tuỳ chọn: Headline quảng cáo, email, tagline
├── proposal/                          # Tuỳ chọn: Mẫu proposal / slide chuẩn của riêng dịch vụ
└── landing-page-html/                 # Tuỳ chọn: Mockup thiết kế landing page tham chiếu
```

| Quy tắc | Chi tiết |
|---|---|
| Tên folder và file mới | `kebab-case`, tiếng Anh, không dấu cách, không chữ hoa |
| File nguồn chính | Mỗi dịch vụ lấy `<service-slug>.md` hoặc brochure tiếng Anh `.html` làm nguồn chuẩn (chỉ rõ trong `readme.md`) |
| Gói bổ trợ (Add-ons) | Các gói đi kèm như *Teaser Video*, *Care+* nếu chưa tách folder riêng thì niêm yết tại brochure gốc và bảng mục lục `readme.md` |
| Dịch vụ đã ngừng | Chuyển nguyên folder hoặc file vào `archived/`, không xoá trắng |
| Không để ở đây | Proposal viết riêng cho từng đối tác cụ thể → `bootstrap/` hoặc `clients/` |

> Thư mục `source-code-rescue/Landing page-html/` hiện chưa theo quy tắc `kebab-case`. **Không tự ý đổi tên.** Báo Anderson và chờ duyệt trước khi đổi vì sẽ làm gãy đường dẫn tài nguyên bên trong.

---

## 2. Frontmatter bắt buộc (cho file `.md`)

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
| Khi viết | Website / tài liệu dùng "we"/"chúng tôi". Không dùng từ trong danh sách cấm (§7) |
| Trước khi giao | Chạy 6 bài kiểm tra (§6), rồi ghi `voice-check: passed <ngày>` |

- Trang dịch vụ cho website viết bằng **tiếng Anh**. Ghi chú nội bộ, bản hướng dẫn tiếng Việt (`-vi.md`), file `-message.md` có thể viết tiếng Việt.
- Không đổi `status` sang `published` khi `voice-check` còn `pending`.
- Mô tả dịch vụ theo **bài toán dự án đang gặp và kết quả họ muốn**, không theo danh tính người mua (founder, startup, team nhỏ...).

---

## 4. Giá và con số

- **Nguồn giá chính thức:** Nằm trong tài liệu gốc của từng dịch vụ (file `.md` chính hoặc brochure `.html`) và được tổng hợp tại `readme.md` (cùng bảng giá chung trong `marketing/services/`) để tra nhanh.
- Đổi giá dịch vụ → cập nhật đồng bộ cả file gốc của dịch vụ và bảng trong `readme.md` **ngay trong cùng đợt sửa**.
- Không tự đặt hoặc tự đổi giá. Mọi mức giá (trọn gói, giá khởi điểm *"Starting at..."*, đơn giá nhân sự theo tháng) đều do Anderson quyết định.
- Mọi con số (thời gian, %, số dự án) phải có nguồn đo được theo §8 của `writing-rules.md`. Số dự án và số năm lấy từ `positioning.md`.

---

## 5. Link giữa các dịch vụ

Dùng đường dẫn tương đối tính từ vị trí file:

```markdown
[Tech Labs](../tech-labs/tech-labs.md)
```

Không dùng `[Tech Labs](tech-labs.md)`, vì các file nằm ở các folder riêng biệt.

---

## 6. Thêm hoặc ngừng một dịch vụ

**Thêm dịch vụ mới**
1. Tạo `services/<service-slug>/` kèm tài liệu gốc (`.md` có frontmatter ở §2 với `status: draft`, hoặc brochure `.html` + client guide)
2. Thêm vào bảng "Danh sách dịch vụ", "Dịch vụ nào cho bài toán nào" và cây "Cấu trúc folder" trong `readme.md`
3. Báo Anderson duyệt trước khi đưa lên website hoặc gửi đối tác

**Ngừng dịch vụ**
1. Chuyển folder hoặc file của dịch vụ vào `archived/`
2. Xoá dòng khỏi bảng dịch vụ đang bán trong `readme.md`, thêm vào bảng `Dịch vụ đã ngừng (archived/)`
3. Tìm các file đang link tới dịch vụ đó (`grep -rn "<service-slug>" marketing/`) và báo Anderson xử lý link đứt

---

## 7. Không được làm

- Không tự ý sửa các file brochure `.html` / `.pdf` đã dàn trang A4 hoặc các file trong `landing-page-html/` (`Landing page-html/`) khi chưa có lệnh trực tiếp từ Anderson
- Không lấy nội dung hay đơn giá từ `archived/` để viết website, bảng giá hoặc proposal
- Không ghi tên thật đối tác, giá hợp đồng riêng của từng đối tác vào mô tả dịch vụ chung
- Không commit, push hay deploy (theo `AGENTS.md` gốc)

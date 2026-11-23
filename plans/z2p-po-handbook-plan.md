---
type: plan
tags: [plan, zero-to-product, product-owner, handbook, customer-journey, service-overview]
created-date: 2026-11-02
updated-date: 2026-11-02
author: anderson
status: draft
---

# Kế hoạch: Service Overview, bộ tài liệu PO cho Zero to Product, và Customer Journey

## Mục tiêu

1. **Service Overview (nội bộ):** cả team hiểu quy trình dịch vụ của Cyberk, từ Source Code Rescue tới Zero to Product tới Retainer. Sơ đồ quy trình được vẽ lại trong file Markdown. Bản này chi tiết, dành cho người trong Cyberk.
2. **Tài liệu PO:** PO đọc handbook là đủ để dẫn một dự án Zero to Product (Z2P) với khách hàng, từ lúc ký hợp đồng tới khi chuyển sang Retainer.
3. **Customer Journey (cho khách):** PO trình bày trong buổi kick-off để khách hiểu cách Cyberk làm việc. Bản này gọn hơn Service Overview, viết theo góc nhìn của khách.

Cách làm: đi từng phần. Mỗi phần viết xong file thì Anderson duyệt, rồi mới sang phần tiếp theo. **Mỗi lần chỉ hỏi một câu.**

---

## 1. Quy trình theo sơ đồ (đã chốt cách hiểu, 02/11/2026)

Nguồn: sơ đồ "Source Code Rescue → Zero-To-Product → Retainer" (Anderson gửi 02/11/2026). Sơ đồ này là nguồn đúng. Trang dịch vụ sẽ sửa theo sau.

| Chặng | Ai làm | Việc chính | Ghi chú |
|---|---|---|---|
| (Lối vào phụ) Source Code Rescue | Team Asimov | Audit source code | Dự án đã có code thì đi qua audit trước, rồi mới vào Bước 1 |
| **Bước 1** | PO | Chốt design tới khi khách hài lòng, viết clear specs | Có Design UX/UI hỗ trợ. Thường mất khoảng 1 tuần, nhanh hay chậm tuỳ việc chốt specs |
| **Bước 2** | Team Asimov (Senior) | Dựng base | Contract, Infra, Repo, Bảo mật, Phân tích dữ liệu |
| **Bước 3** | Devs | Đắp skin, làm custom functions | Gọi khách mỗi ngày để demo. Vòng "Daily revise" quay lại Bước 3 |
| **QA** | QA | Run test & validate | |
| **Bước 4** | Devs | Launch, bàn giao | Sau đó Distil phần dùng chung về Cyberk Platform |
| **Retainer** | Maintainer (tất cả developer) | Bảo trì, phát triển tiếp | Cả dự án của khách và dự án nhà làm đều đi vào Retainer |

### Những điều Anderson đã chốt

- **PO và Product Lead là một.** Dùng chữ **PO** ở mọi nơi.
- **Kick-off linh hoạt.** Khi khách cần nhanh, team làm design (Bước 1) và giấy tờ cùng lúc. Kick-off không bắt buộc phải đợi PRD.
- **Asimov** là nền tảng AI-native do Cyberk phát triển để làm phần mềm từ đầu tới cuối. **Team Asimov** là team xây Asimov, và cũng dùng Asimov để dựng base, bảo trì, audit... Đây là team giỏi nhất của Cyberk.
- **Giá Z2P tăng lên $10,000/tháng.** Thời gian Bước 1 tuỳ dự án, thường khoảng 1 tuần.
- **Cyberk Platform Distil:** sau mỗi dự án, Cyberk viết thêm code template dùng chung, linh hoạt hơn, để khởi tạo dự án sau nhanh hơn (ví dụ: làm xong một launchpad thì có template launchpad cho dự án mới). Template **viết mới, không dùng code của khách**. Mục đích: khách đến sau được hưởng lợi thế.
- **Dự án nhà làm** (sản phẩm nội bộ của Cyberk) cũng đi vào Retainer.
- **Service Overview là để nội bộ hiểu quy trình**, nên chi tiết hơn. **Customer Journey là để khách hiểu cách Cyberk làm**, dùng trong buổi kick-off.

---

## 2. Rà soát handbook hiện có

### Đã có, dùng được cho Z2P

| Tài liệu | Phục vụ chặng | Tình trạng |
|---|---|---|
| `09-sales/sales-first-call/` | Trước hợp đồng | Tốt. Cần sửa giá và chữ Product Lead |
| `00-account/team-chat-groups/` | Ngay khi khách đồng ý | Dùng được |
| `05-product-owner/po-planning/` | Trước Bước 3 | Đang giả định PRD có sẵn → phải sửa |
| `05-product-owner/po-kick-off/` | Đầu dự án | Giọng văn và mẫu tốt. Chưa có Customer Journey, chưa có các chặng Z2P |
| `05-product-owner/po-board-create/`, `board-handbook/` | Bước 3 | Dùng được |
| `04-developer/dev-daily-report/`, `dev-daily/` | Bước 3 | Viết cho dev, PO chỉ cần link tới |
| `04-developer/dev-write-brd/` | Bước 3 (yêu cầu phát sinh) | Dùng được |
| `04-developer/dev-new-repo/` | Bước 2 | Viết cho dev |
| `06-qa/qa-bugs-handling/`, `qa-bugs-logs/` | QA | Chưa có bước nghiệm thu trước launch |
| `05-product-owner/po-handover/` | Bước 4 | Tốt. Bảo trì miễn phí 30 ngày |
| `01-cyberk-way/5.1-sprint-mot-ngay.md` | Bước 3 | Triết lý vòng phản hồi hằng ngày |

### Còn thiếu

| # | Thiếu | Chặng |
|---|---|---|
| T0 | **Service Overview nội bộ**, có sơ đồ quy trình vẽ lại bằng Mermaid | Toàn bộ |
| T1 | Trang hành trình PO trong Z2P: PO làm gì ở từng chặng, các điều kiện để chuyển chặng (link tới Service Overview, không chép lại) | Toàn bộ |
| T2 | Chốt design và specs với khách: số vòng sửa, cách xin duyệt, mẫu sign-off, mẫu spec | Bước 1 |
| T3 | Bàn giao từ PO sang Team Asimov: PO giao gì, cần xin khách những gì (tài khoản, domain, quyền truy cập) | Bước 2 |
| T4 | Họp demo hằng ngày nhìn từ phía PO: dẫn buổi call, ghi nhận góp ý, xử lý khi khách đổi ý | Bước 3 |
| T5 | Bước nghiệm thu trước launch: tiêu chí QA pass, khách xác nhận | QA |
| T6 | Checklist launch (khác với bàn giao) | Bước 4 |
| T7 | Chuyển sang Retainer, nối với chính sách bảo trì 30 ngày | Retainer |
| T8 | Customer Journey cho buổi kick-off | Kick-off |
| T9 | Báo cáo tuần và retro tháng (trang dịch vụ có hứa, handbook chưa có) | Bước 3 |

### Đang lệch nhau

| # | Chỗ lệch | Trạng thái |
|---|---|---|
| L1 | Sơ đồ có 4 bước + QA, đi một chiều. `zero-to-product.md` lại mô tả vòng lặp 5 bước | Đã chốt: theo sơ đồ. Sửa trang dịch vụ ở P11 |
| L2 | "Product Lead" ↔ "PO" | Đã chốt: dùng PO. Sửa ở P2 |
| L3 | Vị trí kick-off | Đã chốt: linh hoạt. Sửa ở P6 |
| L4 | Nhịp báo cáo: trang dịch vụ có report tuần, stress-test tuần, retro tháng; handbook chưa có | Làm ở P8 |
| L5 | `01-cyberk-way/2.4` vẫn ghi MVP Development (đã ngừng bán) và Tech-Lab | Báo Anderson ở P11 |
| L6 | `services/readme.md` trỏ tới `zero-to-product /` (có dấu cách), nhưng tên folder thật là `zero-to-product/` | Sửa link ở P3 |
| L7 | Giá Z2P vẫn ghi $5,000 ở nhiều nơi | Đã chốt: $10,000. Sửa ở P3 |

---

## 3. Lỗi tìm thấy khi rà soát (02/11/2026)

### "Product Lead" → "PO"

| File | Dòng | Nội dung hiện tại |
|---|---|---|
| `handbook/09-sales/sales-first-call/client-first-call-handbook.md` | 116 | "Người đầu mối đó là **Product Lead** *(cần Anderson xác nhận)*" |
| `marketing/services/zero-to-product/zero-to-product.md` | 108 | "Strategy session with your **Product Lead** — he acts as your CTO" |
| `marketing/services/zero-to-product/zero-to-product.md` | 109 | "...milestones you and your Product Lead agreed on" |
| `marketing/content-review-2026-09.md` | 126 | Bản review cũ trích lại câu ở trên. **Không sửa** (là ghi chép lịch sử) |

Khi nói với khách bằng tiếng Anh: lần đầu viết "Product Owner (PO)", các lần sau viết "PO".

### Giá $5,000 → $10,000 (chỉ áp dụng cho Z2P)

| File | Dòng |
|---|---|
| `marketing/services/zero-to-product/zero-to-product.md` | 16, 91, 148, 150 |
| `marketing/services/readme.md` | 23 (bảng giá) |
| `handbook/09-sales/sales-first-call/client-first-call-handbook.md` | 128, 132, 212, 241 |

Không đụng tới: giá Product Design ($5,000, trong `cyberk-website-content-plan.md`), và các con số $5,000 trong ví dụ postmortem.

---

## 4. Các phần làm lần lượt

| Phần | Việc | File đầu ra (dự kiến) | Trạng thái |
|---|---|---|---|
| **P0** | Chốt cách hiểu quy trình | File này | ✅ Xong 02/11 |
| **P1** | **Service Overview nội bộ** (T0): vẽ lại sơ đồ bằng Mermaid; mô tả từng chặng, vai trò, đầu vào/đầu ra; Team Asimov; Distil; Retainer | `handbook/10-services/README.md`, `handbook/10-services/service-overview/README.md`, `service-overview-process.md`, `service-overview.svg` | 🟡 Đã viết, chờ Anderson review |
| **P2** | Sửa "Product Lead" → "PO" (bảng §3) | Sửa 2 file | Chờ |
| **P3** | Cập nhật giá Z2P $10,000 (bảng §3), sửa link L6 | Sửa 3 file | Chờ. Cần hỏi: giá các role thêm và mức tối thiểu 2 tháng có đổi không |
| **P4** | Dựng cấu trúc folder PO và template trống (Playbook §1.7) | Các folder mới trong `handbook/05-product-owner/` | Chờ |
| **P5** | Hành trình PO trong Z2P (T1) | `po-zero-to-product/` | Chờ |
| **P6** | Bước 1: chốt design và specs (T2); sửa kick-off và planning cho linh hoạt (L3) | `po-design-spec/`, sửa `po-kick-off/*`, `po-planning/*` | Chờ |
| **P7** | Bước 2: bàn giao PO → Team Asimov (T3) | `po-base-handoff/` | Chờ |
| **P8** | Bước 3: demo hằng ngày, khách đổi ý, báo cáo tuần, retro tháng (T4, T9) | `po-daily-demo/` | Chờ |
| **P9** | QA gate, launch, Retainer (T5, T6, T7) | `po-launch/`, `po-retainer/`, sửa nhẹ `po-handover/` | Chờ |
| **P10** | **Customer Journey** cho kick-off (T8), lấy nội dung từ P1 và P5–P9 | Dạng sẽ chốt khi tới phần này | Chờ |
| **P11** | Rà soát chéo: README, link, metadata; sửa `zero-to-product.md` theo sơ đồ (L1); báo L5 | Nhiều file | Chờ |

Ghi chú:
- Tên folder ở trên là đề xuất, sẽ chốt ở P4.
- Viết theo `handbook/workflow/playbook.md` và `marketing/skills/docs/writing-rules.md`. Công cụ: Telegram, GitHub Projects, Git + Markdown.
- Giá và tên folder trong `marketing/services/`: chỉ sửa theo quyết định của Anderson đã ghi trong file này. Không tự đổi tên folder.

---

## 5. Câu hỏi đang mở (hỏi lần lượt, mỗi lần một câu)

1. ~~Đặt Service Overview ở đâu?~~ → `handbook/10-services/service-overview/` (Anderson duyệt 02/11)
1b. **[Đang hỏi]** Dự án của khách sau bàn giao có đi vào Retainer không, và đi bằng cách nào? (Trên sơ đồ chỉ có "Dự án nhà làm" và Distil đi vào Retainer)
2. P3: Giá các role thêm (Extra Developer, Smart Contract, DevOps) và mức tối thiểu 2 tháng có đổi không?
3. P6: Bước 1 có giới hạn số vòng sửa design không?
4. P10: Customer Journey làm dạng deck trình chiếu hay doc?

---

## 6. Nhật ký

| Ngày | Phần | Kết quả |
|---|---|---|
| 2026-11-02 | Rà soát | Đọc sơ đồ, `zero-to-product.md`, `services/readme.md`, PO handbook, sales first-call, Cyberk Way 2.4/2.5/5.1/5.2. Viết bản kế hoạch đầu tiên |
| 2026-11-02 | P0 | Anderson trả lời 7 câu. Thêm Service Overview (P1), sửa tên PO (P2), tăng giá lên $10,000 (P3). Rà soát ra 3 chỗ "Product Lead" và 9 chỗ giá cần sửa |
| 2026-11-02 | P1 | Tạo `handbook/10-services/` và Service Overview: sơ đồ Mermaid vẽ lại từ ảnh (đã render thử, chạy được), bảng chặng, vai trò, quy tắc cứng, checklist chuyển chặng. Còn để trống: thời gian Bước 2–4, ai làm Distil, cách dự án khách vào Retainer. Chưa thêm vào `handbook/README.md` (để P11) |
| 2026-11-02 | P1 (sửa) | Anderson thấy bố cục Mermaid khác bản gốc. Vẽ lại bằng SVG (`service-overview.svg`), giữ đúng bố cục: 3 khu xếp dọc, 5 cột trong Z2P, mũi tên đi vuông góc, có vòng Daily revise. Trang Process nhúng SVG thay cho Mermaid. Sửa lỗi chính tả "Funtions" thành "Functions" |
| 2026-11-02 | P1 (style) | Chỉnh SVG theo Cyberk Guideline: font Satoshi, màu #0A071B/#717070/#D9212E/trắng, tiêu đề section viết hoa đậm có gạch dưới, nhãn cột viết hoa xám, mỗi ô có nhãn nhỏ (BƯỚC 1, AUDIT, DISTIL...). Giữ nguyên toạ độ. Căn thẳng hai chỗ lệch: nhãn QA, ô Design UX/UI |

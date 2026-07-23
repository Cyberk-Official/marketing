---
type: skill
name: brainstorm
description: "Trích xuất thông tin từ file Input (Estimate Bidding/Case study) và sáng tạo 10 ý tưởng kịch bản video ngắn chuẩn PAAST cho Cyberk."
tags: [marketing, video-script, brainstorm, paast, new-media]
created: 2026-07-22
---

# SKILL: Brainstorm 10 Ý Tưởng Video Ngắn (Input $\rightarrow$ PAAST Ideas)

Skill này hướng dẫn quy trình chuyển hóa tài liệu kỹ thuật thô (Bidding Estimate, Case Study, Solution Design) thành **10 ý tưởng kịch bản video ngắn (30–90 giây)** cho Cyberk, nhắm tới khán giả mục tiêu là **Global Founders, CTOs và B2B Tech Leaders**.

---

## 🎯 1. Nguyên Tắc Cốt Lõi & Định Vị

* **Định vị kênh IP:** *"Dev Studio kể chuyện khởi nghiệp"* — Kể chuyện thật, bài học thật, code thật, không giảng đạo lý.
* **Tôn chỉ New-Media:** 
  * **Show, Don't Tell:** Mọi ý tưởng đều phải có bằng chứng trực quan đi kèm (màn hình Cursor IDE, Terminal log, sơ đồ kiến trúc vẽ tay, Billing dashboard).
  * **Anti-Clickbait:** Nói KHÔNG với tiêu đề giật gân rẻ tiền (*"Sập hệ thống"*, *"Cơn ác mộng"*). Thay vào đó, sử dụng **con số thực tế gây bất ngờ** (*"$75/tháng"*, *"1.5s OCR"*, *"20.000 USD chống trùng đơn"*).
  * **Bảo mật tuyệt đối:** Ẩn danh hoàn toàn tên khách hàng (thay bằng *"đối tác phân phối B2B"*, *"startup logistics Singapore"*), bảo mật thông tin mã nguồn và file `.env`.

---

## 🔍 2. Quy Trình Trích Xuất Dữ Liệu Từ Input (Bidding / Estimate File)

Khi đọc một tài liệu đầu vào (ví dụ: `bootstrap/bidding/lubritrade`), AI/Content Creator phải bóc tách 4 nhóm thông tin "nguyên liệu":

1. **Nỗi đau & Vấn đề nghiệp vụ (Business Pain Points):** Khách hàng đang gặp tắc nghẽn gì? (Chi phí cloud cao, xử lý đơn thủ công tốn thời gian, sai sót dữ liệu...).
2. **Con số ấn tượng (Shocking Metrics):** Các chỉ số kỹ thuật/tài chính thực tế thu hoạch được từ bản estimate (ví dụ: Tổng chi phí server $75/tháng, thời gian xử lý giảm từ 5 phút xuống 2 giây...).
3. **Giải pháp kiến trúc & Tráo đổi kỹ thuật (Tech Trade-offs):** Cách Cyberk giải bài toán (Serverless, Durable Objects, Prompt Caching, Idempotency Guard, Microservices vs Monolith...).
4. **Bài học quản trị / Rủi ro (Founder Insights):** Những sai lầm của bên làm cũ hoặc bài học đắt giá khi chọn giải pháp công nghệ.

---

## 🧩 3. Ma Trận Phân Bổ 10 Ý Tưởng Theo Phễu PAAST

10 ý tưởng được tạo ra **PHẢI** bao phủ trọn vẹn 5 tầng tâm lý của phễu **PAAST** (`cyberk-video-strategy-paast-vcl.md`):

| Tầng PAAST | Số lượng ý tưởng | Đòn bẩy tâm lý & Khai thác |
|---|---|---|
| **P — Prefer** (Ưu tiên chọn xem) | **2 Ý tưởng** | Visual Hook mạnh trong 3s đầu với con số thực tế gây bất ngờ hoặc lỗi code thực chiến làm người xem dừng lướt. |
| **A — Acknowledge** (Đồng cảm nỗi đau) | **2 Ý tưởng** | Đánh trúng 3 bài toán lớn của Founder: *Chi phí nhàn rỗi (Zero idle cost)*, *Khả năng co giãn (Scale CCU)*, *Tích hợp legacy system*. |
| **T — Trust** (Xây dựng niềm tin) | **3 Ý tưởng** | Phân tích sâu kiến trúc công nghệ, bóc tách trade-off thực tế để chứng minh năng lực "dev studio có nghề". |
| **S — Stick** (Mở vòng lặp theo dõi) | **1 Ý tưởng** | Định dạng *Build in Public* / *Nhật ký thiết kế*, tạo tính nối tiếp khiến khán giả bấm Follow chờ tập sau. |
| **A — Action** (Hành động chuyển đổi) | **2 Ý tưởng** | Kể câu chuyện case study thực tế kết thúc bằng CTA mềm lặp lại định vị: *"Là một nhà khởi nghiệp..."*. |

---

## 📝 4. Cấu Trúc Mẫu Của Một Ý Tưởng Kịch Bản (Single Idea Card Template)

Mỗi ý tưởng trong danh sách 10 ý tưởng phải tuân thủ chuẩn format sau:

```markdown
### Ý Tưởng #[STT]: [Tên Tiêu Đề Ý Tưởng Thu Hút]
* **Tầng PAAST:** [Prefer / Acknowledge / Trust / Stick / Action]
* **Góc nhìn (Angle):** [Ví dụ: Bóc phốt chi phí / Nhật ký Founder / Tips & Tools / Architecture Breakdown]
* **Visual Hook (3s đầu):** [Mô tả chính xác cảnh quay trực quan: Màn hình IDE, terminal chạy lệnh, dashboard hóa đơn...]
* **Core Insight / Pain Point:** [Vấn đề hoặc nỗi đau cụ thể của Founder được đề cập]
* **Bằng chứng công nghệ (Show, Don't Tell):** [Công nghệ/Sơ đồ/Code sẽ đưa lên màn hình để chứng minh]
* **Key Takeaway:** [Bài học hoặc giá trị đút túi khán giả nhận được sau 60s xem]
* **CTA Mềm (nếu có):** [Mẫu lặp lại định vị Founder hoặc mời gọi thảo luận]
```

---

## 🚀 5. Hướng Dẫn Các Bước Thực Thi (Step-by-Step Execution)

1. **Bước 1 — Nạp Input:** Đọc file tài liệu trong thư mục dự án `input/` (ví dụ: `input/lubritrade-bidding.md`).
2. **Bước 2 — Trích xuất Insight:** Liệt kê các con số, kiến trúc kỹ thuật và nỗi đau nghiệp vụ từ Input.
3. **Bước 3 — Sinh 10 Ý Tưởng:** Áp dụng ma trận PAAST ở Mục 3 để viết 10 Card Ý tưởng theo mẫu ở Mục 4.
4. **Bước 4 — Xuất File Output:** Lưu kết quả vào file `brainstorm/[tên-du-an]-10-ideas.md`.

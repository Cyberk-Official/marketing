---
type: guideline
tags: [marketing, new-media, self-media, script]
created: 2026-07-20
---

# Hướng Dẫn Lên Ý Tưởng & Dựng Kịch Bản Video Ngắn (New-Media)

Tài liệu này tổng hợp các bài học kinh nghiệm cốt lõi từ các buổi thảo luận để xây dựng kịch bản video ngắn (90 giây) chuẩn định vị **"Dev Studio kể chuyện khởi nghiệp"** của Cyberk, nhắm tới đối tượng khách hàng là các **B2B Founders, CTOs, và Startup Leaders**.

---

## 🧠 1. Giai Đoạn Lên Ý Tưởng (Brainstorm)

### 👥 Xác định đúng đối tượng người nghe (Audience)
* **Khách hàng mục tiêu:** Founders, CTOs, Tech Leads của các startup hoặc doanh nghiệp B2B.
* **Tư duy nội dung:** Ít cú pháp code phức tạp hơn, tập trung nhiều hơn vào tư duy business, giải pháp kiến trúc, tối ưu hóa chi phí cloud, quản trị rủi ro vận hành, và bảo mật hệ thống.

### 🎭 Tôn trọng triết lý New-Media & Bảo mật
* **Show, Don't Tell (Trình bày bằng chứng):** Mỗi ý tưởng phải đi kèm với một bằng chứng trực quan cụ thể (sơ đồ vẽ tay, dòng code thực tế trong Cursor IDE, dashboard hóa đơn thật, tin nhắn chat). Khán giả tự quan sát và tự đưa ra kết luận về năng lực của Cyberk.
* **Giọng kể người trong cuộc:** Đóng vai trò là một kỹ sư thực chiến chia sẻ trải nghiệm thực tế (Nhật ký thiết kế/Nhật ký code). Điềm đạm, chân thực và cởi mở.
* **Tuyệt đối không lộ tên khách hàng:** Bảo mật thông tin dự án. Luôn gọi khách hàng bằng các danh xưng ẩn danh (ví dụ: *"đối tác phân phối sỉ"*, *"doanh nghiệp phân phối B2B"*).

### ❌ Nói KHÔNG với giật gân (Anti-Clickbait)
* Tránh xa các tiêu đề giật tít rẻ tiền của mạng xã hội như: *"Sập trong 1 ngày"*, *"Bay màu hotline"*, *"Cơn ác mộng"*, v.v.
* **Thay thế bằng:** Sử dụng các **con số thực tế gây bất ngờ** làm điểm nhấn tự nhiên (ví dụ: *"Hạ tầng AI giá $75/tháng"*, *"Quét hóa đơn đa ngôn ngữ trong 1.5 giây"*, *"Chống trùng đơn hàng 20.000 USD"*).

---

## 📝 2. Giai Đoạn Dựng Kịch Bản (Script Drafting)

Kịch bản video ngắn (90 giây) của Cyberk phải tuân thủ nghiêm ngặt phễu tâm lý **PAAST** và khung thực thi **VCL**:

### 📐 Định dạng Phễu PAAST trong dòng thời gian 90s

#### Step 1: P — Prefer (Hook 0 - 10s)
* **Mục tiêu:** Giữ chân người xem trong 3 giây đầu tiên.
* **Cách làm:** Show trực tiếp con số thực tế gây tò mò làm điểm nhấn.
* *Ví dụ:* Cận cảnh dashboard hóa đơn billing thực tế `$75.02` và nói: *"75 USD một tháng. Đây là toàn bộ chi phí vận hành server và API của một hệ thống AI..."*

#### Step 2: A — Acknowledge (Vấn đề 10s - 30s)
* **Mục tiêu:** Đồng cảm và gọi tên chính xác 3 bài toán/nỗi lo lớn nhất của Founder:
  1. *Chi phí nhàn rỗi:* Không chạy thì không tốn tiền (Zero idle cost).
  2. *Khả năng mở rộng:* Tự động co giãn khi lượng người dùng tăng (Scale CCU) mà không cần thay đổi thiết kế hệ thống.
  3. *Tích hợp:* Kết nối mượt mà vào hệ thống quản lý sẵn có (ERP/Legacy system) của doanh nghiệp.

#### Step 3: T — Trust (Giải pháp & Minh chứng 30s - 1h10)
* **Mục tiêu:** Chứng minh năng lực thực thi thông qua giải pháp công nghệ cụ thể.
* **Cách làm:** Giải thích đơn giản bằng các phép ví von đời thường kết hợp show code/sơ đồ:
  * *Về chi phí & co giãn:* Giải thích cách dùng Serverless (Cloudflare Workers), database tự co giãn (Neon), và quản lý trạng thái riêng biệt cho từng cuộc hội thoại (Durable Objects).
  * *Về API & Tích hợp:* Giải thích cách kết nối qua OAuth 2.0 và thiết lập chốt chặn chống trùng đơn hàng (Idempotency Guard/Duplicate Guard).
  * *Về tối ưu API:* Giải thích cách dùng Prompt Caching (AI học thuộc lòng danh mục thay vì đọc lại từ đầu).

#### Step 4: S — Stick (Mở vòng lặp 1h10 - 1h20)
* **Mục tiêu:** Tạo lý do để người xem bấm follow và chờ đợi các nội dung tiếp theo.
* **Cách làm:** Giới thiệu đây là một phần trong series nhật ký thiết kế giải pháp của studio và hé lộ chủ đề của tập tiếp theo.

#### Step 5: A — Action (Kêu gọi hành động mềm 1h20 - 1h30)
* **Mục tiêu:** Chuyển đổi người xem thành khách hàng tiềm năng mà không mang tính bán hàng.
* **Cách làm:** Thay vì bảo họ click bio tải tài liệu hay mua hàng, hãy kêu gọi: *"Hãy nhắn tin trực tiếp nếu bạn muốn thảo luận sâu hơn về giải pháp."*

---

## 🛠️ 3. Danh Sách Kiểm Tra Khi Duyệt Kịch Bản (Pre-Publish Checklist)
- [ ] Kịch bản đã che giấu tên khách hàng chưa?
- [ ] Có từ ngữ giật gân, câu view không?
- [ ] Đã lồng ghép 3 mục tiêu cốt lõi của Founder vào phần Acknowledge chưa?
- [ ] Đã giải thích giải pháp kỹ thuật (Prompt Caching, Serverless, Idempotency) một cách dễ hiểu chưa?
- [ ] Phần Action có phải là kêu gọi nhắn tin thảo luận trực tiếp (không bán hàng) chưa?
- [ ] Visual đi kèm có đúng chuẩn VCL (Cursor IDE, bảng vẽ sơ đồ, font RobotoMono) chưa?

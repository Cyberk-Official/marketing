# SB7 Narrative Development Workflow

Quy trình này hướng dẫn cách chuyển hóa một ý tưởng thô thành một câu chuyện thương hiệu hoàn chỉnh, sử dụng khung StoryBrand 7-Part (SB7).

---

## Phase 1: Initiation & Context (Khởi tạo & Bối cảnh)

*Mục tiêu: Thiết lập nền móng vững chắc. Một câu chuyện sai bối cảnh giống như một chiếc chìa khóa vàng mở nhầm ổ khóa.*

### 1.1 Setup File

- **Hành động:** Sao chép nội dung từ `workflow/sb7/template.md`.
- **Đích:** Tạo file mới theo định dạng: `stories/[tên-du-an]_sb7.md`.

### 1.2 Contextual Interview (Phỏng vấn bối cảnh)

AI sẽ đóng vai Socrates và hỏi người dùng các câu hỏi sau (nếu chưa được cung cấp):

1. **The Narrator (Ai kể?):** Chúng ta đang kể với tư cách là Thương hiệu, CEO, hay một người bạn? Giọng văn (Tone of voice) là gì? (Trang trọng, hài hước, hay tâm tình?).
2. **The Audience (Kể cho ai?):** Khán giả cụ thể là ai? Họ đang ở trạng thái tâm lý nào trước khi nghe câu chuyện này? (Đang vội, đang nghi ngờ, hay đang khao khát?).
3. **The Goal (Mục đích):** Sau khi nghe xong, chúng ta muốn họ *cảm thấy* gì và *làm* gì?

### 1.3 Memory Bank Creation

Tạo một block `> Context Memory` ngay đầu file nháp để lưu trữ các từ khóa quan trọng xuyên suốt quá trình (giúp đảm bảo tính nhất quán):

- *Key Terms (Thuật ngữ chính)*
- *Forbidden Words (Từ cấm dùng)*
- *Core Emotion (Cảm xúc chủ đạo)*

---

## Phase 2: The Socratic Construction (Xây dựng từng phần)

*Quy tắc vàng: Không bao giờ viết toàn bộ cùng lúc. Đi chậm để đi xa.*

### Quy tắc thực thi (Rules of Engagement)

1. **Step-by-Step:** Chỉ đi chuyển sang phần tiếp theo khi phần hiện tại đã được người dùng `CONFIRM`.
2. **Socratic Questioning:** Trước khi viết, AI phải đặt câu hỏi dựa trên gợi ý trong Template để khai thác "nỗi đau" và "khát vọng" thực sự.
3. **Draft & Refine:** AI viết nháp -> Người dùng phản hồi -> AI sửa lại -> Ghi vào file.

### Trình tự thực hiện (The Flow)

Tuân thủ nghiêm ngặt theo cấu trúc của `workflow/sb7/template.md`. Lặp lại quy trình hỏi đáp và viết cho từng phần sau:

1. **Character (Nhân vật - Người Hùng):** Xác định Singular Desire & Survival Instinct.
2. **Has a Problem (Gặp Vấn Đề):** Xác định Villain, External, Internal & Philosophical Problem.
3. **And Meets a Guide (Gặp Người Dẫn Đường):** Thể hiện Empathy & Authority.
4. **Who Gives Them a Plan (Người Đưa Ra Kế Hoạch):** Process Plan & Agreement Plan.
5. **And Calls Them to Action (Kêu Gọi Hành Động):** Direct CTA & Transitional CTA.
6. **That Helps Them Avoid Failure (Giúp Tránh Thất Bại):** Tragedy & Opportunity Cost.
7. **And Ends in a Success (Và Kết Thúc Thành Công):** External Success, Internal Relief & Identity Transformation.
8. **One-Liner:** Tóm tắt toàn bộ thành một câu công thức.

---

## Phase 3: Critical Review & Polish (Kiểm tra & Tinh chỉnh)

*Mục tiêu: Mài giũa viên ngọc thô. Đảm bảo không có chi tiết thừa.*

### 3.1 Consistency Check (Kiểm tra nhất quán)

- **Công cụ:** Áp dụng quy tắc tại `.cursor/rules/content-rules/consistency-rules.mdc`.
- **Hành động:** Rà soát lỗi chính tả tiếng Việt, cách dùng từ, văn phong đã thống nhất ở Phase 1 chưa.

### 3.2 Logic & Narrative Tension Audit (Kiểm tra Logic & Căng thẳng cốt truyện)

AI rà soát toàn bộ câu chuyện và trả lời các câu hỏi phản biện:

1. **Chekhov's Gun:** Có chi tiết nào được đưa ra ở đầu nhưng không được giải quyết hoặc không có tác dụng ở cuối không? Nếu có, hãy loại bỏ.
2. **The Stakes:** Cái giá phải trả (nếu thất bại) có đủ cao để buộc Người Hùng phải hành động không? Hay nó quá nhẹ nhàng?
3. **Gap Analysis:** Giải pháp của chúng ta có thực sự giải quyết triệt để "Vấn đề nội tại" đã nêu ở phần 2 không?

### 3.3 SB7 Scorecard (Đánh giá mức độ tuân thủ)

- [ ] Nhân vật chính có phải là Khách hàng (không phải Thương hiệu)?
- [ ] Kẻ phản diện có rõ ràng và đáng ghét không?
- [ ] Kế hoạch có đơn giản đến mức "gây sốc" không?
- [ ] Lời kêu gọi hành động có rõ ràng và lặp lại không?
- [ ] Sự chuyển hóa (Transformation) có chạm đến cảm xúc không?

---
*Lưu ý: Sau khi hoàn tất Phase 3 và được duyệt, hãy xóa các phần hướng dẫn/câu hỏi gợi ý, chỉ giữ lại cốt truyện tinh gọn (nếu cần bản clean).*

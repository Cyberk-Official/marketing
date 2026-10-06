# Workflow: Định Hình Nền Tảng Giao Tiếp Nội Bộ 🏛️

> "Giao tiếp hiệu quả bắt đầu từ sự thấu cảm."

Quy trình này là bước **KHỞI ĐẦU** bắt buộc để xây dựng một nền tảng giao tiếp nội bộ nhất quán và hiệu quả. Tại đây, chúng ta sẽ định hình hai "nhân vật" cốt lõi: **Lãnh đạo (Author)** và **Thành viên team (Employee)**.

### Phase 1: Foundation Setup

**Mục tiêu:** Tạo ra hai hồ sơ persona nền tảng, đóng vai trò là "kim chỉ nam" cho mọi hoạt động giao tiếp nội bộ.

**Các bước thực hiện:**

1. **Tạo Hồ sơ Lãnh đạo (Author Profile):**
    * Sao chép nội dung từ template `workflow/docs/personas/author-template.md`.
    * Lưu thành file mới tại `workflow/docs/personas/author.md`.
2. **Tạo Hồ sơ Thành viên (Employee Profile):**
    * Sao chép nội dung từ template `workflow/docs/personas/persona_template.md`.
    * Lưu thành file mới tại `workflow/docs/personas/employee.md`.
3. **Lưu ý:** Hai file `author.md` và `employee.md` là các tài liệu "sống", cần được review và cập nhật định kỳ để phản ánh đúng thực tế của tổ chức.

---

### Phase 2: Defining the Leadership Voice (Author Persona)

**Mục tiêu:** Giúp lãnh đạo tự định hình và làm rõ triết lý, phong thái và nguyên tắc giao tiếp của mình.

**Hồ sơ cần điền:** `workflow/docs/personas/author.md`

**Các bước thực hiện:**

1. **Phỏng vấn sâu (Deep Interview):**
    * AI đóng vai trò người phỏng vấn (Interviewer).
    * Yêu cầu lãnh đạo trả lời từng câu hỏi trong `author.md`.
    * **Nguyên tắc Socratic:** Nếu câu trả lời hời hợt, AI **BẮT BUỘC** phải đặt câu hỏi đào sâu (Probing questions) để làm rõ động cơ và quan điểm cốt lõi.
    * *Ví dụ:* Nếu lãnh đạo nói "Triết lý của tôi là minh bạch", AI phải hỏi: "Cụ thể 'minh bạch' nghĩa là gì? Thông tin nào nên và không nên minh bạch? Tại sao?".
2. **Hoàn thiện:**
    * Sau khi phỏng vấn, điền các câu trả lời đã được làm rõ vào file `author.md`.

---

### Phase 3: Understanding the Team's Perspective (Employee Persona)

**Mục tiêu:** Xây dựng sự thấu cảm sâu sắc với các thành viên trong team, hiểu rõ những mong muốn và rào cản của họ.

**Hồ sơ cần điền:** `workflow/docs/personas/employee.md`

**Các bước thực hiện:**

1. **Thảo luận & Đóng góp:**
    * Tổ chức một buổi làm việc với các quản lý cấp trung hoặc các thành viên team tin cậy.
    * Cùng nhau điền vào `employee.md` dựa trên quan sát và phản hồi thực tế.
2. **Điền Empathy Map:**
    * Sử dụng template để khai thác: Họ thấy gì? Họ nghe gì? Họ sợ gì? Họ muốn gì trong công việc?
    * **Yêu cầu:** Không chấp nhận các mô tả chung chung. Phải mô tả được tâm lý và những rào cản vô hình (ví dụ: "ngại đặt câu hỏi").
3. **Hoàn thiện:**
    * Tổng hợp các insight vào file `employee.md`.

---

### Phase 4: Consistency Check (The Law)

**Mục tiêu:** Đảm bảo các hồ sơ persona tuân thủ quy tắc hệ thống.

**Tham chiếu:** `.cursor/consistency-rules.mdc` (Nếu có)

**Các bước thực hiện:**

1. **Kiểm tra Cấu trúc (Structure):**
    * Các file `author.md` và `employee.md` có đúng định dạng markdown không?
2. **Kiểm tra Ngôn ngữ (Language):**
    * Các thuật ngữ chuyên ngành (Technical Terms) có được giữ nguyên tiếng Anh để đảm bảo sự rõ ràng không?
3. **Kiểm tra tính nhất quán (Consistency):**
    * Hình mẫu lãnh đạo trong `author.md` có đáp ứng được nhu cầu của `employee.md` không?

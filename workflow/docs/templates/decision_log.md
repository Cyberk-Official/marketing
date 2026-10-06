# Template: Nhật Ký Quyết Định (The "Why" Behind The Change)

**Đối tượng:** Toàn bộ team.
**Mục tiêu:** Cung cấp sự minh bạch tuyệt đối về lý do đằng sau một quyết định quan trọng (thay đổi quy trình, công nghệ, chính sách), giúp mọi người hiểu "TẠI SAO" và giảm bớt sự phản kháng hoặc cảm giác mơ hồ.

---

## 1. Bối Cảnh (The Context)

*Explain: Vấn đề hoặc cơ hội nào đã dẫn đến quyết định này? Tình hình lúc đó ra sao?*
*Instruction: Mô tả ngắn gọn tình trạng trước khi có sự thay đổi. Hãy vẽ ra "nỗi đau" mà team đang gặp phải.*

* **Bức tranh trước thay đổi:**
  * *Bad Example: "Quy trình cũ không hiệu quả."*
  * *Good Example: "Team dev đang mất trung bình 3 giờ mỗi tuần để deploy thủ công, dẫn đến việc chậm trễ và dễ phát sinh lỗi vào cuối ngày thứ Sáu."*

## 2. Các Lựa Chọn Đã Cân Nhắc (Options Considered)

*Explain: Thể hiện sự cẩn trọng và tư duy hệ thống. Chúng ta đã không quyết định một cách bốc đồng.*
*Instruction: Liệt kê 2-3 phương án đã được đưa ra bàn bạc, kèm theo ưu và nhược điểm chính của từng phương án.*

* **Phương án A (Ví dụ: Giữ nguyên quy trình cũ):**
  * *Ưu điểm: Không tốn công thay đổi.*
  * *Nhược điểm: Tiếp tục gây lãng phí thời gian, rủi ro cao.*
* **Phương án B (Ví dụ: Xây dựng tool nội bộ):**
  * *Ưu điểm: Tùy chỉnh theo nhu-cầu.*
  * *Nhược điểm: Tốn 2 tháng để phát triển, cần người bảo trì.*
* **Phương án C (Ví dụ: Dùng dịch vụ CI/CD):**
  * *Ưu điểm: Triển khai nhanh trong 1 tuần, ổn định.*
  * *Nhược điểm: Tốn $50/tháng, phụ thuộc vào bên thứ ba.*

## 3. Quyết Định Cuối Cùng & Lý Do (The Decision & The "Why")

*Explain: Phần quan trọng nhất. Kết nối quyết định với các giá trị hoặc mục tiêu lớn hơn của công ty.*
*Instruction: Nêu rõ quyết định được chọn và giải thích lý do một cách thuyết phục. Hãy trả lời câu hỏi: "Điều này giúp chúng ta trở thành những người nghệ nhân giỏi hơn như thế nào?"*

* **The Rationale:**
  * *Bad Example: "Chúng tôi chọn phương án C."*
  * *Good Example: "Chúng tôi quyết định chọn Phương án C (dùng dịch vụ CI/CD). Dù có chi phí, nhưng nó giúp giải phóng thời gian cho team dev tập trung vào việc tạo ra sản phẩm chất lượng, thay vì lãng phí vào các công việc vận hành lặp đi lặp lại. Điều này phù hợp với giá trị 'Tay nghề nghệ nhân' của chúng ta."*

## 4. Lộ Trình Triển Khai (Rollout Plan)

*Explain: Biến quyết định thành hành động. Ai làm gì? Khi nào?*
*Instruction: Cung cấp một kế hoạch ngắn gọn với các mốc thời gian và người chịu trách nhiệm chính.*

* *Good Example: "Tuần 1: Tech Lead sẽ cấu hình hệ thống. Tuần 2: Tổ chức buổi training cho toàn bộ team. Bắt đầu áp dụng chính thức từ ngày [dd/mm]."*

## 5. Kỳ Vọng & Cách Đo Lường (Expected Outcome & Metrics)

*Explain: Làm sao chúng ta biết quyết định này là đúng đắn?*
*Instruction: Nêu rõ kết quả mong đợi và các chỉ số sẽ được theo dõi.*

* *Good Example: "Chúng tôi kỳ vọng sẽ giảm thời gian deploy xuống dưới 15 phút và không có lỗi deploy nào trong tháng đầu tiên. Chúng tôi sẽ review lại kết quả sau 1 tháng."*

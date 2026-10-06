# Template: Biên Bản Mổ Xẻ Vấn Đề (Blameless Postmortem)

**Đối tượng:** Toàn bộ team.
**Mục tiêu:** Phân tích một sự cố hoặc sai lầm để tìm ra nguyên nhân gốc rễ và cải thiện hệ thống. Nguyên tắc cốt lõi: Chúng ta tin rằng mọi người đã làm tốt nhất có thể với thông tin và nguồn lực họ có tại thời điểm đó. Chúng ta tập trung vào "CÁI GÌ" và "TẠI SAO", không phải "AI".

---

## 1. Tóm Tắt Sự Cố (Incident Summary)

*Explain: Chuyện gì đã xảy ra?*
*Instruction: Mô tả ngắn gọn sự cố, thời gian xảy ra, mức độ ảnh hưởng và thời gian khắc phục. Giữ giọng văn trung lập, chỉ nêu sự thật.*

*   **Sự cố:** Lỗi thanh toán qua cổng ZaloPay.
*   **Thời gian:** 14:30 - 16:00, ngày [dd/mm].
*   **Ảnh hưởng:** 150 giao dịch thất bại, ước tính thiệt hại $5,000 doanh thu.
*   **Thời gian khắc phục:** 90 phút.

## 2. Dòng Thời Gian Chi Tiết (Detailed Timeline)

*Explain: Diễn biến sự việc theo trình tự thời gian.*
*Instruction: Liệt kê các sự kiện quan trọng theo mốc thời gian, từ lúc phát hiện, các hành động đã thực hiện, cho đến khi sự cố được giải quyết. Ghi rõ ai đã làm gì.*

*   **14:30:** Hệ thống monitoring báo cáo tỷ lệ lỗi thanh toán tăng đột biến.
*   **14:35:** [Tên Dev] bắt đầu điều tra.
*   **14:50:** [Tên Dev] phát hiện lỗi đến từ việc ZaloPay thay đổi API endpoint mà không thông báo trước.
*   **15:15:** Team họp nhanh để đưa ra giải pháp tạm thời.
*   **15:45:** [Tên Dev] deploy bản vá nóng (hotfix), cập nhật endpoint mới.
*   **16:00:** Hệ thống hoạt động trở lại bình thường.

## 3. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis)

*Explain: Tại sao sự cố lại xảy ra?*
*Instruction: Sử dụng kỹ thuật "5 Whys" để đi đến tận cùng của vấn đề. Tránh dừng lại ở những câu trả lời bề mặt.*

*   **Vấn đề:** Giao dịch ZaloPay thất bại.
    1.  **Tại sao?** Vì hệ thống gọi đến API endpoint cũ của ZaloPay.
    2.  **Tại sao?** Vì ZaloPay đã thay đổi endpoint mà chúng ta không biết.
    3.  **Tại sao chúng ta không biết?** Vì thay đổi này không được thông báo qua kênh chính thức, chỉ được cập nhật trong tài liệu của họ.
    4.  **Tại sao quy trình của chúng ta lại phụ thuộc vào việc họ thông báo?** Vì chúng ta không có cơ chế tự động kiểm tra sức khỏe (health check) của các API đối tác.
    5.  **Tại sao chúng ta không có cơ chế đó?** Vì khi tích hợp, chúng ta đã ưu tiên tốc độ ra mắt và cho rằng API của đối tác lớn sẽ ổn định. **(Đây là nguyên nhân gốc rễ liên quan đến quy trình và giả định sai).**

## 4. Điều Gì Đã Đi Đúng Hướng? (What Went Well?)

*Explain: Ghi nhận và đánh giá cao những phản ứng tích cực.*
*Instruction: Liệt kê những điểm sáng trong quá trình xử lý sự cố.*

*   *Hệ thống monitoring đã cảnh báo rất nhanh.*
*   *Team đã phối hợp xử lý rất hiệu quả.*
*   *Bản vá nóng được triển khai nhanh chóng và chính xác.*

## 5. Các Hành Động Cải Thiện (Action Items)

*Explain: Chúng ta sẽ làm gì để ngăn điều này xảy ra lần nữa?*
*Instruction: Liệt kê các hành động cụ thể, có người chịu trách nhiệm (Owner) và ngày hoàn thành dự kiến (Due Date).*

| Hành Động | Owner | Due Date |
| --- | --- | --- |
| 1. Xây dựng job tự động health check API của tất cả đối tác thanh toán. | @techlead | [dd/mm] |
| 2. Tạo playbook xử lý sự cố khi một đối tác thứ ba gặp vấn đề. | @product | [dd/mm] |
| 3. Review lại quy trình tích hợp đối tác, bổ sung checklist rủi ro. | @techlead | [dd/mm] |

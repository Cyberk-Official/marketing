# Kế Hoạch Dự Án — Planning Report Template

> **Hướng dẫn**: Điền vào các khu vực có chữ *in nghiêng*. Xóa hướng dẫn sau khi hoàn thành.

---

## Thông tin dự án

- **Tên dự án**: *[Tên dự án]*
- **Khách hàng**: *[Tên khách hàng]*
- **Ngày Planning Meeting**: *[dd/mm/yyyy]*
- **Facilitator**: *[Tên người dẫn dắt]*

### Team

| Vai trò | Tên |
|---------|-----|
| Production Lead | *[Tên]* |
| Dev Lead | *[Tên]* |
| Fullstack Dev | *[Tên]* |
| Designer | *[Tên]* |
| QA | *[Tên]* |

---

## 1. Mục tiêu dự án

1. **Deadline**: *[Ngày giờ cụ thể]*

2. **Kỳ vọng của khách hàng**:
   - Mục đích dự án: *[KH làm sản phẩm này có ý nghĩa gì?]*
   - Điều gì quan trọng nhất với họ: *[Điều gì KH care nhất?]*

3. **Kỳ vọng của công ty**:
   - Mục tiêu chiến lược: *[Ý nghĩa của việc hoàn thành dự án — ví dụ: UX/UI vượt trội, showcase năng lực AI]*
   - Mục tiêu với khách hàng: *[Ví dụ: Chinh phục KH bằng chất lượng, tạo mối quan hệ dài hạn]*

---

## 2. Phân loại tính năng

### Tính năng tối quan trọng (Key Success Features)

Các chức năng cốt lõi quyết định **thành công** của dự án. Bắt buộc hoàn thành đúng hạn.

- *[Tên tính năng 1]*: *[Mô tả ngắn]*
- *[Tên tính năng 2]*: *[Mô tả ngắn]*

### Tính năng cơ bản (Thiết yếu)

Nền tảng để sản phẩm sử dụng được. Không phải điểm nhấn nhưng bắt buộc phải có.

- *[Tính năng A]*
- *[Tính năng B]*

### Tính năng không ưu tiên (Điều kiện đủ)

Bổ sung giúp hoàn thiện sản phẩm, **không bắt buộc** trong MVP.

- *[Tính năng X]*

### Tính năng "nice-to-have" (Mở rộng)

Ý tưởng cho các giai đoạn sau. **Không phát triển** trong scope hiện tại.

- *[Tính năng Y]*

---

## 3. Danh sách rủi ro (Risk List)

| # | Rủi ro | Ảnh hưởng | Giải pháp |
|---|--------|-----------|-----------|
| 1 | *[Mô tả rủi ro]* | *[Ảnh hưởng nếu xảy ra]* | *[Cách phòng tránh / xử lý]* |
| 2 | *[Mô tả rủi ro]* | *[Ảnh hưởng nếu xảy ra]* | *[Cách phòng tránh / xử lý]* |

**Các loại rủi ro phổ biến cần xem xét:**

- **Tiến độ**: Thay đổi yêu cầu đột xuất, chậm trễ từ bên thứ ba
- **Công nghệ**: Công cụ/thư viện chưa kiểm chứng, API bên thứ ba
- **Giao tiếp**: Hiểu sai yêu cầu, phản hồi chậm từ KH
- **Con người**: Nghỉ đột xuất, thiếu năng lực, tinh thần không ổn định

---

## 4. Task List / Checklist

| Công việc (Task) | Hạn chót (Deadline) | Người phụ trách | Kết quả đầu ra (Output) |
|------------------|---------------------|-----------------|--------------------------|
| Setup repo | *[dd/mm]* | *[Tên]* | Git repo + README + branch rules |
| Setup infra | *[dd/mm]* | *[Tên]* | Architecture Diagram + Setup guide |
| *[Tính năng 1]* | *[dd/mm]* | *[Tên]* | Test report |
| *[Tính năng 2]* | *[dd/mm]* | *[Tên]* | Test report |
| Họp với KH + update PRD | Daily | *[Tên]* | Meeting Minutes hoặc BRD |
| Tổ chức retro | Weekly | *[Tên]* | Improvement Report |
| UAT & Bug fixing | *[dd/mm]* | *[Tên]* | Critical bugs resolved |
| MVP Release | *[dd/mm]* | *[Tên]* | Deploy + handover doc |

**Giải thích Output:**

- Output của tính năng: **Test reports** — báo cáo kết quả kiểm thử
- Output của retrospective: **Improvement reports** — danh sách cải tiến cho sprint sau
- Output của họp KH: **BRD** hoặc **Meeting Minutes**
- Output của setup cloud: **Architecture Design Document** + hướng dẫn cấu hình
- Output của setup repo: **Git repo chuẩn** + README
- Output của Planning Meeting: **Planning Report** (chính là tài liệu này)

---

## 5. Chiến lược phát triển dự án

- **Mục tiêu chính**:
  - *[Ví dụ: Clear scope sớm nhất có thể]*
  - *[Ví dụ: Priority MVP timeline]*

- **Trọng tâm**:
  - *[Ví dụ: Intuitive UI/UX]*
  - *[Ví dụ: Using AI to faster development time]*

- **Nhân sự chủ lực**: *[Tên]*

- **Phối hợp với khách hàng**: *[Ví dụ: Daily demo + weekly video demo]*

- **Nhiệm vụ cá nhân**:
  - *[Tên 1]*: *[Trách nhiệm chính]*
  - *[Tên 2]*: *[Trách nhiệm chính]*

- **Kết luận**:
  - *[Tóm lại chiến lược]*
  - *[Trong kế hoạch, điểm nào còn yếu?]*
  - *[Bằng bản năng: Có gì không an toàn?]*

---

**Lưu ý:** Đây là tài liệu nội bộ. Cần được cập nhật thường xuyên khi có thay đổi về scope, rủi ro hoặc lịch trình. Sau khi hoàn thành, gửi PDF qua Telegram cho khách hàng và Anderson.

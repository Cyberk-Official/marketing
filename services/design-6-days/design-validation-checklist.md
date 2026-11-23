# Cyberk – Bộ phép thử Design Validation (trước khi code)

> **Mục tiêu:** Kiểm thử bản thân thiết kế ngay trong Figma/Prototype, trước khi chuyển giao cho Dev.
> Lỗi tìm ra ở giai đoạn này chỉ tốn vài phút để sửa; khi đã code thì phải sửa cả design lẫn code.

**Phân biệt:**
- **Design Validation** (tài liệu này): kiểm thử *thiết kế* có tốt không → làm trong Figma, trước khi code.
- **Design QA**: kiểm tra *bản build* có đúng thiết kế không → làm sau khi code (mạng chậm, VoiceOver, overlay so bản build…).

---

## STEP 02 – Wireframe · Kiểm tra luồng & cấu trúc

| ✓ | Phép thử | Cách làm | Bắt lỗi gì |
|---|---|---|---|
| ☐ | **Hallway usability test** | Cho 5 người dùng mục tiêu bấm prototype đen-trắng, giao 3–4 nhiệm vụ cụ thể | Luồng khó hiểu, người dùng bị "kẹt" ở đâu |
| ☐ | **First-click test** | Hỏi "Muốn làm X thì bấm vào đâu?", ghi lại cú bấm đầu tiên | Vị trí / nhãn nút sai kỳ vọng người dùng |
| ☐ | **Card sorting / Tree test** | Người dùng tự nhóm các mục, hoặc tìm một mục trong cây menu | Cấu trúc menu, cách đặt tên mục |
| ☐ | **Walkthrough với Dev** | Dev xem wireframe, đánh dấu chỗ khó làm hoặc thiếu dữ liệu | Thiết kế không khả thi kỹ thuật |

**Đầu ra:** Danh sách vấn đề luồng đã sửa + wireframe được khách hàng duyệt.

---

## STEP 03 – Key Mockup · Kiểm tra thị giác

| ✓ | Phép thử | Cách làm | Bắt lỗi gì |
|---|---|---|---|
| ☐ | **Grayscale test** | Chuyển frame về đen trắng (plugin hoặc layer Saturation = 0) | Phân cấp thông tin phụ thuộc hoàn toàn vào màu |
| ☐ | **Squint / Blur test** | Đặt layer blur 8–10px đè lên màn hình | Điểm nhấn thị giác không rơi vào CTA |
| ☐ | **5-second test** | Cho người lạ xem 5 giây, hỏi "Màn hình này để làm gì?" | Thông điệp chính không rõ |
| ☐ | **Mô phỏng mù màu** | Plugin Stark / Color Blind trong Figma | Trạng thái lỗi/thành công chỉ phân biệt bằng màu đỏ–xanh |
| ☐ | **Xem trên điện thoại thật** | Mở bằng Figma Mirror, cầm tay ở khoảng cách bình thường | Chữ quá nhỏ, chi tiết quá dày (màn desktop đánh lừa kích thước) |
| ☐ | **Test độ sáng thấp** | Xem trên điện thoại ở độ sáng ~30% | Màu xám nhạt, viền mảnh biến mất |

**Đầu ra:** 2–4 màn hình mẫu đã qua kiểm thử + khách hàng chốt định hướng thị giác.

---

## STEP 04 – Design System · Kiểm tra độ bền của quy chuẩn

| ✓ | Phép thử | Cách làm | Bắt lỗi gì |
|---|---|---|---|
| ☐ | **Contrast ratio cho mọi cặp token** | Kiểm tra từng cặp màu chữ/nền theo WCAG: chữ thường ≥ 4.5:1, chữ lớn & UI ≥ 3:1 | Cặp màu nào *không được phép* dùng chung |
| ☐ | **Resize test** | Kéo giãn / co component (auto-layout) từ 320px → 430px | Component vỡ khi đổi kích thước màn hình |
| ☐ | **Font scale test** | Tăng toàn bộ text token lên 130–150% | Layout vỡ khi người dùng bật chữ lớn (đặc biệt app cho người lớn tuổi) |
| ☐ | **Vùng chạm tối thiểu** | Đo vùng bấm của mọi component tương tác | Nhỏ hơn 44×44pt (iOS) / 48×48dp (Android) |
| ☐ | **Dấu tiếng Việt** | Điền "Ưỡng Ổ Ậ Ỹ" vào mọi kiểu chữ trong thang typography | Dấu bị cắt do line-height quá chật |

**Đầu ra:** Bảng token kèm ghi chú cặp màu hợp lệ + bộ Master Components đã qua stress test.

---

## STEP 05 – Detailed UI · Kiểm tra độ phủ & tính nhất quán

| ✓ | Phép thử | Cách làm | Bắt lỗi gì |
|---|---|---|---|
| ☐ | **Stress test nội dung** | Điền tên dài ("Nguyễn Thị Phương Thảo Hoàng Minh"), số tiền lớn (1.250.000.000đ), danh sách 0 / 1 / 100 mục | Tràn chữ, cắt chữ, empty state xấu |
| ☐ | **State coverage checklist** | Mỗi màn hình phải có đủ: Empty · Loading · Error · Success · Disabled | Thiếu trạng thái → Dev phải "tự đoán" |
| ☐ | **Detached component audit** | Plugin quét instance bị detach hoặc style không gắn token | Màn hình lệch khỏi Design System |
| ☐ | **Thumb zone overlay** | Đặt lớp phủ vùng ngón cái lên các màn hình chính | CTA nằm ngoài tầm với khi dùng một tay |
| ☐ | **End-to-end prototype test** | Đi hết luồng chính trên điện thoại thật, gồm cả nhánh lỗi | Đường cụt, thiếu nút quay lại |

**Đầu ra:** Prototype hoàn chỉnh, không còn "vùng xám", sẵn sàng bàn giao cho Dev.

---

## Công cụ gợi ý

| Mục đích | Công cụ |
|---|---|
| Tương phản & mù màu | Stark, Contrast (Figma plugin), WebAIM Contrast Checker |
| Xem trên thiết bị thật | Figma Mirror / Figma mobile app |
| Usability test từ xa | Maze, Useberry (gắn trực tiếp prototype Figma) |
| Card sorting / Tree test | Optimal Workshop, Maze |
| Audit component | Design Lint, Instance Finder (Figma plugin) |

---

## Để dành cho Design QA (sau khi có bản build)

Những phép thử chỉ làm được trên app thật:
- Mạng chậm (Slow 3G) & mất mạng giữa chừng
- Phóng to chữ hệ thống thật (iOS Dynamic Type, Android font scale 200%)
- Screen reader (VoiceOver / TalkBack)
- Reduce motion
- Gián đoạn: cuộc gọi đến, xoay màn hình, thoát ra – vào lại, nút Back Android
- Overlay ảnh thiết kế lên ảnh chụp bản build (50% opacity) & token audit trên code
- Ma trận thiết bị: máy nhỏ, máy có tai thỏ, Android giá rẻ

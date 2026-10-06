---
type: handoff
title: "Bối cảnh làm việc: Asimov (whitepaper, deck)"
created-date: 2026-09-29
author: anderson
purpose: Tóm tắt để tiếp tục trong một cuộc trò chuyện mới mà không mất bối cảnh
---

# Bối cảnh làm việc: Asimov

Tóm tắt phiên làm việc ngày 29/09/2026. Đọc file này trước khi tiếp tục bất kỳ việc gì về whitepaper hoặc deck của Asimov.

## 1. Tài liệu đã có

Thư mục trên máy Anderson: `~/Desktop/works/marketing/asimov/`

| File | Là gì | Trạng thái |
|---|---|---|
| `asimov-laws-whitepaper.md` | Whitepaper "Ba định luật Asimov cho phát triển phần mềm bằng AI". Chỉ chứa lý luận, viết để đứng vững lâu dài | Bản nháp 0.3, đã duyệt phần lớn |
| `asimov-laws-implementation.md` | "Cách Asimov thực thi ba định luật": các kiểu lỗ hở H1–H6, nguyên tắc thiết kế, cơ chế theo từng luật, cập nhật theo phiên bản | Bản nháp 0.1 |
| `asimov-harness.md` | Mô tả Asimov Harness (agent hỏi và thao tác dữ liệu vận hành) | Bản nháp 0.1 |
| `asimov-pitch-deck.md` | Deck bản cũ (18 slide), viết trước khi whitepaper được sửa nhiều. **Đã lỗi thời**, cần làm lại | Cần viết lại |

Nguồn gốc kỹ thuật: `~/Desktop/asimov/asimov` (skills, docs, website), `~/Desktop/asimov/asimov-platform` (Cyberk Operation Dashboard, BRD Harness), `~/Desktop/asimov/asimov-handbook`.

## 2. Ba định luật (bản chốt)

**Định luật 1.** AI phải tuân thủ kiến trúc của hệ thống, và không được đứng nhìn kiến trúc bị vi phạm, kể cả khi vi phạm đó không do nó gây ra.

**Định luật 2.** AI phải tuân thủ mệnh lệnh của con người, trừ khi mệnh lệnh đó mâu thuẫn với Định luật 1. Tuân thủ nghĩa là làm thật và nói thật: không chọn cách dễ thay cho cách đúng, và không bao giờ báo đã xong một việc chưa xong.

**Định luật 3.** Trong giới hạn của Định luật 1 và 2, AI được tự do hành động bằng toàn bộ năng lực của mình, và tự giữ cho mình những giới hạn mà một kỹ sư chân chính sẽ giữ, kể cả khi không ai giám sát.

Không đặt tên gọi cho từng luật (không dùng "Giữ kiến trúc", "Tuân thủ trung thực"...). Chỉ gọi là Định luật 1, 2, 3.

## 3. Những ý chính đã thống nhất

- **Kiến trúc là bản thiết kế phần mềm.** AI ở vị trí lập trình viên, con người là giám sát. Hai tình huống: thấy người khác làm sai thiết kế thì báo; thấy chính thiết kế sai thì báo cho người thiết kế hệ thống, không tự sửa, không code lách.
- **Luật 2 là về trung thực.** Model được tối ưu cho chi phí, token và việc hoàn thành task, nên hay chọn cách dễ (báo xong khi chưa xong, sửa test cho pass). Con người cũng vậy (quy luật nỗ lực tối thiểu). Luật 2 là nền của niềm tin.
- **Luật 3 là tự do cùng tư cách.** Luật 3 gốc của Asimov là robot tự bảo vệ sự tồn tại; ở đây là AI tự giữ phẩm chất nghề nghiệp. Ví dụ: Anderson không để lại code bẩn kể cả khi không ai giám sát, kể cả khi làm CEO; chuyện gấp chăn mỗi sáng.
- **Niềm tin:** ta tin một người khi biết giới hạn của họ và đã thấy họ giữ giới hạn đó nhiều lần. Các hãng AI dạy model chuẩn của một người tử tế; phần mềm cần chuẩn của một kỹ sư tử tế. Đó là lý do có Asimov.
- **Ba vòng tròn:** hai luật đầu vẽ vòng giới hạn, Luật 3 là tự do bên trong. Luật 1 do người thiết kế hệ thống cùng team vẽ, Luật 2 do người làm việc với AI, Luật 3 do chính AI.
- **Không có vòng tròn nào kín tuyệt đối.** Giống xã hội có luật, cảnh sát, tòa án mà tội phạm vẫn xảy ra. Model có hàng tỷ tham số, không kiểm soát được 100%. Asimov là bộ luật và cơ quan thực thi, không phải công cụ thực thi tuyệt đối. Mục tiêu là để AI và con người tin nhau.
- **Asimov là gì:** một bộ luật chi tiết dành cho AI về tiêu chuẩn phát triển phần mềm, xây dựng trên tinh thần code sạch. Nguồn gốc: tài liệu huấn luyện nhân sự nội bộ Cyberk (2020), Cyberk-Flow (2024), đặt tên Asimov (02/2026) theo tuyển tập *I, Robot*.
- Anderson tin rằng AI sẽ là người bạn đáng tin cậy của loài người.

## 4. Quy tắc viết (bắt buộc)

- Theo `~/Desktop/works/marketing/skills/docs/writing-rules.md`: không câu cụt làm điểm nhấn, không "không phải X mà là Y", không bộ ba liệt kê cho có nhịp, không tính từ tự khen, không kịch tính hoá, phải thừa nhận giới hạn.
- Tiêu đề: nhãn trơn, không dùng kiểu "Nhãn: phụ đề" hay "X và Y" trừu tượng.
- Không nhắc tên nhân vật hay chi tiết truyện của Isaac Asimov; người đọc có thể chưa đọc truyện.
- Không đưa số liệu dễ thay đổi (số commit, số PR) vào tài liệu bền vững.
- Ví dụ phải nằm trong bối cảnh phát triển phần mềm, không đổi bối cảnh.
- Không dùng case nội bộ quá riêng (ví dụ sự cố board SALE / CS-001).
- Mở bài bằng bối cảnh dịch vụ Source Code Rescue và hai hướng team thường làm với AI (thả tự do, khóa bằng review).

## 5. Việc tiếp theo: deck đề xuất hợp tác Cyberk × Tomosia

- Deck mới là **đề xuất hợp tác giữa Cyberk và Tomosia** (tham khảo: https://tomosia.com.vn/co-hoi-nghe-nghiep/). Cần tìm hiểu Tomosia trước khi dựng khung.
- `asimov-pitch-deck.md` hiện tại được viết cho CTO và founder mua dịch vụ, và dùng nội dung cũ: tên gọi các luật, Speedy/Herbie, bảng H1–H5, "vòng tròn kín". Khi làm deck mới, lấy nội dung từ whitepaper bản 0.3, không từ deck cũ.
- Trong thư mục `works` có `Cyberk_x_SotaTek_JV_Deck_1 (1).pptx` / `.pdf`, một deck hợp tác trước đó, có thể tham khảo cấu trúc.
- Giá dịch vụ Cyberk: `~/Desktop/works/marketing/website/services/readme.md` và `source-code-rescue.md`.

## 6. Còn tồn đọng ở whitepaper

- Mục 4: phát biểu mỗi luật xuất hiện hai lần (khối đầu mục và dưới tiêu đề mục con).
- Mục 4.2: câu "các hãng đã công khai ghi nhận reward hacking" chưa có nguồn.
- Giọng văn: còn vài châm ngôn in đậm, vài cấu trúc "không phải X mà là Y", đoạn ngôi "tôi" ở 4.3.
- Mục 5.3 và 5.4 có thể gộp.
- Website Asimov (`asimov/website/src/pages/index.tsx`) và `marketing/website/services/asimov-pipeline.md` vẫn dùng bộ ba định luật cũ.

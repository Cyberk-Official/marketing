---
type: product-concept
title: "Asimov Harness"
tags: [asimov, harness, ai-governance, authorization, delegated-access]
created-date: 2026-09-29
updated-date: 2026-09-29
author: anderson
status: draft v0.1
applies-to: Asimov Harness v0.1, tình trạng tại 09/2026
source: asimov-platform/docs/brd/brd-asimov-harness.md (v0.1, 16/09/2026)
related: asimov-laws-whitepaper.md
---

# Asimov Harness

*Tài liệu mô tả · Bản nháp 0.1 · Tình trạng tại 09/2026*

Asimov Harness là một agent chạy trên máy của nhân viên, cho phép họ hỏi và thao tác dữ liệu vận hành của công ty bằng tiếng Việt, trong giới hạn quyền của chính người hỏi. Ví dụ: "tháng này tôi nghỉ mấy ngày", "ai chưa check-in sáng nay".

Whitepaper *Ba định luật Asimov cho phát triển phần mềm bằng AI* áp dụng ba định luật cho việc viết code. Harness áp dụng cùng ba định luật cho một bài toán khác: agent làm việc với dữ liệu và quyền hạn của con người, thay vì với một codebase.

Trên trang chủ Asimov, Harness được xếp cùng tầng với Claude Code, Codex và OpenCode: tầng môi trường mà agent chạy trong đó, nằm giữa model và bộ luật Asimov.

---

## 1. Bài toán

Cách làm dễ nghĩ tới nhất là nối thẳng một LLM vào backend và để nó tự truy vấn. Cách đó đặt sai ranh giới tin cậy:

- Harness chạy trên máy người dùng, là vùng không kiểm soát được. Bất kỳ secret nào đặt ở đó đều coi như đã lộ.
- Nếu LLM có đường đọc thẳng backend, dù là thông tin đăng nhập database hay một tool kiểu "tìm mọi thứ", thì prompt injection, dữ liệu gửi sang nhà cung cấp LLM và log hội thoại đều thành đường rò dữ liệu. Không còn lớp nào phía sau chặn được.
- Một tiến trình chạy trên máy người dùng không thể là nơi quyết định người đó được xem gì.

## 2. Nguyên tắc chốt

> LLM không đọc backend. LLM chỉ nhìn thấy đúng những dòng mà một tool call đã được server cho phép trả về.

Mọi quyết định về quyền nằm ở server. Harness chỉ là nơi soạn câu hỏi và hiển thị câu trả lời.

## 3. Thiết kế

**Danh tính.** Người dùng đăng nhập qua CLI `asimov` bằng OAuth 2.1 với PKCE. Access token sống tối đa 900 giây và chỉ dùng được cho đúng API của Harness. Plugin không tự làm mới token; khi token sắp hết hạn, nó gọi lại CLI.

**Danh sách procedure mặc định đóng.** Server chỉ chấp nhận lời gọi bằng token của Harness tới những procedure nằm trong một danh sách cho phép. Một procedure mới thêm vào hệ thống thì mặc định vẫn bị từ chối. Danh sách tool mà plugin tự khai báo chỉ là gợi ý cho LLM, không có giá trị quyết định.

**Tool là một câu hỏi nghiệp vụ, không phải một câu truy vấn.** Mỗi tool trả lời một câu hỏi có biên giới rõ, và trả về các dòng đã được server lọc theo người đang hỏi. Không có tool dạng chạy SQL, tìm kiếm toàn bộ hay xuất toàn bộ dữ liệu. Nếu LLM truyền tham số trỏ tới người khác, server bỏ qua tham số đó và vẫn lọc theo người đang đăng nhập.

**Ba mức thẩm quyền.**

| Mức | Phạm vi ảnh hưởng | Cách xác nhận |
|---|---|---|
| 1 | Chỉ chính người dùng, ví dụ tự check-in | Harness hỏi người dùng xác nhận, rồi mới ghi |
| 2 | Người khác, ví dụ duyệt đơn nghỉ của nhân viên | Chỉ tạo đề xuất với tham số bị khóa. Người thật duyệt ngoài Harness (web hoặc Telegram), và server kiểm quyền lại trước khi ghi |
| 3 | Admin, dữ liệu cá nhân, cấu hình | Không mở cho Harness; chỉ làm trên web |

Việc đưa bước duyệt mức 2 ra ngoài phiên chat là để prompt injection không tự hoàn tất được hành động: nội dung độc hại có thể khiến LLM gọi tool, nhưng hành động dừng ở bước đề xuất.

**Audit mọi lời gọi.** Server ghi audit không sửa được cho mọi tool call, kể cả lời gọi bị từ chối, kèm người gọi, tên tool, tham số và kết quả quyết định. Lời gọi bị từ chối là tín hiệu đáng giá nhất: đó là lúc thấy agent đang cố làm gì ngoài phạm vi.

## 4. Liên hệ với ba định luật

| Định luật | Trong Harness |
|---|---|
| 1 | "Kiến trúc" ở đây là ranh giới dữ liệu và quyền. LLM không có đường nào đọc thẳng backend, và phạm vi dữ liệu do server quyết định theo người hỏi |
| 2 | Agent làm theo yêu cầu trong phạm vi quyền của người hỏi. Mọi thao tác ghi đều phải có người xác nhận; thao tác ảnh hưởng người khác đi qua người duyệt ngoài phiên. Audit ghi đúng những gì đã xảy ra, kể cả lời gọi bị từ chối |
| 3 | Trong phạm vi quyền, agent tự chọn tool và cách trả lời. Tool đọc không cần hỏi lại |

## 5. Phạm vi v0.1

**Trong phạm vi:** một tenant là Cyberk; module tổ chức gồm chấm công, nghỉ phép, làm việc từ xa, và thông tin của chính người dùng; tool đọc và tool ghi mức 1.

**Ngoài phạm vi:**

| Không làm | Lý do |
|---|---|
| Nhiều tenant | Chạy đúng cho Cyberk trước; mô hình phân quyền đa tenant sẽ thay đổi toàn bộ lớp kiểm quyền |
| Kết nối qua MCP | MCP client hiện chỉ nhận header tĩnh, không làm mới được token sống 15 phút. Harness dùng plugin native thay thế |
| Tool mức 3 | Chỉ làm trên web |
| Module dự án | Chưa có procedure phù hợp ở tầng được ủy quyền |

## 6. Tình trạng tại 09/2026

- Harness là bản fork của DeepSeek Harness, nạp plugin `asimov-tools` gọi thẳng API nội bộ của hệ thống vận hành Cyberk.
- Dịch vụ quản lý đề xuất cho tool mức 2 chưa được xây, nên chưa có tool mức 2 nào được mở.
- Theo lịch sử commit của `asimov-platform`, hai rủi ro lớn trong BRD đã được xử lý: scope đọc và scope ghi đã được tách riêng, và endpoint `POST /ai` không qua kiểm quyền đã được gỡ.
- Còn treo: xếp check-in và check-out vào mức 1 hay mức 2, cần đối chiếu với quy định chấm công.

## Nguồn

- BRD Asimov Harness v0.1 (16/09/2026): `asimov-platform/docs/brd/brd-asimov-harness.md`.
- Nghiên cứu nền: `asimov-platform/docs/research/Asimov Harness Research.md`.
- Kiến trúc mục tiêu: `asimov-platform/docs/design/asimov-harness/asimov-harness-architecture.html`.

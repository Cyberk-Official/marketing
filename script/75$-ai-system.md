# Kịch bản Video 90s: Thiết kế giải pháp AI B2B ($75/tháng)

## Tập 1: Tối ưu chi phí hạ tầng và khả năng tự co giãn ($75/tháng)

- **Prefer (Hook 0 - 10s):**
  * *Visual:* Zoom cận cảnh vào con số `run_cost_launch_usd_month: 75-125` trong phần cấu hình dự án của tài liệu.
  * *Voice:* "75 đến 125 USD một tháng. Đây là toàn bộ chi phí vận hành dự kiến cho một hệ thống Ây-Ai tự vận hành hai tư trên bảy: tự động đọc email, tin nhắn WhatsApp, giải mã tiếng lóng đặt hàng, chủ động nhắn tin xác nhận với khách bằng ngôn ngữ tự nhiên để lấy xác nhận, sau đó tự động lên đơn và gửi thẳng về CRM của doanh nghiệp Bi tu bi mà không cần bất kỳ sự can thiệp thủ công nào."

- **Acknowledge (Mục tiêu 10s - 35s):**
  * *Visual:* Góc máy chéo sau vai kỹ sư đang lướt qua các dòng cấu trúc hạ tầng trên file tài liệu kiến trúc. Kỹ sư vẽ phác thảo 3 biểu tượng tương ứng với 3 nỗi lo của Founder lên bảng vẽ.
  * *Voice:* "Khi thiết kế giải pháp này, mục tiêu của chúng tôi là giải quyết triệt để 3 bài toán lớn của doanh nghiệp: Một là: Không chạy thì không phát sinh chi phí. Hai là: Tự động co giãn từ 0 đến 100 nghìn người dùng đồng thời mà không cần can thiệp thủ công. Ba là: Tích hợp mượt mà vào hệ thống quản lý sẵn có của doanh nghiệp."

- **Trust (Giải pháp cho Mục tiêu 1 & 2: 35s - 55s):**
  * *Visual:* Màn hình show sơ đồ Durable Objects độc lập cho từng cuộc hội thoại và Prompt Caching.
  * *Voice:* "Để hệ thống 'không chạy không tốn tiền' và tự co giãn, chúng tôi thiết kế toàn bộ code chạy trên hạ tầng Serverless của Cloudflare Workers, kết hợp gọi Ây-Ai qua cổng OpenRouter theo cơ chế pay-as-you-go, nghĩa là chỉ tính tiền trên lượng ký tự thực tế được xử lý. Khi không có khách đặt hàng, toàn bộ chi phí máy chủ và chi phí gọi Ây-Ai đều bằng đúng 0 đồng. Đặc biệt, mỗi cuộc trò chuyện sẽ chạy trên một cơ sở dữ liệu siêu nhỏ, độc lập để tự động co giãn khi lượng truy cập tăng vọt. Và ngay cả khi số lượng người dùng tăng lên, chi phí hạ tầng thực tế cũng chỉ tăng nhẹ theo lượng token của Ây-Ai tiêu thụ. Mà chi phí token này đã được chúng tôi tối ưu siêu rẻ nhờ cơ chế caching thông minh."

- **Trust (Giải pháp cho Mục tiêu 3: 55s - 1h15):**
  * *Visual:* Show nhanh code kết nối API sử dụng giao thức OAuth 2.0 và chốt chặn `bc_push_guard`.
  * *Voice:* "Về tích hợp hệ thống, Ây-Ai sẽ kết nối trực tiếp với API của phần mềm Microsoft Business Central sẵn có của doanh nghiệp qua cổng bảo mật OAuth 2.0. Các hệ thống quản lý hay CRM khác như HubSpot cũng đều tích hợp tương tự. Để tránh việc Ây-Ai vô tình đẩy trùng đơn hàng do lỗi mạng chập chờn, một chốt chặn kiểm soát được thiết lập để đảm bảo mỗi đơn hàng chỉ được ghi nhận đúng một lần duy nhất."

- **Stick (Mở vòng lặp 1h15 - 1h25):**
  * *Visual:* Kỹ sư nhìn thẳng vào camera chia sẻ điềm đạm.
  * *Voice:* "Đây là chương đầu tiên trong nhật ký thiết kế giải pháp Ây-Ai Bi tu bi của Cyberk. Ở tập tiếp theo, chúng tôi sẽ chia sẻ cách Ây-Ai đọc hiểu các tiếng lóng đặt hàng đa ngôn ngữ."

- **Action (CTA 1h25 - 1h30):**
  * *Visual:* Trên màn hình hiển thị biểu tượng hộp thư kèm dòng chữ: "Nhắn tin cho Cyberk".
  * *Voice:* "Hãy nhắn tin nếu bạn muốn hiểu sâu hơn về các giải pháp hạ tầng Ây-Ai này nhé."

---

## Tập 2: Bộ máy giải mã tiếng lóng & từ viết tắt thương mại đa ngôn ngữ

- **Prefer (Hook 0 - 10s):**
  * *Visual:* Zoom cận cảnh màn hình Cursor IDE hiển thị tin nhắn WhatsApp thực tế chứa cụm từ lộn xộn: *"carls can 12x50cl 5ctn"* và *"하이네켄 캔 500ml 10박스"*.
  * *Voice:* "Làm thế nào để hệ thống Ây-Ai tự động dịch chính xác những tin nhắn viết tắt, pha trộn nhiều thứ tiếng này thành đúng mã SKU trên phần mềm ERP của doanh nghiệp? Hãy xem cách hệ thống xử lý chỉ trong chưa đầy hai giây."

- **Acknowledge (Mục tiêu 10s - 35s):**
  * *Visual:* Kỹ sư vẽ phác họa 3 bài toán lớn lên bảng vẽ: (1) Khách hàng không bao giờ đặt hàng theo đúng mã SKU chuẩn; (2) Tiếng lóng viết tắt thay đổi theo thói quen của từng khách hàng; (3) Bắt khách hàng dùng app đặt hàng mới sẽ làm giảm tỷ lệ chuyển đổi.
  * *Voice:* "Khi xây dựng tính năng này, mục tiêu của chúng tôi là: Một: Giữ nguyên thói quen nhắn tin tự do của khách hàng qua WhatsApp. Hai: Đảm bảo độ chính xác tuyệt đối khi ánh xạ sang danh mục SKU nội bộ. Ba: Không bắt khách hàng hay đối tác phải học cách sử dụng bất kỳ ứng dụng mới nào."

- **Trust (Giải pháp cho Mục tiêu 1 & 2: 35s - 55s):**
  * *Visual:* Sơ đồ luồng giải quyết SKU 3 tầng hiện lên màn hình: Exact Alias $\rightarrow$ Fuzzy Match $\rightarrow$ bge-m3 Vector Search. Zoom cận cảnh đoạn code gọi Vectorize trên Cloudflare Workers.
  * *Voice:* "Để giải mã tiếng lóng, chúng tôi thiết kế bộ lọc SKU ba tầng. Tầng đầu tiên quét bảng danh từ viết tắt lịch sử riêng của từng khách hàng. Nếu không khớp, tầng hai dùng thuật toán so khớp mờ xử lý các lỗi chính tả nhẹ. Tầng cuối cùng, câu chữ được chuyển đổi thành vector toán học bằng mô hình bge-m3 để tìm kiếm ngữ nghĩa trên Cloudflare Vectorize. Cuối cùng, mô hình ngôn ngữ lớn sẽ chấm điểm độ tin cậy cho từng dòng đơn hàng."

- **Trust (Giải pháp cho Mục tiêu 3: 55s - 1h15):**
  * *Visual:* Màn hình hiển thị đoạn code kiểm tra ngưỡng độ tự tin (confidence threshold) trong Cursor IDE và tin nhắn WhatsApp tự động hỏi lại khách hàng.
  * *Voice:* "Với những sản phẩm đạt độ tin cậy trên 90%, đơn hàng sẽ được duyệt tự động. Những sản phẩm nằm dưới ngưỡng này sẽ được gom lại để hệ thống tự động gửi tin nhắn hỏi lại khách hàng qua các nút bấm tiện lợi. Khách hàng chỉ cần bấm chọn ngay trên WhatsApp mà không cần cài thêm app."

- **Stick (Mở vòng lặp 1h15 - 1h25):**
  * *Visual:* Kỹ sư mỉm cười nhẹ, chỉ vào sơ đồ máy trạng thái trên bảng vẽ.
  * *Voice:* "Đây là tập hai trong chuỗi nhật ký thiết kế giải pháp Ây-Ai của Cyberk. Ở tập tiếp theo, chúng tôi sẽ chia sẻ cách hệ thống hỏi lại khách hàng một cách thông minh mà không đoán mò bằng Durable Objects."

- **Action (CTA 1h25 - 1h30):**
  * *Visual:* Trên màn hình hiển thị text: "Nhắn tin cho Cyberk".
  * *Voice:* "Hãy nhắn tin cho Cyberk nếu bạn muốn xây dựng bộ máy giải mã đơn hàng đa ngôn ngữ này nhé."

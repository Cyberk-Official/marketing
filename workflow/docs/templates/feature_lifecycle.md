# Template: Vòng Đời Của Một Tính Năng (Anatomy of a Feature)

**Đối tượng:** Product, Engineering, Design teams.
**Mục tiêu:** Giúp team hiểu rõ hành trình của một tính năng từ ý tưởng đến khi ra mắt, thấy được sự kết nối giữa các vai trò, và trân trọng công sức của nhau. Đây là câu chuyện về sự hợp tác.

---

## 1. Khởi Nguồn Ý Tưởng (The Spark)

*Explain: Tính năng này đến từ đâu?*
*Instruction: Mô tả nguồn gốc của ý tưởng: từ phản hồi của người dùng, phân tích dữ liệu, hay một buổi brainstorming của team.*

* *Good Example: "Trong buổi phỏng vấn người dùng tuần trước, 5/5 người dùng nói rằng họ gặp khó khăn trong việc tìm kiếm sản phẩm. Điều này đã châm ngòi cho ý tưởng về tính năng 'Tìm kiếm nâng cao'."*

## 2. Giai Đoạn Khám Phá & Thiết Kế (Discovery & Design)

*Explain: Biến ý tưởng thành một bản thiết kế khả thi.*
*Instruction: Mô tả quá trình làm việc của Product Manager và Designer: nghiên cứu thị trường, vẽ wireframe, tạo prototype và user testing. Hãy cho thấy những lựa chọn và sự đánh đổi.*

* **Hành trình của Product & Design:**
  * *Good Example: "Designer đã thử 3 mẫu layout khác nhau. Chúng tôi đã chọn mẫu C sau khi thử nghiệm với người dùng, vì nó cho kết quả tìm kiếm nhanh hơn 2 giây, dù ban đầu trông không đẹp bằng mẫu A."*
  * **Kết quả:** Link đến file Figma, user stories.

## 3. Giai Đoạn "Nhào Nặn" Kỹ Thuật (The Build)

*Explain: Các kỹ sư đã biến bản thiết kế thành hiện thực như thế nào?*
*Instruction: Tech Lead hoặc Senior Dev sẽ mô tả các quyết định kiến trúc quan trọng, những thách thức kỹ thuật đã vượt qua. Đừng sa đà vào code, hãy tập trung vào "câu chuyện" kỹ thuật.*

* **Góc nhìn của Engineering:**
  * *Bad Example: (Dán một đoạn code phức tạp).*
  * *Good Example: "Thách thức lớn nhất là tối ưu tốc độ tìm kiếm với 10 triệu sản phẩm. Chúng tôi đã quyết định dùng Elasticsearch thay vì tìm kiếm trực tiếp trên database, giúp giảm thời gian phản hồi từ 5 giây xuống còn 200ms."*
  * **Kết quả:** Link đến Pull Request, tài liệu kiến trúc (nếu có).

## 4. Giai Đoạn Đảm Bảo Chất Lượng (Quality Assurance)

*Explain: Làm thế nào chúng ta đảm bảo tính năng hoạt động như mong đợi?*
*Instruction: Mô tả công việc của QA: viết test case, thực hiện kiểm thử (manual & automated) và tìm ra những bug "khó nhằn".*

* **Câu chuyện của QA:**
  * *Good Example: "QA đã phát hiện một bug nghiêm trọng ở trường hợp tìm kiếm bằng emoji, có thể làm sập server. Nhờ đó, chúng tôi đã kịp thời sửa lỗi trước khi ra mắt."*
  * **Kết quả:** Link đến báo cáo kiểm thử.

## 5. Ra Mắt & Đo Lường (Launch & Learn)

*Explain: Tính năng đã được đón nhận như thế nào?*
*Instruction: Mô tả quá trình triển khai (deployment), theo dõi các chỉ số và thu thập phản hồi từ người dùng sau khi ra mắt.*

* **Kết quả thực tế:**
  * *Good Example: "Sau 1 tuần ra mắt, 70% người dùng đã sử dụng tính năng tìm kiếm mới. Tỷ lệ chuyển đổi từ tìm kiếm sang mua hàng tăng 15%. Tuy nhiên, chúng tôi nhận được phản hồi rằng bộ lọc theo giá chưa trực quan."*
  * **Hành động tiếp theo:** Tạo ticket để cải thiện bộ lọc trong sprint tới.

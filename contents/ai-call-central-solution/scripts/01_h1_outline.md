# OUTLINE: Thiết kế hệ thống tổng đài AI — tự động gọi điện và chốt lịch hẹn khi có lead mới

**Dự án:** Startup giai đoạn đầu, Singapore, đặt lịch hẹn cho chuyên viên bảo hiểm & bất động sản
**Thời lượng:** 420s · 790–840 từ

---

## 1. Hook

Thiết kế hệ thống tổng đài AI — tự động gọi điện và chốt lịch hẹn khi có lead mới. Nghe đơn giản, nhưng có 3 bài toán kỹ thuật cần giải trước: chống trùng lịch, tuân thủ pháp luật Singapore, và xử lý khi không ai nghe máy.

## 2. Yêu cầu bài toán

Một startup vận hành mô hình đặt lịch hẹn. Yêu cầu dự án: khi có lead điền form, hệ thống gọi lại trong vòng 1 phút, xác nhận nhu cầu tư vấn, chốt lịch hẹn với chuyên viên, tự gọi lại nếu không nghe máy, và chuyển sang người thật khi cần.

Điểm quan trọng: đây là startup giai đoạn đầu, gần như chưa có người dùng thực tế, ngân sách lean, và sản phẩm cần ra thị trường nhanh. Thông tin này đòi hỏi hệ thống phải tiết kiệm tối đa chi phí vận hành khi chưa có người dùng — nếu phải trả hàng trăm đô mỗi tháng cho server và hạ tầng thì rất lãng phí. Nhưng ngược lại, khi startup thành công và lượng cuộc gọi tăng đột biến, hệ thống phải tự động đáp ứng được mà không cần viết lại kiến trúc — chỉ cần trả thêm tiền theo lượng sử dụng là xong.

## 3. Phân tích đề bài

Trước khi code, tôi phân tích 3 ràng buộc kỹ thuật:

- Trí tuệ hội thoại: AI không chỉ đọc kịch bản cứng — nó phải hiểu bài toán kinh doanh đằng sau cuộc gọi. Mỗi ngành có cách hỏi khác nhau: bảo hiểm thì hỏi nhu cầu bảo vệ và timeline, bất động sản thì hỏi vị trí và ngân sách. AI phải nhanh chóng xác nhận nhu cầu thực sự của người gọi, phân loại họ thuộc nhóm nào (đang tìm hiểu, sẵn sàng mua, hay chỉ tham khảo), rồi chốt lịch hẹn ngay — tất cả trong một cuộc gọi ngắn. Và kịch bản phải dễ thay đổi mà không cần viết lại code, vì mỗi chuyên viên có cách tiếp cận khác nhau.

- Compliance: Singapore có 3 lớp luật chồng nhau — MAS (bảo hiểm), CEA (bất động sản), PDPA (dữ liệu cá nhân). AI chỉ được hỏi thông tin thực tế và book lịch, không được tư vấn sản phẩm, so sánh, hay đưa ý kiến suitability. Vi phạm phạt đến S$1M. Vậy nên compliance không thể dựa vào prompt — phải enforced bằng kiến trúc.

- Tốc độ phản hồi: khi người dùng nói xong một câu, AI phải trả lời ngay — không được để im lặng, không được có khoảng chờ. Nếu người gọi phải đợi 2-3 giây mỗi lần AI phản hồi, họ sẽ nghĩ cuộc gọi bị lỗi hoặc cúp máy. Hệ thống phải đảm bảo phản hồi dưới 1 giây, dù AI đang xử lý thông tin phức tạp phía sau.

## 4. Giải pháp kỹ thuật

**Luận điểm 1 — Kiến trúc "không dùng thì không tốn": Giải bài toán startup**

Vì đây là startup giai đoạn đầu, tôi chọn toàn bộ hạ tầng theo nguyên tắc: không có cuộc gọi nào thì không mất đồng nào. Khi cuộc gọi tăng, chi phí tăng tuyến tính — không cần nâng cấp server, không cần thuê thêm người vận hành.

Cụ thể: thay vì thuê server chạy 24/7, tôi dùng serverless — hệ thống chỉ "thức" khi có việc (nhận lead mới, thực hiện cuộc gọi, ghi kết quả), xong lại "ngủ". Database cũng vậy — dùng Neon, một loại database tự động tắt khi không ai truy cập, tự bật lại trong vài trăm mili-giây khi cần. Tháng đầu chưa có cuộc gọi nào? Chi phí hạ tầng gần bằng 0. Tháng sau có 1000 cuộc gọi? Chỉ trả tiền cho đúng 1000 cuộc đó. Không cần dự đoán trước lượng sử dụng, không cần mua trước tài nguyên.

Về phần voice — thay vì tự xây dựng toàn bộ engine giọng nói (mất hàng tháng), tôi dùng nền tảng managed sẵn có. Nền tảng này xử lý toàn bộ việc nghe → hiểu → trả lời → gọi điện. Tôi chỉ cần tập trung vào nội dung cuộc hội thoại và logic kinh doanh, không cần quan tâm đến hạ tầng giọng nói phía sau.

Chi phí cuối cùng: khoảng $0.11/phút cho mỗi cuộc gọi AI, bao gồm tất cả — cước điện thoại, engine giọng nói, xử lý ngôn ngữ, và database. So với chi phí một nhân viên tổng đài truyền thống, đây là một phần nhỏ.

**Luận điểm 2 — Kịch bản hội thoại thông minh: Làm sao AI hiểu bài toán và phản hồi nhanh?**

Thay vì viết một đoạn chỉ dẫn dài rồi hy vọng AI tự biết phải làm gì, tôi thiết kế cuộc gọi như một luồng có nhiều bước rõ ràng — mỗi bước AI chỉ tập trung vào đúng một việc. Bước chào hỏi thì chào hỏi, bước hỏi nhu cầu thì hỏi nhu cầu, bước chốt lịch thì chốt lịch. AI không cần "nhớ" toàn bộ kịch bản — chỉ cần xử lý đúng bước hiện tại.

Điều này giải quyết cả 2 vấn đề đặt ra: thứ nhất, vì phạm vi suy luận nhỏ hơn nên AI trả lời chính xác hơn và nhanh hơn — mỗi lượt chỉ trả lời dưới 2 câu, nên thời gian xử lý ngắn, cuộc trò chuyện tự nhiên, không có khoảng im lặng. Thứ hai, khi cần thay đổi kịch bản — thêm câu hỏi, đổi thứ tự, điều chỉnh cách hỏi cho từng chuyên viên hay từng ngành — chỉ cần sửa đúng bước đó, không ảnh hưởng phần còn lại.

Thêm một lớp nữa: trong lúc AI đang xử lý việc phức tạp (như kiểm tra lịch trống), AI vẫn nói với người gọi "Tôi đang kiểm tra, một chút nhé" — không bao giờ để im lặng. Người gọi luôn cảm thấy được phản hồi, dù hệ thống đang chạy nhiều thứ phía sau.

**Luận điểm 3 — Chốt lịch không trùng + Tuân thủ pháp luật: Giải bằng kiến trúc, không phải bằng hy vọng**

Khi AI gọi nhiều người cùng lúc, hai cuộc gọi có thể cùng chốt một khung giờ trong cùng một giây. Giải pháp: mỗi lịch hẹn được đánh một mã duy nhất — nếu hai cuộc gọi cùng chốt, hệ thống chỉ chấp nhận cái đầu tiên, cái còn lại tự động đề xuất khung giờ khác. Người gọi không hề biết có xung đột — trải nghiệm vẫn mượt. Dữ liệu lịch hẹn nằm trên Neon database — cùng hạ tầng serverless, cùng nguyên tắc pay-as-you-go.

Quy trình bắt buộc: AI xác nhận nhu cầu xong mới đề xuất lịch. Offer 2-3 khung giờ, người gọi xác nhận bằng giọng nói, rồi mới chốt. Không bao giờ book trước khi qualify.

Về compliance Singapore: thay vì dựa vào việc AI "nhớ" danh sách những gì không được nói (cách này không đáng tin — AI có thể quên hoặc diễn giải sai), tôi thiết kế luồng hội thoại sao cho AI không có cơ hội vi phạm. Khi ai đó hỏi "bảo hiểm nào tốt nhất?", hệ thống tự động chuyển sang người thật — quyết định này được gắn cứng vào kiến trúc, không phải do AI tự phán đoán. Sau mỗi cuộc gọi, hệ thống tự kiểm tra xem AI có vô tình đưa ra lời tư vấn nào không.

Khi gọi mà không ai nghe, hệ thống tự động gọi lại 2-3 lần, cách nhau vài giờ, chỉ trong khung giờ cho phép (8h-21h). Nếu vẫn không nghe, đánh dấu và dừng — không spam.

## 5. Thành quả & kết luận

- Chi phí hạ tầng khi chưa có cuộc gọi: gần bằng 0 (serverless + Neon auto-suspend). Chi phí khi vận hành: ~$0.11/phút all-in. Scale lên không cần thay đổi kiến trúc — chỉ trả thêm tiền.
- Callback < 60 giây, 100% không trùng lịch hẹn, compliance được đảm bảo bằng kiến trúc chứ không phải bằng prompt.
- Takeaway: "Tổng đài AI cho startup không cần phức tạp — cần đúng thiết kế: hạ tầng không tốn tiền khi chưa dùng, kịch bản hội thoại dễ thay đổi, và compliance gắn cứng vào kiến trúc."
- Tập tiếp: thiết kế AI song ngữ Anh-Hoa — khi không engine nhận diện giọng nói nào hiểu Singlish, tại sao chọn 2 agent đơn ngữ thay vì 1 agent đa ngữ.

## 6. CTA

"Nếu bạn quan tâm tới thiết kế hệ thống, hoặc đang làm startup công nghệ, hãy để lại comment để cùng thảo luận nhé."

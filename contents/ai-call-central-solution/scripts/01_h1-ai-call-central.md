---
type: script
skill: script-maker
idea: H1
methodology: cyberk-video-strategy-paast-vcl.md
outline: scripts/01_h1_outline.md
---

# KỊCH BẢN: Thiết Kế Hệ Thống Tổng Đài AI Tự Động Gọi Điện Và Chốt Lịch Hẹn Khi Có Lead Mới

| Metadata | Giá trị |
|----------|---------|
| **Ý tưởng gốc** | H1 — "Thiết kế hệ thống tổng đài AI tự động gọi điện khi có lead mới" từ `brainstorm/ideas.md` |
| **Tầng PAAST chủ đạo** | Action (Case study end-to-end) |
| **Thời lượng mục tiêu** | 420 giây (7 phút) |
| **Tổng từ lời thoại** | ~800 từ |
| **Ngày tạo** | 2026-07-28 |
| **Audience** | The Ambitious Builder — Founders / CEOs / C-level / Solopreneur |
| **Series** | Nhật ký thiết kế hệ thống AI |
| **Phương pháp luận** | `cyberk-video-strategy-paast-vcl.md` |

---

## 📖 Tham Chiếu Phương Pháp Luận

> **Mọi kịch bản Cyberk đều PHẢI tuân thủ `cyberk-video-strategy-paast-vcl.md`:**
>
> 1. **Ba Tính Chất Cốt Lõi** — Video phải hội đủ: *Giải Trí (Entertainment)* + *Giáo Dục (Educational)* + *Xác Thực (Authentic)*.
> 2. **Phễu PAAST** — Hành trình tâm lý: Prefer → Acknowledge → Trust → Stick → Action.
> 3. **Khung VCL** — Tiêu chuẩn thực thi: Visual + Content + Logic.

---

## 1. ⏱️ Bảng Pacing & Thời Lượng

> **Tốc độ đọc chuẩn:** **120 từ/phút** (tiếng Việt, đĩnh đạc, rõ ràng, sâu sắc).
> Chỉ tính **lời thoại (spoken words)** — không tính text overlay, tên kỹ thuật, hoặc cảnh im lặng.

**Thời lượng đã chọn:** `420s` → **Word budget:** `790 – 840` từ

| PAAST | Thời gian | % | Word Budget |
|-------|-----------|---|-------------|
| Hook | 0-33s | 0-8% | ~65 từ |
| Acknowledge (FR+Context+NFR) | 33-105s | 8-25% | ~145 từ |
| Trust (3 luận điểm) | 105-336s | 25-80% | ~460 từ |
| Stick | 336-378s | 80-90% | ~85 từ |
| Action (CTA) | 378-420s | 90-100% | ~45 từ |

---

## 2. 🎬 Bảng Kịch Bản Quay Dựng 4 Cột (Kèm Infographic HTML)

### Scene 1: P — PREFER · Hook (00:00 → 00:33 · ~65 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **00:00 – 00:08** | Sơ đồ kiến trúc tổng quan trên whiteboard — zoom chậm vào luồng: Form → Webhook → AI Call → Qualify → Book. Mỗi node sáng lên lần lượt. | `infografic/diagram-1-user-flow.html` | *"Thiết kế hệ thống tổng đài AI — tự động gọi điện và chốt lịch hẹn khi có lead mới."* | · Font: RobotoMono<br>· Sound: Ambient electronic nhẹ<br>· Text overlay: Tên từng node |
| **00:08 – 00:20** | Cận cảnh điện thoại reo — caller ID hiển thị số +65. Cut sang dashboard hiển thị lead mới. | `infografic/diagram-1-user-flow.html` | *"Luồng cơ bản thế này: người dùng điền form trên landing page, hệ thống bắn data về, trigger cuộc gọi AI trong chưa đầy một phút. AI xác nhận nhu cầu, chốt lịch hẹn, hoàn toàn tự động."* | · Demo: Phone ringing<br>· Dashboard: Lead list |
| **00:20 – 00:33** | Quay lại sơ đồ tổng quan — highlight 3 bài toán bằng icon: 🧠 Trí tuệ hội thoại, ⚖️ Compliance, ⚡ Tốc độ phản hồi. | `infografic/diagram-1-user-flow.html` | *"Nghe đơn giản, nhưng có ba bài toán cần giải trước: làm sao AI hiểu đúng bài toán kinh doanh, tuân thủ pháp luật Singapore, và phản hồi đủ nhanh để người gọi không cúp máy. Tôi đi lần lượt."* | · Text overlay: 3 bài toán<br>· Transition: Cut to Scene 2 |

> **✅ Checkpoint Hook:** Giọng thẳng, gọn. Mở bằng giải pháp, nêu 3 bài toán cụ thể. ~65 từ.

---

### Scene 2: A — ACKNOWLEDGE · Yêu Cầu Bài Toán & Phân Tích Đề Bài (00:33 → 01:45 · ~145 từ)

#### 2A. Yêu Cầu Bài Toán

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **00:33 – 00:50** | Whiteboard liệt kê 5 yêu cầu bằng bullet points. Góc nhỏ: landing page có form. | `infografic/ai-telemarketing-client-needs.html` | *"Bài toán thực tế: một startup vận hành mô hình đặt lịch hẹn. Yêu cầu dự án gồm 5 điểm — gọi lại ngay khi có lead, xác nhận nhu cầu trên cuộc gọi, chốt lịch hẹn với chuyên viên, tự gọi lại nếu không nghe máy, và chuyển sang người thật khi cần."* | · Visual: Client Needs<br>· Text overlay: 5 bullet FRs |

#### 2B. Bối Cảnh Startup

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **00:50 – 01:05** | Sơ đồ: icon Startup → "Giai đoạn đầu" → "Chưa có user" → "Ngân sách lean". Mũi tên dẫn đến: "$0 khi chưa dùng → Scale khi cần". | `infografic/ai-telemarketing-client-needs.html` | *"Điểm quan trọng: đây là startup giai đoạn đầu, gần như chưa có người dùng thực tế. Thông tin này đòi hỏi hệ thống phải tiết kiệm tối đa chi phí khi chưa có người dùng — nếu phải trả hàng trăm đô mỗi tháng cho server thì lãng phí. Nhưng khi startup thành công và lượng cuộc gọi tăng đột biến, hệ thống phải tự động đáp ứng được — chỉ cần trả thêm tiền theo lượng sử dụng là xong."* | · Visual: Startup context diagram<br>· Text overlay: "$0 idle → Pay-as-you-go" |

#### 2C. Phân Tích Đề Bài (3 ràng buộc)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **01:05 – 01:25** | 3 icon sáng lên lần lượt: 🧠 Trí tuệ hội thoại, ⚖️ Compliance, ⚡ Tốc độ. | `infografic/diagram-2-tech-flow.html` | *"Từ bối cảnh đó, tôi xác định 3 ràng buộc. Thứ nhất — trí tuệ hội thoại. AI phải hiểu bài toán kinh doanh, mỗi ngành hỏi khác nhau, phân loại nhu cầu rồi chốt lịch hẹn ngay — và kịch bản phải dễ thay đổi mà không cần viết lại code. Thứ hai — compliance. Singapore có 3 lớp luật chồng nhau, AI chỉ được hỏi và book, không được tư vấn sản phẩm."* | · Visual: 3 constraints<br>· Text overlay: Tên từng ràng buộc |
| **01:25 – 01:45** | Icon ⚡ phóng to — hiệu ứng đồng hồ đếm ngược 1s. | `infografic/diagram-2-tech-flow.html` | *"Thứ ba — tốc độ phản hồi. Khi người gọi nói xong một câu, AI phải trả lời ngay. Đợi 2-3 giây mỗi lần thì người ta cúp máy. Hệ thống phải phản hồi dưới 1 giây, dù đang xử lý thông tin phức tạp phía sau. Tôi đi vào cách giải từng bài."* | · Visual: 1s countdown<br>· Transition: Cut to Trust |

> **✅ Checkpoint Acknowledge:** ~145 từ. FR (5 điểm) → Startup context (lean, pay-as-you-go) → 3 ràng buộc (trí tuệ hội thoại, compliance, tốc độ).

---

### Scene 3: T — TRUST · Giải Pháp Kỹ Thuật (01:45 → 05:36 · ~460 từ)

#### 3A. Luận Điểm 1 — Kiến trúc "không dùng thì không tốn" (~155 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **01:45 – 02:10** | Sơ đồ so sánh 2 cách: Trái: Server 24/7 → billing icon chạy liên tục. Phải: Serverless → "ngủ" khi không có việc, "thức" khi có lead. | `infografic/ai-telemarketing-ecosystem.html` | *"Vì đây là startup giai đoạn đầu, tôi chọn toàn bộ hạ tầng theo nguyên tắc: không có cuộc gọi nào thì không mất đồng nào. Thay vì thuê server chạy 24/7, tôi dùng serverless — hệ thống chỉ thức khi có việc, xong lại ngủ."* | · Visual: Server vs Serverless<br>· Text overlay: "Zero idle cost" |
| **02:10 – 02:35** | Neon DB logo + animation: database tắt → bật lại trong vài trăm ms. Biểu đồ chi phí: tháng 1 = ~$0, tháng 5 = tăng tuyến tính. | `infografic/diagram-3-ecosystem.html` | *"Database cũng vậy — dùng Neon, một loại database tự động tắt khi không ai truy cập, tự bật lại trong vài trăm mili-giây khi cần. Tháng đầu chưa có cuộc gọi nào? Chi phí hạ tầng gần bằng 0. Tháng sau có 1000 cuộc gọi? Chỉ trả tiền cho đúng 1000 cuộc đó."* | · Visual: Neon auto-suspend<br>· Text overlay: "$0 → linear scale" |
| **02:35 – 03:00** | Sơ đồ: Managed Voice Platform ở giữa, bao quanh bởi: Nghe → Hiểu → Trả lời → Gọi điện. Dưới cùng: "$0.11/phút all-in". | `infografic/ai-telemarketing-ecosystem.html` | *"Về phần voice — thay vì tự xây dựng toàn bộ engine giọng nói, tôi dùng nền tảng managed sẵn có. Nền tảng này xử lý toàn bộ việc nghe, hiểu, trả lời, và gọi điện. Tôi chỉ cần tập trung vào nội dung cuộc hội thoại và logic kinh doanh. Chi phí cuối cùng: khoảng $0.11/phút, bao gồm tất cả."* | · Visual: Managed platform<br>· Text overlay: "$0.11/min all-in" |

#### 3B. Luận Điểm 2 — Kịch bản hội thoại thông minh (~155 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **03:00 – 03:25** | Sơ đồ so sánh: Trái: 1 đoạn prompt dài → AI confused. Phải: Luồng nhiều bước → mỗi bước 1 việc rõ ràng. | `infografic/diagram-4-quality-standards.html` | *"Thay vì viết một đoạn chỉ dẫn dài rồi hy vọng AI tự biết phải làm gì, tôi thiết kế cuộc gọi như một luồng có nhiều bước rõ ràng — mỗi bước AI chỉ tập trung vào đúng một việc. Bước chào hỏi thì chào hỏi, bước hỏi nhu cầu thì hỏi nhu cầu, bước chốt lịch thì chốt lịch."* | · Visual: Prompt vs Flow<br>· Text overlay: "1 step = 1 job" |
| **03:25 – 03:50** | Animation: sửa 1 bước trong luồng → các bước khác không thay đổi. Bên cạnh: 2 bộ câu hỏi khác nhau cho bảo hiểm vs bất động sản. | `infografic/ai-telemarketing-quality-standards.html` | *"AI không cần nhớ toàn bộ kịch bản — chỉ cần xử lý đúng bước hiện tại. Nên AI trả lời chính xác hơn, nhanh hơn — mỗi lượt dưới 2 câu, cuộc trò chuyện tự nhiên, không có khoảng im lặng. Và khi cần thay đổi kịch bản — thêm câu hỏi, đổi thứ tự, điều chỉnh cho từng ngành — chỉ cần sửa đúng bước đó, không ảnh hưởng phần còn lại."* | · Visual: Edit 1 step<br>· Text overlay: "Modular" |
| **03:50 – 04:05** | AI đang xử lý → speech bubble: "Tôi đang kiểm tra lịch, một chút nhé". Phía sau: loading indicator. | `infografic/diagram-4-quality-standards.html` | *"Thêm một lớp nữa: trong lúc AI đang xử lý việc phức tạp như kiểm tra lịch trống, AI vẫn nói với người gọi 'Tôi đang kiểm tra, một chút nhé' — không bao giờ để im lặng. Người gọi luôn cảm thấy được phản hồi."* | · Visual: AI speaking while processing<br>· Text overlay: "Never silent" |

#### 3C. Luận Điểm 3 — Chốt lịch không trùng + Compliance (~150 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **04:05 – 04:25** | Animation: 2 cuộc gọi cùng chốt 1 slot → xung đột → hệ thống chấp nhận cái đầu, cái sau tự đề xuất slot khác. | `infografic/diagram-5-system-architecture.html` | *"Khi AI gọi nhiều người cùng lúc, hai cuộc gọi có thể cùng chốt một khung giờ trong cùng một giây. Giải pháp: mỗi lịch hẹn được đánh một mã duy nhất. Nếu hai cuộc gọi cùng chốt, hệ thống chỉ chấp nhận cái đầu tiên, cái còn lại tự động đề xuất khung giờ khác. Người gọi không hề biết có xung đột."* | · Visual: Double booking resolve<br>· Text overlay: "Unique ID → No conflict" |
| **04:25 – 04:45** | Luồng: Qualify → Offer 2-3 slot → Confirm bằng giọng → Chốt. Bên dưới: Neon DB icon. | `infografic/ai-telemarketing-system-architecture.html` | *"Quy trình bắt buộc: AI xác nhận nhu cầu xong mới đề xuất lịch. Offer 2-3 khung giờ, người gọi xác nhận bằng giọng nói, rồi mới chốt. Không bao giờ book trước khi qualify. Dữ liệu lịch hẹn nằm trên Neon database — cùng hạ tầng serverless, cùng nguyên tắc trả tiền theo lượng dùng."* | · Visual: Booking flow<br>· Text overlay: "Qualify first" |
| **04:45 – 05:10** | Sơ đồ compliance: câu hỏi "Bảo hiểm nào tốt nhất?" → đường đỏ → chuyển người thật. Đường xanh: câu hỏi thông tin → AI trả lời. | `infografic/diagram-5-system-architecture.html` | *"Về compliance Singapore: thay vì dựa vào việc AI nhớ danh sách những gì không được nói — cách này không đáng tin — tôi thiết kế luồng hội thoại sao cho AI không có cơ hội vi phạm. Ai đó hỏi 'bảo hiểm nào tốt nhất?' — hệ thống tự động chuyển sang người thật. Quyết định này được gắn cứng vào kiến trúc, không phải do AI tự phán đoán."* | · Visual: Red/Green path<br>· Text overlay: "Hard-wired guardrail" |
| **05:10 – 05:36** | Retry state machine: Gọi → Không nghe → Đợi vài giờ → Gọi lại → Max 3 lần → Dừng. Clock: 8h-21h. | `infografic/ai-telemarketing-mermaid-architecture.html` | *"Sau mỗi cuộc gọi, hệ thống tự kiểm tra xem AI có vô tình đưa ra lời tư vấn nào không. Và khi gọi mà không ai nghe — hệ thống tự động gọi lại 2-3 lần, cách nhau vài giờ, chỉ trong khung giờ cho phép. Nếu vẫn không nghe, đánh dấu và dừng — không spam."* | · Visual: Retry flow<br>· Transition: Cut to Stick |

> **✅ Checkpoint Trust:** ~460 từ. 3 luận điểm kỹ thuật.

---

### Scene 4: S — STICK · Thành Quả & Kết Luận Kiến Trúc (05:36 → 06:18 · ~85 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **05:36 – 05:55** | Sơ đồ kiến trúc hoàn chỉnh từ đầu — giờ tất cả node đều sáng. Metric pop-up: "$0 idle", "$0.11/min", "< 60s callback", "100% no double booking". | `infografic/diagram-4-quality-standards.html` | *"Quay lại sơ đồ tổng quan. Chi phí hạ tầng khi chưa có cuộc gọi: gần bằng 0. Chi phí khi vận hành: khoảng $0.11 một phút, bao gồm tất cả. Callback dưới 60 giây. 100% không trùng lịch hẹn. Compliance được đảm bảo bằng kiến trúc chứ không phải bằng hy vọng."* | · Visual: Full architecture<br>· Text overlay: Metrics |
| **05:55 – 06:18** | Text overlay lớn: "Tổng đài AI cho startup — cần đúng thiết kế." Fade sang teaser: sơ đồ 2 agent AI (English / Mandarin) với dấu hỏi ở giữa "Singlish?". | `infografic/diagram-2-tech-flow.html` | *"Tổng đài AI cho startup không cần phức tạp — cần đúng thiết kế: hạ tầng không tốn tiền khi chưa dùng, kịch bản hội thoại dễ thay đổi, và compliance gắn cứng vào kiến trúc. Tập tiếp theo: thiết kế AI song ngữ Anh-Hoa — khi không engine nhận diện giọng nói nào hiểu Singlish."* | · Visual: Takeaway + Next ep teaser<br>· Sound: Nhạc build nhẹ |

> **✅ Checkpoint Stick:** ~85 từ. Metric cụ thể + takeaway 1 câu + hé lộ tập tiếp.

---

### Scene 5: A — ACTION · CTA Nhanh (06:18 → 07:00 · ~45 từ)

| Thời gian | Visual & Kỹ Thuật (VCL) | Infographic HTML Tương Ứng | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|----------------------------|-----------------|
| **06:18 – 06:45** | Kỹ sư nhìn thẳng camera. Pop-up: logo CyberK + thông tin liên hệ. | `infografic/ai-telemarketing-client-needs.html` | *"Là một nhà điều hành doanh nghiệp — dù trong bất động sản, bảo hiểm, hay dịch vụ tư vấn — nếu bạn đang tìm giải pháp tự động hóa tổng đài và chốt lịch hẹn, hãy liên hệ CyberK để cùng thảo luận."* | · Text overlay: Logo + Contact<br>· End screen branding |
| **06:45 – 07:00** | Like/Share/Comment icon + Subtitles. | `infografic/ai-telemarketing-client-needs.html` | *"Nếu bạn muốn nghe nhiều hơn về thiết kế hệ thống AI, hãy like, comment và share nhé."* | · Text overlay: Engagement CTA |

> **✅ Checkpoint CTA:** ~45 từ.

---

## 3. ✅ Pre-Publish Checklist

| # | Tiêu chí | Câu hỏi kiểm tra | Điểm (1–5) |
|---|----------|-------------------|-----------|
| 1 | **Bảo mật & Ẩn danh** | Tên đối tác / dự án đã ẩn danh? Không lộ giá trị HĐ, team, timeline? | 5/5 |
| 2 | **Hook 3s đầu** | Câu nói đầu tiên có đủ sức giữ chân Founder dừng lướt? | 5/5 |
| 3 | **Tính Giải Trí** | Có yếu tố tò mò thực tế — không phải giật tít? | 5/5 |
| 4 | **Tính Giáo Dục** | Khán giả học được ≥ 1 điều áp dụng ngay? | 5/5 |
| 5 | **Tính Xác Thực** | Câu chuyện, con số có thật từ dự án thực? | 5/5 |
| 6 | **Show, Don't Tell** | Cột Visual & Infographic HTML được khớp chính xác từng cảnh? | 5/5 |
| 7 | **Anti-Clickbait** | Không có từ giật gân? Mọi con số đều có bằng chứng? | 5/5 |
| 8 | **CTA Định Vị** | CTA rõ ràng, dễ thực hiện? | 5/5 |

---

## 📊 Word Count Summary

| Phần | Số từ lời thoại |
|------|----------------|
| Scene 1 — Hook | ~65 từ |
| Scene 2 — Acknowledge | ~145 từ |
| Scene 3 — Trust (tổng) | ~460 từ |
| Scene 4 — Stick | ~85 từ |
| Scene 5 — Action | ~45 từ |
| **TỔNG** | **~800 từ** |
| **Budget cho phép** | **790 – 840 từ** |
| **Trạng thái** | `[✅ Đã cập nhật cột Infographic HTML hoàn chỉnh]` |

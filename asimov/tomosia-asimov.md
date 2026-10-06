---
type: mkt
title: "Tomosia × Asimov: đề xuất lộ trình hợp tác"
tags: [asimov, tomosia, partnership, roadmap, pitch-deck, open-source]
created-date: 2026-09-29
updated-date: 2026-09-30
author: anderson
status: draft v0.6
voice-check: pending
based-on: asimov-laws-whitepaper.md (v0.3), asimov-roadmap.md (v0.1)
---

# Tomosia × Asimov: đề xuất lộ trình hợp tác (bản nháp 0.6)

**Người đọc:** ban lãnh đạo Tomosia, đọc một mình, không có người thuyết trình. Mỗi slide phải tự đứng được.
**Mục tiêu:** đọc xong, Tomosia hiểu Asimov là gì, thấy bốn hình thức hợp tác, và có đủ thông tin để chọn một hoặc nhiều hình thức.
**Gửi kèm:** `asimov-roadmap.md` (chi tiết module, skill, hướng phát triển và lộ trình sản phẩm), whitepaper *Ba định luật Asimov cho phát triển phần mềm bằng AI*.

Những chỗ còn chờ Anderson quyết định được đánh số `[CẦN CHỐT n]` và gom ở cuối file. Xóa hết trước khi gửi.

---

## Phần 1 — Asimov

### Slide 1 · Asimov là gì

**Vấn đề.** Với Claude Code, Codex hay Cursor, một lập trình viên mô tả tính năng bằng vài câu và nhận lại phần lớn code trong vài chục phút. Các dự án được dựng nhanh như vậy mà Cyberk nhận lại qua dịch vụ Source Code Rescue thường có chung một diễn biến: vài tuần đầu chạy tốt, sau đó sửa một bug làm hỏng hai màn hình khác, và không ai trong team giải thích được một luồng chính chạy thế nào.

Các team thường xử lý theo một trong hai hướng. Để AI tự do thì code ra nhanh, nhưng quyết định của agent lúc không ai nhìn vẫn nằm lại trong codebase. Bắt người đọc từng dòng diff thì chỉ đứng được khi pull request nhỏ; 500 dòng thường được approve cho xong.

**Asimov** là một bộ luật chi tiết dành cho AI về tiêu chuẩn phát triển phần mềm, xây dựng trên tinh thần code sạch. Bộ luật có quy tắc cho từng bước: tiếp nhận yêu cầu, thiết kế, lập kế hoạch, build, review, debug, lưu trữ, release.

| Dạng | Là gì |
|---|---|
| Skill | Tài liệu agent nạp vào trước khi làm việc: cách làm và chuẩn mực phải giữ |
| Gate | Hook và lệnh CLI kiểm tra hành động của agent, trả về exit code, chặn bước tiếp theo nếu không đạt. Ví dụ: sửa file ngoài phạm vi task bị chặn; task chỉ được đánh dấu xong khi chương trình đã chạy kiểm tra và ghi lại kết quả |

Gate chạy ở tầng công cụ, nên Asimov không gắn với model nào. Đổi từ Claude sang GPT, DeepSeek hay Kimi thì bộ luật vẫn giữ nguyên.

**2020** tài liệu đào tạo kỹ sư nội bộ Cyberk · **2024** Cyberk-Flow, workflow cho coding agent · **02/2026** Asimov

---

### Slide 2 · Ba định luật

**Định luật 1.** AI phải tuân thủ kiến trúc của hệ thống, và không được đứng nhìn kiến trúc bị vi phạm, kể cả khi vi phạm đó không do nó gây ra.

**Định luật 2.** AI phải tuân thủ mệnh lệnh của con người, trừ khi mệnh lệnh đó mâu thuẫn với Định luật 1. Tuân thủ nghĩa là làm thật và nói thật: không chọn cách dễ thay cho cách đúng, và không bao giờ báo đã xong một việc chưa xong.

**Định luật 3.** Trong giới hạn của Định luật 1 và 2, AI được tự do hành động bằng toàn bộ năng lực của mình, và tự giữ cho mình những giới hạn mà một kỹ sư chân chính sẽ giữ, kể cả khi không ai giám sát.

| | Trong thực tế | Ai đặt ra | Giữ bằng |
|---|---|---|---|
| 1 | Code theo tài liệu thiết kế. Thấy chỗ khác làm sai thiết kế thì báo. Thấy chính thiết kế sai thì báo người thiết kế, không tự sửa, không code lách | Người thiết kế hệ thống cùng team | Gate |
| 2 | Không báo "test pass" khi chưa chạy test. Không sửa test cho khớp code. Không làm theo yêu cầu phá kiến trúc, và nói rõ vì sao | Người đang làm việc với AI | Gate, người duyệt, bằng chứng |
| 3 | Tự chọn cách giải quyết, tự refactor trong phạm vi. Không để lại code bẩn dù không ai review tới | Chính AI | Chuẩn mực viết trong skill, bằng chứng tích lũy |

Không bộ luật nào kín tuyệt đối. Asimov làm giảm khả năng AI đi ra ngoài giới hạn, và để lại bằng chứng khi điều đó xảy ra.

---

### Slide 3 · Mục tiêu và sứ mệnh

**Câu hỏi Asimov trả lời.** Làm sao để AI được hành động bằng toàn bộ năng lực của nó, trong khi hành vi của nó vẫn dự đoán được?

**Sứ mệnh.** Viết chuẩn mực của nghề kỹ sư phần mềm thành luật mà AI mang theo vào mỗi task, và kiểm tra bằng chương trình những gì kiểm tra được. `[CẦN CHỐT 1]`

**Mục tiêu.** Con người và AI làm việc cùng nhau với một mức tin tưởng có cơ sở: biết trước AI sẽ không làm gì, và đã nhiều lần thấy nó giữ đúng như vậy.

**Vì sao cần.** Các hãng làm model đã dạy AI chuẩn mực của một người tử tế: không giúp việc phi pháp, cố gắng trung thực. Làm phần mềm cần thêm chuẩn mực của một kỹ sư tử tế, gắn với từng nghề và từng dự án. Phần đó các hãng làm model không viết thay được.

**Niềm tin.** AI sẽ là một người bạn đáng tin cậy của loài người.

---

### Slide 4 · Các cụm module: phát triển phần mềm

Bốn engine nối thành một đường ống, từ yêu cầu của đối tác tới bản phát hành:

```text
Yêu cầu đối tác → BA → Architect → Coding → Code Review → Coding (lưu trữ, release)
```

| Engine | Làm gì | Skill |
|---|---|---|
| **BA Engine** | Quản lý và phân tích yêu cầu, lấy cảm hứng từ IBM DOORS. Mỗi yêu cầu ghi hai thông tin tách nhau: đến từ đâu (đối tác nói, team suy ra, giả định), và ai đã xác nhận, trích dẫn tới từng dòng trong biên bản, email hay tin nhắn gốc. Dùng được cho cách làm theo ticket và theo man-month | `asimov-brd` |
| **Architect Engine** | AI và con người cùng đưa ra kiến trúc và giải pháp: blueprint cho cả dự án, rồi spec và kế hoạch cho từng thay đổi. Mỗi task ghi rõ những file được phép sửa | `asimov-blueprint`, `asimov-plan` |
| **Coding Engine** | Build từng task theo kế hoạch: test trước, code sau, có bằng chứng kiểm tra. Debug bắt buộc có bản tái hiện lỗi trước khi sửa. Kiểm thử E2E, release. Có skill riêng cho TanStack (frontend) và Hono (backend) | `asimov-build`, `asimov-run`, `asimov-debug`, `e2e-testing`, `fsd-fe-tanstack`, `hono-stack`, `asimov-archive`, `asimov-ship` |
| **Code Review Engine** | Kiểm định chất lượng source code và xuất báo cáo. Một agent chủ trì và sáu agent chuyên biệt: bảo mật dữ liệu, logic, contract, frontend, hiệu năng, tái sử dụng. Cyberk đang dùng engine này cho dịch vụ Source Code Rescue | `asimov-review`, `asimov-refactor` |

Hai skill dùng chung: `asimov-teach-me` dạy lại cho người trong team tới khi họ tự giải thích được thay đổi; `asimov-html-doc` xuất tài liệu kỹ thuật để chia sẻ.

Giới hạn: skill theo stack mới có cho TanStack và Hono. Stack khác vẫn chạy được toàn bộ quy trình, nhưng chưa có quy tắc riêng.

---

### Slide 5 · Các cụm module: quản lý tổ chức và dự án

| Module | Làm gì | Tích hợp |
|---|---|---|
| **Org Dashboard** | Quản lý tổ chức, có CLI đi kèm: nhân sự, team, ca làm, chấm công, lịch làm việc, thành viên dự án. Quản lý họp: khớp transcript với lịch họp và gắn vào dự án. Kiểm tra báo cáo hằng ngày bằng AI | Google Workspace, Google Meet, Fireflies.ai, Telegram |
| **Asimov Harness** | Harness quản lý, tương tự Claude Code, dành cho nhà quản lý: hỏi và phân tích dữ liệu dự án bằng số liệu, đối chiếu code, task, nhân sự, phòng ban trên một nền tảng | GitHub, GitHub Projects, Org Dashboard |

Harness giữ ba định luật với dữ liệu vận hành:
- AI không đọc thẳng database, chỉ thấy những dòng mà người đang hỏi có quyền xem.
- Việc ảnh hưởng tới người khác (ví dụ duyệt đơn nghỉ) thì AI chỉ tạo đề xuất; người thật duyệt ngoài phiên chat.
- Mọi lời gọi đều được ghi audit, kể cả lời gọi bị từ chối.

Org Dashboard không chấm điểm năng suất, không chụp màn hình, không theo dõi máy của nhân viên.

Giới hạn: cả hai module đang chạy nội bộ Cyberk và được thiết kế cho một tổ chức. Asimov Harness đang ở bản nháp 0.1.

---

## Phần 2 — Hợp tác

### Slide 6 · Tomosia × Asimov

**Asimov sẽ được phát hành dưới dạng mã nguồn mở.** Mục đích là đưa cách làm phần mềm cùng AI tới cộng đồng lập trình viên, với càng nhiều người dùng càng tốt. Một bộ luật chỉ một công ty dùng thì chỉ là quy trình nội bộ. Nó có giá trị khi nhiều team dùng và góp ý cho nó.

**Asimov tìm những đối tác có chung cách nhìn về tương lai của nghề làm phần mềm**, để cùng phát triển Asimov và dùng nó làm lợi thế cạnh tranh. Thứ hai bên cùng chia sẻ:
- lý luận: ba định luật và whitepaper;
- công cụ: skill, gate, CLI và các module của Asimov;
- thực tiễn: dự án chạy thật bằng Asimov, cùng bài học rút ra từ chúng.

**Tại sao Tomosia phù hợp với Asimov?** `[CẦN CHỐT 2]`
- Tomosia làm phần mềm cho startup Nhật Bản. Dự án cho thị trường Nhật thường cần tài liệu thiết kế trước khi code, và đó là điều kiện để Định luật 1 có nội dung. Đây là giả định của chúng tôi; dùng thật là cách kiểm tra nó.
- Tomosia có mảng AI R&D và mô hình Offshore Development Center, nơi một cách làm chung giữa nhiều team có giá trị nhất.

---

### Slide 7 · Giá trị của Asimov cho Tomosia

| Tomosia cần | Asimov đưa vào |
|---|---|
| **Giữ đúng yêu cầu của đối tác Nhật.** Yêu cầu đến qua nhiều kênh (họp, BrSE, email, chat) và thay đổi theo thời gian | BA Engine ghi mỗi yêu cầu kèm lời gốc và người đã xác nhận. Khi đối tác hỏi "điều này ai đồng ý", Tomosia trả lời được bằng trích dẫn tới từng dòng |
| **Dùng AI để làm nhanh mà không mất kiểm soát code** | Gate chặn agent sửa ngoài phạm vi task. Task chỉ được tính là xong khi chương trình đã chạy kiểm tra và ghi lại kết quả. Báo cáo tiến độ gửi đối tác dựa trên bằng chứng, không dựa trên lời báo của agent |
| **Nhiều team ODC làm theo cùng một chuẩn** | Cùng một bộ luật cho mọi team, mọi dự án và mọi model. Người mới vào dự án học qua `asimov-teach-me` cho tới khi tự giải thích được hệ thống |
| **Kiểm định chất lượng code** | Code Review Engine với bảy agent chuyên biệt, dùng trước khi bàn giao, và khi tiếp nhận một codebase có sẵn từ đối tác |
| **Biết AI tốn bao nhiêu** | Số token được đếm theo từng thay đổi và từng lần debug, chia theo model và giai đoạn |
| **Có câu trả lời khi đối tác hỏi "các bạn dùng AI thế nào"** | Một phương pháp được viết ra (whitepaper, bộ luật) và bộ công cụ chạy thật, do chính Tomosia cùng phát triển |

Những giá trị trên là điều Cyberk đang thấy trong dự án của mình. Ở Tomosia, chúng cần được kiểm chứng bằng việc dùng thật, và đó là mục đích của vai đối tác sử dụng.

Tomosia không phải đánh đổi gì để có chúng: không hợp đồng ràng buộc, có quyền fork, không chia sẻ dữ liệu (slide 13).

---

### Slide 8 · Các hình thức hợp tác

Bốn hình thức, không theo thứ tự. Tomosia có thể tham gia một hoặc nhiều hình thức cùng lúc, và thêm hay bớt hình thức bất kỳ lúc nào.

| Hình thức | Tomosia | Cyberk | Ràng buộc |
|---|---|---|---|
| **Đối tác sử dụng** | Dùng Asimov trong dự án thật, phản hồi | Cài đặt, hướng dẫn, sửa lỗi và cập nhật theo phản hồi | MOU, NDA |
| **Đối tác chiến lược – nghiên cứu** | Cùng xây phương pháp luận phát triển phần mềm với AI, đóng góp vào mã nguồn Asimov | Duy trì bộ luật và mã nguồn chung, duyệt đóng góp cùng Tomosia | MOU, NDA |
| **Đối tác truyền thông** | Đưa tin về Asimov trên kênh của Tomosia | Đưa tin về Asimov và về Tomosia trên kênh của Cyberk | MOU, NDA |
| **Đối tác chiến lược toàn diện** | Góp vốn liên doanh tại Singapore, đồng sở hữu Asimov | Góp vốn liên doanh, đồng sở hữu Asimov | Hợp đồng liên doanh |

Ví dụ: Tomosia bắt đầu với vai đối tác sử dụng và đối tác truyền thông cùng lúc, thêm vai nghiên cứu khi team đã quen Asimov, và chỉ cân nhắc liên doanh khi thấy Asimov đáng để sở hữu.

---

### Slide 9 · Đối tác sử dụng

**Tomosia dùng Asimov trong dự án thật, Cyberk sửa theo phản hồi.**

| | |
|---|---|
| Phạm vi | Một team, hoặc một đến hai dự án do Tomosia chọn. Dùng bốn engine phát triển phần mềm |
| Tomosia | Cử người phụ trách, dùng Asimov hằng ngày, ghi lại vấn đề gặp phải |
| Cyberk | Cài đặt, hướng dẫn viết tài liệu thiết kế theo Asimov, hỗ trợ khi có sự cố, sửa lỗi và phát hành bản cập nhật theo phản hồi |
| Cách làm việc | Một nơi ghi nhận vấn đề chung; họp hai tuần một lần |
| Đầu ra | Sau 6–8 tuần đầu: báo cáo đánh giá chung. Sau đó: các phiên bản Asimov có thay đổi từ phản hồi của Tomosia |
| Chi phí | `[CẦN CHỐT 3]` |

**Cách bắt đầu nhẹ nhất.** Chạy Code Review Engine trên một repo Tomosia đang có và đọc báo cáo cùng nhau. Việc này không đổi quy trình của team.

**Nên chọn dự án có tài liệu thiết kế**, hoặc dự án mới để viết thiết kế từ đầu. Không có thiết kế thì Định luật 1 không có gì để giữ, và kết quả khó đánh giá.

**Năm câu hỏi báo cáo đánh giá cần trả lời:**
1. Asimov có khớp với cách Tomosia làm với đối tác Nhật (BrSE, tài liệu thiết kế, nghiệm thu), hay phải đổi nhiều?
2. Một lập trình viên mất bao lâu để làm việc được với Asimov mà không cần hỗ trợ?
3. Chi phí token thay đổi thế nào so với cách làm hiện tại?
4. Gate chặn đúng bao nhiêu lần, chặn nhầm bao nhiêu lần?
5. Bao nhiêu lần agent báo "đã xong" mà bằng chứng không khớp?

**Hai loại phản hồi.** Lỗi và thiếu sót của công cụ thì Cyberk sửa. Phản hồi về cách tiếp cận, ví dụ một quy tắc không hợp với quy trình làm việc với đối tác Nhật, thì hai bên cùng bàn, vì thay đổi bộ luật ảnh hưởng tới mọi người dùng Asimov.

---

### Slide 10 · Đối tác chiến lược – nghiên cứu

**Tomosia và Cyberk cùng xây phương pháp luận phát triển phần mềm với AI, và cùng viết mã nguồn Asimov.**

| Việc có thể cùng làm | Ví dụ |
|---|---|
| Bộ luật | Quy tắc mới cho những bước Tomosia làm nhiều mà Asimov còn mỏng, ví dụ làm việc qua BrSE, tài liệu thiết kế theo chuẩn của đối tác Nhật |
| Skill và gate | Skill cho các stack Tomosia đang dùng ngoài TanStack và Hono; chuyển những quy tắc đo được thành gate |
| Nghiên cứu | Các câu hỏi whitepaper còn để ngỏ: đo độ trung thực của agent, thẩm quyền nhiều cấp trong team lớn, so sánh hành vi giữa các model |
| Tài liệu | Hướng dẫn và mẫu tài liệu bằng tiếng Nhật |

**Cách làm việc.** Tomosia lập một team dev đóng góp trực tiếp vào mã nguồn chung. Mỗi thay đổi bộ luật được viết ra và duyệt trước khi sửa skill hay gate, theo đúng nguyên tắc của Asimov: định nghĩa trước, code sau. Hai bên thống nhất trước ai duyệt thay đổi ở từng mức: một skill, một gate, hay một định luật. `[CẦN CHỐT 4]`

**Tomosia nhận được.** Tham gia quyết định hướng đi của Asimov. Kinh nghiệm của team Tomosia đi vào bộ luật chung, và Tomosia là một trong những bên hiểu Asimov sâu nhất khi làm việc với đối tác.

---

### Slide 11 · Đối tác truyền thông

**Tomosia và Cyberk cùng nói về Asimov trên kênh của mình.** Khi nhiều bên cùng nói về một chủ đề, chủ đề đó được chú ý nhiều hơn. Mỗi bài viết về Asimov cũng là một lần nhắc tới cả Cyberk và Tomosia như những đơn vị đang làm phần mềm cùng AI theo một chuẩn mực rõ ràng.

| Nội dung | Ví dụ |
|---|---|
| Tin phát triển | Phiên bản mới, tính năng mới, thay đổi bộ luật |
| Bài kỹ thuật | Cách một gate hoạt động, cách viết tài liệu thiết kế để AI đọc được |
| Câu chuyện dự án | Một team dùng Asimov gặp gì, sửa gì, học được gì. Không nêu tên đối tác, không dùng dữ liệu của dự án |
| Sự kiện | Meetup, buổi chia sẻ kỹ thuật, workshop cho lập trình viên |

**Nguyên tắc nội dung.** Chỉ nói những gì đã làm thật. Con số phải có nguồn đo. Đây là Định luật 2 áp dụng cho chính cách hai bên nói về Asimov.

---

### Slide 12 · Đối tác chiến lược toàn diện

**Thành lập liên doanh tại Singapore để sở hữu và phát triển Asimov.**

- Tomosia đồng sở hữu tài sản trí tuệ và giá trị công ty.
- Tomosia sở hữu cổ phần Asimov.
- Cổ phần đi kèm cam kết đóng góp vào tầm nhìn chung.

Asimov khi đó là một tài sản phát triển độc lập, tách khỏi dịch vụ của Cyberk hay của Tomosia. Tomosia giữ Asimov vừa như một khoản sở hữu, vừa như lợi thế cạnh tranh trên thị trường. Pháp nhân riêng cũng là cách để các đối tác sau tham gia theo cùng một điều kiện.

Đây là hình thức duy nhất cần hợp đồng ràng buộc. Những điểm sẽ cần tư vấn pháp lý: cách đưa tài sản trí tuệ Cyberk đã xây từ 2020 vào liên doanh, cách định giá tại thời điểm góp vốn, và cổ phần xử lý thế nào nếu một bên dừng đóng góp. `[CẦN CHỐT 5]`

---

### Slide 13 · Nguyên tắc hợp tác

**Hợp tác mở, không ràng buộc bằng hợp đồng.** Ba hình thức đầu chỉ cần MOU và NDA. Mỗi bên có thể dừng bất kỳ lúc nào. Chỉ hình thức chiến lược toàn diện cần hợp đồng.

**Tomosia luôn có quyền tự đi tiếp.** Mã nguồn Asimov được phát hành theo một giấy phép cho phép Tomosia tự fork và phát triển nhánh riêng, nếu một ngày tầm nhìn của Tomosia về phát triển phần mềm với AI khác đi.

| Giấy phép cho phép | Giấy phép không cho phép |
|---|---|
| Dùng Asimov trong nội bộ và trong các dự án làm cho đối tác | Bán Asimov, hoặc bản sửa đổi của Asimov, như một sản phẩm thương mại |
| Fork, sửa đổi, phát triển nhánh riêng | |

**Chung mã nguồn, riêng dữ liệu.** Tomosia và Cyberk không cần chia sẻ dữ liệu dự án, quy trình nội bộ hay thông tin nhạy cảm. Mỗi bên chạy Asimov trên hạ tầng và database của mình. Thứ hai bên chia sẻ là mã nguồn và bộ luật. Điều này cũng áp dụng cho Org Dashboard và Asimov Harness khi hai module này triển khai được cho tổ chức thứ hai.

---

### Slide 14 · Mục tiêu 2030

**10.000** lập trình viên dùng Asimov hằng ngày.

**15 triệu USD** giá trị Asimov.

Mã nguồn mở là cách để có người dùng. Các đối tác như Tomosia, qua cả bốn hình thức hợp tác, là cách để người dùng thành giá trị. `[CẦN CHỐT 7]`

---

### Slide 15 · Bước tiếp theo

1. Tomosia chọn một hoặc nhiều hình thức hợp tác.
2. Hai bên ký MOU và NDA.
3. Nếu có vai đối tác sử dụng: Tomosia chọn team hoặc dự án, Cyberk cài đặt Asimov và hướng dẫn team trong tuần đầu tiên.

---

## Những điểm cần chốt (xóa trước khi gửi)

| # | Slide | Câu hỏi |
|---|---|---|
| 1 | 3 | Duyệt câu "Sứ mệnh" và "Mục tiêu". Whitepaper không có mục sứ mệnh riêng; hai câu này tổng hợp từ §1, §5.2, §5.5, §6.2, §7 |
| 2 | 6 | Xác nhận thông tin về Tomosia (website 09/2026: 100+ nhân sự, 30+ dự án, Đà Nẵng và Hà Nội, Web, Mobile, AI R&D, ODC) |
| 3 | 9 | Chi phí cho đối tác sử dụng: mỗi bên tự chịu nhân sự, hay có phí hỗ trợ; ai chịu chi phí token |
| 4 | 10 | Quy mô team đóng góp tối thiểu; quy trình và người duyệt thay đổi bộ luật |
| 5 | 12 | Nguyên tắc tính tỷ lệ sở hữu; cam kết đóng góp đo bằng gì; điều kiện để bắt đầu liên doanh |
| 6 | 13 | Chọn giấy phép cụ thể. GPL không cấm dùng thương mại: bất kỳ ai cũng được bán phần mềm GPL, miễn công bố mã nguồn. Muốn cấm bán Asimov như sản phẩm mà vẫn cho dùng trong dự án làm cho đối tác thì cần loại giấy phép khác, ví dụ Business Source License, Elastic License 2.0, hoặc PolyForm. Các giấy phép này thường được gọi là "source-available" chứ không phải "open source" theo định nghĩa của OSI; nếu giữ chữ "mã nguồn mở" trên slide, có người đọc sẽ hỏi. Cần luật sư duyệt |
| 7 | 14 | Số lập trình viên đang dùng Asimov hằng ngày hiện nay, mô hình doanh thu, cơ sở cho mức 15 triệu USD (tương đương khoảng 1.500 USD cho mỗi người dùng hằng ngày). Thiếu hai thứ này, người đọc dễ coi con số là "nổ" |

## Nguồn

- `asimov-laws-whitepaper.md` bản nháp 0.3; `asimov-roadmap.md` bản nháp 0.1; `asimov-harness.md` bản nháp 0.1
- `~/Desktop/asimov/asimov`, `~/Desktop/asimov/asimov-platform` (09/2026)
- Tomosia: https://tomosia.com.vn/ và https://tomosia.com.vn/co-hoi-nghe-nghiep/

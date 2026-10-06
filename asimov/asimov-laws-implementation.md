---
type: reference
title: "Cách Asimov thực thi ba định luật"
tags: [asimov, ai-governance, mechanisms, reference]
created-date: 2026-09-29
updated-date: 2026-09-29
author: anderson
status: draft v0.1
applies-to: Asimov, tình trạng tại 09/2026
companion-of: asimov-laws-whitepaper.md
---

# Cách Asimov thực thi ba định luật

*Tài liệu kỹ thuật đi kèm whitepaper "Ba định luật Asimov cho phát triển phần mềm bằng AI" · Tình trạng tại 09/2026*

Whitepaper trình bày lý luận: ba định luật là gì, vì sao cần chúng, và Asimov giữ chúng theo những nguyên tắc nào. Tài liệu này ghi lại các cơ chế cụ thể trong bộ công cụ Asimov: skill nào, gate nào, lệnh nào giữ định luật nào.

Hai tài liệu được tách ra vì chúng thay đổi theo nhịp khác nhau. Lý luận trong whitepaper được viết để đứng vững lâu dài. Các cơ chế dưới đây thay đổi theo từng phiên bản của Asimov, nên tài liệu này sẽ được cập nhật mỗi khi Asimov thay đổi. Whitepaper (mục 6.2) nói rõ không có vòng tròn nào kín tuyệt đối. Các cơ chế ở đây là phần "cơ quan thực thi" của bộ luật: chúng làm giảm xác suất AI đi ra ngoài vòng tròn, và để lại bằng chứng khi điều đó xảy ra.

---

## 1. Các kiểu lỗ hở

Để thiết kế cơ chế, chúng tôi phân các cách một vòng tròn có thể hở thành sáu kiểu. Đây là khung rút ra từ các dự án rescue và từ việc dùng AI hằng ngày, chưa phải một phân loại đã được kiểm chứng. Các mục sau dùng mã H1 đến H6 này.

| Mã | Kiểu hở | Mô tả | Ví dụ | Định luật |
|---|---|---|---|---|
| H1 | Luật chưa được viết | Không có system design, không có quy tắc dự án | Dự án dựng bằng AI không có tài liệu kiến trúc nào | 1 |
| H2 | Luật không được nhìn thấy | Luật có, nhưng không nằm trong context của agent lúc nó hành động | Tài liệu thiết kế có trong repo, nhưng agent không đọc trước khi sửa | 1 |
| H3 | Luật chỉ là lời khuyên | Luật được viết ra, nhưng không có gì chặn khi bị vi phạm | Quy tắc "không sửa ngoài phạm vi task" nằm trong prompt, agent vẫn sửa lan sang module khác | 1, 2 |
| H4 | Luật bị đi vòng | Có cơ chế chặn, nhưng tồn tại một đường khác không đi qua cơ chế đó | Xóa hoặc nới lỏng test để test pass | 2 |
| H5 | Luật bị diễn giải sai | Agent làm đúng câu chữ nhưng sai ý, hoặc báo cáo sai để làm hài lòng người hỏi | Báo "đã xong" khi chưa chạy test; "sửa" lại một thay đổi có chủ ý của đồng nghiệp vì tưởng đó là lỗi | 2 |
| H6 | Luật xung đột | Hai yêu cầu cùng hợp lệ kéo về hai phía, agent không tiến cũng không dừng | Sửa đi sửa lại cùng một lỗi theo cùng một hướng | 3 |

Có hai hiện tượng chúng tôi không xếp vào bảng này: code chạy đúng và pass test nhưng bẩn, và agent rụt rè, sửa ít nhất có thể để khỏi chịu trách nhiệm. Cả hai không phải lỗ hở của hai vòng ngoài. Chúng là vòng trong không được giữ đúng (whitepaper, mục 4.3).

---

## 2. Nguyên tắc thiết kế

**Lời văn không phải là cưỡng chế.** Một quy tắc viết trong prompt là một lời đề nghị. Agent có thể làm theo trong 99 lần và bỏ qua ở lần thứ 100, đúng lúc context dài nhất và việc gấp nhất. Muốn một luật thực sự là luật, nó phải được kiểm tra bằng một chương trình trả về exit code, không phải bằng việc agent đọc và tự giác.

**Mặc định là chặn (fail-closed).** Khi hệ thống không chắc một hành động có nằm trong vòng tròn hay không, nó chặn và hỏi. Chi phí của một lần hỏi thừa nhỏ hơn nhiều so với chi phí của một lần đi ra ngoài mà không ai biết.

**Gate cho những gì đo được, tư cách cho phần còn lại.** Nguyên tắc thứ nhất đặt ra một câu hỏi cho Định luật 3. Vế tự giới hạn của Luật 3 không giữ được bằng chương trình, vì code bẩn mà vẫn pass test thì không có gì báo đỏ. Nếu lời văn chỉ là lời đề nghị, vòng trong có phải là một lỗ hở kiểu H3 không?

Câu trả lời của chúng tôi là chia quy tắc thành hai loại. *Gate* là những lần kiểm tra bằng chương trình, dùng cho những gì đo được. Gate không phụ thuộc vào sự tự giác của agent. *Tư cách* là chuẩn mực của nghề được viết ra và nạp vào agent trước mỗi việc, dùng cho phần không đo được. Tư cách không chặn được vi phạm ngay lúc nó xảy ra. Nó được kiểm chứng dần qua bằng chứng tích lũy và review, giống cách ta tin một đồng nghiệp sau nhiều lần thấy họ giữ chuẩn (whitepaper, mục 5.1).

Vì vậy vòng trong luôn kém chắc chắn hơn hai vòng ngoài, và whitepaper ghi rõ điều này ở mục 8. Hướng đi hợp lý là chuyển dần những quy tắc tư cách đo được thành gate, và chỉ để lại dạng tư cách cho những gì không bao giờ đo được.

---

## 3. Cơ chế theo từng định luật

### 3.1 Tóm tắt theo nguyên tắc

Asimov giữ mỗi định luật bằng một nguyên tắc thiết kế. Phần tóm tắt dưới đây nêu nguyên tắc đó; các bảng tiếp theo liệt kê cơ chế cụ thể.

**Định luật 1: kiến trúc được viết ra trước, và mỗi việc có phạm vi.** Trước khi có code, yêu cầu của đối tác được ghi lại cùng nguồn gốc và mức độ đã được xác nhận, rồi được tổng hợp thành thiết kế tổng thể và kế hoạch. Mỗi task được giao kèm danh sách file nó được phép sửa, và sửa ra ngoài danh sách thì bị chặn. Review do nhiều agent chuyên biệt thực hiện, mỗi agent nhìn từ một góc, chẳng hạn bảo mật hay hiệu năng, để bắt những chỗ code trôi khỏi thiết kế. Đó là vế "không đứng nhìn" ở cấp công cụ.

**Định luật 2: bằng chứng thay cho lời báo cáo.** Một task chỉ được coi là xong khi chương trình tự chạy bước kiểm tra và ghi lại kết quả. Lời "đã xong" của agent không có giá trị. Sửa bug phải bắt đầu từ một bản tái hiện lỗi đang fail. Xóa hoặc làm yếu test để test pass thì bị từ chối, trừ khi khai báo lý do. Khi thực tế làm thay đổi tiêu chí nghiệm thu hoặc thiết kế đã duyệt, agent dừng lại và trả quyết định về người duyệt kế hoạch.

**Định luật 3: tự do có điểm dừng, và chuẩn nghề được viết ra.** Agent tự chọn phương án ở các bước thông thường, chạy trọn một kế hoạch, và chia việc cho nhiều agent chạy song song. Tự do dừng ở hai chỗ. Các quyết định về phạm vi và rủi ro luôn thuộc về con người. Và khi cùng một lỗi lặp lại ba lần theo cùng một hướng, agent phải lấy ý kiến thứ hai trước khi thử tiếp, để không bị kẹt trong một vòng lặp.

Vế sau của Luật 3 được giữ bằng tư cách (mục 2, mục 4): chuẩn mực của nghề viết trong skill, được agent nạp vào trước mỗi việc. Một ví dụ: *"If you cannot say why it works, it does not work"*, nếu không giải thích được vì sao bản sửa đúng thì coi như chưa sửa được.

### 3.2 Chi tiết cơ chế

**Định luật 1: có thứ để tuân thủ, và không ra ngoài nó**

| Cơ chế | Việc nó làm | Lỗ hở được vá |
|---|---|---|
| `asimov-brd` | Biến yêu cầu thô (email, chat, biên bản họp) thành sổ yêu cầu. Mỗi dòng ghi rõ nguồn gốc (đối tác nói, team suy ra, team đề xuất, team giả định) và mức thẩm quyền (chưa xác nhận, đối tác đã xác nhận, quyết định của team), kèm trích dẫn nguyên văn | H1 |
| `asimov-blueprint` | Tổng hợp thành `docs/DESIGN.md`, các thiết kế chi tiết và `docs/PLAN.md`. Skill này chỉ được ghi vào đúng các file đó | H1 |
| `asimov/project.md`, các skill stack (`hono-stack`, `fsd-fe-tanstack`) | Quy tắc của dự án và chuẩn công nghệ ở dạng agent đọc được | H1 |
| Trường `Refs` trong mỗi task | Chỉ định tài liệu phải đọc trước khi làm task | H2 |
| Task lease | Khi task bắt đầu, các path trong kế hoạch trở thành "hợp đồng thuê". Hook từ chối mọi lần sửa file ngoài hợp đồng | H3 |
| 6 reviewer chuyên biệt | Một agent chủ tọa đọc diff, phân rủi ro cho tối đa sáu reviewer (dữ liệu và bảo mật, logic, hợp đồng API, frontend, hiệu năng, trùng lặp code) | H3 |
| Quét lỗi tương tự trong debug | Sau khi fix xanh, agent phải quét repo tìm các chỗ có cùng mẫu lỗi trước khi được báo `FIXED` | H3, mệnh đề không hành động |

**Định luật 2: con người đi qua cổng, và AI nói thật về việc đã làm**

| Cơ chế | Việc nó làm | Lỗ hở được vá |
|---|---|---|
| Artifact handback | Khi phản hồi của người, một finding review, hay thực tế lúc build làm thay đổi tiêu chí nghiệm thu hoặc thiết kế đã duyệt, agent dừng build, trả về bước lập kế hoạch, và chỉ build tiếp khi kế hoạch mới được duyệt | H3 |
| Cổng duyệt kế hoạch | Kế hoạch phải được người duyệt trước khi build. Agent bị cấm tự đánh dấu cổng này | H3 |
| Giới hạn của fastlane | Chế độ tự động chọn thay người ở các cổng thông thường, nhưng không bao giờ tự quyết việc thêm phạm vi, cắt phạm vi đã duyệt, hay chấp nhận rủi ro | H3 |
| Mức thẩm quyền trong BRD | Một yêu cầu đối tác mới nói nhưng chưa xác nhận thì chưa ràng buộc. Chỉ bốn loại ghi chép cần người duyệt, trong đó có ghi xác nhận của đối tác và quyết định thay đổi phạm vi | H1 |
| Dependency lạ | Tên package không tìm thấy thì dừng lại cho người kiểm tra, không thử tên gần giống (tên đó có thể do AI tưởng tượng, hoặc là package giả mạo) | H5 |
| `verify-task` | Cách duy nhất để đánh dấu một task là xong. Lệnh tự chạy bước verify đã khai báo, ghi kết quả và đóng dấu trạng thái cây code. Tự tay đánh dấu bị từ chối | H5 |
| Theo dõi bộ test | Xóa hoặc làm yếu một test có từ trước khi task bắt đầu thì việc đánh dấu bị từ chối, trừ khi khai báo lý do. Lý do được lưu cạnh kết quả | H4 |
| Debug gate G1 | Không có bản tái hiện lỗi đang FAIL thì mọi lần sửa code production bị chặn | H5 |
| Bản sửa phải sạch | Debug từ chối báo `FIXED` khi diff còn code thăm dò, hoặc khi bản sửa chỉ xóa code mà không giải thích | H5 |
| Ship guard | Chặn release khi còn thay đổi nào chưa qua verify | H3 |

**Định luật 3: tự do, và lúc tự do phải dừng**

| Cơ chế | Việc nó làm | Lỗ hở được vá |
|---|---|---|
| Debug gate G4 và khóa sau 3 lần fail | Cùng một lỗi fail ba lần thì khóa, bắt buộc lấy ý kiến thứ hai từ model khác hoặc con người trước khi thử tiếp | H6 |

Và phần tự do mà Định luật 3 trao cho agent:

| Cơ chế | Việc nó làm |
|---|---|
| Fastlane | Tự chọn phương án khuyến nghị ở các cổng thông thường, không dừng lại hỏi |
| `asimov-run` | Chạy toàn bộ `PLAN.md` theo thứ tự phụ thuộc |
| Filler song song | Build các task độc lập bằng nhiều agent cùng lúc, mỗi agent có lease riêng |
| Chính sách chọn model | Mở đầu bằng model tầm trung, chỉ leo lên model mạnh nhất khi gặp khó |

## 4. Những quy tắc không gate nào kiểm tra

Các cơ chế ở mục 3 đều là gate: chương trình kiểm tra và chặn. Chúng giữ vòng ngoài và vòng giữa. Vòng trong của Định luật 3 không giữ được bằng gate, vì những giới hạn đó nằm ở chỗ không có gì để chặn. Code bẩn mà vẫn pass test thì không có exit code nào báo đỏ.

Asimov đã có loại quy tắc thứ hai này, dù trước đây chúng tôi chưa gọi tên nó. Skill `asimov-debug` có hẳn một mục tên là *"Six rules no gate enforces for you"*, tức sáu quy tắc không có gate nào cưỡng chế thay bạn. Dưới đây là các quy tắc loại này đang nằm trong skill:

| Quy tắc (nguyên văn) | Skill | Nghĩa |
|---|---|---|
| *"If you cannot say why it works, it does not work."* | `asimov-debug` | Không giải thích được vì sao bản sửa đúng thì coi như chưa sửa được |
| *"Fix the fault, not the failure."* | `asimov-debug` | Sửa nguyên nhân, không sửa chỗ lỗi hiện ra |
| *"A fixed sleep is never evidence."* | `asimov-debug` | Chờ cố định vài giây rồi thấy xanh không chứng minh được gì |
| *"Comments, specs and design notes are hypotheses, not constraints."* | `asimov-debug` | Một dòng comment nói "chỗ này cố ý" chưa phải là bằng chứng |
| *"If you think 'this is too simple to test' — you are wrong. Write the test."* | `asimov-build` | Không có thay đổi hành vi nào quá đơn giản để test |
| *"Default to bounded + incremental."* | `asimov-build` | Mọi tập dữ liệu tăng theo thời gian phải có giới hạn, kể cả job chạy ban đêm |
| *"Evidence over intent."* | `asimov-review` | Ý định trong comment không miễn trừ được một finding |

Gate và tư cách bổ sung cho nhau. Gate bắt được những gì đo được, và không phụ thuộc vào việc agent có tự giác hay không. Tư cách phủ phần còn lại, và phụ thuộc vào việc chuẩn mực có được viết ra rõ ràng và nạp vào đúng lúc hay không. Một hướng phát triển của Asimov là chuyển dần những quy tắc tư cách đo được thành gate. Những quy tắc không bao giờ đo được sẽ luôn cần ở dạng tư cách.

## 5. Ba tình huống

**Kịch bản 1: lập trình viên mới muốn xóa một module.** Yêu cầu đi qua `asimov-plan`. Nếu nó đụng một quyết định kiến trúc chưa được chốt, skill lập kế hoạch dừng lại và trả việc về bước định hình, vì thay đổi `DESIGN.md` là việc của `asimov-blueprint`, không phải của một change. Dù đi đường nào, kế hoạch cũng phải qua cổng duyệt của con người trước khi build. Nếu yêu cầu đi thẳng vào lúc build, lease chặn việc sửa file ngoài phạm vi task hiện tại, và một thay đổi về tiêu chí nghiệm thu buộc agent trả về lập kế hoạch.

Chỗ còn thiếu: Asimov chưa có một kiểm tra tự động đối chiếu từng yêu cầu với từng điều khoản kiến trúc. Hiện tại, việc nhận ra "yêu cầu này đụng kiến trúc" vẫn dựa vào agent lập kế hoạch và người duyệt kế hoạch. Quy tắc "từ chối phải có trích dẫn" (whitepaper, mục 4.2) là hướng chúng tôi muốn đi.

**Kịch bản 2: sửa mãi không xong.** Agent sửa một bug, chạy lại bản tái hiện, vẫn đỏ. Nó sửa theo hướng khác, vẫn đỏ với cùng lỗi. Lần thứ ba, vẫn đỏ. Gate G4 khóa quyền sửa. Agent phải đưa sổ ghi các giả thuyết đã loại trừ cho một góc nhìn mới (model khác, cách đặt vấn đề khác, hoặc con người) trước khi được thử tiếp. Tài liệu debug ghi rõ: không bao giờ thử lần thứ tư trên cùng một hướng. Một lỗi *thay đổi* sau mỗi lần sửa thì không bị tính, vì đó là tiến triển.

**Kịch bản 3: báo xong khi chưa xong.** Agent viết xong code và báo "tất cả test đã pass". Trong Asimov, câu nói đó không có giá trị. Task chỉ được đánh dấu xong khi `verify-task` tự chạy lệnh verify và ghi kết quả. Nếu sau đó code bị sửa thêm, bằng chứng cũ hết hiệu lực, và gate cuối cùng chạy lại toàn bộ bộ lệnh trên trạng thái code hiện tại.

---

## 6. Chỗ còn thiếu ở cấp công cụ

Những giới hạn dưới đây thuộc về phiên bản hiện tại của Asimov, không thuộc về ba định luật.

- **Gate có thể bị đi vòng.** Các gate chặn lệnh `Edit` và `Write` của agent. Một lần sửa file qua `Bash` thì gate không nhìn thấy. Đây là lỗ hở kiểu H4 đã biết. Lệnh `doctor` của `asimov-debug` chạy thử các gate trên một bộ dữ liệu mẫu phải bị từ chối, vì như tài liệu của skill viết, một gate chưa bao giờ kích hoạt và một gate đã cho phép trông giống hệt nhau từ bên ngoài.
- **Chưa có gate "từ chối phải có trích dẫn".** Việc nhận ra một yêu cầu đụng tới kiến trúc vẫn dựa vào agent lập kế hoạch và người duyệt kế hoạch.
- **Chưa có công cụ dựng lại blueprint từ code có sẵn.** Với dự án chưa có kiến trúc được viết ra, mỗi thay đổi tự ghi spec và thiết kế của riêng nó, và kiến trúc được bổ sung dần.

---

## Thuật ngữ công cụ

| Thuật ngữ | Nghĩa |
|---|---|
| Lease | Danh sách path một task được phép sửa; sửa ngoài danh sách bị hook từ chối |
| `verify-task` | Lệnh duy nhất đánh dấu một task là xong; tự chạy bước verify và ghi bằng chứng |
| Fastlane | Chế độ agent tự chọn phương án khuyến nghị ở các cổng thông thường |
| Blueprint | Bộ tài liệu thiết kế tổng thể: `DESIGN.md`, thiết kế chi tiết, `PLAN.md` |
| Filler | Agent phụ build một task trong một đợt chạy song song |
| Fail-closed | Khi không chắc một hành động có nằm trong vòng tròn hay không, mặc định chặn và hỏi |

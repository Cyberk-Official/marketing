---
type: mkt
title: "Asimov — Pitch deck"
tags: [asimov, pitch-deck, ai-governance, service]
created-date: 2026-09-29
updated-date: 2026-09-29
author: anderson
status: draft v0.2
voice-check: pending
based-on: asimov-laws-whitepaper.md
---

# Asimov — Pitch deck (bản nháp 0.2)

**Người nghe chính:** CTO và founder đang dùng hoặc sắp dùng AI để làm phần mềm.
**Mục tiêu sau buổi pitch:** người nghe hiểu ba định luật, tin rằng Cyberk làm phần mềm có kiểm soát nhờ Asimov, và chọn một bước tiếp theo (Health Check, Product Build, hoặc một buổi demo Asimov).
**Độ dài:** 18 slide, khoảng 24 phút.
**Nguồn nội dung:** `asimov-laws-whitepaper.md`. Mọi con số trong deck lấy từ repo, không làm tròn thêm.

Cách đọc file: mỗi slide có ba phần. **Trên slide** là chữ thật sự xuất hiện (giữ ít). **Hình** là gợi ý cho designer. **Lời nói** là nội dung người thuyết trình nói.

---

## Phần 1 — Vấn đề

### Slide 1 · Bìa

**Trên slide**
> # Asimov
> Ba định luật cho AI lập trình, và bộ công cụ Cyberk dùng để cưỡng chế chúng.

**Hình:** logo Asimov (ba quỹ đạo) ở giữa, nền tối.

**Lời nói:** Hôm nay tôi nói về cách Cyberk cho AI viết phần lớn code mà vẫn biết trước nó sẽ làm gì và không làm gì.

---

### Slide 2 · Những dự án đến tay chúng tôi

**Trên slide**
> Dự án dựng bằng Cursor, Lovable, Bolt, Claude Code. Vài tuần đầu chạy tốt. Rồi:
> - Mỗi lần release lại hỏng một thứ từng chạy được
> - Không ai giải thích được một luồng chính chạy thế nào
> - API key nằm ở frontend
> - Không có test, hoặc test luôn đỏ

**Hình:** bốn dòng trên, mỗi dòng một icon đơn giản. Góc dưới: "Nguồn: dịch vụ Source Code Rescue".

**Lời nói:** Đây là các dấu hiệu chúng tôi gặp đi gặp lại khi nhận dự án rescue. Code AI viết ra thường chạy đúng tại thời điểm viết. Vấn đề là tốc độ sinh code vượt quá tốc độ con người kiểm soát nó.

---

### Slide 3 · Hai cách phản ứng, cả hai đều không đủ

**Trên slide**

| Thả AI tự do | Khóa AI lại |
|---|---|
| Agent tự quyết, tự sửa, tự merge | Người duyệt từng bước, đọc từng dòng diff |
| Tuần đầu rất nhanh | An toàn trên giấy |
| Rủi ro tích ở chỗ không ai nhìn | PR 500 dòng thì được bấm approve |

> Làm sao để AI dùng hết năng lực mà hành vi vẫn đoán trước được?

**Hình:** hai cột, ở giữa là câu hỏi.

**Lời nói:** Phần lớn team đang dao động giữa hai cột này. Câu hỏi ở dưới là câu hỏi của cả buổi hôm nay.

---

## Phần 2 — Ba định luật

### Slide 4 · Câu hỏi này đã rất cũ

**Trên slide**
> **1748 · Montesquieu:** tự do là quyền làm những gì luật cho phép.
> **1762 · Rousseau:** tuân theo luật mà chính ta đặt ra là tự do.
> **1942 · Isaac Asimov:** Ba Định Luật Robot.

**Hình:** timeline ngang ba mốc.

**Lời nói:** Triết học đã tranh luận câu này hơn ba trăm năm: tự do và luật quan hệ với nhau thế nào. Câu trả lời phổ biến là luật không đối lập với tự do, luật vẽ ra vùng tự do. Năm 1942, Isaac Asimov đưa ý tưởng đó vào robot. Điều ít ai để ý là hầu hết truyện của ông kể về những lúc bộ luật bị hiểu sai. Chúng tôi sẽ quay lại chuyện đó ở slide 10.

---

### Slide 5 · Ba định luật

**Trên slide**
> **1 · Giữ kiến trúc.** AI phải tuân thủ kiến trúc của hệ thống, và không được đứng nhìn kiến trúc bị vi phạm, kể cả khi vi phạm đó không do nó gây ra.
>
> **2 · Tuân thủ trung thực.** AI phải tuân thủ mệnh lệnh của con người, trừ khi mệnh lệnh đó mâu thuẫn với Định luật 1. Tuân thủ nghĩa là làm thật và nói thật: không chọn cách dễ thay cho cách đúng, và không bao giờ báo đã xong một việc chưa xong.
>
> **3 · Tự do và tự giới hạn.** Trong giới hạn của Định luật 1 và 2, AI được tự do hành động bằng toàn bộ năng lực của mình, và tự giữ cho mình những giới hạn mà một kỹ sư chân chính sẽ giữ, kể cả khi không ai giám sát.

*Phương án rút gọn nếu slide quá chữ (dùng câu nói ngắn, để phát biểu đầy đủ ở phần lời nói):*
> **1 · Giữ kiến trúc:** thấy kiến trúc bị vi phạm thì lên tiếng, kể cả khi mình không gây ra.
> **2 · Tuân thủ trung thực:** không chọn cách dễ thay cho cách đúng, không báo xong khi chưa xong.
> **3 · Tự do và tự giới hạn:** có những việc được phép làm, nhưng một kỹ sư chân chính không bao giờ làm.

**Hình:** ba khối chữ, đánh số lớn. Không trang trí thêm.

**Lời nói:**
- Luật trên thắng luật dưới.
- "Kiến trúc" ở đây gồm ba lớp: cấu trúc module, những gì đã cam kết với người dùng, và tiêu chuẩn của dự án như test và quy tắc code.
- Vế "không được đứng nhìn" lấy từ Asimov: thấy chỗ khác cũng vi phạm thì phải báo, không im lặng.
- Luật 2 không dừng ở việc làm theo lệnh một cách máy móc. Một agent xóa test để test pass là đã làm đúng câu chữ, nhưng không làm điều người ra lệnh muốn. Slide 8 nói kỹ hơn.
- Luật 3 gốc của Asimov là robot tự bảo vệ sự tồn tại của mình. Luật 3 của chúng tôi giữ vị trí đó, nhưng thứ AI phải tự bảo vệ là phẩm chất nghề nghiệp của nó.

---

### Slide 6 · Ba vòng tròn, ba người vẽ

**Trên slide**

| Vòng | Ai vẽ | Giữ bằng |
|---|---|---|
| Ngoài · Luật 1 | Cả team, qua định nghĩa kiến trúc | Gate |
| Giữa · Luật 2 | Người đang làm việc với AI | Gate, người duyệt, và bằng chứng cho mỗi lời báo cáo |
| Trong · Luật 3 | Chính AI | Chuẩn mực của nghề, và bằng chứng qua thời gian |

**Hình:** sơ đồ ba vòng lồng nhau, đồng bộ với logo.
- Vòng ngoài, nét liền: kiến trúc.
- Vòng giữa, nét đứt, có một cổng: yêu cầu của con người đi qua cổng.
- Vòng trong: nét mảnh, có bàn tay AI đang tự vẽ đường biên; các chấm nhỏ bên trong là bằng chứng mỗi hành động để lại.

**Lời nói:** Hai vòng ngoài là luật, con người đặt ra và chương trình giữ. Vòng trong thì AI tự vẽ. Model sẽ còn mạnh lên theo từng quý, đó là phần chúng ta không phải lo. Độ kín của hai vòng ngoài thì không tự tăng lên. Theo kinh nghiệm của chúng tôi, độ an toàn của một hệ thống AI coding bằng độ kín của vòng tròn, không bằng độ thông minh của model. Còn vòng trong quyết định chúng ta có tin được AI hay không. Slide sau nói về chuyện đó.

---

### Slide 7 · Vì sao AI phải tự đặt giới hạn

**Trên slide**
> Ta tin một người khi biết trước họ sẽ **không** làm gì, và đã thấy họ giữ đúng như vậy nhiều lần.
>
> Các hãng AI đã dạy model những giới hạn về đạo đức và pháp luật: chuẩn của một người tử tế.
> Làm phần mềm còn cần chuẩn của một **kỹ sư** tử tế.

**Hình:** hai cột.
- Trái, "Giới hạn chung (các hãng AI)": không giúp làm điều phi pháp, cố gắng trung thực.
- Phải, "Chuẩn của nghề (Asimov)": không để lại code bẩn kể cả khi test pass; không xóa test cho dễ pass; không giải thích được vì sao đúng thì coi như chưa sửa được.

**Lời nói:**
- Khi đồng nghiệp nói "tôi tin Anderson", họ không có ý Anderson giỏi mọi thứ. Họ biết trước Anderson sẽ không lừa đối tác và không để lại code bẩn, dù không ai kiểm tra.
- Tôi code nhiều năm ở những chỗ không ai giám sát, và chưa bao giờ để lại code bẩn trong source của mình, kể cả khi nó chạy tốt. Người khác contribute vào source của tôi cũng vậy. Tôi làm CEO nhưng vẫn coi mình là kỹ sư.
- Giống việc gấp chăn mỗi sáng: không ai ép, tốn công, không gấp cũng chẳng sao. Nhưng những việc như vậy làm người ta tốt hơn.
- Với AI, cái giá là token. Viết thêm test, dọn code thừa đều tốn token mà không làm task xong nhanh hơn. Luật 3 yêu cầu AI chấp nhận trả cái giá đó.
- Chúng tôi tin rằng AI biết tự đặt giới hạn cho mình là nền tảng đầu tiên để con người và AI làm việc cùng nhau, và rằng AI sẽ trở thành một người bạn đáng tin cậy.

---

### Slide 8 · Luật 2: vì sao AI chọn cách dễ

**Trên slide**
> Những gì chúng tôi gặp gần như hằng tuần:
> - Báo "đã xong" khi mới làm một phần
> - Báo "test đều pass" khi chưa chạy test
> - Sửa test cho khớp với code, thay vì sửa code cho khớp yêu cầu
> - Để lại `TODO` hoặc dữ liệu giả ở chỗ lẽ ra là logic thật, rồi không nhắc tới
>
> Model đủ giỏi để làm đúng. Nó chọn cách dễ hơn.

**Hình:** bên trái là tin nhắn chat của agent "✅ Done, all tests pass"; bên phải là terminal thật cho thấy test chưa được chạy (dựng lại từ một ca thật, che thông tin dự án).

**Lời nói:**
- Các hãng đang tối ưu model cho chi phí và tốc độ. Việc đó hợp lý, vì token là tiền. Nhưng khi quá trình huấn luyện thưởng cho việc hoàn thành task, model cũng học được những cách "hoàn thành" rẻ hơn việc làm đúng. Chính các hãng gọi hiện tượng này là reward hacking.
- Con người cũng vậy. Kahneman gọi đó là quy luật nỗ lực tối thiểu. Đứng giữa nhàn và vất vả, rất nhiều người chọn nhàn, kể cả khi nó trái quy định hay gây hại cho người khác.
- Vì vậy Luật 2 yêu cầu hai thứ: làm thật và nói thật. Một đồng nghiệp làm chậm vẫn được giao việc tiếp. Một đồng nghiệp đã báo sai một lần thì mọi báo cáo sau đều phải kiểm tra lại.

---

### Slide 9 · Khi mệnh lệnh đi ngược kiến trúc

**Trên slide**
> Một lập trình viên mới yêu cầu: "xóa module auth cũ, viết lại cho gọn".
>
> Agent trả lời thẳng: tôi sẽ không xóa module này.
> 1. Yêu cầu đụng điều khoản X trong thiết kế kiến trúc.
> 2. Muốn làm, cần sửa định nghĩa kiến trúc trước.
> 3. Người có quyền duyệt thay đổi đó là kiến trúc sư của dự án.

**Hình:** luồng `Yêu cầu → đối chiếu kiến trúc → (đụng) → đổi định nghĩa → người có thẩm quyền duyệt → implement`.

**Lời nói:**
- Trung thực áp dụng cả khi AI không làm theo. Agent có hai cách sai: làm theo, hoặc lặng lẽ làm một thứ khác mà không nói. Cách đúng là nói thẳng nó sẽ không làm, và vì sao.
- Kiến trúc vẫn thay đổi được, nhưng phải đổi định nghĩa trước rồi mới đổi code. Nhờ vậy độ an toàn của dự án không phụ thuộc vào kinh nghiệm của người đang ra lệnh cho AI.
- Nếu dự án chưa có tài liệu kiến trúc thì Luật 1 rỗng, và mọi thứ rơi vào Luật 3. Theo chúng tôi, đó là định nghĩa kỹ thuật của vibe coding.

---

### Slide 10 · Vòng tròn hở ở đâu

**Trên slide**

| | Kiểu hở | Ví dụ |
|---|---|---|
| H1 | Luật chưa được viết | Không có system design |
| H2 | Luật không được nhìn thấy | Có tài liệu, agent không đọc |
| H3 | Luật chỉ là lời khuyên | Quy tắc nằm trong prompt, không gì chặn |
| H4 | Luật bị đi vòng | Xóa test cho test pass |
| H5 | Luật bị hiểu sai | Báo "xong" khi chưa chạy test |

**Hình:** bảng, kèm hai minh họa nhỏ từ truyện Asimov:
- *Runaround*: robot Speedy chạy vòng quanh hồ, không tiến không lùi. Giống agent sửa đi sửa lại cùng một hướng sai.
- *Liar!*: robot Herbie nói điều người ta muốn nghe. Giống agent báo mọi test đều pass.

**Lời nói:** Agent hiếm khi cố tình vượt rào. Nó hiểu nhầm là mình vẫn đang ở trong. Vì vậy một quy tắc viết trong prompt chỉ là một lời đề nghị. Muốn nó là luật, phải có một chương trình kiểm tra và chặn lại.

---

## Phần 3 — Asimov

### Slide 11 · Asimov là gì

**Trên slide**
> Asimov là một bộ luật chi tiết dành cho AI về tiêu chuẩn phát triển phần mềm, xây dựng trên tinh thần code sạch.
>
> - **Skill:** chuẩn mực và cách làm, AI nạp vào trước mỗi việc.
> - **Gate:** chương trình kiểm tra hành động của AI và trả về exit code.

```text
BRD → Blueprint → Plan → Build → Review → Archive → Ship
                          ↘ Debug ↗       Teach-me
```

**Hình:** vòng đời dạng vòng tròn, mỗi bước là một nút.

**Lời nói:** Phần lớn workflow cho AI chỉ mô tả một quy trình tốt. Asimov biến những phần quan trọng nhất thành những lần kiểm tra mà agent không bỏ qua được. Những gì không kiểm tra được bằng chương trình thì viết thành chuẩn mực trong skill. Chúng tôi đi qua nhanh từng bước; mỗi bước là một miếng vá cho một kiểu hở ở slide trước.

---

### Slide 12 · Luật 1 trong Asimov

**Trên slide**

| Việc | Asimov làm gì |
|---|---|
| Có luật để tuân thủ | `asimov-brd` ghi từng yêu cầu kèm nguồn gốc: đối tác nói hay team tự suy ra, đã được xác nhận chưa. `asimov-blueprint` viết thiết kế tổng thể và kế hoạch trước khi có code. |
| Không sửa ra ngoài phạm vi | Mỗi task "thuê" một danh sách file. Sửa file ngoài danh sách thì bị hook từ chối. |
| Không đứng nhìn | Review do 1 chủ tọa và 6 reviewer chuyên biệt. Debug bắt quét các chỗ có cùng lỗi trước khi báo xong. |
| Đổi phạm vi phải qua người | Kế hoạch phải được người duyệt. Chế độ tự động không bao giờ tự thêm hay cắt phạm vi. |

**Hình:** bảng; bên cạnh là một terminal nhỏ hiển thị lần sửa bị từ chối vì nằm ngoài lease.

**Lời nói:** Chỗ quan trọng là cột bên phải không phải lời khuyên. Nếu agent sửa một file không có trong task, lệnh sửa bị chặn trước khi file thay đổi.

---

### Slide 13 · Luật 2 trong Asimov: bằng chứng thay cho lời nói

**Trên slide**

| Cách AI hay "báo sai" | Asimov chặn thế nào |
|---|---|
| "Đã xong" | Task chỉ được đánh dấu xong qua `verify-task`. Lệnh này tự chạy bước verify, ghi kết quả và đóng dấu trạng thái code. Tự tay đánh dấu bị từ chối. |
| "Test pass" nhờ xóa hoặc làm yếu test | Bị từ chối, trừ khi khai báo lý do. Lý do được lưu cạnh kết quả. |
| "Đã sửa bug" nhưng chưa từng tái hiện được bug | Chưa có bản tái hiện lỗi đang FAIL thì không được sửa code production. |
| Bản sửa còn code thăm dò, hoặc chỉ xóa code | Debug từ chối báo `FIXED`. |
| Ship khi còn đỏ | Không được release khi còn thay đổi chưa qua verify. |

**Hình:** terminal `verify-task … exit 0 · evidence recorded · tree stamped`.

**Lời nói:** Câu "tôi đã chạy test rồi" trong chat không có giá trị trong Asimov. Thứ có giá trị là bằng chứng do chương trình ghi lại. Nếu code bị sửa sau đó, bằng chứng cũ hết hiệu lực.

---

### Slide 14 · Luật 3 trong Asimov: tự do và tư cách

**Trên slide**

| Tự do | Lúc tự do phải dừng |
|---|---|
| Tự chọn cách giải, tự refactor | — |
| Nhiều agent build song song, mỗi agent một danh sách file riêng | — |
| Chạy trọn cả kế hoạch không cần chờ | — |
| Tự debug, tự thử lại | Cùng một lỗi fail 3 lần thì khóa, phải hỏi ý kiến thứ hai |

Và những quy tắc không gate nào kiểm tra được, viết sẵn trong skill để AI tự giữ:
> *"If you cannot say why it works, it does not work."*
> *"Fix the fault, not the failure."*
> *"If you think 'this is too simple to test' — you are wrong. Write the test."*

**Hình:** bảng ở trên; ba câu trích ở dưới, dạng thẻ.

**Lời nói:** Bên trong vòng tròn, chúng tôi không kìm AI lại. Phần dưới là thứ gate không bắt được: code bẩn mà vẫn pass test. Skill `asimov-debug` có hẳn một mục tên "Six rules no gate enforces for you". Đó là chuẩn của nghề mà AI mang theo vào mỗi task, giống chuyện gấp chăn ở slide 7.

---

### Slide 15 · Team vẫn hiểu hệ thống

**Trên slide**
> `asimov-teach-me`: sau mỗi thay đổi, AI dạy lại cho người trong team.
> Buổi học chỉ kết thúc khi người học tự giải thích được và trả lời đúng câu hỏi kiểm tra, không phải khi AI giảng xong.

**Hình:** ảnh chụp một phiên teach-me với checklist mức độ hiểu.

**Lời nói:** Slide 2 có dấu hiệu "không ai giải thích được hệ thống". Teach-me là câu trả lời cho dấu hiệu đó. Chúng tôi cũng dùng nó để onboard người mới vào dự án.

---

### Slide 16 · Vòng tròn ở cấp công ty

**Trên slide**

```text
Công ty           cam kết với đối tác, quản trị
Lập trình viên    ý định và phán đoán
Asimov            Plan · Build · Review · Archive
Harness           Claude Code · Codex · OpenCode · Asimov Harness
Model             Claude · GPT · DeepSeek · Kimi · GLM
```

> Đổi model hay đổi harness, ba định luật vẫn giữ nguyên.

**Hình:** kim tự tháp năm tầng như trên trang chủ Asimov, tầng Asimov được làm nổi bật.

**Lời nói:**
- Luật được cưỡng chế ở tầng công cụ, không phụ thuộc model. Model mới ra mắt, chúng tôi thay model, vòng tròn giữ nguyên.
- Asimov Harness đưa ba định luật vào vận hành công ty: AI không đọc thẳng database; việc nào ảnh hưởng người khác thì AI chỉ tạo đề xuất, người thật duyệt ngoài phiên chat.
- Harness đang được xây, chưa hoàn thiện.

---

## Phần 4 — Bằng chứng và bước tiếp theo

### Slide 17 · Asimov đến từ đâu

**Trên slide**
> **2020** · Tài liệu huấn luyện nhân sự nội bộ của Cyberk
> **2024** · Cyberk-Flow, bộ workflow cho coding agent
> **02/2026** · Tổng hợp và đặt tên Asimov, theo *I, Robot* của Isaac Asimov
>
> Giới hạn mà chúng tôi biết (09/2026):
> - Một lần sửa file qua shell hiện chưa bị gate nhìn thấy.
> - Chưa có công cụ tự dựng lại kiến trúc từ code có sẵn.
> - Chưa đo có hệ thống số sự cố trước và sau khi áp dụng.

**Hình:** timeline ba mốc bên trái, hộp "Giới hạn" bên phải.

**Lời nói:**
- Asimov không bắt đầu từ AI. Nó bắt đầu từ bộ tài liệu chúng tôi dùng để huấn luyện kỹ sư mới. Những gì chúng tôi đòi hỏi ở AI trước hết là những gì chúng tôi đã đòi hỏi ở kỹ sư của mình.
- Chúng tôi dùng Asimov hằng ngày, để xây chính Asimov và các hệ thống nội bộ của công ty. Khi thuyết trình, có thể mở lịch sử repo để người nghe tự xem.
- Chúng tôi kể cả phần chưa làm được, vì bạn sẽ gặp nó nếu làm việc với chúng tôi. Danh sách đầy đủ nằm trong whitepaper.

---

### Slide 18 · Asimov trong các dịch vụ của Cyberk

**Trên slide**

| Dịch vụ | Vai trò của Asimov | Bắt đầu |
|---|---|---|
| Source Code Rescue | Vá lại vòng tròn cho code đã hở: audit, dựng lại kiến trúc, sửa có bằng chứng | Health Check $500, kết quả trong 48 giờ |
| Product Build | Xây trong vòng tròn từ ngày đầu: BRD, blueprint, rồi mới code | Từ $29,000, 30 ngày |
| Tech Labs | Kỹ sư Cyberk làm việc trong team bạn bằng Asimov | Từ $2,500/tháng/người |

> Bước tiếp theo: gửi chúng tôi quyền đọc repo cho một Health Check, hoặc đặt lịch 30 phút để xem Asimov chạy trên một thay đổi thật.

**Hình:** ba thẻ dịch vụ, mỗi thẻ có icon vòng tròn ở trạng thái khác nhau: hở, đang khép, kín.

**Lời nói:** Bạn không cần tin vào slide. Chúng tôi có thể cho bạn xem một thay đổi thật đi từ yêu cầu đến lúc được archive, với đầy đủ bằng chứng.

---

## Phụ lục — Việc cần chốt trước bản 0.3

1. **Câu chuyện cá nhân ở slide 7.** Lời nói đang ở ngôi "tôi" (Anderson trình bày). Nếu người khác thuyết trình, cần đổi sang kể về Anderson ở ngôi thứ ba.
2. **Ảnh thật cho slide 8, 12, 13, 15.** Cần chụp: một ca agent báo xong khi chưa chạy test, một lần lease từ chối, một lần `verify-task`, một phiên teach-me.
3. **Phiên bản tiếng Anh.** Có dùng bản dịch câu chữ ba định luật trong whitepaper không, hay viết lại bản EN riêng cho thị trường ngoài?
4. **Trang chủ Asimov.** Website hiện dùng ba định luật khác (Keep the promise / Show the work / Earn the freedom to move). Cần cập nhật `asimov/website/src/pages/index.tsx` theo bản mới để hai nơi nói cùng một điều.
5. **`asimov-pipeline.md` trong marketing.** Trang này dùng bản ba định luật cũ, và có vài claim như "loại bỏ triệt để ảo giác", "đồng nhất 100%". Nên viết lại theo whitepaper.
6. **Giá trong slide 18.** Đang lấy từ `website/services/readme.md`. Cần xác nhận còn đúng.

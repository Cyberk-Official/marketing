---
type: doc
name: writing-rules
description: "Luật viết mọi nội dung marketing Cyberk — website, tài liệu, social, kịch bản. Chống giọng AI (AI slop)."
tags: [marketing, voice, writing, quality-control, cyberk]
created: 2026-09-22
audience: Người viết + AI
---

# Luật Viết Content Cyberk

> Dùng cho **cả người và AI**. Khi nhờ AI viết bất cứ nội dung marketing nào, dán file này vào trước.
>
> Áp dụng cho: website, tài liệu, social, email, kịch bản video, proposal.

---

# 1. Một câu luật gốc

Luật này đã có trong `skills/script-maker/SKILL.md` từ 07/2026. Nó đúng cho mọi loại nội dung, không chỉ video:

> # Nói như đang pair programming, không phải đang lên sân khấu.

Người ngồi cạnh bạn lúc pair programming: bạn nói thẳng, gọn, chỉ vào màn hình, thừa nhận chỗ chưa biết. Không ai lên giọng, không ai ra khẩu hiệu.

**Vì sao trước giờ nội dung website bị giọng AI:** luật trên chỉ được áp cho kịch bản video. Website, proposal, tài liệu không có luật nào — nên nó tự trôi về giọng mặc định của máy.

---

# 2. Khán giả không tha cho giọng "nổ"

`docs/audience_profile.md` ghi rõ kẻ thù bên trong của khán giả Cyberk:

> *"Không biết đánh giá tech: không phân biệt được dev team đang làm tốt hay đang **'nổ'**."*

Và họ nói thẳng họ muốn gì:

> *"Cho tôi xem case study thực tế — đừng nói lý thuyết."*

Người đọc của Cyberk đã bị nhiều agency "nổ" vào mặt rồi. Mỗi tính từ tự khen làm họ nghi thêm một chút.

---

# 3. Ba đăng ký giọng

Cùng một tinh thần, khác độ thân mật.

| Nơi dùng | Nhân xưng | Emoji | Ví dụ |
|---|---|---|---|
| **Inbox / Telegram** | "tôi", "mình" | Được | *"Vâng nó khá đơn giản, tôi chỉ cần dùng vài thư viện để trích xuất frame mỗi giây."* |
| **Kịch bản video** | **luôn "tôi"** | Không | *"Cái này sẽ bị race condition, cần xử lý ở tầng database."* |
| **Website / tài liệu** | "chúng tôi" | Không | *"Chúng tôi đưa sản phẩm cho bạn dùng mỗi sáng."* |

Điểm chung của cả ba: **cụ thể, gọn, dám nói cái chưa làm được.**

---

# 4. Chín dấu hiệu giọng AI

Mỗi dấu hiệu kèm một cặp sai/đúng. Các ví dụ ✅ đều lấy từ file thật trong repo.

### 4.1 Câu cụt làm điểm nhấn

| | |
|---|---|
| ❌ | *"Not a demo. A product that runs."* · *"Fixed price. Fixed timeline."* |
| ✅ | *"Cuối mỗi vòng bạn có một phần sản phẩm chạy được — không phải bản cập nhật tiến độ, không phải file Figma."* |

Câu cụt dùng để tạo kịch tính. Kỹ sư không nói kịch tính.

### 4.2 Cấu trúc lật ngược

| | |
|---|---|
| ❌ | *"We don't just use AI. We control it."* · *"Không chỉ là code, mà là kiến trúc."* |
| ✅ | *"Mỗi thay đổi đi qua bốn vòng review tự động trước khi tới tay người."* |

Cấu trúc "không chỉ A, mà B" luôn là dấu hiệu người viết chưa có gì cụ thể để nói.

### 4.3 Bộ ba

| | |
|---|---|
| ❌ | *"designed, built and shipped"* · *"reason, decide, and act"* · *"nhanh, gọn, hiệu quả"* |
| ✅ | *"Thiết kế xong thì code. Code xong thì bạn dùng thử."* |

Ba thứ liệt kê ra cho có nhịp. Chọn một thứ và nói rõ nó.

### 4.4 Tính từ thay cho sự việc

| | |
|---|---|
| ❌ | *"production-grade"*, *"battle-tested"*, *"world-class"*, *"seamless"*, *"chuyên nghiệp"*, *"tối ưu"* |
| ✅ | *"Chạy được từ 0 tới 100.000 người dùng mà không phải sửa kiến trúc."* |

**Quy tắc:** mỗi tính từ khen mình phải đổi được thành một con số, một cái ảnh, hoặc một hành vi. Không đổi được thì xoá.

### 4.5 Câu tuyên ngôn mở đầu

| | |
|---|---|
| ❌ | *"Anyone can generate an app in an afternoon. The hard part is what happens next."* |
| ✅ | *"Với những công cụ như Cursor hay Lovable, một ý tưởng có thể biến thành ứng dụng chạy mượt trên máy bạn chỉ sau vài giờ."* — `articles/cyberk/01-is-vibe-coding.../article-vn.md` |

Mở bài bằng **bối cảnh cụ thể có tên công cụ thật**, không bằng một câu triết lý.

### 4.6 Danh từ hoá hành động

| | |
|---|---|
| ❌ | *"delivery excellence"*, *"quy trình tối ưu hoá chất lượng"*, *"cam kết minh bạch"* |
| ✅ | *"Mỗi sáng developer gửi báo cáo: hôm qua làm gì, hôm nay làm gì, mỗi việc bao lâu."* — `services/zero-to-product.md` |

Nếu một cụm danh từ mô tả một việc, hãy kể việc đó ra.

### 4.7 Nhịp đều

Mọi câu dài xấp xỉ nhau → giọng máy. Người viết thật có câu 5 chữ nằm cạnh câu 40 chữ.

Đoạn mở bài trong article của Anderson: câu 1 dài 24 chữ, câu 2 dài 31 chữ, câu 3 dài 9 chữ. Không cố ý — tự nhiên như vậy.

### 4.8 Châm ngôn in đậm ở mọi đoạn

Một châm ngôn cho cả bài thì mạnh. Mỗi đoạn một châm ngôn thì thành áp phích.

> Cả bài `article-vn.md` dài 900 từ chỉ có **một** câu chốt: *"chúng ta đã tự tay buông bỏ quyền kiểm soát source code."*

### 4.9 Không bao giờ thừa nhận giới hạn

Đây là dấu hiệu dễ nhận nhất và cũng nguy hiểm nhất.

| | |
|---|---|
| ❌ | Cả bài chỉ nói mình mạnh |
| ✅ | *"Quality won't match the flagship models, but I'm genuinely excited to give it a try."* — `anderson/message-example/ai-video-fiona.md` |
| ✅ | *"Vấn đề không nằm ở chất lượng code do AI sinh ra. AI viết code nhanh, tối ưu và hầu hết đều chạy đúng yêu cầu ở thời điểm đó."* — article-vn.md, nhượng bộ đối phương trước khi phản biện |

Một bài không có chỗ nào thừa nhận cái khó, cái chưa làm được, hay điểm mạnh của đối phương — là một bài quảng cáo. Người đọc biết ngay.

---

### 4.10 Đầu đoạn in đậm kiểu mini-header

| | |
|---|---|
| ❌ | ***Hai luật cân bằng nhau.** Một robot nhận một mệnh lệnh...* |
| ❌ | ***Vì sao phải trao tự do.** Giá trị của AI nằm ở đây.* |
| ✅ | *Khi hai luật kéo về hai phía với lực ngang nhau, robot đi vòng quanh mục tiêu: không hoàn thành việc, cũng không bỏ cuộc.* |

Dùng bold fragment mở đầu đoạn như mini-header để tạo nhịp giả. Kỹ sư không viết như vậy — họ để câu đứng bằng nội dung của nó, không bằng font chữ.

**Nhận ra nhanh:** quét qua bài, thấy nhiều đoạn liên tiếp bắt đầu bằng `**Từ ngữ.**` → đang xài pattern này.

---

### 4.11 Ca đã bắt được

Ghi lại ca thật theo §11. Mỗi dòng là một câu đã bị sửa, không phải ví dụ giả định.

| Ngày | ❌ Câu gốc | ✅ Đã sửa thành | Dấu hiệu | File |
|---|---|---|---|---|
| 2026-09-22 | *"Not a status report. The thing itself, running."* | *"What you get is the thing itself, running on your phone, not a note saying we are nearly done."* | 4.1 | `homepage-new-content.md` |
| 2026-09-22 | *"We don't just use AI. We control it."* | Bỏ hẳn khỏi trang chủ. Thay bằng ảnh màn hình Asimov đang chạy | 4.2 | `homepage.md` (bản nháp) |
| 2026-09-22 | *"Không phải 'công ty AI'. Không phải 'công ty blockchain'. Không phải 'đối tác toàn cầu'. Một xưởng nghề."* | *"Cyberk là một xưởng nghề."* | 4.2 + 4.3 | `homepage-new-content.md` |
| 2026-09-22 | *"Production-grade products for founders — designed, built and shipped in 30 days."* | *"Chạy được từ 0 tới 100.000 người dùng mà không phải sửa kiến trúc."* | 4.3 + 4.4 | `homepage.md` (bản nháp) |
| 2026-09-22 | *"Trang cũ cần một người dàn trang. Trang mới cần một người chọn và trưng đồ."* | *"Phần lớn công sức chuyển từ việc sắp chữ sang việc chọn ảnh và xử lý ảnh."* | 4.8 | `home-page-changes.md` |
| 2026-09-30 | ***Hai luật cân bằng nhau.** Một robot nhận một mệnh lệnh được đưa ra hờ hững...* | *Khi hai luật kéo về hai phía với lực ngang nhau, robot đi vòng quanh mục tiêu: không hoàn thành việc, cũng không bỏ cuộc.* | 4.10 | `asimov-laws-whitepaper.md` |

> Cả năm ca đầu đều do AI viết ra trong cùng một tuần. Đây là lý do luật này tồn tại.

---

# 5. Cặp đối chiếu chuẩn — cùng một chủ đề, hai giọng

Cả hai đoạn dưới đây nằm trong **cùng một file**: `anderson/message-example/telegram-aol.md`. Một do AI sinh, một do Anderson viết.

### ❌ Bản AI sinh

> *"Mobile application development is a core competency of our team. We specialize in engineering high-performance, secure, and user-centric mobile applications. By leveraging robust cross-platform frameworks, we deliver seamless experiences for both iOS and Android ensuring rapid deployment without compromising on native-level performance or aesthetics."*

46 từ. Không một danh từ cụ thể nào. Không thể kiểm chứng một chữ.

### ✅ Bản Anderson viết

> *"Vâng, phát triển Mobile App cũng là một trong những thế mạnh cốt lõi của bên mình luôn! Team mình chuyên và rất quen thuộc với cả React Native lẫn Flutter nhé. Gửi bạn xem thử vài project bên mình từng làm nha: Oracler Wallet App — [link]"*

Trả lời ngay. Gọi tên công cụ thật. **Rồi đưa link cho người ta tự xem.**

> Đây chính là bí quyết 3 của handbook — *"Trăm nghe không bằng một thấy. Báo cáo bằng hiện vật."*

---

# 6. Sáu bài kiểm tra trước khi publish

Làm lần lượt. Mỗi bài mất dưới một phút.

| # | Bài kiểm tra | Cách làm | Hỏng thì sao |
|---|---|---|---|
| 1 | **Đọc to** | Đọc thành tiếng cả bài | Nghe như đang thuyết trình trên sân khấu → viết lại |
| 2 | **Hiện vật** | Mỗi tuyên bố: quy về được một con số đo được, một ảnh, hay một hành vi? | Không quy được → xoá câu đó |
| 3 | **Thay bằng ảnh** | Câu này có thay được bằng một hình không? | Thay được → thay đi |
| 4 | **Gạch tính từ** | Gạch hết tính từ khen mình. Bài còn đứng được không? | Sụp → bài đang rỗng |
| 5 | **Đếm câu cụt** | Đếm câu dưới 6 chữ | Quá 1 câu trong một đoạn → đang giật cục |
| 6 | **Thừa nhận** | Cả bài có chỗ nào nói cái khó / cái chưa làm được? | Không có → thêm vào, nếu không sẽ bị đọc là quảng cáo |

---

# 7. Từ và cụm cấm

### Cấm vì rỗng

`world-class` · `production-grade` · `battle-tested` · `cutting-edge` · `seamless` · `robust` · `leverage` · `empower` · `unlock` · `elevate` · `game-changing` · `next-level` · `đỉnh cao` · `vượt trội` · `tối ưu` (khi không kèm số) · `chuyên nghiệp` · `toàn diện`

### Cấm vì cấu trúc

`không chỉ... mà còn` · `không phải là X, mà là Y` · `We don't just... we...` · bộ ba liệt kê

### Cấm vì kịch tính hoá (luật sẵn có trong script-maker)

`sụp đổ` · `nguy hiểm nhất` · `thảm hoạ` · `mất uy tín ngay từ ngày đầu`
→ Thay bằng ngôn ngữ kỹ thuật bình thản: *"sẽ bị race condition"*, *"gây ra double booking"*.

### Cấm vì đã có luật riêng

| Cấm | Thay bằng | Nguồn luật |
|---|---|---|
| **"khách hàng"** | "dự án", "đối tác", "bài toán thực tế" | `script-maker/SKILL.md` |
| **"chúng tôi"** trong kịch bản video | **"tôi"** | `script-maker/SKILL.md` |
| Tên thật đối tác | "một startup logistics", "nhà phân phối sỉ FMCG tại Singapore" | `review/review.md` L1.1 |
| Giá hợp đồng, quy mô team, timeline cụ thể | "giai đoạn đầu", "quy mô vừa và nhỏ" | `script-maker/SKILL.md` |
| Tên sản phẩm đối thủ kèm lời chê | Không nhắc tên, hoặc nói về hạn chế kỹ thuật trung tính | — |

---

# 8. Con số

Luật đã có trong `review/review.md`:

> *"Mọi con số được sử dụng ($75/tháng, 1.5s OCR) phải có dữ liệu đo lường thực tế từ dự án chứng minh."*

Thêm hai luật:

- **Một con số chỉ có một phiên bản.** Hiện `/marketing` đang có 4 phiên bản số dự án (dozens / 30+ / 40+ / 50+) và 3 mốc năm (5 / 6+ / 12). Trước khi viết, tra lại `positioning.md` để lấy số chuẩn.
- **Số cụ thể mạnh hơn số tròn.** *"1.5 giây"* đáng tin hơn *"dưới 2 giây"*. *"$75/tháng"* đáng tin hơn *"chi phí thấp"*.

---

# 9. Ba mẫu mở bài

Không mở bài bằng khẩu hiệu. Có ba cách mở đã dùng và hiệu quả:

**Mở bằng bối cảnh có tên công cụ thật**
> *"Với những công cụ như Cursor hay Lovable, một ý tưởng có thể biến thành ứng dụng chạy mượt trên máy bạn chỉ sau vài giờ."*

**Mở bằng một câu hỏi làm trục cho cả bài**
> *"Ba tháng sau, khi bạn cần thay đổi một luồng logic cốt lõi, ai trong team thực sự hiểu hệ thống này đang vận hành như thế nào?"*

**Mở bằng một cảnh có thật, có thời gian và con số**
> *"Giao thừa Tết Âm lịch năm 2020, sau khi trả hết lương thưởng cho mọi người, tài khoản công ty chỉ còn lại chưa đến hai triệu đồng."* — `social/stories/cau-thi.md`

---

# 10. Mẫu giọng chuẩn để tham chiếu

Khi bí, mở một trong bốn file này ra đọc lại:

| File | Dùng cho |
|---|---|
| `website/about-us.md` | Giọng website — bình tĩnh, câu thường |
| `articles/cyberk/01-is-vibe-coding.../article-vn.md` | Giọng bài dài — lập luận, nhượng bộ, số thật |
| `anderson/message-example/*.md` | Giọng trả lời đối tác — thẳng, gọn, đưa link |
| `social/stories/cau-thi.md` | Giọng kể chuyện — cảnh thật, không tô vẽ |

---

---

# 11. Cách luật này được nhớ và được cải tiến

## Nguyên tắc: một luật, một chỗ, nhiều điểm nạp

**Không copy luật này sang file khác.** Luật được copy sẽ trôi — đúng như `Cyberk Framework` và `Asimov` hiện đang là hai tên cho cùng một thứ ở 8 chỗ khác nhau.

File này là nguồn duy nhất. Các nơi khác chỉ **trỏ tới**, không chép lại.

## Ba điểm nạp

| Nơi | Nạp khi nào | Trạng thái |
|---|---|---|
| `AGENTS.md` (gốc repo) | Mọi AI agent, mọi lúc | ⬜ cần thêm một mục |
| `skills/script-maker/SKILL.md` | Mỗi phase viết kịch bản | ✅ đã trỏ |
| Frontmatter mỗi file content | Lúc review trước publish | ⬜ quy ước dưới |

## Quy ước `voice-check` trong frontmatter

Mọi file content mới thêm một trường:

```yaml
---
type: mkt
status: draft
voice-check: pending
---
```

Chạy xong 6 bài kiểm tra ở §6 thì đổi thành:

```yaml
status: ready
voice-check: passed 2026-09-22
```

> **Luật:** không file nào được đổi `status` sang `published` khi `voice-check` còn `pending`.

Rẻ, không cần công cụ, và grep một phát là ra file nào chưa kiểm:
`grep -rn "voice-check: pending" marketing/`

## Vòng lặp cải tiến

Luật này **dày lên từ ca thật**, không từ lý thuyết.

```
Bắt được một câu giọng AI
        ↓
Thêm thẳng một cặp ❌/✅ vào §4 của chính file này
        ↓
Ghi ngày + nguồn (file nào, ai viết)
        ↓
Lần sau AI đọc file này sẽ thấy ca đó
```

**Không tạo file log riêng.** Một file, dày dần. File log thứ hai sẽ bị bỏ quên trong hai tuần.

Ba tháng một lần, đọc lại §4: cặp nào không còn ai mắc nữa thì xoá, giữ file gọn.

## Thứ tự sửa nội dung đang có

Đừng viết lại tất cả. Sửa theo thứ tự người lạ chạm vào:

| Ưu tiên | File | Lý do |
|---|---|---|
| 1 | `website/homepage-new-content.md`, `home-page-changes.md` | Chưa publish — sửa trước khi lên là rẻ nhất |
| 2 | `website/services/*.md` | Người đọc ngay trước khi quyết định mua |
| 3 | `website/capabilities/*.md` | Người lạ vào từ Google |
| 4 | `social/*` | Chỉ áp cho bài đăng mới. Bài cũ để yên |

---

# Một câu để nhớ

> Cyberk không thuyết phục bằng cách nói mình giỏi.
> Cyberk mở tủ đồ ra.

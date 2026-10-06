---
type: mkt
tags: [review, audit, positioning, consistency]
status: draft
created: 2026-09-20
scope: toàn bộ marketing/
---

# Content Review — marketing/ (2026-09)

> Rà soát toàn bộ nội dung marketing sau khi chốt định vị AI-first.
> Mỗi phát hiện đều có trích dẫn file + dòng để đối chiếu.

**Kết luận ngắn:** nội dung *viết* tốt, nhưng *không nhất quán với nhau*. Vấn đề lớn nhất không phải chất lượng câu chữ — mà là cùng một sự thật đang được kể bằng nhiều phiên bản khác nhau. Khách hàng đọc hai trang liền nhau sẽ thấy mâu thuẫn.

---

## 🔴 Nghiêm trọng — sửa trước khi publish bất cứ thứ gì

### 1. Bốn con số khác nhau cho cùng một thành tích

| Con số | Xuất hiện ở |
|---|---|
| "dozens of projects" | `services/product-build.md:18,99` · `services/product-design.md:19` |
| **30+** projects/startups | `services/zero-to-product.md:25,78,162` |
| **40+** projects | `capabilities/blockchain-development.md:32,47,184,241` · `capabilities/smart-contract-development.md:22,51` |
| **50+** solutions | cyberk.io (live) |

Số năm cũng vậy: **5 năm** (`blockchain-development.md:32`), **6+ năm** (live site), **12 năm** (`skills/docs/audience_profile.md:12`).

> Đây là thứ giết uy tín nhanh nhất. Một khách hàng cẩn thận mở hai tab là thấy.
> **Việc cần làm:** chốt **một** bộ số chuẩn, ghi vào `positioning.md`, rồi find & replace toàn bộ. Nếu 40+ là blockchain và 50+ là tổng, phải nói rõ *"50+ sản phẩm, trong đó 40+ on-chain"* — đừng để hai số trôi nổi không nhãn.

### 2. Hai tên thương hiệu cho cùng một tài sản

| Tên | Số lần | File |
|---|---|---|
| **Cyberk Framework** | 8 | `product-build.md` · `tech-labs.md` · `product-design.md` · `blockchain-development.md` |
| **Asimov** (Architect / Pipeline / AI / toolset) | 15+ | `zero-to-product.md` · `asimov-pipeline.md` |

Chia đúng theo tuổi tài liệu: file cũ (03–04/2026) gọi "Cyberk Framework", file mới (09/2026) gọi "Asimov". Tức là việc đổi tên đã xảy ra nhưng chưa ai dọn.

> **Việc cần làm:** chốt **Asimov** là tên duy nhất, và chốt luôn cấu trúc con:
> - **Asimov Architect** = hạ tầng (serverless, 0→100k)
> - **Asimov Pipeline** = quy trình sản xuất (spec-driven, 4 cửa review)
> - **Asimov** = tên gọi chung
>
> Bỏ hẳn "Cyberk Framework". Một tài sản không được có hai tên.

### 3. `product-build.md` và `tech-labs.md` vẫn là tài liệu Web3 thuần

Những dòng này mâu thuẫn trực diện với định vị AI-first:

- `product-build.md:21` — *"**Web3 expertise.** Cyberk specializes in blockchain development — DeFi, RWA tokenization, NFT platforms... **This is our home turf.**"*
- `product-build.md` FAQ — *"The Basic package is designed for standard **Web3 MVPs** (10–20 screens, **2–5 smart contracts**)"* → định nghĩa gói sản phẩm bằng số smart contract
- `tech-labs.md:19` — *"brings **Web3 expertise by default**"*
- `tech-labs.md` — role *"**Web3** UX Designer"*
- `product-design.md:12` — *"years of experience shipping **Web3** products"*

AI xuất hiện đúng **một lần**, chôn trong tech stack: `product-build.md:107` — *"AI/Agent: LangChain, custom agent frameworks"*.

> **Việc cần làm:** viết lại phần "Why" của cả hai file. Web3 giữ lại nhưng chuyển từ *bản sắc* sang *một năng lực trong danh sách*. Định nghĩa gói Basic bằng phạm vi sản phẩm, không bằng số smart contract.

### 4. Giá biến mất khi khách bấm "Learn more"

`services/readme.md` có bảng giá đầy đủ ($29,000 / $35,000 / $4,000 / $2,500 / $3,500). Nhưng:

- `product-build.md` — **không có một con số giá nào**
- `tech-labs.md` — **không có một con số giá nào**

Khách đọc readme thấy giá → bấm vào trang chi tiết → giá biến mất. Đây là lỗi conversion cơ bản.

> **Việc cần làm:** đưa bảng giá vào chính trang dịch vụ. `zero-to-product.md` đã làm đúng — lấy làm mẫu.

### 5. Xung đột giá giữa Zero to Product và Tech Labs

Cùng một thứ — thuê thêm một developer — ba mức giá:

| Nguồn | Giá |
|---|---|
| `zero-to-product.md` — "+ Extra Developer" | **+$3,000/mo** |
| `readme.md` / `tech-labs.md` — Middle Developer | **$2,500/mo** |
| `readme.md` / `tech-labs.md` — Senior Developer | **$4,000/mo** |

Khách so sánh hai trang sẽ hỏi ngay: "extra developer $3,000 là senior hay middle?"

> **Việc cần làm:** hoặc gán rõ level cho add-on của Z2P, hoặc thống nhất một bảng giá nhân sự dùng chung cho cả hai dịch vụ.

### 6. `social/facebook-post/telegram-report-checker.md` — rủi ro thương hiệu

Ba vấn đề trong một file:

1. **Xúc phạm sản phẩm đối thủ có tên thật** — *"tôi chỉ cần thêm **deepshit-helper**... tôi sẽ gọi nó là deepshit vì reasoning của nó quá tệ"*. DeepSeek là sản phẩm có thật. Đây là thứ bị screenshot.
2. **Ngôn ngữ không phù hợp thương hiệu** — *"mớ shitty code"*, *"khứa claude nấu cho tôi món gì đó nên hồn"*, *"nồi lẩu thập cẩm giữa try-catch và một mớ code rác"*.
3. **Mâu thuẫn văn hoá** — *"Hệ thống cần biến một ngày làm việc tuyệt vời của họ thành một ngày làm việc tồi tệ, như các manager tồi tệ khác."* Handbook `2.3` viết Cyberk là nơi *"quan hệ anh chị em"*, `4.2` nói về *trao quyền và tự chịu trách nhiệm*. Câu đùa này đi ngược cả hai.

Thêm một tầng nữa: bài này **tự nhận là vibe-coding** (*"tôi muốn thử một cách vibe-code, không bmad, không các phương pháp"*) — trong khi `asimov-pipeline.md:19` lên án chính xác phương pháp đó là *"tiềm ẩn rủi ro về độ ổn định"*.

> **Việc cần làm:** không đăng bản này. Nếu muốn giữ nội dung (nó thật sự hay về mặt kỹ thuật), viết lại: bỏ tên đối thủ, bỏ chửi thề, đổi framing từ "vibe code cho vui" sang "vì sao tôi kiểm soát low-level design ngay cả khi dùng AI" — khi đó nó thành bài ủng hộ Asimov thay vì phản bác.

---

## 🟡 Cần sửa

### 7. Hai bài social phản bác chính định vị mới

`dung-ai-sao-cho-dung.md` và `hoc-truoc-code-sau.md` lập luận rằng AI gây *"Xói Mòn Nền Tảng"*, *"Nợ Hiểu Biết"*, *"Ảo Tưởng về Năng Suất"*.

**Nội dung đúng. Khung sai.** Hiện tại đọc ra là *"AI là cái bẫy"*. Chỉ cần đổi một tầng: *"**AI không kiểm soát** là cái bẫy — và đây là cách chúng tôi kiểm soát nó"* → lập tức trở thành lời biện hộ mạnh nhất cho Asimov Pipeline. Cùng nội dung, ngược tác dụng.

### 8. Thống kê không nguồn

`product-design.md:17` — *"**80% of product failures** happen because of bad design decisions, not bad code."*

Không có nguồn. Với audience là CTO/founder, một con số bịa bị bắt bài sẽ làm hỏng toàn trang.

> Hoặc dẫn nguồn cụ thể, hoặc bỏ số và viết bằng lập luận.

### 9. Ai là người tư vấn?

| File | Nói gì |
|---|---|
| `readme.md` | *"direct advisory from our **CEO**"* |
| `product-design.md:12,19` | *"Our **Technical Advisor** personally advises"* |
| `product-build.md` | *"**CTO** product advisory"* |
| `zero-to-product.md` | *"your **Product Lead** — he acts as your CTO"* |

Bốn tên gọi cho vai trò tư vấn. Khách không biết mình đang mua thời gian của ai.

### 10. Audience đang mâu thuẫn với chính persona

- `content-pillar.md` — audience là *"Global Founders, CTOs và B2B Tech Leaders"*
- `skills/docs/audience_profile.md:6` — anti-persona ghi rõ: *"**lập trình viên (không phải đối tượng trực tiếp)**"*
- Nhưng toàn bộ `social/facebook-post/` là tiếng Việt, nội dung kỹ thuật, nhắm thẳng developer Việt Nam

Tức là kênh social đang phục vụ đúng nhóm mà persona tuyên bố không nhắm.

> Không sai — nhưng phải **khai báo có hai audience** (employer branding VN + client acquisition global) và tách kênh, tách pillar. Hiện chưa file nào nói điều này.

### 11. File đặt nhầm chỗ

- `website/services/Decks_Digital_—_Platform_UI_UX_&_Quality_Improvement_Project_Proposal.md` — đây là proposal cho một khách hàng cụ thể, không phải nội dung website. Nên chuyển sang `works/proposal/`.
- `website/services/asimov-pipeline.md` — là phương pháp luận, không phải dịch vụ bán. Chuyển sang trang `/how-we-build`.
- `marketing/services/` — **thư mục rỗng**, trùng tên với `marketing/website/services/`. Xoá hoặc dùng.

### 12. README.md mô tả sai cấu trúc

`README.md:16` ghi `research/self-media/` nhưng thư mục thật tên **`new-media/`**. README cũng không nhắc tới `ideas/`, `skills/`, `workflow/`, `social/stories/`.

---

## 🟢 Tài sản đang bị bỏ phí

### 13. `social/stories/cau-thi.md` — mạnh nhất trong cả folder

> *"Giao thừa Tết Âm lịch năm 2020, sau khi trả hết lương thưởng cho mọi người, tài khoản công ty chỉ còn lại chưa đến hai triệu đồng... **AI và Blockchain là hai cánh cửa mở ra lúc đó.**"*

Câu này làm được ba việc cùng lúc:

1. Chứng minh giá trị **Cầu** bằng một chuyện có thật, có mất mát — không phải lời tự khen
2. Chứng minh **AI không phải trend mới đu** — nó đã ở đó từ 2020, ngang hàng Blockchain ngay từ đầu
3. Vô hiệu hoá câu hỏi *"hype AI hết thì các anh có còn không?"*

Đang nằm chết trong `social/stories/`. Nên đưa lên `/about-us` và dùng làm gốc cho tuyến content về founder.

### 14. `capabilities/smart-contract-development.md` đã tự giải xong bài toán

> *"**Smart contracts for the agent economy.** AI agents that pay, trust, and hire each other — through smart contracts we write."*
> `x402 → agents PAY · ERC-8004 → agents TRUST · ERC-8183 → agents WORK`

Đây là **cây cầu Web3 → AI hoàn hảo**: không bỏ Web3, không chối AI, mà biến 5 năm smart contract thành lợi thế trong nền kinh tế agent. Không đối thủ AI thuần nào nói được câu này.

> Lấy file này làm **template** để viết lại `blockchain-development.md` — file đó hiện vẫn là *"5 years. 40+ projects. every major chain"*, thuần hoài niệm Web3, không có một chữ AI.

### 15. Clutch 4.8/5 và GoodFirms 5/5 không xuất hiện ở đâu trong `/marketing`

Đánh giá bên thứ ba là bằng chứng mạnh nhất cho giá trị **Tín**, và nó đang có sẵn trên live site nhưng không file marketing nào dùng tới.

### 16. `zero-to-product.md` là tài liệu tốt nhất — nên làm chuẩn

Nó có đủ thứ các file khác thiếu: tên Asimov nhất quán, bảng giá rõ, nhịp ngày/tuần/tháng cụ thể, mermaid diagram, và mô hình **Evidence → Register → Output** cho change management. Mục *"What Zero to Product Is Not"* cũng là kỹ thuật định vị tốt.

> Dùng nó làm khuôn cho việc viết lại `product-build.md` và `tech-labs.md`.

---

## Thứ tự làm

| # | Việc | File | Ưu tiên |
|---|---|---|---|
| 1 | Chốt bộ số chuẩn + find/replace | toàn bộ | 🔴 |
| 2 | Chốt tên Asimov, bỏ "Cyberk Framework" | 8 chỗ | 🔴 |
| 3 | Gỡ `telegram-report-checker.md` khỏi hàng đợi đăng | social | 🔴 |
| 4 | Đưa giá vào `product-build.md` + `tech-labs.md` | services | 🔴 |
| 5 | Gỡ xung đột giá Z2P ↔ Tech Labs | services | 🔴 |
| 6 | Tạo `positioning.md` làm nguồn chân lý | mới | 🔴 |
| 7 | Viết lại "Why" của product-build + tech-labs | services | 🟡 |
| 8 | Thống nhất tên vai trò tư vấn | 4 file | 🟡 |
| 9 | Reframe 2 bài AI social | social | 🟡 |
| 10 | Viết lại `blockchain-development.md` theo mẫu smart-contract | capabilities | 🟡 |
| 11 | Bỏ/dẫn nguồn số 80% | product-design | 🟡 |
| 12 | Dọn file đặt nhầm chỗ + sửa README | cấu trúc | 🟢 |
| 13 | Đưa `cau-thi.md` vào about-us | website | 🟢 |
| 14 | Viết 4 case study (đang chặn trang chủ) | mới | 🟢 |

---

## Đã xử lý trong lần review này

- `services/ai-powered-studio.md` + `ai-powered-studio-en.md` (04/2026) → chuyển vào `services/archived/`, được thay thế bởi `zero-to-product.md` (09/2026).

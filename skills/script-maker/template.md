---
type: template
skill: script-maker
output-file: scripts/[STT]_[slug].md
methodology: cyberk-video-strategy-paast-vcl.md
---

<!--
  ╔══════════════════════════════════════════════════════════════════╗
  ║  HƯỚNG DẪN SỬ DỤNG TEMPLATE                                   ║
  ║                                                                ║
  ║  1. Điền metadata ở phần Header                                ║
  ║  2. Chọn thời lượng clip → tra bảng Pacing ở mục 1             ║
  ║  3. Viết Script Brief ở mục 2                                  ║
  ║  4. Dựng kịch bản 2 cột ở mục 3 (phân bổ theo % PAAST)        ║
  ║  5. Tự kiểm tra Pre-Publish Checklist ở mục 4                  ║
  ║  6. Ghi chú Asset cần chuẩn bị ở mục 5                         ║
  ║                                                                ║
  ║  📖 PHƯƠNG PHÁP LUẬN BẮT BUỘC THAM KHẢO:                      ║
  ║  → cyberk-video-strategy-paast-vcl.md                          ║
  ║    (Phễu PAAST + Khung VCL + Scorecard + Ba tính chất cốt lõi) ║
  ║                                                                ║
  ║  📋 GUIDELINE VIẾT KỊCH BẢN:                                   ║
  ║  → script-make.md                                              ║
  ║    (Phễu PAAST timeline + Bảng quy đổi từ/phút + Checklist)   ║
  ╚══════════════════════════════════════════════════════════════════╝
-->

# KỊCH BẢN: [Tên Video / Slug]

| Metadata | Giá trị |
|----------|---------|
| **Ý tưởng gốc** | #[STT] — [Tên ý tưởng] từ `brainstorm/ideas.md` |
| **Tầng PAAST chủ đạo** | [Prefer / Acknowledge / Trust / Stick / Action] |
| **Thời lượng mục tiêu** | [90 / 120 / 150 / 180 / 240 / 270] giây |
| **Tổng từ lời thoại** | [Điền sau khi viết xong — tra bảng Pacing bên dưới] |
| **Ngày tạo** | [YYYY-MM-DD] |
| **Audience** | The Ambitious Builder — Founders / CEOs / C-level / Solopreneur |
| **Series (nếu có)** | [Tên series — ví dụ: "Nhật ký thiết kế hệ thống AI"] |
| **Phương pháp luận** | `cyberk-video-strategy-paast-vcl.md` |

---

## 📖 Tham Chiếu Phương Pháp Luận

> **Mọi kịch bản Cyberk đều PHẢI tuân thủ `cyberk-video-strategy-paast-vcl.md`:**
>
> 1. **Ba Tính Chất Cốt Lõi** — Video phải hội đủ: *Giải Trí (Entertainment)* + *Giáo Dục (Educational)* + *Xác Thực (Authentic)*.
> 2. **Phễu PAAST** — Hành trình tâm lý: Prefer → Acknowledge → Trust → Stick → Action.
> 3. **Khung VCL** — Tiêu chuẩn thực thi: Visual (Cursor IDE, sơ đồ vẽ tay, font RobotoMono) + Content (1 Video = 1 Vấn đề = 1 Giải pháp) + Logic (tần suất đăng, UTM tracking, tái cấu trúc asset).
> 4. **Pre-Publish Scorecard** — Chấm điểm ≥ 12/40 mới được xuất bản.

---

## 1. ⏱️ Bảng Pacing & Thời Lượng

> **Tốc độ đọc chuẩn:** **120 từ/phút** (tiếng Việt, đĩnh đạc, rõ ràng, sâu sắc).  
> Chỉ tính **lời thoại (spoken words)** — không tính text overlay, tên kỹ thuật, hoặc cảnh im lặng.

| Thời lượng clip | Số từ tối thiểu | Số từ tối đa | PAAST Timeline & Phân Bổ Chi Tiết |
|----------------|----------------|-------------|-----------------------------------|
| **300s** (5 phút) | ~570 từ | ~600 từ | Hook 0-24s (~45t) · Ack (FR+NFR) 24-75s (~100t) · Trust 75-240s (~330t) · Stick (Show thành quả) 240-270s (~65t) · CTA 270-300s (~30t) |
| **360s** (6 phút) | ~680 từ | ~720 từ | Hook 0-28s (~55t) · Ack (FR+NFR) 28-90s (~125t) · Trust 90-288s (~395t) · Stick (Show thành quả) 288-324s (~75t) · CTA 324-360s (~35t) |
| **420s** (7 phút) | ~790 từ | ~840 từ | Hook 0-33s (~65t) · Ack (FR+NFR) 33-105s (~145t) · Trust 105-336s (~460t) · Stick (Show thành quả) 336-378s (~85t) · CTA 378-420s (~45t) |

**Thời lượng đã chọn:** `____s` → **Word budget:** `____` từ (Tính theo 120 từ/phút)

---

## 2. 📋 Script Brief (Tóm Tắt Kịch Bản)

> Phần này giúp đội sản xuất nắm được tinh thần kịch bản trong 30 giây đọc.

| Mục | Nội dung |
|-----|---------|
| **Hook chính (Scene 1)** | [Mô tả Visual Hook: cận cảnh dashboard billing / terminal báo lỗi / sơ đồ kiến trúc tổng quan...] |
| **Yêu cầu dự án (FR)** | [Yêu cầu bài toán / tính năng mong muốn từ phía dự án — ngắn gọn, đơn giản, dễ hiểu] |
| **Phân tích đề bài (NFR)** | [Điểm mấu chốt kỹ thuật: realtime latency, zero hallucination, multi-tenancy, scale...] |
| **Giải pháp kiến trúc (Trust)** | [Thiết kế server, Neon DB per SaaS instance, pipeline STT/LLM/TTS, caching strategy...] |
| **Thành quả & Kết luận (Stick)** | [Minh chứng hệ thống thực tế hoạt động + Bài học kiến trúc cốt lõi rút ra] |
| **CTA (Action)** | *"Nếu bạn muốn nghe nhiều hơn về thiết kế hệ thống AI thì hãy comment, like và share nhé!"* |

---

## 3. 🎬 Bảng Kịch Bản Quay Dựng 2 Cột (Production Script)

### Scene 1: P — PREFER · Hook (0% → ~8% · ~15–30s)

> **📌 Hướng dẫn:** Đọc kỹ `analysis/00-client-needs.md` và `input/` để xác định đúng bài toán cốt lõi của dự án. Từ đó đặt tiêu đề Hook phù hợp — phải là con số hoặc tình huống thực tế gây tò mò ngay 3 giây đầu. Tham khảo thêm `cyberk-research/` để tìm góc nhìn bất ngờ.

**📝 Phân tích:**
> *Kết quả đọc hiểu tài liệu và quyết định triển khai:*
> - **Bài toán cốt lõi:** [Tóm tắt 1 câu bài toán chính]
> - **Góc Hook được chọn:** [Con số / tình huống dùng làm Hook? Lý do chọn?]
> - **Tài liệu tham chiếu:** [Liệt kê file đã đọc]

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:00 – 00:__** | [Mô tả cụ thể cảnh quay mở đầu.] | *"[Câu mở bằng con số hoặc tình huống thực tế gây tò mò...]"* | · Font: RobotoMono<br>· Sound: [ambient/nhạc nền] |

> **✅ Checkpoint Hook:** Khán giả có dừng lướt trong 3-5s đầu không?

---

### Scene 2: A — ACKNOWLEDGE · Vấn Đề & Phân Tích Đề Bài (~8% → ~25% · ~50–80s)

> **📌 Hướng dẫn:** Đọc kỹ `analysis/00-client-needs.md` để trích xuất FR ngắn gọn. Đọc `cyberk-research/`, `analysis/01-scope-of-work.md`, `analysis/02-assumptions-and-constraints.md`, và `technical/system-architecture.md` để phân tích NFR.

**📝 Phân tích:**
> *Kết quả đọc hiểu tài liệu và quyết định triển khai:*
> - **Bối cảnh dự án:** [Startup / Enterprise...]
> - **FR chính:** [2-3 feature]
> - **NFR mấu chốt:** [Latency / Scale / Cost...]

#### 2A. Yêu Cầu Bài Toán (Functional Requirements — Ngắn gọn & Đơn giản)

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Chuyển cảnh: Màn hình giao diện / Bảng vẽ sơ đồ yêu cầu bài toán / Chat ẩn danh] | *"Đọc kỹ yêu cầu bài toán, các tính năng mà dự án đặt ra rất rõ ràng: [Mô tả ngắn gọn 2-3 feature chính. Ví dụ: Hệ thống AI tự động nghe điện thoại, hỗ trợ tiếng Anh và Tây Ban Nha, tốc độ phản hồi phải dưới 1 giây...]. Và một điều quan trọng cần lưu ý: [Phân tích ngắn gọn bối cảnh dự án. Ví dụ: Đây là một startup đang ở giai đoạn đầu, sản phẩm chưa có người dùng thực tế. Hoặc: Đây là một dự án chuyển đổi số cho doanh nghiệp truyền thống, lượng người dùng ban đầu chưa xác định rõ — thông tin này rất quan trọng vì nó sẽ quyết định cách tôi thiết kế toàn bộ kiến trúc phía sau...]"* | · Visual: Sơ đồ vẽ tay<br>· Text overlay: Bullet points FR<br>· ⚠️ Nhấn mạnh bối cảnh startup/chuyển đổi số |

#### 2B. Phân Tích Đề Bài (Chiến Lược Thiết Kế & Non-Functional Requirements)

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show sơ đồ chiến lược thiết kế: 2 trục — Chi phí vận hành vs Khả năng Scale] | *"Vì đây là một startup ở giai đoạn đầu, chiến lược thiết kế của chúng tôi ưu tiên hàng đầu là: Tiết kiệm tối đa chi phí vận hành và hạ tầng khi chưa có người dùng — nhưng vẫn phải đảm bảo khả năng scale. Lý do rất đơn giản: Startup giai đoạn đầu gần như chưa có người dùng thực tế, nếu lúc đó mà phải trả hàng trăm đô mỗi tháng cho server và database thì rất lãng phí. Nhưng ngược lại, khi startup thành công và người dùng tăng đột biến, hệ thống phải tự động đáp ứng được mà không cần can thiệp thủ công — chỉ cần trả thêm tiền theo lượng sử dụng là xong. Như vậy vừa tiết kiệm khi chưa có người dùng, mà vẫn sẵn sàng phục vụ khi người dùng thực sự đến..."* | · Visual: Sơ đồ 2 trục chiến lược<br>· Text overlay: "$0 idle → Auto-scale"<br>· Transition: Smooth cut |
| **00:__ – 00:__** | [Show kết quả Research & Analytics / Sơ đồ phân tích thách thức ngầm] | *"Từ chiến lược đó, chúng tôi đặt ra các yêu cầu phi chức năng (Non-functional Requirements) cụ thể cho dự án: [Phân tích điểm mấu chốt. Ví dụ: Toàn bộ hạ tầng phải là Serverless — không chạy thì không tốn tiền. Hệ thống bắt buộc phải phản hồi Realtime dưới 1 giây. AI không bao giờ được phép trả lời sai hoặc hallucinate thông tin. Và khi scale lên vài trăm nghìn người dùng, không cần thay đổi kiến trúc — chỉ cần trả thêm tiền...]"* | · Visual: Highlight NFRs<br>· Text overlay: Bullet points NFR |

---

### Scene 3: T — TRUST · Giải Pháp Kỹ Thuật, Cost Estimate & Architecture Demo (~25% → ~80% · ~165–230s)

> **📌 Hướng dẫn:** Đọc kỹ `technical/system-architecture.md`, `analysis/03-cost-and-time-estimations.md`, và `cyberk-research/` (đặc biệt: `cyberk-research-tech-stack.md`, `cyberk-research-voice-infrastructure.md`, `cyberk-research-unit-economics.md`). Phân tích để đưa ra giải pháp kỹ thuật chi tiết cho từng vấn đề NFR đã nêu ở Scene 2B. Mỗi luận điểm phải bám sát vào kiến trúc thực tế, có con số cost estimate cụ thể nhưng balanced (không nói một phía).

> **⚡ Chiếm 55% thời lượng.** Bám sát chi tiết thiết kế hệ thống (Architecture design), giải pháp hạ tầng và bài toán tối ưu chi phí (Cost Estimate).

**📝 Phân tích:**

> *Kết quả đọc hiểu tài liệu và quyết định triển khai:*
>
> - **Kiến trúc tổng quan:** [Tóm tắt architecture. Ví dụ: "Serverless Event-driven + Neon DB Multi-tenant + OpenRouter LLM + Deepgram STT + ElevenLabs TTS"]
> - **Luận điểm kỹ thuật chọn trình bày (2-4 luận điểm):** [Liệt kê + lý do chọn. Ví dụ: "1) Zero Idle Cost Architecture 2) Neon DB auto-suspend 3) OpenRouter Pay-per-call 4) Latency Pipeline"]
> - **Cost estimate tham chiếu:** [Lấy từ `analysis/03-cost-and-time-estimations.md`. Ghi rõ nguồn con số]
> - **Tài liệu tham chiếu:** [`technical/system-architecture.md`, `analysis/03-cost-and-time-estimations.md`, `cyberk-research/cyberk-research-tech-stack.md`]

**Luận điểm 1: Kiến trúc Server & Tối ưu Chi Phí Nhàn Rỗi (Zero Idle Cost Architecture)**

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show sơ đồ kiến trúc Serverless / Edge Function trên Cursor IDE hoặc Excalidraw · Code config route API] | *"Về mặt kiến trúc server, thay vì thuê một server riêng chạy 24/7, tôi chọn mô hình Serverless Event-driven. Khi chưa có cuộc gọi nào, server không chạy — chi phí duy trì gần như bằng 0. Nhưng khi dự án bắt đầu có hàng nghìn cuộc gọi mỗi ngày, kiến trúc này vẫn tự động scale mà không cần cấu hình lại bất kỳ thứ gì. Chi phí lúc đó sẽ tăng tuyến tính theo lượng request thực tế — hoàn toàn dự đoán được và kiểm soát được..."* | · Visual: Architecture Diagram<br>· Code: `api/webhook/route.ts`<br>· Tech: Serverless Edge |

**Luận điểm 2: Cơ chế Database Multi-Tenant & Neon DB (Auto-suspend)**

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show Neon DB Console dashboard · Branching database diagram · Connection pool config] | *"Về phần dữ liệu, tôi chọn Neon DB — một dịch vụ Serverless Postgres. Điểm quan trọng nhất là: trong giai đoạn startup chưa có người dùng, Neon DB tự động ngủ (auto-suspend) — chi phí duy trì bằng 0 đồng. Bạn không phải trả tiền cho một database đang chờ không. Nhưng khi dự án bắt đầu scale lên vài chục nghìn hay vài trăm nghìn người dùng, Neon DB vẫn xử lý tốt nhờ Connection Pooling và khả năng auto-scale compute. Chi phí lúc đó sẽ tăng theo lượng dữ liệu và số kết nối thực tế — nhưng bạn chỉ trả cho những gì mình thực sự dùng, không trả trước cho capacity chưa cần..."* | · Visual: Neon DB Console<br>· Key: auto-suspend = $0 idle<br>· Tech: Serverless Postgres |

**Luận điểm 3: Linh Hoạt LLM & Chi Phí Thực Tế Qua OpenRouter (Pay-per-call)**

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show OpenRouter Dashboard · Routing logic chọn model theo latency & cost · Code API client] | *"Với phần trí tuệ AI, thay vì tự host model tốn GPU đắt đỏ cả ngàn đô mỗi tháng, tôi tích hợp qua OpenRouter theo mô hình Pay-as-you-go. Khi chưa có cuộc gọi, chi phí AI bằng 0 — không có người dùng thì không mất tiền. Khi volume tăng lên hàng nghìn cuộc gọi mỗi ngày, chi phí sẽ tăng theo số lượng token xử lý. Điều quan trọng là chi phí này tăng tuyến tính và hoàn toàn dự đoán được — bạn luôn biết trước mình sẽ trả bao nhiêu dựa trên volume thực tế, không bao giờ bị bất ngờ bởi hóa đơn cuối tháng..."* | · Visual: OpenRouter API Logs<br>· Key: $0 idle, linear scaling<br>· Tech: OpenRouter LLM Router |

**Luận điểm 4: Tối Ưu Latency < 1s & Anti-Hallucination Guardrails**

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show Voice Pipeline STT -> OpenRouter -> TTS streaming trên Terminal / Chrome DevTools Performance tab] | *"Để đạt tốc độ phản hồi dưới 1 giây, luồng audio được stream từng chunk nhỏ qua Deepgram STT, đẩy qua OpenRouter chọn model có time-to-first-token ngắn nhất. Để đảm bảo AI không trả lời sai, pipeline được bọc thêm lớp RAG kiểm chứng kiến thức doanh nghiệp trước khi phát giọng nói. Đây là trade-off: thêm lớp Guardrails sẽ tốn thêm vài chục mili-giây xử lý, nhưng đổi lại là độ chính xác mà bạn hoàn toàn kiểm soát được — và trong bài toán Telemarketing, trả lời đúng quan trọng hơn trả lời nhanh..."* | · Visual: Streaming Pipeline Trace<br>· Tech: Deepgram + OpenRouter + ElevenLabs/Cartesia |

---

### Scene 4: S — STICK · Show Thành Quả & Kết Luận Kiến Trúc (~80% → ~90% · ~30–45s)

> **📌 Hướng dẫn:** Tổng hợp kết quả từ Scene 3, đưa ra kết luận về bản thiết kế. Đọc lại `analysis/03-cost-and-time-estimations.md` để lấy metric thực tế. Kết luận phải balanced: nói rõ lợi ích khi chưa có user VÀ khả năng scale khi tăng trưởng. Không cam kết con số tuyệt đối.

**📝 Phân tích:**

> *Kết quả đọc hiểu tài liệu và quyết định triển khai:*
>
> - **Metric thành quả sẽ show:** [Ví dụ: "Latency 650ms / Zero downtime / $0 idle cost / Auto-scale tested"]
> - **Kết luận kiến trúc cốt lõi:** [1 câu. Ví dụ: "Serverless-first = không trả trước cho capacity chưa cần"]
> - **Visual demo:** [Mô tả demo thực tế sẽ quay. Ví dụ: "Cuộc gọi AI nghe mượt < 1s + Billing dashboard $0"]

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Show Demo cuộc gọi AI nghe mượt dưới 1s · Sơ đồ chi phí theo giai đoạn: $0 idle → scale tuyến tính] | *"Đây là bản thiết kế từ lý thuyết ra thực tế. Kết luận quan trọng nhất là: Trong giai đoạn startup chưa có người dùng, toàn bộ hệ thống này gần như không mất phí duy trì — Server không chạy thì không tốn tiền, Database tự ngủ thì không tính tiền, AI không có cuộc gọi thì không phát sinh chi phí. Nhưng khi dự án bắt đầu tăng trưởng lên vài trăm nghìn người dùng, kiến trúc này vẫn đảm bảo scale mượt mà mà chi phí chỉ tăng tuyến tính theo lượng sử dụng thực tế. Bạn không bao giờ phải trả trước cho capacity chưa cần — và đó là triết lý thiết kế cốt lõi..."* | · Demo clip cuộc gọi<br>· Sơ đồ chi phí $0 → scale<br>· Key Takeaway Overlay |

---

### Scene 5: A — ACTION · CTA Nhanh (~90% → 100% · ~15–20s)

> **📌 Hướng dẫn:** CTA ngắn gọn, tự nhiên, không ép buộc. Khuyến khích comment/like/share để tăng tương tác. Không cần đọc thêm tài liệu cho phần này.

**📝 Phân tích:**

> *Quyết định triển khai:*
>
> - **Loại CTA:** [Engagement CTA — comment + like + share / Lead CTA — liên hệ trực tiếp]
> - **Câu CTA chọn:** [Ghi câu CTA cuối cùng]

| Thời gian | Visual & Kỹ Thuật (VCL) | Audio & Lời Thoại (PAAST) | Ghi Chú & Asset |
|-----------|--------------------------|----------------------------|-----------------|
| **00:__ – 00:__** | [Kỹ sư nhìn thẳng camera · Pop-up Like/Share/Comment icon & Subtitles] | *"Nếu bạn muốn nghe nhiều hơn về thiết kế hệ thống AI, hãy comment, like và share nhé!"* | · Text overlay: Comment & Sub<br>· End screen branding |

> **⚠️ Lưu ý:** Giữ CTA tự nhiên, ngắn gọn, súc tích trong 10-15s cuối. Tuyệt đối **tránh CTA thô/bán hàng trực diện** và **KHÔNG nhắc tên thương hiệu** (ví dụ: *"Nếu bạn đang tìm giải pháp... hãy liên hệ CyberK"*). LUÔN đóng vai một người bạn đồng hành công nghệ kêu gọi trao đổi, tạo thảo luận mở (ví dụ: *"Nếu bạn quan tâm tới thiết kế hệ thống, hoặc đang làm startup công nghệ, hãy để lại comment để chúng mình cùng thảo luận nhé."*).

---

## 4. ✅ Pre-Publish Checklist

> Tự chấm điểm 1–5 cho mỗi tiêu chí. **Yêu cầu tổng ≥ 12/40 điểm** mới được phép xuất bản.
> *(Tham chiếu Scorecard chi tiết: `cyberk-video-strategy-paast-vcl.md` → Mục 4)*

| # | Tiêu chí | Câu hỏi kiểm tra | Điểm (1–5) |
|---|----------|-------------------|-----------|
| 1 | **Bảo mật & Ẩn danh** | Tên đối tác / dự án đã ẩn danh? File `.env` / API key / token không xuất hiện trong bất kỳ cảnh quay nào? | |
| 2 | **Hook 3s đầu** | Hình ảnh / câu nói đầu tiên có đủ sức giữ chân Founder dừng lướt? Có con số thực tế gây bất ngờ? | |
| 3 | **Tính Giải Trí (Entertainment)** | Có yếu tố bất ngờ / tò mò thực tế — không phải giật tít rẻ tiền? | |
| 4 | **Tính Giáo Dục (Educational)** | Khán giả học được ≥ 1 điều thực tế áp dụng ngay? Giải pháp có ví von dễ hiểu? | |
| 5 | **Tính Xác Thực (Authentic)** | Câu chuyện, code, con số có thật từ dự án thực? Không dàn dựng demo giả? | |
| 6 | **Show, Don't Tell** | Cột Visual có thao tác thực tế (code/demo/sơ đồ) — hay chỉ nói suông? | |
| 7 | **Anti-Clickbait** | Không có từ giật gân ("sập", "bay màu", "ác mộng")? Mọi con số đều có bằng chứng thực? | |
| 8 | **CTA Định Vị** | Có cụm lặp *"Là một nhà khởi nghiệp..."* ở phần Action? CTA rõ ràng, dễ thực hiện? | |
| 9 | **Chuẩn VCL** | Font RobotoMono, âm thanh rõ ràng, nhịp cắt snappy, không cảnh thừa? | |
| 10 | **Pacing** | Tổng số từ lời thoại khớp với thời lượng clip (chuẩn 120 từ/phút)? | |
| | **TỔNG ĐIỂM** | **Yêu cầu ≥ 12 điểm** | **/50** |

---

## 5. 📦 Asset Checklist (Chuẩn Bị Cho Đội Quay Dựng)

> Liệt kê toàn bộ tài nguyên cần chuẩn bị trước khi bấm máy.

### Visual Assets
- [ ] Screen record: [Tên file / màn hình cần quay — Cursor IDE, Terminal, Dashboard...]
- [ ] Sơ đồ kiến trúc: [Vẽ tay / Mermaid / Draw.io — ghi rõ nội dung]
- [ ] Text overlay: [Danh sách text sẽ hiển thị trên màn hình — con số, keyword highlight]
- [ ] QR Code / Bio link: [URL đích]
- [ ] Logo / Watermark: Cyberk logo góc trên phải

### Audio Assets
- [ ] Nhạc nền: [Tên track / Loại nhạc — lo-fi, ambient, electronic]
- [ ] Sound effect: [Mô tả — typing sound, notification beep...]
- [ ] Giọng đọc: [Ai đọc / Tone: bình thản, rõ ràng, không vội]

### Mock Data & Bảo Mật
- [ ] Dữ liệu demo đã dùng mock data / sandbox? (không dùng data thật của đối tác)
- [ ] Mọi tên đối tác / dự án đã ẩn danh?
- [ ] File `.env` / API key đã được ẩn khỏi mọi cảnh quay?

---

## 6. 📝 Ghi Chú Kịch Bản

> Ghi lại các quyết định sản xuất đặc biệt, vấn đề cần xử lý khi quay, hoặc tài nguyên cần chuẩn bị thêm.
> Các quyết định quan trọng của AI sẽ được cộng dồn vào `spec-ai.html`.

---

## 📊 Word Count Summary

| Phần | Số từ lời thoại |
|------|----------------|
| Scene 1 — Hook | __ từ |
| Scene 2 — Acknowledge | __ từ |
| Scene 3 — Trust (tổng) | __ từ |
| Scene 4 — Stick | __ từ |
| Scene 5 — Action | __ từ |
| **TỔNG** | **__ từ** |
| **Budget cho phép** | **__ – __ từ** |
| **Trạng thái** | `[✅ Khớp / ⚠️ Thiếu / 🔴 Vượt]` |

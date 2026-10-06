# Copyright Workflow: Content Production Line ✍️

> "Content is King, but Consistency is Queen."

Quy trình này hướng dẫn chi tiết các bước để sản xuất một bài viết hoàn chỉnh, từ ý tưởng thô sơ đến thành phẩm chất lượng cao, đảm bảo đúng giọng văn của Persona.

## Phases Overview

1. [**Phase 1: Initialization**](#phase-1-initialization) - Chuẩn bị không gian làm việc.
2. [**Phase 2: Strategic Template Selection**](#phase-2-strategic-template-selection) - Chọn "khuôn" phù hợp cho thông điệp.
3. [**Phase 3: Raw Material Input**](#phase-3-raw-material-input) - Cung cấp nguyên liệu đầu vào.
4. [**Phase 4: Drafting & Refinement**](#phase-4-drafting--refinement) - Viết và tinh chỉnh.
5. [**Phase 5: Quality Control**](#phase-5-quality-control) - Kiểm soát chất lượng nghiêm ngặt.
6. [**Phase 6: Publishing**](#phase-6-publishing) - Xuất bản.

---

### Phase 1: Initialization

**Mục tiêu:** Thiết lập môi trường viết bài.

**Tham chiếu:** `workflows/commons/project-init-workflow.md`

**Các bước thực hiện:**

1. **Xác định Dự án:** Bạn đang viết cho ai? (Ví dụ: `project/jon`).
2. **Load Memory:** Đọc file `memory.md` của dự án đó để nắm bối cảnh và những quyết định gần đây.
3. **Đặt tên file:** Tạo file nháp với quy ước `YYYY-MM-DD-[topic-slug].md` trong thư mục dự án (hoặc thư mục drafts).

---

### Phase 2: Strategic Template Selection

**Mục tiêu:** Chọn cấu trúc bài viết tối ưu nhất cho mục đích truyền tải.

**Danh sách Template (`workflows/docs/templates/`):**

| Template | Mục đích sử dụng (Use Case) | Đối tượng |
| :--- | :--- | :--- |
| **`strategic_insight.md`** | Khi muốn thay đổi tư duy, đập tan một quan điểm sai lầm (Myth-busting), chia sẻ bài học xương máu. | Founder, Investor |
| **`comparative_analysis.md`** | Khi muốn so sánh 2 lựa chọn khó khăn (A vs B) để giúp ra quyết định. | CTO, Architect |
| **`architectural_deep_dive.md`** | Khi muốn giải thích cấu trúc hệ thống phức tạp một cách tổng quan (Big Picture). | Technical Leaders |
| **`procedural_guide.md`** | Khi muốn hướng dẫn lộ trình thực thi, các bước quản lý dự án. | PM, Tech Lead |

**Hành động:**

- Chọn 1 template phù hợp nhất.
- Copy cấu trúc của template đó vào file nháp.

---

### Phase 3: Raw Material Input

**Mục tiêu:** Thu thập đủ dữ liệu để AI có thể viết bài sâu sắc.

**Yêu cầu Input (từ người dùng):**

1. **Topic (Chủ đề):** Muốn nói về cái gì?
2. **Key Message (Thông điệp cốt lõi):** 1 câu duy nhất muốn người đọc nhớ sau khi đọc xong.
3. **Specific Context (Bối cảnh cụ thể):** Tại sao lại viết bài này NGAY LÚC NÀY? (Có sự kiện gì hot? Có nỗi đau gì vừa gặp phải?).
4. **Bullet Points (Ý chính):** 3-5 gạch đầu dòng về nội dung cần triển khai.
5. **Data/Evidence:** Số liệu hoặc ví dụ cụ thể để chứng minh.

---

### Phase 4: Drafting & Refinement

**Mục tiêu:** Biến nguyên liệu thô thành bài viết hoàn chỉnh.

**Hành động của AI:**

1. **Inject Persona:** Đọc `author_profile.md` và `audience_profile.md`. "Nhập vai" tác giả (Tone, Voice) và hình dung người đọc (Pain, Gain).
2. **Drafting:** Viết nội dung dựa trên Template đã chọn + Input + Persona.
3. **Refinement:**
    - Kiểm tra độ trôi chảy (Flow).
    - Kiểm tra các thuật ngữ chuyên ngành (giữ nguyên tiếng Anh).
    - Đảm bảo tính "Socratic" (gợi mở tư duy thay vì giáo điều).

---

### Phase 5: Quality Control (QC)

**Mục tiêu:** Đảm bảo bài viết đạt chuẩn trước khi xuất xưởng.

**Tham chiếu:** `.cursor/consistency-rules.mdc`

**Checklist kiểm tra:**

- [ ] **Tone Check:** Có đúng giọng văn của Persona không? (Ví dụ: Jon có "Pragmatic" không hay đang bị "Salesy"?).
- [ ] **Format Check:** Các tiêu đề, bold, list có đúng chuẩn Markdown không?
- [ ] **Term Check:** Các từ khóa kỹ thuật (Blockchain, RWA, Liquidity) có được sử dụng chính xác không?
- [ ] **Value Check:** Bài viết có mang lại giá trị thực sự (Insight) hay chỉ là sáo rỗng (Fluff)?

---

### Phase 6: Publishing

**Mục tiêu:** Hoàn thiện và lưu trữ.

**Tham chiếu:** `workflows/commons/publishing-workflow.md`

**Các bước thực hiện:**

1. **Final Polish:** Sửa các lỗi chính tả, ngữ pháp cuối cùng.
2. **Update Memory:** Ghi chú lại topic này vào `project/[name]/memory.md` để tránh lặp lại hoặc để mở rộng trong tương lai.
3. **Export:** Xuất ra định dạng cần thiết (PDF/Docx) hoặc copy để đăng lên Social Media.

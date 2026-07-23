---
type: skill
name: review
description: "Rà soát, kiểm duyệt kịch bản 3 lớp: Bảo mật & Pháp lý, Giá trị cốt lõi Cyberk (Entertainment + Educational + Authentic), và Tiêu chuẩn cộng đồng đa nền tảng."
tags: [marketing, review, quality-control, compliance, cyberk]
created: 2026-07-22
---

# SKILL: Review & Kiểm Duyệt Kịch Bản Cyberk

Skill này hướng dẫn quy trình **kiểm duyệt 3 lớp** đối với mọi kịch bản video ngắn trước khi chuyển sang giai đoạn sản xuất (quay dựng). Mục tiêu là đảm bảo 100% video không vi phạm pháp lý, bảo mật, chính sách nền tảng và giữ trọn giá trị cốt lõi của Cyberk.

---

## 🛡️ Quy Trình Kiểm Duyệt 3 Lớp (3-Layer Compliance Filter)

```text
Kịch Bản Chi Tiết (scripts/*.md)
           │
           ▼
┌───────────────────────────────────────────┐
│ LỚP 1: Bảo Mật, An Toàn & Pháp Lý        │
└─────────────────────┬─────────────────────┘
                      │ Pass
                      ▼
┌───────────────────────────────────────────┐
│ LỚP 2: Giá Trị Cốt Lõi Cyberk             │
│ (Entertainment + Educational + Authentic) │
└─────────────────────┬─────────────────────┘
                      │ Pass
                      ▼
┌───────────────────────────────────────────┐
│ LỚP 3: Tiêu Chuẩn Cộng Đồng Nền Tảng     │
│ (TikTok, YouTube, Facebook, LinkedIn)     │
└─────────────────────┬─────────────────────┘
                      │ Pass
                      ▼
            ✅ APPROVED FOR PRODUCTION
```

---

## 🔒 LỚP 1: Kiểm Tra Bảo Mật, An Toàn & Pháp Lý

* **1.1. Ẩn Danh Khách Hàng:**
  * Tuyệt đối không để lộ tên công ty, cá nhân, hoặc thương hiệu thật của khách hàng (trừ khi có văn bản đồng ý bằng miệng/chữ ký).
  * Danh xưng chuẩn: *"một doanh nghiệp B2B Singapore"*, *"đối tác phân phối sỉ"*, *"startup logistics"*.
* **1.2. Bảo Mật Mã Nguồn & Dữ Liệu:**
  * Mọi cảnh quay Cursor IDE/Terminal không được chứa: API Key, Password, Connection String, Token, File `.env`, thông tin cá nhân (PII) của khách hàng.
  * Nếu demo code thật, phải sử dụng mock data hoặc môi trường sandbox đã làm sạch.
* **1.3. Trung Thực Về Cam Kết:**
  * Không đưa ra các cam kết sai sự thật hoặc phóng đại kết quả (ví dụ: *"giúp tăng 1000% doanh thu ngay lập tức"*).
  * Mọi con số được sử dụng (*$75/tháng*, *1.5s OCR*) phải có dữ liệu đo lường thực tế từ dự án chứng minh.

---

## 🪞 LỚP 2: Kiểm Tra Giá Trị Cốt Lõi Cyberk

Video được duyệt phải thỏa mãn **Ba Tính Chất Cốt Lõi** của thương hiệu Cyberk:

1. **Tính Giải Trí (Entertainment First - Hook 3s):**
   * Có yếu tố bất ngờ/ngạc nhiên thực tế trong 3-8s đầu không? (Dashboard billing bất ngờ, lỗi terminal thực tế, sơ đồ kiến trúc độc đáo).
   * Có bị sa lầy vào giật tít rẻ tiền (Anti-clickbait test) không?
2. **Tính Giáo Dục (Educational & Useful):**
   * Người xem (Global Founders / CTOs) có mang về được **ít nhất 1 bài học/góc nhìn thực tế** có thể áp dụng được không?
   * Giải pháp kỹ thuật có được giải thích dễ hiểu thông qua ví von đời thường không?
3. **Tính Xác Thực (Authentic):**
   * Câu chuyện, bài học và code có thật sự là trải nghiệm thực chiến của Cyberk không?
   * Không dàn dựng demo đẹp mắt giả tạo, cởi mở chia sẻ cả khó khăn/bug thực tế.
4. **Định Vị IP & Action CTA:**
   * Giọng kể là người trong cuộc (*"Dev Studio kể chuyện khởi nghiệp"*).
   * Cụm từ định vị lặp lại ở Action CTA: *"Là một nhà khởi nghiệp, nếu bạn cũng đang trăn trở..."*.

---

## 🌐 LỚP 3: Kiểm Tra Tiêu Chuẩn Cộng Đồng Đa Nền Tảng

| Nền Tảng | Yêu Cầu Cốt Lõi & Bẫy Cần Tránh |
|---|---|
| **TikTok / Reels** | Tránh các từ khóa bị bóp reach: *"chuyển khoản"*, *"tiền"*, *"mua bán"*, *"link bio"* (nói lái hoặc dùng text overlay vừa phải). Không có âm thanh vi phạm bản quyền. |
| **YouTube Shorts** | Hook trực quan mạnh, subtitle font to rõ (RobotoMono), không chứa liên kết spam trong phần mô tả. |
| **LinkedIn Video** | Giữ phong thái chuyên nghiệp, tập trung vào tư duy Business & Tech Architecture trade-offs. |

---

## 🚀 Hướng Dẫn Thực Thi

1. Đọc kịch bản chi tiết từ `scripts/[STT]_[slug].md`.
2. Kiểm tra lần lượt qua 3 Lớp tiêu chuẩn ở trên.
3. Chấm điểm Pre-Publish Scorecard (yêu cầu ≥ 12/40 điểm).
4. Xuất kết quả biên bản vào file `reviews/review.md` theo template tại `skills/review/template.md`.
5. Cộng dồn các quyết định/điều chỉnh quan trọng vào `spec-ai.html`.

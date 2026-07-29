---
type: skill
name: mermaid-chart
description: "Skill chuyên biệt xử lý, làm đẹp & trực quan hóa sơ đồ kỹ thuật Mermaid.js phức tạp (System Architecture, Sequence Flow) thành trang HTML Vector mượt mượt với 3 Tab tương tác và tự động xuất video MP4."
tags: [marketing, mermaid-chart, architecture, sequence-flow, system-design, visualization, cyberk-brand, b-roll, html-diagram]
created: 2026-07-28
---

# SKILL: Mermaid Chart — Làm Đẹp & Xuất Sơ Đồ Kỹ Thuật Chi Tiết

Skill này chuyên môn hóa việc **chuyển đổi mã nguồn Mermaid.js thô (Flowchart, Sequence Diagram, Subgraph)** từ các tài liệu kỹ thuật (như `system-architecture.md`) thành các **trang HTML tương tác Vector sắc nét, chuẩn nhận diện Cyberk Solid Red**, hỗ trợ xem đa tab và tự động xuất video MP4 B-roll.

---

## 🎯 4 Tiêu Chuẩn Nâng Cấp Sơ Đồ Mermaid

### 1. Cấu Trúc 3 Tab Tương Tác (Multi-Tab Interactive Views)
Mọi sơ đồ kỹ thuật lớn khi xuất ra HTML bắt buộc phải có 3 tab chuyển đổi mượt mà:
* **🏛️ Full Architecture:** Hiển thị sơ đồ tổng thể Flowchart với các Subgraph phân vùng (Client Tenant, Control Plane, Persistent Worker, Voice Engine, Data, Billing).
* **🔄 End-to-End Flow:** Hiển thị sơ đồ trình tự Sequence Flow từ bước 1 đến bước 11 (từ lúc nhập Lead ➔ kiểm tra DNC/Calling Hours ➔ gọi thoại ➔ AMD ➔ đặt lịch GCal ➔ Post-call Webhook).
* **📋 Component Matrix:** Bảng phân bổ chi tiết về công nghệ, nhiệm vụ và vai trò của từng thành phần.

### 2. Cấu Hình Theme Vector Cyberk Solid Red (Mermaid Theme Overrides)
Ghi đè màu mặc định của Mermaid bằng màu thương hiệu Cyberk Red `#EC2B39` trên nền tối `#07080c`:

```javascript
mermaid.initialize({
    startOnLoad: true,
    theme: 'dark',
    themeVariables: {
        fontFamily: 'Plus Jakarta Sans, sans-serif',
        primaryColor: '#12141e',
        primaryTextColor: '#ffffff',
        primaryBorderColor: '#EC2B39',
        lineColor: '#EC2B39',
        secondaryColor: '#1a131b',
        tertiaryColor: '#090a0f',
        nodeBorder: '#EC2B39',
        clusterBkg: '#0d0f18',
        clusterBorder: '#242838'
    }
});
```

### 3. Tối Ưu Nền Tối & Viền Nổi Sắc Nét (No Gradients)
- Nền khung chứa Mermaid: `#07080c`.
- Viền thẻ Subgraph & Nodes: `1px solid #EC2B39` hoặc `1px solid #242838`.
- Đường nối dữ liệu: Nét đậm sắc (`#EC2B39`) với hiệu ứng mũi tên nét rõ.

### 4. Quy Chuẩn Đặt Tên File & Export MP4
- **Tên File HTML:** `[project-name]-mermaid-[chart-name].html`  
  *(Ví dụ: `ai-telemarketing-mermaid-architecture.html`)*
- **Tên File Video MP4 Bàn Giao:** `videos/[project-name]-mermaid-[chart-name].mp4`  
  *(Ví dụ: `videos/ai-telemarketing-mermaid-architecture.mp4`)*

---

## 💻 Template Mẫu HTML Mermaid Chart Chuẩn Cyberk

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mermaid System Architecture — Cyberk Solid Edition</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;900&family=Plus+Jakarta+Sans:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        :root {
            --cyberk-red: #EC2B39;
            --bg-dark: #07080c;
            --bg-card: #12141e;
            --border: #242838;
        }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: var(--bg-dark);
            color: #ffffff;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .tab-bar {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }
        .tab-btn {
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: #94a3b8;
            padding: 10px 20px;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 700;
        }
        .tab-btn.active {
            background: var(--cyberk-red);
            color: #ffffff;
            border-color: var(--cyberk-red);
        }
        .view-content { display: none; width: 100%; max-width: 980px; }
        .view-content.active { display: block; }
    </style>
</head>
<body>
    <div class="tab-bar">
        <button class="tab-btn active" onclick="switchTab('arch')">🏛️ Full Architecture</button>
        <button class="tab-btn" onclick="switchTab('flow')">🔄 End-to-End Flow</button>
    </div>

    <div id="arch" class="view-content active">
        <div class="mermaid">
            flowchart TB
                subgraph Client["Tenant Dashboard"]
                    A["Web Dashboard"]
                end
                subgraph Engine["AI Voice Engine"]
                    B["Retell AI Engine"]
                end
                A --> B
        </div>
    </div>

    <script>
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark',
            themeVariables: { primaryBorderColor: '#EC2B39', lineColor: '#EC2B39' }
        });
        function switchTab(id) {
            document.querySelectorAll('.view-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            event.target.classList.add('active');
        }
    </script>
</body>
</html>
```

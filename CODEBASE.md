# Tài liệu Chi tiết Kho Mã nguồn — GitHub Profile (`Tthanh2k6`)

> **Đường dẫn dự án:** `d:\Project\Tthanh2k6`  
> **Kho lưu trữ GitHub:** `https://github.com/Tthanh2k6/Tthanh2k6` (Special Profile Repository hiển thị trực tiếp tại `https://github.com/Tthanh2k6`)  
> **Mục đích:** Trang giới thiệu năng lực kỹ thuật chuẩn quốc tế (English) cho khách hàng Upwork, nhà tuyển dụng và cộng đồng mã nguồn mở.

---

## 1. Cấu trúc Thư mục & Tệp tin

```text
Tthanh2k6/
├── assets/
│   ├── hero-banner.svg     # Banner SVG động (CSS keyframe animations) phong cách 3D Isometric Neon Grid
│   └── metrics-strip.svg   # Thanh 4 thẻ chỉ số kỹ thuật thực chiến (KPI Cards) tự chủ 100%, không phụ thuộc server bên thứ 3
├── README.md               # Nội dung trang GitHub Profile chính (Hero, Quick Links, Capabilities, 2x2 Bento Grid, Case Studies, Tech Stack)
├── CODEBASE.md             # Tài liệu kiến trúc kho lưu trữ (file hiện tại)
└── agent.md                # Hướng dẫn cập nhật dành cho AI Agent
```

---

## 2. Thiết kế Kỹ thuật & Điểm nhấn Thị giác

1. **Tự chủ hoàn toàn đồ họa SVG (`assets/*.svg`):**
   - Thay vì phụ thuộc vào các dịch vụ bên thứ ba dễ lỗi `503` hoặc bị chặn rate-limit trên GitHub Camo (`github-readme-stats.vercel.app`), dự án tự đóng gói [`assets/hero-banner.svg`](file:///d:/Project/Tthanh2k6/assets/hero-banner.svg) và [`assets/metrics-strip.svg`](file:///d:/Project/Tthanh2k6/assets/metrics-strip.svg) với hiệu ứng hoạt ảnh CSS `@keyframes` nhúng trực tiếp.
   - Phối màu đồng bộ tuyệt đối với dự án [`d:\Project\Portfolio`](file:///d:/Project/Portfolio): nền tối `#07080D`, khối lập phương 3D isometric phát sáng cam `#FF6B00` / xanh `#00F0FF`, đèn trạng thái xanh lá `#10B981` nhấp nháy và khung cửa sổ Terminal trực quan.
2. **Bố cục Lưới Dự án 2×2 (Visual Bento Grid):**
   - Trình bày 4 dự án công khai chủ lực (`web-scraping-showcase`, `Portfolio`, `AI_Lab`, `DiemDanhQR`) kèm ảnh chụp màn hình 16:9 sắc nét, thông số kỹ thuật định lượng và nút bấm tới thẳng **Live Demo** / **Source Code**.
3. **Liên kết Chéo Hệ sinh thái Cá nhân:**
   - Kết nối trực tiếp tới **Upwork Profile** (`https://www.upwork.com/freelancers/~01ee7c2348cb4b62fe`), **3D Interactive Portfolio** (`https://portfolio-red-theta-65.vercel.app/`) và trang xuất **CV A4**.

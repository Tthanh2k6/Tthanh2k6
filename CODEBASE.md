# Tài liệu Chi tiết Kho Mã nguồn — GitHub Profile (`Tthanh2k6`)

> **Đường dẫn dự án:** `d:\Project\Tthanh2k6`  
> **Kho lưu trữ GitHub:** `https://github.com/Tthanh2k6/Tthanh2k6` (Special Profile Repository hiển thị trực tiếp tại `https://github.com/Tthanh2k6`)  
> **Mục đích:** Trang giới thiệu năng lực (English) cho khách Upwork, nhà tuyển dụng và cộng đồng mã nguồn mở.

---

## 1. Cấu trúc Thư mục & Tệp tin

```text
Tthanh2k6/
├── assets/
│   ├── hero-banner.svg      # Banner SVG động (CSS @keyframes): pill "Available", tên, chức danh, thanh terminal 1 dòng, khối lập phương isometric
│   ├── vn-sme-tools.gif     # GIF 4 màn hình THẬT của vn-sme-offline-tools (chụp khổ 840px, DPR 2, thu về 1260x840)
│   └── cards/*.svg          # 4 thẻ dự án 410x200 (web-scraping-showcase, b2b-enricher, price-monitor, diemdanhqr)
├── scripts/
│   ├── make_cards.py        # Sinh assets/cards/*.svg — sửa danh sách CARDS rồi chạy: python -X utf8 scripts/make_cards.py assets/cards
│   └── shoot.py             # Chụp màn vn-sme-offline-tools bằng Playwright: python -X utf8 scripts/shoot.py <thư-mục-ra>
├── README.md                # Nội dung trang profile
├── CODEBASE.md              # Tài liệu này
└── agent.md                 # Hướng dẫn cho AI Agent
```

---

## 2. Bố cục `README.md` (từ trên xuống)

1. Hero banner (`assets/hero-banner.svg`) + dòng chữ tự gõ (`readme-typing-svg.demolab.com`).
2. Hàng badge `shields.io`: Upwork · Apify Store · Portfolio (`trungthanhtran.vercel.app`) · dev.to · Email.
3. "Hi, I'm Thanh" + câu kêu gọi thuê (blockquote).
4. "What I work on" — danh sách 4 mảng.
5. "Stack" — `skillicons.dev` + badge cho httpx/Playwright/Apify/n8n/Make/Apps Script/Expo.
6. "Featured projects" — `vn-sme-offline-tools` (GIF thật + badge Live demo/Source) và lưới 2×2 thẻ SVG; `<details>` "More public projects".
7. "Certificates" — badge HackerRank; chân trang sóng `capsule-render.vercel.app`.

---

## 3. Bất biến (Guardrails)

1. **Chỉ thông tin kiểm chứng được, ẩn điểm yếu nhưng không bịa điểm mạnh.** Không đưa số liệu tự đặt (accuracy %, tốc độ x lần, "N accounts verified"...). Đã gỡ `metrics-strip.svg` và các ảnh `Portfolio/public/IMG/project-*.png` vì là ảnh minh họa dựng sẵn kèm số liệu bịa.
2. **Không đặt thẻ làm lộ số yếu:** streak (dài nhất 4 ngày), tổng contributions, rắn contribution (20 tuần đầu năm trống), star/follower count.
3. **Ảnh minh họa phải là ảnh chụp thật** của sản phẩm, không dùng ảnh AI/mockup.
4. **Cỡ chữ:** cột README trên profile rộng ~830px. Ảnh/SVG phải thiết kế theo kích thước hiển thị thật (thẻ 2 cột → rộng 410; ảnh full cột → chụp ~840px) để chữ ≥ 12px.
5. Dịch vụ thống kê chạy trên Vercel (`github-readme-stats`, `github-readme-activity-graph`) đang lỗi `402/503` — không dùng.

---

## 4. Kiểm tra trước khi push

Render bằng API của GitHub (chế độ `markdown`, giống README) rồi xem ở khổ 830px:

```bash
python -X utf8 -c "import json;print(json.dumps({'text':open('README.md',encoding='utf8').read(),'mode':'markdown'}))" > req.json
gh api markdown --input req.json > body.html   # bọc thêm github-markdown-dark.css, width:830px để xem
```

---

## 9. Nhật ký Cập nhật Tài liệu

- 2026-10-31: Thiết kế lại profile — banner chữ lớn, GIF màn hình thật, thẻ SVG 410px, bỏ `metrics-strip.svg`, thêm `scripts/make_cards.py` + `scripts/shoot.py`, thêm mục Bất biến.

"""Sinh thẻ dự án SVG cho GitHub profile — chỉ chữ thật, không số liệu bịa."""
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

CARDS = [
    ("web-scraping-showcase", "PYTHON · TOOLKIT", "web-scraping-showcase",
     "Async httpx + Playwright scraping patterns, an API sniffer CLI, retry/backoff, CSV / XLSX / SQLite output.",
     ["httpx", "Playwright", "SQLite", "pytest"], "#3776AB"),
    ("b2b-enricher", "APIFY ACTOR", "B2B lead & contact enricher",
     "Finds emails, phone numbers, social links and the tech stack on company websites.",
     ["Python", "Apify SDK", "httpx", "BS4"], "#97D700"),
    ("price-monitor", "APIFY ACTOR", "E-commerce price & stock monitor",
     "Reads price and stock from Shopify / WooCommerce product pages, including Product JSON-LD.",
     ["Python", "Apify", "Shopify", "WooCommerce"], "#97D700"),
    ("diemdanhqr", "PWA · APPS SCRIPT", "DiemDanhQR",
     "QR attendance check-in PWA that writes straight to Google Sheets through an Apps Script webhook.",
     ["JavaScript", "PWA", "Apps Script", "Sheets"], "#10B981"),
]

W, H = 410, 200
SANS = "'Segoe UI', -apple-system, Helvetica, Arial, sans-serif"
MONO = "Consolas, 'SFMono-Regular', ui-monospace, monospace"


def card(label, title, desc, chips, accent):
    lines = textwrap.wrap(desc, 54)[:3]
    desc_svg = "".join(
        f'<text x="22" y="{98 + i * 20}" class="d">{escape(l)}</text>' for i, l in enumerate(lines)
    )
    x, chip_svg = 22, ""
    for c in chips:
        w = 14 + len(c) * 6.8
        chip_svg += (f'<rect x="{x}" y="160" width="{w:.0f}" height="24" rx="12" class="chip"/>'
                     f'<text x="{x + w / 2:.0f}" y="175" class="ct" text-anchor="middle">{escape(c)}</text>')
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <style>
    .l {{ font: 600 11px {MONO}; letter-spacing: 1.5px; fill: {accent}; }}
    .t {{ font: 700 19px {SANS}; fill: #F0F6FC; }}
    .d {{ font: 400 13.5px {SANS}; fill: #9DA7B3; }}
    .chip {{ fill: #161B26; stroke: #2A3140; }}
    .ct {{ font: 500 11.5px {MONO}; fill: #C9D1D9; }}
    .sweep {{ animation: sweep 4s ease-in-out infinite; }}
    @keyframes sweep {{ 0% {{ transform: translateX(-120px); }} 100% {{ transform: translateX({W}px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .sweep {{ animation: none; opacity: 0; }} }}
  </style>
  <defs>
    <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#FF6B00" stop-opacity="0"/><stop offset=".5" stop-color="#FF6B00"/><stop offset="1" stop-color="#FF6B00" stop-opacity="0"/></linearGradient>
    <clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="#0D111A"/>
    <rect width="{W}" height="2" fill="#1F2633"/>
    <rect class="sweep" width="120" height="2" fill="url(#g)"/>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="#232A36"/>
  <circle cx="27" cy="32" r="4" fill="{accent}"/>
  <text x="38" y="36" class="l">{escape(label)}</text>
  <text x="22" y="70" class="t">{escape(title)}</text>
  {desc_svg}
  {chip_svg}
</svg>
'''


for slug, label, title, desc, chips, accent in CARDS:
    (OUT / f"{slug}.svg").write_text(card(label, title, desc, chips, accent), encoding="utf-8")
    print("wrote", slug)

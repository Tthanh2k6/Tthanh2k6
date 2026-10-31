"""Chụp màn thật của vn-sme-offline-tools ở khổ hẹp (~bằng cột README GitHub), DPR 2 cho nét."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://tthanh2k6.github.io/vn-sme-offline-tools/tools/"
PAGES = ["vietqr-cashier", "fleet-reconciler", "ar-aging", "wholesale-quote", "tax-xml-reconciler"]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 840, "height": 560}, device_scale_factor=2)
    for name in PAGES:
        pg.goto(BASE + name + ".html", wait_until="networkidle")
        pg.wait_for_timeout(800)
        pg.screenshot(path=str(OUT / f"{name}.png"))
        print("shot", name)
    b.close()

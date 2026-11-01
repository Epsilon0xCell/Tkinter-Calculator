#!/usr/bin/env python3
"""Tkinter-Calculator wordmark banner: inside the ropewalk, strands running the shed length
between fixed post and travelling hook, workers as distant silhouettes walking backward,
bales, tar pot, chalk tally board carrying the name in Anybody, oil lamps pooling amber,
finished coil beside a measuring rod in the foreground."""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H = 1600, 560
img = Image.new("RGB", (W, H), (48, 42, 32)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(64 - 14 * t), int(56 - 12 * t), int(40 - 6 * t)))
d.rectangle([770, 190, 830, 330], fill=(235, 230, 205))  # far door postage stamp of light
for bx in (120, 420, 700, 960, 1200):
    d.rectangle([bx, 60, bx + 22, 430], fill=(36, 30, 22))
    d.line([(bx, 70), (bx + 260, 56)], fill=(36, 30, 22), width=8)
for lx in (260, 620, 980, 1320):  # lamps pooling amber
    d.line([(lx, 60), (lx, 120)], fill=(30, 26, 20), width=3)
    d.ellipse([lx - 16, 120, lx + 16, 148], fill=(255, 176, 64))
    d.ellipse([lx - 90, 400, lx + 90, 446], fill=(255, 176, 64, 46))
# strands full length at waist height
for k in range(3):
    pts = [(x, 268 + k * 16 + math.sin(x / 90.0 + k * 2.1) * (10 * x / W)) for x in range(120, 1490, 8)]
    d.line(pts, fill=(198, 160, 94), width=9)
d.rectangle([100, 190, 132, 420], fill=(26, 24, 24))
d.arc([1420, 230, 1490, 320], 90, 300, fill=(180, 180, 178), width=7)
for wx in (520, 1080):  # worker silhouettes walking backward, small and dark
    d.ellipse([wx - 11, 218, wx + 11, 240], fill=(18, 16, 14))
    d.polygon([(wx - 10, 240), (wx + 12, 240), (wx + 16, 310), (wx + 2, 310)], fill=(18, 16, 14))
    d.line([(wx + 2, 310), (wx - 8, 372)], fill=(18, 16, 14), width=8)
    d.line([(wx + 4, 310), (wx + 20, 370)], fill=(18, 16, 14), width=8)
# tally board with chalked name
d.rectangle([180, 330, 720, 500], fill=(28, 34, 32), outline=(110, 88, 56), width=5)
try:
    f = ImageFont.truetype("fonts/Anybody.ttf", 46)
    fs = ImageFont.truetype("fonts/Anybody.ttf", 26)
except Exception:
    f = ImageFont.load_default(); fs = f
d.text((206, 356), "Tkinter-Calculator", font=f, fill=(245, 242, 230))
d.text((206, 424), "length just completed", font=fs, fill=(200, 205, 195))
for tx in range(206, 700, 34):
    d.line([(tx, 462), (tx, 480)], fill=(220, 220, 205), width=3)
# finished coil and measuring rod foreground right
for r in (86, 64, 42):
    d.ellipse([1180 - r, 470 - r // 2, 1180 + r, 470 + r // 2], outline=(198, 160, 94), width=11)
d.rectangle([1330, 440, 1540, 456], fill=(150, 118, 66))
for tx in range(1338, 1536, 20):
    d.line([(tx, 440), (tx, 450)], fill=(40, 32, 18), width=2)
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)

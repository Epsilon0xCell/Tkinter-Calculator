#!/usr/bin/env python3
"""Tkinter-Calculator logo: three hemp strands mid twist forming one diagonal cord, tar
black grooves, foam white fibre tops, one lantern amber glint; Anybody wordmark beneath
like a stencil on a rope bale. At 64px the diagonal twist alone carries it."""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H = 900, 700
img = Image.new("RGB", (W, H), (16, 42, 46)); d = ImageDraw.Draw(img, "RGBA")
for phase, col, wdt in ((0.0, (24, 22, 18), 64), (2.1, (196, 164, 100), 44), (4.2, (226, 200, 138), 44)):
    pts = [(x, 330 - (x - 450) * 0.42 + math.sin(x / 52.0 + phase) * 34) for x in range(120, 790, 6)]
    d.line(pts, fill=col, width=wdt)
pts = [(x, 330 - (x - 450) * 0.42 + math.sin(x / 52.0) * 34) for x in range(120, 790, 6)]
gx, gy = pts[len(pts) // 2]
d.ellipse([gx - 16, gy - 16, gx + 16, gy + 16], fill=(255, 176, 64))
for x in range(140, 780, 26):  # fibre ticks on top strand
    y = 330 - (x - 450) * 0.42 + math.sin(x / 52.0 + 2.1) * 34
    d.line([(x, y - 20), (x + 8, y - 6)], fill=(250, 246, 232), width=3)
try:
    f = ImageFont.truetype("fonts/Anybody.ttf", 54)
except Exception:
    f = ImageFont.load_default()
txt = "Tkinter-Calculator"
bb = d.textbbox((0, 0), txt, font=f)
d.text(((W - (bb[2] - bb[0])) / 2, 540), txt, font=f, fill=(240, 230, 196))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out)
img.resize((64, 64)).save("scratch/logo64-ship.png" if v == "ship" else f"scratch/logo64-{v}.png")
print(out)

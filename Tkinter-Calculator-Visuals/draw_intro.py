#!/usr/bin/env python3
"""Tkinter-Calculator intro banner: inside the ropewalk, wordless. Iron post with three
fanned hemp strands converging and twisting into one rope down a long shed of bays, high
windows with dusty daylight, bales, cold tar kettle, bench tools, open doors at the end.
No writing, signs, labels, or figures facing the viewer."""
import sys, os, random, math
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(41)
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H = 1600, 900
img = Image.new("RGB", (W, H), (52, 46, 36)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(70 - 18 * t), int(62 - 14 * t), int(46 - 8 * t)))
# floorboards perspective
for k in range(14):
    y = 560 + k * 26
    d.line([(0, y), (W, y)], fill=(38, 30, 20), width=3)
for x in range(-200, 1900, 180):
    d.line([(x, 560), (800 + (x - 800) // 3, 900)], fill=(40, 32, 22), width=2)
# shed bays receding: posts, beams, high windows
for i, bx in enumerate((60, 340, 580, 760, 900, 1010, 1090)):
    s = 1 - i * 0.11
    d.rectangle([bx, 120, bx + int(26 * s) + 8, 580], fill=(44, 36, 26))
    d.line([(bx, 130), (bx + 300, 110)], fill=(44, 36, 26), width=int(10 * s) + 3)
    wx, wy = bx + 90, 150
    d.rectangle([wx, wy, wx + int(110 * s) + 20, wy + int(120 * s) + 20], fill=(226, 214, 170))
    d.rectangle([wx, wy, wx + int(110 * s) + 20, wy + int(120 * s) + 20], outline=(30, 26, 20), width=3)
# dusty daylight columns
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
for sx in (200, 520, 800):
    ld.polygon([(sx, 150), (sx + 90, 150), (sx + 260, 700), (sx + 60, 700)], fill=(255, 232, 170, 42))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(14))).convert("RGB"); d = ImageDraw.Draw(img, "RGBA")
# far doors open onto plain daylight, yard grass
d.rectangle([742, 330, 858, 560], fill=(232, 230, 200)); d.rectangle([742, 520, 858, 560], fill=(110, 140, 80))
# bales along left wall
for bx, by, bw in ((90, 470, 190), (110, 380, 160), (880, 470, 150)):
    d.rectangle([bx, by, bx + bw, by + 76], fill=(168, 138, 84), outline=(96, 76, 44), width=3)
    d.line([(bx + bw // 2, by), (bx + bw // 2, by + 76)], fill=(96, 76, 44), width=4)
    for fx in range(bx + 8, bx + bw - 8, 9):
        d.line([(fx, by + 6), (fx + 3, by + 70)], fill=(190, 162, 100), width=1)
# tar kettle cold, bench with knives combs hooks (right)
d.ellipse([1180, 520, 1310, 566], fill=(18, 18, 18)); d.rectangle([1196, 470, 1294, 528], fill=(26, 26, 26))
d.rectangle([1150, 600, 1520, 626], fill=(74, 58, 38))
for kx in (1200, 1260, 1330):
    d.polygon([(kx, 586), (kx + 34, 592), (kx, 598)], fill=(190, 192, 190))
for hx in (1400, 1440, 1480):
    d.arc([hx, 570, hx + 26, 606], 180, 330, fill=(170, 170, 168), width=4)
# reel leaning on wall
d.ellipse([1360, 300, 1490, 430], outline=(96, 74, 44), width=10); d.ellipse([1398, 338, 1452, 392], outline=(96, 74, 44), width=6)
for ang in range(0, 360, 45):
    d.line([(1425, 365), (1425 + int(58 * math.cos(math.radians(ang))), 365 + int(58 * math.sin(math.radians(ang))))], fill=(150, 122, 72), width=4)
# three strands from near post, fanning then twisting into one rope
d.rectangle([150, 300, 196, 640], fill=(30, 28, 28)); d.rectangle([128, 620, 218, 648], fill=(22, 20, 20))
for sx in (0, 1, 2):
    pts = []
    for t in range(0, 101):
        x = 196 + t * 6.2
        y = 360 + sx * 70 + (470 - (360 + sx * 70)) * (t / 100) + (math.sin(t / 9.0 + sx * 2.1) * 16 * (t / 100))
        pts.append((x, y))
    d.line(pts, fill=(196, 158, 92), width=13)
    d.line([(x, y - 4) for x, y in pts], fill=(232, 200, 130), width=4)
for t in range(0, 60):  # fibre scraps near post
    x, y = random.randint(110, 330), random.randint(630, 700)
    d.line([(x, y), (x + random.randint(6, 20), y + random.randint(-3, 3))], fill=(200, 168, 100), width=2)
img = img.filter(ImageFilter.GaussianBlur(0.5))
rng = np.random.default_rng(7); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)

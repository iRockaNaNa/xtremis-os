#!/usr/bin/env python3
"""Xtremis OS boot animation generator — a Nanatech Creative Solutions project.

Draws a Windows 10 Mobile-style boot animation: the four-pane window logo
fades in on black (part0, plays once), then holds with the classic rotating
dot chase beneath it (part1, loops until boot completes).

Output: bootanimation.zip (stored, uncompressed — as Android requires)
plus the raw frames, next to this script. Spec: 720x1280 @ 30 fps; the
Razer Phone 2 panel is 1440x2560, Android scales the frames to fit.

Usage: python3 generate_bootanimation.py
"""
import math, os, zipfile
from PIL import Image, ImageDraw

W, H, FPS = 720, 1280, 30
WHITE = (255, 255, 255)
OUT = os.path.dirname(os.path.abspath(__file__))

def logo(draw, cx, cy, size, alpha):
    """Four squares with gaps — the window mark, flat front view."""
    gap = size * 0.045
    cell = (size - gap) / 2
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for r in range(2):
        for c in range(2):
            x0 = cx - size / 2 + c * (cell + gap)
            y0 = cy - size / 2 + r * (cell + gap)
            d.rectangle([x0, y0, x0 + cell, y0 + cell], fill=WHITE + (alpha,))
    return layer

def frame_part0(i, total):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    t = i / max(total - 1, 1)
    ease = 1 - (1 - t) ** 3
    alpha = int(255 * ease)
    size = 300 * (0.94 + 0.06 * ease)
    img.alpha_composite(logo(None, W / 2, H * 0.42, size, alpha))
    return img.convert("RGB")

def frame_part1(i, total):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    img.alpha_composite(logo(None, W / 2, H * 0.42, 300, 255))
    dots = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(dots)
    cx, cy, R = W / 2, H * 0.60, 46
    head = (i / total) * 2 * math.pi
    for k in range(5):
        ang = head - k * 0.42
        a = int(255 * (1 - k / 5.5))
        r = 9 - k * 0.9
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE + (a,))
    img.alpha_composite(dots)
    return img.convert("RGB")

def main():
    parts = {"part0": (frame_part0, 24), "part1": (frame_part1, 30)}
    os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
    with zipfile.ZipFile(os.path.join(OUT, "bootanimation.zip"), "w", zipfile.ZIP_STORED) as z:
        desc = f"{W} {H} {FPS}\np 1 0 part0\np 0 0 part1\n"
        z.writestr("desc.txt", desc)
        for part, (fn, count) in parts.items():
            pdir = os.path.join(OUT, "frames", part)
            os.makedirs(pdir, exist_ok=True)
            for i in range(count):
                frame = fn(i, count)
                name = f"{i:03d}.png"
                frame.save(os.path.join(pdir, name))
                with open(os.path.join(pdir, name), "rb") as f:
                    z.writestr(f"{part}/{name}", f.read())
    print("bootanimation.zip written to", OUT)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Arc-reactor boot animation for Xtremis OS — a Nanatech Creative Solutions project.

The reactor powers up (ring sweeps in, coils light in sequence, the
triangular core ignites) in part0, then breathes with a slow pulse in
part1 until boot completes. Pairs with the ARC Kernel
("Another Really Cool Kernel").

Output: bootanimation-arc.zip (stored) + frames, next to this script.
Spec: 720x1280 @ 30 fps.
"""
import math, os, zipfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

import os as _os
W = int(_os.environ.get("XTREMIS_W", "720"))
H = int(_os.environ.get("XTREMIS_H", "1280"))
FPS = 30
S = W / 720.0
GLOW = (140, 220, 255)
CORE = (230, 250, 255)
COBALT = (0, 80, 239)
OUT = os.path.dirname(os.path.abspath(__file__))
CX, CY, R = W / 2, H * 0.44, 150 * S

def reactor(power, rot):
    """power 0..1 ignition level; rot = coil highlight rotation (rad)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    # outer glow rings
    for wdt, a in [(int(26 * S), 60), (int(16 * S), 100), (int(8 * S), 170)]:
        d.ellipse([CX - R, CY - R, CX + R, CY + R], outline=GLOW + (int(a * power),), width=wdt)
    # coils: 10 segments around the ring, lighting with the sweep
    for k in range(10):
        ang = rot + k * (2 * math.pi / 10)
        lit = 1.0 if power >= (k + 1) / 10 else max(0.0, power * 10 - k)
        if lit <= 0:
            continue
        x0, y0 = CX + (R - 26 * S) * math.cos(ang), CY + (R - 26 * S) * math.sin(ang)
        x1, y1 = CX + (R + 6 * S) * math.cos(ang), CY + (R + 6 * S) * math.sin(ang)
        col = tuple(int(c * lit) for c in GLOW)
        d.line([x0, y0, x1, y1], fill=col + (int(230 * lit),), width=int(17 * S))
    # inner ring
    r2 = R * 0.66
    d.ellipse([CX - r2, CY - r2, CX + r2, CY + r2], outline=GLOW + (int(200 * power),), width=int(7 * S))
    # triangular core (apex down), ignites last
    tri_a = max(0.0, (power - 0.55) / 0.45)
    if tri_a > 0:
        pts = [(CX + r2 * 0.78 * math.cos(a), CY + r2 * 0.78 * math.sin(a))
               for a in (math.pi / 2, math.pi / 2 + 2.094, math.pi / 2 + 4.189)]
        d.polygon(pts, outline=CORE + (int(255 * tri_a),), width=int(10 * S))
        d.polygon(pts, fill=(120, 200, 255, int(70 * tri_a)))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(6 * S)))
    img.alpha_composite(glow)
    return img

FONT_DIR = "/usr/share/fonts/truetype/noto"

ASSETS = os.path.join(OUT, "assets")

def _load_asset(name):
    try:
        return Image.open(os.path.join(ASSETS, name)).convert("RGBA")
    except OSError:
        return None

def footer(alpha):
    """Footer lockup: the classic thin lowercase 'powered by android'
    badge (reference art supplied by the project owner, used directly)
    with the official green bugdroid head peeking from the bottom
    edge beneath it, as on production devices."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cx = W / 2
    head = _load_asset("android-head.png")
    if head is not None:
        tw = int(200 * S)
        head = head.resize((tw, int(head.size[1] * tw / head.size[0])), Image.LANCZOS)
        if alpha < 255:
            a = head.split()[3].point(lambda v: v * alpha // 255)
            head.putalpha(a)
        layer.alpha_composite(head, (int(cx - tw / 2), int(H - head.size[1] * 0.88)))
    badge = _load_asset("powered-by-android.png")
    if badge is not None:
        tw = int(330 * S)
        badge = badge.resize((tw, int(badge.size[1] * tw / badge.size[0])), Image.LANCZOS)
        if alpha < 255:
            a = badge.split()[3].point(lambda v: v * alpha // 255)
            badge.putalpha(a)
        layer.alpha_composite(badge, (int(cx - tw / 2), int(H * 0.822)))
    return layer

def part0(i, total):
    t = i / max(total - 1, 1)
    base = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    base.alpha_composite(reactor(min(1.0, t * 1.15), -math.pi / 2))
    fa = int(255 * max(0.0, min(1.0, (t - 0.45) / 0.4)))
    if fa > 0:
        base.alpha_composite(footer(fa))
    return base.convert("RGB")

def part1(i, total):
    t = i / total
    pulse = 0.88 + 0.12 * math.sin(t * 2 * math.pi)
    base = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    r = reactor(pulse, -math.pi / 2 + t * 2 * math.pi / 10)
    base.alpha_composite(r)
    base.alpha_composite(footer(255))
    return base.convert("RGB")

def main():
    parts = {"part0": (part0, 36), "part1": (part1, 40)}
    fdir = os.path.join(OUT, "frames-reactor" if (W, H) == (720, 1280) else f"frames-reactor-{W}x{H}")
    with zipfile.ZipFile(os.path.join(OUT, "bootanimation-arc.zip" if (W, H) == (720, 1280) else f"bootanimation-arc-{W}x{H}.zip"), "w", zipfile.ZIP_STORED) as z:
        z.writestr("desc.txt", f"{W} {H} {FPS}\np 1 0 part0\np 0 0 part1\n")
        for part, (fn, count) in parts.items():
            pdir = os.path.join(fdir, part)
            os.makedirs(pdir, exist_ok=True)
            for i in range(count):
                fr = fn(i, count)
                name = f"{i:03d}.png"
                fr.save(os.path.join(pdir, name))
                with open(os.path.join(pdir, name), "rb") as f:
                    z.writestr(f"{part}/{name}", f.read())
    print("bootanimation-arc written:", W, "x", H)

if __name__ == "__main__":
    main()

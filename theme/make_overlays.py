#!/usr/bin/env python3
"""Generate Xtremis accent RRO overlay packages — Nanatech Creative Solutions.

Stamps out framework + SystemUI runtime-resource-overlay sources for one
accent from the WP palette (ASSETS.md). Cobalt is the shipped default;
every other accent generates identically, ready for the Phase 3
switcher. Usage: python3 make_overlays.py [accent-name]  (default cobalt)
"""
import colorsys, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ACCENTS = {
    "lime": "#A4C400", "green": "#60A917", "emerald": "#008A00",
    "teal": "#00ABA9", "cyan": "#1BA1E2", "cobalt": "#0050EF",
    "indigo": "#6A00FF", "violet": "#AA00FF", "pink": "#F472D0",
    "magenta": "#D80073", "crimson": "#A20025", "red": "#E51400",
    "orange": "#FA6800", "amber": "#F0A30A", "yellow": "#E3C800",
    "brown": "#825A2C", "olive": "#6D8764", "steel": "#647687",
    "mauve": "#76608A", "taupe": "#87794E",
}
TONES = [0, 10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def hex2hls(hx):
    r, g, b = (int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return colorsys.rgb_to_hls(r, g, b)

def tone_hex(h, l_base, s, t):
    """AOSP tonal convention: 0 = white, 1000 = black, ~500 = source."""
    L = (1000 - t) / 1000.0
    r, g, b = colorsys.hls_to_rgb(h % 1.0, L, s)
    return "#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))

def palette(hx):
    h, _l, s = hex2hls(hx)
    pal = {}
    for name, (hh, ss) in {
        "accent1": (h, s), "accent2": (h, s * 0.45),
        "accent3": (h + 60 / 360.0, s * 0.8),
        "neutral1": (h, 0.08), "neutral2": (h, 0.16),
    }.items():
        for t in TONES:
            pal[f"system_{name}_{t}"] = tone_hex(hh, _l, ss, t)
    pal["system_accent1_500"] = hx.upper()  # source tone = the accent itself
    return pal

def colors_xml(hx, extra):
    pal = palette(hx)
    lines = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
    for k in sorted(pal, key=lambda k: (k.rsplit("_", 1)[0], int(k.rsplit("_", 1)[1]))):
        lines.append(f'    <color name="{k}">{pal[k]}</color>')
    for k, v in extra.items():
        lines.append(f'    <color name="{k}">{v}</color>')
    lines.append("</resources>")
    return "\n".join(lines) + "\n"

MANIFEST = """<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.nanatech.xtremis.accent.{accent}.{pkg}">
    <overlay android:targetPackage="{target}" android:priority="10"
        android:isStatic="true" />
    <application android:label="Xtremis Accent {Title} ({label})"
        android:hasCode="false" />
</manifest>
"""
BP = """runtime_resource_overlay {
    name: "XtremisAccent{Title}{Label}",
    certificate: "platform",
    product_specific: true,
}
"""

def write_pkg(accent, hx, pkg, target, label, extra):
    title = accent.capitalize()
    d = os.path.join(HERE, "overlays", accent, f"XtremisAccent{label}")
    os.makedirs(os.path.join(d, "res", "values"), exist_ok=True)
    open(os.path.join(d, "AndroidManifest.xml"), "w").write(
        MANIFEST.replace("{accent}", accent).replace("{pkg}", pkg)
        .replace("{target}", target).replace("{Title}", title)
        .replace("{label}", label))
    open(os.path.join(d, "Android.bp"), "w").write(
        BP.replace("{Title}", title).replace("{Label}", label))
    open(os.path.join(d, "res", "values", "colors.xml"), "w").write(colors_xml(hx, extra))
    return d

def main():
    accent = sys.argv[1] if len(sys.argv) > 1 else "cobalt"
    hx = ACCENTS[accent]
    fw_extra = {
        "accent_material_dark": hx, "accent_material_light": hx,
        "background_dark": "#000000",
    }
    write_pkg(accent, hx, "framework", "android", "Framework", fw_extra)
    write_pkg(accent, hx, "systemui", "com.android.systemui", "SystemUI", {})
    json.dump(ACCENTS, open(os.path.join(HERE, "accents.json"), "w"), indent=1)
    print(f"overlays for {accent} ({hx}) written under overlays/{accent}/")

if __name__ == "__main__":
    main()

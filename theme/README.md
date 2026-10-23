# Accent theme overlays

A Nanatech Creative Solutions project.

Runtime resource overlays (RRO) that carry the Windows Phone accent
system into Android's framework and SystemUI.

## How it works

- `make_overlays.py` generates one overlay pair per accent from the
  palette in ASSETS.md (all 20 accents are in `accents.json`):
  - **XtremisAccent\<Name\>Framework** → targets `android`: the full
    Material tonal scales (accent1/2/3, neutral1/2, tones 0–1000)
    computed from the accent, the material accent hooks, and
    `background_dark` pinned to pure black #000000 (the WP look).
  - **XtremisAccent\<Name\>SystemUI** → targets
    `com.android.systemui`: the same tonal scales (SystemUI keeps its
    own copies), which drive quick-settings tiles, sliders, and the
    notification shade.
- Tone convention follows AOSP: 0 = white, 1000 = black, and
  `system_accent1_500` is pinned to the accent hex itself.
- **Cobalt (#0050EF) is the shipped default** — its packages are
  generated and committed under `overlays/cobalt/`. Generate any
  other accent with `python3 make_overlays.py <accent>`; the Phase 3
  switcher enables the chosen pair at runtime.
- Settings needs no overlay package: AOSP Settings reads the
  framework's dynamic palette, so it follows automatically. (Verify
  on device in Phase 2 testing.)

## Integration

- ROM route: add the two packages to the product (`PRODUCT_PACKAGES`)
  under `device/razer/aura`; they are static, platform-signed RROs.
- Flashable-zip route: the same APKs install to `/product/overlay/`.

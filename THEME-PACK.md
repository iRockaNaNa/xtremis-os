# Xtremis OS — Phase 2: Theme Pack Plan

A Nanatech Creative Solutions project.

The theme pack is a flashable zip that turns the stock LineageOS 22.2
baseline into Xtremis visually — and later merges into the ROM tree so
MK builds ship it built-in. Everything visual comes from the Metro 10
Launcher's own definitions (see ASSETS.md); nothing is reinvented.

## Package format

- One recovery-flashable zip: `xtremis-theme-pack.zip`
- Installs to `/system/media`, `/system/fonts`, and framework/SystemUI
  overlay (RRO) locations on the baseline build
- Same files, same paths when merged into `device/razer/aura` for MK
  builds — the pack is the ROM theme, just delivered separately first

## Contents

### 1. Boot animation — ASSET DONE
- Arc-reactor animation (default): reactor power-up + breathing loop,
  classic "powered by android" badge, official bugdroid head peeking
  from the bottom edge. Generator: `bootanimation/`
- DONE 2026-10-23: frames re-rendered at the Razer Phone 2's native
  1440×2560 (`bootanimation/bootanimation-arc-1440x2560.zip`, 15 MB);
  the 720×1280 master remains for previews
- The Windows-logo animation is parked for a later MK release

### 2. Fonts — PACK ASSEMBLED 2026-10-23
- Ship: **Noto Sans** family from Google Fonts (open license) —
  8 TTFs (Light 300, Regular 400 + Italic, Medium 500, SemiBold 600,
  Bold 700 + Bold Italic, Black 900) in `fonts/`, with
  `fonts-xtremis.xml` family definitions. At packaging, the TTFs go
  to /system/fonts and the families merge into the baseline's
  fonts.xml (fallbacks preserved)
- The genuine Windows default font is owner-supplied for personal
  builds only and never ships in a public zip (Microsoft IP)

### 3. Wallpaper set — SOURCED 2026-10-23
- The genuine Windows 10 Mobile stock set, supplied by the project
  owner: 10 photos at 1080×1920 (the build-10162-era extraction) in
  `wallpapers/` (img0–img9: teal abstract, sea stacks, Milky Way tent,
  climber, snorkeler, Windows hero light, fjord, ice cave, tropical
  bay, mountain biker)
- 1080×1920 is exactly 9:16 like the Razer Phone 2's 1440×2560 panel,
  so they upscale cleanly with no cropping
- Rights note: Microsoft's photos are Microsoft IP — personal build
  use; a public MK release ships open-licensed WP-style photography
  unless rights are cleared

### 4. Accent theme — OVERLAYS BUILT 2026-10-23
- Full palette captured (20 WP accents, ASSETS.md); cobalt #0050EF is
  the default
- Built in `theme/`: a generator stamps out framework + SystemUI RRO
  overlay packages for any accent (full tonal scales from the accent,
  background_dark pinned to pure black #000000); cobalt's packages
  are generated and ready, the other 19 generate on demand for the
  Phase 3 switcher. Settings follows the framework palette (verify
  on device)

### 5. Sounds — DONE 2026-10-23 (two sets, see sounds/README.md)
- Authentic library (owner-supplied): the Lumia/WP stock tones —
  43 ringtones, 15 notifications, 2 alarms, WMA→OGG converted.
  Defaults: Microsoft Ringtone / Lumia Message / Lumia Clock.
  Personal builds only (Microsoft IP)
- Original synthesized set: lock, unlock, keypress family, tick,
  camera, plus notification/alert — covers UI sounds in all builds
  and is the public-release sound set

### 6. System glyphs — BUILT 2026-10-23
- 15 Android vector drawables in `glyphs/` (thin-stroke 48-grid,
  W10M outline style, tint at use site): the 7 Action Center glyphs
  (flashlight, bluetooth, wi-fi, DND, airplane, rotation, brightness)
  + 8 Settings category glyphs from the reference screenshot. v1
  geometry; fidelity pass against the Elite x3 during device testing

### 7. Built-in suite apps
- Metro 10 Launcher preinstalled as the default home
- Metro 10 Messaging preinstalled
- (Suite accent sync noted in ASSETS.md applies here: Messaging's
  hard-coded #0078D7 unifies to the launcher palette when packaged)

### 8. Live wallpaper support — MODERNIZATION (added 2026-10-23)
Windows 10 Mobile never had live wallpapers; Xtremis keeps the look
but runs modern underneath. Two parts:
- **Support:** Metro 10 Launcher's Start gets a see-through mode so
  any Android live wallpaper (WallpaperService) shows behind the
  tiles, with a dim/transparency control so tiles stay readable.
  Anything the Play Store offers then just works, lock screen too.
- **Bundled signature live wallpaper — "PhotoFlow":** the sourced
  W10M stock photos crossfading with a slow Ken Burns pan/zoom,
  finished with a gradient tint in the active accent color. On the
  lock screen it can carry Metro-type time/weather, WP "live lock
  screen" style, modernized.
- Later options (not v1): short looping video wallpapers, parallax
  tilt, battery-aware dimming at night.

## Milestone
- Theme pack flashed on the Phase 1-verified baseline and verified
  on the phone → this becomes **MK1**

## Out of scope for Phase 2
- WP10 lock screen and nav bar (Phase 3, SystemUI rebuild)
- Accent switching UI (Phase 3; Phase 2 only prepares the overlays)
- ARC Kernel identity (Phase 3)

## Order of work
1. Native-res boot animation render (1440×2560)
2. Fonts pack + fonts.xml mapping
3. Wallpaper set sourced and cropped
4. Cobalt theme overlay (framework + SystemUI)
5. Original sound set
6. Glyph set
7. Suite apps packaged (Launcher default home, Messaging)
8. Zip assembly + install script
9. Flash-test on the Phase 1-verified baseline; fix; verified on the
   phone → **MK1**; then merge into the ROM tree

## Dependency
Execution waits on **Phase 1** (Razer Phone 2 in hand, baseline
flashed and hardware-verified). Planning and asset work can run ahead
of it — the boot animation already has.

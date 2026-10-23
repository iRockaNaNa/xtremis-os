# Boot animation

A Nanatech Creative Solutions project.

Windows 10 Mobile-style boot animation for Xtremis OS: the four-pane
window logo fades in on black, then holds with the classic rotating dot
chase underneath until boot completes.

- `generate_bootanimation.py` — the generator (Python + Pillow). Run it
  to rebuild `bootanimation.zip` and the raw frames.
- Spec: 720×1280 @ 30 fps, `part0` (intro, plays once) + `part1` (dot
  chase, loops). The zip is stored uncompressed, as Android requires.
  Android scales the frames to the Razer Phone 2's 1440×2560 panel.
- Install (Phase 2 theme pack): the chosen zip ships as
  `/system/media/bootanimation.zip` in the ROM/theme package.
- **Decision 2026-10-23:** the arc-reactor animation
  (`bootanimation-arc.zip`, generator `generate_reactor_bootanimation.py`)
  is the default — reactor powering up over a Pixel-style
  "powered by android" footer. The Windows-logo animation above is
  parked for later MK releases.
- Note: the frames, zips and footer artwork (`assets/`) are binary, so
  they live outside git — the generator scripts in this folder are the
  source of truth and rebuild the animations exactly (footer art is
  re-supplied from the project's local asset store).

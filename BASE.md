# Xtremis OS — Base

A Nanatech Creative Solutions project.

## The pin

**LineageOS 22.2 (Android 15)** for the Razer Phone 2 (`aura`).

## Why this base

- `aura` is on LineageOS's official support list, and 22.2 is the
  current, actively maintained branch for it — the device tree saw
  commits as recently as September 2026.
- All three pieces line up on the same branch:
  - Device tree: `LineageOS/android_device_razer_aura`
  - Kernel: `LineageOS/android_kernel_razer_sdm845`
  - Vendor blobs: `TheMuppets/proprietary_vendor_razer_aura`
- The next branch (lineage-23.0, Android 16) exists only as a bring-up
  in progress. It is a watch item, not a base — Xtremis builds on the
  branch that is finished and supported.
- The LineageOS wiki lists no known issues for `aura` on this branch.

## What the base already gives us

- **Chroma RGB logo, fully supported.** The device settings (AuraParts)
  drive the logo's LP5523 controller: static color, spectrum and wave
  effects, a color picker, suspend on screen-off, and restore on boot.
  The Xtremis Settings redesign re-skins these controls — it must not
  remove them.
- **120 Hz display.** The panel runs at 120 Hz; the base ships no
  refresh-rate controls, so none need preserving.
- **Unlockable bootloader** with factory images available (below),
  which is what makes the recovery path in PLAN.md possible.

## Flashing notes (from the LineageOS wiki and Razer)

- Unlock flow: enable OEM unlocking in Developer options, then
  `fastboot flashing unlock`.
- A **full factory restore** additionally needs
  `fastboot flashing unlock_critical`.
- **Do not flash with the USB-C cable from the phone's box** — it is
  charge-only. Use a USB 3 A-to-C cable.
- Factory images live on the Razer Developer Portal; the latest stock
  is Android 9.0 Global (9.0-SMR7). Caution: the SMR7 download has been
  reported to actually serve the older MR6 build — **verify the
  SHA-256 hash of any factory image before flashing it.**

## Retest on hardware (Phase 1)

Old bug reports from the LineageOS 18.1 era — flashlight not working,
the camera picking the wrong lens, quiet audio, video playback
lock-ups — are unverified on 22.2. They are not assumed fixed or
assumed broken; Phase 1 tests each one on the real phone before any
theme work is judged against the baseline.

## Sources

LineageOS wiki (`aura` device page and build guide), the LineageOS
GitHub organization, and the Razer Developer Portal — researched
October 2026.

# Xtremis OS — Build Plan

A Nanatech Creative Solutions project.
Target: Razer Phone 2 (`aura`) · Base: LineageOS 22.2 · Reference: HP
Elite x3 (Windows 10 Mobile 1709)

## Build numbering

Releases are MK1, MK2, MK3… A build earns its MK number only after it
has been verified on the real phone.

## Phase 0 — Preparation

- [x] Xtremis OS repository created.
- [ ] Base pinned and documented: LineageOS 22.2 (Android 15) for
      `aura`, the officially supported, actively maintained branch.
- [ ] Build machine prepared (WSL2 Ubuntu) and a completely stock
      LineageOS build completed — the known-good baseline.
- [ ] Theme asset inventory: accents, icons, fonts, sounds and boot
      animation material collected for the theme work.
- [ ] HP Elite x3 in hand as the visual reference device.

## Phase 1 — Baseline on hardware

- [ ] Bootloader unlocked; stock LineageOS flashed.
- [ ] Core hardware verified: calls, SMS, camera, Wi-Fi, Bluetooth,
      fingerprint, 120 Hz display, Chroma logo.
- [ ] Factory-image recovery path tested (brick insurance).

## Phase 2 — Theme pack

- [ ] Flashable theme package: fonts, boot animation, wallpapers,
      system sounds, icon pack, accent colors.
- [ ] Metro 10 Launcher as default home; Metro 10 Messaging
      preinstalled.
- [ ] Verified on the phone → **MK1**.

## Phase 3 — Full ROM

- [ ] Framework, SystemUI and Settings restyled to Windows 10 Mobile.
- [ ] WP10 lock screen and navigation bar built into SystemUI.
- [ ] Metro 10 suite shipped as system apps.
- [ ] Verified on the phone → next MK release.

## Phase 4 — Polish & release

- [ ] Side-by-side fidelity pass against the Elite x3.
- [ ] Screenshots, flashing guide, public MK release.

## Working rules

- One phase at a time: finish, verify on hardware, then move on.
- Nothing is "done" from a compile alone — the phone decides.
- The stock recovery path stays tested and one command away at all
  times.

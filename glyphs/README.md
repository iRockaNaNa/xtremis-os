# System glyphs

A Nanatech Creative Solutions project.

Android vector drawables in the Windows 10 Mobile outline style —
thin strokes (2.2 on a 48 grid), drawn from the reference Settings
screenshot in `reference/`. Stroke color is white in the files; tint
at the use site (accent for Settings categories, white/accent for
Action Center states), exactly as W10M tints its glyphs.

## Sets

**Action Center** (`action-center/`) — the 7 quick-settings glyphs,
matching the toggles already wired in Metro 10 Launcher:
flashlight, bluetooth, wi-fi, do-not-disturb (crescent), airplane,
rotation lock, brightness.

**Settings** (`settings/`) — the top-level category glyphs from the
reference list: System (phone), Devices, Network & wireless (globe),
Personalization (display), Accounts (person), Time & language
(clock), Ease of Access, Privacy (padlock).

## Notes

- v1 geometry: clean geometric constructions, XML-validated. Final
  fidelity pass happens against the HP Elite x3 in Phase 1/2 device
  testing, like every other asset.
- Drop into the SystemUI / Settings overlay resource sets at
  packaging; names are ready (`ic_*`).

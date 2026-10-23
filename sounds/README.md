# Sounds

A Nanatech Creative Solutions project.

Two complementary sets — together they cover everything:

## 1. Authentic tone library — `authentic/` (owner-supplied)
The Lumia / Windows Phone stock tones, supplied by the project owner
as WMA and converted to OGG for Android. Provenance: the community
share linked from Microsoft's own Q&A — "Windows 10 Mobile System
Sounds for download" (learn.microsoft.com/answers/questions/2798536),
posted for personal use: **43 ringtones, 15
notifications, 2 alarms** — including Alert-01…10, the Lumia
Calendar/Clock/Email/Message/Voicemail set, and the Microsoft
Ringtone.

Defaults chosen for Xtremis:
- Ringtone: `ringtones/Microsoft_Ringtone.ogg`
- Notification: `notifications/Lumia_Message.ogg`
- Alarm: `alarms/Lumia_Clock.ogg`

These are Microsoft/Nokia material: **personal builds only**, never
in a public MK zip (same rule as the font and wallpapers).

## 2. Original synthesized set — `ui/`, `notifications/`
WP-style sounds synthesized from scratch for this project (no
samples): Lock, Unlock, Keypress (standard/space/delete/return),
Effect_Tick, camera_click, VideoRecord, plus XtremisNotify and
XtremisAlert. The authentic library has no UI sounds — WP kept those
elsewhere in the firmware — so this set covers UI in *both* build
types, and serves as the complete public-release sound set.

## Install (at packaging)
- `authentic/ringtones` → `/system/media/audio/ringtones/`
- `authentic/notifications`, `notifications/` → `/system/media/audio/notifications/`
- `authentic/alarms` → `/system/media/audio/alarms/`
- `ui/` → `/system/media/audio/ui/` (AOSP file names, drop-in)
- Defaults wired via framework config / Settings defaults at ROM
  integration time.

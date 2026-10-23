# Fonts

A Nanatech Creative Solutions project.

System typeface for Xtremis OS: **Noto Sans** (Google) — the free,
open-license stand-in for Segoe UI (see ASSETS.md font decision). The
genuine Windows font is owner-supplied for personal builds only and is
never in this folder or any public zip.

## Contents

Eight static TTFs (genuine Google Noto Sans):

| File | Weight | WP-style usage |
|---|---|---|
| NotoSans-Light.ttf | 300 | Large headings, lock-screen clock |
| NotoSans-Regular.ttf | 400 | Body text |
| NotoSans-Italic.ttf | 400 italic | Body italic |
| NotoSans-Medium.ttf | 500 | Emphasis, tile labels |
| NotoSans-SemiBold.ttf | 600 | Strong emphasis |
| NotoSans-Bold.ttf | 700 | Headlines, buttons |
| NotoSans-BoldItalic.ttf | 700 italic | Headline italic |
| NotoSans-Black.ttf | 900 | Display weight |

`fonts-xtremis.xml` — the Android family definitions for these files.

## Install (at theme-pack packaging)

1. Copy the TTFs to `/system/fonts/`.
2. Merge the families from `fonts-xtremis.xml` into the baseline's
   `/system/etc/fonts.xml`, replacing its Latin `sans-serif`,
   `sans-serif-light`, and `sans-serif-medium` families. Keep the
   baseline's fallback sections untouched — they carry other scripts
   and emoji.

## License

Noto Sans is © Google, licensed under the SIL Open Font License 1.1 —
free to bundle and redistribute, which is exactly why it ships and
Segoe UI does not.

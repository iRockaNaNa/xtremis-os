# Xtremis OS — Theme Asset Inventory

A Nanatech Creative Solutions project.

What the Metro 10 Launcher already defines, collected in one place so the
Xtremis OS ROM theme reuses exactly these values instead of reinventing
them. Every group cites its source file in the launcher tree
(`app/src/main/java/com/metrolauncher/…` unless noted). Items the ROM
needs that do not exist yet are marked **GAP**.

## 1. Accent palette

The full palette is the 20 authentic Windows Phone 8.1 accent colors,
defined in `data/AccentColor.kt`:

| Name | Hex |
|---|---|
| lime | #A4C400 |
| green | #60A917 |
| emerald | #008A00 |
| teal | #00ABA9 |
| cyan | #1BA1E2 |
| cobalt | #0050EF |
| indigo | #6A00FF |
| violet | #AA00FF |
| pink | #F472D0 |
| magenta | #D80073 |
| crimson | #A20025 |
| red | #E51400 |
| orange | #FA6800 |
| amber | #F0A30A |
| yellow | #E3C800 |
| brown | #825A2C |
| olive | #6D8764 |
| steel | #647687 |
| mauve | #76608A |
| taupe | #87794E |

Companion rules (`data/LauncherPreferences.kt`, `ui/theme/Theme.kt`):

- **Default accent: cobalt (#0050EF).**
- **Default theme: dark** — surface and background are pure black
  (#000000), text white. The light scheme inverts to white background,
  black text. In both schemes the Material `primary`, `secondary` and
  `tertiary` are all set to the single chosen accent — one accent drives
  everything, as on Windows Phone.
- **Per-tile accent override exists**: any tile can carry its own accent
  from the same palette instead of the global one
  (`data/PinnedTile.kt`, `PinnedTile.resolveColor` in
  `ui/start/MetroTile.kt`). The ROM's Start should keep this behavior.
- The XML theme under it all is a placeholder only
  (`res/values/themes.xml`): black window background, black status bar,
  black navigation bar. All real theming is in Compose.

Cross-check — Metro 10 Messaging (`../metro-messaging`, package
`com.metromessaging`, `MainActivity.kt`) hard-codes its own values and
they do **not** match the launcher yet: accent **#0078D7** (the Windows
10 desktop blue, not cobalt), background #000000, text #FFFFFF, muted
text #9E9E9E, read-conversation tile #3B3B3B. Unifying the suite on the
palette above is pending work the ROM should finish.

## 2. Typography

Font choices are defined in `data/LauncherFont.kt`; the picker offers
five options:

| Option | Notes |
|---|---|
| Segoe | "Windows 10 Mobile style" — **the default** |
| Roboto | Android system sans-serif |
| Monospace | Terminal feel |
| Serif | Editorial look |
| Rounded | Soft, friendly curves |

How they resolve today (`ui/theme/Type.kt`): **no font files are
bundled.** Each option maps to a built-in Android `FontFamily` stand-in —
Segoe → `FontFamily.Default`, Roboto → `FontFamily.SansSerif`, Monospace
→ `FontFamily.Monospace`, Serif → `FontFamily.Serif`, Rounded →
`FontFamily.Cursive` (flagged in a code comment as a placeholder for a
real rounded font such as Quicksand/Nunito). The chosen family is applied
to every Material 3 text style (`Typography.withFontFamily`).

**GAP (partial):** a real bundled Segoe UI (or Segoe-like) typeface.
`res/` contains no `font/` directory. The ROM needs the actual font
files to make system-wide type authentic; the launcher's own code
comments name bundling fonts under `res/font/` as the intended next
step.

## 3. Iconography

Icon treatment is a user setting with three styles
(`data/IconStyle.kt`, rendering in `TileFront` in
`ui/start/MetroTile.kt`). **Default: Metro glyphs.**

| Style | Rendering |
|---|---|
| Metro glyphs | The app icon is tinted pure white and drawn centered at 55% of the tile — a white pictogram on the accent-colored tile, the classic Windows Phone look. |
| Modern rounded | The original, full-color app icon, at 72% of the tile, inside a white (92% opacity) container with 24dp corner radius and 8dp padding. The tile itself also gets a 12dp corner radius. |
| Mono outline | The app icon tinted white at 85% opacity/alpha, centered at 50% of the tile. |

Supporting details:

- **Corners:** tiles are sharp-cornered (0dp radius) in every style
  except Modern rounded (12dp). Sharp corners are the Metro norm.
- **Icon source:** there is no icon pack and no bundled glyph set. Icons
  are the installed apps' own icons, fetched live from PackageManager
  and rasterized (`data/LauncherRepository.kt`, `util/DrawableExt.kt`).
  The ROM will need real WP10-style glyphs for its own system apps —
  tinting arbitrary icons white only works as a launcher trick (see
  Gaps).
- **Fallback:** if an icon can't be resolved, the tile shows the app's
  first letter, uppercased, in `headlineLarge`.
- **Label:** every tile face carries the app name bottom-left in 12sp
  white, padding 8dp start / 6dp bottom — the Windows Phone signature.
- **Only bundled drawable:** the app icon itself,
  `res/drawable/ic_launcher_tile.xml` — a vector: cobalt #0050EF square
  with a white 2×2 tile-grid mark (four white squares). This is the
  natural seed for the Xtremis logo/boot mark.

## 4. Sounds

**GAP.** The launcher bundles no sounds of any kind — no `res/raw/`, no
ringtone, notification, or UI sound files, and no sound references
anywhere in the code. Windows 10 Mobile system sounds (notification
chimes, keyboard, lock/unlock, camera shutter) all have to be sourced
or produced for the ROM.

## 5. Wallpapers & imagery

- **No bundled wallpapers.** There is no wallpaper file, setting, or
  picker anywhere in the launcher. The Start background is simply the
  theme background: pure black in the default dark theme, white in the
  light theme (`ui/theme/Theme.kt`).
- **Lock-screen imagery: GAP.** The launcher has no lock screen (on
  Xtremis that is SystemUI work), so there is no lock-screen photo or
  artwork asset to reuse.
- **Live photo imagery:** the one real imagery pipeline is the Photos
  live tile (`data/LiveTileProviders.kt`, `ui/start/LiveTileFaces.kt`):
  up to **24 most recent photos** from the device MediaStore, shown
  full-bleed with `ContentScale.Crop`, advancing every **10 seconds**,
  with a 44dp-tall bottom scrim so the tile label stays readable. This
  is the model for the ROM's lock-screen photo rotation.

## 6. Motion

The numbers that define the launcher's feel
(`ui/start/MetroTile.kt` unless noted):

- **Tile flip:** 3D `rotationY` flip, 0° ↔ 180°, **600 ms** tween
  (Compose default easing — no custom curve is specified),
  `cameraDistance = 12 × density` to keep the flip from distorting.
  The back face is counter-rotated 180° so its content reads correctly.
- **Flip cadence:** non-live medium/wide tiles flip decoratively every
  **4,500 ms**; tiles with live mode on flip every **10,000 ms**. Small
  (1×1) tiles never flip.
- **Clock face:** content re-renders on the minute boundary (delay to
  the next minute + 250 ms), never per-second.
- **Photos face:** advances to the next photo every 10,000 ms, in step
  with the flip.
- **Data refresh behind the faces:** calendar events every 15 minutes,
  weather every 30 minutes (also cached 30 minutes in
  `data/LiveTileProviders.kt`), Feed articles cached 30 minutes
  (`data/FeedContent.kt`).
- **Navigation gestures** (`MainActivity.kt`): horizontal swipe past
  **±120 px** switches panels (Start → app list on swipe-left, Start →
  Feed on swipe-right, back to Start from Feed on swipe-left); a
  **>90 px** pull from the top edge on Start opens the Action Center.
  Panel switches are state changes, not animated transitions — the ROM
  should note the *gestures* are the spec; transition animation is
  still open.

## 7. Tile system defaults

Grid and sizes (`data/TileSize.kt`, `ui/start/StartScreen.kt`):

- **Grid: 4 columns**, content padding 12dp, gaps 8dp horizontal and
  8dp vertical, vertically scrolling.
- **Sizes:** small 1×1, medium 2×2, wide 4×2 (columns × rows); tile
  aspect ratio is taken straight from the size.
- Tiles support per-tile size change, per-tile accent override, and a
  per-tile live-mode toggle (long-press edit flow,
  `ui/start/TileEditDialog.kt`). Live mode only takes effect on medium
  and wide tiles.

Out-of-box state (`MainActivity.kt`, `data/LauncherRepository.kt`,
`data/LauncherPreferences.kt`):

- **First run** is a "pick a look" step: choose dark/light and an
  accent, then the default Start layout is seeded.
- **Seeded layout** (only apps actually installed are pinned; capped at
  8 tiles): the built-in **Clock live tile (wide, live on)** first, then
  Phone (medium), Messaging (medium), Camera (medium), Browser (wide),
  Settings (small), Contacts (small).
- **Setting defaults:** dark theme on, accent cobalt, font Segoe, icon
  style Metro glyphs.
- **Built-in live tiles** (`data/LiveTileContent.kt`) ship as synthetic
  tiles that can be pinned like apps: Clock (time face / date face),
  Calendar (next 3 events over the coming 7 days), Weather (current
  conditions / today's high-low), Photos (recent-photo cycle). On the
  ROM these become the system Clock/Calendar/Weather/Photos tiles.

## 8. Gaps for the ROM

Theme assets Xtremis needs that the launcher does not have:

- **GAP — Boot animation frames.** Nothing exists: no Tiles-style boot
  animation, no boot logo beyond the seed in the launcher's app-icon
  vector (Section 3).
- **GAP — System sounds.** Ringtones, notification sounds, and UI
  sounds are entirely absent (Section 4).
- **GAP — Bundled Segoe typeface.** Only built-in font stand-ins exist
  (Section 2); real font files are required for system-wide use.
- **GAP — Wallpaper set and lock-screen imagery.** No bundled
  wallpapers and no lock-screen artwork (Section 5).
- **GAP — System glyph set.** WP10-style white glyphs for the ROM's own
  system apps (Phone, Messaging, Settings, Camera…) — the launcher
  never needed any because it tints other apps' icons (Section 3).
- **GAP — Suite accent sync.** Metro 10 Messaging's hard-coded #0078D7
  accent family must be unified with the Section 1 palette before the
  suite ships as system apps.

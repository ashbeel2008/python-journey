# Premiere Pro 2019 on a 6 GB Laptop

This is the daily workflow. Follow it and Premiere behaves. Ignore it and you'll fight the machine.

Your machine: **i5-4210U (2 cores), 6 GB RAM, Intel HD, SSD, ~59 GB free.**

---

## The four rules that matter

1. **Software Only renderer.** Never GPU acceleration on Intel HD.
2. **Playback resolution 1/4 or 1/8.** Preview only — export is unaffected.
3. **Keep clips short.** 15–90 seconds. Long timelines are where low-RAM machines die.
4. **Close Chrome before editing.** A browser eats 1–2 GB you don't have.

---

## Project template (set this up once)

Make a project called `TEMPLATE.pcpro` with:
- `1080x1920_30` sequence (vertical)
- `1920x1080_30` sequence (horizontal)
- Bin structure: `01_Footage`, `02_Audio`, `03_Graphics`, `04_Exports`
- Your title style saved as a **Motion Graphics Template** (Essential Graphics → Export as .mogrt)

Then `File → Save As` a copy for each new client. You never rebuild from scratch.

---

## Import and organize

1. `Ctrl + I` → select your Rewind exports.
2. Put them in `01_Footage`.
3. Rename clips to something readable (`funny_moment_01.mp4`), not `Rewind_2026-11-02_18-44.mp4`.
4. **Never move the source files after importing.** Premiere links by path. If you must move
   them, use `File → Project Manager → Consolidate`.

---

## Cropping horizontal footage to vertical

Your sequence is 1080×1920. Your footage is 1920×1080.

1. Drag the clip onto the timeline.
2. Right-click → **Set to Frame Size** (this fits it inside, with black bars).
3. In **Effect Controls → Motion → Scale**, type **178%**.
4. Adjust **Position** so the character/crosshair is centered.
5. If the subject moves, use **keyframes** on Position to follow them.

**178%** is the number that makes 16:9 footage fill a 9:16 frame. On 1080p source it's still
sharp enough for phones.

> Alternative: export vertical 1080×1920 straight from Rewind and skip this. Less control, fewer
> steps. Try both and pick what you like.

---

## Proxies (use these for anything over ~90 seconds)

Proxies are low-resolution stand-ins. Premiere edits the light file and swaps in the full-quality
one at export.

1. Select clips in the Project panel.
2. Right-click → **Proxy → Create Proxies**.
3. Format: **H.264**. Preset: **HD 720p 29.97** (or 540p if available).
4. Destination: **Next to original**.
5. Wait. On this CPU it's slow — do it once, then make coffee.
6. Toggle: right-click clip → **Proxy → Toggle Proxies**, or the **Toggle Proxies** button in the
   Program Monitor.

For 30-second clips, you can usually skip proxies and just use 1/8 playback resolution.

---

## Editing hotkeys you'll actually use

| Action | Shortcut |
|--------|----------|
| Import | `Ctrl + I` |
| Razor / cut | `Ctrl + K` |
| Selection tool | `V` |
| Ripple delete | `Shift + Delete` |
| Add edit to all tracks | `Ctrl + Shift + K` |
| Export media | `Ctrl + M` |
| Save | `Ctrl + S` |
| Undo | `Ctrl + Z` |
| Zoom to sequence | `\` |
| Add marker | `M` |

Learn 6 of these. You don't need the rest.

---

## Captions (Premiere 2019 has no auto-captions)

This is the biggest annoyance. Options, cheapest first:

1. **Manual captions** in Premiere: Type tool → create text → copy/paste per line. Slow but free.
2. **Essential Graphics templates** for consistent caption styling.
3. **Free SRT generation** — I can set up a local Whisper script on your machine (Python is already
   installed). You record → it writes an `.srt` → you import it in Premiere and style it. This is
   the fastest long-term option. Ask me when you're ready.

**Caption rules for Shorts:**
- 2–4 words per line
- Bold, high contrast, white with a dark outline or box
- Keep them inside the middle 60% of the frame (platform UI covers the edges)
- One idea per caption, synced to the cut

---

## Effects to avoid on this machine

These will make your timeline crawl:

- Warp Stabilizer
- Heavy Lumetri Color stacks (one basic correction is fine)
- Multiple nested sequences
- 4K footage, 60fps timelines
- Motion blur, glows, particle effects
- Several .mogrt templates layered at once

Minecraft Shorts don't need them. Cuts, text, zoom, sound effects, and music are enough.

---

## Export settings (Shorts)

`Ctrl + M` → **Format: H.264**

| Setting | Value |
|---------|-------|
| Preset | Match Source – High Bitrate |
| Resolution | **1080 × 1920** |
| Frame Rate | **30** |
| Bitrate | **VBR, 2-pass**, target **10 Mbps**, max **15** |
| Profile | High |
| Level | 4.1 |
| Audio | AAC, **320 kbps**, 48 kHz |
| Use Maximum Render Quality | **Off** (slower, no visible gain here) |
| Use Previews | On, if you rendered the timeline |

Export to `04_Exports`, name it `Client_Project_YYYYMMDD_v1.mp4`.

---

## If Premiere + footage live on an external SSD

- Use a **direct USB 3 port** (usually blue). Not a hub, not a USB 2 port — USB 2 caps at
  ~40 MB/s and will make 1080p editing feel broken.
- Keep the **project file and footage on the same drive**, so Premiere isn't jumping between disks.
- **Never unplug the drive while Premiere is open.** Eject it first.
- Keep the **drive letter stable** — plug into the same port. If it changes from E: to F:, every
  project goes offline.
- Put **media cache on the internal C:** drive, not on the same drive as the footage. Reading and
  writing one disk at once slows both down.
- Leave **25–30 GB free** on that drive. Below 10 GB, exports start failing.

---

## Weekly maintenance (5 minutes)

1. `Edit → Preferences → Media → Delete` next to **Media Cache Files**.
2. Delete old Rewind exports you've already used.
3. Empty the Recycle Bin.
4. Check C: has **20+ GB free**.
5. Save a backup copy of the project file to Google Drive.

---

## When it crashes (it will)

1. Reopen. Premiere auto-saves every 5 minutes — accept the recovery.
2. If a specific clip crashes it, re-export that clip from Rewind at **720p**.
3. If export fails repeatedly, export a **720p** version first, then a 1080p one.
4. If Premiere becomes unusable, don't switch software mid-project. Finish at 720p, then reassess.

---

## The honest limit

This laptop can do **30–90 second Minecraft Shorts** comfortably once set up. It will struggle
with 10-minute videos and multiple effects layers. That's fine — your business is Shorts first.

When you're earning, the upgrade order is:
1. **RAM to 12–16 GB** (biggest win, cheapest)
2. External SSD for media
3. A newer laptop

Don't buy anything until a client is paying you.

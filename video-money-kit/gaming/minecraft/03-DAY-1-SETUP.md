# Day 1 — Setup: Rewind + Premiere Pro 2019

Your stack: **Lunar Client Rewind** to record → **Premiere Pro 2019** to edit.

No OBS. No CapCut. Ignore the old setup file if you saw it.

---

## Read this first: the hardware reality

Premiere Pro 2019 officially wants **8 GB RAM minimum**. You have **6 GB**.

It will run, but only if you follow the low-end rules. The two things that save you:

1. **Your C: drive is an SSD** — good. Premiere leans on it hard.
2. **Proxies + low playback resolution** — this is what keeps the timeline from freezing.

If you skip `04-PREMIERE-LOW-END.md`, you will think Premiere is broken. It isn't. It's just
starved for RAM.

---

## 1. Install Premiere Pro 2019

1. Run the installer you have. Use the official Adobe installer if possible.
2. Install to the default location on **C:** (your SSD).
3. Launch it once and sign in.
4. If it warns about your graphics driver, ignore it for now — we're using software rendering.

> **Premiere 2019 does not have auto-captions.** That feature came later. You'll do captions
> manually (or with a free tool I can set up later). Don't waste an hour looking for the button.

---

## 2. First-run settings (do these before any project)

### Renderer → Software Only
`File → Project Settings → General → Renderer` → **Mercury Playback Engine Software Only**

The Intel HD GPU is not strong enough to help, and OpenCL acceleration often crashes on this
hardware. Software Only is slower but stable.

### Media cache → controlled folder
`Edit → Preferences → Media`
- **Media Cache Files:** `C:\PremiereCache`
- Check **"Delete media cache files older than 30 days"**

Premiere's cache can eat 10–20 GB without asking. On a 59 GB-free drive, that matters.

### Auto-save
`Edit → Preferences → Auto Save` → every **5 minutes**, keep **20** versions.

On a low-end machine, crashes happen. Auto-save is your seatbelt.

### Playback resolution
Open the Program Monitor → **wrench/settings icon → Playback Resolution → 1/4**.
Drop to **1/8** if it still stutters. This only affects preview, not the export.

---

## 3. Create your project and sequence

### Project
`File → New → Project`
- Name: `MC_Shorts_2026`
- Location: `C:\Video\Projects\`
- Scratch Disks: **Same as Project**

### Sequence (vertical Shorts)
`File → New → Sequence → Settings` tab:

| Setting | Value |
|---------|-------|
| Editing Mode | **Custom** |
| Frame Size | **1080** horizontal × **1920** vertical |
| Pixel Aspect Ratio | **Square Pixels** |
| Frame Rate | **30.00** |
| Fields | **No Fields (Progressive Scan)** |
| Display Format | Timecode |

Name it `1080x1920_30`.

### Sequence (horizontal, for trailers/long)
Same, but **1920 × 1080**.

---

## 4. Rewind recording settings

### Recording
- **`Shift + R`** to start/stop a Rewind
- Turn on **Record Microphone** and **Record System Audio** in Rewind settings
- Set a **marker hotkey** — mark moments while playing so you don't scrub for 20 minutes later
- Enable **Shadow Rewind** (saves the last 15–60 seconds when something happens and you forgot
  to record)

### Export from Rewind
Open the Rewind Editor → **Export** tab:
- **File Format:** MP4
- **Codec:** H.264
- **Resolution:** **1920×1080** (drop to **1280×720** if export is slow)
- **Frame Rate:** **30**
- **Audio:** AAC, 48 kHz

Export **only the section you need**. A 3-minute clip is easy. A 40-minute VOD is pain.

### Vertical shortcut
Rewind's project settings include **orientation**. If you export **1080×1920** directly, you skip
the crop step in Premiere. The trade-off: less control over framing.

**Recommended:** export **1920×1080** and crop in Premiere. You can always reframe a horizontal
clip; you can't recover what a vertical crop cut off.

---

## 5. Test the whole pipeline (20 minutes, do not skip)

1. Record **2 minutes** of Minecraft with Rewind.
2. Export it from Rewind as **1080p / 30fps / H.264 MP4**.
3. Open Premiere → new project → new `1080x1920_30` sequence.
4. Import the MP4 (`Ctrl + I`).
5. Drag it onto the timeline.
6. Right-click the clip → **Set to Frame Size**.
7. In **Effect Controls**, set **Scale** to about **178%** and reposition so the action is centered.
8. Add one text layer (`Ctrl + T` or the Type tool).
9. Export: `Ctrl + M` → Format **H.264** → Preset **Match Source – High Bitrate** →
   Resolution **1080×1920**, 30 fps, **VBR 2-pass, target 10 Mbps, max 15**.
10. Play the exported file on your phone.

If that works, you're set up. If not, check the table below.

---

## 6. Troubleshooting

| Problem | Fix |
|---------|-----|
| Premiere won't launch / crashes on open | Run as administrator; update Intel HD driver; disable GPU in Project Settings |
| Playback stutters | Playback resolution **1/8**, close Chrome/Discord, create proxies |
| "Media Offline" | You moved the file after importing. Keep media in one folder. |
| Export fails at 99% | Free 20 GB, clear media cache, export to a different folder |
| Export is very slow | Turn off "Use Maximum Render Quality"; try Hardware Encoding; export 720p |
| Audio out of sync | Make sure Rewind exported **30fps constant**, not variable |
| Premiere eats all RAM | Close everything else. 6 GB is the floor; see upgrade note. |
| Timeline turns red/yellow | Red = needs rendering. `Sequence → Render In to Out`. |

---

## 7. The one hardware upgrade worth doing

Your laptop has **two RAM slots**: a **4 GB** and a **2 GB** stick, both **DDR3L-1600**.

- Cheapest fix: replace the **2 GB** stick with an **8 GB DDR3L-1600 SODIMM** → **12 GB total**.
- Better: two **8 GB** sticks → **16 GB** (your CPU supports it).
- Cost is usually small for used DDR3L. This is the single biggest speed-up for Premiere.

Do it only when you have your first paid client or two. You don't need it to start.

---

## Checkpoint

- [ ] Premiere 2019 installed and opens
- [ ] Renderer set to **Software Only**
- [ ] Media cache set to `C:\PremiereCache`
- [ ] `1080x1920_30` sequence created
- [ ] One Rewind clip exported and edited in Premiere
- [ ] One vertical MP4 exported and played on your phone
- [ ] 20+ GB free on C:

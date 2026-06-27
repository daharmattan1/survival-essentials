---
entry_id: public-domain-id-image-sources
title: Public-Domain ID Image Sources — Where Real Deadly-Pair Photos Come From
type: METHOD
domain: substrate/10_key_resources
region_scope: universal
usda_zone: n/a
confidence: high
source_tier: T1
method_for: locate trusted public-domain and CC0 identification images for plant, mushroom, and game animal confirmation
materials:
  - Internet access (during prep phase; captured/archived offline)
  - Computer or phone
  - Local storage for downloaded images (Ziploc bag + printed photos, or offline device)
difficulty: easy
sources:
  - title: "Biodiversity Heritage Library (BHL)"
    publisher: "BHL Consortium (public archives)"
    url: "https://www.biodiversitylibrary.org/"
    tier: T1
  - title: "USDA PLANTS Database"
    publisher: "USDA Natural Resources Conservation Service"
    url: "https://plants.usda.gov/"
    tier: T1
  - title: "USDA Weed Images"
    publisher: "USDA National Agricultural Library"
    url: "https://data.nal.usda.gov/dataset/weed-images-source-images-weeds-and-weed-management-agriculture"
    tier: T1
  - title: "Wikimedia Commons — Edible Plants & Mushrooms"
    publisher: "Wikimedia Foundation"
    url: "https://commons.wikimedia.org/wiki/Category:Edible_plants"
    tier: T1
  - title: "iNaturalist (CC0 filter)"
    publisher: "California Academy of Sciences / iNaturalist"
    url: "https://www.inaturalist.org/"
    tier: T1
  - title: "Mushroom Observer"
    publisher: "Mushroom Observer Collaborative"
    url: "https://mushroomobserver.org/"
    tier: T2
last_reviewed: 2026-06-27
review_status: reviewed
---

## Goal & When To Use

This entry points to the **legitimate public-domain and CC0 sources** where real ID photos live. During the prep phase (calm, with power, with internet), you:

1. Find deadly-pair photos (morel vs. false morel, wild onion vs. death camas, etc.).
2. Verify the license (public domain or CC0).
3. Download and archive them (or print + laminate for field reference).
4. Catalog them in this repo's `_media/SOURCES.md`.

**The critical rule:** Images are **supporting evidence, never sufficient for ID**. A photo alone can kill. This source list is for triangulation — combining field observation (morphology, habitat, season) WITH reference photos WITH the positive-ID checklist in the substrate entries.

---

## Steps

### 1. Search the Primary PD/CC0 Sources

**Biodiversity Heritage Library (BHL)** — highest-quality, detailed botanical illustrations:
- URL: https://www.biodiversitylibrary.org/
- Search by binomial (e.g., "Morchella esculenta") or common name.
- Filter to **books with public-domain illustrations** (most BHL content is PD, published 1850–1920s).
- Look for **multiple growth stages** (cross-section, underside, whole organism) in one source.
- Example: search "Morchella" → *Edible and Poisonous Mushrooms* (1899) → color plates showing cap, gills, stem, spore print.

**USDA PLANTS Database**:
- URL: https://plants.usda.gov/
- Search by binomial (e.g., "Allium tricoccum" — wild leek).
- Select "Photos" tab; all USDA photos are public domain (U.S. gov work).
- Shows habitat context (soil, companion plants, growth stage).
- Good for confirming leaf shape, growth habit, and natural range.

**USDA Weed Images**:
- URL: https://data.nal.usda.gov/dataset/weed-images-source-images-weeds-and-weed-management-agriculture
- Focus: common wild edibles that resemble weeds (dandelion, plantain, clover, amaranth).
- Public domain; all angles shown (top, bottom, seed stage, mature).

**Wikimedia Commons (CC0/PD filter)**:
- URL: https://commons.wikimedia.org/
- Search by common name or binomial.
- **Critical:** check the license on EVERY image. Only download if marked:
  - "Public domain (PD)"
  - "CC0" (Creative Commons Zero — effectively PD)
- Skip "CC-BY" or "CC-SA" (require attribution).
- Multi-angle photos from modern photography (modern plant, not 100-year-old illustration).

**iNaturalist (CC0 subset)**:
- URL: https://www.inaturalist.org/
- Search species, filter by location (your region) to see current, real-world appearance.
- **Filter to CC0 license only** (use the license filter on the results page).
- Community IDs help validate (if ≥2 expert identifications agree, it's likely correct).
- Low-quality photos are useless; prioritize high-resolution, clear-angle shots.

**Mushroom Observer (regional societies)**:
- URL: https://mushroomobserver.org/
- Search by binomial; filter by region (e.g., "Eastern North America").
- Many are CC0; check license on each image.
- Links to regional mycological society IDs (expert confirmation).
- Spore print photos shown where available (critical for fungal ID).

### 2. Validate License Before Downloading

**Public Domain (PD):**
- U.S. government works (USDA, FEMA, CDC, etc.) — always PD.
- Published works before 1929 in the U.S. — PD.
- Published works marked "public domain" — use freely.

**Creative Commons Zero (CC0):**
- No attribution required; use freely.

**NOT acceptable:**
- CC-BY (requires attribution; acceptable but adds overhead).
- CC-SA (requires you to share derivatives under same license; avoid complexity).
- © Copyrighted (privately owned; don't use).

**Check the source:**
- On Wikimedia Commons, the license is shown at the bottom of the image page.
- On iNaturalist, click the photo → license shown in details.
- On USDA pages, text states "public domain."

### 3. Download & Archive for Offline Access

**During prep phase (with internet):**

Create a folder structure:
```
_media/photos/
├── deadly-pairs/
│   ├── morel-vs-false-morel/
│   │   ├── morchella-esculenta_whole_top.jpg
│   │   ├── morchella-esculenta_cross-section.jpg
│   │   ├── gyromitra-esculenta_whole_top.jpg
│   │   ├── gyromitra-esculenta_cross-section.jpg
│   │   └── SOURCES_morel_pair.txt (license + URL)
│   ├── wild-onion-vs-death-camas/
│   └── ...
├── field-reference/
│   ├── ramps_allium-tricoccum.jpg
│   └── ...
```

**For each image:**
1. Download the full-resolution version.
2. Create a text file alongside it with:
   ```
   filename: morchella-esculenta_whole_top.jpg
   URL: https://archive.org/details/[BHL_source]
   License: Public Domain
   Source: Biodiversity Heritage Library, Edible and Poisonous Mushrooms (1899)
   Attribution: [author/artist if listed]
   Downloaded: [date]
   ```
3. Store the folder on multiple devices (phone, offline laptop, USB stick, printed).

### 4. Print Deadly Pairs for Field Reference

**High-ROI laminated cards** (for your bag during foraging):

1. **Select the most reliable image pair** from your downloads (e.g., morel vs. false morel).
2. **Print side-by-side on card stock** (8.5" × 5.5" index card or larger).
3. **Include captions** (common name, binomial, key differences, hazard if misidentified).
4. **Laminate** at FedEx Office (~$0.50/card) or use a home laminator (~$30, one-time).
5. **Hole-punch and clip to your field pack**, or keep in a waterproof pocket.

Example card:
```
┌─────────────────────────────────────┐
│   MOREL vs. FALSE MOREL             │
├─────────────────────────────────────┤
│ [Photo A: true morel]  [Photo B: false morel]
│                                      │
│ Morel (Morchella esculenta):        │
│ • Hollow cap AND hollow stem        │
│ • Honeycomb ridges extend to top    │
│ • Gills: ridges run down from cap   │
│ • Season: Mar–May                   │
│                                      │
│ FALSE MOREL (Gyromitra esculenta):  │
│ • Hollow cap, SOLID/chambered stem  │
│ • Brain-like wrinkles (NOT ridges)  │
│ • Gills: NOT attached to stem       │
│ • ⚠ TOXIC: hydrazine, liver damage │
│                                      │
│ DO NOT EAT FALSE MOREL.             │
└─────────────────────────────────────┘
```

### 5. Log Every Image in This Repo

After downloading, add a row to [`../../_media/SOURCES.md`](../../../_media/SOURCES.md):

Example row:
```
| morchella-esculenta_whole_top.jpg | True morel (*Morchella esculenta*) whole fruiting body, top view | Biodiversity Heritage Library, *Edible and Poisonous Mushrooms* (1899) | Public Domain | Artist: [if listed]; source: BHL | Whole organism, top view, cap detail, honeycomb ridges visible |
```

---

## Failure Modes & Fixes

| Failure | Fix |
|---------|-----|
| **Downloaded image shows only one angle (top view)** | Discard; find another source showing underside, cross-section, and whole organism. A single angle is insufficient for ID. |
| **Image license is unclear (no license marked)** | Do NOT use. Contact the source site or assume copyrighted. Use a different image with clear PD/CC0 license. |
| **Wikimedia Commons photo looks similar but isn't the species you searched** | Verify the species name in the image details; user-uploaded photos sometimes have wrong IDs. Check expert comments ("Mushroom Observer IDs" or "Inaturalist community ID"). |
| **Printed laminated card becomes unreadable in field (wet, faded)** | Keep a color printout at home (backup reference) and check against the full entry in this repo. Laminated cards are field-quick, but the substrate entry is the full safety gate. |
| **You can't access the internet during prep to download** | Use your local library's WiFi or a friend's internet. Download and archive BEFORE the emergency. If you have no internet at all, acquire printed field guides from used bookstores (see physical-book-backup-layer entry). |
| **AI-generated images are mixed into search results (fake deadly pairs)** | They are. AI images often show hallucinated traits. **Always verify the source URL and license.** If you see an image on a non-official site (Reddit, Facebook, random blog), cross-check it against a T1/T2 reference (BHL, USDA, Wikimedia PD). When in doubt, don't download it. |

---

## Sources

- **Biodiversity Heritage Library** — https://www.biodiversitylibrary.org/ (150k+ PD botanical illustrations)
- **USDA PLANTS Database** — https://plants.usda.gov/ (PD photos + distribution, regional habitat)
- **USDA Weed Images** — USDA National Agricultural Library (PD, common wild edibles)
- **Wikimedia Commons (CC0 filter)** — https://commons.wikimedia.org/ (modern PD/CC0 photos, multi-angle)
- **iNaturalist (CC0 subset)** — https://www.inaturalist.org/ (contemporary photos, community ID verification, region filter)
- **Mushroom Observer** — https://mushroomobserver.org/ (regional society IDs, spore print photos, CC0 filter)
- **CONVENTIONS.md §8 (Imagery rules)** — [`../CONVENTIONS.md`](../../../CONVENTIONS.md) — the hard rule that images are supporting evidence never sufficient for ID
- **Media catalog** — [`../../_media/SOURCES.md`](../../../_media/SOURCES.md) (canonical log of all local images and their sources)
- **Survey** — [`../../10_key_resources.md`](../../../10_key_resources.md)

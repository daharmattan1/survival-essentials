# Mid-Atlantic / Appalachian — Biome Profile

> The first region pack. A **temperate deciduous forest** in **USDA hardiness zone 7a**, referenced
> to **Baltimore, Maryland** and the surrounding Piedmont → Appalachian gradient. This profile is the
> doorway to the biome's biology; for a food/consumption query go to
> [`food_hub.md`](food_hub.md), and for the calendar go to [`seasonality.md`](seasonality.md).
>
> Registry: [`../_index.md`](../_index.md). Layer model + retrieval recipes: [`../../AGENTS.md`](../../AGENTS.md).

This is life-safety content. Every consumption answer leads with the positive-ID gate and the
uncertainty, never a verdict (`../../CONVENTIONS.md` §9). **Positive ID or do not consume.**

---

## Biome at a glance

| Attribute | Value |
|-----------|-------|
| **USDA hardiness zone** | **7a** (avg. annual minimum ≈ 0 to 5 °F / −18 to −15 °C) |
| **Reference point** | Baltimore, MD (Piedmont), grading west into the Appalachian ridges |
| **Forest type** | Temperate **deciduous** (broadleaf), mixed oak-hickory; mesic cove hardwoods at elevation |
| **Last spring frost** | ≈ **mid-April** (Baltimore lowland; later at elevation) |
| **First fall frost** | ≈ **late October** (Baltimore lowland; earlier at elevation) |
| **Growing season** | ≈ 185–200 frost-free days in the lowland |
| **Elevation bands** | Coastal plain/Piedmont (~0–800 ft) → Blue Ridge/ridge-and-valley (~800–3,000+ ft) — higher = cooler, later spring, earlier fall, shifted fruiting |
| **Precipitation** | Humid; ~40–45 in/yr, fairly even — abundant surface water, but **all of it needs treatment** (see [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md)) |

**Dominant trees (anchor your foraging to these):** oak (*Quercus* — white & red groups), hickory
(*Carya*), maple (*Acer*), tulip poplar (*Liriodendron*), with beech, black walnut, and ash. Oak and
hickory matter most for food: acorns and hickory nuts are the calorie-dense fall mast, and many
choice edible mushrooms fruit *on* or *with* oak.

**Elevation matters for timing.** The same species fruits/ripens **later** as you climb and the
frost window **narrows** — treat every season window in this pack as the lowland (Baltimore) baseline
and shift later/earlier with elevation.

---

## What's in this pack

| Surface | File | Use |
|---------|------|-----|
| **Food decision hub** | [`food_hub.md`](food_hub.md) | "What can I eat here, and what could kill me?" — season-indexed; routes through the deadly-look-alike matrix + hazards first |
| **Seasonality calendar** | [`seasonality.md`](seasonality.md) | Month/season overview of foraging, hunting, and growing windows (orienting overview, **not** an ID source) |
| **Edible plants** | [`edible-plants/_index.md`](edible-plants/_index.md) | WILD-EDIBLE-PLANT entries — **deadly-twin matrix leads the index** |
| **Mushrooms** | [`mushrooms/_index.md`](mushrooms/_index.md) | MUSHROOM entries — **mushroom doctrine + deadly-look-alike matrix lead the index** (highest-consequence) |
| **Game animals** | [`game-animals/_index.md`](game-animals/_index.md) | GAME-ANIMAL entries — incl. white-tailed deer (full flow + CWD) |
| **Crops** | [`crops/_index.md`](crops/_index.md) | CROP entries — zone-7a planting/harvest windows |
| **Hazards** | [`hazards/_index.md`](hazards/_index.md) | HAZARD entries — venomous snakes, ticks/Lyme, toxic plants |

---

## Load order (this biome)

```
Food/consumption?  → food_hub.md  →  bio index (matrix/doctrine FIRST)  →  entry  →  cross-check hazards/
Just orienting?    → seasonality.md (what's roughly available now — NOT an ID source)
Hazard?            → hazards/_index.md
Always: positive ID or do not consume; for expert_id_required species refuse a field-ID-only "yes."
```

## `check_manifests` (biome level)

- [ ] `food_hub.md` and `seasonality.md` both exist and link the five biology subfolders.
- [ ] Each biology subfolder has an `_index.md` + an `entries/` dir.
- [ ] `mushrooms/_index.md` leads with the doctrine + deadly-look-alike matrix;
      `edible-plants/_index.md` leads with the deadly-twin matrix.
- [ ] Season windows are stated as the lowland (Baltimore, 7a) baseline with an elevation caveat.

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
| **Last spring frost** | Average **April 15 to 25** in zone 7a (Virginia Cooperative Extension, quoted in the [potato entry](crops/entries/potato.md)); later at elevation |
| **First fall frost** | Average **October 15 to 25** in zone 7a (same source); earlier at elevation |
| **Region covered** | Roughly Virginia, Maryland, West Virginia, Pennsylvania, Delaware, New Jersey and the southern Appalachians, USDA zones about 5b to 8a; Baltimore (7a) is the reference point for the calendar |
| **Elevation bands** | Coastal plain/Piedmont (~0–800 ft) → Blue Ridge/ridge-and-valley (~800–3,000+ ft) — higher = cooler, later spring, earlier fall, shifted fruiting |
| **Precipitation** | Humid; ~40–45 in/yr, fairly even — abundant surface water, but **all of it needs treatment** (see [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md)) |

**Dominant trees (anchor your foraging to these):** oak (*Quercus* — white & red groups), hickory
(*Carya*), maple (*Acer*), tulip poplar (*Liriodendron*), with beech, black walnut, and ash. Oak
matters most for food: [acorns](edible-plants/entries/acorn-oak.md) are the main wild calorie source the pack covers (they need
mandatory leaching and have a potentially fatal look-alike nut), and several mushroom entries name oak as a host or
neighbor ([hen-of-the-woods](mushrooms/entries/hen-of-the-woods-grifola.md),
[chicken-of-the-woods](mushrooms/entries/chicken-of-the-woods-laetiporus.md),
[lion's mane](mushrooms/entries/lions-mane-hericium.md), [black trumpet](mushrooms/entries/black-trumpet-craterellus.md)).
Naming a host tree identifies nothing: every mushroom needs an expert who has examined it in hand.

**Elevation matters for timing.** Fruit and nut entries say the same species ripens **later** higher
in the Appalachians (general practice; no opened source gives the size of the shift). Treat every season
window in this pack as the lowland (Baltimore) baseline.

---

## What's in this pack

| Surface | File | Use |
|---------|------|-----|
| **Food decision hub** | [`food_hub.md`](food_hub.md) | "What can I eat here, and what could kill me?" — season-indexed; routes through the deadly-look-alike matrix, the mushroom doctrine and hazards first |
| **Seasonality calendar** | [`seasonality.md`](seasonality.md) | Month/season overview of foraging, hunting, and growing windows (orienting overview, **not** an ID source) |
| **Edible plants (8)** | [`edible-plants/_index.md`](edible-plants/_index.md) | WILD-EDIBLE-PLANT entries — **look-alike matrix leads the index** (wild onion, acorn, cattail, black walnut, violet / chickweed, dandelion, pawpaw, wild blackberry / raspberry) |
| **Mushrooms (8)** | [`mushrooms/_index.md`](mushrooms/_index.md) | MUSHROOM entries — **9-point mushroom doctrine + deadly-look-alike matrix lead the index** (highest-consequence): morel, chicken-of-the-woods, oyster, chanterelle, wood ear / puffball, hen-of-the-woods, lion's mane, black trumpet |
| **Game animals (5)** | [`game-animals/_index.md`](game-animals/_index.md) | GAME-ANIMAL entries — white-tailed deer (full flow + CWD), rabbit, squirrel, wild turkey, raccoon / opossum |
| **Crops (7)** | [`crops/_index.md`](crops/_index.md) | CROP entries — zone-7a planting/harvest windows: potato, dry beans, winter squash, kale / collards, flint corn, garlic, sweet potato |
| **Hazards (6)** | [`hazards/_index.md`](hazards/_index.md) | HAZARD entries — amatoxin mushrooms, water hemlock, toxic plants (poison hemlock, poison ivy), rabies and wildlife bites, ticks and Lyme, venomous snakes |

**Total: 34 entries** (edible plants 8, mushrooms 8, game animals 5, crops 7, hazards 6).

---

## Load order (this biome)

```
Food/consumption?  → food_hub.md  →  bio index (matrix/doctrine FIRST)  →  entry  →  cross-check hazards/
Just orienting?    → seasonality.md (what's roughly available now — NOT an ID source)
Hazard?            → hazards/_index.md
Always: positive ID or do not consume; for expert_id_required species refuse a field-ID-only "yes."
```

## `check_manifests` (biome level)

- [x] `food_hub.md` and `seasonality.md` both exist and link the five biology subfolders.
- [x] Each biology subfolder has an `_index.md` + an `entries/` dir (34 entries in all).
- [x] `mushrooms/_index.md` leads with the doctrine + deadly-look-alike matrix;
      `edible-plants/_index.md` leads with the look-alike matrix.
- [x] Season windows are stated as the lowland (Baltimore, 7a) baseline with an elevation caveat.

# regional/_index.md — Region Registry

> The biology layer. **Region-bound knowledge** lives here — edible plants, mushrooms, game, crops,
> and local hazards — because **season, habitat, deadly look-alikes, and legality are biome
> variables.** Universal technique (water, fire, shelter, nav, comms, gear) lives in
> [`../substrate/_index.md`](../substrate/_index.md), not here.
>
> Start at [`../AGENTS.md`](../AGENTS.md) for the layer model and retrieval recipes. **This registry
> is where every food/consumption query pivots** (retrieval recipe A).

This is life-safety content. Consumption answers must lead with the positive-ID gate and the
uncertainty, never a verdict (`../CONVENTIONS.md` §9).

---

## How region packs extend the universal core

The universal `substrate/` answers "how do I disinfect water / build a fire / set a snare" — the same
everywhere. A **region pack** answers "what can I eat *here*, and what could kill me by mistake" —
which changes completely with geography. So each pack holds the biology for one biome, structured the
same way, and the universal core stays geography-free.

**The food pivot (do not skip):** the universal [`../substrate/05_food/_index.md`](../substrate/05_food/_index.md)
holds *technique only* and deliberately links **this registry**, not a specific biome. Every
consumption/ID query resolves:

```
../substrate/05_food/_index.md   (technique only — no edibility verdicts)
  → regional/_index.md           (THIS registry — pick the active biome)
    → <biome>/food_hub.md        (the season-indexed food DECISION surface)
      → edible-plants / mushrooms / game-animals / crops index  (DEADLY-LOOK-ALIKE MATRIX + DOCTRINE first)
      → cross-check <biome>/hazards/
    → CITE the specific entries
```

---

## Active regions

| Biome | Status | Zone | Reference point | Pack |
|-------|--------|------|-----------------|------|
| **Mid-Atlantic / Appalachian** | **active** | USDA 7a reference (region about 5b to 8a) | Baltimore, MD | [`mid-atlantic-appalachian/_index.md`](mid-atlantic-appalachian/_index.md) |
| **Northeast / New England** | **active** | USDA 5b at the reference point (region about 4b to 6b) | Concord, NH | [`northeast-new-england/_index.md`](northeast-new-england/_index.md) |

Coverage: **Mid-Atlantic / Appalachian** is about Virginia, Maryland, West Virginia, Pennsylvania, Delaware, New Jersey and the southern Appalachians; **Northeast / New England** is New Hampshire, Vermont, Maine, Massachusetts, Connecticut, Rhode Island and upstate and eastern New York. Elsewhere, no pack applies yet: use the universal survey and substrate, and never assume a pack's seasons or look-alikes hold outside its range.

**Mid-Atlantic / Appalachian is Victor's biome and the first pack built.** It is a temperate
deciduous forest in USDA zone 7a. Enter it through its biome profile
([`mid-atlantic-appalachian/_index.md`](mid-atlantic-appalachian/_index.md)) or, for a food query,
straight through its decision hub
([`mid-atlantic-appalachian/food_hub.md`](mid-atlantic-appalachian/food_hub.md)).

The **Northeast / New England** pack is the second one built: New Hampshire, Vermont, Maine, Massachusetts,
Connecticut, Rhode Island and upstate and eastern New York, referenced to Concord, NH (zone 5b on the USDA
2023 map). It has the same layout and a smaller set of entries, all `draft`. Enter it through its biome profile
([`northeast-new-england/_index.md`](northeast-new-england/_index.md)) or, for a food query, straight through
its decision hub ([`northeast-new-england/food_hub.md`](northeast-new-england/food_hub.md)). Amatoxin, rabies
and snake entries are not yet written for it; its hub points to the Mid-Atlantic entries for general facts.

**Entry counts.** Mid-Atlantic / Appalachian: **34 entries** (edible plants 8, mushrooms 8, game animals 5,
crops 7, hazards 6). Northeast / New England: **15 entries** (edible plants 3, mushrooms 3, hazards 3, game
animals 3, crops 3). Regional total: **49 entries**. Universal core in [`../substrate/`](../substrate/_index.md):
**67 entries**. Grand total: **116 entries**.

## Future biomes (later passes)

Additional biomes (e.g. desert Southwest, Pacific Northwest, northern boreal) will mirror this exact
layout — a biome `_index.md` profile, a `food_hub.md` decision surface, a `seasonality.md` calendar,
and the five biology subfolders (`edible-plants/`, `mushrooms/`, `game-animals/`, `crops/`,
`hazards/`). They are not built yet: region packs are hand-reviewed,
in-the-loop, never auto-generated at scale (the look-alike data is life-safety-critical).

---

## `check_manifests` (registry level)

- [ ] Every biome listed as "active" has a folder containing `_index.md`, `food_hub.md`,
      `seasonality.md`, and the five biology subfolders (each with `_index.md` + `entries/`).
- [ ] The food pivot from `../substrate/05_food/_index.md` lands here (registry), not on a biome.
- [ ] Each biology `_index.md` carries its deadly-look-alike matrix (and, for mushrooms, the
      doctrine) ahead of its manifest table.

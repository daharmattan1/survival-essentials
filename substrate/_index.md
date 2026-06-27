# substrate/_index.md — Master Manifest (Universal Technique)

> The top of the substrate. This is the **room a reasoning AI queries** for universal technique —
> the parts of survival that do **not** change with geography (water disinfection, fire, shelter,
> first-aid, navigation, comms, gear). Region-bound biology (what grows here, what could kill you by
> mistake, what is legal to hunt) lives in [`../regional/_index.md`](../regional/_index.md), not here.
>
> Start at [`../AGENTS.md`](../AGENTS.md) for the layer model, danger facets, retrieval recipes, and
> answer policy. **Load order is always: doctrine/matrix → index → entry → cite.**

This is life-safety content. Danger is encoded structurally (orthogonal facets + mandatory body
blocks per `../SCHEMAS.md`), never left to prose.

---

## How to use this file

1. Pick the domain whose `_index.md` answers your question (table below).
2. Open that domain `_index.md`, read its synthesis + load order, and read its **manifest table**
   (you can filter on the danger facets without opening any entry).
3. Open the specific Layer-3 entry in that domain's `entries/`.
4. For **consumption/food** queries, do **not** stop here — universal `05_food` is *technique only*;
   pivot to [`../regional/_index.md`](../regional/_index.md) → the active biome's `food_hub.md`.

---

## Domain manifest

| # | Domain index | Primary type | Planned entries | One-line synthesis |
|---|--------------|--------------|----------------:|--------------------|
| 01 | [`01_core_principles/_index.md`](01_core_principles/_index.md) | PRINCIPLE | 3 | The decision doctrine — rule of threes, the STOP priority order, and the will-to-live that governs everything below. |
| 02 | [`02_water/_index.md`](02_water/_index.md) | METHOD | 5 | Make water drinkable; every method carries the ⚠CONTAMINATION boundary (boil time, micron limit, chemical-vs-biological). |
| 03 | [`03_fire/_index.md`](03_fire/_index.md) | METHOD | 3 | Get and keep fire — structure, ignition, and the tinder→fuel progression that keeps it alive. |
| 04 | [`04_shelter/_index.md`](04_shelter/_index.md) | METHOD | 3 | Hold core temperature — site selection and hazards, ground/insulation barrier, and shelter types. |
| 05 | [`05_food/_index.md`](05_food/_index.md) | METHOD (technique) | 3 | Calorie acquisition **technique** only (passive fishing, trapping, processing). Consumption/ID resolves through `../regional/_index.md` → `food_hub.md`. |
| 06 | [`06_first_aid/_index.md`](06_first_aid/_index.md) | PROTOCOL | 5 | Field response when EMS is gone — each protocol leads with RECOGNIZE → ⚠RED FLAGS/EVAC and a ⚠DO NOT. Not medical advice. |
| 07 | [`07_navigation/_index.md`](07_navigation/_index.md) | METHOD | 3 | Find direction without GPS — celestial, terrain/map reading, dead reckoning. |
| 08 | [`08_communication/_index.md`](08_communication/_index.md) | METHOD | 3 | Be found and stay informed — visual/audible signaling, radio bands, mesh/emergency comms. |
| 09 | [`09_urban_survival/_index.md`](09_urban_survival/_index.md) | METHOD / PROTOCOL | 3 | Bug-in survival — power-outage, civil-disruption safety, and sanitation/human-waste disease control. |
| 10 | [`10_key_resources/_index.md`](10_key_resources/_index.md) | mixed | 3 | The backup layers — physical books, public-domain ID image sources, and skills to drill now. Links the existing [`../10_key_resources.md`](../10_key_resources.md). |
| 11 | [`11_gear/_index.md`](11_gear/_index.md) | KIT-GEAR | 3 | The 3-tier kit — EDC (tier 1), bug-out (tier 2), home stockpile (tier 3); multi-use discipline. |

**Total planned universal entries: 37** (sum of the count column above). Regional biology is counted
separately — **23 planned** in [`../regional/_index.md`](../regional/_index.md) (edible-plants 5,
mushrooms 5, game-animals 5, crops 5, hazards 3). **Grand total planned across the repo: 60.**

---

## `check_manifests` (master level)

- [ ] Every domain folder listed above exists and contains an `_index.md` + an `entries/` dir.
- [ ] Each domain `_index.md` carries its own manifest table with the SCHEMAS.md §"Manifest row
      contract" columns, and its own `check_manifests` checklist.
- [ ] The planned-entry counts in the table above match the number of rows in each domain manifest.
- [ ] No domain has stray entry files without a manifest row (none yet — Phase 2 writes zero entries).
- [ ] `grep -rn "danger_class" .` returns nothing; no `safe` token on biology facets.

---

## Note on entries

Phase 2 (scaffolding) writes **zero entry files**. Every `entries/` dir is intentionally empty (it
holds a `.gitkeep`). The manifest rows below each domain `_index.md` are **planned** rows
(`review_status: planned`, `source_count: 0`) that later phases fill in. No row here implies an
existing file yet.

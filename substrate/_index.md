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

| # | Domain index | Primary type | Entries | One-line synthesis |
|---|--------------|--------------|----------------:|--------------------|
| 01 | [`01_core_principles/_index.md`](01_core_principles/_index.md) | PRINCIPLE | 5 | The decision doctrine — the rule of threes as a teaching tool (injury first), STOP as a pause before you act, managing fear and stress, the stay-or-go decision, and group roles. |
| 02 | [`02_water/_index.md`](02_water/_index.md) | METHOD | 8 | Make water drinkable; every method carries the ⚠CONTAMINATION boundary (boil time, micron limit, chemical-vs-biological). Clear cloudy water first (settling and pre-filtering), treat with boiling, filters, chemicals, UV or SODIS, and do not treat floodwater or chemical spills at all. |
| 03 | [`03_fire/_index.md`](03_fire/_index.md) | METHOD | 6 | Get and keep fire outside — structure, ignition, the tinder→fuel progression, fire in wet weather, keeping it overnight, and putting it out. Nothing burns inside a tent, vehicle, garage, snow shelter or home. |
| 04 | [`04_shelter/_index.md`](04_shelter/_index.md) | METHOD | 6 | Hold core temperature — site selection and hazards, ground/insulation barrier, shelter types, tarp pitches, a cold-weather sleep system, and a stranded vehicle (carbon monoxide). |
| 05 | [`05_food/_index.md`](05_food/_index.md) | METHOD (technique) | 6 | Food **technique** only (calorie planning and rationing, cooking without power, passive fishing, trapping, processing to temperature, tested home drying). Consumption/ID resolves through `../regional/_index.md` → `food_hub.md`. |
| 06 | [`06_first_aid/_index.md`](06_first_aid/_index.md) | PROTOCOL | 10 | Field response when EMS is gone — each protocol leads with RECOGNIZE → ⚠RED FLAGS/EVAC and a ⚠DO NOT. Bleeding and shock, anaphylaxis, carbon monoxide, head injury, burns, fractures, thermal injury, dehydration, wound infection, medication continuity. Not medical advice. |
| 07 | [`07_navigation/_index.md`](07_navigation/_index.md) | METHOD | 5 | Find direction without GPS — celestial (rough direction), terrain/map reading, compass and declination, dead reckoning, and when not to cross a river. |
| 08 | [`08_communication/_index.md`](08_communication/_index.md) | METHOD | 5 | Be found and stay informed — visual/audible signaling, radio services, emergency alerts and NOAA Weather Radio, a family communication plan, and mesh as an optional extra. |
| 09 | [`09_urban_survival/_index.md`](09_urban_survival/_index.md) | METHOD / PROTOCOL | 7 | Bug-in survival — power outage, generator and heater carbon monoxide prevention, food safety, extreme heat and winter storm at home, civil-disruption safety, and sanitation. |
| 10 | [`10_key_resources/_index.md`](10_key_resources/_index.md) | mixed | 4 | The backup layers — physical books, official emergency information sources, public-domain ID image sources, and skills to drill now. Links the existing [`../10_key_resources.md`](../10_key_resources.md). |
| 11 | [`11_gear/_index.md`](11_gear/_index.md) | KIT-GEAR | 5 | Kit tiers — EDC (tier 1), bug-out (tier 2), home stockpile (tier 3), plus a vehicle kit and an individual first-aid kit; the survey guide groups them as carry daily, grab-and-go, car and home supply. |

**Total universal entries: 67**, all written as files in each domain's `entries/` folder (sum of the count
column above). Regional biology is counted separately: 34 entries are written in
[`../regional/mid-atlantic-appalachian/`](../regional/_index.md) (edible-plants 8, mushrooms 8,
game-animals 5, crops 7, hazards 6) and 15 in [`../regional/northeast-new-england/`](../regional/_index.md)
(edible-plants 3, mushrooms 3, game-animals 3, crops 3, hazards 3), for 49 regional entries. **Repo total: 116
written entries** (67 universal + 49 regional).

---

## `check_manifests` (master level)

- [ ] Every domain folder listed above exists and contains an `_index.md` + an `entries/` dir.
- [ ] Each domain `_index.md` carries its own manifest table with the SCHEMAS.md §"Manifest row
      contract" columns, and its own `check_manifests` checklist.
- [ ] The entry counts in the table above match the number of rows in each domain manifest.
- [x] No domain has stray entry files without a manifest row.
- [ ] No entry or domain `_index.md` uses `danger_class`; no `safe` token on biology facets.

---

## Note on entries

All 67 universal entries exist as files in each domain's `entries/` folder, and every manifest row maps
to one; no `planned` rows remain. If a `planned` row ever reappears, it has no file yet: do not cite it,
and fall back to the domain's survey guide. When an entry is written, its row changes to the entry's own
status and source count.

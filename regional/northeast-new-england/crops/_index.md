# Northeast / New England: Survival Crops (CROP)

> Cold-hardy, storable crops and one late-winter sugar source for **USDA zones about 4b to 6b** (reference
> point Concord, NH, about 5b/6a). CROP entries (`../../../SCHEMAS.md` §3): zone fit, planting windows
> counted from the last frost, growing, harvest and storage, **seed saving**, and
> `## ⚠ MANDATORY PREPARATION` where any part needs processing to be edible or carries a hazard in the
> work (green potatoes, boiling sap).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Calendar:
> [`../seasonality.md`](../seasonality.md).

---

## Synthesis

In a short-season climate the calendar, not the soil, is the limit. New Hampshire Extension tells gardeners
to find their own last-frost date and treats Memorial Day as a conservative estimate for central New
Hampshire; first fall frost runs from mid-to-late September in northern New Hampshire to early or mid-October
in the central and southern parts, and from early September to late October across Vermont. The three entries
here are chosen for that window.

- **Potato** goes in before the last frost (UNH: 1 to 2 weeks before; UVM: 2 to 4 weeks before; soil 40 to 50
  F depending on the source) and stores for months dark and cool: about 40 F, not below 38 F and not above about 46 F (the sources'
  ranges run 37 to 46 F). Light turns tubers green and raises solanine, which cooking does not remove.
- **Cabbage and kale** are the cold-hardy brassicas: set out about 4 weeks before the last frost, sown again
  in midsummer for fall, and kale keeps growing in frost. Cabbage keeps months in a cold, humid cellar; both
  freeze after a blanch (collards 3 minutes, most greens 2, cabbage 1 1/2).
- **Maple sap and syrup** is not planted. Sap runs on freeze-thaw days in late winter, spoils like milk if
  warm, and has to be boiled down, with three hazards in the work: carbon monoxide and fire (boil outdoors
  only), lead from old galvanized or tin gear, and burns.

Seed saving is where these crops differ. Potatoes are clones and extension advises certified seed. Cabbage
and most kale are biennial and cross within one species (Red Russian kale is a different species, *Brassica napus*), so buying seed is the practical route. Maple needs no
seed, but the trees need protecting: tap only large, healthy trees and limit taps.

## Load order (this domain)

```
Planning what to grow?  → pick from the manifest by storability and days to the first fall frost
Planting now?           → the crop entry's "Planting Windows (Zones 4b-6b)" (potato, cabbage and kale go in BEFORE the last frost)
Green, bitter or sprouted potatoes?  → entries/potato-short-season.md ⚠ MANDATORY PREPARATION FIRST (cooking does not remove solanine; throw out heavily green or bitter tubers)
Boiling maple sap?      → entries/maple-sap-and-syrup.md ⚠ MANDATORY PREPARATION FIRST (outdoors only for carbon monoxide; lead-free gear; fire and burns; boil to 7.1 to 7.5 F above the boiling point of water; pack hot)
Freezing or storing greens?  → entries/cabbage-and-kale-cold-hardy.md (blanch times; cellar conditions; no home canning method for cabbage heads)
Putting food by?        → ../../../05_food.md (universal food guide; unknown canned jars go in the trash)
Carbon monoxide?        → ../../../03_fire.md (the carbon monoxide rule)
Calendar context: ../seasonality.md and ../food_hub.md (written by the biome pass).
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| maple-sap-and-syrup | entries/maple-sap-and-syrup.md | CROP | northeast-new-england | tap on freeze-thaw days, mid-Feb to late Apr depending on latitude and elevation; stop when buds break | edible-when-prepared | high | low | false | T1 | 11 | agent-verified |
| potato-short-season | entries/potato-short-season.md | CROP | northeast-new-england | plant 1-4 weeks before last frost (soil 40-50 F), dig storage potatoes about mid-Sep | edible-when-prepared | low | none | false | T1 | 13 | agent-verified |
| cabbage-and-kale-cold-hardy | entries/cabbage-and-kale-cold-hardy.md | CROP | northeast-new-england | set out about 4 weeks before last frost; fall kale sown midsummer; harvest into hard frost | edible-raw | none | none | false | T1 | 15 | agent-verified |

`maple-sap-and-syrup` is `hazard_severity: high` + `preparation_required: true`. The hazard is in the work,
not the tree: carbon monoxide from boiling with wood, propane or charcoal in a closed space (CDC; boil
outdoors only, matching the carbon monoxide rule in `03_fire.md`), fire and burns, and lead from galvanized
buckets, old tin spouts or lead-soldered pans (UMaine, UNH, and a Vermont-hosted good-practice guide).
`confusability_level: low`: only maples are tapped, and the entry tells the reader to tap only trees they
have positively identified (UMaine notes ash and horse chestnut also have opposite buds). `legal_status:
regulated`: tap only trees you own or have permission to tap (Vermont licenses sugaring on state forestland);
open fires may need a permit (UNH); selling syrup needs labeling and, in Maine, a processing license.
`potato-short-season` is `hazard_severity: low` + `preparation_required: true` (green tubers, sprouts and
eyes carry solanine and chaconine; cooking does not remove them; trim small green spots, throw out heavily
green or bitter tubers). `cabbage-and-kale-cold-hardy` needs no mandatory preparation; its sources give no
canning method for cabbage heads. Sources are Northeast extension programs (UMaine, UNH, UVM, Cornell
Cooperative Extension, UMass) as T1, with Mid-Atlantic extension and Oregon State for the points the Northeast
pages do not cover (kale spacing and the lower cold-tolerance figures in degrees F, potato glycoalkaloids); cabbage and kale frost tolerance also has a Cornell Cooperative Extension (Warren County) and a UNH source, and one T2 database
(Massey) and one T2 good-practice guide (IMSI) where noted.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each CROP entry carries "Planting Windows (Zones 4b-6b)" + "Seed Saving"; `preparation_required:
      true` crops (potato, maple) carry `## ⚠ MANDATORY PREPARATION`.
- [ ] Frost dates consistent with the biome profile (to be confirmed once `../_index.md` exists; the entries
      cite UNH and UVM frost statements and give no single Concord date).
